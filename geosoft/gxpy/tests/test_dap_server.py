import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.dap_server as gxdap
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

        with gxdap.DapServer(get_catalog=False) as dap:
            self.assertEqual(dap.url, 'http://dap.geosoft.com/')
            self.assertEqual(str(dap), 'http://dap.geosoft.com/: Geosoft Public DAP Server (? datasets)')
            self.assertEqual(len(dap), 0)

        with gxdap.DapServer('http://dap.geosoft.com/rest/', get_catalog=False) as dap:
            self.assertEqual(dap.url, 'http://dap.geosoft.com/')
            self.assertEqual(str(dap), 'http://dap.geosoft.com/: Geosoft Public DAP Server (? datasets)')

        with gxdap.DapServer('http://dap.geosoft.com', get_catalog=False) as dap:
            self.assertEqual(dap.url, 'http://dap.geosoft.com/')
            self.assertEqual(str(dap), 'http://dap.geosoft.com/: Geosoft Public DAP Server (? datasets)')

        self.assertRaises(gxdap.DapServerException, gxdap.DapServer, 'http://www.geosoft.com')

    def test_catalog(self):
        self.start()

        with gxdap.DapServer() as dap:
            self.assertEqual(dap.url, 'http://dap.geosoft.com/')
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
            except gxdap.DapServerException:
                pass

    def test_fetch_grid(self):
        self.start()

        with gxdap.DapServer() as dap:

            # get a grid
            dataset = dap['SRTM1 Canada']
            extent = gxgeo.Point2(((-79.8, 43.5), (-79.25, 43.8)), coordinate_system='NAD83')
            extent = gxgeo.Point2(extent, coordinate_system='NAD83 / UTM zone 17N')
            data_file = dap.fetch_data(dataset, extent=extent, progress=print, resolution=500)
            with gxgrd.Grid.open(data_file) as grd:
                self.assertEqual(grd.nx, 115)

    def test_fetch_point(self):
        self.start()

        with gxdap.DapServer() as dap:
            # some point data
            dataset = dap['Kimberlite Indicator Mineral Grain Chemistry']
            extent = gxgeo.Point2(((-112, 65), (-111, 65.5)), coordinate_system='NAD83')
            data_file = dap.fetch_data(dataset, extent=extent, progress=print, resolution=0)
            self.assertEqual(os.path.splitext(data_file)[1], '.csv')

            extent = gxgeo.Point2(((-80, 65), (-70, 65.5)), coordinate_system='NAD83')
            self.assertRaises(gxdap.DapServerException, dap.fetch_data, dataset, None, extent)

    def test_dap_on_tap(self):
        self.start()
        pass

###############################################################################################

if __name__ == '__main__':

    gxc = gx.GXpy()
    print(gxc.gid)
    unittest.main()
