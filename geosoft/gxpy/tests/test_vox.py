#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.vox as gxvox
import geosoft.gxpy.gdb as gxgdb

from base import GXPYTest


class Test(GXPYTest):

    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py), 'testvoxset.zip'),
                                       folder=cls._gx.temp_folder())
        cls.vox_file = os.path.join(cls.folder, 'test.geosoft_voxel')
        cls.vectorvox_file = os.path.join(cls.folder, 'mvi.geosoft_vectorvoxel')

    @classmethod
    def tearDownClass(cls):
        cls.tearDownGXPYTest()
        pass #gxvox.delete_files(cls.vox_file)

    def test_voxProperties(self):
        self.start()

        with gxvox.Vox.open(self.vox_file) as vox:
            self.assertEqual(vox.name, 'test')
            self.assertEqual(len(vox.locations_x), vox.nx)
            self.assertEqual(len(vox.locations_y), vox.ny)
            self.assertEqual(len(vox.locations_z), vox.nz)
            self.assertEqual(vox.xyz(0, 0, 0), (vox.origin_x, vox.origin_y, vox.origin_z))
            self.assertEqual(vox.extent_xyz, (438550.0, 6126150.0, -1022.3323879241943, 441500.0, 6129500.0, 575.0))
            self.assertEqual(vox.extent_xy, (438550.0, 6126150.0, 441500.0, 6129500.0))
            self.assertEqual((vox.nx, vox.ny, vox.nz), (59, 67, 26))
            self.assertEqual(str(vox.coordinate_system), 'NAD83 / UTM zone 20N')

            vox.is_depth = True
            self.assertFalse(vox.is_elevation)
            vox.is_elevation = True
            self.assertFalse(vox.is_depth)
            vox.is_depth = True
            self.assertEqual(vox.xyz(0, 0, 0), (vox.origin_x, vox.origin_y, vox.origin_z))
            self.assertEqual(vox.extent_xyz, (438550.0, 6126150.0, -575.0, 441500.0, 6129500.0, 1022.3323879241943))
            self.assertEqual(vox.extent_xy, (438550.0, 6126150.0, 441500.0, 6129500.0))
            self.assertEqual((vox.nx, vox.ny, vox.nz), (59, 67, 26))


    def test_iter(self):
        self.start()

        with gxvox.Vox.open(self.vox_file) as vox:
            valid = 0
            dummy = 0
            sum = 0.
            for x, y, z, v in vox:
                if v is not None:
                    valid += 1
                    sum += v
                else:
                    dummy += 1

            self.assertAlmostEqual(sum, 45.9709323711)
            self.assertEqual(valid + dummy, vox.nx * vox.ny * vox.nz)

            self.assertEqual(vox[50, 65, 18], (441075.0, 6129425.0, 370.34108924865723, 0.00019816514181249432))
            self.assertEqual(vox[0, 0, 0], (vox.origin_x, vox.origin_y, vox.origin_z, None))

        with gxvox.Vox.open(self.vox_file, dtype=np.int_) as vox:
            valid = 0
            dummy = 0
            sum = 0.
            for x, y, z, v in vox:
                if v is not None:
                    valid += 1
                    sum += v
                else:
                    dummy += 1

            self.assertAlmostEqual(sum, 0)
            self.assertEqual(valid + dummy, vox.nx * vox.ny * vox.nz)

            self.assertEqual(vox[50, 65, 18], (441075.0, 6129425.0, 370.34108924865723, 0.0))
            self.assertEqual(vox[0, 0, 0], (vox.origin_x, vox.origin_y, vox.origin_z, None))

            data = vox.np()
            self.assertEqual(data.dtype, np.int_)

            data = vox.np(dtype=np.float64)
            self.assertEqual(data.dtype, np.float64)

        data = gxvox.Vox.open(self.vox_file, dtype=np.int_).np(dtype=np.float64)
        self.assertEqual(data.dtype, np.float64)
        data = gxvox.Vox.open(self.vox_file, dtype=np.float64).np(dtype=np.int_)
        self.assertEqual(data.dtype, np.int_)

    def test_value(self):
        self.start()

        with gxvox.Vox.open(self.vox_file) as vox:
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

        with gxvox.Vox.open(self.vox_file) as vox:
            npv = vox.np()
            self.assertEqual(npv.shape, (vox.nz, vox.ny, vox.nx))
            sum = npv[np.isfinite(npv)].sum()
            self.assertAlmostEqual(sum, 45.9709323711)

        size = (5, 8, 14)
        with gxvox.Vox.open(self.vox_file) as vox:
            npv = vox.np(subset=((30, 50, 9), size))
            self.assertEqual(npv.shape, (size[2], size[1], size[0]))
            sum = npv[np.isfinite(npv)].sum()
            self.assertAlmostEqual(sum, 0.56577674920814858)

        with gxvox.Vox.open(self.vox_file) as vox:
            npv = vox.np(subset=(None, (2, 3, 4)))
            self.assertEqual(npv.shape, (4, 3, 2))
            sum = npv[np.isfinite(npv)].sum()
            self.assertAlmostEqual(sum, 0.0)

        with gxvox.Vox.open(self.vox_file) as vox:
            npv = vox.np(subset=((None, None, -3), (None, None, 1)))
            self.assertEqual(npv.shape, (1, vox.ny, vox.nx))
            sum = npv[np.isfinite(npv)].sum()
            self.assertAlmostEqual(sum, 1.00971206805)

        with gxvox.Vox.open(self.vox_file) as vox:
            npv = vox.np(subset=((None, None, -1), (None, None, 1)))
            self.assertEqual(npv.shape, (1, vox.ny, vox.nx))
            sum = npv[np.isfinite(npv)].sum()
            self.assertAlmostEqual(sum, 0.01212498417)

    def test_metadata(self):
        self.start()

        with gxvox.Vox.open(self.vox_file, mode=gxvox.MODE_READWRITE) as vox:
            m = vox.metadata
            gm = m['geosoft']
            self.assertTrue('dataset' in gm)
            self.assertTrue('georeference' in gm['dataset'])

            newstuff = {'maki': {'a': 1, 'b': (4, 5, 6), 'units': 'nT'}}
            vox.metadata = newstuff
            vox.unit_of_measure = 'billy_bob'

        with gxvox.Vox.open(self.vox_file) as vox:
            m = vox.metadata
            maki = m['maki']
            self.assertEqual(maki['b'], ['4', '5', '6'])
            self.assertEqual(maki['units'], 'nT')
            self.assertEqual(vox.unit_of_measure, 'billy_bob')

    def test_new(self):
        self.start()

        npd = np.zeros((12, 50, 35), dtype=np.float64)
        npd[:] = np.nan
        with gxvox.Vox.new("test_new", npd, temp=True) as vox:
            self.assertEqual((vox.nx, vox.ny, vox.nz), (35, 50, 12))
            npv = vox.np()
            self.assertEqual(np.sum(npv[np.isfinite(npv)]), 0)
            self.assertEqual(list(vox.locations_x[0:2]), [0., 1.])
            self.assertEqual(list(vox.locations_y[0:2]), [0., 1.])
            self.assertEqual(list(vox.locations_z[0:2]), [0., 1.])

        npd[:] = 1
        with gxvox.Vox.new("test_new", npd,
                            origin=(1, 2, 3),
                            cell_size=(0.1, 0.2, 10),
                            temp=True) as vox:
            self.assertEqual((vox.nx, vox.ny, vox.nz), (35, 50, 12))
            npv = vox.np()
            self.assertEqual(np.sum(npv[np.isfinite(npv)]), vox.nx * vox.ny * vox.nz)
            self.assertEqual(list(vox.locations_x[0:2]), [1., 1.1])
            self.assertEqual(list(vox.locations_y[0:2]), [2., 2.2])
            self.assertEqual(list(vox.locations_z[0:2]), [3., 13.])

        cx = (1, 2, 3, 2, 1)
        cy = (10, 10, 10)
        cz = (5, 4, 3, 2)

        npd = np.ones((len(cz), len(cy), len(cx)))
        with gxvox.Vox.new("test_new", npd,
                           origin=(1, 2, 3),
                           cell_size=(cx, cy, cz),
                           temp=True) as vox:
            self.assertEqual((vox.nx, vox.ny, vox.nz), (5, 3, 4))
            npv = vox.np()
            self.assertEqual(np.sum(npv[np.isfinite(npv)]), vox.nx * vox.ny * vox.nz)
            self.assertEqual(list(vox.locations_x), [1.0, 2.5, 5.0, 7.5, 9.0])
            self.assertEqual(list(vox.locations_y), [2.0, 12.0, 22.0])
            self.assertEqual(list(vox.locations_z), [3.0, 7.5, 11.0, 13.5])


        with gxvox.Vox.new("test_new", npd,
                           origin=(0.5, 5.0, 2.5),
                           cell_size=(cx, cy, cz),
                           temp=True,
                           depth=True) as vox:
            self.assertEqual((vox.nx, vox.ny, vox.nz), (5, 3, 4))
            npv = vox.np()
            self.assertEqual(np.sum(npv[np.isfinite(npv)]), vox.nx * vox.ny * vox.nz)
            self.assertEqual(list(vox.locations_x), [0.5, 2.0, 4.5, 7.0, 8.5])
            self.assertEqual(list(vox.locations_y), [5.0, 15.0, 25.0])
            self.assertEqual(list(vox.locations_z), [2.5, 7.0, 10.5, 13.0])

        self.assertRaises(gxvox.VoxException, gxvox.Vox.new, "test",
                          np.zeros((2,3,15)), cell_size=(cx, cy, cz))

    def test_new_data(self):
        self.start()

        with gxvox.Vox.open(self.vox_file) as vox:
            npv = vox.np()
            test_edge = list(vox.np(subset=((vox.nx - 1, 6, vox.nz - 8), (1, 10, 1))).flatten())
            with gxvox.Vox.new("test_data", npv, temp=True,
                               origin=(vox.origin_x, vox.origin_y, vox.origin_z),
                               cell_size=(vox.cells_x, vox.cells_y, vox.cells_z),
                               coordinate_system=vox.coordinate_system) as vox_copy:
                npv = vox_copy.np()
                self.assertEqual(npv.shape, (vox.nz, vox.ny, vox.nx))
                sum = npv[np.isfinite(npv)].sum()
                self.assertAlmostEqual(sum, 45.9709323711)
                test_copy = list(vox_copy.np(subset=((vox_copy.nx - 1, 6, vox_copy.nz - 8), (1, 10, 1))).flatten())
                self.assertEqual(test_edge, test_copy)

                ez = vox_copy[57, 62, 8][3]
                vox_copy.is_depth = True
                self.assertEqual(vox_copy[57, 62, vox_copy.nz - 9][3], ez)

                test_copy = list(vox_copy.np(subset=((vox_copy.nx - 1, 6, 7), (1, 10, 1))).flatten())
                self.assertEqual(test_edge, test_copy)

    def test_vectorvoxel(self):
        self.start()

        with gxvox.Vox.open(self.vectorvox_file) as vox:
            npv = vox.np(dtype=np.float64)
            self.assertEqual(npv.shape, (38, 56, 55, 3))
            self.assertEqual(tuple(npv[25, 25, 25]), (-0.16268515586853027, -0.02528655156493187, 1.6525727510452271))
            self.assertAlmostEqual(tuple(vox[25, 25, 25][3])[0], -0.16268516)
            self.assertAlmostEqual(tuple(vox[25, 25, 25][3])[1], -0.025286552)
            self.assertAlmostEqual(tuple(vox[25, 25, 25][3])[2], 1.6525728)

            npv[25, 25, 25] = (1., 2., np.nan)
            with gxvox.Vox.new('vox_', npv, temp=True, overwrite=True) as newvox:
                self.assertAlmostEqual(tuple(newvox[25, 25, 25][3])[0], 1.)
                self.assertAlmostEqual(tuple(newvox[25, 25, 25][3])[1], 2.)
                self.assertAlmostEqual(tuple(newvox[25, 25, 25][3])[2], None)

            with gxvox.Vox.copy_vox('vox_', vox, npv, temp=True, overwrite=True) as newvox:
                self.assertAlmostEqual(tuple(newvox[25, 25, 25][3])[0], 1.)
                self.assertAlmostEqual(tuple(newvox[25, 25, 25][3])[1], 2.)
                self.assertAlmostEqual(tuple(newvox[25, 25, 25][3])[2], None)

    def test_uom(self):
        self.start()

        uom = gxvox.Vox.open(self.vectorvox_file).unit_of_measure
        with gxvox.Vox.open(self.vectorvox_file) as g:
            g.unit_of_measure = 'maki'
            self.assertEqual(g.unit_of_measure, 'maki')
        self.assertEqual(gxvox.Vox.open(self.vectorvox_file).unit_of_measure, uom)

        with gxvox.Vox.open(self.vectorvox_file, mode=gxvox.MODE_READWRITE) as g:
            g.unit_of_measure = 'maki'
            self.assertEqual(g.unit_of_measure, 'maki')
        self.assertEqual(gxvox.Vox.open(self.vectorvox_file).unit_of_measure, 'maki')

    @unittest.skip('WIP')
    def test_rbf(self):
        self.start()

        def feed_data(n):
            if n >= len(nxyzv):
                return None
            return nxyzv[n]

        def gdb_from_callback(callback):
            _gdb = gxgdb.Geosoft_gdb.new()
            channels = ('x', 'y', 'z', 'v')
            il = 0
            xyzv_kist = callback(il)
            while xyzv_kist is not None:
                _gdb.write_line('L{}'.format(il), xyzv_kist, channels=channels)
                il += 1
                xyzv_kist = callback(il)
            _gdb.xyz_channels = channels[:3]
            return _gdb

        xyzv = [(45., 10., 0., 100), (60., 25., 0., 77.), (50., 8., 5., 80.), (55., 18., 12., 90.)]
        with gxvox.Vox.rbf(xyzv, cs=1.) as vox:
            self.assertEqual((vox.nx, vox.ny), (9, 9))
            self.assertAlmostEqual(vox.statistics()['sd'], 8.708599, 5)

        # a callback, used for very large data, or to feed data efficiently from some other source.
        nxyzv = np.array([[(45., 10., 0., 100), (60., 25., 10., 77.), (50., 8., 10., 81.), (55., 11., 25., 66.)],
                          [(20., 15., 5., 108), (25., 5., 12., 77.), (33., 9., 10., np.nan), (28., 2., 20., 22.)],
                          [(35., 18., 8., 110), (40., 31., 18., 77.), (13., 4., 10., 83.), (44., 4., 18., 7.)]])

        with gxvox.Vox.rbf(feed_data, cs=0.25) as vox:
            self.assertEqual((vox.nx, vox.ny), (189, 117))
            self.assertAlmostEqual(vox.statistics()['sd'], 22.320659139902336, 5)

        with gdb_from_callback(feed_data) as gdb:
            with gxvox.Vox.rbf((gdb, 'v'), cs=0.25) as vox:
                self.assertEqual((vox.nx, vox.ny), (189, 117))
                self.assertAlmostEqual(vox.statistics()['sd'], 22.320659139902336, 5)

###############################################################################################

if __name__ == '__main__':

    unittest.main()
