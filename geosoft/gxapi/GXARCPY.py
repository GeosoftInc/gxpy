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
class GXARCPY(gxapi_cy.WrapARCPY):
    """
    GXARCPY class.

    This library allows legacy GX code to call back into 
    arcpy methods in the Geosoft AddIn for ArcGIS Pro.
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXARCPY <geosoft.gxapi.GXARCPY>`
        
        :returns: A null `GXARCPY <geosoft.gxapi.GXARCPY>`
        :rtype:   GXARCPY
        """
        return GXARCPY()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def add_message(cls, message):
        """
        Add informational message to output of current script
        
        :param message:  Message
        :type  message:  str

        .. versionadded:: 9.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapARCPY._add_message(GXContext._get_tls_geo(), message.encode())
        



    @classmethod
    def add_warning(cls, message):
        """
        Add warning message to output of current script
        
        :param message:  Message
        :type  message:  str

        .. versionadded:: 9.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapARCPY._add_warning(GXContext._get_tls_geo(), message.encode())
        



    @classmethod
    def add_error(cls, message):
        """
        Add error message to output of current script
        
        :param message:  Message
        :type  message:  str

        .. versionadded:: 9.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapARCPY._add_error(GXContext._get_tls_geo(), message.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer