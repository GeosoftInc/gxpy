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

    def test_read_write_channel_vv_va(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:
            gdb.delete_channel('test_chan_vv')
            vv = gxvv.GXvv(np.array([1.,2.,3.]), fid=(-10, 2.5))
            gdb.write_channel_vv('T46', 'test_chan_vv', vv)
            vv = gdb.read_channel_vv('T46', 'test_chan_vv')
            self.assertEqual(vv.length, 3)
            self.assertEqual(vv.fid, (-10.0, 2.5))
            va = gdb.read_channel_va('T46', 'test_chan_vv')
            self.assertEqual(va.width, 1)
            self.assertEqual(va.length, 3)
            self.assertEqual(va.fid, (-10.0, 2.5))
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

    def test_various(self):
        self.start()

        def setxyz(xyz):
            gdb.xyz_channels = xyz


        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:
            self.assertRaises(gxdb.GdbException, gdb.is_line, 'nope', True)
            self.assertRaises(gxdb.GdbException, gdb.is_channel, 'nope', True)
            self.assertRaises(gxdb.GdbException, setxyz, ('x', 'y', 'crazy_cannot_exist'))
            gdb.discard()


    def test_read_masked_GDB(self):
        self.start()


        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

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

            gdb.discard()

    def test_write_vv_GDB(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            gdb.delete_channel('test')
            gdb.new_channel('test')
            vv = gxvv.GXvv(np.array([1.0,2.0,3.0,4.0]))
            gdb.write_channel_vv('D590875', 'test', vv)
            npd, ch, fid = gdb.read_line('D590875', channels=['test'])
            self.assertEqual(npd.shape,(4,1))
            self.assertEqual(npd[:,0].tolist(),[1.0,2.0,3.0,4.0])

            gdb.delete_channel('test')
            gdb.new_channel('test', np.float64)
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

            npd,ch,fid = gdb.read_line('D578625',channels=['dx','dy','vector'])

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
            gdb.write_line('testline',npd,channels=ch)
            npd2,ch2,fid2 = gdb.read_line('testline',channels=ch)
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
            gdb.write_line('testline',npd,channels=ch)
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

            gdb.discard()

    def test_new(self):
        self.start()

        gdb_file = os.path.join(self.folder, 'new.gdb')
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
        with gxdb.Geosoft_gdb.new( os.path.join(self.folder, gdb_file), overwrite=True) as gdb:
            pass
        gxdb.delete_files(gdb_file)


    def test_details(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

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

            gdb.discard()

    def test_channel(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            gdb.delete_channel("detailtest")
            ch = gxdb.Channel.new(gdb, "detailtest")
            det = gdb.channel_details(ch.name)
            try:
                self.assertEqual(ch.name, det['name'])
                self.assertEqual(ch.array, det['array'])
                self.assertEqual(ch.decimal, det['decimal'])
                self.assertEqual(ch.format, det['format'])
                self.assertEqual(ch.label, det['label'])
                self.assertEqual(ch.protect, det['protect'])
                self.assertEqual(ch.symbol, det['symbol'])
                self.assertEqual(ch.type, det['type'])
                self.assertEqual(ch.unit, det['unit'])
                self.assertEqual(ch.width, det['width'])
                self.assertEqual(ch.class_, det['class'])

                ch.protect = 1
                ch.decimal = 6
                ch.width = 10
                ch.unit = 'nT'
                ch.label = 'weirdo'
                ch.format = gxapi.DB_CHAN_FORMAT_GEOGR
                ch.class_ = 'geochem'
                self.assertEqual(ch.protect, True)
                self.assertEqual(ch.decimal, 6)
                self.assertEqual(ch.unit, 'nT')
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

            finally:
                self.assertRaises(gxdb.GdbException, gdb.delete_channel, ch.name)
                ch.protect = False
                gdb.delete_channel(ch.name)
                gdb.discard()

    def test_line(self):
        self.start()

        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:

            gdb.delete_line("T9999")
            ln = gxdb.Line.new(gdb, "T9999")
            det = gdb.line_details(ln.name)
            try:
                self.assertEqual(ln.name, det['name'])
                self.assertEqual(ln.category, det['category'])
                self.assertEqual(ln.date, det['date'])
                self.assertEqual(ln.flight, det['flight'])
                self.assertEqual(ln.number, det['number'])
                self.assertEqual(ln.type, det['type'])
                self.assertEqual(ln.version, det['version'])
                self.assertEqual(ln.group_class, det['groupclass'])
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
                try:
                    ln.group_class = 'billy'
                    self.assertTrue(False)
                except gxdb.GdbException:
                    pass

            finally:
                gdb.delete_line(ln.name)

            gdb.delete_line("L88")
            ln = gxdb.Line.new(gdb, "L88", group='john')
            try:
                self.assertEqual(ln.group_class, 'john')
                ln.group_class = 'billy'
                self.assertEqual(ln.group_class, 'billy')
            finally:
                gdb.delete_line(ln.name)

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

    def test_coordinate_system(self):
        self.start()
        with gxdb.Geosoft_gdb.open(self.gdb_name) as gdb:
            try:
                self.assertEqual(str(gdb.coordinate_system), 'Corrego Alegre 1970-72 / UTM zone 23S')
                gdb.coordinate_system = 'NAD83 / UTM zone 25N'
                self.assertEqual(str(gdb.coordinate_system), 'NAD83 / UTM zone 25N')
            finally:
                gdb.discard()


###############################################################################################

if __name__ == '__main__':

    unittest.main()
