### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXIPJ import GXIPJ
from .GXLTB import GXLTB


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
        super().__init__(GXContext._get_tls_geo(), handle)

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
        
        :param z_units:      List of possible z-units,separated by newlines
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
        




    def has_sane_setup(self, error_messages):
        """
        Returns true if reader has a valid configuration and passes some basic sanity checks. If this function returns false, `Export()` will not run and some of the getters may return garbage values.
        
        :param error_messages:  A string, suitable for displaying to the user, indicating why the configuration is not valid. (Ignore this string if the function returns true.
        :type  error_messages:  str_ref
        :rtype:                 int

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val, error_messages.value = self._has_sane_setup(error_messages.value.encode())
        return ret_val



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
        




    def get_num_tie_points(self):
        """
        Get the number of tie points.
        
        :rtype:              int

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = self._get_num_tie_points()
        return ret_val




    def get_tie_point(self, i, x, y, inline, crossline):
        """
        Return  the currently-active tie points. If SetTiePoints() has not already been called, then the returned points will be the automatically-selected ones.
        
        :param i:            Tie point index.
        :param x:            x-coordinate
        :param y:            inline-coordinate
        :param inline:       Tie point index.
        :param crossline:    crossline-coordinate
        :type  i:            int
        :type  x:            float_ref
        :type  y:            float_ref
        :type  inline:       int_ref
        :type  crossline:    int_ref

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        x.value, y.value, inline.value, crossline.value = self._get_tie_point(i, x.value, y.value, inline.value, crossline.value)
        




    def set_num_tie_points(self, count):
        """
        Get the number of tie points.
        
        :param count:        Number of tie points
        :type  count:        int

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_num_tie_points(count)
        




    def set_tie_point(self, i, x, y, inline, crossline):
        """
        Set the currently-active tie points. If SetTiePoints() has not already been called, then the returned points will be the automatically-selected ones.
        
        :param i:            Tie point index.
        :param x:            x-coordinate
        :param y:            inline-coordinate
        :param inline:       Tie point index.
        :param crossline:    crossline-coordinate
        :type  i:            int
        :type  x:            float
        :type  y:            float
        :type  inline:       int
        :type  crossline:    int

        .. versionadded:: 9.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._set_tie_point(i, x, y, inline, crossline)
        




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
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer