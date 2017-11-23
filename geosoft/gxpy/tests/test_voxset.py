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

            print(sum, dummy, valid)
            self.assertEqual(valid + dummy, vox.nx * vox.ny * vox.nz)


###############################################################################################

if __name__ == '__main__':

    unittest.main()
