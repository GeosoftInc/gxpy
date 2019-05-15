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
class GXVECTOR3D(gxapi_cy.WrapVECTOR3D):
    """
    GXVECTOR3D class.

    `GXVECTOR3D <geosoft.gxapi.GXVECTOR3D>` Display object.
    """

    def __init__(self, handle=0):
        super(GXVECTOR3D, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVECTOR3D <geosoft.gxapi.GXVECTOR3D>`
        
        :returns: A null `GXVECTOR3D <geosoft.gxapi.GXVECTOR3D>`
        :rtype:   GXVECTOR3D
        """
        return GXVECTOR3D()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous





    def get_itr(self, itr):
        """
        Get the `GXITR <geosoft.gxapi.GXITR>` of the `GXVECTOR3D <geosoft.gxapi.GXVECTOR3D>`
        
        :param itr:        `GXITR <geosoft.gxapi.GXITR>` object
        :type  itr:        GXITR

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_itr(itr)
        




    def set_itr(self, itr):
        """
        Set the `GXITR <geosoft.gxapi.GXITR>` of the `GXVECTOR3D <geosoft.gxapi.GXVECTOR3D>`
        
        :param itr:        `GXITR <geosoft.gxapi.GXITR>` object
        :type  itr:        GXITR

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_itr(itr)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer