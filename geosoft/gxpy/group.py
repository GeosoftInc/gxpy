"""
A Geosoft View (:class:`geosoft.gxpy.view.View` or :class:`geosoft.gxpy.view.View_3d`) contains graphical elements as
:class:`Group` instances. Groups are named and are available to a user in a Geosoft viewer, which allows groups to
be turned on or off, modify the transparency, or be deleted.

2D views can only accept 2D groups, while a 3D view can accept both 2D and 3D groups. When a 2D group is placed
in a 3D view, the group is placed on a the active plane inside the 3D view

:Classes:

    ============================ =============================================================================
    :class:`Group`               base class for named rendering groups in 2D and 3D views.
    :class:`Draw`                2D drawing group, handles 2D drawing to a view or plane in a 3D view
    :class:`Draw_3d`             3D grawing group for 3D objects placed in a 3d view
    :class:`Color_symbols_group` group for 2D symbols rendered based on data values
    :class:`Aggregate_group`     group that contains a :class:`geosoft.gxpy.agg.Aggregate_image` instance
    :class:`Color`               colour definition
    :class:`Color_map`           maps values to colors
    :class:`Pen`                 pen definition, includes line colour, thickness and pattern, and fill.
    :class:`Text_def`            defined text characteristics
    :class:`Vox_display_group`   add a 'geosoft.gxpy.vox.Vox_display` to a `geosoft.gxpy.view.View_3d`
    ============================ =============================================================================

.. note::

    Regression tests provide usage examples:     
    `group drawing tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_group.py>`_
    
.. seealso:: :mod:`geosoft.gxpy.view`, :mod:`geosoft.gxpy.map`

   :class:`geosoft.gxapi.GXMVIEW`, :class:`geosoft.gxapi.GXMVU`

"""
from functools import wraps
import threading
import os

import geosoft
import geosoft.gxapi as gxapi
from . import gx
from . import vv as gxvv
from . import geometry as gxgm
from . import coordinate_system as gxcs
from . import utility as gxu
from . import view as gxv
from . import agg as gxagg
from . import metadata as gxmeta
from . import vox_display as gxvoxd

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)

MAX_TRANSPARENT = 4

class GroupException(Exception):
    """
    Exceptions from :mod:`geosoft.gxpy.group`.

    .. versionadded:: 9.2
    """
    pass

GROUP_NAME_SIZE = gxv.VIEW_NAME_SIZE #:

NEW = gxapi.MVIEW_GROUP_NEW #:
APPEND = gxapi.MVIEW_GROUP_APPEND #:
READ_ONLY = max(NEW, APPEND) + 1 #:
REPLACE = READ_ONLY + 1 #:

SMOOTH_NONE = gxapi.MVIEW_SMOOTH_NEAREST #:
SMOOTH_CUBIC = gxapi.MVIEW_SMOOTH_CUBIC #:
SMOOTH_AKIMA = gxapi.MVIEW_SMOOTH_AKIMA #:

TILE_RECTANGULAR = gxapi.MVIEW_TILE_RECTANGULAR #:
TILE_DIAGONAL = gxapi.MVIEW_TILE_DIAGONAL #:
TILE_TRIANGULAR = gxapi.MVIEW_TILE_TRIANGULAR #:
TILE_RANDOM = gxapi.MVIEW_TILE_RANDOM #:

UNIT_VIEW = 0 #:
UNIT_MAP = 2 #:
UNIT_VIEW_UNWARPED = 3 #:

GRATICULE_DOT = 0 #:
GRATICULE_LINE = 1 #:
GRATICULE_CROSS = 2 #:

LINE_STYLE_SOLID = 1 #:
LINE_STYLE_LONG = 2 #:
LINE_STYLE_DOTTED = 3 #:
LINE_STYLE_SHORT = 4 #:
LINE_STYLE_LONG_SHORT_LONG = 5 #:
LINE_STYLE_LONG_DOT_LONG = 6 #:

SYMBOL_NONE = 0 #:
SYMBOL_DOT = 1 #:
SYMBOL_PLUS = 2 #:
SYMBOL_X = 3 #:
SYMBOL_BOX = 4 #:
SYMBOL_TRIANGLE = 5 #:
SYMBOL_INVERTED_TRIANGLE = 6 #:
SYMBOL_HEXAGON = 7 #:
SYMBOL_SMALL_BOX = 8 #:
SYMBOL_SMALL_DIAMOND = 9 #:
SYMBOL_CIRCLE = 20 #:

SYMBOL_3D_SPHERE = 0 #:
SYMBOL_3D_CUBE = 1 #:
SYMBOL_3D_CYLINDER = 2 #:
SYMBOL_3D_CONE = 3 #:

_weight_factor = (1.0 / 48.0, 1.0 / 24.0, 1.0 / 16.0, 1.0 / 12.0, 0.145, 1.0 / 4.0)

FONT_WEIGHT_ULTRALIGHT = 1 #:
FONT_WEIGHT_LIGHT = 2 #:
FONT_WEIGHT_MEDIUM = 3 #:
FONT_WEIGHT_BOLD = 4 #:
FONT_WEIGHT_XBOLD = 5 #:
FONT_WEIGHT_XXBOLD = 6 #:

CMODEL_RGB = 0 #:
CMODEL_CMY = 1 #:
CMODEL_HSV = 2 #:

C_BLACK = 67108863 #:
C_RED = 33554687 #:
C_GREEN = 33619712 #:
C_BLUE = 50266112 #:
C_CYAN = 50331903 #:
C_MAGENTA = 50396928 #:
C_YELLOW = 67043328 #:
C_GREY = 41975936 #:
C_LT_RED = 54542336 #:
C_LT_GREEN = 54526016 #:
C_LT_BLUE = 50348096 #:
C_LT_CYAN = 50331712 #:
C_LT_MAGENTA = 50348032 #:
C_LT_YELLOW = 54525952 #:
C_LT_GREY = 54542400 #:
C_GREY10 = 51910680 #:
C_GREY25 = 54542400 #:
C_GREY50 = 41975936 #:
C_WHITE = 50331648 #:
C_TRANSPARENT = 0 #:

REF_BOTTOM_LEFT = 0 #:
REF_BOTTOM_CENTER = 1 #:
REF_BOTTOM_RIGHT = 2 #:
REF_CENTER_LEFT = 3 #:
REF_CENTER = 4 #:
REF_CENTER_RIGHT = 5 #:
REF_TOP_LEFT = 6 #:
REF_TOP_CENTER = 7 #:
REF_TOP_RIGHT = 8 #:

GROUP_ALL = 0 #:
GROUP_MARKED = 1 #:
GROUP_VISIBLE = 2 #:
GROUP_AGG = 3 #:
GROUP_CSYMB = 4 #:
GROUP_VOXD = 5 #:

LOCATE_FIT = gxapi.MVIEW_RELOCATE_FIT #:
LOCATE_FIT_KEEP_ASPECT = gxapi.MVIEW_RELOCATE_ASPECT #:
LOCATE_CENTER = gxapi.MVIEW_RELOCATE_ASPECT_CENTER #:

COLOR_BAR_RIGHT = 0 #:
COLOR_BAR_LEFT = 1 #:
COLOR_BAR_BOTTOM = 2 #:
COLOR_BAR_TOP = 3 #:

COLOR_BAR_ANNOTATE_RIGHT = 1 #:
COLOR_BAR_ANNOTATE_LEFT = -1 #:
COLOR_BAR_ANNOTATE_TOP = 1 #:
COLOR_BAR_ANNOTATE_BOTTOM = -1 #:

CYLINDER_OPEN = 0 #:
CYLINDER_CLOSE_START = 1 #:
CYLINDER_CLOSE_END = 2 #:
CYLINDER_CLOSE_ALL = 3 #:

POINT_STYLE_DOT = 0 #:
POINT_STYLE_SPHERE = 1 #:

LINE3D_STYLE_LINE = 0 #:
LINE3D_STYLE_TUBE = 1 #:
LINE3D_STYLE_TUBE_JOINED = 2 #:

_uom_attr = '/geosoft/data/unit_of_measure'


def color_from_string(cstr):
    """
    Return a Geosoft color number from a color string.

    :param cstr:    color string (see below)
    :returns:       color

    Colour strings may be "R", "G", "B", "C", "M", "Y",
    "H", "S", "V", or "K" or a combination of these
    characters, each followed by up to three digits
    specifying a number between 0 and 255.
    An empty string will produce C_ANY_NONE.

    You must stay in the same color model, RGB, CMY,
    HSV or K.

    For example "R", "R127G22", "H255S127V32"

    Characters are not case sensitive.

    .. versionadded:: 9.3
    """

    return gxapi.GXMVIEW.color(str(cstr))


def edge_reference(area, reference):
    """
    Location of a reference point of an area.
    
    :param area:        :class:`Point2` instance, or (x0, y0, x1, y1)
    :param reference:   reference point relative to the clip limits of the view to
                        which reference location.  The points are:
                        
                        ::
                            
                            6 7 8   top left, center, right
                            3 4 5   middle left, center, right
                            0 1 2   bottom left, center, right
    
    :returns:           Point desired reference location as a Point

    .. versionadded:: 9.2
    """
    if not isinstance(area, gxgm.Point2):
        area = gxgm.Point2(area)
    centroid = area.centroid
    half_dim = gxgm.Point(area.dimension) * 0.5
    xoff = yoff = 0.0
    if reference in (0, 1, 2):
        yoff = -half_dim.y
    elif reference in (6, 7, 8):
        yoff = half_dim.y
    if reference in (0, 3, 6):
        xoff = -half_dim.x
    elif reference in (2, 5, 8):
        xoff = half_dim.x

    return centroid + gxgm.Point((xoff, yoff))

