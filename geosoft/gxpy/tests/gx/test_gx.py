import unittest

import pprint

import geosoft
import geosoft.gxpy.system as gsys
import geosoft.gxpy.gx as gxp

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gxp = gxp.GXpy()
        cls.pp = pprint.PrettyPrinter(indent=3)

    @classmethod
    def tearDownClass(cls):
        pass
        
    @classmethod
    def start(cls,test):
        print("\n*** {} ***".format(test))

    def test_gxpy(self):
        self.start(gsys.func_name())

        self.assertTrue(self.gxp.gid.find('@') > 0)
        self.assertEqual(self.gxp.main_wind_id(),0)
        self.assertEqual(self.gxp.active_wind_id(), 0)
        self.assertEqual(gxp.__version__, geosoft.__version__)

    def test_ui_onoff(self):
        self.start(gsys.func_name())

        self.gxp.dissable_app()
        self.gxp.enable_app()

    def test_env(self):
        self.start(gsys.func_name())

        env = self.gxp.environment()
        
        self.assertFalse(env.get('gid') is None)
        self.assertFalse(env.get('current_date') is None)
        self.assertFalse(env.get('current_utc_date') is None)
        self.assertFalse(env.get('current_time') is None)
        self.assertFalse(env.get('current_utc_time') is None)
        self.assertFalse(env.get('license_class') is None)
        self.assertFalse(env.get('folder_workspace') is None)
        self.assertFalse(env.get('folder_temp') is None)
        self.assertFalse(env.get('folder_user') is None)

        env = self.gxp.environment(2)
        self.assertTrue(isinstance(env,str))
        print(env)


    def test_entitlements(self):
        self.start(gsys.func_name())

        ent = self.gxp.entitlements()
        self.assertTrue(ent.get('1000'), 'Oasis montaj™ Base')
        #self.pp.pprint(ent)

    def test_display_message(self):
        self.start(gsys.func_name())

        self.gxp.display_message('test title', 'test message')

###############################################################################################

if __name__ == '__main__':

    unittest.main()
