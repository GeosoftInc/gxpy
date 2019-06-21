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
class GXMXD(gxapi_cy.WrapMXD):
    """
    GXMXD class.

    A `GXMXD <geosoft.gxapi.GXMXD>` wraps and provides manipulation and usage for
    the content of an ArcGIS `GXMXD <geosoft.gxapi.GXMXD>` file.
    """

    def __init__(self, handle=0):
        super(GXMXD, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXMXD <geosoft.gxapi.GXMXD>`
        
        :returns: A null `GXMXD <geosoft.gxapi.GXMXD>`
        :rtype:   GXMXD
        """
        return GXMXD()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create_metadata(cls, mxd):
        """
        Create metadata for this brand new `GXMXD <geosoft.gxapi.GXMXD>` (we are the creator)
        
        :param mxd:  `GXMXD <geosoft.gxapi.GXMXD>` file name
        :type  mxd:  str

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapMXD._create_metadata(GXContext._get_tls_geo(), mxd.encode())
        



    @classmethod
    def convert_to_map(cls, mxd, map):
        """
        Create Geosoft map from ArcGIS `GXMXD <geosoft.gxapi.GXMXD>`
        
        :param mxd:  ArcGIS `GXMXD <geosoft.gxapi.GXMXD>` file name
        :param map:  Geosoft map file name
        :type  mxd:  str
        :type  map:  str

        .. versionadded:: 9.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapMXD._convert_to_map(GXContext._get_tls_geo(), mxd.encode(), map.encode())
        



    @classmethod
    def sync(cls, mxd):
        """
        Syncronize any Metadata for this `GXMXD <geosoft.gxapi.GXMXD>`
        
        :param mxd:  `GXMXD <geosoft.gxapi.GXMXD>` file name
        :type  mxd:  str

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapMXD._sync(GXContext._get_tls_geo(), mxd.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer