import unittest
import os
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.mapplot as gxmapl
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.view as gxv
import geosoft.gxpy.viewer as gxvwr

def test_map(name=None, data_area=(1000,0,11000,5000)):

    if name is None:
        name = os.path.join(gx.GXpy().temp_folder(), "test")
    gxmap.delete_files(name)
    return gxmap.GXmap.new_standard_geosoft(filename=name,
                                            data_area=data_area,
                                            cs=gxcs.GXcs("WGS 84 / UTM zone 15N"),
                                            media="A4",
                                            margins=(1.5,3,1.5,1),
                                            inside_margin=0.5)

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gx = gx.GXpy(log=print, parent_window=-1, max_warnings=8)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    
    @classmethod
    def start(cls,test):
        cls.gx.log("*** {} > {}".format(os.path.split(__file__)[1], test))

    def test_command(self):
        self.start(gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map) as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_xy(x_sep=1500, tick=0.1)
                mapl.define_named_attribute('gridpen', pen_def="bt200")
                mapl.command("GRID 3,,,,,gridpen\n")

        #gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 1145267206)

    def test_text(self):
        self.start(gsys.func_name())

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

        #gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 3942171818)

    def test_surround(self):
        self.start(gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map) as mapl:
                mapl.surround()

        # gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 2890917966)

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map) as mapl:
                mapl.surround(gap=0.15)

        # gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 2694721289)

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map) as mapl:
                mapl.surround(outer_pen="rt2000", gap=1, inner_pen="gt250")

        # gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 3763029646)

    def test_att(self):
        self.start(gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxv.GXview(map, viewname='*Data', mode=gxv.READ_ONLY) as v:
                extent = v.extent(extent=gxv.EXTENT_MAP)
            with gxmapl.GXmapplot(map) as mapl:
                mapl.define_named_attribute('Red', pen_def='Rkt100')
                mapl.define_named_attribute('Blue', pen_def='bGt1000')
                mapl.rectangle(extent, ref_point=(1, 0, 0), att='Red')
                extent = (extent[0]+1, extent[1]+1, extent[2]-1, extent[3]-1)
                mapl.rectangle(extent, ref_point=(1, 0, 0), att='Blue')
                extent = (extent[0] + 1, extent[1] + 1, extent[2] - 1, extent[3] - 1)
                mapl.rectangle(extent, ref_point=(1, 0, 0), pen_def="yt2000")

        #gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 3472166003)

    def test_rectangle(self):
        self.start(gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxv.GXview(map, viewname='*Data', mode=gxv.READ_ONLY) as v:
                extent = v.extent(extent=gxv.EXTENT_MAP)
            with gxmapl.GXmapplot(map) as mapl:
                mapl.surround(outer_pen="rt1000")
                mapl.rectangle(extent, ref_point=(1, 0, 0), pen_def="bRG200B200t2000")

        # gxvwr.map(mapfile)
        crc1 = gxmap.crc_map(mapfile)

        with test_map() as map:
            with gxmapl.GXmapplot(map) as mapl:
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_BASE, pen_def="rt1000")
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="bRG200B200t2000")

        #gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), crc1)

    def test_annotate_xy(self):
        self.start(gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map) as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.surround(outer_pen="rt10")
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="gt200")
                mapl.annotate_data_xy(x_sep=1500, pen_def="kt10")

        #gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 449148037)

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map) as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_xy(x_sep=1500, grid=gxmapl.GRID_DOTTED)

        #gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 4125672500)

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map) as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_xy(x_sep=1500, tick=0.1, grid=gxmapl.GRID_CROSSES, grid_pen="bt100")

        #gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 3827981335)

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map) as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_xy(x_sep=1500, tick=0.1, grid=gxmapl.GRID_LINES, grid_pen="bt100")

        #gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 1145267206)

    def test_annotate_ll(self):
        self.start(gsys.func_name())

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map) as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt1")
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      text_def = (0.18, 15),
                                      grid_pen="bt250")

        #gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 1911276164)

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map) as mapl:
                mapl.define_named_attribute(font="Arial", pen_def='kt50')
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def="kt200")
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      grid_pen="bt250",
                                      pen_def="kt1", text_def=(0.18, 15),
                                      top=gxmapl.TOP_IN)

        #gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 610738257)


if __name__ == '__main__':

    unittest.main()
