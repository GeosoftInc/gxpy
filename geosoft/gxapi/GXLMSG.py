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
class GXLMSG(gxapi_cy.WrapLMSG):
    """
    GXLMSG class.

    Message class methods.
    """

    def __init__(self, handle=0):
        super(GXLMSG, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXLMSG <geosoft.gxapi.GXLMSG>`
        
        :returns: A null `GXLMSG <geosoft.gxapi.GXLMSG>`
        :rtype:   GXLMSG
        """
        return GXLMSG()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def goto_point(cls, x, y, z, ipj):
        """
        Sends a move cursor message
        
        :param x:    X location
        :param y:    Y location
        :param z:    Z location
        :param ipj:  `GXIPJ <geosoft.gxapi.GXIPJ>` (if (`GXIPJ <geosoft.gxapi.GXIPJ>`)0, default coordinate system)
        :type  x:    float
        :type  y:    float
        :type  z:    float
        :type  ipj:  GXIPJ

        .. versionadded:: 5.0.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapLMSG._goto_point(GXContext._get_tls_geo(), x, y, z, ipj)
        



    @classmethod
    def view_area(cls, x0, y0, x1, y1, ipj):
        """
        Sends a view area message
        
        :param x0:   X0 location
        :param y0:   Y0 location
        :param x1:   X1 location
        :param y1:   Y1 location
        :param ipj:  `GXIPJ <geosoft.gxapi.GXIPJ>` (if (`GXIPJ <geosoft.gxapi.GXIPJ>`)0, default coordinate system)
        :type  x0:   float
        :type  y0:   float
        :type  x1:   float
        :type  y1:   float
        :type  ipj:  GXIPJ

        .. versionadded:: 5.0.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapLMSG._view_area(GXContext._get_tls_geo(), x0, y0, x1, y1, ipj)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer