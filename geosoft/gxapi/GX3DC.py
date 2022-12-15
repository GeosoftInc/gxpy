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
class GX3DC(gxapi_cy.Wrap3DC):
    """
    GX3DC class.

    This is a 3D container class which facilitates rendering a 3D viewport
    to controls. To be used in tandem with the Geosoft.View3D.View class
    present in geoengine.3dv.csharp. Creation of the 3D container is
    facilitated through Create_3DC, and disposal through the instance
    method Destroy_3DC.
    """

    def __init__(self, handle=0):
        super(GX3DC, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GX3DC <geosoft.gxapi.GX3DC>`
        
        :returns: A null `GX3DC <geosoft.gxapi.GX3DC>`
        :rtype:   GX3DC
        """
        return GX3DC()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, handle):
        """
        Create a 3D view container which can be used to instantiate a full 3D View.
        
        :param handle:  Window handle for the OpenGL context.
        :type  handle:  int

        :returns:       `GX3DC <geosoft.gxapi.GX3DC>` object
        :rtype:         GX3DC

        .. versionadded:: 2022.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            DestroyInternal_3DC
        """
        ret_val = gxapi_cy.Wrap3DC._create(GXContext._get_tls_geo(), handle)
        return GX3DC(ret_val)




    def get_geo_view(self):
        """
        Retrieves the GeoView associated with the 3D container.
        
        :rtype:       Type.INT64_T

        .. versionadded:: 2022.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_geo_view()
        return ret_val




    def destroy_internal(self):
        """
        Destroys a 3D container object and cleans up any unmanaged resources.
        

        .. versionadded:: 2022.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._destroy_internal()
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer