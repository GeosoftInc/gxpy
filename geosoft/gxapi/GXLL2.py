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
class GXLL2:
    """
    GXLL2 class.

    local datum lookup creator
    ll2 methods are used to create :class:`geosoft.gxapi.GXLL2` objects.  :class:`geosoft.gxapi.GXLL2` objects contain
    latitude, longitude correction lookup tables to convert between datums.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapLL2(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXLL2`
        
        :returns: A null :class:`geosoft.gxapi.GXLL2`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXLL2` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXLL2`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Create an empty :class:`geosoft.gxapi.GXLL2` table to be filled
        """
        ret_val = gxapi_cy.WrapLL2.create(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6, p7._wrapper, p8._wrapper)
        return GXLL2(ret_val)






    def save(self, p2):
        """
        Save an :class:`geosoft.gxapi.GXLL2` to a named resource

        **Note:**

        The named resource is the name of the datum transform define
        inside square brackets in the datum transform name in the
        datumtrf table.
        """
        self._wrapper.save(p2.encode())
        




    def set_row(self, p2, p3, p4):
        """
        Define a row of the :class:`geosoft.gxapi.GXLL2`

        **Note:**

        The correction data is in degrees, added to the input
        datum to product output datum results.
        
        The :class:`geosoft.gxapi.GXVV` lengths must be equal to #longitudes defined
        by Create_LL2.
        """
        self._wrapper.set_row(p2, p3._wrapper, p4._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer