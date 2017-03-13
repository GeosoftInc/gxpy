import os
import atexit
from functools import wraps

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import utility as gxu

__version__ = geosoft.__version__

def _t(s):
    return s

BOTTOM_LEFT = -1
BOTTOM_CENTER = 0
BOTTOM_RIGHT = 1
ALL_CENTER = 1
BASE_LEFT= 3
BASE_CENTER = 4
BASE_RIGHT = 5
BASE_ALL_CENTER = 6
BASE_FIT_BY_CHARACTER_WIDTH = 7
BASE_FIT_BY_CHARACTER_SIZE = 8

RECTANGLE_EXTENT_BASE = -1
RECTANGLE_EXTENT_DATA = -2

TOP_IN = 1
TOP_OUT = -1

GRID_NONE = 0
GRID_DOTTED = 1
GRID_CROSSES = 2
GRID_LINES = 3

class MapplotException(Exception):
    """
    Exceptions from this module.

    .. versionadded:: 9.2
    """
    pass

# decorators
def _attrib(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):

        if 'ref_point' in kwargs:
            self.ref_point = kwargs.pop('ref_point')
        if 'pen_def' in kwargs:
            self.pen_def = kwargs.pop('pen_def')
        if 'line_def' in kwargs:
            self.line_def = kwargs.pop('line_def')
        if 'text_def' in kwargs:
            self.text_def = kwargs.pop('text_def')
        if 'font' in kwargs:
            self.font = kwargs.pop('font')

        if 'att' in kwargs:
            self._att = kwargs.pop('att') #TODO need a test

        func(self, *args, **kwargs)

    return wrapper

