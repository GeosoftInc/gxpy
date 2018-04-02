"""
Geosoft Fast Fourier Transform processes for 2D gridded data.

:Classes:

    =============== ==============================================================
    `GridFFT`       Grid FFT
    `PowerSpectrum` Descrete transform power spectrum
    =============== ==============================================================

.. seealso:: :class:`geosoft.gxapi.GXFFT2`

.. note::

    Regression tests provide usage examples:     
    `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_grid_fft.py>`_
    
"""
import numpy as np
import math

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import grid as gxgrd
from . import utility as gxu
from . import vv as gxvv

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


MAX_DIMENSION = 16384  #:


class GridFFTException(geosoft.GXRuntimeError):
    """ Exceptions from this module. """
    pass


class GridFFT:
    """
    Descrete Fourier Transform of a grid.

    :param grid:        grid file name or a `geosoft.gxpy.grid.Grid` instance.
    :param progress:    call-back to report progress, `progress=print` to prints to the console

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


                self._fft_transform.close(discard=True)
                if self._filtered_transform:
                    self._filtered_transform.close(discard=True)
                self._prep_grid.close(discard=True)
                gxu.delete_files_by_root(self._reference_file)

                self._source_grid = None
                self._trend = None

                gx.pop_resource(self._open)
                self._open = None

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return '<class GridFFT>: {} ({}, {})'.format(self._name, self._source_grid.nx, self._source_grid.ny)

    def __init__(self, grid, progress=None):

        if not isinstance(grid, gxgrd.Grid):
            grid = gxgrd.Grid.open(grid)
        self._source_grid = grid
        self._name = self._source_grid.name
        if progress:
            progress(_t('\nGridFFT from: {}').format(grid.file_name))

        # trend
        if progress:
            progress(_t('Remove trend...'))
        gpg = grid.gxpg()
        tpg = gxapi.GXPG.create(grid.ny, grid.nx, self._source_grid.gxtype)
        self._trend = gxapi.GXTR.create(2)  # order 2
        gxapi.GXPGU.trend(gpg, tpg, self._trend,
                          0,    # 0 - calculate
                          1,    # 1 - edge
                          grid.x0, grid.y0, grid.dx, grid.dy)

        # expand
        if progress:
            progress(_t('Expand from ({}, {})').format(grid.nx, grid.ny))
        xpg = gxapi.GXPG.create(1, 1, tpg.e_type())
        gxapi.GXPGU.expand(tpg, xpg, 10.0, 1, 0, 0)
        xnx = xpg.n_cols()
        xny = xpg.n_rows()
        if xnx > MAX_DIMENSION or xny > MAX_DIMENSION:
            raise GridFFTException(_t('Expanded size ({}, {}) exceeds maximum dimension {{}, {}').
                                   format(xnx, xny, MAX_DIMENSION, MAX_DIMENSION))
        if progress:
            progress(_t('         to ({}, {})...').format(xnx, xny))

        properties = grid.properties()
        properties['x0'], properties['y0'] = grid.xy_from_index(-(xnx - grid.nx) / 2., -(xny - grid.ny) / 2.)

        # fill
        if progress:
            progress(_t('Fill...'))
        self._reference_file = gx.gx().temp_file('grd')
        gxapi.GXPGU.ref_file(xpg, self._reference_file)
        gxapi.GXPGU.fill(xpg,
                         2,     # Roll off weighting option: 1 - linear, 2 - square
                         0.0,   # the value to roll off to, GS_R8DM for roll off to mean value line by line.
                         -1,    # roll-off distance in cells, 0 for none, -1 default: 2 times of min. dummy edge dim.
                         0,     # max. filter length. -1 for no max. entropy. 0 for the default.
                         0,     # max. pred. sample 0 for the default of 2*lMxf.
                         0.,    # limit (abs. value) amplitudes to this level, starting at half this value. 0. for none.
                         -1.,   # limit edge (abs. value) amplitudes to this level. <0.0 for no edge limit.
                         0,     # edge limit width in cells, 0 for default.
                         1,     # number of times to pass smooth filter
                         self._reference_file)

        # prepped grid
        self._prep_grid = gxgrd.Grid.from_data_array(xpg, properties=properties)
        self._prep_grid.gximg.set_tr(self._trend)

        # fft
        if progress:
            progress(_t('FFT...').format(xnx, xny))
        xpg.re_allocate(self._prep_grid.ny, self._prep_grid.nx + 2)
        gxapi.GXFFT2.trans_pg(xpg, gxapi.FFT2_PG_FORWARD)
        trn_file = gx.gx().temp_file('.trn(GRD)')
        self._fft_transform = gxgrd.Grid.from_data_array(xpg, file_name=trn_file, properties=properties)
        self._fft_transform.gximg.set_tr(self._trend)

        self._filtered_transform = None

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
        """ Folded descrete Fourier transform as a `geosoft.gxpy.grid.Grid` instance."""
        return self._fft_transform

    @property
    def filtered_transform(self):
        """ Folded descrete Fourier transform after filters applied."""
        return self._filtered_transform

    def filter_con(self, header=None, filters=None, cumulatative=False):

        if (not cumulatative) or (self._filtered_transform is None):
            transform = self._fft_transform
        else:
            transform = self._filtered_transform
        rpg = transform.gxpg()
        tpg = gxapi.GXPG.create(rpg.n_rows(), rpg.n_cols(), rpg.e_type())
        tpg.copy(rpg)
        transform.gximg.get_tr(self._trend)

        #control file
        con_file = gx.gx().temp_file('con')
        with open(con_file, 'x') as cf:

            # header:
            i = 0
            if header:
                for h in header:
                    cf.write('{} /\n'.format(h))
                    i += 1
                    if i == 5:
                        break
            for n in range(i, 5):
                cf.write('/\n')

            # filters
            if filters:
                for f in filters:
                    cf.write('{} /\n'.format(f))

        # filter
        gxapi.GXFFT2.filter_pg(tpg, con_file, self._trend,
                               self._source_grid.dx, self._source_grid.dy, self._source_grid.rot)

        file_name = gx.gx().temp_file('.trn(GRD)')
        self._filtered_transform = gxgrd.Grid.from_data_array(tpg, file_name=file_name,
                                                              properties=self._fft_transform.properties())
        self._filtered_transform.gximg.set_tr(self._trend)

        gxu.delete_file(con_file)

    def result_grid(self, file_name=None, overwrite=False):
        """
        Produce a filter result grid.

        :param file_name:   result grid file, default greates a temporary grid
        :param overwrite:   `True` to overwrite an existing grid
        :return:            `geosoft.gxpy.grid.Grid` instance

        .. versionadded:: 9.4
        """

        if self._filtered_transform is None:
            trn = self._fft_transform
        else:
            trn = self._filtered_transform
        fpg = trn.gxpg()
        tpg = gxapi.GXPG.create(fpg.n_rows(), fpg.n_cols(), fpg.e_type())
        tpg.copy(fpg)

        # fft result
        gxapi.GXFFT2.trans_pg(tpg, gxapi.FFT2_PG_INVERSE)

        # mask and reduce
        gxapi.GXPGU.bool_mask(tpg, self._reference_file)
        ix0 = ((tpg.n_cols() - 2) - self._source_grid.nx) // 2
        iy0 = (tpg.n_rows() - self._source_grid.ny) // 2
        rpg = gxapi.GXPG.create(self._source_grid.ny, self._source_grid.nx, self._source_grid.gxtype)
        rpg.copy_subset(tpg, 0, 0, iy0, ix0, self._source_grid.ny, self._source_grid.nx)

        # put back the trend, which may have been filtered
        gxapi.GXIMG.get_tr(trn.gximg, self._trend)
        result_pg = gxapi.GXPG.create(rpg.n_rows(), rpg.n_cols(), rpg.e_type())
        gxapi.GXPGU.trend(rpg, result_pg, self._trend, 2, 1,
                          self._source_grid.x0, self._source_grid.y0,
                          self._source_grid.dx, self._source_grid.dy)

        return gxgrd.Grid.from_data_array(result_pg, properties=self._source_grid.properties(),
                                          file_name=file_name, overwrite=overwrite)


class PowerSpectrum:
    """
    Power spectrum of an FFT transform.

    :param transform: `GridFFT.transform` or `GridFFT.filtered_transform`.

    .. versionadded:: 9.4
    """

    def __init__(self, transform):
        self._transform = transform
        self._spectrum = None


    @property
    def radially_averaged_spectrum(self):
        """
        Radially averaged spectrum as a Numpy array shaped (n_wavenumbers, 5).

        Numpy array shaped (n_wavenumbers, 5), where each row contains:
        [wavenumber, sample_count, log_power, 3-point_depth, 5-point_depth], wavenumber in cycles per
        1000 * distance unit of measure (cycle/km for metres), and log_power is the natural log of
        the power. The point depths are an estimate of the source depth assuming the slope
        is 1 / (4 * pi * depth),  with the 3-point depth based on on a centered 3-point average,
        and the 5-point depth based on a centered 5-point average.

        .. versionadded:: 9.4
        """

        if self._spectrum is None:

            spec_file = gx.gx().temp_file()
            try:
                gxapi.GXFFT2.rad_spc(self._transform.gximg, spec_file)
            except geosoft.gxapi.GXAPIError:
                tpg = gxapi.GXPG.create(self._transform.ny, self._transform.nx, gxapi.GS_FLOAT)
                tpg.copy(self._transform.gxpg())
                with gxgrd.Grid.from_data_array(tpg, properties=self._transform.properties()) as tgd:
                    tgd.delete_files()
                    gxapi.GXFFT2.rad_spc(tgd.gximg, spec_file)
                tpg = None

            length = max(self._transform.nx, self._transform.ny) // 2
            self._spectrum = np.zeros((length, 5))
            wavenumber = self._spectrum[:, 0]
            n_sample = self._spectrum[:, 1]
            log_power = self._spectrum[:, 2]
            depth_3 = self._spectrum[:, 3]
            depth_5 = self._spectrum[:, 4]
            self._asd = None

            i = 0
            with open(spec_file) as f:
                for sl in f:
                    if sl:
                        if sl[0] == '/':
                            if '=' in sl:
                                try:
                                    self._asd = float(sl.split('=')[1])
                                except ValueError:
                                    self._asd = None
                        else:
                            pv = sl.split()
                            wavenumber[i] = float(pv[0])
                            n_sample[i] = float(pv[1])
                            log_power[i] = float(pv[2])
                            try:
                                depth_3[i] = float(pv[3])
                            except ValueError:
                                depth_3[i] = np.nan
                            try:
                                depth_5[i] = float(pv[4])
                            except ValueError:
                                depth_5[i] = np.nan
                            i += 1
            self._spectrum = self._spectrum[:i]
            gxu.delete_file(spec_file)

            # get power as a vv for full resolution
            pvv = gxvv.GXvv()
            gxapi.GXFFT2.rad_spc1(self._transform.gximg, pvv.gxvv)
            log_power[:] = np.log(pvv.np[:]) - self.log_average_spectral_density

        return self._spectrum

    @property
    def wavenumber(self):
        """
        Wavenumbers as an array.

        .. versionadded:: 9.4
        """
        return self.radially_averaged_spectrum[:, 0]

    @property
    def log_power(self):
        """
        Log power average as an array.

        .. versionadded:: 9.4
        """
        return self.radially_averaged_spectrum[:, 2]

    @property
    def samples(self):
        """
        Samples per wavenumber as an array.

        .. versionadded:: 9.4
        """
        return self.radially_averaged_spectrum[:, 1]

    @property
    def depth_3(self):
        """
        Depth estimate as a function of wavenumber averaged over 3 wavenumbers.

        Depth estimate based on slope of the spectrum 1 / (4 * pi * depth), using method
        of Spector and Grant (1970).

        .. versionadded:: 9.4
        """
        return self.radially_averaged_spectrum[:, 3]

    @property
    def depth_5(self):
        """
        Depth estimate as a function of wavenumber averaged over 5 wavenumbers.

        Depth estimate based on slope of the spectrum 1 / (4 * pi * depth), using method
        of Spector and Grant (1970).

        .. versionadded:: 9.4
        """
        return self.radially_averaged_spectrum[:, 4]

    @property
    def log_average_spectral_density(self):
        """
        Log of the average spectral density of the transform.

        .. versionadded:: 9.4
        """

        if self._asd is None:
            tot_samples = np.sum(self.samples)
            tot_energy = np.sum(np.exp(self.log_power))
            self._asd = math.log(tot_energy / tot_samples)
        return self._asd
