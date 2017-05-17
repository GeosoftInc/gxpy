import unittest
import os

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.system as gsys
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.metadata as gxmeta

from geosoft.gxpy.tests import GXPYTest


class Test(GXPYTest):
    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()
        cls.folder, files = gsys.unzip(os.path.join(os.path.dirname(__file__), 'testgrids.zip'),
                                       folder=cls._gx.temp_folder())
        cls.g1f = os.path.join(cls.folder, 'test_grid_1.grd')
        cls.g2f = os.path.join(cls.folder, 'test_grid_2.grd')

    def test_grc(self):
        self.start()
        self.assertEqual(gxgrd.__version__, geosoft.__version__)

    @unittest.skip('INM - under development')
    def test_grid_metadata(self):
        self.start()

        with gxgrd.Grid.open(self.g1f) as g1:
            gxm = gxapi.GXMETA.create()
            g1.gximg.get_meta(gxm)
            meta = gxmeta.Metadata(gxm)
            meta_dict = meta.metadata
            self.assertTrue('Geosoft' in meta_dict)
            self.assertEqual(meta_dict["Geosoft"]["Data"]["Name"], "test_grid_1")
            self.assertEqual(int(meta_dict["Geosoft"]["Data"]["Grid"]["X Dimension"]), 101)

            meta = gxmeta.Metadata(meta.xml())
            yaml = meta.yaml()
            json = meta.json()
            pass

###############################################################################################

if __name__ == '__main__':

    unittest.main()
