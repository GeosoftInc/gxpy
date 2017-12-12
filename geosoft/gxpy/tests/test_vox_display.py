import unittest
import os

import geosoft.gxpy.system as gsys
import geosoft.gxpy.vox as gxvox
import geosoft.gxpy.vox_display as gxvoxd
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.view as gxview
import geosoft.gxpy.group as gxgroup

from base import GXPYTest


class Test(GXPYTest):

    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py), 'testvoxset.zip'),
                                       folder=cls._gx.temp_folder())
        cls.vox_file = os.path.join(cls.folder, 'test.geosoft_voxel')
        cls.vectorvox_file = os.path.join(cls.folder, 'mvi.geosoft_vectorvoxel')

    def test_voxd(self):
        self.start()

        with gxvox.Vox.open(self.vox_file) as vox:
            vox.unit_of_measure = 'maki'
            with gxvoxd.Vox_display.new(vox) as voxd:
                self.assertFalse(voxd.is_thematic)
                self.assertTrue(voxd.opacity, 1.0)
                voxd.opacity = 0.2
                self.assertTrue(voxd.opacity, 0.2)
                self.assertEqual(voxd.color_map.unit_of_measure, 'maki')

                self.assertEqual(voxd.shell_limits, (None, None))
                voxd.shell_limits = (None, 0.00002)
                self.assertEqual(voxd.shell_limits, (None, 0.00002))
                voxd.shell_limits = (0.00002, None)
                self.assertEqual(voxd.shell_limits, (0.00002, None))
                voxd.shell_limits = (0.00002, 0.00003)
                self.assertEqual(voxd.shell_limits, (0.00002, 0.00003))

    def test_figure_map(self):
        self.start()

        with gxvox.Vox.open(self.vox_file) as vox:
            vox.unit_of_measure = 'SI Susc'
            with gxvoxd.Vox_display.new(vox) as voxd:
                voxd.shell_limits = (0.0001, None)
                fig_map = voxd.figure_map(title="My Test Vox").file_name
        self.assertEqual(gxmap.Map.open(fig_map).crc_image(pix_width=800), 1419295652)

    def test_figure_map_vectorvoxel(self):
        self.start()

        with gxvox.Vox.open(self.vectorvox_file) as vox:
            vox.unit_of_measure = 'SI Susc'
            with gxvoxd.Vox_display.new(vox) as voxd:
                voxd.shell_limits = (0.0001, None)
                fig_map = voxd.figure_map(title="My Test VectorVox").file_name
        #fig = gxmap.Map.open(fig_map).image_file()
        self.assertEqual(gxmap.Map.open(fig_map).crc_image(pix_width=800), 3227637535)

    def test_figure_map_vectorvoxel_vector(self):
        self.start()

        with gxvox.Vox.open(self.vectorvox_file) as vox:
            vox.unit_of_measure = 'SI Susc'
            with gxvoxd.Vox_display.new(vox, vector=True) as voxd:
                voxd.shell_limits = (0.01, None)
                voxd.vector_cone_specs = (10, None, None, 100)
                fig_map = voxd.figure_map(title="My Test VectorVox").file_name
        #fig = gxmap.Map.open(fig_map).image_file()
        self.assertEqual(gxmap.Map.open(fig_map).crc_image(pix_width=800), 3304937008)

    def test_open(self):
        self.start()

        with gxvox.Vox.open(self.vox_file) as vox:
            vox.unit_of_measure = 'maki'
            with gxvoxd.Vox_display.new(vox) as voxd:
                with gxview.View_3d.new() as v3d:
                    v3d_file = v3d.file_name
                    group_name = gxgroup.Vox_display_group.new(v3d, voxd).name
        with gxview.View_3d.open(v3d_file) as v3d:
            self.assertEqual(len(v3d.group_list_voxel), 1)
            self.assertTrue(group_name in v3d.group_list_voxel)
            with gxgroup.Vox_display_group.open(v3d, group_name) as gvd:
                self.assertEqual(gvd.name, group_name)
                self.assertEqual(gvd.voxd.name, group_name)
                self.assertEqual(gvd.voxd.vox.name, group_name)
                self.assertEqual(gvd.unit_of_measure, 'maki')

        with gxvox.Vox.open(self.vectorvox_file) as vox:
            vox.unit_of_measure = 'vecmaki'
            with gxvoxd.Vox_display.new(vox) as voxd:
                with gxview.View_3d.new() as v3d:
                    v3d_file = v3d.file_name
                    group_name = gxgroup.Vox_display_group.new(v3d, voxd).name
        with gxview.View_3d.open(v3d_file) as v3d:
            self.assertEqual(len(v3d.group_list_voxel), 1)
            self.assertTrue(group_name in v3d.group_list_voxel)
            with gxgroup.Vox_display_group.open(v3d, group_name) as gvd:
                self.assertEqual(gvd.name, group_name)
                self.assertEqual(gvd.voxd.name, group_name)
                self.assertEqual(gvd.voxd.vox.name, group_name)
                self.assertEqual(gvd.unit_of_measure, 'vecmaki')

        with gxvox.Vox.open(self.vectorvox_file) as vox:
            vox.unit_of_measure = 'vecmaki'
            with gxvoxd.Vox_display.new(vox, vector=True) as voxd:
                with gxview.View_3d.new() as v3d:
                    v3d_file = v3d.file_name
                    group_name = gxgroup.Vox_display_group.new(v3d, voxd).name
        with gxview.View_3d.open(v3d_file) as v3d:
            self.assertEqual(len(v3d.group_list_vectorvoxel), 1)
            self.assertTrue(group_name in v3d.group_list_vectorvoxel)
            with gxgroup.Vox_display_group.open(v3d, group_name) as gvd:
                self.assertEqual(gvd.name, group_name)
                self.assertEqual(gvd.voxd.name, group_name)
                self.assertEqual(gvd.unit_of_measure, 'vecmaki')

if __name__ == '__main__':

    unittest.main()
