"""
Geosoft Fast Fourier Transform processes for 2D gridded data.

:Classes:

    =============== ==============================================================
    `GridFFT`       Grid FFT
    `PowerSpectrum` Descrete transform power spectrum
    =============== ==============================================================

Note that 'wavenumber' in this module refers to cycles/unit_distance. Multiply by 2pi to
determine the angular wavenumber.

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


FILL_MAXIMUM_ENTROPY = 0    #:
FILL_MINIMUM_CURVATURE = 1  #:

SOURCE = 0    #:
FILTERED = 1  #:
WAVENUMBER = 0      #: index in radial spectrum
SAMPLE_COUNT = 1    #: index in radial spectrum
LOG_POWER = 2       #: index in radial spectrum
DEPTH_3 = 3         #: index in radial spectrum
DEPTH_5 = 4         #: index in radial spectrum


class GridFFTException(geosoft.GXRuntimeError):
    """ Exceptions from this module. """
    pass


class GridFFT:
    """
    Descrete Fourier Transform of a grid.

    :param grid:            grid file name or a `geosoft.gxpy.grid.Grid` instance.
    :param buffer:          percentage buffer area, default 2%.  The buffer expands the size of the grid
                            footprint before filling internal space with a minimum-curvacture surface.  This
                            minimizes edge effects from high-amplitude features at the edge of the grid.
    :param buffer_iterations: maximum iterations to resolve the minimum curvature surface for the internal fill.
    :param expand:          minimum expansion percent to create a periodic function. The default is 10.
    :param trend_order:     trend order to remove, default is 1
    :param roll_to_zero:    `True` to roll-off to zero in expanded area
    :param roll_off_method: 1 - linear, 2 - square (default)
    :param fill_method:     FILL_MAXIMUM_ENTROPY (default) or FILL_MINIMUM_CURVATURE
    :param max_entropy_filter_length: maximum entropy filter length,
    :param amplitude_limit:         Amplitudes limiting, which starts at halve this setting.  Default no limiting.
    :param edge_amplitude_limit:    edge amplitude limiting, starting at half this value. Default no limiting.
    :param edge_limit_cells:        if edge limiting, start this many cells from the edge
    :param smooth:                  `True` (default) to smooth the filled expanded area.


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

                self._source_transform.close(discard=True)
                if self._filtered_transform:
                    self._filtered_transform.close(discard=True)
                self._prep_grid.close(discard=True)

                self._source_grid = None
                self._trend = None

                gx.pop_resource(self._open)
                self._open = None

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return '<class GridFFT>: {} ({}, {})'.format(self._name, self._source_grid.nx, self._source_grid.ny)

    def __init__(self, grid,
                 buffer=2.,
                 buffer_iterations=250,
                 buffer_tolerance=None,
                 trend_order=1,
                 trend_edge=1,
                 expand=10.,
                 roll_to_zero=False,
                 roll_off_method=2,
                 fill_method=FILL_MAXIMUM_ENTROPY,
                 max_entropy_filter_length=0,
                 amplitude_limit=0.,
                 edge_amplitude_limit=-1.,
                 edge_limit_cells=0,
                 smooth=1):

        def tpg_rows(n):
            if n >= grid.ny:
                return None
            tpg.read_row(n, 0, 0, rvv.gxvv)
            xyv[:, 1] = grid.y0 + n * grid.dy
            xyv[:, 2] = rvv.np
            return xyv

        def max_entropy_fill(btol, rtz, melen):

            # expand buffer and fill
            if buffer == 0.:
                buffer_cells = 0
            else:
                buffer_cells = max(int(0.5 + min(grid.nx, grid.ny) * buffer / 100.), 1)
            gxc.log(_t('Internal fill with {} cell buffer...').format(buffer_cells))
            expanded_area = (grid.x0 - buffer_cells * grid.dx,
                             grid.y0 - buffer_cells * grid.dy,
                             grid.x0 + (grid.nx + buffer_cells - 1) * grid.dx,
                             grid.y0 + (grid.ny + buffer_cells - 1) * grid.dy)
            rvv.length = grid.nx
            xyv[:, 0] = [(grid.x0 + i * grid.dx) for i in range(grid.nx)]
            bkd = max(grid.nx, grid.ny) * grid.dx
            if btol is None:
                btol = grid.statistics()['sd'] * 0.001
            buffer_grid = gxgrd.Grid.minimum_curvature(tpg_rows,
                                                       cs=grid.dx,
                                                       area=expanded_area,
                                                       bkd=bkd,
                                                       itrmax=buffer_iterations,
                                                       pastol=99.,
                                                       tol=btol,
                                                       icgr=16,
                                                       max_segments=grid.ny)

            # expand for periodic function
            gxc.log(_t('Expand from ({}, {})').format(grid.nx, grid.ny))
            ppg = gxapi.GXPG.create(1, 1, tpg.e_type())
            gxapi.GXPGU.expand(buffer_grid.gxpg(), ppg, expand, 1, 0, 0)

            xnx = ppg.n_cols()
            xny = ppg.n_rows()
            gxc.log(_t('         to ({}, {})...').format(xnx, xny))

            # fill
            gxc.log(_t('Maximum-entropy prediction fill...'))
            if rtz:
                rtz = 0.0
                roll_distance = min(xnx - self._source_grid.nx,
                                    xny - self._source_grid.ny) // 2
            else:
                rtz = gxapi.rDUMMY
                roll_distance = 0

            reference_file = gx.gx().temp_file('grd')
            gxapi.GXPGU.ref_file(ppg, reference_file)
            gxapi.GXPGU.fill(ppg,
                             roll_off_method,       # Roll off weighting option: 1 - linear, 2 - square
                             rtz,                   # the value to roll off to, GS_R8DM for line mean
                             roll_distance,         # roll-off distance in cells, 0 for none, -1 default
                             melen,                 # max. filter length. -1 for no max. entropy. 0 for the default.
                             0,                     # max. pred. sample 0 for the default of 2*lMxf.
                             amplitude_limit,       # limit amplitudes to this level, starting at half, 0. for none
                             edge_amplitude_limit,  # limit edge amplitudes to this level. <0.0 for no none
                             edge_limit_cells,      # edge limit width in cells, 0 for default.
                             int(bool(smooth)),     # pass smooth filter, 0 or 1.
                             reference_file)
            gxu.delete_files_by_root(reference_file)

            # prepped grid
            properties = grid.properties()
            properties['x0'], properties['y0'] = grid.xy_from_index((grid.nx - ppg.n_cols()) / 2.,
                                                                    (grid.ny - ppg.n_rows()) / 2.)
            prep_grid = gxgrd.Grid.from_data_array(ppg, properties=properties)

            return prep_grid, ppg

        def min_curve_fill(btol):

            # expand for periodic function
            gxc.log(_t('Expand from ({}, {})').format(grid.nx, grid.ny))
            ppg = gxapi.GXPG.create(1, 1, tpg.e_type())
            gxapi.GXPGU.expand(grid.gxpg(), ppg, expand, 1, 0, 0)
            gxc.log(_t('         to ({}, {})...').format(ppg.n_cols(), ppg.n_rows()))

            # expand buffer and fill
            gxc.log(_t('Minimum-curvature surface fill...'))

            x0, y0 = grid.xy_from_index(-(ppg.n_cols() - grid.nx) / 2,
                                        -(ppg.n_rows() - grid.ny) / 2)
            xx, yy = grid.xy_from_index((ppg.n_cols() + grid.nx) / 2 - 1,
                                        (ppg.n_rows() + grid.ny) / 2 - 1)
            expanded_area = (x0, y0, xx, yy)
            rvv.length = grid.nx
            xyv[:, 0] = [(grid.x0 + i * grid.dx) for i in range(grid.nx)]
            bkd = max(ppg.n_cols() * grid.dx, ppg.n_rows() * grid.dy)
            if btol is None:
                btol = grid.statistics()['sd'] * 0.001
            filled_grid = gxgrd.Grid.minimum_curvature(tpg_rows,
                                                       cs=grid.dx,
                                                       area=expanded_area,
                                                       bkd=bkd,
                                                       itrmax=buffer_iterations,
                                                       pastol=99.,
                                                       tol=btol,
                                                       icgr=16,
                                                       max_segments=grid.ny)
            ppg = gxapi.GXPG.create(filled_grid.ny, filled_grid.nx, filled_grid.gxtype)
            ppg.copy(filled_grid.gxpg())
            ppg.re_allocate(filled_grid.ny, filled_grid.nx + 2)
            gxc.log(_t('Expanded grid ({}, {})...').format(filled_grid.nx, filled_grid.ny))

            # TODO: add a cosine roll-off taper to the expanded edges

            return filled_grid, ppg

        # lets do this...

        gxc = gx.gx()  # for logging

        if not isinstance(grid, gxgrd.Grid):
            grid = gxgrd.Grid.open(grid)
        self._source_grid = grid
        self._name = self._source_grid.name

        if grid.rot != 0.:
            # TODO: add support for rotated grids
            raise(_t('Rotated grids are not supported.'))
        if grid.dx != grid.dy:
            raise(_t('Cell size must be square'))

        gxc.log(_t('\nGridFFT from: {}').format(grid.file_name))

        # trend
        method = _t('edge') if trend_edge == 1 else _t('all')
        gxc.log(_t('Remove {} order trend determined from {} data ...').format(trend_order, method))
        self._trend = gxapi.GXTR.create(trend_order)
        tpg = gxapi.GXPG.create(grid.ny, grid.nx, self._source_grid.gxtype)
        gxapi.GXPGU.trend(grid.gxpg(), tpg, self._trend, 0,
                          trend_edge,
                          grid.x0, grid.y0,
                          grid.dx, grid.dy)

        xyv = np.empty((grid.nx, 3))
        rvv = gxvv.GXvv()
        if fill_method == FILL_MAXIMUM_ENTROPY:
            self._prep_grid, fpg = max_entropy_fill(buffer_tolerance, roll_to_zero, max_entropy_filter_length)
        else:
            self._prep_grid, fpg = min_curve_fill(buffer_tolerance)

        self._prep_grid.gximg.set_tr(self._trend)

        # fft
        gxc.log(_t('FFT...'))
        fpg.re_allocate(self._prep_grid.ny, self._prep_grid.nx + 2)
        gxapi.GXFFT2.trans_pg(fpg, gxapi.FFT2_PG_FORWARD)
        trn_file = gx.gx().temp_file('.trn(GRD)')
        self._source_transform = gxgrd.Grid.from_data_array(fpg, file_name=trn_file,
                                                            properties=self._prep_grid.properties())
        self._source_transform.gximg.set_tr(self._trend)

        self._filtered_transform = None
        self._next = 0
        self._ny2 = self._source_transform.ny // 2
        self._u = None
        self._u2 = None
        self._source_spectrum = None
        self._filtered_spectrum = None
        self._source_average_spectral_density = None
        self._filtered_average_spectral_density = None

        # track
        self._open = gx.track_resource(self.__class__.__name__, str(self))

    def uv_row_from_tr(self, i):
        """ 
        Returns (u, v) space row index of a transform row.

        .. versionadded:: 9.4
        """
        return (i + self._ny2) if i < self._ny2 else (i - self._ny2)

    def tr_row_from_uv(self, i):
        """
        Returns transform row index from (u, v) space row index.

        .. versionadded:: 9.4
        """
        return (i - self._ny2) if i >= self._ny2 else (i + self._ny2)

    def read_uv_row(self, row, trn=SOURCE):
        """
        Read a row (constant wavenumber v) from (u, v) transform.

        :param row:     row number in (u, v) space, row 0 is minimum v
        :param trn:     `SOURCE` from the source transform (default) or `FILTERED`
        :return:        (u_array, v, real_array, imaginary_array)

        To calculate a wavenumber array: wavenumber = np.sqrt(u_array**2 + v**2).

        Upward continuation example:

        .. code::

            import geosoft.gxpy.gx as gx
            import geosoft.gxpy.grid_fft as gfft

            gxc = gx.GXpy(log=print)

            with gxfft.GridFFT('some_mag_grid_file.grd') as fft:

                # for each row v in (u, v)
                for vrow in range(fft.nv):

                    # read the row
                    u, v, r, i = fft.read_uv_row(vrow)

                    # wavenumber along the row
                    wn = np.sqrt(u**2 + v**2)

                    # upward continue 500 grid distance units
                    continuation_filter = np.exp(-2. * math.pi * 500. * wn)
                    r *= continuation_filter
                    i *= continuation_filter

                    # write the filtered result to the FILTERED transform
                    fft.write_uv_row(r, i, vrow, trn=gxfft.FILTERED)

                # create an output grid of the upward-continued result
                fft.result_grid(file_name='upward_continued_500.grd')

        .. seealso:: `write_uv_row()`

        .. versionadded:: 9.4
        """

        if trn == SOURCE:
            tr = self.source_transform
        else:
            tr = self.filtered_transform
        data = tr.read_row(self.tr_row_from_uv(row)).np
        r = data[0::2]
        i = data[1::2]
        if self._u is None:
            self._u = np.arange(len(r)) * self.dv
            self._u2 = self._u**2
        v = (row - self._ny2) * self.dv
        return self._u, v, r, i

    def write_uv_row(self, r, i, row, trn=SOURCE):
        """
        Write a row (constant wavenumber v) to the (u, v) transform.

        :param r:       reals as a numpy array length half the width of the transform (as returned from `read_row`).
        :param i:       imaginary as a numpy array, matches r.
        :param row:     row number in (u, v) space, row 0 is minimum v
        :param trn:     `SOURCE` from the source transform (default) or `FILTERED`

        .. seealso:: `read_uv_row()`

        .. versionadded:: 9.4
        """

        if trn == SOURCE:
            tr = self.source_transform
        else:
            tr = self.filtered_transform
        data = np.empty(len(r) * 2, dtype=tr.dtype)
        data[0::2] = r
        data[1::2] = i
        tr.write_row(data, self.tr_row_from_uv(row))
        if row == tr.ny - 1:
            if trn == SOURCE:
                self._source_transform = gxgrd.reopen(tr)
            else:
                self._filtered_transform = gxgrd.reopen(tr)

    @property
    def du(self):
        """ Wavenumber increment in the grid X direction in (cycles / grid distance uom)"""
        return 1.0 / (self._source_transform.dx * (self._source_transform.nx - 2))

    @property
    def dv(self):
        """ Wavenumber increment in the grid Y direction in (cycles / grid distance uom)."""
        return 1.0 / (self._source_transform.dy * self._source_transform.ny)

    @property
    def nu(self):
        """
        Number of discrete wavenumbers in grid X direction.

        The transform is folded in the x direction, will be half the transform width + 1
        """
        return self._source_transform.nx // 2

    @property
    def nv(self):
        """
        Number of discrete wavenumbers in the grid Y direction.
        """
        return self._source_transform.ny

    @property
    def u0(self):
        """ First u (X-direction) wavenumber, always 0. """
        return 0.

    @property
    def v0(self):
        """ First v (Y-direction) wavenumber. """
        return (self.nv // 2) * self.dv

    def filter(self, filters=None,
               trn=SOURCE,
               height='',
               mag_inclination='',
               mag_declination='',
               mag_strength=''):
        """
        Apply a pre-defined filter.

        See filter reference: https://github.com/GeosoftInc/gxc/blob/master/reference/con_files/magmap.con
        
        :param filters:         list of filters to apply.  Each filter can be a string, or a tuple with the first
                                item being the filter name followed by the filter parameters. See `magmap.con`
                                referenced above for the full list of filters.
        :param trn:             `SOURCE` apply to the source transform (default) or `FILTERED` to apply to the current
                                filtered state.

        The following parameter are the default for magnetic filed filters like pole/equator reduction and
        aparent susceptibility.

        :param height:          survey ground clearance in grid distance units
        :param mag_inclination: magnetic field inclination
        :param mag_declination: magnetic field declination
        :param mag_strength:    total magnetic filed strength for converting magnetization to susceptibility.

        Example upward continuation 500 grid distance units and a first vertical derivative:

        .. code::

            import geosoft.gxpy.gx as gx
            import geosoft.gxpy.grid_fft as gfft

            gxc = gx.GXpy(log=print)

            with gxfft.GridFFT('some_mag_grid_file.grd') as fft:

                # apply the filer
                fft.filter(['CNUP 500', 'DRVZ 1'])  # equlavalent to `fft.filter([('CNUP', 500), ('DRVZ', 1)])`

                # create an output grid of the upward-continued result
                fft.result_grid(file_name='upward_continued_500.grd')

        .. versionadded:: 9.4
        """

        if (trn == SOURCE) or (self._filtered_transform is None):
            transform = self._source_transform
        else:
            transform = self._filtered_transform
        rpg = transform.gxpg()
        tpg = gxapi.GXPG.create(rpg.n_rows(), rpg.n_cols(), rpg.e_type())
        tpg.copy(rpg)
        transform.gximg.get_tr(self._trend)

        # control file
        con_file = gx.gx().temp_file('con')
        with open(con_file, 'x') as cf:

            # control-file header parameters:
            cf.write('\n')      # title not used
            cf.write('{} /\n'.format(height))
            cf.write('{} /\n'.format(mag_inclination))
            cf.write('{} /\n'.format(mag_declination))
            cf.write('{} /\n'.format(mag_strength))

            if isinstance(filters, str):
                filters = [filters]

            # filters
            if filters:
                for f in filters:
                    if isinstance(f, str):
                        cf.write('{} /\n'.format(f))
                    else:
                        for p in f:
                            cf.write('{} '.format(p))
                        cf.write('/\n')

        # filter
        gxapi.GXFFT2.filter_pg(tpg, con_file, self._trend,
                               self._source_grid.dx, self._source_grid.dy, self._source_grid.rot)
        gxu.delete_file(con_file)

        file_name = gx.gx().temp_file('.trn(GRD)')
        self._filtered_transform = gxgrd.Grid.from_data_array(tpg, file_name=file_name,
                                                              properties=self._source_transform.properties())
        self._filtered_transform.gximg.set_tr(self._trend)
        self._filtered_average_spectral_density = None
        self._filtered_spectrum = None

    def radially_averaged_spectrum(self, trn=SOURCE):
        """
        Radially averaged spectrum as a Numpy array shaped (n_wavenumbers, 5).

        Numpy array shaped (n_wavenumbers, 5), where each row contains:
        [wavenumber, sample_count, log_power, 3-point_depth, 5-point_depth], wavenumber in cycles per
        1000 * distance unit of measure (cycle/km for metres), and log_power is the natural log of
        the power.

        Point depths are calculated by dividing the local slope(3 points and 5 points) of the log_power by (4 * pi)
        (see Spector and Grant, 1970).

        :param trn:     `SOURCE` (default) return spectrum of the source data, or `FILTERED` return spectrum
                        of the current filtered state.

        .. versionadded:: 9.4
        """
        
        if trn == SOURCE:
            if self._source_spectrum is not None:
                return self._source_spectrum
            tr = self.source_transform
        else:
            if self._filtered_spectrum is not None:
                return self._filtered_spectrum
            tr = self.filtered_transform

        # spectrum            
        spec_file = gx.gx().temp_file()
        try:
            gxapi.GXFFT2.rad_spc(tr.gximg, spec_file)
        except geosoft.gxapi.GXAPIError:
            tpg = gxapi.GXPG.create(tr.ny, tr.nx, gxapi.GS_FLOAT)
            tpg.copy(tr.gxpg())
            with gxgrd.Grid.from_data_array(tpg, properties=tr.properties()) as tgd:
                tgd.delete_files()
                gxapi.GXFFT2.rad_spc(tgd.gximg, spec_file)

        length = max(tr.nx, tr.ny) // 2
        spectrum = np.zeros((length, 5))
        wavenumber = spectrum[:, 0]
        n_sample = spectrum[:, 1]
        log_power = spectrum[:, 2]
        depth_3 = spectrum[:, 3]
        depth_5 = spectrum[:, 4]

        i = 0
        asd = None
        with open(spec_file) as f:
            for sl in f:
                if sl:
                    if sl[0] == '/':
                        if '=' in sl:
                            try:
                                asd = float(sl.split('=')[1])
                            except ValueError:
                                asd = None
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
        spectrum = spectrum[:i]
        gxu.delete_file(spec_file)

        # add the average spectral density back into the log_power
        spectrum[:, LOG_POWER] += asd

        if trn == SOURCE:
            self._source_spectrum = spectrum
            self._source_average_spectral_density = asd
        else:
            self._filtered_spectrum = spectrum
            self._filtered_average_spectral_density = asd

        return spectrum

    def log_average_spectral_density(self, trn=SOURCE):
        """
        Log of the average spectral density of the transform.
        
        :param trn:  `SOURCE` (default) source data spectrum, or `FILTERED` current filtered transform.

        .. versionadded:: 9.4
        """

        if trn == SOURCE:
            if self._source_average_spectral_density:
                return self._source_average_spectral_density
        else:
            if self._filtered_average_spectral_density:
                return self._filtered_average_spectral_density

        # estimate from radial spectrum data
        rspec = self.radially_averaged_spectrum(trn)
        tot_samples = np.sum(rspec[SAMPLE_COUNT])
        tot_energy = np.sum(np.exp(rspec[LOG_POWER]))
        asd = math.log(tot_energy / tot_samples)
        
        if trn == SOURCE:
            self._source_average_spectral_density = asd
        else:
            self._filtered_average_spectral_density = asd
            
        return asd

    def spectrum_grid(self, trn=SOURCE, file_name=None, overwrite=False):
        """
        Return the 2D log(power) amplitude as a grid in wavenumber domain (u, v).

        Amplitude = log(real**2 + imaginary**2)
        
        :param trn:      `SOURCE` source spectrum (default) or `FILTERED` filtered spectrum
        :param file_name:   name for the grid file, default is a temporary grid.
        :param overwrite:   `True` to overwrite existing grid.

        :return: `geosoft.gxpy.grid.Grid` instance
        
        .. versionadded:: 9.4
        """
        
        if trn == SOURCE:
            tr = self._source_transform
        else:
            tr = self._filtered_transform

        du = 1.0 / (tr.dx * (tr.nx - 2))
        dv = 1.0 / (tr.dy * tr.ny)
        props = tr.properties()
        props['nx'] = tr.nx // 2 
        props['ny'] = tr.ny
        props['x0'] = 0
        props['y0'] = -(tr.ny // 2) * dv
        props['dx'] = du 
        props['dy'] = dv
        nperr = {}

        sgrd = gxgrd.Grid.new(file_name=file_name, properties=props, overwrite=overwrite)
        try:
            nperr = np.seterr(under='ignore')
            for row in range(tr.ny):
                data = tr.read_row(row).np
                r = np.clip(data[0::2]**2, 1.0e-20, None)
                i = np.clip(data[1::2]**2, 1.0e-20, None)
                sgrd.write_row(np.log(r + i), self.uv_row_from_tr(row))
        finally:
            np.seterr(**nperr)

        return sgrd

    @property
    def source_grid(self):
        """ Source grid as a `geosoft.gxpy.grid.Grid` instance. """
        return self._source_grid

    @property
    def expanded_filled_grid(self):
        """ Expanded and filled grid as a `geosoft.gxpy.grid.Grid` instance. """
        return self._prep_grid

    @property
    def source_transform(self):
        """ Folded descrete Fourier transform as a `geosoft.gxpy.grid.Grid` instance."""
        return self._source_transform

    @property
    def filtered_transform(self):
        """ Folded descrete Fourier transform after filters applied."""
        if self._filtered_transform is None:
            self._filtered_transform = gxgrd.Grid.new(properties=self._source_transform.properties())
        return self._filtered_transform

    def result_grid(self, file_name=None, overwrite=False):
        """
        Produce a filter result grid.

        :param file_name:   result grid file, default greates a temporary grid
        :param overwrite:   `True` to overwrite an existing grid
        :return:            `geosoft.gxpy.grid.Grid` instance

        .. versionadded:: 9.4
        """

        if self._filtered_transform is None:
            self._source_transform = gxgrd.reopen(self._source_transform)
            trn = self._source_transform
        else:
            self._filtered_transform = gxgrd.reopen(self._filtered_transform)
            trn = self._filtered_transform
        fpg = trn.gxpg()
        tpg = gxapi.GXPG.create(fpg.n_rows(), fpg.n_cols(), fpg.e_type())
        tpg.copy(fpg)

        # fft result
        gxapi.GXFFT2.trans_pg(tpg, gxapi.FFT2_PG_INVERSE)

        # reduce
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

        result = gxgrd.Grid.from_data_array(result_pg, properties=self._source_grid.properties(),
                                            file_name=file_name, overwrite=overwrite)

        # mask against original grid
        result.mask(self.source_grid)

        return result
