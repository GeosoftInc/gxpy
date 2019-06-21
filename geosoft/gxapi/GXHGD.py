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
class GXHGD(gxapi_cy.WrapHGD):
    """
    GXHGD class.

    High Performance Grid. Designed to place grid data
    on a DAP server. It produces a multi-resolution
    compressed object that supports multi-threading and
    allows for high-speed extraction of data at any
    resolution.
    """

    def __init__(self, handle=0):
        super(GXHGD, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXHGD <geosoft.gxapi.GXHGD>`
        
        :returns: A null `GXHGD <geosoft.gxapi.GXHGD>`
        :rtype:   GXHGD
        """
        return GXHGD()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, name):
        """
        Create a handle to an `GXHGD <geosoft.gxapi.GXHGD>` object
        
        :param name:  File Name
        :type  name:  str

        :returns:     `GXHGD <geosoft.gxapi.GXHGD>` handle, terminates if creation fails
        :rtype:       GXHGD

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapHGD._create(GXContext._get_tls_geo(), name.encode())
        return GXHGD(ret_val)






    def export_img(self, name):
        """
        Export all layers of this `GXHGD <geosoft.gxapi.GXHGD>` into grid files.
        
        :param name:  Name of grids (each layers adds _Number to the name)
        :type  name:  str

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._export_img(name.encode())
        




    def get_meta(self, meta):
        """
        Get the metadata of a grid.
        
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` object to save `GXHGD <geosoft.gxapi.GXHGD>`'s meta to
        :type  meta:  GXMETA

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_meta(meta)
        



    @classmethod
    def h_create_img(cls, img, name):
        """
        Make an `GXHGD <geosoft.gxapi.GXHGD>` from an `GXIMG <geosoft.gxapi.GXIMG>`
        
        :param img:   Image Handle
        :param name:  Name of `GXHGD <geosoft.gxapi.GXHGD>` object
        :type  img:   GXIMG
        :type  name:  str

        :returns:     `GXHGD <geosoft.gxapi.GXHGD>` Object
        :rtype:       GXHGD

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapHGD._h_create_img(GXContext._get_tls_geo(), img, name.encode())
        return GXHGD(ret_val)




    def set_meta(self, meta):
        """
        Set the metadata of a grid.
        
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` object to add to `GXHGD <geosoft.gxapi.GXHGD>`'s meta
        :type  meta:  GXMETA

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_meta(meta)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer