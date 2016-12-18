import unittest
import os

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
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


    def test_line_box(self):
        self.start(gsys.func_name())

        with gxv.GXview() as view:

            view.rectangle(gxv.Point(0,0), gxv.Point(15,10))
            self.assertTrue(os.path.isfile(view.map().filename()))

        with gxmap.GXmap.new("test_rectangle", overwrite=True) as gmap:
            mapfile = gmap.filename()
            with gxv.GXview("rectangle_test", gmap) as view:
                p1 = gxv.Point(0,0)
                p2 = gxv.Point(150,100)
                poff = gxv.Point(10,5)
                view.set_pen({'fill_color': gxapi.C_LT_GREEN})
                pen = view.get_pen()
                self.assertEqual(pen['fill_color'], gxapi.C_LT_GREEN)
                view.rectangle(p1, p2)

                view.set_pen({'line_style': (2, 2.0)})
                view.xy_line(p1 + poff, p2 - poff)

        gxvwr.map_viewer(mapfile)
        gxmap.delete_files(mapfile)


if __name__ == '__main__':

    unittest.main()
