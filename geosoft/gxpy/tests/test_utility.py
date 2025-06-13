#  Copyright (c) 2025 Bentley Systems, Incorporated. All rights reserved.
import unittest
import numpy as np
import os
import datetime
import time
import requests
from datetime import timezone, datetime

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.utility as gxu

from base import GXPYTest


class Test(GXPYTest):
    def test_misc(self):
        self.start()

        self.assertEqual(gxu.__version__, geosoft.__version__)

        self.assertEqual(gxu.gx_dtype('float'),gxapi.GS_DOUBLE)
        self.assertEqual(gxu.gx_dtype('int'),gxapi.GS_LONG)
        self.assertEqual(gxu.gx_dtype("<U18"),-72) # x4 for full range of UTF-8 characters
        self.assertEqual(gxu.gx_dtype('uint64'),gxapi.GS_ULONG64)

        self.assertEqual(gxu.dtype_gx(gxapi.GS_DOUBLE), np.float64)
        self.assertEqual(gxu.dtype_gx(gxapi.GS_FLOAT), np.float32)
        self.assertEqual(gxu.dtype_gx(gxapi.GS_LONG), np.int32)
        self.assertEqual(gxu.dtype_gx(-2000).str, "<U2000")
        self.assertEqual(gxu.dtype_gx(gxapi.GS_ULONG64), np.uint64)

        self.assertEqual(gxu.gx_dummy(np.float64),gxapi.rDUMMY)
        self.assertEqual(gxu.gx_dummy(np.int32),gxapi.iDUMMY)
        self.assertEqual(gxu.gx_dummy(np.int64),gxapi.GS_S8DM)
        self.assertEqual(gxu.gx_dummy(np.str_), '')
        self.assertEqual(gxu.gx_dummy('U48'), '')

        self.assertEqual(gxu.gx_dummy(np.uint), gxapi.GS_U4DM)
        self.assertEqual(gxu.gx_dummy(np.uint8), gxapi.GS_U1DM)
        self.assertEqual(gxu.gx_dummy(np.uint16), gxapi.GS_U2DM)
        self.assertEqual(gxu.gx_dummy(np.uint32), gxapi.GS_U4DM)
        self.assertEqual(gxu.gx_dummy(np.uint64), gxapi.GS_U8DM)

        self.assertEqual(gxu.gx_dummy(1.5),gxapi.rDUMMY)
        self.assertEqual(gxu.gx_dummy(type(1.5)), gxapi.rDUMMY)
        self.assertEqual(gxu.gx_dummy(3),gxapi.iDUMMY)
        self.assertEqual(gxu.gx_dummy(type(3)), gxapi.iDUMMY)
        self.assertEqual(gxu.gx_dummy(0xff),gxapi.iDUMMY)
        self.assertEqual(gxu.gx_dummy('string'), '')
        self.assertEqual(gxu.gx_dummy('U48'), '')
        self.assertRaises(KeyError, gxu.gx_dummy, 1j)
        self.assertRaises(KeyError, gxu.gx_dummy, type(1j))

        self.assertEqual(gxu.dummy_none(0), 0)
        self.assertEqual(gxu.dummy_none(1.), 1.)
        self.assertEqual(gxu.dummy_none(gxapi.iDUMMY), None)
        self.assertEqual(gxu.dummy_none(gxapi.rDUMMY), None)

        self.assertTrue(gxu.is_float(gxu.gx_dtype('float')))
        self.assertFalse(gxu.is_int(gxu.gx_dtype('float')))
        self.assertTrue(gxu.is_int(gxu.gx_dtype('uint64')))
        self.assertFalse(gxu.is_float(gxu.gx_dtype('uint64')))
        self.assertTrue(gxu.is_string(gxu.gx_dtype('U18')))
        self.assertFalse(gxu.is_int(gxu.gx_dtype('U18')))
        self.assertFalse(gxu.is_float(gxu.gx_dtype('U18')))
        self.assertEqual(gxu.is_string(gxu.gx_dtype('U18')), 72)

        self.assertEqual(gxu.dtype_gx_dimension(gxapi.GS_FLOAT), (np.float32, 1))
        self.assertEqual(gxu.dtype_gx_dimension(gxapi.GS_FLOAT2D), (np.float32, 2))
        self.assertEqual(gxu.dtype_gx_dimension(gxapi.GS_FLOAT3D), (np.float32, 3))
        self.assertEqual(gxu.dtype_gx_dimension(gxapi.GS_DOUBLE), (np.float64, 1))
        self.assertEqual(gxu.dtype_gx_dimension(gxapi.GS_DOUBLE2D), (np.float64, 2))
        self.assertEqual(gxu.dtype_gx_dimension(gxapi.GS_DOUBLE3D), (np.float64, 3))

        self.assertEqual(gxu.gx_dtype_dimension(np.float32), gxapi.GS_FLOAT)
        self.assertEqual(gxu.gx_dtype_dimension(np.float32, 1), gxapi.GS_FLOAT)
        self.assertEqual(gxu.gx_dtype_dimension(np.float32, 2), gxapi.GS_FLOAT2D)
        self.assertEqual(gxu.gx_dtype_dimension(np.float32, 3), gxapi.GS_FLOAT3D)
        self.assertEqual(gxu.gx_dtype_dimension(np.float64), gxapi.GS_DOUBLE)
        self.assertEqual(gxu.gx_dtype_dimension(np.float64, 1), gxapi.GS_DOUBLE)
        self.assertEqual(gxu.gx_dtype_dimension(np.float64, 2), gxapi.GS_DOUBLE2D)
        self.assertEqual(gxu.gx_dtype_dimension(np.float64, 3), gxapi.GS_DOUBLE3D)

        self.assertRaises(gxu.UtilityException, gxu.gx_dtype_dimension, np.int_, 2)
        self.assertRaises(gxu.UtilityException, gxu.gx_dtype_dimension, np.int_, 3)
        self.assertRaises(gxu.UtilityException, gxu.gx_dtype_dimension, np.float32, 4)

        npd = np.array([[1,1],[2,2],[-127,1],[3,3]],dtype=gxu.dtype_gx(gxapi.GS_BYTE))
        self.assertEqual(list(gxu.dummy_mask(npd)),[False,False,True,False])

        npd = np.array([1,2,3,4],dtype=gxu.dtype_gx(gxapi.GS_BYTE))
        try:
            gxu.dummy_mask(npd)
            self.assertTrue(False)
        except: pass

    def test_dictlist(self):
        self.start()

        lst = gxapi.GXLST.create(1000)
        lst.add_item("a","aa")
        lst.add_item("b","bb")
        lst.add_item("c","cc")
        d = gxu.dict_from_lst(lst)
        self.assertEqual(len(d),lst.size())
        self.assertEqual(d.get('b'),'bb')

    def test_dictreg(self):
        self.start()

        d = {'a':'A', 'b':'BEE', 'c':[1,2,3], 'g':7.123, 'h':{'hh':'name'}}
        reg = gxu.reg_from_dict(d)
        dd = gxu.dict_from_reg(reg)
        for key, value in d.items():
            self.assertEqual(value, dd[key])
        self.assertRaises(gxu.UtilityException, gxu.reg_from_dict, d, max_size=10)

    def test_parameters(self):
        self.start()

        p = {'a': 'string', 'list': [1,2,3], 'tup': (['a','b'], {'q': 1.5})}
        gxu.save_parameters('param_test', p)
        r = gxu.get_parameters('param_test')
        self.assertEqual(r['A'], p['a'])
        self.assertEqual(r['LIST'], p['list'])
        self.assertEqual(r['TUP'][0][1], 'b')
        self.assertEqual(r['TUP'][1]['q'], 1.5)

        s = gxu.get_parameters('param_test', ['a', 'tup', 'not_there'])
        self.assertEqual(s['a'], 'string')
        self.assertEqual(s['tup'][1]['q'], 1.5)
        self.assertEqual(s.get('not_there', None), None)

        q = gxu.get_parameters('param_test', ['not_there'], default="yes I am")
        self.assertEqual(q['not_there'], "yes I am")

        t = {'1': '\\', '2': '\\\\', '3': '\\\\\\', '4': '\\\\\\\\', '5': '\\\\\\\\\\'}
        gxu.save_parameters('escape', t)
        tt = gxu.get_parameters('escape')
        self.assertEqual(t, tt)

    def test_parameters_2(self):
        self.start()

        self.assertRaises(gxu.UtilityException, gxu.save_parameters)
        self.assertRaises(gxu.UtilityException, gxu.save_parameters, self._test_case_filename)
        group = os.path.basename(self._test_case_filename).split('.')[0]
        self.assertRaises(gxu.UtilityException, gxu.save_parameters, group, {'bad.parameter': ''})

        parameter = 'GRID_NAME'
        p = {parameter: ''}
        gxu.save_parameters(group, p)
        r = gxu.get_parameters(group)
        self.assertEqual(r[parameter], '')

        r = gxu.get_parameters(group, {parameter: 'bogus'})
        self.assertEqual(r[parameter], '')
        r = gxu.get_parameters(group, {'test': 'bogus'})
        self.assertEqual(r['test'], 'bogus')

        r = gxu.get_parameters(group, (parameter, 'test1', 'test2'))
        self.assertEqual(r[parameter], '')
        self.assertEqual(r['test1'], None)
        self.assertEqual(r['test2'], None)

        r = gxu.get_parameters(group, (parameter, 'test1', 'test2'), 99)
        self.assertEqual(r[parameter], '')
        self.assertEqual(r['test1'], 99)
        self.assertEqual(r['test2'], 99)

        gxu.save_parameters(group, r)
        r = gxu.get_parameters(group)
        self.assertEqual(r[parameter], '')
        self.assertEqual(r['TEST1'], 99)
        self.assertEqual(r['TEST2'], 99)

        gxu.save_parameters(parms={'test_file': '.\\some_file', 't2': 'c:\\abc\\def'})
        r = gxu.get_parameters()
        self.assertEqual(r['TEST_FILE'], '.\\some_file')
        self.assertEqual(r['T2'], 'c:\\abc\\def')


    def test_rdecode(self):
        self.start()

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
        self.start()

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
        self.start()

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
        self.start()

        testpy = os.path.join(os.getcwd(),'test_python.py')
        with open(testpy, 'w') as py:
            py.write("import sys\n")
            py.write("import geosoft.gxpy as gxpy\n")
            py.write("import geosoft.gxpy.utility as gxu\n")
            py.write("with gxpy.gx.GXpy() as gxc:\n")
            py.write("    d = gxu.get_shared_dict()\n")
            py.write("    gxpy.utility.set_shared_dict({'a':'letter a', 'b':'letter b', 'c':[1,2,3], 'argv': sys.argv, 'in_dict':d})\n")
            #py.write("input('RUN_EXTERNAL! Press return to continue...')\n")

        try:
            test_result = gxu.run_external_python(testpy,
                                                  script_args='test1 test2',
                                                  shared_dict={'howdy':'hey there'},
                                                  console=False)
            self.assertEqual(test_result['a'], 'letter a')
            l = test_result['c']
            self.assertEqual(len(l), 3)
            self.assertEqual(l[1], 2)
            self.assertEqual(test_result['argv'][1], 'test1')
            self.assertEqual(test_result['argv'][2], 'test2')
            self.assertEqual(test_result['in_dict']['howdy'], 'hey there')

        finally:
            gxu.delete_file(testpy)

        self.assertRaises(gxu.UtilityException, gxu.run_external_python, testpy, 'test1 test2')


    def test_run_external_bad_python(self):
        self.start()

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
        self.start()

        local = gxu.folder_workspace()
        self.assertEqual(os.path.normpath(local), os.getcwd())
        user = gxu.folder_user()
        self.assertTrue(os.path.isdir(user))
        temp = gxu.folder_temp()
        self.assertTrue(os.path.isdir(temp))

    def test_display_message(self):
        self.start()
        gxu.display_message('test title', 'test message')

    def test_version(self):
        self.start()

        with self.assertRaises(gxu.UtilityException):
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
                gxu.check_version("9.2.0b")
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
        self.start()

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
        self.start()

        self.assertEqual(gxu.crc32(b'bunch of bytes'), 3271364337)
        self.assertEqual(gxu.crc32_str('a string'), 2577552858)

    def test_sig_fig(self):
        self.start()

        self.assertEqual(gxu.str_significant(1.0, 1), '1')
        self.assertEqual(gxu.str_significant(-1.0, 1), '-1')
        self.assertEqual(gxu.str_significant(105.1005, 2), '110')
        self.assertEqual(gxu.str_significant(-105.0, 2), '-100')
        self.assertEqual(gxu.str_significant(-105.0001000, 2), '-110')
        self.assertEqual(gxu.str_significant(105.0, 2, mode=-1), '100')
        self.assertEqual(gxu.str_significant(-105.0, 2, mode=-1), '-100')

        self.assertEqual(gxu.str_significant(0.000456789123, 3), '0.000457')
        self.assertEqual(gxu.str_significant(-0.000456789123, 3), '-0.000457')
        self.assertEqual(gxu.str_significant(0.000456789123, 3, 1), '0.000457')
        self.assertEqual(gxu.str_significant(0.000456789123, 3, -1), '0.000456')
        self.assertEqual(gxu.str_significant(-0.000456789123, 3, -1), '-0.000456')
        self.assertEqual(gxu.str_significant(4567800000.0, 3), '4570000000')
        self.assertEqual(gxu.str_significant(4567800000.0, 3, 1), '4570000000')
        self.assertEqual(gxu.str_significant(4567800000.0, 3, -1), '4560000000')

        self.assertEqual(gxu.str_significant(0.00045, 3), '0.00045')
        self.assertEqual(gxu.str_significant(4500000000.0, 3), '4500000000')
        self.assertEqual(gxu.str_significant(0.000451, 1), '0.0005')
        self.assertEqual(gxu.str_significant(4510000000.0, 1), '5000000000')
        self.assertEqual(gxu.str_significant(0.000451, 1, -1), '0.0004')
        self.assertEqual(gxu.str_significant(4510000000.0, 1, -1), '4000000000')

    def test_xml(self):
        self.start()

        d = {'my_root':{'a':1, 'b':'text_string', 'c':(1, 2), 'd':[1, 2, 'txt']},
             'more':{'a':1, 'b':'text_string', 'c':(1, 2), 'd':[1, 2, 'txt']}}
        xml = gxu.xml_from_dict(d, pretty=True)
        dxml = gxu.dict_from_xml(xml)

        self.assertEqual(len(dxml), 2)
        self.assertTrue('my_root' in dxml)
        self.assertEqual(dxml['my_root']['b'], 'text_string')
        self.assertEqual(dxml['my_root']['c'], ['1', '2'])
        self.assertEqual(dxml['my_root']['d'], ['1', '2', 'txt'])
        self.assertEqual(dxml['more']['b'], 'text_string')
        self.assertEqual(dxml['more']['c'], ['1', '2'])
        self.assertEqual(dxml['more']['d'], ['1', '2', 'txt'])

        xml = '<?xml version="1.0" encoding="UTF-8"?>\
                <gmd:MD_Metadata xsi:schemaLocation="http://www.isotc211.org/2005/gmd ../schemas/iso19139fra/gmd/gmd.xsd">\
                    <geosoft xmlns="http://www.geosoft.com/schema/geo">\
                        <dataset version="1" beta="abc">\
                            <title>test_grid_1</title>\
                            <file_format>Geosoft Grid</file_format>\
                        </dataset>\
                    </geosoft>\
                </gmd:MD_Metadata>'
        d = gxu.dict_from_xml(xml)
        self.assertEqual(d['gmd:MD_Metadata']['geosoft']['dataset']['@version'], "1")
        xml = gxu.xml_from_dict(d, pretty=True)
        self.assertTrue('<dataset ' in xml)

        d = {'geosoft': d['gmd:MD_Metadata']['geosoft']}
        d['geosoft'].pop('@xmlns', None)
        xml = gxu.xml_from_dict(d, pretty=True)
        self.assertFalse('xmlns=' in xml)
        xml = gxu.geosoft_xml_from_dict(d, pretty=True)
        self.assertTrue('xmlns=' in xml)
        xml = gxu.geosoft_xml_from_dict(d['geosoft'], pretty=True)
        self.assertTrue('<geosoft xmlns=' in xml)

        folder, files = gsys.unzip(os.path.join(os.path.dirname(self._test_case_py), 'testgrids.zip'),
                                   folder=gx.gx().temp_folder())
        gxml = os.path.join(folder, 'test_grid_1.grd.xml')
        with open(gxml) as f:
            m = gxu.dict_from_xml(f.read())
        xml = gxu.xml_from_dict(m, pretty=True)
        m2 = gxu.dict_from_xml(xml)
        self.assertEqual(m2['gmd:MD_Metadata']['idinfo']['status']['update'], 'None planned')

    def test_url_retrieve(self):
        self.start

        def del_file(f):
            try:
                os.remove(f)
            except:
                pass

        def hook(a, b, c):
            print(a, b, c)

        url = 'https://github.com/GeosoftInc/gxpy/raw/master/README.md'
        big = 'https://github.com/GeosoftInc/gxpy/raw/master/examples/tutorial/2D%20Views%20and%20Maps/Wittichica Creek Residual Total Field.grd'
        ref_file = 'README.md'
        test_file = 'test.grd'

        try:

            file_name = gxu.url_retrieve(url)
            self.assertEqual(file_name, ref_file)

            file_name = gxu.url_retrieve(url, test_file)
            self.assertEqual(file_name, test_file)

            file_name = gxu.url_retrieve(big, reporthook=hook)
            del_file(file_name)

        except:
            print('No internet')
            pass

        finally:
            del_file(ref_file)
            del_file(test_file)

    def test_unique_name(self):
        self.start()

        def exists(name):
            if name in ('ab', 'ab(1)', 'ab(2)', 'ab.txt', 'ab(1).txt'):
                return True
            if name in ('ab', 'ab_1', 'ab_2', 'ab.txt', 'ab_1.txt'):
                return True
            if name in ('ab(special).txt',):
                return True
            if name in ('ab(special.txt', 'ab(maki_.txt','ab(maki_3.txt'):
                return True
            return False

        def true(name):
            return True

        self.assertEqual(gxu.unique_name('c:/temp/billybob', exists), 'c:/temp/billybob')
        self.assertEqual(gxu.unique_name('ab', exists), 'ab(3)')
        self.assertEqual(gxu.unique_name('ab.txt', exists), 'ab(2).txt')
        self.assertEqual(gxu.unique_name('ab', exists, separator='_'), 'ab_3')
        self.assertEqual(gxu.unique_name('ab.txt', exists, separator='_'), 'ab_2.txt')
        self.assertEqual(gxu.unique_name('ab(special).txt', exists), 'ab(special)(1).txt')
        self.assertEqual(gxu.unique_name('ab(special.txt', exists), 'ab(special(1).txt')
        self.assertEqual(gxu.unique_name('ab(special_.txt', exists, separator='_'), 'ab(special_.txt')
        self.assertEqual(gxu.unique_name('ab(maki_.txt', exists, separator='_'), 'ab(maki__1.txt')
        self.assertEqual(gxu.unique_name('ab(maki_3.txt', exists, separator='_'), 'ab(maki_4.txt')
        self.assertRaises(gxu.UtilityException, gxu.unique_name, 'anything', true, '()', 10)

        with open('test(2).txt', 'w+') as f:
            f.write('stuff')
        self.assertEqual(gxu.unique_name('test(2).txt'), 'test(3).txt')
        os.remove('test(2).txt')

    def test_vec_norm(self):
        self.start()

        a = np.array(range(24))
        self.assertEqual(gxu.vector_normalize(a).shape, (1,))
        self.assertEqual(gxu.vector_normalize(a).sum(), 1.)
        a = a.reshape((6, 4))
        self.assertEqual(gxu.vector_normalize(a).shape, (6, 4))
        self.assertAlmostEqual(gxu.vector_normalize(a).sum(), 11.536183542606089)
        a = a.reshape((3, 2, 4))
        self.assertEqual(gxu.vector_normalize(a).shape, (3, 2, 4))
        self.assertAlmostEqual(gxu.vector_normalize(a).sum(), 11.536183542606089)
        a[1, 1, :] = [0, 0, 0, 0]
        self.assertTrue(np.isnan(gxu.vector_normalize(a).sum()))
        self.assertAlmostEqual(np.nansum(gxu.vector_normalize(a)), 9.5430071721870711)

    def test_file_manipulation(self):
        self.start()

        fn = gx.gx().temp_file()
        with open(fn, '+w') as f:
            f.write('maki')
        self.assertFalse(gxu.is_file_locked(fn))
        self.assertFalse(gxu.is_path_locked(fn))
        dir = os.path.dirname(fn)
        self.assertFalse(gxu.is_path_locked(dir))
        self.assertTrue(gxu.is_path_locked(dir, age=1000.*60*60))
        self.assertEqual(gxu.file_age('a completely bogus file name'), -1)
        time.sleep(0.1)
        self.assertTrue(gxu.file_age(fn) > 0.)

    @unittest.skip('HTTP tests are skipped for automated regression')
    def test_http_stuff(self):
        self.start()

        def hook(o):
            return o

        def pairs_hook(o):
            return o

        params = {'key': 'test'}
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        try:
            r = requests.get("http://dap.geosoft.com/rest/service/configuration",
                             params=params,
                             headers=headers)
            response = gxu.dict_from_http_response_text(r.text, object_hook=hook)
            self.assertTrue(response['MajorVersion'] >= 12)
            response = gxu.dict_from_http_response_text(r.text, object_pairs_hook=pairs_hook)
            self.assertEqual(response[0][0], 'Name')

            r = requests.get("http://dap.geosoft.com/rest/service/configuration", params=params)
            response = gxu.dict_from_http_response_text(r.text)
            self.assertTrue(int(response['MajorVersion']) >= 12)
            response = gxu.dict_from_http_response_text(r.text, object_hook=hook)
            self.assertTrue(int(response['MajorVersion']) >= 12)

        except:
            print('No internet')
            pass



if __name__ == '__main__':

    unittest.main()
