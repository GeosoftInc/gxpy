import numpy as np
import unittest

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.va as gxva
import geosoft.gxpy.vv as gxvv
import geosoft.gxpy.utility as gxu

from base import GXPYTest


class Test(GXPYTest):

    def test_vv(self):
        self.start()

        npdata = np.empty(gxapi.iMAX)
        with gxvv.GXvv(npdata) as vv:
            self.assertTrue(vv.length, gxapi.iMAX)
        npdata = np.empty(gxapi.iMAX + 1)
        self.assertRaises(gxvv.VVException, gxvv.GXvv, npdata)

    def test_va(self):
        self.start()

        max = gxapi.iMAX // 2
        npdata = np.empty(max * 2).reshape((max, 2))
        with gxva.GXva(npdata) as va:
            self.assertTrue(va.length, gxapi.iMAX)
        del npdata
        npdata = np.empty((max + 1) * 2).reshape((max + 1, 2))
        self.assertRaises(gxva.VAException, gxva.GXva, npdata)


##############################################################################################
if __name__ == '__main__':

    unittest.main()