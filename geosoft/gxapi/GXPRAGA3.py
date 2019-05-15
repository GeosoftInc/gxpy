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
class GXPRAGA3(gxapi_cy.WrapPRAGA3):
    """
    GXPRAGA3 class.

    `GXPRAGA3 <geosoft.gxapi.GXPRAGA3>` application methods

    **Note:**

    No notes
    """

    def __init__(self, handle=0):
        super(GXPRAGA3, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXPRAGA3 <geosoft.gxapi.GXPRAGA3>`
        
        :returns: A null `GXPRAGA3 <geosoft.gxapi.GXPRAGA3>`
        :rtype:   GXPRAGA3
        """
        return GXPRAGA3()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def launch(cls):
        """
        This method launches the application.
        

        :returns:    1 - OK, 2 - Cancel
        :rtype:      int

        .. versionadded:: 6.4

        **License:** `Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-ext-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapPRAGA3._launch(GXContext._get_tls_geo())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer