import unittest
import os

import geosoft.gxpy.system as gsys
import geosoft.gxpy.surface as gxsurf

from base import GXPYTest


class Test(GXPYTest):

    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py), 'testsurface.zip'),
                                       folder=cls._gx.temp_folder())
        cls.surface_file = os.path.join(cls.folder, 'test.geosoft_surface')

    @classmethod
    def tearDownClass(cls):
        cls.tearDownGXPYTest()
        pass #gxsurf.delete_files(cls.surface_file)

    def test_surfaceProperties(self):
        self.start()

        with gxsurf.SurfaceDataset.open(self.surface_file) as surfdataset:
            self.assertEqual(surfdataset.name, 'test')
            self.assertEqual(surfdataset.surface_count, 5)
            self.assertEqual(str(surfdataset.coordinate_system), 'WGS 84 / MGA zone 50')
            self.assertAlmostEqual(surfdataset.extent,
                                   (504900.1984126984, 6470217.261904762, -1364.1862840323884,
                                    505708.9285714286, 6471183.928571428, 301.8100000000011))

    def test_lists(self):
        self.start()

        with gxsurf.SurfaceDataset.open(self.surface_file) as surfdataset:
            surface_names = surfdataset.surface_names
            self.assertEqual(surface_names[0], 'Isosurface 0.4')
            self.assertEqual(surface_names[1], 'Isosurface 0.8')
            self.assertEqual(surface_names[2], 'Isosurface 0.1')
            self.assertEqual(surface_names[3], 'Isosurface 0.2')
            self.assertEqual(surface_names[4], 'Isosurface 1.6')

            self.assertEqual(surfdataset.surface_guid[4], '{691909E6-78FE-4A23-B866-12CD2C47D5BC}')
            self.assertEqual(surfdataset.surface_dict[surfdataset.surface_guid[4]], 'Isosurface 1.6')

    def test_iter(self):
        self.start()
        with gxsurf.SurfaceDataset.open(self.surface_file) as surfdataset:
            for surf in surfdataset:
                print(surf)

###############################################################################################

if __name__ == '__main__':

    unittest.main()
