import os
import atexit
from math import ceil
from functools import wraps

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import utility as gxu
from . import dataframe as gxdf
from . import view as gxv
from . import geometry as gxgm

__version__ = geosoft.__version__

def _t(s):
    return s

class MapException(Exception):
    """
    Exceptions from this module.

    .. versionadded:: 9.2
    """
    pass

WRITE_NEW = 1
WRITE_OLD = 2

LIST_ALL = gxapi.MAP_LIST_MODE_ALL
LIST_3D = gxapi.MAP_LIST_MODE_3D
LIST_2D = gxapi.MAP_LIST_MODE_NOT3D

VIEW_NAME_SIZE = 2080

# 2D map reference points
REF_BOTTOM_LEFT = 0
REF_BOTTOM_CENTER = 1
REF_BOTTOM_RIGHT = 2
REF_CENTER_LEFT = 3
REF_CENTER = 4
REF_CENTER_RIGHT = 5
REF_TOP_LEFT = 6
REF_TOP_CENTER = 7
REF_TOP_RIGHT = 8

TEXT_BOTTOM_LEFT = -1
TEXT_BOTTOM_CENTER = 0
TEXT_BOTTOM_RIGHT = 1
TEXT_ALL_CENTER = 2
TEXT_BASE_LEFT= 3
TEXT_BASE_CENTER = 4
TEXT_BASE_RIGHT = 5
TEXT_BASE_ALL_CENTER = 6
TEXT_BASE_FIT_BY_CHARACTER_WIDTH = 7
TEXT_BASE_FIT_BY_CHARACTER_SIZE = 8

MAP_LANDSCAPE = 0
MAP_PORTRAIT = 1

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

COLOR_BAR_RIGHT = 0
COLOR_BAR_LEFT = 1
COLOR_BAR_BOTTOM = 2
COLOR_BAR_TOP = 3

COLOR_BAR_ANNOTATE_RIGHT = 1
COLOR_BAR_ANNOTATE_LEFT = -1
COLOR_BAR_ANNOTATE_TOP = 1
COLOR_BAR_ANNOTATE_BOTTOM = -1

class Line_def:
    def __init__(self,
                 line_colour='k',
                 fill_colour=None,
                 thickness=100):
        self._line_colour = line_colour
        self._fill_colour = fill_colour
        self._thickness = thickness

def map_file_name(filename):
    """
    Return a fully resolved map file path using the filename, with .map extyension

    :param filename:    file name, with ot without path and/or extension
    :return:            file name path with extension .map

    .. versionadded:: 9.2
    """
    ext = os.path.splitext(filename)[1].lower()
    if ext != '.map' and ext != '.geosoft_3dv':
        filename += '.map'
    return os.path.abspath(filename)

def delete_files(filename):
    """
    Delete all files associates with this map name.
    :param filename:

    .. versionadded:: 9.2
    """

    def remove(fn):
        try:
            os.remove(fn)
        except FileNotFoundError:
            pass

    filename = map_file_name(filename)
    remove(filename + '.xml')
    remove(os.path.splitext(filename)[0] + '.mdf')
    remove(filename)

def save_as_image(mapfile, imagefile, type="PNG", pix_width=1000, pix_height=0):
    """
    Save a map to an image file
    :param mapfile:     mapfile name
    :param imagefile:   name of the output raster file
    :param type:        one of type list below
    :param pix_width:   image pixel width, if 0 use pix_height only
    :param pix_height:  image pixel height, if 0 use pix_width only
    :return:

    .. versionadded:: 9.2
    """

    with GXmap.open(mapfile) as g:
        g.gxmap.export_all_raster(imagefile, '',
                                  pix_width, pix_height, gxapi.rDUMMY,
                                  gxapi.MAP_EXPORT_BITS_24,
                                  gxapi.MAP_EXPORT_METHOD_NONE,
                                  type, '')

def crc_map(mapfile, pix_width=1000):
    """
    Return the CRC of a map based on the output bitmap image.
    :param mapfile:     name of the map file
    :param pix_width:   image pixel width - use a higher resolution to test more detail
    :return:            CRC as an int

    .. versionadded:: 9.2
    """
    crc_image = os.path.join(gx.GXpy().temp_folder(), "__crc_image__.bmp")
    save_as_image(mapfile, crc_image, type='BMP', pix_width=pix_width)
    crc = gxu.crc32_file(crc_image)
    os.remove(crc_image)
    try:
        os.remove(crc_image + '.gi')
        os.remove(crc_image + '.xml')
    except FileNotFoundError:
        pass
    return crc

class GXmap:
    """
    Geosoft map files.

    A Geosoft map is a container for views.  A view has a defined coordinate system (2D or 3D) and
    contains graphical elements defined relative to the coordinate system of the view.  The
    ``geosoft.gxpy.view`` module provides classes and methods for working with individual 2D or
     3D views.

    Geosoft maps will always have a 2D 'base' view, which uses map cm as the coordinate system and is
    intended for drawing map annotations, such as titles, a scale bar, North arrow and legends.  The
    lower-left corner of the base view at location (0, 0) and the upper-right corner is defined by the
    media size and may be adjusted to fit the data view.

    Geosoft maps will also have one or more data views, each with it's own defined coordinate system
    and graphical content.  Creating a new map will create one data view, which will become the map's 
    ``current_data_view``, within which any spatial data drawn by Geosoft 2D drawing applications
    will be placed.  Maps may have more than one data view, including 3D data views, and the 
    ``current_data_view`` can be changed to any 2D or 3D view, and subsequent drawing will be placed
    in that view.

    3D views define a 3D spatial volume and accept both 2D and 3D drawing elements.  A 3D view will always
    contain a plane or surface on which 2D elements are drawn, and when a 3D view is the
    `default data view`, 2D elements will be drawn to the identified plane or surface.  When a 3D view is
    rendered on a map, which is a flat surface, the view is rendered from the last use point of view.  Geosoft
    map viewing applications allow a user to open a 3D view in a 3D viewer, which provides for 3D viewing,
    3D navigation and 3D drawing capabilities.

    Map constructors:

        ======== =============================
        `open()` open an existing map
        `new()`  create a new map
        ======== =============================

    .. versionadded:: 9.2
    """

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self._close()

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self._filename

    def __init__(self, filename, mode=WRITE_NEW, _internal=False):

        if not _internal:
            raise MapException(_t("GXmap must be created from GXmap.new(), or GXmap.open()."))

        self.gxmap = None
        self._remove = False
        self._filename = map_file_name(filename)
        self._annotation_outer_edge = 0.0
        self.gxmap = gxapi.GXMAP.create(self.filename, mode)

        atexit.register(self._close, pop=False)
        self._open = gx.track_resource(self.__class__.__name__, self._filename)

    def _close(self, pop=True):
        if self._open:
            if self.gxmap:

                if not self._remove:
                    pass
                    #self.gxmap.clean()

                self.gxmap = None

                if self._remove:
                    try:
                        delete_files(self._filename)
                    except OSError:  # remove if we can
                        pass
            if pop:
                gx.pop_resource(self._open)
            self._open = None

    @classmethod
    def open(cls, filename):
        """
        Open an existing map file.

        :param filename:    name of the map file

        .. versionadded:: 9.2
        """

        gmap = cls(filename, mode=WRITE_OLD, _internal=True)

        return gmap

    @classmethod
    def new(cls, filename=None, data_area=(0.,0.,100.,100.), scale=None,
            cs=None, media=None, layout=None, fixed_size=None, map_style='figure',
            margins=None, inside_margin=1.0, overwrite=False, no_data_view=False):

        """
        Create and open a new Geosoft map.

        :parameters:
            :filename:      Map file name.  If not specified a temporary file is created in the instance
                            temporary folder.  Use ``filename()`` to get the file name if needed.  The 
                            temporary map file will be unique and will exist through the life of the
                            Python GX instance, but will be deleted along with all temporary files
                            when the GX loses context.
            :data_area:     (min_x, min_y, max_x, max_y) data area for a 2D data view on the map
            :scale:         required scale, default will fit data to the map media
            :cs:            coordinate system, default is an unknown coordinate system.  You may pass
                            a ``coordinate_system.GXcs`` instance, a string descriptor, such as
                            `WGS 84 / UTM zone 15N`, or another valid constructor supported by
                            ``coordinate_system.GXcs``.
            :media:         media size as a tuple(x_cm, y_cm), or as a standard media name string.
                            If the media name contains 'portrait', the media is media aspect will be portrait.
                            Named media sizes are read from media.csv, which includes A4, A3, A2, A1, A0, 
                            letter, legal, ledger, A, B, C, D, E. For example `media='A4 portrait'`.
            :layout:        MAP_PORTRAIT or MAP_LANDSCAPE, overrides media setting.  If the layout is not 
                            defined by media or this parameter, the layout is determined by the aspect
                            ratio of the data area.
            :map_style:     'map' or 'figure' (default).  A 'map' style is intended for A3 or larger
                            media with a larger right or left margin for map annotations.  A 'figure'
                            style is intended for smaller media with a larger bottom margin for a
                            title and limited annotations.
            :fixed_size:    True for fixed media size, if, and only if, a media size is defined.
                            The default is True for 'figure' map_style, and False for 'map' map_style. 
                            If False, the base view boundary will be reduced to the data view plus margins.  
                            Tf True, the base view boundary is fixed to the media size and margins are 
                            adjusted to locate the data view proportionally relative to the requested margins.
            :margins:       (left, right, bottom, top) map margins in map cm.  The default for 'map'
                            style is (3, 14, 6, 3), and for figure (1, 4, 1, 1).
            :inside_margin: additional margin (cm) inside the base view.  This margin effectively
                            expands the data_area to allow room for graphical elements related to
                            spatial data near the edge of the defined data area.
            :overwrite:     True to overwrite an existing map.  If False and map exists, raises
                            ``MapException``.
            :no_data_view:  True to omit data view during map creation.

        .. versionadded:: 9.2
        """

        def data_window_on_map():
            mx = media[0] - m_left - m_right
            my = media[1] - m_bottom - m_top
            im = inside_margin * 2
            return mx - im, my - im  # data window on map cm

        def set_registry(gmap, style, inside_margin):
            rd = {'MAP.STYLE': style,
                  'MAP.MARGIN_INSIDE': str(inside_margin),
                  'MAP.UP_DIRECTION': 'right',
                  'MAP.UP_ANGLE': '67.5'}
            gmap.gxmap.set_reg(gxu.reg_from_dict(rd))

        
        if ((data_area[2] - data_area[0]) <= 0.0) or ((data_area[3] - data_area[1]) <= 0.0):
            raise MapException(_t('Invalid data area {}'.format(data_area)))

        if layout is None:
            if (data_area[2] - data_area[0]) < (data_area[3] - data_area[1]):
                layout = MAP_PORTRAIT
            else:
                layout = MAP_LANDSCAPE

        if filename is None:

            # get a new temporary map file name
            tempname = "temp_map"
            i = 0
            while True:
                filename = map_file_name(os.path.join(gx.GXpy().temp_folder(), tempname + str(i) + '.map'))
                if not os.path.isfile(filename):
                    break
                i += 1

        else:
            if not overwrite:
                filename = map_file_name(filename)
                if os.path.isfile(filename):
                    raise MapException(_t('Cannot overwrite existing file: "{}"').format(filename))

        gmap = cls(filename, WRITE_NEW, _internal=True)

        if type(media) is str:
            try:
                spec = gxdf.table_record('media', media.upper())
                media = (float(spec['SIZE_X']), float(spec['SIZE_Y']))
            except:
                media = None
                fixed_size = False

        if media is None:
            fixed_size = False
            if scale:
                media = (5000., 4000.)  # crazy large, will be trimmed to scale
                if margins is None:
                    if map_style == 'map':
                        margins = (1.5, 14.0, 5.0, 1.5)
                    else:
                        margins = (1.0, 1.0, 4.0, 1.0)
            else:
                media = (50., 40.)

        if (layout == MAP_PORTRAIT) and (media[0] > media[1]):
            media = (media[1], media[0])

        if margins:
            m_left, m_right, m_bottom, m_top = margins

        else:
            mx, my = media
            if map_style == 'map':
                if mx <= 30.0:
                    raise MapException('\'map\' style requires minimum 30cm media. Yours is {}cm'.format(mx))
                m_left = max(1.5, mx * 0.025)
                m_right = max(14.0, mx * 0.15)
                m_bottom = max(5.0, my * 0.1)
                m_top = max(1.5, my * 0.025)
            else:
                m_left = max(1.0, mx * 0.04)
                m_right = max(1.0, mx * 0.04)
                m_bottom = max(4.0, my * 0.15)
                m_top = max(1.0, my * 0.04)

        if scale is None:
            # determine largest scale to fit the media
            mx, my = data_window_on_map()
            sx = (data_area[2] - data_area[0]) * 100.0 / mx
            sy = (data_area[3] - data_area[1]) * 100.0 / my
            scale = max(sx, sy)

            # TODO - add a round_to_precision() function with option to round up or down.
            if scale > 100:
                scale = float(ceil(scale))

        if fixed_size is None:
            if map_style == 'figure':
                fixed_size = True
            else:
                fixed_size = False

        if fixed_size:
            mx, my = data_window_on_map()
            x_adjust = max(0., (mx - ((data_area[2] - data_area[0]) * 100.0 / scale)) * 0.5)
            y_adjust = max(0., (my - ((data_area[3] - data_area[1]) * 100.0 / scale)) * 0.5)
            m_left += x_adjust
            m_right += x_adjust
            m_bottom += y_adjust
            m_top += y_adjust

        # ensure the data fits on this media
        mx, my = data_window_on_map()
        dmx = (data_area[2] - data_area[0]) * 100.0 / scale
        dmy = (data_area[3] - data_area[1]) * 100.0 / scale
        if (mx - dmx) < -0.01 or (my - dmy) < -0.01:
            raise MapException(_t('The data does not fit media ({},{})cm at a scale of 1:{}')
                               .format(media[0], media[1], scale))

        gxapi.GXMVU.mapset(gmap.gxmap,
                           'base', 
                           '' if no_data_view else 'data',
                           data_area[0], data_area[2],
                           data_area[1], data_area[3],
                           '{},{}'.format(media[0] + 50.0, media[1] + 50.0), layout,
                           0, scale, gxapi.rDUMMY,
                           m_left, m_right, m_bottom, m_top,
                           float(inside_margin))

        with gxv.GXview(gmap=gmap, viewname='*data', mode=gxv.WRITE_OLD) as view:
            view.set_cs(cs)
        set_registry(gmap, map_style, inside_margin)

        return gmap

    @property
    def filename(self):
        """
        Full map file path name.
        """
        return self._filename

    @property
    def current_data_view(self):
        """ The current default data view which accepts drawing commands from Geosoft methods."""
        return self.get_class_view_name('data')

    @current_data_view.setter
    def current_data_view(self, s):
        if not self.has_view(s):
            raise MapException(_t('Map does not contain a view named "{}"').format(s))
        self.gxmap.set_class_name('data', s)

    @property
    def current_base_view(self):
        """ The current default base view which accepts drawing commands from Geosoft methods."""
        return self.get_class_view_name('base')

    @current_base_view.setter
    def current_base_view(self, s):
        if not self.has_view(s):
            raise MapException(_t('Map does not contain a view named "{}"').format(s))
        self.gxmap.set_class_name('base', s)

    @property
    def current_section_view(self):
        """ The current default base view which accepts drawing commands from Geosoft methods."""
        return self.get_class_view_name('section')

    @current_section_view.setter
    def current_section_view(self, s):
        if not self.has_view(s):
            raise MapException(_t('Map does not contain a view named "{}"').format(s))
        self.gxmap.set_class_name('section', s)

    def close(self):
        """ Close the map and release resources. """
        self._close()

    def remove_on_close(self, remove=True):
        """
        :param remove:  if True (the default), remove the map file when finished.
        """
        self._remove = remove

    def commit_changes(self):
        """Commit changes to the map."""
        self.gxmap.commit()

    def classview(self, name):
        """
        Given a view name that may be a class name ('*' prefix), return the view name for that class.  if not
        class decorated, the name passed is returned. 
        that 
        :param name:    view name: '*data' will return the name associated with the 'data' class, while
                        'my_view' will return 'my_view'.
        
        :return:        the name, or if a class name, the view name associated with that class.
        
        .. versionadded: 9.2
        """
        if name[0] != '*':
            return name
        return self.get_class_view_name(name[1:])


    def _views(self, view_type=LIST_ALL):
        """
        Return dictionary of view names.
        :param view_type: `gxmap.LIST_ALL`, `gxapi.LIST_2D` or `gxapi.LIST_3D`
        :return: list of views
        """
        glst = gxapi.GXLST.create(VIEW_NAME_SIZE)
        self.gxmap.view_list_ex(glst, view_type)
        return list(gxu.dict_from_lst(glst))

    @property
    def view_list(self):
        return self._views()

    @property
    def view_list_2D(self):
        return self._views(LIST_2D)

    @property
    def view_list_3D(self):
        return self._views(LIST_3D)

    def aggregate_list(self, mode=0):
        glst = gxapi.GXLST.create(gxv.GROUP_NAME_SIZE)
        self.gxmap.agg_list_ex(glst, mode, 0)
        return list(gxu.dict_from_lst(glst))

    def has_view(self, view):
        """ Returns True if the map contains this view."""
        return self.gxmap.exist_view(self.classview(view))

    def copy_view(self, old, new, overwrite=False, copy_all=True):
        """
        Copy an existing view into a new view.
        
        :param old:         name of the existing view
        :param new:         name for the new view
        :param overwrite:   True to overwrite an existing view if it exists
        :param copy_all:    True to copy content of old to new, false to create an empty new view
                            with the same coordinate system, scale and clipping as the old view.
        """

        old = self.classview(old)
        new = self.classview(new)

        if not self.has_view(old):
            raise MapException(_t('"{}" view does not exist.').format(old))
        if self.has_view(new):
            if overwrite:
                self.gxmap.delete_view(new)
            else:
                raise MapException(_t('Cannot overwtite existing view "{}"').format(new))

        s = gxapi.str_ref()
        s.value = new

        self.gxmap.duplicate_view(old, s, copy_all)

        if s.value != new:
            self.gxmap.delete_view(new)
            raise MapException(_t('Invalud view name "{}", suggest "{}"').format(new, s.value ))

    def delete_view(self, viewname):
        """
        Delete a view from a map. You cannot delete the last view in a mep.
        
        :param viewname: name of the view to delete
        
        .. versionadded:: 9.2
        """
        self.gxmap.delete_view(self.classview(viewname))

    def mdf(self):
        """
        Returns the Map Description File specification for maps that contain
        both a base view and a data view.

        ((x_size, y_size, margin_bottom, margin_right, margin_top, margin_left),
         (scale, units_per_metre, x_origin, y_origin))\

        .. versionadded: 9.2
        """

        views = self.view_list_2D

        if not(self.has_view(self.current_data_view) and self.has_view(self.current_base_view)):
            raise MapException('The map must have both a base view and a data view.')

        xmn = gxapi.float_ref()
        ymn = gxapi.float_ref()
        xmx = gxapi.float_ref()
        ymx = gxapi.float_ref()

        with gxv.GXview(self, self.current_base_view, gxv.READ_ONLY) as v:
            v.gxview.extent(gxapi.MVIEW_EXTENT_CLIP, gxapi.MVIEW_EXTENT_UNIT_MM,
                            xmn, ymn, xmx, ymx)
            mapx = (xmx.value - xmn.value) * 0.1
            mapy = (ymx.value - ymn.value) * 0.1

        with gxv.GXview(self, self.current_data_view, gxv.READ_ONLY) as v:
            v.gxview.extent(gxapi.MVIEW_EXTENT_CLIP, gxapi.MVIEW_EXTENT_UNIT_MM,
                            xmn, ymn, xmx, ymx)
            view_map = (xmn.value * 0.1,
                        ymn.value * 0.1,
                        xmx.value * 0.1,
                        ymx.value * 0.1)

            v.gxview.extent(gxapi.MVIEW_EXTENT_CLIP, gxapi.MVIEW_EXTENT_UNIT_VIEW,
                            xmn, ymn, xmx, ymx)
            view_view = (xmn.value, ymn.value, xmx.value, ymx.value)

        m1 = (mapx, mapy, view_map[1], mapx - view_map[2], mapy - view_map[3], view_map[0])
        sc = (view_view[2] - view_view[0]) / ((view_map[2] - view_map[0]) / 100.0)
        ufac = 1.0
        x0 = view_view[0]
        y0 = view_view[1]
        m2 = (sc, ufac, x0, y0)

        return m1, m2

    def get_class_view_name(self, view_class):
        """
        Get the view name associated with a class.

        :param view_class:  desired class

        Common view class names are::

            'Base'      the base map/figure view, uses map cm
            'Data'      the default data view for drawing spatial data.
            'Section'   the default section view for things drawn in section

        Other class names may be defined, though they are not used by Geosoft.

        :return: view name associated with the class, '' if not defined.

        .. versionadded:: 9.2
        """
        sr = gxapi.str_ref()
        self.gxmap.get_class_name(view_class, sr)
        return sr.value.lower()

    def set_class_view_name(self, view_class, view_name):
        """
        Set the view name associated with a class.

        :param view_class:  class name
        :param view_name:   name of the view associated with this class.

        Common view class names are::

            'Base'      the base map/figure view, uses map cm
            'Data'      the default data view for drawing spatial data.
            'Section'   the default section view for things drawn in section

        .. versionadded:: 9.2
        """
        self.gxmap.set_class_name(view_class, view_name)

    def create_linked_3d_view(self, view, view_name = '3D', area=(0,0,30,30)):
        """
        Create a linked 3D view inside a 2D map to a `gxpy.view.GXview3d` in a 3DV

        :param view: A `gxpy.view.GXview3d` instance
        :param view_name:   name of the linked view to create
        :param area: (min_x, min_y, max_x, max_y) placement of view on map in mm

        .. versionadded:: 9.2
        """
        self.gxmap.create_linked_3d_view(view.gxview, view_name, area[0], area[1], area[2], area[3])

    def map_reference_location(self, refp, viewname='base'):
        """
        Return the location of a reference point relative to the current clipping window
        extent of a view on the map.
        
        :param refp: One of:
        
            ::
            
                REF_BOTTOM_LEFT
                REF_BOTTOM_CENTER
                REF_BOTTOM_RIGHT
                REF_CENTER_LEFT
                REF_CENTER
                REF_CENTER_RIGHT
                REF_TOP_LEFT
                REF_TOP_CENTER
                REF_TOP_RIGHT
                
        :param viewname:    the name of the view, default is the base view which returns the
                            extent in map cm.

        :return:    (x, y) in view units
        
        .. versionadded:: 9.2
        """

        viewname = self.classview(viewname)

        if not viewname:
            with gxv.GXview(self, self.current_base_view) as v:
                extent = v.extent_map_cm(v.extent_clip)
        else:
            with gxv.GXview(self, viewname) as v:
                extent = v.extent_clip

        xc = extent[0] + (extent[2] - extent[0]) * 0.5
        yc = extent[1] + (extent[3] - extent[1]) * 0.5
        rpoints = ((extent[0], extent[1]),
                   (xc, extent[1]),
                   (extent[2], extent[1]),
                   (extent[0], yc),
                   (xc, yc),
                   (extent[2], yc),
                   (extent[0], extent[3]),
                   (xc, extent[3]),
                   (extent[2], extent[3]))

        return rpoints[refp]

    def surround(self, outer_pen=None, inner_pen=None, gap=0):
        """
        Draw a map surround.  This will draw a single or a double neat-line around the base view of the
        map.
        
        :param outer_pen:   outer-line pen attributes
        :param inner_pen:   inner-line pen attributes
        :param gap:         gap between the outer and inner line in cm.  If 0, only the outer line is drawn.
         
        .. versionadded:: 9.2
        """

        if outer_pen is None:
            outer_pen = gxv.Pen(line_thick=0.0500)

        with _Mapplot(self) as mpl:

            mpl.start_group('surround', view=VIEW_BASE, mode=GROUP_APPEND)
            mpl.define_named_attribute('outer', pen=outer_pen)
            if gap <= 0:
                inner = ''
                gap = ''
            else:
                if inner_pen is None:
                    inner_pen = gxv.Pen(line_thick=0.01)
                inner = 'inner'
                mpl.define_named_attribute(inner, pen=inner_pen)

            mpl.command('SURR "{}",{},"{}"'.format('outer', gap, inner))

    def north_arrow(self,
                    location=(1, 2., 2.7),
                    direction=None,
                    length=3,
                    inclination=None,
                    declination=None,
                    text_def=None,
                    pen=None):
        """
        Add a North arrow to the base view of the map.

        :param location:    (reference, x_offset, y_offset) reference is a reference point relative to the
                            base map extents (1 through 9) nd the offsets are the offset from that reference
                            point in cm.
        :param direction:   North direction in degrees azimuth (clockwise from map Y axis).  The efault is 
                            calculated direction of North at the center of the data view.
        :param length:      arrow length in cm
        :param inclination: magnetic inclination, not shown if not specified
        :param declination: magnetic declination, not shown if not specified
        :param text_def:    ``gxpy.view.Text_def`` instance, or ``None`` for the default.
        :param pen:         ``gxpy.view.Pen`` instance, or ``None`` for the default

        .. versionadded:: 9.2
        """

        #TODO add IGRF calculation from a date, igrfdate=

        if direction is None:
            with gxv.GXview(self, '*data', mode=gxv.WRITE_OLD) as v:
                direction = round(v.gxview.north(), 1)
                if direction == gxapi.rDUMMY:
                    direction = ''

        if inclination is None:
            inclination = ''

        if declination is None:
            declination = ''

        if pen is None:
            pen = gxv.Pen(line_thick=0.015)

        if text_def is None:
            text_def = gxv.Text_def(height=0.25, italics=True, weight=gxv.FONT_WEIGHT_LIGHT)

        with _Mapplot(self) as mpl:
            mpl.start_group('north_arrow', view=VIEW_BASE, mode=GROUP_APPEND)
            mpl.define_named_attribute('arrow', pen=pen)
            mpl.define_named_attribute('annot', text_def=text_def)
            mpl.command("NARR {},{},{},{},{},{},{},{}".format(location[0], location[1], location[2],
                                                              direction,
                                                              length,
                                                              'arrow',
                                                              inclination,
                                                              declination))
            mpl.command('     annot')

    def scale_bar(self,
                  location=(1, 5, 2),
                  length=5,
                  sections=None,
                  post_scale=False,
                  text=None,
                  pen=None):
        """

        :param length:      maximum scale bar length, default is 5 cm. scale=0.0 will suppress drawing of the bar.
        :param sections:    number of major sections in the bar, default is determined automatically.
        :param post_scale:  True to post the actual scale as a string, e.g. '1:50,000'.  Note that a posted
                            scale is only relevant for printed maps.  The default does not post the scale.
        :param text:        ``gxpy.view.Text_def`` instance.
        :param pen:         ``gxpy.view.Pen`` instance.


        .. versionadded:: 9.2
        """

        if sections is None:
            sections = ''

        if post_scale:
            option = 2
        else:
            option = 1

        if text is None:
            text = gxv.Text_def(height=0.25, italics=True)

        if pen is None:
            pen = gxv.Pen(line_thick=0.050)

        with _Mapplot(self) as mpl:
            mpl.start_group('scale_bar', view=VIEW_BASE, mode=GROUP_APPEND)
            att = 'scale_bar'
            mpl.define_named_attribute(att, pen=pen, text_def=text)
            mpl.command("SCAL {},{},{},,,{},{},,{},".format(location[0], location[1], location[2],
                                                            length, sections, option))
            mpl.command('     {}'.format(att))

    def _annotation_offset(self, offset, text_height):
        inside = text_height * 0.25
        if offset:
            offset = offset + inside
        else:
            offset = self._annotation_outer_edge + inside
        self._annotation_outer_edge += offset + text_height + inside * 0.5
        return offset

    def annotate_data_xy(self, viewname='*data',
                         tick='', offset='',
                         x_sep='', x_dec='',
                         y_sep='', y_dec='',
                         compass=True,
                         top=TOP_OUT,
                         text_def=None,
                         edge_pen=None,
                         grid=GRID_NONE,
                         grid_pen=None):
        """
        Annotate a data view axis

        :param viewname:    name of the data view to annotate
        :param tick:        inner tick size in cm
        :param offset:      posting offset from the edge in cm. The posting edge is adjusted to be outside
                            character height for a subsequent call to an edge annotation.  This allows one to
                            annotate both geographic and projected coordinates.
        :param top:         TOP_IN or TOP_OUT (default) for vertical annotations
        :param x_sep:       separation between X annotations, default is calculated from data
        :param x_dec:       X axis label decimals, default is 0
        :param y_sep:       separation between Y annotations, default is calculated from data
        :param y_dec:       Y axis label decimals, default is 0
        :param compass:     True (default) to append compass direction to annotations
        :param grid:        Plot grid lines:

                            ::
   
                                GRID_NONE       no grid
                                GRID_DOTTED     dotted lines
                                GRID_CROSSES    crosses at intersections
                                GRID_LINES      lines
       
        :param text_def:    ``gxv.Text_def``
        :param edge_pen:    ``gxv.Pen``
        :param grid_pen:    ``gxv.Pen``        

        .. versionadded:: 9.2
        """

        if text_def is None:
            text_def = gxv.Text_def(height=0.18)
        if edge_pen is None:
            edge_pen = gxv.Pen()
        if grid_pen is None:
            grid_pen = edge_pen

        current_view = self.current_data_view
        viewname = self.classview(viewname)
        self.current_data_view = viewname

        offset = self._annotation_offset(offset, text_def.height)

        with gxv.GXview(self, viewname) as v:
            v.xy_rectangle(v.extent_clip, pen=gxv.Pen(default=edge_pen, factor=v.units_per_map_cm))

        try:

            with _Mapplot(self) as mpl:

                mpl.start_group(viewname + '_edge', 1, viewname)

                if not tick and grid == GRID_LINES:
                    tick = 0.0

                mpl.define_named_attribute('annot', text_def=text_def,
                                           pen=gxv.Pen(line_color=text_def.color, line_thick=text_def.line_thick))
                mpl.define_named_attribute(pen=edge_pen)

                mpl.command("ANOX ,,,,,{},{},,{},,,,{},{},1".format(x_sep, tick, 0 if compass else -1, offset, x_dec))
                mpl.command('     annot')
                mpl.command("ANOY ,,,,,{},{},,{},{},,,{},{},1".format(y_sep, tick, 0 if compass else -1, top, offset, y_dec))
                mpl.command('     annot')

                if grid:
                    mpl.define_named_attribute(pen=grid_pen)
                    mpl.command("GRID {},,,,,_".format(grid))

        except:
            raise

        finally:
            self.current_data_view = current_view

    def annotate_data_ll(self, viewname='*data',
                         tick='',
                         offset='',
                         sep='',
                         top=TOP_OUT,
                         text_def=None,
                         edge_pen=None,
                         grid=GRID_LINES,
                         grid_pen=None):

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

        if text_def is None:
            text_def = gxv.Text_def(height=0.18)
        if edge_pen is None:
            edge_pen = gxv.Pen()
        if grid_pen is None:
            grid_pen = edge_pen

        current_view = self.current_data_view
        viewname = self.classview(viewname)
        self.current_data_view = viewname

        offset = self._annotation_offset(offset, text_def.height)

        with gxv.GXview(self, viewname) as v:
            v.xy_rectangle(v.extent_clip, pen=gxv.Pen(default=edge_pen, factor=v.units_per_map_cm))

        try:

            with _Mapplot(self) as mpl:

                mpl.start_group(viewname + '_edge', 1, viewname)
                if not tick and grid == GRID_LINES:
                    tick = 0.0

                mpl.define_named_attribute('annot', text_def=text_def,
                                           pen=gxv.Pen(line_color=text_def.color, line_thick=text_def.line_thick))
                mpl.define_named_attribute(pen=edge_pen)

                mpl.command("ALON {},{},{},,1".format(sep, tick, offset))
                mpl.command('    annot')
                mpl.command("ALAT {},{},{},,,{}".format(sep, tick, offset, top))
                mpl.command('    annot')

                if grid:
                    mpl.define_named_attribute(pen=grid_pen)
                    mpl.command("GRID -{},,,,,_".format(grid))

        except:
            raise

        finally:
            self.current_data_view = current_view

    def color_bar(self):
        pass

    def agg_legend(self,
                   view_name='*data',
                   agg_name=None,
                   bar_location = COLOR_BAR_RIGHT,
                   location=None,
                   decimals = 1,
                   annotation_height = 0.2,
                   annotation_offset = None,
                   annotation_side = COLOR_BAR_ANNOTATE_RIGHT,
                   box_size = None,
                   bar_width = None,
                   max_bar_size = None,
                   minimum_gap = 0,
                   post_end_values = False,
                   annotate_vertical = False,
                   division_line = 1,
                   interval_1 = None,
                   interval_2 = None,
                   title=''):
        """
        Draw an aggregate legend.
        
        :param view_name:           view name, default is '*data'
        :param agg_name:            aggregate name, default is the first aggregate found
        :param bar_location:        one of:
        
            ::
            
                COLOR_BAR_RIGHT = 0
                COLOR_BAR_LEFT = 1
                COLOR_BAR_BOTTOM = 2
                COLOR_BAR_TOP = 3
                
        :param location:            offset or (x, y) offset from view reference point, in cm.
        :param decimals:            annotation decimal places
        :param annotation_height:   annotation number height
        :param annotation_offset:   offset of annotations from the bar (cm)
        :param annotation_side:     side of the bar for annotations
        
            ::
            
                COLOR_BAR_ANNOTATE_RIGHT = 1
                COLOR_BAR_ANNOTATE_LEFT = -1
                COLOR_BAR_ANNOTATE_TOP = 1
                COLOR_BAR_ANNOTATE_BOTTOM = -1

        :param box_size:            box size, height for vertical bars, width for horizontal bars
        :param bar_width:           width of the colour boxes
        :param max_bar_size:        maximum bar size, default is the size of the view edge
        :param minimum_gap:         minimum gap to between annotations.  Annotations are dropped in necessary.
        :param post_end_values:     post the maximum and minimum values
        :param annotate_vertical:   True to orient labels vertically 
        :param division_line:       0, no division lines, 1 - line, 2 - tick
        :param interval_1:          annotation increment, default annotates everything
        :param interval_2:          secondary smaller annotations, 1/10, 1/ 5, 1/4 or 1/2 interval_1
        :param title:               bar title, use new-lines for sub-titles.
        
        .. versionadded:: 9.2
        """

        def layers_in_agg(view, agg_name):
            layers = []
            for val in self.aggregate_list(1):
                if val[:val.index('\\')] == view:
                    al = val[val.index('\\') + 1:]
                    if agg_name is None:
                        agg_name = al[:al.index('\\')]
                    if al[:al.index('\\')] == agg_name:
                        layers.append(val)

            layers.sort()
            return layers, agg_name

        def center_w_h(rect):
            w = v_extent[2] - v_extent[0]
            h = v_extent[3] - v_extent[1]
            c = (v_extent[0] +  w * 0.5, v_extent[1] + h * 0.5)
            return c, w, h

        view_name = self.classview(view_name)
        layers, agg_name = layers_in_agg(view_name, agg_name)
        if not layers:
            return

        itr1 = gxapi.GXITR.create_map(self.gxmap, layers[0])
        if len(layers) >= 2:
            itr2 = gxapi.GXITR.create_map(self.gxmap, layers[1])
        else:
            itr2 = gxapi.GXITR.null()


        with gxv.GXview(self, view_name) as v:

            v_extent = v.extent_clip
            center, v_width, v_height = center_w_h(v_extent)

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
            def_size = default_bar_size / itr1.get_size()
            if box_size is None:
                box_size = max(0.4 * v.units_per_map_cm, def_size)
            else:
                box_size *= v.units_per_map_cm
            if bar_width is None:
                if bar_location in (COLOR_BAR_LEFT, COLOR_BAR_RIGHT):
                    bar_width = max(0.4 * v.units_per_map_cm, box_size * 2.0)
                else:
                    bar_width = max(0.4 * v.units_per_map_cm, box_size)
            else:
                bar_width *= v.units_per_map_cm
            if max_bar_size is not None:
                box_size = min(box_size, (max_bar_size * v.units_per_map_cm) / itr1.get_size())

            annotation_height *= v.units_per_map_cm
            if annotation_offset is None:
                annotation_offset = annotation_height * 0.5
            else:
                annotation_offset *= v.units_per_map_cm
            annotation_offset *= annotation_side
            minimum_gap *= v.units_per_map_cm

            cdict = {
                "BAR_ORIENTATION": bar_orient,
                "DECIMALS": decimals,
                'ANNOFF': annotation_offset,
                'BOX_SIZE': box_size,
                'BAR_WIDTH': bar_width,
                'MINIMUM_GAP': minimum_gap,
                "X": center[0],
                "Y": center[1],
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

            gname = 'COLORBAR_' + agg_name
            v.start_group(gname)
            v.text_def = gxv.Text_def(height=annotation_height)
            gxapi.GXMVU.color_bar_reg(v.gxview, itr1, itr2, gxu.reg_from_dict(cdict, 100, json_encode=False))

            if title:

                title_height = annotation_height * 1.5
                v.text_def = gxv.Text_def(height=title_height, weight=gxv.FONT_WEIGHT_BOLD)
                p = gxgm.Point(v.reference_point(gxv.REF_BOTTOM_CENTER, v.extent_group(gname)))
                p -= (0, title_height * 0.5)
                try:
                    tline = title[:title.index('\n')]
                    title = title[title.index('\n')+1:]
                except:
                    tline = title
                    title = ''
                v.text(tline, p, reference=gxv.REF_TOP_CENTER)

                if title:
                    v.text_def = gxv.Text_def(height=title_height * 0.8, weight=gxv.FONT_WEIGHT_LIGHT)
                    p -= (0, title_height * 1.5)
                    v.text(title, p, reference=gxv.REF_TOP_CENTER)

            # locate the bar
            default_offset = 1.5 * v.units_per_map_cm
            if location and (not hasattr(location, '__iter__')):
                default_offset = location * v.units_per_map_cm
                location = None
            if location is not None:
                location = location[0] * v.units_per_map_cm, location[1]*v.units_per_map_cm

            if bar_location == COLOR_BAR_RIGHT:
                if location is None:
                    location = (default_offset, 0)
                xy = v.reference_point(REF_CENTER_RIGHT)
                ref = gxv.REF_CENTER_LEFT
            elif bar_location == COLOR_BAR_LEFT:
                if location is None:
                    location = (-default_offset, 0)
                xy = v.reference_point(REF_CENTER_LEFT)
                ref = gxv.REF_CENTER_RIGHT
            elif bar_location == COLOR_BAR_BOTTOM:
                if location is None:
                    location = (0, -default_offset)
                xy = v.reference_point(REF_BOTTOM_CENTER)
                ref = gxv.REF_TOP_CENTER
            elif bar_location == COLOR_BAR_TOP:
                if location is None:
                    location = (0, default_offset)
                xy = v.reference_point(REF_TOP_CENTER)
                ref = gxv.REF_BOTTOM_CENTER

            location = xy[0] + location[0], xy[1] + location[1]
            v.locate_group(gname, location, ref)


class _Mapplot:

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self._process()

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "mapplot({})".format(self._map.filename)

    def __init__(self, map, data_view=None, ref_prefix='', **kwargs):

        if not (map.has_view(map.current_base_view) and map.has_view(map.current_data_view)):
            raise MapException("Map must have a '*Base' and '*Data' view.")

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
        self._annotation_outer_edge = 0.0

        atexit.register(self._process, pop=False)
        self._open = gx.track_resource(self.__class__.__name__, self._maplfilename)

        self.define_named_attribute()

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

    def command(self, command):
        self._maplfile.write(command)
        if command and command[-1] != '\n':
            self._maplfile.write('\n')
        # geosoft.gxpy.gx.GXpy().log(command)

    def define_named_attribute(self, name='_', pen=None, text_def=None):

        if (pen is None) and (text_def is None):
            self.command("DATT {}".format(name))

        else:
            if pen is None:
                pen = gxv.Pen(line_color=text_def.color, line_thick=text_def.line_thick)
            ls = pen.line_style
            lp = pen.line_pitch
            pen = pen.mapplot_string

            if text_def is None:
                text = ''
            else:
                text = text_def.mapplot_string

            self.command("DATT {}={},{},{},{}".format(name, pen, ls, lp, text))

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
        if type(view) is str:
            if view.lower() == 'base':
                view = VIEW_BASE
            else:
                view = VIEW_DATA
        self.command('MGRP {},{},{}'.format(name, mode, view))
