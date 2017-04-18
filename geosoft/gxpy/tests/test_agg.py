import unittest
import os

import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.agg as gxagg
import geosoft

from geosoft.gxpy.tests import GXPYTest


class Test(GXPYTest):

    @classmethod
    def setUpClass(cls):
        GXPYTest.setUpGXPYTest(res_stack=4)
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                       folder=cls._gx.temp_folder())
        cls.g1f = os.path.join(cls.folder, 'test_grid_1.grd')
        cls.g2f = os.path.join(cls.folder, 'test_grid_2.grd')
        cls.g3f = os.path.join(cls.folder, 'test_agg_utm.grd')

    def test_version(self):
        self.start()
        self.assertEqual(gxagg.__version__, geosoft.__version__)

    def test_agg(self):
        self.start()

        with gxagg.GXagg.new() as agg:
            self.assertEqual(str(agg), '')
            self.assertEqual(agg.layer_count, 0)

        with gxagg.GXagg.new(self.g3f) as agg:
            self.assertEqual(str(agg), 'test_agg_utm')
            self.assertEqual(agg.layer_count, 1)

        with gxagg.GXagg.new(self.g3f, shade=True) as agg:
            self.assertEqual(str(agg), 'test_agg_utm')
            self.assertEqual(agg.layer_count, 2)

            agg.add_layer(self.g2f)
            self.assertEqual(str(agg), 'test_agg_utm, test_grid_2')
            self.assertEqual(agg.layer_count, 3)

            agg.add_layer(self.g1f, shade=True)
            self.assertEqual(str(agg), 'test_agg_utm, test_grid_2, test_grid_1')
            self.assertEqual(agg.layer_count, 5)

    def test_open(self):
        self.start()

        with gxagg.GXagg.new(self.g3f) as agg:
            self.assertEqual(str(agg), 'test_agg_utm')
            self.assertEqual(agg.layer_count, 1)

            with gxagg.GXagg.open(agg.gxagg) as open_agg:
                self.assertEqual(agg.name, open_agg.name)
                self.assertEqual(open_agg.layer_count, 1)


    def test_settings(self):
        self.start()

        with gxagg.GXagg.new(self.g3f, shade=True) as agg:
            self.assertEqual(agg.layer_count, 2)
            self.assertEqual(agg.brightness, 0.0)
            agg.brightness = -0.5
            self.assertEqual(agg.brightness, -0.5)



if __name__ == '__main__':

    unittest.main()
