import unittest
import os

import geosoft
import geosoft.gxpy as gxpy
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.dataframe as gxdf

from geosoft.gxpy.tests import GXPYTest


class Test(GXPYTest):

    def test_df(self):
        self.start()

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
            self.assertEqual(len(df.columns), 1)
            self.assertEqual(df.loc['*Cape to WGS 84 (3*)', 'DX'], '-138')

        with gxdf.GXdf(initial='datumtrf', columns=["DX", "DZ"]) as df:
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
        self.start()

        self.assertRaises(gxdf.DfException, gxdf.GXdf, initial='bogus')
        self.assertRaises(gxdf.DfException, gxdf.GXdf, initial='datumtrf', columns="NOT_THERE")
        self.assertRaises(gxdf.DfException, gxdf.GXdf, initial='datumtrf', records="NOT_THERE")
        self.assertRaises(gxdf.DfException, gxdf.GXdf, initial='datumtrf', records="")


    def test_dict(self):
        self.start()

        m = gxdf.table_record('media', 'Unlimited')
        self.assertEqual(m['SIZE_X'], '300')
        self.assertEqual(gxdf.table_record('maptmpl', 'portrait A4')['MEDIA'], 'A4')
        m = gxdf.table_column('media','FULLSIZE_Y')
        self.assertEqual(m['letter'], '21.59')

        self.assertRaises(gxdf.DfException, gxdf.table_record, 'bogus', 'bogus')
        self.assertRaises(gxdf.DfException, gxdf.table_record, 'maptmpl', 'bogus')
        self.assertRaises(gxdf.DfException, gxdf.table_column, 'maptmpl', 'bogus')

    def test_doc_sample(self):
        self.start()

        def testraise(index, column):
            df.loc[index, column]

        with open(self.gx.temp_file()+'.csv', 'w') as f:
            rcname = f.name
            f.write('/ standard Geosoft rock codes\n')
            f.write('code,label,__DESCRIPTION,PATTERN,PAT_SIZE,PAT_DENSITY,PAT_THICKNESS,COLOR\n')
            f.write('bau,BAU,BAUXITE,100,,,,RG49B181\n')
            f.write('bif,BIF,"BANDED IRON FM",202,,,,R\n')
            f.write('cal,CAL,CALCRETE,315,,,,B\n')
            f.write('cbt,CBT,CARBONATITE,305,,,,R128G128B192\n')

        with gxpy.dataframe.GXdf(rcname) as df:
            self.assertEqual(len(df), 4)
            self.assertEqual(df.loc['bif', 'DESCRIPTION'], "BANDED IRON FM")
            self.assertEqual(df.loc['bif'][1], "BANDED IRON FM")
            self.assertEqual(df.iloc[1,0], "BIF")
            self.assertEqual(df.loc['cal', 'PATTERN'], "315")
            self.assertRaises(KeyError, testraise, 'cal', 'pattern')

if __name__ == '__main__':

    unittest.main()