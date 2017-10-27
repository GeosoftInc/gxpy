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
class GXSTRINGS:
    """
    GXSTRINGS class.

    The `GXSTRINGS <geosoft.gxapi.GXSTRINGS>` class is used for displaying digitization tools for interpretations
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSTRINGS(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSTRINGS`
        
        :returns: A null `GXSTRINGS`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXSTRINGS` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXSTRINGS`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def launch_digitization_ui(cls, stringfile, feature_guid):
        """
        Launch Digitization modeless window
        
        :param stringfile:    String file
        :param feature_guid:  Definition guid
        :type  stringfile:    str
        :type  feature_guid:  str

        .. versionadded:: 7.5
        """
        gxapi_cy.WrapSTRINGS.launch_digitization_ui(GXContext._get_tls_geo(), stringfile.encode(), feature_guid.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer