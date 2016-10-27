import unittest
import numpy as np
import json

import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.ipj as gxipj
import geosoft

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gx = gx.GXpy()

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def start(cls,test):
        print("\n*** {} *** - {}".format(test, geosoft.__version__))

    def test_ipj(self):
        self.start(gsys.func_name())
        self.assertEqual(gxipj.__version__, geosoft.__version__)

    def test_lists_IPJ(self):
        self.start(gsys.func_name())
        
        #name lists
        dlist = gxipj.GXipj.names(gxipj.LIST_DATUM)
        self.assertTrue('Arc 1950' in dlist)
        dlist = gxipj.GXipj.names(gxipj.LIST_LOCALDATUMNAME)
        self.assertTrue('SIRGAS to WGS 84 (1)' in dlist)
        dlist = gxipj.GXipj.names(gxipj.LIST_COORDINATESYSTEM)
        self.assertTrue('MGI 1901 / Slovenia Grid' in dlist)
        dlist = gxipj.GXipj.names(gxipj.LIST_PROJECTION)
        self.assertTrue('Rectified Skew Orthomorphic Malaya Grid (metres)' in dlist)
        dlist = gxipj.GXipj.names(gxipj.LIST_UNITS,'')
        self.assertTrue('hemisphere degree minute second' in dlist)
        dlist = gxipj.GXipj.names(gxipj.LIST_UNITSDESCRIPTION)
        self.assertTrue('US survey inch' in dlist)
        dlist = gxipj.GXipj.names(gxipj.LIST_LOCALDATUMDESCRIPTION)
        self.assertTrue('[SIRGAS-ROU98] (1m) Uruguay' in dlist)
        dlist = gxipj.GXipj.names(gxipj.LIST_LOCALDATUMDESCRIPTION,'AGD66')
        self.assertTrue('[AGD66] Cocos Is Anna 1 ASTRO 1965' in dlist)
        self.assertTrue(dlist[0][:7],'[AGD66]')

        return

    def test_name_IPJ(self):
        self.start(gsys.func_name())

        ipj = gxipj.GXipj.from_name( 'DHDN / Okarito 2000')
        print(ipj,ipj.__repr__())
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')
        self.assertEqual(ipj.name(),'DHDN / Okarito 2000')
        self.assertEqual(ipj.name(what=gxipj.NAME),'DHDN / Okarito 2000')
        self.assertEqual(ipj.name(what=gxipj.NAME_PCS),'DHDN / Okarito 2000')
        self.assertEqual(ipj.name(what=gxipj.NAME_DATUM),'DHDN')
        self.assertEqual(ipj.name(what=gxipj.NAME_PROJECTION),'Okarito 2000')
        self.assertEqual(ipj.name(what=gxipj.NAME_ORIENTATION),'0,0,0,0,0,0')
        self.assertEqual(ipj.name(what=gxipj.NAME_UNIT),'m')
        self.assertEqual(ipj.name(what=gxipj.NAME_UNIT_FULL),'metre')

        ipj = gxipj.GXipj.from_name( 'DHDN / Okarito 2000 <1,2,3,4,5,6>')
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000 <1,2,3,4,5,6>')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')
        self.assertEqual(ipj.name(),'DHDN / Okarito 2000 (1,2,3) <6 deg,5 deg,4 deg>')
        self.assertEqual(ipj.name(what=gxipj.NAME),'DHDN / Okarito 2000 (1,2,3) <6 deg,5 deg,4 deg>')
        self.assertEqual(ipj.name(what=gxipj.NAME_PCS),'DHDN / Okarito 2000')
        self.assertEqual(ipj.name(what=gxipj.NAME_DATUM),'DHDN')
        self.assertEqual(ipj.name(what=gxipj.NAME_PROJECTION),'Okarito 2000')
        self.assertEqual(ipj.name(what=gxipj.NAME_ORIENTATION),'1,2,3,4,5,6')

        ipj = gxipj.GXipj.from_name( 'WGS 84')
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'WGS 84')
        self.assertEqual(gxfs[1],'"WGS 84",6378137,0.0818191908426215,0')
        self.assertEqual(gxfs[2],'')
        self.assertEqual(gxfs[3],'dega,1')
        self.assertEqual(gxfs[4],'"WGS 84",0,0,0,0,0,0,0')
        self.assertEqual(ipj.name(),'WGS 84')
        self.assertEqual(ipj.name(what=gxipj.NAME),'WGS 84')
        self.assertEqual(ipj.name(what=gxipj.NAME_PCS),'WGS 84')
        self.assertEqual(ipj.name(what=gxipj.NAME_DATUM),'WGS 84')
        self.assertEqual(ipj.name(what=gxipj.NAME_PROJECTION),'')
        self.assertEqual(ipj.name(what=gxipj.NAME_ORIENTATION),'0,0,0,0,0,0')

    def test_GXF_IPJ(self):
        self.start(gsys.func_name())

        stref = gxapi.str_ref()

        #test IPJ creation using GXF strings
        ipj = gxipj.GXipj.from_gxf( ['','DHDN','Okarito 2000','',''])
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

        ipj = gxipj.GXipj.from_gxf( gxfs)
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')
        #s6 = gxapi.str_ref()
        ipj._ipj.get_name(gxipj.NAME_METHOD_LABEL,stref)
        self.assertEqual(stref.value,'Lat0,Lon0,SF,FE,FN')
        ipj._ipj.get_name(gxipj.NAME_METHOD_PARMS,stref)
        self.assertEqual(stref.value,'-43.11,170.260833333333,1,400000,800000')

        #test IPJ creation using GXF strings
        ipj = gxipj.GXipj.from_gxf( ['','DHDN','"Transverse Mercator",0,39,0.9996,500000,99999','m,1',''])
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'DHDN / *Transverse Mercator')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,39,0.9996,500000,99999')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

        #test minimum with local rotation
        ipj = gxipj.GXipj.from_gxf( [',500000,6000000,0,0,0,15','NAD83','"Transverse Mercator",0,-69,0.9996,500000,0','m,1',''])
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'NAD83 / UTM zone 19N')
        self.assertEqual(gxfs[1],'NAD83,6378137,0.0818191910428158,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,-69,0.9996,500000,0')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"NAD83 to WGS 84 (1)",0,0,0,0,0,0,0')

        ipj = gxipj.GXipj.from_gxf( ['','NAD83','UTM zone 19N','m,1',''])
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'NAD83 / UTM zone 19N')
        self.assertEqual(gxfs[1],'NAD83,6378137,0.0818191910428158,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,-69,0.9996,500000,0')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"NAD83 to WGS 84 (1)",0,0,0,0,0,0,0')

        #test EPSG numbers
        ipj = gxipj.GXipj.from_gxf( ['','4193','','',''])
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'Manoca 1962')
        self.assertEqual(gxfs[1],'"Manoca 1962",6378249.2,0.0824832567634178,0')
        self.assertEqual(gxfs[2],'')
        self.assertEqual(gxfs[3],'dega,1')
        self.assertEqual(gxfs[4],'"Manoca 1962 to WGS 84 (1)",-70.9,-151.8,-41.4,0,0,0,0')

        ipj = gxipj.GXipj.from_gxf( ['4210','','','',''])
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[1],'"Arc 1960",6378249.145,0.082483400044185,0')

        ipj = gxipj.GXipj.from_gxf( ['21037','','','',''])
        print(ipj)
        gxfs = ipj.to_gxf()
        print("1:{}\n2:{}\n3:{}\n4:{}\n5:{}".format(gxfs[0],gxfs[1],gxfs[2],gxfs[3],gxfs[4]))
        self.assertEqual(gxfs[1],'"Arc 1960",6378249.145,0.082483400044185,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,39,0.9996,500000,10000000')

        ipj = gxipj.GXipj.from_gxf( ['','4210','16137','',''])
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[1],'"Arc 1960",6378249.145,0.082483400044185,0')

    def test_ESRI_IPJ(self):
        self.start(gsys.func_name())

        stref = gxapi.str_ref()

        #test IPJ creation using GXF strings
        ipj = gxipj.GXipj.from_gxf( ['','DHDN','Okarito 2000','',''])
        ipj._ipj.get_esri(stref)
        print("ESRI coordinates: {}".format(stref.value))
        self.assertEqual(stref.value,'PROJCS["Okarito_2000",GEOGCS["GCS_Deutsches_Hauptdreiecksnetz",DATUM["D_Deutsches_Hauptdreiecksnetz",SPHEROID["Bessel_1841",6377397.155,299.152812800001]],PRIMEM["Greenwich",0],UNIT["Degree",0.0174532925199432955]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",400000],PARAMETER["False_Northing",800000],PARAMETER["Central_Meridian",170.260833333333],PARAMETER["Scale_Factor",1],PARAMETER["Latitude_Of_Origin",-43.11],UNIT["Meter",1]]')

        ipj = gxipj.GXipj.from_esri(stref.value)
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'DHDN / *Okarito 2000')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225274,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

    def test_MAPINFO_IPJ(self):
        self.start(gsys.func_name())

        stref1 = gxapi.str_ref()
        stref2 = gxapi.str_ref()
        
        #test IPJ creation using GXF strings
        ipj = gxipj.GXipj.from_gxf( ['','DHDN','Okarito 2000','',''])
        ipj._ipj.get_mi_coord_sys(stref1,stref2)
        print(ipj)
        print("Mapinfo coordinates: {}".format(stref1.value))
        print("Mapinfo units: {}".format(stref2.value))
        self.assertEqual(stref1.value,'CoordSys Earth Projection 8,1000,"m",170.2608333333,-43.1100000000,1,400000,800000')
        self.assertEqual(stref2.value,'Units "m"')

        ipj._ipj.set_mi_coord_sys(stref1.value,stref2.value)
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.2608333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

    def test_ORIENTATION_IPJ(self):
        self.start(gsys.func_name())

        stref = gxapi.str_ref()

        #test IPJ creation using GXF strings
        ipj = gxipj.GXipj.from_gxf( ['<525000,6000000,0,0,0,15>','DHDN','Okarito 2000','',''])
        ipj._ipj.get_name(gxapi.IPJ_NAME_ORIENTATION_PARMS,stref)
        self.assertEqual(stref.value,'525000,6000000,0,0,0,15')
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000 <525000,6000000,0,0,0,15>')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

        #test IPJ creation using GXF strings
        ipj = gxipj.GXipj.from_gxf( ['DRUKREF 03 / Bumthang TM <525000,6000000,0,0,0,15>','','','',''])
        ipj._ipj.get_display_name(stref)
        ipj._ipj.get_name(gxapi.IPJ_NAME_ORIENTATION_PARMS,stref)
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'DRUKREF 03 / Bumthang TM <525000,6000000,0,0,0,15>')
        self.assertEqual(gxfs[1],'"Bhutan National Geodetic Datum",6378137,0.0818191910428158,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,90.7333333333333,1,250000,-2500000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'')

        del(ipj)

    def test_JSON_IPJ(self):
        self.start(gsys.func_name())

        stref = gxapi.str_ref()
        ipj = gxipj.GXipj.from_json( "{'type': 'EPSG', 'properties': {'code': 20250}}")
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'AGD66 / AMG zone 50')
        self.assertEqual(gxfs[1],'AGD66,6378160,0.0818201799960599,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,117,0.9996,500000,10000000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"AGD66 to WGS 84 (12)",-129.193,-41.212,130.73,0.246,0.374,0.329,-2.95500000002669')

        ipj = gxipj.GXipj.from_json( "{'type': 'EPSG', 'properties': {'code': '20250 <1000,500,20,0,0,25>'}}")
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'AGD66 / AMG zone 50 <1000,500,20,0,0,25>')
        self.assertEqual(gxfs[1],'AGD66,6378160,0.0818201799960599,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,117,0.9996,500000,10000000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"AGD66 to WGS 84 (12)",-129.193,-41.212,130.73,0.246,0.374,0.329,-2.95500000002669')

        wkt = 'PROJCS["Okarito_2000",GEOGCS["GCS_Deutsches_Hauptdreiecksnetz",DATUM["D_Deutsches_Hauptdreiecksnetz",SPHEROID["Bessel_1841",6377397.155,299.152812800001]],PRIMEM["Greenwich",0],UNIT["Degree",0.0174532925199432955]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",400000],PARAMETER["False_Northing",800000],PARAMETER["Central_Meridian",170.260833333333],PARAMETER["Scale_Factor",1],PARAMETER["Latitude_Of_Origin",-43.11],UNIT["Meter",1]]'
        wkt = wkt.replace('"', '\\"')
        orientation = '"<35000,55555,0,0,0,33>"'
        ipj = gxipj.GXipj.from_json( '{"type":"ESRI","orientation":'+orientation+',"properties":{"wkt":"' + wkt + '"}}')
        ipj._ipj.get_display_name(stref)
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'DHDN / *Okarito 2000 <35000,55555,0,0,0,33>')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

        ipj = gxipj.GXipj.from_json( '{"type":"Geosoft","properties":{"name":"<25000,1000000,50,90,0,15>","datum":"DHDN","projection":"Okarito 2000"}}')
        self.assertEqual(ipj.__str__(),'DHDN / Okarito 2000 (25000,1000000,50) <15 deg,0 deg,90 deg>')
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000 <25000,1000000,50,90,0,15>')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

        ipj = gxipj.GXipj.from_json( '{"type":"Geosoft","properties":{"orientation":"<25000,1000000,50,90,0,15>","datum":"DHDN","projection":"Okarito 2000"}}')
        self.assertEqual(ipj.__str__(),'DHDN / Okarito 2000 (25000,1000000,50) <15 deg,0 deg,90 deg>')
        print(ipj)
        js = json.loads(ipj.to_json())
        print( json.dumps(js, sort_keys=True, indent=3) )


        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000 <25000,1000000,50,90,0,15>')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

        jsons = ipj.to_json()
        ipj = gxipj.GXipj.from_json( jsons)
        self.assertEqual(ipj.__str__(),'DHDN / Okarito 2000 (25000,1000000,50) <15 deg,0 deg,90 deg>')
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'DHDN / Okarito 2000 <25000,1000000,50,90,0,15>')
        self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

    def test_DICT_IPJ(self):
        self.start(gsys.func_name())

        stref = gxapi.str_ref()
        ipj = gxipj.GXipj.from_json( "{'type': 'EPSG', 'properties': {'code': 20250}}")
        ipj = gxipj.GXipj.from_dict( ipj.dict())
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'AGD66 / AMG zone 50')
        self.assertEqual(gxfs[1],'AGD66,6378160,0.0818201799960599,0')
        self.assertEqual(gxfs[2],'"Transverse Mercator",0,117,0.9996,500000,10000000')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"AGD66 to WGS 84 (12)",-129.193,-41.212,130.73,0.246,0.374,0.329,-2.95500000002669')

        stref = gxapi.str_ref()
        ipj = gxipj.GXipj.from_dict( 'NAD27 / UTM zone 15N <500000,6000000,0,0,0,15>')
        print(ipj)
        self.assertEqual(ipj.name(),'NAD27 / UTM zone 15N (500000,6000000,0) <15 deg>')

    def test_OBLIQUESTEREO_IPJ(self):
        self.start(gsys.func_name())

        stref = gxapi.str_ref()

        ipj = gxipj.GXipj.from_json( '{"type": "Geosoft", "properties": {"datum":"NAD83,6378137,0.0818191910428158,0","projection":"\\"Oblique Stereographic\\",61.40.00,-128.10.00,1,0,0","units":"m,1","gxf5":"\\"NAD83 to WGS 84 (1)\\",0,0,0,0,0,0,0"}}')
        ipj._ipj.get_display_name(stref)
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'NAD83 / *Oblique Stereographic')
        self.assertEqual(gxfs[1],'NAD83,6378137,0.0818191910428158,0')
        self.assertEqual(gxfs[2],'"Oblique Stereographic",61.6666666666667,-128.166666666667,1,0,0')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"NAD83 to WGS 84 (1)",0,0,0,0,0,0,0')

        ipj = gxipj.GXipj.from_json( '{"type": "Localgrid", "properties": {"longitude":"-128.10.00","latitude":"61.40.00","azimuth":-15,"units":"ft"}}')
        ipj._ipj.get_display_name(stref)
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'WGS 84 / *Local grid [61.40.00,-128.10.00] <0,0,0,0,0,-15>')
        self.assertEqual(gxfs[1],'"WGS 84",6378137,0.0818191908426215,0')
        self.assertEqual(gxfs[2],'"Oblique Stereographic",61.6666666666667,-128.166666666667,0.9996,0,0')
        self.assertEqual(gxfs[3],'ft,0.3048')
        self.assertEqual(gxfs[4],'"WGS 84",0,0,0,0,0,0,0')

        ipj = gxipj.GXipj.from_json( '{"type": "Localgrid", "properties": {"longitude":"-128.10.00","latitude":"61.40.00","azimuth":-15,"units":"ft","elevation":133.1567}}')
        ipj._ipj.get_display_name(stref)
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'WGS 84 / *Local grid [61.40.00,-128.10.00] <0,0,133.1567,0,0,-15>')
        self.assertEqual(gxfs[1],'"WGS 84",6378137,0.0818191908426215,0')
        self.assertEqual(gxfs[2],'"Oblique Stereographic",61.6666666666667,-128.166666666667,0.9996,0,0')
        self.assertEqual(gxfs[3],'ft,0.3048')
        self.assertEqual(gxfs[4],'"WGS 84",0,0,0,0,0,0,0')

        ipj = gxipj.GXipj.from_json( '{"type": "Localgrid", "properties": {"longitude":0,"latitude":0}}')
        ipj._ipj.get_display_name(stref)
        print(ipj)
        gxfs = ipj.to_gxf()
        self.assertEqual(gxfs[0],'WGS 84 / *Local grid [0,0]')
        self.assertEqual(gxfs[1],'"WGS 84",6378137,0.0818191908426215,0')
        self.assertEqual(gxfs[2],'"Oblique Stereographic",0,0,0.9996,0,0')
        self.assertEqual(gxfs[3],'m,1')
        self.assertEqual(gxfs[4],'"WGS 84",0,0,0,0,0,0,0')

    def test_names_IPJ(self):
        self.start(gsys.func_name())

        ipj = gxipj.GXipj.from_json( '{"type": "Geosoft", "properties": {"datum":"NAD83,6378137,0.0818191910428158,0","projection":"Oblique Stereographic,61.40.00,-128.10.00,1,0,0","units":"m,1","gxf5":"NAD83 to WGS 84 (1),0,0,0,0,0,0,0"}}')
        print(ipj)
        coordinateSystem = ipj.dict()
        self.assertEqual(coordinateSystem["type"],'Geosoft')
        self.assertEqual(coordinateSystem["properties"]["name"],'NAD83 / *Oblique Stereographic')
        self.assertEqual(coordinateSystem["properties"]["datum"],'NAD83,6378137,0.0818191910428158,0')
        self.assertEqual(coordinateSystem["properties"]["projection"],'"Oblique Stereographic",61.6666666666667,-128.166666666667,1,0,0')
        self.assertEqual(coordinateSystem["properties"]["units"],'m,1')
        self.assertEqual(coordinateSystem["name"],'NAD83 / *Oblique Stereographic')
        self.assertEqual(coordinateSystem["baseName"],'NAD83 / *Oblique Stereographic')
        self.assertEqual(coordinateSystem["datumName"],'NAD83')
        self.assertEqual(coordinateSystem["projectionName"],'*Oblique Stereographic')
        self.assertEqual(coordinateSystem["projectionType"],'Oblique Stereographic')
        self.assertEqual(coordinateSystem["orientation"],'<0,0,0,0,0,0>')
        self.assertEqual(coordinateSystem["unitName"],'m')
        self.assertEqual(coordinateSystem["localDatumName"],'NAD83 to WGS 84 (1)')

        ipj = gxipj.GXipj.from_json( '{"type": "Geosoft", "properties": {"name":"NAD83 / UTM zone 26N"},"orientation":"<1000,500,0,0,0,15>"}')
        print(ipj)
        coordinateSystem = ipj.dict()
        self.assertEqual(coordinateSystem["type"],'Geosoft')
        self.assertEqual(coordinateSystem["properties"]["name"],'NAD83 / UTM zone 26N <1000,500,0,0,0,15>')
        self.assertEqual(coordinateSystem["properties"]["datum"],'NAD83,6378137,0.0818191910428158,0')
        self.assertEqual(coordinateSystem["properties"]["projection"],'"Transverse Mercator",0,-27,0.9996,500000,0')
        self.assertEqual(coordinateSystem["properties"]["units"],'m,1')
        self.assertEqual(coordinateSystem["name"],'NAD83 / UTM zone 26N <1000,500,0,0,0,15>')
        self.assertEqual(coordinateSystem["baseName"],'NAD83 / UTM zone 26N')
        self.assertEqual(coordinateSystem["datumName"],'NAD83')
        self.assertEqual(coordinateSystem["projectionName"],'UTM zone 26N')
        self.assertEqual(coordinateSystem["projectionType"],'Transverse Mercator')
        self.assertEqual(coordinateSystem["orientation"],'<1000,500,0,0,0,15>')
        self.assertEqual(coordinateSystem["unitName"],'m')
        self.assertEqual(coordinateSystem["localDatumName"],'NAD83 to WGS 84 (1)')

    def test_compare(self):
        self.start(gsys.func_name())

        ipj = gxipj.GXipj.from_name( 'NAD27 / UTM zone 18N')
        ipj2 = gxipj.GXipj.from_name( 'NAD27 / UTM zone 18N')
        self.assertTrue(gxipj.GXipj.compare(ipj,ipj2))
        ipj2 = gxipj.GXipj.from_name( 'NAD83 / UTM zone 18N')
        self.assertFalse(gxipj.GXipj.compare(ipj,ipj2))

    def test_units(self):
        self.start(gsys.func_name())
        ipj = gxipj.GXipj.from_name("NAD27 / Arizona Coordinate System Central zone")
        self.assertAlmostEqual(ipj.units()[0],0.304800609601219)
        self.assertEqual(ipj.units()[1],'ftUS')

    def test_PJ(self):
        self.start(gsys.func_name())

        data = np.zeros((10,5),dtype='float')
        for i in range(data.shape[0]):
            data[i,0] = 5000000.0 - i
            data[i,1] = 2000000.0 + i
            data[i,2] = 0.0 + i/2.0
            data[i,3] = -1000.0 + i
            data[i,4] = 1000.0 + i

        ipj = gxipj.GXipj.from_name( 'NAD27 / UTM zone 18N')
        ipj2 = gxipj.GXipj.from_name( 'NAD83 / UTM zone 18N')
        pj = gxipj.GXpj( ipj, ipj2)
        print(pj,'\n',pj.__repr__())

        new = data.copy()
        pj.convert(new)
        self.assertEqual(new[0,0], 5015680.1233521616)
        self.assertEqual(new[0,1], 1995617.5525243089)
        self.assertEqual(new[0,2], 0.0)
        self.assertEqual(new[4,0], 5015676.0866539562)
        self.assertEqual(new[4,1], 1995621.5795361274)
        self.assertEqual(new[4,2], 2.0)

        #test xyz only
        new = data.copy()
        pj.convert(new[:,:3])
        self.assertEqual(new[0,0], 5015680.1233521616)
        self.assertEqual(new[0,1], 1995617.5525243089)
        self.assertEqual(new[0,2], 0.0)
        self.assertEqual(new[4,0], 5015676.0866539562)
        self.assertEqual(new[4,1], 1995621.5795361274)
        self.assertEqual(new[4,2], 2.0)

        #test xy only
        new = data.copy()
        pj.convert(new[:,:2])
        self.assertEqual(new[0,0], 5015680.1233521616)
        self.assertEqual(new[0,1], 1995617.5525243089)
        self.assertEqual(new[0,2], 0.0)
        self.assertEqual(new[4,0], 5015676.0866959104)
        self.assertEqual(new[4,1], 1995621.5795778199)
        self.assertEqual(new[4,2], 2.0)

        #test integers, why not!
        new = np.zeros((10,5),dtype='int')
        new[:] = data[:]
        pj.convert(new[:,:2])
        self.assertEqual(new[0,0], 5015680)
        self.assertEqual(new[0,1], 1995617)
        self.assertEqual(new[0,2], 0)
        self.assertEqual(new[4,0], 5015676)
        self.assertEqual(new[4,1], 1995621)
        self.assertEqual(new[4,2], 2)

        #test exception
        try:
            pj.convert(new[:,0])
            self.assertTrue(False)
        except:
            self.assertTrue(True)


    def print_some_lists(self):

        # code skeleton to print lists
        dlist = gxipj.GXipj.names(gxipj.LIST_DATUM)
        for d in dlist:
            print(' "{}",\\'.format(d))
        return
        dlist = gxipj.GXipj.names(gxipj.LIST_PROJECTION)
        unitset = set()
        notfound = []
        for d in dlist:
            try:
                ipj = gxipj.GXipj.from_name( 'WGS 84 / ' + d)
                u = ipj.units()
                unitset.add(u)
                print(' "{}\":"{}",\\'.format(d,u[1]))
            except:
                print(' "{}\":"m",\\'.format(d,u))
                notfound.append(d)
        print (notfound)
        for u in unitset:
            print(' "{}":{},\\'.format(u[1],u[0]))


###############################################################################################

if __name__ == '__main__':

    unittest.main()
