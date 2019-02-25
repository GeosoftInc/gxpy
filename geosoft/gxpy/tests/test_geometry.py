import unittest
import os
import numpy as np
import json

import geosoft
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.geometry as gxgeo
import geosoft.gxpy.vv as gxvv
import geosoft.gxpy.coordinate_system as gxcs

from base import GXPYTest


class Test(GXPYTest):
    def test_version(self):
        self.start()
        self.assertEqual(gxmap.__version__, geosoft.__version__)

    def test_exception(self):
        self.start()

        self.assertRaises(ValueError, gxgeo.Point, [1, 'yada', 2])

    def test_base(self):
        self.start()
        g = gxgeo.Geometry()
        self.assertEqual(g.name, '_geometry_')
        self.assertEqual(g.coordinate_system, None)
        self.assertEqual(g.extent, None)
        self.assertEqual(g.extent_xyz, (None, None, None, None, None, None))
        self.assertEqual(g.extent_xy, (None, None, None, None))
        self.assertEqual(g.dimension, (None, None, None))
        self.assertEqual(g.dimension_xy, (None, None))
        self.assertEqual(g.centroid, None)
        self.assertEqual(g.centroid_xyz, (None, None, None))
        self.assertEqual(g.centroid_xy, (None, None))

    def test_new_point(self):
        self.start()

        p = gxgeo.Point((5, 10))
        self.assertEqual(p.xyz, (5, 10, 0))
        self.assertEqual(len(p), 1)
        self.assertEqual(tuple(p.pp[0]), (5, 10, 0))
        p = gxgeo.Point((5, 10), z=2)
        self.assertEqual(p.xyz, (5, 10, 2))
        p = gxgeo.Point((5, 10, 2))
        self.assertEqual(p.xyz, (5, 10, 2))
        p = gxgeo.Point(np.array((5, 10), dtype=np.float64))
        self.assertEqual(p.xyz, (5, 10, 0))
        p = gxgeo.Point(np.array((5, 10), dtype=np.float64), z=2)
        self.assertEqual(p.xyz, (5, 10, 2))
        p = gxgeo.Point(np.array((5, 10, 2), dtype=np.float64))
        self.assertEqual(p.xyz, (5, 10, 2))
        self.assertEqual(p.x, 5)
        self.assertEqual(p.y, 10)
        self.assertEqual(p.z, 2)
        p.x = 2.5
        self.assertEqual(p.x, 2.5)
        self.assertEqual(p.y, 10)
        self.assertEqual(p.z, 2)
        p.y = 7.5
        self.assertEqual(p.x, 2.5)
        self.assertEqual(p.y, 7.5)
        self.assertEqual(p.z, 2)
        p.z = 3.3
        self.assertEqual(p.x, 2.5)
        self.assertEqual(p.y, 7.5)
        self.assertEqual(p.z, 3.3)

    def test_cs(self):
        self.start()

        p = gxgeo.Point((5, 10))
        self.assertTrue(p == p)
        self.assertTrue(gxgeo.Point((1,2), coordinate_system="WGS 84") == gxgeo.Point((1,2), coordinate_system="WGS 84"))
        self.assertTrue(gxgeo.Point((1, 2), coordinate_system="WGS 84") == gxgeo.Point((1, 2)))
        self.assertTrue(gxgeo.Point((1, 2)) == gxgeo.Point((1, 2)))

        s = "WGS 84 / UTM zone 32N <0, 0, 0, 10, 15, 32>"
        p = gxgeo.Point((5,10), coordinate_system=s)
        hcsd = p.coordinate_system.coordinate_dict()
        self.assertEqual(hcsd['name'], "WGS 84 / UTM zone 32N <0,0,0,10,15,32>")
        self.assertTrue(p == p)

        s = s + ' [geoid]'
        pp = gxgeo.PPoint(((8, 12), (5, 10)), coordinate_system=s)
        hcsd = p.coordinate_system.coordinate_dict()
        self.assertEqual(hcsd['name'], "WGS 84 / UTM zone 32N <0,0,0,10,15,32>")
        self.assertEqual(pp.coordinate_system.vcs, "geoid")
        self.assertTrue(pp == pp)
        self.assertTrue(pp == gxgeo.PPoint(((8, 12), (5, 10))))
        self.assertFalse(pp == gxgeo.PPoint(((8, 12), (5, 10)), coordinate_system='WGS 84 [geoid]'))
        self.assertFalse(gxgeo.PPoint(((8, 12), (5, 10)), coordinate_system='WGS 84 [geoid]') == pp)

    def test_point(self):
        self.start()

        p = gxgeo.Point((5,10))
        self.assertEqual(p.p.tolist(), [5.0, 10.0, 0.0])
        self.assertEqual(p.xy, (5.0,10.0))
        self.assertEqual(p.xyz, (5.0, 10.0, 0.0))
        self.assertEqual(p.x, 5.0)
        self.assertEqual(p.y, 10.0)
        self.assertEqual(p.z, 0.0)

        p -= (0, 0, 15)
        self.assertEqual(p.xyz, (5.0, 10.0, -15.0))

        p = gxgeo.Point((5,10,3.5))
        self.assertEqual(p.p.tolist(), [5.0, 10.0, 3.5])
        self.assertEqual(p.xyz, (5.0, 10.0, 3.5))
        self.assertEqual(p.x, 5.0)
        self.assertEqual(p.y, 10.0)
        self.assertEqual(p.z, 3.5)

        p = gxgeo.Point(4)
        self.assertEqual(p.xyz, (4.0, 4.0, 4.0))

        p += (1, 2, 3)
        self.assertEqual(p.xyz, (5., 6., 7.))

        p *= 2
        self.assertEqual(p.xyz, (10., 12., 14.))

        p /= 2
        self.assertEqual(p.xyz, (5., 6., 7.))

        p = -p
        self.assertEqual(p.xyz, (-5., -6., -7.))

        p = p + 1
        self.assertEqual(p.xyz, (-4., -5., -6.))

        p = p + (1, 2)
        self.assertEqual(p.xyz, (-3., -3., -6.))

        p = p + (5, 2, 6)
        self.assertEqual(p.xyz, (2., -1., 0.))

        p.x = p.x + 2
        p.y -= 2
        p.z = 5
        self.assertEqual(p.xyz, (4., -3., 5.))

        p.xy = (99, '88')
        self.assertEqual(p.xyz, (99., 88., 5.))

        p.xyz = [0, 1, 45]
        self.assertEqual(p.xyz, (0., 1., 45.))

    def test_ppoint(self):
        self.start()

        points = [(5, 10), (6, 11), (7, 12)]
        pp = gxgeo.PPoint(points)
        self.assertEqual(len(pp), 3)
        i = 0
        for p in pp:
            self.assertEqual(p.xy, points[i])
            i += 1
        i = 0
        for p in pp:
            self.assertEqual(p.xyz, (points[i][0], points[i][1], 0.0))
            i += 1

        p = pp[1]
        self.assertEqual(p.xy, points[1])

        pp -= (0, 0, 15)
        self.assertEqual(pp[0].xyz, (5.0, 10.0, -15.0))
        self.assertEqual(pp[2].xyz, (7.0, 12.0, -15.0))

        pp += gxgeo.Point((0, 0, 15))
        self.assertEqual(pp[0].xyz, (5.0, 10.0, 0.0))
        self.assertEqual(pp[2].xyz, (7.0, 12.0, 0.0))

        px = pp + gxgeo.PPoint(((0, 0, 15), (-1, -1, -10), (1, 2, 3)))
        self.assertEqual(px[0].xyz, (5.0, 10.0, 15.0))
        self.assertEqual(px[2].xyz, (8.0, 14.0, 3.0))


        pp -= gxgeo.PPoint(((0, 0, 15), (-1, -1, -10), (0, 0, 0)))
        self.assertEqual(pp[0].xyz, (5.0, 10.0, -15.0))
        self.assertEqual(pp[1].xyz, (7, 12, 10))
        self.assertEqual(pp[2].xyz, (7., 12., 0.))

        pp -= gxgeo.Point((1, 2, 3))
        self.assertEqual(pp[0].xyz, (4.0, 8.0, -18.0))
        self.assertEqual(pp[1].xyz, (6, 10, 7))
        self.assertEqual(pp[2].xyz, (6., 10., -3.))

        pp = gxgeo.PPoint([(5, 10, 3.5)])
        self.assertEqual(pp[0].xyz, (5.0, 10.0, 3.5))

        pp = gxgeo.PPoint(((1, 2, 3), (4, 5, 6), (7, 8, 9)))

        pp += (1, 2, 3)
        self.assertEqual(pp[0].xyz, (2., 4., 6.))
        self.assertEqual(pp[2].xyz, (8., 10., 12.))

        pp *= (1, 2, 3)
        pp /= (1, 2, 3)
        self.assertEqual(pp[0].xyz, (2., 4., 6.))
        self.assertEqual(pp[2].xyz, (8., 10., 12.))
        pp *= (1, 2, 3)
        pp /= gxgeo.Point((1, 2, 3))
        self.assertEqual(pp[0].xyz, (2., 4., 6.))
        self.assertEqual(pp[2].xyz, (8., 10., 12.))
        pp *= (1, 2, 3)
        p = gxgeo.Point((1, 2, 3))
        pp /= gxgeo.PPoint((p, p, p))
        self.assertEqual(pp[0].xyz, (2., 4., 6.))
        self.assertEqual(pp[2].xyz, (8., 10., 12.))

        pp *= gxgeo.Point((-1, -1, -1))
        self.assertEqual(pp[0].xyz, (-2., -4., -6.))
        self.assertEqual(pp[2].xyz, (-8., -10., -12.))
        pp = -pp

        pp *= 2
        self.assertEqual(pp[1].xyz, (10., 14., 18.))

        pp /= 2
        self.assertEqual(pp[1].xyz, (5., 7., 9.))

        pp = -pp
        self.assertEqual(pp[1].xyz, (-5., -7., -9.))

        pp = pp + (1, 2)
        self.assertEqual(pp[1].xyz, (-4., -5., -9.))

        pp = pp + (5, 2, 6)
        self.assertEqual(pp[1].xyz, (1., -3., -3.))

        pp = pp + ((1, 2, 3), (4, 5, 6), (7, 8, 9))
        self.assertEqual(pp[1].xyz, (5., 2., 3.))

        pp = pp * gxgeo.PPoint(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
        self.assertEqual(pp[1].xyz, (20., 10., 18.))
        self.assertEqual(len(pp), 3)
        self.assertEqual(tuple(pp.x), (5., 20., 35.))
        self.assertEqual(tuple(pp.y), (4., 10., 16.))
        self.assertEqual(tuple(pp.z), (9., 18., 27.))

        points = [(5, 10), (6, 11), (7, 12)]
        pp = gxgeo.PPoint(points, z=3.5)
        self.assertEqual(pp.x.tolist(), [5., 6., 7.])
        self.assertEqual(pp.z.tolist(), [3.5, 3.5, 3.5])
        self.assertEqual(pp.xy.tolist(), np.array(points).tolist())

        pp.x = 4.8
        pp.y = (8., 5., 3.)
        pp.z = (1., 2., "-3")
        self.assertEqual(pp.x.tolist(), [4.8, 4.8, 4.8])
        self.assertEqual(pp.y.tolist(), [8., 5., 3.])
        self.assertEqual(pp.z.tolist(), [1., 2., -3.])

        pp.xy = [(1, 2), (3,4), (5,6)]
        self.assertEqual(pp.xy.tolist(), [[1., 2.], [3., 4.], [5., 6.]])

        pp = gxgeo.PPoint(((500000, 6000000), (500001, 6000001)), coordinate_system='NAD83 / UTM zone 15N')
        pp27 = gxgeo.PPoint(pp, coordinate_system='NAD27 / UTM zone 15N')
        self.assertEqual(pp27[0].xyz, (500016.35614845896, 5999777.5863711238, 0.0))
        self.assertEqual(pp27[1].xyz, (500017.35614260647, 5999778.5863652565, 0.0))
        self.assertEqual(pp27.length, 2)

    def test_pp_cs(self):
        self.start()

        p0 = gxgeo.Point((500000, 6000000))
        p1 = gxgeo.Point((500000, 6000000), coordinate_system='NAD83 / UTM zone 15N')
        p2 = gxgeo.Point((500000, 6000000), coordinate_system='NAD27 / UTM zone 15N')
        pp = gxgeo.PPoint((p0, p1, p2))
        self.assertEqual(pp.coordinate_system, 'NAD83 / UTM zone 15N')
        self.assertEqual(pp[0].xyz, (500000, 6000000, 0))
        self.assertEqual(pp[1].xyz, (500000, 6000000, 0))
        self.assertEqual(pp[2].xyz, (499983.64366013405, 6000222.4158355873, 0.0))
        pp = gxgeo.PPoint((p0, p2, p1))
        self.assertEqual(pp.coordinate_system, 'NAD27 / UTM zone 15N')
        self.assertEqual(pp[0].xyz, (500000, 6000000, 0))
        self.assertEqual(pp[1].xyz, (500000, 6000000, 0))
        self.assertEqual(pp[2].xyz, (500016.35614845896, 5999777.5863711238, 0.0))
        pp = gxgeo.PPoint((p0, p1, p2), coordinate_system='NAD27 / UTM zone 15N')
        self.assertEqual(pp.coordinate_system, 'NAD27 / UTM zone 15N')
        self.assertEqual(pp[0].xyz, (500000, 6000000, 0))
        self.assertEqual(pp[1].xyz, (500016.35614845896, 5999777.5863711238, 0.0))
        self.assertEqual(pp[2].xyz, (500000, 6000000, 0))


    def test_ppoint_constructors(self):
        self.start()

        def verify():
            self.assertEqual(pp.x.tolist(), [1., 4., 7., 10., 13.])
            self.assertEqual(pp.z.tolist(), [3., 6., 9., 12., 15.])
            self.assertEqual(pp.xy.tolist(), nppp[:, :2].tolist())

        lpp = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15))
        nppp = np.array(lpp)
        pp = gxgeo.PPoint(lpp)
        verify()

        nppp = np.array(lpp)
        pp = gxgeo.PPoint(nppp)
        verify()

        vvx = gxvv.GXvv(nppp[:, 0])
        vvy = gxvv.GXvv(nppp[:, 1])
        vvz = gxvv.GXvv(nppp[:, 2])
        pp = gxgeo.PPoint((vvx, vvy, vvz))
        verify()
        pp = gxgeo.PPoint((vvx, vvy), z=5)
        self.assertEqual(pp.x.tolist(), [1., 4., 7., 10., 13.])
        self.assertEqual(pp.z.tolist(), [5, 5, 5, 5, 5])

        vvx, vvy, vvz = pp. make_xyz_vv()
        self.assertEqual(tuple(vvx), ((1, 0.0), (4, 1.0), (7, 2.0), (10, 3.0), (13, 4.0)))
        self.assertEqual(tuple(vvy), ((2, 0.0), (5, 1.0), (8, 2.0), (11, 3.0), (14, 4.0)))
        self.assertEqual(tuple(vvz), ((5.0, 0.0), (5.0, 1.0), (5.0, 2.0), (5.0, 3.0), (5.0, 4.0)))

        pps = []
        for xyz in lpp:
            pps.append(gxgeo.Point(xyz))
        pp = gxgeo.PPoint(pps)
        verify()

        e = pp.extent
        self.assertTrue(e[0] == gxgeo.Point((1, 2, 3)))
        self.assertTrue(e[1] == gxgeo.Point((13, 14, 15)))

    def test_copy_geometry(self):
        self.start()

        p1 = gxgeo.Point((1,2))
        p2 = p1
        self.assertTrue(p1 is p2)
        p2 = gxgeo.Point(p2)
        self.assertFalse(p1 is p2)
        self.assertTrue(p1 == p2)

        p2.cs = "WGS 84"
        self.assertTrue(p1 == p2)
        p1.cs = "WGS 84"
        self.assertTrue(p1 == p2)
        p1.cs = gxcs.Coordinate_system("WGS 84 [geoid]")
        self.assertTrue(p1 == p2)

    def test_p2(self):
        self.start()

        b1 = gxgeo.Point2((gxgeo.Point((0, 1)), (10, 20, -1)))
        self.assertEqual(len(b1), 2)
        self.assertEqual(tuple(b1.pp[0]), (0, 1, 0))
        self.assertEqual(tuple(b1.pp[1]), (10, 20, -1))
        self.assertEqual(b1.centroid.xyz, (5.0, 10.5, -0.5))
        self.assertEqual(len(b1), 2)
        self.assertEqual('_point2_[(0.0, 1.0, 0.0) (10.0, 20.0, -1.0)]', str(b1))
        self.assertEqual(b1.x2, (0., 10.))
        self.assertEqual(b1.y2, (1., 20.))
        self.assertEqual(b1.z2, (0, -1.))

        b2 = gxgeo.Point2(((0, 1), (10, 20, -1)))
        self.assertTrue(b1 == b2)

        b1 = gxgeo.Point2((gxgeo.Point((0, 1, -20)),(10, 20, -1)))
        self.assertEqual('_point2_[(0.0, 1.0, -20.0) (10.0, 20.0, -1.0)]', str(b1))
        self.assertEqual(b1.x2, (0., 10.))
        self.assertEqual(b1.y2, (1., 20.))
        self.assertEqual(b1.z2, (-20., -1.))
        b2 = gxgeo.Point2((gxgeo.Point((b1.x2[0], b1.y2[0], b1.z2[0])),
                         gxgeo.Point((b1.x2[1], b1.y2[1], b1.z2[1]))))
        self.assertTrue(b1 == b2)
        b2 = gxgeo.Point2((gxgeo.Point((b1.x2[1], b1.y2[1], b1.z2[1])),
                         gxgeo.Point((b1.x2[0], b1.y2[0], b1.z2[0]))), coordinate_system="WGS 84")
        self.assertTrue(b1 == b2)
        b2 = gxgeo.Point2(((b1.x2[1], b1.y2[1], b1.z2[1]), (b1.x2[0], b1.y2[0], b1.z2[0])), coordinate_system="WGS 84")
        self.assertTrue(b1 == b2)
        b2 = gxgeo.Point2((b1.x2[1], b1.y2[1], b1.z2[1], b1.x2[0], b1.y2[0], b1.z2[0]), coordinate_system="WGS 84")
        self.assertTrue(b1 == b2)

        c = gxgeo.Point(((b2.p0.x + b2.p1.x) * 0.5,
                        (b2.p0.y + b2.p1.y) * 0.5,
                        (b2.p0.z + b2.p1.z) * 0.5))
        self.assertEqual(b2.centroid, c)
        self.assertEqual(b2.dimension, (abs(b2.p1.x - b2.p0.x), abs(b2.p1.y - b2.p0.y), abs(b2.p1.z - b2.p0.z)))
        self.assertEqual(b2.dimension_xy, (abs(b2.p1.x - b2.p0.x), abs(b2.p1.y - b2.p0.y)))
        self.assertEqual(b2.extent_xyz, (0.0, 1.0, -20.0, 10.0, 20.0, -1.0))
        self.assertEqual(b2.extent_xy, (0.0, 1.0, 10.0, 20.0))

        b = gxgeo.Point2(5)
        self.assertEqual(b[0].xyz, (5, 5, 5))
        self.assertEqual(b[1].xyz, (5, 5, 5))
        b = gxgeo.Point2((5, 6))
        self.assertEqual(b[0].xyz, (5, 6, 0))
        self.assertEqual(b[1].xyz, (5, 6, 0))
        b = gxgeo.Point2((5, 6, 7))
        self.assertEqual(b[0].xyz, (5, 6, 7))
        self.assertEqual(b[1].xyz, (5, 6, 7))
        b = gxgeo.Point2((5, 6, 7, 8))
        self.assertEqual(b[0].xyz, (5, 6, 0))
        self.assertEqual(b[1].xyz, (7, 8, 0))
        b = gxgeo.Point2((5, 6, 7, 8, 9, 0))
        self.assertEqual(b[0].xyz, (5, 6, 7))
        self.assertEqual(b[1].xyz, (8, 9, 0))
        self.assertRaises(gxgeo.GeometryException, gxgeo.Point2, (2, 3, 4, 5, 6))

    def test_cs_math(self):
        self.start()

        p = gxgeo.Point((5, 10))
        self.assertTrue(p == p)
        self.assertTrue(gxgeo.Point((1,2), coordinate_system="WGS 84") ==
                        gxgeo.Point((1,2), coordinate_system="WGS 84"))
        self.assertTrue(gxgeo.Point((1, 2), coordinate_system="WGS 84") ==
                        gxgeo.Point((1, 2)))
        self.assertTrue(gxgeo.Point((1, 2)) == gxgeo.Point((1, 2)))

        cs = "NAD83 / UTM zone 32N>"
        p = gxgeo.Point((500000,6000000), coordinate_system=cs)
        self.assertEqual(str(p.coordinate_system), "NAD83 / UTM zone 32N")
        p27 = gxgeo.Point(p, "NAD27 / UTM zone 32N")
        self.assertEqual(str(p27.coordinate_system), "NAD27 / UTM zone 32N")
        self.assertAlmostEqual(p27.x, 499840.780459, 3)
        self.assertAlmostEqual(p27.y, 5999920.58165, 3)
        self.assertFalse(p == p27)

        p27 = gxgeo.Point(p, "NAD27 / UTM zone 32N")
        self.assertEqual(str(p27.coordinate_system), "NAD27 / UTM zone 32N")
        self.assertAlmostEqual(p27.x, 499840.780459, 3)
        self.assertAlmostEqual(p27.y, 5999920.58165, 3)
        self.assertFalse(p == p27)

        pd = p - p27
        self.assertEqual(str(pd.coordinate_system), "NAD83 / UTM zone 32N")
        self.assertAlmostEqual(pd.x, 0., 2)
        self.assertAlmostEqual(pd.y, 0., 2)
        pd = p27 - p
        self.assertEqual(str(pd.coordinate_system), "NAD27 / UTM zone 32N")
        self.assertAlmostEqual(pd.x, 0., 2)
        self.assertAlmostEqual(pd.y, 0., 2)
        pp = p + (10, 5)
        self.assertEqual(str(pp.coordinate_system), "NAD83 / UTM zone 32N")
        self.assertEqual(pp.xy, (500010, 6000005))

        p = gxgeo.Point2(((500000, 6000000), (500001, 6000001)), coordinate_system=cs)
        self.assertEqual(str(p.coordinate_system), "NAD83 / UTM zone 32N")
        p27 = gxgeo.Point2(p, "NAD27 / UTM zone 32N")
        self.assertEqual(str(p27.coordinate_system), "NAD27 / UTM zone 32N")
        self.assertAlmostEqual(p27.p0.x, 499840.780459, 3)
        self.assertAlmostEqual(p27.p0.y, 5999920.58165, 3)
        self.assertAlmostEqual(p27.p1.x, 499841.780459, 3)
        self.assertAlmostEqual(p27.p1.y, 5999921.58165, 3)
        self.assertFalse(p == p27)
        pp = p / 2
        self.assertEqual(pp[1].xyz, (250000.5, 3000000.5, 0.0))
        pp = p / gxgeo.Point(2)
        self.assertEqual(pp[1].xyz, (250000.5, 3000000.5, 0.0))
        pp = p / gxgeo.Point2((gxgeo.Point(2), gxgeo.Point(3)))
        self.assertEqual(pp[0].xyz, (250000.0, 3000000.0, 0.0))
        self.assertEqual(pp[1].xyz, (166667.0, 2000000.3333333333, 0.0))

        p27 = gxgeo.Point2(p, "NAD27 / UTM zone 32N")
        self.assertEqual(str(p27.coordinate_system), "NAD27 / UTM zone 32N")
        self.assertAlmostEqual(p27.p0.x, 499840.780459, 3)
        self.assertAlmostEqual(p27.p0.y, 5999920.58165, 3)
        self.assertAlmostEqual(p27.p1.x, 499841.780459, 3)
        self.assertAlmostEqual(p27.p1.y, 5999921.58165, 3)
        self.assertEqual(tuple(p27[0]), (499840.78045944084, 5999920.5816528751, 0.0))
        self.assertEqual(tuple(p27[1]), (499841.7804697603, 5999921.5816632193, 0.0))
        for pp in p27:
            self.assertTrue(isinstance(pp, gxgeo.Point))
        self.assertFalse(p == p27)
        pp = p + p27
        self.assertEqual(tuple(pp[0]), (999999.99835706223, 12000000.002281997, 0.0))
        self.assertEqual(tuple(pp[1]), (1000001.9983570619, 12000002.002281997, 0.0))
        pp = pp - p27[0]
        self.assertEqual(tuple(pp[0]), (500000.0, 6000000.0000000009, 0.0))
        self.assertEqual(tuple(pp[1]), (500001.99999999965, 6000002.0000000009, 0.0))

        pd = p - p27
        self.assertEqual(str(pd.coordinate_system), "NAD83 / UTM zone 32N")
        self.assertAlmostEqual(pd.p0.x, 0., 2)
        self.assertAlmostEqual(pd.p0.y, 0., 2)
        self.assertAlmostEqual(pd.p1.x, 0., 2)
        self.assertAlmostEqual(pd.p1.y, 0., 2)
        pp = pd + 1
        self.assertAlmostEqual(pp.p0.x, 1., 2)
        self.assertAlmostEqual(pp.p0.y, 1., 2)
        self.assertAlmostEqual(pp.p1.x, 1., 2)
        self.assertAlmostEqual(pp.p1.y, 1., 2)
        pp = pd + gxgeo.Point(1)
        self.assertAlmostEqual(pp.p0.x, 1., 2)
        self.assertAlmostEqual(pp.p0.y, 1., 2)
        self.assertAlmostEqual(pp.p1.x, 1., 2)
        self.assertAlmostEqual(pp.p1.y, 1., 2)
        pp = -pp
        self.assertAlmostEqual(pp.p0.x, -1., 2)
        self.assertAlmostEqual(pp.p0.y, -1., 2)
        self.assertAlmostEqual(pp.p1.x, -1., 2)
        self.assertAlmostEqual(pp.p1.y, -1., 2)
        pp = -pp - 1
        self.assertAlmostEqual(pd.p0.x, 0., 2)
        self.assertAlmostEqual(pd.p0.y, 0., 2)
        self.assertAlmostEqual(pd.p1.x, 0., 2)
        self.assertAlmostEqual(pd.p1.y, 0., 2)

        pz = gxgeo.Point2(((0, 1, 2), (1, 2, 3)))
        pp = (pz + 1) * 5
        self.assertEqual(tuple(pp[0]), (5., 10., 15.))
        self.assertEqual(tuple(pp[1]), (10., 15., 20.))
        pp = (pz + 1) * gxgeo.Point((2, 5, 10))
        self.assertEqual(tuple(pp[0]), (2., 10., 30.))
        self.assertEqual(tuple(pp[1]), (4., 15., 40.))
        pp = (pz + 1) * gxgeo.Point2(((2, 5, 10), (1, 2, 3)))
        self.assertEqual(tuple(pp[0]), (2., 10., 30.))
        self.assertEqual(tuple(pp[1]), (2.0, 6.0, 12.0))

        pd = p27 - p
        self.assertEqual(str(pd.coordinate_system), "NAD27 / UTM zone 32N")
        self.assertAlmostEqual(pd.p0.x, 0., 2)
        self.assertAlmostEqual(pd.p0.y, 0., 2)
        self.assertAlmostEqual(pd.p1.x, 0., 2)
        self.assertAlmostEqual(pd.p1.y, 0., 2)
        pp = p + (10, 5)
        self.assertEqual(str(pp.coordinate_system), "NAD83 / UTM zone 32N")
        self.assertEqual(pp.p0.xy, (500010, 6000005))
        self.assertEqual(pp.p1.xy, (500011, 6000006))

        pp.x2 = (1, 2)
        pp.y2 = (3, 4)
        pp.z2 = (5, 6)
        self.assertEqual(pp.p0.xyz, (1, 3, 5))
        self.assertEqual(pp.p1.xyz, (2, 4, 6))

    def test_names(self):
        self.start()

        self.assertEqual(gxgeo.Point((1, 2)).name, '_point_')
        self.assertEqual(gxgeo.Point((1, 2), name='maki').name, 'maki')
        self.assertTrue(gxgeo.Point((1, 2)) == gxgeo.Point((1,2), name='maki'))
        self.assertEqual(gxgeo.Point(gxgeo.Point((1, 2))).name, '_point_')
        self.assertEqual(gxgeo.Point(gxgeo.Point((1, 2)), name='maki').name, 'maki')
        p1 = (1, 2)
        p2 = (2, 3)
        self.assertEqual(gxgeo.Point2((p1, p2)).name, '_point2_')
        self.assertEqual(gxgeo.Point2((p1, p2), name='maki').name, 'maki')
        self.assertTrue(gxgeo.Point2((p1, p2)) == gxgeo.Point2((p1, p2), name='maki'))
        pp = ((1, 2), (3, 2), (4, 5))
        self.assertEqual(gxgeo.PPoint(pp).name, '_ppoint_')
        self.assertEqual(gxgeo.PPoint(pp, name='maki').name, 'maki')
        self.assertTrue(gxgeo.PPoint(pp) == gxgeo.PPoint(pp, name='maki'))

    def test_mesh(self):
        self.start()

        v = list(np.array(range(27), dtype=np.float).reshape(-1, 3))
        f = list(np.array(range(len(v))).reshape(-1, 3))
        m = gxgeo.Mesh((f, v))
        self.assertEqual(len(m.faces), len(f))
        self.assertEqual(len(m.verticies), len(v))
        self.assertEqual(tuple(m[2][2]), (24., 25., 26.))
        self.assertEqual(tuple(m.extent_minimum), (0, 1, 2))
        m2 = m + 1.5
        self.assertEqual(tuple(m2[2][2]), (25.5, 26.5, 27.5))
        self.assertEqual(tuple(m2.extent_minimum), (1.5, 2.5, 3.5))
        m2 = m2 - 1.5
        self.assertEqual(tuple(m2[2][2]), (24., 25., 26.))
        self.assertEqual(tuple(m2.extent_minimum), (0, 1, 2))
        m2 = m + (1, 10, 50)
        self.assertEqual(tuple(m2[2][2]), (25., 35., 76.))
        self.assertEqual(tuple(m2.extent_minimum), (1, 11, 52))
        m2 = m2 - (1, 10, 50)
        self.assertEqual(tuple(m2[2][2]), (24., 25., 26.))
        self.assertEqual(tuple(m2.extent_minimum), (0, 1, 2))
        m2 = m + (m + (1, 10, 50))
        self.assertEqual(tuple(m2.extent_maximum), (25., 35., 76.))
        self.assertEqual(m2.extent_maximum_xyz, (25., 35., 76.))
        self.assertEqual(m2.extent_minimum_xyz, (0, 1, 2))
        self.assertEqual(m2.extent_maximum_xy, (25., 35.))
        self.assertEqual(m2.extent_minimum_xy, (0, 1))
        self.assertEqual(m2.centroid_xyz, (12.5, 18.0, 39.0))
        self.assertEqual(m2.centroid_xy, (12.5, 18.0))

        self.assertEqual(len(m2), 2 * len(m))
        mm = gxgeo.Mesh((np.append(m2.faces, m2.faces, axis=0), m2.verticies))
        self.assertEqual(len(mm), 12)
        self.assertEqual(len(mm.verticies), 18)
        mp = mm.point_array()
        self.assertEqual(len(mp), 18)
        mp = mm.point_array(unique=False)
        self.assertEqual(len(mp), 36)

        v = np.array(v)
        v[:, 0] += 500000
        v[:, 1] += 6000000
        m = gxgeo.Mesh((f, v), coordinate_system="NAD83 / UTM zone 17N")
        m = gxgeo.Mesh(m, coordinate_system="NAD27 / UTM zone 17N")
        self.assertEqual(str(m.coordinate_system), "NAD27 / UTM zone 17N")
        self.assertEqual(tuple(m[2][2]), (500006.87887296296, 5999802.6514122421, 26.0))

        m83 = gxgeo.Mesh(m, coordinate_system="NAD83 / UTM zone 17N")
        self.assertEqual(m83.coordinate_system, "NAD83 / UTM zone 17N")
        self.assertEqual(tuple(m[2][2]), (500006.87887296296, 5999802.6514122421, 26.0))
        self.assertEqual(tuple(m83[2][2]), (500024.00010005565, 6000025.0009018015, 26.0))

        f = np.array(f)
        f1vv = gxvv.GXvv(f[:, 0])
        f2vv = gxvv.GXvv(f[:, 1])
        f3vv = gxvv.GXvv(f[:, 2])
        xvv = gxvv.GXvv(v[:, 0])
        yvv = gxvv.GXvv(v[:, 1])
        zvv = gxvv.GXvv(v[:, 2])
        m = gxgeo.Mesh(((f1vv, f2vv, f3vv), (xvv, yvv, zvv)), coordinate_system="NAD83 / UTM zone 17N", name='vv')
        self.assertEqual(m.name, 'vv')
        mm = gxgeo.Mesh(m, coordinate_system="NAD27 / UTM zone 17N")
        self.assertEqual(mm.name, '_mesh_')
        m2 = gxgeo.Mesh(mm, coordinate_system="NAD27 / UTM zone 17N", name='vv_copy')
        self.assertEqual(m2.name, 'vv_copy')
        self.assertEqual(str(m2.coordinate_system), "NAD27 / UTM zone 17N")
        self.assertEqual(tuple(m2[2][2]), (500006.87887296296, 5999802.6514122421, 26.0))
        self.assertEqual(str(m2), 'vv_copy(3 faces)')
        self.assertTrue(mm == m2)
        self.assertEqual(len(list(m2)), 3)
        self.assertFalse(m == m2)

        m3 = m + m2
        self.assertEqual(len(m3), 6)
        self.assertEqual(m3.length, 6)

        f1vv, f2vv, f3vv = m3.faces_vv()
        self.assertEqual(tuple(f1vv.np), (0, 3, 6, 9, 12, 15))
        self.assertEqual(tuple(f2vv.np), (1, 4, 7, 10, 13, 16))
        self.assertEqual(tuple(f3vv.np), (2, 5, 8, 11, 14, 17))
        xvv, yvv, zvv = m3.verticies_vv()
        self.assertEqual(tuple(xvv.np[:3]), (500000.0, 500003.0, 500006.0))
        self.assertEqual(tuple(yvv.np[:3]), (6000001.0, 6000004.0, 6000007.0))
        self.assertEqual(tuple(zvv.np[:3]), (2.0, 5.0, 8.0))

    def test_pp_from_list(self):
        self.start()
        plinelist = [[110, 5],
                     [120, 20],
                     [130, 15],
                     [150, 50],
                     [160, 70],
                     [175, 35],
                     [190, 65],
                     [220, 50],
                     [235, 18.5]]

        pp = gxgeo.PPoint.from_list(plinelist)
        self.assertEqual(len(pp), len(plinelist))
        self.assertEqual(pp.extent_minimum_xyz, (110, 5, 0))
        self.assertEqual(pp.extent_maximum_xyz, (235, 70., 0))

    def test_pp_merge(self):
        self.start()

        plinelist = [[110, 5],
                     [120, 20],
                     [130, 15]]
        plinelst2 = [[150, 50],
                     [160, 70]]
        plinelst3 = (190, 65, 4)

        pm = gxgeo.PPoint.merge((plinelist, plinelst2, [plinelst3]))
        self.assertEqual(pm.length, 6)
        self.assertEqual(tuple(pm[0]), (110, 5, 0))
        self.assertEqual(tuple(pm[4]), (160, 70, 0))
        self.assertEqual(tuple(pm[5]), (190, 65, 4))

        pm = gxgeo.PPoint.merge((gxgeo.PPoint(plinelist),
                                 gxgeo.Point2(plinelst2),
                                 gxgeo.Point(plinelst3)))
        self.assertEqual(pm.length, 6)
        self.assertEqual(tuple(pm[0]), (110, 5, 0))
        self.assertEqual(tuple(pm[4]), (160, 70, 0))
        self.assertEqual(tuple(pm[5]), (190, 65, 4))

        center = gxgeo.Point((550000, 6000000))
        a = gxgeo.PPoint(plinelist) + center
        b = gxgeo.Point2(plinelst2, coordinate_system="NAD83 / UTM zone 15N") + center
        c = gxgeo.Point(plinelst3, coordinate_system="NAD27 / UTM zone 15N") + center

        pm = gxgeo.PPoint.merge((a, b, c))
        self.assertEqual(pm.length, 6)
        self.assertTrue(pm.coordinate_system == b.coordinate_system)
        self.assertEqual(tuple(pm[0]), (550110., 6000005., 0.))
        self.assertEqual(tuple(pm[4]), (550160., 6000070., 0.))
        self.assertEqual(str(pm[5]), '_point_(550173.9373550161, 6000287.416398498, 4.0)')

    def test_union(self):
        self.start()
        
        cs = "NAD83 / UTM zone 32N>"
        p = gxgeo.Point((500000,6000000), cs)
        ext = gxgeo.extent_union(p, p)
        self.assertEqual(ext.p0.xyz, p.xyz)
        self.assertEqual(ext.p1.xyz, p.xyz)

        p2 = gxgeo.Point((500010,6000100), cs)
        ext = gxgeo.extent_union(p, p2)
        self.assertEqual(ext.p0.xyz, p.xyz)
        self.assertEqual(ext.p1.xyz, p2.xyz)

        p3 = (490000,5900000)
        ext = gxgeo.extent_union(p, p3)
        self.assertEqual(ext.p0.xyz, (490000,5900000, 0))
        self.assertEqual(ext.p1.xyz, p.xyz)

        pp = gxgeo.PPoint((p2, gxgeo.Point(p3)))
        ext = gxgeo.extent_union(p, pp)
        self.assertEqual(ext.p0.xyz, (490000,5900000, 0))
        self.assertEqual(ext.p1.xyz, p2.xyz)

        p2.coordinate_system = "NAD27 / UTM zone 32N"
        p2.z = -88
        p3 = gxgeo.Point(p3, "NAD27 / UTM zone 32N")
        p3.z = 51
        pp = gxgeo.PPoint((p2, p3))
        ext = gxgeo.extent_union(p, pp)
        self.assertEqual(ext.p0.xyz, (490159.31817756349, 5900080.4689568691, -88.0))
        self.assertEqual(ext.p1.xyz, (500169.21834333451, 6000179.4198679868, 51.0))


if __name__ == '__main__':

    unittest.main()
