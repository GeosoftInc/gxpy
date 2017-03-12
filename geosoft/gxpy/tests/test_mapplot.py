import unittest
import os
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.mapplot as gxmapl
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.view as gxv
import geosoft.gxpy.viewer as gxvwr

def test_map(name="test"):
    testmap = os.path.join(gx.GXpy().temp_folder(), name)
    gxmap.delete_files(testmap)
    return gxmap.GXmap.new_standard_geosoft(filename=testmap,
                                            data_area=(1000,0,11000,5000),
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

    def test_text(self):
        self.start(gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map) as mapl:
                mapl.surround(gap=0.5)
                mapl.set_drawing_attributes(font="Arial")
                mapl.text("Bottom left corner")
                mapl.text("One cm higher", ref_point=(1, 0, 1), pen_def=("R", 50))
                mapl.text("Times Roman", ref_point=(1, 0, 2), text_def=(1, 15), font="Times New Roman")
                mapl.text("Curlz MT", ref_point=(1, 0, 4), text_def=(0.8, 0), font="Curlz MT")
                mapl.set_drawing_attributes(font="tr.gfn")
                mapl.text("Big Geosoft GFN", ref_point=(1, 0, 6), text_def=(1.8, 15), pen_def=("g", 1000))

        # gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 2384488690)

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
                mapl.surround(outer_pen=('r', 2000), gap=1, inner_pen=('g', 250))

        # gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 3763029646)

    def test_rectangle(self):
        self.start(gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxv.GXview(map, viewname='*Data', mode=gxv.READ_ONLY) as v:
                extent = v.extent(extent=gxv.EXTENT_MAP)
            with gxmapl.GXmapplot(map) as mapl:
                mapl.surround(outer_pen=("r", 1000))
                mapl.rectangle(extent, ref_point=(1, 0, 0), pen_def=("bRG200B200", 2000))

        # gxvwr.map(mapfile)
        crc1 = gxmap.crc_map(mapfile)

        with test_map() as map:
            with gxmapl.GXmapplot(map) as mapl:
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_BASE, pen_def=("r", 1000))
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def=("bRG200B200", 2000))

        # gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), crc1)

    def test_annotate(self):
        self.start(gsys.func_name())

        with test_map() as map:
            mapfile = map.filename
            with gxmapl.GXmapplot(map) as mapl:
                mapl.set_drawing_attributes(font="Arial")
                mapl.surround()
                mapl.rectangle(gxmapl.RECTANGLE_EXTENT_DATA, pen_def=("k", 200))
                mapl.annotate_data_view(x_sep=1500)

        # gxvwr.map(mapfile)
        self.assertEqual(gxmap.crc_map(mapfile), 3712184528)

if __name__ == '__main__':

    unittest.main()
