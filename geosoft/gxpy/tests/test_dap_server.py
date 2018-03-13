import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.dap_server as gxdap

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

            ds = dap[('nada', 'EMAG2_V3_20170530_SeaLevel')]
            self.assertTrue(ds is None)


###############################################################################################

if __name__ == '__main__':

    gxc = gx.GXpy()
    print(gxc.gid)
    unittest.main()
