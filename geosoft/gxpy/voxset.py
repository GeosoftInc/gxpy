"""
Geosoft voxset/voxel handling.

:Classes:

    ============= ====================================================
    :class:`Voxset` voxset, which can be in memory or created from a file _
    ============= ====================================================

.. seealso:: :class:`geosoft.gxapi.GXIMG`, :class:`geosoft.gxapi.GXIMU`

.. note::

    Regression tests provide usage examples:     
    `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_voxset.py>`_
    
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

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class VoxsetException(Exception):
    """
    Exceptions from :mod:`geosoft.gxpy.voxset`.

    .. versionadded:: 9.1
    """
    pass

def _voxset_file_name(name):
    ext = os.path.splitext(name)[1]
    if ext.lower() != '.geosoft_voxel':
        name = name + '.geosoft_voxel'
    return os.path.relpath(name)

def _voxset_name(name):
    basename = os.path.basename(name)
    return os.path.splitext(basename)[0]

INTERP_NEAREST = gxapi.VOXE_EVAL_NEAR #:
INTERP_LINEAR = gxapi.VOXE_EVAL_INTERP #:
INTERP_SMOOTH = gxapi.VOXE_EVAL_BEST #:

def delete_files(voxset_name):
    """
    Delete all files associates with this voxset name.

    :param voxset_name: name of the voxset file

    .. versionadded:: 9.3
    """

    def df(fn):
        try:
            os.remove(fn)
        except OSError as e:
            pass

    if voxset_name is not None:

        df(voxset_name)
        df(voxset_name + '.xml')


# constants
MODE_READ = 0          #:
MODE_READWRITE = 1     #: file exists, but can change properties
MODE_NEW = 2           #:


class Voxset:
    """
    Voxset and image class.

    :Constructors:

        ======================= ============================================
        :meth:`open`            open an existing voxset
        :meth:`new`             create a new voxset
        :meth:`from_data_array` create a new voxset from a 2d data array
        ======================= ============================================

    A voxset instance supports iteration that yields (x, y, z, voxset_value) by points along horizontal
    rows, then columns, then depth slices starting at minimum z.
    For example, the following prints the x, y, z, voxset_value of every non-dummy point in a voxset:

    .. code::

        import geosoft.gxpy.voxset as gxvox

        with gxvox.Voxset.open('some.geosoft_voxel') ad g:
            for x, y, z, v in g:
                if v is not None:
                    print(x, y, z, v)

    Specific voxset cell values can be indexed (null voxset values are None):

    .. code::

        import geosoft.gxpy.voxset as gxvox

        with gxvox.Voxset.open('some_voxel') as vox:
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

        def df(fn):
            try:
                os.remove(fn)
            except OSError as e:
                pass

        if hasattr(self, '_open'):
            if self._open:

                if self._metadata_changed:
                    with open(self._file_name + '.xml', 'w+') as f:
                        f.write(gxu.xml_from_dict(self._metadata))

                if pop:
                    gx.pop_resource(self._open)
                self._open = None
                self._gxvoxe = None
                self._gxvox = None
                self._cs = None
                self._pg_ = None
                self._vv_ = None

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self.name

    def __init__(self, name=None, gxvox=None):

        self._file_name = _voxset_file_name(name)
        self._name = _voxset_name(self._file_name)
        self._readonly = None
        self._metadata = None
        self._metadata_changed = False
        self._metadata_root = ''
        self._gxvox = gxvox
        self._cs = None
        self._gxvoxe = None
        self._next = self._next_x = self._next_y = self._next_z = 0
        self._xloc = self._yloc = self._zloc = None
        self._pg = self._vv_ = None
        self._buffered_plane = self._buffered_row = None
        self._metadata = None
        self._metadata_changed = False
        self._metadata_root = ''

        ityp = gxapi.int_ref()
        iarr = gxapi.int_ref()
        nx = gxapi.int_ref()
        ny = gxapi.int_ref()
        nz = gxapi.int_ref()
        self._gxvox.get_info(ityp, iarr, nx, ny, nz)
        self._dtype = gxu.dtype_gx(ityp.value)
        self._is_int = gxu.is_int(ityp.value)
        self._nx = nx.value
        self._ny = ny.value
        self._nz = nz.value
        self._max_iter = self._nx * self._ny * self._nz

        # location
        x0 = gxapi.float_ref()
        y0 = gxapi.float_ref()
        z0 = gxapi.float_ref()
        dx = gxapi.float_ref()
        dy = gxapi.float_ref()
        dz = gxapi.float_ref()
        self._gxvox.get_simple_location(x0, y0, z0, dx, dy, dz)
        self._x0 = x0.value
        self._y0 = y0.value
        self._z0 = z0.value
        self._dx = dx.value
        self._dy = dy.value
        self._dz = dz.value

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
            vv = self._vv
            self.gxpg.read_row_3d(iz, iy, 0, self._nx, vv.gxvv)
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
        Return the voxset metadata as a dictionary.  Can be set, in which case
        the dictionary items passed will be added to, or replace existing metadata.

        .. seealso::
            `Geosoft metadata schema
            <https://geosoftgxdev.atlassian.net/wiki/spaces/GXD93/pages/78184638/Geosoft+Metadata+Schema>'


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
    def open(cls, name, mode=MODE_READ):
        """
        Open an existing voxset file.

        :param name:        name of the voxset
        :param mode:        open mode:

            =================  ==================================================
            MODE_READ          only read the voxset, properties cannot be changed
            MODE_READWRITE     voxset stays the same, but properties may change
            =================  ==================================================

        .. versionadded:: 9.3
        """

        vox = cls(name, gxapi.GXVOX.create(_voxset_file_name(name)))

        if mode is None:
            mode = MODE_READ
        if mode == MODE_READ:
            vox._readonly = True
        else:
            vox._readonly = False

        return vox

    def close(self):
        """close the voxset and release all instance resources."""
        self._close()

    @property
    def name(self):
        """Voxset name"""
        return self._name

    @property
    def file_name(self):
        """Voxset file name"""
        return self._file_name

    @property
    def gxvox(self):
        """`gxapi.GXVOX` instance handle"""
        return self._gxvox

    @property
    def nx(self):
        """ number of points in voxel X direction"""
        return self._nx

    @property
    def ny(self):
        """ number of points in voxel Y direction"""
        return self._ny

    @property
    def nz(self):
        """ number of points in voxel Z direction"""
        return self._nz

    @property
    def dx(self):
        """constant X point separation, None if not constant"""
        if self._dx == gxapi.rDUMMY:
            return None
        return self._dx

    @property
    def dy(self):
        """constant Y point separation, None if not constant"""
        if self._dy == gxapi.rDUMMY:
            return None
        return self._dx

    @property
    def dz(self):
        """constant Z point separation, None if not constant"""
        if self._dz == gxapi.rDUMMY:
            return None
        return self._dz

    @property
    def x0(self):
        """X location of the voxset origin."""
        return self._x0

    @property
    def y0(self):
        """Y location of the voxset origin."""
        return self._y0

    @property
    def z0(self):
        """Z location of the voxset origin."""
        return self._z0

    @property
    def uniform_dx(self):
        """True if X point separation is constant"""
        return (self.dx != gxapi.rDUMMY)

    @property
    def uniform_dy(self):
        """True if Y point separation is constant"""
        return (self.dy != gxapi.rDUMMY)

    @property
    def uniform_dz(self):
        """True if Z point separation is constant"""
        return (self.dz != gxapi.rDUMMY)

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
        if self._cs is None:
            ipj = gxapi.GXIPJ.create()
            self.gxvox.get_ipj(ipj)
            self._cs = gxcs.Coordinate_system(ipj)
        return self._cs

    @coordinate_system.setter
    def coordinate_system(self, cs):
        self._cs = gxcs.Coordinate_system(cs)
        self.gxvox.set_ipj(self._cs.gxipj)

    def _location_arrays(self):
        xvv = gxvv.GXvv()
        yvv = gxvv.GXvv()
        zvv = gxvv.GXvv()
        self.gxvox.get_location_points(xvv.gxvv, yvv.gxvv, zvv.gxvv)
        self._xloc = xvv.np.copy()
        self._yloc = yvv.np.copy()
        self._zloc = zvv.np.copy()

    @property
    def x_locations(self):
        """Return array of X locations"""
        if self._xloc is None:
            self._location_arrays()
        return self._xloc

    @property
    def y_locations(self):
        """Return array of X locations"""
        if self._yloc is None:
            self._location_arrays()
        return self._yloc

    @property
    def z_locations(self):
        """Return array of X locations"""
        if self._zloc is None:
            self._location_arrays()
        return self._zloc

    @property
    def gxpg(self):
        if self._pg is None:
            self._pg = self.gxvox.create_pg()
        return self._pg

    @property
    def _vv(self):
        if self._vv_ is None:
            self._vv_ = gxvv.GXvv(dtype=self._dtype)
        return self._vv_

    @property
    def gxvoxe(self):
        """Return a `gxapi.GXVOXE` instance"""
        if self._gxvoxe is None:
            self._gxvoxe = gxapi.GXVOXE.create(self.gxvox)
        return self._gxvoxe

    def _release_pg(self):
        self._pg_ = None

    def _checkindex(self, ix, iy, iz):
        if (ix < 0) or (ix >= self.nx) or (iy < 0) or (iy >= self.ny) or (iz < 0) or (iz >= self.nz):
            raise IndexError(_t("Voxel index ({}, {}, {}) out of range ({}, {}, {}).").format(ix, iy, iz, self.nx, self.ny, self.nz))

    def xyz(self, ix, iy, iz):
        """
        Return the spatial location of a point in the voxset.
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

        :param xyz:         tuple (x, y, z) location in the voxel coordinate system
        :param interpolate: method by which to interpolate between points:

                            INTERP_NEAREST - same as value inside a cell.

                            INTERP_LINEAR - linear interpolation between neighboring points.

                            INTERP_SMOOTH - smooth interpolation (slower than INTERP_LINEAR).

        :returns:           voxel value at that location

        .. versionadded:: 9.3.1
        """
        x, y, z = xyz
        v = self.gxvoxe.value(x, y, z, interpolate)
        if v == gxapi.rDUMMY:
            return None
        return v

    def np_subset(self, start=(0, 0, 0), dimension=None):
        """
        Return voxset subset in a 3D numpy array.

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
            raise VoxsetException(_t("Subset dimension {} invalid, require positive non-zero dimension").format((nx, ny, nz)))

        gxpg = self.gxpg
        npv = np.empty((nz, ny, nx), dtype=self._dtype)
        vv = gxvv.GXvv(dtype=self._dtype)
        vv.length = nx

        for iz in range(z0, z0 + nz):
            for iy in range(y0, y0 + ny):
                gxpg.read_row_3d(iz, iy, x0, nx, vv.gxvv)
                npv[iz - z0, iy - y0, :] = vv.np

        return npv
