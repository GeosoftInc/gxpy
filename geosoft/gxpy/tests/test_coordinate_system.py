import unittest
import numpy as np
import json

import geosoft.gxapi as gxapi
import geosoft.gxpy.coordinate_system as gxcs
import geosoft.gxpy.vv as gxvv
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.spatialdata as gxspd
import geosoft.gxpy.geometry as gxgeo
import geosoft.gxpy.gx as gx

from base import GXPYTest


class Test(GXPYTest):

    def test_any(self):
        self.start()

        # name
        with gxcs.Coordinate_system( 'DHDN / Okarito 2000') as cs:
            gxfs = cs.gxf
            self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
            self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
            self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
            self.assertEqual(gxfs[3],'m,1')
            self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')
            self.assertEqual(cs.cs_name(),'DHDN / Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME),'DHDN / Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS),'DHDN / Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), '')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), 'DHDN / Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_DATUM),'DHDN')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_PROJECTION),'Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_ORIENTATION),'0,0,0,0,0,0')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_UNIT),'m')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_UNIT_FULL),'metre')

        # GXF strings
        with gxcs.Coordinate_system(['','DHDN','Okarito 2000','','']) as cs:
            gxfs = cs.gxf
            self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
            self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
            self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
            self.assertEqual(gxfs[3],'m,1')
            self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

            cs.gxf = ['', 'NAD27', '"Transverse Mercator",0,-87,0.9996,500000,0', 'm,1', '']
            self.assertEqual(cs, 'NAD27 / UTM zone 16N')

        # dictionary, json
        with gxcs.Coordinate_system('DHDN / Okarito 2000') as cs:
            dct = cs.coordinate_dict()
            with gxcs.Coordinate_system(dct) as cs:
                gxfs = cs.gxf
                self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
                self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
                self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
                self.assertEqual(gxfs[3],'m,1')
                self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

                csd = cs.coordinate_dict()
                self.assertEqual(csd['name'],'DHDN / Okarito 2000')
                self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
                self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
                self.assertEqual(gxfs[3],'m,1')
                self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

                js = cs.json
                with gxcs.Coordinate_system(js) as cs:
                    gxfs = cs.gxf
                    self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
                    self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
                    self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
                    self.assertEqual(gxfs[3],'m,1')
                    self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

                cs = gxcs.Coordinate_system()
                cs.json = '{"units": "m,1", "orientation": "", "datum": "NAD27,6378206.4,0.0822718542230039,0", "local_datum": "\\"NAD27 to WGS 84 (4)\\",-8,160,176,0,0,0,0", "projection": "\\"Transverse Mercator\\",0,-105,0.9996,500000,0", "name": "NAD27 / UTM zone 13N", "type": "Geosoft", "vcs": ""}'
                self.assertEqual(cs, 'NAD27 / UTM zone 13N')

        # ESRI wkt
        esri_wkt = 'PROJCS["Okarito_2000",GEOGCS["GCS_Deutsches_Hauptdreiecksnetz",DATUM["D_Deutsches_Hauptdreiecksnetz",SPHEROID["Bessel_1841",6377397.155,299.152812800001]],PRIMEM["Greenwich",0],UNIT["Degree",0.0174532925199432955]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",400000],PARAMETER["False_Northing",800000],PARAMETER["Central_Meridian",170.260833333333],PARAMETER["Scale_Factor",1],PARAMETER["Latitude_Of_Origin",-43.11],UNIT["Meter",1]]'
        with gxcs.Coordinate_system(esri_wkt) as cs:
            gxfs = cs.gxf
            self.assertEqual(gxfs[0],'DHDN / *Okarito 2000')
            self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225274,0')
            self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
            self.assertEqual(gxfs[3],'m,1')
            self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')

            cs.esri_wkt = 'PROJCS["NAD_1927_UTM_Zone_16N",GEOGCS["GCS_North_American_1927",DATUM["D_North_American_1927",SPHEROID["Clarke_1866",6378206.4,294.9786982]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-87.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0],AUTHORITY["EPSG",26716]]'
            self.assertEqual(cs, 'NAD27 / UTM zone 16N')

        # name with a separate vcs
        with gxcs.Coordinate_system('DHDN / Okarito 2000') as cs:
            cs.vcs = 'geoid'
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), str(cs))
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), 'geoid')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), 'DHDN / Okarito 2000 [geoid]')

        # name with embedded vcs
        with gxcs.Coordinate_system('DHDN / Okarito 2000 [geoid]') as cs:
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), str(cs))
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), 'geoid')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), 'DHDN / Okarito 2000 [geoid]')

        ipj = gxapi.GXIPJ.create()
        ipj.set_gxf('', 'DHDN', 'Okarito 2000', '', '')
        with gxcs.Coordinate_system(ipj) as cs:
            gxfs = cs.gxf
            self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
            self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
            self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
            self.assertEqual(gxfs[3],'m,1')
            self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')
            self.assertEqual(cs.cs_name(),'DHDN / Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME),'DHDN / Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS),'DHDN / Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), '')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), 'DHDN / Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_DATUM),'DHDN')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_PROJECTION),'Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_ORIENTATION),'0,0,0,0,0,0')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_UNIT),'m')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_UNIT_FULL),'metre')

        with gxcs.Coordinate_system(gxcs.Coordinate_system(ipj)) as cs:
            self.assertEqual(cs.vcs, '')
            gxfs = cs.gxf
            self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
            self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
            self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
            self.assertEqual(gxfs[3],'m,1')
            self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')
            self.assertEqual(cs.cs_name(),'DHDN / Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME),'DHDN / Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS),'DHDN / Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), '')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), 'DHDN / Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_DATUM),'DHDN')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_PROJECTION),'Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_ORIENTATION),'0,0,0,0,0,0')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_UNIT),'m')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_UNIT_FULL),'metre')

    def test_name_cs(self):
        self.start()

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

        with gxcs.Coordinate_system( 'DHDN / Okarito 2000 [geodetic]') as cs:
            gxfs = cs.gxf
            self.assertEqual(gxfs[0],'DHDN / Okarito 2000 [geodetic]')
            self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
            self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
            self.assertEqual(gxfs[3],'m,1')
            self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')
            self.assertEqual(cs.cs_name(),'DHDN / Okarito 2000 [geodetic]')
            self.assertEqual(cs.cs_name(what=gxcs.NAME),'DHDN / Okarito 2000 [geodetic]')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS),'DHDN / Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), 'geodetic')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_DATUM),'DHDN')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_PROJECTION),'Okarito 2000')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_ORIENTATION),'0,0,0,0,0,0')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_UNIT),'m')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_UNIT_FULL),'metre')

        with gxcs.Coordinate_system('DHDN [geoid]') as cs:
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), cs.name)
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS), cs.hcs)
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), cs.vcs)
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS), 'DHDN')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), 'geoid')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), 'DHDN [geoid]')

        with gxcs.Coordinate_system('DHDN [geodetic]') as cs:
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), cs.name)
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS), cs.hcs)
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), cs.vcs)
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS), 'DHDN')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), 'geodetic')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), 'DHDN [geodetic]')

    def test_vcs(self):
        self.start()

        self.assertEqual(gxcs.Coordinate_system("nad83 / UTM zone 15N [NAVD92]").name, 'NAD83 / UTM zone 15N [NAVD92]')
        self.assertEqual(gxcs.Coordinate_system("nad83 [NAVD92]").name, 'NAD83 [NAVD92]')
        self.assertFalse(gxcs.Coordinate_system("nad83 [NAVD92]").same_as(gxcs.Coordinate_system("NAD83 [geodetic]")))
        self.assertFalse(gxcs.Coordinate_system("nad83 [geoid]").same_vcs(gxcs.Coordinate_system("NAD27 [NAVD92]")))

    def test_pj(self):
        self.start()

        with gxcs.Coordinate_system('DHDN / Okarito 2000') as cs:
            with gxcs.Coordinate_system('DHDN') as csll:
                with gxcs.Coordinate_translate(cs, csll) as pj:

                    lon, lat = pj.convert((500000, 6500000))
                    self.assertAlmostEqual(lon, 171)
                    self.assertAlmostEqual(lat, 8)

                    lon, lat = pj.convert((500000., 6500000.))
                    self.assertAlmostEqual(lon, 171.168823147)
                    self.assertAlmostEqual(lat, 8.36948254242)

                    ll = pj.convert(np.array([500000., 6500000.], dtype=np.float32))
                    self.assertAlmostEqual(ll[0], 171.16882, 5)
                    self.assertAlmostEqual(ll[1], 8.36948, 5)

                    lon, lat, z = pj.convert((500000., 6500000., 50.))
                    self.assertAlmostEqual(lon, 171.168823147)
                    self.assertAlmostEqual(lat, 8.36948254242)
                    self.assertAlmostEqual(z, 50)

                    ll = pj.convert([[500000., 6500000.], [505000., 6510000.]])
                    self.assertAlmostEqual(ll[0][0], 171.168823147)
                    self.assertAlmostEqual(ll[0][1], 8.36948254242)
                    self.assertAlmostEqual(ll[1][0], 171.214439577)
                    self.assertAlmostEqual(ll[1][1], 8.45978927383)

                    ll = pj.convert(np.array([[500000., 6500000.], [505000., 6510000.]]))
                    self.assertTrue(type(ll) is np.ndarray)
                    self.assertAlmostEqual(ll[0][0], 171.168823147)
                    self.assertAlmostEqual(ll[0][1], 8.36948254242)
                    self.assertAlmostEqual(ll[1][0], 171.214439577)
                    self.assertAlmostEqual(ll[1][1], 8.45978927383)

                    vvx = gxvv.GXvv([500000., 505000.])
                    vvy = gxvv.GXvv([6500000., 6510000.])
                    pj.convert_vv(vvx, vvy)
                    self.assertAlmostEqual(vvx[0][0], 171.168823147)
                    self.assertAlmostEqual(vvy[0][0], 8.36948254242)
                    self.assertAlmostEqual(vvx[1][0], 171.214439577)
                    self.assertAlmostEqual(vvy[1][0], 8.45978927383)

    def test_local_dict(self):
        self.start()

        self.assertRaises(gxcs.CSException, gxcs.Coordinate_system, {'type': 'local'})

        csdict = {'type': 'local', 'lon_lat': (-96,43)}
        csd = gxcs.Coordinate_system(csdict)
        self.assertEqual(csd.name, 'WGS 84 / *Local(43,-96,0,0)')

        with gxcs.Coordinate_translate(csd, gxcs.Coordinate_system('WGS 84')) as pj:
            lon, lat, z = pj.convert((0, 0, 0))
            self.assertAlmostEqual(lat, 43)
            self.assertAlmostEqual(lon, -96)
            self.assertAlmostEqual(z, 0)

        csdict['azimuth'] = 25
        csd = gxcs.Coordinate_system(csdict)
        self.assertEqual(csd.name, 'WGS 84 / *Local(43,-96,0,0) <0,0,0,0,0,25>')
        self.assertEqual(csd.gxf[2], '"Oblique Stereographic",43,-96,0.9996,0,0')

        with gxcs.Coordinate_translate(gxcs.Coordinate_system('WGS 84'), csd) as pj:
            x, y, z = pj.convert((-96., 43., 0))
            self.assertAlmostEqual(x, 0)
            self.assertAlmostEqual(y, 0)
            self.assertAlmostEqual(z, 0)
            x, y, z = pj.convert((-95., 43., 0.))
            self.assertAlmostEqual(x, 73665.899715)
            self.assertAlmostEqual(y, 34886.2319719)
            self.assertAlmostEqual(z, 0)

        csdict['origin'] = (1800, 500)
        csd = gxcs.Coordinate_system(csdict)
        self.assertEqual(csd.name, 'WGS 84 / *Local(43,-96,1800,500) <0,0,0,0,0,25>')
        self.assertEqual(csd.gxf[2], '"Oblique Stereographic",43,-96,0.9996,1842.66314753632,-307.558977614934')

        csdict['elevation'] = 800.5
        csdict['vcs'] = 'geoid'
        csd = gxcs.Coordinate_system(csdict)
        self.assertEqual(csd.name, 'WGS 84 / *Local(43,-96,1800,500) <0,0,800.5,0,0,25>')
        self.assertEqual(csd.gxf[2], '"Oblique Stereographic",43,-96,0.9996,1842.66314753632,-307.558977614934')
        with gxcs.Coordinate_translate(gxcs.Coordinate_system('WGS 84'), csd) as pj:
            x, y = pj.convert((-96., 43.))
            self.assertAlmostEqual(x, 1800)
            self.assertAlmostEqual(y, 500)
        with gxcs.Coordinate_translate(csd, gxcs.Coordinate_system('WGS 84')) as pj:
            lon, lat, z = pj.convert((1800., 500., 0.))
            self.assertAlmostEqual(lat, 43)
            self.assertAlmostEqual(lon, -96)
            self.assertAlmostEqual(z, 800.5)

    def test_local(self):
        self.start()

        csd = gxcs.Coordinate_system.local(lon_lat=(-96, 43))
        self.assertEqual(csd.name, 'WGS 84 / *Local(43,-96,0,0)')

        with gxcs.Coordinate_translate(csd, gxcs.Coordinate_system('WGS 84')) as pj:
            lon, lat, z = pj.convert((0, 0, 0))
            self.assertAlmostEqual(lat, 43)
            self.assertAlmostEqual(lon, -96)
            self.assertAlmostEqual(z, 0)

        csd = gxcs.Coordinate_system.local(lon_lat=(-96, 43), azimuth=25)
        self.assertEqual(csd.name, 'WGS 84 / *Local(43,-96,0,0) <0,0,0,0,0,25>')
        self.assertEqual(csd.gxf[2], '"Oblique Stereographic",43,-96,0.9996,0,0')

        with gxcs.Coordinate_translate(gxcs.Coordinate_system('WGS 84'), csd) as pj:
            x, y, z = pj.convert((-96., 43., 0))
            self.assertAlmostEqual(x, 0)
            self.assertAlmostEqual(y, 0)
            self.assertAlmostEqual(z, 0)
            x, y, z = pj.convert((-95., 43., 0.))
            self.assertAlmostEqual(x, 73665.899715)
            self.assertAlmostEqual(y, 34886.2319719)
            self.assertAlmostEqual(z, 0)

        csd = gxcs.Coordinate_system.local(lon_lat=(-96, 43), azimuth=25, origin=(1800, 500))
        self.assertEqual(csd.name, 'WGS 84 / *Local(43,-96,1800,500) <0,0,0,0,0,25>')
        self.assertEqual(csd.gxf[2], '"Oblique Stereographic",43,-96,0.9996,1842.66314753632,-307.558977614934')

        csd = gxcs.Coordinate_system.local(lon_lat=(-96, 43), azimuth=25, origin=(1800, 500),
                                           elevation=800.5, vcs='geoid')
        self.assertEqual(csd.name, 'WGS 84 / *Local(43,-96,1800,500) <0,0,800.5,0,0,25>')
        self.assertEqual(csd.gxf[2], '"Oblique Stereographic",43,-96,0.9996,1842.66314753632,-307.558977614934')
        with gxcs.Coordinate_translate(gxcs.Coordinate_system('WGS 84'), csd) as pj:
            x, y = pj.convert((-96., 43.))
            self.assertAlmostEqual(x, 1800)
            self.assertAlmostEqual(y, 500)
        with gxcs.Coordinate_translate(csd, gxcs.Coordinate_system('WGS 84')) as pj:
            lon, lat, z = pj.convert((1800., 500., 0.))
            self.assertAlmostEqual(lat, 43)
            self.assertAlmostEqual(lon, -96)
            self.assertAlmostEqual(z, 800.5)

        datum = 'NAD27'
        local_datum = '[NAD27] (10m) USA - CONUS - onshore'
        csd = gxcs.Coordinate_system.local(lon_lat=(-96, 43), azimuth=25, origin=(1800, 500),
                                           datum='NAD83', local_datum=local_datum,
                                           elevation=800.5, vcs='geoid')
        self.assertEqual(csd.name, 'NAD83 / *Local(43,-96,1800,500) <0,0,800.5,0,0,25>')
        self.assertEqual(csd.gxf[4], '"NAD83 to WGS 84 (1)",0,0,0,0,0,0,0')

    def test_oriented(self):
        self.start()

        with gxcs.Coordinate_system({'type': 'local', 'lon_lat': (-96., 43.), 'azimuth':25}) as cs:

            self.assertTrue(cs.is_oriented)

            xyzo = (10., 0., 0.)
            xyz = cs.xyz_from_oriented(xyzo)
            self.assertEqual(xyz, (9.063077870366499, -4.2261826174069945, 0.0))

            xyz = (9.063077870366499, -4.2261826174069945, 0.0)
            xyz = cs.oriented_from_xyz(xyz)
            self.assertAlmostEqual(xyz[0], xyzo[0])
            self.assertAlmostEqual(xyz[1], xyzo[1])
            self.assertAlmostEqual(xyz[2], xyzo[2])

            xyzo = ((10., 0., 0.), (0., 10.,5.))
            xyz = cs.xyz_from_oriented(xyzo)
            self.assertEqual(tuple(xyz[0]), (9.063077870366499, -4.2261826174069945, 0.0))
            self.assertEqual(tuple(xyz[1]), (4.2261826174069945, 9.0630778703664987, 5.0))

            xyz = ((9.063077870366499, -4.2261826174069945, 0.0), (4.2261826174069945, 9.0630778703664987, 5.0))
            xyz = cs.oriented_from_xyz(xyz)
            self.assertAlmostEqual(xyz[0][0], xyzo[0][0])
            self.assertAlmostEqual(xyz[0][1], xyzo[0][1])
            self.assertAlmostEqual(xyz[0][2], xyzo[0][2])

            xyzo = ((10., 0.), (0., 10.), (0., 5.))
            xyz = cs.xyz_from_oriented(xyzo, column_ordered=True)
            self.assertEqual(tuple(xyz[0]), (9.063077870366499, 4.2261826174069945))
            self.assertEqual(tuple(xyz[1]), (-4.2261826174069945, 9.063077870366499))
            self.assertEqual(tuple(xyz[2]), (0.0, 5.0))

            self.assertTrue(cs == gxcs.Coordinate_system({'type': 'local', 'lon_lat': (-96., 43.), 'azimuth': 25}))
            self.assertFalse(cs == gxcs.Coordinate_system({'type': 'local', 'lon_lat': (-96., 43.), 'azimuth': 20}))

    def test_parameters(self):
        self.start()

        self.assertTrue(gxcs.parameter_exists(gxcs.PARM_DATUM, 'NAD83'))
        self.assertTrue(gxcs.parameter_exists(gxcs.PARM_PROJECTION, 'UTM zone 15N'))
        self.assertTrue(gxcs.parameter_exists(gxcs.PARM_UNITS, 'ftUS'))
        self.assertTrue(gxcs.parameter_exists(gxcs.PARM_LOCAL_DATUM, gxcs.name_list(gxcs.LIST_LOCALDATUMNAME)[5]))
        self.assertFalse(gxcs.parameter_exists(gxcs.PARM_UNITS, 'hoofs'))

        params = gxcs.parameters(gxcs.PARM_DATUM, 'WGS 84')
        self.assertTrue('ELLIPSOID' in params)

        params = gxcs.parameters(gxcs.PARM_PROJECTION, 'UTM zone 15N')
        self.assertEqual(float(params['P5']), 0.9996)

    def test_unit_only(self):
        self.start()

        with gxcs.Coordinate_system('cm') as cs:
            self.assertEqual(str(cs), '*unknown')
            self.assertEqual(cs.gxf[3], 'cm,0.01')
            self.assertEqual(cs.unit_of_measure, 'cm')
            self.assertEqual(cs.units_name, cs.unit_of_measure)

    def test_array(self):
        self.start()

        # define coordinate systems and a transformer
        cs_utm = gxcs.Coordinate_system('NAD83 / UTM zone 15N')
        cs_nad27 = gxcs.Coordinate_system('NAD27')
        cs_transform = gxcs.Coordinate_translate(cs_utm, cs_nad27)

        # example transform a single (x, y) coordinate
        lon_lat = cs_transform.convert((345000., 64250000.))
        self.assertEqual(tuple(lon_lat), (88.777242210445195, -38.498998514257273))

        # example transform a single (x, y, elevation) coordinate
        ct = cs_transform.convert((345000., 64250000., 50))
        self.assertAlmostEqual(ct[0], 88.77724221146941)
        self.assertAlmostEqual(ct[1], -38.49899848105302)
        self.assertAlmostEqual(ct[2], 50.0)

        # example translate a list of (x, y, z) tuples
        locations = [(345000, 64250000, 50), (345500, 64250000, 60), (346000, 64250000, 70)]
        nad27_locations = cs_transform.convert(locations)
        self.assertEqual(len(nad27_locations), 3)
        ct = nad27_locations[2]
        self.assertAlmostEqual(ct[0], 89)
        self.assertAlmostEqual(ct[1], -38)
        self.assertAlmostEqual(ct[2], 70)

        # example transform a numpy array in-place
        data = np.array([[345000, 64250000, 50, 55000],
                         [345500, 64250000, 60, 55150],
                         [346000, 64250000, 70, 56000]],
                        dtype=float)
        nad27_locations = cs_transform.convert(data, in_place=True)
        self.assertEqual(len(nad27_locations), 3)
        ct = nad27_locations[2]
        self.assertAlmostEqual(ct[0], 8.87657800e+01)
        self.assertAlmostEqual(ct[1], -3.84991719e+01)
        self.assertAlmostEqual(ct[2], 7.00000000e+01)
        self.assertAlmostEqual(ct[3], 5.60000000e+04)

    def test_known(self):
        self.start()

        self.assertFalse(gxcs.is_known(None))
        self.assertTrue(gxcs.is_known('WGS 84'))
        self.assertTrue(gxcs.is_known(gxcs.Coordinate_system('WGS 84')))
        self.assertFalse(gxcs.is_known('crazy'))

    def test_from_xml(self):
        self.start()

        temp_grid = gx.gx().temp_file('grd')
        cs = gxcs.Coordinate_system('NAD27 / UTM zone 18N')
        with gxgrd.Grid.new(temp_grid,
                            properties={'dtype': np.int16,
                                        'nx': 100, 'ny': 50,
                                        'x0': 4, 'y0': 8,
                                        'dx': 0.1, 'dy': 0.2,
                                        'rot': 5,
                                        'coordinate_system': cs}) as grd:
            pass
        cs = gxspd.coordinate_system_from_metadata_file(temp_grid)
        self.assertEqual(str(cs), 'NAD27 / UTM zone 18N')

        gxf = cs.gxf.copy()
        gxf[0] = 'crazy'
        gxf[1] = 'weird,6378206.4,0.0822718542230039,0'
        cs = gxcs.Coordinate_system(gxf)
        with gxgrd.Grid.new(temp_grid, overwrite=True,
                            properties={'dtype': np.int16,
                                        'nx': 100, 'ny': 50,
                                        'x0': 4, 'y0': 8,
                                        'dx': 0.1, 'dy': 0.2,
                                        'rot': 5,
                                        'coordinate_system': cs}) as grd:
            pass
        cs = gxspd.coordinate_system_from_metadata_file(temp_grid)
        self.assertEqual(str(cs), 'weird / UTM zone 18N')


###############################################################################################

if __name__ == '__main__':

    unittest.main()
