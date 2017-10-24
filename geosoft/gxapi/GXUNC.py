### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXUNC:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapUNC(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXUNC':
        """
        A null (undefined) instance of :class:`GXUNC`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXUNC` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXUNC`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# UTF


    @classmethod
    def is_valid_utf16_char(cls, p1: int) -> int:
        ret_val = gxapi_cy.WrapUNC.is_valid_utf16_char(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def valid_symbol(cls, p1: str, p2: int, p3: int) -> int:
        ret_val = gxapi_cy.WrapUNC.valid_symbol(GXContext._get_tls_geo(), p1.encode(), p2, p3)
        return ret_val



    @classmethod
    def utf16_val_to_str(cls, p1: int, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapUNC.utf16_val_to_str(GXContext._get_tls_geo(), p1, p2.value.encode())
        



    @classmethod
    def validate_symbols(cls, p1: 'GXVV', p2: str, p3: int) -> None:
        gxapi_cy.WrapUNC.validate_symbols(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer