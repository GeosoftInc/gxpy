import unittest
import numpy as np
import os

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.system as gsys
import geosoft.gxpy.gx as gx
import geosoft.gxpy.utility as gxu

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gxp = gx.GXpy()

    @classmethod
    def tearDownClass(cls):
        pass
    
    @classmethod
    def start(cls,test):
        print("\n*** {} *** - {}".format(test, geosoft.__version__))

    def test_misc(self):
        self.start(gsys.func_name())

        self.assertEqual(gxu.__version__, geosoft.__version__)

        self.assertEqual(gxu.gxType('float'),gxapi.GS_DOUBLE)
        self.assertEqual(gxu.gxType('int'),gxapi.GS_LONG)
        self.assertEqual(gxu.gxType("<U18"),-18)
        self.assertEqual(gxu.gxType('uint64'),gxapi.GS_ULONG64)

        self.assertEqual(gxu.dtypeGX(gxapi.GS_DOUBLE), np.float)
        self.assertEqual(gxu.dtypeGX(gxapi.GS_FLOAT), np.float32)
        self.assertEqual(gxu.dtypeGX(gxapi.GS_LONG), np.int32)
        self.assertEqual(gxu.dtypeGX(-2000).str, "<U2000")
        self.assertEqual(gxu.dtypeGX(gxapi.GS_TYPE_DEFAULT), None)
        self.assertEqual(gxu.dtypeGX(gxapi.GS_ULONG64), np.uint64)

        self.assertEqual(gxu.gxDummy(np.float),gxapi.rDUMMY)
        self.assertEqual(gxu.gxDummy(np.int64),gxapi.iDUMMY)
        self.assertEqual(gxu.gxDummy("<U1000"),'*')

        npd = np.array([[1,1],[2,2],[-127,1],[3,3]],dtype=gxu.dtypeGX(gxapi.GS_BYTE))
        self.assertEqual(list(gxu.dummyMask(npd)),[False,False,True,False])

        npd = np.array([1,2,3,4],dtype=gxu.dtypeGX(gxapi.GS_BYTE))
        try:
            gxu.dummyMask(npd)
            self.assertTrue(False)
        except: pass

    def test_dictFromList(self):
        self.start(gsys.func_name())

        lst = gxapi.GXLST.create(1000)
        lst.add_item("a","aa")
        lst.add_item("b","bb")
        lst.add_item("c","cc")
        d = gxu.dictFromLst(lst)
        self.assertEqual(len(d),lst.size())
        self.assertEqual(d.get('b'),'bb')

    def test_rdecode(self):
        self.start(gsys.func_name())

        cDUMMY="*"
        rDUMMY=gxu.rdecode(cDUMMY)
        
        def test(s):
            r = gxu.rdecode(s)
            print('\'{}\' -> {}'.format(s,r))
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
            print('\'{},{}\' -> {}'.format(s,f,r))
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
            py.write("gxpy.utility.set_shared_dict({'a':'letter a', 'b':'letter b', 'c':[1,2,3], 'argv': sys.argv, 'input':d})\n")
            #py.write("input('RUN_EXTERNAL! Press return to continue...')\n")

        test_result = gxu.run_external_python(testpy, script_args='test1 test2', dict={'howdy':'hey there'}, console=False)
        self.assertEqual(test_result['a'], 'letter a')
        l = test_result['c']
        self.assertEqual(len(l), 3)
        self.assertEqual(l[1], 2)
        self.assertEqual(test_result['argv'][1], 'test1')
        self.assertEqual(test_result['argv'][2], 'test2')
        self.assertEqual(test_result['input']['howdy'], 'hey there')
        os.remove(testpy)

        try:
            gxu.run_external_python(testpy, script_args='test1 test2')
            self.assertTrue(False)
        except gxu.UtilityException:
            pass
        except:
            raise

    def test_paths(self):
        self.start(gsys.func_name())

        local = gxu.project_path()
        self.assertEqual(os.path.normpath(local), os.getcwd())
        user = gxu.user_path()
        self.assertTrue(os.path.isdir(user))
        temp = gxu.temp_path()
        self.assertTrue(os.path.isdir(temp))

###############################################################################################

if __name__ == '__main__':

    unittest.main()
