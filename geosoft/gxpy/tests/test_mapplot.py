import unittest
import os
import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.mapplot as gxmapl
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.view as gxv
import geosoft.gxpy.viewer as gxvwr
import geosoft.gxpy.grd as gxgrd
import geosoft.gxpy.agg as gxagg

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

    def view_crc(self, mapfile, crc=None, display=False):
        if display:
            gxvwr.map(mapfile)
        if crc:
            self.assertEqual(gxmap.crc_map(mapfile), crc)

    def test_command(self):
        self.start(gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.annotate_data_xy(x_sep=1500, tick=0.1)
                mapl.define_named_attribute('gridpen', pen_def="bt200")
                mapl.command("GRID 3,,,,,gridpen\n")

        self.view_crc(mapfile, 0)

    def test_group(self):
        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      text_def=(0.18, 15),
                                      grid_pen="bt250")

        #self.view_crc(mapfile, 582402369)

    def test_annotate_xy(self):
        self.start(gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.annotate_data_xy(x_sep=1500, pen_def="kt10")

        self.view_crc(mapfile, 0)

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.annotate_data_xy(x_sep=1500, grid=gxmapl.GRID_DOTTED, offset=0.5)

        self.view_crc(mapfile, 0)

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.annotate_data_xy(x_sep=1500, tick=0.1, grid=gxmapl.GRID_CROSSES, grid_pen="bt100")

        self.view_crc(mapfile, 0)

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.annotate_data_xy(x_sep=1500, tick=0.1, grid=gxmapl.GRID_LINES, grid_pen="bt100")

        self.view_crc(mapfile, 0)

    def test_annotate_ll(self):
        self.start(gsys.func_name())

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.annotate_data_xy()
                mapl.annotate_data_ll()

        self.view_crc(mapfile, 0)

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial")
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      grid_pen="bt500")

        self.view_crc(mapfile, 0)

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial", pen_def='kt50')
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      grid_pen="bt250",
                                      pen_def="rt1", text_def=(0.25, 15),
                                      top=gxmapl.TOP_IN)

        self.view_crc(mapfile, 0)

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial", pen_def='kt5', text_def=(0.2, 0))
                mapl.annotate_data_xy(tick=0.1, grid=gxmapl.GRID_LINES, pen_def="kt10", grid_pen="kt100")
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      grid_pen="bt250",
                                      pen_def="kt1", text_def=(0.18, 15))

        self.view_crc(mapfile, 0)

        with test_map(data_area=(350000,7000000,400000,7030000)) as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map, font='Arial') as mapl:
                mapl.define_named_attribute(font="Arial", pen_def='kt5', text_def=(0.2, 0))
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

        self.view_crc(mapfile, 0)

    def test_ll_no_projection(self):
        self.start(gsys.func_name())

        with gxmap.GXmap.new() as map:
            with gxmapl.GXmapplot(map) as mapl:
                mapl.annotate_data_ll(grid=gxmapl.GRID_LINES,
                                      grid_pen="bt250",
                                      pen_def="kt1",
                                      top=gxmapl.TOP_IN,
                                      text_def=(0.15, 15))

if __name__ == '__main__':

    unittest.main()
