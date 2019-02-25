"""
Spatial geometric objects.

:Classes:
    :`Geometry`: base class for all geometries
    :`Point`:    (x, y, z) point
    :`Point2`:   pair of `Point` instances that define a line, or box, etc.
    :`PPoint`:   multiple `Point` instances
    :`Mesh`:     mesh surface made up of triangular faces defined by verticies

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

def _geo_cs(g, geo_class, coordinate_system, **kwargs):
    if hasattr(g, 'coordinate_system') and g.coordinate_system == coordinate_system:
        return g
    return geo_class(g, coordinate_system, **kwargs)

def first_coordinate_system(geo_objects):
    """
    Return the first found known coordinate system in the list

    :param geo_objects: objects as iterable
    :return:            valid coordinate system or `None` if none found

    .. versionadded:: 9.3.1
    """
    for o in geo_objects:
        if hasattr(o, 'coordinate_system'):
            if gxcs.is_known(o.coordinate_system):
                return o.coordinate_system
    return None


class GeometryException(geosoft.GXRuntimeError):
    """
    Exceptions from :mod:`geosoft.gxpy.geometry`.
    """
    pass


def extent_union(g1, g2):
    """
    Return the spatial union of two spatial objects.

    :param g1:  extent (p0 < p1), returned extent will be in this coordinate system
    :param g2:  second object

    :return:    `Point2` instance in the coordinate system of g1

    .. versionadded:: 9.3.1
    """

    def ext(g):
        if g is None or isinstance(g, Point2):
            return g
        if isinstance(g, Geometry):
            return g.extent
        return Point2(g).extent

    g1 = ext(g1)
    g2 = ext(g2)
    if g1 is None:
        return g2
    if g2 is None:
        return g1

    g2p0x, g2p0y, g2p0z = g2.p0.xyz
    g2p1x, g2p1y, g2p1z = g2.p1.xyz
    if g1.coordinate_system != g2.coordinate_system:
        corners = np.array([(g2p0x, g2p0y, g2p0z),
                            (g2p0x, g2p1y, g2p0z),
                            (g2p1x, g2p1y, g2p0z),
                            (g2p1x, g2p0y, g2p0z),
                            (g2p0x, g2p0y, g2p1z),
                            (g2p0x, g2p1y, g2p1z),
                            (g2p1x, g2p1y, g2p1z),
                            (g2p1x, g2p0y, g2p1z)], dtype=np.float64)
        ex = PPoint(PPoint(corners, g2.coordinate_system), g1.coordinate_system).extent
        return extent_union(g1, ex)

    g1p0x, g1p0y, g1p0z = g1.p0.xyz
    g1p1x, g1p1y, g1p1z = g1.p1.xyz
    if g2p0x >= g1p0x and g2p0y >= g1p0y and g2p0z >= g1p0z and\
            g2p1x <= g1p1x and g2p1y <= g1p1y and g2p1z <= g1p1z:
        return g1

    min_x = g1p0x if g1p0x < g2p0x else g2p0x
    min_y = g1p0y if g1p0y < g2p0y else g2p0y
    min_z = g1p0z if g1p0z < g2p0z else g2p0z
    max_x = g1p1x if g1p1x > g2p1x else g2p1x
    max_y = g1p1y if g1p1y > g2p1y else g2p1y
    max_z = g1p1x if g1p1z > g2p1z else g2p1z
    return Point2(((min_x, min_y, min_z), (max_x, max_y, max_z)), g1.coordinate_system)


class Geometry:
    """
    Geometry base class for all geometries and spatial objects in Geosoft.

    :param coordinate_system:   `geosoft.gxpy.coordinate_system.Coordinate_system` instance.
    :param name:                instance name string
    :param gxobj:               optional gxapi instance that can satisfy get_ipj() and/or get_extent()

    :Properties:
        :`Geometry.name`:                 name for the geometry
        :`Geometry.coordinate_system`:    spatial coordinate system of the x, y, z locations
        :`Geometry.extent`:               spatial extent as a `Point2`
        :`Geometry.extent_xyz`:           (min_x, min_y, min_z, max_x, max_y, max_z)
        :`Geometry.extent_xy`:            (min_x, min_y, max_x, max_y)
        :`Geometry.dimension`:            (dx, dy, dz) dimension
        :`Geometry.dimension_xy`:         (dx, dy) dimension
        :`Geometry.centroid`:             center point as a `Point`
        :`Geometry.centroid_xyz`:         (x, y, z) location of the object center
        :`Geometry.centroid_xy`:          (x, y) center

    .. versionadded:: 9.2
    """

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        pass

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __init__(self, coordinate_system=None, name=None, gxobj=None):
        if name is None:
            name = '_geometry_'
        self._cs = coordinate_system
        self._name = name
        self._gxobj = gxobj

    def __eq__(self, other):
        if self.coordinate_system != other.coordinate_system:
            return False
        if self._gxobj != other.gxobj:
            return False
        return True

    @property
    def coordinate_system(self):
        """`geosoft.gxpy.coordinate_system.Coordinate_system` instance or None.  Can be set."""
        if self._cs and not isinstance(self._cs, gxcs.Coordinate_system):
            self._cs = gxcs.Coordinate_system(self._cs)
        if self._gxobj and hasattr(self._gxobj, 'get_ipj'):
            ipj = gxapi.GXIPJ.create()
            self._gxobj.get_ipj(ipj)
            self._cs = gxcs.Coordinate_system(ipj)
        return self._cs

    @coordinate_system.setter
    def coordinate_system(self, cs):
        if cs and self._gxobj and hasattr(self._gxobj, 'set_ipj'):
            if not isinstance(cs, gxcs.Coordinate_system):
                cs = gxcs.Coordinate_system(cs)
            self._gxobj.set_ipj(cs.gxipj)
        self._cs = cs

    @property
    def gxobj(self):
        """An associated gxapi object, or None."""
        return self._gxobj

    @property
    def name(self):
        """Spatial object name, can be set."""
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def extent(self):
        """ Object extent as a `Point2` instance."""
        if self._gxobj and hasattr(self._gxobj, 'get_extents'):
            rx0 = gxapi.float_ref()
            ry0 = gxapi.float_ref()
            rz0 = gxapi.float_ref()
            rx1 = gxapi.float_ref()
            ry1 = gxapi.float_ref()
            rz1 = gxapi.float_ref()
            self._gxobj.get_extents(rx0, ry0, rz0, rx1, ry1, rz1)
            cs = self.coordinate_system
            return Point2(((rx0.value, ry0.value, rz0.value), (rx1.value, ry1.value, rz1.value)), cs)
        else:
            return None

    @property
    def extent_xyz(self):
        """Object extent as a tuple (xmin, ymin, zmin, xmax, ymax, zmax)."""
        e = self.extent
        if e is None:
            return None, None, None, None, None, None
        return e[0].x, e[0].y, e[0].z, e[1].x, e[1].y, e[1].z

    @property
    def extent_xy(self):
        """ Horizontal extent as a tuple (min_x, min_y, max_x, max_y)."""
        e = self.extent
        if e is None:
            return None, None, None, None
        return e[0].x, e[0].y, e[1].x, e[1].y

    @property
    def extent_minimum(self):
        """Minimum geometry extent as `Point` instance."""
        if self.extent is None:
            return None
        return self.extent[0]

    @property
    def extent_maximum(self):
        """Maximum geometry extent as `Point` instance."""
        if self.extent is None:
            return None
        return self.extent[1]

    @property
    def extent_minimum_xyz(self):
        """Minimum geometry extent as tuple (x, y, z)."""
        e = self.extent
        if e is None:
            return None, None, None
        p = e[0]
        return p.x, p.y, p.z

    @property
    def extent_maximum_xyz(self):
        """Maximum geometry extent as tuple (x, y, z)."""
        e = self.extent
        if e is None:
            return None, None, None
        p = e[1]
        return p.x, p.y, p.z

    @property
    def extent_minimum_xy(self):
        """Minimum horizontal extent as tuple (min_x, min_y)."""
        e = self.extent
        if e is None:
            return None, None
        p = e[0]
        return p.x, p.y

    @property
    def extent_maximum_xy(self):
        """Maximum horizontal extent as tuple (max_x, max_y)."""
        e = self.extent
        if e is None:
            return None, None
        p = e[1]
        return p.x, p.y

    @property
    def centroid(self):
        """Object centroid as a `Point` instance."""
        e = self.extent
        if e is None:
            return None
        cx = (e[0].x + e[1].x) * 0.5
        cy = (e[0].y + e[1].y) * 0.5
        cz = (e[0].z + e[1].z) * 0.5
        return Point((cx, cy, cz), e.coordinate_system)

    @property
    def dimension(self):
        """Object dimensions as tuple (dx, dy, dz)"""
        e = self.extent
        if e is None:
            return None, None, None
        dx = abs(e[1].x - e[0].x)
        dy = abs(e[1].y - e[0].y)
        dz = abs(e[1].z - e[0].z)
        return dx, dy, dz

    @property
    def centroid_xy(self):
        """Horizontal centroid as a tuple (x, y)."""
        c = self.centroid
        if c is None:
            return None, None
        return c.x, c.y

    @property
    def centroid_xyz(self):
        """Horizontal centroid as a tuple (x, y, z)."""
        c = self.centroid
        if c is None:
            return None, None, None
        return c.x, c.y, c.z

    @property
    def dimension_xy(self):
        """Horizontal dimension as a tuple (dx, dy)."""
        dx, dy, _ = self.dimension
        if dx is None:
            return None, None
        return dx, dy


class Point(Geometry, Sequence):
    """
    Spatial location (x,y,z).  Basic instance arithmetic and equality testing is supported.

    :param p:   point in one of the following forms:

                    `Point` instance, returns a copy

                    (x, y [,z]) implied z is as defined by z=

                    k makes a point (k, k, k)

    :param coordinate_system:   coordinate system or None
    :param z:                   implied z if len(p) is 2.
    :param kwargs:              passed to base class `Geometry`

    Iterates on [x, y, z]

    Operators supported: = + - * /

    .. versionadded:: 9.2

    .. versionchanged:: 9.3.1 added coordinate_system parameter
    """

    def __str__(self):
        return "{}({}, {}, {})".format(self.name, self.x, self.y, self.z)

    def __init__(self, p, coordinate_system=None, name=None, z=0., **kwargs):

        if name is None:
            name = '_point_'
        super().__init__(coordinate_system=coordinate_system, name=name, **kwargs)

        if isinstance(p, Point):

            if coordinate_system is None:
                coordinate_system = p.coordinate_system

            super().__init__(coordinate_system=coordinate_system, name=name, **kwargs)

            if coordinate_system != p.coordinate_system:
                self.p = gxcs.Coordinate_translate(p.coordinate_system, coordinate_system).convert(p.p)
            else:
                self.p = p.p.copy()

        else:

            super().__init__(coordinate_system=coordinate_system, name=name, **kwargs)

            if isinstance(p, np.ndarray):
                if len(p) > 2:
                    self.p = p[:3].copy()
                else:
                    self.p = np.empty(3)
                    self.p[:2] = p
                    self.p[2] = z

            elif hasattr(p, '__len__'):
                lp = len(p)
                if lp == 1:
                    v = float(p[0])
                    self.p = np.array((v, v, v), dtype=np.float)
                else:
                    self.p = np.empty(3)
                    if lp == 2:
                        self.p[0] = float(p[0]) if p[0] is not None else np.nan
                        self.p[1] = float(p[1]) if p[1] is not None else np.nan
                        self.p[2] = z
                    else:
                        self.p[0] = float(p[0]) if p[0] is not None else np.nan
                        self.p[1] = float(p[1]) if p[1] is not None else np.nan
                        self.p[2] = float(p[2]) if p[2] is not None else np.nan

            else:
                p = float(p)
                self.p = np.array((p, p, p))

        self._next = 0

    def __len__(self):
        return 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= 3:
            self._next = 0
            raise StopIteration
        else:
            item = self._next
            self._next += 1
            return self.p[item]

    def __getitem__(self, item):
        return self.p[item]

    def __add__(self, p):
        if not isinstance(p, Point):
            p = Point(p)
        else:
            p = _geo_cs(p, Point, self.coordinate_system)
        return Point(self.p + p.p, self.coordinate_system)

    def __sub__(self, p):
        if not isinstance(p, Point):
            p = Point(p)
        else:
            p = _geo_cs(p, Point, self.coordinate_system)
        return Point(self.p - p.p, self.coordinate_system)

    def __neg__(self):
        return Point(-self.p, coordinate_system=self.coordinate_system)

    def __mul__(self, p):
        if not isinstance(p, Point):
            p = Point(p)
        else:
            p = _geo_cs(p, Point, self.coordinate_system)
        return Point(self.p * p.p, self.coordinate_system)

    def __truediv__(self, p):
        if not isinstance(p, Point):
            p = Point(p)
        else:
            p = _geo_cs(p, Point, self.coordinate_system)
        return Point(self.p / p.p, self.coordinate_system)

    def __eq__(self, other):
        if not super(Point, self).__eq__(other):
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

    @property
    def extent(self):
        return Point2((self, self))

    @property
    def pp(self):
        """Point as a numpy array shaped (1, 3)"""
        return self.p.reshape((1, 3))

    def copy(self):
        """Return a copy"""
        return Point(self)


class Point2(Geometry, Sequence):
    """
    Two points, for a line, or a rectangle, or a cube.  Basic instance arithmetic and equality testing is supported.

    :param p: Points in one of the following forms:

                `Point2` makes a copy in the required coordinate system

                (`Point`, `Point`)

                (x, y [, z]) two points at the same location

                ((x, y [, z]), (x, y [, z]))

                (x0, y0, x1, y1) implied z is 0

                (x0, y0, z0, x1, y1, z1)

    :param coordinate_system:   coordinate system or None
    :param z:                   implied z value when only (x, y) is passed
    :param kwargs:              passed to base class `Geometry`

    Iterates on two points [p0, p1].

    Operators supported: = + - * /

    Second operand may be a `Point2` or a `Point`.

    .. versionadded:: 9.2

    .. versionchanged:: 9.3.1 added coordinate_system parameter
    """

    def __str__(self):
        return "{}[({}, {}, {}) ({}, {}, {})]".format(self.name, self.p0.x, self.p0.y, self.p0.z,
                                                      self.p1.x, self.p1.y, self.p1.z)

    def __init__(self, p, coordinate_system=None, name=None, z=0, **kwargs):

        if name is None:
            name = '_point2_'
        super().__init__(coordinate_system=coordinate_system, name=name, **kwargs)

        if isinstance(p, Point):
            if coordinate_system is None:
                coordinate_system = p.coordinate_system
            self.p0 = self.p1 = Point(p, coordinate_system=coordinate_system)

        elif isinstance(p, Point2):
            if coordinate_system is None:
                coordinate_system = p.coordinate_system
            self.p0 = Point(p.p0, coordinate_system=coordinate_system)
            self.p1 = Point(p.p1, coordinate_system=coordinate_system)

        else:
            if not hasattr(p, '__iter__'):
                self.p0 = self.p1 = Point(p, coordinate_system, z=z)
            elif len(p) == 2:
                if coordinate_system is None:
                    coordinate_system = first_coordinate_system((p[0], p[1]))
                if hasattr(p[0], '__iter__'):
                    self.p0 = Point(p[0], coordinate_system, z=z)
                    self.p1 = Point(p[1], coordinate_system, z=z)
                else:
                    self.p0 = Point(p, coordinate_system, z=z)
                    self.p1 = Point(self.p0)
            elif len(p) == 3:
                self.p0 = self.p1 = Point((p[0], p[1], p[2]), coordinate_system, z=z)
            elif len(p) == 4:
                self.p0 = Point((p[0], p[1]), coordinate_system, z=z)
                self.p1 = Point((p[2], p[3]), coordinate_system, z=z)
            elif len(p) == 6:
                self.p0 = Point((p[0], p[1], p[2]), coordinate_system, z=z)
                self.p1 = Point((p[3], p[4], p[5]), coordinate_system, z=z)
            else:
                raise GeometryException(_t('Invalid points: {}').format(p))

        self.coordinate_system = coordinate_system
        self._next = 0

    def __len__(self):
        return 2

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= 2:
            self._next = 0
            raise StopIteration
        else:
            if self._next:
                p = self.p1
            else:
                p = self.p0
            self._next += 1
            return p

    def __getitem__(self, item):
        if item == 0:
            return self.p0
        elif item == 1:
            return self.p1
        else:
            raise IndexError

    def __eq__(self, other):
        if not super(Point2, self).__eq__(other):
            return False
        return (self.p0 == other.p0) and (self.p1 == other.p1) or (self.p0 == other.p1) and (self.p1 == other.p0)

    def __add__(self, p):
        if isinstance(p, Point2):
            p = _geo_cs(p, Point2, self.coordinate_system)
            return Point2((self.p0 + p.p0, self.p1 + p.p1), coordinate_system=self.coordinate_system)
        if not isinstance(p, Point):
            p = Point(p)
        else:
            p = _geo_cs(p, Point, self.coordinate_system)
        return Point2((self.p0 + p, self.p1 + p), coordinate_system=self.coordinate_system)

    def __sub__(self, p):
        if isinstance(p, Point2):
            p = _geo_cs(p, Point2, self.coordinate_system)
            return Point2((self.p0 - p.p0, self.p1 - p.p1), coordinate_system=self.coordinate_system)
        if not isinstance(p, Point):
            p = Point(p)
        else:
            p = _geo_cs(p, Point, self.coordinate_system)
        return Point2((self.p0 - p, self.p1 - p), coordinate_system=self.coordinate_system)

    def __neg__(self):
        return Point2((-self.p0, -self.p1), coordinate_system=self.coordinate_system)

    def __mul__(self, p):
        if isinstance(p, Point2):
            p = _geo_cs(p, Point2, self.coordinate_system)
            return Point2((self.p0 * p.p0, self.p1 * p.p1), coordinate_system=self.coordinate_system)
        if isinstance(p, Point):
            p = _geo_cs(p, Point, self.coordinate_system)
        else:
            p = Point(p)
        return Point2((self.p0 * p, self.p1 * p), coordinate_system=self.coordinate_system)

    def __truediv__(self, p):
        if isinstance(p, Point2):
            p = _geo_cs(p, Point2, self.coordinate_system)
            return Point2((self.p0 / p.p0, self.p1 / p.p1), coordinate_system=self.coordinate_system)
        if isinstance(p, Point):
            p = _geo_cs(p, Point, self.coordinate_system)
        else:
            p = Point(p)

        return Point2((self.p0 / p, self.p1 / p), coordinate_system=self.coordinate_system)

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
        return Point2((p1, p2), self.coordinate_system)

    def copy(self):
        """Return a copy"""
        return Point2(self)

    @property
    def pp(self):
        """Point2 as a numpy array shaped (2, 3)"""
        pp = np.empty((2, 3), dtype=np.float64)
        pp[0] = self.p0.p
        pp[1] = self.p1.p
        return pp


class PPoint(Geometry, Sequence):
    """
    Poly-Point class. Basic instance arithmetic and equality testing is supported.

    :param xyz:     array-like: (p1, p2, ...), ((x, y), ...), ((x, y, z), ...) or (vv_x, vv_y, [vv_z]).
                    vv data is resampled to match the first vv.

    :param coordinate_system:   coordinate system or `None`
    :param z:                   constant z value for (x, y) data, ignored for (x, y, z) data
    :param kwargs:              passed to base class `Geometry`

    Operators supported: = + - * /

    .. versionadded:: 9.2

    .. versionchanged:: 9.3.1 added coordinate_system parameter

    """

    def __str__(self):
        return "{}({} points)".format(self.name, len(self))

    def __init__(self, xyz, coordinate_system=None, z=0.0, name=None, **kwargs):

        if name is None:
            name = '_ppoint_'
        super().__init__(coordinate_system=coordinate_system, name=name, **kwargs)

        def blankpp(length):
            pp = np.empty(length * 3, dtype=np.float).reshape((length, 3))
            pp.fill(np.nan)
            pp[:, 2] = z
            return pp

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
                pp[:, 2] = xyz[2].np
            else:
                pp[:, 2] = z
            return pp

        def point_setup(_xyz):
            pp = blankpp(len(_xyz))
            i = 0
            if isinstance(_xyz, Point):
                _xyz = (_xyz,)
            for pt in _xyz:
                if isinstance(pt, Point):
                    pp[i, :] = _geo_cs(pt, Point, coordinate_system, z=z).p
                else:
                    try:
                        pp[i, :] = pt[:3]
                    except:
                        pp[i, :] = _geo_cs(pt, Point, coordinate_system, z=z).p
                i += 1
            return pp

        if isinstance(xyz, np.ndarray):
            self.pp = np_setup(xyz)
        elif isinstance(xyz[0], gxvv.GXvv):
            self.pp = vv_setup()
        else:
            if coordinate_system is None:
                coordinate_system = first_coordinate_system(xyz)
            self.pp = point_setup(xyz)

        self.coordinate_system = coordinate_system
        self._next = 0

    @classmethod
    def from_list(cls, xyzlist, z=0.0):
        """
        .. deprecated:: 9.3 `PPoint` can create directly from a list
        """
        return cls(xyzlist, z=z)

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
            return self.__getitem__(self._next - 1)

    def __getitem__(self, item):
        return Point(self.pp[item], self.coordinate_system)

    def __add__(self, p):
        if isinstance(p, PPoint):
            p = _geo_cs(p, PPoint, self.coordinate_system)
            return PPoint(self.pp + p.pp)
        if isinstance(p, Point):
            p = _geo_cs(p, Point, self.coordinate_system)
            return PPoint(self.pp + p.p)
        try:
            p = Point(p, self.coordinate_system)
            return PPoint(self.pp + p.p)
        except TypeError:
            p = PPoint(p, self.coordinate_system)
            return PPoint(self.pp + p.pp)

    def __sub__(self, p):
        if isinstance(p, PPoint):
            p = _geo_cs(p, PPoint, self.coordinate_system)
            return PPoint(self.pp - p.pp)
        if isinstance(p, Point):
            p = _geo_cs(p, Point, self.coordinate_system)
            return PPoint(self.pp - p.p)
        return PPoint(self.pp - Point(p).p)

    def __neg__(self):
        return PPoint(self.pp * -1.0)

    def __mul__(self, p):
        if isinstance(p, PPoint):
            p = _geo_cs(p, PPoint, self.coordinate_system)
            return PPoint(self.pp * p.pp)
        if isinstance(p, Point):
            p = _geo_cs(p, Point, self.coordinate_system)
            return PPoint(self.pp * p.p)
        return PPoint(self.pp * Point(p).p)

    def __truediv__(self, p):
        if isinstance(p, PPoint):
            p = _geo_cs(p, PPoint, self.coordinate_system)
            return PPoint(self.pp / p.pp)
        if isinstance(p, Point):
            p = _geo_cs(p, Point, self.coordinate_system)
            return PPoint(self.pp / p.p)
        return PPoint(self.pp / Point(p).p)

    def __eq__(self, other):
        if not super(PPoint, self).__eq__(other):
            return False
        return np.array_equal(self.pp, other.pp)

    @classmethod
    def merge(cls, pp_list):
        """
        Create a `PPoint` from a list of `Point`, 'Point2` or `PPoint` instances or point arrays.

        :param pp_list: list of `Point`, 'Point2` or `PPoint` instances or point arrays.
        :return:        `PPoint` instance that contains all points

        .. versionadded:: 9.4
        """

        # count points, get first coordinate system
        npt = 0
        cs = None
        for pp in pp_list:
            npt += len(pp)
            if cs is None and isinstance(pp, Geometry):
                cs = pp.coordinate_system

        npp = np.zeros((npt, 3))
        i = 0
        for pp in pp_list:
            if not isinstance(pp, Geometry):
                pp = PPoint(pp, coordinate_system=cs)
            if pp.coordinate_system != cs:
                pp = PPoint(pp, coordinate_system=cs)
            npp[i:(i+len(pp))] = pp.pp
            i += len(pp)

        return PPoint(npp, coordinate_system=cs)

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

    @property
    def extent(self):
        """
        Volume extent as `Point2` for (min, max).

        .. versionadded:: 9.2
        """
        p1 = Point((np.nanmin(self.x), np.nanmin(self.y), np.nanmin(self.z)), self.coordinate_system)
        p2 = Point((np.nanmax(self.x), np.nanmax(self.y), np.nanmax(self.z)), self.coordinate_system)
        return Point2((p1, p2))

    def make_xyz_vv(self):
        """
        Return x, y and z as a set of :class:`geosoft.gxpy.vv.GXvv`.
        
        :returns: (xvv, yvv, zvv)
        
        .. versionadded:: 9.2
        """

        return gxvv.GXvv(self.x), gxvv.GXvv(self.y), gxvv.GXvv(self.z)

    def copy(self):
        """Return a copy"""
        return PPoint(self)


class Mesh(Geometry, Sequence):
    """
    Mesh - set of triangular faces, which are indexes into verticies.

    :param mesh:                (faces, verticies) that define a trangulated mesh surface. See below.
    :param coordinate_system:   coordinate system or `None`
    :param kwargs:              passed to base class `Geometry`

    A mesh is a set of triangles, where each triangle has three indexes into a set of verticies.
    Verticies are defined by a set of (x, y, z) locations. A Mesh instance can be constructed from
    two arrays in the form (faces, verticies), or from two sets of `geosoft.gxpy.vv.GXvv` instances
    in the form ((f1vv, f2vv, f3vv), (xvv, yvv, zvv)).  In array form, each array is shaped (-1, 3),
    with faces being an integer array that references vertexes in the float vertex array.

    Operators supported: = + -, where '+' can be used to combine two meshes or add a constant offset.

    Iterating yields triangular faces as `PPoint` instances.

    :Example:

    .. code::

        import numpy as np
        import geosoft.gxpy.geometry as gxgm
        import geosoft.gxpy.vv as gxvv

        # create from lists
        faces = [[0, 1, 2],
                 [0, 2, 3],
                 [3, 2, 4]]
        verticies = [[0, 0, 0],
                     [5, 0, 0],
                     [5, 5, 0],
                     [0, 3, 5],
                     [2.5, 2, 10]]
        mesh = gxgm.Mesh((faces, verticies))

        # create from numpy arrays
        faces = np.array(faces, dtype=np.int32)
        verticies = np.array(verticies, dtype=np.float64)
        mesh = gxgm.Mesh((faces, verticies))

        # create from vv
        f1vv, f2vv, f3vv = gxvv.vvset_from_np(faces)
        xvv, yvv, zvv = gxvv.vvset_from_np(verticies)
        mesh = gxgm.Mesh(((f1vv, f2vv, f3vv), (xvv, yvv, zvv)))

    .. versionadded:: 9.3.1
    """
    def __str__(self):
        return "{}({} faces)".format(self.name, len(self))

    def __init__(self, mesh, coordinate_system=None, **kwargs):

        if isinstance(mesh, Mesh):
            if coordinate_system and coordinate_system != mesh.coordinate_system:
                t = gxcs.Coordinate_translate(mesh.coordinate_system, coordinate_system)
                verticies = t.convert(mesh.verticies)
            else:
                verticies = mesh.verticies.copy()
            faces = mesh.faces.copy()

        else:
            faces, verticies = mesh
            if isinstance(faces, list):
                faces = np.array(faces)
            if isinstance(verticies, list):
                verticies = np.array(verticies)

            if not isinstance(faces, np.ndarray):
                f1, f2, f3 = faces
                faces = np.empty((len(f1), 3), dtype=np.int32)
                faces[:, 0] = f1.np
                faces[:, 1] = f2.np
                faces[:, 2] = f3.np
            else:
                faces = faces.copy()
            if not isinstance(verticies, np.ndarray):
                vx, vy, vz = verticies
                verticies = np.empty((len(vx), 3), dtype=np.float64)
                verticies[:, 0] = vx.np
                verticies[:, 1] = vy.np
                verticies[:, 2] = vz.np
            else:
                verticies = verticies.copy()

            # validate faces/verticies
            try:
                verticies[faces]
            except IndexError:
                raise GeometryException(_t('Verticies do not support all face indicies'))

        if 'name' not in kwargs:
           kwargs['name'] = '_mesh_'
        super().__init__(coordinate_system=coordinate_system, **kwargs)

        self._faces = faces
        self._verticies = verticies
        self._next = 0

    def __len__(self):
        return len(self._faces)

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= len(self._faces):
            self._next = 0
            raise StopIteration
        else:
            item = self._next
            self._next += 1
            return self.__getitem__(item)

    def __getitem__(self, item):
        return PPoint(self._verticies[self._faces[item]], self.coordinate_system)

    def __add__(self, m):
        if isinstance(m, Mesh):
            f2 = np.append(self._faces, m.faces + len(self._verticies), axis=0)
            if self.coordinate_system == m.coordinate_system:
                v2 = m.verticies
            else:
                v2 = gxcs.Coordinate_translate(m.coordinate_system, self.coordinate_system).convert(m.verticies)
            v2 = np.append(self._verticies, v2, axis=0)
            return Mesh((f2, v2), self.coordinate_system)
        if hasattr(m, '__iter__'):
            dx = m[0]
            dy = m[1]
            dz = m[2]
        else:
            dx = dy = dz = float(m)
        m = Mesh(self)
        m._verticies[:, 0] += dx
        m._verticies[:, 1] += dy
        m._verticies[:, 2] += dz
        return m

    def __sub__(self, m):
        if hasattr(m, '__iter__'):
            dx = m[0]
            dy = m[1]
            dz = m[2]
        else:
            dx = dy = dz = float(m)
        m = Mesh(self)
        m._verticies[:, 0] -= dx
        m._verticies[:, 1] -= dy
        m._verticies[:, 2] -= dz
        return m

    def __eq__(self, other):
        if not super(Mesh, self).__eq__(other):
            return False
        if not np.array_equal(self._faces, other.faces):
            return False
        if not np.array_equal(self._verticies[self._faces], other.verticies[other.faces]):
            return False
        return True

    @property
    def faces(self):
        """Faces as an integer numpy array, shape (n_faces, 3)."""
        return self._faces

    @property
    def verticies(self):
        """Verticies as a float numpy array, shape (n_verticies, 3)."""
        return self._verticies

    @property
    def pp(self):
        """Verticies as a numpy array shaped (n_verticies, 3)."""
        return self.verticies

    @property
    def length(self):
        """Number of faces"""
        return self.__len__()

    @property
    def extent(self):
        """
        Volume extent as `Point2`.

        .. versionadded:: 9.3.1
        """
        v = self._verticies[self._faces].reshape((-1, 3))
        vx = v[:, 0]
        vy = v[:, 1]
        vz = v[:, 2]
        p1 = Point((np.nanmin(vx), np.nanmin(vy), np.nanmin(vz)), self.coordinate_system)
        p2 = Point((np.nanmax(vx), np.nanmax(vy), np.nanmax(vz)), self.coordinate_system)
        return Point2((p1, p2))

    def point_array(self, unique=True):
        """
        Return numpy array of face corner locations.

        :param unique:  `True` to limit to unique points, otherwise returns all points
                        by unwinding each face. If unique the order will not be related to the faces.

        .. versionadded:: 9.3.1
        """
        if unique:
            return self._verticies[np.unique(self._faces.flatten())].reshape(-1, 3)
        return self._verticies[self._faces].reshape(-1, 3)

    def faces_vv(self):
        """Return faces in `geosoft.gxpy.vv.GXvv` tuple (f1vv, f2vv, f3vv)."""
        return gxvv.GXvv(self._faces[:, 0], dtype=np.int32),\
            gxvv.GXvv(self._faces[:, 1], dtype=np.int32),\
            gxvv.GXvv(self._faces[:, 2], dtype=np.int32)

    def verticies_vv(self):
        """Return verticies in `geosoft.gxpy.vv.GXvv` tuple (xvv, yvv, zvv)."""
        return gxvv.GXvv(self._verticies[:, 0], dtype=np.float64),\
            gxvv.GXvv(self._verticies[:, 1], dtype=np.float64),\
            gxvv.GXvv(self._verticies[:, 2], dtype=np.float64)

    def copy(self):
        """Return a copy"""
        return Mesh(self)
