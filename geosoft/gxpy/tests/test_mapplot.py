import unittest
import os
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.mapplot as gxmapl
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.viewer as gxvwr

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

    def test_map_delete(self):
        self.start(gsys.func_name())

        testmap = os.path.join(self.gx.temp_folder(), "test")
        with gxmap.GXmap.new_standard_geosoft(
            filename=testmap,
            data_area=(1000,0,11000,5000),
            cs=gxcs.GXcs("WGS 84 / UTM zone 15N"),
            media="A4",
            margins=(1.5,3,1.5,1),
            inside_margin=0.5) as map:

            mapfile = map.filename
            with gxmapl.GXmapplot(map) as mapl:
                #mapl.surround(outer_pen="G128R128", inner_pen="B128", gap=0.2)
                mapl.surround(gap=0.5)
                mapl.text("Bottom left corner")
                mapl.text("One cm higher", ref_point=(1, 0, 1), pen_def=("R", 50))
                mapl.text("Times Roman", ref_point=(1, 0, 2), text_def=(1, 15), font="Times New Roman")
                mapl.text("Curlz MT", ref_point=(1, 0, 4), text_def=(0.8, 0), font="Curlz MT")
                mapl.set_drawing_attributes(font="tr.gfn")
                mapl.text("Big Geosoft GFN", ref_point=(1, 0, 6), text_def=(1.8, 15), pen_def=("g", 1000))

        gxvwr.map(mapfile)
        #self.assertEqual(gxmap.crc_map(mapfile), 4001381093)

if __name__ == '__main__':

    unittest.main()
