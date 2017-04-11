import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.geometry as gxgm
import geosoft.gxpy.view as gxgrp
import geosoft.gxpy.grd as gxgrd
import geosoft.gxpy.agg as gxagg
import geosoft.gxpy.system as gxsys
import geosoft.gxpy.view as gxv
import geosoft.gxpy.group as gxg

from geosoft.gxpy.tests import GXPYTest


def rect_line(g, size=100):
    g.xy_rectangle(gxgm.Point2((0, 0, size, size), cs="cm"), pen=g.new_pen(line_thick=1))
    p1 = gxgm.Point((0.1, 0.1)) * size
    p2 = gxgm.Point((0.9, 0.9)) * size
    poff = gxgm.Point((0.15, 0.05)) * size
    g.xy_rectangle((p1, p2), pen=g.new_pen(fill_color=gxg.C_LT_GREEN))
    p12 = gxgm.Point2((p1 + poff, p2 - poff))
    g.xy_line((p12.p1.x, p12.p1.y, p12.p2.x, p12.p2.y), pen=g.new_pen(line_style=2, line_pitch=2.0))


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


def draw_stuff(g, size=1.0):
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
    g.pen = g.new_pen(line_style=2, line_pitch=2.0)
    g.xy_poly_line(pp)
    g.pen = g.new_pen(line_style=4, line_pitch=2.0, line_smooth=gxg.SMOOTH_AKIMA)
    g.xy_poly_line(pp)

    ppp = np.array(plinelist)
    pp = gxgm.PPoint(ppp[3:, :]) * size
    g.pen = g.new_pen(line_style=5, line_pitch=5.0,
                      line_smooth=gxg.SMOOTH_CUBIC,
                      line_color=gxg.C_RED,
                      line_thick=0.25,
                      fill_color=gxg.C_LT_BLUE)
    g.xy_poly_line(pp, close=True)

    g.pen = g.new_pen(fill_color=gxg.C_LT_GREEN)
    p1 = gxgm.Point((100, 0, 0)) * size
    p2 = gxgm.Point((100, 0, 0)) * size
    pp = (pp - p1) / 2 + p2
    g.xy_poly_line(pp, close=True)
    pp += gxgm.Point((0, 25, 0)) * size
    g.pen = g.new_pen(fill_color=gxg.C_LT_RED)
    g.xy_poly_line(pp, close=True)


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

    def test_lock(self):
        Test.start(self, gsys.func_name())

        with gxmap.GXmap.new(data_area=(0, 0, 50, 40), cs='cm') as map:
            with gxv.GXview(map, 'data') as v:
                self.assertFalse(bool(v.lock))
                with gxg.GXdraw(v, 'rectangle') as g:
                    self.assertTrue(bool(v.lock))
                    self.assertEqual(v.lock, 'rectangle')
                    self.assertRaises(gxg.GroupException, gxg.GXgroup, v)
                self.assertFalse(bool(v.lock))

    def test_rectangle(self):
        Test.start(self, gsys.func_name())

        with gxmap.GXmap.new(data_area=(0, 0, 50, 40), cs='cm') as map:
            map_file = map.file_name
            with gxv.GXview(map, 'data') as v:
                with gxg.GXdraw(v, 'rectangle') as g:
                    g.xy_rectangle(v.extent_clip, pen=g.new_pen(line_thick=0.5, line_color='B'))
                    g.xy_rectangle((2, 2, 48, 38),
                                   pen=g.new_pen(line_thick=0.25, line_color='R', line_style=gxg.LINE_STYLE_LONG,
                                                 line_pitch=5))

        self.crc_map(map_file)

    def test_smooth_line(self):
        Test.start(self, gsys.func_name())

        pp = pline()
        p1, p2 = pp.extent()
        area = (p1.x, p1.y, p2.x, p2.y)
        with gxmap.GXmap.new() as map:
            map_file = map.file_name
            with gxv.GXview(map, 'data', area=area, cs='mm') as v:
                with gxg.GXdraw(v) as g:
                    g.xy_rectangle(v.extent_clip)
                    g.xy_poly_line(pp, pen=g.new_pen(line_smooth=gxg.SMOOTH_AKIMA, line_color='r', line_thick=1))
                    g.xy_poly_line(pp, pen=g.new_pen(line_smooth=gxg.SMOOTH_CUBIC, line_color='b', line_thick=2))
                    g.xy_poly_line(pp)

        self.crc_map(map_file)

    def test_view_groups_1(self):
        Test.start(self, gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            map_file = gmap.file_name
            with gxv.GXview(gmap, "rectangle_test", area=(0, 0, 250, 125)) as v:
                with gxg.GXdraw(v, 'test_group') as g:
                    rect_line(g)
                    g.graticule(25, 20, style=gxg.GRATICULE_LINE)
                    g.pen = g.new_pen(line_thick=0.1)
                    g.xy_rectangle(((0, 0), (250, 125)), pen=g.new_pen(line_thick=0.1, line_color='R'))
            with gxv.GXview(gmap, "poly") as v:
                with gxg.GXdraw(v) as g:
                    draw_stuff(g)

        self.crc_map(map_file)
        gxmap.delete_files(map_file)

    def test_view_groups_2(self):
        Test.start(self, gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            map_file = gmap.file_name
            with gxv.GXview(gmap, "rectangle_test", area=(0, 0, 250, 125)) as v:
                with gxg.GXdraw(v, 'line') as g:
                    rect_line(g)
                with gxg.GXdraw(v, 'graticule') as g:
                    g.graticule(25, 20, style=gxg.GRATICULE_LINE)
                    g.pen = g.new_pen(line_thick=0.1)
                with gxg.GXdraw(v, 'test_rectangles') as g:
                    g.xy_rectangle(((0, 0), (250, 125)), pen=g.new_pen(line_thick=0.1, line_color='R'))
                    g.xy_rectangle(((10, 5), (240, 120)), pen=g.new_pen(line_thick=2, line_color='B'))
                v.delete_group('graticule')
            with gxv.GXview(gmap, "poly") as v:
                with gxg.GXdraw(v, 'test_group') as g:
                    draw_stuff(g)

        self.crc_map(map_file)
        gxmap.delete_files(map_file)

    def test_reopen_map_view(self):
        Test.start(self, gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            map_file = gmap.file_name
            with gxv.GXview(gmap, "test_view") as v:
                with gxg.GXdraw(v) as g:
                    rect_line(g)
            with gxv.GXview(gmap, "test_view") as v:
                pass
        gxmap.delete_files(map_file)

    def test_3D(self):
        Test.start(self, gsys.func_name())

        test3dv = os.path.join(self.gx.temp_folder(), "test.geosoft_3dv")
        testmap = os.path.join(self.gx.temp_folder(), "test.map")
        with gxmap.GXmap.new(test3dv, overwrite=True, no_data_view=True) as g3dv:
            with gxv.GXview3d(g3dv, mode=gxv.WRITE_NEW) as view_3d:
                with gxg.GXdraw_3d(view_3d, '2d_group') as g:
                    rect_line(g)
                    draw_stuff(g)
                    g.box_3d(((20, 10, 30), (80, 50, 50)), pen=g.new_pen(fill_color='R255G100B50'))

                with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
                    with gxv.GXview(gmap, "base") as view_base:
                        with gxg.GXdraw(view_base, 'Surround') as g:
                            g.xy_rectangle(((0, 0), (280, 260)))

                    gmap.create_linked_3d_view(view_3d, area=(10, 10, 270, 250))

        self.crc_map(test3dv, alt_crc_name=gxsys.func_name() + '_3dv')
        self.crc_map(testmap, alt_crc_name=gxsys.func_name() + '_map')

    def test_basic_drawing(self):
        Test.start(self, gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True, data_area=(0, 0, 25, 20), scale=100.0) as gmap:
            map_file = gmap.file_name
            with gxv.GXview(gmap, "my_base_view", area=(0, 0, 25, 20), scale=100.0) as v:
                with gxg.GXdraw(v, 'line') as g:
                    g.xy_rectangle(v.extent_clip, pen=g.new_pen(line_thick=0.1, line_color='R'))

            with gxv.GXview(gmap, "my_data_area", map_location=(4, 3), area=(0, 0, 1800, 1500), scale=10000) as v:
                with gxg.GXdraw(v, 'line') as g:
                    g.xy_rectangle(((0, 0), (1800, 1500)),
                                   pen=g.new_pen(line_thick=5, line_color='G'))

                    g.graticule(style=gxg.GRATICULE_LINE, pen=g.new_pen(line_thick=5))

            gmap.delete_view('*data')
            gmap.delete_view('*base')

        self.crc_map(map_file)

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
                             data_area=area, media="A4", margins=(0, 0, 0, 0),
                             cs=cs, overwrite=True) as gmap:
            map_file = gmap.file_name
            with gxv.GXview(gmap, "base") as v:
                with gxg.GXdraw(v, 'line') as g:
                    g.xy_rectangle(v.extent_clip, pen=g.new_pen(line_thick=1, line_color='K'))
            with gxv.GXview(gmap, "data") as v:
                with gxg.GXdraw(v, 'line') as g:
                    g.xy_rectangle(area, pen=g.new_pen(line_thick=0.1, line_color='R'))

                with gxagg.GXagg(grid_file) as agg:
                    with gxg.GXaggregate(v, agg) as g:
                        self.assertEqual(g.name, str(agg))

                self.assertEqual(len(v.group_list_agg), 1)

        self.crc_map(map_file)

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
                             data_area=area, media="A3", margins=(0, 0, 0, 0),
                             scale=(area[2] - area[0]) / 0.2,
                             cs=cs, overwrite=True) as gmap:
            map_file = gmap.file_name
            with gxv.GXview(gmap, "base") as v:
                with gxg.GXdraw(v, 'line') as g:
                    g.xy_rectangle(v.extent_clip, pen=g.new_pen(line_thick=2, line_color='K'))
            with gxv.GXview(gmap, "data") as v:
                with gxg.GXdraw(v, 'line') as g:
                    g.xy_rectangle(area, pen=g.new_pen(line_thick=0.1, line_color='G'))

                with gxagg.GXagg(grid_file) as agg:
                    gxg.GXaggregate(v, agg)

        self.crc_map(map_file)

    # Complete TODO in GXPYTest._agnosticize_and_ensure_consistent_line_endings
    def test_zone_grid(self):
        Test.start(self, gsys.func_name())

        def test_zone(zone, suffix, shade=False):
            map_file = os.path.join(self.gx.temp_folder(), "test_agg_" + suffix)
            with gxmap.GXmap.new(map_file, overwrite=True,
                                 data_area=(ex[0], ex[1], ex[2], ex[3]),
                                 scale=(ex[2] - ex[0]) / 0.2) as gmap:
                map_file = gmap.file_name
                with gxv.GXview(gmap, "data") as v:
                    with gxagg.GXagg(grid_file, zone=zone, shade=shade) as agg:
                        gxg.GXaggregate(v, agg)
                gmap.delete_view('base')

            self.crc_map(map_file, alt_crc_name='{}_{}'.format(gxsys.func_name(1), suffix))

        # test grid file
        folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                   folder=self.gx.temp_folder())

        with gxgrd.GXgrd(os.path.join(folder, 'test_agg_utm.grd')) as grd:
            ex = grd.extent_2d()
            grid_file = 'test_zone'
            gxgrd.delete_files(grid_file)
            test = grd.save_as(grid_file)
            grid_file = test.file_name
            test.close()

        test_zone(gxagg.ZONE_LINEAR, "linear_shade", shade=True)
        test_zone(gxagg.ZONE_EQUALAREA, "eq_area")
        test_zone(gxagg.ZONE_DEFAULT, "default")
        test_zone(gxagg.ZONE_LAST, "last")
        test_zone(gxagg.ZONE_LINEAR, "linear")
        test_zone(gxagg.ZONE_NORMAL, "normal")
        test_zone(gxagg.ZONE_SHADE, "shade")
        test_zone(gxagg.ZONE_LOGLINEAR, "log_linear")

        gxgrd.delete_files(grid_file)

    def test_text_definition(self):
        Test.start(self, gsys.func_name())

        t = gxg.Text_def()
        self.assertEqual(t.slant, 0)
        self.assertEqual(t.height, 0.25)
        self.assertEqual(t.weight, gxg.FONT_WEIGHT_MEDIUM)
        self.assertEqual(t.font, 'DEFAULT')
        t.font = "Arial"
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

        t.weight = gxg.FONT_WEIGHT_ULTRALIGHT
        self.assertAlmostEqual(t.line_thick, 0.005208333333333333)
        t.weight = gxg.FONT_WEIGHT_BOLD
        self.assertAlmostEqual(t.line_thick, 0.020833333333333331)
        thick = t.line_thick
        t.weight = gxg.FONT_WEIGHT_XXBOLD
        self.assertAlmostEqual(t.line_thick, 0.0625)
        t.line_thick = thick
        self.assertEqual(t.weight, gxg.FONT_WEIGHT_BOLD)
        t.height = 10.
        self.assertEqual(t.weight, gxg.FONT_WEIGHT_BOLD)
        self.assertAlmostEqual(t.line_thick, 0.8333333333333333)
        t.line_thick = t.line_thick
        self.assertEqual(t.weight, gxg.FONT_WEIGHT_BOLD)

    def test_colours(self):
        Test.start(self, gsys.func_name())

        c = gxg.Color((150, 200, 500))
        self.assertEqual(c.rgb, (150, 200, 255))
        c = gxg.Color((150, 200, 500), model=gxg.C_CMY)
        self.assertEqual(c.cmy, (150, 200, 255))

        c = gxg.Color('r255g128b56')
        self.assertEqual(c.rgb, (255, 128, 56))
        self.assertEqual(c.cmy, (0, 127, 199))
        c.rgb = (64, 32, 16)
        self.assertEqual(c.rgb, (64, 32, 16))
        c.cmy = (100, 200, 300)
        self.assertEqual(c.cmy, (100, 200, 255))

        c = gxg.Color((0, 127, 64), gxg.C_HSV)
        self.assertEqual(c.rgb, (191, 96, 96))

        c = gxg.Color(gxg.C_GREEN)
        self.assertEqual(c.rgb, (0, 255, 0))

        c2 = gxg.Color(c)
        self.assertEqual(c2.rgb, (0, 255, 0))

        c = gxg.Color(gxg.C_TRANSPARENT)
        self.assertEqual(c.rgb, None)
        self.assertEqual(c.cmy, None)
        self.assertTrue(c == gxg.Color(gxg.C_TRANSPARENT))

    def test_pen(self):
        Test.start(self, gsys.func_name())

        p = gxg.Pen()
        self.assertEqual(p.line_color.int, gxg.C_BLACK)
        self.assertEqual(p.fill_color.int, gxg.C_TRANSPARENT)
        self.assertEqual(p.line_style, gxg.LINE_STYLE_SOLID)

        p.line_color = (255, 127, 64)
        self.assertEqual(p.mapplot_string, 'r255g127b64t100')

        p = gxg.Pen.from_mapplot_string('r20b100k16R64K16')
        ms = p.mapplot_string
        self.assertEqual(ms, 'r4g0b84R48G0B0t1')
        p = gxg.Pen.from_mapplot_string(ms)
        self.assertEqual(p.mapplot_string, ms)

        p = gxg.Pen(line_color='K')
        self.assertEqual(p.line_color.int, gxg.C_BLACK)
        self.assertTrue(p.line_color == gxg.Color(gxg.C_BLACK))

        p = gxg.Pen(line_color=gxg.C_WHITE)
        self.assertEqual(p.line_color.int, gxg.C_WHITE)
        self.assertTrue(p.line_color == gxg.Color(gxg.C_WHITE))

        p = gxg.Pen.from_mapplot_string('r20b100k16R64K16')
        p = gxg.Pen(default=p, line_thick=0.05, fill_color='K')
        ms = p.mapplot_string
        self.assertEqual(ms, 'r4g0b84R0G0B0t500')
        p = gxg.Pen.from_mapplot_string(ms)
        self.assertEqual(p.mapplot_string, ms)

        self.assertRaises(gxg.GroupException, gxg.Pen, bad=1)

    def test_scaled(self):
        Test.start(self, gsys.func_name())

        p = gxg.Pen(factor=10)
        self.assertEqual(p.line_thick, 0.1)
        self.assertEqual(p.line_pitch, 5.0)
        self.assertEqual(p.pat_thick, 0.1)
        self.assertEqual(p.pat_size, 10.0)

        p = gxg.Pen(default=p, factor=5)
        self.assertEqual(p.line_thick, 0.5)
        self.assertEqual(p.line_pitch, 25.0)
        self.assertEqual(p.pat_thick, 0.5)
        self.assertEqual(p.pat_size, 50.0)

        t = gxg.Text_def(factor=0.2)
        self.assertEqual(t.height, 0.05)

    def test_text(self):
        Test.start(self, gsys.func_name())

        with gxmap.GXmap.new(data_area=(400000, 5000000, 500000, 5150000),
                             cs='WGS 84 / UTM zone 15N [geoid]') as map:
            map_file = map.file_name
            with gxv.GXview(map, 'base') as v:
                with gxg.GXdraw(v) as g:
                    g.xy_rectangle(g.extent)
                    g.text('Text on base view')
                    g.text('Bigger, blue, higher',
                           (v.units_per_map_cm, v.units_per_map_cm),
                           text_def=gxg.Text_def(height=20, color='B', font='Times New Roman'))
                    g.text('Bigger, blue, angled, italics',
                           (10, 25),
                           angle=60,
                           text_def=gxg.Text_def(height=20, color='B', font='Calibri', italics=True))

        self.crc_map(map_file)

    def test_text_1(self):
        Test.start(self, gsys.func_name())

        with gxmap.GXmap.new(data_area=(400000, 5000000, 500000, 5050000),
                             cs='WGS 84 / UTM zone 15N [geoid]') as map:
            map_file = map.file_name
            with gxv.GXview(map, '*data') as v:
                with gxg.GXdraw(v) as g:
                    g.xy_rectangle(g.extent)
                    ex = g.extent
                    width = ex[2] - ex[0]
                    height = ex[3] - ex[1]
                    cxy = (ex[0] + width / 2, ex[1] + height / 2)
                    td = gxg.Text_def(height=width / 20, color='K128', font='sr.gfn', weight=gxg.FONT_WEIGHT_XBOLD)
                    g.xy_rectangle(ex)
                    g.xy_line((ex[0], cxy[1], ex[2], cxy[1]))
                    g.xy_line((cxy[0], ex[1], cxy[0], ex[3]))
                    g.text('Centered',
                           cxy,
                           text_def=td,
                           reference=gxg.REF_CENTER)
                    g.text('Bottom',
                           (cxy[0], ex[1]),
                           text_def=td,
                           reference=gxg.REF_BOTTOM_CENTER)
                    g.text('Top',
                           (cxy[0], ex[3]),
                           text_def=td,
                           reference=gxg.REF_TOP_CENTER)
                    g.text('Left',
                           (ex[0], cxy[1]),
                           text_def=td,
                           angle=90,
                           reference=gxg.REF_TOP_CENTER)
                    g.text('Right',
                           (ex[2], cxy[1]),
                           text_def=td,
                           angle=-90,
                           reference=gxg.REF_TOP_CENTER)

        self.crc_map(map_file)

    def test_text_multiline(self):
        Test.start(self, gsys.func_name())

        with gxmap.GXmap.new(data_area=(400000, 5000000, 500000, 5050000),
                             cs='WGS 84 / UTM zone 15N [geoid]') as map:
            map_file = map.file_name
            with gxv.GXview(map, '*data') as v:
                with gxg.GXdraw(v) as g:
                    g.xy_rectangle(g.extent)
                    ex = v.extent_clip
                    width = ex[2] - ex[0]
                    height = ex[3] - ex[1]
                    cxy = (ex[0] + width / 2, ex[1] + height / 2)
                    td = gxg.Text_def(height=width / 20, color='K128', font='sr.gfn', weight=gxg.FONT_WEIGHT_XBOLD)
                    g.xy_rectangle(ex)
                    g.xy_line((ex[0], cxy[1], ex[2], cxy[1]))
                    g.xy_line((cxy[0], ex[1], cxy[0], ex[3]))
                    g.text('Centered\nline2\nand another',
                           cxy,
                           text_def=td,
                           reference=gxg.REF_CENTER)

        self.crc_map(map_file)

    def test_locate_group(self):
        Test.start(self, gsys.func_name())

        with gxmap.GXmap.new(data_area=(400000, 5000000, 500000, 5050000),
                             cs='WGS 84 / UTM zone 15N [geoid]') as map:
            map_file = map.file_name
            with gxv.GXview(map, '*data') as v:
                with gxg.GXdraw(v) as g:
                    g.xy_rectangle(v.extent_clip)
                    rect = gxgm.Point2((v.extent_clip[0], v.extent_clip[1],
                                        (v.extent_clip[2] + v.extent_clip[0]) * 0.5,
                                        (v.extent_clip[3] + v.extent_clip[1]) * 0.5))
                with gxg.GXdraw(v, 'a') as g:
                    g.xy_rectangle(rect)
                with gxg.GXdraw(v, 'b') as g:
                    g.xy_rectangle(rect, pen="b")
                    g.locate((450000, 5025000),
                             ref=gxg.REF_TOP_CENTER)

        self.crc_map(map_file)


if __name__ == '__main__':
    unittest.main()