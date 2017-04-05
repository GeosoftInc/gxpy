import numpy as np
import numbers
from collections.abc import Sequence

import geosoft
from . import coordinate_system as gxcs
from . import vv as gxvv

__version__ = geosoft.__version__

def _t(s):
    return geosoft.gxpy.system.translate(s)

class GeometryException(Exception):
    """
    Exceptions from this module.
    """
    pass

class Geometry:
    """
    Geometry base class.

    :param hcs, vcs:
            horizontal and vertical coordinate systems (see :class::`gxpy.coordinate_system.GXcs`)

    .. versionadded:: 9.2
    """

    def __init__(self, **kwargs):
         self.cs = gxcs.GXcs(**kwargs)

    def __eq__(self, other):
        return self.cs.same_as(other.cs)

    def set_cs(self, *args, **kwargs):
        self.cs = gxcs.GXcs(*args, **kwargs)


class Point(Geometry):
    """
    Spatial location (x,y,z).

    :param p:   point in one of the following forms:

                ::

                    Point   makes a copy
                    (x, y [,z]) implied z is 0.0 if not provided
                    k makes a point (k, k, k)

    .. versionadded:: 9.2
    """
    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        pass

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "({}, {}, {})".format(self.x(), self.y(), self.z())

    def __init__(self, p, **kwargs):

        super().__init__(**kwargs)

        if hasattr(p, "__len__"):
            if len(p) > 2:
                self.p = np.array(p[:3], dtype=float)
            elif len(p) == 2:
                self.p = np.array((p[0], p[1], 0.0))
            else:
                self.p = np.array((p[0], p[0], p[0]), dtype=float)
        else:
            if type(p) is Point:
                self.p = p.p.copy()
            else:
                self.p = np.array((p, p, p))

    def __add__(self, p):
        if type(p) is not Point:
            p = Point(p)
        return Point(self.p + p.p)

    def __sub__(self, p):
        if type(p) is not Point:
            p = Point(p)
        return Point(self.p - p.p)

    def __neg__(self):
        return Point(-self.p)

    def __mul__(self, p):
        if type(p) is not Point:
            p = Point(p)
        return Point(self.p * p.p)

    def __truediv__(self, p):
        if type(p) is not Point:
            p = Point(p)
        return Point(self.p / p.p)

    def __eq__(self, other):
        return (self.cs.same_as(other.cs)) and \
               np.array_equal(self.p, other.p) and \
               self.cs.same_as(other.cs)

    @property
    def p1(self):
        """ Point 1"""
        return self.p1

    @p1.setter
    def p1(self, p):
        self.p1 = Point(p)

    @property
    def p2(self):
        """ Point 2"""
        return self.p1

    @p2.setter
    def p1(self, p):
        self.p2 = Point(p)

    @property
    def x(self):
        """ X value"""
        return self.p[0]

    @x.setter
    def x(self, value):
        self.p[0] = float(value)

    @property
    def y(self):
        """ Y value"""
        return self.p[1]

    @y.setter
    def y(self, value):
        self.p[1] = float(value)

    @property
    def z(self):
        """ z value"""
        return self.p[2]

    @z.setter
    def z(self, value):
        self.p[2] = float(value)

    @property
    def xy(self):
        """ (x, y)"""
        return (self.p[0], self.p[1])

    @xy.setter
    def xy(self, xy):
        self.p[0] = float(xy[0])
        self.p[1] = float(xy[1])

    @property
    def xyz(self):
        """ (x, y, z) """
        return (self.p[0], self.p[1], self.p[2])

    @xyz.setter
    def xyz(self, xyz):
        self.p[0] = float(xyz[0])
        self.p[1] = float(xyz[1])
        self.p[2] = float(xyz[2])

    def copy(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

class Point2(Geometry):
    """
    Two points, for a line, or a rectangle, or a cube

    :param p:       Points in one of the following forms:

                    ::

                        (Point, Point)
                        ((x, y [,z]), (x, y [,z])) implied z is 0 if not specified
                        (x0, y0, x1, y1) implied z is 0
                        (x0, y0, z0, x1, y1, z1)

    .. versionadded:: 9.2
    """
    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        pass

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "Point2[({}, {}, {}) ({}, {}, {})]".format(self.p1.x, self.p1.y, self.p1.z,
                                                          self.p2.x, self.p2.y, self.p2.z)

    def __init__(self, p, **kwargs):

        super().__init__(**kwargs)

        if len(p) == 2:
            self.p1 = Point(p[0])
            self.p2 = Point(p[1])
        elif len(p) == 4:
            self.p1 = Point((p[0], p[1]))
            self.p2 = Point((p[2], p[3]))
        elif len(p) == 6:
            self.p1 = Point((p[0], p[1], p[2]))
            self.p2 = Point((p[3], p[4], p[5]))
        else:
            raise GeometryException(_t('Invalid points: {}').format(p))

    def __eq__(self, other):
        return (self.cs.same_as(other.cs)) and \
                ((self.p1 == other.p1) and (self.p2 == other.p2)
                 or (self.p1 == other.p2) and (self.p2 == other.p1))

    def copy(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    @property
    def x2(self):
        """ X extent (min, max)"""
        return self.p1.x, self.p2.x

    @x2.setter
    def x2(self, value):
        self.p1.x = value[0]
        self.p2.x = value[1]

    @property
    def y2(self):
        """ Y extent (min, max)"""
        return self.p1.y, self.p2.y

    @y2.setter
    def y2(self, value):
        self.p1.y = value[0]
        self.p2.y = value[1]

    @property
    def z2(self):
        """ Z extent (min, max)"""
        return self.p1.z, self.p2.z

    @z2.setter
    def z2(self, value):
        self.p1.z = value[0]
        self.p2.z = value[1]


class PPoint(Geometry, Sequence):
    """
    Poly-Point class.

    :param xyz: array-like, either ((x, y), ...), ((x, y, z), ...) or (vv_x, vv_y, [vv_z]).
                vv data is resampled to match the first vv.
    :param z:   constant z value for (x, y) data, ignored for (x, y, z) data

    :member pp: nparray shape (n,3)

    .. versionadded:: 9.2
    """

    def __init__(self, xyz, z=0.0, **kwargs):

        super().__init__(**kwargs)

        def blankpp(length):
            self.pp = np.zeros(length * 3, dtype=np.float).reshape((length, 3))

        def np_setup(xyz):
            blankpp(xyz.shape[0])
            self.pp[:, 0] = xyz[:, 0]
            self.pp[:, 1] = xyz[:, 1]
            if xyz.shape[1] > 2:
                self.pp[:, 2] = xyz[:, 2]
            else:
                self.pp[:, 2] = z

        def vv_setup(xyz):
            blankpp(xyz[0].length)
            self.pp[:, 0] = xyz[0].get_np()[0][:]
            xyz[1].reFid(xyz[0].fid, self.pp.shape[0])
            self.pp[:, 1] = xyz[1].get_np()[0][:]
            if len(xyz) > 2:
                xyz[2].reFid(xyz[0].fid, self.pp.shape[0])
                self.pp[:, 2] = xyz[2].get_np()[0][:]
            else:
                self.pp[:, 2] = z

        t = type(xyz[0])
        if t is np.ndarray:
            np_setup(xyz)
        elif t is gxvv.GXvv:
            vv_setup(xyz)
        else:
            np_setup(np.array(xyz))

        self._next = 0

    @classmethod
    def from_list(cls, xyzlist, z=0.0):
        return cls(np.array(xyzlist, dtype=np.float), z)

    def __len__(self):
        return self.pp.shape[0]

    def __getitem__(self, item):
        return Point(self.pp[item])

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= self.pp.shape[0]:
            self._next = 0
            raise StopIteration
        else:
            self._next += 1
            return Point(self.pp[self._next - 1])

    def __getitem__(self, item):
        return Point(self.pp[item])

    def __add__(self, p):
        if type(p) is PPoint:
            return PPoint(self.pp + p.pp)
        if type(p) is Point:
            return PPoint(self.pp + p.p)
        return PPoint(self.pp + Point(p).p)

    def __sub__(self, p):
        if type(p) is PPoint:
            return PPoint(self.pp - p.pp)
        if type(p) is Point:
            return PPoint(self.pp - p.p)
        return PPoint(self.pp - Point(p).p)

    def __neg__(self):
        return PPoint(self.pp * -1.0)

    def __mul__(self, p):
        if type(p) is PPoint:
            return PPoint(self.pp * p.pp)
        if type(p) is Point:
            return PPoint(self.pp * p.p)
        return PPoint(self.pp * Point(p).p)

    def __truediv__(self, p):
        if type(p) is PPoint:
            return PPoint(self.pp / p.pp)
        if type(p) is Point:
            return PPoint(self.pp / p.p)
        return PPoint(self.pp / Point(p).p)

    def __eq__(self, other):
        return (self.cs.same_as(other.cs)) and np.array_equal(self.pp, other.pp)

    def copy(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    @property
    def x(self):
        """ X array slice"""
        return self.pp[:,0]

    @x.setter
    def x(self, v):
        self.pp[:,0] = v

    @property
    def y(self):
        """ Y array slice"""
        return self.pp[:,1]

    @y.setter
    def y(self, v):
        self.pp[:,1] = v

    @property
    def z(self):
        """ Z array slice"""
        return self.pp[:,2]

    @z.setter
    def z(self, v):
        self.pp[:,2] = v

    @property
    def xy(self):
        """ XY array slice"""
        return self.pp[:, 0:2]

    @xy.setter
    def xy(self, v):
        self.pp[:, 0:2] = v

    @property
    def xyz(self):
        """ XYZ point array"""
        return self.pp

    def extent(self):
        """
        Returns extent of the polyline.
        
        :returns:   (P_minimum, P_maximum)
        """
        p1 = Point((np.amin(self.x), np.amin(self.y), np.amin(self.z)))
        p2 = Point((np.amax(self.x), np.amax(self.y), np.amax(self.z)))
        return p1, p2
