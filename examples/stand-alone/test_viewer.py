# import pydevd
# pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import os
import numpy as np
import unittest

import geosoft.gxapi as gxapi
import geosoft.gxpy.geometry as gxgm
import geosoft.gxpy.view as gxv
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.group as gxg
import geosoft.gxpy.system as gxsys
from geosoft.gxpy.tests import GXPYTest


def rungx():
    raise Exception("This is not an extension.  Please use a python interpreter.")


def sample_map(map_file, v3d_file, rescale=1.0):

    with gxmap.Map.new(map_file, data_area=(0,0,300,250), overwrite=True) as gmap:
        map_file = gmap.file_name

        p2 = gxgm.Point((110, 110)) * rescale
        with gxv.View(gmap, "rectangle_test", area=(0, 0, p2.x, p2.y), scale=100.0) as v:
            with gxg.Draw(v, 'rect') as g:

                g.rectangle(((0, 0), p2), pen=gxg.Pen(line_thick=1))
    
                p1 = gxgm.Point((5, 5)) * rescale
                p2 = gxgm.Point((100, 100)) * rescale
                poff = gxgm.Point((10, 5)) * rescale
                g.pen = gxg.Pen(fill_color=gxapi.C_LT_GREEN)
                g.rectangle((p1, p2))
    
                g.pen = gxg.Pen(line_style=2, line_pitch=2.0)
                g.line((p1 + poff, p2 - poff))


    with gxv.View_3d.new(v3d_file, overwrite=True) as v:
        v3d_file = v.map.file_name

        with gxg.Draw(v, '2D_stuff') as g:
            p2 = gxgm.Point((250, 110)) * rescale
            g.rectangle(((0, 0), p2), pen = gxg.Pen(line_thick=3, line_color='B'))
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
            g.polyline(pp)
            g.pen = gxg.Pen(line_style=4, line_pitch=2.0, line_smooth=gxg.SMOOTH_AKIMA)
            g.polyline(pp)

            ppp = np.array(plinelist)
            pp = gxgm.PPoint(ppp[3:, :]) * rescale
            g.pen = gxg.Pen(line_style=5,
                            line_pitch=5.0,
                            line_smooth=gxg.SMOOTH_CUBIC,
                            line_color=gxapi.C_RED,
                            line_thick=0.25,
                            fill_color=gxapi.C_LT_BLUE)
            g.polyline(pp, close=True)

            g.pen = gxg.Pen(fill_color=gxapi.C_LT_GREEN,
                            line_smooth=gxg.SMOOTH_CUBIC)
            pp = (pp - (100, 0, 0)) / 2 + (100, 0, 0)
            g.polyline(pp, close=True)
            pp += (0, 25)
            g.pen = gxg.Pen(fill_color="B")
            g.polygon(pp)

        with gxg.Draw_3d(v, '3d_stuff') as g:
            g.box_3d(((20, 10, 30), (80,50,50)), pen = gxg.Pen(line_color='R255G100B50'))

    return map_file, v3d_file 

class Test(GXPYTest):

    def test_mapviewer(self):
        self.start()

        map_file = os.path.join(self.gx.temp_folder(), 'test_map')
        v3d_file = os.path.join(self.gx.temp_folder(), 'test_3dv')
        map_file, v3d_file = sample_map(map_file, v3d_file)
        self.crc_map(map_file, alt_crc_name=gxsys.func_name() + '_map')
        self.crc_map(v3d_file, alt_crc_name=gxsys.func_name() + '_3dv')

if __name__ == '__main__':
    unittest.main()
