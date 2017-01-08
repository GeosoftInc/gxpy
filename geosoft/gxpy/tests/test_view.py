import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.utility as gxu
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.geometry as gxgm
import geosoft.gxpy.view as gxv
import geosoft.gxapi as gxapi
import geosoft.gxpy.viewer as gxvwr


def rect_line(view, size=100):
    view.xy_rectangle(gxgm.Point((0, 0)), gxgm.Point((1, 1)) * size, pen={'line_thick': 1})
    p1 = gxgm.Point((0.1, 0.1)) * size
    p2 = gxgm.Point((0.9, 0.9)) * size
    poff = gxgm.Point((0.15, 0.05)) * size
    view.set_pen({'fill_color': gxapi.C_LT_GREEN})
    view.xy_rectangle(p1, p2)
    view.set_pen({'line_style': (2, 2.0)})
    view.xy_line(p1 + poff, p2 - poff)


def draw_stuff(view, size = 1.0):
    plinelist = [[110, 5],
                 [120, 20],
                 [130, 15],
                 [150, 50],
                 [160, 70],
                 [175, 35],
                 [190, 65],
                 [220, 50],
                 [235, 18.5]]

    pp = gxgm.PPoint.from_list(plinelist) * size
    view.set_pen({'line_style': (2, 2.0)})
    view.xy_poly_line(pp)
    view.set_pen({'line_style': (4, 2.0), 'line_smooth': gxv.SMOOTH_AKIMA})
    view.xy_poly_line(pp)

    ppp = np.array(plinelist)
    pp = gxgm.PPoint(ppp[3:, :]) * size
    view.set_pen({'line_style': (5, 5.0),
                  'line_smooth': gxv.SMOOTH_CUBIC,
                  'line_color': gxapi.C_RED,
                  'line_thick': 0.25,
                  'fill_color': gxapi.C_LT_BLUE})
    view.xy_poly_line(pp, close=True)

    view.set_pen({'fill_color': gxapi.C_LT_GREEN})
    p1 = gxgm.Point((100, 0, 0)) * size
    p2 = gxgm.Point((100, 0, 0)) * size
    pp = (pp - p1) / 2 + p2
    view.xy_poly_line(pp, close=True)
    pp += gxgm.Point((0, 25, 0)) * size
    view.set_pen({'fill_color': gxapi.C_LT_RED})
    view.xy_poly_line(pp, close=True)


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gx = gx.GXpy(log=print, parent_window=-1)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    
    @classmethod
    def start(cls,test):
        cls.gx.log("\n*** {} *** - {}".format(test, geosoft.__version__))

    def test_version(self):
        self.start(gsys.func_name())
        self.assertEqual(gxmap.__version__, geosoft.__version__)

    def test_create(self):
        self.start(gsys.func_name())

        with gxv.GXview():
            pass

        with gxv.GXview() as vw:
            self.assertEqual(vw.viewname(), "_default_view")

        with gxv.GXview("test") as vw:
            self.assertEqual(vw.viewname(), "test")

        test_map = os.path.join(self.gx.temp_folder(),"test_map")
        gmap = gxmap.GXmap.new(test_map)
        mapname = gmap.filename()
        with gxv.GXview("test", gmap) as view:
            self.assertEqual(view.viewname(), "test")
            self.assertEqual(view.mapname(), mapname)

            def_pen = view.get_pen()
            pn = {"line_thick": 99, "pat_number": 88}
            view.push_pen()
            view.set_pen(pn)
            new_pen = view.get_pen()
            self.assertEqual(new_pen["line_thick"], 99)
            self.assertEqual(new_pen["pat_number"], 88)

            view.pop_pen()
            pen = view.get_pen()
            self.assertEqual(pen, def_pen)

            view.push_pen(pn)
            view.set_pen(pn)
            new_pen = view.get_pen()
            self.assertEqual(new_pen["line_thick"], 99)
            self.assertEqual(new_pen["pat_number"], 88)

            view.pop_pen()
            pen = view.get_pen()
            self.assertEqual(pen, def_pen)


    def test_line_drawing(self):
        self.start(gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            mapfile = gmap.filename()
            with gxv.GXview("rectangle_test", gmap) as view:
                rect_line(view)
            with gxv.GXview("poly", gmap) as view:
                draw_stuff(view)

        # gxvwr.map_viewer(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 1477469463)
        gxmap.delete_files(mapfile)

if __name__ == '__main__':

    unittest.main()
