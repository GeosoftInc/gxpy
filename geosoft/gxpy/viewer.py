"""
Geosoft Viewers
"""
#TODO work out a way to satisfy help_ID

import geosoft
import geosoft.gxapi as gxapi
from . import map as gxmap

__version__ = geosoft.__version__

def map_viewer(gmap, title=None):
    """
    Open this map in a modal map viewer.
    :param gmap:    map name
    :param title:   viewer title, default is the map name

    .. versionadded:: 9.2
    """

    gmap = gxmap.GXmap.open(gmap)
    if title is None:
        title = gmap.filename()
    gxapi.GXGUI.simple_map_dialog(gmap._map, title, "")

def viewer(mapfile, view=None, title = None):
    with gxmap.GXmap.open(mapfile) as gmap:
        if title is None:
            title = gmap.filename()
    gxapi.GXGUI.show_3d_viewer_dialog(title, gmap, gmap.filename(), "")
