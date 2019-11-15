### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXIPJ import GXIPJ
from .GXLTB import GXLTB
from .GXVV import GXVV


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXSEGYREADER(gxapi_cy.WrapSEGYREADER):
    """
    GXSEGYREADER class.

    Convert 3D SEG Y files to voxel or database.
    """

    def __init__(self, handle=0):
        super(GXSEGYREADER, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSEGYREADER <geosoft.gxapi.GXSEGYREADER>`
        
        :returns: A null `GXSEGYREADER <geosoft.gxapi.GXSEGYREADER>`
        :rtype:   GXSEGYREADER
        """
        return GXSEGYREADER()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def open_file(cls, filename):
        """
        Opens a 3D SEG Y file.
        
        :param filename:  File name
        :type  filename:  str

        :returns:         `GXSEGYREADER <geosoft.gxapi.GXSEGYREADER>` handle, terminates if creation fails.
        :rtype:           GXSEGYREADER

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapSEGYREADER._open_file(GXContext._get_tls_geo(), filename.encode())
        return GXSEGYREADER(ret_val)




    def set_is_3d(self, is_3d):
        """
        Specify if the input SEG-Y file is 3D or 2D.
        
        :param is_3d:        True is file is 3D, false for 2D.
        :type  is_3d:        bool

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_is_3d(is_3d)
        




    def get_is_3d(self):
        """
        Returns true if the file is 3D false if it is 2D.
        
        :rtype:              bool

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._get_is_3d()
        return ret_val




    def get_endianess(self):
        """
        Returns true if the file is little endian. false if it is big endian.
        
        :rtype:              bool

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._get_endianess()
        return ret_val




    def set_endianess(self, is_little_endian):
        """
        Set the endianess of the file.
        
        :param is_little_endian:  True is file is little endian, false for big endian.
        :type  is_little_endian:  bool

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_endianess(is_little_endian)
        




    def get_xy_units(self, xy_units):
        """
        Get the currently-specified xy-units.
        
        :param xy_units:     The name of the units.
        :type  xy_units:     str_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        xy_units.value = self._get_xy_units(xy_units.value.encode())
        




    def set_z_type(self, z_type):
        """
        Specify if the z-dimension is time or depth.
        
        :param z_type:       Either "DEPTH" or "TIME".
        :type  z_type:       str

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_z_type(z_type.encode())
        




    def get_z_type(self, z_type):
        """
        Indicate if the z-dimension is time or depth.
        
        :param z_type:       Either "DEPTH" or "TIME".
        :type  z_type:       str_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        z_type.value = self._get_z_type(z_type.value.encode())
        




    def get_possible_z_units(self, z_units_list):
        """
        Get a list of the possible values that can be passed to `SetZUnits()`. The values returned by this function depend on what the z-type is set to.
        
        :param z_units_list:  List of possible z-units,separated by newlines
        :type  z_units_list:  str_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        z_units_list.value = self._get_possible_z_units(z_units_list.value.encode())
        




    def get_z_units(self, z_units):
        """
        Get the currently-specified z-units.
        
        :param z_units:      The name of the z-units.
        :type  z_units:      str_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        z_units.value = self._get_z_units(z_units.value.encode())
        




    def set_z_units(self, z_units):
        """
        Set the z-units.
        
        :param z_units:      The Z units. Must be one of the strings returned by `GetPossibleZUnits()`.
        :type  z_units:      str

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_z_units(z_units.encode())
        




    def get_z_offset_units(self, z_units):
        """
        Get the currently-specified units for the z offset.
        
        :param z_units:      List of possible z-units,separated by newlines
        :type  z_units:      str_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        z_units.value = self._get_z_offset_units(z_units.value.encode())
        




    def set_z_offset_units(self, z_units):
        """
        Set the units that the z-offset is in.
        
        :param z_units:      The Z units. Must be one of the strings returned by `GetPossibleZUnits()`.
        :type  z_units:      str

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_z_offset_units(z_units.encode())
        




    def get_last_sample_at(self, value):
        """
        Returns the depth of the last sample in the traces, in the units specified by `SetZUnits()`
        
        :param value:        Out-parameter containing the depth of the last sample in the traces.
        :type  value:        float_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        value.value = self._get_last_sample_at(value.value)
        



    @classmethod
    def list_binary_header_fields(cls):
        """
        Returns the names and offsets of the fields in the binary header.
        
        :rtype:      GXLTB

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapSEGYREADER._list_binary_header_fields(GXContext._get_tls_geo())
        return GXLTB(ret_val)



    @classmethod
    def list_trace_header_fields(cls):
        """
        Returns the names and offsets of the fields in the trace header.
        
        :rtype:      GXLTB

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapSEGYREADER._list_trace_header_fields(GXContext._get_tls_geo())
        return GXLTB(ret_val)




    def get_text_header(self, text):
        """
        Get the SEG Y file's text header.
        
        :param text:         The text header contents.
        :type  text:         str_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        text.value = self._get_text_header(text.value.encode())
        




    def get_binary_header(self):
        """
        Get the SEG Y file's binary header.
        

        :returns:            :class:'LTB' containing three columns: the field name, offset, and value. The value column will be in text form, suitable for display to the end user.
        :rtype:              GXLTB

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._get_binary_header()
        return GXLTB(ret_val)




    def get_trace_data_at(self, data_type_name, number_of_samples, current_trace, is_big_endian):
        """
        Get the SEG Y trace file data for a particular data type, number of samples, and starting trace
        
        :param data_type_name:     The name of a supported data type.
        :param number_of_samples:  The number of samples to return
        :param current_trace:      The trace to start at
        :param is_big_endian:      1 for big endian, 0 for small
        :type  data_type_name:     str
        :type  number_of_samples:  int
        :type  current_trace:      int
        :type  is_big_endian:      int

        :returns:                  :class:'VV' containing the data from the traces
        :rtype:                    GXVV

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._get_trace_data_at(data_type_name.encode(), number_of_samples, current_trace, is_big_endian)
        return GXVV(ret_val)




    def get_trace_header_at(self, data_type_name, number_of_samples, current_trace, is_big_endian):
        """
        Get the SEG Y trace file header data for a particular starting trace
        
        :param data_type_name:     The name of a supported data type.
        :param number_of_samples:  The number of samples to return
        :param current_trace:      The trace to start at
        :param is_big_endian:      1 for big endian, 0 for small
        :type  data_type_name:     str
        :type  number_of_samples:  int
        :type  current_trace:      int
        :type  is_big_endian:      int

        :returns:                  :class:'VV' containing the data from the trace header
        :rtype:                    GXVV

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._get_trace_header_at(data_type_name.encode(), number_of_samples, current_trace, is_big_endian)
        return GXVV(ret_val)




    def estimate_number_of_traces(self, data_type_name, number_of_samples):
        """
        Get the number of traces that would be in the SEG-Y file, given a trace length and data type.
        
        :param data_type_name:     The name of a supported data type.
        :param number_of_samples:  The number of samples to return
        :type  data_type_name:     str
        :type  number_of_samples:  int
        :rtype:                    int

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._estimate_number_of_traces(data_type_name.encode(), number_of_samples)
        return ret_val



    @classmethod
    def get_num_trace_data_types(cls):
        """
        Returns the number of supported trace data types.
        
        :rtype:      int

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapSEGYREADER._get_num_trace_data_types(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_trace_data_type_name(cls, index, name):
        """
        Get the name of one of the available data types. These are the names used as identifiers in this API. To get a name suitable for displaying to the user, use `GetTraceDataTypeDisplayName() instead.
        
        :param index:  Which name to return. Call this function  for each value between 0 and the value returned by `GetNumTraceTypes()` to get a full list of the available types.
        :param name:   The name of a supported data type.
        :type  index:  int
        :type  name:   str_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        name.value = gxapi_cy.WrapSEGYREADER._get_trace_data_type_name(GXContext._get_tls_geo(), index, name.value.encode())
        



    @classmethod
    def get_trace_data_type_display_name(cls, index, name):
        """
        Get a string, suitable for displaying to the user, describing the type returned by passing the same `index` value to `GetTraceDataTypeName()`
        
        :param index:  Which name to return.
        :param name:   The display name of a supported data type.
        :type  index:  int
        :type  name:   str_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        name.value = gxapi_cy.WrapSEGYREADER._get_trace_data_type_display_name(GXContext._get_tls_geo(), index, name.value.encode())
        




    def get_trace_data_type(self, name):
        """
        Get the data type of the trace data. This will match one of the names rfeturned by `GetTraceDataTypeName()`
        
        :param name:         The name of data type.
        :type  name:         str_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        name.value = self._get_trace_data_type(name.value.encode())
        




    def set_trace_data_type(self, name):
        """
        Set the data type of the trace data. This must match one of the names returned by `GetTraceDataTypeName()`
        
        :param name:         The name of data type.
        :type  name:         str

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_trace_data_type(name.encode())
        




    def get_trace_length_configuration(self, which_header, location):
        """
        Specifies where the trace length comes from: can be a field in the binary file header, a field in the trace header, or a value specified by the user.
        
        :param which_header:  Out-parameter indicating which header contains the trace length: "file_header" "trace_header", or "none"
        :param location:      Out-parameter containing the byte offset of the field within the header (if applicable)
        :type  which_header:  str_ref
        :type  location:      int_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        which_header.value, location.value = self._get_trace_length_configuration(which_header.value.encode(), location.value)
        




    def set_trace_length_configuration(self, which_header, location_or_value):
        """
        Specifies where the trace length comes from: can be a field in the binary file header, a field in the trace header, or a value specified by the user.
        
        :param which_header:       Which header contains the trace length: "file_header", "trace_header" or "none"
        :param location_or_value:  If `which_header` is "file_header" or "trace_header", then this parameter is the offset of the field containing the trace length. If `which_header` is "none", then this parameter is the actual trace length.
        :type  which_header:       str
        :type  location_or_value:  int

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_trace_length_configuration(which_header.encode(), location_or_value)
        




    def get_trace_length(self):
        """
        Returns the number of data samples per trace.
        
        :rtype:              int

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._get_trace_length()
        return ret_val




    def get_sample_interval_configuration(self, which_header, location):
        """
        Specifies where the sample interval comes from: can be a field in the binary file header, a field in the trace header, or a value specified by the user.
        
        :param which_header:  Out-parameter indicating which header contains the trace length: "file_header" "trace_header", or "none"
        :param location:      Out-parameter containing the byte offset of the field within the header (if applicable)
        :type  which_header:  str_ref
        :type  location:      int_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        which_header.value, location.value = self._get_sample_interval_configuration(which_header.value.encode(), location.value)
        




    def set_sample_interval_configuration(self, which_header, location, location_or_value):
        """
        Specifies where the sample interval comes from: can be a field in the binary file header, a field in the trace header, or a value specified by the user.
        
        :param which_header:       Which header contains the sample interval: "file_header", "trace_header" or "none"
        :param location:           If `which_header` is "file_header" or "trace_header", then this parameter is the offset of the field containing the sample interval. If `which_header` is "none", thenthis parameter is ignored.
        :param location_or_value:  If `which_header` is "file_header" or "trace_header", then this parameter is ignored. If `which_header` is "none", thenthis parameter is the sample interval.
        :type  which_header:       str
        :type  location:           int
        :type  location_or_value:  float

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_sample_interval_configuration(which_header.encode(), location, location_or_value)
        




    def get_sample_interval(self, sample_interval):
        """
        Returns the sample interval of the trace data.
        
        :param sample_interval:  output parameter for sample interval
        :type  sample_interval:  float_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        sample_interval.value = self._get_sample_interval(sample_interval.value)
        




    def get_z_offset_configuration(self, which_header, location):
        """
        Specifies where the z-offset (time delay) comes from: can be a field in the binary file header, a field in the trace header, or a value specified by the user.
        
        :param which_header:  Out-parameter indicating which header contains the z offset: "file_header" "trace_header", or "none"
        :param location:      Out-parameter containing the byte offset of the field within the header (if applicable)
        :type  which_header:  str_ref
        :type  location:      int_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        which_header.value, location.value = self._get_z_offset_configuration(which_header.value.encode(), location.value)
        




    def set_z_offset_configuration(self, which_header, location, value):
        """
        Specifies where the z-offset (time delay) comes from: can be a field in the binary file header, a field in the trace header, or a value specified by the user.
        
        :param which_header:  Which header contains the z offset: "file_header", "trace_header" or "none"
        :param location:      If `which_header` is "file_header" or "trace_header", then this parameter is the offset of the field. If `which_header` is "none", then this parameter is ignored.
        :param value:         If `which_header` is "file_header" or "trace_header", then this parameter is ignored. If `which_header` is "none", then this parameter is the z offset.
        :type  which_header:  str
        :type  location:      int
        :type  value:         float

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_z_offset_configuration(which_header.encode(), location, value)
        




    def get_z_offset(self, z_offset):
        """
        Returns the z-offset (time delay) of the trace data. Positive values correspond to a deeper top-of-trace; negative values to a higher top-of-trace.
        
        :param z_offset:     The z offset/time delay
        :type  z_offset:     float_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        z_offset.value = self._get_z_offset(z_offset.value)
        




    def scan_file(self):
        """
        Scans the SEG Y file, and attempts to guess the layout.
        

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._scan_file()
        




    def get_field_configuration(self):
        """
        Returns information on the data in the trace headers.
        

        :returns:            :class:'LTB' containing trace header information
        :rtype:              GXLTB

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._get_field_configuration()
        return GXLTB(ret_val)




    def set_field_configuration(self, configuration):
        """
        Sets the interpretation of the fields in the SEG Y file, and specifies which fields should be exported to GDB.
        
        :param configuration:  `GXLTB <geosoft.gxapi.GXLTB>` following the same format as returned by `GetFieldConfiguration()`.
        :type  configuration:  GXLTB

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_field_configuration(configuration)
        




    def get_trace_count(self, count):
        """
        Get the number of traces in the SEG Y file
        
        :param count:        Trace count
        :type  count:        int_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        count.value = self._get_trace_count(count.value)
        




    def check_sane_inline_crossline(self, is_sane, possibly_swapped, only_one_line):
        """
        Checks if the currently-configured inline and crossline fields seem sensible.
        
        :param is_sane:           True is inline/crossline values seem sensible.
        :param possibly_swapped:  True if it looks like the inline and crossline fields are swapped.
        :param only_one_line:     True if it looks like the file only contains one line. This may mean the file is 2D.
        :type  is_sane:           bool_ref
        :type  possibly_swapped:  bool_ref
        :type  only_one_line:     bool_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        is_sane.value, possibly_swapped.value, only_one_line.value = self._check_sane_inline_crossline(is_sane.value, possibly_swapped.value, only_one_line.value)
        




    def get_voxel_dimensions(self, x, y, z):
        """
        Get the size of the voxel that would be exported with the current configuration.
        
        :param x:            Voxel size along X
        :param y:            Voxel size along Y
        :param z:            Voxel size along Z
        :type  x:            int_ref
        :type  y:            int_ref
        :type  z:            int_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        x.value, y.value, z.value = self._get_voxel_dimensions(x.value, y.value, z.value)
        




    def get_voxel_cell_size(self, x, y, z):
        """
        Get the cell size of the voxel that would be exported with the current configuration.
        
        :param x:            Voxel cell size along X
        :param y:            Voxel cell size along Y
        :param z:            Voxel cell size along Z
        :type  x:            float_ref
        :type  y:            float_ref
        :type  z:            float_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        x.value, y.value, z.value = self._get_voxel_cell_size(x.value, y.value, z.value)
        




    def set_auto_voxel_cell_size_xy(self):
        """
        Set the XY cell size of the voxel that would be exported to the dimensions calculated from the tie points..
        

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_auto_voxel_cell_size_xy()
        




    def set_user_voxel_cell_size_xy(self, x, y):
        """
        Set the XY cell size of the voxel that would be exported with the current configuration.
        
        :param x:            Voxel cell size along X
        :param y:            Voxel cell size along Y
        :type  x:            float
        :type  y:            float

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_user_voxel_cell_size_xy(x, y)
        




    def get_georeferencing(self):
        """
        Returns the georeferencing of the voxel that would be exported with the current configuration.
        
        :rtype:              GXIPJ

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._get_georeferencing()
        return GXIPJ(ret_val)




    def set_georeferencing(self, ipj):
        """
        Sets the georeferencing of the voxel that would be exported with the current configuration.
        
        :type  ipj:          GXIPJ

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_georeferencing(ipj)
        




    def get_tie_point(self, i, x, y, in_line, cross_line):
        """
        Return  the currently-active tie points. If SetTiePoints() has not already been called, then the returned points will be the automatically-selected ones.
        
        :param i:            Tie point indexl must be 0, 1 or 2.
        :param x:            x-coordinate
        :param y:            inline-coordinate
        :param in_line:      Tie point index.
        :param cross_line:   crossline-coordinate
        :type  i:            int
        :type  x:            float_ref
        :type  y:            float_ref
        :type  in_line:      int_ref
        :type  cross_line:   int_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        x.value, y.value, in_line.value, cross_line.value = self._get_tie_point(i, x.value, y.value, in_line.value, cross_line.value)
        




    def set_tie_point(self, i, x, y, in_line, cross_line):
        """
        Set the currently-active tie points. If SetTiePoints() has not already been called, then the returned points will be the automatically-selected ones.
        
        :param i:            Tie point index.
        :param x:            x-coordinate
        :param y:            inline-coordinate
        :param in_line:      Tie point index.
        :param cross_line:   crossline-coordinate
        :type  i:            int
        :type  x:            float
        :type  y:            float
        :type  in_line:      int
        :type  cross_line:   int

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_tie_point(i, x, y, in_line, cross_line)
        




    def recalculate_georeferencing(self):
        """
        Recalculate georeferencing; call after configuration has changed.
        

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._recalculate_georeferencing()
        




    def reset_tie_points(self):
        """
        Discard user-supplied tie points and auto-choose new ones..
        

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._reset_tie_points()
        




    def get_inline_and_crossline_azimuths(self, inline_azimuth, crossline_azimuth):
        """
        Get the inline and crossline azimuths, in degrees
        
        :param inline_azimuth:     Inline azimuth
        :param crossline_azimuth:  Crossline azimuth
        :type  inline_azimuth:     float_ref
        :type  crossline_azimuth:  float_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        inline_azimuth.value, crossline_azimuth.value = self._get_inline_and_crossline_azimuths(inline_azimuth.value, crossline_azimuth.value)
        




    def export_voxel_and_database(self, voxel_filename, gdb_filename):
        """
        Exports contents of SEG Y file to voxel and/or database.
        
        :param voxel_filename:  Output voxel file name
        :param gdb_filename:    Output database file name
        :type  voxel_filename:  str
        :type  gdb_filename:    str

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._export_voxel_and_database(voxel_filename.encode(), gdb_filename.encode())
        




    def set_gdb_output_filename(self, filename):
        """
        Exports contents of SEG Y file to a database.
        
        :param filename:     Output database file name
        :type  filename:     str

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_gdb_output_filename(filename.encode())
        




    def set_voxel_output_filename(self, filename):
        """
        Exports contents of SEG Y file to voxel.
        
        :param filename:     Output voxel file name
        :type  filename:     str

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_voxel_output_filename(filename.encode())
        




    def set_section_output_filename(self, filename):
        """
        Exports contents of SEG Y file to a crooked section.
        
        :param filename:     Output crooked section file name
        :type  filename:     str

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_section_output_filename(filename.encode())
        




    def set_slice_output_prefix(self, prefix):
        """
        Exports inline or crossline slices to a section grid.
        
        :param prefix:       Output section file name prefix
        :type  prefix:       str

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_slice_output_prefix(prefix.encode())
        




    def set_inline_slice_indices(self, indices):
        """
        Which inline slices to export to a section grid.
        
        :param indices:      Which inline values to export.
        :type  indices:      GXVV

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_inline_slice_indices(indices)
        




    def set_crossline_slice_indices(self, indices):
        """
        Which crossline slices to export to a section grid.
        
        :param indices:      Which crossline values to export.
        :type  indices:      GXVV

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_crossline_slice_indices(indices)
        




    def set_z_slice_indices(self, indices):
        """
        Which z slices to export to a section grid.
        
        :param indices:      Which z values to export.
        :type  indices:      GXVV

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_z_slice_indices(indices)
        




    def get_slice_filenames(self, filename_list):
        """
        Returns a list of the filenames of the XY slices that will be exported.
        
        :param filename_list:  List of filenames,separated by newlines
        :type  filename_list:  str_ref

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        filename_list.value = self._get_slice_filenames(filename_list.value.encode())
        




    def set_z_decimation(self, factor):
        """
        Sets Z decimation factor.
        
        :param factor:       Decimation factor
        :type  factor:       int

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_z_decimation(factor)
        




    def set_user_z_range(self, z_min, z_max):
        """
        Sets Z-range to clamp to.
        
        :param z_min:        Z minimum
        :param z_max:        Z maximum
        :type  z_min:        float
        :type  z_max:        float

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_user_z_range(z_min, z_max)
        




    def clear_user_z_range(self):
        """
        Clears Z-range to clamp to, disbling z-clamping.
        

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._clear_user_z_range()
        




    def set_user_inline_range(self, inline_min, inline_max, inline_stride, factor):
        """
        Sets inline-range to clamp to.
        
        :param inline_min:     inline minimum
        :param inline_max:     inline maximum
        :param inline_stride:  inline stride
        :param factor:         Decimation factor
        :type  inline_min:     int
        :type  inline_max:     int
        :type  inline_stride:  int
        :type  factor:         int

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_user_inline_range(inline_min, inline_max, inline_stride, factor)
        




    def set_user_crossline_range(self, crossline_min, crossline_max, crossline_stride, factor):
        """
        Sets crossline-range to clamp to.
        
        :param crossline_min:     crossline minimum
        :param crossline_max:     crossline maximum
        :param crossline_stride:  crossline stride
        :param factor:            Decimation factor
        :type  crossline_min:     int
        :type  crossline_max:     int
        :type  crossline_stride:  int
        :type  factor:            int

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_user_crossline_range(crossline_min, crossline_max, crossline_stride, factor)
        




    def clear_user_range(self):
        """
        Clears inline and crossline ranges to clamp to.
        

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._clear_user_range()
        




    def set_trace_dummy_value(self, dummy_value):
        """
        Sets the trace dummy value.
        
        :param dummy_value:  trace dummy value
        :type  dummy_value:  float

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_trace_dummy_value(dummy_value)
        




    def clear_trace_dummy_value(self):
        """
        Disables the trace dummy value.
        

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._clear_trace_dummy_value()
        




    def get_clip_xy_extents(self, is_clip_valid, x_min, x_max, y_min, y_max):
        """
        Gets the X,Y extents to clip the voxel.
        
        :param is_clip_valid:  is clip area valid
        :param x_min:          minimum X value
        :param x_max:          maximum X value
        :param y_min:          minimum Y value
        :param y_max:          maximum Y value
        :type  is_clip_valid:  int_ref
        :type  x_min:          float_ref
        :type  x_max:          float_ref
        :type  y_min:          float_ref
        :type  y_max:          float_ref

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        is_clip_valid.value, x_min.value, x_max.value, y_min.value, y_max.value = self._get_clip_xy_extents(is_clip_valid.value, x_min.value, x_max.value, y_min.value, y_max.value)
        




    def add_trace_filter(self, offset, value1, value2, constraint):
        """
        Add a filter based on trace header fields.
        
        :param offset:       byte-offset of the field to filter by.
        :param value1:       If `constraint` is EQUAL and NOT_EQUAL, this is the value to compare the field to. For IN_RANGE and NOT_IN_RANGE, this is the minimum.
        :param value2:       If `constraint` is EQUAL and NOT_EQUAL, this parameter is ignored For IN_RANGE and NOT_IN_RANGE, this is the maximum.
        :param constraint:   How the values are compared. Can be "IN_RANGE", "NOT_IN_RANGE", "EQUAL" or "NOT_EQUAL".
        :type  offset:       int
        :type  value1:       int
        :type  value2:       int
        :type  constraint:   str

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._add_trace_filter(offset, value1, value2, constraint.encode())
        




    def clear_trace_filters(self):
        """
        Remove all active trace filters.
        

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._clear_trace_filters()
        




    def count_traces_that_pass_filters(self):
        """
        Count the number of traces that pass the currently-configured trace filters.
        
        :rtype:              int

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._count_traces_that_pass_filters()
        return ret_val




    def override_navigation_2d(self, shotpoint_coords, x_coordinates, y_coordinates):
        """
        Specify the X/Y coordinates of the traces, instead of using values from the trace headers.
        
        :param shotpoint_coords:  The shotpoint coordinates, asread from the trace headers.
        :param x_coordinates:     The x-coordinates
        :param y_coordinates:     The y-coordinates
        :type  shotpoint_coords:  GXVV
        :type  x_coordinates:     GXVV
        :type  y_coordinates:     GXVV

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._override_navigation_2d(shotpoint_coords, x_coordinates, y_coordinates)
        




    def export_files(self):
        """
        Exports contents of SEG Y file to voxel and/or database.
        

        .. versionadded:: 9.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._export_files()
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer