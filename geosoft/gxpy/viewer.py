"""
Geosoft Viewers
"""
#TODO work out a way to satisfy help_ID

import geosoft
import geosoft.gxapi as gxapi
from . import map as gxmap

__version__ = geosoft.__version__


def _t(s):
    return geosoft.gxpy.system.translate(s)


class ViewerException(Exception):
    """
    Exceptions from this module.

    .. versionadded:: 9.2
    """
    pass

def map(map_file_name, title=None):
    """
    Open map in a modal map viewer.
    :param map_file_name:   map name
    :param title:           viewer title, default is the map name

    .. versionadded:: 9.2
    """

    with gxmap.GXmap.open(map_file_name) as gmap:
        if title is None:
            title = gmap.filename
        gxapi.GXGUI.simple_map_dialog(gmap.gxmap, title, "")

def v3d(file_name, title = None):
    """
    Open 3D view in a modal 3D viewer.
    :param file_name:   3D View file name (.geosoft_3dv)
    :param title:       viewer title, default is file_name

    .. versionadded:: 9.2

    """

    if title is None:
        title = file_name
    gxapi.GXGUI.show_3d_viewer_dialog(title, file_name)
