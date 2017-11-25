import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.voxset as gxvox

from base import GXPYTest


class Test(GXPYTest):

    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py), 'testvoxset.zip'),
                                       folder=cls._gx.temp_folder())
        cls.vox_file = os.path.join(cls.folder, 'test.geosoft_voxel')

    @classmethod
    def tearDownClass(cls):
        gxvox.delete_files(cls.vox_file)

    def test_voxProperties(self):
        self.start()

        with gxvox.Voxset.open(self.vox_file) as vox:
            self.assertEqual(vox.name, 'test')
            self.assertEqual(vox.file_name, '__tmp__\\_gx_uuid_test_voxset.py_1\\test.geosoft_voxel')
            self.assertEqual(len(vox.x_locations), vox.nx)
            self.assertEqual(len(vox.y_locations), vox.ny)
            self.assertEqual(len(vox.z_locations), vox.nz)
            self.assertEqual(vox.xyz(0, 0, 0), (vox.x0, vox.y0, vox.z0))
            self.assertEqual(vox.extent, (438550.0, 6126150.0, -1022.3323879241943, 441500.0, 6129500.0, 575.0))
            self.assertEqual(vox.extent_2d, (438550.0, 6126150.0, 441500.0, 6129500.0))
            self.assertEqual((vox.nx, vox.ny, vox.nz), (59, 67, 26))
            self.assertEqual(str(vox.coordinate_system), 'NAD83 / UTM zone 20N')

    def test_iter(self):
        self.start()

        with gxvox.Voxset.open(self.vox_file) as vox:
            valid = 0
            dummy = 0
            sum = 0.
            for xyzv in vox:
                if xyzv[3] is not None:
                    valid += 1
                    sum += xyzv[3]
                else:
                    dummy += 1

            self.assertAlmostEqual(sum, 45.9709323711)
            self.assertEqual(valid + dummy, vox.nx * vox.ny * vox.nz)

            self.assertEqual(vox[50, 65, 18], (441075.0, 6129425.0, 370.34108924865723, 0.00019816514181249432))
            self.assertEqual(vox[0, 0, 0], (vox.x0, vox.y0, vox.z0, None))

    def test_value(self):
        self.start()

        with gxvox.Voxset.open(self.vox_file) as vox:
            self.assertEqual(vox.value_at_location(vox.xyz(50, 65, 18)), 0.00019816514181249432)
            self.assertEqual(vox.value_at_location((441075.0, 6129425.0, 370.34108924865723)),
                             0.00019816514181249432)
            self.assertEqual(vox.value_at_location((441076, 6129426, 370), interpolate=gxvox.INTERP_NEAREST),
                             0.00019816514181249432)
            self.assertEqual(vox.value_at_location((441076, 6129426, 370)), 0.0002534898842353971)
            self.assertEqual(vox.value_at_location((441100, 6129400, 225.895), interpolate=gxvox.INTERP_SMOOTH),
                             0.003535265803154243)
            self.assertEqual(vox.value_at_location((0, 0, 0)), None)
            self.assertEqual(vox.value_at_location((-1.0e25, 0, 1e25)), None)

    def test_np(self):
        self.start()

        with gxvox.Voxset.open(self.vox_file) as vox:
            npv = vox.np_subset()
            self.assertEqual(npv.shape, (vox.nz, vox.ny, vox.nx))
            sum = npv[np.isfinite(npv)].sum()
            self.assertAlmostEqual(sum, 45.9709323711)

        size = (5, 8, 14)
        with gxvox.Voxset.open(self.vox_file) as vox:
            npv = vox.np_subset(start=(30, 50, 9), dimension=size)
            self.assertEqual(npv.shape, (size[2], size[1], size[0]))
            sum = npv[np.isfinite(npv)].sum()
            self.assertAlmostEqual(sum, 0.56577674920814858)

    def test_metadata(self):
        self.start()

        with gxvox.Voxset.open(self.vox_file) as vox:
            m = vox.metadata
            gm = m['geosoft']
            self.assertTrue('dataset' in gm)
            self.assertTrue('georeference' in gm['dataset'])

            newstuff = {'maki': {'a': 1, 'b': (4, 5, 6), 'units': 'nT'}}
            vox.metadata = newstuff
            vox.unit_of_measure = 'billy_bob'

        with gxvox.Voxset.open(self.vox_file) as vox:
            m = vox.metadata
            maki = m['maki']
            self.assertEqual(maki['b'], ['4', '5', '6'])
            self.assertEqual(maki['units'], 'nT')
            self.assertEqual(vox.unit_of_measure, 'billy_bob')

###############################################################################################

if __name__ == '__main__':

    unittest.main()
