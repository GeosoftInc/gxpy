import unittest

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.dataframe as gxdf

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gxp = gx.GXpy(log=print)

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def start(cls,test):
        cls.gxp.log("*** {} *** - {}".format(test, geosoft.__version__))

    def test_df(self):
        self.start(gsys.func_name())

        self.assertEqual(gxdf.__version__, geosoft.__version__)

        with gxdf.GXdf(initial='maptmpl') as df:
            #self.gxp.log(df)
            self.assertTrue(len(df) > 0)
            self.assertTrue('LAYOUT' in df.columns)
            self.assertTrue('UP_ANG' in df.columns)
            self.assertTrue('Unlimited figure' in df.index)
            self.assertEqual(df.loc['portrait C', 'MARGIN_LEFT'], '3')

        with gxdf.GXdf(initial='datumtrf', records="*Cape to WGS 84 (3*)") as df:
            self.assertEqual(len(df), 1)
            self.assertEqual(df.loc['*Cape to WGS 84 (3*)', 'DX'], '-138')

        with gxdf.GXdf(initial='datumtrf', records=("*Cape to WGS 84 (3*)","Tete to WGS 84 (6)")) as df:
            self.assertEqual(len(df), 2)
            self.assertEqual(df.loc['*Cape to WGS 84 (3*)', 'DX'], '-138')
            self.assertEqual(df.loc['Tete to WGS 84 (6)', 'CODE'], '6901')

        with gxdf.GXdf(initial='datumtrf', columns="DX") as df:
            self.assertEqual(len(df), 959)
            self.assertEqual(len(df.columns), 1)
            self.assertEqual(df.loc['*Cape to WGS 84 (3*)', 'DX'], '-138')

        with gxdf.GXdf(initial='datumtrf', columns=["DX", "DZ"]) as df:
            self.assertEqual(len(df), 959)
            self.assertEqual(len(df.columns), 2)
            self.assertEqual(df.loc['*Cape to WGS 84 (3*)', 'DX'], '-138')
            self.assertEqual(df.loc['*Cape to WGS 84 (3*)', 'DZ'], '-289')


        with gxdf.GXdf(initial='datumtrf',
                       columns=("DX", "DZ", "CODE"),
                       records=("*Cape to WGS 84 (3*)","Tete to WGS 84 (6)")) as df:
            self.assertEqual(len(df), 2)
            self.assertEqual(len(df.columns), 3)
            self.assertEqual(df.loc['*Cape to WGS 84 (3*)', 'DX'], '-138')
            self.assertEqual(df.loc['*Cape to WGS 84 (3*)', 'DZ'], '-289')
            self.assertEqual(df.loc['Tete to WGS 84 (6)', 'CODE'], '6901')

    def test_raises(self):
        self.start(gsys.func_name())

        self.assertRaises(gxdf.DfException, gxdf.GXdf, initial='bogus')
        self.assertRaises(gxdf.DfException, gxdf.GXdf, initial='datumtrf', columns="NOT_THERE")
        self.assertRaises(gxdf.DfException, gxdf.GXdf, initial='datumtrf', records="NOT_THERE")


    def test_dict(self):
        self.start(gsys.func_name())

        m = gxdf.table_record('media', 'Unlimited')
        self.assertEqual(m['SIZE_X'], '300')
        self.assertEqual(gxdf.table_record('maptmpl', 'portrait A4')['MEDIA'], 'A4')
        m = gxdf.table_column('media','FULLSIZE_Y')
        self.assertEqual(m['letter'], '21.59')

        self.assertRaises(gxdf.DfException, gxdf.table_record, 'bogus', 'bogus')
        self.assertRaises(gxdf.DfException, gxdf.table_record, 'maptmpl', 'bogus')
        self.assertRaises(gxdf.DfException, gxdf.table_column, 'maptmpl', 'bogus')

if __name__ == '__main__':

    unittest.main()