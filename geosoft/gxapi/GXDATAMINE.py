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
class GXDATAMINE(gxapi_cy.WrapDATAMINE):
    """
    GXDATAMINE class.

    `GXDATAMINE <geosoft.gxapi.GXDATAMINE>` functions provide an interface to Datamine Software Limited files.
    See also `GXGIS <geosoft.gxapi.GXGIS>` for various other Datamine-specific functions.

    **Note:**

    None.
    """

    def __init__(self, handle=0):
        super(GXDATAMINE, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDATAMINE <geosoft.gxapi.GXDATAMINE>`
        
        :returns: A null `GXDATAMINE <geosoft.gxapi.GXDATAMINE>`
        :rtype:   GXDATAMINE
        """
        return GXDATAMINE()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create_voxel(cls, file, field, ipj, meta, voxel):
        """
        Create a Geosoft Voxel file from a Datamine block model file.
        
        :param file:   Datamine file name
        :param field:  Field to use for data
        :param ipj:    Projection to set
        :param meta:   `GXMETA <geosoft.gxapi.GXMETA>` to set
        :param voxel:  Output voxel file name
        :type  file:   str
        :type  field:  str
        :type  ipj:    GXIPJ
        :type  meta:   GXMETA
        :type  voxel:  str

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Create a Geosoft Voxel file from a Datamine block model file.
        """
        gxapi_cy.WrapDATAMINE._create_voxel(GXContext._get_tls_geo(), file.encode(), field.encode(), ipj, meta, voxel.encode())
        



    @classmethod
    def numeric_field_lst(cls, file, lst):
        """
        Return a `GXLST <geosoft.gxapi.GXLST>` containing the non-standard numeric fields in a Datamine file.
        
        :param file:  Datamine file name
        :param lst:   `GXLST <geosoft.gxapi.GXLST>` to populate
        :type  file:  str
        :type  lst:   GXLST

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** At this time, only `GIS_DMTYPE_BLOCKMODEL <geosoft.gxapi.GIS_DMTYPE_BLOCKMODEL>` files are supported.
        The field names go in the name part, and field indices (1 to N)
        in the value part.
        """
        gxapi_cy.WrapDATAMINE._numeric_field_lst(GXContext._get_tls_geo(), file.encode(), lst)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer