import unittest
import os

import geosoft.gxpy.system as gsys
import geosoft.gxpy.surface as gxsurf
import geosoft.gxpy.vox as gxvox
import geosoft.gxpy.group as gxgrp
import geosoft.gxpy.spatialdata as gxspd

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
        pass #gxsurf.delete_files(cls.surface_file)

    def test_surfaceProperties(self):
        self.start()

        try:
            fn = gxsurf.SurfaceDataset.vox_surface(gxvox.Vox.open(self.vox_file),
                                                   (0.005, 0.01, 0.02), overwrite=True).file_name
            with gxsurf.SurfaceDataset.open(fn) as surfdataset:
                self.assertEqual(surfdataset.name, 'test')
                self.assertEqual(surfdataset.file_name, 'test.geosoft_surface')
                self.assertEqual(surfdataset.surface_count, 3)
                self.assertEqual(str(surfdataset.coordinate_system), 'NAD83 / UTM zone 20N')
                surface_names = surfdataset.surface_names
                self.assertEqual(surface_names[0], 'Isosurface 0.005')
                self.assertEqual(surface_names[1], 'Isosurface 0.01')
                self.assertEqual(surface_names[2], 'Isosurface 0.02')
                self.assertEqual(surfdataset.surface_guid[2], '{ABCDEF02-2345-6789-6945-2301E0BC0A89}')
                self.assertEqual(surfdataset.surface_dict[surfdataset.surface_guid[2]], 'Isosurface 0.02')

                for surf in surfdataset:
                    self.assertTrue(surf.verticies_count > 0)
                surf = surfdataset[2]
                self.assertEqual(surf.name, 'Isosurface 0.02')
                self.assertEqual(surf.verticies_count, 21)
                self.assertEqual(surf.triangles_count, 26)
                self.assertEqual(surf.compontent_count, 1)
                self.assertEqual(surf.render_color.rgb, (255, 255, 0))
                self.assertEqual(surf.render_transparency, 1.)
                self.assertEqual(surf.render_style, gxsurf.RENDER_STYLE_SMOOTH)

        finally:
            gxsurf.delete_files('test')

    def test_new(self):
        self.start()

        try:
            fn = gxsurf.SurfaceDataset.vox_surface(gxvox.Vox.open(self.vox_file),
                                                   (0.01, 0.02), overwrite=True).file_name

            with gxsurf.SurfaceDataset.open(fn) as surfdataset:
                with gxsurf.SurfaceDataset.new('new', overwrite=True) as newsurf:
                    for surf in surfdataset:
                        newsurf.add_surface(surf)

            with gxsurf.SurfaceDataset.open('new') as surfdataset:
                self.assertEqual(surfdataset.name, 'new')
                self.assertEqual(surfdataset.file_name, 'new.geosoft_surface')
                self.assertEqual(surfdataset.surface_count, 2)
                self.assertEqual(str(surfdataset.coordinate_system), 'NAD83 / UTM zone 20N')
                surface_names = surfdataset.surface_names
                self.assertEqual(surface_names[0], 'Isosurface 0.01')
                self.assertEqual(surface_names[1], 'Isosurface 0.02')
                self.assertEqual(surfdataset.surface_guid[1], '{ABCDEF01-2345-6789-6845-2301DFBC0A89}')
                self.assertEqual(surfdataset.surface_dict[surfdataset.surface_guid[1]], 'Isosurface 0.02')

                for surf in surfdataset:
                    self.assertTrue(surf.verticies_count > 0)
                surf = surfdataset[1]
                self.assertEqual(surf.name, 'Isosurface 0.02')
                self.assertEqual(surf.verticies_count, 21)
                self.assertEqual(surf.triangles_count, 26)
                self.assertEqual(surf.compontent_count, 1)
                self.assertEqual(surf.render_color.rgb, (0, 255, 0))
                self.assertEqual(surf.render_transparency, 1.)
                self.assertEqual(surf.render_style, gxsurf.RENDER_STYLE_SMOOTH)

        finally:
            gxsurf.delete_files('test')
            gxsurf.delete_files('new')

    def test_temp(self):
        self.start()

        fn = gxsurf.SurfaceDataset.vox_surface(gxvox.Vox.open(self.vox_file),
                                               0.01, color=gxgrp.C_GREY, transparency=0.5,
                                               temp=True).file_name

        with gxsurf.SurfaceDataset.open(fn) as surfdataset:
            with gxsurf.SurfaceDataset.new('new', temp=True) as newsurf:
                self.assertEqual(newsurf.name, 'new')
                temp_fn = newsurf.file_name
                for surf in surfdataset:
                    newsurf.add_surface(surf)

        with gxsurf.SurfaceDataset.open(temp_fn) as surfdataset:
            self.assertEqual(surfdataset.surface_count, 1)
            self.assertEqual(str(surfdataset.coordinate_system), 'NAD83 / UTM zone 20N')
            surface_names = surfdataset.surface_names
            self.assertEqual(surface_names[0], 'Isosurface 0.01')
            self.assertEqual(surfdataset.surface_guid[0], '{ABCDEF00-2345-6789-6745-2301DEBC0A89}')
            self.assertEqual(surfdataset.surface_dict[surfdataset.surface_guid[0]], 'Isosurface 0.01')

            for surf in surfdataset:
                self.assertTrue(surf.verticies_count > 0)
            surf = surfdataset[0]
            self.assertEqual(surf.name, 'Isosurface 0.01')
            self.assertEqual(surf.verticies_count, 482)
            self.assertEqual(surf.triangles_count, 855)
            self.assertEqual(surf.compontent_count, 1)
            self.assertEqual(surf.render_color.rgb, (128, 128, 128))
            self.assertEqual(surf.render_transparency, 0.5)
            self.assertEqual(surf.render_style, gxsurf.RENDER_STYLE_SMOOTH)

    def test_exceptions(self):
        self.start()

        fn = 'except.geosoft_surface'
        try:
            with open(fn, '+w') as f:
                f.write('maki')
            self.assertRaises(gxspd.SpatialException, gxsurf.SurfaceDataset.new, 'except')

        finally:
            gxsurf.delete_files(fn)

        with gxsurf.SurfaceDataset.new('test', temp=True, coordinate_system='WGS 84') as sd:
            s = gxsurf.Surface('maki')
            s.coordinate_system = 'NAD83'
            self.assertEqual(str(s.coordinate_system), 'NAD83')
            self.assertRaises(gxsurf.SurfaceException, sd.add_surface, s)

###############################################################################################

if __name__ == '__main__':

    unittest.main()
