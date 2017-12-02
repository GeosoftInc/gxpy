import unittest
import os

import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.vox as gxvox
import geosoft.gxpy.vox_display as gxvoxd
import geosoft.gxpy.viewer as gxviewer

from base import GXPYTest


class Test(GXPYTest):

    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py), 'testvoxset.zip'),
                                       folder=cls._gx.temp_folder())
        cls.vox_file = os.path.join(cls.folder, 'test.geosoft_voxel')

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

    def test_figure_view(self):
        self.start()

        with gxvox.Vox.open(self.vox_file) as vox:
             with gxvoxd.Vox_display.new(vox) as voxd:
                 v3d_file = voxd.figure_view_file()
                 gxviewer.view_document(v3d_file)
                 #self.crc_map(v3d_file)

if __name__ == '__main__':

    unittest.main()
