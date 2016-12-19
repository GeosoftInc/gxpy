import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.geometry as gxgm
import geosoft.gxpy.view as gxv
import geosoft.gxapi as gxapi
import geosoft.gxpy.viewer as gxvwr

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gx = gx.GXpy()
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    
    @classmethod
    def start(cls,test):
        print("\n*** {} *** - {}".format(test, geosoft.__version__))

    def test_version(self):
        self.start(gsys.func_name())
        self.assertEqual(gxmap.__version__, geosoft.__version__)

    def test_geometry(self):
        self.start(gsys.func_name())

        p = gxgm.Point((5,10))
        self.assertEqual(p.p.tolist(), [5.0, 10.0, 0.0])
        self.assertEqual(p.xy(), (5.0,10.0))
        self.assertEqual(p.xyz(), (5.0, 10.0, 0.0))
        self.assertEqual(p.x(), 5.0)
        self.assertEqual(p.y(), 10.0)

        p -= (0, 0, 15)
        self.assertEqual(p.xyz(), (5.0, 10.0, -15.0))


    def test_create(self):
        self.start(gsys.func_name())

        with gxv.GXview():
            pass

        with gxv.GXview() as vw:
            self.assertEqual(vw.viewname(), "_default_view_")

        with gxv.GXview("test") as vw:
            self.assertEqual(vw.viewname(), "test")

        gmap = gxmap.GXmap.new("test_map")
        gmap.remove_on_close(True)
        mapname = gmap.filename()
        with gxv.GXview("test", gmap) as vw:
            self.assertEqual(vw.viewname(), "test")
            self.assertEqual(vw.mapname(), mapname)


    def test_line_drawing(self):
        self.start(gsys.func_name())

        with gxmap.GXmap.new("test", overwrite=True) as gmap:
            mapfile = gmap.filename()
            with gxv.GXview("rectangle_test", gmap) as view:
                p1 = gxgm.Point((0, 0))
                p2 = gxgm.Point((100, 100))
                poff = gxgm.Point((10, 5))
                view.set_pen({'fill_color': gxapi.C_LT_GREEN})
                pen = view.get_pen()
                self.assertEqual(pen['fill_color'], gxapi.C_LT_GREEN)
                view.xy_rectangle(p1, p2)

                view.set_pen({'line_style': (2, 2.0)})
                view.xy_line(p1 + poff, p2 - poff)

            plinelist = [[110,5],
                         [120,20],
                         [130,15],
                         [150,50],
                         [160,70],
                         [190,50],
                         [220,50],
                         [235,18.5]]

            with gxv.GXview("poly", gmap) as view:
                view.set_pen({'line_style': (2, 2.0)})
                view.xy_poly_line(gxgm.PPoint.from_list(plinelist))
                view.set_pen({'line_style': (4, 2.0), 'line_smooth': gxv.SMOOTH_AKIMA})
                view.xy_poly_line(gxgm.PPoint.from_list(plinelist))

                ppp = np.array(plinelist)
                pp = gxgm.PPoint(ppp[3:,:])
                view.set_pen({'line_style': (5, 5.0),
                              'line_smooth': gxv.SMOOTH_CUBIC,
                              'line_color': gxapi.C_RED,
                              'line_thick': 0.25,
                              'fill_color': gxapi.C_LT_BLUE})
                view.xy_poly_line(pp, close=True)

                view.set_pen({'fill_color':gxapi.C_LT_GREEN})
                pp = (pp - (100, 0, 0)) / 2 + (100, 0, 0)
                view.xy_poly_line(pp, close=True)
                pp += (0, 25, 0)
                view.set_pen({'fill_color': gxapi.C_LT_RED})
                view.xy_poly_line(pp, close=True)

        gxvwr.map_viewer(mapfile)
        gxmap.delete_files(mapfile)

if __name__ == '__main__':

    unittest.main()
