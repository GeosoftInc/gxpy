import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.system as gsys
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.grid_utility as gxgrdu
import geosoft.gxpy.geometry as gxgeo
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.gdb as gxgdb

from base import GXPYTest


class Test(GXPYTest):
    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py), 'testgrids.zip'),
                                       folder=cls._gx.temp_folder())
        cls.g1f = os.path.join(cls.folder, 'test_grid_1.grd')
        cls.g2f = os.path.join(cls.folder, 'test_grid_2.grd')
        cls.gcf = os.path.join(cls.folder, 'test_bool1_color.grd')
        cls.mag = os.path.join(cls.folder, 'bhn_tmi_250m.grd')

    def test_grc(self):
        self.start()
        self.assertEqual(gxgrd.__version__, geosoft.__version__)

    def test_mosaic(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g:
            m1s = os.path.join(self.folder, 'm1.grd(GRD)')
            gxgrd.Grid.copy(g, m1s).close()
        with gxgrd.Grid.open(self.g2f) as g:
            m2s = os.path.join(self.folder, 'm2.grd(GRD)')
            gxgrd.Grid.copy(g, m2s).close()

        glist = [m1s, m2s]

        mosaicGrid = os.path.join(self.folder, 'test_mosaic.grd')
        with gxgrdu.grid_mosaic(mosaicGrid, glist) as grd:

            properties = grd.properties()
            self.assertAlmostEqual(properties.get('dx'),0.01)
            self.assertAlmostEqual(properties.get('dy'),0.01)
            self.assertAlmostEqual(properties.get('x0'),7.0)
            self.assertAlmostEqual(properties.get('y0'),44.0)
            self.assertEqual(properties.get('rot'),0.0)
            self.assertEqual(properties.get('nx'),201)
            self.assertEqual(properties.get('ny'),101)
            self.assertEqual(str(properties.get('coordinate_system')),'WGS 84')

        m = os.path.join(self.folder, 'test_mosaic.hgd(HGD)')
        gxgrdu.grid_mosaic(m, glist).close()

        with gxgrd.Grid.open(m) as grd:
            grd.delete_files()
            properties = grd.properties()
            self.assertAlmostEqual(properties.get('dx'),0.01)
            self.assertAlmostEqual(properties.get('dy'),0.01)
            self.assertAlmostEqual(properties.get('x0'),7.0)
            self.assertAlmostEqual(properties.get('y0'),44.0)
            self.assertEqual(properties.get('rot'),0.0)
            self.assertEqual(properties.get('nx'),201)
            self.assertEqual(properties.get('ny'),101)
            self.assertEqual(str(properties.get('coordinate_system')),'WGS 84')

    def test_bool(self):
        self.start()

        g1 = gxgrd.Grid.open(self.g1f)
        g2 = gxgrd.Grid.open(self.g2f)
        grd = gxgrdu.grid_bool(g1, g2, os.path.join(self.folder, 'testBool.grd(GRD;TYPE=SHORT)'), size=3)
        grd.delete_files()
        properties = grd.properties()
        g1.close()
        g2.close()
        grd.close()

        self.assertAlmostEqual(properties.get('dx'),0.01)
        self.assertAlmostEqual(properties.get('dy'),0.01)
        self.assertAlmostEqual(properties.get('x0'),7.0)
        self.assertAlmostEqual(properties.get('y0'),44.0)
        self.assertEqual(properties.get('rot'),0.0)
        self.assertEqual(properties.get('nx'),201)
        self.assertEqual(properties.get('ny'),101)
        self.assertEqual(str(properties.get('coordinate_system')),'WGS 84')
        self.assertEqual(properties.get('dtype'),np.int16)

        grd = gxgrdu.grid_bool(self.g1f, self.g2f, os.path.join(self.folder, 'testBool.grd(GRD;TYPE=SHORT)'), size=3)
        grd.delete_files()
        properties = grd.properties()
        grd.close()

        self.assertAlmostEqual(properties.get('dx'), 0.01)
        self.assertAlmostEqual(properties.get('dy'), 0.01)
        self.assertAlmostEqual(properties.get('x0'), 7.0)
        self.assertAlmostEqual(properties.get('y0'), 44.0)
        self.assertEqual(properties.get('rot'), 0.0)
        self.assertEqual(properties.get('nx'), 201)
        self.assertEqual(properties.get('ny'), 101)
        self.assertEqual(str(properties.get('coordinate_system')), 'WGS 84')
        self.assertEqual(properties.get('dtype'), np.int16)

    def test_remove_trend(self):
        self.start()

        with gxgrd.Grid.open(self.mag) as grd:
            dtg = gxgrdu.remove_trend(grd, method=gxgrdu.TREND_ALL)
            stt = dtg.statistics()
            self.assertAlmostEqual(stt['mean'], 0.7715205926416573)

        dtg = gxgrdu.remove_trend(self.mag, method=gxgrdu.TREND_EDGE)
        stt = dtg.statistics()
        self.assertAlmostEqual(stt['mean'], 31.909457151857282)

    def test_derivatives(self):
        self.start()

        with gxgrd.Grid.open(self.mag, dtype=np.float32) as grd:
            dxg = gxgrdu.derivative(grd, gxgrdu.DERIVATIVE_X)
            self.assertAlmostEqual(dxg.statistics()['sd'], 18.04271016086604)
            self.assertEqual(dxg.dtype, np.float32)

        with gxgrd.Grid.open(self.mag) as grd:
            dyg = gxgrdu.derivative(grd, gxgrdu.DERIVATIVE_Y)
            self.assertAlmostEqual(dyg.statistics()['sd'], 14.884414474960357)

        with gxgrd.Grid.open(self.mag) as grd:
            dzg = gxgrdu.derivative(grd, gxgrdu.DERIVATIVE_Z)
            self.assertAlmostEqual(dzg.statistics()['sd'], 0.22893001533535487)

        with gxgrd.Grid.open(self.mag) as grd:
            dxy = gxgrdu.derivative(grd, gxgrdu.DERIVATIVE_XY)
            self.assertAlmostEqual(dxy.statistics()['sd'], 19.18270809104566)

        with gxgrd.Grid.open(self.mag) as grd:
            das = gxgrdu.derivative(grd, gxgrdu.DERIVATIVE_XYZ)
            self.assertAlmostEqual(das.statistics()['sd'], 19.183085930995492)

        with gxgrd.Grid.open(self.mag) as grd:
            dtd = gxgrdu.derivative(grd, gxgrdu.DERIVATIVE_TILT)
            self.assertAlmostEqual(dtd.statistics()['sd'], 0.033342129413201395)

        with gxgrd.Grid.open(self.mag, dtype=np.float64) as grd:
            dxg = gxgrdu.derivative(grd, gxgrdu.DERIVATIVE_X)
            self.assertAlmostEqual(dxg.statistics()['sd'], 18.04271016086604)
            self.assertEqual(dxg.dtype, np.float64)

        with gxgrd.Grid.open(self.mag, dtype=np.float64) as grd:
            dzg = gxgrdu.derivative(grd, gxgrdu.DERIVATIVE_Z)
            self.assertAlmostEqual(dzg.statistics()['sd'], 0.22893001533535487)
            self.assertEqual(dzg.dtype, np.float64)

        dzg = gxgrdu.derivative(self.mag, gxgrdu.DERIVATIVE_Z)
        self.assertAlmostEqual(dzg.statistics()['sd'], 0.22893001533535487)

        dxg = gxgrdu.derivative(self.mag, gxgrdu.DERIVATIVE_X)
        self.assertAlmostEqual(dxg.statistics()['sd'], 18.04271016086604)

    def test_contour_xy(self):
        self.start()

        xyp = gxgrdu.contour_points(self.mag, 100)
        self.assertTrue(isinstance(xyp, list))
        self.assertTrue(isinstance(xyp[0], gxgeo.PPoint))
        self.assertEqual(xyp[0][0].z, 0.0)

        # oriented grid
        with gxgrd.Grid.open(self.g1f) as g:
            v = g.statistics()['mean']
            with gxgrd.Grid.copy(g) as gm:
                cs_name = gxcs.name_from_hcs_orient_vcs(gm.coordinate_system.hcs, '0, 0, 1000, 0, -90, 25', '')
                gm.coordinate_system = cs_name
                xyp = gxgrdu.contour_points(gm, v)
                self.assertTrue(isinstance(xyp, list))
                self.assertTrue(isinstance(xyp[0], gxgeo.PPoint))
                self.assertEqual(len(xyp), 45)

                self.assertRaises(gxgrdu.GridUtilityException, gxgrdu.contour_points, gm, 0)

                xyp = gxgrdu.contour_points(gm, 500, return_as=gxgrdu.RETURN_PPOINT)
                self.assertTrue(isinstance(xyp, gxgeo.PPoint))
                self.assertEqual(len(xyp), 343)

                xyp = gxgrdu.contour_points(gm, 250, return_as=gxgrdu.RETURN_GDB)
                self.assertTrue(isinstance(xyp, gxgdb.Geosoft_gdb))
                self.assertEqual(len(xyp.list_lines()), 9)

    def test_tilt_depth(self):
        self.start()

        td = gxgrdu.tilt_depth(self.mag, resolution=1000, gdb='temp.gdb', overwrite=True)
        self.assertTrue(isinstance(td, gxgdb.Geosoft_gdb))
        self.assertTrue(td.coordinate_system == 'AGD66 / AMG zone 53')
        n = 0
        for ln in td.list_lines():
            d = td.read_line(ln, 'X')
            n += len(d[0])
        self.assertEqual(n, 1454)
        td.close(discard=True)

        td = gxgrdu.tilt_depth(self.mag, resolution=1000)
        self.assertTrue(isinstance(td, gxgeo.PPoint))
        self.assertTrue(td.coordinate_system == 'AGD66 / AMG zone 53')
        self.assertEqual(len(td), 1454)

        td = gxgrdu.tilt_depth(self.mag, resolution=1000, return_as=gxgrdu.RETURN_LIST_OF_PPOINT)
        self.assertTrue(isinstance(td, list))
        self.assertTrue(td[0].coordinate_system == 'AGD66 / AMG zone 53')
        self.assertTrue(isinstance(td[0], gxgeo.PPoint))
        n = 0
        for p in td:
            n += len(p)
        self.assertEqual(n, 1454)

        td = gxgrdu.tilt_depth(self.mag, resolution=1000, return_as=gxgrdu.RETURN_GDB)
        self.assertTrue(isinstance(td, gxgdb.Geosoft_gdb))
        self.assertTrue(td.coordinate_system == 'AGD66 / AMG zone 53')
        n = 0
        for ln in td.list_lines():
            d = td.read_line(ln, 'X')
            n += len(d[0])
        self.assertEqual(n, 1454)

###############################################################################################

if __name__ == '__main__':

    unittest.main()
