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

TILE_RECTANGULAR = 0
TILE_DIAGONAL = 1
TILE_TRIANGULAR = 2
TILE_RANDOM = 3

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

        elif model == C_RGB:
            self.rgb = color

        elif model == C_CMY:
            self.cmy = color

        elif model == C_HSV:
            hue = max(0, min(255, color[0]))
            sat = max(0, min(255, color[1]))
            val = max(0, min(255, color[2]))
            self._color = gxapi.GXMVIEW.color_hsv(hue, sat, val)

    def __eq__(self, other):
        return self._color == other._color

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
    :param height:      text height in map mm.
    
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
            self.height = 2.5
            self.font = 'DEFAULT'
            self.weight = None
            self.italics = False

        line_thick = None
        for k in kwargs:
            if k == 'color':
                self.color = kwargs[k]
            elif k == 'line_thick':
                line_thick = kwargs[k]
            elif k in self.__dict__:
                self.__dict__[k] = kwargs[k]
            else:
                raise ViewException('Invalid text definition parameter ({})'.format(k))

        if self.weight is None:
            if line_thick is None:
                self.weight = FONT_WEIGHT_MEDIUM
            else:
                self.weight = font_weight_from_line_thickness(line_thick, self.height)

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
            self._font = font
        else:
            self._font = 'DEFAULT'

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
        if '.gfn' in self._font.lower():
            font = self._font.lower().replace('.gfn','')
        elif 'default' in self._font.lower():
            font = 'DEFAULT'
        else:
            font = self._font.strip() + '(TT)'
        return '{},,,{},{}'.format(self.height, self.slant, font)


class Pen:
    """
    Geosoft Pen:
    
    :param line_color:  line Color instance, default is black
    :param fill_color:  fill Color instance, default is transparent
    :param line_thick:  line thickness, default is 1
    :param line_style:  line pattern style
    
                        ::
                        
                            LINE_STYLE_SOLID (default)
                            LINE_STYLE_LONG
                            LINE_STYLE_DOTTED
                            LINE_STYLE_SHORT
                            LINE_STYLE_LONG_SHORT_LONG
                            LINE_STYLE_LONG_DOT_LONG
                        
    :param line_pitch:  line style pitch, default is 1
    :param line_smooth: smooth line:
    
                        ::
                        
                            SMOOTH_NONE (default)
                            SMOOTH_AKIMA
                            SMOOTH_CUBIC
                            
    :param pat_number:  pattern number for filled patterns (refer to ``etc/default.pat``) default 0, flood fill
    :param pat_angle:   pattern angle, default 0
    :param pat_density: pattern density, default 1
    :param pat_size:    pattern size, default 1
    :param pat_style:   pattern style:
    
                        ::
                        
                            TILE_RECTANGULAR (default)
                            TILE_DIAGONAL
                            TILE_TRIANGULAR
                            TILE_RANDOM

    :param pat_thick:   pattern line thickness, default 1
    :param default:     default Pen instance, if specified defaults are established from this

    .. versionadded: 9.2
    """

    def __init__(self, **kwargs):

        if 'default' in kwargs:
            def_pen = kwargs.pop('default')
            self.__dict__ = def_pen.__dict__.copy()
        else:
            self.line_color = Color(C_BLACK)
            self.line_thick = 1
            self.line_style = LINE_STYLE_SOLID
            self.line_pitch = 1
            self.line_smooth = SMOOTH_NONE
            self.fill_color = Color(C_TRANSPARENT)
            self.pat_number = 0
            self.pat_angle = 0
            self.pat_density = 1
            self.pat_size = 1
            self.pat_style = TILE_RECTANGULAR
            self.pat_thick = 1

        for k in kwargs:
            if k == 'line_color':
                self.line_color = kwargs[k]
            elif k == 'fill_color':
                self.fill_color = kwargs[k]
            elif k in self.__dict__:
                self.__dict__[k]= kwargs[k]
            else:
                raise ViewException('Invalid pen parameter ({})'.format(k))

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
            if end == start+1:
                return default
            return int(cstr[start+1:end])

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
        line_thick = max(1, get_part(cstr, 't', 1))

        return cls(line_color=line_color, fill_color=fill_color, line_thick=line_thick)

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
                s += 'r{}g{}b{}'.format(c[0],c[1],c[2])
        if self._fill_color.int != C_TRANSPARENT:
            if self._line_color.int == C_BLACK:
                s += 'K'
            else:
                c = self._fill_color.rgb
                s += 'R{}G{}B{}'.format(c[0], c[1], c[2])

        return s + 't{}'.format(int(self.line_thick))

