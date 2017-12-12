"""
Geosoft voxel (voxset) handling.

:Classes:

    ============ =======================================================
    :class:`Vox` Geosoft voxel (voxset)
    ============ =======================================================

.. seealso:: `geosoft.gxpy.vox_display`, `geosoft.gxapi.GXVOX`

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
    """
    pass

def _vox_file_name(name, vectorvoxel=False):
    ext = os.path.splitext(name)[1].lower()
    if (ext == '.geosoft_voxel') or (ext == '.geosoft_vectorvoxel'):
        return name
    if vectorvoxel:
        return name + '.geosoft_vectorvoxel'
    return name + '.geosoft_voxel'

def _vox_name(name):
    basename = os.path.basename(name)
    return os.path.splitext(basename)[0]

INTERP_NEAREST = gxapi.VOXE_EVAL_NEAR #:
INTERP_LINEAR = gxapi.VOXE_EVAL_INTERP #:
INTERP_SMOOTH = gxapi.VOXE_EVAL_BEST #:

def delete_files(vox_name):
    """
    Delete all files associated with this vox name.

    :param vox_name: name of the vox file

    .. versionadded:: 9.3.1
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

def locations_from_cells(cells, ref=0.0):
    """
    Return the cell center locations from an array of cell sizes.

    :param cells:   array of cell sizes
    :param ref:     reference (origin)  added to values
    :return:        location array

    .. versionadded:: 9.3.1
    """

    if isinstance(cells, gxvv.GXvv):
        cells = list(cells.np)

    locations = list(cells)
    locations[0] = ref
    for i in range(1, len(cells)):
        locations[i] = locations[i - 1] + (cells[i - 1] + cells[i]) * 0.5
    return locations

def elevation_from_depth(depth_origin, depth_cells):
    """
    Return elevation origin and elevation cells sizes from a depth origin and depth cell-sizes

    :param depth_origin:    top vox z origin as depth below 0
    :param depth_cells:     cell sizes with depth
    :return:                elevation origin (bottom cell), cell sizes up from origin

    .. versionadded:: 9.3.1
    """

    vv = False
    if isinstance(depth_cells, gxvv.GXvv):
        depth_cells = list(depth_cells.np)
        vv = True

    elevation_origin = -locations_from_cells(depth_cells, depth_origin)[len(depth_cells) - 1]  # elevation origin is the deepest cell
    elevation_cells = list(reversed(depth_cells))
    if vv:
        return elevation_origin, gxvv.GXvv(elevation_cells)
    return elevation_origin, list(reversed(depth_cells))


# constants
MODE_READ = 0          #:
MODE_READWRITE = 1     #: file exists, but can change properties
MODE_NEW = 2           #:

Z_ELEVATION = 0 #:
Z_DEPTH = 1 #:

class Vox:
    """
    Vox and image class.

    :Constructors:

        ======================= ============================================
        :meth:`open`            open an existing vox
        :meth:`new`             create a new vox
        ======================= ============================================

    A vox instance supports iteration that yields (x, y, z, vox_value) by points along horizontal
    rows, then columns, then depth slices starting at minimum z.
    For example, the following prints the x, y, z, vox_value of every non-dummy point in a vox:

    .. code::

        import geosoft.gxpy.vox as gxvox

        with gxvox.Vox.open('some.geosoft_voxel') as g:
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

    def __init__(self, name=None, gxvox=None, dtype=None):

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
        if dtype is None:
            self._dtype = gxu.dtype_gx(ityp.value)
        else:
            self._dtype = dtype
        self._return_int = gxu.is_int(gxu.gx_dtype(self._dtype))
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

        if self.is_depth:
            iz = self.nz - iz - 1

        if (self._buffered_plane != iz) or (self._buffered_row != iy):
            self._buffered_plane = iz
            self._buffered_row = iy
            if self.is_vectorvox:
                vv = gxvv.GXvv(dtype=self._dtype, dim=3)
            else:
                vv = gxvv.GXvv(dtype=self._dtype)
            self.gxpg.read_row_3d(iz, iy, 0, self._dim[0], vv.gxvv)
            self._buffer_np = vv.np

        v = self._buffer_np[ix]
        if self._return_int:
            v = int(v)
            if v == gxapi.iDUMMY:
                v = None
        else:
            if self.is_vectorvox:
                vx = None if np.isnan(v[0]) else v[0]
                vy = None if np.isnan(v[1]) else v[1]
                vz = None if np.isnan(v[2]) else v[2]
                v = (vx, vy, vz)
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
    def open(cls, name, gxapi_vox=None, dtype=None, mode=MODE_READ, depth=False):
        """
        Open an existing vox.

        :param name:        name of the vox. If a name only the vox is resolved from the
                            project. If a file name or complete path, the vox is resolved from
                            the file system outside of the current project.
        :param gxapi_vox:   `gxapi.GXVOX` instance to create from GXVOX instance.
        :param dtype:       working dtype for retrieving data.
        :param depth:       True to work with z as depth (positive down), origin at the top of the vox.
                            The default is False, z is elevation (positive up), origin at the bottom of the vox.
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
        vox = cls(name, gxapi_vox, dtype=dtype)

        if mode is None:
            mode = MODE_READ
        if mode == MODE_READ:
            vox._readonly = True
        else:
            vox._readonly = False
        vox.is_depth = depth

        return vox

    @classmethod
    def new(cls, name, data, temp=False, overwrite=False, dtype=None,
            origin=(0., 0., 0.), cell_size=None, coordinate_system=None, depth=False):
        """
        Create a new vox dataset

        :param name:        dataset name, or a path to a persistent file. A file with extension `.geosoft_voxel`
                            or `geosoft_vectorvoxel` will be created for vox instances that will persist (`temp=True`).
        :param data:        data to place in the vox, must have 3 dimensions (nz, ny, nx) for simple
                            scalar data, or (nx, ny, nz, 3) for vector data.f
        :param temp:        True to create a temporary vox which will be removed after use
        :param overwrite:   True to overwrite existing persistent vox
        :param dtype:       data type, default is the same as data, or np.float64 of no data.
        :param origin:      (x0, y0, z0) location of the origin vox point. Note that this is not the corner
                            of a cell. This is the center of the first cell for a uniform cell size, or the
                            reference position of the first vox cell accounting for variable cell sizes.
        :param cell_size:   uniform cell size, or (dx, dy, dz) cell sizes in the x, y and z directions. The
                            default is (1., 1., 1.). For variable cell size on a dimension, provide an array
                            of the cell sizes along that dimension. The array length must match the data dimension
                            along that axis. For example:
                            `cell_size=((1, 2.5, 1.5), (1, 1, 1, 1), (5, 4, 3, 2, 1))` will create a vox
                            with (x, y, z) dimension (3, 4, 5) and sizes as specified in each dimension.
        :param coordinate_system:   coordinate system as required to create from `geosoft.gxpy.Coordinate_system`
        :param depth:       True to work with z as depth (positive down). The default is False,
                            z is elevation (positive up)

        .. versionadded:: 9.3.1
        """

        if not isinstance(data, np.ndarray):
            data = np.array(data)
        vec_dim = 1
        if data.ndim == 4:
            if data.shape[3] != 3:
                raise VoxException(_t('Data appears to be vector data, but last dimension is not 3.'))
            if data.dtype != np.float32:
                data = np.array(data, dtype=np.float32)
            vec_dim = 3
        elif data.ndim != 3:
            raise VoxException(_t('Data must have 3 or 4 dimensions, this data has {} dimensions').format(data.ndim))

        if not temp:
            file_name = _vox_file_name(name, vectorvoxel=(vec_dim == 3))
            if not overwrite:
                if os.path.isfile(file_name):
                    raise VoxException(_t('Cannot overwrite existing vox {}'.format(file_name)))
        else:
            if vec_dim == 1:
                file_name = gx.GXpy().temp_file('.geosoft_voxel')
            else:
                file_name = gx.GXpy().temp_file('.geosoft_vectorvoxel')

        dimension = (data.shape[2], data.shape[1], data.shape[0])
        if dtype is None:
            dtype = data.dtype

        if cell_size is None:
            cell_size = (1., 1., 1.)
        elif isinstance(cell_size, int):
            cell_size = (cell_size, cell_size, cell_size)

        dvv = list(cell_size)
        for i in range(3):
            if hasattr(dvv[i], '__iter__'):
                dvv[i] = gxvv.GXvv(dvv[i], dtype=np.float64)
            else:
                dvv[i] = gxvv.GXvv(np.zeros((dimension[i],)) + dvv[i], dtype=np.float64)

        x0, y0, z0 = origin
        cx, cy, cz = dvv

        # dimensions must match
        if dimension != (cx.length, cy.length, cz.length):
            raise VoxException(_t('Vox dimension {} and variable_cell_size dimensions {} do not match'
                                  ).format(dimension, (cx.length, cy.length, cz.length)))

        if depth:
            z0, cz = elevation_from_depth(z0, cz)

        if dtype is None:
            dtype = np.float64

        pg = gxapi.GXPG.create_3d(cz.length, cy.length, cx.length, gxu.gx_dtype_dimension(dtype, vec_dim))
        vv = gxvv.GXvv(dtype=dtype, dim=vec_dim)
        vv.length = cx.length

        for s in range(cz.length):
            for iy in range(cy.length):
                vv.set_data(data[s, iy, :])
                if depth:
                    sz = cz.length - s - 1
                else:
                    sz = s

                pg.write_row_3d(sz, iy, 0, vv.length, vv.gxvv)

        gxvox = gxapi.GXVOX.generate_pgvv(file_name, pg,
                                          x0, y0, z0,
                                          cx.gxvv, cy.gxvv, cz.gxvv,
                                          gxcs.Coordinate_system(coordinate_system).gxipj,
                                          gxapi.GXMETA.create())

        vox = cls(name, gxvox)
        vox._file_name = file_name
        vox._readonly = False
        vox._delete_files = temp
        vox.is_depth = depth

        return vox

    @classmethod
    def copy(cls, name, source_vox, data=None, temp=False, overwrite=False, dtype=None):
        """
        Create a new vox dataset

        :param name:        dataset name, or a path to a persistent file. A file with extension `.geosoft_voxel`
                            will be created for vox instances that will persist (`temp=True`).
        :param source_vox:  `Vox` instance of the source vox
        :param data:        data to place in the vox, must have 3 dimensions (nz, ny, nx). If not
                            specified the vox is initialized to dummy values. Note that data arrays are indexed
                            (z, y, x). If not specified the data from the source_vox is copied.
        :param temp:        True to create a temporary vox which will be removed after use
        :param overwrite:   True to overwrite existing persistent vox
        :param dtype:       data type, default is the same as data, or np.float64 of no data.

        .. versionadded:: 9.3.1
        """

        if data is None:
            data = source_vox.np
        vox = Vox.new(name, data, overwrite=overwrite, temp=temp, dtype=dtype,
                      origin=(source_vox.origin_x, source_vox.origin_y, source_vox.origin_z,),
                      cell_size=(source_vox.cells_x, source_vox.cells_y, source_vox.cells_z),
                      coordinate_system=source_vox.coordinate_system,
                      depth=source_vox.is_depth)

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
    def is_vectorvox(self):
        """True if this is a vector voxel."""
        return bool(self.gxvox.is_vector_voxel())

    @property
    def dtype(self):
        """Working dtype for the data."""
        return self._dtype

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
        """constant X point separation, None if not constant, in which case use `cells_x`"""
        if self._uniform_cell_size[0] == gxapi.rDUMMY:
            return None
        return self._uniform_cell_size[0]

    @property
    def dy(self):
        """constant Y point separation, None if not constant, in which case use `cells_y`"""
        if self._uniform_cell_size[1] == gxapi.rDUMMY:
            return None
        return self._uniform_cell_size[1]

    @property
    def dz(self):
        """constant Z point separation, None if not constant, in which case use `cells_z`"""
        if self._uniform_cell_size[2] == gxapi.rDUMMY:
            return None
        return self._uniform_cell_size[2]

    @property
    def origin_x(self):
        """X location of the vox origin."""
        return self._origin[0]

    @property
    def origin_y(self):
        """Y location of the vox origin."""
        return self._origin[1]

    @property
    def origin_z(self):
        """Z location of the vox origin."""
        return self.locations_z[0]

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
        """ (min_x, min_y, min_z, max_x, max_y, max_z) extent to the outer-cell edges of the vox."""
        rx0 = gxapi.float_ref()
        ry0 = gxapi.float_ref()
        rz0 = gxapi.float_ref()
        rx1 = gxapi.float_ref()
        ry1 = gxapi.float_ref()
        rz1 = gxapi.float_ref()
        self.gxvox.get_area(rx0, ry0, rz0, rx1, ry1, rz1)
        if self.is_depth:
            return (rx0.value, ry0.value, -rz1.value,
                    rx1.value, ry1.value, -rz0.value)
        return (rx0.value, ry0.value, rz0.value,
                rx1.value, ry1.value, rz1.value)

    @property
    def extent_2d(self):
        """ Horizontal (min_x, min_y, max_x, max_y) extent to the outer-cell edges of the vox."""
        ex = self.extent
        return (ex[0], ex[1], ex[3], ex[4])

    @property
    def coordinate_system(self):
        """coordinate system as a `geosoft.gxpy.coordinate_system.Coordinate_system` instance. Can be set using
        any constructor supported by `geosoft.gxpy.coordinate_system.Coordinate_system`."""
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
        self._locations = (list(xvv.np), list(yvv.np), list(zvv.np))
        x0 = gxapi.float_ref()
        y0 = gxapi.float_ref()
        z0 = gxapi.float_ref()
        self.gxvox.get_location(x0, y0, z0, xvv.gxvv, yvv.gxvv, zvv.gxvv)
        self._origin = (x0.value, y0.value, z0.value)
        self._cells = (list(xvv.np), list(yvv.np), list(zvv.np))
        dx = gxapi.float_ref()
        dy = gxapi.float_ref()
        dz = gxapi.float_ref()
        self._gxvox.get_simple_location(x0, y0, z0, dx, dy, dz)
        self._uniform_cell_size = (dx.value, dy.value, dz.value)

    @property
    def locations_x(self):
        """Return array of X locations"""
        return self._locations[0]

    @property
    def locations_y(self):
        """Return array of Y locations"""
        return self._locations[1]

    @property
    def locations_z(self):
        """Return array of Z locations"""
        if self.is_depth:
            return [-z for z in reversed(self._locations[2])]
        return self._locations[2]

    @property
    def cells_x(self):
        """Return array of X cell sizes"""
        return self._cells[0]

    @property
    def cells_y(self):
        """Return array of Y cell sizes"""
        return self._cells[1]

    @property
    def cells_z(self):
        """Return array of Z cell sizes"""
        if self.is_depth:
            return list(reversed(self._cells[2]))
        return self._cells[2]

    @property
    def gxpg(self):
        """
        `geosoft.gxapi.GXPG` instance (3D) for this vox.

        The GXPG will always index z from minimum elevation (bootom of the vox).

        .. versionadded:: 9.3.1
        """

        if self._pg is None:
            self._pg = self.gxvox.create_pg()
        return self._pg

    @property
    def gxvoxe(self):
        """Return a `gxapi.GXVOXE` instance"""
        if self._gxvoxe is None:
            self._gxvoxe = gxapi.GXVOXE.create(self.gxvox)
        return self._gxvoxe

    @property
    def is_depth(self):
        """True if z is depth.  Can be set."""
        return self._is_depth

    @is_depth.setter
    def is_depth(self, b):
        self._is_depth = bool(b)

    @property
    def is_elevation(self):
        """True if z is elevation.  Can be set."""
        return not(self._is_depth)

    @is_elevation.setter
    def is_elevation(self, b):
        self._is_depth = not(bool(b))

    def _checkindex(self, ix, iy, iz):
        if (ix < 0) or (ix >= self.nx) or (iy < 0) or (iy >= self.ny) or (iz < 0) or (iz >= self.nz):
            raise IndexError(_t("Voxel index ({}, {}, {}) out of range ({}, {}, {}).").format(ix, iy, iz, self.nx, self.ny, self.nz))

    def xyz(self, ix, iy, iz):
        """
        Return the spatial location of a point in the vox.
        Raises error if our of range of the data

        :param ix:  x index
        :param iy:  y index
        :param iz:  z index, from bottom for elevation, from top for depth
        :return: (x, y, elevation) or (x, y, depth)

        .. versionadded:: 9.3
        """
        self._checkindex(ix, iy, iz)
        return (self.locations_x[ix], self.locations_y[iy], self.locations_z[iz])


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
        if self.is_depth:
            z = -z
        v = self.gxvoxe.value(x, y, z, interpolate)
        if v == gxapi.rDUMMY:
            return None
        return v

    def np(self, subset=None, dtype=None):
        """
        Return vox subset in a 3D numpy array.

        :param subset:  define a subset ((start_x, start_y, start_z),(nx, ny, nz)). If not specified
                        a numpy array of the entire voxset is returned. Missing items are calculated from the vox,
                        and negative indexes in start indicate a value from the last point.

                        start=(None, None) equivalent: start=((0, 0, 0), (nx, ny, nz))

                        start=((4, 6, 11), None) equivalent: start=((4, 6, 11), (nx - 4, ny - 6, nz - 11))

                        start=((4, 6, 11), (None, None, 1) equivalent: start=((4, 6, 11), (nx - 4, ny - 6, 1))

                        start=((0, 0, -1), None equivalent: start=((0, 0, nx - 1), (nx, ny, 1))

        :return:        numpy array of shape (nz, ny, nx). The order of z depends on is_depth property setting.

        .. versionadded:: 9.3.1
        """

        def set_0(n, nn):
            if n is None:
                return 0
            if n < 0:
                nr = nn + n
            else:
                nr = n
            if nr < 0 or nr >= nn:
                raise VoxException(_t("Invalid start ({}) for axis dimension ({})").format(n, nn))
            return nr

        def set_d(o, n, nn):
            if n is None:
                return nn - o
            return n

        if subset:
            start, dimension = subset
        else:
            start = (0, 0, 0)
            dimension = None

        # start
        if start is None:
            x0 = y0 = z0 = 0
        else:
            x0, y0, z0 = start
            x0 = set_0(x0, self.nx)
            y0 = set_0(y0, self.ny)
            z0 = set_0(z0, self.nz)

        # dimensions
        if dimension is None:
            nx = self.nx - x0
            ny = self.ny - y0
            nz = self.nz - z0
        else:
            nx, ny, nz = dimension
            nx = set_d(x0, nx, self.nx)
            ny = set_d(y0, ny, self.ny)
            nz = set_d(z0, nz, self.nz)

        gxpg = self.gxpg
        if dtype is None:
            dtype = self._dtype
        if self.is_vectorvox:
            shape = (nz, ny, nx, 3)
            dim = 3
        else:
            shape = (nz, ny, nx)
            dim = 1
        npv = np.empty(shape, dtype=dtype)
        vv = gxvv.GXvv(dtype=dtype, dim=dim)
        vv.length = nx

        if self.is_depth:
            z0 = self.nz - (z0 + nz)
            i = 1
            for iz in range(z0, z0 + nz):
                for iy in range(y0, y0 + ny):
                    gxpg.read_row_3d(iz, iy, x0, nx, vv.gxvv)
                    npv[nz - i, iy - y0, :] = vv.np
                i += 1

        else:
            for iz in range(z0, z0 + nz):
                for iy in range(y0, y0 + ny):
                    gxpg.read_row_3d(iz, iy, x0, nx, vv.gxvv)
                    npv[iz - z0, iy - y0, :] = vv.np

        return npv
