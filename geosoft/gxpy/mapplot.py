import os
import atexit
from functools import wraps

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import utility as gxu
from . import view as gxv

__version__ = geosoft.__version__

def _t(s):
    return s

RECTANGLE_EXTENT_BASE = -1
RECTANGLE_EXTENT_DATA = -2

TOP_IN = 1
TOP_OUT = -1

GRID_NONE = 0
GRID_DOTTED = 1
GRID_CROSSES = 2
GRID_LINES = 3

GROUP_NEW = 0
GROUP_APPEND = 1

VIEW_BASE = 0
VIEW_DATA = 1

class MapplotException(Exception):
    """
    Exceptions from this module.

    .. versionadded:: 9.2
    """
    pass

_DEF_ATT = '_'

# decorators
def _attrib(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):

        changed = False
        self._att = _DEF_ATT
        if 'ref_point' in kwargs:
            self.ref_point = kwargs.pop('ref_point')
        if 'pen_def' in kwargs:
            self.pen_def = kwargs.pop('pen_def')
            changed = False
        if 'line_def' in kwargs:
            self.line_def = kwargs.pop('line_def')
            changed = False
        if 'text_def' in kwargs:
            self.text_def = kwargs.pop('text_def')
            changed = False
        if 'font' in kwargs:
            self.font = kwargs.pop('font')
            changed = False
        if 'att' in kwargs:
            self._att = kwargs.pop('att')
            if changed:
                self._define_named_attribute(self.att)

        func(self, *args, **kwargs)

    return wrapper

