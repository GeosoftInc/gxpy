import unittest
import os

import geosoft
import geosoft.gxpy.gx as gx

from base import GXPYTest

import geosoft.gxpy.segy_reader as segy

import geosoft.gxapi as gxapi
import geosoft.gxapi.GXSEGYREADER
import geosoft.gxpy.system as gsys
import geosoft.gxpy.coordinate_system as coordinate_system


class Test(GXPYTest):
    @classmethod
    def setUpClass(cls):
        cls.setUpGXPYTest()
        cls.folder, _files = gsys.unzip(os.path.join(os.path.dirname(cls._test_case_py),
                                                     'testsegy.zip'),
                                        folder=cls._gx.temp_folder())
        cls.testfile_2d = os.path.join(cls.folder, '2d.segy')
        cls.testfile_3d = os.path.join(cls.folder, '3d.segy')

    def test_datatype_constants(self):
        self.start()
        gxapi_datatype_names = []
        for i in range(geosoft.gxapi.GXSEGYREADER.get_num_trace_data_types()):
            name_ref = gxapi.str_ref()
            geosoft.gxapi.GXSEGYREADER.get_trace_data_type_name(
                i, name_ref)
            gxapi_datatype_names.append(name_ref.value)

        for e in segy.DataType:
            self.assertTrue(e.value in gxapi_datatype_names)

    def test_scan_file_non_existing(self):
        self.start()
        with self.assertRaises(gxapi.GXError) as raise_context:
            with segy.SegyReader('this_file_nowhere_to_be_found.sgy') as target:
                target.scan_file()
        self.assertTrue('Unable to open "this_file_nowhere_to_be_found.sgy"' in str(raise_context.exception))

    def test_scan_file(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.scan_file()
            self.assertEqual(target.scan_file(),
                             segy.InlineCrosslineSanity.OK)

    def test_get_georeferencing(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            self.assertEqual(target.georeferencing.coordinate_dict()[
                             'name'], '*unknown')
            self.assertEqual(
                target.georeferencing.coordinate_dict()['units'][:3], 'ft,')
        with segy.SegyReader(self.testfile_2d) as target:
            self.assertEqual(target.georeferencing.coordinate_dict()[
                             'name'], '*unknown')
            self.assertEqual(
                target.georeferencing.coordinate_dict()['units'][:2], 'm,')

    def test_set_georeferencing(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            georef_dict = target.georeferencing.coordinate_dict()
            georef_dict['name'] = 'NAD83 / UTM zone 15N'
            target.georeferencing = coordinate_system.Coordinate_system(
                georef_dict)
            self.assertEqual(target.georeferencing.coordinate_dict()[
                             'name'], 'NAD83 / UTM zone 15N')

    def test_export_gdb(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.scan_file()
            target.export_files(gdb=os.path.join(self.folder, 'test.gdb'))

    def test_export_voxel(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.export_files(voxel=os.path.join(
                self.folder, 'test.geosoft_voxel'))

    def test_export_z_slice(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.export_files(
                slice_prefix=os.path.join(
                    self.folder, 'test_z_slice'),
                z_slices=[0, 10])

    def test_export_inline_slice(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.export_files(
                slice_prefix=os.path.join(
                    self.folder, 'test_inline_slice'),
                inline_slices=[20, 30])

    def test_export_crossline_slice(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.export_files(
                slice_prefix=os.path.join(
                    self.folder, 'test_crossline_slice'),
                crossline_slices=[40, 50])

    def test_export_multi_slice(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.export_files(
                slice_prefix=os.path.join(
                    self.folder, 'test_crossline_slice'),
                inline_slices=[60, 70],
                crossline_slices=[80, 90],
                z_slices=[100, 110])

    def test_get_text_header(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            # Header should be 3200 characters long
            self.assertEqual(len(target.text_header), 3200)
            # Header should be ASCII
            self.assertTrue(all(ord(c) < 128 for c in target.text_header))
            self.assertEqual(target.text_header[:4], 'C 1 ')
            self.assertEqual(target.text_header[3120:3124], 'C40 ')

    def test_get_binary_header(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            self.assertEqual(len(target.binary_header.keys()), 27)
            self.assertEqual(target.binary_header['Line number'], 4)

    def test_get_trace_header(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            self.assertEqual(
                target.get_trace_header(
                    0)["Trace sequence number within line"]["offset"],
                '0')
            self.assertEqual(
                target.get_trace_header(
                    0)["Trace sequence number within line"]["value"],
                '1')
            self.assertEqual(
                target.get_trace_header(
                    0)["Source coordinate - X"]["offset"],
                '72')
            self.assertEqual(
                target.get_trace_header(
                    0)["Source coordinate - X"]["value"],
                '264640')
            self.assertEqual(
                target.get_trace_header(
                    1)["Trace sequence number within line"]["offset"],
                '0')
            self.assertEqual(
                target.get_trace_header(
                    1)["Trace sequence number within line"]["value"],
                '2')
            self.assertEqual(
                target.get_trace_header(
                    1)["Source coordinate - X"]["offset"],
                '72')
            self.assertEqual(
                target.get_trace_header(
                    1)["Source coordinate - X"]["value"],
                '264640')

    def test_get_trace_data(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            trace = target.get_trace_data(100)
            self.assertEqual(trace.length, target.trace_length)

    def test_get_trace_length(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            self.assertEqual(target.trace_length, 901)

    def test_set_trace_length(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.trace_length = 100
            self.assertEqual(target.trace_length, 100)

    def test_get_trace_length_from_file_header(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.get_trace_length_from_file_header(16)
            self.assertEqual(target.trace_length, 14999)

    def test_get_trace_length_from_trace_header(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.get_trace_length_from_trace_header(72)
            self.assertEqual(target.trace_length, 264640)

    def test_get_trace_data_type(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            self.assertEqual(target.trace_data_type, segy.DataType.IBM_FLOAT4)

    def test_set_trace_data_type(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.trace_data_type = segy.DataType.IEEE_FLOAT4
            self.assertEqual(target.trace_data_type, segy.DataType.IEEE_FLOAT4)

    def test_get_trace_sample_interval(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            self.assertEqual(target.trace_sample_interval, 14999)

    def test_set_trace_sample_interval(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.trace_sample_interval = 1000
            self.assertEqual(target.trace_sample_interval, 1000)

    def test_get_z_units(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            self.assertEqual(target.z_units, 'microseconds')

    def test_set_z_units(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.z_units = 'milliseconds'
            self.assertEqual(target.z_units, 'milliseconds')

    def test_get_z_offset(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            self.assertEqual(target.z_offset, -7499)

    def test_set_z_offset(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.z_offset = 2000.5
            self.assertEqual(target.z_offset, 2000.5)

    def test_get_z_offset_units(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            self.assertEqual(target.z_offset_units, "milliseconds")

    def test_set_z_offset_units(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            target.z_offset_units = 'microseconds'
            self.assertEqual(target.z_offset_units, "microseconds")

    def test_get_xy_units(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            self.assertEqual(target.xy_units, "feet")

    def test_get_is_depth_or_time(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            self.assertEqual(target.is_depth_or_time, segy.ZType.TIME)

    def test_get_trace_range(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            top, bottom = target.trace_range
            self.assertEqual(top, -7499)
            self.assertEqual(bottom, 6000.1)

    def test_get_field_configuration(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            config = target.field_configuration
            self.assertEqual(len(config.fields), 15)
            self.assertEqual(
                config.fields[2].mapping, segy.FieldMapping.Crossline)

    def test_set_field_configuratiion(self):
        self.start()
        with segy.SegyReader(self.testfile_3d) as target:
            config = target.field_configuration
            config.fields[2].mapping = segy.FieldMapping.Inline
            config.fields[1].mapping = segy.FieldMapping.Crossline
            target.field_configuration = config
            config2 = target.field_configuration
            self.assertEqual(len(config2.fields), 15)
            self.assertEqual(
                config2.fields[2].mapping, segy.FieldMapping.Inline)


##########################################################################################


if __name__ == '__main__':

    unittest.main()
