import unittest
import numpy as np
import os

import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.coordinate_system as gxcs
import geosoft

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gx = gx.GXpy(log=print)

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def start(cls,test):
        cls.gx.log("*** {} > {}".format(os.path.split(__file__)[1], test))

    def test_cs(self):
        self.start(gsys.func_name())
        self.assertEqual(gxcs.__version__, geosoft.__version__)

    def test_lists_cs(self):
        self.start(gsys.func_name())
        
        #name lists
        dlist = gxcs.name_list(gxcs.LIST_DATUM)
        self.assertTrue('Arc 1950' in dlist)
        dlist = gxcs.name_list(gxcs.LIST_LOCALDATUMNAME)
        self.assertTrue('SIRGAS to WGS 84 (1)' in dlist)
        dlist = gxcs.name_list(gxcs.LIST_COORDINATESYSTEM)
        self.assertTrue('MGI 1901 / Slovenia Grid' in dlist)
        dlist = gxcs.name_list(gxcs.LIST_PROJECTION)
        self.assertTrue('Rectified Skew Orthomorphic Malaya Grid (metres)' in dlist)
        dlist = gxcs.name_list(gxcs.LIST_UNITS,'')
        self.assertTrue('hemisphere degree minute second' in dlist)
        dlist = gxcs.name_list(gxcs.LIST_UNITSDESCRIPTION)
        self.assertTrue('US survey inch' in dlist)
        dlist = gxcs.name_list(gxcs.LIST_LOCALDATUMDESCRIPTION)
        self.assertTrue('[SIRGAS-ROU98] (1m) Uruguay' in dlist)
        dlist = gxcs.name_list(gxcs.LIST_LOCALDATUMDESCRIPTION,'AGD66')
        self.assertTrue('[AGD66] Cocos Is Anna 1 ASTRO 1965' in dlist)
        self.assertTrue(dlist[0][:7],'[AGD66]')

        return

    def test_parameters(self):
        self.start(gsys.func_name())

        # name dictionaries
        pdct = gxcs.parameters(gxcs.PARM_DATUM, 'NAD27')
        self.assertEqual(pdct['ELLIPSOID'], 'Clarke 1866')
        pdct = gxcs.parameters(gxcs.PARM_PROJECTION, 'UTM zone 15N')
        self.assertEqual(pdct['METHOD'], 'Transverse Mercator')
        pdct = gxcs.parameters(gxcs.PARM_UNITS, 'ftUS')
        self.assertEqual(pdct['FACTOR'], '0.304800609601219')
        pdct = gxcs.parameters(gxcs.PARM_LOCAL_DATUM, 'Marshall Islands 1960 to WGS 84 (1)')
        self.assertEqual(pdct['CODE'], '15822')
        pdct = gxcs.parameters(gxcs.PARM_UNITS, 'ftUS')
        self.assertEqual(pdct['FACTOR'], '0.304800609601219')
        self.assertRaises(gxcs.CSException, gxcs.parameters, gxcs.PARM_UNITS, 'bogus')


    def test_any(self):
        self.start(gsys.func_name())

        # name
        with gxcs.GXcs( 'DHDN / Okarito 2000') as cs:
            gxfs = cs.gxf()
            self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
            self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
            self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
            self.assertEqual(gxfs[3],'m,1')
            self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')
            self.assertEqual(cs.name(),'DHDN / Okarito 2000')
            self.assertEqual(cs.name(what=gxcs.NAME),'DHDN / Okarito 2000')
            self.assertEqual(cs.name(what=gxcs.NAME_HCS),'DHDN / Okarito 2000')
            self.assertEqual(cs.name(what=gxcs.NAME_VCS), '')
            self.assertEqual(cs.name(what=gxcs.NAME_HCS_VCS), 'DHDN / Okarito 2000')
            self.assertEqual(cs.name(what=gxcs.NAME_DATUM),'DHDN')
            self.assertEqual(cs.name(what=gxcs.NAME_PROJECTION),'Okarito 2000')
            self.assertEqual(cs.name(what=gxcs.NAME_ORIENTATION),'0,0,0,0,0,0')
            self.assertEqual(cs.name(what=gxcs.NAME_UNIT),'m')
            self.assertEqual(cs.name(what=gxcs.NAME_UNIT_FULL),'metre')

        # GXF strings
        with gxcs.GXcs(['','DHDN','Okarito 2000','','']) as cs:
            gxfs = cs.gxf()
            self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
            self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
            self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
            self.assertEqual(gxfs[3],'m,1')
            self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')
            dct = cs.coordinate_dict.copy()

        # dictionary
        with gxcs.GXcs(dct) as cs:
            gxfs = cs.gxf()
            self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
            self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
            self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
            self.assertEqual(gxfs[3],'m,1')
            self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

            csd = cs.coordinate_dict
            self.assertEqual(csd['name'],'DHDN / Okarito 2000')
            self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
            self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
            self.assertEqual(gxfs[3],'m,1')
            self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

        # name with a separate vcs
        with gxcs.GXcs('DHDN / Okarito 2000', 'geoid') as cs:
            self.assertEqual(cs.name(what=gxcs.NAME_HCS_VCS), str(cs))
            self.assertEqual(cs.name(what=gxcs.NAME_VCS), 'geoid')
            self.assertEqual(cs.name(what=gxcs.NAME_HCS_VCS), 'DHDN / Okarito 2000 [geoid]')

        # name with embedded vcs
        with gxcs.GXcs('DHDN / Okarito 2000 [geoid]') as cs:
            self.assertEqual(cs.name(what=gxcs.NAME_HCS_VCS), str(cs))
            self.assertEqual(cs.name(what=gxcs.NAME_VCS), 'geoid')
            self.assertEqual(cs.name(what=gxcs.NAME_HCS_VCS), 'DHDN / Okarito 2000 [geoid]')

        ipj = gxapi.GXIPJ.create()
        ipj.set_gxf('', 'DHDN', 'Okarito 2000', '', '')
        with gxcs.GXcs(ipj) as cs:
            gxfs = cs.gxf()
            self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
            self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
            self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
            self.assertEqual(gxfs[3],'m,1')
            self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')
            self.assertEqual(cs.name(),'DHDN / Okarito 2000')
            self.assertEqual(cs.name(what=gxcs.NAME),'DHDN / Okarito 2000')
            self.assertEqual(cs.name(what=gxcs.NAME_HCS),'DHDN / Okarito 2000')
            self.assertEqual(cs.name(what=gxcs.NAME_VCS), '')
            self.assertEqual(cs.name(what=gxcs.NAME_HCS_VCS), 'DHDN / Okarito 2000')
            self.assertEqual(cs.name(what=gxcs.NAME_DATUM),'DHDN')
            self.assertEqual(cs.name(what=gxcs.NAME_PROJECTION),'Okarito 2000')
            self.assertEqual(cs.name(what=gxcs.NAME_ORIENTATION),'0,0,0,0,0,0')
            self.assertEqual(cs.name(what=gxcs.NAME_UNIT),'m')
            self.assertEqual(cs.name(what=gxcs.NAME_UNIT_FULL),'metre')

    def test_name_cs(self):
        self.start(gsys.func_name())

        hcs, orient, vcs = gxcs.hcs_orient_vcs_from_name("DHDN / Okarito 2000 [geoid]")
        self.assertEqual(hcs, "DHDN / Okarito 2000")
        self.assertEqual(orient, "")
        self.assertEqual(vcs, "geoid")
        self.assertEqual(gxcs.name_from_hcs_orient_vcs(hcs, orient, vcs), "DHDN / Okarito 2000 [geoid]")

        hcs, orient, vcs = gxcs.hcs_orient_vcs_from_name("DHDN / Okarito 2000    <0,0,0,0,0,0>  [geoid]     ")
        self.assertEqual(hcs, "DHDN / Okarito 2000")
        self.assertEqual(orient, "0,0,0,0,0,0")
        self.assertEqual(vcs, "geoid")
        self.assertEqual(gxcs.name_from_hcs_orient_vcs(hcs, orient, vcs), "DHDN / Okarito 2000 <0,0,0,0,0,0> [geoid]")

        hcs, orient, vcs = gxcs.hcs_orient_vcs_from_name("DHDN / Okarito 2000 <0,0,0,0,0,0>")
        self.assertEqual(hcs, "DHDN / Okarito 2000")
        self.assertEqual(orient, "0,0,0,0,0,0")
        self.assertEqual(vcs, "")
        self.assertEqual(gxcs.name_from_hcs_orient_vcs(hcs, orient, vcs), "DHDN / Okarito 2000 <0,0,0,0,0,0>")

        hcs, orient, vcs = gxcs.hcs_orient_vcs_from_name("DHDN / Okarito 2000")
        self.assertEqual(hcs, "DHDN / Okarito 2000")
        self.assertEqual(orient, "")
        self.assertEqual(vcs, "")
        self.assertEqual(gxcs.name_from_hcs_orient_vcs(hcs, orient, vcs), "DHDN / Okarito 2000")

        with gxcs.GXcs( 'DHDN / Okarito 2000 [geodetic]') as cs:
            gxfs = cs.gxf()
            self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
            self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
            self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
            self.assertEqual(gxfs[3],'m,1')
            self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')
            self.assertEqual(cs.name(),'DHDN / Okarito 2000')
            self.assertEqual(cs.name(what=gxcs.NAME),'DHDN / Okarito 2000')
            self.assertEqual(cs.name(what=gxcs.NAME_HCS),'DHDN / Okarito 2000')
            self.assertEqual(cs.name(what=gxcs.NAME_DATUM),'DHDN')
            self.assertEqual(cs.name(what=gxcs.NAME_PROJECTION),'Okarito 2000')
            self.assertEqual(cs.name(what=gxcs.NAME_ORIENTATION),'0,0,0,0,0,0')
            self.assertEqual(cs.name(what=gxcs.NAME_UNIT),'m')
            self.assertEqual(cs.name(what=gxcs.NAME_UNIT_FULL),'metre')

        with gxcs.GXcs('DHDN', 'geoid') as cs:
            self.assertEqual(cs.name(what=gxcs.NAME_HCS_VCS), cs.cs)
            self.assertEqual(cs.name(what=gxcs.NAME_HCS), cs.hcs)
            self.assertEqual(cs.name(what=gxcs.NAME_VCS), cs.vcs)
            self.assertEqual(cs.name(what=gxcs.NAME_HCS), 'DHDN')
            self.assertEqual(cs.name(what=gxcs.NAME_VCS), 'geoid')
            self.assertEqual(cs.name(what=gxcs.NAME_HCS_VCS), 'DHDN [geoid]')

        with gxcs.GXcs('DHDN [geodetic]') as cs:
            self.assertEqual(cs.name(what=gxcs.NAME_HCS_VCS), cs.cs)
            self.assertEqual(cs.name(what=gxcs.NAME_HCS), cs.hcs)
            self.assertEqual(cs.name(what=gxcs.NAME_VCS), cs.vcs)
            self.assertEqual(cs.name(what=gxcs.NAME_HCS), 'DHDN')
            self.assertEqual(cs.name(what=gxcs.NAME_VCS), 'geodetic')
            self.assertEqual(cs.name(what=gxcs.NAME_HCS_VCS), 'DHDN [geodetic]')

    def test_GXF_cs(self):
        self.start(gsys.func_name())

        stref = gxapi.str_ref()

        #test IPJ creation using GXF strings
        cs = gxcs.GXcs( ['','DHDN','Okarito 2000','',''])
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

        cs = gxcs.GXcs( gxfs)
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')
        #s6 = gxapi.str_ref()
        cs.gxipj.get_name(gxcs.NAME_METHOD_LABEL,stref)
        self.assertEqual(stref.value,'Lat0,Lon0,SF,FE,FN')
        cs.gxipj.get_name(gxcs.NAME_METHOD_PARMS,stref)
        self.assertEqual(stref.value,'-43.11,170.260833333333,1,400000,800000')

        #test IPJ creation using GXF strings
        cs = gxcs.GXcs( ['','DHDN','"Transverse Mercator",0,39,0.9996,500000,99999','m,1',''])
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'DHDN / *Transverse Mercator')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,39,0.9996,500000,99999')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

        #test minimum with local rotation
        cs = gxcs.GXcs( [',500000,6000000,0,0,0,15','NAD83','"Transverse Mercator",0,-69,0.9996,500000,0','m,1',''])
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'NAD83 / UTM zone 19N')
        self.assertEqual(gxfs[1],'NAD83,6378137,0.0818191910428158,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,-69,0.9996,500000,0')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"NAD83 to WGS 84 (1)",0,0,0,0,0,0,0')

        cs = gxcs.GXcs( ['','NAD83','UTM zone 19N','m,1',''])
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'NAD83 / UTM zone 19N')
        self.assertEqual(gxfs[1],'NAD83,6378137,0.0818191910428158,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,-69,0.9996,500000,0')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"NAD83 to WGS 84 (1)",0,0,0,0,0,0,0')

        #test EPSG numbers
        cs = gxcs.GXcs( ['','4193','','',''])
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'Manoca 1962')
        self.assertEqual(gxfs[1],'"Manoca 1962",6378249.2,0.0824832567634178,0')
        self.assertEqual(gxfs[2],'')
        self.assertEqual(gxfs[3],'dega,1')
        self.assertEqual(gxfs[4],'"Manoca 1962 to WGS 84 (1)",-70.9,-151.8,-41.4,0,0,0,0')

        cs = gxcs.GXcs( ['4210','','','',''])
        gxfs = cs.gxf()
        self.assertEqual(gxfs[1],'"Arc 1960",6378249.145,0.082483400044185,0')

        cs = gxcs.GXcs( ['21037','','','',''])
        gxfs = cs.gxf()
        self.assertEqual(gxfs[1],'"Arc 1960",6378249.145,0.082483400044185,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,39,0.9996,500000,10000000')

        cs = gxcs.GXcs( ['','4210','16137','',''])
        gxfs = cs.gxf()
        self.assertEqual(gxfs[1],'"Arc 1960",6378249.145,0.082483400044185,0')

    def test_ESRI_cs(self):
        self.start(gsys.func_name())

        stref = gxapi.str_ref()

        #test IPJ creation using GXF strings
        cs = gxcs.GXcs(['', 'DHDN', 'Okarito 2000', '', ''])
        cs.gxipj.get_esri(stref)
        self.assertTrue('PROJCS["Okari' in stref.value)
        self.assertTrue('GEOGCS["GCS_Deutsches_Hauptdreiecksnetz"' in stref.value)

        wkt = gxcs.Wkt(stref.value)
        self.assertEqual(wkt.name(), 'Okarito_2000')

        cs = gxcs.GXcs(stref.value)
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'DHDN / *Okarito 2000')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225274,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

        gxcs.GXcs("WGS 84 / UTM zone 32N").gxipj.get_esri(stref)
        wkt = gxcs.Wkt(stref.value)
        self.assertEqual(wkt.name(), 'WGS_1984_UTM_Zone_32N')

        gxcs.GXcs("WGS 84").gxipj.get_esri(stref)
        wkt = gxcs.Wkt(stref.value)
        self.assertEqual(wkt.name(), 'GCS_WGS_1984')

    def test_MAPINFO_cs(self):
        self.start(gsys.func_name())

        stref1 = gxapi.str_ref()
        stref2 = gxapi.str_ref()
        
        #test IPJ creation using GXF strings
        cs = gxcs.GXcs( ['','DHDN','Okarito 2000','',''])
        cs.gxipj.get_mi_coord_sys(stref1,stref2)
        self.assertEqual(stref1.value,'CoordSys Earth Projection 8,1000,"m",170.2608333333,-43.1100000000,1,400000,800000')
        self.assertEqual(stref2.value,'Units "m"')

        cs.gxipj.set_mi_coord_sys(stref1.value,stref2.value)
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.2608333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

    def test_ORIENTATION_cs(self):
        self.start(gsys.func_name())

        stref = gxapi.str_ref()

        #test IPJ creation using GXF strings
        cs = gxcs.GXcs( ['<525000,6000000,0,0,0,15>','DHDN','Okarito 2000','',''])
        cs.gxipj.get_name(gxapi.IPJ_NAME_ORIENTATION_PARMS,stref)
        self.assertEqual(stref.value,'525000,6000000,0,0,0,15')
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000 <525000,6000000,0,0,0,15>')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

        #test IPJ creation using GXF strings
        cs = gxcs.GXcs( ['DRUKREF 03 / Bumthang TM <525000,6000000,0,0,0,15>','','','',''])
        cs.gxipj.get_display_name(stref)
        cs.gxipj.get_name(gxapi.IPJ_NAME_ORIENTATION_PARMS,stref)
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'DRUKREF 03 / Bumthang TM <525000,6000000,0,0,0,15>')
        self.assertEqual(gxfs[1],'"Bhutan National Geodetic Datum",6378137,0.0818191910428158,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,90.7333333333333,1,250000,-2500000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'')

        del(cs)

    def test_JSON_cs(self):
        self.start(gsys.func_name())

        stref = gxapi.str_ref()
        cs = gxcs.GXcs( "{'type': 'EPSG', 'code': 20250}")
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'AGD66 / AMG zone 50')
        self.assertEqual(gxfs[1],'AGD66,6378160,0.0818201799960599,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,117,0.9996,500000,10000000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"AGD66 to WGS 84 (12)",-129.193,-41.212,130.73,0.246,0.374,0.329,-2.95500000002669')

        cs = gxcs.GXcs( "{'type': 'EPSG', 'code': '20250 <1000,500,20,0,0,25>'}")
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'AGD66 / AMG zone 50 <1000,500,20,0,0,25>')
        self.assertEqual(gxfs[1],'AGD66,6378160,0.0818201799960599,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,117,0.9996,500000,10000000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"AGD66 to WGS 84 (12)",-129.193,-41.212,130.73,0.246,0.374,0.329,-2.95500000002669')

        wkt = 'PROJCS["Okarito 2000",GEOGCS["GCS_Deutsches_Hauptdreiecksnetz",DATUM["D_Deutsches_Hauptdreiecksnetz",SPHEROID["Bessel_1841",6377397.155,299.152812800001]],PRIMEM["Greenwich",0],UNIT["Degree",0.0174532925199432955]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",400000],PARAMETER["False_Northing",800000],PARAMETER["Central_Meridian",170.260833333333],PARAMETER["Scale_Factor",1],PARAMETER["Latitude_Of_Origin",-43.11],UNIT["Meter",1]]'
        wkt = wkt.replace('"', '\\"')
        orientation = '"35000,55555,0,0,0,33"'
        cs = gxcs.GXcs( '{"type":"ESRI","orientation":'+orientation+',"wkt":"' + wkt + '"}')
        cs.gxipj.get_display_name(stref)
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'DHDN / *Okarito 2000 <35000,55555,0,0,0,33>')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

        cs = gxcs.GXcs( '{"type":"Geosoft","name":"<25000,1000000,50,90,0,15>","datum":"DHDN","projection":"Okarito 2000"}')
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000 <25000,1000000,50,90,0,15>')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000 <25000,1000000,50,90,0,15>')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

    def test_DICT_cs(self):
        self.start(gsys.func_name())

        with gxcs.GXcs({'type': 'EPSG', 'code': 20250}) as cs:
            gxfs = cs.gxf()
            self.assertEqual(gxfs[0],'AGD66 / AMG zone 50')
            self.assertEqual(gxfs[1],'AGD66,6378160,0.0818201799960599,0')
            self.assertEqual(gxfs[2],'"Transverse Mercator",0,117,0.9996,500000,10000000')
            self.assertEqual(gxfs[3],'m,1')
            self.assertEqual(gxfs[4],'"AGD66 to WGS 84 (12)",-129.193,-41.212,130.73,0.246,0.374,0.329,-2.95500000002669')

    def _test_OBLIQUESTEREO_cs(self): #TODO change to a local coordinate system test
        self.start(gsys.func_name())

        stref = gxapi.str_ref()

        cs = gxcs.GXcs( '{"type": "Geosoft", "datum":"NAD83,6378137,0.0818191910428158,0","projection":"\\"Oblique Stereographic\\",61.40.00,-128.10.00,1,0,0","units":"m,1","gxf5":"\\"NAD83 to WGS 84 (1)\\",0,0,0,0,0,0,0"}')
        cs.gxipj.get_display_name(stref)
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'NAD83 / *Oblique Stereographic')
        self.assertEqual(gxfs[1],'NAD83,6378137,0.0818191910428158,0')
        self.assertEqual(gxfs[2],'"Oblique Stereographic",61.6666666666667,-128.166666666667,1,0,0')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"NAD83 to WGS 84 (1)",0,0,0,0,0,0,0')

        cs = gxcs.GXcs( '{"type": "Localgrid", "longitude":"-128.10.00","latitude":"61.40.00","azimuth":-15,"units":"ft"}')
        cs.gxipj.get_display_name(stref)
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'WGS 84 / *Local grid (61.40.00,-128.10.00) <0,0,0,0,0,-15>')
        self.assertEqual(gxfs[1],'"WGS 84",6378137,0.0818191908426215,0')
        self.assertEqual(gxfs[2],'"Oblique Stereographic",61.6666666666667,-128.166666666667,0.9996,0,0')
        self.assertEqual(gxfs[3],'ft,0.3048')
        self.assertEqual(gxfs[4],'"WGS 84",0,0,0,0,0,0,0')

        cs = gxcs.GXcs( '{"type": "Localgrid", "longitude":"-128.10.00","latitude":"61.40.00","azimuth":-15,"units":"ft","elevation":133.1567}')
        cs.gxipj.get_display_name(stref)
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'WGS 84 / *Local grid [61.40.00,-128.10.00] <0,0,133.1567,0,0,-15>')
        self.assertEqual(gxfs[1],'"WGS 84",6378137,0.0818191908426215,0')
        self.assertEqual(gxfs[2],'"Oblique Stereographic",61.6666666666667,-128.166666666667,0.9996,0,0')
        self.assertEqual(gxfs[3],'ft,0.3048')
        self.assertEqual(gxfs[4],'"WGS 84",0,0,0,0,0,0,0')

        cs = gxcs.GXcs( '{"type": "Localgrid", "longitude":0,"latitude":0}')
        cs.gxipj.get_display_name(stref)
        gxfs = cs.gxf()
        self.assertEqual(gxfs[0],'WGS 84 / *Local grid [0,0]')
        self.assertEqual(gxfs[1],'"WGS 84",6378137,0.0818191908426215,0')
        self.assertEqual(gxfs[2],'"Oblique Stereographic",0,0,0.9996,0,0')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"WGS 84",0,0,0,0,0,0,0')

    def test_names_cs(self):
        self.start(gsys.func_name())

        with gxcs.GXcs( '{"type": "Geosoft", "name":"NAD83 / UTM zone 26N", "orientation":"1000,500,0,0,0,15"}') as cs:
            csd = cs.coordinate_dict
            self.assertEqual(csd["type"],'Geosoft')
            self.assertEqual(csd["name"],'NAD83 / UTM zone 26N <1000,500,0,0,0,15>')
            self.assertEqual(csd["datum"],'NAD83,6378137,0.0818191910428158,0')
            self.assertEqual(csd["projection"],'"Transverse Mercator",0,-27,0.9996,500000,0')
            self.assertEqual(csd["units"],'m,1')
            self.assertEqual(csd["orientation"],'1000,500,0,0,0,15')
            self.assertEqual(csd["vcs"], '')

        with gxcs.GXcs( '{"type": "Geosoft", "datum":"NAD83,6378137,0.0818191910428158,0", "projection":"Oblique Stereographic,61.40.00,-128.10.00,1,0,0", "units":"m,1", "local_datum":"NAD83 to WGS 84 (1),0,0,0,0,0,0,0"}') as cs:
            csd = cs.coordinate_dict
            self.assertEqual(csd["type"],'Geosoft')
            self.assertEqual(csd["name"],'NAD83 / *Oblique Stereographic')
            self.assertEqual(csd["datum"],'NAD83,6378137,0.0818191910428158,0')
            self.assertEqual(csd["local_datum"], '"NAD83 to WGS 84 (1)",0,0,0,0,0,0,0')
            self.assertEqual(csd["projection"],'"Oblique Stereographic",61.6666666666667,-128.166666666667,1,0,0')
            self.assertEqual(csd["units"],'m,1')
            self.assertEqual(csd["orientation"],'')
            self.assertEqual(csd["vcs"], '')

    def test_compare(self):
        self.start(gsys.func_name())

        cs = gxcs.GXcs('NAD27 / UTM zone 18N')
        cs2 = gxcs.GXcs('NAD27 / UTM zone 18N')
        self.assertTrue(cs.same_as(cs2))
        cs2 = gxcs.GXcs( 'NAD83 / UTM zone 18N')
        self.assertFalse(cs.same_as(cs2))

        with gxcs.GXcs("wgs 84", "geoid") as cs1:
            with gxcs.GXcs("WGS 84", "geoid") as cs2:
                self.assertTrue(cs1.same_as(cs2))

        with gxcs.GXcs("wgs 84 / UTM zone 32N",) as cs1:
            with gxcs.GXcs("WGS 84", "geoid") as cs2:
                self.assertFalse(cs1.same_as(cs2))

        self.assertTrue(gxcs.GXcs("nad83").same_as(gxcs.GXcs("NAD83")))
        self.assertTrue(gxcs.GXcs("nad83", "NAVD92").same_as(gxcs.GXcs("NAD83", "NAVD92")))
        self.assertTrue(gxcs.GXcs("nad83", "NAVD92").same_as(gxcs.GXcs("NAD83")))
        self.assertTrue(gxcs.GXcs("nad83").same_as(gxcs.GXcs("NAD83", "NAVD92")))
        self.assertTrue(gxcs.GXcs("nad83", "NAVD92").same_vcs(gxcs.GXcs("NAD27", "NAVD92")))
        self.assertTrue(gxcs.GXcs("nad83").same_vcs(gxcs.GXcs("NAD27", "NAVD92")))
        self.assertTrue(gxcs.GXcs("nad27", "geoid").same_hcs(gxcs.GXcs("NAD27", "NAVD92")))

        self.assertFalse(gxcs.GXcs("nad83 / UTM zone 35N").same_as(gxcs.GXcs("NAD83")))
        self.assertFalse(gxcs.GXcs("nad83", "NAVD92").same_as(gxcs.GXcs("NAD83", "geodetic")))
        self.assertFalse(gxcs.GXcs("nad83").same_as(gxcs.GXcs("NAD27")))
        self.assertFalse(gxcs.GXcs("nad83", "geoid").same_vcs(gxcs.GXcs("NAD27", "NAVD92")))


    def test_units(self):
        self.start(gsys.func_name())
        cs = gxcs.GXcs("NAD27 / Arizona Coordinate System Central zone")
        self.assertAlmostEqual(cs.units()[0],0.304800609601219)
        self.assertEqual(cs.units()[1],'ftUS')
        cs = gxcs.GXcs(('', '', '', 'ftUS', ''))
        self.assertAlmostEqual(cs.units()[0], 0.304800609601219)
        self.assertEqual(cs.units()[1], 'ftUS')
        cs = gxcs.GXcs('ftUS')
        self.assertAlmostEqual(cs.units()[0], 0.304800609601219)
        self.assertEqual(cs.units()[1], 'ftUS')
        self.assertRaises(gxcs.CSException, gxcs.GXcs, 'bogus', init=True)

    def test_PJ(self):
        self.start(gsys.func_name())

        data = np.zeros((10,5),dtype='float')
        for i in range(data.shape[0]):
            data[i,0] = 5000000.0 - i
            data[i,1] = 2000000.0 + i
            data[i,2] = 0.0 + i/2.0
            data[i,3] = -1000.0 + i
            data[i,4] = 1000.0 + i

        cs = gxcs.GXcs( 'NAD27 / UTM zone 18N')
        cs2 = gxcs.GXcs( 'NAD83 / UTM zone 18N')
        pj = gxcs.GXpj( cs, cs2)

        new = data.copy()
        pj.convert(new)
        self.assertAlmostEqual(new[0,0], 5015680.1233521616)
        self.assertAlmostEqual(new[0,1], 1995617.5525243089)
        self.assertAlmostEqual(new[0,2], 0.0)
        self.assertAlmostEqual(new[4,0], 5015676.0866539562)
        self.assertAlmostEqual(new[4,1], 1995621.5795361274)
        self.assertAlmostEqual(new[4,2], 2.0)

        #test xyz only
        new = data.copy()
        pj.convert(new[:,:3])
        self.assertAlmostEqual(new[0,0], 5015680.1233521616)
        self.assertAlmostEqual(new[0,1], 1995617.5525243089)
        self.assertAlmostEqual(new[0,2], 0.0)
        self.assertAlmostEqual(new[4,0], 5015676.0866539562)
        self.assertAlmostEqual(new[4,1], 1995621.5795361274)
        self.assertAlmostEqual(new[4,2], 2.0)

        #test xy only
        new = data.copy()
        pj.convert(new[:,:2])
        self.assertAlmostEqual(new[0,0], 5015680.1233521616)
        self.assertAlmostEqual(new[0,1], 1995617.5525243089)
        self.assertAlmostEqual(new[0,2], 0.0)
        self.assertAlmostEqual(new[4,0], 5015676.0866959104)
        self.assertAlmostEqual(new[4,1], 1995621.5795778199)
        self.assertAlmostEqual(new[4,2], 2.0)

        #test integers, why not!
        new = np.zeros((10,5),dtype='int')
        new[:] = data[:]
        pj.convert(new[:,:2])
        self.assertAlmostEqual(new[0,0], 5015680)
        self.assertAlmostEqual(new[0,1], 1995617)
        self.assertAlmostEqual(new[0,2], 0)
        self.assertAlmostEqual(new[4,0], 5015676)
        self.assertAlmostEqual(new[4,1], 1995621)
        self.assertAlmostEqual(new[4,2], 2)

        #test exception
        try:
            pj.convert(new[:,0])
            self.assertTrue(False)
        except:
            self.assertTrue(True)


    def test_lists(self):
        self.start(gsys.func_name())

        self.assertTrue(len(gxcs.name_list(gxcs.LIST_DATUM)))
        self.assertTrue(len(gxcs.name_list(gxcs.LIST_COORDINATESYSTEM)))
        self.assertTrue(len(gxcs.name_list(gxcs.LIST_DATUM)))
        self.assertTrue(len(gxcs.name_list(gxcs.LIST_PROJECTION)))
        self.assertTrue(len(gxcs.name_list(gxcs.LIST_UNITS)))
        self.assertTrue(len(gxcs.name_list(gxcs.LIST_UNITSDESCRIPTION)))
        self.assertTrue(len(gxcs.name_list(gxcs.LIST_LOCALDATUMDESCRIPTION)))
        self.assertTrue(len(gxcs.name_list(gxcs.LIST_LOCALDATUMNAME)))

    def test_gcs(self):
        self.start(gsys.func_name())

        with gxcs.GXcs("wgs 84", init=True) as cs1:
            self.assertEqual(str(cs1), "WGS 84")
            with gxcs.GXcs("NAD27") as cs2:
                self.assertEqual(str(cs2), "NAD27")
                self.assertFalse(cs1 == cs2)
            with gxcs.GXcs("NAD83") as cs2:
                self.assertEqual(str(cs2), "NAD83")
                self.assertFalse(cs1 == cs2)
            with gxcs.GXcs("WGS 84") as cs2:
                self.assertEqual(str(cs2), "WGS 84")

    def test_hcs_vcs(self):
        self.start(gsys.func_name())

        with gxcs.GXcs("wgs 84", "geoid") as cs:
            hcsdict = cs.coordinate_dict
            self.assertEqual(hcsdict['name'], "WGS 84") # TODO fix this once we have orientation fixed in gxapi
            #self.assertEqual(hcsdict['name'], "WGS 84 [geoid]")
            self.assertEqual(hcsdict['datum'], '"WGS 84",6378137,0.0818191908426215,0')
            self.assertEqual(hcsdict['projection'], "")
            self.assertEqual(hcsdict['vcs'], '') # TODO fix this once we have orientation fixed in gxapi
            #self.assertEqual(hcsdict['vcs'], "geoid")
            self.assertEqual(cs.vcs, 'geoid')

    def test_orientation(self):
        self.start(gsys.func_name())

        s = "WGS 84 / UTM zone 32N <0, 0, 0, 10, 15, 32>"
        with gxcs.GXcs(s, init=True) as cs:
            self.assertEqual(str(cs), "WGS 84 / UTM zone 32N (0,0,0) <32 deg,15 deg,10 deg>")

        s = "WGS 84 / UTM zone 32N <0, 0, 0, 0, 0, 0>"
        with gxcs.GXcs(s, init=True) as cs:
            self.assertEqual(str(cs), "WGS 84 / UTM zone 32N")

        s = "WGS 84 / UTM zone 32N <150, 8.5, 0, 0, 0, 32>"
        with gxcs.GXcs(s) as cs:
            self.assertEqual(str(cs), "WGS 84 / UTM zone 32N <150, 8.5, 0, 0, 0, 32>")

        #TODO talk to Stephen about testing of orientation interface

###############################################################################################

if __name__ == '__main__':

    unittest.main()
