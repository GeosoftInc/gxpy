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
class GXGMSYS(gxapi_cy.WrapGMSYS):
    """
    GXGMSYS class.

    The `GXGMSYS <geosoft.gxapi.GXGMSYS>` Methods
    """

    def __init__(self, handle=0):
        super(GXGMSYS, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXGMSYS <geosoft.gxapi.GXGMSYS>`
        
        :returns: A null `GXGMSYS <geosoft.gxapi.GXGMSYS>`
        :rtype:   GXGMSYS
        """
        return GXGMSYS()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def launch(cls, model):
        """
        Launch `GXGMSYS <geosoft.gxapi.GXGMSYS>` with extension
        
        :param model:  Model name
        :type  model:  str

        .. versionadded:: 5.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapGMSYS._launch(GXContext._get_tls_geo(), model.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer