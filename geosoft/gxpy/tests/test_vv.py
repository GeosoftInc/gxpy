import numpy as np
import unittest

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.vv as gxvv

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gxp = gx.GXpy()

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def start(cls,test):
        print("\n*** {} *** - {}".format(test, geosoft.__version__))

    def test_vv(self):
        self.start(gsys.func_name())

        self.assertEqual(gxvv.__version__, geosoft.__version__)

        with gxvv.GXvv(np.float) as vv:
            self.assertEqual(vv.fid(),(0.0,1.0))

        fid = (10.1,0.99)
        with gxvv.GXvv(np.float,fid=fid) as vv:
            self.assertEqual(vv.fid(),fid)

            fid = (-45,7)
            vv.setFid(fid)
            self.assertEqual(vv.fid(),fid)

            vv.reFid((-40,8),4)
            self.assertEqual(vv.fid(),(-40,8))
            self.assertEqual(vv.length(),4)

    def test_np(self):
        self.start(gsys.func_name())

        fid = (99,0.1)
        npdata = np.array([1,2,3,4,5,6,7])
        vv = gxvv.GXvv.vvNp(npdata, fid=fid)
        self.assertEqual(vv.fid(),fid)
        self.assertEqual(vv.length(),len(npdata))

        np2 = vv.np(vv.dtype())
        self.assertEqual(np2[0].shape,(7,))
        np2,fid2 = vv.np(vv.dtype(),start=1)
        self.assertEqual(fid2,(99.1,.1))
        self.assertEqual(np2.shape,(6,))
        self.assertEqual(vv.np(vv.dtype(),start=6)[0].shape,(1,))
        try:
            self.assertEqual(vv.np(vv.dtype(),start=7)[0].shape,(0,))
            self.assertTrue(False)
        except: pass

        np3,fid3 = vv.np(np.int)
        self.assertEqual(fid3,fid)
        self.assertEqual(np3[0],1)
        self.assertEqual(np3[6],7)

        npdata = np.array([1,2,3,4,5,6,7],dtype=np.int)
        vv = gxvv.GXvv.vvNp(npdata, fid=fid)
        np3= vv.np(dtype=np.int64)
        self.assertEqual(np3[0][0],1)
        self.assertEqual(np3[0][6],7)
        np3 = vv.np(np.float)
        self.assertEqual(np3[0][0],1.)
        self.assertEqual(np3[0][6],7.)

        vv.vv(np.array([4,5,6,7],dtype=np.int))
        np3,fid = vv.np(dtype=np.int64)
        self.assertEqual(len(np3), 4)
        self.assertEqual(np3[0], 4)
        self.assertEqual(np3[3], 7)
        np3,fid = vv.np(np.float)
        self.assertEqual(np3[0], 4.)
        self.assertEqual(np3[3], 7.)

        npdata = np.array(['4', '5', '6', '7'])
        vv3= gxvv.GXvv.vvNp(npdata, fid=fid)
        np3, fid = vv3.np()
        self.assertEqual(len(np3), 4)
        self.assertEqual(np3[0], '4')
        self.assertEqual(np3[3], '7')
        np3, fid = vv.np(np.float)
        self.assertEqual(np3[0], 4.)
        self.assertEqual(np3[3], 7.)

        npdata = np.array(['4000', '50', '60', '-70'])
        vv3 = gxvv.GXvv.vvNp(npdata, fid=fid)
        np3, fid = vv3.np()
        self.assertEqual(len(np3), 4)
        self.assertEqual(np3[0], '4000')
        self.assertEqual(np3[3], '-70')
        np3, fid = vv3.np(np.float)
        self.assertEqual(np3[0], 4000.)
        self.assertEqual(np3[3], -70.)

    def test_strings(self):
        self.start(gsys.func_name())

        fidvv = (99,0.1)
        npdata = np.array(["name","ian","neil","macleod"])
        vv = gxvv.GXvv.vvNp(npdata, fid=fidvv)
        self.assertEqual(vv.fid(),fidvv)
        self.assertEqual(vv.length(),len(npdata))
        self.assertEqual(vv.gxtype(),-7)
        self.assertTrue(vv.dtype().type is np.str_)
        self.assertEqual(str(vv.dtype()),'<U7')

        npd,fid = vv.np(vv.dtype())
        self.assertEqual(npd[0],"name")
        self.assertEqual(npd[1],"ian")
        self.assertEqual(npd[2],"neil")
        self.assertEqual(npd[3],"macleod")

        npd,fid = vv.np(vv.dtype(),start=2,n=2)
        self.assertEqual(npd[0],"neil")
        self.assertEqual(npd[1],"macleod")
        self.assertEqual(fid,(99.2,0.1))

        npdata = np.array(["1","2","3","4000","*"])
        vv = gxvv.GXvv.vvNp(npdata, fid=fid)
        npd,fid = vv.np(np.float)
        self.assertEqual(npd[0],1.0)
        self.assertEqual(npd[1],2.0)
        self.assertEqual(npd[2],3.0)
        self.assertEqual(npd[3],4000.0)
        self.assertEqual(npd[4],gxapi.rDUMMY)

        npdata = np.array(["1","2","3","4000","40000","*"])
        vv = gxvv.GXvv.vvNp(npdata, fid=fid)
        npd,fid = vv.np(np.int)
        self.assertEqual(npd[0],1)
        self.assertEqual(npd[1],2)
        self.assertEqual(npd[2],3)
        self.assertEqual(npd[3],4000)
        self.assertEqual(npd[4],40000)
        self.assertEqual(npd[5],gxapi.iDUMMY)

        npdata = np.array(["1","2","3","4000","40000","*"])
        vv = gxvv.GXvv.vvNp(npdata, fid=fid)
        npd,fid = vv.np(np.int,start=2, n=3)
        self.assertEqual(npd[0],3)
        self.assertEqual(npd[1],4000)
        self.assertEqual(npd[2],40000)


        npdata = np.array(["make_it_big enough"])
        vv = gxvv.GXvv.vvNp(npdata, fid=fid)
        npd, fid = vv.np(np.int, start=0, n=1)
        self.assertEqual(npd[0], gxapi.iDUMMY)

        npdata = np.array([1.,2.,-30.,-87.66662])
        vv.vv(npdata)
        npd, fid = vv.np(start=0, n=4)
        self.assertEqual(npd[0], "1.0")
        self.assertEqual(npd[2], "-30.0")
        self.assertEqual(npd[3], "-87.66662")

##############################################################################################
if __name__ == '__main__':

    unittest.main()