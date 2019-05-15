### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXARCDH(gxapi_cy.WrapARCDH):
    """
    GXARCDH class.

    This library is not a class. It contains various utilities
    used in the Target extension for ArcGIS.
    """

    def __init__(self, handle=0):
        super(GXARCDH, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXARCDH <geosoft.gxapi.GXARCDH>`
        
        :returns: A null `GXARCDH <geosoft.gxapi.GXARCDH>`
        :rtype:   GXARCDH
        """
        return GXARCDH()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def close_project(cls):
        """
        Closes the current `GXDH <geosoft.gxapi.GXDH>` project in the Target extension
        

        .. versionadded:: 8.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapARCDH._close_project(GXContext._get_tls_geo())
        



    @classmethod
    def set_project(cls, path, project):
        """
        Sets the current `GXDH <geosoft.gxapi.GXDH>` project in the Target extension
        
        :param path:     Path String
        :param project:  Project Name
        :type  path:     str
        :type  project:  str

        .. versionadded:: 8.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapARCDH._set_project(GXContext._get_tls_geo(), path.encode(), project.encode())
        



    @classmethod
    def set_string_file_gdb(cls, string_file_gdb):
        """
        Sets the current Geostring File Geodatabase in the Target extension
        
        :param string_file_gdb:  File Geodatabase
        :type  string_file_gdb:  str

        .. versionadded:: 8.0

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapARCDH._set_string_file_gdb(GXContext._get_tls_geo(), string_file_gdb.encode())
        



    @classmethod
    def stop_editing_string_file_gdb(cls):
        """
        Stops editing session for current string fGDB
        

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        gxapi_cy.WrapARCDH._stop_editing_string_file_gdb(GXContext._get_tls_geo())
        



    @classmethod
    def has_string_file_gdb_edits(cls):
        """
        Is a Geostring File Geodatabase loaded and contains edits?
        
        :rtype:      int

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapARCDH._has_string_file_gdb_edits(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def geostrings_extension_available(cls):
        """
        Verifies if the geostrings extension in TfA is available. Return 1 if true, 0 otherwise
        
        :rtype:      int

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapARCDH._geostrings_extension_available(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_current_string_file_gdb(cls, name):
        """
        Gets the current Geostring File Geodatabase.
        
        :param name:  Name returned
        :type  name:  str_ref

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        name.value = gxapi_cy.WrapARCDH._get_current_string_file_gdb(GXContext._get_tls_geo(), name.value.encode())
        



    @classmethod
    def is_valid_fgdb_file_name(cls, fgdb):
        """
        Is this a valid FGDB filename?
        
        :param fgdb:  FGDB filename
        :type  fgdb:  str
        :rtype:       int

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapARCDH._is_valid_fgdb_file_name(GXContext._get_tls_geo(), fgdb.encode())
        return ret_val



    @classmethod
    def is_valid_feature_class_name(cls, feature_class_name):
        """
        Is this a valid featureclass name?
        
        :param feature_class_name:  Featureclass name
        :type  feature_class_name:  str
        :rtype:                     int

        .. versionadded:: 8.0.1

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapARCDH._is_valid_feature_class_name(GXContext._get_tls_geo(), feature_class_name.encode())
        return ret_val



    @classmethod
    def s_prompt_for_esri_symbol(cls, hwnd, h_wnd, input_xml_string, xml, fill_color, edge_color):
        """
        Prompt the user to select an ESRI symbol and return it as an XML string. The output string will be empty if the user cancels the dialog.
        
        :param hwnd:              Window handle
        :param h_wnd:             Initial symbol that you want displayed when the dialog is launched (use "" if none)
        :param input_xml_string:  (This parameter is ignored if an initial symbol was specified) Initial symbol type that you want displayed when the dialog is launched (0 for Fill, 1 for Line)
        :param xml:               Returned XML string representing the symbol that was chosen by the user
        :param fill_color:        RGBA representation of fill color to be set
        :param edge_color:        RGBA representation of edge color to be set
        :type  hwnd:              int
        :type  h_wnd:             str
        :type  input_xml_string:  int
        :type  xml:               str_ref
        :type  fill_color:        int_ref
        :type  edge_color:        int_ref

        .. versionadded:: 8.2

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        xml.value, fill_color.value, edge_color.value = gxapi_cy.WrapARCDH._s_prompt_for_esri_symbol(GXContext._get_tls_geo(), hwnd, h_wnd.encode(), input_xml_string, xml.value.encode(), fill_color.value, edge_color.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer