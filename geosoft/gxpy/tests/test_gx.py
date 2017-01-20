import unittest
import os
import time

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        gx.GXpy(log=print)

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def start(cls,test):
        if gx.gx:
            gx.gx.log("*** {} > {}".format(os.path.split(__file__)[1], test))

    def test_gxpy(self):
        self.start(gsys.func_name())

        with gx.GXpy(log=print) as gxc:
            self.assertTrue(gxc.gid.find('@') > 0)
            self.assertEqual(gxc.main_wind_id(),0)
            self.assertEqual(gxc.active_wind_id(), 0)
            self.assertEqual(gx.__version__, geosoft.__version__)

    def test_env(self):
        self.start(gsys.func_name())

        with gx.GXpy(log=print) as gxc:
            env = gxc.environment()

            self.assertFalse(env.get('gid') is None)
            self.assertFalse(env.get('current_date') is None)
            self.assertFalse(env.get('current_utc_date') is None)
            self.assertFalse(env.get('current_time') is None)
            self.assertFalse(env.get('current_utc_time') is None)
            self.assertFalse(env.get('license_class') is None)
            self.assertFalse(env.get('folder_workspace') is None)
            self.assertFalse(env.get('folder_temp') is None)
            self.assertFalse(env.get('folder_user') is None)

            env = gxc.environment(2)
            self.assertTrue(isinstance(env,str))

    def test_entitlements(self):
        self.start(gsys.func_name())

        with gx.GXpy(log=print) as gxc:
            ent = gxc.entitlements()
            self.assertTrue(ent.get('1000'), 'Oasis montaj™ Base')

    def test_temp(self):
        self.start(gsys.func_name())

        with gx.GXpy(log=print) as gxc:
            tf = gxc.temp_folder()
            self.assertTrue(os.path.isdir(tf))

            tf = gxc.temp_file()
            self.assertFalse(os.path.exists(tf))

            tf = gxc.temp_file(ext=".dummy")
            self.assertFalse(os.path.exists(tf))
            self.assertEqual(tf[-6:], ".dummy")
            try:
                with open(tf, 'x'):
                    pass
            except:
                self.assertTrue(False)


    def test_elapsed_time(self):
        self.start(gsys.func_name())

        with gx.GXpy() as gxc:
            self.assertTrue(gxc.elapsed_seconds("startup") > 0.0)
            time.sleep(0.25)
            self.assertTrue(gxc.elapsed_seconds("0.25 seconds later") > 0.25)


###############################################################################################

if __name__ == '__main__':

    unittest.main()
