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
class GXSTRINGS(gxapi_cy.WrapSTRINGS):
    """
    GXSTRINGS class.

    The `GXSTRINGS <geosoft.gxapi.GXSTRINGS>` class is used for displaying digitization tools for interpretations
    """

    def __init__(self, handle=0):
        super(GXSTRINGS, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSTRINGS <geosoft.gxapi.GXSTRINGS>`
        
        :returns: A null `GXSTRINGS <geosoft.gxapi.GXSTRINGS>`
        :rtype:   GXSTRINGS
        """
        return GXSTRINGS()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



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

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSTRINGS._launch_digitization_ui(GXContext._get_tls_geo(), stringfile.encode(), feature_guid.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer