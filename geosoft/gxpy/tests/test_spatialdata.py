import unittest
import os

import geosoft.gxpy.spatialdata as gxspd
import geosoft.gxpy.coordinate_system as gxcs

from base import GXPYTest


class Test(GXPYTest):

    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()

    @classmethod
    def tearDownClass(cls):
        cls.tearDownGXPYTest()

    def test_properties(self):
        self.start()

        with gxspd.SpatialData() as spd:
            self.assertEqual(spd.file_name, None)
            self.assertEqual(spd.name, None)
            self.assertTrue(isinstance(spd.metadata, dict))
            self.assertEqual(spd.unit_of_measure, '')
            self.assertEqual(spd.extent, (None, None, None, None, None, None))
            self.assertEqual(spd.extent_2d, (None, None, None, None))
            self.assertEqual(spd.extent_minimum, (None, None, None))
            self.assertEqual(spd.extent_maximum, (None, None, None))
            self.assertTrue(isinstance(spd.coordinate_system, gxcs.Coordinate_system))
            self.assertEqual(str(spd.coordinate_system), '*unknown')
            self.assertFalse(spd.persist)

        with gxspd.SpatialData(file_name='maki.spd') as spd:
            self.assertEqual(spd.file_name, 'maki.spd')
            self.assertEqual(spd.name, 'maki')

        with gxspd.SpatialData(name='maki') as spd:
            self.assertEqual(spd.file_name, 'maki')
            self.assertEqual(spd.name, 'maki')


        with gxspd.SpatialData('maki', file_name='bogus.spd') as spd:
            self.assertEqual(spd.file_name, 'bogus.spd')
            self.assertEqual(spd.name, 'maki')

        self.assertRaises(gxspd.SpatialException, gxspd.SpatialData, mode=gxspd.MODE_READ)
        self.assertRaises(gxspd.SpatialException, gxspd.SpatialData, mode=gxspd.MODE_READWRITE)

        gxspd.SpatialData().close()

    def test_setters(self):
        self.start()

        with gxspd.SpatialData() as spd:
            spd.unit_of_measure = 'ohms'
            self.assertEqual(spd.unit_of_measure, 'ohms')
            spd.coordinate_system = 'NAD83 / UTM zone 19N'
            self.assertEqual(str(spd.coordinate_system), 'NAD83 / UTM zone 19N')
            self.assertFalse(spd.persist)
            try:
                spd.persist = True
                self.assertFalse(True)
            except gxspd.SpatialException:
                pass

    def test_modes(self):
        self.start()

        fn = 'maki.spd'
        gxspd.delete_files(fn)
        self.assertFalse(os.path.exists(fn))
        self.assertFalse(os.path.exists(fn + '.xml'))

        gxspd.SpatialData(fn, mode=gxspd.MODE_NEW)
        self.assertRaises(gxspd.SpatialException, gxspd.SpatialData, 'maki.spd', mode=gxspd.MODE_READ)
        self.assertRaises(gxspd.SpatialException, gxspd.SpatialData, 'maki.spd', mode=gxspd.MODE_READWRITE)

        try:
            with open(fn, 'w') as f:
                f.write('maki')
            with gxspd.SpatialData(fn, mode = gxspd.MODE_READ) as spd:
                self.assertEqual(spd.name, 'maki.spd')
                spd.metadata = {'name': 'some_name'}
                self.assertEqual(spd.metadata['name'], 'some_name')
                try:
                    spd.persist = False
                    self.assertTrue(False)
                except gxspd.SpatialException:
                    pass
            self.assertTrue(os.path.exists(fn))
            self.assertFalse(os.path.exists(fn + '.xml'))

        finally:
            gxspd.delete_files(fn)

        try:
            with open(fn, 'w') as f:
                f.write('maki')
            with gxspd.SpatialData(fn, mode=gxspd.MODE_READWRITE) as spd:
                self.assertEqual(spd.name, 'maki.spd')
                spd.metadata = {'name': 'some_name'}
            self.assertTrue(os.path.exists(fn))
            self.assertTrue(os.path.exists(fn + '.xml'))
            with gxspd.SpatialData(fn, mode=gxspd.MODE_READ) as spd:
                self.assertEqual(spd.metadata['name'], 'some_name')

        finally:
            gxspd.delete_files(fn)
            self.assertFalse(os.path.exists(fn))
            self.assertFalse(os.path.exists(fn + '.xml'))

        try:
            with open(fn, 'w') as f:
                f.write('maki')
            self.assertRaises(gxspd.SpatialException, gxspd.SpatialData, 'maki.spd', mode=gxspd.MODE_NEW)
            with gxspd.SpatialData(file_name=fn, mode=gxspd.MODE_NEW, overwrite=True) as spd:
                self.assertEqual(spd.name, 'maki')
                spd.metadata = {'name': 'some_name'}
            self.assertTrue(os.path.exists(fn))
            self.assertTrue(os.path.exists(fn + '.xml'))
            with gxspd.SpatialData(fn, mode=gxspd.MODE_READ) as spd:
                self.assertEqual(spd.metadata['name'], 'some_name')

        finally:
            gxspd.delete_files(fn)
            self.assertFalse(os.path.exists(fn))
            self.assertFalse(os.path.exists(fn + '.xml'))

    def test_persist(self):
        self.start()

        fn = 'maki.spd'
        gxspd.delete_files(fn)
        self.assertFalse(os.path.exists(fn))
        self.assertFalse(os.path.exists(fn + '.xml'))

        try:
            with open(fn, 'w') as f:
                f.write('maki')
            with gxspd.SpatialData(fn, mode=gxspd.MODE_READWRITE) as spd:
                self.assertEqual(spd.name, 'maki.spd')
                spd.metadata = {'name': 'some_name'}
                self.assertTrue(spd.persist)
            self.assertTrue(os.path.exists(fn))
            self.assertTrue(os.path.exists(fn + '.xml'))
            with gxspd.SpatialData(fn, mode=gxspd.MODE_READ) as spd:
                self.assertEqual(spd.metadata['name'], 'some_name')

        finally:
            gxspd.delete_files(fn)

        try:
            with gxspd.SpatialData(fn, mode=gxspd.MODE_NEW) as spd:
                self.assertEqual(spd.name, 'maki.spd')
                spd.metadata = {'name': 'some_name'}
                self.assertTrue(spd.persist)
            self.assertFalse(os.path.exists(fn))
            self.assertTrue(os.path.exists(fn + '.xml'))

        finally:
            gxspd.delete_files(fn)

        try:
            with gxspd.SpatialData(fn, mode=gxspd.MODE_NEW) as spd:
                self.assertEqual(spd.name, 'maki.spd')
                spd.metadata = {'name': 'some_name'}
                self.assertTrue(spd.persist)
                spd.persist = False
                self.assertFalse(spd.persist)
            self.assertFalse(os.path.exists(fn))
            self.assertFalse(os.path.exists(fn + '.xml'))

        finally:
            gxspd.delete_files(fn)


        try:
            with open(fn, 'w') as f:
                f.write('maki')
            with gxspd.SpatialData(fn, mode=gxspd.MODE_NEW, overwrite=True) as spd:
                self.assertEqual(spd.name, 'maki.spd')
                spd.metadata = {'name': 'some_name'}
                self.assertTrue(spd.persist)
                spd.persist = False
                self.assertFalse(spd.persist)
            self.assertFalse(os.path.exists(fn))
            self.assertFalse(os.path.exists(fn + '.xml'))

        finally:
            gxspd.delete_files(fn)


###############################################################################################

if __name__ == '__main__':

    unittest.main()
