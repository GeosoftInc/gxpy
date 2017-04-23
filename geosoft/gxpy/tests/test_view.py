import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.view as gxv
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.group as gxg
import geosoft.gxpy.geometry as gxgm

from geosoft.gxpy.tests import GXPYTest

def draw_2d_stuff(g, size=1.0):
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

        with gxmap.GXmap.new() as gmap:
            vlist = gmap.view_list
            self.assertEqual(len(vlist), 2)
            self.assertTrue('base' in vlist)
            self.assertTrue('data' in vlist)
            with gxv.GXview(gmap, 'base') as v:
                self.assertEqual(v.name, "base")
                self.assertEqual(v.scale, 1000.0)
                self.assertEqual(v.aspect, 1.0)
                self.assertEqual(v.units_name, 'unknown')
                self.assertEqual(v.units_per_metre, 1.0)
                self.assertEqual(v.units_per_map_cm, 10.0)

            with gxv.GXview(gmap, 'ft12000', cs='ft', scale=12000,
                            area=(0, 0, 50000, 40000)) as v:
                self.assertEqual(v.name, "ft12000")
                self.assertAlmostEqual(v.scale, 12000.0)
                self.assertAlmostEqual(v.aspect, 1.0)
                self.assertEqual(v.units_name, 'ft')
                self.assertAlmostEqual(v.units_per_metre, 3.280839895)
                self.assertAlmostEqual(v.units_per_map_cm, 393.7007874)

            with gxv.GXview(gmap) as vw:
                self.assertEqual(vw.name, "_unnamed_view")
                self.assertEqual(vw.scale, 100.0)
                self.assertEqual(vw.aspect, 1.0)
                self.assertEqual(vw.units_name, 'unknown')
                self.assertEqual(vw.units_per_metre, 1.0)

        with gxmap.GXmap.new() as gmap:
            with gxv.GXview(gmap, "test") as vw:
                self.assertEqual(vw.name, "test")

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

    def test_scale(self):
        self.start()

        with gxmap.GXmap.new() as gmap:
            with gxv.GXview(gmap, 'ft12000',
                            cs='ft', scale=12000,
                            map_location=(10, 5),
                            area=(0, 0, 50000, 40000)) as v:

                vmin = (v.extent_clip[0], v.extent_clip[1])
                self.assertEqual(v.view_to_map_cm(vmin), (10.0, 5.0))

                vmax = v.view_to_map_cm(v.extent_clip[2], v.extent_clip[3])
                mmax = v.map_cm_to_view(vmax)
                self.assertEqual(mmax, (50000.0, 40000.0))

    def test_reopen_map_view(self):
        self.start()

        testmap = os.path.join(self.gx.temp_folder(), "test_view_reopen_map_view")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            mapfile = gmap.file_name
            with gxv.GXview(gmap, "test_view") as v:
                with gxg.GXdraw(v) as g:
                    g.rectangle(v.extent_clip)
            with gxv.GXview(gmap, "test_view") as v:
                pass
        gxmap.delete_files(mapfile)

    def test_cs(self):
        self.start()

        testmap = os.path.join(self.gx.temp_folder(), "test_view_cs")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            with gxv.GXview(gmap, "rectangle_test", cs="wgs 84") as v:
                self.assertEqual("WGS 84", str(v.cs))
            with gxv.GXview(gmap, "vcs", cs="wgs 84 / UTM zone 15N [special]") as v:
                self.assertTrue("WGS 84 / UTM zone 15N [special]" in str(v.cs))

    def test_3dview(self):
        self.start()

        v3d_file = None

        try:

            with gxv.GXview_3d.new('test_3d', overwrite=True) as v:
                v3d_file = v.file_name
                self.assertTrue(v3d_file.lower().endswith('.geosoft_3dv'))
                self.assertEqual(v.name, 'test_3d')
                self.assertEqual(v.map.name, 'test_3d')

                with gxg.GXdraw(v, '2D stuff') as g:
                    g.rectangle(v.extent_clip)
                    draw_2d_stuff(g)

                self.assertRaises(gxv.ViewException, v.new_drawing_plane, 0)
                v.new_drawing_plane('vertical', rotation=(90.0, 0, 0))
                with gxg.GXdraw(v, '2D stuff vertical', plane='vertical') as g:
                    g.rectangle(v.extent_clip)
                    draw_2d_stuff(g)

                self.assertEqual(v.current_3d_drawing_plane, 'vertical')
                with gxg.GXdraw_3d(v, '3D stuff') as g:
                    g.box_3d(((20, 10, -10), (80, 50, 30)), pen=g.new_pen(line_color='R255G100B50'))
                self.assertEqual(v.current_3d_drawing_plane, 'plane_0')

                self.assertEqual(len(v.plane_list), 2)
                self.assertEqual(v.plane_number('plane_0'), 0)
                self.assertEqual(v.plane_number('vertical'), 1)
                self.assertEqual(v.plane_name('vertical'), 'vertical')
                self.assertEqual(v.plane_name(1), 'vertical')
                self.assertRaises(gxv.ViewException, v.plane_number, 'bogus')
                self.assertRaises(gxv.ViewException, v.plane_number, -1)
                self.assertRaises(gxv.ViewException, v.plane_name, 2)
                self.assertRaises(gxv.ViewException, v.plane_name, 'bogus')

            self.crc_map(v3d_file)

        except:
            raise

        finally:
            if v3d_file:
                gxmap.delete_files(v3d_file)

    def test_3d_map(self):
        self.start()

        v3d_file = None
        map_file = None
        try:

            with gxmap.GXmap.new() as map:
                map_file = map.file_name
                with gxv.GXview(map, '*base') as v:
                    with gxg.GXdraw(v, 'edge') as g:
                        g.rectangle(v.extent_clip)

            with gxv.GXview_3d.new('test_3d', overwrite=True) as v:
                v3d_file = v.map.file_name
                with gxg.GXdraw(v, '2D stuff') as g:
                    draw_2d_stuff(g)
                v.new_drawing_plane('vertical', rotation=(90.0, 0, 0))
                with gxg.GXdraw(v, '2D stuff vertical', plane='vertical') as g:
                    g.rectangle(v.extent_clip)
                    draw_2d_stuff(g)

                with gxg.GXdraw_3d(v, '3D stuff') as g:
                    g.box_3d(((20, 10, -10), (80, 50, 30)), pen=g.new_pen(line_color='R255G100B50'))

                with gxmap.GXmap.open(map_file) as map:
                    map.create_linked_3d_view(v, 'linked_view')

            #TODO this fails in batch, but not in interactive.
            self.crc_map(map_file)

        finally:
            if v3d_file:
                gxmap.delete_files(v3d_file)
            if map_file:
                gxmap.delete_files(map_file)

    def test_3d_open(self):
        self.start()

        v3d_file = None
        try:

            with gxv.GXview_3d.new('test_3d', overwrite=True) as v:
                v3d_file = v.map.file_name
                with gxg.GXdraw(v, '2D stuff') as g:
                    draw_2d_stuff(g)

            self.assertRaises(gxv.ViewException, gxv.GXview_3d.open, 'bogus')

            with gxv.GXview_3d.open(v3d_file) as v:
                v.new_drawing_plane('vertical', rotation=(90.0, 0, 0))
                with gxg.GXdraw(v, '2D stuff vertical', plane='vertical') as g:
                    g.rectangle(v.extent_clip)
                    draw_2d_stuff(g)

                with gxg.GXdraw_3d(v, '3D stuff') as g:
                    g.box_3d(((20, 10, -10), (80, 50, 30)), pen=g.new_pen(line_color='R255G100B50'))

            self.crc_map(v3d_file)

        except:
            raise

        finally:
            if v3d_file:
                gxmap.delete_files(v3d_file)

if __name__ == '__main__':

    unittest.main()
