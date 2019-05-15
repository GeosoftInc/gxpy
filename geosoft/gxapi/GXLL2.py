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
class GXLL2(gxapi_cy.WrapLL2):
    """
    GXLL2 class.

    local datum lookup creator
    ll2 methods are used to create `GXLL2 <geosoft.gxapi.GXLL2>` objects.  `GXLL2 <geosoft.gxapi.GXLL2>` objects contain
    latitude, longitude correction lookup tables to convert between datums.
    """

    def __init__(self, handle=0):
        super(GXLL2, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXLL2 <geosoft.gxapi.GXLL2>`
        
        :returns: A null `GXLL2 <geosoft.gxapi.GXLL2>`
        :rtype:   GXLL2
        """
        return GXLL2()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls, lon0, lat0, lon, lat, nlon, nlat, in_ipj, out_ipj):
        """
        Create an empty `GXLL2 <geosoft.gxapi.GXLL2>` table to be filled
        
        :param lon0:     Longitude origin
        :param lat0:     Latitude origin
        :param lon:      Longitude increment
        :param lat:      Latitude increment
        :param nlon:     # longitudes
        :param nlat:     # latitudes
        :param in_ipj:   Input projection
        :param out_ipj:  Output projection
        :type  lon0:     float
        :type  lat0:     float
        :type  lon:      float
        :type  lat:      float
        :type  nlon:     int
        :type  nlat:     int
        :type  in_ipj:   GXIPJ
        :type  out_ipj:  GXIPJ

        :returns:        `GXLL2 <geosoft.gxapi.GXLL2>` Object
        :rtype:          GXLL2

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        .. seealso::

            `destroy <geosoft.gxapi.GXLL2.destroy>`, `set_row <geosoft.gxapi.GXLL2.set_row>`, `save <geosoft.gxapi.GXLL2.save>`
        """
        ret_val = gxapi_cy.WrapLL2._create(GXContext._get_tls_geo(), lon0, lat0, lon, lat, nlon, nlat, in_ipj, out_ipj)
        return GXLL2(ret_val)






    def save(self, name):
        """
        Save an `GXLL2 <geosoft.gxapi.GXLL2>` to a named resource
        
        :param name:    Named resource
        :type  name:    str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The named resource is the name of the datum transform define
        inside square brackets in the datum transform name in the
        datumtrf table.
        """
        self._save(name.encode())
        




    def set_row(self, row, lon_vv, lat_vv):
        """
        Define a row of the `GXLL2 <geosoft.gxapi.GXLL2>`
        
        :param row:     The row to set
        :param lon_vv:  Longitude corrections
        :param lat_vv:  Latitude corrections
        :type  row:     int
        :type  lon_vv:  GXVV
        :type  lat_vv:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The correction data is in degrees, added to the input
        datum to product output datum results.

        The `GXVV <geosoft.gxapi.GXVV>` lengths must be equal to #longitudes defined
        by `create <geosoft.gxapi.GXLL2.create>`.
        """
        self._set_row(row, lon_vv, lat_vv)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer