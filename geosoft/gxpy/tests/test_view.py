import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.geometry as gxgm
import geosoft.gxpy.view as gxv
import geosoft.gxapi as gxapi
import geosoft.gxpy.viewer as gxvwr
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.grd as gxgrd
import geosoft.gxpy.agg as gxagg
import geosoft.gxpy.system as gxsys

from geosoft.gxpy.tests import GXPYTest


def rect_line(v, size=100):
    v.xy_rectangle(gxgm.Point2((0, 0, size, size), cs="cm"), pen=v.new_pen(line_thick=1))
    p1 = gxgm.Point((0.1, 0.1)) * size
    p2 = gxgm.Point((0.9, 0.9)) * size
    poff = gxgm.Point((0.15, 0.05)) * size
    v.xy_rectangle((p1, p2), pen=v.new_pen(fill_color = gxv.C_LT_GREEN))
    p12 = gxgm.Point2((p1 + poff, p2 - poff))
    v.xy_line((p12.p1.x, p12.p1.y, p12.p2.x, p12.p2.y), pen=v.new_pen(line_style = 2, line_pitch = 2.0))

def pline():
   return gxgm.PPoint([[10, 5],
                 [20, 20],
                 [30, 15],
                 [50, 50],
                 [60, 70],
                 [75, 35],
                 [90, 65],
                 [20, 50],
                 [35, 18.5]])


def draw_stuff(v, size = 1.0):
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
    v.pen = v.new_pen(line_style=2, line_pitch=2.0)
    v.xy_poly_line(pp)
    v.pen = v.new_pen(line_style=4, line_pitch=2.0, line_smooth=gxv.SMOOTH_AKIMA)
    v.xy_poly_line(pp)

    ppp = np.array(plinelist)
    pp = gxgm.PPoint(ppp[3:, :]) * size
    v.pen = v.new_pen(line_style = 5, line_pitch=5.0,
                       line_smooth = gxv.SMOOTH_CUBIC,
                       line_color = gxv.C_RED,
                       line_thick = 0.25,
                       fill_color = gxv.C_LT_BLUE)
    v.xy_poly_line(pp, close=True)

    v.pen = v.new_pen(fill_color = gxv.C_LT_GREEN)
    p1 = gxgm.Point((100, 0, 0)) * size
    p2 = gxgm.Point((100, 0, 0)) * size
    pp = (pp - p1) / 2 + p2
    v.xy_poly_line(pp, close=True)
    pp += gxgm.Point((0, 25, 0)) * size
    v.pen = v.new_pen(fill_color = gxv.C_LT_RED)
    v.xy_poly_line(pp, close=True)


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

    def test_version(self):
        Test.start(self, gsys.func_name())
        self.assertEqual(gxmap.__version__, geosoft.__version__)

    def test_create(self):
        Test.start(self, gsys.func_name())

        with gxmap.GXmap.new() as gmap:
            vlist = gmap.view_list()
            self.assertEqual(len(vlist), 2)
            self.assertTrue('base' in vlist)
            self.assertTrue('data' in vlist)
            with gxv.GXview(gmap, 'base') as v:
                self.assertEqual(v.viewname, "base")
                self.assertEqual(v.scale, 1000.0)
                self.assertEqual(v.aspect, 1.0)
                self.assertEqual(v.units_name, 'unknown')
                self.assertEqual(v.units_per_metre, 1.0)
                self.assertEqual(v.units_per_map_cm, 10.0)

            with gxv.GXview(gmap, 'ft12000', cs='ft', scale=12000,
                            area=(0, 0, 50000, 40000)) as v:
                self.assertEqual(v.viewname, "ft12000")
                self.assertAlmostEqual(v.scale, 12000.0)
                self.assertAlmostEqual(v.aspect, 1.0)
                self.assertEqual(v.units_name, 'ft')
                self.assertAlmostEqual(v.units_per_metre, 3.280839895)
                self.assertAlmostEqual(v.units_per_map_cm, 393.7007874)

            with gxv.GXview(gmap) as vw:
                self.assertEqual(vw.viewname, "_unnamed_view")
                self.assertEqual(vw.scale, 100.0)
                self.assertEqual(vw.aspect, 1.0)
                self.assertEqual(vw.units_name, 'unknown')
                self.assertEqual(vw.units_per_metre, 1.0)

        with gxmap.GXmap.new() as gmap:
            with gxv.GXview(gmap, "test") as vw:
                self.assertEqual(vw.viewname, "test")

        with gxmap.GXmap.new() as gmap:
            area = (100, 500, 15100, 10500)
            scale = 20000
            location = (0,0)
            xcm = (area[2] - area[0])*100.0/scale
            ycm = (area[3] - area[1])*100.0/scale
            with gxv.GXview(gmap, "test", map_location=location, area=area,
                            scale=scale, cs="WGS 84 / UTM zone 34N") as vw:
                self.assertEqual(vw.extent_clip,area)
                self.assertEqual(vw.extent_map_cm(vw.extent_clip), (0, 0, xcm, ycm))
                self.assertEqual(vw.scale, scale, scale)
                self.assertTrue(vw.cs.same_as(gxcs.GXcs("WGS 84 / UTM zone 34N")))
                self.assertEqual(vw.units_per_metre, 1.0)
                self.assertEqual(vw.units_name, 'm')

        with gxmap.GXmap.new() as gmap:
            area = (100, 500, 15100, 10500)
            scale = 12000
            loc = (7.5, 2.0)
            mpu = 1.0 / float(gxcs.parameters(gxcs.PARM_UNITS, 'ftUS')['FACTOR'])
            xcm = 100.0 * ((area[2] - area[0]) / scale) / mpu
            ycm = 100.0 * ((area[3] - area[1]) / scale) / mpu
            with gxv.GXview(gmap, "test", map_location=loc, area=area,
                            scale=scale, cs=("WGS 84 / UTM zone 34N", '', '', 'ftUS', '')) as vw:
                self.assertEqual(vw.extent_clip,area)
                mx = vw.extent_map_cm(vw.extent_clip)
                self.assertAlmostEqual(mx[0], loc[0])
                self.assertAlmostEqual(mx[1], loc[1])
                self.assertAlmostEqual(mx[2], loc[0] + xcm)
                self.assertAlmostEqual(mx[3], loc[1] + ycm)
                self.assertAlmostEqual(vw.scale, scale)
                self.assertAlmostEqual(vw.aspect, 1.0)
                self.assertFalse(vw.cs.same_as(gxcs.GXcs("WGS 84 / UTM zone 34N")))
                self.assertTrue(vw.cs.same_as(gxcs.GXcs(("WGS 84 / UTM zone 34N", '', '', 'ftUS', ''))))
                self.assertAlmostEqual(vw.units_per_metre, 3.28083333333334)
                self.assertEqual(vw.units_name, 'ftUS')

        with gxmap.GXmap.new() as gmap:
            area = (100, 500, 15100, 10500)
            scale = 12000
            loc = (7.5, 2.0)
            mpu = 1.0 / float(gxcs.parameters(gxcs.PARM_UNITS, 'ftUS')['FACTOR'])
            xcm = 100.0 * ((area[2] - area[0]) / scale) / mpu
            ycm = 100.0 * ((area[3] - area[1]) / scale) / mpu
            with gxv.GXview(gmap, "test", map_location=loc, area=area,
                            scale=scale, cs='ftUS') as vw:
                self.assertEqual(vw.extent_clip,area)
                mx = vw.extent_map_cm(vw.extent_clip)
                self.assertAlmostEqual(mx[0], loc[0])
                self.assertAlmostEqual(mx[1], loc[1])
                self.assertAlmostEqual(mx[2], loc[0] + xcm)
                self.assertAlmostEqual(mx[3], loc[1] + ycm)
                self.assertAlmostEqual(vw.scale, scale)
                self.assertAlmostEqual(vw.aspect, 1.0)
                self.assertTrue(vw.cs.same_as(gxcs.GXcs(('', '', '', 'ftUS', ''))))
                self.assertAlmostEqual(vw.units_per_metre, 3.28083333333334)
                self.assertEqual(vw.units_name, 'ftUS')

        with gxmap.GXmap.new() as gmap:
            with gxv.GXview(gmap, "test", area=(100, 500, 15100, 10500), scale=(50000, 10000),
                            map_location=(10, 25)) as vw:
                self.assertEqual(vw.extent_clip,(100, 500, 15100, 10500))
                self.assertEqual(vw.scale, 50000)
                self.assertEqual(vw.aspect, 0.2)
                self.assertEqual(vw.extent_map_cm(vw.extent_clip), (10., 25., 40., 125.))
                self.assertTrue(vw.cs.same_as(gxcs.GXcs()))

    def test_rectangle(self):
        Test.start(self, gsys.func_name())

        with gxmap.GXmap.new(data_area=(0,0,50,40), cs='cm') as map:
            mapfile = map.filename
            with gxv.GXview(map, 'data') as v:
                v.xy_rectangle(v.extent_clip, pen=v.new_pen(line_thick=0.5, line_color='B'))
                v.xy_rectangle((2,2,48,38), pen=v.new_pen(line_thick=0.25, line_color='R', line_style=gxv.LINE_STYLE_LONG, line_pitch=5))

        self.crc_map(mapfile)

    def test_smooth_line(self):
        Test.start(self, gsys.func_name())

        pp = pline()
        p1, p2 = pp.extent()
        area = (p1.x, p1.y, p2.x, p2.y)
        with gxmap.GXmap.new() as map:
            mapfile = map.filename
            with gxv.GXview(map, 'data', area=area, cs='mm') as v:
                v.xy_rectangle(v.extent_clip)
                v.xy_poly_line(pp, pen=v.new_pen(line_smooth=gxv.SMOOTH_AKIMA, line_color='r', line_thick=1))
                v.xy_poly_line(pp, pen=v.new_pen(line_smooth=gxv.SMOOTH_CUBIC, line_color='b', line_thick=2))
                v.xy_poly_line(pp)

        self.crc_map(mapfile)

    def test_view_groups_1(self):
        Test.start(self, gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            mapfile = gmap.filename
            with gxv.GXview(gmap, "rectangle_test", area=(0,0,250, 125)) as v:
                v.start_group('test_group')
                rect_line(v)
                v.graticule(25, 20, style=gxv.GRATICULE_LINE)
                v.pen = v.new_pen(line_thick = 0.1)
                v.xy_rectangle(((0,0),(250,125)), pen=v.new_pen(line_thick = 0.1, line_color ='R'))
            with gxv.GXview(gmap, "poly") as v:
                v.start_group('test_group')
                draw_stuff(v)

        self.crc_map(mapfile)
        gxmap.delete_files(mapfile)

    def test_view_groups_2(self):
        Test.start(self, gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            mapfile = gmap.filename
            with gxv.GXview(gmap, "rectangle_test", area=(0,0,250, 125)) as v:
                v.start_group('line')
                rect_line(v)
                v.start_group('graticule')
                v.graticule(25, 20, style=gxv.GRATICULE_LINE)
                v.pen = v.new_pen(line_thick = 0.1)
                v.start_group('test_rectangles')
                v.xy_rectangle(((0,0),(250,125)), pen=v.new_pen(line_thick = 0.1, line_color ='R'))
                v.xy_rectangle(((10, 5), (240, 120)), pen=v.new_pen(line_thick = 2, line_color = 'B'))
                v.delete_group('graticule')
            with gxv.GXview(gmap, "poly") as v:
                v.start_group('test_group')
                draw_stuff(v)

        self.crc_map(mapfile)
        gxmap.delete_files(mapfile)

    def test_reopen_map_view(self):
        Test.start(self, gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            mapfile = gmap.filename
            with gxv.GXview(gmap, "test_view") as v:
                rect_line(v)
            with gxv.GXview(gmap, "test_view") as v:
                pass
        gxmap.delete_files(mapfile)

    def test_3D(self):
        Test.start(self, gsys.func_name())

        test3dv = os.path.join(self.gx.temp_folder(), "test.geosoft_3dv")
        testmap = os.path.join(self.gx.temp_folder(), "test.map")
        with gxmap.GXmap.new(test3dv, overwrite=True, no_data_view=True) as g3dv:
            with gxv.GXview3d(g3dv, mode=gxv.WRITE_NEW) as view_3d:
                view_3d.start_group('2d_group')
                rect_line(view_3d)
                draw_stuff(view_3d)
                view_3d.start_group('3d_group')
                view_3d.box_3d(((20, 10, 30), (80,50,50)), pen=view_3d.new_pen(fill_color='R255G100B50'))
                
                with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
                    with gxv.GXview(gmap, "base") as view_base:
                        view_base.start_group('Surround')
                        view_base.xy_rectangle(((0, 0), (280, 260)))
                    gmap.create_linked_3d_view(view_3d, area=(10,10,270,250))

        self.crc_map(test3dv, alt_crc_name=gxsys.func_name()+'_3dv')
        self.crc_map(testmap, alt_crc_name=gxsys.func_name()+'_map')

    def test_cs(self):
        Test.start(self, gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            with gxv.GXview(gmap, "rectangle_test", cs="wgs 84") as v:
                self.assertEqual("WGS 84", str(v.cs))
            with gxv.GXview(gmap, "vcs", cs="wgs 84 / UTM zone 15N [special]") as v:
                self.assertTrue("WGS 84 / UTM zone 15N [special]" in str(v.cs))

    def test_basic_drawing(self):
        Test.start(self, gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True, data_area=(0, 0, 25, 20), scale=100.0) as gmap:
            mapfile = gmap.filename
            with gxv.GXview(gmap, "my_base_view", area=(0, 0, 25, 20), scale=100.0) as v:
                v.xy_rectangle(v.extent_clip, pen=v.new_pen(line_thick=0.1, line_color='R'))

            with gxv.GXview(gmap, "my_data_area", map_location=(4,3), area=(0, 0, 1800, 1500), scale=10000) as v:
                v.xy_rectangle(((0, 0), (1800, 1500)),
                                  pen=v.new_pen(line_thick = 5, line_color = 'G'))

                v.graticule(style=gxv.GRATICULE_LINE, pen=v.new_pen(line_thick = 5))

            gmap.delete_view('*data')
            gmap.delete_view('*base')

        self.crc_map(mapfile)

    def test_basic_grid_1(self):
        Test.start(self, gsys.func_name())

        # test grid file
        folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                   folder=self.gx.temp_folder())
        grid_file = os.path.join(folder, 'test_agg_utm.grd')
        map_file = os.path.join(self.gx.temp_folder(), "test_agg_utm")

        with gxgrd.GXgrd(grid_file) as grd:
            cs = grd.cs
            area = grd.extent_2d()
        with gxmap.GXmap.new(map_file,
                             data_area=area, media="A4", margins=(0,0,0,0),
                             cs=cs, overwrite=True) as gmap:
            mapfile = gmap.filename
            with gxv.GXview(gmap, "base") as v:
                v.xy_rectangle(v.extent_clip, pen=v.new_pen(line_thick = 1, line_color = 'K'))
            with gxv.GXview(gmap, "data") as v:
                v.xy_rectangle(area, pen=v.new_pen(line_thick = 0.1, line_color = 'R'))

                with gxagg.GXagg(grid_file) as agg:
                    v.aggregate(agg)

        self.crc_map(mapfile)

    def test_basic_grid_2(self):
        Test.start(self, gsys.func_name())

        # test grid file
        folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                   folder=self.gx.temp_folder())
        grid_file = os.path.join(folder, 'test_agg_utm.grd')
        map_file = os.path.join(self.gx.temp_folder(), "test_agg_utm")

        with gxgrd.GXgrd(grid_file) as grd:
            cs = grd.cs
            area = grd.extent_2d()
        with gxmap.GXmap.new(map_file,
                             data_area=area, media="A3", margins=(0,0,0,0),
                             scale=(area[2] - area[0])/0.2,
                             cs=cs, overwrite=True) as gmap:
            mapfile = gmap.filename
            with gxv.GXview(gmap, "base") as v:
                v.xy_rectangle(v.extent_clip, pen=v.new_pen(line_thick = 2, line_color = 'K'))
            with gxv.GXview(gmap, "data") as v:
                v.xy_rectangle(area, pen=v.new_pen(line_thick = 0.1, line_color = 'G'))
                with gxagg.GXagg(grid_file) as agg:
                    v.aggregate(agg)

        self.crc_map(mapfile)

    @unittest.skip("Inconsistent results due to temp folder use...")  #
    # Complete TODO in GXPYTest._agnosticize_and_ensure_consistent_line_endings
    def test_zone_grid(self):
        Test.start(self, gsys.func_name())

        def test_zone(zone, suffix, shade=False):
            map_file = os.path.join(self.gx.temp_folder(), "test_agg_" + suffix)
            with gxmap.GXmap.new(map_file, overwrite=True,
                                 data_area=(ex[0], ex[1], ex[2], ex[3]),
                                 scale=(ex[2] - ex[0]) / 0.2) as gmap:
                mapfile = gmap.filename
                with gxv.GXview(gmap, "data") as v:
                    with gxagg.GXagg(grid_file, zone=zone, shade=shade) as agg:
                        v.aggregate(agg)
                gmap.delete_view('base')

            self.crc_map(mapfile, alt_crc_name='{}_{}'.format(gxsys.func_name(1), suffix))

        # test grid file
        folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                   folder=self.gx.temp_folder())
        grid_file = os.path.join(folder, 'test_agg_utm.grd')
        with gxgrd.GXgrd(grid_file) as grd:
            ex = grd.extent_2d()
        

        test_zone(gxagg.ZONE_LINEAR, "linear_shade", shade=True)
        test_zone(gxagg.ZONE_EQUALAREA, "eq_area")
        test_zone(gxagg.ZONE_DEFAULT, "default")
        test_zone(gxagg.ZONE_LAST, "last")
        test_zone(gxagg.ZONE_LINEAR, "linear")
        test_zone(gxagg.ZONE_NORMAL, "normal")
        test_zone(gxagg.ZONE_SHADE, "shade")
        test_zone(gxagg.ZONE_LOGLINEAR, "log_linear")

    @unittest.skip("Inconsistent results due to temp folder use...")
    # Complete TODO in GXPYTest._agnosticize_and_ensure_consistent_line_endings
    def test_color_bar(self):
        Test.start(self, gsys.func_name())

        # test grid file
        folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                   folder=self.gx.temp_folder())
        grid_file = os.path.join(folder, 'test_agg_utm.grd')
        map_file = os.path.join(self.gx.temp_folder(), "test_agg_utm")

        with gxgrd.GXgrd(grid_file) as grd:
            ex = grd.extent_2d()
            cs = grd.cs
        with gxmap.GXmap.new(map_file, overwrite=True,
                             data_area=ex, margins=(1,6,3,1)) as gmap:
            mapfile = gmap.filename
            with gxv.GXview(gmap, "data") as v:
                v.xy_rectangle(v.extent_clip, pen=v.new_pen(line_thick = 0.1, line_color = 'R'))

                with gxagg.GXagg(grid_file, shade=True) as agg:
                    v.aggregate(agg)

            with gxv.GXview(gmap, "data") as v:
                v.xy_rectangle(v.extent_clip, pen=v.new_pen(line_thick=0.1, line_color='R'))

            with gxv.GXview(gmap, "base") as v:
                v.xy_rectangle(v.extent_clip, pen=v.new_pen(line_thick = 0.1, line_color = 'B'))

            gmap.annotate_data_ll(grid=gxmap.GRID_LINES,
                                  grid_pen=gxv.Pen.from_mapplot_string("bt250"),
                                  text_def=gxv.Text_def(height=0.25, italics=True),
                                  top=gxmap.TOP_IN)

        self.crc_map(mapfile)

    def test_text_definition(self):
        Test.start(self, gsys.func_name())

        t = gxv.Text_def()
        self.assertEqual(t.slant, 0)
        self.assertEqual(t.height, 0.25)
        self.assertEqual(t.weight, gxv.FONT_WEIGHT_MEDIUM)
        self.assertEqual(t.font, 'DEFAULT')
        t.font="Arial"
        self.assertEqual(t.font, 'Arial')
        self.assertEqual(t.mapplot_string, '0.25,,,0,"Arial(TT)"')
        t.font = 'sr.gfn'
        self.assertEqual(t.mapplot_string, '0.25,,,0,"sr"')
        t.font = ''
        self.assertEqual(t.mapplot_string, '0.25,,,0,"DEFAULT"')
        t.italics = True
        self.assertTrue(t.italics)
        self.assertEqual(t.slant, 15)
        t.italics = 0
        self.assertFalse(t.italics)
        self.assertEqual(t.slant, 0)

        t.weight = gxv.FONT_WEIGHT_ULTRALIGHT
        self.assertAlmostEqual(t.line_thick, 0.005208333333333333)
        t.weight = gxv.FONT_WEIGHT_BOLD
        self.assertAlmostEqual(t.line_thick, 0.020833333333333331)
        thick = t.line_thick
        t.weight = gxv.FONT_WEIGHT_XXBOLD
        self.assertAlmostEqual(t.line_thick, 0.0625)
        t.line_thick = thick
        self.assertEqual(t.weight, gxv.FONT_WEIGHT_BOLD)
        t.height = 10.
        self.assertEqual(t.weight, gxv.FONT_WEIGHT_BOLD)
        self.assertAlmostEqual(t.line_thick, 0.8333333333333333)
        t.line_thick = t.line_thick
        self.assertEqual(t.weight, gxv.FONT_WEIGHT_BOLD)

    def test_colours(self):
        Test.start(self, gsys.func_name())

        c = gxv.Color((150, 200, 500))
        self.assertEqual(c.rgb, (150, 200, 255))
        c = gxv.Color((150, 200, 500), model=gxv.C_CMY)
        self.assertEqual(c.cmy, (150, 200, 255))

        c = gxv.Color('r255g128b56')
        self.assertEqual(c.rgb, (255, 128, 56))
        self.assertEqual(c.cmy, (0, 127, 199))
        c.rgb = (64, 32, 16)
        self.assertEqual(c.rgb, (64, 32, 16))
        c.cmy = (100, 200, 300)
        self.assertEqual(c.cmy, (100, 200, 255))

        c = gxv.Color((0,127,64), gxv.C_HSV)
        self.assertEqual(c.rgb, (191, 96, 96))

        c = gxv.Color(gxv.C_GREEN)
        self.assertEqual(c.rgb, (0, 255, 0))

        c2 = gxv.Color(c)
        self.assertEqual(c2.rgb, (0, 255, 0))

        c = gxv.Color(gxv.C_TRANSPARENT)
        self.assertEqual(c.rgb, None)
        self.assertEqual(c.cmy, None)
        self.assertTrue(c == gxv.Color(gxv.C_TRANSPARENT))

    def test_pen(self):
        Test.start(self, gsys.func_name())

        p = gxv.Pen()
        self.assertEqual(p.line_color.int, gxv.C_BLACK)
        self.assertEqual(p.fill_color.int, gxv.C_TRANSPARENT)
        self.assertEqual(p.line_style, gxv.LINE_STYLE_SOLID)

        p.line_color = (255,127,64)
        self.assertEqual(p.mapplot_string, 'r255g127b64t100')

        p = gxv.Pen.from_mapplot_string('r20b100k16R64K16')
        ms = p.mapplot_string
        self.assertEqual(ms, 'r4g0b84R48G0B0t1')
        p = gxv.Pen.from_mapplot_string(ms)
        self.assertEqual(p.mapplot_string, ms)

        p = gxv.Pen(line_color='K')
        self.assertEqual(p.line_color.int, gxv.C_BLACK)
        self.assertTrue(p.line_color == gxv.Color(gxv.C_BLACK))

        p = gxv.Pen(line_color=gxv.C_WHITE)
        self.assertEqual(p.line_color.int, gxv.C_WHITE)
        self.assertTrue(p.line_color == gxv.Color(gxv.C_WHITE))

        p = gxv.Pen.from_mapplot_string('r20b100k16R64K16')
        p = gxv.Pen(default=p, line_thick=0.05, fill_color='K')
        ms = p.mapplot_string
        self.assertEqual(ms, 'r4g0b84R0G0B0t500')
        p = gxv.Pen.from_mapplot_string(ms)
        self.assertEqual(p.mapplot_string, ms)

        self.assertRaises(gxv.ViewException, gxv.Pen, bad=1)

    def test_scaled(self):
        Test.start(self, gsys.func_name())

        p = gxv.Pen(factor=10)
        self.assertEqual(p.line_thick, 0.1)
        self.assertEqual(p.line_pitch, 5.0)
        self.assertEqual(p.pat_thick, 0.1)
        self.assertEqual(p.pat_size, 10.0)

        p = gxv.Pen(default=p, factor=5)
        self.assertEqual(p.line_thick, 0.5)
        self.assertEqual(p.line_pitch, 25.0)
        self.assertEqual(p.pat_thick, 0.5)
        self.assertEqual(p.pat_size, 50.0)

        t = gxv.Text_def(factor=0.2)
        self.assertEqual(t.height, 0.05)

    def test_text(self):
        Test.start(self, gsys.func_name())

        with gxmap.GXmap.new(data_area=(400000, 5000000, 500000, 5150000),
                         cs='WGS 84 / UTM zone 15N [geoid]') as map:
            mapfile = map.filename
            map.surround()
            with gxv.GXview(map, 'base') as v:
                v.text('Text on base view')
                v.text('Bigger, blue, higher',
                       (v.units_per_map_cm, v.units_per_map_cm),
                       text_def=gxv.Text_def(height=20, color='B', font='Times New Roman'))
                v.text('Bigger, blue, angled, italics',
                       (10, 25),
                       angle=60,
                       text_def=gxv.Text_def(height=20, color='B', font='Calibri', italics=True))

        self.crc_map(mapfile)

    def test_text(self):
        Test.start(self, gsys.func_name())

        with gxmap.GXmap.new(data_area=(400000, 5000000, 500000, 5150000),
                         cs='WGS 84 / UTM zone 15N [geoid]') as map:
            mapfile = map.filename
            map.surround()
            with gxv.GXview(map, 'base') as v:
                v.text('Text on base view')
                v.text('Bigger, blue, higher',
                       (v.units_per_map_cm, v.units_per_map_cm),
                       text_def=gxv.Text_def(height=20, color='B', font='Times New Roman'))
                v.text('Bigger, blue, angled, italics',
                       (10, 25),
                       angle=60,
                       text_def=gxv.Text_def(height=20, color='B', font='Calibri', italics=True))

        self.crc_map(mapfile)

    def test_text_1(self):
        Test.start(self, gsys.func_name())

        with gxmap.GXmap.new(data_area=(400000, 5000000, 500000, 5050000),
                         cs='WGS 84 / UTM zone 15N [geoid]') as map:
            mapfile = map.filename
            map.surround()
            with gxv.GXview(map, '*data') as v:
                ex = v.extent_clip
                width = ex[2] - ex[0]
                height = ex[3] - ex[1]
                cxy = (ex[0] + width / 2, ex[1] + height / 2)
                td = gxv.Text_def(height=width / 20, color='K128', font='sr.gfn', weight=gxv.FONT_WEIGHT_XBOLD)
                v.xy_rectangle(ex)
                v.xy_line((ex[0], cxy[1], ex[2], cxy[1]))
                v.xy_line((cxy[0], ex[1], cxy[0], ex[3]))
                v.text('Centered',
                       cxy,
                       text_def=td,
                       reference=gxv.TEXT_REF_MIDDLE_CENTER)
                v.text('Bottom',
                       (cxy[0], ex[1]),
                       text_def=td,
                       reference=gxv.TEXT_REF_BOTTOM_CENTER)
                v.text('Top',
                       (cxy[0], ex[3]),
                       text_def=td,
                       reference=gxv.TEXT_REF_TOP_CENTER)
                v.text('Left',
                       (ex[0], cxy[1]),
                       text_def=td,
                       angle=90,
                       reference=gxv.TEXT_REF_TOP_CENTER)
                v.text('Right',
                       (ex[2], cxy[1]),
                       text_def=td,
                       angle=-90,
                       reference=gxv.TEXT_REF_TOP_CENTER)

        self.crc_map(mapfile)


if __name__ == '__main__':

    unittest.main()
