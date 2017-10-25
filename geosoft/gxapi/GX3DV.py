### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXMVIEW import GXMVIEW


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GX3DV:
    """
    GX3DV class.

    TODO...
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.Wrap3DV(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GX3DV`
        
        :returns: A null `GX3DV`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GX3DV` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GX3DV`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def open_mview(self, p2):
        """
        Open `GX3DV`'s 3D `GXMVIEW`
        """
        ret_val = self._wrapper.open_mview(p2)
        return GXMVIEW(ret_val)




    def copy_to_map(self, p2, p3, p4, p5, p6, p7, p8, p9, p11):
        """
        Copy the `GX3DV`'s 3D `GXMVIEW` into a map.

        **Note:**

        A `GX3DV` packs all source files. This functions creates an unpacked map and
        unpacks the packed files in the same way that UnPackFilesEx in the `GXMAP` class does.
        """
        p9.value, p11.value = self._wrapper.copy_to_map(p2._wrapper, p3.encode(), p4, p5, p6, p7, p8, p9.value.encode(), p11.value.encode())
        



    @classmethod
    def create_new(cls, p1, p2):
        """
        Create a new `GX3DV`.
        """
        ret_val = gxapi_cy.Wrap3DV.create_new(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        return GX3DV(ret_val)



    @classmethod
    def open(cls, p1):
        """
        Open an existing `GX3DV`.
        """
        ret_val = gxapi_cy.Wrap3DV.open(GXContext._get_tls_geo(), p1.encode())
        return GX3DV(ret_val)



    @classmethod
    def from_map(cls, p1):
        """
        Get an `GX3DV` from `GXMAP` handle (e.g. from `GXEMAP.lock` on open geosoft_3dv document in project)
        """
        ret_val = gxapi_cy.Wrap3DV.from_map(GXContext._get_tls_geo(), p1._wrapper)
        return GX3DV(ret_val)




    def crc_3dv(self, p2, p3):
        """
        Generate an XML CRC of a `GX3DV`
        """
        p2.value = self._wrapper.crc_3dv(p2.value, p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer