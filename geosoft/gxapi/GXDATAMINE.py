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

    :class:`geosoft.gxapi.GXDATAMINE` functions provide an interface to Datamine Software Limited files.
    See also :class:`geosoft.gxapi.GXGIS` for various other Datamine-specific functions.

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
        A null (undefined) instance of :class:`geosoft.gxapi.GXDATAMINE`
        
        :returns: A null :class:`geosoft.gxapi.GXDATAMINE`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXDATAMINE` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXDATAMINE`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create_voxel(cls, p1, p2, p3, p4, p5):
        """
        Create a Geosoft Voxel file from a Datamine block model file.

        **Note:**

        Create a Geosoft Voxel file from a Datamine block model file.
        """
        gxapi_cy.WrapDATAMINE.create_voxel(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper, p4._wrapper, p5.encode())
        



    @classmethod
    def numeric_field_lst(cls, p1, p2):
        """
        Return a :class:`geosoft.gxapi.GXLST` containing the non-standard numeric fields in a Datamine file.

        **Note:**

        At this time, only :attr:`geosoft.gxapi.GIS_DMTYPE_BLOCKMODEL` files are supported.
        The field names go in the name part, and field indices (1 to N)
        in the value part.
        """
        gxapi_cy.WrapDATAMINE.numeric_field_lst(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer