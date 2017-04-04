import unittest
import os

import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.mapplot as gxmapl
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.view as gxv

from geosoft.gxpy.tests import GXPYTest


def test_map(name=None, data_area=(1000,0,11000,5000)):

    if name is None:
        name = os.path.join(gx.GXpy().temp_folder(), "test")
    gxmap.delete_files(name)
    cs = gxcs.GXcs("WGS 84 / UTM zone 15N")
    return gxmap.GXmap.new(filename=name,
                           data_area=data_area,
                           cs=cs,
                           media="A4",
                           margins=(1.5, 3, 1.5, 1),
                           inside_margin=0.5)


class Test(unittest.TestCase, GXPYTest):

    @classmethod
    def setUpClass(cls):
        GXPYTest.setUpClass(cls, __file__)

    @classmethod
    def tearDownClass(cls):
        GXPYTest.tearDownClass(cls)

    @classmethod
    def start(cls, test, test_name):
        parts = os.path.split(__file__)
        test.result_dir = os.path.join(parts[0], 'results', parts[1], test_name)
        cls.gx.log("*** {} > {}".format(parts[1], test_name))

    def view_crc(self, map_file):
        self.crc_map(map_file, display=False, update_result=False)

    @unittest.skip('This test does not produce stable results')  # TODO
    def test_command(self):
        Test.start(self, gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_xy(x_sep=1500, tick=0.1)
                mapl.define_named_attribute('gridpen', pen_def="bt200")
                mapl.command("GRID 3,,,,,gridpen\n")

        self.view_crc(mapfile)

    @unittest.skip('This test does not produce stable results')  # TODO
    def test_text(self):
        Test.start(self, gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map) as mapl:
                mapl.surround(gap=0.5)
                mapl.define_named_attribute(font="Arial")
                mapl.text("Bottom left corner")
                mapl.text("One cm higher", ref_point=(1, 0, 1), pen_def="rt50")
                mapl.text("Times Roman", ref_point=(1, 0, 2), text_def=(1, 15), font="Times New Roman")
                mapl.text("Curlz MT", ref_point=(1, 0, 4), text_def=(0.8, 0), font="Curlz MT")
                mapl.define_named_attribute(font="tr.gfn")
                mapl.text("Big Geosoft GFN", ref_point=(1, 0, 6), text_def=(1.8, 15), pen_def="gt1000")

        self.assertEqual(gxmap.crc_map(mapfile), 1023850529)

    def test_surround(self):
        Test.start(self, gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.surround()

        self.assertEqual(gxmap.crc_map(mapfile), 2477386487)

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.surround(gap=0.15)

        self.assertEqual(gxmap.crc_map(mapfile), 4262826009)

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.surround(outer_pen="rt2000", gap=1, inner_pen="gt250")

        self.assertEqual(gxmap.crc_map(mapfile), 3038258344)

    @unittest.skip('This test does not produce stable results')  # TODO
    def test_att(self):
        Test.start(self, gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxv.GXview(map, viewname='*Data', mode=gxv.READ_ONLY) as v:
                extent = v.extent(extent=gxv.EXTENT_MAP)
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute('Red', pen_def='Rkt100')
                mapl.define_named_attribute('Blue', pen_def='bGt1000')
                mapl.rectangle(extent, ref_point=(1, 0, 0), att='Red')
                extent = (extent[0]+1, extent[1]+1, extent[2]-1, extent[3]-1)
                mapl.rectangle(extent, ref_point=(1, 0, 0), att='Blue')
                extent = (extent[0] + 1, extent[1] + 1, extent[2] - 1, extent[3] - 1)
                mapl.rectangle(extent, ref_point=(1, 0, 0), pen_def="yt2000")

        self.view_crc(mapfile)

    def test_rectangle(self):
        Test.start(self, gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxv.GXview(map, viewname='*Data', mode=gxv.READ_ONLY) as v:
                extent = v.extent(extent=gxv.EXTENT_MAP)
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.surround(outer_pen="rt1000")
                mapl.rectangle(extent, ref_point=(1, 0, 0), pen_def="bRG200B200t2000")

        # gxvwr.map(mapfile)
        crc1 = gxmap.crc_map(mapfile)

        with test_map() as map:
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_BASE, pen_def="rt1000")
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="bRG200B200t2000")

        #gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), crc1)

    @unittest.skip('This test does not produce stable results')  # TODO
    def test_scale(self):
        Test.start(self, gsys.func_name())

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.surround(outer_pen="rt1000")
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.scale_bar()
                mapl.scale_bar(ref_point=(2, 0, 2), length=3, sections=2)
                mapl.scale_bar(ref_point=(5, 0, 0), length=8, sections=2, post_scale=True)
                mapl.scale_bar(ref_point=(3, -3, 1.5), length=4, text_def=(0.2, 15), post_scale=True)

        self.view_crc(mapfile)

    def text_group(self):
        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.surround(outer_pen="rt1000")
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      text_def=(0.18, 15),
                                      grid_pen="bt250")
                mapl.north_arrow(ref_point=(6, -1.5, 0), pen_def="kt500", length=3)

        self.view_crc(mapfile)

    @unittest.skip('This test does not produce stable results')  # TODO
    def test_narr(self):
        Test.start(self, gsys.func_name())

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.surround(outer_pen="rt1000")
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      text_def=(0.18, 15),
                                      grid_pen="bt250")
                mapl.north_arrow(ref_point=(6, -1.5, 0), pen_def="kt500", length=3)

        self.view_crc(mapfile)

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.surround(outer_pen="rt1000")
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      text_def=(0.18, 15),
                                      grid_pen="bt250")
                mapl.north_arrow(ref_point=(3, -1.5, 3),
                                 pen_def="kt500",
                                 inclination=68.5,
                                 declination=3.55,
                                 length=3,
                                 text_def=(0.2,15))

        self.view_crc(mapfile)

    @unittest.skip('This test does not produce stable results')  # TODO
    def test_annotate_xy(self):
        Test.start(self, gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.surround(outer_pen="rt10")
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="gt200")
                mapl.annotate_data_xy(x_sep=1500, pen_def="kt10")

        self.view_crc(mapfile)

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_xy(x_sep=1500, grid=gxmapl.GRID_DOTTED, offset=0.5)

        self.view_crc(mapfile)

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_xy(x_sep=1500, tick=0.1, grid=gxmapl.GRID_CROSSES, grid_pen="bt100")

        self.view_crc(mapfile)

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_xy(x_sep=1500, tick=0.1, grid=gxmapl.GRID_LINES, grid_pen="bt100")

        self.view_crc(mapfile)

    @unittest.skip('This test does not produce stable results')  # TODO
    def test_annotate_ll(self):
        Test.start(self, gsys.func_name())

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA)
                mapl.annotate_data_xy()
                mapl.annotate_data_ll()

        self.view_crc(mapfile)

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt1")
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      grid_pen="bt500")

        self.view_crc(mapfile)

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial", pen_def='kt50')
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      grid_pen="bt250",
                                      pen_def="rt1", text_def=(0.25, 15),
                                      top=gxmapl.TOP_IN)

        self.view_crc(mapfile)

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial", pen_def='kt5', text_def=(0.2, 0))
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_xy(tick=0.1, grid=gxmapl.GRID_LINES, pen_def="kt10", grid_pen="kt100")
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      grid_pen="bt250",
                                      pen_def="kt1", text_def=(0.18, 15))

        self.view_crc(mapfile)

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial", pen_def='kt5', text_def=(0.2, 0))
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      grid_pen="bt250",
                                      pen_def="kt1",
                                      top=gxmapl.TOP_IN,
                                      text_def=(0.15, 15))
                mapl.annotate_data_xy(tick=0.1, grid=gxmapl.GRID_LINES,
                                      grid_pen="kt100",
                                      pen_def="kt20",
                                      top=gxmapl.TOP_IN,
                                      text_def=(0.2, 0))

        self.view_crc(mapfile)

    def test_ll_no_projection(self):
        Test.start(self, gsys.func_name())

        with gxmap.GXmap.new() as map:
            with gxmapl.GXmapplot(map) as mapl:
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      grid_pen="bt250",
                                      pen_def="kt1",
                                      top=gxmapl.TOP_IN,
                                      text_def=(0.15, 15))

    @unittest.skip('This test does not produce stable results')  # TODO
    def test_start_group(self):
        Test.start(self, gsys.func_name())

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.surround(outer_pen="rt1000")
                mapl.start_group('data_surround', view=gxmapl.VIEW_DATA)
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.start_group('north')
                mapl.north_arrow(ref_point=(6, -1.5, 0), pen_def="kt500", length=3)

        self.view_crc(mapfile)

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.surround(outer_pen="rt1000")
                mapl.start_group('data_surround', view=gxmapl.VIEW_DATA)
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.start_group('north')
                mapl.north_arrow(ref_point=(6, -1.5, 0), pen_def="kt500", length=3)
                mapl.start_group('north', mode=gxmapl.GROUP_NEW)
                mapl.north_arrow(ref_point=(4, 1.5, 0), pen_def="kt500", length=3)

        self.view_crc(mapfile)

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.surround(outer_pen="rt1000")
                mapl.start_group('data_surround', view=gxmapl.VIEW_DATA)
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.start_group('north')
                mapl.north_arrow(ref_point=(6, -1.5, 0), pen_def="kt500", length=3)
                mapl.start_group('north', mode=gxmapl.GROUP_APPEND)
                mapl.north_arrow(ref_point=(4, 1.5, 0), pen_def="kt500", length=3)

        self.view_crc(mapfile)

if __name__ == '__main__':

    unittest.main()
