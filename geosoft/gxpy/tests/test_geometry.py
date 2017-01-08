import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.view as gxgm
import geosoft.gxpy.geometry as gxgm

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gx = gx.GXpy(log=print)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        pass

    @classmethod
    def tearDownClass(cls):
        pass
    
    @classmethod
    def start(cls,test):
        cls.gx.log("*** {} *** - {}".format(test, geosoft.__version__))

    def test_version(self):
        self.assertEqual(gxmap.__version__, geosoft.__version__)

    def test_exception(self):
        self.start(gsys.func_name())

        self.assertRaises(ValueError, gxgm.Point, [1, 'yada', 2])

    def test_cs(self):
        self.start(gsys.func_name())

        s = "WGS 84 / UTM zone 32N <0, 0, 0, 10, 15, 32>"
        p = gxgm.Point((5,10), ipj=s)
        self.gx.log(str(p.ipj), " vcs:", str(p.vcs))
        self.assertEqual(str(p.ipj), "WGS 84 / UTM zone 32N (0,0,0) <32 deg,15 deg,10 deg>")

        pp = gxgm.PPoint(((8, 12), (5, 10)), ipj=s, vcs="geoid")
        self.gx.log(str(pp.ipj), " vcs:", str(pp.vcs))
        self.assertEqual(str(pp.ipj), "WGS 84 / UTM zone 32N (0,0,0) <32 deg,15 deg,10 deg>")

    def test_point(self):
        self.start(gsys.func_name())

        p = gxgm.Point((5,10))
        self.assertEqual(p.p.tolist(), [5.0, 10.0, 0.0])
        self.assertEqual(p.xy, (5.0,10.0))
        self.assertEqual(p.xyz, (5.0, 10.0, 0.0))
        self.assertEqual(p.x, 5.0)
        self.assertEqual(p.y, 10.0)
        self.assertEqual(p.z, 0.0)

        p -= (0, 0, 15)
        self.assertEqual(p.xyz, (5.0, 10.0, -15.0))

        p = gxgm.Point((5,10,3.5))
        self.assertEqual(p.p.tolist(), [5.0, 10.0, 3.5])
        self.assertEqual(p.xyz, (5.0, 10.0, 3.5))
        self.assertEqual(p.x, 5.0)
        self.assertEqual(p.y, 10.0)
        self.assertEqual(p.z, 3.5)

        p = gxgm.Point(4)
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
        self.start(gsys.func_name())

        points = [(5, 10), (6, 11), (7, 12)]
        pp = gxgm.PPoint(points)
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

        pp = gxgm.PPoint([(5, 10, 3.5)])
        self.assertEqual(pp[0].xyz, (5.0, 10.0, 3.5))

        pp = gxgm.PPoint(((1, 2, 3), (4, 5, 6), (7, 8, 9)))

        pp += (1, 2, 3)
        self.assertEqual(pp[0].xyz, (2., 4., 6.))
        self.assertEqual(pp[2].xyz, (8., 10., 12.))

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

        pp = pp * gxgm.PPoint(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
        self.assertEqual(pp[1].xyz, (20., 10., 18.))
        self.assertEqual(len(pp), 3)
        self.assertEqual(pp.x.tolist(), [5., 20., 35.])
        self.assertEqual(pp.y.tolist(), [4., 10., 16.])
        self.assertEqual(pp.z.tolist(), [9., 18., 27.])

        points = [(5, 10), (6, 11), (7, 12)]
        pp = gxgm.PPoint(points, 3.5)
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

if __name__ == '__main__':

    unittest.main()
