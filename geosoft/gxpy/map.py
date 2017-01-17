#TODO review grd class to clean-up files like map class does.

import os
import gc
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

    GXmap.open(mapfile).gxmap.export_all_raster(imagefile, '',
                                                pix_width, pix_height, gxapi.rDUMMY,
                                                gxapi.MAP_EXPORT_BITS_24,
                                                gxapi.MAP_EXPORT_METHOD_NONE,
                                                type,
                                                '')

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
    Geosoft map class.

    Creation options:

        ====== =============================
        open() open an existing map
        new()  create a new map
        ====== =============================

    .. versionadded:: 9.2
    """

    def __enter__(self):
        return self

    def __exit__(self, xtype, xvalue, xtraceback):
        self.__del__()

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return self._filename

    def __init__(self, filename, mode=WRITE_NEW):

        self.gxmap = None
        self._remove = False
        self._filename = map_file_name(filename)
        self.gxmap = gxapi.GXMAP.create(filename, mode)

    def __del__(self):
        if self.gxmap:
            del self.gxmap
            self.gxmap = None
            gc.collect()
            if self._remove:
                try:
                    delete_files(self._filename)
                except OSError: # remove if we can
                    pass

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
    def new(cls, filename=None, overwrite=False):
        """
        Create a new map file.

        :param filename:    name of the map file, None for a temporary map (default)
        :param overwrite:   True to overwrite an existing map.  If False and map exists
                            a MapException is raised.

        .. versionadded:: 9.2
        """
        
        if filename is None:
            
            # get a temporary map file name
            filename = map_file_name(os.path.join(gx.GXpy().temp_folder(), str(gxu.uuid())))
            delete = True

        else:
            delete = False
            if overwrite is False:
                filename = map_file_name(filename)
                if os.path.isfile(filename):
                    raise MapException(_t('Cannot overwrite existing file: "{}"').format(filename))

        gmap = cls(filename, WRITE_NEW)
        gmap.remove_on_close(delete)

        return gmap

    @classmethod
    def new_standard_geosoft(cls, data_area, scale=None,
                             hcs=None, vcs=None,
                             media="A3", fixed_size=False, style='figure',
                             margins=None, inside_margin=1.0,
                             **kwa):
        """

        :parameters:
            :data_area:     (min_x, min_y, max_x, max_y) data area for the data view on the map
            :scale:         required scale, default will fit data to the map media
            :hcs:           horizontal coordinate system, default unknown
            :vcs:           vertical coordinate system, default unknown
            :media:         media name and optional 'portrait' suffix.  Named media sizes are read
                            from media.csv.  For example `media='A4 portrait'`.
            :fixed_size:    True for fixed media size
            :map_style:     'map' or 'figure'
            :margins:       (left, right, bottom, top) map margins in map cm
            :inside_margin: additional margin (cm) inside the base view.  This margin effectively
                            expands the data_area.

        .. versionadded:: 9.2
        """

        def setup_map(gmap, data_area, scale, media, margins):

            def set_media_size(media):
                m = media.split(' ')[0]
                try:
                    spec = gxdf.table_record('media', m)
                    size = (float(spec['SIZE_X']),
                            float(spec['SIZE_Y']))
                    if 'portrait' in media:
                        if size[0] > size[1]:
                            return m, (size[1], size[0])
                    return m, size
                except:
                    return 'A3', (37.94, 26.85) # default A3

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
                if style == 'map':
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

            # ensure the data fits on this media
            mx, my = data_window_on_map(media_size, margins, inside_margin, inside=False)
            dmx = (data_area[2] - data_area[0]) * 100.0 / scale
            dmy = (data_area[3] - data_area[1]) * 100.0 / scale
            if (mx - dmx) < -0.01 or (my - dmy) < -0.01:
                raise MapException(_t('The data does not fit media ({},{})cm at a scale of 1:{}')
                                   .format(media_size[0], media_size[1], scale))

            # adjust margins for a fixed map
            if fixed_size:
                mx, my = data_window_on_map(media_size, margins, inside_margin)
                x_adjust = max(0, (mx - ((data_area[2] - data_area[0]) * 100.0 / scale)) * 0.5)
                y_adjust = max(0, (my - ((data_area[3] - data_area[1]) * 100.0 / scale)) * 0.5)
                margins = (margins[0] + x_adjust, margins[1] + x_adjust,
                           margins[2] + y_adjust, margins[3] + y_adjust)

            gxapi.GXMVU.mapset(gmap.gxmap,
                                '*Base', '*Data',
                                data_area[0], data_area[2], data_area[1], data_area[3],
                                media,
                                int(media_size[1] > media_size[0]),
                                0, scale, gxapi.rDUMMY,
                                margins[0], margins[1], margins[2], margins[3],
                                inside_margin)

        def set_coordinate_system(gmap, hcs, vcs):
            with gxvw.GXview(gmap=gmap, viewname='*Data', mode=gxvw.WRITE_OLD) as view:
                view.set_cs(hcs, vcs)

        def set_registry(gmap, style, inside_margin):
            rd = {'MAP.STYLE': style,
                  'MAP.MARGIN_INSIDE': str(inside_margin),
                  'MAP.UP_DIRECTION': 'right',
                  'MAP.UP_ANGLE': '67.5'}
            gmap.gxmap.set_reg(gxu.reg_from_dict(rd))
            mdf = gmap.mapfilename[:-4] + '.mdf'
            #gxapi.GXMVU.map_mdf(gmap.gxmap, mdf, '*Data')

        gmap = cls.new(**kwa)
        setup_map(gmap, data_area, scale, media, margins)
        set_coordinate_system(gmap, hcs, vcs)
        set_registry(gmap, style, inside_margin)

        return gmap

    @property
    def mapfilename(self):
        """
        Full map file path name.
        """
        return self._filename
    
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