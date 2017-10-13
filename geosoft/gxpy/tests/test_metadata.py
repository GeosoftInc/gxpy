import os
import unittest

import geosoft.gxapi as gxapi
import geosoft.gxpy.system as gsys
import geosoft.gxpy.grid as gxgrd
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

        meta = gxmeta.Metadata(geometa)
        self.assertTrue(isinstance(meta.gxmeta, gxapi.GXMETA))
        self.assertTrue(meta.has_node('Geosoft'))
        self.assertTrue(meta.has_node('Geosoft/Data'))
        self.assertTrue(meta.has_node('geosoft/data'))
        self.assertFalse(meta.has_node('Geosoft/maki'))
        self.assertTrue(meta.has_attribute('Geosoft/Data/boundary'))
        self.assertFalse(meta.has_attribute('Geosoft/Data/huh'))

        meta.node_token('Maki')
        self.assertTrue(meta.has_node('maki'))

        meta.node_token('maki/data/more')
        self.assertTrue(meta.has_node('/maki/data'))
        self.assertTrue(meta.has_node('/maki/data/more'))

        meta.set_attribute('/maki/data/more/scale', 45)
        self.assertEqual(meta.get_attribute('/maki/data/more/scale'), 45)

        meta.set_attribute('/maki/data/more/unit_of_measure', 'cm')
        self.assertEqual(meta.get_attribute('/maki/data/more/unit_of_measure'), 'cm')

        meta.set_attribute('/maki/data/more/float', 4.995)
        self.assertEqual(meta.get_attribute('/maki/data/more/float'), 4.995)

        meta.set_attribute('/maki/data/more/array', ['a', 1, 4.95])
        self.assertEqual(meta.get_attribute('/maki/data/more/array'), ['a', 1, 4.95])

        meta.set_attribute('/maki/data/more/tuple', ('ian', 1, 2, 3.5))
        self.assertEqual(meta.get_attribute('/maki/data/more/tuple'), ['ian', 1, 2, 3.5])

        meta.set_attribute('/json/examples/dict', {'a': 25, 'b': (1, 2)})
        d = meta.get_attribute('json/examples/dict')
        self.assertEqual(d['a'], 25)
        self.assertEqual(d['b'], [1, 2])

        md = meta.meta_dict()
        self.assertTrue('Maki' in md)
        self.assertTrue('float' in md['Maki']['data']['more'])
        self.assertTrue('json' in md)


##############################################################################################
if __name__ == '__main__':

    unittest.main()