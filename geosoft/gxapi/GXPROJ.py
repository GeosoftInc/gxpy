### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXPROJ:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPROJ(0)

    @classmethod
    def null(cls) -> 'GXPROJ':
        """
        A null (undefined) instance of :class:`GXPROJ`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXPROJ` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXPROJ`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Drag-and-drop methods


    @classmethod
    def drop_map_clip_data(cls, p1: int) -> None:
        gxapi_cy.WrapPROJ.drop_map_clip_data(GXContext._get_tls_geo(), p1)
        




# Miscellaneous


    @classmethod
    def add_document(cls, p1: str, p2: str, p3: int) -> int:
        ret_val = gxapi_cy.WrapPROJ.add_document(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        return ret_val



    @classmethod
    def add_document_without_opening(cls, p1: str, p2: str) -> int:
        ret_val = gxapi_cy.WrapPROJ.add_document_without_opening(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def get_command_environment(cls) -> int:
        ret_val = gxapi_cy.WrapPROJ.get_command_environment(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def list_documents(cls, p1: 'GXVV', p2: str) -> int:
        ret_val = gxapi_cy.WrapPROJ.list_documents(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return ret_val



    @classmethod
    def list_loaded_documents(cls, p1: 'GXVV', p2: str) -> int:
        ret_val = gxapi_cy.WrapPROJ.list_loaded_documents(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return ret_val



    @classmethod
    def current_document(cls, p1: str_ref, p3: str_ref) -> None:
        p1.value, p3.value = gxapi_cy.WrapPROJ.current_document(GXContext._get_tls_geo(), p1.value.encode(), p3.value.encode())
        



    @classmethod
    def current_document_of_type(cls, p1: str_ref, p3: str) -> None:
        p1.value = gxapi_cy.WrapPROJ.current_document_of_type(GXContext._get_tls_geo(), p1.value.encode(), p3.encode())
        



    @classmethod
    def list_tools(cls, p1: 'GXLST', p2: int) -> int:
        ret_val = gxapi_cy.WrapPROJ.list_tools(GXContext._get_tls_geo(), p1._wrapper, p2)
        return ret_val



    @classmethod
    def remove_document(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapPROJ.remove_document(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def remove_tool(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapPROJ.remove_tool(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def save_close_documents(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapPROJ.save_close_documents(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def get_name(cls, p1: str_ref) -> None:
        p1.value = gxapi_cy.WrapPROJ.get_name(GXContext._get_tls_geo(), p1.value.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer