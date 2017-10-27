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
    ll2 methods are used to create `GXLL2 <geosoft.gxapi.GXLL2>` objects.  `GXLL2 <geosoft.gxapi.GXLL2>` objects contain
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
        A null (undefined) instance of `GXLL2`
        
        :returns: A null `GXLL2`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXLL2` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXLL2`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, lon0, lat0, lon, lat, nlon, nlat, in_ipj, out_ipj):
        """
        Create an empty `GXLL2 <geosoft.gxapi.GXLL2>` table to be filled

        .. seealso::

            `destroy <geosoft.gxapi.GXLL2.destroy>`, `set_row <geosoft.gxapi.GXLL2.set_row>`, `save <geosoft.gxapi.GXLL2.save>`
        """
        ret_val = gxapi_cy.WrapLL2.create(GXContext._get_tls_geo(), lon0, lat0, lon, lat, nlon, nlat, in_ipj._wrapper, out_ipj._wrapper)
        return GXLL2(ret_val)






    def save(self, name):
        """
        Save an `GXLL2 <geosoft.gxapi.GXLL2>` to a named resource

        **Note:**

        The named resource is the name of the datum transform define
        inside square brackets in the datum transform name in the
        datumtrf table.
        """
        self._wrapper.save(name.encode())
        




    def set_row(self, row, lon_vv, lat_vv):
        """
        Define a row of the `GXLL2 <geosoft.gxapi.GXLL2>`

        **Note:**

        The correction data is in degrees, added to the input
        datum to product output datum results.
        
        The `GXVV <geosoft.gxapi.GXVV>` lengths must be equal to #longitudes defined
        by `create <geosoft.gxapi.GXLL2.create>`.
        """
        self._wrapper.set_row(row, lon_vv._wrapper, lat_vv._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer