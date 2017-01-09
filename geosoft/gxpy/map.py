#TODO review grd class to clean-up files like map class does.

import os
import gc

import geosoft
import geosoft.gxapi as gxapi
from . import gx as gx
from . import utility as gxu

__version__ = geosoft.__version__

def _(s):
    return s

class MAPException(Exception):
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

    GXmap.open(mapfile)._map.export_all_raster(imagefile, '',
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

        self._map = None
        self._remove = False
        self._filename = map_file_name(filename)
        self._map = gxapi.GXMAP.create(filename, mode)

    def __del__(self):
        if self._map:
            del self._map
            self._map = None
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
        :param overwrite:   True to overwrite an existing map.

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
                    raise MAPException(_('Cannot overwrite existing file: "{}"').format(filename))

        gmap = cls(filename, MAP_WRITENEW)
        gmap.remove_on_close(delete)

        return gmap

    def filename(self):
        """
        Return the full map file path name.
        """
        return self._filename
    
    def remove_on_close(self, remove=True):
        """
        :param remove:  if True (the default), remove the map file when finished.
        """
        self._remove = remove

    def commit_changes(self):
        """Commit changes to the map."""
        self._map.commit()

    def view_list(self, view_type=LIST_ALL):
        """
        Return dictionary of view names.
        :param view_type: `gxmap.LIST_ALL`, `gxapi.LIST_2D` or `gxapi.LIST_3D`
        :return: list of views
        """
        gxlst = gxapi.GXLST.create(VIEW_NAME_SIZE)
        self._map.view_list_ex(gxlst, view_type)
        return list(gxu.dict_from_lst(gxlst))