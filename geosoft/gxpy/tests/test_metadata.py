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

        meta.node_token('maki/crazy/deep/stuff/is/here')
        self.assertTrue(meta.has_node('/maki/crazy'))
        self.assertTrue(meta.has_node('/maki/crazy/deep'))
        self.assertTrue(meta.has_node('/maki/crazy/deep/stuff/is/here'))
        meta.set_attribute('maki/crazy/hello/deep/stuff/is/here/deep_hello', 'hi there in a deep voice')
        meta.set_attribute('maki/crazy/crazy_hi', 'hi there')
        self.assertEqual(meta.get_attribute('maki/crazy/crazy_hi'), 'hi there')
        meta.set_attribute('maki/weirdo/nested/stuff/hello', 'hi there weirdo')
        self.assertTrue(meta.has_node('/maki/weirdo/nested/stuff'))
        self.assertEqual(meta.get_attribute('maki/weirdo/nested/stuff/hello'), 'hi there weirdo')
        self.assertEqual(meta.meta_dict()['Maki']['weirdo']['nested']['stuff']['hello'], 'hi there weirdo')

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

    def test_meta_dict(self):
        self.start()

        m = {}
        self.assertTrue(gxmeta.get_node_from_meta_dict('maki/rider', m) is None)
        self.assertTrue(gxmeta.get_node_from_meta_dict('', m) is None)
        gxmeta.set_node_in_meta_dict('geosoft', m, [1, 2, 3])
        self.assertEqual(tuple(gxmeta.get_node_from_meta_dict('geosoft', m)), (1, 2, 3))

        self.assertRaises(gxmeta.MetadataException, gxmeta.set_node_in_meta_dict, 'geosoft/dataset/sample/children', m, ('a', 1.8, 'b'))
        gxmeta.set_node_in_meta_dict('geosoft/dataset/sample/children', m, ('a', 1.8, 'b'), replace=True)
        self.assertEqual(gxmeta.get_node_from_meta_dict('geosoft/dataset/sample/children', m), ('a', 1.8, 'b'))

    def test_update_dict(self):
        self.start()

        meta = gxmeta.Metadata()
        meta.set_attribute('geosoft/array', [1, 2, 3])
        self.assertEqual(tuple(meta.get_attribute('geosoft/array')), (1, 2, 3))
        meta.update_dict({'maki': 'someone'})
        self.assertEqual(tuple(meta.get_attribute('geosoft/array')), (1, 2, 3))
        self.assertEqual(meta.get_attribute('maki'), 'someone')
        meta.update_dict({'maki': 'someone'}, trunk_node='geosoft')
        self.assertEqual(meta.get_attribute('geosoft/maki'), 'someone')
        meta.update_dict(meta.meta_dict(), trunk_node='bob')
        self.assertEqual(meta.get_attribute('bob/maki'), 'someone')
        self.assertEqual(meta.get_attribute('bob/geosoft/maki'), 'someone')
        meta.update_dict(meta.meta_dict(), trunk_node='geosoft/bobs/your/uncle')
        self.assertEqual(meta.get_attribute('geosoft/bobs/your/uncle/maki'), 'someone')
        self.assertEqual(tuple(meta.get_attribute('geosoft/bobs/your/uncle/geosoft/array')), (1, 2, 3))


##############################################################################################
if __name__ == '__main__':

    unittest.main()