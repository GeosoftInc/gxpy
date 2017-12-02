"""
Geosoft voxel (voxset) handling.

:Classes:

    ============ =======================================================
    :class:`Vox` Geosoft voxel (voxset)
    ============ =======================================================

.. seealso:: :class:`geosoft.gxapi.GXIMG`, :class:`geosoft.gxapi.GXIMU`

.. note::

    Regression tests provide usage examples:     
    `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_vox.py>`_
    
"""
import os
import numpy as np

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import coordinate_system as gxcs
from . import vv as gxvv
from . import utility as gxu

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class VoxException(Exception):
    """
    Exceptions from :mod:`geosoft.gxpy.vox`.

    .. versionadded:: 9.1
    """
    pass

def _vox_file_name(name):
    ext = os.path.splitext(name)[1]
    if ext.lower() != '.geosoft_voxel':
        name = name + '.geosoft_voxel'
    return os.path.abspath(name)

def _vox_name(name):
    basename = os.path.basename(name)
    return os.path.splitext(basename)[0]

INTERP_NEAREST = gxapi.VOXE_EVAL_NEAR #:
INTERP_LINEAR = gxapi.VOXE_EVAL_INTERP #:
INTERP_SMOOTH = gxapi.VOXE_EVAL_BEST #:

def delete_files(vox_name):
    """
    Delete all files associates with this vox name.

    :param vox_name: name of the vox file

    .. versionadded:: 9.3
    """

    def df(fn):
        try:
            os.remove(fn)
        except OSError as e:
            pass

    if vox_name is not None:

        vox_name = _vox_file_name(vox_name)
        df(vox_name)
        df(vox_name + '.xml')


def cells_from_separations(sep):
    """
    TODO: This does not conform to how Geosoft calculates cells.

    Return cell sizes from a list of point separations. A cell is dimensioned to define a length that
    is the half the distance between a point and its neighbors. Edge cells are always the dimension of
    the separation between the two edge points.

    :param sep: iterable list of point separations
    :returns:   list is cell sizes, one longer than sep.

    .. seealso:: `separations_from_cells`

    .. versionadded:: 9.3.1
    """

    nsep = len(sep)
    cells = [0 for i in range(nsep + 1)]
    cells[0] = sep[0]
    for i in range(1, nsep):
        cells[i] = (sep[i - 1] + sep[i]) * 0.5
    cells[nsep] = sep[nsep-1]
    return cells


def separations_from_cells(cells):
    """
    TODO: This does not conform to how Geosoft calculates cells.

    Return point separations from a list of cell sizes.

    :param cells:   list of cell sizes
    :return:        list of separations, length is one less than cells

    .. seealso:: `cells_from_separations`

    .. versionadded:: 9.3.1
    """

    nsep = len(cells) - 1
    seps = [0 for i in range(nsep)]
    seps[0] = cells[0]
    for i in range(1, nsep):
        seps[i] = (cells[i] - seps[i - 1] * 0.5) * 2.
    return seps


# constants
MODE_READ = 0          #:
MODE_READWRITE = 1     #: file exists, but can change properties
MODE_NEW = 2           #:


