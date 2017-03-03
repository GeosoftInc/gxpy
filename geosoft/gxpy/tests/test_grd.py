import unittest
import os
import numpy as np

import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.grd as gxgrd
import geosoft

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gx = gx.GXpy(log=print, res_stack=4)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                       folder=cls.gx.temp_folder())
        cls.g1f = os.path.join(cls.folder, 'test_grid_1.grd')
        cls.g2f = os.path.join(cls.folder, 'test_grid_2.grd')
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def start(cls,test):
        cls.gx.log("*** {} > {}".format(os.path.split(__file__)[1], test))

    def test_grc(self):
        self.start(gsys.func_name())
        self.assertEqual(gxgrd.__version__, geosoft.__version__)

    def test_gridProperties(self):
        self.start(gsys.func_name())

        with gxgrd.GXgrd.open(self.g1f) as g1:
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


    def test_saveGrid(self):
        self.start(gsys.func_name())

        #create a grids
        outGrid = os.path.join(self.folder, 'testNew.grd(GRD)')
        with gxgrd.GXgrd.open(self.g1f) as g:
            grd = g.save_as(outGrid)
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
            grd.close()

    def test_set_properties(self):
        self.start(gsys.func_name())

        with gxgrd.GXgrd.open(self.g1f) as g1:
            properties = g1.properties()
            properties['x0'] = 45.0
            properties['y0'] = -15.0
            properties['dx'] = 1.5
            properties['dy'] = 2.5
            properties['rot'] = -33.333333
            properties['cs'] = gxcs.GXcs('NAD27 / UTM zone 18N')
            self.assertRaises( gxgrd.GRDException, g1.set_properties, properties)

        outGrid = os.path.join(self.folder, 'testNew.grd(GRD;TYPE=SHORT;COMP=SPEED)')
        with gxgrd.GXgrd.open(self.g1f) as g:
            grd = g.save_as(outGrid)
            grd.dx = 1.5
            grd.dy = 2.5
            grd.x0 = 45.0
            grd.y0 = -15.0
            grd.rot = -33.333333
            grd.cs = gxcs.GXcs('NAD27 / UTM zone 18N')
            grd.close()

        with gxgrd.GXgrd.open(outGrid) as grd:
            properties = grd.properties()
            self.assertEqual(properties.get('dx'),1.5)
            self.assertEqual(properties.get('dy'),2.5)
            self.assertEqual(properties.get('x0'),45.0)
            self.assertEqual(properties.get('y0'),-15.0)
            self.assertEqual(properties.get('rot'),-33.333333)
            self.assertEqual(properties.get('nx'),101)
            self.assertEqual(properties.get('ny'),101)
            self.assertEqual(str(properties.get('cs')),'NAD27 / UTM zone 18N')
            self.assertEqual(properties.get('dtype'),np.int16)

        outGrid = os.path.join(self.folder, 'testNew.grd(GRD;TYPE=SHORT;COMP=SPEED)')
        with gxgrd.GXgrd.open(self.g1f) as g:
            grd = g.save_as(outGrid)
            grd.set_properties(properties)
            grd.close()

        with gxgrd.GXgrd.open(outGrid) as grd:
            properties = grd.properties()
            self.assertEqual(properties.get('dx'),1.5)
            self.assertEqual(properties.get('dy'),2.5)
            self.assertEqual(properties.get('x0'),45.0)
            self.assertEqual(properties.get('y0'),-15.0)
            self.assertEqual(properties.get('rot'),-33.333333)
            self.assertEqual(properties.get('nx'),101)
            self.assertEqual(properties.get('ny'),101)
            self.assertEqual(str(properties.get('cs')),'NAD27 / UTM zone 18N')
            self.assertEqual(properties.get('dtype'),np.int16)

    def test_memoryGrid(self):
        self.start(gsys.func_name())

        with gxgrd.GXgrd.new(properties={'dtype': np.int16,
                                         'nx': 100, 'ny': 50,
                                         'x0':4, 'y0':8,
                                         'dx': 0.1, 'dy':0.2,
                                         'rot': 5,
                                         'cs': gxcs.GXcs('NAD27 / UTM zone 18N')}) as grd:
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

    def test_gridMosaic(self):
        self.start(gsys.func_name())

        with gxgrd.GXgrd.open(self.g1f) as g:
            m1s = os.path.join(self.folder, 'm1.grd(GRD)')
            g.save_as(m1s).close()
        with gxgrd.GXgrd.open(self.g2f) as g:
            m2s = os.path.join(self.folder, 'm2.grd(GRD)')
            g.save_as(m2s).close()

        glist = [m1s, m2s]

        mosaicGrid = os.path.join(self.folder, 'testMozaic.grd')
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

        m = os.path.join(self.folder, 'testMosaic.hgd(HGD)')
        gxgrd.gridMosaic(m, glist).close()

        with gxgrd.GXgrd.open(m) as grd:
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

    def test_gridBool(self):
        self.start(gsys.func_name())

        g1 = gxgrd.GXgrd.open(self.g1f)
        g2 = gxgrd.GXgrd.open(self.g2f)
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

    def test_deleteGridFiles(self):
        self.start(gsys.func_name())

        with gxgrd.GXgrd.open(self.g1f) as g:
            g2 = g.save_as(os.path.join(self.folder,'testDelete.grd'))
            filen = g2.filename
            g2.delete_files()
            g2.close()

        self.assertFalse(os.path.isfile(filen))
        self.assertFalse(os.path.isfile(filen+'.gi'))
        self.assertFalse(os.path.isfile(filen+'.xml'))

    def test_hgd(self):
        self.start(gsys.func_name())

        with gxgrd.GXgrd.open(self.g1f) as g:
            ofile = gxgrd.GXgrd.decorate_name(os.path.join(self.folder, 'test.hgd'), 'HGD')
            g2 = g.save_as(ofile)
            properties = g2.properties()
            g2.close()
            self.assertEqual(properties.get('filename'),os.path.abspath(ofile.split('(')[0]))
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
        self.start(gsys.func_name())

        namep = gxgrd.GXgrd.name_parts("f:/someFolder/name.grd(GRD;TYPE=SHORT)")
        self.assertEqual(namep,('f:\\someFolder', 'name.grd', 'name', '.grd', 'GRD;TYPE=SHORT'))

        namep = gxgrd.GXgrd.name_parts(".\\name.grd(GRD;TYPE=SHORT)")
        self.assertEqual(namep[0],os.getcwd())
        self.assertEqual(namep[1:],('name.grd', 'name', '.grd', 'GRD;TYPE=SHORT'))

        namep = gxgrd.GXgrd.name_parts(".\\name.grd")
        self.assertEqual(namep[0],os.getcwd())
        self.assertEqual(namep[1:],('name.grd', 'name', '.grd', ''))

        ref = 'billybob(decs;more)'
        name = gxgrd.GXgrd.decorate_name('billybob','(decs;more)')
        self.assertEqual(name,ref)
        name = gxgrd.GXgrd.decorate_name('billybob','decs;more')
        self.assertEqual(name,ref)
        name = gxgrd.GXgrd.decorate_name('billybob','(decs;more')
        self.assertEqual(name,ref)
        name = gxgrd.GXgrd.decorate_name('billybob','decs;more)')
        self.assertEqual(name,ref)
        name = gxgrd.GXgrd.decorate_name('billybob','decs;more)(and more)')
        self.assertEqual(name,ref)
        name = gxgrd.GXgrd.decorate_name(ref)
        self.assertEqual(name,ref)

    def test_index_window(self):
        self.start(gsys.func_name())

        with gxgrd.GXgrd.open(self.g1f) as g:
            p = g.properties()
            window = os.path.join(self.folder,'testwindow.grd(GRD)')

            gw = g.index_window(window,4,2,96,5)
            pw = gw.properties()
            self.assertAlmostEqual(gw.x0, g.x0+(4*g.dx))
            self.assertAlmostEqual(gw.y0, g.y0+(2*g.dy))
            self.assertEqual(gw.nx, 96)
            self.assertEqual(gw.ny, 5)
            gw.close()

            gw = g.index_window(window,nx=20,ny=100)
            pw = gw.properties()
            self.assertAlmostEqual(pw.get('x0'),p.get('x0'))
            self.assertAlmostEqual(pw.get('y0'),p.get('y0'))
            self.assertEqual(pw.get('nx'),20)
            self.assertEqual(pw.get('ny'),100)
            gw.close()

            gw = g.index_window(window,x0=29,y0=100)
            pw = gw.properties()
            dx = p.get('dx')
            self.assertAlmostEqual(pw.get('x0'),p.get('x0')+(29*dx))
            dy = p.get('dy')
            self.assertAlmostEqual(pw.get('y0'),p.get('y0')+(100*dy))
            self.assertEqual(pw.get('nx'),72)
            self.assertEqual(pw.get('ny'),1)
            gw.close()

            self.assertRaises(gxgrd.GRDException, g.index_window, window, x0=2900, y0=3600, ny=2)
            self.assertRaises(gxgrd.GRDException, g.index_window, window,-1)
            self.assertRaises(gxgrd.GRDException, g.index_window, window, y0=-1)

        with gxgrd.GXgrd.open(self.g1f) as g:
            window = os.path.join(self.folder, 'testwindow.grd(GRD)')
            gw = g.index_window(window, 4, 2, 96, 5)
            exmin, exmax = gw.extent_2d()
            self.assertAlmostEqual(exmin[0], 7.04)
            self.assertAlmostEqual(exmin[1], 44.02)
            self.assertAlmostEqual(exmax[0], 7.99)
            self.assertAlmostEqual(exmax[1], 44.06)
            gw.close()

            g.rot = 10.0
            window = os.path.join(self.folder, 'testwindow.grd(GRD)')
            gw = g.index_window(window, 4, 2, 96, 5)
            exmin, exmax = gw.extent_2d()
            self.assertAlmostEqual(exmin[0], 7.028973419460472)
            self.assertAlmostEqual(exmin[1], 44.02664208216692)
            self.assertAlmostEqual(exmax[0], 7.971486711928748)
            self.assertAlmostEqual(exmax[1], 44.231000161070995)
            gw.close()


    def test_from_array(self):
        self.start(gsys.func_name())

        filename = os.path.join(self.folder, "test_array.grd")

        data = np.arange(24).reshape((8,3))
        with gxgrd.GXgrd.from_data_array(data, filename) as grd:
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

        with gxgrd.GXgrd.from_data_array(data, filename,
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
        self.start(gsys.func_name())

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
        self.start(gsys.func_name())

        g1 = gxgrd.GXgrd.open(self.g1f)
        g2 = gxgrd.GXgrd.open(self.g2f)
        rs = len(gx._res_heap)
        self.assertTrue(rs >= 2)
        g1.close()
        self.assertEqual(len(gx._res_heap), rs-1)
        g2.close()

    def test_extent(self):
        self.start(gsys.func_name())

        with gxgrd.GXgrd.open(self.g1f) as g:
            grd = g.save_as(os.path.join(self.folder, 'test_extent.grd(GRD)'))
            grd.delete_files()
            grd.x0 = grd.y0 = 0.0
            grd.dx = grd.dy = 0.1
            grd.rot = 30.0

            mn, mx = grd.extent_2d()
            self.assertAlmostEqual(mn[0], -5.0)
            self.assertAlmostEqual(mn[1], 0.0)
            self.assertAlmostEqual(mx[0], 8.66025404)
            self.assertAlmostEqual(mx[1], 13.66025404)

            cs = grd.cs
            cs_name = cs.name(gxcs.NAME_HCS_VCS) + ' <0,0,0,-90,0,45>'
            grd.cs = gxcs.GXcs(cs_name)
            grd.x0 = grd.y0 = 0.0
            grd.dx = grd.dy = 0.1
            grd.rot = 0.0
            mn, mx = grd.extent_3d()
            self.assertAlmostEqual(mx[0], 7.0710678118654755)
            self.assertAlmostEqual(mx[1], 0.0)
            self.assertAlmostEqual(mx[2], 10.0)
            self.assertAlmostEqual(mn[0], 0.0)
            self.assertAlmostEqual(mn[1], -7.0710678118654755)
            self.assertAlmostEqual(mn[2], 0.0)

            grd.rot = 30.0
            mn, mx = grd.extent_3d()
            self.assertAlmostEqual(mx[0], 6.123724356957947)
            self.assertAlmostEqual(mx[1], 3.5355339059327378)
            self.assertAlmostEqual(mx[2], 13.660254037844386)
            self.assertAlmostEqual(mn[0], -3.5355339059327373)
            self.assertAlmostEqual(mn[1], -6.123724356957946)
            self.assertAlmostEqual(mn[2], 0.0)

            grd.close()


###############################################################################################

if __name__ == '__main__':

    unittest.main()
