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
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.grd as gxgrd
import geosoft.gxpy.agg as gxagg


def rect_line(view, size=100):
    view.xy_rectangle(gxgm.Point2((0, 0, size, size)), pen={'line_thick': 1})
    p1 = gxgm.Point((0.1, 0.1)) * size
    p2 = gxgm.Point((0.9, 0.9)) * size
    poff = gxgm.Point((0.15, 0.05)) * size
    view.xy_rectangle((p1, p2), pen={'fill_color': gxapi.C_LT_GREEN})
    p12 = gxgm.Point2((p1 + poff, p2 - poff))
    #view.xy_line(p12, pen={'line_style': (2, 2.0)}) # following form tests p2 construction from 4 values
    view.xy_line((p12.p1.x, p12.p1.y, p12.p2.x, p12.p2.y), pen={'line_style': (2, 2.0)})


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
    view.pen = {'line_style': (2, 2.0)}
    view.xy_poly_line(pp)
    view.pen = {'line_style': (4, 2.0), 'line_smooth': gxv.SMOOTH_AKIMA}
    view.xy_poly_line(pp)

    ppp = np.array(plinelist)
    pp = gxgm.PPoint(ppp[3:, :]) * size
    view.pen = {'line_style': (5, 5.0),
                  'line_smooth': gxv.SMOOTH_CUBIC,
                  'line_color': gxapi.C_RED,
                  'line_thick': 0.25,
                  'fill_color': gxapi.C_LT_BLUE}
    view.xy_poly_line(pp, close=True)

    view.pen = {'fill_color': gxapi.C_LT_GREEN}
    p1 = gxgm.Point((100, 0, 0)) * size
    p2 = gxgm.Point((100, 0, 0)) * size
    pp = (pp - p1) / 2 + p2
    view.xy_poly_line(pp, close=True)
    pp += gxgm.Point((0, 25, 0)) * size
    view.pen = {'fill_color': gxapi.C_LT_RED}
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
        cls.gx.log("*** {} > {}".format(os.path.split(__file__)[1], test))

    def view_crc(self, mapfile, crc=None, display=False):
        if display:
            gxvwr.map(mapfile)
        if crc:
            self.assertEqual(gxmap.crc_map(mapfile), crc)

    def test_version(self):
        self.start(gsys.func_name())
        self.assertEqual(gxmap.__version__, geosoft.__version__)

    def test_create(self):
        self.start(gsys.func_name())

        with gxmap.GXmap.new() as gmap:
            with gxv.GXview(gmap) as vw:
                self.assertEqual(vw.viewname, "_unnamed_view")

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
                self.assertEqual(vw.extent(), area)
                self.assertEqual(vw.extent(gxv.EXTENT_MAP), (0, 0, xcm, ycm))
                self.assertEqual(vw.scale(), (scale, scale))
                self.assertTrue(vw.cs.same_as(gxcs.GXcs("WGS 84 / UTM zone 34N")))
                self.assertEqual(vw.units_per_m, 1.0)
                self.assertEqual(vw.unit_name, 'm')

        with gxmap.GXmap.new() as gmap:
            area = (100, 500, 15100, 10500)
            scale = 12000
            loc = (7.5, 2.0)
            mpu = 1.0 / float(gxcs.parameters(gxcs.PARM_UNITS, 'ftUS')['FACTOR'])
            xcm = 100.0 * ((area[2] - area[0]) / scale) / mpu
            ycm = 100.0 * ((area[3] - area[1]) / scale) / mpu
            with gxv.GXview(gmap, "test", map_location=loc, area=area,
                            scale=scale, cs=("WGS 84 / UTM zone 34N", '', '', 'ftUS', '')) as vw:
                self.assertEqual(vw.extent(), area)
                mx = vw.extent(gxv.EXTENT_MAP)
                self.assertAlmostEqual(mx[0], loc[0])
                self.assertAlmostEqual(mx[1], loc[1])
                self.assertAlmostEqual(mx[2], loc[0] + xcm)
                self.assertAlmostEqual(mx[3], loc[1] + ycm)
                self.assertAlmostEqual(vw.scale()[0], scale)
                self.assertAlmostEqual(vw.scale()[1], scale)
                self.assertFalse(vw.cs.same_as(gxcs.GXcs("WGS 84 / UTM zone 34N")))
                self.assertTrue(vw.cs.same_as(gxcs.GXcs(("WGS 84 / UTM zone 34N", '', '', 'ftUS', ''))))
                self.assertAlmostEqual(vw.units_per_m, 3.28083333333334)
                self.assertEqual(vw.unit_name, 'ftUS')

        with gxmap.GXmap.new() as gmap:
            area = (100, 500, 15100, 10500)
            scale = 12000
            loc = (7.5, 2.0)
            mpu = 1.0 / float(gxcs.parameters(gxcs.PARM_UNITS, 'ftUS')['FACTOR'])
            xcm = 100.0 * ((area[2] - area[0]) / scale) / mpu
            ycm = 100.0 * ((area[3] - area[1]) / scale) / mpu
            with gxv.GXview(gmap, "test", map_location=loc, area=area,
                            scale=scale, cs='ftUS') as vw:
                self.assertEqual(vw.extent(), area)
                mx = vw.extent(gxv.EXTENT_MAP)
                self.assertAlmostEqual(mx[0], loc[0])
                self.assertAlmostEqual(mx[1], loc[1])
                self.assertAlmostEqual(mx[2], loc[0] + xcm)
                self.assertAlmostEqual(mx[3], loc[1] + ycm)
                self.assertAlmostEqual(vw.scale()[0], scale)
                self.assertAlmostEqual(vw.scale()[1], scale)
                self.assertTrue(vw.cs.same_as(gxcs.GXcs(('', '', '', 'ftUS', ''))))
                self.assertAlmostEqual(vw.units_per_m, 3.28083333333334)
                self.assertEqual(vw.unit_name, 'ftUS')

        with gxmap.GXmap.new() as gmap:
            with gxv.GXview(gmap, "test", area=(100, 500, 15100, 10500), scale=(50000, 10000),
                            map_location=(10, 25)) as vw:
                self.assertEqual(vw.extent(), (100, 500, 15100, 10500))
                self.assertEqual(vw.scale(), (50000, 10000))
                self.assertEqual(vw.extent(extent=gxv.EXTENT_MAP), (10., 25., 40., 125.))
                self.assertTrue(vw.cs.same_as(gxcs.GXcs()))

        test_map = os.path.join(self.gx.temp_folder(),"test_map")
        with gxmap.GXmap.new(test_map) as gmap:
            mapname = gmap.filename
            with gxv.GXview(gmap, "test") as view:
                self.assertEqual(view.viewname, "test")
                self.assertEqual(view.mapfilename, mapname)
                view.start_group('test_group')

                def_pen = view.pen
                pn = {"line_thick": 99, "pat_number": 88}
                view.push_pen()
                view.pen = pn
                new_pen = view.pen
                self.assertEqual(new_pen["line_thick"], 99)
                self.assertEqual(new_pen["pat_number"], 88)

                view.pop_pen()
                pen = view.pen
                self.assertEqual(pen, def_pen)

                view.push_pen(pn)
                view.pen = pn
                new_pen = view.pen
                self.assertEqual(new_pen["line_thick"], 99)
                self.assertEqual(new_pen["pat_number"], 88)

                view.pop_pen()
                pen = view.pen
                self.assertEqual(pen, def_pen)

    def test_view_groups(self):
        self.start(gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            mapfile = gmap.filename
            with gxv.GXview(gmap, "rectangle_test", area=(0,0,250, 125)) as view:
                view.start_group('test_group')
                rect_line(view)
                view.graticule(25, 20, style=gxv.GRATICULE_LINE)
                view.pen = {'line_thick': 0.1}
                view.xy_rectangle(((0,0),(250,125)), pen={'line_thick': 0.1, 'line_color':'R'})
            with gxv.GXview(gmap, "poly") as view:
                view.start_group('test_group')
                draw_stuff(view)

        self.view_crc(mapfile, 1690811698)

        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            mapfile = gmap.filename
            with gxv.GXview(gmap, "rectangle_test", area=(0,0,250, 125)) as view:
                view.start_group('line')
                rect_line(view)
                view.start_group('graticule')
                view.graticule(25, 20, style=gxv.GRATICULE_LINE)
                view.pen = {'line_thick': 0.1}
                view.start_group('test_rectangles')
                view.xy_rectangle(((0,0),(250,125)), pen={'line_thick': 0.1, 'line_color':'R'})
                view.xy_rectangle(((10, 5), (240, 120)), pen={'line_thick': 2, 'line_color': 'B'})
                view.delete_group('graticule')
            with gxv.GXview(gmap, "poly") as view:
                view.start_group('test_group')
                draw_stuff(view)

        self.view_crc(mapfile, 4245134056)

        gxmap.delete_files(mapfile)

    def test_reopen_map_view(self):
        self.start(gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            mapfile = gmap.filename
            with gxv.GXview(gmap, "test_view") as view:
                rect_line(view)
            with gxv.GXview(gmap, "test_view") as view:
                pass
        gxmap.delete_files(mapfile)

    def test_3D(self):
        self.start(gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            mapfile = gmap.filename
            with gxv.GXview(gmap, "base", area=(0,0,250, 125), scale=1000) as view:
                view.start_group('test_group')
                view.xy_rectangle(((0, 0), (100, 100)))
            with gxv.GXview3d(gmap, viewname='v3d_test', area=(0,0,300, 300), scale=1000,
                              cs="wgs 84 / UTM zone 15S") as view:
                view.start_group('test_group')
                rect_line(view)
                draw_stuff(view)
                view.box_3d(((0,0,10), (120,100,50)))

        #TODO resolve this with Jacques once 3D viewer works
        #gxvwr.map(mapfile)
        #gxvwr.v3d(mapfile)

    def test_cs(self):
        self.start(gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            with gxv.GXview(gmap, "rectangle_test", cs="wgs 84") as view:
                self.assertEqual("WGS 84", str(view.cs))
            with gxv.GXview(gmap, "vcs", cs="wgs 84 / UTM zone 15N [special]") as view:
                self.assertTrue("WGS 84 / UTM zone 15N [special]" in str(view.cs))

    def test_basic_drawing(self):
        self.start(gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            mapfile = gmap.filename
            with gxv.GXview(gmap, "my_base_view", area=(0, 0, 25, 20), scale=100.0) as view:
                view.xy_rectangle(view.extent(), pen={'line_thick': 0.1, 'line_color': 'R'})

            with gxv.GXview(gmap, "my_data_area", map_location=(4,3), area=(0, 0, 1800, 1500), scale=10000) as view:
                view.xy_rectangle(((0, 0), (1800, 1500)),
                                  pen={'line_thick': 5, 'line_color': 'G'})

                view.graticule(style=gxv.GRATICULE_LINE, pen={'line_thick': 5})

        self.view_crc(mapfile, 3565975558)

    def test_basic_grid(self):
        self.start(gsys.func_name())

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
            with gxv.GXview(gmap, "*Base") as view:
                view.xy_rectangle(view.extent(), pen={'line_thick': 0.2, 'line_color': 'K'})
            with gxv.GXview(gmap, "*Data") as view:
                view.xy_rectangle(area, pen={'line_thick': 0.1, 'line_color': 'R'})

                with gxagg.GXagg(grid_file) as agg:
                    view.aggregate(agg)

        self.view_crc(mapfile, 2610023726)

        with gxgrd.GXgrd(grid_file) as grd:
            cs = grd.cs
            area = grd.extent_2d()
        with gxmap.GXmap.new(map_file,
                             data_area=area, media="A3", margins=(0,0,0,0),
                             scale=(area[2] - area[0])/0.2,
                             cs=cs, overwrite=True) as gmap:
            mapfile = gmap.filename
            with gxv.GXview(gmap, "*Base") as view:
                view.xy_rectangle(view.extent(), pen={'line_thick': 0.2, 'line_color': 'K'})
            with gxv.GXview(gmap, "*Data") as view:
                view.xy_rectangle(area, pen={'line_thick': 0.1, 'line_color': 'G'})
                with gxagg.GXagg(grid_file) as agg:
                    view.aggregate(agg)

        self.view_crc(mapfile, 3402162077)

    def test_zone_grid(self):
        self.start(gsys.func_name())

        def test_zone(zone, crc, shade=False, display=False):
            with gxmap.GXmap.new(map_file, overwrite=True,
                                 data_area=(ex[0], ex[1], ex[2], ex[3]),
                                 scale=(ex[2] - ex[0]) / 0.2) as gmap:
                mapfile = gmap.filename
                with gxv.GXview(gmap, "data") as view:
                    with gxagg.GXagg(grid_file, zone=zone, shade=shade) as agg:
                        view.aggregate(agg)

            self.view_crc(mapfile, crc, display)

        # test grid file
        folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                   folder=self.gx.temp_folder())
        grid_file = os.path.join(folder, 'test_agg_utm.grd')
        with gxgrd.GXgrd(grid_file) as grd:
            ex = grd.extent_2d()
        map_file = os.path.join(self.gx.temp_folder(), "test_agg")

        test_zone(gxagg.ZONE_LINEAR, 3417239441, shade=True)
        test_zone(gxagg.ZONE_EQUALAREA, 2492050454)
        test_zone(gxagg.ZONE_DEFAULT, 2492050454)
        test_zone(gxagg.ZONE_LAST, 2492050454)
        test_zone(gxagg.ZONE_LINEAR, 4101718860)
        test_zone(gxagg.ZONE_NORMAL, 2111320705)
        test_zone(gxagg.ZONE_SHADE, 2447325492)
        test_zone(gxagg.ZONE_LOGLINEAR, 2976995354)


if __name__ == '__main__':

    unittest.main()
