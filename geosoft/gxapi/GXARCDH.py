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
class GXARCDH:
    """
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
    def null(cls) -> 'GXARCDH':
        """
        A null (undefined) instance of :class:`GXARCDH`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXARCDH` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXARCDH`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def close_project(cls) -> None:
        gxapi_cy.WrapARCDH.close_project(GXContext._get_tls_geo())
        



    @classmethod
    def set_project(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapARCDH.set_project(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def set_string_file_gdb(cls, p1: str) -> None:
        gxapi_cy.WrapARCDH.set_string_file_gdb(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def stop_editing_string_file_gdb(cls) -> None:
        gxapi_cy.WrapARCDH.stop_editing_string_file_gdb(GXContext._get_tls_geo())
        



    @classmethod
    def has_string_file_gdb_edits(cls) -> int:
        ret_val = gxapi_cy.WrapARCDH.has_string_file_gdb_edits(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def geostrings_extension_available(cls) -> int:
        ret_val = gxapi_cy.WrapARCDH.geostrings_extension_available(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_current_string_file_gdb(cls, p1: str_ref) -> None:
        p1.value = gxapi_cy.WrapARCDH.get_current_string_file_gdb(GXContext._get_tls_geo(), p1.value.encode())
        



    @classmethod
    def is_valid_fgdb_file_name(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapARCDH.is_valid_fgdb_file_name(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def is_valid_feature_class_name(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapARCDH.is_valid_feature_class_name(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def s_prompt_for_esri_symbol(cls, p1: int, p2: str, p3: int, p4: str_ref, p6: int_ref, p7: int_ref) -> None:
        p4.value, p6.value, p7.value = gxapi_cy.WrapARCDH.s_prompt_for_esri_symbol(GXContext._get_tls_geo(), p1, p2.encode(), p3, p4.value.encode(), p6.value, p7.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer