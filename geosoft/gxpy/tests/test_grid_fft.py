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
            self.assertTrue(gfft.filtered_transform is None)
            gfft.result_grid()
            pspec = gxfft.PowerSpectrum(gfft.transform)
            self.assertEqual(len(pspec.wavenumber), 169)
            self.assertAlmostEqual(pspec.wavenumber[1], 1000.0 / ((gfft.transform.nx - 2) * gfft.transform.dx))
            self.assertAlmostEqual(gfft.du, 1.0 / ((gfft.transform.nx - 2) * gfft.transform.dx))
            self.assertAlmostEqual(gfft.dv, 1.0 / (gfft.transform.ny * gfft.transform.dy))

    def test_filter_con(self):
        self.start()

        gxgrd.Grid.open(self.mag, mode=gxgrd.FILE_READWRITE).coordinate_system='NAD27 / UTM zone 15N'
        with gxfft.GridFFT(self.mag, progress=print) as gfft:
            gfft.filter_con(filters=['CNUP 500'])
            up = gfft.result_grid(file_name='result', overwrite=True)
            self.assertEqual(str(up.coordinate_system), 'NAD27 / UTM zone 15N')
            self.assertAlmostEqual(up.statistics()['variance'], 15371.983796054874, 4)
            gfft.filter_con(filters=['DRVZ 1'], cumulatative=True)
            vd = gfft.result_grid(file_name='up500vd', overwrite=True)
            self.assertAlmostEqual(vd.statistics()['variance'], 0.022758276826459138, 7)
            pspec = gxfft.PowerSpectrum(gfft.transform)
            self.assertAlmostEqual(pspec.wavenumber[0], 0.)
            self.assertAlmostEqual(pspec.log_power[1], 8.086868672175)
            self.assertAlmostEqual(pspec.samples[1], 6.34315, 4)
            self.assertAlmostEqual(pspec.depth_3[5], 0.790437, 5)
            self.assertAlmostEqual(pspec.depth_5[5], 0.605159, 5)

        up.close(discard=True)
        vd.close(discard=True)

    def test_filter_con_double(self):
        self.start()

        grd = gxgrd.Grid.open(self.mag, mode=gxgrd.FILE_READWRITE, dtype=np.float64)
        with gxfft.GridFFT(grd, progress=print) as gfft:
            gfft.filter_con(filters=['CNUP 500'],
                            header=['', '', -66.58, '8.26', 59041])
            up = gfft.result_grid(file_name='result', overwrite=True)
            self.assertEqual(up.dtype, np.float64)
            self.assertAlmostEqual(up.statistics()['variance'], 15371.983796054874, 4)
            gfft.filter_con(filters=['DRVZ 1'], cumulatative=True)
            vd = gfft.result_grid(file_name='up500vd', overwrite=True)
            self.assertAlmostEqual(vd.statistics()['variance'], 0.022758276826459138, 7)
            pspec = gxfft.PowerSpectrum(gfft.transform)
            self.assertAlmostEqual(pspec.wavenumber[0], 0.)
            self.assertAlmostEqual(pspec.log_power[1], 8.086868672175, 4)
            self.assertAlmostEqual(pspec.samples[1], 6.34315, 4)
            self.assertAlmostEqual(pspec.depth_3[5], 0.790437, 5)
            self.assertAlmostEqual(pspec.depth_5[5], 0.605159, 5)

        up.close(discard=True)
        vd.close(discard=True)

###############################################################################################

if __name__ == '__main__':

    unittest.main()
