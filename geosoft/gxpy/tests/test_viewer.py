# import pydevd
# pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import os
import numpy as np

import geosoft.gxpy.gx as gx
import geosoft.gxapi as gxapi
import geosoft.gxpy.geometry as gxgm
import geosoft.gxpy.view as gxv
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.viewer as gxvwr

###############################################################################################

def sample_map(gxp, mapname='test', rescale=1.0, locate=None):

    test_map = os.path.join(gxp.temp_folder(), mapname)
    with gxmap.GXmap.new(test_map, overwrite=True) as gmap:
        with gxv.GXview(gmap, "rectangle_test") as view:
            view.start_group('rect')
            view.xy_rectangle(gxgm.Point((0, 0)), gxgm.Point((110, 110)) * rescale, pen={'line_thick': 1})

            p1 = gxgm.Point((5, 5)) * rescale
            p2 = gxgm.Point((100, 100)) * rescale
            poff = gxgm.Point((10, 5)) * rescale
            view.pen = {'fill_color': gxapi.C_LT_GREEN}
            view.xy_rectangle(p1, p2)

            view.pen = {'line_style': (2, 2.0)}
            view.xy_line(p1 + poff, p2 - poff)

        with gxv.GXview3d(gmap, viewname="poly") as view:
            view.start_group('stuff')
            plinelist = [[110, 5],
                         [120, 20],
                         [130, 15],
                         [150, 50],
                         [160, 70],
                         [175, 35],
                         [190, 65],
                         [220, 50],
                         [235, 18.5]]
            pp = gxgm.PPoint.from_list(plinelist) * rescale
            view.pen = {'line_style': (2, 2.0)}
            view.xy_poly_line(pp)
            view.pen = {'line_style': (4, 2.0), 'line_smooth': gxv.SMOOTH_AKIMA}
            view.xy_poly_line(pp)

            ppp = np.array(plinelist)
            pp = gxgm.PPoint(ppp[3:, :]) * rescale
            view.pen = {'line_style': (5, 5.0),
                          'line_smooth': gxv.SMOOTH_CUBIC,
                          'line_color': gxapi.C_RED,
                          'line_thick': 0.25,
                          'fill_color': gxapi.C_LT_BLUE}
            view.xy_poly_line(pp, close=True)

            view.pen = {'fill_color': gxapi.C_LT_GREEN}
            pp = (pp - (100, 0, 0)) / 2 + (100, 0, 0)
            view.xy_poly_line(pp, close=True)
            pp += (0, 25, 0)
            view.pen = {'fill_color': gxapi.C_LT_RED}
            view.xy_poly_line(pp, close=True)

        return gmap.filename

def test_mapviewer(gxp):

    sample = sample_map(gxp)
    gxvwr.map(sample)
    gxvwr.v3d(sample)

if __name__ == '__main__':

    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    with gx.GXpy(parent_window=-1, log=print) as gxp:
        test_mapviewer(gxp)