#TODO change init create from a file, new or old.
class GXmapplot:
    """
    Annotate a Geosoft map that contains a "base" view and a "data" view.  This class provides
    a number of drawing capabilities intended for base-map or figure annotations.  This wraps
    the GXAPI GXMAPL class and uses the concepts of the Geosoft MAPPLOT system.

    :param map:         gxpy.map.GXmap instance, which must contain a base and a data view.
    :param data_view:   name of the default data view.  If not specified the current default is assumed.
                        All drawing commands that reference the data view will be applied to the default 
                        data view.  On closing of the GXmapplot instance the default data view is
                        reset to the previous default.
    :param ref_prefix:  A prefix to add to the default group in the "BASE" and "DATA" groups.  The
                        default is "MAPL_", which will create a group named "MAPL_BASE" in the
                        base view and "MAPL_DATA" in the data view.  Use the start_group method
                        to create new view groups.   

    Drawing functions share the following keyword parameters, which can be defined on instance
    creation or together with any drawing function.

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

    def __init__(self, map, data_view=None, ref_prefix='', **kwargs):

        if not (map.has_view(map.current_base_view) and map.has_view(map.current_data_view)):
            raise MapplotException("Map must have a '*Base' and '*Data' view.")

        self._map = map
        self._ref_pre = ref_prefix

        if data_view:
            self.prior_data_view = map.current_data_view
            map.current_data_view = data_view
        else:
            self.prior_data_view = None

        # mapplot control file
        self._maplfilename = os.path.join(gx.GXpy().temp_folder(), 'mapl_' + gxu.uuid() + ".con")
        self._maplfile = open(self._maplfilename, "w")
        #self.command('MDFF \"{}\"\n'.format(gxu.normalize_file_name(self._mdffilename)))

        self._refp = (1, 0, 0)
        self._pen_def = 'kt50'
        self._line_def = (1, 0.5)
        self._text_def = (0.3, 0)
        self._font = "DEFAULT.gfn"
        self._att = _DEF_ATT
        self._annotation_outer_edge = 0.0

        atexit.register(self._process, pop=False)
        self._open = gx.track_resource(self.__class__.__name__, self._maplfilename)

        self.define_named_attribute(self._att, **kwargs)

    def _process(self, pop=True):

        if self._maplfile:
            self._maplfile.close()
            self._maplfile = None
            gxmapl = gxapi.GXMAPL.create(self._maplfilename, self._ref_pre, 0)
            gxmapl.process(self._map.gxmap)
            os.remove(self._maplfilename)
            if self.prior_data_view:
                self.map.current_data_view = self.prior_data_view
        if pop:
            gx.pop_resource(self._open)

    def _adjusted_offset(self, offset):

        inside = self._text_def[0] * 0.2
        if offset:
            offset = offset + inside
        else:
            offset = self._annotation_outer_edge + inside
        self._annotation_outer_edge += offset + self._text_def[0] + inside * 0.5
        return offset

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
        def datt(name):
            self.command("DATT {}={},{},{}".format(name,
                                                   self._pen_def,
                                                   self._a_line_def(),
                                                   self._a_text()))
        if name is not None :
            datt(name)
            return name
        elif self._att == _DEF_ATT:
            datt(self._att)
        return self._att

    def _define_default_attribute(self, default):
        if self._att == _DEF_ATT:
            self._define_named_attribute(default)
        return default

    @_attrib
    def define_named_attribute(self, name='_'):
        """
        Create a named set of drawing attributes.

        :param name:    attribute set name, default is the default attribute '_'

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
        self.command("REFP {},{}".format(self._refp[0], self._refp[1]))

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

    def annotate_data_xy(self, tick='', offset='',
                         x_sep='', x_dec='',
                         y_sep='', y_dec='',
                         compass=True, top=TOP_OUT,
                         text_def=(0.18, 0),
                         pen_def='kt1',
                         grid=0, grid_pen=''):
        """
        Annotate the date view axis

        :param tick:    inner tick size in cm
        :param offset:  posting offset from the edge in cm. The posting edge is adjusted to be outside
                        character height for a subsequent call to an edge annotation.  This allows one to
                        annotate both geographic and projected coordinates.
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

        if not tick and grid == GRID_LINES:
            tick = 0.0

        self.define_named_attribute(text_def=text_def, pen_def=pen_def)
        offset = self._adjusted_offset(offset)

        self.command("ANOX ,,,,,{},{},,{},,,,{},{},1".format(x_sep, tick, 0 if compass else -1, offset, x_dec))
        self._add_att('_')
        self.command("ANOY ,,,,,{},{},,{},{},,,{},{},1".format(y_sep, tick, 0 if compass else -1, top, offset, y_dec))
        self._add_att('_')

        if grid:
            if grid_pen:
                self.define_named_attribute('grid', pen_def=grid_pen)
                grid_pen = 'grid'
            self.command("GRID {},,,,,{}".format(grid, grid_pen))

    def annotate_data_ll(self, tick='', offset='', sep='', top=TOP_OUT,
                         text_def=(0.2, 15), pen_def='kt1',
                         grid=GRID_LINES, grid_pen='bt1'):
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

        if not tick and grid == GRID_LINES:
            tick = 0.0

        self.define_named_attribute(text_def=text_def, pen_def=pen_def)
        offset = self._adjusted_offset(offset)

        self.command("ALON {},{},{},,1".format(sep, tick, offset))
        self._add_att('_')
        self.command("ALAT {},{},{},,,{}".format(sep, tick, offset, top))
        self._add_att('_')

        if grid:
            if grid_pen:
                self.define_named_attribute('grid', pen_def=grid_pen)
                grid_pen = 'grid'
            self.command("GRID -{},,,,,{}".format(grid, grid_pen))

    @_attrib
    def start_group(self, name, mode=GROUP_NEW, view=VIEW_BASE):
        """
        Start a view group, or append to an existing group.  Graphic entities can be organized
        into named groups, which appear as separate components that can be managed within a
        Geosoft viewer.

        :param name:    Group name (required).
        :param mode:    GROUP_NEW (default) or GROUP_APPEND.  GROUP_NEW relaces an existing group, and the
                        content of an existing group will be deleted.
        :param view:    VIEW_BASE or VIEW_DATA.  Coordinates in the base view are map cm, and coordionates
                        in the data view are in data view units.

        .. versionadded:: 9.2
        """

        self.command('MGRP {},{},{}'.format(name, mode, view))