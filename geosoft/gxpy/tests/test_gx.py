#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import unittest
import os
import time
import concurrent.futures

import geosoft
import geosoft.gxpy.gx as gx

from base import GXPYTest


class Test(GXPYTest):
    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest(res_stack=4)

    def _get_thread_gx_context(cls, use_gxpy_context: bool):
        if use_gxpy_context:
            return gx.GXpy('ThreadGXContext', geosoft.__version__)
        else:
            return geosoft.gxapi.GXContext.create('ThreadGXContext', geosoft.__version__)

    def _thread_gx_func(self, use_gxpy_context: bool):
        tls_geo = geosoft.gxapi.GXContext._try_get_tls_geo()
        if tls_geo is not None:
            return "(1) We have a GX context geo pointer in TLS but should not!"

        if gx._have_gx():
            return "(2) geosoft.gxpy._have_gx returned True but should be False!"

        with self._get_thread_gx_context(use_gxpy_context) as gxc:
            time.sleep(0.1)
            tls_geo = geosoft.gxapi.GXContext._try_get_tls_geo()
            if tls_geo is None:
                return "(3) We should have a GX context geo pointer in TLS but do not!"
            if use_gxpy_context:
                if not gx._have_gx():
                    return "(4) geosoft.gxpy._have_gx returned False but should be True!"
            else:
                if gx._have_gx():
                    return "(5) geosoft.gxpy._have_gx returned True but should be False!"

        if gx._have_gx():
            return "(6) geosoft.gxpy._have_gx returned True but should be False!"

        tls_geo = geosoft.gxapi.GXContext._try_get_tls_geo()
        if tls_geo is not None:
            return "(7) We have a GX context geo pointer in TLS but should not!"
        return ""

    NUM_THREADS_TO_TEST = 100

    def _run_threads_context(self, use_gxpy_context: bool):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.NUM_THREADS_TO_TEST) as executor:
            futures = []
            for i in range(0, self.NUM_THREADS_TO_TEST):
                futures.append(executor.submit(lambda: self._thread_gx_func(use_gxpy_context)))
            for future in futures:
                result = future.result()
                if result:
                    self.fail(result)

    def test_threads_gxapi_context(self):
        self._run_threads_context(False)

    def test_threads_gxpy_context(self):
        self._run_threads_context(True)

    def test_gxpy(self):
        self.start()
        gxc = self._gx
        self.assertTrue(gxc.gid.find('@') > 0)
        self.assertEqual(gxc.main_wind_id, 0)
        self.assertEqual(gxc.active_wind_id, 0)
        self.assertEqual(gx.__version__, geosoft.__version__)

    def test_env(self):
        self.start()
        gxc = self._gx
        self.assertFalse(gxc.gid is None)
        self.assertFalse(gxc.current_date is None)
        self.assertFalse(gxc.current_utc_date is None)
        self.assertFalse(gxc.current_time is None)
        self.assertFalse(gxc.current_utc_time is None)
        self.assertFalse(gxc.license_class is None)
        self.assertFalse(gxc.folder_workspace is None)
        self.assertFalse(gxc.folder_temp is None)
        self.assertFalse(gxc.folder_user is None)
        self.assertTrue(gxc.geosoft_version_label)
        self.assertTrue(gxc.geosoft_version_major >= 9)
        self.assertTrue(gxc.geosoft_version_minor >= 0)
        self.assertTrue(gxc.geosoft_version_micro >= 0)
        self.assertTrue(gxc.geosoft_build_label)
        self.assertTrue(gxc.geosoft_build_number)
        self.assertTrue(gxc.geosoft_name)


    @unittest.skip('WIP')
    def test_entitlements(self):
        with gx.GXpy() as gxc:
            ent = gxc.entitlements()
            self.assertTrue(ent['1000'], 'Oasis montaj™ Base')
            self.assertTrue(gxc.has_entitlement(1000))
            self.assertTrue(gxc.has_entitlement('Oasis montaj™ Base'))
            self.assertTrue(gxc.has_entitlement(2000))
            self.assertTrue(gxc.has_entitlement("ArcGIS"))
            self.assertTrue(gxc.has_entitlement(3000))
            self.assertTrue(gxc.has_entitlement("MapInfo"))
            self.assertFalse(gxc.has_entitlement("bogus"))
            #for e in ent:
            #    print('{}: "{}"'.format(e, ent[e]))

            if gxc.entitled:
                self.assertTrue(gxc.has_entitlement(10000) or
                                gxc.has_entitlement(30000) or
                                gxc.has_entitlement(30101) or
                                gxc.has_entitlement(40000) or
                                gxc.has_entitlement(41000))
            else:
                self.assertTrue(gxc.has_entitlement(1000) and
                                gxc.has_entitlement(2000) and
                                gxc.has_entitlement(3000))
                self.assertFalse(gxc.has_entitlement(10000))
                self.assertFalse(gxc.has_entitlement(30000))
                self.assertFalse(gxc.has_entitlement(30101))
                self.assertFalse(gxc.has_entitlement(40000))
                self.assertFalse(gxc.has_entitlement(41000))

    def test_temp(self):
        self.start()
        gxc = self._gx

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
        self.start()
        self.assertTrue(self._gx.elapsed_seconds("startup") > 0.0)
        time.sleep(0.25)
        self.assertTrue(self._gx.elapsed_seconds("0.25 seconds later") > 0.25)

    def test_remove_temp_files(self):
        self.start()
        gxc = self._gx

        def make_file(name):
            with open(name, 'w+') as f:
                f.write('ok')

        files = []
        for i in range(3):
            fn = gxc.temp_file()
            make_file(fn)
            files.append(fn)

        gxc.remove_stale_temporary_files()
        for f in files:
            self.assertTrue(os.path.exists(f))

        gxc.remove_stale_temporary_files(age=0)
        for f in files:
            self.assertFalse(os.path.exists(f))

    def test_profile(self):
        self.start()
        gxc = self._gx
        self.assertTrue(len(gxc.profile_name))
        self.assertTrue(len(gxc.profile_url))

###############################################################################################

if __name__ == '__main__':

    unittest.main()
