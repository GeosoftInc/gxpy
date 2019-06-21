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
class GXIGRF(gxapi_cy.WrapIGRF):
    """
    GXIGRF class.

    International Geomagnetic Reference Field
    Methods to work with `GXIGRF <geosoft.gxapi.GXIGRF>` objects. The `GXIGRF <geosoft.gxapi.GXIGRF>` object
    contains data for the `GXIGRF <geosoft.gxapi.GXIGRF>` model of the geomagnetic
    reference field.
    """

    def __init__(self, handle=0):
        super(GXIGRF, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXIGRF <geosoft.gxapi.GXIGRF>`
        
        :returns: A null `GXIGRF <geosoft.gxapi.GXIGRF>`
        :rtype:   GXIGRF
        """
        return GXIGRF()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def calc(self, el, lon, lat, str_val, inc, dec):
        """
        Calculate `GXIGRF <geosoft.gxapi.GXIGRF>` data for a given `GXIGRF <geosoft.gxapi.GXIGRF>` model.
        
        :param el:       Elevation (metres)
        :param lon:      Longitude (-180 to 180)
        :param lat:      Latitude  (-90 to 90) Returns
        :param str_val:  Field strength
        :param inc:      Field inclination
        :param dec:      Field declination
        :type  el:       float
        :type  lon:      float
        :type  lat:      float
        :type  str_val:  float_ref
        :type  inc:      float_ref
        :type  dec:      float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Calculate `GXIGRF <geosoft.gxapi.GXIGRF>` data (total field, inclination, and declination)
        for a given `GXIGRF <geosoft.gxapi.GXIGRF>` model. The model used will be the same as that
        obtained with `create <geosoft.gxapi.GXIGRF.create>`.
        """
        str_val.value, inc.value, dec.value = self._calc(el, lon, lat, str_val.value, inc.value, dec.value)
        




    def calc_vv(self, gv_vel, gv_vlon, gv_vlat, gv_vfs, gv_vinc, gv_vdec):
        """
        Calculate `GXIGRF <geosoft.gxapi.GXIGRF>` data `GXVV <geosoft.gxapi.GXVV>`'s for a given `GXIGRF <geosoft.gxapi.GXIGRF>` model.
        
        :param gv_vel:   Input elevation data (metres)
        :param gv_vlon:  Input longitude data (-180 to 180)
        :param gv_vlat:  Input latitude data  (-90 to 90)
        :param gv_vfs:   Output total field
        :param gv_vinc:  Output inclination
        :param gv_vdec:  Output declination
        :type  gv_vel:   GXVV
        :type  gv_vlon:  GXVV
        :type  gv_vlat:  GXVV
        :type  gv_vfs:   GXVV
        :type  gv_vinc:  GXVV
        :type  gv_vdec:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Calculate `GXIGRF <geosoft.gxapi.GXIGRF>` data (total field, inclination, and declination)
        for a given `GXIGRF <geosoft.gxapi.GXIGRF>` model. The model used will be the same as that
        obtained with `create <geosoft.gxapi.GXIGRF.create>`.
        All of the `GXVV <geosoft.gxapi.GXVV>`'s should be the same length. The function
        will abort if they are not.

        No assumption is made on what data types are contained by
        any of the `GXVV <geosoft.gxapi.GXVV>`'s. However, all total field, inclination, and
        declination values are internally calculated as real data.
        These values will be converted to the types contained in the
        output `GXVV <geosoft.gxapi.GXVV>`'s.
        """
        self._calc_vv(gv_vel, gv_vlon, gv_vlat, gv_vfs, gv_vinc, gv_vdec)
        



    @classmethod
    def create(cls, date, year, filename):
        """
        Create an `GXIGRF <geosoft.gxapi.GXIGRF>`.
        
        :param date:      Date required
        :param year:      Year of the `GXIGRF <geosoft.gxapi.GXIGRF>` model to use
        :param filename:  Name of the `GXIGRF <geosoft.gxapi.GXIGRF>` reference data file
        :type  date:      float
        :type  year:      int
        :type  filename:  str

        :returns:         `GXIGRF <geosoft.gxapi.GXIGRF>` Object
        :rtype:           GXIGRF

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If the year of the `GXIGRF <geosoft.gxapi.GXIGRF>` model is dummy, then
        the `GXIGRF <geosoft.gxapi.GXIGRF>` year nearest to the line's date will
        be used. Otherwise, the specified year is used.
        """
        ret_val = gxapi_cy.WrapIGRF._create(GXContext._get_tls_geo(), date, year, filename.encode())
        return GXIGRF(ret_val)



    @classmethod
    def date_range(cls, file_name, min, max):
        """
        Determine the range of years covered by an `GXIGRF <geosoft.gxapi.GXIGRF>` or DGRF file
        
        :param file_name:  Model data file name
        :param min:        Minimum year  (`rMAX <geosoft.gxapi.rMAX>` if none found)
        :param max:        Maximum year  (`rMIN <geosoft.gxapi.rMIN>` if none found)
        :type  file_name:  str
        :type  min:        float_ref
        :type  max:        float_ref

        .. versionadded:: 6.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This is useful when using a DGRF file, because the system is set
        up only to calculate for years within the date range, and will
        return an error otherwise.
        """
        min.value, max.value = gxapi_cy.WrapIGRF._date_range(GXContext._get_tls_geo(), file_name.encode(), min.value, max.value)
        







### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer