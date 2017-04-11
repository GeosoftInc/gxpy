import atexit
from functools import wraps
import threading

import geosoft
import geosoft.gxapi as gxapi
from . import vv as gxvv
from . import geometry as gxgm
from . import coordinate_system as gxcs
from . import view as gxv

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class GroupException(Exception):
    """
    Exceptions from this module.

    .. versionadded:: 9.2
    """
    pass

GROUP_NAME_SIZE = 2080
NEW = gxapi.MVIEW_GROUP_NEW
APPEND = gxapi.MVIEW_GROUP_APPEND
READ_ONLY = max(NEW, APPEND) + 1

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

# TODO - add and test once bug if fixed
# GRATICULE_DOT = 0 # disabled due to a bug
GRATICULE_LINE = 1
GRATICULE_CROSS = 2

LINE_STYLE_SOLID = 1
LINE_STYLE_LONG = 2
LINE_STYLE_DOTTED = 3
LINE_STYLE_SHORT = 4
LINE_STYLE_LONG_SHORT_LONG = 5
LINE_STYLE_LONG_DOT_LONG = 6

SYMBOL_NONE = 0
SYMBOL_DOT = 1
SYMBOL_PLUS = 2
SYMBOL_X = 3
SYMBOL_BOX = 4
SYMBOL_TRIANGLE = 5
SYMBOL_INVERTED_TRIANGLE = 6
SYMBOL_HEXAGON = 7
SYMBOL_SMALL_BOX = 8
SYMBOL_SMALL_DIAMOND = 9

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

C_BLACK = 67108863
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

REF_BOTTOM_LEFT = 0
REF_BOTTOM_CENTER = 1
REF_BOTTOM_RIGHT = 2
REF_CENTER_LEFT = 3
REF_CENTER = 4
REF_CENTER_RIGHT = 5
REF_TOP_LEFT = 6
REF_TOP_CENTER = 7
REF_TOP_RIGHT = 8

GROUP_ALL = 0
GROUP_MARKED = 1
GROUP_VISIBLE = 2
GROUP_AGG = 3
GROUP_CSYMB = 4
GROUP_VOXD = 5

LOCATE_FIT = gxapi.MVIEW_RELOCATE_FIT
LOCATE_FIT_KEEP_ASPECT = gxapi.MVIEW_RELOCATE_ASPECT
LOCATE_CENTER = gxapi.MVIEW_RELOCATE_ASPECT_CENTER

def edge_reference(area, ref):
    """
    Location of a reference point of an area.
    :param area:        Point2 instance, or (x0, y0, x1, y1)
    :param ref:         reference point from REF_ define group corner at this location.
    
    :returns: Point     desired reference location as a Point

    .. versionadded:: 9.2
    """
    if not isinstance(area, gxgm.Point2):
        area = gxgm.Point2(area)
    centroid = area.centroid
    half_dim = gxgm.Point(area.dimension) * 0.5
    xoff = yoff = 0.0
    if ref in (0, 1, 2):
        yoff = -half_dim.y
    elif ref in (6, 7, 8):
        yoff = half_dim.y
    if ref in (0, 3, 6):
        xoff = -half_dim.x
    elif ref in (2, 5, 8):
        xoff = half_dim.x

    return centroid + gxgm.Point((xoff, yoff))

class GXgroup:
    """
    Geosoft group class.

    :parameters:

        :view:          gxpy.GXview
        :groupname:     group name, default is "_".
        :view_lock:     True to lock the view for a single-stream drawwing group.  Default is False.

    :properties:

        :view:              the GXview instance that contains this group
        :name:              the name of the group
        :extent:            extent of the group in view units
        :extent_map_cm:     extent of the group in map cm
        :drawing_cs:        the coordinate system of drawing coordinates. Setting to None will reset drawing
                            coordinates to the view cs.  If ``drawing_cs`` is set to some other cs the drawing
                            coordinates will be transformed into the view cs.

    .. versionadded:: 9.2
    """

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self._close()

    def _close(self):
        if self._open:
            try:
                self._drawing_cs = None
                self._pen = None
                self._text_def = None
            finally:
                self.view.lock = False
                self._open = False

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return '{}/{}'.format(self.name, self.view.name)

    def __init__(self,
                 view,
                 name='_',
                 view_lock=False,
                 mode=APPEND):

        if (len(name) == 0) or (name == view.name):
            name = name + '_'

        _lock = threading.Lock()
        _lock.acquire()
        try:
            if view.lock:
                raise GroupException(_t('This view is locked by group {}.'.format(view.lock)))
            if view_lock:
                view.lock = name
        finally:
            _lock.release()

        self._view = view
        self._name = name

        self._mode = mode
        self._view.gxview.start_group(name, mode)

        atexit.register(self._close)
        self._open = True

    @property
    def view(self):
        return self._view

    @property
    def name(self):
        return self._name

    def _extent(self, unit=UNIT_VIEW):
        xmin = gxapi.float_ref()
        ymin = gxapi.float_ref()
        xmax = gxapi.float_ref()
        ymax = gxapi.float_ref()
        self.view.gxview.get_group_extent(self.name, xmin, ymin, xmax, ymax, unit)
        return xmin.value, ymin.value, xmax.value, ymax.value

    @property
    def extent(self):
        return self._extent(UNIT_VIEW)

    def extent_map_cm(self, extent=None):
        """
        Return a view extent in map cm.

        :param extent: tuple returned an extent property.

        .. versionadded:: 9.2
        """
        if extent is None:
            extent = self.extent
        xmin, ymin = self.view.view_to_map_cm(extent[0], extent[1])
        xmax, ymax = self.view.view_to_map_cm(extent[2], extent[3])

        return xmin, ymin, xmax, ymax

    def locate(self, location, ref=REF_CENTER):
        """
        Locate the group relative to a point.

        :param location:    location (x, y) or a ``gxpy.geometry.Point``
        :param ref:         locate the REF_ define group corner at this location.

        .. versionadded:: 9.2
        """
        area = gxgm.Point2(self.extent)
        area -= area.centroid
        area -= edge_reference(area, ref)
        area += location
        self.view.gxview.relocate_group(self.name,
                                        area.p1.x, area.p1.y, area.p2.x, area.p2.y,
                                        gxapi.MVIEW_RELOCATE_ASPECT_CENTER)

def _draw(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self._mode == READ_ONLY:
            raise _t('This view is read-only.')
        if not self._pen:
            self._init_pen()
        if 'pen' in kwargs:
            cur_pen = self.pen
            self.pen = kwargs.pop('pen')
            try:
                func(self, *args, **kwargs)
            except:
                raise
            finally:
                self.pen = cur_pen
        else:
            func(self, *args, **kwargs)

    return wrapper


class GXdraw(GXgroup):
    """
    Create (start) a drawing group for 2D drawing elements.  On a 3D view, 2D drawing elements
    are placed on the default drawing plane.  Drawing groups will lock the view such that only one
    drawing group can be instantiated at a time.
    
    Use ``with GXdraw() as group:`` to ensure correct unlocking when complete.
    
    Inherits from the ``GXgroup`` base class.
    """

    @staticmethod
    def _make_Point2(p2):
        if type(p2) is gxgm.Point2:
            return p2
        else:
            return gxgm.Point2(p2)


    def __init__(self, *args, **kwargs):

        kwargs['view_lock'] = True
        super().__init__(*args, **kwargs)

        self._pen = None
        self._text_def = None
        self._drawing_cs = self.view.cs

        if self._mode != READ_ONLY:
            self._init_pen()
            self._text_def = Text_def(factor=self.view.units_per_map_cm)

    @property
    def drawing_cs(self):
        return self._drawing_cs

    @drawing_cs.setter
    def drawing_cs(self, cs):
        if cs is None:
            self.view.gxview.set_user_ipj(self.view.cs.gxipj)
            self._drawing_cs = self.view.cs
        else:
            self._drawing_cs = gxcs.GXcs(cs).gxipj
            self.view.gxview.set_user_ipj(self._drawing_cs)

    @property
    def pen(self):
        return self._pen

    @pen.setter
    def pen(self, pen):

        if self._mode == READ_ONLY:
            raise _t('This view is read-only.')

        if type(pen) is str:
            pen = Pen.from_mapplot_string(pen)
        if self._pen.line_color != pen.line_color:
            self.view.gxview.line_color(pen._line_color.int)
        if self._pen.line_thick != pen.line_thick:
            self.view.gxview.line_thick(pen.line_thick)
        if self._pen.line_smooth != pen.line_smooth:
            self.view.gxview.line_smooth(pen.line_smooth)
        if (self._pen.line_style != pen.line_style) or (self._pen.line_pitch != pen.line_pitch):
            self.view.gxview.line_style(pen.line_style, pen.line_pitch)
        if self._pen.fill_color != pen.fill_color:
            self.view.gxview.fill_color(pen._fill_color.int)
        if self._pen.pat_number != pen.pat_number:
            self.view.gxview.pat_number(pen.pat_number)
        if self._pen.pat_angle != pen.pat_angle:
            self.view.gxview.pat_angle(pen.pat_angle)
        if self._pen.pat_density != pen.pat_density:
            self.view.gxview.pat_density(pen.pat_density)
        if self._pen.pat_size != pen.pat_size:
            self.view.gxview.pat_size(pen.pat_size)
        if self._pen.pat_style != pen.pat_style:
            self.view.gxview.pat_style(pen.pat_style)
        if self._pen.pat_thick != pen.pat_thick:
            self.view.gxview.pat_thick(pen.pat_thick)

        self._pen = pen

    def _init_pen(self):

        scm = self.view.units_per_map_cm
        pen = Pen(line_thick=0.02 * scm,
                  line_pitch=0.5 * scm,
                  pat_size=0.25 * scm,
                  pat_thick=0.02 * scm)

        self.view.gxview.line_color(pen.line_color.int)
        self.view.gxview.line_thick(pen.line_thick)
        self.view.gxview.line_smooth(pen.line_smooth)
        self.view.gxview.line_style(pen.line_style, pen.line_pitch)
        self.view.gxview.fill_color(pen.fill_color.int)
        self.view.gxview.pat_number(pen.pat_number)
        self.view.gxview.pat_angle(pen.pat_angle)
        self.view.gxview.pat_density(pen.pat_density)
        self.view.gxview.pat_size(pen.pat_size)
        self.view.gxview.pat_style(pen.pat_style)
        self.view.gxview.pat_thick(pen.pat_thick)

        self._pen = pen

    def new_pen(self, **kwargs):
        """
        Returns a pen that inherits default from the current view pen.  Arguments are the same
        as the ``Pen`` constructor.  This using this ensures that default sizing of view unit-based
        dimensions (such as ``line_thick``) are not lost when new pens are created.

        :param kwargs: see ``Pen``
        :return: Pen instance

        .. versionadded:: 9.2
        """
        return Pen(default=self.pen, **kwargs)

    @property
    def text_def(self):
        return self._text_def

    @text_def.setter
    def text_def(self, text_def):
        if self._mode == READ_ONLY:
            raise _t('This view is read-only.')
        if self._text_def != text_def:
            self._text_def = text_def
            self.view.gxview.text_font(text_def.font,
                                  text_def.gfn,
                                  text_def.weight,
                                  text_def.italics)
            self.view.gxview.text_size(text_def.height)
            self.view.gxview.text_color(text_def.color.int)


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

        You must stay in the same color model, RGB, CMY,
        HSV or K.

        For example "R", "R127G22", "H255S127V32"

        Characters are not case sensitive.
        """

        return self.view.gxview.color(str)

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
        self.view.gxview.grid(dx, dy, ddx, ddy, style)

    @_draw
    def xy_line(self, p2):
        """
        Draw a line on the current plane
        :param p2: geometry.Point2, or (p1, p2)

        .. versionadded:: 9.2
        """

        p2 = self._make_Point2(p2)
        self.view.gxview.line(p2.p1.x, p2.p1.y, p2.p2.x, p2.p2.y)

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
            self.view.gxview.poly_line(gxapi.MVIEW_DRAW_POLYGON,
                                  gxvv.GXvv(pp.x)._vv,
                                  gxvv.GXvv(pp.y)._vv)
        else:
            self.view.gxview.poly_line(gxapi.MVIEW_DRAW_POLYLINE,
                                  gxvv.GXvv(pp.x)._vv,
                                  gxvv.GXvv(pp.y)._vv)

    @_draw
    def xy_rectangle(self, p2):
        """
        Draw a 2D rectangle on the current plane
        :param p2: geometry.Point2, or (p1, p2), or (x0, y0, x2, y2)

        .. versionadded:: 9.2
        """

        p2 = self._make_Point2(p2)
        self.view.gxview.rectangle(p2.p1.x, p2.p1.y, p2.p2.x, p2.p2.y)

    def text(self,
             text,
             location=(0,0),
             reference=REF_BOTTOM_LEFT,
             angle=0.,
             text_def=None):
        """
        Draw text in the view.
        
        :param text:        text string.  Use line-feed characters for multi-line text.
        :param location:    (x, y) or a ``gxpy.geomerty.Point`` location
        :param reference:   one of TEXT_REF_ defines that locates text relative to the location
        :param angle:       baseline angle in degrees clockwise
        :param text_def:    text definition, if not set the current definition is used
        :param line_spacing: the line spacing for multi-line text as a factor of the text height, default is 1.5

        .. versionadded:: 9.2
        """

        if text_def:
            cur_text = self._text_def
            self.text_def = text_def
        else:
            cur_text = None

        self.view.gxview.text_ref(reference)
        self.view.gxview.text_angle(angle)
        if type(location) is not gxgm.Point:
            location = gxgm.Point(location)
        self.view.gxview.text(text, location.x, location.y)

        if cur_text:
            self.text_def = cur_text

class GXdraw_3d(GXdraw):

    def __init__(self, view, *args, **kwargs):

        if not isinstance(view, gxv.GXview3d):
            raise GroupException(_t('View is not 3D'))

        super().__init__(view, *args, **kwargs)

    @_draw
    def box_3d(self, p2, pen=None):
        """
        Draw a 3D box
        :param p2: geometry.Point2, or (p1, p2), or (x0, y0, x1, y1)

        .. versionadded:: 9.2
        """

        p2 = self._make_Point2(p2)
        self.view.gxview.box_3d(p2.p1.x, p2.p1.y, p2.p1.z,
                                p2.p2.x, p2.p2.y, p2.p2.z)

class Color:
    """
    Colours, which are stored as a 24-bit color integer.

    :param color:   string descriptor (eg. 'R255G0B125'), color letter R, G, B, C, M, Y, H, S or V.;
                    tuple (r, g, b), (c, m, y) or (h, s, v), each item defined in the range 0 to 255;
                    24-bit color number, which can be an item selected from the following list:

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

        if type(color) is Color:
            self._color = color.int

        elif type(color) is int:
            self._color = color

        elif type(color) is str:
            self._color = gxapi.GXMVIEW.color(color)

        elif model == C_CMY:
            self.cmy = color

        elif model == C_HSV:
            hue = max(0, min(255, color[0]))
            sat = max(0, min(255, color[1]))
            val = max(0, min(255, color[2]))
            self._color = gxapi.GXMVIEW.color_hsv(hue, sat, val)

        else:
            self.rgb = color

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return self.__dict__ != other.__dict__

    @property
    def int(self):
        return self._color

    @int.setter
    def int(self, color):
        self.color = int(color)

    @property
    def rgb(self):
        if self.int == 0:
            return None
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
        if self.int == 0:
            return None
        red, green, blue = self.rgb
        return 255 - red, 255 - green, 255 - blue

    @cmy.setter
    def cmy(self, cmy):
        self.rgb = (255 - cmy[0], 255 - cmy[1], 255 - cmy[2])


def font_weight_from_line_thickness(line_thick, height):
    """
    Returns font weight for a text height and line thickness.

    :param line_thick:  line thickness in same units as the text height
    :param height:      text height

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
    ratio = line_thick / height
    fw = 1
    for f in _weight_factor:
        if ratio <= f:
            return fw
        fw += 1
    return FONT_WEIGHT_MEDIUM


def thickness_from_font_weight(weight, height):
    """ 
    Returns the line thickness appropriate for a text weight.

    :param weight: one of:

            ::

                FONT_WEIGHT_ULTRALIGHT
                FONT_WEIGHT_LIGHT
                FONT_WEIGHT_MEDIUM
                FONT_WEIGHT_BOLD
                FONT_WEIGHT_XBOLD
                FONT_WEIGHT_XXBOLD

    :param height:  font height

    .. versionadded:: 9.2
    """
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

    :param line_thick:  line thickness from which to determine a weight, which is calculated from the 
                        ratio of line thickness to height.
    :param italics:     True for italics fonts
    :param height:      text height, default 0.25
    :param factor:      default spatial properties are multiplied by this factor.  This is useful
                        for creating text scaled to the units of a view.  The default text properties
                        are scaled to cm.

    :properties:

        :height:        font height in 
        :font:          font name
        :weight:        font weight, one of FONT_WEIGHT_
        :line_thick:    font line thickness for gfn stroke fonts
        :italics:       True for italics
        :slant:         Slant angle for stroke fonts, 0 if normal, 15 for italics
        :mapplot_string:  mapplot compatible text definition string

    .. versionadded:: 9.2
    """

    def __init__(self, **kwargs):

        if 'default' in kwargs:
            def_pen = kwargs.pop('default')
            self.__dict__ = def_pen.__dict__.copy()
        else:
            self.color = Color(C_BLACK)
            self.height = 0.25
            self.font = 'DEFAULT'
            self.gfn = True
            self.weight = None
            self.italics = False

        factor = kwargs.pop('factor', 1.)
        if factor != 1.0:
            self.height *= factor

        line_thick = None
        for k in kwargs:
            if k == 'color':
                self.color = kwargs[k]
            elif k == 'line_thick':
                line_thick = kwargs[k]
            elif k == 'font':
                self.font = kwargs[k]
            elif k in self.__dict__:
                self.__dict__[k] = kwargs[k]
            else:
                raise GroupException('Invalid text definition parameter ({})'.format(k))

        if self.weight is None:
            if line_thick is None:
                self.weight = FONT_WEIGHT_MEDIUM
            else:
                self.weight = font_weight_from_line_thickness(line_thick, self.height)

    def __eq__(self, other):
        try:
            return self.__dict__ == other.__dict__
        except:
            return False

    def __ne__(self, other):
        return self.__dict__ != other.__dict__

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if type(color) is Color:
            self._color = color
        else:
            self._color = Color(color)

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, font):
        if font:
            if '.gfn' in font.lower():
                self.gfn = True
                self._font = font.lower().replace('.gfn', '')
            else:
                self.gfn = False
                self._font = font.replace('(TT)', '')
        else:
            self._font = 'DEFAULT'
            self.gfn = True

    @property
    def line_thick(self):
        return thickness_from_font_weight(self.weight, self.height)

    @line_thick.setter
    def line_thick(self, line_thick):
        self.weight = font_weight_from_line_thickness(line_thick, self.height)

    @property
    def slant(self):
        if self.italics:
            return 15
        else:
            return 0

    @slant.setter
    def slant(self, slant):
        if slant > 5:
            self.italics = True
        else:
            self.italics = False

    @property
    def mapplot_string(self):
        """
        Return a text definition for mapplot.
        :return: 
        """
        if 'default' in self._font.lower():
            font = 'DEFAULT'
        elif not self.gfn:
            font = self._font.strip() + '(TT)'
        else:
            font = self._font
        return '{},,,{},"{}"'.format(self.height, self.slant, font)


