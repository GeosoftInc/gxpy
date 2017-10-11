import numpy as np
import os
import unittest

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.system as gsys
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.utility as gxu
import geosoft.gxpy.metadata as gxmeta

from base import GXPYTest


class Test(GXPYTest):

    def test_meta(self):
        self.start()

        geometa = gxapi.GXMETA.create()

        folder, files = gsys.unzip(os.path.join(os.path.dirname(self._test_case_py), 'testgrids.zip'),
                                       folder=self._gx.temp_folder())
        g1f = os.path.join(folder, 'test_grid_1.grd')
        with gxgrd.Grid.open(g1f) as g:
            g.gximg.get_meta(geometa)

        meta = gxmeta.Metadata.from_geosoft_meta(geometa)
        pass

##############################################################################################
if __name__ == '__main__':

    unittest.main()