"""
Geosoft maps contain one or more 2D and 3D views.

:Classes:

    ============ ============
    :class:`Map` map class
    ============ ============


Each 2D view has a specific coordinate system and clip region.
Each 3D view is a link to a separate `geosoft_3dv` file, which can be placed in the map 
as a 2D perspective of the last viewing state of the 3D view.

.. seealso:: :mod:`geosoft.gxpy.view`, :mod:`geosoft.gxpy.group`
 
    :mod:`geosoft.gxapi.GXMAP`, :mod:`geosoft.gxapi.GXMVIEW`, :mod:`geosoft.gxapi.GXMVU`

.. note::

    Regression tests provide usage examples:     
    `map tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_map.py>`_
    
"""
import os
from math import ceil

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import utility as gxu
from . import dataframe as gxdf
from . import group as gxg
from . import view as gxv

__version__ = geosoft.__version__


def _t(s):
    return s


class MapException(Exception):
    """
    Exceptions from :mod:`geosoft.gxpy.map`.

    .. versionadded:: 9.2
    """
    pass


WRITE_NEW = 1 #:
WRITE_OLD = 2 #:

LIST_ALL = gxapi.MAP_LIST_MODE_ALL #:
LIST_3D = gxapi.MAP_LIST_MODE_3D #:
LIST_2D = gxapi.MAP_LIST_MODE_NOT3D #:

VIEW_NAME_SIZE = 2080 #:

TEXT_BOTTOM_LEFT = -1 #:
TEXT_BOTTOM_CENTER = 0 #:
TEXT_BOTTOM_RIGHT = 1 #:
TEXT_ALL_CENTER = 2 #:
TEXT_BASE_LEFT = 3 #:
TEXT_BASE_CENTER = 4 #:
TEXT_BASE_RIGHT = 5 #:
TEXT_BASE_ALL_CENTER = 6 #:
TEXT_BASE_FIT_BY_CHARACTER_WIDTH = 7 #:
TEXT_BASE_FIT_BY_CHARACTER_SIZE = 8 #:

MAP_LANDSCAPE = 0 #:
MAP_PORTRAIT = 1 #:

TOP_IN = 1 #:
TOP_OUT = -1 #:

GRID_NONE = 0 #:
GRID_DOTTED = 1 #:
GRID_CROSSES = 2 #:
GRID_LINES = 3 #:

GROUP_NEW = 0 #:
GROUP_APPEND = 1 #:

VIEW_BASE = 0 #:
VIEW_DATA = 1 #:

STYLE_FIGURE = 0 #:
STYLE_MAP = 1 #:


def map_file_name(file_name, file_type='map'):
    """
    Return a fully resolved map file path using the file name, with .map extension

    :param file_name:   file name, with ot without path and/or extension
    :param file_type:   Geosoft file type, 'map' or 'geosoft_3dv' expected.  Default is 'map'    
    :returns:           file name path with extension .map

    .. versionadded:: 9.2
    """

    ext = os.path.splitext(file_name)[1].lower()
    if ext not in ('.map', '.geosoft_3dv'):
        if file_type[0] != '.':
            file_name = file_name + '.' + file_type
        else:
            file_name += file_type
    return os.path.abspath(file_name)


def unique_temporary_file_name(temproot, file_type='map'):
    """
    Create a unique temporary file name.
    
    :param temproot:    root base name
    :param file_type:   Geosoft file type, 'map' or 'geosoft_3dv' expected.  Default is 'map'
    
    .. versionadded:: 9.2
    """

    root, ext = os.path.splitext(temproot)
    if not ext:
        if file_type[0] == '.':
            ext = file_type
        else:
            ext = '.' + file_type

    i = 0
    while True:
        file_name = map_file_name(os.path.join(gx.gx.temp_folder(), root + str(i) + ext))
        if not os.path.isfile(file_name):
            return file_name
        i += 1


def delete_files(file_name):
    """
    Delete all files associates with this map name.
    :param file_name:

    .. versionadded:: 9.2
    """

    def remove(fn):
        try:
            os.remove(fn)
        except FileNotFoundError:
            pass

    file_name = map_file_name(file_name)
    remove(file_name + '.xml')
    remove(os.path.splitext(file_name)[0] + '.mdf')
    remove(file_name)


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

    with Map.open(mapfile) as g:
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
    :returns:           CRC as an int

    .. versionadded:: 9.2
    """
    crc_image = os.path.join(gx.gx.temp_folder(), "__crc_image__.bmp")
    save_as_image(mapfile, crc_image, type='BMP', pix_width=pix_width)
    crc = gxu.crc32_file(crc_image)
    os.remove(crc_image)
    try:
        os.remove(crc_image + '.gi')
        os.remove(crc_image + '.xml')
    except FileNotFoundError:
        pass
    return crc


class Map:
    """
    Geosoft map files.

    A Geosoft map is a container for views.  A view has a defined coordinate system (2D or 3D) and
    contains graphical elements defined relative to the coordinate system of the view.  The
    ``geosoft.gxpy.view`` module provides classes and methods for working with individual 2D or
    3D views.

    Geosoft maps will always have a 2D 'base' view, which uses map cm as the coordinate system and is
    intended for drawing map annotations, such as titles, a scale bar, North arrow and legends.  The
    lower-left corner of the base view ia at location (0, 0) and the upper-right corner is defined by the
    media size and may be adjusted to fit the data view.

    Geosoft maps will also have one or more data views, each with it's own defined coordinate system
    and graphical content.  Creating a new map will create one data view, which will become the map's 
    `current_data_view`, within which any spatial data drawn by Geosoft 2D drawing applications
    will be placed.  Maps may have more than one data view, including 3D data views, and the 
    `current_data_view` can be changed to any 2D or 3D view, and subsequent drawing will be placed
    in that view.

    3D views define a 3D spatial volume and accept both 2D and 3D drawing elements.  A 3D view will always
    contain a plane or surface on which 2D elements are drawn, and when a 3D view is the
    `default data view`, 2D elements will be drawn to the identified plane or surface.  When a 3D view is
    rendered on a map, which is a flat surface, the view is rendered from the last use point of view.  Geosoft
    map viewing applications allow a user to open a 3D view in a 3D viewer, which provides for 3D viewing,
    3D navigation and 3D drawing capabilities.

    :Constructors:

        ============ ========================================
        :meth:`open` open an existing map
        :meth:`new`  create a new map
        ============ ========================================

    .. versionadded:: 9.2
    """

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self._close()

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self._file_name

    def __init__(self, file_name, mode=WRITE_NEW, _internal=False):

        if not _internal:
            raise MapException(_t("Map must be created from Map.new(), or Map.open()."))

        self.gxmap = None
        self._remove = False
        self._file_name = map_file_name(file_name)
        self._name = os.path.splitext(os.path.split(self._file_name)[1])[0]
        self._annotation_outer_edge = 0.0
        self.gxmap = gxapi.GXMAP.create(self.file_name, mode)
        self._metadata = None
        self._metadata_changed = False
        self._metadata_root = ''

        self._open = gx.track_resource(self.__class__.__name__, self._file_name)

    def _close(self, pop=True):
        if self._open:
            if self.gxmap:

                self.gxmap = None

                if self._metadata_changed:
                    with open(self._file_name + '.xml', 'w+') as f:
                        f.write(gxu.xml_from_dict(self._metadata))
                    gxapi.GXMAP.sync(self._file_name)

                if self._remove:
                    try:
                        delete_files(self._file_name)
                    except OSError:  # remove if we can
                        pass
            if pop:
                gx.pop_resource(self._open)
            self._open = None

    @classmethod
    def open(cls, file_name):
        """
        Open an existing map file.

        :param file_name:    name of the map file

        .. versionadded:: 9.2
        """

        map = cls(file_name, mode=WRITE_OLD, _internal=True)

        return map

    @classmethod
    def new(cls, 
            file_name=None, 
            data_area=(0., 0., 100., 100.), 
            scale=None,
            coordinate_system=None,
            media=None, 
            layout=None, 
            fixed_size=False, 
            map_style=None,
            margins=None, inside_margin=1.0, overwrite=False, no_data_view=False):

        """
        Create and open a new Geosoft map.

        :parameters:
            :file_name:         Map file name.  If not specified a temporary file is created in the instance
                                temporary folder.  Use ``file_name()`` to get the file name if needed.  The 
                                temporary map file will be unique and will exist through the life of the
                                Python GX instance, but will be deleted along with all temporary files
                                when the GX loses context.
            :data_area:         (min_x, min_y, max_x, max_y) data area for a 2D data view on the map
            :scale:             required scale, default will fit data to the map media
            :coordinate_system: coordinate system, default is an unknown coordinate system.  You may pass
                                a :class:`geosoft.gxpy.coordinate_system.Coordinate_system` instance, a string 
                                descriptor, such as '`WGS 84 / UTM zone 15N`', or another valid constructor supported
                                by :class:`geosoft.gxpy.coordinate_system.Coordinate_system`.
            :media:             media size as a tuple (x_cm, y_cm), or as a standard media name string.
                                If the media string contains 'portrait', the media aspect will be portrait.
                                Named media sizes are read from media.csv, which includes A4, A3, A2, A1, A0, 
                                letter, legal, ledger, A, B, C, D, E. For example `media='A4 portrait'`.
            :layout:            MAP_PORTRAIT or MAP_LANDSCAPE, overrides media setting.  If the layout is not 
                                defined by media or this parameter, the layout is determined by the aspect
                                ratio of the data area.
            :map_style:         STYLE_FIGURE or STYLE_MAP (default).  A MAP style is intended for A3 or larger
                                media with a larger right or left margin for map annotations.  A FIGURE
                                style is intended for smaller media with a larger bottom margin for a
                                title and limited annotations.
            :fixed_size:        True for fixed media size, if, and only if, a media size is defined.
                                If False, the base view boundary will be reduced to the data view plus margins.  
                                If True, the base view boundary is fixed to the media size and margins are 
                                adjusted to locate the data view proportionally relative to the requested margins.
            :margins:           (left, right, bottom, top) map margins in map cm.  The default for STYLE_MAP
                                is (3, 14, 6, 3), and for figure (1, 4, 1, 1).
            :inside_margin:     additional margin (cm) inside the base view.  This margin effectively
                                expands the data_area to allow room for graphical elements related to
                                spatial data near the edge of the defined data area.
            :overwrite:         True to overwrite an existing map.  If False and map exists, raises
                                ``MapException``.
            :no_data_view:      True to create a map without a 'Data' view. Use :class:`geosoft.gxpy.view.View` and
                                :class:`geosoft.gxpy.view.View_3d` to add data views to a map.

        .. versionadded:: 9.2
        """

        def data_window_on_map():
            mx = media[0] - m_left - m_right
            my = media[1] - m_bottom - m_top
            im = inside_margin * 2
            return mx - im, my - im  # data window on map cm

        def set_registry(map, style, inside_margin):
            rd = {'MAP.STYLE': style,
                  'MAP.MARGIN_INSIDE': str(inside_margin),
                  'MAP.UP_DIRECTION': 'right',
                  'MAP.UP_ANGLE': '67.5'}
            map.gxmap.set_reg(gxu.reg_from_dict(rd))

        if ((data_area[2] - data_area[0]) <= 0.0) or ((data_area[3] - data_area[1]) <= 0.0):
            raise MapException(_t('Invalid data area {}'.format(data_area)))

        if layout is None:
            if (data_area[2] - data_area[0]) < (data_area[3] - data_area[1]):
                layout = MAP_PORTRAIT
            else:
                layout = MAP_LANDSCAPE

        if file_name is None:
            file_name = unique_temporary_file_name('temp_map')

        else:
            if not overwrite:
                file_name = map_file_name(file_name)
                if os.path.isfile(file_name):
                    raise MapException(_t('Cannot overwrite existing file: "{}"').format(file_name))

        map = cls(file_name, WRITE_NEW, _internal=True)

        if type(media) is str:
            try:
                spec = gxdf.table_record('media', media.upper())
                media = (float(spec['SIZE_X']), float(spec['SIZE_Y']))
            except:
                media = None
                fixed_size = False

        if map_style is None:
            map_style = STYLE_FIGURE

        if media is None:
            fixed_size = False
            if scale:
                media = (5000., 4000.)  # crazy large, will be trimmed to scale
                if margins is None:
                    if map_style == STYLE_MAP:
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
            if map_style == STYLE_MAP:
                if mx <= 30.0:
                    raise MapException(_t('\'map\' style requires minimum 30cm media. Yours is {}cm'.format(mx)))
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
            scale = float(gxu.str_significant(max(sx, sy), 4, 1))

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

        gxapi.GXMVU.mapset(map.gxmap,
                           'base',
                           '' if no_data_view else 'data',
                           data_area[0], data_area[2],
                           data_area[1], data_area[3],
                           '{},{}'.format(media[0] + 50.0, media[1] + 50.0), layout,
                           0, scale, gxapi.rDUMMY,
                           m_left, m_right, m_bottom, m_top,
                           float(inside_margin))

        with gxv.View(map=map, name='*data', mode=gxv.WRITE_OLD) as view:
            view.coordinate_system = coordinate_system
        set_registry(map,
                     'figure' if (map_style == STYLE_FIGURE) else 'map',
                     inside_margin)

        return map

    @property
    def name(self):
        """map name, base name of the map file"""
        return self._name

    @property
    def file_name(self):
        """
        full map file path name.
        """
        return self._file_name

    def _init_metadata(self):
        if not self._metadata:
            self._metadata = gxu.geosoft_metadata(self._file_name)
        self._metadata_root = tuple(self._metadata.items())[0][0]

    @property
    def metadata(self):
        """
        Return the map metadata as a dictionary.  Can be set, in which case
        the dictionary items passed will be added to, or replace existing metadata.

        .. versionadded:: 9.2
        """
        self._init_metadata()
        return self._metadata[self._metadata_root]

    @metadata.setter
    def metadata(self, meta):
        self._init_metadata()
        self._metadata[self._metadata_root] = gxu.merge_dict(self._metadata[self._metadata_root], meta)
        self._metadata_changed = True

    @property
    def current_data_view(self):
        """ 
        Current default data view which accepts drawing groups from Geosoft methods that do not
        explicitly identify a view. Set this to a view that should accept default drawing groups.
        If this is a 3D view, new groups are placed on the default drawing plane of the view.
        """
        return self.get_class_name('data')

    @current_data_view.setter
    def current_data_view(self, s):
        if not self.has_view(s):
            raise MapException(_t('Map does not contain a view named "{}"').format(s))
        self.gxmap.set_class_name('data', s)

    @property
    def current_base_view(self):
        """ 
        The current default base view which accepts map annotation drawing groups 
        (like titles, North arrow, etc.) from Geosoft methods.  This can be set, though
        Geosoft uses the 'base' view in most standard cases.
        """
        return self.get_class_name('base')

    @current_base_view.setter
    def current_base_view(self, s):
        if not self.has_view(s):
            raise MapException(_t('Map does not contain a view named "{}"').format(s))
        self.gxmap.set_class_name('base', s)

    @property
    def current_section_view(self):
        """ The current default base view which accepts drawing commands from Geosoft methods."""
        return self.get_class_name('section')

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

    def extent_data_views(self):
        """
        Returns the extent of all data views on the map in map cm.
        
        .. versionadded:: 9.2
        """
        def extents(ex, ext):
            ex = (min(ex[0], ext[0]),
                  min(ex[1], ext[1]),
                  max(ex[2], ext[2]),
                  max(ex[3], ext[3]))
            return ex

        vlist = self.view_list
        ex = (1.0e10, 1.0e10, -1.0e10, -1.0e10)
        base_view = self.classview('base').lower()
        for view_name in vlist:
            if view_name.lower() != base_view:
                with gxv.View(self, view_name) as v:
                    ex = extents(ex, v.extent_map_cm(v.extent_clip))
        if ex[0] == 1.0e10:
            raise MapException(_t('Map "{}" has no data views.').format(self.name))
        return ex


    def classview(self, name):
        """
        Given a view name that may be a class name ('*' prefix), return the view name for that class.  if not
        class decorated, the name passed is returned.
        
        :param name:    view name, `'*data'` will return the name associated with the `'data'` class, while
                        `'my_view'` will return `'my_view'`.

        :returns:       the name, or if a class name, the view name associated with that class.

        .. versionadded: 9.2
        """
        if name[0] != '*':
            return name
        return self.get_class_name(name[1:])

    def _views(self, view_type=LIST_ALL):
        """
        Return dictionary of view names.
        :param view_type: `gxmap.LIST_ALL`, `gxapi.LIST_2D` or `gxapi.LIST_3D`
        :returns: list of views
        """
        glst = gxapi.GXLST.create(VIEW_NAME_SIZE)
        self.gxmap.view_list_ex(glst, view_type)
        return list(gxu.dict_from_lst(glst))

    @property
    def view_list(self):
        """list of views in the map, both 2D and 3D"""
        return self._views()

    @property
    def view_list_2D(self):
        """list of 2D views in the map"""
        return self._views(LIST_2D)

    @property
    def view_list_3D(self):
        """list of 3D views in the map"""
        return self._views(LIST_3D)

    def aggregate_list(self, mode=0):
        """list of aggregates on the map as 'view_name/group_name'"""
        glst = gxapi.GXLST.create(gxg.GROUP_NAME_SIZE)
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
            raise MapException(_t('Invalid view name "{}", suggest "{}"').format(new, s.value))

    def delete_view(self, name):
        """
        Delete a view from a map. You cannot delete the last view in a mep.

        :param name: name of the view to delete

        .. versionadded:: 9.2
        """
        self.gxmap.delete_view(self.classview(name))

    def mdf(self):
        """
        Returns the Map Description File specification for maps that contain
        both a base view and a data view:

        ((x_size, y_size, margin_bottom, margin_right, margin_top, margin_left),
        (scale, units_per_metre, x_origin, y_origin))

        .. versionadded: 9.2
        """

        views = self.view_list_2D

        if not (self.has_view(self.current_data_view) and self.has_view(self.current_base_view)):
            raise MapException(_t('The map must have both a base view and a data view.'))

        with gxv.View(self, self.current_base_view, gxg.READ_ONLY) as base:
            with gxv.View(self, self.current_data_view, gxg.READ_ONLY) as data:
                mdf = data.mdf(base_view=base)

        return mdf

    def get_class_name(self, view_class):
        """
        Get the view name associated with a class.

        :param view_class:  desired class

        Common view class names are::

            'Base'      the base map/figure view, uses map cm
            'Data'      the default data view for drawing spatial data.
            'Section'   the default section view for things drawn in section

        Other class names may be defined, though they are not used by Geosoft.

        :returns: view name associated with the class, '' if not defined.

        .. versionadded:: 9.2
        """
        sr = gxapi.str_ref()
        self.gxmap.get_class_name(view_class, sr)
        return sr.value.lower()

    def set_class_name(self, view_class, name):
        """
        Set the view name associated with a class.

        :param view_class:  class name
        :param name:   name of the view associated with this class.

        Common view class names are::

            'Base'      the base map/figure view, uses map cm
            'Data'      the default data view for drawing spatial data.
            'Section'   the default section view for things drawn in section

        .. versionadded:: 9.2
        """
        self.gxmap.set_class_name(view_class, name)

    def create_linked_3d_view(self, view, name='3D', area_on_map=(0, 0, 300, 300)):
        """
        Create a linked 3D view inside a 2D map to a :class:`gxpy.view.View_3d` in a 3DV

        :param view:        :class:`gxpy.view.View_3d` instance
        :param name:        name of the linked view to create
        :param area_on_map: min_x, min_y, max_x, max_y) placement of view on map in mm

        .. versionadded:: 9.2
        """

        self.gxmap.create_linked_3d_view(view.gxview, name,
                                         area_on_map[0], area_on_map[1],
                                         area_on_map[2], area_on_map[3])

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
            outer_pen = gxg.Pen(line_thick=0.0500)

        with _Mapplot(self) as mpl:

            mpl.start_group('surround', view=VIEW_BASE, mode=GROUP_APPEND)
            mpl.define_named_attribute('outer', pen=outer_pen)
            if gap <= 0:
                inner = ''
                gap = ''
            else:
                if inner_pen is None:
                    inner_pen = gxg.Pen(line_thick=0.01)
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
        :param text_def:    :class:`gxpy.group.Text_def` instance, or `None` for the default.
        :param pen:         :class:`gxpy.group.Pen` instance, or `None` for the default

        .. versionadded:: 9.2
        """

        if direction is None:
            with gxv.View(self, '*data', mode=gxv.WRITE_OLD) as v:
                direction = round(v.gxview.north(), 1)
                if direction == gxapi.rDUMMY:
                    direction = ''

        if inclination is None:
            inclination = ''

        if declination is None:
            declination = ''

        if pen is None:
            pen = gxg.Pen(line_thick=0.015)

        if text_def is None:
            text_def = gxg.Text_def(height=0.25, italics=True, weight=gxg.FONT_WEIGHT_LIGHT)

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
                  text_def=None,
                  pen=None):
        """
        Draw a scale bar.
        
        :param location:    (ref_point, x_off, y_off) bar location reference point an offset from that point
        :param length:      maximum scale bar length, default is 5 cm. scale=0.0 will suppress drawing of the bar.
        :param sections:    number of major sections in the bar, default is determined automatically.
        :param post_scale:  True to post the actual scale as a string, e.g. '1:50,000'.  Note that a posted
                            scale is only relevant for printed maps.  The default does not post the scale.
        :param text_def:    :class:`gxpy.view.Text_def` instance.
        :param pen:         :class:`gxpy.view.Pen` instance.


        .. versionadded:: 9.2
        """

        if sections is None:
            sections = ''

        if post_scale:
            option = 2
        else:
            option = 1

        if text_def is None:
            text_def = gxg.Text_def(height=0.25, weight=gxg.FONT_WEIGHT_LIGHT, italics=True)

        if pen is None:
            pen = gxg.Pen(line_thick=0.001)

        with _Mapplot(self) as mpl:
            mpl.start_group('scale_bar', view=VIEW_BASE, mode=GROUP_APPEND)
            mpl.define_named_attribute('scale_text', text_def=text_def)
            mpl.define_named_attribute('scale_bar', pen=pen)
            mpl.command("SCAL {},{},{},,,{},{},,{},".format(location[0], location[1], location[2],
                                                            length, sections, option))
            mpl.command('     scale_text')

    def _annotation_offset(self, offset, text_height):
        inside = text_height * 0.25
        if offset:
            offset = offset + inside
        else:
            offset = self._annotation_outer_edge + inside
        self._annotation_outer_edge += offset + text_height + inside * 0.5
        return offset

    def annotate_data_xy(self,
                         view_name='*data',
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

        :param view_name:    name of the data view to annotate
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

        :param text_def:    ``gxg.Text_def``
        :param edge_pen:    ``gxg.Pen``
        :param grid_pen:    ``gxg.Pen``        

        .. versionadded:: 9.2
        """

        if text_def is None:
            text_def = gxg.Text_def(height=0.18)
        if edge_pen is None:
            edge_pen = gxg.Pen()
        if grid_pen is None:
            grid_pen = edge_pen

        current_view = self.current_data_view
        view_name = self.classview(view_name)
        self.current_data_view = view_name

        try:

            offset = self._annotation_offset(offset, text_def.height)

            with gxv.View(self, view_name) as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip, pen=gxg.Pen(default=edge_pen, factor=v.units_per_map_cm))

            with _Mapplot(self) as mpl:

                mpl.start_group(view_name + '_edge', 1, view_name)

                if not tick and grid == GRID_LINES:
                    tick = 0.0

                mpl.define_named_attribute('annot', text_def=text_def,
                                           pen=gxg.Pen(line_color=text_def.color, line_thick=text_def.line_thick))
                mpl.define_named_attribute(pen=edge_pen)

                mpl.command("ANOX ,,,,,{},{},,{},,,,{},{},1".format(x_sep, tick, 0 if compass else -1, offset, x_dec))
                mpl.command('     annot')
                mpl.command(
                    "ANOY ,,,,,{},{},,{},{},,,{},{},1".format(y_sep, tick, 0 if compass else -1, top, offset, y_dec))
                mpl.command('     annot')

                if grid:
                    mpl.define_named_attribute(pen=grid_pen)
                    mpl.command("GRID {},,,,,_".format(grid))

        except:
            raise

        finally:
            self.current_data_view = current_view

    def annotate_data_ll(self,
                         view_name='*data',
                         tick='',
                         offset='',
                         sep='',
                         top=TOP_OUT,
                         text_def=None,
                         edge_pen=None,
                         grid=GRID_LINES,
                         grid_pen=None):

        """
        Annotate the data view axis

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

        :param grid_pen: color-thickness string

        .. versionadded:: 9.2
        """

        if text_def is None:
            text_def = gxg.Text_def(height=0.18)
        if edge_pen is None:
            edge_pen = gxg.Pen()
        if grid_pen is None:
            grid_pen = edge_pen

        current_view = self.current_data_view
        view_name = self.classview(view_name)
        self.current_data_view = view_name

        try:

            offset = self._annotation_offset(offset, text_def.height)

            with gxv.View(self, view_name) as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip, pen=gxg.Pen(default=edge_pen, factor=v.units_per_map_cm))

            with _Mapplot(self) as mpl:

                mpl.start_group(view_name + '_edge', 1, view_name)
                if not tick and grid == GRID_LINES:
                    tick = 0.0

                mpl.define_named_attribute('annot', text_def=text_def,
                                           pen=gxg.Pen(line_color=text_def.color, line_thick=text_def.line_thick))
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

    def export_geotiff(self, geotiff, dpi=96):
        """
        Export map as a GeoTIFF image

        :param geotiff:     GeoTIFF file name
        :param dpi:         DPI to use (Default is common screen resolution of 96)

        .. versionadded:: 9.3
        """
        self.gxmap.export_all_in_view(geotiff, "*Data", gxapi.rDUMMY, dpi, 
            gxapi.MAP_EXPORT_BITS_24, gxapi.MAP_EXPORT_METHOD_NONE, 
            gxapi.MAP_EXPORT_FORMAT_GTIFF, "")


class _Mapplot:
    """Internal class to marshal MAPPLOT commands to support basic map annotations."""

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self._process()

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "mapplot({})".format(self._map.file_name)

    def __init__(self, map, data_view=None, ref_prefix='', **kwargs):

        if not (map.has_view(map.current_base_view) and map.has_view(map.current_data_view)):
            raise MapException(_t("Map must have a '*Base' and '*Data' view."))

        self._map = map
        self._ref_pre = ref_prefix

        if data_view:
            self.prior_data_view = map.current_data_view
            map.current_data_view = data_view
        else:
            self.prior_data_view = None

        # mapplot control file
        self._maplfile_name = os.path.join(gx.gx.temp_folder(), 'mapl_' + gxu.uuid() + ".con")
        self._maplfile = open(self._maplfile_name, "w")
        self._annotation_outer_edge = 0.0

        self._open = gx.track_resource(self.__class__.__name__, self._maplfile_name)

        self.define_named_attribute()

    def _process(self, pop=True):

        if self._maplfile:
            self._maplfile.close()
            self._maplfile = None
            gxmapl = gxapi.GXMAPL.create(self._maplfile_name, self._ref_pre, 0)
            gxmapl.process(self._map.gxmap)
            os.remove(self._maplfile_name)
            if self.prior_data_view:
                self.map.current_data_view = self.prior_data_view
        if pop:
            gx.pop_resource(self._open)

    def command(self, command):
        self._maplfile.write(command)
        if command and command[-1] != '\n':
            self._maplfile.write('\n')
            # geosoft.gxpy.gx.gx.log(command)

    def define_named_attribute(self, name='_', pen=None, text_def=None):

        if (pen is None) and (text_def is None):
            self.command("DATT {}".format(name))

        else:
            if pen is None:
                pen = gxg.Pen(line_color=text_def.color, line_thick=text_def.line_thick)
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