import unittest
import os
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gx = gx.GXpy(log=print)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    
    @classmethod
    def start(cls,test):
        cls.gx.log("\n*** {} *** - {}".format(test, geosoft.__version__))

    def test_version(self):
        self.start(gsys.func_name())
        self.assertEqual(gxmap.__version__, geosoft.__version__)

    def test_newmap(self):
        self.start(gsys.func_name())

        # temp map
        with gxmap.GXmap.new() as gmap:
            gmap.commit_changes()
            mapfile = gmap.filename()
            self.assertTrue(os.path.isfile(mapfile))
        self.assertFalse(os.path.isfile(mapfile))

        # test map
        map_name = 'test_newmap'
        gxmap.delete_files(map_name)
        with gxmap.GXmap.new(map_name) as gmap:
            mapfile = gmap.filename()
            self.assertEqual(mapfile, os.path.abspath((map_name + '.map')))
        self.assertTrue(os.path.isfile(mapfile))

        # verify can't write on a new map
        self.assertRaises(gxmap.MAPException, gxmap.GXmap.new, map_name)
        self.assertRaises(gxmap.MAPException, gxmap.GXmap.new, mapfile)
        with gxmap.GXmap.new(map_name, overwrite=True):
            pass

        # but I can open it
        with gxmap.GXmap.open(map_name):
            pass
        with gxmap.GXmap.open(mapfile):
            pass

        gxmap.delete_files(mapfile)
        self.assertFalse(os.path.isfile(mapfile))


if __name__ == '__main__':

    unittest.main()
