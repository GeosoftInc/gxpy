import atexit
from functools import wraps

import geosoft
import geosoft.gxapi as gxapi
from . import vv as gxvv
from . import geometry as gxgm
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

UNIT_VIEW = 0
UNIT_MAP = 2
UNIT_VIEW_UNWARPED = 3

#TODO - add and test once bug if fixed
# GRATICULE_DOT = 0 # disabled due to a bug
GRATICULE_LINE = 1
GRATICULE_CROSS = 2

_weight_factor = (1.0 / 48.0, 1.0 / 24.0, 1.0 / 16.0, 1.0 / 12.0, 0.145, 1.0 / 4.0)
FONT_WEIGHT_ULTRALIGHT = 1
FONT_WEIGHT_LIGHT = 2
FONT_WEIGHT_MEDIUM = 3
FONT_WEIGHT_BOLD = 4
FONT_WEIGHT_XBOLD = 5
FONT_WEIGHT_XXBOLD = 6

C_RGB = 0
C_CMY = 1
C_HSV = 2

C_BLACK = 33554432
C_RED = 33554687
C_GREEN = 33619712
C_BLUE = 50266112
C_CYAN = 50331903
C_MAGENTA = 50396928
C_YELLOW = 67043328
C_GREY = 41975936
C_LT_RED = 54542336
C_LT_GREEN = 54526016
C_LT_BLUE = 50348096
C_LT_CYAN = 50331712
C_LT_MAGENTA = 50348032
C_LT_YELLOW = 54525952
C_LT_GREY = 54542400
C_GREY10 = 51910680
C_GREY25 = 54542400
C_GREY50 = 41975936
C_WHITE = 50331648
C_TRANSPARENT = 0

class Color:
    """
    Colours, which are stored in a Windows-compatible 24-bit colour integer.
    
    :param color:   string descriptor, tuple (r, g, b), (c, m, y) or (h, s, v), each item defined in the range
                    0 to 255, or a 24-bit color number, which can be an item selected from the following list:
                    
                    ::
                    
                        C_BLACK
                        C_RED
                        C_GREEN
                        C_BLUE
                        C_CYAN
                        C_MAGENTA
                        C_YELLOW
                        C_GREY
                        C_LT_RED
                        C_LT_GREEN
                        C_LT_BLUE
                        C_LT_CYAN
                        C_LT_MAGENTA
                        C_LT_YELLOW
                        C_LT_GREY
                        C_GREY10
                        C_GREY25
                        C_GREY50
                        C_WHITE
                        C_TRANSPARENT
                        
    :param model:   model of the tuple: C_RGB, C_CMY or C_HSV.  Default is C_RGB
    
    .. versionadded:: 9.2
    """

    def __init__(self, color, model=C_RGB):

        def get_part(cstr, c, default=255):
            if c not in cstr:
                return default, cstr
            start = cstr.index(c)
            end = start + 1
            for c in cstr[end:]:
                if not (c in '0123456789'):
                    break
                end += 1
            return_cstr = cstr[:start] + cstr[end:]
            if end == start+1:
                return default, return_cstr
            return int(cstr[start+1:end]), return_cstr

        if type(color) is str:

            #self.thickness, color = get_part(color, 't', default=0)
            self._color = gxapi.GXMVIEW.color(color)

        elif type(color) is int:
            self._color = color

        elif model == C_RGB:
            self.rgb = color

        elif model == C_CMY:
            self.cmy = color

        elif model == C_HSV:
            hue = max(0, min(255, color[0]))
            sat = max(0, min(255, color[1]))
            val = max(0, min(255, color[2]))
            self._color = gxapi.GXMVIEW.color_hsv(hue, sat, val)

    @property
    def int(self):
        return self._color

    @int.setter
    def int(self, color):
        self.color = int(color)

    @property
    def rgb(self):
        r = gxapi.int_ref()
        g = gxapi.int_ref()
        b = gxapi.int_ref()
        gxapi.GXMVIEW.color2_rgb(self._color, r, g, b)
        return (r.value, g.value, b.value)

    @rgb.setter
    def rgb(self, rgb):
        r = max(min(255, rgb[0]), 0)
        g = max(min(255, rgb[1]), 0)
        b = max(min(255, rgb[2]), 0)
        self._color = gxapi.GXMVIEW.color_rgb(r, g, b)

    @property
    def cmy(self):
        red, green, blue = self.rgb
        return 255 - red, 255 - green, 255 - blue

    @cmy.setter
    def cmy(self, cmy):
        self.rgb = (255 - cmy[0], 255 - cmy[1], 255 - cmy[2])


def font_weight_from_line_thickness(thickness, height):
    """
    Returns font weight from the defined text height and line thickness.
    :param thickness: line thickness in same units as the text height
    :param height: text height
    
    :returns: one of:
    
            ::
            
                FONT_WEIGHT_ULTRALIGHT
                FONT_WEIGHT_LIGHT
                FONT_WEIGHT_MEDIUM
                FONT_WEIGHT_BOLD
                FONT_WEIGHT_XBOLD
                FONT_WEIGHT_XXBOLD

    .. versionadded:: 9.2
    """
    if height <= 0.:
        return FONT_WEIGHT_ULTRALIGHT
    ratio = thickness / height
    fw = 1
    for f in _weight_factor:
        if ratio <= f:
            return fw
        fw += 1
    return FONT_WEIGHT_MEDIUM

def thickness_from_font_weight(weight, height):
    """ Returns line thickness appropriate for a text weight."""
    return height * _weight_factor[weight - 1]

class Text_def:
    """
    Text definition:
    
    :param font:        font name.  TrueType fonts are assumed unless the name ends with '.gfn',
                        which is a Geosoft gfn font.
    :param weight:      one of:
    
                        ::
                        
                            FONT_WEIGHT_ULTRALIGHT
                            FONT_WEIGHT_LIGHT
                            FONT_WEIGHT_MEDIUM
                            FONT_WEIGHT_BOLD
                            FONT_WEIGHT_XBOLD
                            FONT_WEIGHT_XXBOLD
                    
    :param thickness:   line thickness from which to determine a weight, which is calculated from the 
                        ration of line thickness to height.
    :param italics:     True for italics fonts
    :param height:      text height in map mm.
    
    :properties:
    
        :height:        font height in 
        :font:          font name
        :weight:        font weight, one of FONT_WEIGHT_
        :thickness:     font line thickness for gfn stroke fonts
        :italics:       True for italics
        :slant:         Slant angle for stroke fonts, 0 if normal, 15 for italics
        :mapplot_text:  mapplot compatible text definition string
    """
    def __init__(self,
                 height=2.5,
                 font='DEFAULT',
                 weight=None,
                 thickness=None,
                 italics=False):
        self._font = font
        self._weight = weight
        self._thickness = thickness
        if type(italics) is bool:
            self._italics = italics
        elif italics > 5:
            self.italics = True
        else:
            italics = False
        self._height = height

        if weight is None:
            if thickness is None:
                self._weight = FONT_WEIGHT_MEDIUM
            else:
                self._weight = font_weight_from_line_thickness(thickness, height)

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, font):
        if font:
            self._font = font
        else:
            self._font = 'DEFAULT'

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def thickness(self):
        return thickness_from_font_weight(self._weight, self._height)

    @thickness.setter
    def thickness(self, thickness):
        self._weight = font_weight_from_line_thickness(thickness, self._height)

    @property
    def italics(self):
        return self._italics

    @italics.setter
    def italics(self, italics):
        if type(italics) is bool:
            self._italics = italics
        elif italics > 5:
            self._italics = True
        else:
            self._italics = False

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def slant(self):
        if self._italics:
            return 15
        else:
            return 0

    @slant.setter
    def slant(self, slant):
        if slant > 5:
            self._italics = True
        else:
            self._italics = False

    @property
    def mapplot_text(self):
        if '.gfn' in self._font.lower():
            font = self._font.lower().replace('.gfn','')
        elif 'default' in self._font.lower():
            font = 'DEFAULT'
        else:
            font = self._font.strip() + '(TT)'
        return '{},,,{},{}'.format(self.height, self.slant, font)

