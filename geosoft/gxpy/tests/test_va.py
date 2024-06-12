import numpy as np
import unittest
import os

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.va as gxva
import geosoft.gxpy.utility as gxu

from base import GXPYTest


class Test(GXPYTest):
    def test_va(self):
        self.start()

        self.assertEqual(gxva.__version__, geosoft.__version__)

        with gxva.GXva(width=12, dtype=np.float_) as va:
            self.assertTrue(isinstance(va.gxva, gxapi.GXVA))
            self.assertEqual(va.fid, (0.0,1.0))
            self.assertEqual(va.width, 12)

        fid = (10.1,0.99)
        with gxva.GXva(width=7, dtype=np.float_, fid=fid) as va:
            self.assertEqual(va.fid, fid)
            self.assertEqual(va.width, 7)

            fid = (-45,7)
            va.fid = fid
            self.assertEqual(va.fid,fid)

            va.refid((-40,8),4)
            self.assertEqual(va.fid,(-40,8))
            self.assertEqual(va.length,4)
            self.assertEqual(va.dimensions, (4,7))
            self.assertEqual(va.gxtype, gxu.gx_dtype(np.float_))
            self.assertEqual(va.np.shape, (4, 7))

            va.length = 16
            self.assertEqual(va.fid,(-40,8))
            self.assertEqual(va.length,16)
            self.assertEqual(va.dimensions, (16,7))
            self.assertEqual(va.gxtype, gxu.gx_dtype(np.float_))
            self.assertEqual(va.np.shape, (16, 7))


    def test_exceptions(self):
        self.start()

        self.assertRaises(gxva.VAException, gxva.GXva,
                          np.array([["bones", "queens", "geology"], ["a", "b", "c"]]))

        with gxva.GXva([[1, 2, 3, 4, 5, 6, 7]], width=7, dtype=np.float_) as va:
            self.assertRaises(gxva.VAException, va.get_data, dtype="U7")

        with gxva.GXva(np.array(range(45)).reshape((9, 5))) as va:
            self.assertRaises(gxva.VAException, va.get_data, n=0)

        with gxva.GXva(np.array(range(45)).reshape((9, 5))) as va:
            self.assertRaises(gxva.VAException, va.get_data, n_col=0)

        with gxva.GXva(np.array(range(40)).reshape((20, 2))) as va:
            self.assertRaises(gxva.VAException, va.set_data, np.array(range(3)))

    def test_np(self):
        self.start()

        fid = (99,0.1)
        npdata = np.array(range(45)).reshape((9,5))
        with gxva.GXva(npdata, fid=fid) as va:
            self.assertEqual(va.fid, fid)
            self.assertEqual(va.length, npdata.shape[0])
            self.assertEqual(va.width, npdata.shape[1])

            np2 = va.get_data(va.dtype)
            self.assertEqual(np2[0].shape, npdata.shape)
            np2,fid2 = va.get_data(dtype=va.dtype, start=1)
            self.assertEqual(fid2,(99.1,.1))
            self.assertEqual(np2.shape, (8, 5))
            self.assertEqual(va.get_data(start=6)[0].shape, (3, 5))
            try:
                self.assertEqual(va.get_data(dtype=va.dtype, start=50)[0].shape, (0,))
                self.assertTrue(False)
            except gxva.VAException:
                pass

            np3,fid3 = va.get_data(np.int_)
            self.assertEqual(fid3,fid)
            self.assertEqual(np3[0, 0], 0)
            self.assertEqual(np3[1, 4], 9)

            np3, fid3 = va.get_data(np.float64)
            self.assertEqual(fid3, fid)
            self.assertEqual(np3[0, 0], 0.0)
            self.assertEqual(np3[1, 4], 9.0)

            np3, fid3 = va.get_data(np.float64, n=2)
            self.assertEqual(fid3, fid)
            self.assertEqual(np3.shape[0], 2)
            self.assertEqual(np3[0, 0], 0.0)
            self.assertEqual(np3[1, 4], 9.0)

            np3, fid3 = va.get_data(np.float64, n=99)
            self.assertEqual(fid3, fid)
            self.assertEqual(np3.shape[0], va.length)

            np3, fid3 = va.get_data(np.float64, n_col=3)
            self.assertEqual(fid3, fid)
            self.assertEqual(np3.shape[1], 3)

            np3, fid3 = va.get_data(np.float64, n_col=99)
            self.assertEqual(fid3, fid)
            self.assertEqual(np3.shape[1], va.width)

        npdata = np.array(range(64), dtype=np.int_).reshape(4, 16)
        npdata[1, 2] = gxapi.iDUMMY
        with gxva.GXva(npdata, fid=fid) as va:

            np3, fid = va.get_data(dtype=np.int64)
            self.assertEqual(np3[0, 0], 0.)
            self.assertEqual(np3[2, 11], 43)
            self.assertEqual(np3[1, 2], gxapi.GS_S8DM)

            np3, fid = va.get_data(dtype=np.int32)
            self.assertEqual(np3[0, 0], 0.)
            self.assertEqual(np3[2, 11], 43)
            self.assertEqual(np3[1, 2], gxapi.GS_S4DM)
            self.assertEqual(np3[1, 2], gxapi.iDUMMY)

            np3, fid = va.get_data(np.float_)
            self.assertEqual(np3[0, 0], 0.)
            self.assertEqual(np3[2, 11], 43.)
            self.assertTrue(np.isnan(np3[1, 2]))

            d = np.array(range(32), dtype=np.int_).reshape(-1, va.width)
            d[0,3] = gxu.gx_dummy(d.dtype)
            va.set_data(d)
            np3, fid = va.get_data(dtype=np.int32)
            self.assertEqual(np3.shape[0], 2)
            self.assertEqual(np3[0,0], 0)
            self.assertEqual(np3[1,15], 31)
            self.assertEqual(np3[0, 3], gxapi.GS_S4DM)

    def test_iterator(self):
        self.start()
        npdata = np.array(range(45)).reshape((9, 5))
        with gxva.GXva(npdata) as va:
            self.assertEqual(tuple(va[0][0]), (0, 1, 2, 3, 4))
            self.assertEqual(va[4][1], 4)
            list2d = [v[0] for v in va]
            self.assertEqual(tuple(list2d[1]), (5, 6, 7, 8, 9))
            self.assertEqual(va.np.shape, (9, 5))

    def test_strings(self):
        self.start()

        fidva = (99,0.1)
        npdata = np.array(["name","maki","neil","macleod"]).reshape(2,2)
        self.assertRaises(gxva.VAException, gxva.GXva, npdata, fid=fidva)

    def test_uom(self):
        self.start()

        npdata = np.array(range(45)).reshape((9, 5))
        with gxva.GXva(npdata, unit_of_measure='maki') as va:
            self.assertEqual(va.unit_of_measure, 'maki')
            va.unit_of_measure = 'nT'
            self.assertEqual(va.unit_of_measure, 'nT')

    def test_dummy_nan(self):
        self.start()

        npdata = np.array(range(45), dtype=np.float32).reshape((9, 5))
        npdata[0,1] = np.nan
        with gxva.GXva(npdata) as va:
            self.assertTrue(npdata[0,1])
            self.assertEqual(tuple(va[0][0])[4], 4.)
            self.assertTrue(np.isnan(va[0][0][1]))

    def test_empty(self):
        self.start()

        empty = np.array([[],[]])
        va = gxva.GXva(empty, width=2)
        self.assertEqual(len(va), 0)
        self.assertEqual(va.np.size, 0)
        va.set_data(empty)
        self.assertEqual(len(va), 0)
        self.assertEqual(va.np.size, 0)

##############################################################################################
if __name__ == '__main__':

    unittest.main()