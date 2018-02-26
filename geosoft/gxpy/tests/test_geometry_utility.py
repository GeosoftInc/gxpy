import unittest
import os
import numpy as np

import geosoft
import geosoft.gxpy.system as gsys
import geosoft.gxpy.geometry as gxgeo
import geosoft.gxpy.geometry_utility as gxgeou
import geosoft.gxpy.geometry as gxgeo
import geosoft.gxpy.coordinate_system as gxcs

from base import GXPYTest


class Test(GXPYTest):
    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()

    def test_version(self):
        self.start()
        self.assertEqual(gxgeo.__version__, geosoft.__version__)

    def test_resample(self):
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
        ppr = gxgeou.resample(pp, 2.5)
        self.assertEqual(ppr.length, 93)
        self.assertEqual(ppr[0], pp[0])
        self.assertEqual(str(ppr[-1]), '_point_(234.61203746485876, 20.64579408987188, 0.0)')

        ppr = gxgeou.resample(pp, 2.5, closed=True)
        self.assertEqual(ppr.length, 145)
        self.assertEqual(ppr[0], pp[0])
        self.assertEqual(ppr[-1].xyz, ppr[0].xyz)

        ppr = gxgeou.resample(pp, 2.5, spline=gxgeou.SPLINE_AKIMA, closed=True)
        self.assertEqual(ppr.length, 145)
        self.assertEqual(ppr[0], pp[0])
        self.assertEqual(str(ppr[-2]), '_point_(109.96046205631022, 4.960353267681198, 0.0)')

        ppr = gxgeou.resample(pp, 2.5, spline=gxgeou.SPLINE_LINEAR, closed=True)
        self.assertEqual(ppr.length, 145)
        self.assertEqual(ppr[0], pp[0])
        self.assertEqual(str(ppr[-2]), '_point_(110.15605873233088, 5.016854343091733, 0.0)')

        ppr = gxgeou.resample(plinelist, 2.5, spline=gxgeou.SPLINE_LINEAR, closed=True)
        ppr = gxgeo.PPoint(ppr)
        self.assertEqual(ppr.length, 145)
        self.assertEqual(ppr[0], pp[0])
        self.assertEqual(str(ppr[-2]), '_point_(110.15605873233088, 5.016854343091733, 0.0)')

        ppr = gxgeou.resample(plinelist, 2.5, spline=gxgeou.SPLINE_NEAREST, closed=True)
        ppr = gxgeo.PPoint(ppr)
        self.assertEqual(ppr.length, 144)
        self.assertEqual(ppr[0], pp[0])
        self.assertEqual(ppr[-1], pp[0])

        ppr = gxgeou.resample(plinelist, 2.5, spline=gxgeou.SPLINE_NEAREST)
        ppr = gxgeo.PPoint(ppr)
        self.assertEqual(ppr.length, 93)
        self.assertEqual(ppr[0], pp[0])
        self.assertEqual(str(ppr[-1]), '_point_(235.0, 18.5, 0.0)')

        pp = np.array(plinelist)
        ppr = gxgeou.resample(pp[:, 0].flatten(), 2.5, spline=gxgeou.SPLINE_CUBIC)
        self.assertEqual(len(ppr), 51)
        self.assertEqual(ppr[0, 0], pp[0, 0])
        self.assertEqual(ppr[-1, 0], 235.)

        pp = np.array(plinelist)
        ppr = gxgeou.resample(pp[:, 0].flatten(), 2.5, spline=gxgeou.SPLINE_CUBIC, closed=True)
        self.assertEqual(len(ppr), 102)
        self.assertEqual(ppr[0, 0], pp[0, 0])
        self.assertEqual(ppr[-1, 0], pp[0,0])


        self.assertRaises(gxgeou.GeometryUtilityException, gxgeou.resample, plinelist, -1)

        plinelist = [[110, 5],
                     [120, 20],
                     [130, 15],
                     [150, 50],
                     [160, 70],
                     [175, 35],
                     [190, 65],
                     [220, 50],
                     [235, 18.5],
                     [110, 5]]

        pp = gxgeo.PPoint(plinelist)
        ppr = gxgeou.resample(pp, 2.5, spline=gxgeou.SPLINE_AKIMA)
        self.assertEqual(ppr.length, 145)
        self.assertEqual(ppr[0], pp[0])
        self.assertEqual(str(ppr[-2]), '_point_(109.96046205631022, 4.960353267681198, 0.0)')

        pp = gxgeo.PPoint([[110, 5], [120, 20]])
        ppr = gxgeou.resample(pp, 2.5, spline=gxgeou.SPLINE_AKIMA)
        self.assertEqual(ppr.length, 8)
        self.assertEqual(ppr[0], pp[0])
        self.assertEqual(str(ppr[-1]), '_point_(119.7072534339415, 19.560880150912265, 0.0)')

        pp = gxgeo.PPoint([[110, 5]])
        ppr = gxgeou.resample(pp, 2.5, spline=gxgeou.SPLINE_AKIMA)
        self.assertEqual(ppr.length, 1)
        self.assertEqual(ppr[0], pp[0])

        pp = gxgeo.PPoint([[110, 5], [110, 5]])
        ppr = gxgeou.resample(pp, 2.5, spline=gxgeou.SPLINE_AKIMA)
        self.assertEqual(ppr.length, 2)
        self.assertEqual(ppr[0], pp[0])
        self.assertEqual(ppr[1], pp[1])


###############################################################################################

if __name__ == '__main__':

    unittest.main()
