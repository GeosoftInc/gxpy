import unittest
import numpy as np
import os
import datetime
from datetime import timezone, datetime

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.system as gsys
import geosoft.gxpy.utility as gxu

from geosoft.gxpy.tests import GXPYTest


class Test(unittest.TestCase, GXPYTest):
    @classmethod
    def setUpClass(cls):
        GXPYTest.setUpClass(cls, __file__)

    @classmethod
    def tearDownClass(cls):
        GXPYTest.tearDownClass(cls)

    @classmethod
    def start(cls,test):
        cls.gx.log("*** {} > {}".format(os.path.split(__file__)[1], test))

    def test_misc(self):
        self.start(gsys.func_name())

        self.assertEqual(gxu.__version__, geosoft.__version__)

        self.assertEqual(gxu.gx_dtype('float'),gxapi.GS_DOUBLE)
        self.assertEqual(gxu.gx_dtype('int'),gxapi.GS_LONG)
        self.assertEqual(gxu.gx_dtype("<U18"),-18)
        self.assertEqual(gxu.gx_dtype('uint64'),gxapi.GS_ULONG64)

        self.assertEqual(gxu.dtype_gx(gxapi.GS_DOUBLE), np.float)
        self.assertEqual(gxu.dtype_gx(gxapi.GS_FLOAT), np.float32)
        self.assertEqual(gxu.dtype_gx(gxapi.GS_LONG), np.int32)
        self.assertEqual(gxu.dtype_gx(-2000).str, "<U2000")
        self.assertEqual(gxu.dtype_gx(gxapi.GS_TYPE_DEFAULT), None)
        self.assertEqual(gxu.dtype_gx(gxapi.GS_ULONG64), np.uint64)

        self.assertEqual(gxu.gx_dummy(np.float),gxapi.rDUMMY)
        self.assertEqual(gxu.gx_dummy(np.int32),gxapi.iDUMMY)
        self.assertEqual(gxu.gx_dummy(np.int64),gxapi.GS_S8DM)
        self.assertEqual(gxu.gx_dummy(np.str_), '')
        self.assertEqual(gxu.gx_dummy('U48'), '')

        self.assertTrue(gxu.is_float(gxu.gx_dtype('float')))
        self.assertFalse(gxu.is_int(gxu.gx_dtype('float')))
        self.assertTrue(gxu.is_int(gxu.gx_dtype('uint64')))
        self.assertFalse(gxu.is_float(gxu.gx_dtype('uint64')))
        self.assertTrue(gxu.is_string(gxu.gx_dtype('U18')))
        self.assertFalse(gxu.is_int(gxu.gx_dtype('U18')))
        self.assertFalse(gxu.is_float(gxu.gx_dtype('U18')))
        self.assertEqual(gxu.is_string(gxu.gx_dtype('U18')), 18)

        npd = np.array([[1,1],[2,2],[-127,1],[3,3]],dtype=gxu.dtype_gx(gxapi.GS_BYTE))
        self.assertEqual(list(gxu.dummy_mask(npd)),[False,False,True,False])

        npd = np.array([1,2,3,4],dtype=gxu.dtype_gx(gxapi.GS_BYTE))
        try:
            gxu.dummy_mask(npd)
            self.assertTrue(False)
        except: pass

    def test_dictlist(self):
        self.start(gsys.func_name())

        lst = gxapi.GXLST.create(1000)
        lst.add_item("a","aa")
        lst.add_item("b","bb")
        lst.add_item("c","cc")
        d = gxu.dict_from_lst(lst)
        self.assertEqual(len(d),lst.size())
        self.assertEqual(d.get('b'),'bb')

    def test_dictreg(self):
        self.start(gsys.func_name())

        d = {'a':'A', 'b':'BEE', 'c':[1,2,3], 'g':7.123, 'h':{'hh':'name'}}
        reg = gxu.reg_from_dict(d)
        dd = gxu.dict_from_reg(reg)
        for key, value in d.items():
            self.assertEqual(value, dd[key])
        self.assertRaises(gxu.UtilityException, gxu.reg_from_dict, d, max_size=10)

    def test_parameters(self):
        self.start(gsys.func_name())

        p = {'a': 'string', 'list': [1,2,3], 'tup': (['a','b'], {'q': 1.5})}
        gxu.save_parameters('param_test', p)
        r = gxu.get_parameters('param_test')
        self.assertEqual(r['A'], p['a'])
        self.assertEqual(r['LIST'], p['list'])
        self.assertEqual(r['TUP'][0][1], 'b')
        self.assertEqual(r['TUP'][1]['q'], 1.5)

        s = gxu.get_parameters('param_test', ['a', 'tup', 'not_there'])
        self.assertEqual(s['A'], 'string')
        self.assertEqual(s['TUP'][1]['q'], 1.5)
        self.assertEqual(s.get('NOT_THERE', None), None)

        q = gxu.get_parameters('param_test', ['not_there'], default="yes I am")
        self.assertEqual(q['NOT_THERE'], "yes I am")

        t = {'1': '\\', '2': '\\\\', '3': '\\\\\\', '4': '\\\\\\\\', '5': '\\\\\\\\\\'}
        gxu.save_parameters('escape', t)
        tt = gxu.get_parameters('escape')
        self.assertEqual(t, tt)

    def test_rdecode(self):
        self.start(gsys.func_name())

        cDUMMY="*"
        rDUMMY=gxu.rdecode(cDUMMY)
        
        def test(s):
            r = gxu.rdecode(s)
            return r
            
        self.assertEqual(test("1.9"),1.9)
        self.assertEqual(test("1.o9"),1.09)
        self.assertEqual(test(""),rDUMMY)
        self.assertEqual(test("*"),rDUMMY)
        self.assertEqual(test("*ab"),rDUMMY)
        self.assertEqual(test("\t"),rDUMMY)
        self.assertEqual(test("    \t   \t"),rDUMMY)
        self.assertEqual(test("\t             000oooOOO45.o0o0   \t\t"),45)
        self.assertEqual(test("62"),62)
        self.assertEqual(test("62S"),-62)
        self.assertEqual(test("62 00 00N"),62)
        self.assertEqual(test("-62 00 00"),-62)
        self.assertEqual(test("62.00.00S"),-62)
        self.assertEqual(test("62N"),62)
        self.assertEqual(test("62 45S"),-62.75)
        self.assertEqual(test("62 29 60w"),-62.5)
        self.assertEqual(test("62 29 60.00E"),62.5)
        self.assertEqual(test("-62 29 60.00E"),-62.5)
        self.assertEqual(test("62.45.0.00s"),-62.75)
        self.assertEqual(test("62.30.30.15W"),-62.508375)
        self.assertEqual(test("-62.30.30.15"),-62.508375)
        self.assertEqual(test("-62.30.30.15W"),62.508375)
        self.assertEqual(test("13:14:60.00"),13.25)
        self.assertEqual(test("13:14:60.00pm"),25.25)
        self.assertEqual(test("13:15"),13.25)
        self.assertEqual(test("2:15PM"),14.25)
        self.assertEqual(test("2:90pm"),15.5)
        self.assertEqual(test("\to o o   "),0.0)
        self.assertEqual(test("\to 59 6O   "),1.0)
        self.assertEqual(test("bogus"),rDUMMY)
        self.assertEqual(test("2014-01-01"),2014.0)
        self.assertEqual(test("2014-02-25"),2014.150684931507)
        self.assertEqual(test("2014/02/25"),2014.150684931507)
        self.assertEqual(test("2014/2/25"),2014.150684931507)
        self.assertEqual(test("2014/02/5"),2014.0958904109589)
        self.assertEqual(test("2014/12/31"),2014.9972602739726)
        self.assertEqual(test("2016/12/31"),2016.9972677595629)
        self.assertEqual(test("2017-1-1"),2017.0)

        try:
            gxu.rdecode_err("bogus")
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
        try:
            gxu.rdecode_err("\t0 o 0 0")
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_decode(self):
        self.start(gsys.func_name())

        cDUMMY="*"
        rDUMMY=gxapi.GS_R8DM
        iDUMMY=gxu.decode(cDUMMY,'i')

        def test(s,f):
            r = gxu.decode(s,f)
            return r

        self.assertEqual(test("1.9",'f8'),1.9)
        self.assertEqual(test("*",'f'),rDUMMY)
        self.assertEqual(test("*",'f4'),rDUMMY)
        self.assertEqual(test("*",'f8'),rDUMMY)
        self.assertEqual(test("*",'i'),iDUMMY)
        self.assertEqual(test("*",'i2'),iDUMMY)
        self.assertEqual(test("*",'i4'),iDUMMY)
        self.assertEqual(test("*",'i8'),iDUMMY)
        self.assertEqual(test("*",'i8'),iDUMMY)
        self.assertEqual(test("62N",'i'),62)
        self.assertEqual(test("62",'f'),62.0)
        self.assertEqual(test("62.500001",'i'),63.0)
        self.assertEqual(test("-62.500001",'i'),-63.0)
        self.assertEqual(test("62.4999",'i'),62)
        self.assertEqual(test("-62.4999",'i'),-62)
        self.assertEqual(test("-62.4999",'i2'),-62)
        self.assertEqual(test("-62.4999",'i4'),-62)
        self.assertEqual(test("-62.4999",'i8'),-62)
        self.assertEqual(test("62.4999",'u'),62)
        self.assertEqual(test("62.4999",'b'),True)
        self.assertEqual(test("0",'b'),False)
        self.assertEqual(test("0.0",'b'),False)
        self.assertEqual(test("*",'b'),False)
        self.assertEqual(test("62N",'U5'),"62N")
        self.assertEqual(test("62Nabcdef",'U3'),"62N")
        self.assertEqual(test("62N12345",'U5'),"62N12")
        self.assertEqual(test("62N12345",'S5'),"62N12")
        self.assertEqual(test("62N12345",'a5'),"62N12")

    def test_shared_dict(self):
        self.start(gsys.func_name())

        gxu.set_shared_dict()
        d = gxu.get_shared_dict()
        self.assertEqual(len(d), 0)

        gxu.set_shared_dict({'a':0, 'b':[1,2,3]})
        d = gxu.get_shared_dict()
        self.assertEqual(d['a'], 0)
        self.assertEqual(d['b'][2], 3)

        d = gxu.get_shared_dict()
        self.assertEqual(len(d), 0)

    def test_run_external_python(self):
        self.start(gsys.func_name())

        testpy = os.path.join(os.getcwd(),'test_python.py')
        with open(testpy, 'w') as py:
            py.write("import sys\n")
            py.write("import geosoft.gxpy as gxpy\n")
            py.write("import geosoft.gxpy.utility as gxu\n")
            py.write("gxc = gxpy.gx.GXpy()\n")
            py.write("d = gxu.get_shared_dict()\n")
            py.write("gxpy.utility.set_shared_dict({'a':'letter a', 'b':'letter b', 'c':[1,2,3], 'argv': sys.argv, 'in_dict':d})\n")
            #py.write("input('RUN_EXTERNAL! Press return to continue...')\n")

        test_result = gxu.run_external_python(testpy,
                                              script_args='test1 test2',
                                              dict={'howdy':'hey there'},
                                              console=False)
        os.remove(testpy)
        self.assertEqual(test_result['a'], 'letter a')
        l = test_result['c']
        self.assertEqual(len(l), 3)
        self.assertEqual(l[1], 2)
        self.assertEqual(test_result['argv'][1], 'test1')
        self.assertEqual(test_result['argv'][2], 'test2')
        self.assertEqual(test_result['in_dict']['howdy'], 'hey there')

        try:
            gxu.run_external_python(testpy, script_args='test1 test2')
            self.assertTrue(False)
        except gxu.UtilityException:
            pass
        except:
            raise

    def test_run_external_bad_python(self):
        self.start(gsys.func_name())

        testpy = os.path.join(os.getcwd(), 'test_python.py')
        with open(testpy, 'w') as py:
            py.write("import this_module_not_there\n")

        try:
            gxu.run_external_python(testpy, script_args='test1 test2')
            self.assertTrue(False)
        except gxu.UtilityException as e:
            self.assertTrue('External python error' in str(e))
        except:
            os.remove(testpy)
            raise
        finally:
            os.remove(testpy)

    def test_paths(self):
        self.start(gsys.func_name())

        local = gxu.folder_workspace()
        self.assertEqual(os.path.normpath(local), os.getcwd())
        user = gxu.folder_user()
        self.assertTrue(os.path.isdir(user))
        temp = gxu.folder_temp()
        self.assertTrue(os.path.isdir(temp))

    def test_display_message(self):
        self.start(gsys.func_name())

        gxu.display_message('test title', 'test message')

    def test_version(self):
        self.start(gsys.func_name())

        with self.assertRaises(ValueError):
            gxu.check_version("x.y.z")

        version_backup = gxu.__version__
        try:
            gxu.__version__ = "9.1"
        
            self.assertTrue(gxu.check_version("8.5.9"))
            self.assertTrue(gxu.check_version("9.0"))
            self.assertTrue(gxu.check_version("9.1"))
            self.assertTrue(gxu.check_version("9.1.0"))
            self.assertTrue(gxu.check_version("9.1a0"))
            self.assertTrue(gxu.check_version("9.1b0"))
            self.assertTrue(gxu.check_version("9.1a1"))
            self.assertTrue(gxu.check_version("9.1b1"))

            with self.assertRaises(gxu.UtilityException):
                gxu.check_version("9.1.1")
            with self.assertRaises(gxu.UtilityException):
                gxu.check_version("9.2")
            with self.assertRaises(gxu.UtilityException):
                gxu.check_version("999.999")

            self.assertFalse(gxu.check_version("9.1.1", raise_on_fail=False)) 
            self.assertFalse(gxu.check_version("9.2", raise_on_fail=False)) 
            self.assertFalse(gxu.check_version("999.999", raise_on_fail=False))

            gxu.__version__ = "9.1a1"

            self.assertTrue(gxu.check_version("9.0"))
            self.assertTrue(gxu.check_version("9.0a0"))
            self.assertFalse(gxu.check_version("9.1", raise_on_fail=False)) 
        finally:
            gxu.__version__ = version_backup

    def test_datetime(self):
        self.start(gsys.func_name())

        geo_utc = gxu.datetime_from_year(gxapi.GXSYS.utc_date())

        # Due to testing environment variables the above would always be 2003-01-01
        py_utc = datetime(2003, 1, 1, tzinfo=timezone.utc)

        self.assertEqual(geo_utc.year, py_utc.year)
        self.assertEqual(geo_utc.month, py_utc.month)
        self.assertEqual(geo_utc.day, py_utc.day)
        self.assertEqual(geo_utc.hour, 0)
        self.assertEqual(geo_utc.minute, 0)
        self.assertEqual(geo_utc.second, 0)
        self.assertEqual(geo_utc.microsecond, 0)

        dec_year = gxu.year_from_datetime(py_utc)
        dt = gxu.datetime_from_year(dec_year)
        self.assertEqual(dt.year, py_utc.year)
        self.assertEqual(dt.month, py_utc.month)
        self.assertEqual(dt.day, py_utc.day)
        self.assertEqual(dt.hour, py_utc.hour)
        self.assertEqual(dt.minute, py_utc.minute)
        self.assertEqual(dt.second, py_utc.second)
        self.assertEqual(dt.microsecond, round(py_utc.microsecond / 1000.0) * 1000)

    def test_crc(self):
        self.start(gsys.func_name())

        self.assertEqual(gxu.crc32(b'bunch of bytes'), 3271364337)
        self.assertEqual(gxu.crc32_str('a string'), 2577552858)


if __name__ == '__main__':

    unittest.main()
