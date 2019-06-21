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
class GXDATALINKD(gxapi_cy.WrapDATALINKD):
    """
    GXDATALINKD class.

    DATALINK Display object.
    """

    def __init__(self, handle=0):
        super(GXDATALINKD, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDATALINKD <geosoft.gxapi.GXDATALINKD>`
        
        :returns: A null `GXDATALINKD <geosoft.gxapi.GXDATALINKD>`
        :rtype:   GXDATALINKD
        """
        return GXDATALINKD()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create_arc_lyr(cls, arc_lyr_file):
        """
        Create an `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` object from a ArcGIS LYR file
        
        :param arc_lyr_file:  Arc LYR file name
        :type  arc_lyr_file:  str

        :returns:             `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` handle, terminates if creation fails
        :rtype:               GXDATALINKD

        .. versionadded:: 6.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Needs ArcEngine licence.
        """
        ret_val = gxapi_cy.WrapDATALINKD._create_arc_lyr(GXContext._get_tls_geo(), arc_lyr_file.encode())
        return GXDATALINKD(ret_val)



    @classmethod
    def create_arc_lyr_ex(cls, arc_lyr_file, o3d_group):
        """
        Create an `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` object from a ArcGIS LYR file
        
        :param arc_lyr_file:  Arc LYR file name
        :param o3d_group:     Display as 3D Group? (as opposed to bitmap on plane)
        :type  arc_lyr_file:  str
        :type  o3d_group:     int

        :returns:             `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` handle, terminates if creation fails
        :rtype:               GXDATALINKD

        .. versionadded:: 9.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Needs ArcEngine licence.
        """
        ret_val = gxapi_cy.WrapDATALINKD._create_arc_lyr_ex(GXContext._get_tls_geo(), arc_lyr_file.encode(), o3d_group)
        return GXDATALINKD(ret_val)



    @classmethod
    def create_arc_lyr_from_tmp(cls, arc_lyr_file):
        """
        Create an `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` object from a temporary ArcGIS LYR file
        
        :param arc_lyr_file:  Arc LYR file name
        :type  arc_lyr_file:  str

        :returns:             `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` handle, terminates if creation fails
        :rtype:               GXDATALINKD

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Needs ArcEngine licence.
        """
        ret_val = gxapi_cy.WrapDATALINKD._create_arc_lyr_from_tmp(GXContext._get_tls_geo(), arc_lyr_file.encode())
        return GXDATALINKD(ret_val)



    @classmethod
    def create_arc_lyr_from_tmp_ex(cls, arc_lyr_file, o3d_group):
        """
        Create an `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` object from a temporary ArcGIS LYR file
        
        :param arc_lyr_file:  Arc LYR file name
        :param o3d_group:     Display as 3D Group? (as opposed to bitmap on plane)
        :type  arc_lyr_file:  str
        :type  o3d_group:     int

        :returns:             `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` handle, terminates if creation fails
        :rtype:               GXDATALINKD

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Needs ArcEngine licence.
        """
        ret_val = gxapi_cy.WrapDATALINKD._create_arc_lyr_from_tmp_ex(GXContext._get_tls_geo(), arc_lyr_file.encode(), o3d_group)
        return GXDATALINKD(ret_val)



    @classmethod
    def create_bing(cls, layer):
        """
        Create an `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` object for a BING dataset
        
        :param layer:  0 = Aerial, 1 = Road
        :type  layer:  int

        :returns:      `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` handle, terminates if creation fails
        :rtype:        GXDATALINKD

        .. versionadded:: 8.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val = gxapi_cy.WrapDATALINKD._create_bing(GXContext._get_tls_geo(), layer)
        return GXDATALINKD(ret_val)






    def get_extents(self, min_x, max_x, min_y, max_y):
        """
        Get the data extents of the DATALINK Display object.
        
        :param min_x:      Min X
        :param max_x:      Max X
        :param min_y:      Min Y
        :param max_y:      Max Y
        :type  min_x:      float_ref
        :type  max_x:      float_ref
        :type  min_y:      float_ref
        :type  max_y:      float_ref

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        min_x.value, max_x.value, min_y.value, max_y.value = self._get_extents(min_x.value, max_x.value, min_y.value, max_y.value)
        




    def get_ipj(self, ipj):
        """
        Get the projection of the DATALINK Display object.
        
        :param ipj:        `GXIPJ <geosoft.gxapi.GXIPJ>` object to set the projection to
        :type  ipj:        GXIPJ

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_ipj(ipj)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer