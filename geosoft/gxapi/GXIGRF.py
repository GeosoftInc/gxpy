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
    Methods to work with :class:`geosoft.gxapi.GXIGRF` objects. The :class:`geosoft.gxapi.GXIGRF` object
    contains data for the :class:`geosoft.gxapi.GXIGRF` model of the geomagnetic
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
        A null (undefined) instance of :class:`geosoft.gxapi.GXIGRF`
        
        :returns: A null :class:`geosoft.gxapi.GXIGRF`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXIGRF` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXIGRF`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def calc(self, p2, p3, p4, p5, p6, p7):
        """
        Calculate :class:`geosoft.gxapi.GXIGRF` data for a given :class:`geosoft.gxapi.GXIGRF` model.

        **Note:**

        Calculate :class:`geosoft.gxapi.GXIGRF` data (total field, inclination, and declination)
        for a given :class:`geosoft.gxapi.GXIGRF` model. The model used will be the same as that
        obtained with Create_IGRF.
        """
        p5.value, p6.value, p7.value = self._wrapper.calc(p2, p3, p4, p5.value, p6.value, p7.value)
        




    def calc_vv(self, p2, p3, p4, p5, p6, p7):
        """
        Calculate :class:`geosoft.gxapi.GXIGRF` data :class:`geosoft.gxapi.GXVV`'s for a given :class:`geosoft.gxapi.GXIGRF` model.

        **Note:**

        Calculate :class:`geosoft.gxapi.GXIGRF` data (total field, inclination, and declination)
        for a given :class:`geosoft.gxapi.GXIGRF` model. The model used will be the same as that
        obtained with Create_IGRF.
        All of the :class:`geosoft.gxapi.GXVV`'s should be the same length. The function
        will abort if they are not.
        
        No assumption is made on what data types are contained by
        any of the :class:`geosoft.gxapi.GXVV`'s. However, all total field, inclination, and
        declination values are internally calculated as real data.
        These values will be converted to the types contained in the
        output :class:`geosoft.gxapi.GXVV`'s.
        """
        self._wrapper.calc_vv(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper)
        



    @classmethod
    def create(cls, p1, p2, p3):
        """
        Create an :class:`geosoft.gxapi.GXIGRF`.

        **Note:**

        If the year of the :class:`geosoft.gxapi.GXIGRF` model is dummy, then
        the :class:`geosoft.gxapi.GXIGRF` year nearest to the line's date will
        be used. Otherwise, the specified year is used.
        """
        ret_val = gxapi_cy.WrapIGRF.create(GXContext._get_tls_geo(), p1, p2, p3.encode())
        return GXIGRF(ret_val)



    @classmethod
    def date_range(cls, p1, p2, p3):
        """
        Determine the range of years covered by an :class:`geosoft.gxapi.GXIGRF` or DGRF file

        **Note:**

        This is useful when using a DGRF file, because the system is set
        up only to calculate for years within the date range, and will
        return an error otherwise.
        """
        p2.value, p3.value = gxapi_cy.WrapIGRF.date_range(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value)
        







### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer