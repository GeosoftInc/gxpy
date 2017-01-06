import numpy as np
import numbers

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
    Coordinate System, which includes a horizontal and vertical reference system.
    """

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "({} {})".format(str(self.ipj()), str(self.vcs()))

    def __init__(self, ipj=None, vcs=None):
        self._init_ipj = ipj
        self._init_vcs = vcs
        self._ipj = None
        self._vcs = None

    def set_ipj(self, ipj):
        self._ipj = ipj

    def set_vcs(self, vcs):
        self._ipj = vcs

    def ipj(self):
        if self._ipj is None:
            self._ipj = gxipj.GXipj.from_any(self._init_ipj)
        return self._ipj

    def vcs(self):
        if self._vcs is None:
            self._vcs = self._init_vcs
        return self._vcs

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

    def x(self):
        """ Return x of a point"""
        return self.p[0]

    def y(self):
        """ Return y of a point"""
        return self.p[1]

    def z(self):
        """ Return z of a point"""
        return self.p[2]

    def xy(self):
        """ Return (x, y) of a point"""
        return (self.p[0], self.p[1])

    def xyz(self):
        """ Return (x, y, z) of a point"""
        return (self.p[0], self.p[1], self.p[2])


class PPoint(CS):
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

    def x(self):
        """ Return X array slice"""
        return self.pp[:,0]

    def y(self):
        """ Return Y array slice"""
        return self.pp[:,1]

    def z(self):
        """ Return Z array slice"""
        return self.pp[:,2]

    def xyz(self):
        """ Return xyz point array"""
        return self.pp