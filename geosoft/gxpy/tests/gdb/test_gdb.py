#TODO review fiducials reading/writing with respect to VV
#TODO can read compound line with VA, but what about writing?
#TODO write VA channel

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
        self.assertEqual(gdb.fileName(),self.gdb_name)
        self.assertEqual(str(gdb),os.path.basename(self.gdb_name))
        gdb.readLine('D578625',channels=['x','y','z','vector']) #to force creation of VA slices

        self.assertTrue(len(gdb.channels())>=6)
        self.assertTrue('X' in gdb.channels())
        self.assertTrue('dx' in gdb.channels(chan=gxgdb.CHAN_ALL))
        self.assertTrue(list(gdb.channels(chan=gxgdb.CHAN_DISPLAYED)) == [])
        self.assertTrue('vector' in gdb.channels(chan=gxgdb.CHAN_ARRAY))
        self.assertFalse('vector' in gdb.channels(chan=gxgdb.CHAN_NORMAL))

        self.assertEqual(gdb.chanArray('vector'),3)
        self.assertEqual(gdb.chanArray('x'),1)

        gdb.discard()

    def test_create_del_GDB(self):
        self.start(gsys.func_name())

        gdb = self.gdb

        gdb.delChan('ian')
        gdb.newChannel('ian')
        self.assertTrue('ian' in gdb.channels())
        gdb.delChan('ian')
        self.assertFalse('ian' in gdb.channels())

        gdb.delChan('ian2')
        gdb.newChannel('ian2', np.int32, array =3)
        self.assertTrue('ian2' in gdb.channels(chan=gxgdb.CHAN_ARRAY))
        gdb.delChan('ian2')
        self.assertFalse('ian2' in gdb.channels())


    def test_properties_GDB(self):
        self.start(gsys.func_name())

        gdb = self.gdb

        ch = gdb.channels()
        self.assertTrue('X' in ch)
        self.assertTrue('vector' in ch)
        self.assertEqual(ch.get('dx'),1153)

        try:
            gdb.lineNameSymb(8456712552)
            self.assertTrue(False)
        except: pass

        ln,ls = gdb.lineNameSymb('bogus',create=True)
        self.assertEqual(ln,'bogus')
        gdb.delLine('bogus')
        ls = gdb.lineNameSymb('bogus2',create=True)[1]
        gdb.delLine(ls)

        ln,ls = gdb.lineNameSymb('D578625')
        self.assertEqual(ln,'D578625')
        ln,ls = gdb.lineNameSymb('Dwonk')
        self.assertEqual(ln,'Dwonk')
        ln,ls = gdb.lineNameSymb(ls)
        self.assertEqual(ln,'Dwonk')

        gdb.delChan('ccva')
        gdb.newChannel('ccva',array=8)
        cn,cs = gdb.chanNameSymb('ccva')
        self.assertEqual(cn,'ccva')
        cn,cs = gdb.chanNameSymb('ccva[4]')
        self.assertEqual(cn,'ccva[4]')

        gdb.discard()
        cs = gdb.newChannel('cava',dtype=np.int64)
        self.assertTrue(gdb.chanDtype(cs).type is np.int64)

        gdb.selectLines(select=False)
        ln = gdb.lines()
        self.assertEqual(len(ln),0)

        gdb.selectLines('bogus')
        ln = gdb.lines()
        self.assertEqual(len(ln), 0)

        gdb.selectLines('D2')
        ln = gdb.lines()
        self.assertEqual(len(ln), 1)

        gdb.selectLines('D')
        ln = gdb.lines()
        self.assertEqual(len(ln), 3)
        self.assertTrue('D2' in ln)
        self.assertTrue('Dwonk' in ln)
        self.assertTrue('D578625' in ln)

        gdb.selectLines('D578625',select=False)
        ln = gdb.lines()
        self.assertFalse('D578625' in ln)
        self.assertEqual(len(ln), 2)

        gdb.discard()

    def test_read_GDB(self):
        self.start(gsys.func_name())

        gdb = self.gdb

        npd,ch,fid = gdb.readLine('D578625')
        self.assertEqual(npd.shape[0],832)
        self.assertEqual(fid[0],0.0)
        self.assertEqual(fid[1],1.0)

        ln,ls = gdb.lineNameSymb('D578625')
        npd,ch,fid = gdb.readLine(ls,channels=['X','Y','Z','dx','dy'])
        self.assertEqual(npd.shape,(832,5))
        self.assertEqual(npd[10,:3].tolist(),[578625.0, 7773625.0, -1195.7531280517615])

        npd,ch,fid = gdb.readLine(ls,'X')
        self.assertEqual(npd.shape,(832,1))
        self.assertEqual(npd[10],578625.0)

        npd,ch,fid = gdb.readLine(ls,channels=['X','Y','Z'], dtype='<U32')
        self.assertEqual(npd.shape,(832,3))
        self.assertEqual(npd[10,:3].tolist(),['578625.0', '7773625.0', '-1195.8'])

        gdb.discard()

    def test_read_masked_GDB(self):
        self.start(gsys.func_name())

        gdb = self.gdb

        npd,ch,fid = gdb.readLine('D2',dummy=gxgdb.READ_REMOVE_DUMMYROWS)
        self.assertEqual(npd.shape[0],825)
        self.assertEqual(npd.shape[1],8)
        self.assertEqual(npd.shape[1],len(ch))

        npd,ch,fid = gdb.readLine('D2',dummy=gxgdb.READ_REMOVE_DUMMYCOLUMNS)
        self.assertEqual(npd.shape,(832,2))
        self.assertEqual(npd.shape[1],len(ch))

        npd,ch,fid = gdb.readLine('D2', channels=('x','y'), dummy=gxgdb.READ_REMOVE_DUMMYCOLUMNS)
        self.assertEqual(npd.shape,(832,1))
        self.assertEqual(npd.shape[1],len(ch))

        gdb.discard()

    def test_write_GDB(self):
        self.start(gsys.func_name())

        gdb = self.gdb

        gdb.delChan('test')
        gdb.newChannel('test')
        gdb.writeDataChan('D590875','test',np.array([1.0,2.0,3.0,4.0]))
        npd,ch,fid = gdb.readLine('D590875',channels=['test'])
        self.assertEqual(npd.shape,(4,1))
        self.assertEqual(npd[:,0].tolist(),[1.0,2.0,3.0,4.0])

        gdb.delChan('test')
        gdb.newChannel('test', np.float64)
        gdb.writeDataChan('D590875','test',np.array([1,2,3,4],dtype=np.int))
        npd,ch,fid = gdb.readLine('D590875',channels=['test'],dtype=np.int)
        self.assertEqual(npd.shape,(4,1))
        self.assertEqual(npd[:,0].tolist(),[1,2,3,4])

        gdb.delChan('test')
        gdb.newChannel('test', np.int32)
        gdb.writeDataChan('D590875','test',np.array([1,2,3,4],dtype=np.int))
        npd,ch,fid = gdb.readLine('D590875',channels=['test'])
        self.assertEqual(npd.shape,(4,1))
        self.assertEqual(npd[:,0].tolist(),[1.0,2.0,3.0,4.0])

        gdb.delChan('test')
        gdb.newChannel('test', dtype=np.int32)
        gdb.writeDataChan('D590875','test',np.array([1,2,3,4],dtype=np.int),fid=(3,2))
        npd,ch,fid = gdb.readLine('D590875',channels=['test'])
        self.assertEqual(npd.shape,(4,1))
        self.assertEqual(npd[:,0].tolist(),[1.0,2.0,3.0,4.0])
        self.assertEqual(fid[0],3.0)
        self.assertEqual(fid[1],2.0)

        gdb.newChannel('test', np.int32)
        gdb.writeDataChan('D590875','test',np.array([1,2,3,4],dtype=np.int),fid=(2.50,0.33))
        npd,ch,fid = gdb.readLine('D590875',channels=['test'])
        self.assertEqual(npd.shape,(4,1))
        self.assertEqual(npd[:,0].tolist(),[1.0,2.0,3.0,4.0])
        self.assertEqual(fid[0],2.5)
        self.assertEqual(fid[1],0.33)

        gdb.delChan('test')

        gdb.discard()

    def test_dummy_GDB(self):
        self.start(gsys.func_name())

        gdb = self.gdb

        gdb.delChan('test')
        gdb.newChannel('test',dtype=np.int)
        dummy = gxu.gxDummy(np.int)
        gdb.writeDataChan('D590875','test',np.array([1,2,dummy,4]))
        npd,ch,fid = gdb.readLine('D590875',channels=['test'],dtype=np.int)
        self.assertEqual(npd.shape,(4,1))
        self.assertEqual(npd[:,0].tolist(),[1,2,dummy,4])

        dm = gxu.dummyMask(npd)
        self.assertEqual(dm.tolist(),[False,False,True,False])

        gdb.discard()


    def test_newline_GDB(self):
        self.start(gsys.func_name())

        gdb = self.gdb
        npd,ch,fid = gdb.readLine('D578625',channels=['dx','dy','vector'])

        try:
            gdb.newLine("&$#@**")
            self.assertTrue(False)
        except gxgdb.GDBException: pass

        try:
            gdb.newLine("D578625")
            self.assertTrue(False)
        except gxgdb.GDBException: pass

        gdb.delLine('wonk')
        gdb.newLine('wonk',group="wink")
        try:
            gdb.newLine('wonk')
            self.assertTrue(False)
        except gxgdb.GDBException: pass
        gdb.delLine('wonk')

        gdb.delLine('testline')
        gdb.newLine('testline')
        gdb.writeDataLine('testline',npd,channels=ch)
        npd2,ch2,fid2 = gdb.readLine('testline',channels=ch)
        self.assertEqual(npd.shape,npd2.shape)

        gdb.delLine('testline')
        gdb.newLine('testline',gxgdb.SYMB_LINE_NORMAL)
        gdb.writeDataLine('testline',npd[:,0],"single")
        npd2,ch2,fid2 = gdb.readLine('testline',"single")
        self.assertEqual(npd2.shape,(npd.shape[0],1))

        gdb.delLine('testline')
        gdb.newLine('testline',gxgdb.SYMB_LINE_GROUP)
        gdb.writeDataLine('testline',npd[:,0],"single")
        npd2,ch2,fid2 = gdb.readLine('testline',"single")
        self.assertEqual(npd2.shape,(npd.shape[0],1))

        gdb.delLine('testline')
        gdb.newLine('testline',linetype=gxgdb.SYMB_LINE_FLIGHT)
        ch = ['a','b','c','d']
        try:
            gdb.writeDataLine('testline',npd,channels=ch)
            self.assertTrue(False)
        except gxgdb.GDBException:
            pass

        ch = ['a','b','c','d','e']
        gdb.writeDataLine('testline',npd,channels=ch)
        npd2,ch2,fid2 = gdb.readLine('testline',channels=ch)
        self.assertEqual(npd.shape,npd2.shape)
        self.assertEqual(ch2,ch)
        gdb.delChan(ch)

        gdb.delLine('testline')
        gdb.newLine('testline')
        gdb.delChan("bopper")
        gdb.writeDataLine('testline',npd,channels="bopper")
        npd2,ch2,fid2 = gdb.readLine('testline',"bopper")
        self.assertEqual(npd.shape,npd2.shape)
        self.assertEqual(ch2[0],"bopper[0]")
        self.assertEqual(ch2[4],"bopper[4]")

        gdb.discard()


    def test_listValues_GDB(self):
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
        gdb.selectLines(select=False)
        gdb.selectLines('D578625,D2',select=True)
        self.nl = 0
        self.stp = 2

        gdb.delChan('testlist')
        gdb.newChannel('testlist',dtype=np.int)
        gdb.writeDataChan('D578625', 'testlist', np.array([1,2,3,4,4,4,5,6,7,7,7,6,5,4], dtype=np.int))
        gdb.writeDataChan('D2', 'testlist', np.array([12,12,12,13,13,13], dtype=np.int))

        listVal = gdb.listValues('testlist', max=100, progress=progress, stop=enough)
        listVal.sort()
        self.assertEqual(listVal, ['1','12','13','2','3','4','5','6','7'])
        self.nl = 0
        self.stp = 1
        listVal = gdb.listValues('dx', max=10000, progress=progress)
        self.assertEqual(len(listVal),29)
        listVal = gdb.listValues('dx')
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
            gdb.newChannel('R',dtype=np.int)
            gdb.newChannel('G',dtype=np.int)
            gdb.newChannel('B', dtype=np.int)
            gdb.newChannel('A', dtype=np.int)
            for l in range(imageIn.shape[0]):
                gdb.writeDataLine('L{}'.format(l),imageIn[l,:,:],channels=['R','G','B','A'])

            self.assertEqual(len(gdb.lines()),imageIn.shape[0])
            self.assertEqual(len(gdb.channels()),4)
            d,c,f = gdb.readLine('L5')
            self.assertEqual(d.shape[0],imageIn.shape[1])
            self.assertEqual(d.shape[1],imageIn.shape[2])

    def test_details(self):
        self.start(gsys.func_name())

        gdb = self.gdb
        cs = gdb.newChannel("detailtest")
        det = gdb.chanDetails(cs)
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

        gdb.chanSetDetails(cs,{'protect':1, 'decimal':6, 'unit':'ft'})
        det2 = gdb.chanDetails(cs)
        self.assertEqual(det2.get('protect'),1)
        self.assertEqual(det2.get('decimal'),6)
        self.assertEqual(det2.get('unit'),'ft')

        gdb.chanSetDetails(cs,det)
        det2 = gdb.chanDetails(cs)
        self.assertEqual(det2.get('protect'),0)
        self.assertEqual(det2.get('decimal'),2)
        self.assertEqual(det2.get('unit'),'')

        det = gdb.lineDetails('D578625')
        self.assertEqual(det.get('category'),gxgdb.SYMB_LINE_NORMAL)
        self.assertEqual(det.get('number'),578625)
        self.assertEqual(det.get('name'),'D578625')
        self.assertEqual(det.get('flight'),0)
        self.assertEqual(det.get('version'),0)
        self.assertEqual(det.get('type'),gxapi.DB_LINE_TYPE_RANDOM)
        self.assertEqual(det.get('groupclass'),'')

        gdb.delLine('testgroup')
        ls = gdb.newLine('testgroup',group="TeSt")
        det = gdb.lineDetails(ls)
        self.assertEqual(det.get('category'),gxgdb.SYMB_LINE_GROUP)
        self.assertEqual(det.get('name'),'testgroup')
        self.assertEqual(det.get('symbol'),ls)
        self.assertEqual(det.get('groupclass'),'TeSt')
        gdb.delLine('testgroup')

        gdb.discard()

    def test_examples(self):
        self.start(gsys.func_name())

        gdb = self.gdb
        gdb.selectLines('',select=False)
        gdb.selectLines('Testline,D578625,P3',select=True)
        lines = gdb.lines()
        for line in lines:

            try:
                npd,ch,fid = gdb.readLine(line)
                # npd is a 2D numpy array to all data in this line; ch is a list of the channels;
                # fid is the (start,increment) fiducial.

                # do something with the data in npd ...
                print('{}: {}'.format(line,npd.shape))


            except gxgdb.GDBException as err:
                print ("Reading line '{}': encountered error: {}".format(line,err))


###############################################################################################

if __name__ == '__main__':

    unittest.main()
