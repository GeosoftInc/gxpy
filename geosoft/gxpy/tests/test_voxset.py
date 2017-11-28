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
        cls.tearDownGXPYTest()
        pass #gxvox.delete_files(cls.vox_file)

    def test_voxProperties(self):
        self.start()

        with gxvox.Voxset.open(self.vox_file) as vox:
            self.assertEqual(vox.name, 'test')
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

    def test_new(self):
        self.start()

        with gxvox.Voxset.new("test_new", dimension=(35, 50, 12), temp=True) as vox:
            self.assertEqual((vox.nx, vox.ny, vox.nz), (35, 50, 12))
            npv = vox.np_subset()
            self.assertEqual(np.sum(npv[np.isfinite(npv)]), 0)
            self.assertEqual(list(vox.x_locations[0:2]), [0., 1.])
            self.assertEqual(list(vox.y_locations[0:2]), [0., 1.])
            self.assertEqual(list(vox.z_locations[0:2]), [0., 1.])

        with gxvox.Voxset.new("test_new",
                              dimension=(35, 50, 12),
                              origin=(1, 2, 3),
                              cell_size=(0.1, 0.2, 10),
                              temp=True,
                              init_value=1) as vox:
            self.assertEqual((vox.nx, vox.ny, vox.nz), (35, 50, 12))
            npv = vox.np_subset()
            self.assertEqual(np.sum(npv[np.isfinite(npv)]), vox.nx * vox.ny * vox.nz)
            self.assertEqual(list(vox.x_locations[0:2]), [1., 1.1])
            self.assertEqual(list(vox.y_locations[0:2]), [2., 2.2])
            self.assertEqual(list(vox.z_locations[0:2]), [3., 13.])

        # test cell-separation conversions TODO: Geosoft cell-separation algorithm differs
        dx = (1, 2, 3, 2, 1)
        cells = gxvox.cells_from_separations(dx)
        seps = gxvox.separations_from_cells(cells)
        self.assertEqual(seps, list(dx))
        dx = (4, 3, 2, 1, 1, 2, 55)
        cells = gxvox.cells_from_separations(dx)
        seps = gxvox.separations_from_cells(cells)
        self.assertEqual(seps, list(dx))
        dx = (4, 3, 2, 1)
        cells = gxvox.cells_from_separations(dx)
        seps = gxvox.separations_from_cells(cells)
        self.assertEqual(seps, list(dx))
        dx = (1,)
        cells = gxvox.cells_from_separations(dx)
        seps = gxvox.separations_from_cells(cells)
        self.assertEqual(seps, list(dx))

        cx = (1, 2, 3, 2, 1)
        cy = (10, 10, 10)
        cz = (5, 4, 3, 2)

        with gxvox.Voxset.new("test_new",
                              origin=(1, 2, 3),
                              cell_size=(cx, cy, cz),
                              temp=True,
                              init_value=1) as vox:
            self.assertEqual((vox.nx, vox.ny, vox.nz), (5, 3, 4))
            npv = vox.np_subset()
            self.assertEqual(np.sum(npv[np.isfinite(npv)]), vox.nx * vox.ny * vox.nz)
            self.assertEqual(list(vox.x_locations), [1.0, 2.5, 5.0, 7.5, 9.0])
            self.assertEqual(list(vox.y_locations), [2.0, 12.0, 22.0])
            self.assertEqual(list(vox.z_locations), [3.0, 7.5, 11.0, 13.5])

    def test_new_data(self):
        self.start()

        with gxvox.Voxset.open(self.vox_file) as vox:
            npv = vox.np_subset()
            with gxvox.Voxset.new("test_data", data=npv, temp=True,
                                  origin=(vox.x0, vox.y0, vox.z0),
                                  cell_size=(vox.x_cells, vox.y_cells, vox.z_cells),
                                  coordinate_system=vox.coordinate_system) as vox_copy:
                npv = vox_copy.np_subset()
                self.assertEqual(npv.shape, (vox.nz, vox.ny, vox.nx))
                sum = npv[np.isfinite(npv)].sum()
                self.assertAlmostEqual(sum, 45.9709323711)


###############################################################################################

if __name__ == '__main__':

    unittest.main()
