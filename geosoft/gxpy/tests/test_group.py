import unittest
import os
import sys
import numpy as np

import geosoft
import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.geometry as gxgm
import geosoft.gxpy.view as gxgrp
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.agg as gxagg
import geosoft.gxpy.system as gxsys
import geosoft.gxpy.view as gxv
import geosoft.gxpy.group as gxg
import geosoft.gxpy.utility as gxu
import geosoft.gxpy.gdb as gxdb

from geosoft.gxpy.tests import GXPYTest


def rect_line(g, size=100):
    g.rectangle(gxgm.Point2((0, 0, size, size), cs="cm"), pen=g.new_pen(line_thick=1))
    p1 = gxgm.Point((0.1, 0.1)) * size
    p2 = gxgm.Point((0.9, 0.9)) * size
    poff = gxgm.Point((0.15, 0.05)) * size
    g.rectangle((p1, p2), pen=g.new_pen(fill_color=gxg.C_LT_GREEN))
    p12 = gxgm.Point2((p1 + poff, p2 - poff))
    g.line((p12.p0.x, p12.p0.y, p12.p1.x, p12.p1.y), pen=g.new_pen(line_style=2, line_pitch=2.0))


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
    g.polyline(pp)
    g.pen = g.new_pen(line_style=4, line_pitch=2.0, line_smooth=gxg.SMOOTH_AKIMA)
    g.polyline(pp)

    ppp = np.array(plinelist)
    pp = gxgm.PPoint(ppp[3:, :]) * size
    g.pen = g.new_pen(line_style=5, line_pitch=5.0,
                      line_smooth=gxg.SMOOTH_CUBIC,
                      line_color=gxg.C_RED,
                      line_thick=0.25,
                      fill_color=gxg.C_LT_BLUE)
    g.polygon(pp)

    g.pen = g.new_pen(fill_color=gxg.C_LT_GREEN)
    p1 = gxgm.Point((100, 0, 0)) * size
    p2 = gxgm.Point((100, 0, 0)) * size
    pp = (pp - p1) / 2 + p2
    g.polygon(pp)
    pp += gxgm.Point((0, 25, 0)) * size
    g.pen = g.new_pen(fill_color=gxg.C_LT_RED)
    g.polygon(pp)


class Test(GXPYTest):
    def test_version(self):
        self.start()
        self.assertEqual(gxmap.__version__, geosoft.__version__)

    def test_create(self):
        self.start()

    def test_lock(self):
        self.start()

        with gxmap.Map.new(data_area=(0, 0, 50, 40), cs='cm') as map:
            with gxv.View(map, 'data') as v:
                self.assertFalse(bool(v.lock))
                with gxg.Draw(v, 'rectangle') as g:
                    self.assertTrue(bool(v.lock))
                    self.assertEqual(v.lock, 'rectangle')
                    self.assertRaises(gxg.GroupException, gxg.Group, v)
                self.assertFalse(bool(v.lock))

    def test_rectangle(self):
        self.start()

        with gxmap.Map.new(data_area=(0, 0, 50, 40), cs='cm') as map:
            map_file = map.file_name
            with gxv.View(map, 'data') as v:
                with gxg.Draw(v, 'rectangle') as g:
                    g.rectangle(v.extent_clip, pen=g.new_pen(line_thick=0.5, line_color='B'))
                    g.rectangle((2, 2, 48, 38),
                                   pen=g.new_pen(line_thick=0.25, line_color='R', line_style=gxg.LINE_STYLE_LONG,
                                                 line_pitch=5))

        self.crc_map(map_file)

    def test_smooth_line(self):
        self.start()

        pp = pline()
        p1, p2 = pp.extent()
        area = (p1.x, p1.y, p2.x, p2.y)
        with gxmap.Map.new() as map:
            map_file = map.file_name
            with gxv.View(map, 'data', area=area, cs='mm') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip)
                    g.polyline(pp, pen=g.new_pen(line_smooth=gxg.SMOOTH_AKIMA, line_color='r', line_thick=1))
                    g.polyline(pp, pen=g.new_pen(line_smooth=gxg.SMOOTH_CUBIC, line_color='b', line_thick=2))
                    g.polyline(pp)

        self.crc_map(map_file)

    def test_view_groups_1(self):
        self.start()

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.Map.new(testmap, overwrite=True) as gmap:
            map_file = gmap.file_name
            with gxv.View(gmap, "rectangle_test", area=(0, 0, 250, 125)) as v:
                with gxg.Draw(v, 'test_group') as g:
                    rect_line(g)
                    g.graticule(25, 20, style=gxg.GRATICULE_LINE)
                    g.pen = g.new_pen(line_thick=0.1)
                    g.rectangle(((0, 0), (250, 125)), pen=g.new_pen(line_thick=0.1, line_color='R'))
            with gxv.View(gmap, "poly") as v:
                with gxg.Draw(v) as g:
                    draw_stuff(g)

        self.crc_map(map_file)
        gxmap.delete_files(map_file)

    def test_view_groups_2(self):
        self.start()

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.Map.new(testmap, overwrite=True) as gmap:
            map_file = gmap.file_name
            with gxv.View(gmap, "rectangle_test", area=(0, 0, 250, 125)) as v:
                with gxg.Draw(v, 'line') as g:
                    rect_line(g)
                with gxg.Draw(v, 'graticule') as g:
                    g.graticule(25, 20, style=gxg.GRATICULE_LINE)
                    g.pen = g.new_pen(line_thick=0.1)
                with gxg.Draw(v, 'test_rectangles') as g:
                    g.rectangle(((0, 0), (250, 125)), pen=g.new_pen(line_thick=0.1, line_color='R'))
                    g.rectangle(((10, 5), (240, 120)), pen=g.new_pen(line_thick=2, line_color='B'))
                v.delete_group('graticule')
            with gxv.View(gmap, "poly") as v:
                with gxg.Draw(v, 'test_group') as g:
                    draw_stuff(g)

        self.crc_map(map_file)
        gxmap.delete_files(map_file)

    def test_reopen_map_view(self):
        self.start()

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.Map.new(testmap, overwrite=True) as gmap:
            map_file = gmap.file_name
            with gxv.View(gmap, "test_view") as v:
                with gxg.Draw(v) as g:
                    rect_line(g)
            with gxv.View(gmap, "test_view") as v:
                pass
        gxmap.delete_files(map_file)

    def test_3D(self):
        self.start()

        testmap = os.path.join(self.gx.temp_folder(), "test.map")
        with gxmap.Map.new(testmap, overwrite=True) as gmap:
            with gxv.View(gmap, "base") as view_base:
                with gxg.Draw(view_base, 'Surround') as g:
                    g.rectangle(((0, 0), (280, 260)))

        test3dv = os.path.join(self.gx.temp_folder(), "test.geosoft_3dv")
        with gxv.View_3d.new(test3dv, overwrite=True) as view_3d:

            with gxg.Draw(view_3d, '2d_group') as g:
                rect_line(g)
                draw_stuff(g)

            with gxg.Draw_3d(view_3d, '3d_group_cylinders') as g:
                self.assertEqual(g.render_backfaces, False)
                g.cylinder_3d(((100, 10, 10), (120, 10, 10)), 8, pen='r', close=gxg.CYLINDER_CLOSE_ALL)
                g.cylinder_3d(((100, 10, 30), (120, 10, 30)), 8, pen='g', close=gxg.CYLINDER_CLOSE_START)
                g.cylinder_3d(((100, 10, 50), (120, 10, 50)), 8, pen='b', close=gxg.CYLINDER_CLOSE_END)
                g.cylinder_3d(((100, 10, 70), (120, 10, 70)), 8, pen='c', close=gxg.CYLINDER_OPEN)
                self.assertEqual(g.render_backfaces, True)

            with gxg.Draw_3d(view_3d, '3d_group') as g:
                g.cylinder_3d(((20, 10, 60), (80, 50, 80)), 5, pen='b')
                g.cone_3d(((20, 10, 80), (80, 50, 60)), 8, pen='g')
                g.cone_3d(((20, 50, 65), (20, 50, 40)), 30, pen='r')
                g.sphere((20, 50, 80), 10, pen='c')
                self.assertEqual(g.render_backfaces, False)
                g.cylinder_3d(((80, 10, 0), (80, 10, 80)), 5, pen='y', close=gxg.CYLINDER_OPEN)
                self.assertEqual(g.render_backfaces, True)
                g.box_3d(((20, 10, 30), (80, 50, 50)), pen=g.new_pen(line_color='R255G100B50'))

            with gxmap.Map.open(testmap) as gmap:
                gmap.create_linked_3d_view(view_3d, area_on_map=(10, 10, 270, 250))

        self.crc_map(test3dv, alt_crc_name=gxsys.func_name() + '_3dv')
        self.crc_map(testmap, alt_crc_name=gxsys.func_name() + '_map')

    def test_graticule(self):
        self.start()

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.Map.new(testmap, overwrite=True) as gmap:
            map_file = gmap.file_name
            gmap.delete_view('data')

            with gxv.View(gmap, "my_data_1", map_location=(2, 3), area=(0, 0, 1000, 1500), scale=10000) as v:
                with gxg.Draw(v, 'line') as g:
                    g.rectangle(v.extent_clip,
                                   pen=g.new_pen(line_thick=5, line_color='G'))

                    g.graticule(style=gxg.GRATICULE_LINE, pen=g.new_pen(line_thick=5))

            with gxv.View(gmap, "my_data_2", map_location=(15, 3), area=(0, 0, 1000, 1500), scale=10000) as v:
                with gxg.Draw(v, 'line') as g:
                    g.rectangle(v.extent_clip,
                                   pen=g.new_pen(line_thick=5, line_color='G'))
                    g.graticule(style=gxg.GRATICULE_DOT, pen=g.new_pen(line_thick=5))

            ex = gmap.extent_data_views()
            area = (0, 0, ex[2] + 2, ex[3] + 3)
            with gxv.View(gmap, "my_base_view", area=area, scale=100.0) as v:
                with gxg.Draw(v, 'base_edge') as g:
                    g.rectangle(v.extent_clip, pen=g.new_pen(line_thick=0.1, line_color='R'))
            gmap.delete_view('base')

        print(map_file)
        self.crc_map(map_file)

    def test_basic_grid_1(self):
        self.start()

        # test grid file
        folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                   folder=self.gx.temp_folder())
        grid_file = os.path.join(folder, 'test_agg_utm.grd')
        map_file = os.path.join(self.gx.temp_folder(), "test_agg_utm")

        with gxgrd.Grid(grid_file) as grd:
            cs = grd.cs
            area = grd.extent_2d()
        with gxmap.Map.new(map_file,
                             data_area=area, media="A4", margins=(0, 10, 0, 0),
                             cs=cs, overwrite=True) as gmap:
            map_file = gmap.file_name

            with gxv.View(gmap, "base") as v:
                with gxg.Draw(v, 'line') as g:
                    g.rectangle(v.extent_clip, pen=g.new_pen(line_thick=1, line_color='K'))

            with gxv.View(gmap, "data") as v:
                with gxg.Draw(v, 'line') as g:
                    g.rectangle(area, pen=g.new_pen(line_thick=0.1, line_color='R'))

                with gxagg.Aggregate_image.new(grid_file) as agg:
                    with gxg.Agg_group.new(v, agg) as gagg:
                        self.assertEqual(gagg.name, str(agg))

                self.assertEqual(len(v.group_list_agg), 1)

        self.crc_map(map_file)

    def test_basic_grid_2(self):
        self.start()

        # test grid file
        folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                   folder=self.gx.temp_folder())
        grid_file = os.path.join(folder, 'test_agg_utm.grd')
        map_file = os.path.join(self.gx.temp_folder(), "test_agg_utm")

        with gxgrd.Grid(grid_file) as grd:
            cs = grd.cs
            area = grd.extent_2d()
        with gxmap.Map.new(map_file,
                             data_area=area, media="A3", margins=(0, 0, 0, 0),
                             scale=(area[2] - area[0]) / 0.2,
                             cs=cs, overwrite=True) as gmap:
            map_file = gmap.file_name
            with gxv.View(gmap, "base") as v:
                with gxg.Draw(v, 'line') as g:
                    g.rectangle(v.extent_clip, pen=g.new_pen(line_thick=2, line_color='K'))
            with gxv.View(gmap, "data") as v:
                with gxg.Draw(v, 'line') as g:
                    g.rectangle(area, pen=g.new_pen(line_thick=0.1, line_color='G'))

                with gxagg.Aggregate_image.new(grid_file) as agg:
                    gxg.Agg_group.new(v, agg)

        self.crc_map(map_file)

    def test_zone_grid(self):
        self.start()

        def test_zone(zone, suffix, shade=False):
            map_file = os.path.join(self.gx.temp_folder(), "test_agg_" + suffix)
            with gxmap.Map.new(map_file, overwrite=True,
                                 data_area=(ex[0], ex[1], ex[2], ex[3]),
                                 scale=(ex[2] - ex[0]) / 0.2) as gmap:
                map_file = gmap.file_name
                with gxv.View(gmap, "data") as v:
                    with gxagg.Aggregate_image.new(grid_file, zone=zone, shade=shade) as agg:
                        gxg.Agg_group.new(v, agg)
                gmap.delete_view('base')

            self.crc_map(map_file, alt_crc_name='{}_{}'.format(gxsys.func_name(1), suffix))

        # test grid file
        folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                   folder=self.gx.temp_folder())

        with gxgrd.Grid(os.path.join(folder, 'test_agg_utm.grd')) as grd:
            ex = grd.extent_2d()
            grid_file = 'test_zone'
            gxgrd.delete_files(grid_file)
            with gxgrd.Grid.copy(grd, grid_file) as test:
                grid_file = test.file_name

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
        self.start()

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
        self.start()

        c = gxg.Color((150, 200, 500))
        self.assertEqual(c.rgb, (150, 200, 255))
        c = gxg.Color((150, 200, 500), model=gxg.CMODEL_CMY)
        self.assertEqual(c.cmy, (150, 200, 255))

        c = gxg.Color('r255g128b56')
        self.assertEqual(c.rgb, (255, 128, 56))
        self.assertEqual(c.cmy, (0, 127, 199))
        c.rgb = (64, 32, 16)
        self.assertEqual(c.rgb, (64, 32, 16))
        c.cmy = (100, 200, 300)
        self.assertEqual(c.cmy, (100, 200, 255))

        c = gxg.Color((0, 127, 64), gxg.CMODEL_HSV)
        self.assertEqual(c.rgb, (191, 96, 96))

        c = gxg.Color((0, 127, 64), gxg.CMODEL_RGB)
        self.assertEqual(c.rgb, (0, 127, 64))


        c = gxg.Color(gxg.C_GREEN)
        self.assertEqual(c.rgb, (0, 255, 0))

        c2 = gxg.Color(c)
        self.assertEqual(c2.rgb, (0, 255, 0))

        c = gxg.Color(gxg.C_TRANSPARENT)
        self.assertEqual(c.rgb, None)
        self.assertEqual(c.cmy, None)
        self.assertTrue(c == gxg.Color(gxg.C_TRANSPARENT))

    def test_pen(self):
        self.start()

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

        p = gxg.Pen.from_mapplot_string('c64K64')
        self.assertEqual(p.line_color.rgb, (191, 255, 255))
        self.assertEqual(p.fill_color.rgb, (191, 191, 191))

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
        self.start()

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
        self.start()

        with gxmap.Map.new(data_area=(400000, 5000000, 500000, 5150000),
                             cs='WGS 84 / UTM zone 15N [geoid]') as map:
            map_file = map.file_name
            with gxv.View(map, 'base') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(g.extent)
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
        self.start()

        with gxmap.Map.new(data_area=(400000, 5000000, 500000, 5050000),
                             cs='WGS 84 / UTM zone 15N [geoid]') as map:
            map_file = map.file_name
            with gxv.View(map, '*data') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(g.extent)
                    ex = g.extent
                    width = ex[2] - ex[0]
                    height = ex[3] - ex[1]
                    cxy = (ex[0] + width / 2, ex[1] + height / 2)
                    td = gxg.Text_def(height=width / 20, color='K128', font='sr.gfn', weight=gxg.FONT_WEIGHT_XBOLD)
                    g.rectangle(ex)
                    g.line((ex[0], cxy[1], ex[2], cxy[1]))
                    g.line((cxy[0], ex[1], cxy[0], ex[3]))
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
        self.start()

        with gxmap.Map.new(data_area=(400000, 5000000, 500000, 5050000),
                             cs='WGS 84 / UTM zone 15N [geoid]') as map:
            map_file = map.file_name
            with gxv.View(map, '*data') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(g.extent)
                    ex = v.extent_clip
                    width = ex[2] - ex[0]
                    height = ex[3] - ex[1]
                    cxy = (ex[0] + width / 2, ex[1] + height / 2)
                    td = gxg.Text_def(height=width / 20, color='K128', font='sr.gfn', weight=gxg.FONT_WEIGHT_XBOLD)
                    g.rectangle(ex)
                    g.line((ex[0], cxy[1], ex[2], cxy[1]))
                    g.line((cxy[0], ex[1], cxy[0], ex[3]))
                    g.text('Centered\nline2\nand another',
                           cxy,
                           text_def=td,
                           reference=gxg.REF_CENTER)

        self.crc_map(map_file)

    def test_locate_group(self):
        self.start()

        with gxmap.Map.new(data_area=(400000, 5000000, 500000, 5050000),
                             cs='WGS 84 / UTM zone 15N [geoid]') as map:
            map_file = map.file_name
            with gxv.View(map, '*data') as v:
                with gxg.Draw(v) as g:
                    g.rectangle(v.extent_clip)
                    rect = gxgm.Point2((v.extent_clip[0], v.extent_clip[1],
                                        (v.extent_clip[2] + v.extent_clip[0]) * 0.5,
                                        (v.extent_clip[3] + v.extent_clip[1]) * 0.5))
                with gxg.Draw(v, 'a') as g:
                    g.rectangle(rect)
                with gxg.Draw(v, 'b') as g:
                    self.assertEqual(g.number, 2)
                    g.rectangle(rect, pen="b")
                    g.locate((450000, 5025000),
                             reference=gxg.REF_TOP_CENTER)



        self.crc_map(map_file)

    def test_color_bar(self):
        self.start()

        # test grid file
        folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                   folder=self.gx.temp_folder())
        grid_file = os.path.join(folder, 'test_agg_utm.grd')
        map_file = os.path.join(self.gx.temp_folder(), "test_agg_utm")

        with gxgrd.Grid(grid_file) as grd:
            cs = grd.cs
            area = grd.extent_2d()
        with gxmap.Map.new(map_file, fixed_size=False,
                             data_area=area, media="A4", margins=(2, 10, 2, 1),
                             cs=cs, overwrite=True) as gmap:
            map_file = gmap.file_name
            with gxv.View(gmap, "base") as v:
                with gxg.Draw(v, 'line') as g:
                    g.rectangle(v.extent_clip, pen=g.new_pen(line_thick=1, line_color='K'))

            with gxv.View(gmap, "data") as v:
                with gxg.Draw(v, 'line') as g:
                    #g.rectangle(area, pen=g.new_pen(line_thick=0.1, line_color='R'))
                    g.rectangle(v.extent_clip, pen=g.new_pen(line_thick=0.1, line_color='G'))
                    g.rectangle(v.extent_all, pen=g.new_pen(line_thick=0.1, line_color='B'))

                with gxagg.Aggregate_image.new(grid_file) as agg:
                    itr = gxapi.GXITR.create()
                    agg.gxagg.get_layer_itr(0, itr)
                    gxg.legend_color_bar(v, 'color_legend', itr)

        self.crc_map(map_file)

    def test_color_bar_existing_agg(self):
        self.start()

        # test grid file
        folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                   folder=self.gx.temp_folder())
        grid_file = os.path.join(folder, 'test_agg_utm.grd')
        map_file = os.path.join(self.gx.temp_folder(), "test_agg_utm")

        with gxgrd.Grid(grid_file) as grd:
            cs = grd.cs
            area = grd.extent_2d()
        with gxmap.Map.new(map_file, fixed_size=False,
                             data_area=area, media="A4", margins=(2, 10, 2, 1),
                             cs=cs, overwrite=True) as gmap:
            map_file = gmap.file_name
            with gxv.View(gmap, "base") as v:
                with gxg.Draw(v, 'line') as g:
                    g.rectangle(v.extent_clip, pen=g.new_pen(line_thick=1, line_color='K'))

            with gxv.View(gmap, "data") as v:
                with gxg.Draw(v, 'line') as g:
                    g.rectangle(v.extent_clip, pen=g.new_pen(line_thick=0.1, line_color='G'))
                    g.rectangle(v.extent_all, pen=g.new_pen(line_thick=0.1, line_color='B'))

                with gxagg.Aggregate_image.new(grid_file) as agg:
                    with gxg.Agg_group.new(v, agg) as g:
                        agg_group_name = g.name

            with gxv.View(gmap, "data") as v:
                with gxg.Agg_group.open(v, agg_group_name) as g:
                    itr = gxapi.GXITR.create()
                    g.agg.gxagg.get_layer_itr(0, itr)
                    gxg.legend_color_bar(v, 'color_legend', itr)


        self.crc_map(map_file)


    def test_properties(self):
        self.start()

        with gxmap.Map.new() as map:
            with gxv.View(map, "base") as v:
                with gxg.Draw(v, 'edge') as g:
                    g.rectangle(v.extent_clip, pen=g.new_pen(line_thick=1, line_color='K'))
            with gxv.View(map, "data") as v:
                with gxg.Draw(v, 'edge') as g:
                    g.rectangle(v.extent_clip, pen=g.new_pen(line_thick=1, line_color='B'))
                    self.assertTrue(g.visible)
                    g.visible = False
                    self.assertFalse(g.visible)

    def test_graticule(self):
        self.start()

        test_map = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.Map.new(test_map, overwrite=True) as map:
            map_file = map.file_name
            map.delete_view('data')

            with gxv.View(map, "my_data_1", map_location=(2, 3), area=(0, 0, 1000, 1500), scale=10000) as v:
                with gxg.Draw(v, 'line') as g:
                    g.rectangle(v.extent_clip,
                                   pen=g.new_pen(line_thick=5, line_color='G'))

                    g.graticule(style=gxg.GRATICULE_LINE, pen=g.new_pen(line_thick=5))
                ex1 = v.extent_group('line', unit=gxv.UNIT_MAP)

            with gxv.View(map, "my_data_2", map_location=(15, 3), area=(0, 0, 1000, 1500), scale=10000) as v:
                with gxg.Draw(v, 'line') as g:
                    g.rectangle(v.extent_clip,
                                   pen=g.new_pen(line_thick=5, line_color='G'))

                    g.graticule(style=gxg.GRATICULE_DOT, pen=g.new_pen(line_thick=5))
                ex2 = v.extent_group('line', unit=gxv.UNIT_MAP)

            with gxv.View(map, "my_data_3", map_location=(28, 3), area=(0, 0, 1000, 1500), scale=10000) as v:
                with gxg.Draw(v, 'line') as g:
                    g.rectangle(v.extent_clip,
                                   pen=g.new_pen(line_thick=5, line_color='G'))

                    g.graticule(style=gxg.GRATICULE_CROSS, pen=g.new_pen(line_thick=5))
                ex3 = v.extent_group('line', unit=gxv.UNIT_MAP)

            area = (min(ex1[0], ex2[0], ex3[0])/10.0 - 2, max(ex1[1], ex2[1], ex3[1])/10.0 - 2,
                    max(ex1[2], ex2[2], ex3[2])/10.0 + 2, max(ex1[3], ex2[3], ex3[3])/10.0 + 2)
            with gxv.View(map, "my_base_view", area=area, scale=100.0) as v:
                with gxg.Draw(v, 'base_edge') as g:
                    g.rectangle(v.extent_clip, pen=g.new_pen(line_thick=0.1, line_color='R'))
            map.delete_view('base')

        self.crc_map(map_file)

    def test_ppoint_3d(self):
        self.start()
        
        plist = [[110, 5, 0],
                 [120, 20, 10],
                 [130, 15, 50],
                 [150, 50, 20],
                 [160, 70, 0],
                 [175, 35, 30],
                 [190, 65, 80],
                 [220, 50, 90],
                 [235, 18.5, 100]]
        pp = gxgm.PPoint(plist)
        with gxv.View_3d.new(gxsys.func_name(), overwrite=True) as v:
            file_name = v.file_name
            with gxg.Draw_3d(v) as g:
                g.pen = gxg.Pen(line_color='R')
                g.polypoint_3d(pp)
                pp += (0, 0, 20)
                g.polypoint_3d(pp, style=gxg.POINT_STYLE_SPHERE, pen=gxg.Pen(line_color='G', line_thick=5))

        self.crc_map(file_name)
        gxmap.delete_files(file_name)

    def test_pp_3d(self):
        self.start()

        plist = [[110, 5, 0],
                 [120, 20, 10],
                 [130, 15, 50],
                 [150, 50, 20],
                 [160, 70, 0],
                 [175, 35, 30],
                 [190, 65, 80],
                 [220, 50, 90],
                 [235, 18.5, 100]]
        with gxv.View_3d.new(gxsys.func_name(), overwrite=True) as v:
            file_name = v.file_name
            with gxg.Draw_3d(v) as g:
                pp = gxgm.PPoint(plist)

                g.pen = gxg.Pen(line_color='R')
                g.polypoint_3d(pp)

                pp += (0, 0, 10)
                g.polypoint_3d(pp, style=gxg.POINT_STYLE_SPHERE, pen=gxg.Pen(line_color='G', line_thick=4))

                pp += (0, 0, 10)
                g.pen = gxg.Pen(line_color='R')
                g.polyline_3d(pp)

                pp += (0, 0, 10)
                g.pen = gxg.Pen(line_color='C', line_thick=3)
                g.polyline_3d(pp, style=gxg.LINE3D_STYLE_TUBE)

                pp += (0, 0, 10)
                g.polyline_3d(pp, style=gxg.LINE3D_STYLE_TUBE_JOINED, pen=gxg.Pen(line_color='K64', line_thick=4))

        self.crc_map(file_name)
        gxmap.delete_files(file_name)

    def test_color_map(self):
        self.start()

        cm = gxg.Color_map()
        self.assertEqual(cm.length, 39)
        self.assertFalse(cm.initialized)

        cm = gxg.Color_map(16)
        self.assertEqual(cm.length, 16)
        self.assertEqual(cm[0][1], gxg.Color(gxg.C_BLACK))
        self.assertEqual(cm[cm.length-1], (None, gxg.Color(gxg.C_BLACK)))
        cm[4] = (cm[4][0], gxg.Color(gxg.C_GREEN))
        self.assertEqual(cm[4][1].rgb, (0, 255, 0))
        self.assertFalse(cm.initialized)

        self.assertTrue(isinstance(cm.gxitr, gxapi.GXITR))

        cm = gxg.Color_map('grey')
        self.assertFalse(cm.initialized)
        cm.set_sequential()
        self.assertTrue(cm.initialized)
        self.assertEqual(cm.length, 32)
        self.assertEqual(cm[0][1].rgb, (31, 31, 31))
        self.assertEqual(cm[cm.length-1][1].rgb, (255, 255, 255))
        self.assertEqual(cm.color_of_value(0), cm[0][1])
        self.assertEqual(cm.color_of_value(7.0), cm[7][1])
        self.assertEqual(cm.color_of_value(7.000001), cm[8][1])

        self.assertEqual(cm.brightness, 0.)
        cm.brightness = 0.5
        self.assertEqual(cm.brightness, 0.5)
        self.assertEqual(cm[0][1].rgb, (143, 143, 143))
        self.assertEqual(cm[cm.length - 1][1].rgb, (255, 255, 255))
        cm.brightness = -0.25
        self.assertEqual(cm.brightness, -0.25)
        self.assertEqual(cm[0][1].rgb, (24, 24, 24))
        self.assertEqual(cm[cm.length - 1][1].rgb, (192, 192, 192))
        cm.brightness = 0
        self.assertEqual(cm[0][1].rgb, (31, 31, 31))
        self.assertEqual(cm[cm.length - 1][1].rgb, (255, 255, 255))

        cm.set_linear(4, 45)
        self.assertEqual(cm.length, 32)
        self.assertEqual(cm[0][0], 4)
        self.assertEqual(cm[30][0], 45)

        cm.set_linear(4, 45, inner_limits=False)
        self.assertEqual(cm.length, 32)
        self.assertEqual(cm[0][0], 5.28125)
        self.assertEqual(cm[30][0], 43.71875)

        cm.set_linear(5, 50, contour_interval=5)
        self.assertEqual(cm.length, 11)

        cm = gxg.Color_map('grey')
        cm.set_logarithmic(0.0001,1000)
        self.assertEqual(cm.length, 32)
        cm.set_logarithmic(0.0001,1000, contour_interval=10)
        self.assertEqual(cm.length, 7)
        cm = gxg.Color_map('grey')
        cm.set_logarithmic(0.000023,18000, contour_interval=100)
        self.assertEqual(cm.length, 5)

        cm = gxg.Color_map()
        cm.set_normal(25, 55000)
        self.assertAlmostEqual(cm[cm.length//2][0], 55000.811582690316)

        itr = cm.save_file()
        cm2 = gxg.Color_map(itr)
        self.assertTrue(cm == cm2)
        tbl = gxg.Color_map().save_file()
        self.assertEqual(os.path.splitext(tbl)[1], '.tbl')
        cm = gxg.Color_map(tbl)
        self.assertFalse(cm.initialized)

    def test_color_symbols(self):
        self.start()

        data = [((0, 0), 1),
                ((10, 0), 2),
                ((0, 10), 3),
                ((10, 10), 4)]
        data2 = [((0, 0, 45), 1, 4),
                 ((10, 0, 8), None, None),
                 ((0, 10, 16), 3, 75),
                 ((None, 10, -22), 4, 7)]

        cmap = gxg.Color_map()
        cmap.set_linear(0, 5, contour_interval=1)

        with gxmap.Map.new(data_area=(-1, -1, 11, 11), scale=100) as map:
            map_file = map.file_name
            with gxv.View(map, '*data') as v:

                with gxg.Draw(v) as g:
                    g.rectangle(g.extent)

                gxg.Color_symbols_group.new(v, 'outer_symbols', data, cmap)
                cmap = gxg.Color_map('hotcycle')
                cmap.set_linear(0, 5, contour_interval=1)
                gxg.Color_symbols_group.new(v, 'mark', data2, cmap,
                                            symbol=gxg.SYMBOL_BOX,
                                            symbol_def=gxg.Text_def(font='symbols.gfn',
                                                                    height=0.15,
                                                                    color=gxg.C_WHITE,
                                                                    weight=gxg.FONT_WEIGHT_ULTRALIGHT))

                cs = gxg.Color_symbols_group.open(v, 'mark')
                self.assertEqual(cs.number, 2)

        self.crc_map(map_file)

    def test_polydata_3d(self):
        self.start()

        def render_spheres(item, cmap_radius):
            xyz, value = item
            if None in xyz or value is None:
                return None
            cmap, radius = cmap_radius
            cint = cmap.color_of_value(value)
            return xyz, gxg.SYMBOL_3D_SPHERE, cint.int, (radius,)

        data = [((0, 0, 0), 1),
                ((10, 0, 5), 2),
                ((0, 10, -5), 3),
                ((0, None, -5), 99),
                ((0, 10, -5), None),
                ((10, 10, 10), 4)]

        cmap = gxg.Color_map()
        cmap.set_linear(0, 5, contour_interval=1)

        with gxv.View_3d.new(area_2d=(-1, -1, 11, 11)) as v:
            v3d_file = v.file_name

            with gxg.Draw(v, 'rect') as g:
                g.rectangle((0,0,10,10),
                            pen=gxg.Pen(line_color=gxg.C_BLACK,
                                        line_thick=0.2,
                                        fill_color=gxg.C_GREEN))

            with gxg.Draw_3d(v, 'pipes') as g:
                g.polyline_3d(((0,0,0), (10,0,0), (10,10,0), (0,10,0), (0,0,0)),
                              style=gxg.LINE3D_STYLE_TUBE_JOINED,
                              pen=gxg.Pen(line_color=gxg.C_GREY,
                                          line_thick=0.2))

            with gxg.Draw_3d(v, 'outer') as g:
                g.polydata_3d(data, render_spheres, (cmap, 0.25))

        self.crc_map(v3d_file)

    def test_polydata_3d_grid(self):
        self.start()

        def render_spheres(item, cmap_radius):
            value = item[3]
            cmap, radius = cmap_radius
            if gxu.is_nan(value):
                xyz = (item[0], item[1], item[2])
                return xyz, gxg.SYMBOL_3D_SPHERE, gxg.Color(gxg.C_GREY10).int, (radius*0.5,)
            xyz = (item[0], item[1], item[2])
            cint = cmap.color_of_value(value)
            return xyz, gxg.SYMBOL_3D_SPHERE, cint.int, (radius,)

        # test grid file
        folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                   folder=self.gx.temp_folder())

        grid_file = os.path.join(folder, 'test_agg_utm.grd')
        with gxgrd.Grid(grid_file) as grd:

            # orient the grid just to make it look interesting
            gxf = grd.cs.gxf
            gxf[0] += ' <0,0,0,0,45,25>'
            grd.x0 = 0
            grd.y0 = 0
            grd.cs = gxf

            data = grd.xyzv()

            cmap = gxg.Color_map()
            try:
                std = np.nanstd(data[:, :, 3])
                mean = np.nanmean(data[:, :, 3])
                cmap.set_normal(std, mean)
            except:
                cmap.set_linear(0,1)

            with gxv.View_3d.new(cs=grd.cs) as v:
                v3d_file = v.file_name
                with gxg.Draw_3d(v, 'outer') as g:
                    g.polydata_3d(data.reshape((-1,4)), render_spheres, (cmap, grd.dx * 0.25))
                    g.box_3d(grd.extent_3d(), wireframe=True, pen=gxg.Pen(line_color='b', line_thick=grd.dx))

        self.crc_map(v3d_file)

    def test_polydata_3d_gdb(self):
        self.start()

        def render_spheres(item, cmap_radius):
            cmap, radius = cmap_radius
            if not gxu.is_nan(item[2]):
                cint = cmap.color_of_value(item[2]).int
                return item, gxg.SYMBOL_3D_SPHERE, cint, (radius,)

        folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'dem.zip'),
                                   folder=self.gx.temp_folder())

        gdb_file = os.path.join(folder, 'dem')
        with gxdb.Geosoft_gdb.open(gdb_file) as gdb:
            gdb.xyz_channels = ('x', 'y', 'elevation')

            data = None
            for l in gdb.lines():
                dataline = gxu.dummy_to_nan(gdb.read_line(l, channels=('x', 'y', 'elevation'))[0])
                if data is None:
                    data = dataline
                else:
                    data = np.append(data, dataline, axis=0)

            data *= (1, 1, 10)
            cmap = gxg.Color_map()
            try:
                std = np.nanstd(data[:, 2])
                mean = np.nanmean(data[:, 2])
                cmap.set_normal(std, mean)
            except:
                cmap.set_linear(0, 1)

            with gxv.View_3d.new(cs=gdb.coordinate_system) as v:
                v3d_file = v.file_name
                with gxg.Draw_3d(v, 'outer') as g:
                    g.polydata_3d(data.reshape((-1, 3)), render_spheres, (cmap, 50 * v.units_per_map_cm))
                    g.box_3d(gdb.extent_xyz(),
                             wireframe=True,
                             pen=gxg.Pen(line_color='b', line_thick=0.25 * v.units_per_map_cm))

        self.crc_map(v3d_file)

if __name__ == '__main__':
    unittest.main()