# import pydevd
# pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import os
import geosoft.gxpy.gx as gx
import geosoft.gxapi as gxapi
import geosoft.gxpy.geometry as gxgm
import geosoft.gxpy.view as gxv
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.viewer as gxvwr

###############################################################################################

def sample_map():
    sample = os.path.join(gx.gxcontext.temp_folder(), "sample_map")
    with gxmap.GXmap.new(sample, overwrite=True) as gmap:
        with gxv.GXview("rectangle_test", gmap) as view:
            p1 = gxgm.Point((0,0))
            p2 = gxgm.Point((150,100))
            poff = gxgm.Point((10,5))
            view.set_pen({'fill_color': gxapi.C_LT_GREEN})
            view.xy_rectangle(p1, p2)

            view.set_pen({'line_style': (2, 2.0)})
            view.xy_line(p1 + poff, p2 - poff)
        return gmap.filename()

def test_mapviewer():
    
    gxvwr.map_viewer(sample_map())

if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    with gx.GXpy(parent_window=-1) as gxp:
        test_mapviewer()
