import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.geometry as gxgm

from base import GXPYTest


class Test(GXPYTest):
    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py), 'testgrids.zip'),
                                       folder=cls._gx.temp_folder())
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py), 'testgrids.zip'),
                                       folder=cls._gx.temp_folder())
        cls.g1f = os.path.join(cls.folder, 'test_grid_1.grd')
        cls.g2f = os.path.join(cls.folder, 'test_grid_2.grd')
        cls.gcf = os.path.join(cls.folder, 'test_bool1_color.grd')

    def test_grc(self):
        self.start()
        self.assertEqual(gxgrd.__version__, geosoft.__version__)

    def test_gridProperties(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g1:
            properties = g1.properties()
            self.assertEqual(properties.get('dx'),0.01)
            self.assertEqual(properties.get('dy'),0.01)
            self.assertEqual(properties.get('x0'),7.0)
            self.assertEqual(properties.get('y0'),44.0)
            self.assertEqual(properties.get('rot'),0.0)
            self.assertEqual(properties.get('is_color'),False)
            self.assertEqual(properties.get('nx'),101)
            self.assertEqual(properties.get('ny'),101)
            self.assertEqual(str(properties.get('coordinate_system')),'WGS 84')

            self.assertEqual(g1.dx, 0.01)
            self.assertEqual(g1.dy, 0.01)
            self.assertEqual(g1.x0, 7.0)
            self.assertEqual(g1.y0, 44.0)
            self.assertEqual(g1.rot, 0.0)
            self.assertEqual(g1.is_color, False)
            self.assertEqual(g1.nx, 101)
            self.assertEqual(g1.ny, 101)
            self.assertEqual(str(g1.coordinate_system), 'WGS 84')

    def test_copy(self):
        self.start()

        #create a grids
        outGrid = os.path.join(self.folder, 'test_copy.grd(GRD)')
        with gxgrd.Grid.open(self.g1f) as g:
            with gxgrd.Grid.copy(g, outGrid) as grd:
                grd.delete_files()
                properties = grd.properties()
                self.assertEqual(properties.get('dx'),0.01)
                self.assertEqual(properties.get('dy'),0.01)
                self.assertEqual(properties.get('x0'),7.0)
                self.assertEqual(properties.get('y0'),44.0)
                self.assertEqual(properties.get('rot'),0.0)
                self.assertEqual(properties.get('nx'),101)
                self.assertEqual(properties.get('ny'),101)
                self.assertEqual(str(properties.get('coordinate_system')),'WGS 84')

    def test_set_properties(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g1:
            properties = g1.properties()
            properties['x0'] = 45.0
            properties['y0'] = -15.0
            properties['dx'] = 1.5
            properties['dy'] = 2.5
            properties['rot'] = 33.333333
            properties['coordinate_system'] = gxcs.Coordinate_system('NAD27 / UTM zone 18N')
            self.assertRaises( gxgrd.GridException, g1.set_properties, properties)

        outGrid = os.path.join(self.folder, 'test_set_properties.grd(GRD;TYPE=SHORT;COMP=SPEED)')
        with gxgrd.Grid.open(self.g1f) as g:
            with gxgrd.Grid.copy(g, outGrid) as grd:
                grd.dx = 1.5
                grd.dy = 2.5
                grd.x0 = 45.0
                grd.y0 = -15.0
                grd.rot = 33.333333
                grd.coordinate_system = gxcs.Coordinate_system('NAD27 / UTM zone 18N')

        with gxgrd.Grid.open(outGrid) as grd:
            properties = grd.properties()
            self.assertEqual(properties.get('dx'),1.5)
            self.assertEqual(properties.get('dy'),2.5)
            self.assertEqual(properties.get('x0'),45.0)
            self.assertEqual(properties.get('y0'),-15.0)
            self.assertEqual(properties.get('rot'),33.333333)
            self.assertEqual(properties.get('nx'),101)
            self.assertEqual(properties.get('ny'),101)
            self.assertEqual(str(properties.get('coordinate_system')),'NAD27 / UTM zone 18N')
            self.assertEqual(properties.get('dtype'),np.int16)

        outGrid = os.path.join(self.folder, 'test_set_properties.grd(GRD;TYPE=SHORT;COMP=SPEED)')
        with gxgrd.Grid.open(self.g1f) as g:
            with gxgrd.Grid.copy(g, outGrid, overwrite=True) as grd:
                grd.set_properties(properties)

        with gxgrd.Grid.open(outGrid) as grd:
            properties = grd.properties()
            self.assertEqual(properties.get('dx'),1.5)
            self.assertEqual(properties.get('dy'),2.5)
            self.assertEqual(properties.get('x0'),45.0)
            self.assertEqual(properties.get('y0'),-15.0)
            self.assertEqual(properties.get('rot'),33.333333)
            self.assertEqual(properties.get('nx'),101)
            self.assertEqual(properties.get('ny'),101)
            self.assertEqual(str(properties.get('coordinate_system')),'NAD27 / UTM zone 18N')
            self.assertEqual(properties.get('dtype'),np.int16)

    def test_memory(self):
        self.start()

        with gxgrd.Grid.new(properties={'dtype': np.int16,
                                         'nx': 100, 'ny': 50,
                                         'x0':4, 'y0':8,
                                         'dx': 0.1, 'dy':0.2,
                                         'rot': 5,
                                         'coordinate_system': gxcs.Coordinate_system('NAD27 / UTM zone 18N')}) as grd:
            properties = grd.properties()
            self.assertEqual(properties.get('dx'),0.1)
            self.assertEqual(properties.get('dy'),0.2)
            self.assertEqual(properties.get('x0'),4.0)
            self.assertEqual(properties.get('y0'),8.0)
            self.assertEqual(properties.get('rot'),5.0)
            self.assertEqual(properties.get('nx'),100)
            self.assertEqual(properties.get('ny'),50)
            self.assertEqual(str(properties.get('coordinate_system')),'NAD27 / UTM zone 18N')
            self.assertEqual(properties.get('dtype'),np.int16)

            m = grd.metadata
            self.assertFalse(bool(m))

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
        with gxgrd.gridMosaic(mosaicGrid, glist) as grd:

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
        gxgrd.gridMosaic(m, glist).close()

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
        grd = gxgrd.gridBool(g1, g2, os.path.join(self.folder, 'testBool.grd(GRD;TYPE=SHORT)'), size=3)
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

        grd = gxgrd.gridBool(self.g1f, self.g2f, os.path.join(self.folder, 'testBool.grd(GRD;TYPE=SHORT)'), size=3)
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

    def test_delete_grid(self):
        self.start()

        self.assertRaises(gxgrd.GridException, gxgrd.Grid.new, self.g1f)
        with gxgrd.Grid.open(self.g1f) as g:
            with gxgrd.Grid.copy(g, os.path.join(self.folder,'testDelete.grd'), overwrite=True) as g2:
                filen = g2.file_name
                g2.delete_files()

        self.assertFalse(os.path.isfile(filen))
        self.assertFalse(os.path.isfile(filen+'.gi'))
        self.assertFalse(os.path.isfile(filen+'.xml'))

    def test_hgd(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g:
            ofile = gxgrd.Grid.decorate_name(os.path.join(self.folder, 'test.hgd'), 'HGD')
            with gxgrd.Grid.copy(g, ofile) as g2:
                properties = g2.properties()
            self.assertEqual(properties.get('file_name'),os.path.abspath(ofile.split('(')[0]))
            self.assertEqual(properties.get('decoration'),'HGD')
            self.assertEqual(properties.get('gridtype'),'HGD')
            self.assertAlmostEqual(properties.get('dx'),0.01)
            self.assertAlmostEqual(properties.get('dy'),0.01)
            self.assertAlmostEqual(properties.get('x0'),7.0)
            self.assertAlmostEqual(properties.get('y0'),44.0)
            self.assertEqual(properties.get('rot'),0.0)
            self.assertEqual(properties.get('nx'),101)
            self.assertEqual(properties.get('ny'),101)
            self.assertEqual(str(properties.get('coordinate_system')),'WGS 84')

    def test_name_parts(self):
        self.start()

        namep = gxgrd.Grid.name_parts("f:/someFolder/name.grd(GRD;TYPE=SHORT)")
        self.assertEqual(namep,('f:\\someFolder', 'name.grd', 'name', '.grd', 'GRD;TYPE=SHORT'))

        namep = gxgrd.Grid.name_parts(".\\name.grd(GRD;TYPE=SHORT)")
        self.assertEqual(namep[0],os.getcwd())
        self.assertEqual(namep[1:],('name.grd', 'name', '.grd', 'GRD;TYPE=SHORT'))

        namep = gxgrd.Grid.name_parts(".\\name.grd")
        self.assertEqual(namep[0],os.getcwd())
        self.assertEqual(namep[1:],('name.grd', 'name', '.grd', ''))

        ref = 'billybob(decs;more)'
        name = gxgrd.Grid.decorate_name('billybob','(decs;more)')
        self.assertEqual(name,ref)
        name = gxgrd.Grid.decorate_name('billybob','decs;more')
        self.assertEqual(name,ref)
        name = gxgrd.Grid.decorate_name('billybob','(decs;more')
        self.assertEqual(name,ref)
        name = gxgrd.Grid.decorate_name('billybob','decs;more)')
        self.assertEqual(name,ref)
        name = gxgrd.Grid.decorate_name(ref)
        self.assertEqual(name,ref)

    def test_index_window(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g:
            p = g.properties()
            window = os.path.join(self.folder,'testwindow.grd(GRD)')

            with gxgrd.Grid.index_window(g, window, 4, 2, 96, 5, overwrite=True) as gw:
                pw = gw.properties()
                self.assertAlmostEqual(gw.x0, g.x0+(4*g.dx))
                self.assertAlmostEqual(gw.y0, g.y0+(2*g.dy))
                self.assertEqual(gw.nx, 96)
                self.assertEqual(gw.ny, 5)

            with gxgrd.Grid.index_window(g, x0=4, y0=2, nx=96, ny=5, overwrite=True) as gw:
                nx = gw.nx
                gw.delete_files()
                pw = gw.properties()
                self.assertAlmostEqual(gw.x0, g.x0+(4*g.dx))
                self.assertAlmostEqual(gw.y0, g.y0+(2*g.dy))
                self.assertEqual(gw.nx, 96)
                self.assertEqual(gw.ny, 5)
                self.assertEqual(gw.name, 'test_grid_1_(4,2)(96,5)')

            with gxgrd.Grid.index_window(g, window, nx=20, ny=100, overwrite=True) as gw:
                gw.delete_files()
                pw = gw.properties()
                self.assertAlmostEqual(pw.get('x0'),p.get('x0'))
                self.assertAlmostEqual(pw.get('y0'),p.get('y0'))
                self.assertEqual(pw.get('nx'),20)
                self.assertEqual(pw.get('ny'),100)

            with gxgrd.Grid.index_window(g, window, x0=29, y0=100, overwrite=True) as gw:
                gw.delete_files()
                pw = gw.properties()
                dx = p.get('dx')
                self.assertAlmostEqual(pw.get('x0'),p.get('x0')+(29*dx))
                dy = p.get('dy')
                self.assertAlmostEqual(pw.get('y0'),p.get('y0')+(100*dy))
                self.assertEqual(pw.get('nx'),72)
                self.assertEqual(pw.get('ny'),1)

            self.assertRaises(gxgrd.GridException, gxgrd.Grid.index_window, g, window, x0=2900, y0=3600, ny=2)
            self.assertRaises(gxgrd.GridException, gxgrd.Grid.index_window, g, window, -1)
            self.assertRaises(gxgrd.GridException, gxgrd.Grid.index_window, g, window, y0=-1)

        with gxgrd.Grid.open(self.g1f) as g:
            window = os.path.join(self.folder, 'testwindow.grd(GRD)')
            with gxgrd.Grid.index_window(g, window, 4, 2, 96, 5, overwrite=True) as gw:
                gw.delete_files()
                ex = gw.extent_2d()
                self.assertAlmostEqual(ex[0], 7.04)
                self.assertAlmostEqual(ex[1], 44.02)
                self.assertAlmostEqual(ex[2], 7.99)
                self.assertAlmostEqual(ex[3], 44.06)

            g.rot = 10.0
            window = os.path.join(self.folder, 'testwindow.grd(GRD)')
            with gxgrd.Grid.index_window(g, window, 4, 2, 96, 5, overwrite=True) as gw:
                gw.delete_files()
                ex = gw.extent_2d()
                self.assertAlmostEqual(ex[0], 6.95713471)
                self.assertAlmostEqual(ex[1], 43.822284)
                self.assertAlmostEqual(ex[2], 7.8996480)
                self.assertAlmostEqual(ex[3], 44.0266421)

    def test_from_array(self):
        self.start()

        file_name = os.path.join(self.folder, "test_array.grd")

        data = np.arange(24).reshape((8,3))
        with gxgrd.Grid.from_data_array(data, file_name) as grd:
            grd.delete_files()
            properties = grd.properties()
            self.assertEqual(properties.get('dx'),1.0)
            self.assertEqual(properties.get('dy'),1.0)
            self.assertEqual(properties.get('x0'),0.0)
            self.assertEqual(properties.get('y0'),0.0)
            self.assertEqual(properties.get('rot'),0.0)
            self.assertEqual(properties.get('nx'),3)
            self.assertEqual(properties.get('ny'),8)
            self.assertEqual(str(properties.get('coordinate_system')),'*unknown')

        with gxgrd.Grid.from_data_array(list(data), file_name) as grd:
            grd.delete_files()
            properties = grd.properties()
            self.assertEqual(properties.get('dx'),1.0)
            self.assertEqual(properties.get('dy'),1.0)
            self.assertEqual(properties.get('x0'),0.0)
            self.assertEqual(properties.get('y0'),0.0)
            self.assertEqual(properties.get('rot'),0.0)
            self.assertEqual(properties.get('nx'),3)
            self.assertEqual(properties.get('ny'),8)
            self.assertEqual(str(properties.get('coordinate_system')),'*unknown')

        with gxgrd.Grid.from_data_array(data, file_name,
                                         properties={'x0':575268, 'dx':2.0, 'dy':1.5, 'rot':15, 'coordinate_system':'WGS 84'}) as grd:
            grd.delete_files()
            properties = grd.properties()
            self.assertEqual(properties.get('dx'),2.0)
            self.assertEqual(properties.get('dy'),1.5)
            self.assertEqual(properties.get('x0'),575268.0)
            self.assertEqual(properties.get('y0'),0.0)
            self.assertEqual(properties.get('rot'),15.0)
            self.assertEqual(properties.get('nx'),3)
            self.assertEqual(properties.get('ny'),8)
            self.assertEqual(str(properties.get('coordinate_system')),'WGS 84')

    def test_array_locations(self):
        self.start()

        with gxgrd.Grid.new(properties={'x0':100, 'y0':-25.25, 'dx': 5, 'nx':101, 'ny':501}) as g:
            a = g.xyzv()
            self.assertEqual(len(a.shape),3)
            self.assertEqual(a.shape[0], g.ny)
            self.assertEqual(a.shape[1], g.nx)
            self.assertEqual(a.shape[2], 4)
            self.assertEqual(a[0,0,0], 100.0)
            self.assertEqual(a[0,0,1], -25.25)
            self.assertEqual(a[0,0,2], 0.0)
            self.assertTrue(np.isnan(a[0, 0, 3]))
            self.assertEqual(a[0,1,0]-a[0,0,0], g.dx)
            self.assertEqual(a[1,0,1]-a[0,0,1], g.dy)
            self.assertEqual(a[0,0,2]-a[1,1,2], 0.)

        props = {'x0':100, 'y0':-25.25, 'dx': 5, 'nx':101, 'ny':501, 'rot':10}
        a = gxgrd.array_locations(props)
        self.assertEqual((tuple(a[0, 0, :])), (100.0, -25.25, 0.0))
        self.assertEqual((tuple(a[0, 10, :])), (149.24038765061039, -33.932408883346518, 0.0))
        self.assertEqual((tuple(a[10, 0, :])), (108.68240888334651, 23.990387650610401, 0.0))
        self.assertEqual((tuple(a[10, 10, :])), (157.92279653395693, 15.307978767263883, 0.0))

        cs = gxcs.Coordinate_system({'type': 'local',
                                     'lon_lat': (-96,43),
                                     'azimuth': 10}).gxf
        props = {'x0':0, 'y0':0, 'dx': 5, 'nx':101, 'ny':501, 'coordinate_system':cs}
        a = gxgrd.array_locations(props)
        self.assertEqual((tuple(a[0, 0, :])), (0.0, 0.0, 0.0))
        self.assertEqual((tuple(a[0, 10, :])), (49.240387650610401, -8.6824088833465165, 0.0))
        self.assertEqual((tuple(a[10, 0, :])), (8.6824088833465165, 49.240387650610401, 0.0))
        self.assertEqual((tuple(a[10, 10, :])), (57.92279653395692, 40.557978767263883, 0.0))

    def test_hanging_resource(self):
        self.start()

        g1 = gxgrd.Grid.open(self.g1f)
        g2 = gxgrd.Grid.open(self.g2f)
        rs = len(gx._res_heap)
        self.assertTrue(rs >= 2)
        g1.close()
        self.assertEqual(len(gx._res_heap), rs-1)
        g2.close()

    def test_extent(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g:
            with gxgrd.Grid.copy(g, os.path.join(self.folder, 'test_extent.grd(GRD)')) as grd:
                grd.delete_files()
                grd.x0 = grd.y0 = 0.0
                grd.dx = grd.dy = 0.1
                grd.rot = 0.0

                ex = grd.extent_2d()
                self.assertAlmostEqual(ex[0], 0.0)
                self.assertAlmostEqual(ex[1], 0.0)
                self.assertAlmostEqual(ex[2], 10.0)
                self.assertAlmostEqual(ex[3], 10.0)

                grd.rot = 30.0
                ex = grd.extent_2d()
                self.assertAlmostEqual(ex[0], 0)
                self.assertAlmostEqual(ex[1], -5)
                self.assertAlmostEqual(ex[2], 13.66025404)
                self.assertAlmostEqual(ex[3], 8.66025404)

                cs = grd.coordinate_system
                cs_name = cs.cs_name(gxcs.NAME_HCS_VCS) + ' <0,0,0,0,0,30>'
                grd.coordinate_system = gxcs.Coordinate_system(cs_name)
                ex = grd.extent_2d()
                self.assertAlmostEqual(ex[0], 0)
                self.assertAlmostEqual(ex[1], -5)
                self.assertAlmostEqual(ex[2], 13.66025404)
                self.assertAlmostEqual(ex[3], 8.66025404)

                grd.rot = 0
                ex = grd.extent_2d()
                self.assertAlmostEqual(ex[0], 0.0)
                self.assertAlmostEqual(ex[1], 0.0)
                self.assertAlmostEqual(ex[2], 10.0)
                self.assertAlmostEqual(ex[3], 10.0)
                ex = grd.extent_3d()
                self.assertAlmostEqual(ex[0], 0.0)
                self.assertAlmostEqual(ex[1], -5)
                self.assertAlmostEqual(ex[2], 0.0)
                self.assertAlmostEqual(ex[3], 13.66025404)
                self.assertAlmostEqual(ex[4], 8.66025404)
                self.assertAlmostEqual(ex[5], 0)

                cs_name = cs.cs_name(gxcs.NAME_HCS_VCS) + ' <0,0,0,90,0,30>'
                grd.coordinate_system = gxcs.Coordinate_system(cs_name)
                ex = grd.extent_3d()
                self.assertAlmostEqual(ex[0], 0.0)
                self.assertAlmostEqual(ex[1], -5)
                self.assertAlmostEqual(ex[2], -10.0)
                self.assertAlmostEqual(ex[3], 8.66025404)
                self.assertAlmostEqual(ex[4], 0)
                self.assertAlmostEqual(ex[5], 0)

                grd.rot = 30.0
                ex = grd.extent_2d()
                self.assertAlmostEqual(ex[0], 0)
                self.assertAlmostEqual(ex[1], -5)
                self.assertAlmostEqual(ex[2], 13.66025404)
                self.assertAlmostEqual(ex[3], 8.66025404)
                ex = grd.extent_3d()
                self.assertAlmostEqual(ex[0], 0)
                self.assertAlmostEqual(ex[1], -6.83012701892219)
                self.assertAlmostEqual(ex[2], -8.66025403784439)
                self.assertAlmostEqual(ex[3], 11.830127018922193)
                self.assertAlmostEqual(ex[4], 0)
                self.assertAlmostEqual(ex[5], 5)

    def test_extent_cell(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g:
            with gxgrd.Grid.copy(g, os.path.join(self.folder, 'test_extent.grd(GRD)')) as grd:
                grd.delete_files()
                grd.x0 = grd.y0 = 0.0
                grd.dx = 0.1
                grd.dy = 0.2
                grd.rot = 0.0

                ex = grd.extent_cell_2d()
                self.assertAlmostEqual(ex[0], -0.05)
                self.assertAlmostEqual(ex[1], -0.1)
                self.assertAlmostEqual(ex[2], 10.05)
                self.assertAlmostEqual(ex[3], 20.1)

                ex = grd.extent_cell_3d()
                self.assertEqual(ex, (-0.05, -0.1, 0.0, 10.05, 20.1, 0.0))

                grd.rot = 30.0
                ex = grd.extent_cell_2d()
                self.assertEqual(ex, (-0.09330127018922194, -5.111602540378444,
                                      18.753555308033608, 17.432110616067217))

                cs = grd.coordinate_system
                cs_name = cs.cs_name(gxcs.NAME_HCS_VCS) + ' <0,0,0,90,0,30>'
                grd.coordinate_system = gxcs.Coordinate_system(cs_name)
                ex = grd.extent_cell_3d()
                self.assertEqual(ex, (-0.08080127018922209, -9.376777654016802, -17.432110616067217,
                                      16.24105530803361, 0.046650635094611884, 5.111602540378444))

                self.assertTrue(grd.extent == gxgm.Point2(ex))

    def test_read(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g:
            for row in range(g.ny):
                vv = g.read_row(row)
                self.assertEqual(vv.length, g.nx)

            for col in range(g.nx):
                vv = g.read_column(col)
                self.assertEqual(vv.length, g.ny)

    def test_getitem(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g:
            self.assertTrue(isinstance(g[0], tuple))
            self.assertTrue(isinstance(g[0][3], float))
            self.assertEqual(g[0][3], 771.0)
            self.assertEqual(g[(0,0)][3], 771.0)
            self.assertEqual(g[(g.nx * g.ny) - 1][3], 243.0)
            self.assertEqual(g[(g.nx - 1, g.ny - 1)][3], 243.0)

    def test_copy_from_file_name(self):
        self.start()

        with gxgrd.Grid.copy(self.g1f, dtype=int) as g:
            self.assertTrue(isinstance(g[0][3], int))
            self.assertEqual(g[0][3], 771)
            self.assertEqual(g[45], (7.45, 44.0, 0.0, 1699))

    def test_open_int(self):
        self.start()

        with gxgrd.Grid.open(self.g1f, dtype=int) as g:
            vv = g.read_row(0)
            self.assertEqual(g[0][3], 771)

    def test_value(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g:
            self.assertEqual(g.get_value(7.043, 44.625), 1912.4500000000035)
            self.assertEqual(g.get_value(0, 0), None)

        with gxgrd.Grid.open(self.g1f, dtype=int) as g:
            self.assertEqual(g.get_value(7.043, 44.625), 1912.4500000000035)
            self.assertEqual(g.get_value(0,0), None)

    def test_metadata(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g:
            m = g.metadata
            gm = m['geosoft']
            self.assertTrue('dataset' in gm)
            self.assertTrue('georeference' in gm['dataset'])

            newstuff = {'maki':{'a':1, 'b':(4, 5, 6), 'units': 'nT'}}
            g.metadata = newstuff

        with gxgrd.Grid.open(self.g1f) as g:
            m = g.metadata
            maki = m['maki']
            self.assertEqual(maki['b'], ['4', '5', '6'])
            self.assertEqual(maki['units'], 'nT')

    def test_units_of_measure(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g:

            uom = g.unit_of_measure
            self.assertEqual(uom, 'm')
            g.unit_of_measure = 'metres'

        with gxgrd.Grid.open(self.g1f) as g:
            uom = g.unit_of_measure
            self.assertEqual(uom, 'metres')

    def test_iterator(self):

        with gxgrd.Grid.open(self.g2f) as g0:

            self.assertEqual(g0[0, 0], (8.0, 44.0, 0.0, 763.0))
            self.assertEqual(g0[100, 100], (9.0, 45.0, 0.0, 88.0))

            with gxgrd.Grid.index_window(g0, nx=75, ny=60, overwrite=True) as g:
                g.delete_files()

                self.assertEqual(g[1, 1], (8.0099999999999998, 44.009999999999998, 0.0, 384.0))
                self.assertEqual(g[74, 59], (8.7400000000000002, 44.590000000000003, 0.0, 530.0))

                data = g.xyzv()[:, :, 3]
                i = 0
                sum = 0.0
                dummies = 0

                for x, y, z, v in g:
                    i += 1
                    if v is None:
                        dummies += 1
                    else:
                        sum += v

                self.assertEqual(i, g.nx * g.ny)

        self.assertEqual(sum, np.nansum(data))
        self.assertEqual(dummies, np.count_nonzero(np.isnan(data)))

    def test_xyz(self):

        with gxgrd.Grid.open(self.g1f) as g:
            self.assertEqual(g.xyz(0), (g.x0, g.y0, 0.0))
            self.assertEqual(g.xyz(1), (g.x0 + g.dx, g.y0, 0.0))
            self.assertEqual(g.xyz(g.nx), (g.x0, g.y0 + g.dy, 0.0))
            self.assertEqual(g.xyz((0,1)), (g.x0, g.y0 + g.dy, 0.0))

            with gxgrd.Grid.copy(g) as gm:
                cs_name = gxcs.name_from_hcs_orient_vcs(gm.coordinate_system.hcs, '0, 0, 1000, 0, -90, 25', '')
                gm.coordinate_system = cs_name
                self.assertEqual(gm.xyz(0), (18.595203516590775, 39.8775426296126, 1007.0))
                self.assertEqual(gm.xyz((g.nx-1, g.ny-1)), (19.017821778331474, 40.783850416649244, 1008.0))

                gm.rot = 2.0
                self.assertEqual(gm.xyz(0), (18.595203516590775, 39.8775426296126, 1007.0))
                self.assertEqual(gm.xyz((g.nx - 1, g.ny - 1)), (19.00281516607315, 40.75166863280787, 1008.0342903237216))

    def test_figure_map(self):
        self.start()

        map_file = gxgrd.figure_map(self.g1f, title='image_test', features='all').file_name
        self.assertEqual(gxmap.Map.open(map_file).crc_image(pix_width=800), 2252249278)

    def test_np(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g1:
            data = g1.np()
            self.assertEqual(data.dtype, np.dtype(np.float32))
            self.assertEqual(data.shape, (101, 101))
            self.assertEqual(data[0, 0], 771.0)
            self.assertEqual(data[100, 100], 243.0)

            self.assertEqual(10081870.0, np.nansum(data))
            self.assertEqual(91, np.count_nonzero(np.isnan(data)))

        with gxgrd.Grid.open(self.g2f) as g2:
            data = g2.np()
            self.assertEqual(data.dtype, np.dtype(np.float32))
            self.assertEqual(data.shape, (101, 101))
            self.assertEqual(data[0, 0], 763.0)
            self.assertEqual(data[100, 100], 88.0)

            self.assertEqual(2696851.0, np.nansum(data))
            self.assertEqual(0, np.count_nonzero(np.isnan(data)))

        with gxgrd.Grid.open(self.gcf) as gc:
            data = gc.np()
            self.assertEqual(data.dtype, np.dtype(np.uint8))
            self.assertEqual(data.shape, (153, 254, 4))
            col_1 = data[0, 0]
            self.assertEqual(col_1[0], 0)
            self.assertEqual(col_1[1], 0)
            self.assertEqual(col_1[2], 0)
            self.assertEqual(col_1[3], 0)
            col_2 = data[100, 100]
            self.assertEqual(col_2[0], 208)
            self.assertEqual(col_2[1], 144)
            self.assertEqual(col_2[2], 102)
            self.assertEqual(col_2[3], 255)

    def test_image_file(self):
        self.start()

        image_file = gxgrd.image_file(self.g1f)
        with gxgrd.Grid.open(self.g1f) as g:
            with gxgrd.Grid.open(image_file + '(IMG,t=png)') as gi:
                self.assertEqual(g.coordinate_system, gi.coordinate_system)
                self.assertEqual(g.nx, gi.nx)
                self.assertEqual(g.ny, gi.ny)
                self.assertAlmostEqual(g.x0, gi.x0)
                self.assertAlmostEqual(g.y0, gi.y0)
                self.assertAlmostEqual(g.dx, gi.dx)
                self.assertAlmostEqual(g.dy, gi.dy)
                self.assertAlmostEqual(g.rot, gi.rot)

        with gxgrd.Grid.open(self.g1f) as g:
            with gxgrd.Grid.open(g.image_file() + '(IMG,t=png)') as gi:
                self.assertEqual(g.coordinate_system, gi.coordinate_system)
                self.assertEqual(g.nx, gi.nx)
                self.assertEqual(g.ny, gi.ny)
                self.assertAlmostEqual(g.x0, gi.x0)
                self.assertAlmostEqual(g.y0, gi.y0)
                self.assertAlmostEqual(g.dx, gi.dx)
                self.assertAlmostEqual(g.dy, gi.dy)
                self.assertAlmostEqual(g.rot, gi.rot)

        with gxgrd.Grid.open(self.g1f) as g:
            g.rot = 30
            with gxgrd.Grid.open(g.image_file(pix_width=800) + '(IMG,t=png)') as gi:
                self.assertEqual(g.coordinate_system, gi.coordinate_system)
                self.assertEqual(800, gi.nx)
                self.assertEqual(800, gi.ny)
                self.assertAlmostEqual(6.994032176517, gi.x0)
                self.assertAlmostEqual(43.494032176517, gi.y0)

###############################################################################################

if __name__ == '__main__':

    unittest.main()