# decorator
def _draw(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self._group:
            self.start_group()
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
            #TODO revisit resource cleaning once we have cython interface.  Jacques suspects boost.
            self.gxview = None
            self._pen = None
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
        self._pen = None
        self._group = None

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
        if self._pen is None:
            self._init_pen()
        return self._pen

    @pen.setter
    def pen(self, pen):

        if self._pen is None:
            self._init_pen()

        if self._pen.line_color != pen.line_color:
            self.gxview.line_color(pen._line_color.int)
        if self._pen.line_thick!= pen.line_thick:
            self.gxview.line_thick(pen.line_thick)
        if self._pen.line_smooth != pen.line_smooth:
            self.gxview.line_smooth(pen.line_smooth)
        if (self._pen.line_style != pen.line_style) or (self._pen.line_pitch != pen.line_pitch):
            self.gxview.line_style(pen.line_style, pen.line_pitch)
        if self._pen.fill_color != pen.fill_color:
            self.gxview.fill_color(pen._fill_color.int)
        if self._pen.pat_number != pen.pat_number:
            self.gxview.pat_number(pen.pat_number)
        if self._pen.pat_angle != pen.pat_angle:
            self.gxview.pat_angle(pen.pat_angle)
        if self._pen.pat_density != pen.pat_density:
            self.gxview.pat_density(pen.pat_density)
        if self._pen.pat_size != pen.pat_size:
            self.gxview.pat_size(pen.pat_size)
        if self._pen.pat_style != pen.pat_style:
            self.gxview.pat_style(pen.pat_style)
        if self._pen.pat_thick!= pen.pat_thick:
            self.gxview.pat_thick(pen.pat_thick)

        self._pen = pen

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

    def _init_pen(self):

        scm = self.units_per_map_cm
        pen = Pen(line_thick = 0.02 * scm,
                  line_pitch = 0.5 * scm,
                  pat_size = 0.25 * scm,
                  pat_thick = 0.02 * scm)

        if self._group is None:
            self.start_group()
        self.gxview.line_color(pen.line_color.int)
        self.gxview.line_thick(pen.line_thick)
        self.gxview.line_smooth(pen.line_smooth)
        self.gxview.line_style(pen.line_style, pen.line_pitch)
        self.gxview.fill_color(pen.fill_color.int)
        self.gxview.pat_number(pen.pat_number)
        self.gxview.pat_angle(pen.pat_angle)
        self.gxview.pat_density(pen.pat_density)
        self.gxview.pat_size(pen.pat_size)
        self.gxview.pat_style(pen.pat_style)
        self.gxview.pat_thick(pen.pat_thick)

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

    def start_group(self, name=None, append=False):
        """
        Start a new named group in a view.  Drawing functions that follow will be rendered into this group.

        :param name:    name of the group.  If a group name is the same as the view name, '_' is appended
                        to the group name to make it different. If no group name is specified the default
                        group name '_' is assumed with append=True.
        :param append:  True to append to an existing group

        .. versionadded:: 9.2
        """

        if name is None:
            name = '_'
            append = True
        if append:
            mode = gxapi.MVIEW_GROUP_APPEND
        else:
            mode = gxapi.MVIEW_GROUP_NEW

        if name == self.viewname:
            name = name + '_'
        self._group = name
        self.gxview.start_group(name, mode)

    def delete_group(self, group_name):
        """
        Delete a group from a map. Nothing happens if the view does not contain this group.
        
        :param group_name: Name of the group to delete.

        .. versionadded:: 9.2
        """

        self.gxview.delete_group(group_name)

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


