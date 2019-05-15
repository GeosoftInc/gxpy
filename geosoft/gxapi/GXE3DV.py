### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXMVIEW import GXMVIEW


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXE3DV(gxapi_cy.WrapE3DV):
    """
    GXE3DV class.

    Methods to manipulate an active 3D View
    """

    def __init__(self, handle=0):
        super(GXE3DV, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXE3DV <geosoft.gxapi.GXE3DV>`
        
        :returns: A null `GXE3DV <geosoft.gxapi.GXE3DV>`
        :rtype:   GXE3DV
        """
        return GXE3DV()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def get_data_view(self):
        """
        Get the current data (3D) `GXMVIEW <geosoft.gxapi.GXMVIEW>`
        

        :returns:      `GXMVIEW <geosoft.gxapi.GXMVIEW>` object
        :rtype:        GXMVIEW

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_data_view()
        return GXMVIEW(ret_val)




    def get_base_view(self):
        """
        Get the current Base `GXMVIEW <geosoft.gxapi.GXMVIEW>` (used to draw 2D legends for groups)
        

        :returns:      `GXMVIEW <geosoft.gxapi.GXMVIEW>` object
        :rtype:        GXMVIEW

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_base_view()
        return GXMVIEW(ret_val)





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer