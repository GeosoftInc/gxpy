"""
Spatial geometric elements.

:Classes:

    ========== ==============================================================
    `Geometry` base class for all geometries
    `Point`    (x, y, z) point
    `Point2`   pair of :class:`Point` instances that define a line, or extent
    `PPoint`   multiple :class:`Point` instances
    `Mesh`     mesh surface made up of triangular faces defined by verticies
    ========== ==============================================================

.. note::

    Regression tests provide usage examples: 
    `geometry tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_geometry.py>`_

"""
import numpy as np
from collections.abc import Sequence

import geosoft
import geosoft.gxapi as gxapi
from . import coordinate_system as gxcs
from . import vv as gxvv

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class GeometryException(Exception):
    """
    Exceptions from :mod:`geosoft.gxpy.geometry`.
    """
    pass


class Geometry:
    """
    Geometry base class for all geometries.

    :param coordinate_system:   `geosoft.gxpy.coordinate_system.Coordinate_system` instance.
    :param name:                instance name string
    :param gxobj:               optional gxapi instance that can satisfy get_ipj() and/or get_extent()

    .. versionadded:: 9.2
    """

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        pass

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __init__(self, coordinate_system=None, name='_geometry_', gxobj=None):
        self._cs = coordinate_system
        self._name = name
        self._gxobj = gxobj

    def __eq__(self, other):
        if self._cs != other.coordinate_system:
            return False
        if self._gxobj != other.gxobj:
            return False
        return True

    @property
    def coordinate_system(self):
        """`geosoft.gxpy.coordinate_system.Coordinate_system` instance or None.  Can be set."""
        if self._cs and not isinstance(self._cs, gxcs.Coordinate_system):
            self._cs = gxcs.Coordinate_system(self._cs)
        return self._cs

    @coordinate_system.setter
    def coordinate_system(self, cs):
        self._cs = cs

    @property
    def gxobj(self):
        """the associated gxapi object, or None"""
        return self._gxobj

    @property
    def name(self):
        """spatial object name"""
        return self._name

    @property
    def extent(self):
        """ minimum `Point`, maximum `Point`."""
        if self._gxobj and hasattr(self._gxobj, 'get_extents'):
            rx0 = gxapi.float_ref()
            ry0 = gxapi.float_ref()
            rz0 = gxapi.float_ref()
            rx1 = gxapi.float_ref()
            ry1 = gxapi.float_ref()
            rz1 = gxapi.float_ref()
            self._gxobj.get_extents(rx0, ry0, rz0, rx1, ry1, rz1)
            cs = self.coordinate_system
            return Point((rx0.value, ry0.value, rz0.value), cs), Point((rx1.value, ry1.value, rz1.value), cs)
        else:
            return None, None

    @property
    def extent_xyz(self):
        """return extent as a tuple (xmin, ymin, zmin, xmax, ymax, zmax)"""
        p1, p2 = self.extent
        return p1.x, p1.y, p1.z, p2.x, p2.y, p2.z

    @property
    def extent_xy(self):
        """ Horizontal minimum Point, maximum Point"""
        p1, p2 = self.extent
        return p1.x, p1.y, p2.x, p2.y

    @property
    def extent_minimum(self):
        """ minimum geometry extent as tuble (min_x, min_y, min_z)"""
        p, _ = self.extent
        return p.x, p.y, p.z

    @property
    def extent_maximum(self):
        """ maximum geometry extent as tuple (max_x, max_y, max_z)"""
        _, p = self.extent
        return p.x, p.y, p.z

    @property
    def extent_minimum_xy(self):
        """ minimum geometry extent as tuple (min_x, min_y)"""
        p, _ = self.extent
        return p.x, p.y

    @property
    def extent_maximum_xy(self):
        """ maximum geometry extent as tuple (max_x, max_y)"""
        _, p = self.extent
        return p.x, p.y, p.z

    @property
    def centroid(self):
        """ centroid of the geometry"""
        p1, p2 = self.extent
        cx = (p1.x + p2.x) * 0.5
        cy = (p1.y + p2.y) * 0.5
        cz = (p1.z + p2.z) * 0.5
        return Point((cx, cy, cz), p1.coordinate_system)

    @property
    def dimension(self):
        """ dimensions as (dx, dy, dz)"""
        p1, p2 = self.extent
        dx = abs(p2.x - p1.x)
        dy = abs(p2.y - p1.y)
        dz = abs(p2.z - p1.z)
        return dx, dy, dz

    @property
    def centroid_xy(self):
        """ centroid of the geometry"""
        c = self.centroid
        return Point((c.x, c.y), c.coordinate_system)

    @property
    def dimension_xy(self):
        """ dimensions as (dx, dy, dz)"""
        dx, dy, _ = self.dimension
        return dx, dy

    def copy(self, name=None):
        """return an exact copy of the geometry"""
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        if name:
            result.__dict__['_name'] = name
        return result

    def copy_cs(self, coordinate_system):
        if self.coordinate_system == coordinate_system:
            return self
        return self.copy(coordinate_system)


class Point(Geometry):
    """
    Spatial location (x,y,z).  Basic instance arithmetic and equality testing is supported.

    :param p:   point in one of the following forms:

                    `Point` instance, returns a copy

                    (x, y [,z]) implied z is 0.0 if not provided

                    k makes a point (k, k, k)

    :param coordinate_system:   coordinate system or None
    :param **kwargs:            passed to base class `Geometry`

    .. versionadded:: 9.2

    .. versionchanged:: 9.3.1 added coordinate_system parameter
    """

    def __str__(self):
        return "({}, {}, {})".format(self.x(), self.y(), self.z())

    def __init__(self, p, coordinate_system=None, **kwargs):

        if 'name' not in kwargs:
            kwargs['name'] = '_point_'
        super().__init__(coordinate_system=coordinate_system, **kwargs)

        if hasattr(p, "__len__"):
            if len(p) > 2:
                self.p = np.array(p[:3], dtype=float)
            elif len(p) == 2:
                self.p = np.array((p[0], p[1], 0.0))
            else:
                self.p = np.array((p[0], p[0], p[0]), dtype=float)
        else:
            if isinstance(p, Point):
                if not self.coordinate_system == coordinate_system:
                    self.p = p.copy(coordinate_system).p
                else:
                    self.p = p.p.copy()
            else:
                self.p = np.array((p, p, p))

    def __add__(self, p):
        if not isinstance(p, Point):
            p = Point(p)
        else:
            p = p.copy_cs(self.coordinate_system)
        return Point(self.p + p.p, self.coordinate_system)

    def __sub__(self, p):
        if not isinstance(p, Point):
            p = Point(p)
        else:
            p = p.copy_cs(self.coordinate_system)
        return Point(self.p - p.p, self.coordinate_system)

    def __neg__(self):
        return Point(-self.p, coordinate_system=self.coordinate_system)

    def __mul__(self, p):
        if not isinstance(p, Point):
            p = Point(p)
        else:
            p = p.copy_cs(self.coordinate_system)
        return Point(self.p * p.p, self.coordinate_system)

    def __truediv__(self, p):
        if not isinstance(p, Point):
            p = Point(p)
        else:
            p = p.copy_cs(self.coordinate_system)
        return Point(self.p / p.p, self.coordinate_system)

    def __eq__(self, other):
        if not super(Point).__eq__(other):
            return False
        return np.array_equal(self.p, other.p)

    @property
    def x(self):
        """ x value, can be set"""
        return self.p[0]

    @x.setter
    def x(self, value):
        self.p[0] = float(value)

    @property
    def y(self):
        """ y value, can be set"""
        return self.p[1]

    @y.setter
    def y(self, value):
        self.p[1] = float(value)

    @property
    def z(self):
        """ z value, can be set"""
        return self.p[2]

    @z.setter
    def z(self, value):
        self.p[2] = float(value)

    @property
    def xy(self):
        """ (x, y), can be set"""
        return self.p[0], self.p[1]

    @xy.setter
    def xy(self, xy):
        self.p[0] = float(xy[0])
        self.p[1] = float(xy[1])

    @property
    def xyz(self):
        """ (x, y, z), can be set"""
        return self.p[0], self.p[1], self.p[2]

    @xyz.setter
    def xyz(self, xyz):
        self.p[0] = float(xyz[0])
        self.p[1] = float(xyz[1])
        self.p[2] = float(xyz[2])

    def copy(self, coordinate_system=None, name=None):
        """ return a copy as a :class:`Point` instance"""
        if coordinate_system and self.coordinate_system != coordinate_system:
            if not isinstance(coordinate_system, gxcs.Coordinate_system):
                coordinate_system = gxcs.Coordinate_system(coordinate_system)
            return Point(gxcs.Coordinate_translate(self.coordinate_system, coordinate_system).convert(self.p),
                         coordinate_system=coordinate_system, name=name)
        return super(Point, self).copy(name)

    def extent(self):
        return self.p, self.p


class Point2(Geometry):
    """
    Two points, for a line, or a rectangle, or a cube.  Basic instance arithmetic and equality testing is supported.

    :param p: Points in one of the following forms:

                (`Point`, `Point`)

                ((x, y [,z]), (x, y [,z])) implied z is 0 if not specified

                (x0, y0, x1, y1) implied z is 0

                (x0, y0, z0, x1, y1, z1)

    :param coordinate_system:   coordinate system or None
    :param **kwargs:            passed to base class `Geometry`

    .. versionadded:: 9.2

    .. versionchanged:: 9.3.1 added coordinate_system parameter
    """

    def __str__(self):
        return "Point2[({}, {}, {}) ({}, {}, {})]".format(self.p0.x, self.p0.y, self.p0.z,
                                                          self.p1.x, self.p1.y, self.p1.z)

    def __init__(self, p, coordinate_system=None, **kwargs):

        if 'name' not in kwargs:
            kwargs['name'] = '_point2_'
        super().__init__(coordinate_system=coordinate_system, **kwargs)
        kwargs.pop('name')
        if coordinate_system:
            kwargs['coordinate_system'] = gxcs.Coordinate_system(coordinate_system)
        if not hasattr(p, '__iter__'):
            self.p0 = self.p1 = Point(p, **kwargs)
        if len(p) == 2:
            self.p0 = Point(p[0], **kwargs)
            self.p1 = Point(p[1], **kwargs)
        elif len(p) == 4:
            self.p0 = Point((p[0], p[1]), **kwargs)
            self.p1 = Point((p[2], p[3]), **kwargs)
        elif len(p) == 6:
            self.p0 = Point((p[0], p[1], p[2]), **kwargs)
            self.p1 = Point((p[3], p[4], p[5]), **kwargs)
        else:
            raise GeometryException(_t('Invalid points: {}').format(p))

    def __eq__(self, other):
        if not super(Point2, self).__eq__(other):
            return False
        return (self.p0 == other.p0) and (self.p1 == other.p1) or (self.p0 == other.p1) and (self.p1 == other.p0)

    def __add__(self, p):
        if isinstance(p, Point2):
            p = p.copy_cs(self.coordinate_system)
            return Point2((self.p0 + p.p0, self.p1 + p.p1), coordinate_system=self.coordinate_system)
        if not isinstance(p, Point):
            p = Point(p)
        else:
            p = p.copy_cs(self.coordinate_system)
        return Point2((self.p0 + p, self.p1 + p), coordinate_system=self.coordinate_system)

    def __sub__(self, p):
        if isinstance(p, Point2):
            p = p.copy_cs(self.coordinate_system)
            return Point2((self.p0 - p.p0, self.p1 - p.p1), coordinate_system=self.coordinate_system)
        if not isinstance(p, Point):
            p = Point(p)
        else:
            p = p.copy_cs(self.coordinate_system)
        return Point2((self.p0 - p, self.p1 - p), coordinate_system=self.coordinate_system)

    def __neg__(self):
        return Point2((-self.p0, -self.p1), coordinate_system=self.coordinate_system)

    def __mul__(self, p):
        if isinstance(p, Point2):
            p = p.copy_cs(self.coordinate_system)
            return Point2((self.p0 * p.p0, self.p1 * p.p1), coordinate_system=self.coordinate_system)
        if not isinstance(p, Point):
            p = Point(p)
        else:
            p = p.copy_cs(self.coordinate_system)
        return Point2((self.p0 * p, self.p1 * p), coordinate_system=self.coordinate_system)

    def __truediv__(self, p):
        if isinstance(p, Point2):
            p = p.copy_cs(self.coordinate_system)
            return Point2((self.p0 / p.p0, self.p1 / p.p1), coordinate_system=self.coordinate_system)
        if not isinstance(p, Point):
            p = Point(p)
        else:
            p = p.copy_cs(self.coordinate_system)
        return Point2((self.p0 / p, self.p1 / p), coordinate_system=self.coordinate_system)

    def copy(self, coordinate_system=None, name=None):
        """return a copy as a :class:`Point2` instance"""
        if coordinate_system and self.coordinate_system != coordinate_system:
            if not isinstance(coordinate_system, gxcs.Coordinate_system):
                coordinate_system = gxcs.Coordinate_system(coordinate_system)
            t = gxcs.Coordinate_translate(self.coordinate_system, coordinate_system)
            return Point2((t.convert(self.p0.p), t.convert(self.p1.p)),
                          coordinate_system=coordinate_system, name=name)
        return super(Point2, self).copy(name)

    @property
    def x2(self):
        """(x0, x1), can be set"""
        return self.p0.x, self.p1.x

    @x2.setter
    def x2(self, value):
        self.p0.x = value[0]
        self.p1.x = value[1]

    @property
    def y2(self):
        """ (y0, y1), can be set"""
        return self.p0.y, self.p1.y

    @y2.setter
    def y2(self, value):
        self.p0.y = value[0]
        self.p1.y = value[1]

    @property
    def z2(self):
        """ (z0, z1), can be set"""
        return self.p0.z, self.p1.z

    @z2.setter
    def z2(self, value):
        self.p0.z = value[0]
        self.p1.z = value[1]

    @property
    def extent(self):
        """Extent as (xmin, ymin, zmin, xmax, ymax, zmax)"""
        p1 = Point((min(self.p0.x, self.p1.x), min(self.p0.y, self.p1.y), min(self.p0.z, self.p1.z)),
                   self.coordinate_system)
        p2 = Point((max(self.p0.x, self.p1.x), max(self.p0.y, self.p1.y), max(self.p0.z, self.p1.z)),
                   self.coordinate_system)
        return p1, p2


