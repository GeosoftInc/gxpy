import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.dap_client as gxdap
import geosoft.gxpy.geometry as gxgeo
import geosoft.gxpy.grid as gxgrd

from base import GXPYTest


class Test(GXPYTest):

    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()

    @classmethod
    def tearDownClass(cls):
        cls.tearDownGXPYTest()

    def test_dap(self):
        self.start()

        with gxdap.DapClient(get_catalog=False) as dap:
            self.assertEqual(dap.url, 'http://dap.geosoft.com/')
            self.assertEqual(str(dap), 'http://dap.geosoft.com/: Geosoft Public DAP Server (? datasets)')
            self.assertEqual(len(dap), 0)

        with gxdap.DapClient('http://dap.geosoft.com/rest/', get_catalog=False) as dap:
            self.assertEqual(dap.url, 'http://dap.geosoft.com/')
            self.assertEqual(str(dap), 'http://dap.geosoft.com/: Geosoft Public DAP Server (? datasets)')

        with gxdap.DapClient('http://dap.geosoft.com', get_catalog=False) as dap:
            self.assertEqual(dap.url, 'http://dap.geosoft.com/')
            self.assertEqual(str(dap), 'http://dap.geosoft.com/: Geosoft Public DAP Server (? datasets)')

        self.assertRaises(gxdap.DapClientException, gxdap.DapClient, 'http://www.geosoft.com')

    def test_catalog(self):
        self.start()

        with gxdap.DapClient() as dap:
            self.assertEqual(dap.url, 'http://dap.geosoft.com/')
            self.assertTrue(len(dap) == 0)
            dap.catalog()
            self.assertTrue(len(dap) > 0)

            for ds in dap:
                self.assertTrue(len(ds.Title) > 0)

            ds = dap['EMAG2_V3_20170530_SeaLevel']
            self.assertEqual(int(ds.Id), 970)

            ds = dap[('/World/Magnetics/EMAG2', 'EMAG2_V3_20170530_SeaLevel')]
            self.assertEqual(int(ds.Id), 970)

            try:
                dap[-1]
            except IndexError:
                pass
            try:
                dap[100000000]
            except IndexError:
                pass
            try:
                dap[('nada', 'EMAG2_V3_20170530_SeaLevel')]
            except gxdap.DapClientException:
                pass

            ds = dap.datacard_from_id(905)
            self.assertEqual(ds.Title, 'SRTM1 Middle East')

    def test_fetch_grid(self):
        self.start()

        with gxdap.DapClient() as dap:

            # get a grid
            dataset = dap['SRTM1 Canada']
            extent = gxgeo.Point2(((-79.8, 43.5), (-79.25, 43.8)), coordinate_system='NAD83')
            extent = gxgeo.Point2(extent, coordinate_system='NAD83 / UTM zone 17N')
            data_file = dap.fetch_data(dataset, extent=extent, progress=print, resolution=500)
            with gxgrd.Grid.open(data_file) as grd:
                self.assertEqual(grd.nx, 115)

    def test_fetch_point(self):
        self.start()

        with gxdap.DapClient() as dap:
            # some point data
            dataset = dap['Kimberlite Indicator Mineral Grain Chemistry']
            extent = gxgeo.Point2(((-112, 65), (-111, 65.5)), coordinate_system='NAD83')
            data_file = dap.fetch_data(dataset, extent=extent, progress=print)
            self.assertEqual(os.path.splitext(data_file)[1], '.csv')

            extent = gxgeo.Point2(((-80, 65), (-70, 65.5)), coordinate_system='NAD83')
            self.assertRaises(gxdap.DapClientException, dap.fetch_data, dataset, None, extent)

    def test_datacard_properties(self):
        self.start()

        with gxdap.DapClient() as dap:

            # some point data
            datacard = dap['Kimberlite Indicator Mineral Grain Chemistry']

            # individual properties
            self.assertEqual(datacard.info['Id'], '127')
            self.assertEqual(datacard.edition, '')
            self.assertEqual(datacard.disclaimer['title'], 'Copyright Notice')
            self.assertEqual(datacard.permission, 1)
            self.assertEqual(len(datacard.metadata), 4)
            self.assertEqual(str(gxcs.Coordinate_system(datacard.spatial_properties['CoordinateSystem'])), 'WGS 84')
            self.assertEqual(len(datacard.point_properties), 9)
            self.assertTrue(datacard.grid_properties is None)
            self.assertTrue(datacard.voxel_properties is None)
            self.assertTrue(datacard.map_properties is None)

            self.assertEqual(len(dap.datacard_from_id(905).grid_properties), 13)
            self.assertEqual(len(dap.datacard_from_id(872).document_properties), 8)

    def test_geometry(self):
        self.start()

        with gxdap.DapClient() as dap:
            datacard= dap['Kimberlite Indicator Mineral Grain Chemistry']
            ex = datacard.extent
            self.assertEqual(str(ex.coordinate_system), 'WGS 84')


###############################################################################################

if __name__ == '__main__':

    gxc = gx.GXpy()
    print(gxc.gid)
    unittest.main()
