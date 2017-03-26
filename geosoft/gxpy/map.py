import os
import atexit
from math import ceil

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import utility as gxu
from . import dataframe as gxdf
from . import view as gxvw

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

def map_file_name(filename):
    """
    Return a fully resolved map file path using the filename, with .map extyension

    :param filename:    file name, with ot without path and/or extension
    :return:            file name path with extension .map

    .. versionadded:: 9.2
    """
    if os.path.splitext(filename)[1].lower() != '.map':
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

    Geosoft maps will also have one or more 'data' views, each with it's own defined coordinate system
    and graphical content.  Creating a new map will always create one data view, which will become
    the map's `default data view`, within which any spatial data presented by Geosoft 2D drawing applications
    will be placed.  Maps may have more than one data view, including 3D data views, and the `default
    data view` can be changed to any 2D or 3D view such that subsequent drawing will occur in the so-identified
    view.  See ``set_default_data_view`` for more information.

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

    def __init__(self, filename, mode=WRITE_NEW):

        self.gxmap = None
        self._remove = False
        self._filename = map_file_name(filename)
        self.gxmap = gxapi.GXMAP.create(self.filename, mode)

        atexit.register(self._close, pop=False)
        self._open = gx.track_resource(self.__class__.__name__, self._filename)

    def _close(self, pop=True):
        if self._open:
            if self.gxmap:

                if not self._remove:

                    # if I have read access to the map, creat an MDF
                    if self.has_view("*Base") and self.has_view("*Data"):

                        # close the file to close all views, then re-open to create an mdf
                        self.gxmap = None
                        gxmap = gxapi.GXMAP.create(self._filename, WRITE_OLD)
                        mdfname = os.path.splitext(self.filename)[0] + '.mdf'
                        try:
                            gxapi.GXMVU.map_mdf(gxmap, mdfname, "*Data")
                        except:
                            pass

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

        gmap = cls(filename, mode=WRITE_OLD)

        return gmap

    @classmethod
    def new(cls, filename=None, data_area=(0.,0.,100.,100.), scale=None,
            cs=None, media="A0", fixed_size=None, map_style='figure',
            margins=None, inside_margin=1.0, overwrite=False):

        """
        Create and open a new Geosoft map.

        :parameters:
            :filename:      Map file name.  If not specified a temporary file is created.
            :data_area:     (min_x, min_y, max_x, max_y) data area for a 2D data view on the map
            :scale:         required scale, default will fit data to the map media
            :cs:            coordinate system, default is an unknown coordinate system.  You may pass
                            a ``coordinate_system.GXcs`` instance, a string descriptor, such as
                            `WGS 84 / UTM zone 15N`, or another valid constructor supported by
                            ``coordinate_system.GXcs``.
            :media:         media name and optional 'portrait' suffix.  Named media sizes are read
                            from media.csv.  The default is 'Unlimited', which allows for a map size of
                            up to 300 x 300 cm.  For example `media='A4 portrait'`.
            :map_style:     'map' or 'figure' (default).  A 'map' style is intended for A3 or larger
                            media with a larger right or left margin for map annotations.  A 'figure'
                            style is intended for smaller media with a larger bottom margin for a
                            title and limited annotations.
            :fixed_size:    True for fixed media size. The default is True for 'figure' map_style, and
                            False for 'map' map_style. If False, the base view boundary will be reduced
                            to the data view plus margins.  Tf True, the base view boundary is fixed to
                            the media size and margins are adjusted to locate the data view proportionally
                            relative to the requested margins.
            :margins:       (left, right, bottom, top) map margins in map cm.  The default for 'map'
                            style is (3, 14, 6, 3), and for figure (1, 4, 1, 1).
            :inside_margin: additional margin (cm) inside the base view.  This margin effectively
                            expands the data_area to allow room for graphical elements related to
                            spatial data near the edge of the defined data area.
            :overwrite:     True to overwrite an existing map.  If False and map exists, raises
                            ``MapException``.

        .. versionadded:: 9.2
        """

        def setup_map(gmap, data_area, scale, media, margins, fixed_size):

            def set_media_size(media):
                m = media.split(' ')[0]
                try:
                    spec = gxdf.table_record('media', m)
                    size = (float(spec['SIZE_X']),
                            float(spec['SIZE_Y']))
                except:
                    m = 'A3'
                    size = (37.94, 26.85)

                if 'portrait' in media:
                    if size[0] > size[1]:
                        return m, (size[1], size[0])
                return m, size

            def data_window_on_map(media_size, margins, inside_margin, inside=True):
                mx = media_size[0] - margins[0] - margins[1]
                my = media_size[1] - margins[2] - margins[3]
                if inside:
                    im = inside_margin * 2
                    mx -= im
                    my -= im
                return mx, my # data window on map cm

            media, media_size = set_media_size(media)
            if margins is None:
                mx, my = media_size
                if map_style == 'map':
                    if mx <= 30.0:
                        raise MapException('\'map\' style requires minimum 30cm media. Yours is {}cm'.format(mx))
                    margins = (max(1.5, mx * 0.025),
                               max(14.0, mx * 0.15),
                               max(5.0, my * 0.1),
                               max(1.5, mx * 0.025))
                else:
                    margins = (max(1.0, mx * 0.04),
                               max(1.0, mx * 0.04),
                               max(4.0, my * 0.15),
                               max(1.5, mx * 0.04))

            if scale is None:
                # determine largest scale to fit the media
                mx, my = data_window_on_map(media_size, margins, inside_margin)
                sx = (data_area[2] - data_area[0]) * 100.0 / mx
                sy = (data_area[3] - data_area[1]) * 100.0 / my
                scale = max(sx, sy)
                if scale > 100:
                    scale = float(ceil(scale))

            # adjust margins for a fixed map
            if fixed_size is None:
                if map_style == 'figure':
                    fixed_size = True
                else:
                    fixed_size = False

            if fixed_size:
                mx, my = data_window_on_map(media_size, margins, inside_margin)
                x_adjust = max(0, (mx - ((data_area[2] - data_area[0]) * 100.0 / scale)) * 0.5)
                y_adjust = max(0, (my - ((data_area[3] - data_area[1]) * 100.0 / scale)) * 0.5)
                margins = (margins[0] + x_adjust, margins[1] + x_adjust,
                           margins[2] + y_adjust, margins[3] + y_adjust)

            # ensure the data fits on this media
            mx, my = data_window_on_map(media_size, margins, inside_margin, inside=False)
            dmx = (data_area[2] - data_area[0]) * 100.0 / scale
            dmy = (data_area[3] - data_area[1]) * 100.0 / scale
            if (mx - dmx) < -0.01 or (my - dmy) < -0.01:
                raise MapException(_t('The data does not fit media ({},{})cm at a scale of 1:{}')
                                   .format(media_size[0], media_size[1], scale))

            gxapi.GXMVU.mapset( gmap.gxmap,
                                '*Base', '*Data',
                                data_area[0], data_area[2], data_area[1], data_area[3],
                                media,
                                int(media_size[1] > media_size[0]),
                                0, scale, gxapi.rDUMMY,
                                margins[0], margins[1], margins[2], margins[3],
                                inside_margin)

        def set_coordinate_system(gmap, cs):
            with gxvw.GXview(gmap=gmap, viewname='*Data', mode=gxvw.WRITE_OLD) as view:
                view.set_cs(cs)

        def set_registry(gmap, style, inside_margin):
            rd = {'MAP.STYLE': style,
                  'MAP.MARGIN_INSIDE': str(inside_margin),
                  'MAP.UP_DIRECTION': 'right',
                  'MAP.UP_ANGLE': '67.5'}
            gmap.gxmap.set_reg(gxu.reg_from_dict(rd))

        if filename is None:

            # get a temporary map file name
            filename = map_file_name(os.path.join(gx.GXpy().temp_folder(), str(gxu.uuid())))
            delete = True

        else:
            delete = False
            if not overwrite:
                filename = map_file_name(filename)
                if os.path.isfile(filename):
                    raise MapException(_t('Cannot overwrite existing file: "{}"').format(filename))

        gmap = cls(filename, WRITE_NEW)
        gmap.remove_on_close(delete)

        setup_map(gmap, data_area, scale, media, margins, fixed_size)
        set_coordinate_system(gmap, cs)
        set_registry(gmap, map_style, inside_margin)

        return gmap

    @property
    def filename(self):
        """
        Full map file path name.
        """
        return self._filename

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

    def view_list(self, view_type=LIST_ALL):
        """
        Return dictionary of view names.
        :param view_type: `gxmap.LIST_ALL`, `gxapi.LIST_2D` or `gxapi.LIST_3D`
        :return: list of views
        """
        gxlst = gxapi.GXLST.create(VIEW_NAME_SIZE)
        self.gxmap.view_list_ex(gxlst, view_type)
        return list(gxu.dict_from_lst(gxlst))

    def has_view(self, view):
        """ Returns True if the map contains this view."""
        return self.gxmap.exist_view(view)

    def mdf(self):
        """
        Returns the Map Description File specification for maps that contain
        both a base view and a data view.

        ((x_size, y_size, margin_bottom, margin_right, margin_top, margin_left),
         (scale, units_per_metre, x_origin, y_origin))\

        .. versionadded: 9.2
        """

        views = self.view_list()

        if not(self.has_view("*Data") and self.has_view("*Base")):
            raise MapException('The map must have both a "*Base" view and a "*Data" view.')

        xmn = gxapi.float_ref()
        ymn = gxapi.float_ref()
        xmx = gxapi.float_ref()
        ymx = gxapi.float_ref()

        with gxvw.GXview(self, "*Base", gxvw.READ_ONLY) as v:
            v.gxview.extent(gxapi.MVIEW_EXTENT_CLIP, gxapi.MVIEW_EXTENT_UNIT_MM,
                            xmn, ymn, xmx, ymx)
            mapx = (xmx.value - xmn.value) * 0.1
            mapy = (ymx.value - ymn.value) * 0.1

        with gxvw.GXview(self, "*Data", gxvw.READ_ONLY) as v:
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
        return sr.value

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
