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
class GXMPLY(gxapi_cy.WrapMPLY):
    """
    GXMPLY class.

    The `GXMPLY <geosoft.gxapi.GXMPLY>` object contains the definitions for one or more
    PPLY.
    """

    def __init__(self, handle=0):
        super(GXMPLY, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMPLY <geosoft.gxapi.GXMPLY>`
        
        :returns: A null `GXMPLY <geosoft.gxapi.GXMPLY>`
        :rtype:   GXMPLY
        """
        return GXMPLY()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls):
        """
        Creates a Multi Polygon Object.
        

        :returns:    `GXMPLY <geosoft.gxapi.GXMPLY>` Handle
        :rtype:      GXMPLY

        .. versionadded:: 9.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapMPLY._create(GXContext._get_tls_geo())
        return GXMPLY(ret_val)







### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer