import unittest
import os
import numpy as np
import math

import geosoft.gxpy.system as gsys
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.grid_fft as gxfft

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

        with gxfft.GridFFT(self.mag) as fft:
            fft.result_grid()
            pspec = fft.radially_averaged_spectrum()
            self.assertEqual(len(pspec), 169)
            self.assertAlmostEqual(pspec[1, gxfft.I_WAVENUMBER], 1000.0 /
                                   ((fft.source_transform.nx - 2) * fft.source_transform.dx))
            self.assertAlmostEqual(fft.du, 1.0 / ((fft.source_transform.nx - 2) * fft.source_transform.dx))
            self.assertAlmostEqual(fft.dv, 1.0 / (fft.source_transform.ny * fft.source_transform.dy))

    def test_create_MC(self):
        self.start()

        with gxfft.GridFFT(self.mag, fill_method=gxfft.FILL_MINIMUM_CURVATURE) as fft:
            fft.result_grid()
            pspec = fft.radially_averaged_spectrum()
            self.assertEqual(len(pspec), 169)
            self.assertAlmostEqual(pspec[1, gxfft.I_WAVENUMBER], 1000.0 /
                                   ((fft.source_transform.nx - 2) * fft.source_transform.dx))
            self.assertAlmostEqual(fft.du, 1.0 / ((fft.source_transform.nx - 2) * fft.source_transform.dx))
            self.assertAlmostEqual(fft.dv, 1.0 / (fft.source_transform.ny * fft.source_transform.dy))

    def test_filter(self):
        self.start()

        gxgrd.Grid.open(self.mag, mode=gxgrd.FILE_READWRITE).coordinate_system='NAD27 / UTM zone 15N'
        with gxfft.GridFFT(self.mag) as fft:
            fft.filter(filters=['CNUP 500'])
            up = fft.result_grid(file_name='result', overwrite=True)
            self.assertEqual(str(up.coordinate_system), 'NAD27 / UTM zone 15N')
            self.assertAlmostEqual(up.statistics()['variance'], 15442.23622462059, 0)
            fft.filter(filters=['DRVZ 1'], trn=gxfft.TRN_FILTERED)
            vd = fft.result_grid(file_name='up500vd', overwrite=True)
            self.assertAlmostEqual(vd.statistics()['variance'], 0.02167, 3)
            pspec = fft.radially_averaged_spectrum()
            self.assertAlmostEqual(pspec[0, gxfft.I_WAVENUMBER], 0.)
            self.assertAlmostEqual(pspec[1, gxfft.I_WAVENUMBER], fft.dv * 1000., 6)

        up.close(discard=True)
        vd.close(discard=True)

    def test_filter_double(self):
        self.start()

        grd = gxgrd.Grid.open(self.mag, mode=gxgrd.FILE_READWRITE, dtype=np.float64)
        with gxfft.GridFFT(grd) as fft:
            fft.filter(filters=['CNUP 500'],
                       mag_inclination=-66.58,
                       mag_declination='8.26',
                       mag_strength=59041)
            up = fft.result_grid(file_name='result', overwrite=True)
            self.assertEqual(up.dtype, np.float64)
            self.assertAlmostEqual(up.statistics()['variance'], 15441.51060320867, 0)
            fft.filter(filters=['DRVZ 1'], trn=gxfft.TRN_FILTERED)
            vd = fft.result_grid(file_name='up500vd', overwrite=True)
            self.assertAlmostEqual(vd.statistics()['variance'], 0.0217, 3)
            pspec = fft.radially_averaged_spectrum(gxfft.TRN_FILTERED)
            self.assertAlmostEqual(pspec[0, gxfft.I_WAVENUMBER], 0.)
            self.assertAlmostEqual(pspec[1, gxfft.I_LOG_POWER], 15.332930000000001, 0)

        up.close(discard=True)
        vd.close(discard=True)

    def test_spectrum_grids(self):
        self.start()

        with gxfft.GridFFT(self.mag) as fft:
            source_spec = fft.spectrum_grid()
            self.assertAlmostEqual(source_spec.statistics()['variance'], 16.017015790664406, 0)
            fft.filter([('CNUP', 1000)])
            filter_spec = fft.spectrum_grid(gxfft.TRN_FILTERED)
            self.assertAlmostEqual(filter_spec.statistics()['variance'], 136.6656119975559, 0)

    def test_custom_filter(self):
        self.start()

        distance = 500
        with gxfft.GridFFT(self.mag, buffer=10, expand=15) as fft:
            for vrow in range(fft.nv):
                u, v, r, i = fft.read_uv_row(vrow)
                w = np.sqrt(u**2 + v**2)
                continuation_filter = np.exp(-2. * math.pi * distance * w)
                r *= continuation_filter
                i *= continuation_filter
                fft.write_uv_row(r, i, vrow, trn=gxfft.TRN_FILTERED)

            self.assertAlmostEqual(fft.result_grid().statistics()['sd'], 99.68591520777781, 0)

###############################################################################################

if __name__ == '__main__':

    unittest.main()
