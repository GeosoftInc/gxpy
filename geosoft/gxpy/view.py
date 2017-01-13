#TODO review grd class to clean-up files like map class does.

import numpy as np
import numbers

import geosoft
import geosoft.gxapi as gxapi
from . import map as gxmap
from . import vv as gxvv
from . import geometry as gxgm
from . import ipj as gxipj
from . import utility as gxu
from . import coordinate_system as gxcs

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

class GXview:
    """
    Geosoft view class.

    :param viewname:    view name, default is "_default_view"
    :param gmap:        map instance, if not specified a new default map is created and deleted on closing
    :param hcs, vcs:    horizontal and vertical coordinate system definition.  See :class:`coordinate_system.GXcs`.
    :param groupname:   default initial group name

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
        return self._viewname

    def __init__(self,
                 viewname="_default_view",
                 gmap=None,
                 mode=MODE_WRITENEW,
                 hcs=None,
                 vcs=None,
                 groupname = '_default'):

        if isinstance(gmap, gxmap.GXmap):
            self._gmap = gmap
        else:
            self._gmap = gxmap.GXmap.new(gmap)

        self._viewname = viewname
        self.gxview = gxapi.GXMVIEW.create(self._gmap.gxmap, self._viewname, mode)
        self.gxview.start_group(groupname, gxapi.MVIEW_GROUP_NEW)

        # intitialize pen
        self._init_pen_attributes()
        self._pen_stack = []

        # coordinate system
        self._cs = gxcs.GXcs(hcs, vcs)
        self.gxview.set_ipj(self._cs.gxipj)

    @property
    def cs(self):
        return self._cs.hcs, self._cs.vcs

    def _line_style(self, ls):
        self.gxview.line_style(ls[0], ls[1])

    def _init_pen_attributes(self):

        # set the default pen characteristics, initializes pen dictionaries

        def setpen(att, fn, setting):
            fn(setting)
            self._pen[att] = setting
            self._pen_fn[att] = fn

        self._pen = {}
        self._pen_fn = {}
        setpen('line_color', self.gxview.line_color, gxapi.C_BLACK)
        setpen('line_thick', self.gxview.line_thick, 0.1)
        setpen('line_smooth',self.gxview.line_smooth, SMOOTH_NONE)
        setpen('line_style', self._line_style, (0, 1.0))
        setpen('fill_color', self.gxview.fill_color, gxapi.C_TRANSPARENT)
        setpen('pat_number', self.gxview.pat_number, 0)
        setpen('pat_angle', self.gxview.pat_angle, 0.0)
        setpen('pat_density', self.gxview.pat_density, 1.0)
        setpen('pat_size', self.gxview.pat_size, 5.0)
        setpen('pat_style', self.gxview.pat_style, TILE_RECTANGULAR)
        setpen('pat_thick', self.gxview.pat_thick, 0.1)

    @property
    def gmap(self):
        """ gxpy.GXmap instance that contains this view."""
        return self._gmap

    @property
    def viewname(self):
        """ Name of the view"""
        return self._viewname

    @property
    def mapfilename(self):
        """ Name of the map file that contains this view. """
        return self._gmap.mapfilename

    def color(self, cstr):
        """
        Return a color from a color string.
        :param cstr:    color string (see below)
        :return:        color

        Colour strings may be "R","G","B","C","M","Y",
        "H","S","V", or "K" or a combination of these
        characters, each followed by up to three digits
        specifying a number between 0 and 255.
        An empty string will produce C_ANY_NONE.

        You must stay in the same colour model, RGB, CMY,
        HSV or K.

        For example "R", "R127G22", "H255S127V32"

        Characters are not case sensitive.
        """

        return self.gxview.color(str)

    @property
    def pen(self):
        """
        Dictionary of the current pen settings.
        """
        return self._pen.copy()

    @pen.setter
    def pen(self, pen=None):
        """
        Set the current drawing pen attributes from a pen dictionary
        """

        if pen is None:
            self._init_pen_attributes()

        else:
            for att, setting in pen.items():
                if self._pen[att] != setting:
                    self._pen_fn[att](setting)
                    self._pen[att] = setting

    def push_pen(self, pen=None):
        """Push current pen attributes on the pen stack. If pen not specified, all pen attributes are pushed."""
        if pen is None:
            self._pen_stack.append(self._pen.copy())
        else:
            oldpen = {}
            for key in pen:
                oldpen[key] = self._pen[key]
            self._pen_stack.append(oldpen)

    def pop_pen(self):
        """Pop the last pen off the pen stack."""
        if len(self._pen_stack) > 0:
            self.pen = self._pen_stack[-1]
            del self._pen_stack[-1:]

    def start_group(self, name, append=False):
        """
        Start a new named group in a view.  Drawing functions that follow will be rendered into this group.

        :param name:    name of the group
        :param append:  True to append to an existing group

        .. versionadded:: 9.2
        """

    # drawing to a plane

    def xy_line(self, p1, p2):
        """
        Draw a line on the current plane
        :param p1:  gxpy.geometry.Point starting
        :param p2:  gxpy.geometry.Point end

        .. versionadded:: 9.2
        """

        self.gxview.line(p1.x, p1.y, p2.x, p2.y)

    def xy_poly_line(self, pp, close=False):
        """
        Draw a polyline the current plane
        :param pline: gxpy.geometry.PPoint
        :param close: if True, draw a polygon, default is a polyline

        .. note::
            Smooth-line polygons must have at least 6 points for the closure to
            appear continuous.

        .. versionadded:: 9.2
        """

        if close:
            self.gxview.poly_line(gxapi.MVIEW_DRAW_POLYGON,
                                 gxvv.GXvv.vv_np(pp.x)._vv,
                                 gxvv.GXvv.vv_np(pp.y)._vv)
        else:
            self.gxview.poly_line(gxapi.MVIEW_DRAW_POLYLINE,
                                 gxvv.GXvv.vv_np(pp.x)._vv,
                                 gxvv.GXvv.vv_np(pp.y)._vv)

    def xy_rectangle(self, p1, p2, pen=None):
        """
        Draw a 2D rectangle on the current plane
        :param p1:  Point starting
        :param p2:  Point diagonal
        :param pen: pen to use, attribtutes modify current pen for the rectangle only

        .. versionadded:: 9.2
        """

        if pen is not None:
            self.push_pen(pen)
            self.pen = pen

        self.gxview.rectangle(p1.x, p1.y, p2.x, p2.y)

        if pen is not None:
            self.pop_pen()

    def box_3d(self, box, pen=None):
        """
        Draw a 3D box on the current plane
        :param box: geometry.Box
        :param pen: pen to use

        .. versionadded:: 9.2
        """

        if pen is not None:
            self.push_pen(pen)
            self.pen = pen

        self.gxview.box_3d(box.p1.x, box.p1.y, box.p1.z,
                           box.p2.x, box.p2.y, box.p2.z)

        if pen is not None:
            self.pop_pen()


class GXview3d(GXview):

    def __init__(self, viewname='_default_3d', locate=(0,0,100,100), area=None, **kwds):

        if 'gmap' not in kwds:
            kwds['gmap'] = None
        super().__init__(viewname, **kwds)

        # construct a 3D view

        h3dn = gxapi.GX3DN.create()
        pov = (4., 20., 25.)
        pov = (5., 0., 90.)
        h3dn.set_point_of_view(pov[0], pov[1], pov[2])
        render = (0, 0, 'x', 'y', 'z')
        h3dn.set_render_controls(render[0], render[1], render[2], render[3], render[4])
        self.gxview.set_h_3dn(h3dn)

        mminx, mminy, mmaxx, mmaxy = locate
        if area is None:
            dminx, dminy, dmaxx, dmaxy = locate
        else:
            dminx, dminy, dmaxx, dmaxy = area
        self.gxview.fit_map_window_3d(mminx, mminy, mmaxx, mmaxy,
                                      dminx, dminy, dmaxx, dmaxy)


