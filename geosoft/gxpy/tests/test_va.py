import numpy as np
import unittest

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.va as gxva

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

    def test_va(self):
        self.start(gsys.func_name())

        self.assertEqual(gxva.__version__, geosoft.__version__)

        with gxva.GXva(12, np.float) as va:
            self.assertEqual(va.fid(), (0.0,1.0))
            self.assertEqual(va.width(), 12)

        fid = (10.1,0.99)
        with gxva.GXva(7, np.float,fid=fid) as va:
            self.assertEqual(va.fid(), fid)
            self.assertEqual(va.width(), 7)

            fid = (-45,7)
            va.setFid(fid)
            self.assertEqual(va.fid(),fid)

            va.reFid((-40,8),4)
            self.assertEqual(va.fid(),(-40,8))
            self.assertEqual(va.length(),4)

    def test_np(self):
        self.start(gsys.func_name())

        fid = (99,0.1)
        npdata = np.array(range(45)).reshape((9,5))
        with gxva.GXva.va_np(npdata, fid=fid) as va:
            self.assertEqual(va.fid(), fid)
            self.assertEqual(va.length(), npdata.shape[0])
            self.assertEqual(va.width(), npdata.shape[1])

            np2 = va.np(va.dtype())
            self.assertEqual(np2[0].shape, npdata.shape)
            np2,fid2 = va.np(va.dtype(), start=1)
            self.assertEqual(fid2,(99.1,.1))
            self.assertEqual(np2.shape, (8, 5))
            self.assertEqual(va.np(start=6)[0].shape, (3, 5))
            try:
                self.assertEqual(va.np(va.dtype(), start=50)[0].shape, (0,))
                self.assertTrue(False)
            except gxva.VAException:
                pass

            np3,fid3 = va.np(np.int)
            self.assertEqual(fid3,fid)
            self.assertEqual(np3[0, 0], 0)
            self.assertEqual(np3[1, 4], 9)

            np3, fid3 = va.np(np.float64)
            self.assertEqual(fid3, fid)
            self.assertEqual(np3[0, 0], 0.0)
            self.assertEqual(np3[1, 4], 9.0)

        npdata = np.array(range(64), dtype=np.int).reshape(4, 16)
        with gxva.GXva.va_np(npdata, fid=fid) as va:
            np3, fid = va.np(dtype=np.int64)
            self.assertEqual(np3[0, 0], 0.)
            self.assertEqual(np3[2, 11], 43)
            np3, fid = va.np(np.float)
            self.assertEqual(np3[0, 0], 0.)
            self.assertEqual(np3[2, 11], 43.)

            va.va(np.array(range(32), dtype=np.int))
            np3, fid = va.np(dtype=np.int64)
            self.assertEqual(np3.shape[0], 2)
            self.assertEqual(np3[0,0], 0)
            self.assertEqual(np3[1,15], 31)

    def test_strings(self):
        self.start(gsys.func_name())

        fidva = (99,0.1)
        npdata = np.array(["name","maki","neil","macleod"]).reshape(2,2)
        try:
            va = gxva.GXva.va_np(npdata, fid=fidva)
            self.assertTrue(False)
        except gxva.VAException:
            pass

##############################################################################################
if __name__ == '__main__':

    unittest.main()