class Pen:

    def __init__(self,
                 color,
                 thickness,
                 line_style,
                 line_pitch,
                 fill_color):
        pass

# decorators
def _draw(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self._pen:
            self.start_group('_')
        if 'pen' in kwargs:
            self.push_pen(kwargs.pop('pen'))
            func(self, *args, **kwargs)
            self.pop_pen()
        else:
            func(self, *args, **kwargs)

    return wrapper


def _make_Point2(p2):
    if type(p2) is gxgm.Point2:
        return p2
    else:
        return gxgm.Point2(p2)

class GXview:
    """
    Geosoft view class.

    :parameters:
    
        :viewname:      view name, default is "_unnamed_view".
        :gmap:          map instance, if not specified a new default map is created and deleted on closing
        :mode:          open view mode:

                        ::

                            gxpy.view.READ_ONLY
                            gxpy.view.WRITE_NEW
                            gxpy.view.WRITE_OLD

        The following are used with ``mode=gxpy.view.WRITE_NEW``:
        
        :cs:            coordinate system as a gxpy.coordinate_system.GXcs instance, or one of the GXcs
                        constructor types.
        :map_location:  (x, y) view location on the map, in map cm
        :area:          (min_x, min_y, max_x, max_y) area in view units
        :scale:         Map scale if a coordinate system is defined.  If the coordinate system is not
                        defined this is view units per map metre.
        :copy:          name of a view to copy into the new view.

    :properties:
    
        :gmap:              the GXmap instance that contains this view
        :viewname:          the name of the view
        :units_per_metre:   view units per view metres (eg. a view in 'ft' will be 3.28084).
        :units_per_map_cm:  view units per map cm. (eg. a view in ft, with a scale of 1:12000 returns 393.7 ft/cm)
        :unit_name:         view units name.
        :scale:             view scale, which is the # of view units per  unit on the printed map.
        :aspect:            ratio of the view x units to y units (x/y).  Usually this is 1.0.
        :extent:            extent of the visible (clipped) view in view units.
        :extent_map_cm:     extent of the visible view in map cm.
        
    .. versionadded:: 9.2
    """

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self._close()

    def _close(self):
        if self._open:
            #TODO revisit why failing to free _pen, _pen_fn and _pen_stack fails once we have cython interface.  Jacques suspects boost.
            self.gxview = None
            self._pen = None
            self._pen_fn = None
            self._pen_stack = None
            self._gmap = None
            self._open = False

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self._viewname

    def __init__(self,
                 gmap,
                 viewname="_unnamed_view",
                 mode=WRITE_OLD,
                 cs=None,
                 map_location=(0,0),
                 area=(0,0,30,20),
                 scale=100,
                 copy=None):

        self._gmap = gmap
        self._viewname = viewname
        if mode == WRITE_OLD and not gmap.has_view(self._viewname):
            mode = WRITE_NEW
        self.gxview = gxapi.GXMVIEW.create(self._gmap.gxmap, self._viewname, mode)
        self._mode = mode
        self._pen = {}
        self._pen_fn = {}
        self._pen_stack = []

        atexit.register(self._close)
        self._open = True
        
        if mode == WRITE_NEW:
            self.locate(cs, map_location, area, scale)

            if copy:
                with GXview(gmap, viewname=copy, mode=READ_ONLY) as v:
                    v.gxview.mark_all_groups(1)
                    v.gxview.copy_marked_groups(self.gxview)

        else:
            ipj = gxapi.GXIPJ.create()
            self.gxview.get_ipj(ipj)
            self.cs = self.drawing_cs = gxcs.GXcs(ipj)
            metres_per = self.cs.units_to_metres
            self._uname = self.cs.units_name
            if metres_per <= 0.:
                raise ViewException('Invalid units {}({})'.format(self._uname, metres_per))
            self._units_to_metres = 1.0/metres_per

    def set_cs(self, cs):
        """
        Set the coordinate system of the view.

        :param cs:  coordinate system as a gxpy.coordinate_system.GXcs instance, or one of the GXcs
                    constructor types.

        .. versionadded:: 9.2
        """
        self.cs = self.drawing_cs = gxcs.GXcs(cs)
        metres_per = self.cs.units_to_metres
        self._uname = self.cs.units_name
        if metres_per <= 0.:
            raise ViewException('Invalid units {}({})'.format(self._uname, metres_per))
        self._units_to_metres = 1.0/metres_per
        self.gxview.set_ipj(self.cs.gxipj)

    def set_drawing_cs(self, cs=None):
        """
        Set the coordinate system of drawing coordinates.  Subsequent drawing methods are assumed to be in this
        coordinate system and will be re-projected to the view coordinate system.

        If called with no defined coordinate system the drawing coordinate system is reset to the
        view coordinate system.

        :param cs:  coordinate system as a gxpy.coordinate_system.GXcs instance, or one of the GXcs
                    constructor types.

        .. versionadded:: 9.2
        """
        if cs is None:
            self.gxview.set_user_ipj(self.cs.gxipj)
            self.drawing_cs = self.cs
        else:
            self.drawing_cs = gxcs.GXcs(cs).gxipj
            self.gxview.set_user_ipj(self.drawing_cs)

    def locate(self,
               cs=None,
               map_location=None,
               area=None,
               scale=None):
        """
        Locate and scale the view on the map.

        :parameters:
            :cs:            coordinate system as a gxpy.coordinate_system.GXcs instance, or one of the GXcs
                            constructor types.
            :map_location:  New (x, y) view location on the map, in map cm.
            :area:          New (min_x, min_y, max_x, max_y) area in view units
            :scale:         New scale in view units per map metre, either as a single value or
                            (x_scale, y_scale)

        .. versionadded:: 9.2
        """

        if self._mode == READ_ONLY:
            raise ViewException('Cannot modify a READ_ONLY view.')

        # coordinate system
        self.set_cs(cs)
        upm = 1.0 / self.cs.units_to_metres

        if area == None:
            area = self.extent

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
        #self.gxview.set_u_fac(1.0 / x_scale)

    def _invalid_pen(self, key):
        raise ViewException(_t('Invalid pen attribute \'{}\'. Valid attibutes are {}')
                            .format(key, list(self._pen)))

    @property
    def gmap(self):
        """ gxpy.GXmap instance that contains this view."""
        return self._gmap

    @property
    def viewname(self):
        """ Name of the view"""
        return self._viewname

    @property
    def units_per_metre(self):
        return self._units_to_metres

    @property
    def units_per_map_cm(self):
        return self.gxview.scale_mm() * 10.0

    @property
    def units_name(self):
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
            try:
                if self._pen[att] != setting:
                    self._pen_fn[att](setting)
                    self._pen[att] = setting
            except:
                self._invalid_pen(att)

    @property
    def extent(self):
        xmin = gxapi.float_ref()
        ymin = gxapi.float_ref()
        xmax = gxapi.float_ref()
        ymax = gxapi.float_ref()
        self.gxview.extent(gxapi.MVIEW_EXTENT_UNIT_VIEW, UNIT_VIEW, xmin, ymin, xmax, ymax)
        return xmin.value, ymin.value, xmax.value, ymax.value

    @property
    def extent_map_cm(self):

        ex = self.extent
        xmin, ymin = self.view_to_map(ex[0], ex[1])
        xmax, ymax = self.view_to_map(ex[2], ex[3])
        return xmin, ymin, xmax, ymax

    @property
    def scale(self):
        return 1000.0 * self.gxview.scale_mm() * self.cs.units_to_metres

    @property
    def aspect(self):
        return self.gxview.scale_ymm() / self.gxview.scale_mm()

    def _line_style(self, ls):
        self.gxview.line_style(ls[0], ls[1])

    def _init_pen_attributes(self):

        # set the default pen characteristics, initializes pen dictionaries

        def setpen(att, fn, setting):
            fn(setting)
            self._pen[att] = setting
            self._pen_fn[att] = fn

        self._pen_stack = []
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

    def delete_group(self, group_name):
        """
        Delete a group from a map. Nothing happens if the view does not contain this group.
        
        :param group_name: Name of the group to delete.

        .. versionadded:: 9.2
        """

        self.gxview.delete_group(group_name)

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
                try:
                    oldpen[key] = self._pen[key]
                except KeyError:
                    self._invalid_pen(key)
            self._pen_stack.append(oldpen)
            self.pen = pen

    def pop_pen(self):
        """Pop the last pen off the pen stack."""
        if len(self._pen_stack) > 0:
            self.pen = self._pen_stack[-1]
            del self._pen_stack[-1:]

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
    def graticule(self, dx=None, dy=None, ddx=None, ddy=None, style=GRATICULE_LINE):
        """
        Draw a graticule reference on a view.
        
        :param style:   ``GRATICULE_LINE`` or ``GRATICULE_CROSS``
        :param dx:      vertical line separation
        :param dy:      horizontal line separation
        :param ddh:     horizontal cross size for ``GRATICULE_CROSS``
        :param ddv:     vertical cross size for ``GRATICULE_CROSS``
        
        .. versionadded:: 9.2
        """

        ext = self.extent
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
    def xy_line(self, p2):
        """
        Draw a line on the current plane
        :param p2: geometry.Point2, or (p1, p2)

        .. versionadded:: 9.2
        """

        p2 = _make_Point2(p2)
        self.gxview.line(p2.p1.x, p2.p1.y, p2.p2.x, p2.p2.y)

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
                                 gxvv.GXvv(pp.x)._vv,
                                 gxvv.GXvv(pp.y)._vv)
        else:
            self.gxview.poly_line(gxapi.MVIEW_DRAW_POLYLINE,
                                 gxvv.GXvv(pp.x)._vv,
                                 gxvv.GXvv(pp.y)._vv)

    @_draw
    def xy_rectangle(self, p2):
        """
        Draw a 2D rectangle on the current plane
        :param p2: geometry.Point2, or (p1, p2), or (x0, y0, x2, y2)

        .. versionadded:: 9.2
        """

        p2 = _make_Point2(p2)
        self.gxview.rectangle(p2.p1.x, p2.p1.y, p2.p2.x, p2.p2.y)

    @_draw
    def box_3d(self, p2, pen=None):
        """
        Draw a 3D box
        :param p2: geometry.Point2, or (p1, p2), or (x0, y0, x1, y1)

        .. versionadded:: 9.2
        """

        p2 = _make_Point2(p2)
        self.gxview.box_3d(p2.p1.x, p2.p1.y, p2.p1.z,
                           p2.p2.x, p2.p2.y, p2.p2.z)

    def aggregate(self, agg, name=None):
        """
        Add an aggregate to a view
        :param agg:     GXagg instance
        :param name:    group name, default is the aggregate string
        :return:
        """

        if name is None:
            name = str(agg)

        self.gxview.aggregate(agg.gxagg, name)


class GXview3d(GXview):


    def __init__(self, *args, **kwds):

        if 'viewname' not in kwds:
            kwds['viewname'] = "_unnamed_3D_view"
        super().__init__(*args, **kwds)

        mminx, mminy, mmaxx, mmaxy = self.extent_map_cm
        vminx, vminy, vmaxx, vmaxy = self.extent

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


