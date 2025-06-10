#  Copyright (c) 2025 Bentley Systems, Incorporated. All rights reserved.
"""
Read SEG-Y files into geosoft databases, grids and voxels.

:Classes:
    :class:`SegyReader` Reads SEG-Y files and creates Geosoft grids or voxels

.. versionadded:: 9.9.1
"""

import geosoft
import geosoft.gxapi as gxapi
from . import coordinate_system as coordinate_system
from . import vv as gxvv

__version__ = geosoft.__version__

from enum import Enum
import json


class Endianess(Enum):
    LITTLE_ENDIAN = True
    BIG_ENDIAN = False


class DataType(Enum):
    IBM_FLOAT4 = 'IBM_float4'
    IEEE_FLOAT4 = 'IEEE_float4'
    INT32 = 'int32'
    INT16 = 'int16'
    INT8 = 'int8'

    @classmethod
    def from_str(cls, str):
        for member in list(cls):
            if member.value == str:
                return member
        raise ValueError("Not a valid DataType name")


class InlineCrosslineSanity(Enum):
    OK = 0
    MAYBE_SWAPPED = 1
    ONLY_ONE_LINE = 2
    UNKNOWN_PROBLEM = 3


class ZType(Enum):
    DEPTH = "DEPTH"
    TIME = "TIME"


class FieldMapping(Enum):
    Inline = "INLINE"
    Crossline = "CROSSLINE"
    X = "X"
    Y = "Y"


class TraceConfigField:
    """
    TODO: Not really finished.

    After the SEG-Y is scanned, `SegyReader.field_configuration.fields` will contain a
    list of all the trace header fields that contain nonzero values.

    The EXPORT_TO_GDB field is used to indicate if the data from this field should be
    written to the GDB on export. The MAPPING field is used to indicate which fields
    should be interpreted as inline, crossline, x and y. For 3D SEG-Y files, exactly one
    field should be set to each of these values. For 2D files, only X and Y apply.

    The rest of the fields are read-only. I've defined the field names for all of them
    in __INIT__ but some of them are still missing accessors.
    """

    def __init__(self, ltb, index):
        self.index = index
        self.ltb = ltb

        self._export_to_gdb_field = ltb.find_field("EXPORT_TO_GDB")
        self._offset_field = ltb.find_field("OFFSET")
        self._datatype_field = ltb.find_field("FORMAT")
        self._scale_by_field_field = ltb.find_field("SCALE_BY")
        self._count_field = ltb.find_field("COUNT")
        self._min_field = ltb.find_field("MIN")
        self._max_field = ltb.find_field("MAX")
        self._scaled_min_field = ltb.find_field("SCALED_MIN")
        self._scaled_max_field = ltb.find_field("SCALED_MAX")
        self._stride_field = ltb.find_field("STRIDE")
        self._mapping_field = ltb.find_field("MAPPING")

    @property
    def name(self):
        ref = gxapi.str_ref()
        self.ltb.get_english_string(self.index, 0, ref)
        return ref.value

    @property
    def export_to_gdb(self):
        ref = gxapi.int_ref()
        self.ltb.get_int(self.index, self._export_to_gdb_field, ref)
        return bool(ref.value)

    @export_to_gdb.setter
    def export_to_gdb(self, value):
        self.ltb.set_int(self.index, self._export_to_gdb_field, value)

    @property
    def min(self):
        ref = gxapi.int_ref()
        self.ltb.get_int(self.index, self._max_field, ref)
        return ref.value

    @property
    def max(self):
        ref = gxapi.int_ref()
        self.ltb.get_int(self.index, self._min_field, ref)
        return ref.value

    @property
    def mapping(self):
        ref = gxapi.str_ref()
        self.ltb.get_english_string(self.index, self._mapping_field, ref)
        for member in list(FieldMapping):
            if member.value == ref.value:
                return member

    @mapping.setter
    def mapping(self, mapping):
        self.ltb.set_string(
            self.index, self._mapping_field, mapping.value)


class TraceFieldConfiguration:
    def __init__(self, ltb):
        self._ltb = ltb
        self.fields = []
        for i in range(ltb.records()):
            self.fields.append(TraceConfigField(self._ltb, i))


class SegyReader:
    """
    TODO: The GXSEGYREADER GetTiePoint and SetTiePoint functions are important and
    don't have wrappers yet. Also, none of the filtering functionality is implemented.


    Reads a SEG-Y file and can generate Geosoft database, grid or voxel files from it.

    For many SEG-Y files, the following is all that's needed to use this class::

    .. code::

        >>> import geosoft.gxpy.segy_reader as gxsegy
        >>> segy = gxsegy.SegyReader('c:/data/example.segy')
        >>> segy.export_file(gdb='c:/data/output.gdb')

    Unfortunately, some SEG-Y files will require some configuration before they can be
    read properly. TODO: more documentation once the API is finalized.
    """

    def __init__(self, filename, is3d=None, endianess=None):
        """
        Initialize the SegyReader object and do a quick initial scan of the SEG-Y file.

        :param filename:   The name of the SEG-Y file to read
        :param is3d        True is the SEG-Y file is 3D, False if the file is 2D. If this
                           parameter is not specified, the reader will attempt to
                           automatically determine if the file is 2D or 3D.
        :param endianess:  Endianess.LITTLE_ENDIAN or Endianess.BIG_ENDIAN, specifying
                           the endianess (byte order) of the SEG-Y file. Defaults to big-
                           endian which is correct for most SEG-Y files.

        The new SegyReader object will read the first part of the SEG-Y file and attempt
        to determine the correct configuration. Most of the methods for this class are for
        querying and modifying that configuration.

        """

        self._gx_segy_reader = gxapi.GXSEGYREADER.open_file(filename)

        if endianess is not None:
            self._gx_segy_reader.set_endianess(endianess)
        if is3d is not None:
            self._gx_segy_reader.set_is_3d(is3d)

        self._trace_data_type_names = []
        for i in range(self._gx_segy_reader.get_num_trace_data_types()):
            name_ref = gxapi.str_ref()
            self._gx_segy_reader.get_trace_data_type_name(i, name_ref)
            self._trace_data_type_names.append(name_ref.value)

        unit_list_ref = gxapi.str_ref()
        self._gx_segy_reader.get_possible_z_units(unit_list_ref)
        self._z_units_list = unit_list_ref.value.splitlines(keepends=False)

        self._scan_completed = False

    def scan_file(self):
        self._gx_segy_reader.scan_file()
        self._scan_completed = True
        if self._gx_segy_reader.get_is_3d():
            return self._check_sane_inline_crossline()

    @property
    def georeferencing(self):
        """A :class:`geosoft.gxpy.coordinate_system.Coordinate_system` object containing
        the coordinate system for the SEG-Y file and the generated output files.
        """
        return coordinate_system.Coordinate_system(
            self._gx_segy_reader.get_georeferencing())

    @georeferencing.setter
    def georeferencing(self, georef_object):
        self._gx_segy_reader.set_georeferencing(georef_object.gxipj)

    def export_files(self, **kwargs):
        """
        Export the data in the SEG-Y file to the specified Geosoft files.

        What files are output depend on the keyword arguments::

        :param gdb:              The filename of the Geosoft database file to export to.
                                 If this parameter is not specified, then no database is
                                 output.
        :param voxel:            The filename of the Geosoft voxel file to export to.
                                 Only valid for 3D SEG-Y files. If this option is not
                                 specified, then no voxel file is output.
        :param slice_prefix:     The base path and filename for slice grids. If this
                                 argument is specified, then at least one of 
                                 `inline_slices`, `crossline_slices` or z_slices` must
                                 also be specified.
        :param inline_slices:    An array-like containing the inline coordinates for slice
                                 grids. If this argument is specified then, for each
                                 coordinate in the list a geosoft grid file is generated
                                 from the slice of the SEG-Y volume with that inline
                                 coordinate. The filename will consist of `slice_prefix`
                                 folowed by "_IL???.grd" where ??? is the inline
                                 coordinate. Only valid for 3D SEG-Y files.
        :param crossline_slices: An array-like containing the crossline coordinates for 
                                 slice grids. If this argument is specified then, for each
                                 coordinate in the list a geosoft grid file is generated
                                 from the slice of the SEG-Y volume with that crossline
                                 coordinate. The filename will consist of `slice_prefix`
                                 folowed by "_XL???.grd" where ??? is the crossline
                                 coordinate. Only valid for 3D SEG-Y files.
        :param z_slices:         An array-like containing the trace index for slice
                                 grids. If this argument is specified then, for coordinate
                                 in the list a geosoft grid file is generated by taking
                                 the element at that index in the trace data for each
                                 trace. The filename will consist of `slice_prefix`
                                 folowed by "_Z???.grd" where ??? is the z coordinate.
                                 (The parameter values are array indices (0, for the top
                                 of the volumne, 1 for the next slice down, etc.) but the
                                 number in the file name is the z-coordinate in physical
                                 units (e.g. feet, metres, etc,)) Only
                                 valid for 3D SEG-Y files.
        """

        def validate_kwargs(kwargs):
            if 'gdb' in kwargs.keys():
                return True
            if 'voxel' in kwargs.keys():
                return True
            if 'slice_prefix' in kwargs.keys():
                if 'inline_slices' in kwargs.keys():
                    return True
                if 'crossline_slices' in kwargs.keys():
                    return True
                if 'z_slices' in kwargs.keys():
                    return True
            return False
        if not validate_kwargs(kwargs):
            raise ValueError('No output files configured')

        if not self._scan_completed:
            self.scan_file()

        for key, value in kwargs.items():
            if key == 'gdb':
                self._gx_segy_reader.set_gdb_output_filename(value)
            elif key == 'voxel':
                self._gx_segy_reader.set_voxel_output_filename(value)
            elif key == 'slice_prefix':
                self._gx_segy_reader.set_slice_output_prefix(value)
            elif key == 'inline_slices':
                indices_vv = gxvv.GXvv(value).gxvv
                self._gx_segy_reader.set_inline_slice_indices(indices_vv)
            elif key == 'crossline_slices':
                indices_vv = gxvv.GXvv(value).gxvv
                self._gx_segy_reader.set_crossline_slice_indices(indices_vv)
            elif key == 'z_slices':
                indices_vv = gxvv.GXvv(value).gxvv
                self._gx_segy_reader.set_z_slice_indices(indices_vv)
            else:
                raise TypeError('Unexpected keyword argument: {}'.format(key))

        self._gx_segy_reader.export_files()

    def _check_sane_inline_crossline(self):
        is_sane_ref = gxapi.bool_ref()
        possibly_swapped_ref = gxapi.bool_ref()
        only_one_line_ref = gxapi.bool_ref()
        self._gx_segy_reader.check_sane_inline_crossline(
            is_sane_ref, possibly_swapped_ref, only_one_line_ref)
        if is_sane_ref.value:
            return InlineCrosslineSanity.OK
        elif possibly_swapped_ref.value:
            return InlineCrosslineSanity.MAYBE_SWAPPED
        elif only_one_line_ref.value:
            return InlineCrosslineSanity.ONLY_ONE_LINE
        else:
            return InlineCrosslineSanity.UNKNOWN_PROBLEM

    @property
    def text_header(self):
        """
        The text header from the SEG-Y file as a string.

        This is human-readable text and often usefull for configuring the reader.
        """

        result = gxapi.str_ref()
        self._gx_segy_reader.get_text_header(result)
        return result.value

    @property
    def binary_header(self):
        """
        The contents of the SEG-Y binary header, as a dictionary. Usefull for diagnostic
        purposes.
        """

        ltb = self._gx_segy_reader.get_binary_header()
        result = dict()
        for record_num in range(ltb.records()):
            field_name = gxapi.str_ref()
            ltb.get_english_string(record_num, 0, field_name)
            result[field_name.value] = ltb.get_int(record_num, 1)
        return result

    def get_trace_header(self, trace_number):
        ref = gxapi.str_ref()
        self._gx_segy_reader.get_trace_header_as_json(trace_number, ref)
        return json.loads(ref.value)

    def get_trace_data(self, trace_number):
        vv = self._gx_segy_reader.get_trace_data(trace_number)
        # It seems like ther should be an easier and more efficient way to
        # create a gxpy.vv from a gxapi.vv, but if there is I can't find it.
        return gxvv.GXvv(vv.get_data_array(0, vv.length(), gxapi.GS_DOUBLE))

    @property
    def trace_length(self):
        """The number of elements in each trace."""
        return self._gx_segy_reader.get_trace_length()

    @trace_length.setter
    def trace_length(self, value):
        self._gx_segy_reader.set_trace_length_configuration('none', value)

    def get_trace_length_from_file_header(self, offset):
        """
        Specify that `trace_length` should be set to the value from the specified
        byte offset in the binary file header.
        """

        self._gx_segy_reader.set_trace_length_configuration(
            'file_header', offset)

    def get_trace_length_from_trace_header(self, offset):
        """
        Specify that `trace_length` should be set to the value from the specified
        byte offset in the binary trace header.

        Even when this setting is used, the SEG-Y reader still requires that all traces
        be the same length.
        """

        self._gx_segy_reader.set_trace_length_configuration(
            'trace_header', offset)

    @property
    def trace_data_type(self):
        """
        The data type of the trace data in the SEG-Y file. Specified using one of the
        constants defined in the `DataType` Enum.
        """
        ref = gxapi.str_ref()
        self._gx_segy_reader.get_trace_data_type(ref)
        return DataType.from_str(ref.value)

    @trace_data_type.setter
    def trace_data_type(self, data_type):
        if not isinstance(data_type, DataType):
            raise ValueError("Expected DataType instance.")
        self._gx_segy_reader.set_trace_data_type(data_type.value)

    @property
    def trace_sample_interval(self):
        """
        The interval between successive values in the trace data.
        E.g. microseconds or millimetres.
        """

        ref = gxapi.float_ref()
        self._gx_segy_reader.get_sample_interval(ref)
        return ref.value

    @trace_sample_interval.setter
    def trace_sample_interval(self, value):
        self._gx_segy_reader.set_sample_interval_configuration(
            'none', 0, value)

    @property
    def z_units(self):
        """The units used for `trace_sample_interval`"""
        ref = gxapi.str_ref()
        self._gx_segy_reader.get_z_units(ref)
        return ref.value

    @z_units.setter
    def z_units(self, value):
        if value not in self._z_units_list:
            raise ValueError("Unsupported Z units")
        self._gx_segy_reader.set_z_units(value)

    @property
    def z_offset(self):
        """The Z-coordinate of the start (top) of each trace"""
        ref = gxapi.float_ref()
        self._gx_segy_reader.get_z_offset(ref)
        return ref.value

    @z_offset.setter
    def z_offset(self, value):
        self._gx_segy_reader.set_z_offset_configuration('none', 0, value)

    @property
    def z_offset_units(self):
        """The units used for `z_offset`"""
        ref = gxapi.str_ref()
        self._gx_segy_reader.get_z_offset_units(ref)
        return ref.value

    @z_offset_units.setter
    def z_offset_units(self, value):
        if value not in self._z_units_list:
            raise ValueError("Unsupported Z units")
        self._gx_segy_reader.set_z_offset_units(value)

    @property
    def xy_units(self):
        """The horizontal units or the SEG_Y"""
        ref = gxapi.str_ref()
        self._gx_segy_reader.get_xy_units(ref)
        return ref.value

    @property
    def is_depth_or_time(self):
        """The "type" of z-units: either ZType.DEPTH or ZType.TIME."""
        ref = gxapi.str_ref()
        self._gx_segy_reader.get_z_type(ref)
        return ZType[ref.value]

    @property
    def trace_range(self):
        """The depth of the top and bottom of the traces."""
        top = self.z_offset
        bottom_ref = gxapi.float_ref()
        self._gx_segy_reader.get_last_sample_at(bottom_ref)
        return (top, bottom_ref.value)

    @property
    def field_configuration(self):
        if not self._scan_completed:
            self.scan_file()
        return TraceFieldConfiguration(self._gx_segy_reader.get_field_configuration())

    @field_configuration.setter
    def field_configuration(self, field_configuration):
        self._gx_segy_reader.set_field_configuration(field_configuration._ltb)

    def __enter__(self):
        return self

    def __exit__(self, _type, _value, _traceback):
        self.__del__()

    def __del__(self):
        self._gx_segy_reader = None
