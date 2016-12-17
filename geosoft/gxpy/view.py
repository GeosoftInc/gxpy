#TODO review grd class to clean-up files like map class does.

import os
import gc
import uuid
import collections

import geosoft
import geosoft.gxapi as gxapi
from . import map as gxmap
from . import ipj as gxipj
from . import utility as gxu

__version__ = geosoft.__version__

def _(s):
    return s

class VIEWException(Exception):
    """
    Exceptions from this module.

    .. versionadded:: 9.2
    """
    pass

MODE_READ = gxapi.MVIEW_READ
MODE_WRITENEW = gxapi.MVIEW_WRITENEW
MODE_WRITEOLD = gxapi.MVIEW_WRITEOLD
SMOOTH_NONE = gxapi.MVIEW_SMOOTH_NEAREST
SMOOTH_CUBIC = gxapi.MVIEW_SMOOTH_CUBIC
SMOOTH_AKIMA = gxapi.MVIEW_SMOOTH_AKIMA
TILE_RECTANGULAR = gxapi.MVIEW_TILE_RECTANGULAR
TILE_DIAGONAL = gxapi.MVIEW_TILE_DIAGONAL
TILE_TRIANGULAR = gxapi.MVIEW_TILE_TRIANGULAR
TILE_RANDOM = gxapi.MVIEW_TILE_RANDOM

_def_group = "_default_group_"

# spatial data structures
class Point:
    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self.__del__()

    def __del__(self):
        pass

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __init__(self, x, y, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, p):
        if type(p) is Point:
            return Point(self.x + p.x, self.y + p.y, self.z + p.z)
        else:
            v = float(p)
            return Point(self.x + v, self.y + v, self.z + v)

    def __sub__(self, p):
        if type(p) is Point:
            return Point(self.x - p.x, self.y - p.y, self.z - p.z)
        else:
            v = float(p)
            return Point(self.x - v, self.y - v, self.z - v)

    def __neg__(self):
        return Point(-self.x, -self.y, -self.z)

    def __mul__(self, p):
        if type(p) is Point:
            return Point(self.x * p.x, self.y * p.y, self.z * p.z)
        else:
            v = float(p)
            return Point(self.x * v, self.y * v, self.z * v)

    def xy(self):
        """ Return (x, y, z) of a point"""
        return (self.x, self.y)

    def xyz(self):
        """ Return (x, y, z) of a point"""
        return (self.x, self.y, self.z)


class GXview:
    """
    Geosoft view class.

    .. versionadded:: 9.2
    """

    _view = None

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self.__del__()

    def __del__(self):

        if self._view:

            # remove the default group if it is empty

            if self._view.is_group_empty(_def_group):
                self._view.delete_group(_def_group)
            self._view = None

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self._filename

    def __init__(self, viewname="_default_view_", gmap=None, mode=MODE_WRITENEW):

        # temporary map for the view
        if gmap is None:
            self._map = gxmap.GXmap.new()
        else:
            self._map = gmap
        self._viewname = viewname
        self._view = gxapi.GXMVIEW.create(self._map._map, self._viewname, mode)

        # start a default group
        self._view.start_group("_default_group_", gxapi.MVIEW_GROUP_NEW)

        # intitialize pen
        self._init_pen_attributes()

    def _line_style(self, ls):
        self._view.line_style(ls[0], ls[1])

    def _init_pen_attributes(self):

        # set the default pen characteristics, initializes pen dictionaries

        def setpen(att, fn, setting):
            fn(setting)
            self.pen[att] = setting
            self.pen_fn[att] = fn

        self.pen = {}
        self.pen_fn = {}
        setpen('line_color', self._view.line_color, gxapi.C_BLACK)
        setpen('line_thick', self._view.line_thick, 0.1)
        setpen('line_smooth',self._view.line_smooth, SMOOTH_NONE)
        setpen('line_style', self._line_style, (0, 1.0))
        setpen('fill_color', self._view.fill_color, gxapi.C_TRANSPARENT)
        setpen('pat_number', self._view.pat_number, 0)
        setpen('pat_angle', self._view.pat_angle, 0.0)
        setpen('pat_density', self._view.pat_density, 1.0)
        setpen('pat_size', self._view.pat_size, 5.0)
        setpen('pat_style', self._view.pat_style, TILE_RECTANGULAR)
        setpen('pat_thick', self._view.pat_thick, 0.1)

    def map(self):
        """
        :return: name of the map that contains this view

        .. versionadded:: 9.2
        """
        return self._map

    def viewname(self):
        """
        :return: name of the view contains this view

        .. versionadded:: 9.2
        """
        return self._viewname

    def mapname(self):
        """
        :return: name of the map that contains this view

        .. versionadded:: 9.2
        """
        return self._map.filename()

    def set_pen(self, pen=None):
        """
        Set the current drawing pen attributes
        :param pen: dictionary of pen attrbutes and settings, if None, set to default

        .. versionadded:: 9.2
        """

        if pen is None:
            self._init_pen_attributes()

        else:
            for att, setting in pen.items():
                if self.pen[att] != setting:
                    self.pen_fn[att](setting)
                    self.pen[att] = setting

    def get_pen(self):
        """
        Return a dictionary of the current pen settings.

        .. versionadded:: 9.2
        """
        return self.pen

    def group(self, name, append=False):
        """
        Start a new named group in a view.  Drawing functions that follow will be rendered into this group.

        :param name:    name of the group
        :param append:  True to append to the group should it exist

        .. versionadded:: 9.2
        """

    # drawing to a plane

    def line(self, p1, p2):
        """
        Draw a line on the current plane
        :param p1:  Point starting
        :param p2:  Point end

        .. versionadded:: 9.2
        """

        self._view.line( p1.x, p1.y, p2.x, p2.y)

    def rectangle(self, p1, p2):
        """
        Draw a 2D rectangle on the current plane
        :param p1:  Point starting
        :param p2:  Point diagonal

        .. versionadded:: 9.2
        """

        self._view.rectangle( p1.x, p1.y, p2.x, p2.y)
