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
class GXGER:
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

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapGER(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXGER`
        
        :returns: A null `GXGER`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXGER` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXGER`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, file):
        """
        Opens an ASCII error file to read from.

        **Note:**

        The `GXGER <geosoft.gxapi.GXGER>` file may be in the local directory or the GEOSOFT
        directory.
        """
        ret_val = gxapi_cy.WrapGER.create(GXContext._get_tls_geo(), file.encode())
        return GXGER(ret_val)






    def get(self, num, message):
        """
        Get a message string.
        """
        ret_val, message.value = self._wrapper.get(num, message.value.encode())
        return ret_val




    def set_int(self, parm, set):
        """
        Set a replacement string value to an int.
        """
        self._wrapper.set_int(parm.encode(), set)
        




    def set_double(self, parm, set):
        """
        Set a replacement string value to a real.
        """
        self._wrapper.set_double(parm.encode(), set)
        




    def set_string(self, parm, set):
        """
        Set a replacement string value.
        """
        self._wrapper.set_string(parm.encode(), set.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer