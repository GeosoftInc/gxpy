#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import numpy as np
import os
import unittest

import geosoft
import geosoft.gxpy
import geosoft.gxapi as gxapi
import geosoft.gxpy.vv as gxvv
import geosoft.gxpy.utility as gxu

from base import GXPYTest


class Test(GXPYTest):
    def test_vv(self):
        self.start()

        self.assertEqual(gxvv.__version__, geosoft.__version__)

        with gxvv.GXvv(dtype=np.float_) as vv:
            self.assertTrue(vv.gxvv, gxapi.GXVV)
            self.assertEqual(vv.fid, (0.0, 1.0))

        fid = (10.1,0.99)
        with gxvv.GXvv(dtype=np.float_, fid=fid) as vv:
            self.assertTrue(vv.is_float)
            self.assertFalse(vv.is_int)
            self.assertFalse(vv.is_string)
            self.assertEqual(vv.fid, fid)
            self.assertEqual(vv.length, 0)

            fid = (-45,7)
            vv.fid = fid
            self.assertEqual(vv.fid, fid)

            vv.refid((-40, 8), 4)
            self.assertEqual(vv.fid, (-40,8))
            self.assertEqual(vv.length, 4)
            self.assertEqual(len(vv.np), 4)

            vv.length = 16
            self.assertEqual(vv.fid, (-40,8))
            self.assertEqual(vv.length, 16)
            self.assertEqual(len(vv.np), 16)
            self.assertEqual(vv.dim, 1)

            vv.refid((-38, 1.5))
            self.assertEqual(vv.fid, (-38, 1.5))
            self.assertEqual(vv.length, 80)

            vv.refid((1000, 50))
            self.assertEqual(vv.fid, (1000., 50.))
            self.assertEqual(vv.length, 0)

            self.assertRaises(gxvv.VVException, vv.refid, (1, 0))
            self.assertRaises(gxvv.VVException, vv.refid, (1, -1))

        with gxvv.GXvv([1, 2, 3, 4, 5, 6]) as vv:
            self.assertTrue(vv.is_int)
            self.assertFalse(vv.is_float)
            self.assertFalse(vv.is_string)

            self.assertEqual(vv.fid, (0.0, 1.0))
            self.assertEqual(vv.length, 6)
            self.assertEqual(vv.dtype, np.int32)
            self.assertEqual(vv.gxtype, gxu.gx_dtype(np.int32))

        with gxvv.GXvv([1, 2, 3, 4, 5, 6], dtype=np.int64) as vv:
            self.assertEqual(vv.fid, (0.0, 1.0))
            self.assertEqual(vv.length, 6)
            self.assertEqual(vv.dtype, np.int64)
            self.assertEqual(vv.gxtype, gxu.gx_dtype(np.int64))

    def test_init_len(self):
        self.start()
        with gxvv.GXvv(dtype=np.float_, len=10) as vv:
            self.assertEqual(vv.length, 10)

    def test_np(self):
        self.start()

        fid = (99,0.1)
        npdata = np.array([1,2,3,4,5,6,7])
        with gxvv.GXvv(npdata, fid=fid) as vv:
            self.assertEqual(vv.fid, fid)
            self.assertEqual(vv.length, len(npdata))

            np2 = vv.get_data(vv.dtype)
            self.assertEqual(np2[0].shape,(7,))
            np2,fid2 = vv.get_data(vv.dtype,start=1)
            self.assertEqual(fid2,(99.1,.1))
            self.assertEqual(np2.shape,(6,))
            self.assertEqual(vv.get_data(vv.dtype,start=6)[0].shape,(1,))
            self.assertRaises(gxvv.VVException, vv.get_data, vv.dtype, start=7)

            np3,fid3 = vv.get_data(np.int_)
            self.assertEqual(fid3,fid)
            self.assertEqual(np3[0], 1)
            self.assertEqual(np3[6], 7)

            self.assertEqual(float(vv.np[6]), 7.0)
            self.assertEqual(int(vv.np[6]), 7)
            self.assertEqual(str(vv.np[6]), "7")

        npdata = np.array([1,2,3,4,5,6,7],dtype=np.int_)
        with gxvv.GXvv(npdata, fid=fid) as vv:
            np3= vv.get_data(dtype=np.int64)
            self.assertEqual(np3[0][0],1)
            self.assertEqual(np3[0][6],7)
            np3 = vv.get_data(np.float_)
            self.assertEqual(np3[0][0],1.)
            self.assertEqual(np3[0][6],7.)

            vv.set_data(np.array([4,5,6,7], dtype=np.int_))
            np3,fid = vv.get_data(dtype=np.int64)
            self.assertEqual(len(np3), 4)
            self.assertEqual(np3[0], 4)
            self.assertEqual(np3[3], 7)
            np3,fid = vv.get_data(np.float_)
            self.assertEqual(np3[0], 4.)
            self.assertEqual(np3[3], 7.)

        npdata = np.array(['4', '5', '6', '7'])
        with gxvv.GXvv(npdata, fid=fid) as vv3:
            np3, fid = vv3.get_data()
            self.assertEqual(len(np3), 4)
            self.assertEqual(np3[0], '4')
            self.assertEqual(np3[3], '7')
            np3, fid = vv3.get_data(np.float_)
            self.assertEqual(np3[0], 4.)
            self.assertEqual(np3[3], 7.)

        npdata = np.array(['4000', '50', '60', '-70'])
        with gxvv.GXvv(npdata, fid=fid) as vv3:
            self.assertTrue(vv3.is_string)
            self.assertFalse(vv3.is_int)
            self.assertFalse(vv3.is_float)
            npf = vv3.np
            self.assertEqual(len(npf), 4)
            self.assertEqual(npf[0], '4000')
            self.assertEqual(npf[3], '-70')
            npf, fid = vv3.get_data(np.float_)
            self.assertEqual(npf[0], 4000.)
            self.assertEqual(npf[3], -70.)
            self.assertEqual(vv3.min_max(), (-70., 4000.))

        with gxvv.GXvv(['maki', 'bob']) as vv:
            self.assertEqual(vv.min_max(), (None, None))

        self.assertEqual(gxvv.GXvv(['*', 1]).min_max(), (1., 1.))

    def test_strings(self):
        self.start()

        fidvv = (99,0.1)
        npdata = np.array(["name", "maki", "neil", "rider"])
        with  gxvv.GXvv(npdata, fid=fidvv) as vv:
            self.assertTrue(vv.is_string)
            self.assertFalse(vv.is_int)
            self.assertFalse(vv.is_float)
            self.assertEqual(vv.fid,fidvv)
            self.assertEqual(vv.length,len(npdata))
            self.assertEqual(vv.gxtype,-20)
            self.assertTrue(vv.dtype.type is np.str_)
            self.assertEqual(str(vv.dtype),'<U5')

            npd,fid = vv.get_data(vv.dtype)
            self.assertEqual(npd[0],"name")
            self.assertEqual(npd[1],"maki")
            self.assertEqual(npd[2],"neil")
            self.assertEqual(npd[3],"rider")

            npd,fid = vv.get_data(vv.dtype,start=2,n=2)
            self.assertEqual(npd[0],"neil")
            self.assertEqual(npd[1],"rider")
            self.assertEqual(fid,(99.2,0.1))

            vv.fill(2.5)
            self.assertEqual(vv[0][0], '2.5')
            self.assertEqual(vv[len(vv) - 1][0], '2.5')

        npdata = np.array(["1","2","3","4000","*"])
        with gxvv.GXvv(npdata, fid=fid) as vv:
            npd,fid = vv.get_data(np.float_)
            self.assertEqual(npd[0],1.0)
            self.assertEqual(npd[1],2.0)
            self.assertEqual(npd[2],3.0)
            self.assertEqual(npd[3],4000.0)
            self.assertTrue(np.isnan(npd[4]))

        npdata = np.array(["1","2","3","4000","40000","*"])
        with gxvv.GXvv(npdata, fid=fid) as vv:
            npd,fid = vv.get_data(np.int_)
            self.assertEqual(npd[0],1)
            self.assertEqual(npd[1],2)
            self.assertEqual(npd[2],3)
            self.assertEqual(npd[3],4000)
            self.assertEqual(npd[4],40000)
            self.assertEqual(npd[5],gxapi.iDUMMY)

        with gxvv.GXvv(npdata, fid=fid, dtype=np.float_) as vv:
            npd, fid = vv.get_data(np.int_)
            self.assertEqual(npd[0],1)
            self.assertEqual(npd[1],2)
            self.assertEqual(npd[2],3)
            self.assertEqual(npd[3],4000)
            self.assertEqual(npd[4],40000)
            self.assertEqual(npd[5], gxapi.iDUMMY)
            npd, fid = vv.get_data(np.int32)
            self.assertEqual(npd[5], gxapi.GS_S4DM)
            npd, fid = vv.get_data(np.int64)
            self.assertEqual(npd[5], gxapi.GS_S8DM)
            npd, fid = vv.get_data(np.float_)
            self.assertTrue(np.isnan(npd[5]))
            npd, fid = vv.get_data(np.float32)
            self.assertTrue(np.isnan(npd[5]))
            npd, fid = vv.get_data(np.float64)
            self.assertTrue(np.isnan(npd[5]))

        with gxvv.GXvv(npdata, fid=fid, dtype=np.float32) as vv:
            npd, fid = vv.get_data(np.float)
            self.assertTrue(np.isnan(npd[5]))
            npd, fid = vv.get_data(np.float32)
            self.assertTrue(np.isnan(npd[5]))
            npd, fid = vv.get_data(np.float64)
            self.assertTrue(np.isnan(npd[5]))

        with gxvv.GXvv(npdata, fid=fid, dtype=np.int64) as vv:
            npd, fid = vv.get_data(np.float_)
            self.assertTrue(np.isnan(npd[5]))

        npdata = np.array(["1","2","3","4000","40000","*"])
        with gxvv.GXvv(npdata, fid=fid) as vv:
            npd,fid = vv.get_data(np.int_,start=2, n=3)
            self.assertEqual(npd[0],3)
            self.assertEqual(npd[1],4000)
            self.assertEqual(npd[2],40000)


        npdata = np.array(["make_it_big enough"])
        with gxvv.GXvv(npdata, fid=fid) as vv:
            npd, fid = vv.get_data(np.int_, start=0, n=1)
            self.assertEqual(npd[0], gxapi.iDUMMY)

            npdata = np.array([1.,2.,-30.,-87.66662])
            vv.set_data(npdata)
            npd, fid = vv.get_data(start=0, n=4)
            self.assertEqual(npd[0], "1.0")
            self.assertEqual(npd[2], "-30.0")
            self.assertEqual(npd[3], "-87.66662")

        npdata = np.array([1, 2, 3])
        with gxvv.GXvv(npdata, fid=fid) as vv:
            npd = vv.np
            self.assertEqual(npd[1], 2)

            npdata = np.array([1.,2.,-30.,-87.66662])
            vv.set_data(npdata)
            npd, fid = vv.get_data(start=0, n=4)
            self.assertEqual(npd[0], 1)
            self.assertEqual(npd[2], -30)
            self.assertEqual(npd[3], -88)


    def test_string(self):
        self.start()

        l = [1, 2, 3]
        with gxvv.GXvv(l, dtype='U2') as vv:
            self.assertEqual(list(vv.np), ['1', '2', '3'])

        # Since we are using UTF-8 internally characters can take anywhere between 1 and 4 bytes.
        # Specifying a numpy dtype to instantiate VV will ensure the internal space is enough to allocate up to
        # that 4 times the Unicode characters, however any Numpy arrays will limit the characters to the passed dtype.
        l = [1, 2, "abcdefghijklmnopqrstuvxyz"]
        with gxvv.GXvv(l, dtype='U4') as vv:
            self.assertEqual(list(vv.np), ['1', '2', 'abcd'])

        # The following 4-byte UTF-8 characters can be correctly extracted (to limits of what is specified).
        # Characters from http://www.i18nguy.com/unicode/supplementary-test.html
        l = [1, 2, "𠜎𠜱𠝹𠱓𠱸𠲖"]
        with gxvv.GXvv(l, dtype='U4') as vv:
            self.assertEqual(list(vv.np), ['1', '2', '𠜎𠜱𠝹𠱓'])
        with gxvv.GXvv(l, dtype='U2') as vv:
            self.assertEqual(list(vv.np), ['1', '2', '𠜎𠜱'])

    def test_iterator(self):
        self.start()

        with gxvv.GXvv(range(1000)) as vv:
            l2 = [v for v in vv]
            self.assertEqual(len(l2), 1000)
            self.assertEqual(l2[0], (0., 0))
            self.assertEqual(l2[999], (999., 999))

            vvlist = vv.list()
            self.assertEqual(len(vvlist), 1000)
            self.assertEqual(vvlist[0], 0.0)
            self.assertEqual(vvlist[999], 999.)

    def test_uom(self):
        self.start()

        with gxvv.GXvv(range(1000), unit_of_measure='maki') as vv:
            self.assertEqual(vv.unit_of_measure, 'maki')
            vv.unit_of_measure = 'nT'
            self.assertEqual(vv.unit_of_measure, 'nT')

    def test_dim(self):
        self.start()

        data = np.array(range(1000), dtype=np.float64).reshape((500, 2))
        with gxvv.GXvv(data) as vv:
            self.assertEqual(vv.dim, 2)
            self.assertEqual(vv.np.shape, (500, 2))
            self.assertEqual(tuple(vv.np[499,:]), (998., 999.))

        data = np.array(range(300), dtype=np.float64).reshape((100, 3))
        with gxvv.GXvv(data) as vv:
            self.assertEqual(vv.dim, 3)
            self.assertEqual(vv.np.shape, (100, 3))
            self.assertEqual(tuple(vv.np[99,:]), (297., 298., 299.))

        with gxvv.GXvv(dim=3) as vv:
            vv.set_data(np.array(range(300), dtype=np.float64))
            self.assertEqual(vv.dim, 3)
            self.assertEqual(vv.np.shape, (100, 3))
            self.assertEqual(tuple(vv.np[99, :]), (297., 298., 299.))

        with gxvv.GXvv(dim=3) as vv:
            data = np.array(range(300), dtype=np.float64)
            data[1] = data[299] = np.nan
            vv.set_data(data)
            self.assertTrue(np.isnan(data[299]))
            self.assertEqual(vv.dim, 3)
            self.assertEqual(vv.np.shape, (100, 3))
            self.assertEqual(tuple(vv.np[99, :2]), (297., 298.))
            self.assertTrue(np.isnan(vv.np[99, 2]))

    def test_vvset(self):
        self.start()

        npd = np.array(range(12), dtype=np.float64).reshape(-1, 2)
        vv = gxvv.vvset_from_np(npd)
        self.assertEqual(len(vv), npd.shape[1])
        self.assertEqual(len(vv[0]), npd.shape[0])
        vv = gxvv.vvset_from_np(npd, axis=0)
        self.assertEqual(len(vv), npd.shape[0])
        self.assertEqual(len(vv[0]), npd.shape[1])

        npd = np.array(range(48), dtype=np.float64).reshape(6, 2, 4)
        vv = gxvv.vvset_from_np(npd)
        self.assertEqual(len(vv), 4)
        self.assertEqual(len(vv[0]), 12)
        vv = gxvv.vvset_from_np(npd, axis=0)
        self.assertEqual(len(vv), 12)
        self.assertEqual(len(vv[0]), 4)

        npd = gxvv.np_from_vvset(vv)
        self.assertEqual(npd.shape, (4, 12))
        npd = gxvv.np_from_vvset(vv, axis=0)
        self.assertEqual(npd.shape, (12, 4))


    def test_vv_creation(self):
        self.start()

        vv = gxvv.GXvv(range(6), fid=(-0.5, 2), dtype=np.float32, unit_of_measure='maki')
        vv2 = gxvv.GXvv(vv)
        self.assertTrue(vv == vv2)
        self.assertEqual(tuple(vv2.np), tuple(vv.np))
        self.assertEqual(vv.fid, vv2.fid)
        self.assertEqual(vv.dim, vv2.dim)
        self.assertEqual(vv.unit_of_measure, vv2.unit_of_measure)
        self.assertEqual(vv.dtype, vv2.dtype)
        vv.fid = (0., 1.)
        self.assertFalse(vv == vv2)
        vv2 = gxvv.GXvv(vv, unit_of_measure='maki2')
        self.assertFalse(vv == vv2)
        vv2 = gxvv.GXvv(vv, dim=1)
        self.assertTrue(vv == vv2)
        vv2 = gxvv.GXvv(vv, dim=2)
        self.assertFalse(vv == vv2)
        vv2 = gxvv.GXvv(vv, dim=3)
        self.assertFalse(vv == vv2)
        vv3 = gxvv.GXvv(vv2, dim=1)
        self.assertTrue(vv == vv3)

    def test_empty(self):
        self.start()

        empty = np.array([])
        vv = gxvv.GXvv(empty)
        self.assertEqual(len(vv), 0)
        self.assertEqual(vv.np.size, 0)


##############################################################################################
if __name__ == '__main__':

    unittest.main()