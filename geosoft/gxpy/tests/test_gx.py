import unittest
import os
import time

import geosoft
import geosoft.gxpy.gx as gx

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
        
    def test_gxpy(self):

        with gx.GXpy(log=print) as gxc:

            self.assertTrue(gxc.gid.find('@') > 0)
            self.assertEqual(gxc.main_wind_id(),0)
            self.assertEqual(gxc.active_wind_id(), 0)
            self.assertEqual(gx.__version__, geosoft.__version__)
            self.assertTrue(gx.gxcontext is not None)

            gxcontext = gx.gxcontext
            self.assertEqual(gxc, gxcontext)
            self.assertRaises(gx.GXException, gx.GXpy)

        self.assertTrue(gx.gxcontext is None)

        with gx.GXpy(parent_window=-1, log=print) as gxc:
            gxc.log("\n\ngxc window ID: {}\n\n".format(gxc.main_wind_id()))
            self.assertNotEqual(gxc.main_wind_id(), 0)

    def test_ui_onoff(self):
        with gx.GXpy(log=print) as gxc:
            gxc.disable_app()
            gxc.enable_app()

    def test_env(self):

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
            gxc.log(env)

    def test_entitlements(self):

        with gx.GXpy(log=print) as gxc:
            ent = gxc.entitlements()
            self.assertTrue(ent.get('1000'), 'Oasis montaj™ Base')

    def test_temp(self):

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
        with gx.GXpy(log=print) as gxc:
            gxc.log('\n******* test elapsed time **********')
            self.assertTrue(gxc.elapsed_seconds("startup") > 0.0)
            time.sleep(0.25)
            self.assertTrue(gxc.elapsed_seconds("0.25 seconds later") > 0.25)


###############################################################################################

if __name__ == '__main__':

    unittest.main()
