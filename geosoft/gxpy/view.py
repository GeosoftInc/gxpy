import atexit
from functools import wraps

import geosoft
import geosoft.gxapi as gxapi
from . import map as gxmap
from . import vv as gxvv
from . import geometry as gxgm
from . import ipj as gxipj
from . import utility as gxu
from . import coordinate_system as gxcs

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class ViewException(Exception):
    """
    Exceptions from this module.

    .. versionadded:: 9.2
    """
    pass

READ_ONLY = gxapi.MVIEW_READ
WRITE_NEW = gxapi.MVIEW_WRITENEW
WRITE_OLD = gxapi.MVIEW_WRITEOLD

SMOOTH_NONE = gxapi.MVIEW_SMOOTH_NEAREST
SMOOTH_CUBIC = gxapi.MVIEW_SMOOTH_CUBIC
SMOOTH_AKIMA = gxapi.MVIEW_SMOOTH_AKIMA

TILE_RECTANGULAR = gxapi.MVIEW_TILE_RECTANGULAR
TILE_DIAGONAL = gxapi.MVIEW_TILE_DIAGONAL
TILE_TRIANGULAR = gxapi.MVIEW_TILE_TRIANGULAR
TILE_RANDOM = gxapi.MVIEW_TILE_RANDOM

EXTENT_VIEW = 1
EXTENT_MAP = -1

UNIT_VIEW = 0
UNIT_MAP = 2
UNIT_VIEW_UNWARPED = 3

GRATICULE_DOT = 0
GRATICULE_LINE = 1
GRATICULE_CROSS = 2