class GXmapplot:
    """
    Annotate a Geosoft map that contains a "base" view and a "data" view.  This class provides
    a number of drawing capabilities intended for base-map or figure annotations.  This wraps
    the GXAPI GXMAPL class and uses the concepts of the Geosoft MAPPLOT system.

    :param map:        gxpy.map.GXmap instance, which must contain a "*Base" and "*Data" view.
    :param ref_prefix: reference prefix for map groups

    All drawing functions share the following keyword parameters:

    :param pen_def:     string that describes the colour-thickness of a line and fill colour.
                        Colours are defined by a colour letter from "rgbcmy" optionally
                        followed by an intensity between 0 and 255.  Lower-case colour letters
                        define the line colour and upper-case colour letters define the fill colour.
                        Line thickness is defined by a letter "t" followed by the desired line
                        thickness in microns.

                        Examples::

                            'k'             black
                            'k64'           light grey
                            'k128t200'      medium grey line 200 microns thick
                            'k0'            white (which will be a white line on a coloured background)
                            'r128b255t50'   purple, 50 microns thick
                            'r128b255K15'   purple with light-grey fill

    :param line_def:    (pattern, pitch) line pattern and pitch in cm.  Patterns::

                            1   solid
                            2   long dashes
                            3   dotted
                            4   short dashes
                            5   long/short/long dashes

                        If pattern is negative a smooth line is used.

    :param text_def:    (size, slant), text character size in cm, slant in degrees.  For true-type fonts
                        any slant above 10 degrees is taken as italics, and for Geosoft stroke fonts the
                        slant is the slant angle.

    :param font:        True-Type font name, or a Geosoft stroke font name::

                            'sr.gfn'         simplex roman
                            'ss.gfn'         simplex script
                            'cr.gfn'         complex roman
                            'ci.gfn'         complex italic
                            'tr.gfn'         triplex roman
                            'ti.gfn'         triplex italic
                            'dr.gfn'         duplex roman
                            'cs.gfn'         complex script
                            'sg.gfn'         simplex greek
                            'cg.gfn'         complex greek
                            'es.gfn'         equal-spaced simplex roman
                            'russian.gfn'    simple Cyrillic

    :param ref_point:   (refp, x_off, y_off) a reference point and offset from that point::

        Drawing commands use reference points to define the positions at which to plot objects.
        This allows the user to work either relative to a ground coordinate system, relative to
        any one of the map corners, or relative to a user specified point.

        The 'refp' parameter identifies the reference point relative to the map layout as follows::

            7, 8, 9     Top left, center and right
            4, 5, 6     Horizontal center line left, middle and right.
            1, 2, 3     Bottom left, center and right of map surround.
            10          Plot origin (lowest-left plottable point on the media)
            11          Movable reference point (see the refp() function)
            12          Bottom left of the "*data" view clip window
            0           Data view origin, offsets are in data view coordinates.

        All offset and relative units for referents point 1 through 10, and reference point 12
        are centimetres on the map.  Offsets using reference point 0 are are in the units of the
        data view.  The movable reference point 11 will be in data view units if defined
        relative to reference point 0, otherwise using are map centimetres.

        For example, if we are creating a series of maps on which we want to place the title block
        and legends in the top right hand corner and along the right side of a map, we define
        the locations of these objects relative to the top right hand corner of the map (reference
        point 9).

    .. versionadded:: 9.2
    """

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self._process()

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "mapplot({})".format(self._maplfilename)

    def __init__(self, map, ref_prefix="_mpl"):

        if not (map.has_view("*Base") and map.has_view("*Data")):
            raise MapplotException("Map must have a '*Base' and '*Data' view.")

        self._map = map
        self._ref_pre = ref_prefix

        # create an mdf file
        # mdf1, mdf2 = map.mdf()
        # self._mdffilename = os.path.join(gx.GXpy().temp_folder(), gxu.uuid() + ".mdf")
        # with open(self._mdffilename, "w") as f:
        #    f.write("{}\n{}\n".format(str(mdf1)[1:-1], str(mdf2)[1:-1]))

        # mapplot control file
        self._maplfilename = os.path.join(gx.GXpy().temp_folder(), 'mapl_' + gxu.uuid() + ".con")
        self._maplfile = open(self._maplfilename, "w")
        #self.command('MDFF \"{}\"\n'.format(gxu.normalize_file_name(self._mdffilename)))

        self._refp = (1, 0, 0)
        self._pen_def = 'kt50'
        self._line_def = (1, 0.5)
        self._text_def = (0.3, 0)
        self._font = "DEFAULT.gfn"
        self._att = '_'
        self.define_named_attribute(self._att)

        atexit.register(self._process, pop=False)
        self._open = gx.track_resource(self.__class__.__name__, self._maplfilename)

    def _process(self, pop=True):

        if self._maplfile:
            self._maplfile.close()
            self._maplfile = None
            gxmapl = gxapi.GXMAPL.create(self._maplfilename, self._ref_pre, 0)
            gxmapl.process(self._map.gxmap)
            os.remove(self._maplfilename)
            #os.remove(self._mdffilename)
        if pop:
            gx.pop_resource(self._open)

    @property
    def ref_point(self):
        """(refp, x_off, y_off)"""
        return self._refp

    @ref_point.setter
    def ref_point(self, refp):
        self._refp = refp

    def _a_ref_point(self):
        return "{},{},{}".format(self._refp[0], self._refp[1], self._refp[2])

    @property
    def pen_def(self):
        """(colour, thickness) colour is a colour string, line thickness in microns"""
        return self._pen_def

    @pen_def.setter
    def pen_def(self, pen):
        self._pen_def = pen

    @property
    def line_def(self):
        """(line_style, pitch)"""
        return self._line_def

    @line_def.setter
    def line_def(self, ls):
        self._line_def = ls

    def _a_line_def(self):
        return "{},{}".format(self._line_def[0], self._line_def[1])

    @property
    def font(self):
        """font name"""
        return self._font

    @font.setter
    def font(self, font):
        self._font = font

    @property
    def text_def(self):
        """(character_size, slant) in (cm, degrees)"""
        return self._text_def

    @text_def.setter
    def text_def(self, ts):
        self._text_def = ts

    def _a_text(self):
        if ".gfn" in self._font.lower():
            f = self._font.lower().split('.gfn')[0]
        else:
            f = self._font + "(TT)"

        th = self._text_def[0]
        return "{},{},{},{},\"{}\"".format(th, th, th, self.text_def[1], f)

    def _add_att(self, att):
        self.command('     {}\n'.format(att))

    def _define_named_attribute(self, name=None):
        """
        Create a named set of drawing attributes.

        :param name:    attribute set name, None to change the current drawing attributes

        .. versionadded:: 9.2
        """
        name = self._att if name is None else name
        self.command("DATT {}={},{},{}\n".format(name,
                                                 self._pen_def,
                                                 self._a_line_def(),
                                                 self._a_text()))
        self._att = '_'
        return name

    @_attrib
    def define_named_attribute(self, name=None):
        """
        Create a named set of drawing attributes.

        :param name:    attribute set name, None to change the current drawing attributes

        .. versionadded:: 9.2
        """
        return self._define_named_attribute(name)

    def refp(self, ref_point):
        """
        Define the movable reference point (11) location.

        :param ref_point: (refp, x_off, y_off)

        The moveaple reference point is point 11.  This can be defined relative to any of
        the map reference points or reference point 0.  If defined relative to reference
        point 0 then offsets use the data coordinate system units.

        .. versionadded:: 9.2
        """

        self._refp = ref_point
        self.command("REFP {},{}\n".format(self._refp[0], self._refp[1]))
        
    def command(self, command):
        """
        Add MAPPLOT commands to the command list.  See the MAPPLOT reference in the 
        Geosoft Desktop help system for command usage and syntax.
        
        :param command:     text string containing one or more MAPPLOT command
                            lines, each new-line terminated.
        
        .. versionadded:: 9.2
        """
        self._maplfile.write(command)
        if command and command[-1] != '\n':
            self._maplfile.write('\n')

    def surround(self, outer_pen=3, inner_pen=1, gap=0):
        if type(outer_pen) is not int:
            self.define_named_attribute('outer', pen_def=outer_pen)
            outer_pen = 'outer'
        if gap <= 0:
            self.command("SURR {}\n".format(outer_pen))
        else:
            if type(inner_pen) is not int:
                self.define_named_attribute('inner', pen_def=inner_pen)
                inner_pen = 'inner'
            self.command("SURR {},{},{}\n".format(outer_pen, gap, inner_pen))


    @_attrib
    def text(self, text, just=BOTTOM_LEFT):
        """
        Add text to the map.

        :param text:    Text string.
        :param just:    Justification relative to the reference point:

                        ::

                            BOTTOM_LEFT
                            BOTTOM_CENTER
                            BOTTOM_RIGHT
                            ALL_CENTER

        .. versionadded:: 9.2
        """
        att = self._define_named_attribute()
        self.command("TEXT {},{},\"{}\"\n".format(self._a_ref_point(), just, text))
        self._add_att(att)

    @_attrib
    def rectangle(self, extent):
        """
        Draw a rectangle.

        :param rect:    (x_min, y_min, x_max, y_max) rectangle extent relative to the reference point or:

                        ::

                            RECTANGLE_EXTENT_BASE   base view edge
                            RECTANGLE_EXTENT_DATA   data view window


        .. versionadded:: 9.2
        """

        self.define_named_attribute(name='rect')
        if extent == RECTANGLE_EXTENT_BASE:
            self.command('RECT -1,,,,,rect\n')
        elif extent == RECTANGLE_EXTENT_DATA:
            self.command('RECT -2,,,,,rect')
        else:
            self.command("RECT {},{},{},{},{},rect\n".format(self._refp[0],
                                                        extent[0], extent[1],extent[2], extent[3]))


    @_attrib
    def annotate_data_xy(self, tick=0.15, offset=0.07,
                         x_sep='', x_dec='',
                         y_sep='', y_dec='',
                         compass=True, top=TOP_OUT,
                         grid=0, grid_pen=''):
        """
        Annotate the date view axis

        :param tick:    inner tick size in cm
        :param offset:  posting offset from the edge in cm
        :param top:     TOP_IN or TOP_OUT (default) for vertical annotations
        :param x_sep:   separation between X annotations, default is calculated from data
        :param x_dec:   X axis label decimals, default is 0
        :param y_sep:   separation between Y annotations, default is calculated from data
        :param y_dec:   Y axis label decimals, default is 0
        :param compass: True (default) to append compass direction to annotations
        :param grid:    Plot grid lines:

                        ::

                            GRID_NONE       no grid
                            GRID_DOTTED     dotted lines
                            GRID_CROSSES    crosses at intersections
                            GRID_LINES      lines

        :param grid_pen:    (colour, thickness) for grid detail

        .. versionadded:: 9.2
        """
        att = self._define_named_attribute()
        self.command("ANOX ,,,,,{},{},,{},,,,{},{},1\n".format(x_sep, tick, 0 if compass else -1, offset, x_dec))
        self._add_att(att)
        self.command("ANOY ,,,,,{},{},,{},1,,,{},{},1\n".format(y_sep, tick, 0 if compass else -1, offset, y_dec))
        self._add_att(att)

        if grid:
            if grid_pen:
                self.define_named_attribute('grid', pen_def=grid_pen)
                grid_pen = 'grid'
            self.command("GRID {},,,,,{}".format(grid, grid_pen))

    @_attrib
    def annotate_data_ll(self, tick=0.15, offset=0.07, sep='', top=TOP_OUT,
                         grid=0, grid_pen=''):
        """
        Annotate the date view axis

        :param tick:    inner tick size in cm
        :param offset:  posting offset from the edge in cm
        :param sep:     separation between annotations, default is calculated from data
        :param top:     TOP_IN or TOP_OUT (default) for vertical annotations
        :param grid:    Plot grid lines:

                        ::

                            GRID_NONE       no grid
                            GRID_DOTTED     dotted lines
                            GRID_CROSSES    crosses at intersections
                            GRID_LINES      lines

        :param grid_pen: colour-thickness string

        .. versionadded:: 9.2
        """

        att = self._define_named_attribute()
        self.command("ALON {},{},{},,1\n".format(sep, tick, offset))
        self._add_att(att)
        self.command("ALAT {},{},{},,,{}\n".format(sep, tick, offset, top))
        self._add_att(att)
        if grid:
            if grid_pen:
                self.define_named_attribute('grid', pen_def=grid_pen)
                grid_pen = 'grid'
            self.command("GRID -{},,,,,{}".format(grid, grid_pen))
