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
class GXGD(gxapi_cy.WrapGD):
    """
    GXGD class.

    This class provides access to Geosoft grid files using an old interface.
    Only the `GXDU.sample_gd <geosoft.gxapi.GXDU.sample_gd>` function uses this class.  Use the `GXIMG <geosoft.gxapi.GXIMG>` class
    instead.
    """

    def __init__(self, handle=0):
        super(GXGD, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXGD <geosoft.gxapi.GXGD>`
        
        :returns: A null `GXGD <geosoft.gxapi.GXGD>`
        :rtype:   GXGD
        """
        return GXGD()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, name, type):
        """
        This method creates a `GXGD <geosoft.gxapi.GXGD>` object.
        
        :param name:  Name of the Grid File
        :param type:  :ref:`GD_STATUS`
        :type  name:  str
        :type  type:  int

        :returns:     Handle to the `GXGD <geosoft.gxapi.GXGD>` object
        :rtype:       GXGD

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapGD._create(GXContext._get_tls_geo(), name.encode(), type)
        return GXGD(ret_val)







### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer