import unittest
import os
import numpy as np
import geosoft.gxapi as gxapi
import geosoft.gxpy.system as gsys
import geosoft.gxpy.gdb as gxdb
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.metadata as gxmeta
import geosoft.gxpy.vv as gxvv

from base import GXPYTest


class Test(GXPYTest):

    @classmethod
    def setUpClass(cls):

        cls.setUpGXPYTest()
        print('User:', cls._gx.gid)
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'test_database.zip'),
                                       folder=cls._gx.temp_folder())
        cls.gdb_name = os.path.join(cls.folder, files[0])

    def skip(self):
        if self._gx.entitled:
            print('\n****** Skipping free-licence test for licenced ID: {} ******'.format(self._gx.gid))
            return False
        return True

    def tf(f):
        return os.path.join(os.path.dirname(__file__), f)

    def test_noprops_GDB(self):
        self.start()
        if self.skip():
            with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:
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
        if self.skip():
            with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:
                for l in gdb.list_lines():
                    npd, ch, fid = gdb.read_line(l)
                    self.assertEqual(len(ch), 8)

    def test_large_write(self):
        self.start()
        if self.skip():
            try:
                name = None
                with gxdb.Geosoft_gdb.new('new', overwrite=True) as gdb:
                    name = gdb.file_name
                    npd = np.empty((200000, 2))
                    npd[:,:] = np.nan
                    line = gdb.new_line('test')
                    gdb.write_line(line, npd, ['x', 'y'])
                    npd2, ch, fid = gdb.read_line(line)
                    self.assertEqual(len(ch), 2)
                    self.assertEqual(npd2.shape, npd.shape)
            finally:
                gxdb.delete_files(name)

    def test_va_write(self):
        self.start()
        if self.skip():
            try:
                name = None
                with gxdb.Geosoft_gdb.new('new', overwrite=True) as gdb:
                    name = gdb.file_name
                    npd = np.empty((2000000, 3))
                    npd[:, :] = np.nan
                    line = gdb.new_line('test')
                    c = gxdb.Channel.new(gdb, 'xx', array=3)
                    gdb.write_line(line, npd, ['xx[0]', 'xx[1]', 'xx[2]'])
                    c = gxdb.Channel(gdb, 'xx')
                    self.assertEqual(c.array, 3)
                    npd2, ch, fid = gdb.read_line(line)
                    self.assertEqual(len(ch), 3, npd.shape)

            finally:
                gxdb.delete_files(name)

    def test_grid(self):
        self.start()

        if self.skip():

            name = 'test_free.grd(GRD)'
            with gxgrd.Grid.new(name, properties={'nx': 1200, 'ny': 800}, overwrite=True) as grd:
                name = grd.file_name_decorated
                self.assertEqual(grd.nx, 1200)
                self.assertEqual(grd.ny, 800)
            with gxgrd.Grid.open(name) as grd:
                grd.delete_files()
                self.assertEqual(grd.nx, 1200)
                self.assertEqual(grd.ny, 800)


    def test_voxel(self):
        self.start()
        if self.skip():

            name = 'voxel.geosoft_voxel'
            gxapi.GXVOX.generate_constant_value(name,
                                                1.0,
                                                5,
                                                0, 0, 0,
                                                1, 1, 1,
                                                300, 200, 50,
                                                gxcs.Coordinate_system().gxipj,
                                                gxmeta.Metadata().gxmeta)

            gxvox = gxapi.GXVOX.create(name)
            minx = gxapi.float_ref()
            miny = gxapi.float_ref()
            minz = gxapi.float_ref()
            maxx = gxapi.float_ref()
            maxy = gxapi.float_ref()
            maxz = gxapi.float_ref()
            gxvox.get_area(minx, miny, minz, maxx, maxy, maxz)
            self.assertEqual(minx.value, -0.5)
            self.assertEqual(maxz.value, 49.5)

            vvx = gxvv.GXvv()
            vvy = gxvv.GXvv()
            vvz = gxvv.GXvv()
            gxvox.get_location_points(vvx.gxvv, vvy.gxvv, vvz.gxvv)
            gxvoxe = gxapi.GXVOXE.create(gxvox)
            vvd = gxvv.GXvv([float(n) for n in range(500)])
            gxvoxe.vector(0., 0., 0., 1.5, 1.5, 0.5, vvd.gxvv, gxapi.VOXE_EVAL_INTERP)
            self.assertEqual(vvd.length, 500)
            self.assertEqual(vvd[0][0], 1.0)
            self.assertTrue(np.isnan(vvd[499][0]))
            gxvoxe = None
            gxvox = None

            try:
                os.remove(name)
                os.remove(name + '.xml')
            except:
                pass

###############################################################################################

if __name__ == '__main__':
    unittest.main()