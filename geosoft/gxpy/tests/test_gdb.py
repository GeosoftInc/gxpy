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
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py), 'test_database.zip'),
                                       folder=cls._gx.temp_folder())
        cls.gdb_name = os.path.join(cls.folder, 'test_database.gdb')

    def test_gdb(self):
        self.start()
        self.assertEqual(gxdb.__version__, geosoft.__version__)

        def setxyz(xyz):
            gdb.xyz_channels = xyz

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:
            try:
                self.assertRaises(gxdb.GdbException, gdb.is_line, 'nope', True)
                self.assertRaises(gxdb.GdbException, gdb.is_channel, 'nope', True)
                self.assertRaises(gxdb.GdbException, setxyz, ('x', 'y', 'crazy_cannot_exist'))
                self.assertRaises(gxdb.GdbException, setxyz, ('crazy_cannot_exist', 'y'))
                gdb.xyz_channels = ('x', 'y', 'z')
                self.assertEqual(gdb.xyz_channels[2], 'z')
                gdb.xyz_channels = ('x', 'y')
                self.assertEqual(gdb.xyz_channels[2], 'z')

            finally:
                gdb.discard()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:
            self.assertEqual(len(gdb.file_name), len(self.gdb_name))

        with gxdb.Geosoft_gdb.open(os.path.splitext(self.gdb_name)[0]) as gdb:
            self.assertEqual(len(gdb.file_name), len(self.gdb_name))
            gdb.commit()
            try:
                l = list(gdb.list_lines())
                c = list(gdb.list_channels())
                self.assertTrue(gdb._exist_symb(gxdb.Line(gdb, l[0]), gxapi.DB_SYMB_LINE))
                self.assertTrue(gdb._exist_symb(gxdb.Channel(gdb, c[0]), gxapi.DB_SYMB_CHAN))
                self.assertFalse(gdb._exist_symb(gxdb.Channel(gdb, c[0]), gxapi.DB_SYMB_LINE))

            finally:
                gdb.discard()

        self.assertFalse(gxdb.is_valid_line_name(123))

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:
            self.assertEqual(gdb.max_blobs, 650)
            self.assertEqual(gdb.max_lines, 500)
            self.assertEqual(gdb.max_channels, 50)
            self.assertEqual(gdb.used_blobs, 14)
            self.assertEqual(gdb.used_lines, 5)
            self.assertEqual(gdb.used_channels, 6)
            self.assertEqual(gdb.max_compressed_channel_bytes, 67106816)
            self.assertEqual(gdb.number_of_blocks, 275)
            self.assertEqual(gdb.lost_blocks, 0)
            self.assertEqual(gdb.free_blocks, 36)
            self.assertEqual(gdb.compression, 0)
            self.assertEqual(gdb.pages_for_blobs, 0)
            self.assertEqual(gdb.db_size_kb, 638)
            self.assertEqual(gdb.index_size_kb, 303)
            self.assertEqual(gdb.max_block_size_bytes, 67106792)
            self.assertEqual(gdb.data_has_changed, 0)

        with gxdb.Geosoft_gdb.open(os.path.splitext(self.gdb_name)[0]) as gdb:
            try:
                gxdb.Channel.new(gdb, 'empty')
                data = gdb.read_line('D2','empty')[0]
                self.assertEqual(len(data), 0)
                data = gdb.read_line('D2', ('x', 'y', 'empty'))[0]
                self.assertEqual(len(data), 832)
                self.assertFalse(np.isfinite(data[:,2]).any())
            finally:
                gdb.discard()

    def test_noprops_GDB(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:
            self.assertEqual(len(gdb.file_name), len(self.gdb_name))
            self.assertEqual(str(gdb).lower(),os.path.basename(self.gdb_name).lower())
            self.assertTrue(len(gdb.list_channels())>=6)
            self.assertTrue('X' in gdb.list_channels())
            self.assertTrue('dx' in gdb.list_channels(chan=gxdb.CHAN_ALL))
            self.assertTrue('vector' in gdb.list_channels(chan=gxdb.CHAN_ARRAY))
            self.assertFalse('vector' in gdb.list_channels(chan=gxdb.CHAN_NORMAL))

            self.assertEqual(gdb.channel_width('vector'),3)
            self.assertEqual(gdb.channel_width('x'),1)

            gdb.discard()

    def test_empty(self):
        self.start()

        name = 'empty'
        try:
            with gxdb.Geosoft_gdb.new(name, overwrite=True) as gdb:
                name = gdb.file_name
                self.assertEqual(len(gdb.list_lines()), 0)
                gdb.new_line('some_line')
                gdb.new_line('_some_line')
                lines = gdb.list_lines()
                self.assertEqual(len(lines), 2)
                self.assertTrue('Some_line' in lines) # note leading 's' was interpreted as line type 'S'
                self.assertTrue('D_some_line' in lines)

                npd, ch, fid = gdb.read_line(list(lines)[0])
                self.assertEqual(npd.size, 0)
                self.assertEqual(len(ch), 0)

                gdb.new_channel('one')
                npd, ch, fid = gdb.read_line(list(lines)[0])
                self.assertEqual(npd.shape, (0, 1))
                self.assertEqual(len(ch), 1)
                self.assertEqual(fid, (0.0, 1.0))

                gdb.new_channel('two')
                npd, ch, fid = gdb.read_line(list(lines)[0])
                self.assertEqual(npd.shape, (0, 2))
                self.assertEqual(len(ch), 2)
                self.assertEqual(fid, (0.0, 1.0))

                ch = gdb.new_channel('three')
                line = list(lines)[0]
                gdb.write_channel(line, ch, [1, 2, 3, 4, 5])
                npd, ch, fid = gdb.read_line(list(lines)[0])
                self.assertEqual(npd.shape, (5, 3))
                self.assertEqual(len(ch), 3)
                self.assertEqual(fid, (0.0, 1.0))

                ch = gdb.new_channel('four', dtype=np.int)
                line = list(lines)[0]
                gdb.write_channel(line, ch, [10, 20, 30, 40], fid=(-1.5, 2))
                npd, ch, fid = gdb.read_line(line)
                self.assertEqual(npd.shape, (7, 4))
                self.assertEqual(len(ch), 4)
                self.assertEqual(fid, (-1.5, 1.0))
                self.assertEqual(npd[0][0], 10.)
                self.assertEqual(npd[2][2], 1.5)
                self.assertEqual(npd[5][2], 4.5)
                self.assertTrue(np.isnan(npd[0][1]))
                self.assertTrue(np.isnan(npd[1][2]))
                self.assertTrue(np.isnan(npd[6][2]))

                npd, ch, fid = gdb.read_line(line, 'four', dtype=np.int)
                self.assertEqual(npd.shape, (4, 1))
                self.assertEqual(len(ch), 1)
                self.assertEqual(fid, (-1.5, 2.0))
                self.assertEqual(npd[0][0], 10)
                self.assertEqual(npd[3][0], 40)

                npd, ch, fid = gdb.read_line(line, 'four', fid=(-0.13333, 0.000666))
                self.assertEqual(npd.shape, (6958, 1))
                self.assertEqual(len(ch), 1)
                self.assertEqual(fid, (-0.13333, 0.000666))
                self.assertAlmostEqual(npd[0][0], 16.83335)
                self.assertAlmostEqual(npd[1000][0], 20.16335)


        finally:
            gxdb.delete_files(name)


    def test_read_write_channel_vv_va(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:
            gdb.delete_channel('test_chan_vv')
            vv = gxvv.GXvv(np.array([1.,2.,3.]), fid=(-10, 2.5))
            gdb.write_channel_vv('T46', 'test_chan_vv', vv)
            vv = gdb.read_channel_vv('T46', 'test_chan_vv')
            self.assertEqual(vv.length, 3)
            self.assertEqual(vv.fid, (-10.0, 2.5))
            self.assertRaises(gxva.VAException, gdb.read_channel_va, 'T46', 'test_chan_vv')
            gdb.delete_channel('test_chan_vv')

            va = gxva.GXva(np.array([[1., 2., 3.],[8,9,10]]), fid=(-10, 2.5))
            gdb.write_channel_va('T46', 'test_chan_va', va)
            self.assertRaises(gxdb.GdbException, gdb.read_channel_vv, 'T46', 'test_chan_va')
            va = gdb.read_channel_va('T46', 'test_chan_va')
            self.assertEqual(va.width, 3)
            self.assertEqual(va.length, 2)
            self.assertEqual(va.fid, (-10.0, 2.5))
            gdb.delete_channel('test_chan_va')

    def test_group_VA_read_write(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            self.assertEqual(len(gdb.file_name), len(self.gdb_name))
            self.assertEqual(str(gdb).lower(),os.path.basename(self.gdb_name).lower())
            data, ch, fid = gdb.read_line('D578625')
            self.assertEqual(data.shape, (832, 8))

            gdb.write_line('T45', data, fid=(99, 0.5))
            data, ch, fid = gdb.read_line('T45')
            self.assertEqual(data.shape, (832, 8))
            self.assertEqual(len(ch), 8)
            self.assertEqual(ch[0], 'X')
            self.assertEqual(fid, (99.0, 0.5))

            gdb.write_channel('T46', 'wva', data, fid=(-10, 2.5))
            data, fid = gdb.read_channel('T46', 'wva')
            self.assertEqual(data.shape, (832, 8))
            self.assertEqual(fid, (-10.0, 2.5))
            gdb.delete_channel('wva')

            gdb.write_line('T46', data, channels='wideva', fid=(-10, 2.5))
            data, ch, fid = gdb.read_line('T46', 'wideva')
            self.assertEqual(data.shape, (832, 8))
            self.assertEqual(len(ch), 8)
            self.assertEqual(ch[0], 'wideva[0]')
            self.assertEqual(fid, (-10.0, 2.5))

            data, ch, fid = gdb.read_line('T46')
            self.assertEqual(data.shape, (832, 16))
            self.assertEqual(len(ch), 16)
            self.assertEqual(ch[0], 'X')
            self.assertEqual(fid, (-10.0, 2.5))

            data, fid = gdb.read_channel('T46', 'wideva')
            self.assertEqual(data.shape, (832, 8))
            self.assertEqual(fid, (-10.0, 2.5))

            gdb.discard()

    def test_create_del_GDB(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:


            gdb.delete_channel('ian')
            gdb.new_channel('ian')
            self.assertTrue('ian' in gdb.list_channels())
            gdb.delete_channel('ian')
            self.assertFalse('ian' in gdb.list_channels())

            gdb.delete_channel('ian2')
            gdb.new_channel('ian2', np.int32, array=3)
            self.assertTrue('ian2' in gdb.list_channels(chan=gxdb.CHAN_ARRAY))
            gdb.delete_channel('ian2')
            self.assertFalse('ian2' in gdb.list_channels())

    def test_properties_GDB(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            ch = gdb.list_channels()
            self.assertTrue('X' in ch)
            self.assertTrue('vector' in ch)
            self.assertEqual(ch.get('dx'),1153)

            try:
                gdb.line_name_symb(8456712552)
                self.assertTrue(False)
            except: pass

            ln,ls = gdb.line_name_symb('bogus',create=True)
            self.assertEqual(ln,'bogus')
            gdb.delete_line('bogus')
            ls = gdb.line_name_symb('bogus2',create=True)[1]
            gdb.delete_line(ls)

            ln,ls = gdb.line_name_symb('D578625')
            self.assertEqual(ln,'D578625')
            ln,ls = gdb.line_name_symb('Dwonk')
            self.assertEqual(ln,'Dwonk')
            ln,ls = gdb.line_name_symb(ls)
            self.assertEqual(ln,'Dwonk')

            gdb.delete_channel('ccva')
            gdb.new_channel('ccva',array=8)
            cn,cs = gdb.channel_name_symb('ccva')
            self.assertEqual(cn,'ccva')
            cn,cs = gdb.channel_name_symb('ccva[4]')
            self.assertEqual(cn,'ccva[4]')

            gdb.discard()
            cs = gdb.new_channel('cava',dtype=np.int64)
            self.assertTrue(gdb.channel_dtype(cs).type is np.int64)

            gdb.select_lines(select=False)
            ln = gdb.list_lines()
            self.assertEqual(len(ln),0)

            gdb.select_lines('bogus')
            ln = gdb.list_lines()
            self.assertEqual(len(ln), 0)

            gdb.select_lines('D2')
            ln = gdb.list_lines()
            self.assertEqual(len(ln), 1)

            gdb.select_lines('D')
            ln = gdb.list_lines()
            self.assertEqual(len(ln), 3)
            self.assertTrue('D2' in ln)
            self.assertTrue('Dwonk' in ln)
            self.assertTrue('D578625' in ln)

            gdb.select_lines('D578625',select=False)
            ln = gdb.list_lines()
            self.assertFalse('D578625' in ln)
            self.assertEqual(len(ln), 2)

            gdb.discard()

    def test_read_GDB(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            npd,ch,fid = gdb.read_line('D578625')
            self.assertEqual(npd.shape[0],832)
            self.assertEqual(fid[0],0.0)
            self.assertEqual(fid[1],1.0)

            ln,ls = gdb.line_name_symb('D578625')
            npd,ch,fid = gdb.read_line(ls,channels=['X','Y','Z','dx','dy'])
            self.assertEqual(npd.shape,(832,5))
            self.assertEqual(npd[10,:3].tolist(),[578625.0, 7773625.0, -1195.7531280517615])

            npd,ch,fid = gdb.read_line(ls,'X')
            self.assertEqual(npd.shape,(832,1))
            self.assertEqual(npd[10],578625.0)

            npd,ch,fid = gdb.read_line(ls,channels=['X','Y','Z'], dtype='<U32')
            self.assertEqual(npd.shape,(832,3))
            self.assertEqual(npd[10,:3].tolist(),['578625.0', '7773625.0', '-1195.8'])

            gdb.discard()

    def test_read_vv_GDB(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            data = gdb.read_line_vv('D578625')
            for chvv in data:
                self.assertEqual(len(data), 8)
                vv = chvv[1]
                fid = vv.fid
                self.assertEqual(vv.length, 832)
                self.assertEqual(fid[0], 0.0)
                self.assertEqual(fid[1], 1.0)

            data = gdb.read_line_vv('D578625', common_fid=True)
            for chvv in data:
                self.assertEqual(len(data), 8)
                vv = chvv[1]
                fid = vv.fid
                self.assertEqual(vv.length, 832)
                self.assertEqual(fid[0], 0.0)
                self.assertEqual(fid[1], 1.0)

            data = gdb.read_line_vv('D578625', common_fid=True, fid=(0.1,4.8))
            for chvv in data:
                self.assertEqual(len(data), 8)
                vv = chvv[1]
                fid = vv.fid
                self.assertEqual(vv.length, 175)
                self.assertEqual(fid[0], 0.1)
                self.assertEqual(fid[1], 4.8)

            ln,ls = gdb.line_name_symb('D578625')
            data = gdb.read_line_vv(ls,channels=['X','Y','Z','dx','dy'])
            self.assertEqual(len(data), 5)
            self.assertEqual(data[0][0], 'X')
            self.assertEqual(data[4][0], 'dy')
            npd = data[0][1].get_data()[0]
            self.assertEqual(npd[10], 578625.0)
            npd = data[1][1].get_data()[0]
            self.assertEqual(npd[10], 7773625.0)
            npd = data[2][1].get_data()[0]
            self.assertEqual(npd[10], -1195.7531280517615)

            data = gdb.read_line_vv(ls, 'X')
            self.assertEqual(data[0][0], 'X')
            npd = data[0][1].get_data()[0]
            self.assertEqual(npd[10],578625.0)

            data = gdb.read_line_vv(ls,channels=['X','Y','Z'], dtype='<U32')
            npd = data[0][1].get_data()[0]
            self.assertEqual(npd[10], '578625.0')
            npd = data[1][1].get_data()[0]
            self.assertEqual(npd[10], '7773625.0')
            npd = data[2][1].get_data()[0]
            self.assertEqual(npd[10], '-1195.8')

            gdb.discard()

    def test_read_masked_GDB(self):
        self.start()


        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            try:

                npd,ch,fid = gdb.read_line('D2', dummy=gxdb.READ_REMOVE_DUMMYROWS)
                self.assertEqual(npd.shape, (825, 8))
                self.assertEqual(npd.shape[1], 8)
                self.assertEqual(npd.shape[1], len(ch))

                npd,ch,fid = gdb.read_line('D2',dummy=gxdb.READ_REMOVE_DUMMYCOLUMNS)
                self.assertEqual(npd.shape, (832,2))
                self.assertEqual(npd.shape[1], len(ch))

                npd,ch,fid = gdb.read_line('D2', channels=('x','y'), dummy=gxdb.READ_REMOVE_DUMMYCOLUMNS)
                self.assertEqual(npd.shape, (832,1))
                self.assertEqual(npd.shape[1], len(ch))

                px = geosoft.gxpy.geometry.Point2(gdb.extent_xyz())
                self.assertEqual(str(px), 'Point2[(578625.0, 7773625.0, -5261.5553894043005) (578625.0, 7782875.0, 1062.4999999999964)]')

            finally:
                gdb.discard()

    def test_extent(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            try:

                l = gdb.list_lines()
                gdb.select_lines()
                self.assertEqual(len(gdb.list_lines()), 5)
                gdb.select_lines(select=False)
                self.assertEqual(len(gdb.list_lines()), 0)
                gdb.select_lines('D2')
                self.assertEqual(len(gdb.list_lines()), 1)
                self.assertFalse(gdb.is_line('D0'))
                self.assertEqual(len(gdb.list_lines(select=False)), 5)

                self.assertTrue(gdb.is_line('Dwonk'))

                dy,_ = gdb.read_channel('D2', 'y')
                dy [:] = np.nan
                gdb.write_channel('D2', 'y', dy)
                px = geosoft.gxpy.geometry.Point2(gdb.extent_xyz())
                self.assertEqual(str(px), 'Point2[(578625.0, nan, -5261.5553894043005) (578625.0, nan, 1062.4999999999964)]')

            finally:
                gdb.discard()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            try:
                gdb.select_lines(select=False)
                gdb.select_lines('D2')
                dx,_ = gdb.read_channel('D2', 'x')
                dx [:] = np.nan
                gdb.write_channel('D2', 'x', dx)
                px = geosoft.gxpy.geometry.Point2(gdb.extent_xyz())
                self.assertEqual(str(px), 'Point2[(nan, 7773625.0, -5261.5553894043005) (nan, 7782875.0, 1062.4999999999964)]')

            finally:
                gdb.discard()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            try:
                gdb.select_lines(select=False)
                gdb.select_lines('D2')
                dx, _ = gdb.read_channel('D2', 'x')
                dx[:] = np.nan
                dx[1] = 1
                dx[2] = 2
                gdb.write_channel('D2', 'x', dx)
                px = geosoft.gxpy.geometry.Point2(gdb.extent_xyz())
                self.assertEqual(str(px),
                                 'Point2[(1.0, 7773625.0, -5261.5553894043005) (2.0, 7782875.0, 1062.4999999999964)]')

            finally:
                gdb.discard()

    def test_write_vv_GDB(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            gdb.delete_channel('test')
            gdb.new_channel('test')
            vv = gxvv.GXvv(np.array([1.0,2.0,3.0,4.0]))
            gdb.write_channel_vv('D590875', 'test', vv)
            npd, ch, fid = gdb.read_line('D590875', channels=['test'])
            self.assertEqual(gdb.channel_fid('D590875', 'test'), fid)
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1.0,2.0,3.0,4.0])

            gdb.delete_channel('test')
            gdb.new_channel('test', np.float64, details={'unit': 'bubba'})
            self.assertEqual(gxdb.Channel(gdb, 'test').unit, 'bubba')
            vv = gxvv.GXvv(dtype=np.float64)
            vv.set_data(np.array([1,2,3,4], dtype=np.int64))
            gdb.write_channel_vv('D590875', 'test', vv)
            npd,ch,fid = gdb.read_line('D590875', channels=['test'], dtype=np.int)
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1,2,3,4])

            gdb.delete_channel('test')
            gdb.new_channel('test', np.int32)
            gdb.write_channel_vv('D590875', 'test', vv)
            npd,ch,fid = gdb.read_line('D590875', 'test')
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1.0,2.0,3.0,4.0])

            gdb.delete_channel('test')
            gdb.new_channel('test', dtype=np.int32)
            vv.fid = (3,2)
            gdb.write_channel_vv('D590875', 'test', vv)
            npd,ch,fid = gdb.read_line('D590875', 'test', dtype=int)
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1,2,3,4])
            self.assertEqual(fid[0],3.0)
            self.assertEqual(fid[1],2.0)

            gdb.new_channel('test', np.int32)
            vv = gxvv.GXvv(np.array([1, 2, 3, 4], dtype=np.int32), fid=(2.5,0.33))
            gdb.write_channel_vv('D590875', 'test', vv)
            npd,ch,fid = gdb.read_line('D590875', channels=['test'])
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1,2,3,4])
            self.assertEqual(fid[0], 2.5)
            self.assertEqual(fid[1], 0.33)

            gdb.discard()

    def test_write_vv_GDB(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            gdb.delete_channel('test')
            gdb.new_channel('test')
            vv = gxvv.GXvv(np.array([1.0,2.0,3.0,4.0]))
            gdb.write_channel_vv('D590875', 'test', vv)
            npd, ch, fid = gdb.read_line('D590875', channels=['test'])
            self.assertEqual(gdb.channel_fid('D590875', 'test'), fid)
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1.0,2.0,3.0,4.0])

            gdb.delete_channel('test')
            gdb.new_channel('test', np.float64, details={'unit': 'bubba'})
            self.assertEqual(gxdb.Channel(gdb, 'test').unit_of_measure, 'bubba')
            vv = gxvv.GXvv(dtype=np.float64)
            vv.set_data(np.array([1,2,3,4], dtype=np.int64))
            gdb.write_channel_vv('D590875', 'test', vv)
            npd,ch,fid = gdb.read_line('D590875', channels=['test'], dtype=np.int)
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1,2,3,4])

            gdb.delete_channel('test')
            gdb.new_channel('test', np.int32)
            gdb.write_channel_vv('D590875', 'test', vv)
            npd,ch,fid = gdb.read_line('D590875', 'test')
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1.0,2.0,3.0,4.0])

            gdb.delete_channel('test')
            gdb.new_channel('test', dtype=np.int32)
            vv.fid = (3,2)
            gdb.write_channel_vv('D590875', 'test', vv)
            npd,ch,fid = gdb.read_line('D590875', 'test', dtype=int)
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1,2,3,4])
            self.assertEqual(fid[0],3.0)
            self.assertEqual(fid[1],2.0)

            gdb.new_channel('test', np.int32)
            vv = gxvv.GXvv(np.array([1, 2, 3, 4], dtype=np.int32), fid=(2.5,0.33))
            gdb.write_channel_vv('D590875', 'test', vv)
            npd,ch,fid = gdb.read_line('D590875', channels=['test'])
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1,2,3,4])
            self.assertEqual(fid[0], 2.5)
            self.assertEqual(fid[1], 0.33)

            gdb.discard()

    def test_write_GDB(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            gdb.delete_channel('test')
            gdb.new_channel('test')
            gdb.write_channel('D590875','test',np.array([1.0,2.0,3.0,4.0]))
            npd, ch, fid = gdb.read_line('D590875', channels=['test'])
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1.0,2.0,3.0,4.0])

            gdb.delete_channel('test')
            gdb.new_channel('test', np.float64)
            gdb.write_channel('D590875','test',np.array([1,2,3,4],dtype=np.int))
            npd,ch,fid = gdb.read_line('D590875',channels=['test'],dtype=np.int)
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1,2,3,4])

            gdb.delete_channel('test')
            gdb.new_channel('test', np.int32)
            gdb.write_channel('D590875','test',np.array([1,2,3,4],dtype=np.int))
            npd,ch,fid = gdb.read_line('D590875',channels=['test'])
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1.0,2.0,3.0,4.0])

            gdb.delete_channel('test')
            gdb.new_channel('test', dtype=np.int32)
            gdb.write_channel('D590875','test',np.array([1,2,3,4],dtype=np.int),fid=(3,2))
            npd,ch,fid = gdb.read_line('D590875',channels=['test'])
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1.0,2.0,3.0,4.0])
            self.assertEqual(fid[0],3.0)
            self.assertEqual(fid[1],2.0)

            gdb.new_channel('test', np.int32)
            gdb.write_channel('D590875', 'test', np.array([1,2,3,4], dtype=np.int), fid=(2.50,0.33))
            npd,ch,fid = gdb.read_line('D590875', channels=['test'])
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1.0,2.0,3.0,4.0])
            self.assertEqual(fid[0], 2.5)
            self.assertEqual(fid[1], 0.33)

            gdb.discard()

    def test_write_VA_GDB(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            gdb.delete_channel('testVA')
            gdb.new_channel('testVA')
            try:
                gdb.write_channel('D590875', 'testVA',
                                  np.array([[1.0, 2.0, 3.0, 4.0], [10.0, 20.0, 30.0, 40.0], [15.0, 25.0, 35.0, 45.0]]))
                self.assertTrue(False)
            except gxdb.GdbException:
                pass

            gdb.delete_channel('testVA')
            gdb.write_channel('D590875', 'testVA',
                              np.array([[1.0, 2.0, 3.0, 4.0], [10.0, 20.0, 30.0, 40.0], [15.0, 25.0, 35.0, 45.0]]))
            npd,ch,fid = gdb.read_line('D590875', channels=['testVA'])
            self.assertEqual(npd.shape,(3, 4))
            self.assertEqual(npd[0, :].tolist(), [1.0, 2.0, 3.0, 4.0])
            self.assertEqual(npd[1, :].tolist(), [10.0, 20.0, 30.0, 40.0])
            self.assertEqual(npd[2, :].tolist(), [15.0, 25.0, 35.0, 45.0])

            gdb.discard()

    def test_dummy_GDB(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            gdb.delete_channel('test')
            gdb.new_channel('test',dtype=np.int)
            dummy = gxu.gx_dummy(np.int)

            gdb.write_channel('D590875', 'test', np.array([1, 2, dummy, 4]))
            npd,ch,fid = gdb.read_line('D590875', channels=['test'], dtype=np.int)
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1,2,dummy,4])

            dm = gxu.dummy_mask(npd)
            self.assertEqual(dm.tolist(),[False,False,True,False])

            gdb.discard()


    def test_newline_vv_GDB(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            data = gdb.read_line_vv('D578625',channels=['dx','dy','vector'])
            ch = [c[0] for c in data]
            datalen = data[0][1].length

            gdb.delete_line('testline')
            gdb.new_line('testline')
            gdb.write_line_vv('testline', data)
            npd2,ch2,fid2 = gdb.read_line('testline', channels=ch)
            self.assertEqual(npd2.shape, (datalen, len(data)))

            gdb.delete_line('testline')
            gdb.new_line('testline', gxdb.SYMB_LINE_NORMAL)
            gdb.write_line_vv('testline', (("single", data[0][1]),))
            npd2,ch2,fid2 = gdb.read_line('testline',"single")
            self.assertEqual(npd2.shape,(datalen, 1))

            gdb.delete_line('testline')
            gdb.new_line('testline', gxdb.SYMB_LINE_GROUP)
            gdb.write_line_vv('testline', [("single", data[0][1])])
            npd2,ch2,fid2 = gdb.read_line('testline',"single")
            self.assertEqual(npd2.shape, (datalen, 1))

            gdb.discard()

    def test_newline_GDB(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            npd, ch, fid = gdb.read_line('D578625', channels=['dx','dy','vector'])

            try:
                gdb.new_line("&$#@**")
                self.assertTrue(False)
            except gxdb.GdbException: pass

            try:
                gdb.new_line("D578625")
                self.assertTrue(False)
            except gxdb.GdbException: pass

            gdb.delete_line('wonk')
            gdb.new_line('wonk',group="wink")
            try:
                gdb.new_line('wonk')
                self.assertTrue(False)
            except gxdb.GdbException: pass
            gdb.delete_line('wonk')

            gdb.delete_line('testline')
            gdb.new_line('testline')
            gdb.write_line('testline', npd, channels=ch)
            npd2,ch2,fid2 = gdb.read_line('testline', channels=ch)
            self.assertEqual(npd.shape,npd2.shape)

            gdb.delete_line('testline')
            gdb.new_line('testline',gxdb.SYMB_LINE_NORMAL)
            gdb.write_line('testline',npd[:,0],"single")
            npd2,ch2,fid2 = gdb.read_line('testline',"single")
            self.assertEqual(npd2.shape,(npd.shape[0],1))

            gdb.delete_line('testline')
            gdb.new_line('testline',gxdb.SYMB_LINE_GROUP)
            gdb.write_line('testline',npd[:,0],"single")
            npd2,ch2,fid2 = gdb.read_line('testline',"single")
            self.assertEqual(npd2.shape,(npd.shape[0],1))

            gdb.delete_line('testline')
            gdb.new_line('testline',linetype=gxdb.SYMB_LINE_FLIGHT)
            ch = ['a','b','c','d']
            try:
                gdb.write_line('testline', npd, channels=ch)
                self.assertTrue(False)
            except gxdb.GdbException:
                pass

            ch = ['a','b','c','d','e']
            self.assertRaises(gxdb.GdbException, gdb.write_line, 'testline', npd, ['xx', 'yy'])
            gdb.write_line('testline', npd, channels=ch)
            npd2, ch2, fid2 = gdb.read_line('testline',channels=ch)
            self.assertEqual(npd.shape,npd2.shape)
            self.assertEqual(ch2, ch)
            gdb.delete_channel(ch)

            gdb.delete_line('testline')
            gdb.new_line('testline')
            gdb.delete_channel("bopper")
            gdb.write_line('testline',npd,channels="bopper")
            npd2,ch2,fid2 = gdb.read_line('testline',"bopper")
            self.assertEqual(npd.shape,npd2.shape)
            self.assertEqual(ch2[0],"bopper[0]")
            self.assertEqual(ch2[4],"bopper[4]")

            gdb.discard()

    def test_list_values_GDB(self):
        self.start()

        self.nl = 0
        self.stp = 100
        def enough():
            self.nl += 1
            if self.nl >= self.stp: return True
            else: return False

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            try:
                gdb.select_lines(select=False)
                gdb.select_lines('D578625,D2',select=True)
                self.nl = 0
                self.stp = 2

                gdb.delete_channel('testlist')
                gdb.new_channel('testlist',dtype=np.int)
                gdb.write_channel('D578625', 'testlist', np.array([1,2,3,4,4,4,5,6,7,7,7,6,5,4], dtype=np.int))
                gdb.write_channel('D2', 'testlist', np.array([12,12,12,13,13,13], dtype=np.int))

                listVal = gdb.list_values('testlist', max=100, stop=enough)
                listVal.sort()
                self.assertEqual(listVal, ['1','12','13','2','3','4','5','6','7'])
                self.nl = 0
                self.stp = 1
                listVal = gdb.list_values('dx', max=10000)
                self.assertEqual(len(listVal),29)
                listVal = gdb.list_values('dx')
                self.assertEqual(len(listVal),29)
            finally:
                gdb.discard()

    def test_new(self):
        self.start()

        gdb_file = os.path.join(self.folder, 'new.gdb')

        try:

            with gxdb.Geosoft_gdb.new(gdb_file, overwrite=True) as gdb:

                #read an image and put it in a new database
                with open(os.path.join(self.folder, 'image.png'), 'rb') as im_handle:
                    im = Image.open(im_handle)
                    im.thumbnail( (20,20), Image.ANTIALIAS)
                    imageIn = np.asarray(im,dtype=np.float32)
                gdb.new_channel('R',dtype=np.int)
                gdb.new_channel('G',dtype=np.int)
                gdb.new_channel('B', dtype=np.int)
                gdb.new_channel('A', dtype=np.int)
                for l in range(imageIn.shape[0]):
                    gdb.write_line('L{}'.format(l),imageIn[l,:,:],channels=['R','G','B','A'])

                self.assertEqual(len(gdb.list_lines()),imageIn.shape[0])
                self.assertEqual(len(gdb.list_channels()),4)
                d,c,f = gdb.read_line('L5')
                self.assertEqual(d.shape[0],imageIn.shape[1])
                self.assertEqual(d.shape[1],imageIn.shape[2])

            self.assertRaises(gxdb.GdbException, gxdb.Geosoft_gdb.new, gdb_file)

            with gxdb.Geosoft_gdb.new(gdb_file, overwrite=True) as gdb:
                self.assertEqual(gdb.max_compressed_channel_bytes, 67106816)
            with gxdb.Geosoft_gdb.new(gdb_file, overwrite=True, pageSize=0) as gdb:
                self.assertEqual(gdb.max_compressed_channel_bytes, 4194176)
            with gxdb.Geosoft_gdb.new(gdb_file, overwrite=True, pageSize=4096) as gdb:
                self.assertEqual(gdb.max_compressed_channel_bytes, 268427264)
            try:
                with gxdb.Geosoft_gdb.new(gdb_file, overwrite=True, pageSize=5000) as gdb:
                    self.assertTrue(False) # this should have failed
            except:
                pass

        finally:
            gxdb.delete_files(gdb_file)


    def test_details(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            try:
                cs = gdb.new_channel("detailtest")
                det = gdb.channel_details(cs)
                self.assertEqual(det.get('name'),"detailtest")
                self.assertEqual(det.get('array'),1)
                self.assertEqual(det.get('decimal'),2)
                self.assertEqual(det.get('format'),0)
                self.assertEqual(det.get('label'),'detailtest')
                self.assertEqual(det.get('protect'),0)
                self.assertEqual(det.get('symbol'),cs)
                self.assertEqual(det.get('type'),gxapi.GS_DOUBLE)
                self.assertEqual(det.get('unit'),'')
                self.assertEqual(det.get('width'),12)

                gdb.set_channel_details(cs,{'protect':1, 'decimal':6, 'unit':'ft'})
                det2 = gdb.channel_details(cs)
                self.assertEqual(det2.get('protect'),1)
                self.assertEqual(det2.get('decimal'),6)
                self.assertEqual(det2.get('unit'),'ft')

                gdb.set_channel_details(cs,det)
                det2 = gdb.channel_details(cs)
                self.assertEqual(det2.get('protect'),0)
                self.assertEqual(det2.get('decimal'),2)
                self.assertEqual(det2.get('unit'),'')

                det = gdb.line_details('D578625')
                self.assertEqual(det.get('category'),gxdb.SYMB_LINE_NORMAL)
                self.assertEqual(det.get('number'),578625)
                self.assertEqual(det.get('name'),'D578625')
                self.assertEqual(det.get('flight'),0)
                self.assertEqual(det.get('version'),0)
                self.assertEqual(det.get('type'),gxapi.DB_LINE_TYPE_RANDOM)
                self.assertEqual(det.get('groupclass'), None)

                gdb.delete_line('testgroup')
                ls = gdb.new_line('testgroup', group="TeSt")
                det = gdb.line_details(ls)
                self.assertEqual(det.get('category'),gxdb.SYMB_LINE_GROUP)
                self.assertEqual(det.get('name'),'testgroup')
                self.assertEqual(det.get('symbol'),ls)
                self.assertEqual(det.get('groupclass'),'TeSt')
                gdb.delete_line('testgroup')

            finally:
                gdb.discard()

    def test_channel(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            try:
                gdb.delete_channel("detailtest")
                ch = gxdb.Channel.new(gdb, "detailtest")
                name, symb = gdb.channel_name_symb(ch)
                self.assertEqual(ch.name, name)
                self.assertEqual(ch.symbol, symb)
                det = gdb.channel_details(ch.name)
                self.assertEqual(ch.name, det['name'])
                self.assertEqual(ch.array, det['array'])
                self.assertEqual(ch.decimal, det['decimal'])
                self.assertEqual(ch.format, det['format'])
                self.assertEqual(ch.label, det['label'])
                self.assertEqual(ch.protect, det['protect'])
                self.assertEqual(ch.symbol, det['symbol'])
                self.assertEqual(ch.type, det['type'])
                self.assertEqual(ch.unit_of_measure, det['unit'])
                self.assertEqual(ch.width, det['width'])
                self.assertEqual(ch.class_, det['class'])

                ch.protect = 1
                ch.decimal = 6
                ch.width = 10
                ch.unit_of_measure = 'nT'
                ch.label = 'weirdo'
                ch.format = gxapi.DB_CHAN_FORMAT_GEOGR
                ch.class_ = 'geochem'
                self.assertEqual(ch.protect, True)
                self.assertEqual(ch.decimal, 6)
                self.assertEqual(ch.unit_of_measure, 'nT')
                self.assertEqual(ch.label, 'weirdo')
                self.assertEqual(ch.format, 4)
                self.assertEqual(ch.class_, 'geochem')

                ch.name = "new_name"
                self.assertEqual(ch.name, "new_name")
                try:
                    ch.name = list(gdb.list_channels())[0]
                    self.assertTrue(False)
                except:
                    pass
                try:
                    ch.name = 45
                    self.assertTrue(False)
                except:
                    pass

                self.assertFalse(ch.locked)
                ch.lock = gxdb.SYMBOL_LOCK_READ
                self.assertTrue(ch.locked)
                self.assertEqual(ch.lock, gxdb.SYMBOL_LOCK_READ)
                ch.lock = gxdb.SYMBOL_LOCK_WRITE
                self.assertTrue(ch.locked)
                self.assertEqual(ch.lock, gxdb.SYMBOL_LOCK_WRITE)
                ch.locked = False

                self.assertRaises(gxdb.GdbException, gdb.delete_channel, ch.name)
                self.assertRaises(gxdb.GdbException, ch.delete)
                ch.protect = False
                ch.delete()
                self.assertEqual(ch.symbol, gxapi.NULLSYMB)

            finally:
                gdb.discard()

    def test_line(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            try:
                gdb.delete_line("T9999")
                ln = gxdb.Line.new(gdb, "T9999")
                det = gdb.line_details(ln.name)
                self.assertEqual(ln.name, det['name'])
                self.assertEqual(ln.category, det['category'])
                self.assertEqual(ln.date, det['date'])
                self.assertEqual(ln.flight, det['flight'])
                self.assertEqual(ln.number, det['number'])
                self.assertEqual(ln.type, det['type'])
                self.assertEqual(ln.version, det['version'])
                self.assertEqual(ln.group, det['groupclass'])
                self.assertTrue(ln.selected)

                ln.date = 2017
                self.assertEqual(ln.date, 2017)
                ln.selected = False
                self.assertFalse(ln.selected)
                ln.selected = True
                self.assertTrue(ln.selected)
                ln.number = 88.9
                self.assertEqual(ln.number, 88)
                ln.number = -88.9
                self.assertEqual(ln.number, -88)
                ln.type = gxdb.LINE_TYPE_NORMAL
                self.assertEqual(ln.type, 0)
                ln.type = gxdb.LINE_TYPE_BASE
                self.assertEqual(ln.type, 1)
                ln.type = gxdb.LINE_TYPE_TIE
                self.assertEqual(ln.type, 2)
                ln.type = gxdb.LINE_TYPE_TEST
                self.assertEqual(ln.type, 3)
                ln.type = gxdb.LINE_TYPE_TREND
                self.assertEqual(ln.type, 4)
                ln.type = gxdb.LINE_TYPE_SPECIAL
                self.assertEqual(ln.type, 5)
                ln.type = gxdb.LINE_TYPE_RANDOM
                self.assertEqual(ln.type, 6)
                ln.version = 7
                self.assertEqual(ln.version, 7)
                ln.flight = 1000
                self.assertEqual(ln.flight, 1000)

                self.assertFalse(ln.grouped)
                try:
                    ln.group = 'billy'
                    self.assertTrue(False)
                except gxdb.GdbException:
                    pass

                self.assertEqual(ln.lock, gxdb.SYMBOL_LOCK_NONE)
                self.assertFalse(ln.locked)
                ln.lock = gxdb.SYMBOL_LOCK_READ
                self.assertTrue(ln.locked)
                self.assertEqual(ln.lock, gxdb.SYMBOL_LOCK_READ)
                ln.lock = gxdb.SYMBOL_LOCK_WRITE
                self.assertTrue(ln.locked)
                self.assertEqual(ln.lock, gxdb.SYMBOL_LOCK_WRITE)
                ln.locked = False

                ln.delete()
                self.assertEqual(ln.symbol, gxapi.NULLSYMB)

                gdb.delete_line("L88")
                ln = gxdb.Line.new(gdb, "L88", group='john')
                self.assertTrue(ln.grouped)
                self.assertEqual(ln.group, 'john')
                ln.group = 'billy'
                self.assertEqual(ln.group, 'billy')
                gdb.delete_line(ln.name)

            finally:
                gdb.discard()

    def test_locks(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            try:
                gdb.delete_line("T9999")
                l = gxdb.Line.new(gdb, "T9999")
                l.lock = gxdb.SYMBOL_LOCK_WRITE
                self.assertTrue(l.locked)
                ll = gxdb.Line.new(gdb, "T8")
                ll.lock = gxdb.SYMBOL_LOCK_READ
                self.assertTrue(ll.locked)
                c = gxdb.Channel.new(gdb, "dummy")
                c.lock = gxdb.SYMBOL_LOCK_WRITE
                self.assertTrue(c.locked)
                cc = gxdb.Channel.new(gdb, "dummy2")
                cc.lock = gxdb.SYMBOL_LOCK_WRITE
                self.assertTrue(cc.locked)

                gdb.unlock_all()
                self.assertFalse(l.locked)
                self.assertFalse(ll.locked)
                self.assertFalse(c.locked)
                self.assertFalse(cc.locked)

            finally:
                gdb.discard()


    def test_create_line_name(self):
        self.start()
        self.assertEqual(gxdb.create_line_name(10, gxdb.LINE_TYPE_NORMAL, 4), 'L10.4')
        self.assertEqual(gxdb.create_line_name(10, gxdb.LINE_TYPE_BASE, 4), 'B10.4')
        self.assertEqual(gxdb.create_line_name('abc', gxdb.LINE_TYPE_RANDOM, 4), 'Dabc.4')
        self.assertEqual(gxdb.create_line_name('20', gxdb.LINE_TYPE_SPECIAL, 4), 'P20.4')
        self.assertEqual(gxdb.create_line_name('899', gxdb.LINE_TYPE_TIE, 1), 'T899.1')
        self.assertEqual(gxdb.create_line_name('899', gxdb.LINE_TYPE_TEST, 1), 'S899.1')
        self.assertEqual(gxdb.create_line_name('899', gxdb.LINE_TYPE_TREND, 1), 'R899.1')

    def test_bearing(self):
        self.start()
        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:
            ln = gxdb.Line(gdb, 'D578625')
            self.assertAlmostEqual(ln.bearing(), 0.0)

    def test_metadata(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as g:
            m = g.metadata
            gm = m['geosoft']
            self.assertEqual(len(gm), 2)
            self.assertTrue('dataset' in gm)
            self.assertTrue('georeference' in gm['dataset'])

            newstuff = {'maki': {'a': 1, 'b': (4, 5, 6), 'units': 'nT'}}
            g.metadata = newstuff

        with gxdb.Geosoft_gdb.open(self.gdb_name) as g:
            m = g.metadata

            gm = m['geosoft']
            self.assertEqual(len(gm), 2)
            self.assertTrue('dataset' in gm)

            maki = m['maki']
            self.assertEqual(maki['b'], ['4', '5', '6'])
            self.assertEqual(maki['units'], 'nT')

        with gxdb.Geosoft_gdb.open(self.gdb_name) as g:
            d = g.get_gx_metadata().meta_dict()
            self.assertTrue('Geosoft' in d)

    def test_coordinate_system(self):
        self.start()
        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            try:
                x, y, z = gdb.xyz_channels
                self.assertEqual(gxdb.Channel(gdb, x).unit_of_measure, 'm')
                gdb.coordinate_system = '{"units": "km"}'
                self.assertEqual(gxdb.Channel(gdb, x).unit_of_measure, 'km')
                self.assertEqual(gxdb.Channel(gdb, y).unit_of_measure, 'km')
                self.assertEqual(gxdb.Channel(gdb, z).unit_of_measure, 'km')
                self.assertEqual(gdb.coordinate_system, '*unknown')

                gxdb.Channel(gdb, 'Z').delete()
                self.assertEqual(gdb.xyz_channels, ('X', 'Y', None))
                gdb.coordinate_system = '{"units": "cm"}'
                self.assertEqual(gxdb.Channel(gdb, x).unit_of_measure, 'cm')
                self.assertEqual(gxdb.Channel(gdb, y).unit_of_measure, 'cm')

            finally:
                gdb.discard()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            try:
                self.assertEqual(str(gdb.coordinate_system), 'Corrego Alegre 1970-72 / UTM zone 23S')
                gdb.coordinate_system = 'NAD83 / UTM zone 25N'
                self.assertEqual(str(gdb.coordinate_system), 'NAD83 / UTM zone 25N')
            finally:
                gdb.discard()


    def test_dup(self):
        self.start()
        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            try:
                gxdb.Channel(gdb, 'x').width = 45
                gxdb.Channel(gdb, 'x').decimal = 4
                xx = gxdb.Channel.new(gdb, 'xx', dup='x')
                self.assertEqual(xx.unit_of_measure, 'm')
                self.assertEqual(xx.width, 45)
                self.assertEqual(xx.decimal, 4)

                master_line = gxdb.Line(gdb, list(gdb.list_lines())[0])
                master_line.flight = 77
                copyline = gxdb.Line.new(gdb, 'D234567', dup=master_line)
                self.assertEqual(copyline.flight, 77)

            finally:
                gdb.discard()

    @unittest.skip('skipping to let fixture pass')
    def test_large_stress(self):
        self.start()

        try:
            name = None
            with gxdb.Geosoft_gdb.new('new', overwrite=True, comp=gxdb.COMP_NONE, pageSize=64) as gdb:
                name = gdb.file_name
                npd = np.zeros(1000000) #TODO, this is 8 meg of data. This should not fit in 4 meg.
                line = gdb.new_line('test')
                gdb.write_line(line, npd, ['xx'])
                npd2, ch, fid = gdb.read_line(line)
                self.assertEqual(len(ch), 1)

            with gxdb.Geosoft_gdb.new('new', overwrite=True, comp=gxdb.COMP_NONE, pageSize=64) as gdb:
                name = gdb.file_name
                npd = np.zeros(4000000) #TODO, this is 32 meg of data, reported as 4.11 meg in the error?
                line = gdb.new_line('test')
                gdb.write_line(line, npd, ['xx'])
                npd2, ch, fid = gdb.read_line(line)
                self.assertEqual(len(ch), 1)

        finally:
            gxdb.delete_files(name)

    def test_code_example(self):
        self.start()

        gdb = gxdb.Geosoft_gdb.open(self.gdb_name)

        try:
            for line in gdb.list_lines():
                npd, ch, fid = gdb.read_line(line, channels=['X', 'Y', 'Z'])

                npd = np.square(npd)
                distance_from_origin = np.sqrt(npd[0] + npd[1] + npd[2])

                gdb.write_channel(line, 'distance', distance_from_origin, fid)

        finally:
            gdb.discard()


    def test_figure(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:
            #map_file = gdb.figure_map(title='gdb_test', features='all').file_name
            #self.crc_map(map_file)
            pass


###############################################################################################

if __name__ == '__main__':

    unittest.main()
