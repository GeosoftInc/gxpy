#TODO review grd class to clean-up files like map class does.

import os
import gc
import uuid

import geosoft
import geosoft.gxapi as gxapi
from . import ipj as gxipj
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

    filename = map_file_name(filename)
    os.remove(filename + '.xml')
    os.remove(filename)


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
            filename = str(uuid.uuid1())
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
