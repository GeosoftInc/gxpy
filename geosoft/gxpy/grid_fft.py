"""
Geosoft Fast Fourier Transform processes for 2D gridded data.

:Classes:

    =============== ==============================================================
    `GridFFT`       Grid FFT
    `PowerSpectrum` Descrete transform power spectrum
    =============== ==============================================================

.. seealso:: :class:`geosoft.gxapi.GXIMG`, :class:`geosoft.gxapi.GXIMU`

.. note::

    Regression tests provide usage examples:     
    `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_grid_fft.py>`_
    
"""
import numpy as np

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import grid as gxgrd
from . import grid_utility as gxgrdu
from . import utility as gxu

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class GridFFTException(geosoft.GXRuntimeError):
    """ Exceptions from this module. """
    pass


class GridFFT:
    """
    Descrete Fourier Transform of a grid.

    :param grid: grid file name or a `geosoft.gxpy.Grid` instance.

    .. versionadded:: 9.4
    """

    def __enter__(self):
        return self

    def __exit__(self, _type, _value, _traceback):
        self.__del__()

    def __del__(self):
        if hasattr(self, '_close'):
            self._close()

    def _close(self):
        if hasattr(self, '_open'):
            if self._open:
                gx.pop_resource(self._open)
                self._open = None

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return '<class GridFFT>: {}'.format(self._name)

    def __init__(self, grid):

        if not isinstance(grid, gxgrd.Grid):
            grid = gxgrd.Grid.open(grid)
        self._source_grid = grid
        self._name = self._source_grid.name

        # trend
        trend = gxgrdu.remove_trend(grid)
        tpg = trend.gxpg()

        # expand
        xpg = gxapi.GXPG.create(1, 1, gxapi.GS_FLOAT)
        gxapi.GXPGU.expand(tpg, xpg, 10.0, 1, 0, 0)
        xnx = xpg.n_cols()
        xny = xpg.n_rows()
        x0, y0 = grid.xy_from_index((xnx - grid.nx) / 2., (xny - grid.ny) / 2.)

        # fill
        self._reference_file = gx.gx().temp_file('grd')
        gxapi.GXPGU.ref_file(xpg, self._reference_file)
        gxapi.GXPGU.fill(xpg,
                         2,     # Roll off weighting option: 1 - linear, 2 - square
                         0.0,   # the value to roll off to, GS_R8DM for roll off to mean value line by line.
                         -1,    # roll-off distance in cells, 0 for none, -1 default: 2 times of min. dummy edge dim.
                         0,     # max. filter length. -1 for no max. entropy. 0 for the default.
                         0,     # max. pred. sample 0 for the default of 2*lMxf.
                         0.,    # limit (abs. value) amplitudes to this level, starting at half this value. 0. for none.
                         0.,    # limit edge (abs. value) amplitudes to this level. <0.0 for no edge limit.
                         0,     # edge limit width in cells, 0 for default.
                         1,     # number of time to pass smooth filter
                         self._reference_file)

        # create prepped grid
        properties = grid.properties()
        properties['x0'] = x0
        properties['y0'] = y0
        self._prep_grid = gxgrd.Grid.from_data_array(xpg, properties=properties)
        nx = self._prep_grid.nx
        ny = self._prep_grid.ny

        # fft
        xpg.re_allocate(ny, nx + 2)
        gxapi.GXFFT2.trans_pg(xpg, gxapi.FFT2_PG_FORWARD)
        trn_file = gx.gx().temp_file('.trn(GRD)')
        self._fft_transform = gxgrd.Grid.from_data_array(xpg, file_name=trn_file, properties=properties)

        self._spec_file = None

        # track
        self._open = gx.track_resource(self.__class__.__name__, str(self))

    @property
    def du(self):
        """ Wavenumber increment in the grid X direction in (cycles / grid distance uom)"""
        return 1.0 / (self._fft_transform.dx * (self._fft_transform.nx - 2))

    @property
    def dv(self):
        """ Wavenumber increment in the grid Y direction in (cycles / grid distance uom)."""
        return 1.0 / (self._fft_transform.dy * self._fft_transform.ny)

    @property
    def transform(self):
        """ Descrete Fourier Transform as a `geosoft.gxpy.Grid` instance."""
        return self._fft_transform


class PowerSpectrum:
    """
    Power spectrun of a descrete FFT transform.

    :param fft: `GridFFT` instance
    """

    def __init__(self, fft):

        spec_file = gx.gx().temp_file()
        gxapi.GXFFT2.rad_spc(fft.transform.gximg, spec_file)

        length = max(fft.transform.nx, fft.transform.ny) // 2
        self._spectrum = np.zeros((length, 5))
        self._wavenumber = self._spectrum[:, 0]
        self._n_sample = self._spectrum[:, 1]
        self._log_power = self._spectrum[:, 2]
        self._depth_3 = self._spectrum[:, 3]
        self._depth_5 = self._spectrum[:, 4]

        i = 0
        with open(spec_file) as f:
            for sl in f:
                if sl and sl[0] != '/':
                    pv = sl.split()
                    self._wavenumber[i] = float(pv[0])
                    self._n_sample[i] = float(pv[1])
                    self._log_power[i] = float(pv[2])
                    try:
                        self._depth_3[i] = float(pv[3])
                    except ValueError:
                        self._depth_3[i] = np.nan
                    try:
                        self._depth_5[i] = float(pv[4])
                    except ValueError:
                        self._depth_5[i] = np.nan
                    i += 1

        self._spectrum = self._spectrum[:i]
        gxu.delete_file(spec_file)

    @property
    def wn_samples_power_d3_d5(self):
        """
        Numpy array of radially averaged spectrum, shapes (n_wavenumbers, 5).

        Rows contain [wavenumber, sample_count, log_power, 3-point_depth, 5-point_depth]

        The point depths are an estimate of the source depth assuming the slope is 1 / (4 * pi * depth),
        with the 3-point depth based on on a centered 3-point average, and the 5-point depth based on a centered
        5-point average.

        .. versionadded:: 9.4
        """
        return self._spectrum