class Vox:
    """
    Vox and image class.

    :Constructors:

        ======================= ============================================
        :meth:`open`            open an existing vox
        :meth:`new`             create a new vox
        :meth:`from_data_array` create a new vox from a 2d data array
        ======================= ============================================

    A vox instance supports iteration that yields (x, y, z, vox_value) by points along horizontal
    rows, then columns, then depth slices starting at minimum z.
    For example, the following prints the x, y, z, vox_value of every non-dummy point in a vox:

    .. code::

        import geosoft.gxpy.vox as gxvox

        with gxvox.Vox.open('some.geosoft_voxel') ad g:
            for x, y, z, v in g:
                if v is not None:
                    print(x, y, z, v)

    Specific vox cell values can be indexed (null vox values are None):

    .. code::

        import geosoft.gxpy.vox as gxvox

        with gxvox.Vox.open('some_voxel') as vox:
            for iz in range(vox.nz):
                for iy in range(vox.ny):
                    for ix in range(vox.nx):
                        x, y, z, v = vox[ix, iy, iz]
                        if v is not None:
                            print(x, y, z, v)

    .. versionadded:: 9.3.1
    """

    _delete_files = False
    _name = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.__del__()

    def __del__(self):
        if hasattr(self, '_close'):
            self._close()

    def _close(self, pop=True):

        if hasattr(self, '_open'):
            if self._open:

                if self._metadata_changed:
                    with open(self._file_name + '.xml', 'w+') as f:
                        f.write(gxu.xml_from_dict(self._metadata))

                self._gxvoxe = None
                self._gxvox = None
                self._pg =  None
                self._origin = None
                self._locations = None
                self._cells = None
                self._uniform_cell_size = None
                self._buffer_np = None
                self._metadata = None

                if self._delete_files:
                    delete_files(self._file_name)

                if pop:
                    gx.pop_resource(self._open)
                self._open = None

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self.name

    def __init__(self, name=None, gxvox=None):

        self._file_name = _vox_file_name(name)
        self._name = _vox_name(self._file_name)
        self._readonly = None
        self._metadata = None
        self._metadata_changed = False
        self._metadata_root = ''
        self._gxvox = gxvox
        self._cs = None
        self._gxvoxe = None
        self._next = self._next_x = self._next_y = self._next_z = 0
        self._locations = None
        self._cells = None
        self._pg = None
        self._buffered_plane = self._buffered_row = None
        self._metadata = None
        self._metadata_changed = False
        self._metadata_root = ''
        self._delete_files = False

        ityp = gxapi.int_ref()
        iarr = gxapi.int_ref()
        nx = gxapi.int_ref()
        ny = gxapi.int_ref()
        nz = gxapi.int_ref()
        self._gxvox.get_info(ityp, iarr, nx, ny, nz)
        self._dtype = gxu.dtype_gx(ityp.value)
        self._is_int = gxu.is_int(ityp.value)
        self._dim = (nx.value, ny.value, nz.value)
        self._max_iter = nx.value * ny.value * nz.value

        # location
        self._setup_locations()

        self._open = gx.track_resource(self.__class__.__name__, self._name)

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= self._max_iter:
            self._next = 0
            raise StopIteration
        else:
            v = self.__getitem__(self._next)
            self._next += 1
            return v

    def __getitem__(self, item):

        if isinstance(item, int):
            iz = item // (self.nx * self.ny)
            item -= iz * self.nx * self.ny
            ix = item % self.nx
            iy = item // self.nx

        else:
            ix, iy, iz = item

        x, y, z = self.xyz(ix, iy, iz)

        if (self._buffered_plane != iz) or (self._buffered_row != iy):
            self._buffered_plane = iz
            self._buffered_row = iy
            vv = gxvv.GXvv(dtype=self._dtype)
            self.gxpg.read_row_3d(iz, iy, 0, self._dim[0], vv.gxvv)
            self._buffer_np = vv.np
            if not self._is_int:
                gxu.dummy_to_nan(self._buffer_np)

        v = self._buffer_np[ix]
        if self._is_int:
            v = int(v)
            if v == gxapi.iDUMMY:
                v = None
        elif np.isnan(v):
            v = None
        return x, y, z, v

    def _init_metadata(self):
        if not self._metadata:
            self._metadata = gxu.geosoft_metadata(self._file_name)
        self._metadata_root = tuple(self._metadata.items())[0][0]

    @property
    def metadata(self):
        """
        Return the vox metadata as a dictionary.  Can be set, in which case
        the dictionary items passed will be added to, or replace existing metadata.

        .. seealso::
            `Geosoft metadata schema <https://geosoftgxdev.atlassian.net/wiki/spaces/GXD93/pages/78184638/Geosoft+Metadata+Schema>`

        .. versionadded:: 9.3
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
        except:
            uom = ''
        return uom

    @unit_of_measure.setter
    def unit_of_measure(self, uom):
        self.metadata = {'geosoft': {'dataset': {'geo:unitofmeasurement': {'#text': str(uom)}}}}
        self.metadata = {
            'geosoft': {'dataset': {'geo:unitofmeasurement': {'@xmlns:geo': 'http://www.geosoft.com/schema/geo'}}}}

    @classmethod
    def open(cls, name, gxapi_vox=None, mode=MODE_READ):
        """
        Open an existing vox.

        :param name:        name of the vox. If a name only the vox is resolved from the
                            project. If a file name or complete path, the vox is resolved from
                            the file system outside of the current project.
        :param gxapi_vox:   `gxapi.GXVOX` instance. Normally not required.
        :param mode:        open mode:

            =================  ==================================================
            MODE_READ          only read the vox, properties cannot be changed
            MODE_READWRITE     vox stays the same, but properties may change
            =================  ==================================================

        :returns:       `Vox` instance

        .. versionadded:: 9.3.1
        """

        if gxapi_vox is None:
            gxapi_vox = gxapi.GXVOX.create(_vox_file_name(name))
        vox = cls(name, gxapi_vox)

        if mode is None:
            mode = MODE_READ
        if mode == MODE_READ:
            vox._readonly = True
        else:
            vox._readonly = False

        return vox

    @classmethod
    def new(cls, name, data=None, dimension=None, temp=False, overwrite=False, dtype=None,
            origin=(0., 0., 0.), cell_size=(1., 1., 1.), init_value=None, coordinate_system=None):
        """
        Create a new vox dataset

        :param name:        dataset name, or a path to a persistent file.
        :param data:        data to place in the vox, must have 3 dimensions (nz, ny, nx). If not
                            specified the vox is initialized to dummy values.
        :param dimension:   required dimension, data and/or cell-sizes take precedence
        :param temp:        True to create a temporary vox which will be removed after use
        :param overwrite:   True to overwrite existing persistent vox
        :param dtype:       data type, default is the same as data, or np.float64
        :param origin:      (x0, y0, z0) location of the origin vox point. Note that this is not the corner
                            of a cell. This is the center of the first cell for a uniform cell size, or the
                            reference position of the first vox cell accounting for variable cell sizes.
        :param cell_size:   uniform cell size, or (dx, dy, dz) cell sizes in the x, y and z directions,
                            or a arrays of cell sizes for variable cell-size vox.  For example:
                            `cell_size=((1, 2.5, 1.5), (1, 1, 1, 1), (5, 4, 3, 2, 1))` will create a vox
                            with (x, y, z) dimension (3, 4, 5) and sizes as specified in each dimension.
        :param init_value:  initial value, default is the dummy for the dtype.
        :param coordinate_system:   coordinate system as required to create from `geosoft.gxpy.Coordinate_system`
        :returns:           `Vox` instance

        .. versionadded:: 9.3.1
        """

        if not temp:
            file_name = _vox_file_name(name)
            if not overwrite:
                if os.path.isfile(file_name):
                    raise VoxException(_t('Cannot overwrite existing vox {}'.format(file_name)))
        else:
            file_name = gx.GXpy().temp_file('.geosoft_voxel')

        if data is not None:
            if not isinstance(data, np.ndarray):
                data = np.array(data)
            if data.ndim != 3:
                raise VoxException(_t('Data must have 3 dimensions, this data has {} dimensions').format(data.ndim))
            dimension = (data.shape[2], data.shape[1], data.shape[0])
            dtype = data.dtype

        if (dimension is None):
            if ((not hasattr(cell_size[0], '__iter__')) or
                    (not hasattr(cell_size[1], '__iter__')) or
                    (not hasattr(cell_size[2], '__iter__'))):
                raise VoxException(_t('unable to determine vox dimension'))
            dimension = (len(cell_size[0]), len(cell_size[1]), len(cell_size[2]))

        dvv = list(cell_size)
        for i in range(3):
            if hasattr(dvv[i], '__iter__'):
                dvv[i] = gxvv.GXvv(dvv[i], dtype=np.float64)
            else:
                dvv[i] = np.zeros((dimension[i],)) + dvv[i]
                dvv[i] = gxvv.GXvv(dvv[i], dtype=np.float64)

        if dtype is None:
            dtype = np.float64

        if data is not None:

            pg = gxapi.GXPG.create_3d(dvv[2].length, dvv[1].length, dvv[0].length, gxu.gx_dtype(dtype))
            vv = gxvv.GXvv(dtype=dtype)
            vv.length = dvv[0].length

            for s in range(dvv[2].length):
                for iy in range(dvv[1].length):
                    vv.set_data(data[s, iy, :])
                    pg.write_row_3d(s, iy, 0, vv.length, vv.gxvv)

            gxvox = gxapi.GXVOX.generate_pgvv(file_name, pg,
                                              origin[0], origin[1], origin[2],
                                              dvv[0].gxvv, dvv[1].gxvv, dvv[2].gxvv,
                                              gxcs.Coordinate_system(coordinate_system).gxipj,
                                              gxapi.GXMETA.create())

        else:

            if init_value is None:
                init_value = gxu.gx_dummy(dtype)

            # create the vox
            gxvox = gxapi.GXVOX.generate_constant_value_vv(file_name,
                                                           init_value,
                                                           gxu.gx_dtype(dtype),
                                                           origin[0], origin[1], origin[2],
                                                           dvv[0].gxvv, dvv[1].gxvv, dvv[2].gxvv,
                                                           gxcs.Coordinate_system(coordinate_system).gxipj,
                                                           gxapi.GXMETA.create())

        vox = cls(name, gxvox)
        vox._file_name = file_name
        vox._readonly = False
        vox._setup_locations()
        vox._delete_files = temp

        return vox

    def close(self):
        """close the vox and release all instance resources."""
        self._close()

    @property
    def name(self):
        """Vox name"""
        return self._name

    @property
    def file_name(self):
        """Vox file name"""
        return self._file_name

    @property
    def gxvox(self):
        """`gxapi.GXVOX` instance handle"""
        return self._gxvox

    @property
    def nx(self):
        """ number of points in vox X direction"""
        return self._dim[0]

    @property
    def ny(self):
        """ number of points in vox Y direction"""
        return self._dim[1]

    @property
    def nz(self):
        """ number of points in vox Z direction"""
        return self._dim[2]

    @property
    def dx(self):
        """constant X point separation, None if not constant"""
        if self._uniform_cell_size[0] == gxapi.rDUMMY:
            return None
        return self._uniform_cell_size[0]

    @property
    def dy(self):
        """constant Y point separation, None if not constant"""
        if self._uniform_cell_size[1] == gxapi.rDUMMY:
            return None
        return self._uniform_cell_size[0]

    @property
    def dz(self):
        """constant Z point separation, None if not constant"""
        if self._uniform_cell_size[2] == gxapi.rDUMMY:
            return None
        return self._uniform_cell_size[2]

    @property
    def x0(self):
        """X location of the vox origin."""
        return self._origin[0]

    @property
    def y0(self):
        """Y location of the vox origin."""
        return self._origin[1]

    @property
    def z0(self):
        """Z location of the vox origin."""
        return self._origin[2]

    @property
    def uniform_dx(self):
        """True if X point separation is constant"""
        return self.dx is not None

    @property
    def uniform_dy(self):
        """True if Y point separation is constant"""
        return self.dy is not None

    @property
    def uniform_dz(self):
        """True if Z point separation is constant"""
        return self.dz is not None

    @property
    def extent(self):
        rx0 = gxapi.float_ref()
        ry0 = gxapi.float_ref()
        rz0 = gxapi.float_ref()
        rx1 = gxapi.float_ref()
        ry1 = gxapi.float_ref()
        rz1 = gxapi.float_ref()
        self.gxvox.get_area(rx0, ry0, rz0, rx1, ry1, rz1)
        return (rx0.value, ry0.value, rz0.value,
                rx1.value, ry1.value, rz1.value)

    @property
    def extent_2d(self):
        ex = self.extent
        return (ex[0], ex[1], ex[3], ex[4])

    @property
    def coordinate_system(self):
        """coordinate system"""
        ipj = gxapi.GXIPJ.create()
        self.gxvox.get_ipj(ipj)
        return gxcs.Coordinate_system(ipj)

    @coordinate_system.setter
    def coordinate_system(self, cs):
        self.gxvox.set_ipj(gxcs.Coordinate_system(cs).gxipj)

    def _setup_locations(self):
        xvv = gxvv.GXvv()
        yvv = gxvv.GXvv()
        zvv = gxvv.GXvv()
        self.gxvox.get_location_points(xvv.gxvv, yvv.gxvv, zvv.gxvv)
        self._locations = (xvv.np, yvv.np, zvv.np)
        x0 = gxapi.float_ref()
        y0 = gxapi.float_ref()
        z0 = gxapi.float_ref()
        xvv = gxvv.GXvv()
        yvv = gxvv.GXvv()
        zvv = gxvv.GXvv()
        self.gxvox.get_location(x0, y0, z0, xvv.gxvv, yvv.gxvv, zvv.gxvv)
        self._origin = (x0.value, y0.value, z0.value)
        self._cells = (xvv.np, yvv.np, zvv.np)
        dx = gxapi.float_ref()
        dy = gxapi.float_ref()
        dz = gxapi.float_ref()
        self._gxvox.get_simple_location(x0, y0, z0, dx, dy, dz)
        self._uniform_cell_size = (dx.value, dy.value, dz.value)


    @property
    def x_locations(self):
        """Return array of X locations"""
        if self._locations is None:
            self._setup_locations()
        return self._locations[0]

    @property
    def y_locations(self):
        """Return array of Y locations"""
        if self._locations is None:
            self._setup_locations()
        return self._locations[1]

    @property
    def z_locations(self):
        """Return array of Z locations"""
        if self._locations is None:
            self._setup_locations()
        return self._locations[2]

    @property
    def x_cells(self):
        """Return array of X cell sizes"""
        if self._cells is None:
            self._setup_locations()
        return self._cells[0]

    @property
    def y_cells(self):
        """Return array of Y cell sizes"""
        if self._cells is None:
            self._setup_locations()
        return self._cells[1]

    @property
    def z_cells(self):
        """Return array of Z cell sizes"""
        if self._cells is None:
            self._setup_locations()
        return self._cells[2]

    @property
    def gxpg(self):
        if self._pg is None:
            self._pg = self.gxvox.create_pg()
        return self._pg

    @property
    def gxvoxe(self):
        """Return a `gxapi.GXVOXE` instance"""
        if self._gxvoxe is None:
            self._gxvoxe = gxapi.GXVOXE.create(self.gxvox)
        return self._gxvoxe

    def _checkindex(self, ix, iy, iz):
        if (ix < 0) or (ix >= self.nx) or (iy < 0) or (iy >= self.ny) or (iz < 0) or (iz >= self.nz):
            raise IndexError(_t("Voxel index ({}, {}, {}) out of range ({}, {}, {}).").format(ix, iy, iz, self.nx, self.ny, self.nz))

    def xyz(self, ix, iy, iz):
        """
        Return the spatial location of a point in the vox.
        Raises error if our of range of the data

        :param ix:  x index
        :param iy:  y index
        :param iz:  z index, from bottom
        :return: (x, y, z)

        .. versionadded:: 9.3
        """
        self._checkindex(ix, iy, iz)
        return (self.x_locations[ix], self.y_locations[iy], self.z_locations[iz])

    def value_at_location(self, xyz, interpolate=INTERP_LINEAR):
        """
        Voxcet value at a location.

        :param xyz:         tuple (x, y, z) location in the vox coordinate system
        :param interpolate: method by which to interpolate between points:

                            INTERP_NEAREST - same as value inside a cell.

                            INTERP_LINEAR - linear interpolation between neighboring points.

                            INTERP_SMOOTH - smooth interpolation (slower than INTERP_LINEAR).

        :returns:           vox value at that location

        .. versionadded:: 9.3.1
        """
        x, y, z = xyz
        v = self.gxvoxe.value(x, y, z, interpolate)
        if v == gxapi.rDUMMY:
            return None
        return v

    def np_subset(self, start=(0, 0, 0), dimension=None):
        """
        Return vox subset in a 3D numpy array.

        :return: numpy array of shape (nz, ny, nx)

        .. versionadded:: 9.3.1
        """

        # dimensions
        x0, y0, z0 = start
        self._checkindex(x0, y0, z0)
        if dimension is None:
            nx = self.nx - x0
            ny = self.ny - y0
            nz = self.nz - z0
        else:
            nx, ny, nz = dimension
            self._checkindex(x0 + nx - 1, y0 + ny - 1, z0 + nz - 1)
        if nx < 0 or ny < 0 or nz < 0:
            raise VoxException(_t("Subset dimension {} invalid, require positive non-zero dimension").format((nx, ny, nz)))

        gxpg = self.gxpg
        npv = np.empty((nz, ny, nx), dtype=self._dtype)
        vv = gxvv.GXvv(dtype=self._dtype)
        vv.length = nx

        for iz in range(z0, z0 + nz):
            for iy in range(y0, y0 + ny):
                gxpg.read_row_3d(iz, iy, x0, nx, vv.gxvv)
                npv[iz - z0, iy - y0, :] = vv.np

        return npv
