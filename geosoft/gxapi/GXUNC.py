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
class GXUNC(gxapi_cy.WrapUNC):
    """
    GXUNC class.

    This library is not a class. Use the `GXUNC <geosoft.gxapi.GXUNC>` library functions
    to work with Unicode characters and strings. Since version 6.2
    all strings are represented internally in the the GX engine
    as UTF-8. The character set concept was discarded as a way to
    work with characters that does not fall within the normal
    ASCII range 0x01-0x7F. The utilities here aids with any new
    functionality that is now possible (e.g. an expanded symbol range
    with TrueType fonts).
    """

    def __init__(self, handle=0):
        super(GXUNC, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXUNC <geosoft.gxapi.GXUNC>`
        
        :returns: A null `GXUNC <geosoft.gxapi.GXUNC>`
        :rtype:   GXUNC
        """
        return GXUNC()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# UTF


    @classmethod
    def is_valid_utf16_char(cls, ch):
        """
        Check if the UTF-16 value is a valid Unicode character code point.
        
        :param ch:  UTF-16 value (32-bit int, lower 16 bits used, upper bits reserved for future use)
        :type  ch:  int
        :rtype:      bool

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapUNC._is_valid_utf16_char(GXContext._get_tls_geo(), ch)
        return ret_val



    @classmethod
    def valid_symbol(cls, face, geofont, number):
        """
        See if a Symbol number is valid in a particular font.
        
        :param face:     Face name (undecorated)
        :param geofont:  Geosoft font?
        :param number:   Symbol number
        :type  face:     str
        :type  geofont:  bool
        :type  number:   int
        :rtype:          bool

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapUNC._valid_symbol(GXContext._get_tls_geo(), face.encode(), geofont, number)
        return ret_val



    @classmethod
    def utf16_val_to_str(cls, ch, str_val):
        """
        Convert a UTF-16 value to a UTF-8 encoded string.
        
        :param ch:       UTF-16 value (32-bit int, lower 16 bits used, upper bits reserved for future use)
        :param str_val:  Converted string
        :type  ch:       int
        :type  str_val:  str_ref

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** An empty string will be returned for invalid symbols
        """
        str_val.value = gxapi_cy.WrapUNC._utf16_val_to_str(GXContext._get_tls_geo(), ch, str_val.value.encode())
        



    @classmethod
    def validate_symbols(cls, vv, face, geofont):
        """
        High performance method to see if a set of symbols
        are valid in a particular font.
        
        :param vv:       `GXVV <geosoft.gxapi.GXVV>` of symbols
        :param face:     Face name (undecorated)
        :param geofont:  Geosoft font?
        :type  vv:       GXVV
        :type  face:     str
        :type  geofont:  bool

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Invalid symbols in the `GXVV <geosoft.gxapi.GXVV>` will be set to -1 by this call. `GXVV <geosoft.gxapi.GXVV>` has to be of type `GS_LONG <geosoft.gxapi.GS_LONG>`.
        """
        gxapi_cy.WrapUNC._validate_symbols(GXContext._get_tls_geo(), vv, face.encode(), geofont)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer