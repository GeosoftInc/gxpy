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
class GXGER(gxapi_cy.WrapGER):
    """
    GXGER class.

    Allows access to a Geosoft format error message file. This class
    does not in itself produce an error message, but retrieves a
    selected message from the file, and allows the
    setting of replacement parameters within the message. It
    is up to the user to display or use the message.

    **Note:**

    `GXGER <geosoft.gxapi.GXGER>` message files contain numbered messages that can be used within GXs.
    Following is an example from the file GEOSOFT.`GXGER <geosoft.gxapi.GXGER>`:


          #20008
          ! Invalid password. The product installation has failed.

          #20009
          ! Unable to find INI file: %1
          ! See the documentation for details


    A '#' character in column 1 indicates a message number.  The message
    follows on lines that begin with a '!' character.  Strings in the message
    may be replaced at run time with values using the `set_string <geosoft.gxapi.GXGER.set_string>`,
    `set_int <geosoft.gxapi.GXGER.set_int>` and `set_double <geosoft.gxapi.GXGER.set_double>` methods. The iGet_GER will return the message
    with strings replaced by their settings.  By convention, we recommend
    that you use "%1", "%2", etc. as replacement strings.
    """

    def __init__(self, handle=0):
        super(GXGER, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXGER <geosoft.gxapi.GXGER>`
        
        :returns: A null `GXGER <geosoft.gxapi.GXGER>`
        :rtype:   GXGER
        """
        return GXGER()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, file):
        """
        Opens an ASCII error file to read from.
        
        :param file:  `GXGER <geosoft.gxapi.GXGER>` file name.
        :type  file:  str

        :returns:     `GXGER <geosoft.gxapi.GXGER>` Object
        :rtype:       GXGER

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXGER <geosoft.gxapi.GXGER>` file may be in the local directory or the GEOSOFT
        directory.
        """
        ret_val = gxapi_cy.WrapGER._create(GXContext._get_tls_geo(), file.encode())
        return GXGER(ret_val)






    def get(self, num, message):
        """
        Get a message string.
        
        :param num:      Message number
        :param message:  Message string returned, replacements filtered
        :type  num:      int
        :type  message:  str_ref

        :returns:        0 if message found
                         1 if no message, passed message remains unchanged
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val, message.value = self._get(num, message.value.encode())
        return ret_val




    def set_int(self, parm, set):
        """
        Set a replacement string value to an int.
        
        :param parm:  Replacement string (ie. "%1")
        :param set:   Setting
        :type  parm:  str
        :type  set:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_int(parm.encode(), set)
        




    def set_double(self, parm, set):
        """
        Set a replacement string value to a real.
        
        :param parm:  Replacement string (ie. "%1")
        :param set:   Setting
        :type  parm:  str
        :type  set:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_double(parm.encode(), set)
        




    def set_string(self, parm, set):
        """
        Set a replacement string value.
        
        :param parm:  Replacement string (ie. "%1")
        :param set:   Setting
        :type  parm:  str
        :type  set:   str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_string(parm.encode(), set.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer