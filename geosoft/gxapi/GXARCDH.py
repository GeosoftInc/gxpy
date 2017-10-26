### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXARCDH:
    """
    GXARCDH class.

    This library is not a class. It contains various utilities
    used in the Target extension for ArcGIS.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapARCDH(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXARCDH`
        
        :returns: A null `GXARCDH`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXARCDH` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXARCDH`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def close_project(cls):
        """
        Closes the current `GXDH` project in the Target extension
        """
        gxapi_cy.WrapARCDH.close_project(GXContext._get_tls_geo())
        



    @classmethod
    def set_project(cls, path, project):
        """
        Sets the current `GXDH` project in the Target extension
        """
        gxapi_cy.WrapARCDH.set_project(GXContext._get_tls_geo(), path.encode(), project.encode())
        



    @classmethod
    def set_string_file_gdb(cls, string_file_gdb):
        """
        Sets the current Geostring File Geodatabase in the Target extension
        """
        gxapi_cy.WrapARCDH.set_string_file_gdb(GXContext._get_tls_geo(), string_file_gdb.encode())
        



    @classmethod
    def stop_editing_string_file_gdb(cls):
        """
        Stops editing session for current string fGDB
        """
        gxapi_cy.WrapARCDH.stop_editing_string_file_gdb(GXContext._get_tls_geo())
        



    @classmethod
    def has_string_file_gdb_edits(cls):
        """
        Is a Geostring File Geodatabase loaded and contains edits?
        """
        ret_val = gxapi_cy.WrapARCDH.has_string_file_gdb_edits(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def geostrings_extension_available(cls):
        """
        Verifies if the geostrings extension in TfA is available. Return 1 if true, 0 otherwise
        """
        ret_val = gxapi_cy.WrapARCDH.geostrings_extension_available(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_current_string_file_gdb(cls, name):
        """
        Gets the current Geostring File Geodatabase.
        """
        name.value = gxapi_cy.WrapARCDH.get_current_string_file_gdb(GXContext._get_tls_geo(), name.value.encode())
        



    @classmethod
    def is_valid_fgdb_file_name(cls, fgdb):
        """
        Is this a valid FGDB filename?
        """
        ret_val = gxapi_cy.WrapARCDH.is_valid_fgdb_file_name(GXContext._get_tls_geo(), fgdb.encode())
        return ret_val



    @classmethod
    def is_valid_feature_class_name(cls, feature_class_name):
        """
        Is this a valid featureclass name?
        """
        ret_val = gxapi_cy.WrapARCDH.is_valid_feature_class_name(GXContext._get_tls_geo(), feature_class_name.encode())
        return ret_val



    @classmethod
    def s_prompt_for_esri_symbol(cls, hwnd, h_wnd, input_xml_string, p4, p6, p7):
        """
        Prompt the user to select an ESRI symbol and return it as an XML string. The output string will be empty if the user cancels the dialog.
        """
        p4.value, p6.value, p7.value = gxapi_cy.WrapARCDH.s_prompt_for_esri_symbol(GXContext._get_tls_geo(), hwnd, h_wnd.encode(), input_xml_string, p4.value.encode(), p6.value, p7.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer