import unittest
import os
import numpy as np
from PIL import Image

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.utility as gxu
import geosoft.gxpy.system as gsys
import geosoft.gxpy.gdb as gxdb
import geosoft.gxpy.vv as gxvv
import geosoft.gxpy.va as gxva

from base import GXPYTest


class Test(GXPYTest):
    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'test_database.zip'),
                                       folder=cls._gx.temp_folder())
        cls.gdb_name = os.path.join(cls.folder, files[0])

    def tf(f):
        return os.path.join(os.path.dirname(__file__), f)

    def test_gdb(self):
        self.start()
        self.assertEqual(gxdb.__version__, geosoft.__version__)

    def test_noprops_GDB(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:
            # self.assertEqual(gdb.file_name.lower(),self.gdb_name.lower())
            self.assertEqual(str(gdb).lower(), os.path.basename(self.gdb_name).lower())
            self.assertTrue(len(gdb.list_channels()) >= 6)
            self.assertTrue('X' in gdb.list_channels())
            self.assertTrue('dx' in gdb.list_channels(chan=gxdb.CHAN_ALL))
            self.assertTrue('vector' in gdb.list_channels(chan=gxdb.CHAN_ARRAY))
            self.assertFalse('vector' in gdb.list_channels(chan=gxdb.CHAN_NORMAL))

            self.assertEqual(gdb.channel_width('vector'), 3)
            self.assertEqual(gdb.channel_width('x'), 1)

            gdb.discard()

    def test_read(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:
            for l in gdb.list_lines():
                npd, ch, fid = gdb.read_line(l)
                self.assertEqual(len(ch), 8)


###############################################################################################

if __name__ == '__main__':
    unittest.main()