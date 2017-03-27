import unittest
import os
import numpy as np

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.view as gxv
import geosoft.gxpy.geometry as gxgm
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.viewer as gxvwr


def new_test_map(mapname=None, rescale=1.0):

    if mapname is None:
        mapname = os.path.join(gx.GXpy().temp_folder(), 'test')
    with gxmap.GXmap.new(mapname, overwrite=True) as gmap:
        with gxv.GXview(gmap, "rectangle_test") as view:
            view.start_group('rectangle')
            view.xy_rectangle((gxgm.Point((0, 0)), gxgm.Point((250, 110))), pen={'line_thick': 1})

            p1 = gxgm.Point((5, 5)) * rescale
            p2 = gxgm.Point((100, 100)) * rescale
            poff = gxgm.Point((10, 5)) * rescale
            view.pen = {'fill_color': gxapi.C_LT_GREEN}
            view.xy_rectangle((p1, p2))

            view.pen = {'line_style': (2, 2.0)}
            view.xy_line((p1 + poff, p2 - poff))

        with gxv.GXview(gmap, "poly") as view:
            view.start_group('poly')
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

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gx = gx.GXpy(log=print, parent_window=-1, max_warnings=8)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    
    @classmethod
    def start(cls,test):
        cls.gx.log("*** {} > {}".format(os.path.split(__file__)[1], test))

    def test_version(self):
        self.start(gsys.func_name())
        self.assertEqual(gxmap.__version__, geosoft.__version__)

    def test_newmap(self):
        self.start(gsys.func_name())

        # temp map
        with gxmap.GXmap.new() as gmap:
            mapfile = gmap.filename
            self.assertTrue(os.path.isfile(mapfile))
        self.assertFalse(os.path.isfile(mapfile))

        # test map
        map_name = 'test_newmap'
        gxmap.delete_files(map_name)
        with gxmap.GXmap.new(map_name) as gmap:
            mapfile = gmap.filename
            self.assertEqual(mapfile, os.path.abspath((map_name + '.map')))
        self.assertTrue(os.path.isfile(mapfile))

        # verify can't write on a new map
        self.assertRaises(gxmap.MapException, gxmap.GXmap.new, map_name)
        self.assertRaises(gxmap.MapException, gxmap.GXmap.new, mapfile)
        with gxmap.GXmap.new(map_name, overwrite=True):
            pass

        # but I can open it
        with gxmap.GXmap.open(map_name):
            pass
        with gxmap.GXmap.open(mapfile):
            pass

        gxmap.delete_files(mapfile)
        self.assertFalse(os.path.isfile(mapfile))

    def test_new_geosoft_map(self):
        self.start(gsys.func_name())

        # temp map
        with gxmap.GXmap.new(data_area=(0, 0, 100, 80)) as gmap:
            views = gmap.view_list(gxmap.LIST_ALL)
            self.assertTrue('Base' in views)
            self.assertTrue('Data' in views)

        with gxmap.GXmap.new(data_area=(0, 0, 100, 80),
                             cs=gxcs.GXcs("DHDN / Okarito 2000 [geodetic]")) as gmap:
            with gxv.GXview(gmap, 'Data', mode=gxv.WRITE_OLD) as v:
                self.assertEqual("DHDN / Okarito 2000 [geodetic]", str(v.cs))

    def test_lists(self):
        self.start(gsys.func_name())

        mapname = new_test_map()
        with gxmap.GXmap.open(mapname) as gmap:

            views = gmap.view_list(gxmap.LIST_ALL)
            self.assertTrue('rectangle_test' in views)
            self.assertTrue('poly' in views)

            views = gmap.view_list(gxmap.LIST_2D)
            self.assertTrue('rectangle_test' in views)
            self.assertTrue('poly' in views)

            views = gmap.view_list(gxmap.LIST_3D)
            self.assertEqual(len(views), 0)

    def test_map_delete(self):
        self.start(gsys.func_name())

        with gxmap.GXmap.new(filename='test_geosoft', overwrite=True) as gmap:
            filename = gmap.filename
            self.assertEqual(len(gmap.view_list()), 2)
            self.assertTrue(gmap.has_view('*Data'))
            self.assertTrue(gmap.has_view('*Base'))
        self.assertTrue(os.path.isfile(filename))
        with open(filename, 'rb') as f:
            pass

        with gxmap.GXmap.new(filename='test_geosoft',
                             overwrite=True,
                             data_area=(1000,200,11000,5000)) as gmap:
            filename = gmap.filename
            self.assertEqual(len(gmap.view_list()), 2)
            self.assertTrue(gmap.has_view('*Data'))
            self.assertTrue(gmap.has_view('*Base'))
        self.assertTrue(os.path.isfile(filename))
        with open(filename, 'rb') as f:
            pass

        with gxmap.GXmap.new(filename='test_geosoft', overwrite=True) as gmap:
            filename = gmap.filename
            gmap.remove_on_close(True)
        self.assertFalse(os.path.isfile(filename))

        for i in range(3):
            gmap = gxmap.GXmap.new(filename='t{}'.format(i), overwrite=True)
            gmap.remove_on_close(True)
            gmap.close()

    def test_map_classes(self):
        self.start(gsys.func_name())

        with gxmap.GXmap.new(filename='test_geosoft', overwrite=True) as gmap:
            self.assertEqual(gmap.get_class_view_name('Data'), 'Data')
            self.assertEqual(gmap.get_class_view_name('data'), 'Data')
            self.assertEqual(gmap.get_class_view_name('Base'), 'Base')
            self.assertEqual(gmap.get_class_view_name('base'), 'Base')
            self.assertEqual(gmap.get_class_view_name('Section'), 'Section')
            self.assertEqual(gmap.get_class_view_name('section'), 'Section')
            self.assertEqual(gmap.get_class_view_name('some_class_name'), 'some_class_name')

            gmap.set_class_view_name('Base', 'bogus')
            self.assertEqual(gmap.get_class_view_name('Base'), 'bogus')
            gmap.set_class_view_name('Data', 'bogus_Data')
            #self.assertEqual(gmap.get_class_view_name('Data'), 'bogus_Data')
            gmap.set_class_view_name('Section', 'yeah')
            self.assertEqual(gmap.get_class_view_name('Section'), 'yeah')
            gmap.set_class_view_name('mine', 'boom')
            self.assertEqual(gmap.get_class_view_name('mine'), 'boom')

        with gxmap.GXmap.new(data_area=(0, 0, 100, 80),
                             cs=gxcs.GXcs("DHDN / Okarito 2000 [geodetic]")) as gmap:

            self.assertEqual(gmap.get_class_view_name('Base'), 'Base')
            self.assertEqual(gmap.get_class_view_name('Data'), 'Data')

            gxv.GXview(gmap, "copy_data", mode=gxv.WRITE_NEW, copy="*Data")
            gmap.set_class_view_name('Data', 'copy_data')
            self.assertEqual(gmap.get_class_view_name('Data'), 'copy_data')

    def test_media(self):
        self.start(gsys.func_name())

        def test_crc(mapfile, crc=None, display=False):
            with gxmap.GXmap.open(mapfile) as map:
                with gxv.GXview(map, "*Base") as view:
                    view.xy_rectangle(view.extent(), pen={'line_thick': 0.2, 'line_color': 'K'})
                with gxv.GXview(map, "*Data") as view:
                    view.xy_rectangle(view.extent(), pen={'line_thick': 0.2, 'line_color': 'R'})
            if display:
                gxvwr.map(mapfile)
            if crc:
                self.assertEqual(gxmap.crc_map(mapfile), crc)

        test_media_map = os.path.join(gx.GXpy().temp_folder(), 'test_media')

        with gxmap.GXmap.new(test_media_map, overwrite=True, scale=800,
                             data_area=(5, 10, 50, 100)) as map:
            filename = map.filename
        test_crc(filename, 1043288043)

        with gxmap.GXmap.new(test_media_map, overwrite=True, scale=100,
                             data_area=(5, 10, 50, 100)) as map:
            filename = map.filename
        test_crc(filename, 1535590917)

        with gxmap.GXmap.new(test_media_map, overwrite=True, media='A4 portrait') as map:
            filename = map.filename
        test_crc(filename, 2682492121)

        with gxmap.GXmap.new(test_media_map, overwrite=True, media='Portraita4') as map:
            filename = map.filename
        test_crc(filename, 2682492121)

        with gxmap.GXmap.new(test_media_map, overwrite=True, media='A4 landscape') as map:
            filename = map.filename
        test_crc(filename, 2828292428)

        with gxmap.GXmap.new(test_media_map, overwrite=True, media='A4', data_area=(10, 5, 100, 50)) as map:
            filename = map.filename
        test_crc(filename, 1741315204)

        with gxmap.GXmap.new(test_media_map, overwrite=True, media='A4',
                             data_area=(5, 10, 50, 100), layout='landscape') as map:
            filename = map.filename
        test_crc(filename, 1539773502)

        with gxmap.GXmap.new(test_media_map, overwrite=True, media='A4',
                             data_area=(5, 10, 50, 100)) as map:
            filename = map.filename
        test_crc(filename, 211035832)

        for m in (None, (60, 50), 'unlimited', 'bogus', 'A4', 'A3', 'A2', 'A1', 'A0',
                  'A', 'B', 'C', 'D', 'E'):
            with gxmap.GXmap.new(media=m) as map: pass

        self.assertRaises(gxmap.MapException,
                          gxmap.GXmap.new,
                          test_media_map, overwrite=True, media='A4',
                          data_area=(100, 50, 10, 5), layout='landscape')

if __name__ == '__main__':

    unittest.main()
