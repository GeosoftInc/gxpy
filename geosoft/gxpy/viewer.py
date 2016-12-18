"""
Geosoft Viewers
"""
#TODO work out a way to satisfy help_ID

import geosoft
import geosoft.gxapi as gxapi
from . import map as gxmap

__version__ = geosoft.__version__

def map_viewer(gmap):
    """
    Open this map in a modal map viewer.
    :param gmap: map name

    .. versionadded:: 9.2
    """

    gmap = gxmap.GXmap.open(gmap)
    gxapi.GXGUI.simple_map_dialog(gmap._map, gmap.filename(), "")
