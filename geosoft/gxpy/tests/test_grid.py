import unittest
import os
import numpy as np

import geosoft
import geosoft.gxapi as gxa
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.map as gxmap
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
        cls.mag = os.path.join(cls.folder, 'mag.grd')
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py), 'section_grids.zip'),
                                       folder=cls._gx.temp_folder())
        cls.section = os.path.join(cls.folder, 'section.grd')
        cls.swing = os.path.join(cls.folder, 'swing_section.grd')
        cls.crooked = os.path.join(cls.folder, 'crooked_section.grd')

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
        with gxgrd.Grid.open(self.gcf) as gc:
            properties = gc.properties()
            self.assertEqual(properties.get('is_color'),True)
            self.assertEqual(gc.is_color, True)

    def test_statistics(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g1:
            stats = g1.statistics()
            self.assertAlmostEqual(stats['mean'], 997.2176063303659)
            self.assertEqual(stats['num_data'] + stats['num_dummy'], g1.nx * g1.ny)

    def test_copy(self):
        self.start()

        #create a grids
        outGrid = os.path.join(self.folder, 'test_copy')
        with gxgrd.Grid.open(self.g1f) as g:
            mean = g.statistics()['mean']
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
                self.assertAlmostEqual(grd.statistics()['mean'], mean)

        # temporary grid copy
        with gxgrd.Grid.open(self.g1f) as g:
            mean = g.statistics()['mean']
            with gxgrd.Grid.copy(g) as grd:
                self.assertAlmostEqual(grd.statistics()['mean'], mean)

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

    def test_in_memory(self):
        self.start()

        with gxgrd.Grid.new(in_memory=True,
            properties={'dtype': np.int16,
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

            stats = grd.statistics()
            self.assertTrue(stats['mean'] is None)

    def test_from_pg(self):
        self.start()

        with gxgrd.Grid.open(self.mag) as grd:
            magpg = grd.gxpg()
            with gxgrd.Grid.from_data_array(magpg, properties=grd.properties()) as newpg:
                self.assertEqual(newpg.nx, grd.nx)


    def test_temp(self):
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
                g2.delete_files()
                properties = g2.properties()
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
                self.assertAlmostEqual(ex[0], 7.035)
                self.assertAlmostEqual(ex[1], 44.015)
                self.assertAlmostEqual(ex[2], 7.995)
                self.assertAlmostEqual(ex[3], 44.065)

            g.rot = 10.0
            window = os.path.join(self.folder, 'testwindow.grd(GRD)')
            with gxgrd.Grid.index_window(g, window, 4, 2, 96, 5, overwrite=True) as gw:
                gw.delete_files()
                ex = gw.extent_2d()
                self.assertAlmostEqual(ex[0], 6.9513424466727765)
                self.assertAlmostEqual(ex[1], 43.81649172360945)
                self.assertAlmostEqual(ex[2], 7.905440298447842)
                self.assertAlmostEqual(ex[3], 44.032434361820314)

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
                self.assertAlmostEqual(ex[0], -0.05)
                self.assertAlmostEqual(ex[1], -0.05)
                self.assertAlmostEqual(ex[2], 10.05)
                self.assertAlmostEqual(ex[3], 10.05)

                grd.rot = 30.0
                ex = grd.extent_2d()
                self.assertAlmostEqual(ex[0], -0.06830127018922194)
                self.assertAlmostEqual(ex[1], -5.068301270189221)
                self.assertAlmostEqual(ex[2], 13.72855530803361)
                self.assertAlmostEqual(ex[3], 8.72855530803361)

                cs = grd.coordinate_system
                cs_name = cs.cs_name(gxcs.NAME_HCS_VCS) + ' <0,0,0,0,0,30>'
                grd.coordinate_system = gxcs.Coordinate_system(cs_name)
                ex = grd.extent_2d()
                self.assertAlmostEqual(ex[0], -0.06830127018922194)
                self.assertAlmostEqual(ex[1], -5.068301270189221)
                self.assertAlmostEqual(ex[2], 13.72855530803361)
                self.assertAlmostEqual(ex[3], 8.72855530803361)

                grd.rot = 0
                ex = grd.extent_2d()
                self.assertAlmostEqual(ex[0], -0.05)
                self.assertAlmostEqual(ex[1], -0.05)
                self.assertAlmostEqual(ex[2], 10.05)
                self.assertAlmostEqual(ex[3], 10.05)
                ex = grd.extent_3d()
                self.assertAlmostEqual(ex[0], -0.06830127018922)
                self.assertAlmostEqual(ex[1], -5.068301270189221)
                self.assertAlmostEqual(ex[2], 0.0)
                self.assertAlmostEqual(ex[3], 13.72855530803361)
                self.assertAlmostEqual(ex[4], 8.72855530803361)
                self.assertAlmostEqual(ex[5], 0)

                cs_name = cs.cs_name(gxcs.NAME_HCS_VCS) + ' <0,0,0,90,0,30>'
                grd.coordinate_system = gxcs.Coordinate_system(cs_name)
                ex = grd.extent_3d()
                self.assertAlmostEqual(ex[0], -0.04330127018922194)
                self.assertAlmostEqual(ex[1], -5.025)
                self.assertAlmostEqual(ex[2], -10.05)
                self.assertAlmostEqual(ex[3], 8.70355530803360)
                self.assertAlmostEqual(ex[4], 0.025)
                self.assertAlmostEqual(ex[5], 0.05)

                grd.rot = 30.0
                ex = grd.extent_2d()
                self.assertAlmostEqual(ex[0], -0.0683012701892219)
                self.assertAlmostEqual(ex[1], -5.068301270189221)
                self.assertAlmostEqual(ex[2], 13.72855530803361)
                self.assertAlmostEqual(ex[3], 8.72855530803361)
                ex = grd.extent_3d()
                self.assertAlmostEqual(ex[0], -0.05915063509461113)
                self.assertAlmostEqual(ex[1], -6.864277654016804)
                self.assertAlmostEqual(ex[2], -8.72855530803361)
                self.assertAlmostEqual(ex[3], 11.889277654016805)
                self.assertAlmostEqual(ex[4], 0.03415063509461143)
                self.assertAlmostEqual(ex[5], 5.068301270189221)

    def test_read(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g:
            for row in range(g.ny):
                vv = g.read_row(row)
                self.assertEqual(vv.length, g.nx)

            for col in range(g.nx):
                vv = g.read_column(col)
                self.assertEqual(vv.length, g.ny)

    def test_write(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g:
            with gxgrd.Grid.new(properties=g.properties()) as gwr:
                for row in range(g.ny):
                    gwr.write_row(g.read_row(row), row)

            with gxgrd.Grid.new(properties=g.properties()) as gwc:
                for col in range(g.nx):
                    gwc.write_column(g.read_column(col))


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

        with gxgrd.Grid.open(self.g1f, mode=gxgrd.FILE_READWRITE) as g:
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

        with gxgrd.Grid.open(self.g1f, mode=gxgrd.FILE_READWRITE) as g:

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
        self.assertEqual(gxmap.Map.open(map_file).crc_image(pix_width=800), 2301553865)

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

    def test_expression(self):
        self.start()

        with gxgrd.Grid.open(self.mag) as grd:
            x = gxgrd.expression({'first': grd, 'second': grd}, 'first-second')
            self.assertEqual(x.statistics()['mean'], 0.)

        with gxgrd.Grid.open(self.mag) as grd:
            x = gxgrd.expression((grd, grd), 'g1-g2')
            self.assertEqual(x.statistics()['mean'], 0.)

    def test_default_color_map(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g1:
            cm = g1.get_default_color_map()
            self.assertEqual(gxa.ITR_ZONE_EQUALAREA, cm.model_type)
            self.assertEqual(39, cm.length)
            v, rgb = cm.color_map_rgb[0]
            self.assertAlmostEqual(231.6705835, v)
            self.assertEqual(0, rgb[0])
            self.assertEqual(0, rgb[1])
            self.assertEqual(255, rgb[2])
            limits = cm.data_limits
            self.assertAlmostEqual(157, limits[0])
            self.assertAlmostEqual(3187, limits[1])

    def test_default_color_map_none_set(self):
        self.start()

        with gxgrd.Grid.open(self.mag) as g1:
            cm = g1.get_default_color_map()
            self.assertEqual(gxa.ITR_ZONE_EQUALAREA, cm.model_type)
            self.assertEqual(39, cm.length)
            v, rgb = cm.color_map_rgb[0]
            self.assertAlmostEqual(4748.27257047, v)
            self.assertEqual(0, rgb[0])
            self.assertEqual(0, rgb[1])
            self.assertEqual(255, rgb[2])
            limits = cm.data_limits
            self.assertAlmostEqual(3796.711425781, limits[0])
            self.assertAlmostEqual(6295.0, limits[1])

    def test_uom(self):
        self.start()

        uom = gxgrd.Grid.open(self.mag).unit_of_measure
        with gxgrd.Grid.open(self.mag) as g:
            g.unit_of_measure = 'maki'
            self.assertEqual(g.unit_of_measure, 'maki')
        self.assertEqual(gxgrd.Grid.open(self.mag).unit_of_measure, uom)

        with gxgrd.Grid.open(self.mag, mode=gxgrd.FILE_READWRITE) as g:
            g.unit_of_measure = 'maki'
            self.assertEqual(g.unit_of_measure, 'maki')
        self.assertEqual(gxgrd.Grid.open(self.mag).unit_of_measure, 'maki')

    def test_reproject(self):
        self.start()

        gxgrd.Grid.open(self.mag, mode=gxgrd.FILE_READWRITE).coordinate_system = "NAD27 / UTM zone 32N"
        with gxgrd.Grid.open(self.mag) as g:
            self.assertEqual(str(g.coordinate_system), "NAD27 / UTM zone 32N")

        with gxgrd.Grid.open(self.mag, coordinate_system="NAD83 / UTM zone 32N") as g:
            self.assertEqual(str(g.coordinate_system), "NAD83 / UTM zone 32N")

        with gxgrd.Grid.open(self.mag, coordinate_system="WGS 84") as g:
            self.assertEqual(str(g.coordinate_system), "WGS 84")

        with gxgrd.Grid.open(self.mag, coordinate_system='', cell_size=75) as g:
            self.assertEqual(g.dx, 75.)
            self.assertEqual(g.dy, 75.)
            self.assertEqual(g.nx, 125)
            self.assertEqual(g.ny, 191)

        with gxgrd.Grid.open(self.mag, cell_size=75, expand=25) as g:
            self.assertEqual(g.dx, 75.)
            self.assertEqual(g.dy, 75.)
            self.assertEqual(g.nx, 183)
            self.assertEqual(g.ny, 280)

    def test_section(self):
        self.start()
        with gxgrd.Grid.open(self.section) as sect:
            self.assertTrue(sect.coordinate_system.is_oriented)
            self.assertEqual(sect.extent_xyz, (515694.9128668542, 7142239.234535628, 1425.0,
                                               516233.9140090464, 7142637.2015803885, 1835.0))
            self.assertEqual(sect.extent_2d(), (-5.0, 1425.0, 665.0, 1835.0))

    def test_swing(self):
        self.start()
        with gxgrd.Grid.open(self.swing) as swing:
            self.assertTrue(swing.coordinate_system.is_oriented)
            self.assertEqual(swing.extent_xyz, (716313.064376335, 1716142.3054918314, -0.6066017177982133,
                                                717108.3819305873, 1716809.6889240067, 360.01785668734107))
            self.assertEqual(swing.extent_2d(), (-347.1403049983618, -15.0, 363.006674942662, 495.0))

    def test_crooked(self):
        self.start()
        with gxgrd.Grid.open(self.crooked) as crooked:
            self.assertTrue(crooked.coordinate_system.is_oriented)
            self.assertTrue(crooked.is_crooked_path)
            self.assertEqual(crooked.extent_xyz, (632840.885099, 4633310.4612, 1203.0,
                                                  634556.6023, 4635124.0248, 1217.0))
            self.assertEqual(crooked.extent_2d(), (-1.0, 1203.0, 4071.0, 1217.0))

    def test_minimum_curvature(self):
        self.start()

        def feed_data(n):
            if n >= len(nxyv):
                return None
            return nxyv[n]

        def gdb_from_callback(callback):
            _gdb = gxgdb.Geosoft_gdb.new()
            channels = ('x', 'y', 'v')
            il = 0
            xyz_list = callback(il)
            while xyz_list is not None:
                _gdb.write_line('L{}'.format(il), xyz_list, channels=channels)
                il += 1
                xyz_list = callback(il)
            _gdb.xyz_channels = channels[:2]
            return _gdb

        xyv = [(45., 10., 100), (60., 25., 77.), (50., 8., 80.)]
        with gxgrd.Grid.minimum_curvature(xyv) as grd:
            self.assertEqual((grd.nx, grd.ny), (9, 9))
            self.assertAlmostEqual(grd.statistics()['sd'], 8.708599, 5)

        # a callback, used for very large data, or to feed data efficiently from some other source.
        nxyv = np.array([[(45., 10., 100), (60., 25., 77.), (50., 8., 81.), (55., 11., 66.)],
                         [(20., 15., 108), (25.,  5., 77.), (33., 9., np.nan), (28., 2., 22.)],
                         [(35., 18., 110), (40., 31., 77.), (13.1, 3.88, 83.), (44., 4., 7.)]])

        with gxgrd.Grid.minimum_curvature(feed_data, cs=1.) as grd:
            self.assertEqual((grd.nx, grd.ny), (48, 30))
            self.assertAlmostEqual(grd.statistics()['sd'], 30.3606587, 5)

        with gxgrd.Grid.minimum_curvature(feed_data, cs=0.25, bkd=20) as grd:
            self.assertEqual((grd.nx, grd.ny), (189, 117))
            self.assertAlmostEqual(grd.statistics()['sd'], 22.36498279, 5)

        with gdb_from_callback(feed_data) as gdb:
            with gxgrd.Grid.minimum_curvature((gdb, 'v'), cs=0.25, bkd=20) as grd:
                self.assertEqual((grd.nx, grd.ny), (189, 117))
                self.assertAlmostEqual(grd.statistics()['sd'], 22.36498279, 5)

        # TODO: update this test once BASE-1265 is addressed
        with gxgrd.Grid.minimum_curvature(feed_data, cs=0.25, bkd=500, edgclp=5) as grd:
            self.assertEqual((grd.nx, grd.ny), (199, 127))
            self.assertAlmostEqual(grd.statistics()['sd'], 23.65622712, 5)
            if grd.gridding_log:
                for l in grd.gridding_log:
                    print(l)


###############################################################################################

if __name__ == '__main__':

    unittest.main()
