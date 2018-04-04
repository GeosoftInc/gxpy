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


MAX_DIMENSION = 16384  #: maximum expanded grid is 16384 x 16384
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

                self._source_transform.close(discard=True)
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
        # TODO add step-wise expansion option as used in the fft2prep gx
        # TODO add arguments to control filling options
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
        self._source_transform = gxgrd.Grid.from_data_array(xpg, file_name=trn_file, properties=properties)
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

            gxc = gx.GXpy()

            with gxfft.GridFFT('some_mag_grid_file.grd', progress=print) as fft:

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

            gxc = gx.GXpy()

            with gxfft.GridFFT('some_mag_grid_file.grd', progress=print) as fft:

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

        :param trn:  `SOURCE` (default) return spectrum of the source data, or `FILTERED` return spectrum
                        of the current filtered state.

        .. versionadded:: 9.4
        """
        
        if trn == SOURCE:
            if self._source_spectrum is not None:
                return self._source_spectrum
            tr = self._source_transform
        else:
            if self._filtered_spectrum is not None:
                return self._filtered_spectrum
            tr = self._filtered_transform

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