# decorators
def _draw(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not hasattr(self,'_pen'):
            self.start_group('_')
        if 'pen' in kwargs:
            self.push_pen(kwargs.pop('pen'))
            func(self, *args, **kwargs)
            self.pop_pen()
        else:
            func(self, *args, **kwargs)

    return wrapper

class GXview:
    """
    Geosoft view class.

    :parameters:
        :viewname:      view name, default is "_unnamed_view"
        :gmap:          map instance, if not specified a new default map is created and deleted on closing
        :mode:          open view mode:
                            | view.READ_ONLY
                            | view.WRITE_NEW
                            | view.WRITE_OLD

        The following are only used if WRITE_NEW.
        
        :hcs, vcs:      horizontal and vertical coordinate system definition.  See :class:`coordinate_system.GXcs`.
        :map_location:  (x, y) view location on the map, in map cm
        :area:          (min_x, min_y, max_x, max_y) area in view units
        :scale:         Map scale if a coordinate system is defined.  If the coordinate system (hcs) is not
                        defined this is view units per map metre.

    .. versionadded:: 9.2
    """

    _view = None

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self._close()

    def _close(self):
        if self._open:
            self._gmap = None  # release map
            self.gxview = None # release the view
            self._open = False

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self._viewname

    def __init__(self,
                 gmap,
                 viewname="_unnamed_view",
                 mode=WRITE_NEW,
                 hcs=None,
                 vcs=None,
                 map_location=(0,0),
                 area=(0,0,30,20),
                 scale=100):

        self._gmap = gmap
        self._viewname = viewname
        self.gxview = gxapi.GXMVIEW.create(self._gmap.gxmap, self._viewname, mode)
        self._mode = mode

        atexit.register(self._close)
        self._open = True
        
        if mode == WRITE_NEW:
            self.locate(hcs, vcs, map_location, area, scale)
        else:
            ipj = gxapi.GXIPJ.create()
            self.gxview.get_ipj(ipj)
            self.cs = gxcs.GXcs(hcs=ipj)
            self._uname, self._units_per_m = self.cs.units()

    def set_cs(self, hcs=None, vcs=None):
        """
        Set the coordinate system of the view.

        :param hcs: horizontal coordinate system
        :param vcs: vertical coordinate system

        Refer to `gxpy.GXcs()` for `hcs`, `vcs` usage.
        """
        self.cs = gxcs.GXcs(hcs, vcs)
        metres_per, self._uname = self.cs.units()
        if metres_per <= 0.:
            raise ViewException('Invalid units {}({})'.format(self._uname, metres_per))
        self._units_per_m = 1.0/metres_per
        self.gxview.set_ipj(self.cs.gxipj)

    def locate(self,
               hcs=None, vcs=None,
               map_location=None,
               area=None,
               scale=None):
        """
        Locate and scale the view on the map.

        :parameters:
            :hcs, vcs:      New horizontal and vertical coordinate system definition.
                            See :class:`coordinate_system.GXcs`.
            :map_location:  New (x, y) view location on the map, in map cm.
            :area:          New (min_x, min_y, max_x, max_y) area in view units
            :scale:         New scale in view units per map metre, either as a single value or
                            (x_scale, y_scale)

        .. versionadded:: 9.2
        """

        if self._mode == READ_ONLY:
            raise ViewException('Cannot modify a READ_ONLY view.')

        # coordinate system
        self.set_cs(hcs, vcs)
        upm = self.units_per_m

        if area == None:
            area = self.extent(EXTENT_VIEW)

        # area and scale
        if hasattr(scale, "__iter__"):
            x_scale, y_scale = scale
        else:
            x_scale = y_scale = scale
        a_minx, a_miny, a_maxx, a_maxy = area
        mm_minx = map_location[0] * 10.0
        mm_miny = map_location[1] * 10.0
        mm_maxx = mm_minx + (a_maxx - a_minx) * 1000.0 / upm / x_scale
        mm_maxy = mm_miny + (a_maxy - a_miny) * 1000.0 / upm / y_scale
        self.gxview.fit_window(mm_minx, mm_miny, mm_maxx, mm_maxy,
                               a_minx, a_miny, a_maxx, a_maxy)
        self.gxview.set_window(a_minx, a_miny, a_maxx, a_maxy, UNIT_VIEW)


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
        return self._gmap.filename

    @property
    def units_per_m(self):
        return self._units_per_m

    @property
    def unit_name(self):
        return self._uname

    @property
    def pen(self):
        """
        Dictionary of the current pen settings.
        """
        return self._pen.copy()

    @pen.setter
    def pen(self, pen):
        """
        Set the current drawing pen attributes from a pen dictionary
        """
        for att, setting in pen.items():
            if type(setting) is str:
                setting = self.gxview.color(setting)
            if self._pen[att] != setting:
                self._pen_fn[att](setting)
                self._pen[att] = setting

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

    def start_group(self, name, append=False):
        """
        Start a new named group in a view.  Drawing functions that follow will be rendered into this group.

        :param name:    name of the group.  If a group name is the same as the view name, '_' is appended
                        to the group name to make it different.
        :param append:  True to append to an existing group

        .. versionadded:: 9.2
        """
        if append:
            mode = gxapi.MVIEW_GROUP_APPEND
        else:
            mode = gxapi.MVIEW_GROUP_NEW

        if name == self.viewname:
            name = name + '_'
        self.gxview.start_group(name, mode)
        self._init_pen_attributes()
        self._pen_stack = []


    def push_pen(self, pen=None):
        """
        Push current pen attributes on the pen stack, and set the pen.
        If pen not specified, all pen attributes are pushed.  pop_pen recovers
        last pen pushed.

        :param pen: pen to set after pushing current attributes.
        """
        if pen is None:
            self._pen_stack.append(self._pen.copy())
        else:
            oldpen = {}
            for key in pen:
                oldpen[key] = self._pen[key]
            self._pen_stack.append(oldpen)
            self.pen = pen

    def pop_pen(self):
        """Pop the last pen off the pen stack."""
        if len(self._pen_stack) > 0:
            self.pen = self._pen_stack[-1]
            del self._pen_stack[-1:]

    def extent(self, extent=EXTENT_VIEW):
        xmin = gxapi.float_ref()
        ymin = gxapi.float_ref()
        xmax = gxapi.float_ref()
        ymax = gxapi.float_ref()
        self.gxview.extent(EXTENT_VIEW, UNIT_VIEW, xmin, ymin, xmax, ymax)
        if extent == EXTENT_MAP:
            xmin.value, ymin.value = self.view_to_map(xmin.value, ymin.value)
            xmax.value, ymax.value = self.view_to_map(xmax.value, ymax.value)
        return xmin.value, ymin.value, xmax.value, ymax.value

    def scale(self):
        x = 1000.0 * self.gxview.scale_mm() / self.units_per_m
        y = 1000.0 * self.gxview.scale_ymm() / self.units_per_m
        return x, y

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

    def map_to_view(self, x, y):
        xr = gxapi.float_ref()
        xr.value = x * 1000.0
        yr = gxapi.float_ref()
        yr.value = y * 1000.0
        self.gxview.plot_to_view(xr, yr)
        return xr.value, yr.value

    def view_to_map(self, x, y):
        xr = gxapi.float_ref()
        xr.value = x
        yr = gxapi.float_ref()
        yr.value = y
        self.gxview.view_to_plot(xr, yr)
        return xr.value / 10.0, yr.value / 10.0

    # drawing to a plane

    @_draw
    def graticule(self, dx=None, dy=None, ddx=None, ddy=None, style=GRATICULE_DOT):

        ext = self.extent()
        if dx is None:
            dx = (ext[2] - ext[0]) * 0.2
            ddx = dx * 0.25
        if dy is None:
            dy = (ext[3] - ext[1]) * 0.2
            ddy = dy * 0.25
        if ddy is None:
            ddy = dy * 0.25
        if ddx is None:
            ddx = dx * 0.25
        self.gxview.grid(dx, dy, ddx, ddy, style)


    @_draw
    def xy_line(self, p1, p2):
        """
        Draw a line on the current plane
        :param p1:  gxpy.geometry.Point starting
        :param p2:  gxpy.geometry.Point end

        .. versionadded:: 9.2
        """
        self.gxview.line(p1.x, p1.y, p2.x, p2.y)

    @_draw
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

    @_draw
    def xy_rectangle(self, p1, p2):
        """
        Draw a 2D rectangle on the current plane
        :param p1:  Point starting
        :param p2:  Point diagonal
        :param pen: pen to use, attribtutes modify current pen for the rectangle only

        .. versionadded:: 9.2
        """
        self.gxview.rectangle(p1.x, p1.y, p2.x, p2.y)

    @_draw
    def box_3d(self, box, pen=None):
        """
        Draw a 3D box on the current plane
        :param box: geometry.Box
        :param pen: pen to use

        .. versionadded:: 9.2
        """
        self.gxview.box_3d(box.p1.x, box.p1.y, box.p1.z,
                           box.p2.x, box.p2.y, box.p2.z)


class GXview3d(GXview):

    def __init__(self, *args, **kwds):

        if 'viewname' not in kwds:
            kwds['viewname'] = "_unnamed_3D_view"
        super().__init__(*args, **kwds)

        mminx, mminy, mmaxx, mmaxy = self.extent(EXTENT_MAP)
        vminx, vminy, vmaxx, vmaxy = self.extent(EXTENT_VIEW)

        # construct a 3D view

        h3dn = gxapi.GX3DN.create()
        pov = (4., 20., 25.)
        pov = (5., 0., 90.)
        h3dn.set_point_of_view(pov[0], pov[1], pov[2])
        render = (0, 0, 'x', 'y', 'z')
        h3dn.set_render_controls(render[0], render[1], render[2], render[3], render[4])
        self.gxview.set_h_3dn(h3dn)
        self.gxview.fit_map_window_3d(mminx, mminy, mmaxx, mmaxy,
                                      vminx, vminy, vmaxx, vmaxy)