class PPoint(Geometry, Sequence):
    """
    Poly-Point class. Basic instance arithmetic and equality testing is supported.

    :param xyz:     array-like: (p1, p2, ...), ((x, y), ...), ((x, y, z), ...) or (vv_x, vv_y, [vv_z]).
                    vv data is resampled to match the first vv.

    :param coordinate_system:   coordinate system or None
    :param z:                   constant z value for (x, y) data, ignored for (x, y, z) data
    :param **kwargs:            passed to base class `Geometry`

    .. versionadded:: 9.2

    .. versionchanged:: 9.3.1 added coordinate_system parameter

    """

    def __init__(self, xyz, coordinate_system=None, z=0.0, **kwargs):

        if 'name' not in kwargs:
            kwargs['name'] = '_ppoint_'
        super().__init__(coordinate_system=coordinate_system, **kwargs)
        kwargs.pop('name')
        if coordinate_system:
            kwargs['coordinate_system'] = gxcs.Coordinate_system(coordinate_system)

        def blankpp(length):
            return np.zeros(length * 3, dtype=np.float).reshape((length, 3))

        def np_setup(npxyz):
            pp = blankpp(npxyz.shape[0])
            pp[:, 0] = npxyz[:, 0]
            pp[:, 1] = npxyz[:, 1]
            if npxyz.shape[1] > 2:
                pp[:, 2] = npxyz[:, 2]
            else:
                pp[:, 2] = z
            return pp

        def vv_setup():
            pp = blankpp(xyz[0].length)
            pp[:, 0] = xyz[0].get_data()[0][:]
            xyz[1].refid(xyz[0].fid, pp.shape[0])
            pp[:, 1] = xyz[1].get_data()[0][:]
            if len(xyz) > 2:
                xyz[2].refid(xyz[0].fid, pp.shape[0])
                pp[:, 2] = xyz[2].get_data()[0][:]
            else:
                pp[:, 2] = z
            return pp

        def point_setup():
            pp = blankpp(len(xyz))
            i = 0
            for p in xyz:
                pp[i, :] = p.xyz
                i += 1
            return pp

        if isinstance(xyz, np.ndarray):
            self.pp = np_setup(xyz)
        elif isinstance(xyz[0], gxvv.GXvv):
            self.pp = vv_setup()
        elif isinstance(xyz[0], Point):
            self.pp = point_setup()
        else:
            self.pp = np_setup(np.array(xyz))

        self._next = 0

    @classmethod
    def from_list(cls, xyzlist, z=0.0):
        """
        .. deprecated:: 9.3 `PPoint` can create directly from a list
        """
        return cls(np.array(xyzlist, dtype=np.float), z)

    def __len__(self):
        return self.pp.shape[0]

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= self.pp.shape[0]:
            self._next = 0
            raise StopIteration
        else:
            self._next += 1
            return Point(self.pp[self._next - 1], self.coordinate_system)

    def __getitem__(self, item):
        return Point(self.pp[item], self.coordinate_system)

    def __add__(self, p):
        if isinstance(p, PPoint):
            return PPoint(self.pp + p.pp)
        if isinstance(p, Point):
            return PPoint(self.pp + p.p)
        return PPoint(self.pp + Point(p).p)

    def __sub__(self, p):
        if isinstance(p, PPoint):
            return PPoint(self.pp - p.pp)
        if isinstance(p, Point):
            return PPoint(self.pp - p.p)
        return PPoint(self.pp - Point(p).p)

    def __neg__(self):
        return PPoint(self.pp * -1.0)

    def __mul__(self, p):
        if isinstance(p, PPoint):
            return PPoint(self.pp * p.pp)
        if isinstance(p, Point):
            return PPoint(self.pp * p.p)
        return PPoint(self.pp * Point(p).p)

    def __truediv__(self, p):
        if isinstance(p, PPoint):
            return PPoint(self.pp / p.pp)
        if isinstance(p, Point):
            return PPoint(self.pp / p.p)
        return PPoint(self.pp / Point(p).p)

    def __eq__(self, other):
        if not super(PPoint, self).__eq__(other):
            return False
        return np.array_equal(self.pp, other.pp)

    def copy(self, coordinate_system=None, name=None):
        """return a copy as a :class:`PPoint` instance"""
        if coordinate_system and self.coordinate_system != coordinate_system:
            if not isinstance(coordinate_system, gxcs.Coordinate_system):
                coordinate_system = gxcs.Coordinate_system(coordinate_system)
            t = gxcs.Coordinate_translate(self.coordinate_system, coordinate_system)
            return PPoint(t.convert(self.pp), coordinate_system=coordinate_system, name=name)
        return super(PPoint, self).copy(name=name)

    @property
    def length(self):
        """number of points"""
        return self.__len__()

    @property
    def x(self):
        """ x array slice, can be set"""
        return self.pp[:, 0]

    @x.setter
    def x(self, v):
        self.pp[:, 0] = v

    @property
    def y(self):
        """ y array slice, can be set"""
        return self.pp[:, 1]

    @y.setter
    def y(self, v):
        self.pp[:, 1] = v

    @property
    def z(self):
        """ z array slice, can be set"""
        return self.pp[:, 2]

    @z.setter
    def z(self, v):
        self.pp[:, 2] = v

    @property
    def xy(self):
        """ (x, y) array slice, can be set"""
        return self.pp[:, 0:2]

    @xy.setter
    def xy(self, v):
        self.pp[:, 0:2] = v

    @property
    def xyz(self):
        """ xyz point array"""
        return self.pp

    def extent(self):
        """
        Volume extent as (`Point`, `Point`) for (min, max).

        .. versionadded:: 9.2
        """
        p1 = Point((np.amin(self.x), np.amin(self.y), np.amin(self.z)), self.coordinate_system)
        p2 = Point((np.amax(self.x), np.amax(self.y), np.amax(self.z)), self.coordinate_system)
        return p1, p2

    def make_xyz_vv(self):
        """
        Return x, y and z as a set of :class:`geosoft.gxpy.vv.GXvv`.
        
        :returns: (xvv, yvv, zvv)
        
        .. versionadded:: 9.2
        """

        return gxvv.GXvv(self.x), gxvv.GXvv(self.y), gxvv.GXvv(self.z)
