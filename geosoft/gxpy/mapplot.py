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

        style_changed = False
        if 'ref_point' in kwargs:
            self.ref_point = kwargs.pop('ref_point')
        if 'pen' in kwargs:
            self.pen = kwargs.pop('pen')
            style_changed = True
        if 'line_style' in kwargs:
            self.line_style = kwargs.pop('line_style')
            style_changed = True
        if 'font' in kwargs:
            f = kwargs.pop('font')
            if ".gfn" in f.lower():
                self.font = f.split('.gfn')[0]
            else:
                self.font = f + "(TT)"
            style_changed = True
        if 'text_style' in kwargs:
            self.text_style = kwargs.pop('text_style')
            style_changed = True

        if style_changed and not ("set_drawing_attributes" in str(func)):
            self._set_attributes()

        func(self, *args, **kwargs)

    return wrapper

class GXmapplot:
    """
    Draw on a Geosoft map.

    :param map:        gxpy.map.GXmap instance
    :param ref_prefix: reference prefix for map groups

    The map must contain a "*Base" and "*Data" view.

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
        #self._maplfile.write('MDFF \"{}\"\n'.format(gxu.normalize_file_name(self._mdffilename)))

        self._refp = (1,0,0)
        self._pen = ("k", 1)
        self._line_style = (1, 0.5)
        self._text_style = (0.3, False)
        self._font = "DEFAULT"

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

    def _set_attributes(self, name='def'):
        self._maplfile.write("DATT {}={},{},{}\n".format(name,
                                                         self._a_pen(),
                                                         self._a_line_style(),
                                                         self._a_text()))

    @property
    def ref_point(self):
        return self._refp

    @ref_point.setter
    def ref_point(self, refp):
        self._refp = refp

    def _a_ref_point(self):
        return "{},{},{}".format(self._refp[0], self._refp[1], self._refp[2])

    @property
    def pen(self):
        return self._pen

    @pen.setter
    def pen(self, pen):
        self._pen = pen

    def _a_pen(self):
        return "{}t{}".format(self._pen[0].lower(), self._pen[1])

    @property
    def line_style(self):
        return self._line_style

    @line_style.setter
    def line_style(self, ls):
        self._line_style = ls

    def _a_line_style(self):
        return "{},{}".format(self._line_style[0], self._line_style[1])

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, font):
        self._font = font

    @property
    def text_style(self):
        return self._text_style

    @text_style.setter
    def text_style(self, ts):
        self._text_style = ts

    def _a_text(self):
        th = self._text_style[0]
        return "{},{},{},{},\"{}\"".format(th, th, th,
                                               10 if self.text_style[1] else 0, self.font)

    def surround(self, outer_pen=3, inner_pen=1, gap=0):
        if type(outer_pen) is str:
            outer_pen = '3:' + outer_pen
        if gap <= 0:
            self._maplfile.write("SURR {}\n".format(outer_pen))
        else:
            if type(inner_pen) is str:
                inner_pen = '1:' + inner_pen
            self._maplfile.write("SURR {},{},{}\n".format(outer_pen, gap, inner_pen))

    @_attrib
    def set_drawing_attributes(self, name='default'):
        self._set_attributes(name)

    @_attrib
    def text(self, text, just=BOTTOM_LEFT):
        self._maplfile.write("TEXT {},{},\"{}\"\n".format(self._a_ref_point(), just, text))

    def annotate_data_view(self, *titles):
        pass