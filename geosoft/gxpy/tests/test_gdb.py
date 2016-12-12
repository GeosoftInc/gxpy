import unittest
import os
import numpy as np
import gc
from PIL import Image

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.utility as gxu
import geosoft.gxpy.system as gsys
import geosoft.gxpy.gdb as gxgdb

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gx = gx.GXpy()
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'test_database.zip'))
        cls.gdb_name = os.path.join(cls.folder, files[0])
        cls.gdb = gxgdb.GXdb.open(cls.gdb_name)


    @classmethod
    def tearDownClass(cls):
        del cls.gdb
        gc.collect()
        try: gsys.remove_dir(cls.folder)
        except: pass

        pass

    @classmethod
    def start(cls,test):
        print("\n*** {} *** - {}".format(test, geosoft.__version__))
        
    def tf(f):
        return os.path.join(os.path.dirname(__file__), f)

    def test_gdb(self):
        self.start(gsys.func_name())
        self.assertEqual(gxgdb.__version__, geosoft.__version__)

    def test_noprops_GDB(self):
        self.start(gsys.func_name())

        gdb = self.gdb
        self.assertEqual(gdb.file_name(),self.gdb_name)
        self.assertEqual(str(gdb),os.path.basename(self.gdb_name))
        self.assertTrue(len(gdb.list_channels())>=6)
        self.assertTrue('X' in gdb.list_channels())
        self.assertTrue('dx' in gdb.list_channels(chan=gxgdb.CHAN_ALL))
        self.assertTrue('vector' in gdb.list_channels(chan=gxgdb.CHAN_ARRAY))
        self.assertFalse('vector' in gdb.list_channels(chan=gxgdb.CHAN_NORMAL))

        self.assertEqual(gdb.channel_width('vector'),3)
        self.assertEqual(gdb.channel_width('x'),1)

        gdb.discard()

    def test_group_VA_read_write(self):
        self.start(gsys.func_name())

        gdb = self.gdb
        self.assertEqual(gdb.file_name(),self.gdb_name)
        self.assertEqual(str(gdb),os.path.basename(self.gdb_name))
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
        self.start(gsys.func_name())

        gdb = self.gdb

        gdb.delete_channel('ian')
        gdb.new_channel('ian')
        self.assertTrue('ian' in gdb.list_channels())
        gdb.delete_channel('ian')
        self.assertFalse('ian' in gdb.list_channels())

        gdb.delete_channel('ian2')
        gdb.new_channel('ian2', np.int32, array =3)
        self.assertTrue('ian2' in gdb.list_channels(chan=gxgdb.CHAN_ARRAY))
        gdb.delete_channel('ian2')
        self.assertFalse('ian2' in gdb.list_channels())


    def test_properties_GDB(self):
        self.start(gsys.func_name())

        gdb = self.gdb

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
        self.start(gsys.func_name())

        gdb = self.gdb

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
        self.start(gsys.func_name())

        gdb = self.gdb

        data = gdb.read_line_vv('D578625')
        for chvv in data:
            self.assertEqual(len(data), 8)
            vv = chvv[1]
            fid = vv.fid()
            self.assertEqual(vv.length(), 832)
            self.assertEqual(fid[0], 0.0)
            self.assertEqual(fid[1], 1.0)

        data = gdb.read_line_vv('D578625', common_fid=True)
        for chvv in data:
            self.assertEqual(len(data), 8)
            vv = chvv[1]
            fid = vv.fid()
            self.assertEqual(vv.length(), 832)
            self.assertEqual(fid[0], 0.0)
            self.assertEqual(fid[1], 1.0)

        data = gdb.read_line_vv('D578625', common_fid=True, fid=(0.1,4.8))
        for chvv in data:
            self.assertEqual(len(data), 8)
            vv = chvv[1]
            fid = vv.fid()
            self.assertEqual(vv.length(), 175)
            self.assertEqual(fid[0], 0.1)
            self.assertEqual(fid[1], 4.8)

        ln,ls = gdb.line_name_symb('D578625')
        data = gdb.read_line_vv(ls,channels=['X','Y','Z','dx','dy'])
        self.assertEqual(len(data), 5)
        self.assertEqual(data[0][0], 'X')
        self.assertEqual(data[4][0], 'dy')
        npd = data[0][1].np()[0]
        self.assertEqual(npd[10], 578625.0)
        npd = data[1][1].np()[0]
        self.assertEqual(npd[10], 7773625.0)
        npd = data[2][1].np()[0]
        self.assertEqual(npd[10], -1195.7531280517615)

        data = gdb.read_line_vv(ls, 'X')
        self.assertEqual(data[0][0], 'X')
        npd = data[0][1].np()[0]
        self.assertEqual(npd[10],578625.0)

        data = gdb.read_line_vv(ls,channels=['X','Y','Z'], dtype='<U32')
        npd = data[0][1].np()[0]
        self.assertEqual(npd[10], '578625.0')
        npd = data[1][1].np()[0]
        self.assertEqual(npd[10], '7773625.0')
        npd = data[2][1].np()[0]
        self.assertEqual(npd[10], '-1195.8')

        gdb.discard()

    def test_read_masked_GDB(self):
        self.start(gsys.func_name())

        gdb = self.gdb

        npd,ch,fid = gdb.read_line('D2', dummy=gxgdb.READ_REMOVE_DUMMYROWS)
        self.assertEqual(npd.shape, (825, 8))
        self.assertEqual(npd.shape[1], 8)
        self.assertEqual(npd.shape[1], len(ch))

        npd,ch,fid = gdb.read_line('D2',dummy=gxgdb.READ_REMOVE_DUMMYCOLUMNS)
        self.assertEqual(npd.shape, (832,2))
        self.assertEqual(npd.shape[1], len(ch))

        npd,ch,fid = gdb.read_line('D2', channels=('x','y'), dummy=gxgdb.READ_REMOVE_DUMMYCOLUMNS)
        self.assertEqual(npd.shape, (832,1))
        self.assertEqual(npd.shape[1], len(ch))

        gdb.discard()

    def test_write_GDB(self):
        self.start(gsys.func_name())

        gdb = self.gdb

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
        self.start(gsys.func_name())

        gdb = self.gdb

        gdb.delete_channel('testVA')
        gdb.new_channel('testVA')
        try:
            gdb.write_channel('D590875', 'testVA',
                              np.array([[1.0, 2.0, 3.0, 4.0], [10.0, 20.0, 30.0, 40.0], [15.0, 25.0, 35.0, 45.0]]))
            self.assertTrue(False)
        except gxgdb.GDBException:
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
        self.start(gsys.func_name())

        gdb = self.gdb

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


    def test_newline_GDB(self):
        self.start(gsys.func_name())

        gdb = self.gdb
        npd,ch,fid = gdb.read_line('D578625',channels=['dx','dy','vector'])

        try:
            gdb.new_line("&$#@**")
            self.assertTrue(False)
        except gxgdb.GDBException: pass

        try:
            gdb.new_line("D578625")
            self.assertTrue(False)
        except gxgdb.GDBException: pass

        gdb.delete_line('wonk')
        gdb.new_line('wonk',group="wink")
        try:
            gdb.new_line('wonk')
            self.assertTrue(False)
        except gxgdb.GDBException: pass
        gdb.delete_line('wonk')

        gdb.delete_line('testline')
        gdb.new_line('testline')
        gdb.write_line('testline',npd,channels=ch)
        npd2,ch2,fid2 = gdb.read_line('testline',channels=ch)
        self.assertEqual(npd.shape,npd2.shape)

        gdb.delete_line('testline')
        gdb.new_line('testline',gxgdb.SYMB_LINE_NORMAL)
        gdb.write_line('testline',npd[:,0],"single")
        npd2,ch2,fid2 = gdb.read_line('testline',"single")
        self.assertEqual(npd2.shape,(npd.shape[0],1))

        gdb.delete_line('testline')
        gdb.new_line('testline',gxgdb.SYMB_LINE_GROUP)
        gdb.write_line('testline',npd[:,0],"single")
        npd2,ch2,fid2 = gdb.read_line('testline',"single")
        self.assertEqual(npd2.shape,(npd.shape[0],1))

        gdb.delete_line('testline')
        gdb.new_line('testline',linetype=gxgdb.SYMB_LINE_FLIGHT)
        ch = ['a','b','c','d']
        try:
            gdb.write_line('testline', npd, channels=ch)
            self.assertTrue(False)
        except gxgdb.GDBException:
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
        self.start(gsys.func_name())

        def progress(txt,pct):
            print(txt,pct)

        self.nl = 0
        self.stp = 100
        def enough():
            self.nl += 1
            if self.nl >= self.stp: return True
            else: return False

        gdb = self.gdb
        gdb.select_lines(select=False)
        gdb.select_lines('D578625,D2',select=True)
        self.nl = 0
        self.stp = 2

        gdb.delete_channel('testlist')
        gdb.new_channel('testlist',dtype=np.int)
        gdb.write_channel('D578625', 'testlist', np.array([1,2,3,4,4,4,5,6,7,7,7,6,5,4], dtype=np.int))
        gdb.write_channel('D2', 'testlist', np.array([12,12,12,13,13,13], dtype=np.int))

        listVal = gdb.list_values('testlist', max=100, progress=progress, stop=enough)
        listVal.sort()
        self.assertEqual(listVal, ['1','12','13','2','3','4','5','6','7'])
        self.nl = 0
        self.stp = 1
        listVal = gdb.list_values('dx', max=10000, progress=progress)
        self.assertEqual(len(listVal),29)
        listVal = gdb.list_values('dx')
        self.assertEqual(len(listVal),29)

        gdb.discard()

    def test_new(self):
        self.start(gsys.func_name())

        with gxgdb.GXdb.new( os.path.join(self.folder, 'new.gdb')) as gdb:

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

    def test_details(self):
        self.start(gsys.func_name())

        gdb = self.gdb
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
        self.assertEqual(det.get('category'),gxgdb.SYMB_LINE_NORMAL)
        self.assertEqual(det.get('number'),578625)
        self.assertEqual(det.get('name'),'D578625')
        self.assertEqual(det.get('flight'),0)
        self.assertEqual(det.get('version'),0)
        self.assertEqual(det.get('type'),gxapi.DB_LINE_TYPE_RANDOM)
        self.assertEqual(det.get('groupclass'),'')

        gdb.delete_line('testgroup')
        ls = gdb.new_line('testgroup', group="TeSt")
        det = gdb.line_details(ls)
        self.assertEqual(det.get('category'),gxgdb.SYMB_LINE_GROUP)
        self.assertEqual(det.get('name'),'testgroup')
        self.assertEqual(det.get('symbol'),ls)
        self.assertEqual(det.get('groupclass'),'TeSt')
        gdb.delete_line('testgroup')

        gdb.discard()

    def test_examples(self):
        self.start(gsys.func_name())

        gdb = self.gdb
        gdb.select_lines('',select=False)
        gdb.select_lines('Testline,D578625,P3',select=True)
        lines = gdb.list_lines()
        for line in lines:

            try:
                npd,ch,fid = gdb.read_line(line)
                # npd is a 2D numpy array to all data in this line; ch is a list of the channels;
                # fid is the (start,increment) fiducial.

                # do something with the data in npd ...
                print('{}: {}'.format(line,npd.shape))


            except gxgdb.GDBException as err:
                print ("Reading line '{}': encountered error: {}".format(line,err))


###############################################################################################

if __name__ == '__main__':

    unittest.main()
