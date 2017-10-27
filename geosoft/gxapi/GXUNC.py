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
class GXUNC:
    """
    GXUNC class.

    This library is not a class. Use the `GXUNC` library functions
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
    def null(cls):
        """
        A null (undefined) instance of `GXUNC`
        
        :returns: A null `GXUNC`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXUNC` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXUNC`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# UTF


    @classmethod
    def is_valid_utf16_char(cls, ch):
        """
        Check if the UTF-16 value is a valid Unicode character code point.
        """
        ret_val = gxapi_cy.WrapUNC.is_valid_utf16_char(GXContext._get_tls_geo(), ch)
        return ret_val



    @classmethod
    def valid_symbol(cls, face, geofont, number):
        """
        See if a Symbol number is valid in a particular font.
        """
        ret_val = gxapi_cy.WrapUNC.valid_symbol(GXContext._get_tls_geo(), face.encode(), geofont, number)
        return ret_val



    @classmethod
    def utf16_val_to_str(cls, ch, str_val):
        """
        Convert a UTF-16 value to a UTF-8 encoded string.

        **Note:**

        An empty string will be returned for invalid symbols
        """
        str_val.value = gxapi_cy.WrapUNC.utf16_val_to_str(GXContext._get_tls_geo(), ch, str_val.value.encode())
        



    @classmethod
    def validate_symbols(cls, vv, face, geofont):
        """
        High performance method to see if a set of symbols
        are valid in a particular font.

        **Note:**

        Invalid symbols in the `GXVV` will be set to -1 by this call. `GXVV` has to be of type `GS_LONG`.
        """
        gxapi_cy.WrapUNC.validate_symbols(GXContext._get_tls_geo(), vv._wrapper, face.encode(), geofont)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer