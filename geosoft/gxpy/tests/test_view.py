import unittest
import os

import geosoft
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.view as gxv
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.group as gxg

from geosoft.gxpy.tests import GXPYTest





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
        Test.start(self, gsys.func_name())

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
        Test.start(self, gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            mapfile = gmap.file_name
            with gxv.GXview(gmap, "test_view") as v:
                with gxg.GXdraw(v) as g:
                    g.xy_rectangle(v.extent_clip)
            with gxv.GXview(gmap, "test_view") as v:
                pass
        gxmap.delete_files(mapfile)

    def test_cs(self):
        Test.start(self, gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new(testmap, overwrite=True) as gmap:
            with gxv.GXview(gmap, "rectangle_test", cs="wgs 84") as v:
                self.assertEqual("WGS 84", str(v.cs))
            with gxv.GXview(gmap, "vcs", cs="wgs 84 / UTM zone 15N [special]") as v:
                self.assertTrue("WGS 84 / UTM zone 15N [special]" in str(v.cs))


if __name__ == '__main__':

    unittest.main()
