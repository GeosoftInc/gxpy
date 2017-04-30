import unittest
import os
import numpy as np

import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.grd as gxgrd
import geosoft

from geosoft.gxpy.tests import GXPYTest


class Test(GXPYTest):
    @classmethod
    def setUpClass(cls):
        GXPYTest.setUpGXPYTest()
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                       folder=cls._gx.temp_folder())
        cls.g1f = os.path.join(cls.folder, 'test_grid_1.grd')
        cls.g2f = os.path.join(cls.folder, 'test_grid_2.grd')

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
            self.assertEqual(properties.get('nx'),101)
            self.assertEqual(properties.get('ny'),101)
            self.assertEqual(str(properties.get('cs')),'WGS 84')

            self.assertEqual(g1.dx, 0.01)
            self.assertEqual(g1.dy, 0.01)
            self.assertEqual(g1.x0, 7.0)
            self.assertEqual(g1.y0, 44.0)
            self.assertEqual(g1.rot, 0.0)
            self.assertEqual(g1.nx, 101)
            self.assertEqual(g1.ny, 101)
            self.assertEqual(str(g1.cs), 'WGS 84')


    def test_copy(self):
        self.start()

        #create a grids
        outGrid = os.path.join(self.folder, 'testNew.grd(GRD)')
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
                self.assertEqual(str(properties.get('cs')),'WGS 84')

    def test_set_properties(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g1:
            properties = g1.properties()
            properties['x0'] = 45.0
            properties['y0'] = -15.0
            properties['dx'] = 1.5
            properties['dy'] = 2.5
            properties['rot'] = 33.333333
            properties['cs'] = gxcs.Coordinate_system('NAD27 / UTM zone 18N')
            self.assertRaises( gxgrd.GRDException, g1.set_properties, properties)

        outGrid = os.path.join(self.folder, 'testNew.grd(GRD;TYPE=SHORT;COMP=SPEED)')
        with gxgrd.Grid.open(self.g1f) as g:
            with gxgrd.Grid.copy(g, outGrid) as grd:
                grd.dx = 1.5
                grd.dy = 2.5
                grd.x0 = 45.0
                grd.y0 = -15.0
                grd.rot = 33.333333
                grd.cs = gxcs.Coordinate_system('NAD27 / UTM zone 18N')

        with gxgrd.Grid.open(outGrid) as grd:
            properties = grd.properties()
            self.assertEqual(properties.get('dx'),1.5)
            self.assertEqual(properties.get('dy'),2.5)
            self.assertEqual(properties.get('x0'),45.0)
            self.assertEqual(properties.get('y0'),-15.0)
            self.assertEqual(properties.get('rot'),33.333333)
            self.assertEqual(properties.get('nx'),101)
            self.assertEqual(properties.get('ny'),101)
            self.assertEqual(str(properties.get('cs')),'NAD27 / UTM zone 18N')
            self.assertEqual(properties.get('dtype'),np.int16)

        outGrid = os.path.join(self.folder, 'testNew.grd(GRD;TYPE=SHORT;COMP=SPEED)')
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
            self.assertEqual(str(properties.get('cs')),'NAD27 / UTM zone 18N')
            self.assertEqual(properties.get('dtype'),np.int16)

    def test_memory(self):
        self.start()

        with gxgrd.Grid.new(properties={'dtype': np.int16,
                                         'nx': 100, 'ny': 50,
                                         'x0':4, 'y0':8,
                                         'dx': 0.1, 'dy':0.2,
                                         'rot': 5,
                                         'cs': gxcs.Coordinate_system('NAD27 / UTM zone 18N')}) as grd:
            properties = grd.properties()
            self.assertEqual(properties.get('dx'),0.1)
            self.assertEqual(properties.get('dy'),0.2)
            self.assertEqual(properties.get('x0'),4.0)
            self.assertEqual(properties.get('y0'),8.0)
            self.assertEqual(properties.get('rot'),5.0)
            self.assertEqual(properties.get('nx'),100)
            self.assertEqual(properties.get('ny'),50)
            self.assertEqual(str(properties.get('cs')),'NAD27 / UTM zone 18N')
            self.assertEqual(properties.get('dtype'),np.int16)

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
            self.assertEqual(str(properties.get('cs')),'WGS 84')

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
            self.assertEqual(str(properties.get('cs')),'WGS 84')

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
        self.assertEqual(str(properties.get('cs')),'WGS 84')
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
        self.assertEqual(str(properties.get('cs')), 'WGS 84')
        self.assertEqual(properties.get('dtype'), np.int16)

    def test_delete_grid(self):
        self.start()

        self.assertRaises(gxgrd.GRDException, gxgrd.Grid.new, self.g1f)
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
            self.assertEqual(str(properties.get('cs')),'WGS 84')

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

            with gxgrd.Grid.index_window(g, window, 4, 2, 96, 5) as gw:
                pw = gw.properties()
                self.assertAlmostEqual(gw.x0, g.x0+(4*g.dx))
                self.assertAlmostEqual(gw.y0, g.y0+(2*g.dy))
                self.assertEqual(gw.nx, 96)
                self.assertEqual(gw.ny, 5)

            with gxgrd.Grid.index_window(g, x0=4, y0=2, nx=96, ny=5, overwrite=True) as gw:
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

            self.assertRaises(gxgrd.GRDException, gxgrd.Grid.index_window, g, window, x0=2900, y0=3600, ny=2)
            self.assertRaises(gxgrd.GRDException, gxgrd.Grid.index_window, g, window, -1)
            self.assertRaises(gxgrd.GRDException, gxgrd.Grid.index_window, g, window, y0=-1)

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
            self.assertEqual(str(properties.get('cs')),'*unknown')

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
            self.assertEqual(str(properties.get('cs')),'*unknown')

        with gxgrd.Grid.from_data_array(data, file_name,
                                         properties={'x0':575268, 'dx':2.0, 'dy':1.5, 'rot':15, 'cs':'WGS 84'}) as grd:
            grd.delete_files()
            properties = grd.properties()
            self.assertEqual(properties.get('dx'),2.0)
            self.assertEqual(properties.get('dy'),1.5)
            self.assertEqual(properties.get('x0'),575268.0)
            self.assertEqual(properties.get('y0'),0.0)
            self.assertEqual(properties.get('rot'),15.0)
            self.assertEqual(properties.get('nx'),3)
            self.assertEqual(properties.get('ny'),8)
            self.assertEqual(str(properties.get('cs')),'WGS 84')

    def test_array_locations(self):
        self.start()

        props = {'x0':100, 'y0':-25.25, 'dx': 5, 'nx':101, 'ny':501}
        a = gxgrd.array_locations(props)
        self.assertEqual(len(a.shape),3)
        self.assertEqual(a.shape[0], props.get('ny'))
        self.assertEqual(a.shape[1], props.get('nx'))
        self.assertEqual(a.shape[2], 3)
        self.assertEqual(a[0,0,0], 100.0)
        self.assertEqual(a[0,0,1], -25.25)
        self.assertEqual(a[0,0,2], 0.0)
        self.assertEqual(a[0,1,0]-a[0,0,0], props.get('dx'))
        self.assertEqual(a[1,0,1]-a[0,0,1], props.get('dx'))
        self.assertEqual(a[0,0,2]-a[1,1,2], 0.)

        props = {'x0':100, 'y0':-25.25, 'dx': 5, 'dy': 1, 'nx':101, 'ny':501}
        a = gxgrd.array_locations(props, z=10.1)
        self.assertEqual(len(a.shape),3)
        self.assertEqual(a.shape[0], props.get('ny'))
        self.assertEqual(a.shape[1], props.get('nx'))
        self.assertEqual(a.shape[2], 3)
        self.assertEqual(a[0,0,0], 100.0)
        self.assertEqual(a[0,0,1], -25.25)
        self.assertEqual(a[0,0,2], 10.1)
        self.assertEqual(a[0,1,0]-a[0,0,0], props.get('dx'))
        self.assertEqual(a[1,0,1]-a[0,0,1], props.get('dy'))
        self.assertEqual(a[0,0,2]-a[1,1,2], 0.)

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

                cs = grd.cs
                cs_name = cs.cs_name(gxcs.NAME_HCS_VCS) + ' <0,0,0,0,0,30>'
                grd.cs = gxcs.Coordinate_system(cs_name)
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
                grd.cs = gxcs.Coordinate_system(cs_name)
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


###############################################################################################

if __name__ == '__main__':

    unittest.main()
