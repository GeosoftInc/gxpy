import numpy as np
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
        cls.gx = gx.GXpy()

    def test_vv(self):

        npdata = np.empty(gxapi.iMAX)
        with gxvv.GXvv(npdata) as vv:
            self.assertTrue(vv.length, gxapi.iMAX)
        del npdata
        npdata = np.empty(gxapi.iMAX + 1)
        self.assertRaises(gxvv.VVException, gxvv.GXvv, npdata)
        del npdata

    def test_va(self):

        max = gxapi.iMAX // 2
        npdata = np.empty(max * 2).reshape((max, 2))
        with gxva.GXva(npdata) as va:
            self.assertTrue(va.length, gxapi.iMAX)
        del npdata
        npdata = np.empty((max + 1) * 2).reshape((max + 1, 2))
        self.assertRaises(gxva.VAException, gxva.GXva, npdata)
        del npdata

    def test_gdb(self):

        try:
            name = None
            max_index = gxapi.iMAX
            with gxdb.Geosoft_gdb.new('new', overwrite=True, comp=gxdb.COMP_NONE, pageSize=64) as gdb:
                name = gdb.file_name
                line = gdb.new_line('test')

                npd = np.empty(max_index + 1)
                self.assertRaises(gxvv.VVException, gdb.write_line, line, npd, ['xx'])
                del npd

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