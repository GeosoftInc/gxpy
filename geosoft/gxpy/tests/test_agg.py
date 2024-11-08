#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import unittest
import os

import geosoft.gxpy.system as gsys
import geosoft.gxpy.agg as gxagg
import geosoft.gxpy.grid as gxgrid
import geosoft.gxpy.utility as gxu
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.geometry as gxgm
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
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py), 'section_grids.zip'),
                                       folder=cls._gx.temp_folder())
        cls.g4f = os.path.join(cls.folder, 'X_Slices.grd')

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

        gxgrid.Grid.open(self.g3f, mode=gxgrid.FILE_READWRITE).unit_of_measure = 'nT'
        with gxagg.Aggregate_image.new(self.g3f, shade=True, color_map='elevation.tbl', contour=20) as agg:
            self.crc_map(agg.figure_map(title='image test').file_name)

    def test_figure_2(self):
        self.start()

        gxgrid.Grid.open(self.g3f, mode=gxgrid.FILE_READWRITE).unit_of_measure = 'nT'
        with gxagg.Aggregate_image.new(self.g3f, shade=True, color_map='elevation.tbl', contour=20) as agg:
            self.crc_map(agg.figure_map(title='Image with LL Annotations\nsub-title',
                                        legend_label='nT',
                                        features='all').file_name)

    def test_image_file(self):
        self.start()

        image_file = ''
        try:
            with gxagg.Aggregate_image.new(self.g3f, shade=True, color_map='elevation.tbl', contour=20) as agg:

                image_file = agg.image_file(image_type=gxmap.RASTER_FORMAT_PNG, pix_width=None)

                with gxgrid.Grid.open(image_file + '(IMG,t=png)') as g:
                    nx, ny, x0, y0, dx, dy, rot = agg.spatial_properties
                    self.assertEqual(g.coordinate_system, agg.coordinate_system)
                    self.assertEqual(g.nx, nx)
                    self.assertEqual(g.ny, ny)
                    self.assertEqual(g.x0, x0)
                    self.assertEqual(g.y0, y0)
                    self.assertAlmostEqual(g.dx, dx)
                    self.assertAlmostEqual(g.dy, dy)
                    self.assertAlmostEqual(g.rot, rot)
        finally:
            gxu.delete_file(image_file)

        try:
            with gxagg.Aggregate_image.new(self.g3f, shade=True, color_map='elevation.tbl', contour=20) as agg:

                display_area = gxgm.Point2(((336000, 6160000, 0.0),(338000, 6161500, 0.0)))

                image_file = agg.image_file(image_type=gxmap.RASTER_FORMAT_PNG,
                                            pix_width=800, display_area=display_area)

                with gxgrid.Grid.open(image_file + '(IMG,t=png)') as g:
                    self.assertEqual(g.coordinate_system, agg.coordinate_system)
                    self.assertEqual(g.nx, 800)
                    self.assertEqual(g.ny, 600)
                    self.assertEqual(g.extent_xy, display_area.extent_xy)
                    self.assertEqual(g.extent_minimum_xy, display_area.extent_minimum_xy)
                    self.assertEqual(g.extent_maximum_xy, display_area.extent_maximum_xy)

        finally:
            gxu.delete_file(image_file)

        try:
            with gxagg.Aggregate_image.new(self.g3f, shade=True, color_map='elevation.tbl', contour=20) as agg:

                display_area = gxgm.Point2(agg.extent, coordinate_system='AGD66 / AMG zone 53')

                image_file = agg.image_file(image_type=gxmap.RASTER_FORMAT_PNG,
                                            pix_width=800, display_area=display_area)

                with gxgrid.Grid.open(image_file + '(IMG,t=png)') as g:
                    self.assertEqual(g.coordinate_system, display_area.coordinate_system)
                    self.assertEqual(g.nx, 800)
                    self.assertEqual(g.ny, 602)

        finally:
            gxu.delete_file(image_file)

    def test_slice_agg(self):
        self.start()

        with gxagg.Aggregate_image.new(self.g4f) as agg:
            image_file = agg.image_file(image_type=gxmap.RASTER_FORMAT_PNG, pix_width=None)
            with gxgrid.Grid.open(image_file + '(IMG;T=png)') as img:
                self.assertEqual(img.nx, 57)
                self.assertEqual(img.ny, 13)
                self.assertTrue(img.coordinate_system.is_oriented)
                self.assertEqual(img.dimension, (28499.968724331295, 42.222175888717175, 6500.0))

if __name__ == '__main__':

    unittest.main()
