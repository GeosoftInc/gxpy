### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXIGRF:
    """
    GXIGRF class.

    International Geomagnetic Reference Field
    Methods to work with `GXIGRF <geosoft.gxapi.GXIGRF>` objects. The `GXIGRF <geosoft.gxapi.GXIGRF>` object
    contains data for the `GXIGRF <geosoft.gxapi.GXIGRF>` model of the geomagnetic
    reference field.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapIGRF(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXIGRF`
        
        :returns: A null `GXIGRF`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXIGRF` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXIGRF`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def calc(self, el, lon, lat, str_val, inc, dec):
        """
        Calculate `GXIGRF <geosoft.gxapi.GXIGRF>` data for a given `GXIGRF <geosoft.gxapi.GXIGRF>` model.

        **Note:**

        Calculate `GXIGRF <geosoft.gxapi.GXIGRF>` data (total field, inclination, and declination)
        for a given `GXIGRF <geosoft.gxapi.GXIGRF>` model. The model used will be the same as that
        obtained with `create <geosoft.gxapi.GXIGRF.create>`.
        """
        str_val.value, inc.value, dec.value = self._wrapper.calc(el, lon, lat, str_val.value, inc.value, dec.value)
        




    def calc_vv(self, gv_vel, gv_vlon, gv_vlat, gv_vfs, gv_vinc, gv_vdec):
        """
        Calculate `GXIGRF <geosoft.gxapi.GXIGRF>` data `GXVV <geosoft.gxapi.GXVV>`'s for a given `GXIGRF <geosoft.gxapi.GXIGRF>` model.

        **Note:**

        Calculate `GXIGRF <geosoft.gxapi.GXIGRF>` data (total field, inclination, and declination)
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
        self._wrapper.calc_vv(gv_vel._wrapper, gv_vlon._wrapper, gv_vlat._wrapper, gv_vfs._wrapper, gv_vinc._wrapper, gv_vdec._wrapper)
        



    @classmethod
    def create(cls, date, year, filename):
        """
        Create an `GXIGRF <geosoft.gxapi.GXIGRF>`.

        **Note:**

        If the year of the `GXIGRF <geosoft.gxapi.GXIGRF>` model is dummy, then
        the `GXIGRF <geosoft.gxapi.GXIGRF>` year nearest to the line's date will
        be used. Otherwise, the specified year is used.
        """
        ret_val = gxapi_cy.WrapIGRF.create(GXContext._get_tls_geo(), date, year, filename.encode())
        return GXIGRF(ret_val)



    @classmethod
    def date_range(cls, file_name, min, max):
        """
        Determine the range of years covered by an `GXIGRF <geosoft.gxapi.GXIGRF>` or DGRF file

        **Note:**

        This is useful when using a DGRF file, because the system is set
        up only to calculate for years within the date range, and will
        return an error otherwise.
        """
        min.value, max.value = gxapi_cy.WrapIGRF.date_range(GXContext._get_tls_geo(), file_name.encode(), min.value, max.value)
        







### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer