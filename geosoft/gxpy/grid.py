"""
Geosoft grid and image handling, including all
`supported file formats <https://geosoftgxdev.atlassian.net/wiki/display/GXDEV92/Grid+File+Name+Decorations>`_ .

:Classes:
    :`Grid`: grid dataset

:Constants:
   :FILE_READ:       0 open for read, files are not changed
   :FILE_READWRITE:  1 open for read and write, files can be changed
   :FILE_NEW:        2 new grid file, accompanied by `overwrite=` parameter

.. seealso:: :mod:`geosoft.gxpy.grid_utility`, :mod:`geosoft.gxpy.grid_fft`,
    :class:`geosoft.gxapi.GXIMG`, :class:`geosoft.gxapi.GXIMU`

.. note::

    Regression tests provide usage examples:     
    `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_grid.py>`_

"""
import os
import numpy as np
import math

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import coordinate_system as gxcs
from . import vv as gxvv
from . import utility as gxu
from . import agg as gxagg
from . import geometry as gxgm
from . import map as gxmap
from . import grid_utility as gxgrdu
from . import view as gxview
from . import gdb as gxgdb

__version__ = geosoft.__version__


FILE_READ = 0
FILE_READWRITE = 1
FILE_NEW = 2


def _t(s):
    return geosoft.gxpy.system.translate(s)


class GridException(geosoft.GXRuntimeError):
    """
    Exceptions from :mod:`geosoft.gxpy.grid`.

    .. versionadded:: 9.1
    """
    pass


def reopen(g, dtype=None, mode=FILE_READWRITE):
    """
    Reopen a grid to access the grid as an existing grid.
    
    Some gxapi.GXIMU methods will not work with grids open as new grids. This method closes
    the grid and reopens in the specific mode
    
    :param g:       `Grid` instance
    :param dtype:   data type, None to match the data type of the grid being reopened
    :param mode:    `FILE_READWRITE` (default) or `FILE_READ`
    :return:        new `Grid` instance
    
    .. versionadded:: 9.4
    """

    if dtype is None:
        dtype = g.dtype
    dfn = g.file_name_decorated
    delete_set = g.remove_on_close
    g.delete_files(False)
    g.close()
    g = Grid.open(dfn, dtype=dtype, mode=mode)
    if delete_set:
        g.delete_files()
    return g


def name_parts(name):
    """
    Return folder, undecorated file name + ext, file root, ext, decorations.

    If extension is not specified, ".grd" assumed

    For example:

    .. code::

        >>> import geosoft.gxpy.grid as gxgrd
        >>> namep = gxgrd.name_parts("f:/someFolder/name.grd(GRD;TYPE=SHORT)")
        >>> print(namep)
        ('f:/someFolder/','name.grd','name','.grd','(GRD;TYPE=SHORT)')

    .. versionadded:: 9.1
    """

    path = os.path.abspath(name)
    fn = os.path.dirname(path)
    root, ext = os.path.splitext(os.path.basename(path))

    if '(' in ext:
        ext, dec = ext.split('(')
        if ')' in dec:
            dec = dec.split(')')[0]
    else:
        dec = ''

    if not ext:
        if (not dec) or (dec[:3].upper() == 'GRD'):
            ext = '.grd'
    name = root + ext

    return fn, name, root, ext, dec


def decorate_name(name, decorations=''):
    """
    Properly decorate a grid name.

    :param name:        file name
    :param decorations: file decorations, semicolon delimited
    :returns:           decorated file name

    .. versionadded:: 9.1
    """

    if name is None:
        return None

    root, ext = os.path.splitext(name)
    dec = decorations.strip()
    if dec:
        d = decorations.lstrip('(')
        end = d.rfind(')')
        if end != -1:
            d = d[:end]
        ext = ext.split('(')[0]
        return '{}{}({})'.format(root, ext, d)

    else:
        if ext.lower() == '.grd':
            return '{}{}(GRD)'.format(root, ext)
        else:
            return name


def delete_files(file_name):
    """
    Delete all files associates with this grid name.

    :param file_name: name of the grid file

    .. versionadded:: 9.2
    """

    if file_name is not None:

        fn = name_parts(file_name)
        file_name = os.path.join(fn[0], fn[1])
        ext = fn[3]
        gxu.delete_file(file_name)
        gxu.delete_file(file_name + '.gi')
        gxu.delete_file(file_name + '.xml')

        # remove shaded files associated with this grid
        file_s = os.path.join(fn[0], fn[1].replace('.', '_')) + '_s.grd'
        gxu.delete_file(file_s)
        gxu.delete_file(file_s + '.gi')
        gxu.delete_file(file_s + '.xml')

        # hgd files
        if ext == '.hgd':
            for i in range(16):
                gxu.delete_file(file_name + str(i))


def _transform_color_int_to_rgba(np_values):
    np_values[np_values == gxapi.iDUMMY] = 0
    a = (np.right_shift(np_values, 24) & 0xFF).astype(np.uint8)
    b = (np.right_shift(np_values, 16) & 0xFF).astype(np.uint8)
    g = (np.right_shift(np_values, 8) & 0xFF).astype(np.uint8)
    r = (np_values & 0xFF).astype(np.uint8)
    # the values for color grids actually do not contain alphas but just
    # 0 or 1 to indicate if the color is valid or not
    a[a > 0] = 255
    return np.array([r, g, b, a]).transpose()


class Grid(gxgm.Geometry):
    """
    Grid and image class.

    :Constructors:

        ========================= ==============================================================
        :meth:`open`              open an existing grid/image
        :meth:`new`               create a new grid/image
        :meth:`copy`              create a copy
        :meth:`index_window`      create a windowed grid based on grid indexes
        :meth:`from_data_array`   create a new grid from a 2d data array
        :meth:`minimum_curvature` create by fitting a minimum-curvature surface to located data.
        ========================= ==============================================================

    A grid instance supports iteration that yields (x, y, z, grid_value) by points along rows.
    For example, the following prints the x, y, z, grid_value of every non-dummy point in a grid:

    .. code::

        import geosoft.gxpy.grid as gxgrd

        with gxgrd.Grid.open('some.grd') ad g:
            for x, y, z, v in g:
                if v is not None:
                    print(x, y, z, v)

    Specific grid cell values can be indexed (null grid values are None):

    .. code::

        import geosoft.gxpy.grid as gxgrd

        with gxgrd.Grid.open('some.grd') as g:
            for ix in range(g.nx):
                for iy in range(g.ny):
                    x, y, z, v = g[ix, iy]
                    if v is not None:
                        print(x, y, z, v)

    .. versionadded:: 9.1

    .. versionchanged:: 9.2.1 added iterator support
    """

    _delete_files = False
    _file_name = None

    def __enter__(self):
        return self

    def __exit__(self, _type, _value, _traceback):
        self.__del__()

    def __del__(self):
        if hasattr(self, '_close'):
            self._close()

    def _close(self, pop=True):

        def flush_hgd(hgd_temp):

            # convert tempory grid to an HGD file
            img = gxapi.GXIMG.create_file(gxapi.GS_TYPE_DEFAULT,
                                          decorate_name(hgd_temp, 'GRD'),
                                          gxapi.IMG_FILE_READONLY)
            gxapi.GXHGD.h_create_img(img, decorate_name(self._hgd_name, 'HGD'))
            img = None

        if hasattr(self, '_open'):
            if self._open:

                self._img = None

                grid_file_name = self._file_name
                file_name_decorated = decorate_name(self._file_name, self._decoration) if self._decoration else None

                if self._hgd:

                    flush_hgd(self._file_name)
                    if self._metadata_changed:
                        with open(self._file_name + '.xml', 'w+') as f:
                            f.write(gxu.xml_from_dict(self._metadata))
                        if file_name_decorated:
                            gxapi.GXIMG.sync(file_name_decorated)
                    delete_files(grid_file_name)

                else:

                    if self._delete_files:
                        delete_files(self._file_name)
                    elif self._mode != FILE_READ:
                        if file_name_decorated:
                            try:
                                gxapi.GXIMG.sync(file_name_decorated)
                            except (geosoft.GXRuntimeError, geosoft.gxapi.GXAPIError):
                                # Locked files, extremely large files (e.g. GXF) etc. could cause errors with the
                                # command above. TODO: Do we even need it? The code below overwrites it anyway?
                                pass

                        if grid_file_name:
                            if self._metadata and self._metadata_changed:
                                with open(grid_file_name + '.xml', 'w+') as f:
                                    f.write(gxu.xml_from_dict(self._metadata))

                if pop:
                    gx.pop_resource(self._open)
                self._open = None
                self._buffer_np = None
                self._buffer_x = None
                self._buffer_y = None
                self._cs = None
                self._gxpg = None

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        if self._file_name is None:
            return '<class Grid>: memory ({}, {})'.format(self.nx, self.ny)
        else:
            return '<class Grid>: {} ({}, {})'.format(self.file_name_decorated, self.nx, self.ny)

    def __init__(self, file_name=None, in_memory=False, dtype=None, mode=None, kx=1, dim=None, overwrite=False, **kwargs):

        self._delete_files = False
        self._readonly = False
        self._decoration = ''

        if 'name' not in kwargs:
            if file_name:
                kwargs['name'] = os.path.splitext(file_name)[0]
            else:
                kwargs['name'] = '_grid_'
        super().__init__(**kwargs)

        self._hgd = False
        self._hgd_name = None
        self._metadata = None
        self._metadata_changed = False
        self._metadata_root = ''
        self._img = None
        self._buffered_row = None
        self._buffer_np = None
        self._buffered_xy = None
        self._buffer_x = None
        self._buffer_y = None
        self._cs = None
        self._gxpg = None

        # build a file name
        if in_memory:
            self._file_name = None
        else:
            if (file_name is None) or (len(file_name.strip()) == 0):
                file_name = gx.gx().temp_file('.grd(GRD)')
            path, file_name, root, ext, self._decoration = name_parts(file_name)
            self._file_name = os.path.join(path, file_name)

            # for an HGD file work with a temporary grid, save to HGD on closing
            if mode == FILE_NEW and ext.lower() == '.hgd':
                self._hgd = True
                self._hgd_name = self._file_name
                file_name = gx.gx().temp_file('.grd(GRD)')
                path, file_name, root, ext, self._decoration = name_parts(file_name)
                self._file_name = os.path.join(path, file_name)

        if mode == FILE_NEW:
            if dtype is None:
                dtype = np.float64
            gxtype = gxu.gx_dtype(dtype)
            if in_memory:
                self._img = gxapi.GXIMG.create(gxtype, kx, dim[0], dim[1])
                # Need to set the kx otherwise it will be 0 and some routines (e.g. IMU stats calc) could cause aborts
                self._img.opt_kx(kx)
            else:    
                if not overwrite:
                    if os.path.isfile(self._file_name):
                        raise GridException(_t('Cannot overwrite existing grid {}'.format(self.file_name)))
                self._img = gxapi.GXIMG.create_new_file(gxtype,
                                                        kx, dim[0], dim[1],
                                                        decorate_name(self._file_name, self._decoration))
        else:  # open an existing grid

            if mode == FILE_READ:
                open_mode = gxapi.IMG_FILE_READONLY
                self._readonly = True
            else:
                mode = FILE_READWRITE
                open_mode = gxapi.IMG_FILE_READORWRITE
                self._readonly = False

            # always open in default type unless float or double specifically requested
            gxtype = gxapi.GS_TYPE_DEFAULT
            if dtype is not None:
                gxtype_from_dtype = gxu.gx_dtype(dtype)
                if gxtype_from_dtype in (gxapi.GS_FLOAT, gxapi.GS_DOUBLE):
                    gxtype = gxtype_from_dtype

            self._img = gxapi.GXIMG.create_file(gxtype,
                                                self.file_name_decorated,
                                                open_mode)
            if dtype is None:
                dtype = gxu.dtype_gx(self._img.e_type())

        self._mode = mode
        self._next = 0
        self._next_row = 0
        self._next_col = 0
        self._gxtype = self._img.e_type()
        self._dtype = dtype
        self._dummy = gxu.gx_dummy(self._dtype)
        self._is_int = gxu.is_int(gxu.gx_dtype(self.dtype))
        self._cos_rot = self._sin_rot = None
        self.rot = self.rot  # this sets _cos_rot and _sin_rot

        self._open = gx.track_resource(self.__class__.__name__, self._file_name)

    @classmethod
    def open(cls, file_name, dtype=None, mode=FILE_READ,
             coordinate_system=None, cell_size=None, expand=None):
        """
        Open an existing grid file.

        :param file_name:   name of the grid file, with decorations. See `supported file formats
                            <https://geosoftgxdev.atlassian.net/wiki/display/GXDEV92/Grid+File+Name+Decorations>`_)
        :param dtype:       numpy data type, which will be the grid data type.
        :param mode:        open mode:

            =================  ================================================
            FILE_READ          only read the file, properties cannot be changed
            FILE_READWRITE     grid stays the same, but properties may change
            =================  ================================================

        :param coordinate_system:   desired coordinate system. The grid will be reprojected if necessary.
        :param cell_size:           desired cell size, defaults to the current cell size.
        :param expand:              if reprojecting or resampling the are can be expanded by this percentage
                                    to allow for curved edges in the new coordinate system space.  The default
                                    expands by 1%. Set to 0 to prevent expansion.

        If reprojecting or setting the cell size different from the original grid, the mode must be FILE_READ.

        If reprojecting without setting the cell size a default cell size will be calculated in the new
        coordinate system that is nominally equivalent to the current cell size.

        .. versionadded:: 9.1

        .. versionchanged:: 9.4     added reprojection support
        """

        grd = cls(file_name, dtype=dtype, mode=mode)

        # determine if we need to reproject or resample
        repro = False
        if coordinate_system:
            if not isinstance(coordinate_system, gxcs.Coordinate_system):
                coordinate_system = gxcs.Coordinate_system(coordinate_system)
            repro = coordinate_system != grd.coordinate_system

        if (not repro and cell_size is not None) and ((cell_size != grd.dx) or (cell_size != grd.dy)):
            repro = True

        if repro:
            if mode != FILE_READ:
                raise GridException(_t('Mode must be FILE_READ to reproject or resample a grid.'))
            if cell_size is None:
                cell_size = gxapi.rDUMMY
            if expand is None:
                expand = gxapi.rDUMMY
            if not coordinate_system:
                coordinate_system = grd.coordinate_system
            grd.gximg.create_projected3(coordinate_system.gxipj, cell_size, expand)
            grd._cs = None
            grd._cos_rot = 1.0
            grd._sin_rot = 0.0

        return grd

    @classmethod
    def new(cls, file_name=None, properties=None, overwrite=False, in_memory=False):
        """
        Create a new grid file.

        :param file_name:   name of the grid file, None for a temporary grid. See `supported file formats
                            <https://geosoftgxdev.atlassian.net/wiki/display/GXDEV92/Grid+File+Name+Decorations>`_)
        :param in_memory:   Creates an in-memory grid (file_name will be ignored)
        :param properties:  dictionary of grid properties, see :meth:`properties`
        :param overwrite:   True to overwrite existing file

        .. versionadded:: 9.1
        """

        if properties is None:
            raise GridException(_t("Missing properties dictionary."))

        # set basic grid properties
        dtype = properties.get('dtype', None)
        nx = properties.get('nx', 0)
        ny = properties.get('ny', 0)
        if (nx <= 0) or (ny <= 0):
            raise GridException(_t('Grid dimension ({},{}) must be > 0').format(nx, ny))

        grd = cls(file_name, in_memory=in_memory, dtype=dtype, mode=FILE_NEW, dim=(nx, ny), overwrite=overwrite)
        grd.set_properties(properties)

        return grd

    @classmethod
    def minimum_curvature(cls, data,
                          unit_of_measure=None,
                          file_name=None, overwrite=False,
                          max_segments=1000,
                          coordinate_system=None,
                          cs='',
                          area=('', '', '', ''),
                          bclip='',
                          logopt='',
                          logmin='',
                          idsf='',
                          bkd='',
                          srd='',
                          iwt='',
                          edgclp='',
                          tol='',
                          pastol='100',
                          itrmax='',
                          ti='',
                          icgr=''):
        """
        Create a minimum-curvature surface grid from (x, y, value) located data.

        Reference: Smith and Wessel, 1990, Gridding with continuous curvature splines in tension.

        :param data:        list of [(x, y, value), ...] or a callback that returns lists, or a tuple
                            (gdb, value_channel, x_channel, y_channel) where x_channel and y_channel, if not
                            specified, default to the current database (x, y) channels.  See below.
        :param unit_of_measure: string unit of measurement descriptor.
        :param file_name:   name of the grid file, None for a temporary grid. See `supported file formats
                            <https://geosoftgxdev.atlassian.net/wiki/display/GXDEV92/Grid+File+Name+Decorations>`_)
        :param overwrite:   True to overwrite existing file
        :param max_segments:   Maximum number of line segments if using a callback, defaults to 1000.
        :param coordinate_system:   coordinate system

        Gridding parameters follow the nomenclature of the rangrid.con file:
        https://github.com/GeosoftInc/gxc/blob/master/reference/con_files/rangrid.con

        :param cs:      The grid cell size in reference system units.
        :param area:    (xmin, ymin, xmax, ymax) - grid area, default is the data limits
        :param bclip:   0 to use all data (default), 1 to only use data in the dat area.
        :param logopt:  1 for log(value) minimum cliped to log(logmin); 2 for `logmin + log(value/logmin)` for
                        postive `value`, `-logmin - log(-value/logmin` for negative `value`
        :param logmin:  see `logopt`, default is 1.
        :param idsf:    low-pass desampling factor in cells, default is 1. Effectively a low-pass filter that
                        can smooth noisy data that has clustered locations.
        :param bkd:     Blanking distance. All grid cells farther than the blanking
                        distance from a valid point will be blanked in the output grid.
                        The default is the nominal sample interval, i.e. sqrt(area/#data).
                        This parameter should normally be set to just greater than the maximum
                        sampling interval through which interpolation is desired.
                        If there are too many holes in the resulting grid,
                        increase appropriately.
        :param srd:     The maximum search radius to use for establishing the starting
                        values for the coarse grid.  The default is four times the coarse
                        grid size defined by `icgr`.  If no data is found within the maximum
                        search radius, the mean of the data is used as the starting value.
                        If the search radius is too small, the starting grid can be a poor
                        approximation of the desired grid, resulting in excessive processing
                        time.  If too large, too much time will be consumed establishing
                        the original coarse grid.
        :param iwt:     The weighting power to use to establish the coarse starting grid.
                        The default is 2, for inverse distance squared.  There is little
                        reason to change this from the default.
        :param edgclp:  Edge clipping parameter, the number of grid cells to extend beyond
                        the outside limits of the data. The default (-1) is not to apply
                        edge clipping to the blanking distanced grid.
                        Use this parameter to ensure the grid does not extend too far
                        beyond the actual data limits, which can occur when using a large
                        blanking distance with widely spaced data.
        :param tol:     The tolerance required for each grid cell. The default is 0.1
                        percent of the range of the data. Decrease for a more accurate grid.
        :param pastol:  The percentage of points that must meet the tolerance. The
                        iteration process will stop when the percentage of points change
                        by higher than this required percentage in iteration. The default
                        is 100.0 percent. Decrease for rough data to reduce minimum curvature
                        overshoot, and increase for a to make the grid surface more accurately
                        match the data. Overshoot can also be controlled by increasing tension (ti).
        :param itrmax:  Maximum number of iterations to use in solving the minimum curvature
                        function.  The default is 200 iterations.  Increase for a more
                        accurate grid.  A value of 1000 is typically sufficient for maximum accuracy.
        :param ti:      The degree of internal tension ( between 0 and 1 ).
                        The default is no tension (0.0) which produces a true minimum
                        curvature surface.  Increasing tension can prevent overshooting of
                        valid data in sparse areas at the expense of increased local curvature
                        near data points.
        :param icgr:    The course grid size relative to the final grid size.  Allowable
                        factors are 16,8,4,2 or 1.  The default is 8.  The optimum is a
                        factor close to half the nominal data spacing, although in most
                        situations the default is fine.  This parameter effects the
                        length of time it takes to find a solution.

        **The** `data` **parameter:**

        The data can be provided to the gridding algorithm either as a list array, a callback function that
        returns list array segments, or a `geosoft.gxpy.gdb.Geosoft_database` instance. In the case of a list or
        a callback, a temporary database is constructed internally.

        A callback is passed a sequence number, 0, 1, 2, ... and is expected to return a list array with each call
        or None when there is no more data.  See the example below. When a callback is used, the `max_segments`
        parameter sets the maximum number of lines for the temporary database as each return from the
        callback will create a new line in the internal temporary database.

        If a database instance is passed it must be the first item in a tuple of 2 or 4 items:
        (gdb_instance, value_channel) or (gdb_instance, value_channel, x_channel, y_channel).
        In the first case the default spatial (x, y) channels in the database are assumed.

        Examples:

        .. code::

            import numpy as np
            import geosoft.gxpy.grid as gxgrd

            # simple data array
            xyv = [(45., 10., 100), (60., 25., 77.), (50., 8., 80.)]
            grid = gxgrd.Grid.minimum_curvature(xyv)

            # or a numpy array
            grid = gxgrd.Grid.minimum_curvature(np.array(xyv))

            # a database, grid to a cell size of 100
            import geosoft.gxpy.gdb as gxgdb
            gdb = gxgdb.Geosoft_database.open('some_mag_data.gdb')
            grid = gxgrd.Grid.minimum_curvature((gdb, 'tmi'), cs=100)

            # a callback, used for very large data, or to feed data efficiently from some other source.
            nxyv = np.array([[(45., 10., 100), (60., 25., 77.), (50., 8., 81.), (55., 11., 66.)],
                             [(20., 15., 108), (25.,  5., 77.), (33., 9., np.nan), (28., 2., 22.)],
                             [(35., 18., 110), (40., 31., 77.), (13., 4., 83.), (44., 4., 7.)]])
            def feed_data(n):
                if n >= len(nxyv):
                    return None
                return nxyv[n]
            grid = gxgrd.Grid.minimum_curvature(feed_data, cs=1.)

        .. versionadded:: 9.4
        """

        def gdb_from_callback(callback):
            _gdb = gxgdb.Geosoft_gdb.new(max_lines=max_segments)
            channels = ('x', 'y', 'v')
            il = 0
            xyz_list = callback(il)
            while xyz_list is not None:
                _gdb.write_line('L{}'.format(il), xyz_list, channels=channels)
                il += 1
                xyz_list = callback(il)
            _gdb.xyz_channels = channels[:2]
            return _gdb

        def gdb_from_data(_d):
            def _data(i):
                if i == 0:
                    return _d
                else:
                    return None
            return gdb_from_callback(_data)

        # create a database from the data
        xc, yc = ('x', 'y')
        discard = False
        if callable(data):
            gdb = gdb_from_callback(data)
            vc = 'v'
            discard = True

        elif isinstance(data, tuple):
            gdb = data[0]
            vc = data[1]
            if len(data) == 4:
                xc = data[2]
                yc = data[3]
            else:
                xc, yc, _ = gdb.xyz_channels
            discard = True

        else:
            gdb = gdb_from_data(data)
            vc = 'v'

        if tol and float(tol) <= 0.:
            tol = 1.0e-25

        # parameter control file
        con_file = gx.gx().temp_file('con')
        with open(con_file, 'x') as f:
            f.write('{} / cs\n'.format(cs))
            f.write('{},{},{},{},{} / xmin, ymin, xmax, ymax, bclip\n'.
                    format(area[0], area[1], area[2], area[3], bclip))
            f.write(',,,{},{} / ,,, logopt, logmin\n'.format(logopt, logmin))
            f.write('{},{},{},{},{} / idsf, bkd, srd, iwt, edgeclp\n'.format(idsf, bkd, srd, iwt, edgclp))
            f.write('{},{},{},{},{} / tol, pastol, itrmax, ti, icgr\n'.format(tol, pastol, itrmax, ti, icgr))

        if file_name is None:
            file_name = gx.gx().temp_file('grd(GRD)')
        elif os.path.exists(file_name):
            if overwrite:
                gxu.delete_files_by_root(file_name)
            else:
                raise GridException(_t('Cannot overwrite existing file: {}').format(file_name))

        gxapi.GXRGRD.run2(gdb.gxdb, xc, yc, vc, con_file, file_name)

        grd = cls.open(file_name, mode=FILE_READWRITE)
        if coordinate_system is None:
            coordinate_system = gdb.coordinate_system
        grd.coordinate_system = coordinate_system
        if unit_of_measure is None:
            unit_of_measure = gxgdb.Channel(gdb, vc).unit_of_measure
        grd.unit_of_measure = unit_of_measure

        log_file = 'rangrid.log'
        if os.path.exists(log_file):
            gxu.delete_file(log_file)

        if discard:
            gdb.close(discard=True)

        return grd

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= self.nx * self.ny:
            self._next = 0
            raise StopIteration
        else:
            v = self.__getitem__(self._next)
            self._next += 1
            return v

    def __getitem__(self, item):

        if isinstance(item, int):
            ix = item % self.nx
            iy = item // self.nx
        else:
            ix, iy = item

        x, y, z = self.xyz((ix, iy))

        if self._buffered_row != iy:
            self._buffered_row = iy
            self._buffer_np = self.read_row(self._buffered_row).np

        v = self._buffer_np[ix]
        if self._is_int:
            v = int(v)
            if v == gxapi.iDUMMY:
                v = None
        elif np.isnan(v):
            v = None
        else:
            v = float(v)
        return x, y, z, v

    def gxpg(self, copy=False):
        """
        Get a copy of the `geosoft.gxapi.GXPG` instance for the grid.

        :param copy:    `True` to return a copy of the grids pager. The default is `False`, which
                        returns the shared grid pager, such that changes to the pager change the grid
                        and the pager is invalid when thr grid is closed or loses context.

        .. versionadded:: 9.1

        .. versionchanged:: 9.4 added `copy` parameter
        """

        if self._gxpg is None:
            self._gxpg = self._img.geth_pg()

        if copy:
            pg = gxapi.GXPG.create(self._gxpg.n_rows(), self._gxpg.n_cols(), self._gxpg.e_type())
            pg.copy(self._gxpg)
            return pg
        return self._gxpg

    def get_value(self, x, y):
        """
        Return a grid value at a point as a float.  For scalar data the point value will
        be interpolated between neighbors.  For color data the nearest value is returned
        as a color int.
        
        :param x: X location on the grid plane 
        :param y: Y location on the grid plane
        :returns: grid value, or None if outside of grid area
        
        """
        return gxu.dummy_none(self.gximg.get_z(x, y))

    @classmethod
    def copy(cls, grd, file_name=None, dtype=None, overwrite=False, in_memory=False, mode=FILE_READWRITE):
        """
        Create a new Grid instance as a copy of an existing grid.

        :param grd:         :class:`Grid` instance to save as a new grid, or a grid file name
        :param file_name:   name of the new grid (file with optional decorations). If not specified a temporary file
                            is created.
        :param dtype:       numpy data type, None to use type of the parent grid
        :param overwrite:   True to overwrite if the file exists, False to not overwrite.
        :param in_memory:   True to create a grin in memory.
        :param mode:        `open` mode for working with the copy.

        .. versionadded:: 9.2
        """

        if not isinstance(grd, Grid):
            grd = cls.open(grd, mode=FILE_READ)
            close_grid = True
        else:
            close_grid = False

        p = grd.properties()
        if dtype is not None:
            p['dtype'] = dtype

        if not in_memory and file_name is not None:
            path0, base_file0, root0, ext0, dec0 = name_parts(grd.file_name_decorated)
            path1, base_file1, root1, ext1, dec1 = name_parts(file_name)
            if not ext1:
                ext1 = ext0
            if (ext1 == ext0) and not dec1:
                dec1 = dec0
            file_name = decorate_name(os.path.join(path1, root1) + ext1, dec1)

        copy = cls.new(file_name, p, overwrite=overwrite, in_memory=in_memory)
        if file_name is None:
            file_name = copy.file_name_decorated
        grd.gximg.copy(copy.gximg)

        if close_grid:
            grd.close()

        if in_memory:
            return copy

        copy.close()
        return cls.open(file_name, dtype=dtype, mode=mode)

    @classmethod
    def index_window(cls, grd, name=None, x0=0, y0=0, nx=None, ny=None, overwrite=False):
        """
        Create a windowed instance of a grid.
        
        :param grd:         :class:`Grid` instance
        :param name:        name for the windowed_grid, default is constructed from input grid
        :param x0:          integer index of the first X point
        :param y0:          integer index of the first Y point
        :param nx:          number of points in x
        :param ny:          number of points in y
        :param overwrite:   True to overwrite existing file, default is False

        .. versionadded:: 9.2
        """

        if not isinstance(grd, Grid):
            grd = Grid.open(grd)

        gnx = grd.nx
        gny = grd.ny
        if nx is None:
            nx = gnx - x0
        if ny is None:
            ny = gny - y0
        mx = x0 + nx
        my = y0 + ny
        if ((x0 >= gnx) or (y0 >= gny) or
                (x0 < 0) or (y0 < 0) or
                (nx <= 0) or (ny <= 0) or
                (mx > gnx) or (my > gny)):
            raise GridException(_t('Window x0,y0,mx,my({},{},{},{}) out of bounds ({},{})').
                                format(x0, y0, mx, my, gnx, gny))

        if name is None:
            path, file_name, root, ext, dec = name_parts(grd.file_name_decorated)
            name = '{}_({},{})({},{}){}'.format(root, x0, y0, nx, ny, ext)
            name = decorate_name(name, dec)
            overwrite = True

        # create new grid
        p = grd.properties()
        p['nx'] = nx
        p['ny'] = ny
        if grd.rot == 0.0:
            p['x0'] = grd.x0 + grd.dx * x0
            p['y0'] = grd.y0 + grd.dy * y0
        else:
            dx = grd.dx * x0
            dy = grd.dy * y0
            cos, sin = grd.rotation_cos_sine
            p['x0'] = grd.x0 - dx * cos - dy * sin
            p['y0'] = grd.y0 - dy * cos + dx * sin

        window_grid = cls.new(name, p, overwrite=overwrite)
        source_pager = grd.gxpg(copy=False)
        window_pager = window_grid.gxpg(copy=False)
        window_pager.copy_subset(source_pager, 0, 0, y0, x0, ny, nx)

        return window_grid

    @classmethod
    def from_data_array(cls, data, file_name=None, properties=None, overwrite=False):
        """
        Create grid from a 2D data array or `geosoft.gxapi.GXPG`.

        :param data:        2D numpy data array, a 2d list, ir a `geosoft.gxapi.GXPG`.
        :param file_name:   name of the file, default creates a temporary file name
        :param properties:  grid properties as a dictionary
        :param overwrite:   `True` to overwrite existing grid.
        :returns:           :class:`Grid` instance

        .. versionadded:: 9.1

        .. versionchanged:: 9.4 - support for default temporary file name and creation from a GXPG.
        """

        if isinstance(data, gxapi.GXPG):
            if data.n_slices() != 1:
                raise GridException(_t('Pager must be 2D'))
            nx = data.n_cols()
            ny = data.n_rows()
            dtype = gxu.dtype_gx(data.e_type())

        else:
            if not isinstance(data, np.ndarray):
                data = np.array(data)
            ny, nx = data.shape
            dtype = data.dtype

        if properties is None:
            properties = {}
        properties['nx'] = nx
        properties['ny'] = ny
        properties['dtype'] = dtype

        if (file_name is None) or (len(file_name.strip()) == 0):
            file_name = gx.gx().temp_file('.grd(GRD)')

        grd = cls.new(file_name, properties=properties, overwrite=overwrite)
        grd.write_rows(data)

        return reopen(grd)

    @property
    def is_crooked_path(self):
        """True if this grid follows a crooked path section."""
        return self.coordinate_system.gxipj.get_orientation() == gxapi.IPJ_ORIENT_SECTION_CROOKED

    def crooked_path(self):
        """
        Return the `CrookedPath` instance for a crooked-path grid.

        .. versionadded::9.4
        """
        if not self.is_crooked_path:
            raise GridException(_t("This is not a crooked-path section grid."))
        return gxview.CrookedPath(self.coordinate_system)

    @property
    def rotation_cos_sine(self):
        """
        Returns grid rotation (cosine, sine).

        .. versionadded:: 9.3.1
        """
        return self._cos_rot, self._sin_rot

    def delete_files(self, delete=True):
        """
        Delete the files associated with this grid when deleting the grid object.
        Note that files are not deleted until all references to this object are
        deleted and garbage collection is performed.

        :param delete: set to False to reverse a previous delete request

        .. versionadded:: 9.1
        """
        self._delete_files = delete

    @property
    def remove_on_close(self):
        """Remove files on close setting, can be set."""
        return self._delete_files
    
    @remove_on_close.setter
    def remove_on_close(self, tf):
        self._delete_files = bool(tf)

    def close(self, discard=False):
        """
        Close the grid and release all instance resources.

        :param discard: `True` to discard associated files on close

        .. versionchanged:: 9.4 added `discard` parameter
        """
        if discard:
            self.delete_files()
        self._close()

    @property
    def dummy_value(self):
        """ Return the grid data dummy value."""
        return self._dummy

    @property
    def gximg(self):
        """ The `geosoft.gxapi.GXIMG` instance handle."""
        return self._img

    def _init_metadata(self):
        if not self._metadata:
            self._metadata = gxu.geosoft_metadata(self._file_name)
        self._metadata_root = tuple(self._metadata.items())[0][0]

    @property
    def metadata(self):
        """
        Return the grid metadata as a dictionary.  Can be set, in which case
        the dictionary items passed will be added to, or replace existing metadata.
        
        .. seealso::
            `Geosoft metadata schema <https://geosoftgxdev.atlassian.net/wiki/display/GXDEV92/Geosoft+Metadata+Schema>`_     

        .. versionadded:: 9.2
        """
        self._init_metadata()
        return self._metadata[self._metadata_root]

    @metadata.setter
    def metadata(self, meta):
        self._init_metadata()
        self._metadata[self._metadata_root] = gxu.merge_dict(self._metadata[self._metadata_root], meta)
        self._metadata_changed = True

    @property
    def unit_of_measure(self):
        """
        Units of measurement (a string) for the grid data, can be set.
        
        .. versionadded:: 9.2
        """
        try:
            uom = self.metadata['geosoft']['dataset']['geo:unitofmeasurement']['#text']
        except (KeyError, TypeError):
            uom = ''
        return uom

    @unit_of_measure.setter
    def unit_of_measure(self, uom):
        self.metadata = {'geosoft':
                             {'@xmlns': 'http://www.geosoft.com/schema/geo',
                              'dataset':
                                  {'geo:unitofmeasurement':
                                       {'@xmlns:geo': 'http://www.geosoft.com/schema/geo',
                                        '#text': str(uom)}}}}

    @property
    def dtype(self):
        """
        numpy data type for the grid

        .. versionadded:: 9.2
        """
        return self._dtype

    @property
    def gxtype(self):
        """
        Geosoft data type for the grid

        .. versionadded:: 9.2
        """
        return self._gxtype

    @property
    def is_int(self):
        """ returns True if base grid type is integer, which includes color integers"""
        return self._is_int

    @property
    def nx(self):
        """
        grid x dimension (number of columns)

        .. versionadded:: 9.2
        """
        return self._img.nx()

    @property
    def ny(self):
        """
        grid y dimension (number of rows)

        .. versionadded:: 9.2
        """
        return self._img.ny()

    @property
    def x0(self):
        """
        grid origin x location in the plane coordinate system

        .. versionadded:: 9.2
        """
        return self._img.query_double(gxapi.IMG_QUERY_rXO)

    @property
    def y0(self):
        """
        grid origin y location in the plane coordinate system

        .. versionadded:: 9.2
        """
        return self._img.query_double(gxapi.IMG_QUERY_rYO)

    @property
    def dx(self):
        """
        separation between grid points in the grid x direction

        .. versionadded:: 9.2
        """
        return self._img.query_double(gxapi.IMG_QUERY_rDX)

    @property
    def dy(self):
        """
        separation between grid points in the grid y direction

        .. versionadded:: 9.2
        """
        return self._img.query_double(gxapi.IMG_QUERY_rDY)

    @property
    def rot(self):
        """
        grid rotation angle, degrees azimuth
        
        Note that grid rotations in the gxapi GXIMG are degrees clockwise, which is the opposite of
        degree azimuth, used here.  All horizontal plane angles in the Python gxpy module are degrees
        azimuth for consistency.

        .. versionadded:: 9.2
        """
        return -self._img.query_double(gxapi.IMG_QUERY_rROT)

    @property
    def is_color(self):
        """ returns True if grid contains colors. is_int will also be True"""
        return bool(self._img.is_colour())

    @property
    def file_name(self):
        """
        grid file name without decorations

        .. versionadded:: 9.2
        """
        if self._hgd:
            return self._hgd_name
        return self._file_name

    @property
    def file_name_decorated(self):
        """
        grid file name with decorations

        .. versionadded:: 9.2
        """
        if self._hgd:
            decor = 'HGD'
        else:
            decor = self._decoration
        return decorate_name(self.file_name, decor)

    @property
    def name(self):
        """
        Grid name, usually the file name without path or extension.
        
        .. versionadded:: 9.2
        """
        if self._file_name is None:
            return 'None'
        basename = os.path.basename(self.file_name)
        return os.path.splitext(basename)[0]

    @property
    def gridtype(self):
        """
        grid type (ie. 'GRD' or 'HGD')

        .. versionadded:: 9.2
        """
        _, _, _, ext, dec = name_parts(self._file_name)
        if len(dec) > 0:
            return dec.split(';')[0]
        else:
            return ext[1:].upper()

    @property
    def decoration(self):
        """
        grid descriptive decoration

        .. versionadded:: 9.2
        """
        return self._decoration

    @property
    def coordinate_system(self):
        """
        grid coordinate system as a :class:`geosoft.gxpy.coordinate_system.Coordinate_system` instance.

        Can be set from any :class:`geosoft.gxpy.coordinate_system.Coordinate_system` constructor.

        .. versionadded:: 9.2

        .. versionchanged:: 9.3
            added ability to set directly
        """
        if self._cs is None:
            ipj = gxapi.GXIPJ.create()
            self._img.get_ipj(ipj)
            self._cs = gxcs.Coordinate_system(ipj)

        return self._cs

    @coordinate_system.setter
    def coordinate_system(self, cs):
        self._cs = gxcs.Coordinate_system(cs)
        self._img.set_ipj(self._cs.gxipj)

    def properties(self):
        """
        Get the grid properties dictionary

        :returns: dictionary of all grid properties

        .. versionadded:: 9.1

        .. versionchanged:: 9.4 added 'unit_of_measure'
        """

        properties = {'nx': self.nx,
                      'ny': self.ny,
                      'x0': self.x0,
                      'y0': self.y0,
                      'dx': self.dx,
                      'dy': self.dy,
                      'rot': self.rot,
                      'is_color': self.is_color,
                      'dtype': self.dtype,
                      'gridtype': self.gridtype,
                      'decoration': self._decoration,
                      'unit_of_measure': self.unit_of_measure,
                      'coordinate_system': self.coordinate_system}

        return properties

    def statistics(self, gxst=None):
        """
        Calculate and return current grid data statistics as a dictionary.

        :param gxst:    gxapi.GXST instance, to which stats will be accumulated, or None.

        :returns: dictionary of grid data statistics:

        =============== ============================
        min             minimum
        max             maximum
        mean            mean
        geometric_mean  geometric mean
        variance        variance
        sd              standard deviation
        skew            skew
        kurtosis        kurtosis
        sum             sum of all data
        sum_power_2     sum of data**2
        sum_power_3     sum of data**3
        sum_power_4     sum of data**4
        num_data        number of valid data values
        num_dummy       number of dummy values
        =============== ============================

        .. versionadded:: 9.4
        """

        def get_st(what):
            v = gxst.get_info(what)
            if v == gxapi.rDUMMY:
                return None
            return v

        if gxst is None:
            gxst = gxapi.GXST.create()
        vv = gxvv.GXvv()
        for iv in range(self.gximg.nv()):
            self.gximg.read_v(iv, 0, 0, vv.gxvv)
            gxst.data_vv(vv.gxvv)

        st = {'min': get_st(gxapi.ST_MIN),
              'max': get_st(gxapi.ST_MAX),
              'mean': get_st(gxapi.ST_MEAN),
              'geometric_mean': get_st(gxapi.ST_GEOMEAN),
              'variance': get_st(gxapi.ST_VARIANCE),
              'sd': get_st(gxapi.ST_STDDEV),
              'skew': get_st(gxapi.ST_SKEW),
              'kurtosis': get_st(gxapi.ST_KURTOSIS),
              'sum': get_st(gxapi.ST_SUM),
              'sum_power_2': get_st(gxapi.ST_SUM2),
              'sum_power_3': get_st(gxapi.ST_SUM3),
              'sum_power_4': get_st(gxapi.ST_SUM4),
              'num_data': get_st(gxapi.ST_ITEMS),
              'num_dummy': get_st(gxapi.ST_DUMMIES)
              }

        return st

    @x0.setter
    def x0(self, v):
        self._img.set_info(self.dx, self.dy, v, self.y0, -self.rot)

    @y0.setter
    def y0(self, v):
        self._img.set_info(self.dx, self.dy, self.x0, v, -self.rot)

    @dx.setter
    def dx(self, v):
        self._img.set_info(v, self.dy, self.x0, self.y0, -self.rot)

    @dy.setter
    def dy(self, v):
        self._img.set_info(self.dx, v, self.x0, self.y0, -self.rot)

    @rot.setter
    def rot(self, v):
        self._img.set_info(self.dx, self.dy, self.x0, self.y0, -v)
        self._cos_rot = math.cos(math.radians(v))
        self._sin_rot = math.sin(math.radians(v))

    def set_properties(self, properties):
        """
        Set grid properties from a properties dict.  Settable property keys are:

            ==================== ============================================
            'x0'                 grid X origin location (default 0.0)
            'y0'                 grid Y origin location (0.0)
            'dx'                 grid X point separation (1.0)
            'dy'                 grid Y point separation (1.0)
            'rot'                grid rotation angle in degrees azimuth (0.0)
            'unit_of_measure'    unit of measure for the grid data
            'coordinate_system'  coordinate system (unchanged)
            ==================== ============================================

        Not all keys need be passed, though typically one will get the properties from
        the grid and modify those that need to change and pass the properties back.

        :param properties: properties dictionary

        .. versionadded:: 9.1
        """

        if self._readonly:
            raise GridException(_t('{} opened as read-only, cannot set properties.').format(self.file_name_decorated))

        dx = properties.get('dx', 1.0)
        dy = properties.get('dy', dx)
        self._img.set_info(dx, dy,
                           properties.get('x0', 0.0),
                           properties.get('y0', 0.0),
                           -properties.get('rot', 0.0))
        self.rot = self.rot  # calculates cos and sin

        uom = properties.get('unit_of_measure', None)
        if uom is not None:
            self.unit_of_measure = uom

        cs = properties.get('coordinate_system', None)
        if cs is not None:
            if not isinstance(cs, gxcs.Coordinate_system):
                cs = gxcs.Coordinate_system(cs)
            self._img.set_ipj(cs.gxipj)

    def write_rows(self, data, ix0=0, iy0=0, order=1):
        """
        Write data to a grid by rows.

        :param data:    array of data to write, numpy, list or `geosoft.gxapi.GXPG`
        :param ix0:     grid X index of first point
        :param iy0:     grid Y index of first point, top index if writing rows top to bottom
        :param order:   1: bottom to top; -1: top to bottom

        .. versionadded:: 9.1

        .. versionchanged:: 9.4 accepts list or GXPG
        """

        if isinstance(data, gxapi.GXPG):
            nx = data.n_cols()
            ny = data.n_rows()

        else:
            if not isinstance(data, np.ndarray):
                data = np.array(data)
            ny, nx = data.shape

        if ((nx - ix0) > self.nx) or ((ny - iy0) > self.ny):
            raise(_t('Data size exceeds grid size.'))

        dvv = gxvv.GXvv(dtype=self.dtype)
        dvv.length = nx
        iy = iy0

        for i in range(ny):
            if isinstance(data, gxapi.GXPG):
                data.read_row(i, 0, 0, dvv.gxvv)
            else:
                dvv.set_data(data[i, :])
            self._img.write_y(iy, ix0, 0, dvv.gxvv)
            iy += order

    def read_row(self, row=None, start=0, length=None):
        """

        :param row:     row to read, if not specified the next row is read starting from row 0
        :param start:   the first point in the row, default is 0
        :param length:  number of points to read, the default is to the end of the row.
        :return:        :class:`geosoft.gxvv.GXvv` instance

        .. versionadded:: 9.1
        """

        if row is None:
            row = self._next_row
        self._next_row = row + 1
        if self._next_row == self.ny:
            self._next_row = 0

        if row >= self.ny:
            raise GridException(_t('Attempt to read row {} past the last row {}'.format(row, self.ny)))
        vv = gxvv.GXvv(dtype=self.dtype)
        if length is None:
            length = 0
        self._img.read_y(row, start, length, vv.gxvv)

        return vv

    def read_column(self, column=None, start=0, length=0):
        """

        :param column:  column to read, if not specified the next column is read starting from column 0
        :param start:   the first point in the column, default is 0
        :param length:  number of points to read, the default is to the end of the col.
        :return:        :class:`geosoft.gxvv.GXvv` instance

        .. versionadded:: 9.1
        """

        if column is None:
            column = self._next_col
        if column >= self.nx:
            raise GridException(_t('Attempt to read column {} past the last column {}'.format(column, self.ny)))
        self._next_col = column + 1
        if self._next_col == self.nx:
            self._next_col = 0

        vv = gxvv.GXvv(dtype=self.dtype)
        self._img.read_x(column, start, length, vv.gxvv)

        return vv

    def write_row(self, data, row=None, start=0, length=None):
        """

        :param data:    data to write, `geosoft.gxpy.vv.GXvv` instance or an array
        :param row:     row to write, if not specified the next row is written starting from row 0
        :param start:   the first point in the row, default is 0
        :param length:  number of points to read, the default is to the end of the row.

        .. versionadded:: 9.4
        """

        if not isinstance(data, gxvv.GXvv):
            data = gxvv.GXvv(data, dtype=self.dtype)

        if row is None:
            row = self._next_row
        self._next_row = row + 1
        if self._next_row == self.ny:
            self._next_row = 0

        if row >= self.ny:
            raise GridException(_t('Attempt to read row {} past the last row {}'.format(row, self.ny)))
        if length is None:
            length = 0
        self._img.write_y(row, start, length, data.gxvv)

    def write_column(self, data, column=None, start=0, length=None):
        """

        :param data:    data to write, `geosoft.gxpy.vv.GXvv` instance or an array
        :param column:  column to write, if not specified the next column is written starting from column 0
        :param start:   the first point in the column, default is 0
        :param length:  number of points to write, the default is to the end of the row.

        .. versionadded:: 9.4
        """

        if not isinstance(data, gxvv.GXvv):
            data = gxvv.GXvv(data, dtype=self.dtype)

        if column is None:
            column = self._next_col
        self._next_col = column + 1
        if self._next_col == self.nx:
            self._next_col = 0

        if column >= self.nx:
            raise GridException(_t('Attempt to read column {} past the last column {}'.format(column, self.nx)))
        if length is None:
            length = 0
        self._img.write_x(column, start, length, data.gxvv)

    def reset_read_write(self):
        """ Reset the default read/write to the grid row 0, column 0. """
        self._next = self._next_col = self._next_row = 0

    @staticmethod
    def name_parts(name):
        """
        .. deprecated:: 9.2 use gxpy.grid.name_parts()
        """
        return name_parts(name)

    @staticmethod
    def decorate_name(name, decorations=''):
        """
        .. deprecated:: 9.2 use gxpy.grid.name_parts()
        """
        return decorate_name(name, decorations)

    def indexWindow(self, name, x0=0, y0=0, nx=None, ny=None):
        """
        .. deprecated:: 9.2 gxpy.Grid.index_window()
        """
        return self.index_window(self, name, x0, y0, nx, ny, overwrite=True)

    def xy_from_index(self, ix, iy):
        """
        Return the rotated location of grid index ix, iy

        :param ix:  grid index x
        :param iy:  grid index y

        .. versionadded:: 9.4
        """

        def rotate(x, y):
            x -= self.x0
            y -= self.y0
            _x = x * self._cos_rot + y * self._sin_rot
            _y = -x * self._sin_rot + y * self._cos_rot
            return _x + self.x0, _y + self.y0

        x = self.x0 + (ix * self.dx)
        y = self.y0 + (iy * self.dy)
        if self.rot != 0.:
            return rotate(x, y)
        return x, y

    def extent_2d(self):
        """
        Return the 2D extent of the grid on the grid plane.

        Extent is to the outer edge of grid "cells", which extend half a cell beyond the edge points.

        :returns:(min_x, min_y, max_x, max_y)

        .. versionadded:: 9.2

        .. versionchanged:: 9.4 - extent to the cell edges.
        """

        x0, y0 = self.xy_from_index(-0.5, -0.5)
        x1, y1 = self.xy_from_index(self.nx - 0.5, self.ny - 0.5)

        if self.rot != 0.:
            xx0, yy0 = self.xy_from_index(self.nx - 0.5, -0.5)
            xx1, yy1 = self.xy_from_index(-0.5, self.ny - 0.5)
            min_x = min(x0, xx0, x1, xx1)
            min_y = min(y0, yy0, y1, yy1)
            max_x = max(x0, xx0, x1, xx1)
            max_y = max(y0, yy0, y1, yy1)
            return min_x, min_y, max_x, max_y

        return x0, y0, x1, y1

    def extent_point_2d(self):
        """
        Return the 2D extent of the grid point (cell centers) on the grid plane.

        :returns:(min_x, min_y, max_x, max_y)

        .. versionadded:: 9.4
        """

        x0, y0 = self.x0, self.y0
        x1, y1 = self.xy_from_index(self.nx - 1, self.ny - 1)

        if self.rot != 0.:
            xx0, yy0 = self.xy_from_index(self.nx - 1, 0)
            xx1, yy1 = self.xy_from_index(0, self.ny - 1)
            min_x = min(x0, xx0, x1, xx1)
            min_y = min(y0, yy0, y1, yy1)
            max_x = max(x0, xx0, x1, xx1)
            max_y = max(y0, yy0, y1, yy1)
            return min_x, min_y, max_x, max_y

        return x0, y0, x1, y1

    def extent_cell_2d(self):
        """
        .. deprecated:: 9.4 - same as `extent_2d()`
        """
        return self.extent_2d()

    def extent_3d(self):
        """
        Return the 3D extent of the grid in the base coordinate system.

        :returns: (min_x, min_y, min_z, max_x, max_y, max_z)

        .. versionadded:: 9.2
        """

        cs = self.coordinate_system
        ex2d = self.extent_2d()
        if self.is_crooked_path:
            min_x, min_y, max_x, max_y = self.crooked_path().extent_xy
            min_z = cs.xyz_from_oriented((ex2d[0], ex2d[1], 0.0))[2]
            max_z = cs.xyz_from_oriented((ex2d[0], ex2d[3], 0.0))[2]

        else:
            xyz0 = cs.xyz_from_oriented((ex2d[0], ex2d[1], 0.0))
            xyz1 = cs.xyz_from_oriented((ex2d[2], ex2d[1], 0.0))
            xyz2 = cs.xyz_from_oriented((ex2d[2], ex2d[3], 0.0))
            xyz3 = cs.xyz_from_oriented((ex2d[0], ex2d[3], 0.0))

            min_x = min(xyz0[0], xyz1[0], xyz2[0], xyz3[0])
            min_y = min(xyz0[1], xyz1[1], xyz2[1], xyz3[1])
            min_z = min(xyz0[2], xyz1[2], xyz2[2], xyz3[2])
            max_x = max(xyz0[0], xyz1[0], xyz2[0], xyz3[0])
            max_y = max(xyz0[1], xyz1[1], xyz2[1], xyz3[1])
            max_z = max(xyz0[2], xyz1[2], xyz2[2], xyz3[2])

        return min_x, min_y, min_z, max_x, max_y, max_z

    def extent_cell_3d(self):
        """
        .. deprecated:: 9.4 - same as `extent_3d()`
        """
        return self.extent_3d()

    @property
    def extent(self):
        """
        Grid cell extent as `geosoft.gxpy.geometry.Point2`.

        .. versionadded:: 9.3.1
        """
        return gxgm.Point2((self.extent_3d()), coordinate_system=self.coordinate_system)

    def np(self, dtype=None):
        """
        Return a numpy array of grid values in the working dtype.

        :param dtype:   desired data type, default is the work_dtype, ignored for color grids

        :returns: numpy array shape (nx, ny) or (nx, ny, 4) containing RGBA bytes in case of color grids

        .. versionadded:: 9.3.1
        """

        nx = self.nx
        ny = self.ny
        if self.is_color:
            data = np.zeros((ny, nx, 4), np.dtype(np.uint8))
        else:
            if dtype is None:
                dtype = self.dtype
            data = np.zeros((ny, nx), dtype=dtype)
        if self.gximg.query_kx() == -1:
            for i in range(self.nx):
                column = self.read_column(i).np
                if self.is_color:
                    column = _transform_color_int_to_rgba(column)
                data[:, i] = column
        else:
            for i in range(self.ny):
                row = self.read_row(i).np
                if self.is_color:
                    row = _transform_color_int_to_rgba(row)
                data[i, :] = row

        return data

    def xyzv(self):
        """
        Return a numpy float array of (x, y, z, v) grid points.

        x, y, z) is the location of each grid point in 3D space and v is the grid value at that location.
        Dummies will be numpy.nan.

        :returns: numpy array shape (nx, ny, 4)

        .. versionadded:: 9.2
        """

        nx = self.nx
        ny = self.ny
        dx = self.dx
        dy = self.dy
        cs = self.coordinate_system
        xyzv = np.zeros((ny, nx, 4))
        xyzv[:, :, 0:2] = np.mgrid[0: (nx - 0.5) * dx: dx, 0: (ny - 0.5) * dy: dy].swapaxes(0, 2)

        if self.rot != 0.:
            x = xyzv[:, :, 0]
            cosx = x * self._cos_rot
            sinx = x * self._sin_rot
            y = xyzv[:, :, 1]
            cosy = y * self._cos_rot
            siny = y * self._sin_rot
            xyzv[:, :, 0] = cosx + siny
            xyzv[:, :, 1] = cosy - sinx

        xyzv += (self.x0, self.y0, 0, 0)

        if cs.is_oriented:
            xyzv[:, :, :3] = cs.xyz_from_oriented(xyzv[:, :, :3].reshape((-1, 3))).reshape((ny, nx, 3))

        if self.gximg.query_kx() == -1:
            for i in range(self.nx):
                xyzv[:, i, 3] = self.read_column(i).np
        else:
            for i in range(self.ny):
                xyzv[i, :, 3] = self.read_row(i).np

        return xyzv

    def xyz(self, item):
        """
        Returns the (x, y, z) location of an indexed point in the grid.

        :param item: tuple (ix, iy) grid point, or the point number counting by row
        :return: tuple (x, y, z) location

        .. versionadded:: 9.2.1
        """

        if isinstance(item, int):
            ix = item % self.nx
            iy = item // self.nx
        else:
            ix, iy = item

        if self._buffered_xy != iy:
            self._buffered_xy = iy
            self._buffer_x = np.arange(self.nx, dtype=np.float64)
            self._buffer_x *= self.dx
            self._buffer_y = np.zeros(self.nx, dtype=np.float64)
            self._buffer_y += iy * self.dy

            if self.rot != 0.:
                rx = self._buffer_x * self._cos_rot + self._buffer_y * self._sin_rot
                self._buffer_y *= self._buffer_y * self._cos_rot
                self._buffer_y -= self._buffer_x * self._sin_rot
                self._buffer_x = rx

            self._buffer_x += self.x0
            self._buffer_y += self.y0

        ggx = self._buffer_x[ix]
        ggy = self._buffer_y[ix]
        ggz = 0.

        if self.coordinate_system.is_oriented:
            ggx, ggy, ggz = self.coordinate_system.xyz_from_oriented((ggx, ggy, ggz))

        return ggx, ggy, ggz

    def image_file(self, image_file_name=None, image_type=gxmap.RASTER_FORMAT_PNG, pix_width=None,
                   shade=False, color_map=None, contour=None, display_area=None, pix_32_bit=False):
        """
        Save as a georeferenced image file.

        :param image_file_name:  image file name. The extension should be consistent with the image_type.
                            If not specified a temporary PNG file is created.
        :param image_type:  image type, one ot the RASTER_FORMAT constants in `geosoft.gxpy.map`.
        :param pix_width:   desired image width in pixels, default is the width of the aggregate base layer
        :param shade:       `True` to add shading effect
        :param color_map:   `geosoft.gxpy.group.Color_map` instance, or a colour ramp file name,
                            default is grid's default
        :param contour:     colour contour interval if colours need to break at exact levels
        :param display_area:    `geosoft.gxpy.geometry.Point2` instance, which defines the desired display
                                area. The display area coordinate system can be different from the grid.
        :param pix_32_bit:  make 32-bit image (with 8-bit alpha background)
        :return:            image file name.

        .. seealso:: `geosoft.gxpy.grid.image_file`, which creates an image directly from a grid file.

        .. Note:: Unless read-only this method saves the grid as a temporary file from which an aggregate and image are
            created. If the grid already exists as a grid file it is more efficient to call
            `geosoft.gxpy.grid.image_file`.

        .. versionadded:: 9.3.1
        """

        temp_grid = gx.gx().temp_file('grd')
        try:
            if self._mode == FILE_READ and self._file_name is not None:
                grd_decorated = self.file_name_decorated
            else:
                with self.__class__.copy(self, temp_grid) as g:
                    grd_decorated = g.file_name_decorated

            if color_map is None:
                color_map = self.get_default_color_map()

            imagefile = image_file(grd_decorated,
                                   image_file=image_file_name,
                                   image_type=image_type,
                                   pix_width=pix_width,
                                   shade=shade,
                                   color_map=color_map,
                                   contour=contour,
                                   display_area=display_area,
                                   pix_32_bit=pix_32_bit)
        finally:
            delete_files(temp_grid)

        return imagefile

    def generate_color_map(self, method=gxapi.ITR_ZONE_DEFAULT):
        """
        Generate color map for grid based on statistics and method

        :param      method:  :ref:`ITR_ZONE`
        :return:    A `geosoft.gxpy.group.Color_map` instance.

        .. versionadded:: 9.4.0
        """
        itr = gxapi.GXITR.create_img(self._img, "", method, gxapi.rDUMMY)
        return geosoft.gxpy.group.Color_map(itr)

    def get_default_color_map(self):
        """
        Get default color map for grid

        :return:  A `geosoft.gxpy.group.Color_map` instance.

        .. versionadded:: 9.4.0
        """
        itr = gxapi.GXITR.create()
        if 1 == self._img.get_def_itr(itr):
            return self.generate_color_map()

        return geosoft.gxpy.group.Color_map(itr)


    def mask(self, mask):
        """
        Mask against blank areas in `mask` grid.  Both grids must be same dimension.

        :param mask:  reference mask grid, file of `Grid` instance.

        .. versionadded:: 9.4
        """

        if not isinstance(mask, Grid):
            mask = Grid.open(mask)

        if (self.nx != mask.nx or self.ny != mask.ny):
            raise GridException(_t('Grids dimensions do not match'))

        for row in range(self.ny):
            mr = self.read_row(row)
            mr.gxvv.mask(mask.read_row(row).gxvv)
            self.write_row(mr, row)


# grid utilities
def array_locations(properties):
    """
    Create an array of (x,y,z) points for a grid defined by properties
    :param properties:  grid properties
    :returns:           array of points, shaped (ny, nx, 3)

    .. versionadded:: 9.1
    """

    with Grid.new(properties=properties) as g:
        return g.xyzv()[:, :, :3]


def gridMosaic(*args, **kwargs):
    """
    .. deprecated:: 9.2 use :py:method: grid_mosaic
    """
    return grid_mosaic(*args, **kwargs)


def grid_mosaic(*args, **kwargs):
    """
    .. deprecated:: 9.4 use `geosoft.gxpy.grid_utility.grid_mosaic`
    """


def gridBool(*args, **kwargs):
    """
    .. deprecated:: 9.2 use `grid_bool`
    """
    return grid_bool(*args, **kwargs)


def grid_bool(*args, **kwargs):
    """
    .. deprecated:: 9.4 use `geosoft.gxpy.grid_utility.grid_bool`
    """
    return gxgrdu.grid_bool(*args, **kwargs)


def figure_map(grid_file, map_file=None, shade=True, color_map=None, contour=None, **kwargs):
    """
    Create a map figure from a grid file.

    :param grid_file:   grid file name
    :param map_file:    name of the map file, if `None` a default map is created.
    :param shade:       `True` to add shading effect
    :param color_map:   `geosoft.gxpy.group.Color_map` instance, or a colour ramp file name, default is user's default
    :param contour:     colour contour interval if colours need to break at exact levels
    :param kwargs:      passed to  `geosoft.gxpy.agg.Aggregate_image.figure_map` and `geosoft.gxpy.map.Map.new`
    :return:            `geosoft.gxpy.map.Map` instance

    .. versionadded:: 9.3
    """

    with gxagg.Aggregate_image.new(grid_file, shade=shade, color_map=color_map, contour=contour) as agg:
        return agg.figure_map(file_name=map_file, **kwargs)


def image_file(grid_file, image_file=None, image_type=gxmap.RASTER_FORMAT_PNG, pix_width=None,
               shade=True, color_map=None, contour=None, display_area=None, pix_32_bit=False):
    """
    Save a grid file grid as a georeferenced image file.

    :param grid_file:   grid file name
    :param image_file:  image file name. The extension should be consistent with the image_type.
                        If not specified a temporary PNG file is created.
    :param image_type:  image type, one ot the RASTER_FORMAT constants in `geosoft.gxpy.map`.
    :param pix_width:   desired image width in pixels, default is the width of the aggregate base layer
    :param shade:       `True` to add shading effect
    :param color_map:   `geosoft.gxpy.group.Color_map` instance, or a colour ramp file name, default is grid's default
    :param contour:     colour contour interval if colours need to break at exact levels
    :param display_area:    `geosoft.gxpy.geometry.Point2` instance, which defines the desired display
                            area. The display area coordinate system can be different from the grid.
    :param pix_32_bit:  make 32-bit image (with 8-bit alpha background)

    :return:            image file name.

    .. versionadded:: 9.3.1
    """

    if color_map is None:
        with Grid.open(grid_file) as g:
            color_map = g.get_default_color_map()

    with gxagg.Aggregate_image.new(grid_file, shade=shade, color_map=color_map, contour=contour) as agg:
        return agg.image_file(image_file, image_type=image_type, pix_width=pix_width,
                              display_area=display_area, pix_32_bit=pix_32_bit)
