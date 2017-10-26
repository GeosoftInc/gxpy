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
class GXDATAMINE:
    """
    GXDATAMINE class.

    `GXDATAMINE` functions provide an interface to Datamine Software Limited files.
    See also `GXGIS` for various other Datamine-specific functions.

    **Note:**

    None.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDATAMINE(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDATAMINE`
        
        :returns: A null `GXDATAMINE`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXDATAMINE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXDATAMINE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create_voxel(cls, file, field, ipj, meta, voxel):
        """
        Create a Geosoft Voxel file from a Datamine block model file.

        **Note:**

        Create a Geosoft Voxel file from a Datamine block model file.
        """
        gxapi_cy.WrapDATAMINE.create_voxel(GXContext._get_tls_geo(), file.encode(), field.encode(), ipj._wrapper, meta._wrapper, voxel.encode())
        



    @classmethod
    def numeric_field_lst(cls, file, lst):
        """
        Return a `GXLST` containing the non-standard numeric fields in a Datamine file.

        **Note:**

        At this time, only `GIS_DMTYPE_BLOCKMODEL` files are supported.
        The field names go in the name part, and field indices (1 to N)
        in the value part.
        """
        gxapi_cy.WrapDATAMINE.numeric_field_lst(GXContext._get_tls_geo(), file.encode(), lst._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer