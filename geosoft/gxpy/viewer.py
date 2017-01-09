"""
Geosoft Viewers
"""
#TODO work out a way to satisfy help_ID

import geosoft
import geosoft.gxapi as gxapi
from . import map as gxmap

__version__ = geosoft.__version__

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
            title = gmap.filename()
        gxapi.GXGUI.simple_map_dialog(gmap._map, title, "")

def v3d(map_file_name, viewname=None, title = None):
    """
    Open 3D view in a modal 3D viewer.
    :param map_file_name:   map name
    :param viewname:        3D view name, default is the first 3D view found in the map
    :param title:           viewer title, default is the view name

    .. versionadded:: 9.2

    """

    with gxmap.GXmap.open(map_file_name) as gmap:

        vlist = gmap.view_list(gxmap.LIST_3D)
        if len(vlist) == 0:
            raise ViewerException('\'{}\' has no 3D views.'.format(map_file_name))
        if viewname is None:
            viewname = vlist[0]
        elif viewname not in vlist:
            raise ViewerException('\'{}\' has no view named \'{}\'.'.format(map_file_name, viewname))

        if title is None:
            title = viewname
        map_file_name = gmap.filename()

    #TODO title is not used in the viewer - viewer bug

    gxapi.GXGUI.show_3d_viewer_dialog(title, map_file_name, viewname)
