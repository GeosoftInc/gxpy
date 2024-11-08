#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import numpy as np
import gc
import unittest

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.va as gxva
import geosoft.gxpy.vv as gxvv
import geosoft.gxpy.gdb as gxdb

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gx = gx.GXpy(log=print)

    def start(self):
        self._func = self.id().split('.')[-1]
        gx.gx().log('\n' + self._func)

    def test_vv(self):
        self.start()

        max = gxapi.iMAX // 16
        npdata = np.empty(max)
        with gxvv.GXvv(npdata) as vv:
            self.assertTrue(vv.length, max)
        del npdata
        gc.collect()

        npdata = np.empty(gxapi.iMAX + 1)
        self.assertRaises(gxvv.VVException, gxvv.GXvv, npdata)
        del npdata
        gc.collect()

    def test_va(self):
        self.start()

        max = gxapi.iMAX // 16
        print('max', max)
        npdata = np.empty(max * 2).reshape((max, 2))
        with gxva.GXva(npdata) as va:
            self.assertTrue(va.length, gxapi.iMAX)
        del npdata
        gc.collect()

        npdata = np.empty((gxapi.iMAX + 1) * 2).reshape(((gxapi.iMAX + 1), 2))
        self.assertRaises(gxva.VAException, gxva.GXva, npdata)
        del npdata
        gc.collect()

    def test_gdb(self):
        self.start()

        name = None
        pagesize = 4096
        try:
            max_index = 65534 * pagesize // 8
            print('maximum index', max_index)
            with gxdb.Geosoft_gdb.new('new', overwrite=True, comp=gxdb.COMP_NONE, page_size=pagesize) as gdb:
                name = gdb.file_name
                line = gdb.new_line('test')

                npd = np.zeros(max_index)
                npd_size = np.size(npd)
                gdb.write_line(line, npd, ['xx'])
                del npd

                npd2, ch, fid = gdb.read_line(line)
                self.assertEqual(len(ch), 1)
                self.assertEqual(np.size(npd2), npd_size)
                del npd2

        finally:
            gxdb.delete_files(name)


##############################################################################################
if __name__ == '__main__':

    unittest.main()