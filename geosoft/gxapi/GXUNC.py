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
class GXUNC:
    """
    GXUNC class.

    This library is not a class. Use the :class:`GXUNC` library functions
    to work with Unicode characters and strings. Since version 6.2
    all strings are represented internally in the the GX engine
    as UTF-8. The character set concept was discarded as a way to
    work with characters that does not fall within the normal
    ASCII range 0x01-0x7F. The utilities here aids with any new
    functionality that is now possible (e.g. an expanded symbol range
    with TrueType fonts).
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
        
        :returns: A null :class:`GXUNC`
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