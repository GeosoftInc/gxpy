import unittest
import os

import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.agg as gxagg
import geosoft

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gx = gx.GXpy(log=print, res_stack=4)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                       folder=cls.gx.temp_folder())
        cls.g1f = os.path.join(cls.folder, 'test_grid_1.grd')
        cls.g2f = os.path.join(cls.folder, 'test_grid_2.grd')
        cls.g3f = os.path.join(cls.folder, 'test_agg_utm.grd')
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def start(cls,test):
        cls.gx.log("*** {} > {}".format(os.path.split(__file__)[1], test))

    def test_version(self):
        self.start(gsys.func_name())
        self.assertEqual(gxagg.__version__, geosoft.__version__)

    def test_agg(self):
        self.start(gsys.func_name())

        with gxagg.GXagg() as agg:
            self.assertEqual(str(agg), 'GXagg')

        with gxagg.GXagg(self.g3f) as agg:
            self.assertEqual(str(agg), 'GXagg> test_agg_utm')


if __name__ == '__main__':

    unittest.main()
