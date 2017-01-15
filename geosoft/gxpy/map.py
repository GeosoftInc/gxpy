#TODO review grd class to clean-up files like map class does.

import os
import gc

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import utility as gxu
from . import dataframe as gxdf

__version__ = geosoft.__version__

def _t(s):
    return s

class MapException(Exception):
    """
    Exceptions from this module.

    .. versionadded:: 9.2
    """
    pass

MAP_WRITENEW = 1
MAP_WRITEOLD = 2

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

    def __init__(self, filename, mode=MAP_WRITENEW):

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

        gmap = cls(filename, mode=MAP_WRITEOLD)

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

        gmap = cls(filename, MAP_WRITENEW)
        gmap.remove_on_close(delete)

        return gmap

    @classmethod
    def new_standard_geosoft(cls, data_area, scale=None,
                             map_spec="landscape A3",
                             hcs=None, vcs=None,
                             z_scale=1.0,
                             **kwa):
        """

        :parameters:
            :data_area: (min_x, min_y, max_x, max_y) data area for the data view on the map
            :scale:     required scale, default will fit data to the map media
            :map_spec:  map template name from the maptmpl table, or a template dictionary (see below)
            :hcs:       horizontal coordinate system, default unknown
            :vcs:       vertical coordinate system, default unknown
            :z_scale:   vertical exaggeration, default no exaggeration

        map_spec dictionary:

        .. code::

            {
                "media":                                # media name from the media table.
                "map_margin": (left, right, bottom, top)# map margins in map cm
                "inside_margin": 0.0                    # additional margin (cm) inside the base view
                "fixed_size":                           # 0 to reduce size to fit data, 1 for fixed media size
                "orient":                               # 0 for landscape, 1 for portrait
            }


        """

        def setup_map_layout(data_area, scale, map_spec):

            def map_spec_from_template(template):
                try:
                    layout = gxdf.table_record('maptmpl', template)

                except gxdf.DfException:
                    return {'template': None,
                            'media': 'Unlimited',
                            'map_margin': (1., 1., 4., 1.),
                            'inside_margin': 1.,
                            'fixed_size': 0,
                            'orient': int((data_area[3] - data_area[1]) > (data_area[2] - data_area[0]))}

                spec = {'template': template,
                        'media': layout['MEDIA'],
                        'map_margin': (float(layout['MARGIN_LEFT']), float(layout['MARGIN_RIGHT']),
                                       float(layout['MARGIN_BOTTOM']), float(layout['MARGIN_TOP'])),
                        'inside_margin': float(layout['MARGIN_INSIDE']),
                        'fixed_size': 1 if layout['FIXED'] == 'fixed' else 0,
                        'orient': 1 if layout['LAYOUT'] == 'portrait' else 0}
                
                return spec

            def media_size(spec):
                if 'media_size' in spec:
                    return spec['media_size']
                try:
                    media = gxdf.table_record('media', spec['media'])
                    size = (float(media['SIZE_X']),
                            float(media['SIZE_Y']),
                            float(media['FULLSIZE_X']),
                            float(media['FULLSIZE_Y']))
                except gxdf.DfException:
                    size = (300.0, 300.0, 300.0, 300.0)
                spec['media_size'] = size
                return size


            def data_window_on_map(spec):
                m = media_size(spec)
                mm = spec['map_margin']
                mx = m[0] - spec['inside_margin'] * 2 - mm[0] - mm[1]
                my = m[1] - spec['inside_margin'] * 2 - mm[2] - mm[3]
                return mx, my # data window on map cm

            if type(map_spec) is str:
                map_spec = map_spec_from_template(map_spec)

            if scale is None:
                # determine largest scale to fit the media
                mx, my = data_window_on_map(map_spec)
                sx = (data_area[2] - data_area[0]) / (mx / 100.0)
                sy = (data_area[3] - data_area[1]) / (my / 100.0)
                scale = max(sx, sy)

            # ensure the data fits on this media
            mx, my = data_window_on_map(map_spec)
            dmx = (data_area[2] - data_area[0]) * 100.0 / scale
            dmy = (data_area[3] - data_area[1]) * 100.0 / scale
            excess_x = mx - dmx
            excess_y = my - dmy
            if excess_x < -0.01 or excess_y < -0.01:
                raise MapException(_t('The data does not fit {}cm at a scale of 1:{}')
                                   .format(map_spec['media_size'][0:2], scale))

            # adjust margins for a fixed map
            if map_spec['fixed_size']:
                x_adjust = excess_x * 0.5
                y_adjust = excess_y * 0.5
                mm = map_spec['map_margin']
                map_spec['map_margin'] = (mm[0] + x_adjust, mm[1] + x_adjust,
                                          mm[2] + y_adjust, mm[3] + y_adjust)

            return map_spec, scale

        def setup_map(gmap, spec, data_area, scale, z_scale):
            margin = spec['map_margin']
            gxapi.GXMVU.mapset2(gmap.gxmap,
                                '*base', '*data',
                                data_area[0], data_area[2], data_area[1], data_area[3],
                                spec['media'],
                                spec['orient'],
                                spec['fixed_size'],
                                scale,
                                z_scale,
                                gxapi.rDUMMY,
                                margin[0], margin[1], margin[2], margin[3],
                                spec['inside_margin'])

        gmap = cls.new(**kwa)
        map_layout, scale = setup_map_layout(data_area, scale, map_spec)
        setup_map(gmap, map_layout, data_area, scale, z_scale)

        # TODO seup map registry - see newmap.gx

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