class Group:
    """
    Geosoft group class.

    :parameters:

        :view:              gxpy.View
        :name:              group name, default is "_".
        :plane:             plane number, or plane name if drawing to a 3D view.  Default is plane number 0.
        :view_lock:         True to lock the view for a single-stream drawing group.  Default is False.
        :unit_of_measure:   unit of measurement for data in this group, default is ''
        :group_3d:          True for a 3D drawing group, default assumes a 2D drawing group to a plane.
        :mode:              `APPEND` (default), `NEW` or `READ_ONLY`

    :Properties:

        :view:              the :class:`geosoft.gxpy.view.View` instance that contains this group
        :name:              the name of the group
        :unit_of_measure:   the unit of measurement (uom) for this data in this group
        :name_uom:          uom decorated group name as it appears in a view
        :extent:            extent of the group in view units
        :extent_map_cm:     extent of the group in map cm
        :drawing_coordinate_system:        the coordinate system of drawing coordinates. Setting to None will reset drawing
                            coordinates to the view cs.  If `drawing_coordinate_system` is set to some other cs the drawing
                            coordinates will be transformed into the view cs.

    .. versionadded:: 9.2

    .. versionchanged:: 9.3 added support for `unit_of_measure`

    .. versionchanged:: 9.3.1 added mode=REPLACE and changed mode=NEW to always create a new unique group.
    """

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self.__del__()

    def __del__(self):
        if hasattr(self, '_close'):
            self._close()

    def _close(self):
        if hasattr(self, '_open'):
            if self._open:
                try:
                    self._drawing_coordinate_system = None
                    self._pen = None
                    self._text_def = None

                    # write metadata
                    if self._new_meta:
                        bf = gxapi.GXBF.create("", gxapi.BF_READWRITE_NEW)
                        try:
                            self._meta.gxmeta.serial(bf)
                            bf.seek(0, gxapi.BF_SEEK_START)
                            self.view.gxview.write_group_storage(self.number, "Geosoft_META", bf)
                        finally:
                            del bf

                finally:
                    self._view.lock = False
                    self._view = None
                    self._open = False
                    self._meta = None
                    self._new_meta = False

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        if self.view.is_3d and not self.group_3d:
            return '{}/{}/{}'.format(self.name, self.view.current_3d_drawing_plane, self.view.name)
        return '{}/{}'.format(self.name, self.view.name)

    def __init__(self,
                 view,
                 name='_',
                 plane=None,
                 view_lock=False,
                 mode=APPEND,
                 unit_of_measure='',
                 group_3d=False):

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

        self._gx = gx.GXpy()
        self.group_3d = False
        if view.is_3d:
            self.group_3d = group_3d

            if not group_3d:
                # setup a 2D drawing plane for this 2D group
                if plane is None:
                    if view.current_3d_drawing_plane:
                        plane = view.current_3d_drawing_plane
                    else:
                        plane = 'Plane'
                view.current_3d_drawing_plane = plane

        self._view = view
        self._name = name
        self._mode = mode

        self._new_meta = False
        self._meta = None

        if mode == REPLACE:
            if self.view.gxview.exist_group(name):
                self.view.delete_group(name)

        elif mode == NEW:
            # if the group exists, find a new unique group name
            if self.view.gxview.exist_group(name):
                self._name = gxu.unique_name(name, self.view.gxview.exist_group, separator='_')

        elif self.view.gxview.exist_group(self.name):
            sr = gxapi.str_ref()
            group_number = self.view.gxview.find_group(self.name)
            if self.view.gxview.group_storage_exists(group_number, "Geosoft_META"):
                bf = self.view.gxview.read_group_storage(group_number, "Geosoft_META")
                if bf.size():
                    try:
                        self._meta = gxmeta.Metadata(gxapi.GXMETA.create_s(bf))
                    finally:
                        del bf

        if unit_of_measure:
            self.unit_of_measure = unit_of_measure

        self._view.gxview.start_group(self.name, mode)
        self._open = True

    def close(self):
        """ Close the group, unlocks the view"""
        self._close()

    @property
    def guid(self):
        """
        The group GUID.

        .. versionadded:: 9.3
        """
        sr = gxapi.str_ref()
        self.view.gxview.get_group_guid(self.number, sr)
        return sr.value

    @property
    def view(self):
        """view that contains this group."""
        return self._view

    @property
    def name(self):
        """group name"""
        return self._name

    @property
    def drawing_plane(self):
        """ drawing plane of this group, None for a group in a 2D view."""
        if self.view.is_3d:
            return self.view.current_3d_drawing_plane
        else:
            return None

    @property
    def unit_of_measure(self):
        """
        Unit of measure for scalar data contained in this group. This is only relevant
        for groups that contain scalar data, such as a Colour_symbols_group. For
        the spatial unit_of_measure use :attr:`drawing_coordinate_system.unit_of_measure`

        Can be set.

        ..versionadded:: 9.3

        """
        gxm = self.gx_metadata
        if gxm.has_attribute(_uom_attr):
            return gxm.get_attribute(_uom_attr)
        return ''

    @unit_of_measure.setter
    def unit_of_measure(self, uom):
        gxm = self.gx_metadata
        gxm.set_attribute(_uom_attr, str(uom))
        self.gx_metadata = gxm

    @property
    def number(self):
        """group number in the view"""
        return self.view.gxview.find_group(self.name)

    def _extent(self, unit=UNIT_VIEW):
        xmin = gxapi.float_ref()
        ymin = gxapi.float_ref()
        xmax = gxapi.float_ref()
        ymax = gxapi.float_ref()
        self.view.gxview.get_group_extent(self.name, xmin, ymin, xmax, ymax, unit)
        return xmin.value, ymin.value, xmax.value, ymax.value

    @property
    def extent(self):
        """group extent as (xmin, ymin, xmax, ymax) in view units"""
        return self._extent(UNIT_VIEW)

    @property
    def visible(self):
        """True if group is visible, can be set."""
        return self.name in self.view.group_list_visible

    @visible.setter
    def visible(self, visibility):
        if self.visible != visibility:
            marked = self.view.group_list_marked
            self.view.gxview.mark_all_groups(0)
            self.view.gxview.mark_group(self.name, 1)
            if visibility is True:
                self.view.gxview.hide_marked_groups(0)
            else:
                self.view.gxview.hide_marked_groups(1)
            self.view.gxview.mark_all_groups(0)
            for g in marked:
                self.view.gxview.mark_group(g, 1)

    def extent_map_cm(self, extent=None):
        """
        Return an extent in map cm.

        :param extent: an extent in view units as a tuple (xmin, ymin, xmax, ymax), Default is the group extent.

        .. versionadded:: 9.2
        """
        if extent is None:
            extent = self.extent
        xmin, ymin = self.view.view_to_map_cm(extent[0], extent[1])
        xmax, ymax = self.view.view_to_map_cm(extent[2], extent[3])

        return xmin, ymin, xmax, ymax

    def locate(self, location, reference=REF_CENTER):
        """
        Locate the group relative to a point.

        :param location:    location (x, y) or a `geosoft.gxpy.geometry.Point`
        :param reference:   reference point relative to the clip limits of the view to
                            which reference location.  The points are:
                            
                                ::
                                    
                                    6 7 8   top left, center, right
                                    3 4 5   center left, center, right
                                    0 1 2   bottom left, center, right


        .. versionadded:: 9.2
        """
        area = gxgm.Point2(self.extent)
        area -= area.centroid
        area -= edge_reference(area, reference)
        area += location
        self.view.gxview.relocate_group(self.name,
                                        area.p0.x, area.p0.y, area.p1.x, area.p1.y,
                                        gxapi.MVIEW_RELOCATE_ASPECT_CENTER)

    @property
    def gx_metadata(self):
        """
        The group metadata as a Geosoft `geosoft.gxpy.metadata.Metadata` instance. This metadata
        may contain standard Geosoft metadata, such as unit_of_measure for data contained in the group,
        and you can add your own metadata spexific to your application. See `geosoft.gxpy.metadata.Metadata`
        for information about working with metadata.

        Can be set, in which case the metadata is replaced by the new metadata. Normally you will get the current
        metadata, add to or modify, then set it back.

        .. versionadded:: 9.3
        """
        if self._meta:
            return self._meta
        else:
            return gxmeta.Metadata()

    @gx_metadata.setter
    def gx_metadata(self, meta):
        self._new_meta = True
        self._meta = meta

def _draw(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self._mode == READ_ONLY:
            raise _t('This view is read-only.')
        if not self._pen:
            self._init_pen()
        if 'pen' in kwargs:
            cur_pen = self.pen
            try:
                self.pen = kwargs.pop('pen')
                func(self, *args, **kwargs)
            finally:
                self.pen = cur_pen
        else:
            func(self, *args, **kwargs)

    return wrapper

def _make_Point(p):
    if isinstance(p, gxgm.Point):
        return p
    else:
        return gxgm.Point(p)

def _make_Point2(p2):
    if isinstance(p2, gxgm.Point2):
        return p2
    else:
        return gxgm.Point2(p2)

def _make_PPoint(p):
    if isinstance(p, gxgm.PPoint):
        return p
    else:
        return gxgm.PPoint(p)


class Draw(Group):
    """
    Create (start) a drawing group for 2D drawing elements.

    On a 3D view, 2D drawing elements are placed on the default drawing plane.
    Drawing groups will lock the view such that only one drawing group can be instantiated at a time.
    
    Use `with Draw() as group:` to ensure correct unlocking when complete.
    
    Inherits from the `Group` base class. See `Group` arguments.
    """

    def __init__(self, *args, **kwargs):

        kwargs['view_lock'] = True
        super().__init__(*args, **kwargs)

        self._pen = None
        self._text_def = None
        self._drawing_coordinate_system = None

        if self._mode != READ_ONLY:
            self._init_pen()
            self._text_def = Text_def(factor=self.view.units_per_map_cm)

    def _set_dot_symbol(self):

        # this is a hack because we cannot draw a box or a zero-length line, so
        # instead we draw a filled box
        self.view.gxview.symb_number(4)
        self.view.gxview.symb_color(0)
        self.view.gxview.symb_fill_color(self.pen.line_color._color)
        self.view.gxview.symb_size(self.pen.line_thick)

    @property
    def drawing_coordinate_system(self):
        """
        The coordinate of incoming spatial data, which are converted to the coordinate system of the
        view.  This is normally the same as the view coordinate system, but it can be set to a different
        coordinate system to have automatic reprojection occur during drawing.
        """
        if self._drawing_coordinate_system is None:
            return self.view.coordinate_system
        return self._drawing_coordinate_system

    @drawing_coordinate_system.setter
    def drawing_coordinate_system(self, cs):
        if cs is None:
            self.view.gxview.set_user_ipj(self.view.coordinate_system.gxipj)
            self._drawing_coordinate_system = None
        else:
            self._drawing_coordinate_system = gxcs.Coordinate_system(cs)
            self.view.gxview.set_user_ipj(self._drawing_coordinate_system.gxipj)

    @property
    def pen(self):
        """the current drawing pen as a :class:`Pen` instance"""
        return self._pen

    @pen.setter
    def pen(self, pen):

        if self._mode == READ_ONLY:
            raise _t('This view is read-only.')

        if type(pen) is str:
            pen = Pen.from_mapplot_string(pen)
        if self._pen.line_color != pen.line_color:
            self.view.gxview.line_color(pen._line_color.int_value)
        if self._pen.line_thick != pen.line_thick:
            self.view.gxview.line_thick(pen.line_thick)
        if self._pen.line_smooth != pen.line_smooth:
            self.view.gxview.line_smooth(pen.line_smooth)
        if (self._pen.line_style != pen.line_style) or (self._pen.line_pitch != pen.line_pitch):
            self.view.gxview.line_style(pen.line_style, pen.line_pitch)
        if self._pen.fill_color != pen.fill_color:
            self.view.gxview.fill_color(pen._fill_color.int_value)
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

        self.view.gxview.line_color(pen.line_color.int_value)
        self.view.gxview.line_thick(pen.line_thick)
        self.view.gxview.line_smooth(pen.line_smooth)
        self.view.gxview.line_style(pen.line_style, pen.line_pitch)
        self.view.gxview.fill_color(pen.fill_color.int_value)
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
        as the `Pen` constructor.  This using this ensures that default sizing of view unit-based
        dimensions (such as `line_thick`) are not lost when new pens are created.

        :param kwargs: see :class:`Pen`
        :returns: :class:`Pen` instance

        .. versionadded:: 9.2
        """
        return Pen(default=self.pen, **kwargs)

    @property
    def text_def(self):
        """the current text definition as a :class:`Text_def` instance, can be set."""
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
            self.view.gxview.text_color(text_def.color.int_value)

    @_draw
    def point(self, p):
        """
        Draw a point.

        :param p:   point location as `geosoft.gxpy.geometry.Point`

        .. versionadded:: 9.3
        """

        # just draw a box. TODO: MVIEW needs a way to draw a dot, and/or address issue #44
        self._set_dot_symbol()
        self.view.gxview.symbol(p.x, p.y)

    @_draw
    def polypoint(self, pp):
        """
        Draw many points.

        :param pp:  point location as `geosoft.gxpy.geometry.PPoint`, or a pair of VVs (vvx, vvy), or
                    something that `gxpy.geometry.PPoint` can construct into a PP.

        .. versionadded:: 9.3
        """
        self._set_dot_symbol()

        if not((len(pp) == 2) and isinstance(pp[0], gxvv.GXvv)):
            pp = _make_PPoint(pp)
            pp = (gxvv.GXvv(pp.x), gxvv.GXvv(pp.y))
        self.view.gxview.symbols(pp[0].gxvv, pp[1].gxvv)

    @_draw
    def line(self, p2):
        """
        Draw a line on the current plane
        
        :param p2: :class:`geometry.Point2`, or (p1, p2)

        .. versionadded:: 9.2
        """

        p2 = _make_Point2(p2)
        self.view.gxview.line(p2.p0.x, p2.p0.y, p2.p1.x, p2.p1.y)

    @_draw
    def polyline(self, pp, close=False):
        """
        Draw a polyline the current plane
        
        :param pp:      `geosoft.gxpy.geometry.PPoint` instance or something that can be constructed, or a
                        pair of `geosoft.gxpy.vv.GXvv` (xvv, yvv)
        :param close:   if True, draw a polygon, default is a polyline

        .. note::
            Smooth-line polygons must have at least 6 points for the closure to
            appear continuous.

        .. versionadded:: 9.2
        """

        if not((len(pp) == 2) and isinstance(pp[0], gxvv.GXvv)):
            pp = _make_PPoint(pp)
            pp = (gxvv.GXvv(pp.x), gxvv.GXvv(pp.y))

        if close:
            self.view.gxview.poly_line(gxapi.MVIEW_DRAW_POLYGON, pp[0].gxvv, pp[1].gxvv)
        else:
            self.view.gxview.poly_line(gxapi.MVIEW_DRAW_POLYLINE, pp[0].gxvv, pp[1].gxvv)

    @_draw
    def polygon(self, pp, close=False):
        """
        Draw a polygon on the current plane.
        
        :param pp: :class:`geosoft.gxpy.geometry.PPoint`

        .. note::
            Smooth-line polygons must have at least 6 points for the closure to
            appear continuous.

        .. versionadded:: 9.2
        """
        self.polyline(pp, True)

    @_draw
    def rectangle(self, p2):
        """
        Draw a 2D rectangle on the current plane
        :param p2: geometry.Point2, or (p1, p2), or (x0, y0, x2, y2)

        .. versionadded:: 9.2
        """

        p2 = _make_Point2(p2)
        self.view.gxview.rectangle(p2.p0.x, p2.p0.y, p2.p1.x, p2.p1.y)

    @_draw
    def graticule(self, dx=None, dy=None, ddx=None, ddy=None, style=GRATICULE_LINE):
        """
        Draw a graticule reference on a view.

        :param style:   `GRATICULE_LINE`, `GRATICULE_CROSS` or `GRATICULE_DOT`
        :param dx:      vertical line separation
        :param dy:      horizontal line separation
        :param ddh:     horizontal cross size for `GRATICULE_CROSS`
        :param ddv:     vertical cross size for `GRATICULE_CROSS`

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


    def text(self,
             text,
             location=(0,0),
             reference=REF_BOTTOM_LEFT,
             angle=0.,
             text_def=None):
        """
        Draw text in the view.
        
        :param text:        text string.  Use line-feed characters for multi-line text.
        :param location:    (x, y) or a `gxpy.geomerty.Point` location
        :param reference:   Text justification point relative text outline box.
                            The points are:
                            
                                ::
                                    
                                    6 7 8   top left, center, right
                                    3 4 5   middle left, center, right
                                    0 1 2   bottom left, center, right

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
        if not isinstance(location, gxgm.Point):
            location = gxgm.Point(location)
        self.view.gxview.text(text, location.x, location.y)

        if cur_text:
            self.text_def = cur_text

    def contour(self, grid_file_name):
        """
        Draw contours for a grid file.  A default contour interval is determined from the grid.
        
        :param grid_file_name: Grid file name
        
        .. versionadded:: 9.2
        """

        scale, ufac, x0, y0 = self.view.mdf()[1]
        control_file = gx.GXpy().temp_file('.con')
        with open(control_file, 'w+') as f:
            f.write('{},{},{},{}/\n,,-1/\n'.format(scale, ufac, x0, y0))
        geosoft.gxapi.GXMVU.contour(self.view.gxview, control_file, grid_file_name)


class Draw_3d(Draw):
    """
    Create a 3D drawing group within a 3D view.

    3D drawing groups accept 3D drawing objects that can be created using methods of this class.
    2D objects can also be drawn to a 3D group and will be placed on the default drawing plane
    within the 3D view.
    
    :param render_backfaces:    True to turn backface rendering on.
    
    .. versionadded:: 9.2
    """

    def __init__(self,
                 view,
                 *args,
                 render_backfaces=False,
                 **kwargs):

        if not isinstance(view, gxv.View_3d):
            raise GroupException(_t('View is not 3D'))

        kwargs['group_3d'] = True
        super().__init__(view, *args, **kwargs)

        if render_backfaces:
            self.render_backfaces = True

    @property
    def render_backfaces(self):
        """
        True if backface rendering is on, default is off (False).
        Backface rendering controls the rendering of parts of solid objects that
        would normally be hidden from view.  If drawing solid objects that have 
        an open face, such as cylinders with an open end, backface rendering will be
        be turned on.   Once on it cannot be turned off for a view.

        .. versionadded:: 9.2
        """
        return bool(self.view.gxview.get_3d_group_flags(self.number) & 0b1)

    @render_backfaces.setter
    def render_backfaces(self, setting):
        if not setting and self.render_backfaces:
            raise GroupException(_t('Once backface rendering is on it cannot be turned off.'))
        if not self.render_backfaces:
            f3d = (self.view.gxview.get_3d_group_flags(self.number) & 0b11111110) | 0b1
            self.view.gxview.set_3d_group_flags(self.number, f3d)

    @_draw
    def sphere(self, p, radius):
        """
        Draw a sphere.

        :param p:       location as geometry.Point, or (x, y, z)
        :param radius:  sphere radius
        
        .. versionadded:: 9.2
        """

        # solids use the fill color as the object color
        fci = self.pen._fill_color.int_value
        self.view.gxview.fill_color(self.pen._line_color.int_value)

        try:
            p = _make_Point(p)
            self.view.gxview.sphere_3d(p.x, p.y, p.z, radius)
        finally:
            self.view.gxview.fill_color(fci)

    @_draw
    def box_3d(self, p2, wireframe=False):
        """
        Draw a 3D box
        
        :param p2:          box corners as geometry.Point2, or (p0, p1), or (x0, y0, z0, x1, y1, z1)
        :param wireframe:   True to draw edges only

        .. versionadded:: 9.2
        """

        # solids use the fill color as the object color
        fci = self.pen._fill_color.int_value
        self.view.gxview.fill_color(self.pen._line_color.int_value)
        pp = _make_Point2(p2)

        try:
            if wireframe:
                sq = gxgm.PPoint(((pp.p0.x, pp.p0.y, pp.p0.z),
                                  (pp.p0.x, pp.p1.y, pp.p0.z),
                                  (pp.p1.x, pp.p1.y, pp.p0.z),
                                  (pp.p1.x, pp.p0.y, pp.p0.z),
                                  (pp.p0.x, pp.p0.y, pp.p0.z)))
                self.polyline_3d(sq, style=LINE3D_STYLE_TUBE_JOINED)
                sq += (0, 0, pp.p1.z - pp.p0.z)
                self.polyline_3d(sq, style=LINE3D_STYLE_TUBE_JOINED)
                self.cylinder_3d(gxgm.Point2(((pp.p0.x, pp.p0.y, pp.p0.z), (pp.p0.x, pp.p0.y, pp.p1.z))),
                                 radius = self.pen.line_thick * 0.5)
                self.cylinder_3d(gxgm.Point2(((pp.p0.x, pp.p1.y, pp.p0.z), (pp.p0.x, pp.p1.y, pp.p1.z))),
                                 radius = self.pen.line_thick * 0.5)
                self.cylinder_3d(gxgm.Point2(((pp.p1.x, pp.p1.y, pp.p0.z), (pp.p1.x, pp.p1.y, pp.p1.z))),
                                 radius = self.pen.line_thick * 0.5)
                self.cylinder_3d(gxgm.Point2(((pp.p1.x, pp.p0.y, pp.p0.z), (pp.p1.x, pp.p0.y, pp.p1.z))),
                                 radius = self.pen.line_thick * 0.5)

            else:
                self.view.gxview.box_3d(pp.p0.x, pp.p0.y, pp.p0.z,
                                        pp.p1.x, pp.p1.y, pp.p1.z)
        finally:
            self.view.gxview.fill_color(fci)


    @_draw
    def cylinder_3d(self, p2, radius, r2=None, close=CYLINDER_CLOSE_ALL):
        """
        Draw a cylinder.
        
        :param p2:      end points as geometry.Point2, or (p0, p1), or (x0, y0, z0, x1, y1, z1)
        :param radius:  cylinder radius.
        :param r2:      end radius if different from the start
        :param close:   one of:
        
                            ::
                
                                CYLINDER_OPEN
                                CYLINDER_CLOSE_START
                                CYLINDER_CLOSE_END
                                CYLINDER_CLOSE_ALL

        .. versionadded:: 9.2
        """

        # solids use the fill color as the object color
        fci = self.pen._fill_color.int_value
        self.view.gxview.fill_color(self.pen._line_color.int_value)

        if close != CYLINDER_CLOSE_ALL:
            self.render_backfaces = True

        try:
            p2 = _make_Point2(p2)
            if r2 is None:
                r2 = radius
            self.view.gxview.cylinder_3d(p2.p0.x, p2.p0.y, p2.p0.z,
                                         p2.p1.x, p2.p1.y, p2.p1.z,
                                         radius, r2,
                                         close)
        finally:
            self.view.gxview.fill_color(fci)


    @_draw
    def cone_3d(self, p2, radius):
        """
        Draw a cone.

        :param p2:      end points as geometry.Point2, or (p0, p1), or (x0, y0, z0, x1, y1, z1).
        :param radius:  cone base radius, base is as the the first point of p2.

        .. versionadded:: 9.2
        """
        self.cylinder_3d(p2, radius, r2=0.)

    def _poly_3d(self, points, ptype, smooth=gxapi.MVIEW_DRAWOBJ3D_MODE_FLAT):
        vvx, vvy, vvz = points.make_xyz_vv()
        null_vv = gxapi.GXVV.null()
        self.view.gxview.draw_object_3d(ptype, smooth,
                                        vvx.length, 0,
                                        vvx.gxvv, vvy.gxvv, vvz.gxvv,
                                        null_vv, null_vv, null_vv,
                                        null_vv, null_vv, null_vv)
    @_draw
    def polypoint_3d(self, points, style=POINT_STYLE_DOT):
        """
        Draw multiple points.
        
        :param points:  points to draw, :class:`geosoft.gxpy.geometry.PPoint` instance, or array-like [x,y,z]
        :param style:   POINT_STYLE_DOT or POINT_STYLE_SPHERE.  Dots are fast and intended for point clouds.
                        The current pen thickness is used as the sphere sizes.
        
        .. versionadded:: 9.2
        """

        points = _make_PPoint(points)
        if style == POINT_STYLE_DOT:
            self._poly_3d(points, gxapi.MVIEW_DRAWOBJ3D_ENTITY_POINTS)
        else:
            radius = self.pen.line_thick * 0.5
            for i in range(points.length):
                self.sphere(points[i], radius=radius)

    @_draw
    def polyline_3d(self, points, style=LINE3D_STYLE_LINE):
        """
        Draw a polyline.
        
        :param points:  verticies of the polyline, :class:`geosoft.gxpy.geometry.PPoint` instance, or array-like [x,y,z]
        :param style:   LINE3D_STYLE_LINE, LINE3D_STYLE_TUBE or LINE3D_STYLE_TUBE_JOINED.
                        Lines are single-pixel-wide.  Tubes have width defined by the pen line thickness.
                        Joined tubes have a joints and rounded ends.

        .. versionadded:: 9.2 
        """
        points = _make_PPoint(points)
        if points.length < 2:
            raise GroupException(_t('Need at least two points.'))
        if style == LINE3D_STYLE_LINE:
            vvx, vvy, vvz = points.make_xyz_vv()
            self.view.gxview.poly_line_3d(vvx.gxvv, vvy.gxvv, vvz.gxvv)
        else:
            radius = self.pen.line_thick * 0.5
            self.pen = Pen(fill_color=self.pen.line_color, default=self.pen)
            for i in range(points.length-1):
                self.cylinder_3d(gxgm.Point2((points[i], points[i+1])), radius=radius)
            if style == LINE3D_STYLE_TUBE_JOINED:
                for i in range(points.length):
                    self.sphere(points[i], radius=radius)

    def polydata_3d(self,
                    data,
                    render_info_func=None,
                    passback=None):
        """
        Create 3D objects rendered using data attributes.

        :param view:                a 3D view in which to place the group
        :param data:                iterable that yields items passed to your `render_info_func` callback
        :param render_info_func:    a callback that given `(item, passback)` returns the rendering `(symbol_type,
                                    geometry, color_integer, attibute)`:
                                    
                                    ================== ======== =============== =========
                                    Symbol             Geometry Color           Attribute
                                    ================== ======== =============== =========
                                    SYMBOL_3D_SPHERE   Point    Color.int_value radius
                                    SYMBOL_3D_CUBE     Point2   Color.int_value None
                                    SYMBOL_3D_CYLINDER Point2   Color.int_value radius
                                    SYMBOL_3D_CONE     Point2   Color.int_value radius
                                    ================== ======== =============== =========

        :param passback:            something passed back to your render_info_func function, default None.
        
        **Example**
        
        .. code::
        
            import geosoft.gxpy.geometry as gxgm
            import geosof.gxpy.view as gxv
            import geosogt.gxpy.group as gxg
            
            def render_spheres(xyz, cmap_radius):
                color, radius = cmap_radius
                return gxg.SYMBOL_3D_SPHERE, xyz, color.int_value, radius
            
            data = gxgm.PPoint(((5, 5, 5), (7, 5, 5), (7, 7, 7)))
            with gxv.View_3d.new('example_polydata') as v:
                with gxg.Draw_3d(v, 'red_spheres') as g:
                    g.polydata_3d(data, render_spheres, (gxg.Color('r'), 0.25))

        .. versionadded:: 9.2
        """

        cint = None
        for item in data:
            render = render_info_func(item, passback)
            if render:
                symbol, geometry, color, attribute = render
                if color != cint:
                    self.view.gxview.fill_color(color)
                    cint = color

                if symbol == SYMBOL_3D_SPHERE:
                    self.view.gxview.sphere_3d(geometry[0], geometry[1], geometry[2], attribute)

                elif symbol == SYMBOL_3D_CUBE:
                    self.view.gxview.box_3d(geometry.p0.x, geometry.p0.y, geometry.p0.z,
                                            geometry.p1.x, geometry.p1.y, geometry.p1.z)

                elif symbol == SYMBOL_3D_CYLINDER:
                    self.view.gxview.cylinder_3d(geometry.p0.x, geometry.p0.y, geometry.p0.z,
                                                 geometry.p1.x, geometry.p1.y, geometry.p1.z,
                                                 attribute, attribute, CYLINDER_CLOSE_ALL)

                elif symbol == SYMBOL_3D_CONE:
                    self.view.gxview.cylinder_3d(geometry.p0.x, geometry.p0.y, geometry.p0.z,
                                                 geometry.p1.x, geometry.p1.y, geometry.p1.z,
                                                 attribute, 0, CYLINDER_CLOSE_ALL)

                else:
                    raise GroupException(_t('Symbol type not implemented'))


def contour(view, group_name, grid_file_name, **kwargs):
    """
    Create a contour group from a grid file.  A default contour interval is determined from the grid.

    :param group_name: name for the contour group
    :param grid_file_name: Grid file name

    .. versionadded:: 9.3
    """

    with Draw(view, group_name) as g:
        g.contour(grid_file_name, **kwargs)


def legend_color_bar(view,
                     group_name,
                     cmap,
                     cmap2=None,
                     bar_location=COLOR_BAR_RIGHT,
                     location=None,
                     decimals=None,
                     annotation_height=0.2,
                     annotation_offset=None,
                     annotation_side=COLOR_BAR_ANNOTATE_RIGHT,
                     box_size=None,
                     bar_width=None,
                     max_bar_size=None,
                     minimum_gap=0,
                     post_end_values=False,
                     annotate_vertical=False,
                     division_line=1,
                     interval_1=None,
                     interval_2=None,
                     title=None):
    """
    Draw a color bar legend from :class:Color_map coloring definitions.

    :param view:                :class:`gxpy.view.View` instance in which to place the bar
    :param group_name:          name for the color_bar group, overwrites group if it exists.
    :param cmap:                :class:`Color_map` instance
    :param cmap2:               optional orthogonal blended :class:`Color_map` instance.  If making
                                a shaded-color legend, provide the shaded color map here.
    :param bar_location:        one of:

        ::

            COLOR_BAR_RIGHT = 0
            COLOR_BAR_LEFT = 1
            COLOR_BAR_BOTTOM = 2
            COLOR_BAR_TOP = 3

    :param location:            offset or (x, y) offset from `bar_location` reference point, in cm.  The default is
                                determined to center the bar off the location side specified.
    :param decimals:            annotation decimal places
    :param annotation_height:   annotation number height (cm)
    :param annotation_offset:   offset of annotations from the bar (cm)
    :param annotation_side:     side of the bar for annotations

        ::

            COLOR_BAR_ANNOTATE_RIGHT = 1
            COLOR_BAR_ANNOTATE_LEFT = -1
            COLOR_BAR_ANNOTATE_TOP = 1
            COLOR_BAR_ANNOTATE_BOTTOM = -1

    :param box_size:            box size, height for vertical bars, width for horizontal bars
    :param bar_width:           width of the color boxes, horizontal for vertical bars, vertical for horizontal bars
    :param max_bar_size:        maximum bar size, default is the size of the view edge
    :param minimum_gap:         minimum gap to between annotations.  Annotations are dropped in necessary.
    :param post_end_values:     post the maximum and minimum values
    :param annotate_vertical:   True to orient labels vertically 
    :param division_line:       0, no division lines, 1 - line, 2 - tick
    :param interval_1:          Major annotation increment, default annotates everything
    :param interval_2:          secondary smaller annotations, reduced to 1/10, 1/5, 1/4 or 1/2 of interval_1.
                                Default chooses something reasonable.
    :param title:               bar title, use new-lines for sub-titles.  Default uses the title and unit_of_measure
                                from `cmap`.

    .. versionadded:: 9.2
    """

    # ensure group name is unique in the view
    while group_name in view.group_list:
        group_name += '_'

    # default decimals
    if decimals is None:
        decimals = 1
        minz = maxz = cmap.color_map[0][0]
        for c in cmap.color_map:
            z = c[0]
            if z:
                if z < minz:
                    minz = z
                elif z > maxz:
                    maxz = z
        range = maxz - minz
        while range < 100:
            range *= 10.
            decimals += 1

    itr = cmap.gxitr
    with Draw(view, group_name) as g:

        v_area = gxgm.Point2(view.extent_clip)
        v_width = v_area.dimension[0]
        v_height = v_area.dimension[1]

        if (bar_location == COLOR_BAR_LEFT) or (bar_location == COLOR_BAR_RIGHT):
            bar_orient = 0
            default_bar_size = v_height * 0.8
            if max_bar_size is None:
                max_bar_size = v_height

        else:
            bar_orient = 1
            default_bar_size = v_width * 0.8
            if max_bar_size is None:
                max_bar_size = v_width * 0.8

        # bar cell sizing
        def_box_size = default_bar_size / itr.get_size()
        if box_size is None:
            box_size = min(0.4 * view.units_per_map_cm, def_box_size)
        else:
            box_size *= view.units_per_map_cm
        if bar_width is None:
            if bar_location in (COLOR_BAR_LEFT, COLOR_BAR_RIGHT):
                bar_width = max(0.4 * view.units_per_map_cm, box_size * 2.0)
            else:
                bar_width = max(0.4 * view.units_per_map_cm, box_size)
        else:
            bar_width *= view.units_per_map_cm
        if max_bar_size is not None:
            box_size = min(box_size, max_bar_size / itr.get_size())

        annotation_height *= view.units_per_map_cm
        if annotation_offset is None:
            annotation_offset = annotation_height * 0.5
        else:
            annotation_offset *= view.units_per_map_cm
        annotation_offset *= annotation_side
        minimum_gap *= view.units_per_map_cm

        cdict = {
            "BAR_ORIENTATION": bar_orient,
            "DECIMALS": decimals,
            'ANNOFF': annotation_offset,
            'BOX_SIZE': box_size,
            'BAR_WIDTH': bar_width,
            'MINIMUM_GAP': minimum_gap,
            "X": v_area.centroid.x,
            "Y": v_area.centroid.y,
            "POST_MAXMIN": 1 if post_end_values else 0,
            "LABEL_ORIENTATION": 0 if annotate_vertical else 1,
            "DIVISION_STYLE": division_line,
        }

        if interval_1:
            if interval_2 is None:
                interval_2 = gxapi.rDUMMY
            if interval_2 <= interval_1 / 10.:
                interval_2 = interval_1 / 10.
            elif interval_2 <= interval_1 / 5.:
                interval_2 = interval_1 / 5.
            elif interval_2 <= interval_1 / 4.:
                interval_2 = interval_1 / 4.
            elif interval_2 <= interval_1 / 2.:
                interval_2 = interval_1 / 2.
            else:
                interval_2 = gxapi.rDUMMY
            cdict["FIXED_INTERVAL"] = interval_1
            cdict["FIXED_MINOR_INTERVAL"] = interval_2

        g.text_def = Text_def(height=annotation_height)
        if cmap2 is None:
            itr2 = gxapi.GXITR.null()
        else:
            itr2 = cmap2.gxitr
        gxapi.GXMVU.color_bar_reg(view.gxview, itr, itr2, gxu.reg_from_dict(cdict, 100, json_encode=False))

        if title is None:
            if cmap.unit_of_measure:
                title = '{}\n({})'.format(cmap.title, cmap.unit_of_measure)
            else:
                title = cmap.title

        if title:

            title_height = annotation_height * 1.5
            g.text_def = Text_def(height=title_height, weight=FONT_WEIGHT_BOLD)
            p = gxgm.Point(edge_reference(g.extent, REF_BOTTOM_CENTER))
            p -= (0, title_height * 0.5)
            try:
                tline = title[:title.index('\n')]
                title = title[title.index('\n') + 1:]
            except:
                tline = title
                title = ''
            g.text(tline, p, reference=REF_TOP_CENTER)

            if title:
                g.text_def = Text_def(height=title_height * 0.8, weight=FONT_WEIGHT_LIGHT)
                p -= (0, title_height * 1.5)
                g.text(title, p, reference=REF_TOP_CENTER)

        # locate the bar
        default_offset = 1.5 * view.units_per_map_cm
        if location and (not hasattr(location, '__iter__')):
            default_offset = location * view.units_per_map_cm
            location = None
        if location is not None:
            location = location[0] * view.units_per_map_cm, location[1] * view.units_per_map_cm

        area = gxgm.Point2(view.extent_clip)
        if bar_location == COLOR_BAR_LEFT:
            if location is None:
                location = (-default_offset, 0)
            xy = edge_reference(area, REF_CENTER_LEFT)
            reference = REF_CENTER_RIGHT
        elif bar_location == COLOR_BAR_BOTTOM:
            if location is None:
                location = (0, -default_offset)
            xy = edge_reference(area, REF_BOTTOM_CENTER)
            reference = REF_TOP_CENTER
        elif bar_location == COLOR_BAR_TOP:
            if location is None:
                location = (0, default_offset)
            xy = edge_reference(area, REF_TOP_CENTER)
            reference = REF_BOTTOM_CENTER
        else: #BAR_RIGHT
            if location is None:
                location = (default_offset, 0)
            xy = edge_reference(area, REF_CENTER_RIGHT)
            reference = REF_CENTER_LEFT

        location = xy + location
        g.locate(location, reference)
            
                
class Color:
    """
    Colours, which are stored as a 32-bit color integer.

    :param color:   string descriptor (eg. 'R255G0B125'), color letter R, G, B, C, M, Y, H, S or V.;
                    tuple (r, g, b), (c, m, y) or (h, s, v), each item defined in the range 0 to 255;
                    32-bit color number, which can be an item selected from the following list:

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

    :param model:   model of the tuple: 
    
                    ::
                    
                        CMODEL_RGB (default)
                        CMODEL_CMY
                        CMODEL_HSV

    .. versionadded:: 9.2
    """

    def __init__(self, color, model=CMODEL_RGB):

        if isinstance(color, Color):
            self._color = color.int_value

        elif isinstance(color, int):
            self.int_value = color

        elif isinstance(color, str):
            self._color = gxapi.GXMVIEW.color(color)

        else:

            if model == CMODEL_CMY:
                self.cmy = color

            elif model == CMODEL_HSV:
                hue = max(0, min(255, color[0]))
                sat = max(0, min(255, color[1]))
                val = max(0, min(255, color[2]))
                self._color = gxapi.GXMVIEW.color_hsv(hue, sat, val)

            else:
                self.rgb = color

    def __eq__(self, other):
        return self.int_value == other.int_value

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def int_value(self):
        """ color as a 32-bit color integer, can be set"""
        return self._color

    @int_value.setter
    def int_value(self, color):
        if color < 0:
            raise GroupException(_t('Invalid color integer {}, must be >= 0').format(color))
        self._color = int(color)

    @property
    def rgb(self):
        """color as an (red, green, brue) tuple, can be set"""
        if self.int_value == 0:
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
        """color as an (cyan, magenta, yellow) tuple, can be set"""
        if self.int_value == 0:
            return None
        red, green, blue = self.rgb
        return 255 - red, 255 - green, 255 - blue

    @cmy.setter
    def cmy(self, cmy):
        self.rgb = (255 - cmy[0], 255 - cmy[1], 255 - cmy[2])

    def adjust_brightness(self, brightness):
        """
        Return a :class:`Color` instance adjusted for brightness.
        
        .. versionadded:: 9.2
        """
        if brightness == 0.:
            return self

        c, m, y = self.rgb
        if brightness > 0.0:
            w = round(brightness * 255)
            c = max(c - w, 0)
            m = max(m - w, 0)
            y = max(y - w, 0)
            return Color((c, m, y), model = CMODEL_CMY)
        else:
            k = round(-brightness * 255)
            c = max(c + k, 255)
            m = max(m + k, 255)
            y = max(y + k, 255)
            return Color((c, m, y), model=CMODEL_CMY)

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

    :Properties:

        :height:        font height in view units
        :font:          font name
        :weight:        font weight, one of FONT_WEIGHT
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
                raise GroupException(_t('Invalid text definition parameter ({})'.format(k)))

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
        """text color as a :class:`Color` instance, can be set"""
        return self._color

    @color.setter
    def color(self, color):
        if isinstance(color, Color):
            self._color = color
        else:
            self._color = Color(color)

    @property
    def font(self):
        """text font name, can be set."""
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
        """text line thickness determined from the font weight, can be set."""
        return thickness_from_font_weight(self.weight, self.height)

    @line_thick.setter
    def line_thick(self, line_thick):
        self.weight = font_weight_from_line_thickness(line_thick, self.height)

    @property
    def slant(self):
        """text slant, 15 for italics, 0 for not italics, can be set.  If set, any slant
           greater than 5 will result in a 15 degree slant to create italics."""
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
        Mapplot text definition string, assumes scaling in cm.
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
    Geosoft Pen class.  
    
    The default dimensioned properties (`line_thick`, `line_pitch`,
    `pat_size` and `pat_thick`) assume the view units are cm, and this is usually
    only the case for the base view.  For views in other units either
    explicitly define the dimention in view units, or pass `factor` set 
    the the view :attr:`geosoft.gxpy.view.View.units_per_map_cm`.

    :param line_color:  line :class:`Color` instance, default is black
    :param fill_color:  fill :class:`Color` instance, default is transparent
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

    :param pat_number:  pattern number for filled patterns (refer to `etc/default.pat`) default 0, flood fill
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
    :param default:     default :class:`Pen` instance, if specified defaults are established from this
    :param factor:      default spatial properties are multiplied by this factor.  This is useful
                        for creating pens scaled to the units of a view.  The default pen properties
                        are scaled to cm.  Typically you will pass :attr:`geosoft.gxpy.view.View.units_per_map_cm`.

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
                raise GroupException(_t('Invalid pen parameter ({})'.format(k)))

    @classmethod
    def from_mapplot_string(cls, cstr):
        """
        Create a :class:`Pen` instance from a mapplot-style string descriptor using either a
        krgbKRGB or kcmyKCMY color model.  Lower case letters indicate line color, uppercase
        indicates fill color, 'k', 'K' for black.  Each letter may be followed by an intensity
        between 0 and 255.  If an intensity is not specified 255 is assumed.

        Line thickness can be defined by 't' followed by a thickness in 1000'th of the view unit,
        which for the default 'base' view would be microns.

        :param cstr:    mapplot-style color definition
                      
        Examples:
        
            =========== ==============================================
            'r'         red line
            'R'         red fill
            'rG64'      red line, light-green fill
            'c64'       light cyan line, equivalent to 'R191G255B255'
            'c64K96'    light cyan line, light-grey fill
            'bt500'     blue line, 0.5 units thick
            =========== ==============================================
            
        .. versionadded:: 9.2
        """

        def color_model(cstr):
            s = cstr.lower()
            for c in 'cmy':
                if c in s:
                    return 'cmyk'
            return 'rgbk'

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
                    if model[0] == 'c' or model[0] == 'C':
                        return add_k((255 - get_part(cstr, cc[0]),
                                      255 - get_part(cstr, cc[1]),
                                      255 - get_part(cstr, cc[2])),
                                     k)
                    else:
                        return add_k((get_part(cstr, cc[0]),
                                      get_part(cstr, cc[1]),
                                      get_part(cstr, cc[2])),
                                     k)
                else:
                    return add_k((255, 255, 255), k)
            else:
                return C_TRANSPARENT

        model = color_model(cstr)
        line_color = color(cstr, model)
        fill_color = color(cstr, model.upper())
        line_thick = max(1, get_part(cstr, 't', 1)) * 0.001

        return cls(line_color=line_color, fill_color=fill_color, line_thick=line_thick)

    def __eq__(self, other):
        for k, v in self.__dict__.items():
            if other.__dict__[k] != v:
                return False
        return True

    @property
    def line_color(self):
        """pen line color as a :class:`color` instance, can be set."""
        return self._line_color

    @line_color.setter
    def line_color(self, color):
        if isinstance(color, Color):
            self._line_color = color
        else:
            self._line_color = Color(color)

    @property
    def fill_color(self):
        return self._fill_color

    @fill_color.setter
    def fill_color(self, color):
        """pen fill color as a :class:`color` instance, can be set."""
        if isinstance(color, Color):
            self._fill_color = color
        else:
            self._fill_color = Color(color)

    @property
    def mapplot_string(self):
        """line/fill colour and thickness string suing mapplor format, eg. 'kR125B64t1000'"""
        s = ''
        if self._line_color.int_value != C_TRANSPARENT:
            if self._line_color.int_value == C_BLACK:
                s += 'k'
            else:
                c = self._line_color.rgb
                s += 'r{}g{}b{}'.format(c[0], c[1], c[2])
        if self._fill_color.int_value != C_TRANSPARENT:
            if self._line_color.int_value == C_BLACK:
                s += 'K'
            else:
                c = self._fill_color.rgb
                s += 'R{}G{}B{}'.format(c[0], c[1], c[2])

        return s + 't{}'.format(int(self.line_thick * 1000.))


class Color_symbols_group(Group):
    """
    Data represented as colored symbols based on a :class:`Color_map`.

    :Constructors:

        ============ =======================================
        :func:`new`  create a new symbol group in a view
        :func:`open` open an existing symbol group in a view
        ============ =======================================

    """

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__del__()

    def __del__(self):
        if hasattr(self, '_gxcsymb'):
            self._gxcsymb = None
        if hasattr(self, '_close'):
            self._close()

    def __init__(self, view, group_name, **kwargs):

        self._gxcsymb = None
        super().__init__(view, group_name, **kwargs)

    @classmethod
    def new(cls,
            view,
            name,
            data,
            color_map,
            symbol_def=None,
            symbol=SYMBOL_CIRCLE,
            mode=REPLACE,
            **kwargs):
        """
        Create a new color symbols group with color mapping. If the group exists a new unique name is
        constructed.

        :param view:            the view in which to place the group
        :param group_name:      group name
        :param data:            iterable that yields `((x, y), data)`, or `((x, y, z), data, ...)`.  Only the
                                first `data` value is used.
        :param color_map:       symbol fill color :class:`Color_map`.
                                Symbols are filled with the color lookup using `data`.
        :param symbol_def:      :class:`Text_def` defines the symbol font to use, normally
                                `symbols.gfn` is expected, and if used the symbols defined by the `SYMBOL` manifest
                                are valid.  For other fonts you will get the symbol requested.  The default is
                                `Text_def(font='symbols.gfn', color='k', weight=FONT_WEIGHT_ULTRALIGHT)`
        :param symbol:          the symbol to plot, normally one of `SYMBOL`.
        :param mode:            REPLACE (default) or NEW, which creates a new unique name if group exists
        :return:                :class:`Color_symbols_group` instance

        .. versionadded:: 9.2
        """

        def valid(xyd):
            if xyd[0][0] is None or xyd[0][1] is None or xyd[1] is None:
                return False
            return True

        cs = cls(view, name, mode=mode, **kwargs)
        cs._gxcsymb = gxapi.GXCSYMB.create(color_map.save_file())

        if symbol_def is None:
            symbol_def = Text_def(font='geosoft.gfn',
                                  height=(0.25 * view.units_per_map_cm),
                                  weight=FONT_WEIGHT_ULTRALIGHT,
                                  color=C_BLACK)
        cs._gxcsymb.set_font(symbol_def.font, symbol_def.gfn, symbol_def.weight, symbol_def.italics)
        cs._gxcsymb.set_static_col(symbol_def.color.int_value, 0)
        cs._gxcsymb.set_scale(symbol_def.height)
        cs._gxcsymb.set_number(symbol)

        xy = gxgm.PPoint([xy[0] for xy in data if valid(xy)])
        cs._gxcsymb.add_data(gxvv.GXvv(xy.x).gxvv,
                          gxvv.GXvv(xy.y).gxvv,
                          gxvv.GXvv([d[1] for d in data if valid(d)]).gxvv)
        view.gxview.col_symbol(cs.name, cs._gxcsymb)

        if cs.unit_of_measure:
            color_map.unit_of_measure = cs.unit_of_measure

        return cs

    @classmethod
    def open(cls,
             view,
             group_name):
        """
        Open an existing color symbols group.

        :param view:        view that contains the group
        :param group_name:  name of the group, which must be a color symbols group
        :return:            :class:`Color_symbols_group` instance

        .. versionadded:: 9.2
        """
        cs = cls(view, group_name, mode=READ_ONLY)
        group_number = view.gxview.find_group(group_name)
        cs._gxcsymb = view.gxview.get_col_symbol(group_number)
        return cs

    def color_map(self):
        """
        Return the :class:`geosoft.gxpy.group.Color_map` of a color symbol group.

        .. versionadded:: 9.3
        """

        itr = gxapi.GXITR.create()
        self._gxcsymb.get_itr(itr)
        cmap = geosoft.gxpy.group.Color_map(itr)
        cmap.title = self.name
        cmap.unit_of_measure = self.unit_of_measure

        return cmap


class Aggregate_group(Group):
    """
    Aggregate group in a view
    
    :Constructors:

        ======== ================================
        `open()` open an existing aggregate group
        `new()`  create a new aggregate group
        ======== ================================

    :Properties:
    
        :name:  aggregate group name
        :agg:   :class:`gxpy.agg.Aggregate_image` instance
    
    .. versionadded:: 9.2
    """

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__del__()

    def __del__(self):
        if hasattr(self, 'agg'):
            self.agg = None
        if hasattr(self, '_close'):
            self._close()

    def __init__(self, view, group_name, mode):

        self.agg = None
        super().__init__(view, group_name, mode=mode)


    @classmethod
    def new(cls, view, agg, name=None, mode=REPLACE):
        """
        Create a new aggregate group in a view.

        :param view:    `geosoft.gxpy.view.View` or `geosoft.gxpy.view.View_3d` instance
        :param agg:     `geosoft.gxpy.agg.Aggregate` instance.
        :param name:    group name, default is the aggregate name
        :param mode:    REPLACE (default) or NEW, which creates a unique name if the group exists

        .. versionadded:: 9.2
        """

        if name is None:
            name = agg.name
        agg_group = cls(view, name, mode=mode)
        agg_group.agg = agg
        view.gxview.aggregate(agg.gxagg, agg_group.name)
        return agg_group

    @classmethod
    def open(cls,
             view,
             group_name):
        """
        Open an existing aggregate group in a view.

        :param view:        `geosoft.gxpy.view.View` or `geosoft.gxpy.view.View_3d` instance
        :param group_name:  group name (or number)

        .. versionadded:: 9.2
        """
        agg_group = cls(view, group_name, mode=READ_ONLY)
        if isinstance(group_name, int):
            group_number = group_name
        else:
            group_number = view.gxview.find_group(agg_group.name)
        agg_group.agg = gxagg.Aggregate_image.open(view.gxview.get_aggregate(group_number))
        return agg_group


class Vox_display_group(Group):
    """
    Vox display group in a view.  Use class methods `new()` and `open()`
    to create instances of `Vox_display_group`.

    :Constructors:

        ======== ==================================
        `open()` open an existing vox_display group
        `new()`  create a new vox_display group
        ======== ==================================

   .. versionadded:: 9.3.1
    """

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__del__()

    def __del__(self):
        if hasattr(self, '_voxd'):
            self._voxd = None
        if hasattr(self, '_close'):
            self._close()

    def __init__(self, view3d, group_name, mode=REPLACE):

        self._voxd = None
        if not view3d.is_3d:
            raise GroupException(_t('View must be 3d'))
        super().__init__(view3d, group_name, mode=mode)

    @classmethod
    def new(cls, view3d, voxd, name=None, mode=REPLACE):
        """
        Add a Vox_display as a new group in the view

        :param view3d:  `geosoft.gxpy.view.View_3d` instance
        :param voxd:    `geosoft.gxpy.vox_display.Vox_display` instance
        :param name:    group name, default is the voxd name
        :param mode:    REPLACE (default) or NEW, which creates a unique name if the group exists

        .. versionadded:: 9.3.1
        """

        if name is None:
            name = voxd.name
        voxd_group = cls(view3d, name, mode=mode)
        if voxd.vector:
            scale, height_base_ratio, max_base_size_ratio, max_cones = voxd.vector_cone_specs
            if max_cones is None:
                max_cones = gxapi.iDUMMY
            minimum_value = voxd.shell_limits[0]
            if minimum_value is None:
                minimum_value = 0.
            view3d.gxview.draw_vector_voxel_vectors(voxd.vox.gxvox,
                                                    name,
                                                    voxd.color_map.gxitr,
                                                    scale,
                                                    height_base_ratio,
                                                    max_base_size_ratio,
                                                    minimum_value,
                                                    max_cones)
        else:
            view3d.gxview.voxd(voxd.gxvoxd, voxd_group.name)
        voxd_group._voxd = voxd
        voxd_group.unit_of_measure = voxd.unit_of_measure
        return voxd_group

    @classmethod
    def open(cls,
             view,
             group_name):
        """
        Open an existing `Vox_display_group` in a 3d view.

        :param view:        the 3d view
        :param group_name:  the name of the group to open, must be a `gxapi.GXVOXD` or
                            `gxapi.GXVECTOR3D`.

        .. versionadded: 9.3.1
        """
        voxd_group = cls(view, group_name, mode=READ_ONLY)
        if view.gxview.is_group(group_name, gxapi.MVIEW_IS_VOXD):
            voxd_group._voxd = gxvoxd.Vox_display.open(voxd_group.view.gxview.get_voxd(voxd_group.number))
        elif view.gxview.is_group(group_name, gxapi.MVIEW_IS_VECTOR3D):
            voxd_group._voxd = gxvoxd.Vox_display.open(voxd_group.view.gxview.get_vector_3d(voxd_group.number),
                                                       name=group_name + ".geosoft_vectorvoxel")
        else:
            raise GroupException('Group "{}" is not a GXVOXD or a GXVECTOR3D'.format(group_name))
        return voxd_group

    @property
    def voxd(self):
        """
        The `geosoft.gxpy.vox_display.Vox_display` for this vox group.

        .. versionadded:: 9.3.1
        """
        return self._voxd


class Color_map:
    """
    Color map for establishing data color mapping for things like aggregates and color symbols.
    
    :param cmap:    the name of a Geosoft color map file (`.tbl, .zon, .itr, .agg`) from which to
                    establish the initial colors.  If the file does not have zone values,
                    which is the case for a `.tbl` file, the Color_map will be uninitialized and you
                    can use one of the `set` methods to establish zone values.
                    
                    You can also provide an `int`, which will create an uninitialized map of the the
                    specified length, or a :class:`geosoft.gxapi.GXITR` instance.
                    
                    If not specified the Geosoft default color table is used.

    :param title:   Color map title which is displayed in the color map legend.
    :param unit_of_measure: Unit of measure to be displayed in a color map legend.

    .. versionadded:: 9.2

    .. versionchanged:: 9.3
        changed `units` to `unit_of_measure` for consistency across gxpy
    """

    def __init__(self, cmap=None, title=None, unit_of_measure=None):

        if cmap is None:
            sr = gxapi.str_ref()
            if gxapi.GXSYS.global_('MONTAJ.DEFAULT_COLOUR', sr) == 0:
                cmap = sr.value
            if not cmap:
                cmap = 'colour'

        if isinstance(cmap, str):
            if cmap == 'color':
                cmap = 'colour'
            base, ext = os.path.splitext(cmap)
            if not ext:
                cmap = cmap + '.tbl'
            self.file_name = cmap
            self.gxitr = gxapi.GXITR.create_file(cmap)

        elif isinstance(cmap, int):

            self.gxitr = gxapi.GXITR.create()
            self.gxitr.set_size(cmap)
            for i in range(cmap):
                self.__setitem__(i, (gxapi.rMAX, C_BLACK))
            self.file_name = None

        elif isinstance(cmap, gxapi.GXITR):
            self.gxitr = cmap

        else:
            raise ValueError('Cannot make a color map from: {}'.format(cmap))

        self._next = 0
        self._title = title
        self._units= unit_of_measure

    def __iter__(self):
        return self

    def __next__(self):
        if self._next >= self.length:
            self._next = 0
            raise StopIteration
        else:
            self._next += 1
            return self.__getitem__(self._next - 1)

    def __getitem__(self, item):
        if item < 0 or item >= self.length:
            raise IndexError
        ir = gxapi.int_ref()
        self.gxitr.get_zone_color(item, ir)
        color = Color(ir.value)
        if item < self.length - 1:
            v = self.gxitr.get_zone_value(item)
        else:
            v = None
        return v, color

    def __setitem__(self, item, setting):
        if item < 0 or item >= self.length:
            raise IndexError
        if not isinstance(setting[1], int):
            setting = (setting[0], setting[1].int_value)
        self.gxitr.set_zone_color(item, setting[1])
        if item < self.length - 1:
            self.gxitr.set_zone_value(item, setting[0])

    def __eq__(self, other):
        if self.length != other.length:
            return False
        for i in range(self.length):
            if self[i] != other[i]:
                return False
        return True

    @property
    def title(self):
        """
        Title, usually the name of the data from which the color bar was made or is intended. 
        None if no title
        
        .. versionadded:: 9.2
        """
        return self._title

    @title.setter
    def title(self, title):
        if title:
            self._title = str(title)
        else:
            self._title = None

    @property
    def unit_of_measure(self):
        """
        Data unit of measure for the data from which the color bar was made or is intended.
        None if the unit of measure is unknown.

        .. versionadded:: 9.2
        """
        return self._units

    @unit_of_measure.setter
    def unit_of_measure(self, units):
        if units:
            self._units = str(units)
        else:
            self._units = None

    @property
    def length(self):
        """ 
        Number of color zones in the map.
        """
        return self.gxitr.get_size()

    @property
    def brightness(self):
        """
        Brightness is a value between -1 (black) and +1 (white),  The default is 0.
        :returns: brightness, -1 to +1
        
        .. versionadded:: 9.2
        """
        return self.gxitr.get_brightness()

    @property
    def color_map(self):
        """list of zone limts, colours in the color map"""
        return [vc for vc in self]

    @property
    def color_map_rgb(self):
        """list of zone limits and (red, green, blue) colours"""
        return [(vc[0], vc[1].rgb) for vc in self]

    @brightness.setter
    def brightness(self, value):
        """Map brightness between -1 (black ) and +1 (white.  Can be set."""
        self.gxitr.change_brightness(value)

    @property
    def model_type(self):
        """Geosoft colour model used in the Geosoft :class:`geosoft.gxapi.GXITR`"""
        return self.gxitr.get_zone_model_type()

    @property
    def initialized(self):
        """
        Returns True if the color_map has been initialized to have zone boundaries.
        
        .. versionadded:: 9.2
        """
        return self.length > 0 and self[0][0] != gxapi.rMAX

    def set_sequential(self, start=0, increment=1):
        """
        Set color map zones based on a start and increment between each color zone.
        
        :param start:       minimum zone boundary, values <= this value will have the first color
        :param increment:   increment between each color.
        
        .. versionadded:: 9.2
        """
        if increment <= 0:
            raise ValueError(_t('increment must be > 0.'))
        for i in range(self.length - 1):
            self.gxitr.set_zone_value(i, start + i * increment)

    def set_linear(self, minimum, maximum, inner_limits=True, contour_interval=None):
        """
        Set the map boundaries based on a linear distribution between minimum and maximum.
        
        :param minimum:             minimum 
        :param maximum:             maximum
        :param inner_limits:        True if the range specifies the inner limits of the color mappings, in which
                                    case values less than or equal to the minimum are mapped to the first color
                                    and colors greater than the maximum are mapped to the last color.  If False,
                                    the minimum and maximum are at the outer-edges of the color map.
        :param contour_interval:    align color edges on this interval, which is useful for matching colors
                                    contour map, for example.  The color map will be reduced in size by thinning of 
                                    unneeded colors if necessary.
                                    
        .. versionadded:: 9.2
        """

        if inner_limits:
            if self.length < 3:
                raise GroupException(_t("Colour map must have length >= 3 for inner edge linear range."))
            delta = (maximum - minimum) / (self.length - 2)
            minimum -= delta
            maximum += delta

        self.gxitr.linear(minimum, maximum,
                          gxapi.rDUMMY if contour_interval is None else contour_interval)

    def set_logarithmic(self, minimum, maximum, contour_interval=None):
        """
        Set the color boundaries based on a logarithmic distribution between minimum and maximum.

        :param minimum:             minimum, must be > 0
        :param maximum:             maximum
        :param contour_interval:    align color edges on this interval, 10 for powers of 10.
                                    unneeded colors if necessary.

        .. versionadded:: 9.2
        """

        self.gxitr.log_linear(minimum, maximum,
                              gxapi.rDUMMY if contour_interval is None else contour_interval)


    def set_normal(self, standard_deviation, mean, expansion=1.0, contour_interval=None):
        """
        Set the color boundaries using a normal distribution around a mean.

        :param standard_deviation:  the standard deviation of the normal distribution.
        :param mean:                maximum
        :param contour_interval:    align color edges on this interval, 10 for powers of 10.
                                    unneeded colors if necessary.

        .. versionadded:: 9.2
        """
        self.gxitr.normal(standard_deviation,
                          mean,
                          expansion,
                          gxapi.rDUMMY if contour_interval is None else contour_interval)


    def color_of_value(self, value):
        """
        Return the gxg.Color of a value.  The mapping is determined with exclusive minima, inclusive maxima
        for each color level.  Values <= level [0] are assigned the [0] color, and values greater than the 
        the [n-2] level are assigned the [n-1] color.
        
        :param value:   data value
        :returns:       :class:`Color` instance
        
        .. versionadded:: 9.2
        """
        return Color(self.gxitr.color_value(value))

    def save_file(self, file_name=None):
        """
        Save to a Geosoft file, `.tbl`, `.itr` or `.zon`.  If the file_name does not have an
        extension and the color_map has not been initialized a `.tbl` file is created (colors only), 
        otherwise a `.itr` is created, which contains both zone boundaries and colors.

        :param file_name:   file name, if None a temporary file is created

        This is useful for gxapi methods that require a colour map to be loaded from a file. Say you
        cave a Color_map instance named `cmap` and you want to create a GXCSYMB instance, which
        requires a colur map file:

        .. code::

            cs = gxapi.GXCSYMB.create(cmap.save_file())

        .. versionadded:: 9.2
        """

        if file_name is None:
            file_name = gx.GXpy().temp_file()

        fn, ext = os.path.splitext(file_name)
        if not ext:
            if self.initialized:
                file_name = fn + '.itr'
            else:
                file_name = fn + '.tbl'
        self.gxitr.save_file(file_name)

        return file_name

def surface_group_from_file(view, surface_file, group_name=None, overwrite=False):
    """Add a surface"""

    if group_name is None:
        group_name = os.path.basename(surface_file)
        group_name = os.path.splitext(group_name)[0]

    if view.has_group(group_name) and not overwrite:
        raise GroupException(_t('Cannot overwerwrite existing group: {}').format(group_name))

    view.gxview.draw_surface_3d_from_file(group_name, surface_file)
