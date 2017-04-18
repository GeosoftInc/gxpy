# import pydevd
# pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import os
import numpy as np
import unittest

import geosoft.gxpy.gx as gx
import geosoft.gxapi as gxapi
import geosoft.gxpy.geometry as gxgm
import geosoft.gxpy.view as gxv
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.viewer as gxvr
import geosoft.gxpy.group as gxg
import geosoft.gxpy.system as gsys
from geosoft.gxpy.tests import GXPYTest

###############################################################################################

def sample_map(map_file, v3d_file, rescale=1.0):

    with gxmap.GXmap.new(map_file, data_area=(0,0,300,250), overwrite=True) as gmap:
        map_file = gmap.file_name

        p2 = gxgm.Point((110, 110)) * rescale
        with gxv.GXview(gmap, "rectangle_test", area=(0, 0, p2.x, p2.y), scale=100.0) as v:
            with gxg.GXdraw(v, 'rect') as g:

                g.xy_rectangle(((0, 0), p2), pen=gxg.Pen(line_thick=1))
    
                p1 = gxgm.Point((5, 5)) * rescale
                p2 = gxgm.Point((100, 100)) * rescale
                poff = gxgm.Point((10, 5)) * rescale
                g.pen = gxg.Pen(fill_color=gxapi.C_LT_GREEN)
                g.xy_rectangle((p1, p2))
    
                g.pen = gxg.Pen(line_style=2, line_pitch=2.0)
                g.xy_line((p1 + poff, p2 - poff))


    with gxv.GXview3d.new(v3d_file, overwrite=True) as v:
        v3d_file = v.map.file_name

        with gxg.GXdraw(v, '2D_stuff') as g:
            p2 = gxgm.Point((250, 110)) * rescale
            g.xy_rectangle(((0, 0), p2), pen = gxg.Pen(line_thick=3, line_color='B'))
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
            g.pen = gxg.Pen(line_style=2, line_pitch=2.0)
            g.xy_polyline(pp)
            g.pen = gxg.Pen(line_style=4, line_pitch=2.0, line_smooth=gxg.SMOOTH_AKIMA)
            g.xy_polyline(pp)

            ppp = np.array(plinelist)
            pp = gxgm.PPoint(ppp[3:, :]) * rescale
            g.pen = gxg.Pen(line_style=5, line_pitch=5.0,
                     line_smooth=gxg.SMOOTH_CUBIC,
                     line_color=gxapi.C_RED,
                     line_thick=0.25,
                     fill_color=gxapi.C_LT_BLUE)
            g.xy_polyline(pp, close=True)

            g.pen = gxg.Pen(fill_color=gxapi.C_LT_GREEN)
            pp = (pp - (100, 0, 0)) / 2 + (100, 0, 0)
            g.xy_polyline(pp, close=True)
            pp += (0, 25)
            g.pen = gxg.Pen(fill_color="B")
            g.xy_polygon(pp)

        with gxg.GXdraw3d(v, '3d_stuff') as g:
            g.box_3d(((20, 10, 30), (80,50,50)), pen = gxg.Pen(fill_color='R255G100B50'))

    return map_file, v3d_file 

class Test(unittest.TestCase, GXPYTest):

    @classmethod
    def setUpClass(cls):
        GXPYTest.setUpClass(cls, __file__)

    @classmethod
    def tearDownClass(cls):
        GXPYTest.tearDownClass(cls)

    @classmethod
    def start(cls, test, test_name):
        parts = os.path.split(__file__)
        test.result_dir = os.path.join(parts[0], 'results', parts[1], test_name)
        cls.gx.log("*** {} > {}".format(parts[1], test_name))

    def test_mapviewer(self):
        Test.start(self, gsys.func_name())

        map_file = os.path.join(self.gx.temp_folder(), 'test_map')
        v3d_file = os.path.join(self.gx.temp_folder(), 'test_3dv')
        map_file, v3d_file = sample_map(map_file, v3d_file)
        gxvr.map(map_file)
        gxvr.v3d(v3d_file)

if __name__ == '__main__':
    unittest.main()
