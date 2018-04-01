import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.system as gsys
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.grid_fft as gxfft
import geosoft.gxpy.grid_utility as gxgrdu
import geosoft.gxpy.geometry as gxgeo
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.gdb as gxgdb

from base import GXPYTest


class Test(GXPYTest):

    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py), 'testgrids.zip'),
                                       folder=cls._gx.temp_folder())
        cls.mag = os.path.join(cls.folder, 'mag.grd')

    def test_create(self):
        self.start()

        with gxfft.GridFFT(self.mag) as gfft:
            pspec = gxfft.PowerSpectrum(gfft).wn_samples_power_d3_d5
            self.assertEqual(len(pspec), 169)
            self.assertAlmostEqual(pspec[1, 0], 1000.0 / ((gfft.transform.nx - 2) * gfft.transform.dx))
            self.assertAlmostEqual(gfft.du, 1.0 / ((gfft.transform.nx - 2) * gfft.transform.dx))
            self.assertAlmostEqual(gfft.dv, 1.0 / (gfft.transform.ny * gfft.transform.dy))

###############################################################################################

if __name__ == '__main__':

    unittest.main()
