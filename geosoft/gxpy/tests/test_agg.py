import unittest
import os

import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.agg as gxagg
import geosoft.gxpy.grid as gxgrid
import geosoft.gxpy.utility as gxu
import geosoft

from base import GXPYTest


class Test(GXPYTest):

    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest(res_stack=4)
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py), 'testgrids.zip'),
                                       folder=cls._gx.temp_folder())
        cls.g1f = os.path.join(cls.folder, 'test_grid_1.grd')
        cls.g2f = os.path.join(cls.folder, 'test_grid_2.grd')
        cls.g3f = os.path.join(cls.folder, 'test_agg_utm.grd')

    def test_version(self):
        self.start()
        self.assertEqual(gxagg.__version__, geosoft.__version__)

    def test_agg(self):
        self.start()

        with gxagg.Aggregate_image.new() as agg:
            self.assertEqual(str(agg), '')
            self.assertEqual(agg.layer_count, 0)

        with gxagg.Aggregate_image.new(self.g3f) as agg:
            self.assertEqual(str(agg), 'test_agg_utm')
            self.assertEqual(agg.layer_count, 1)

        with gxagg.Aggregate_image.new(self.g3f, shade=True, color_map='cycle') as agg:
            self.assertEqual(str(agg), 'test_agg_utm')
            self.assertEqual(agg.layer_count, 2)

            agg.add_layer(self.g2f)
            self.assertEqual(str(agg), 'test_agg_utm, test_grid_2')
            self.assertEqual(agg.layer_count, 3)

            agg.add_layer(self.g1f, shade=True, color_map='hotcycle')
            self.assertEqual(str(agg), 'test_agg_utm, test_grid_2, test_grid_1')
            self.assertEqual(agg.layer_count, 5)
            self.assertEqual(len(agg.layer_file_names), 5)

            cmap = agg.layer_color_map()
            self.assertEqual(cmap.length, 64)
            cmap = agg.layer_color_map(4)
            self.assertEqual(cmap.length, 25)
            self.assertRaises(gxagg.AggregateException, agg.layer_color_map, 5)

            cmap = agg.layer_color_map(layer=agg.layer_file_names[3])
            self.assertEqual(cmap.length, 63)
            cmap = agg.layer_color_map(agg.layer_file_names[1])
            self.assertEqual(cmap.length, 25)


    def test_open(self):
        self.start()

        with gxagg.Aggregate_image.new(self.g3f) as agg:
            self.assertEqual(str(agg), 'test_agg_utm')
            self.assertEqual(agg.layer_count, 1)

            with gxagg.Aggregate_image.open(agg.gxagg) as open_agg:
                self.assertEqual(agg.name, open_agg.name)
                self.assertEqual(open_agg.layer_count, 1)


    def test_settings(self):
        self.start()

        with gxagg.Aggregate_image.new(self.g3f, shade=True) as agg:
            self.assertEqual(agg.layer_count, 2)
            self.assertEqual(agg.brightness, 0.0)
            agg.brightness = -0.5
            self.assertEqual(agg.brightness, -0.5)

    def test_figure_1(self):
        self.start()

        gxgrid.Grid.open(self.g3f).unit_of_measure = 'nT'
        with gxagg.Aggregate_image.new(self.g3f, shade=True, color_map='elevation.tbl', contour=20) as agg:
            self.crc_map(agg.figure_map(title='image test').file_name)

    def test_figure_2(self):
        self.start()

        gxgrid.Grid.open(self.g3f).unit_of_measure = 'nT'
        with gxagg.Aggregate_image.new(self.g3f, shade=True, color_map='elevation.tbl', contour=20) as agg:
            self.crc_map(agg.figure_map(title='Image with LL Annotations\nsub-title',
                                        legend_label='nT',
                                        features='all').file_name)


if __name__ == '__main__':

    unittest.main()
