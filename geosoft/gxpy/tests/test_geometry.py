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
        cls.gx = gx.GXpy(log='test_geometry.log')
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

    def test_point(self):
        self.start(gsys.func_name())

        p = gxgm.Point((5,10))
        self.assertEqual(p.p.tolist(), [5.0, 10.0, 0.0])
        self.assertEqual(p.xy(), (5.0,10.0))
        self.assertEqual(p.xyz(), (5.0, 10.0, 0.0))
        self.assertEqual(p.x(), 5.0)
        self.assertEqual(p.y(), 10.0)
        self.assertEqual(p.z(), 0.0)

        p -= (0, 0, 15)
        self.assertEqual(p.xyz(), (5.0, 10.0, -15.0))

        p = gxgm.Point((5,10,3.5))
        self.assertEqual(p.p.tolist(), [5.0, 10.0, 3.5])
        self.assertEqual(p.xyz(), (5.0, 10.0, 3.5))
        self.assertEqual(p.x(), 5.0)
        self.assertEqual(p.y(), 10.0)
        self.assertEqual(p.z(), 3.5)

        p = gxgm.Point(4)
        self.assertEqual(p.xyz(), (4.0, 4.0, 4.0))

        p += (1, 2, 3)
        self.assertEqual(p.xyz(), (5., 6., 7.))

        p *= 2
        self.assertEqual(p.xyz(), (10., 12., 14.))

        p /= 2
        self.assertEqual(p.xyz(), (5., 6., 7.))

        p = -p
        self.assertEqual(p.xyz(), (-5., -6., -7.))

        p = p + 1
        self.assertEqual(p.xyz(), (-4., -5., -6.))

        p = p + (1, 2)
        self.assertEqual(p.xyz(), (-3., -3., -6.))

        p = p + (5, 2, 6)
        self.assertEqual(p.xyz(), (2., -1., 0.))

    def test_ppoint(self):
        self.start(gsys.func_name())

        points = [(5, 10), (6, 11), (7, 12)]
        pp = gxgm.PPoint(points)
        self.assertEqual(len(pp), 3)
        i = 0
        for p in pp:
            self.assertEqual(p.xy(), points[i])
            i += 1
        i = 0
        for p in pp:
            self.assertEqual(p.xyz(), (points[i][0], points[i][1], 0.0))
            i += 1

        p = pp[1]
        self.assertEqual(p.xy(), points[1])

        pp -= (0, 0, 15)
        self.assertEqual(pp[0].xyz(), (5.0, 10.0, -15.0))
        self.assertEqual(pp[2].xyz(), (7.0, 12.0, -15.0))

        pp = gxgm.PPoint([(5, 10, 3.5)])
        self.assertEqual(pp[0].xyz(), (5.0, 10.0, 3.5))

        pp = gxgm.PPoint(((1, 2, 3), (4, 5, 6), (7, 8, 9)))

        pp += (1, 2, 3)
        self.assertEqual(pp[0].xyz(), (2., 4., 6.))
        self.assertEqual(pp[2].xyz(), (8., 10., 12.))

        pp *= 2
        self.assertEqual(pp[1].xyz(), (10., 14., 18.))

        pp /= 2
        self.assertEqual(pp[1].xyz(), (5., 7., 9.))

        pp = -pp
        self.assertEqual(pp[1].xyz(), (-5., -7., -9.))

        pp = pp + (1, 2)
        self.assertEqual(pp[1].xyz(), (-4., -5., -9.))

        pp = pp + (5, 2, 6)
        self.assertEqual(pp[1].xyz(), (1., -3., -3.))

        pp = pp + ((1, 2, 3), (4, 5, 6), (7, 8, 9))
        self.assertEqual(pp[1].xyz(), (5., 2., 3.))

        pp = pp * gxgm.PPoint(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
        self.assertEqual(pp[1].xyz(), (20., 10., 18.))
        self.assertEqual(len(pp), 3)
        self.assertEqual(pp.x().tolist(), [5., 20., 35.])
        self.assertEqual(pp.y().tolist(), [4., 10., 16.])
        self.assertEqual(pp.z().tolist(), [9., 18., 27.])


if __name__ == '__main__':

    unittest.main()