class Pen:
    """
    Geosoft Pen class.  Default dimensioned proprties (line_thick, line_pitch,
    pat_size and pat_thick) are scaled assuming scale units are cm.  To scale
    a pen to view units, use Pen.scaled(units_per_cm) to create a default
    pen scaled to the units of a view.

    :param line_color:  line Color instance, default is black
    :param fill_color:  fill Color instance, default is transparent
    :param line_thick:  line thickness, default is 0.01
    :param line_style:  line pattern style

                        ::

                            LINE_STYLE_SOLID (default)
                            LINE_STYLE_LONG
                            LINE_STYLE_DOTTED
                            LINE_STYLE_SHORT
                            LINE_STYLE_LONG_SHORT_LONG
                            LINE_STYLE_LONG_DOT_LONG

    :param line_pitch:  line style pitch, default is 0.5
    :param line_smooth: smooth line:

                        ::

                            SMOOTH_NONE (default)
                            SMOOTH_AKIMA
                            SMOOTH_CUBIC

    :param pat_number:  pattern number for filled patterns (refer to ``etc/default.pat``) default 0, flood fill
    :param pat_angle:   pattern angle, default 0
    :param pat_density: pattern density, default 1
    :param pat_size:    pattern size, default 1.0
    :param pat_style:   pattern style:

                        ::

                            TILE_RECTANGULAR (default)
                            TILE_DIAGONAL
                            TILE_TRIANGULAR
                            TILE_RANDOM

    :param pat_thick:   pattern line thickness, default 0.01
    :param default:     default Pen instance, if specified defaults are established from this
    :param factor:      default spatial properties are multiplied by this factor.  This is useful
                        for creating pens scaled to the units of a view.  The default pen properties
                        are scaled to cm.

    .. versionadded: 9.2
    """

    def __init__(self, **kwargs):

        if 'default' in kwargs:
            def_pen = kwargs.pop('default')
            self.__dict__ = def_pen.__dict__.copy()
        else:
            self.line_color = Color(C_BLACK)
            self.line_thick = 0.01
            self.line_style = LINE_STYLE_SOLID
            self.line_pitch = 0.5
            self.line_smooth = SMOOTH_NONE
            self.fill_color = Color(C_TRANSPARENT)
            self.pat_number = 0
            self.pat_angle = 0
            self.pat_density = 1
            self.pat_size = 1
            self.pat_style = TILE_RECTANGULAR
            self.pat_thick = self.line_thick

        factor = kwargs.pop('factor', 1.)
        if factor != 1.0:
            self.line_thick *= factor
            self.line_pitch *= factor
            self.pat_size *= factor
            self.pat_thick *= factor

        for k in kwargs:
            if k == 'line_color':
                self.line_color = kwargs[k]
            elif k == 'fill_color':
                self.fill_color = kwargs[k]
            elif k in self.__dict__:
                self.__dict__[k] = kwargs[k]
            else:
                raise GroupException('Invalid pen parameter ({})'.format(k))

    @classmethod
    def from_mapplot_string(cls, cstr):
        """
        Create a Pen instance from a mapplot-style string descriptor.

        :param cstr:                example 'r45g255t500B'

        .. versionadded:: 9.2
        """

        def get_part(cstr, c, default=255):
            if c not in cstr:
                return 0
            start = cstr.index(c)
            end = start + 1
            for c in cstr[end:]:
                if not (c in '0123456789'):
                    break
                end += 1
            if end == start + 1:
                return default
            return int(cstr[start + 1:end])

        def add_k(c, k):
            return max(c[0] - k, 0), max(c[1] - k, 0), max(c[2] - k, 0)

        def has_color(cstr, cc):
            for c in cc:
                if c in cstr:
                    return True
            return False

        def color(cstr, cc):
            if has_color(cstr, cc):
                k = get_part(cstr, cc[3])
                if has_color(cstr, cc[:3]):
                    return add_k((get_part(cstr, cc[0]), get_part(cstr, cc[1]), get_part(cstr, cc[2])), k)
                else:
                    return add_k((255, 255, 255), k)
            else:
                return C_TRANSPARENT

        line_color = color(cstr, 'rgbk')
        fill_color = color(cstr, 'RGBK')
        line_thick = max(1, get_part(cstr, 't', 1)) * 0.0001

        return cls(line_color=line_color, fill_color=fill_color, line_thick=line_thick)

    def __eq__(self, other):
        for k, v in self.__dict__:
            if other[k] != v:
                return False
        return True

    @property
    def line_color(self):
        return self._line_color

    @line_color.setter
    def line_color(self, color):
        if type(color) is Color:
            self._line_color = color
        else:
            self._line_color = Color(color)

    @property
    def fill_color(self):
        return self._fill_color

    @fill_color.setter
    def fill_color(self, color):
        if type(color) is Color:
            self._fill_color = color
        else:
            self._fill_color = Color(color)

    @property
    def mapplot_string(self):
        s = ''
        if self._line_color.int != C_TRANSPARENT:
            if self._line_color.int == C_BLACK:
                s += 'k'
            else:
                c = self._line_color.rgb
                s += 'r{}g{}b{}'.format(c[0], c[1], c[2])
        if self._fill_color.int != C_TRANSPARENT:
            if self._line_color.int == C_BLACK:
                s += 'K'
            else:
                c = self._fill_color.rgb
                s += 'R{}G{}B{}'.format(c[0], c[1], c[2])

        return s + 't{}'.format(int(self.line_thick * 10000.))

class GXaggregate(GXgroup):
    """
    Create an aggregate group
    
    :param view:        gxpy.GXview instance
    :param name:        group name, default uses the aggregate name
    :param agg:         GXagg instance
    
    """

    def __init__(self, view, agg, name=None):

        if name is None:
            name = agg.name
        view.gxview.aggregate(agg.gxagg, name)

        #TODO think about mode, and openign an existing agg in a view
        super().__init__(view, name, mode=READ_ONLY)
