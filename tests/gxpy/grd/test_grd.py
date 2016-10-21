import unittest
import os,gc
import numpy as np

import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.ipj as gxipj
import geosoft.gxpy.grd as gxgrd

class Test(gx.GXTestCase):

    @classmethod
    def setUpClass(cls):
        cls.gx = gx.GXpy()
        cls.folder, files = gsys.unzip('.\\testdata.zip')
        cls.g1 = gxgrd.GXgrd.open(os.path.join(cls.folder, files[0]))
        cls.g2 = gxgrd.GXgrd.open(os.path.join(cls.folder, files[3]))
        pass

    @classmethod
    def tearDownClass(cls):
        del cls.g1
        del cls.g2
        gc.collect()
        try: gsys.remove_dir(cls.folder)
        except: pass

    
    @classmethod
    def start(cls,test):
        print("\n*** {} ***".format(test))
        os.chdir(os.path.dirname(os.path.realpath(__file__)))

    def test_gridProperties(self):
        self.start(gsys.func_name())

        properties = self.g1.properties()
        self.assertEqual(properties.get('dx'),0.01)
        self.assertEqual(properties.get('dy'),0.01)
        self.assertEqual(properties.get('x0'),7.0)
        self.assertEqual(properties.get('y0'),44.0)
        self.assertEqual(properties.get('rot'),0.0)
        self.assertEqual(properties.get('nx'),101)
        self.assertEqual(properties.get('ny'),101)
        self.assertEqual(str(properties.get('ipj')),'WGS 84')

    def test_saveGrid(self):
        self.start(gsys.func_name())

        #create a grids
        outGrid = os.path.join(self.folder, 'testNew.grd(GRD)')
        grd = self.g1.saveAs(outGrid)
        grd.deleteFiles()
        properties = grd.properties()
        self.assertEqual(properties.get('dx'),0.01)
        self.assertEqual(properties.get('dy'),0.01)
        self.assertEqual(properties.get('x0'),7.0)
        self.assertEqual(properties.get('y0'),44.0)
        self.assertEqual(properties.get('rot'),0.0)
        self.assertEqual(properties.get('nx'),101)
        self.assertEqual(properties.get('ny'),101)
        self.assertEqual(str(properties.get('ipj')),'WGS 84')

        del grd
        gc.collect()

    def test_setProperties(self):
        self.start(gsys.func_name())

        properties = self.g1.properties()
        properties['x0'] = 45.0
        properties['y0'] = -15.0
        properties['dx'] = 1.5
        properties['dy'] = 2.5
        properties['rot'] = -33.333333
        properties['ipj'] = gxipj.GXipj.from_name('NAD27 / UTM zone 18N')
        try:
            self.g1.setProperties(properties)
            self.assertTrue(False) #should not be able to set properties of a read-only grid
        except: pass

        outGrid = os.path.join(self.folder, 'testNew.grd(GRD;TYPE=SHORT;COMP=SPEED)')
        grd = self.g1.saveAs(outGrid)
        grd.setProperties(properties) #this should now work
        del grd

        grd = gxgrd.GXgrd.open(outGrid)
        properties = grd.properties()
        self.assertEqual(properties.get('dx'),1.5)
        self.assertEqual(properties.get('dy'),2.5)
        self.assertEqual(properties.get('x0'),45.0)
        self.assertEqual(properties.get('y0'),-15.0)
        self.assertEqual(properties.get('rot'),-33.333333)
        self.assertEqual(properties.get('nx'),101)
        self.assertEqual(properties.get('ny'),101)
        self.assertEqual(str(properties.get('ipj')),'NAD27 / UTM zone 18N')
        self.assertEqual(properties.get('dtype'),np.int16)

        del grd
        gc.collect()

    def test_memoryGrid(self):
        self.start(gsys.func_name())

        grd = gxgrd.GXgrd.new(properties={'dtype':np.int16,'nx': 100, 'ny': 50, 'x0':4, 'y0':8, 'dx': 0.1, 'dy':0.2,
                                          'rot': 5, 'ipj': gxipj.GXipj.from_name('NAD27 / UTM zone 18N')})
        properties = grd.properties()
        self.assertEqual(properties.get('dx'),0.1)
        self.assertEqual(properties.get('dy'),0.2)
        self.assertEqual(properties.get('x0'),4.0)
        self.assertEqual(properties.get('y0'),8.0)
        self.assertEqual(properties.get('rot'),5.0)
        self.assertEqual(properties.get('nx'),100)
        self.assertEqual(properties.get('ny'),50)
        self.assertEqual(str(properties.get('ipj')),'NAD27 / UTM zone 18N')
        self.assertEqual(properties.get('dtype'),np.int16)

        del grd
        gc.collect()

    def test_gridMosaic(self):
        self.start(gsys.func_name())

        m1s = os.path.join(self.folder, 'm1.grd(GRD)')
        m1 = self.g1.saveAs(m1s)
        m2s = os.path.join(self.folder, 'm2.grd(GRD)')
        m2 = self.g2.saveAs(m2s)
        del m1, m2
        gc.collect()

        glist = [m1s, m2s]

        mosaicGrid = os.path.join(self.folder, 'testMozaic.grd')
        grd = gxgrd.gridMosaic(mosaicGrid, glist, report=print)

        properties = grd.properties()
        self.assertAlmostEqual(properties.get('dx'),0.01)
        self.assertAlmostEqual(properties.get('dy'),0.01)
        self.assertAlmostEqual(properties.get('x0'),7.0)
        self.assertAlmostEqual(properties.get('y0'),44.0)
        self.assertEqual(properties.get('rot'),0.0)
        self.assertEqual(properties.get('nx'),201)
        self.assertEqual(properties.get('ny'),101)
        self.assertEqual(str(properties.get('ipj')),'WGS 84')

        m= os.path.join(self.folder, 'testMosaic.hgd(HGD)')
        grd = gxgrd.gridMosaic(m, glist, report=print)
        del grd
        gc.collect()

        grd = gxgrd.GXgrd.open(m)
        grd.deleteFiles()
        properties = grd.properties()
        self.assertAlmostEqual(properties.get('dx'),0.01)
        self.assertAlmostEqual(properties.get('dy'),0.01)
        self.assertAlmostEqual(properties.get('x0'),7.0)
        self.assertAlmostEqual(properties.get('y0'),44.0)
        self.assertEqual(properties.get('rot'),0.0)
        self.assertEqual(properties.get('nx'),201)
        self.assertEqual(properties.get('ny'),101)
        self.assertEqual(str(properties.get('ipj')),'WGS 84')

        del grd
        gc.collect()

    def test_gridBool(self):
        self.start(gsys.func_name())

        grd = gxgrd.gridBool(self.g1, self.g2, os.path.join(self.folder, 'testBool.grd(GRD;TYPE=SHORT)'), size=3)
        grd.deleteFiles()
        properties = grd.properties()
        self.assertAlmostEqual(properties.get('dx'),0.01)
        self.assertAlmostEqual(properties.get('dy'),0.01)
        self.assertAlmostEqual(properties.get('x0'),7.0)
        self.assertAlmostEqual(properties.get('y0'),44.0)
        self.assertEqual(properties.get('rot'),0.0)
        self.assertEqual(properties.get('nx'),201)
        self.assertEqual(properties.get('ny'),101)
        self.assertEqual(str(properties.get('ipj')),'WGS 84')
        self.assertEqual(properties.get('dtype'),np.int16)

        del grd
        gc.collect()

    def test_deleteGridFiles(self):
        self.start(gsys.func_name())

        def makefile(): #to force garbage collection on exit
            g2 = self.g1.saveAs(os.path.join(self.folder,'testDelete.grd'))
            g2.deleteFiles()
            s = str(g2).split('(')[0]
            del g2
            gc.collect()
            return s

        filen = makefile()
        self.assertFalse(os.path.isfile(filen))
        self.assertFalse(os.path.isfile(filen+'.gi'))
        self.assertFalse(os.path.isfile(filen+'.xml'))

    def test_hgd(self):
        self.start(gsys.func_name())

        g = self.g1
        ofile = gxgrd.GXgrd.decorateName(os.path.join(self.folder, 'test.hgd'), 'HGD')
        g2 = g.saveAs(ofile)
        properties = g2.properties()
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
        self.assertEqual(str(properties.get('ipj')),'WGS 84')

        del g,g2
        gc.collect()

    def test_nameParts(self):
        self.start(gsys.func_name())

        namep = gxgrd.GXgrd.nameParts("f:/someFolder/name.grd(GRD;TYPE=SHORT)")
        self.assertEqual(namep,('f:\\someFolder', 'name.grd', 'name', '.grd', 'GRD;TYPE=SHORT'))

        namep = gxgrd.GXgrd.nameParts(".\\name.grd(GRD;TYPE=SHORT)")
        self.assertEqual(namep[0],os.getcwd())
        self.assertEqual(namep[1:],('name.grd', 'name', '.grd', 'GRD;TYPE=SHORT'))

        namep = gxgrd.GXgrd.nameParts(".\\name.grd")
        self.assertEqual(namep[0],os.getcwd())
        self.assertEqual(namep[1:],('name.grd', 'name', '.grd', ''))

        ref = 'billybob(decs;more)'
        name = gxgrd.GXgrd.decorateName('billybob','(decs;more)')
        self.assertEqual(name,ref)
        name = gxgrd.GXgrd.decorateName('billybob','decs;more')
        self.assertEqual(name,ref)
        name = gxgrd.GXgrd.decorateName('billybob','(decs;more')
        self.assertEqual(name,ref)
        name = gxgrd.GXgrd.decorateName('billybob','decs;more)')
        self.assertEqual(name,ref)
        name = gxgrd.GXgrd.decorateName('billybob','decs;more)(and more)')
        self.assertEqual(name,ref)
        name = gxgrd.GXgrd.decorateName(ref)
        self.assertEqual(name,ref)

    def test_indexWindow(self):
        self.start(gsys.func_name())

        g = self.g1
        p = g.properties()
        window = os.path.join(self.folder,'testwindow.grd(GRD)')

        gw = g.indexWindow(window,4,2,96,5)
        pw = gw.properties()
        dx = p.get('dx')
        self.assertAlmostEqual(pw.get('x0'),p.get('x0')+(4*dx))
        dy = p.get('dy')
        self.assertAlmostEqual(pw.get('y0'),p.get('y0')+(2*dy))
        self.assertEqual(pw.get('nx'),96)
        self.assertEqual(pw.get('ny'),5)
        del gw; gc.collect()

        gw = g.indexWindow(window,nx=20,ny=100)
        pw = gw.properties()
        self.assertAlmostEqual(pw.get('x0'),p.get('x0'))
        self.assertAlmostEqual(pw.get('y0'),p.get('y0'))
        self.assertEqual(pw.get('nx'),20)
        self.assertEqual(pw.get('ny'),100)
        del gw; gc.collect()

        gw = g.indexWindow(window,x0=29,y0=100)
        pw = gw.properties()
        dx = p.get('dx')
        self.assertAlmostEqual(pw.get('x0'),p.get('x0')+(29*dx))
        dy = p.get('dy')
        self.assertAlmostEqual(pw.get('y0'),p.get('y0')+(100*dy))
        self.assertEqual(pw.get('nx'),72)
        self.assertEqual(pw.get('ny'),1)
        del gw; gc.collect()

        try:
            g.indexWindow(window,x0=2900,y0=3600,ny=2)
            self.assertFalse(True)
        except: pass

        try:
            g.indexWindow(window,-1)
            self.assertFalse(True)
        except: pass

        try:
            g.indexWindow(window,y0=-1)
            self.assertFalse(True)
        except: pass

    def test_from_array(self):
        self.start(gsys.func_name())

        filename = ".\\testdata\\test_array.grd"

        data = np.arange(24).reshape((8,3))
        grd = gxgrd.GXgrd.from_data_array(data, filename)
        grd.deleteFiles()
        properties = grd.properties()
        self.assertEqual(properties.get('dx'),1.0)
        self.assertEqual(properties.get('dy'),1.0)
        self.assertEqual(properties.get('x0'),0.0)
        self.assertEqual(properties.get('y0'),0.0)
        self.assertEqual(properties.get('rot'),0.0)
        self.assertEqual(properties.get('nx'),3)
        self.assertEqual(properties.get('ny'),8)
        self.assertEqual(str(properties.get('ipj')),'*unknown')
        del grd

        grd = gxgrd.GXgrd.from_data_array(data, filename, properties={'x0':575268, 'dx':2.0, 'dy':1.5, 'rot':15, 'ipj':'WGS 84'})
        grd.deleteFiles()
        properties = grd.properties()
        self.assertEqual(properties.get('dx'),2.0)
        self.assertEqual(properties.get('dy'),1.5)
        self.assertEqual(properties.get('x0'),575268.0)
        self.assertEqual(properties.get('y0'),0.0)
        self.assertEqual(properties.get('rot'),15.0)
        self.assertEqual(properties.get('nx'),3)
        self.assertEqual(properties.get('ny'),8)
        self.assertEqual(str(properties.get('ipj')),'WGS 84')
        del grd


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


###############################################################################################

if __name__ == '__main__':

    unittest.main()
