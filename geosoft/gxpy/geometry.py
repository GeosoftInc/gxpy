import numpy as np
import numbers
from collections.abc import Sequence

import geosoft
import geosoft.gxapi as gxapi
from . import map as gxmap
from . import vv as gxvv
from . import ipj as gxipj
from . import utility as gxu

__version__ = geosoft.__version__

def _(s):
    return s

class GeometryException(Exception):
    """
    Exceptions from this module.
    """
    pass

class CS:
    """
    Base-class to manage coordinate system for all geometries.
    A coordinate system defines the horizontal and vertical reference system relative to the Earth.

    :param ipj: IPJ as an IPJ instance or a named string that can be constructred from `gxpy.ipj.from_any()`.
    :param vcs: Vertical Coordinate System name
    """

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "({} {})".format(str(self.ipj()), str(self.vcs()))

    def _set_ipj(self, ipj):
        if isinstance(ipj, gxipj.GXipj):
            self._init_ipj = str(ipj)
            self._ipj = ipj
        else:
            self._init_ipj = ipj
            self._ipj = None

    def __init__(self, ipj=None, vcs=None):

        self._set_ipj(ipj)
        self._init_vcs = vcs
        self._vcs = None

    @property
    def ipj(self):
        """IPJ instance"""
        if self._ipj is None:
            self._ipj = gxipj.GXipj.from_any(self._init_ipj)
        return self._ipj

    @ipj.setter
    def ipj(self, ipj):
        self._set_ipj(ipj)

    @property
    def vcs(self):
        """Vertical Coordinate System"""
        if self._vcs is None:
            self._vcs = self._init_vcs
        return self._vcs

    @vcs.setter
    def vcs(self, vcs):
        self._ipj = vcs


# geometry spatial data structures
class Point(CS):
    """
    Spatial location (x,y,z)

    :param p:   array-line (x, y, z) create a Point (x, y, z)
                if Point, returns a copy.
                if array-like (x, y), create a Point (x, y, 0.0)
                if a single value k (integral or float), create a Point (k, k, k)

    .. versionadded:: 9.2
    """
    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self.__del__()

    def __del__(self):
        pass

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "({}, {}, {})".format(self.x(), self.y(), self.z())

    def __init__(self, p, **kwds):
        super().__init__(**kwds)
        if hasattr(p, "__len__"):
            if len(p) > 2:
                self.p = np.array(p[:3], dtype=float)
            elif len(p) == 2:
                self.p = np.array((p[0], p[1], 0.0))
            else:
                self.p = np.array((p[0], p[0], p[0]), dtype=float)
        else:
            if type(p) is Point:
                self.p = Point.p.copy()
            elif isinstance(p, numbers.Real) or isinstance(p, numbers.Integral):
                p = float(p)
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

class PPoint(CS, Sequence):
    """
    Poly-Point class.

    :param xyz: array-like, either (x, y) or (x, y, z) (shape (n, 2) or (n, 3))
    :param z:   constant z value for (x, y) data, ignored for (x, y, z) data

    :member pp: nparray shape (n,3)

    .. versionadded:: 9.2
    """

    def __init__(self, xyz, z=0.0, **kwds):
        """
        Create a PPoint from a list of (x, y, z) points (array-like)
        :param xyz: array-line, either (x, y) or (x, y, z) (shape (n, 2) or (n, 3))
        :param z:   constant z value for (x, y) data, ignored for (x, y, z) data
        """
        super().__init__(**kwds)
        if type(xyz) is not np.ndarray:
            xyz = np.array(xyz)

        self.pp = np.zeros(xyz.shape[0]*3, dtype=np.float).reshape((xyz.shape[0], 3))
        self.pp[:, 0] = xyz[:, 0]
        self.pp[:, 1] = xyz[:, 1]
        if xyz.shape[1] > 2:
            self.pp[:, 2] = xyz[:, 2]
        else:
            self.pp[:, 2] = z
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