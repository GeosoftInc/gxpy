import unittest
import numpy as np
import os

import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.coordinate_system as gxcs
import geosoft

from geosoft.gxpy.tests import GXPYTest


class Test(GXPYTest):

    def test_any(self):
        self.start()

        # name
        with gxcs.GXcs( 'DHDN / Okarito 2000') as cs:
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
        with gxcs.GXcs(['','DHDN','Okarito 2000','','']) as cs:
            gxfs = cs.gxf
            self.assertEqual(gxfs[0],'DHDN / Okarito 2000')
            self.assertEqual(gxfs[1],'DHDN,6377397.155,0.0816968312225275,0')
            self.assertEqual(gxfs[2],'"Transverse Mercator",-43.11,170.260833333333,1,400000,800000')
            self.assertEqual(gxfs[3],'m,1')
            self.assertEqual(gxfs[4],'"DHDN to WGS 84 (1)",582,105,414,1.04,0.35,-3.08,8.29999999996112')
            dct = cs.coordinate_dict().copy()

        # dictionary
        with gxcs.GXcs(dct) as cs:
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

        # name with a separate vcs
        with gxcs.GXcs('DHDN / Okarito 2000 [geoid]') as cs:
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), str(cs))
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), 'geoid')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), 'DHDN / Okarito 2000 [geoid]')

        # name with embedded vcs
        with gxcs.GXcs('DHDN / Okarito 2000 [geoid]') as cs:
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), str(cs))
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), 'geoid')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), 'DHDN / Okarito 2000 [geoid]')

        ipj = gxapi.GXIPJ.create()
        ipj.set_gxf('', 'DHDN', 'Okarito 2000', '', '')
        with gxcs.GXcs(ipj) as cs:
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

        with gxcs.GXcs(gxcs.GXcs(ipj)) as cs:
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

        with gxcs.GXcs( 'DHDN / Okarito 2000 [geodetic]') as cs:
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

        with gxcs.GXcs('DHDN [geoid]') as cs:
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), cs.name)
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS), cs.hcs)
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), cs.vcs)
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS), 'DHDN')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), 'geoid')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), 'DHDN [geoid]')

        with gxcs.GXcs('DHDN [geodetic]') as cs:
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), cs.name)
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS), cs.hcs)
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), cs.vcs)
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS), 'DHDN')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_VCS), 'geodetic')
            self.assertEqual(cs.cs_name(what=gxcs.NAME_HCS_VCS), 'DHDN [geodetic]')

    def test_vcs(self):
        self.start()

        self.assertEqual(gxcs.GXcs("nad83 / UTM zone 15N [NAVD92]").name, 'NAD83 / UTM zone 15N [NAVD92]')
        self.assertEqual(gxcs.GXcs("nad83 [NAVD92]").name, 'NAD83 [NAVD92]')
        self.assertFalse(gxcs.GXcs("nad83 [NAVD92]").same_as(gxcs.GXcs("NAD83 [geodetic]")))
        self.assertFalse(gxcs.GXcs("nad83 [geoid]").same_vcs(gxcs.GXcs("NAD27 [NAVD92]")))



###############################################################################################

if __name__ == '__main__':

    unittest.main()
