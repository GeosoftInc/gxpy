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



    def open_mview(self, mode):
        """
        Open `GX3DV`'s 3D `GXMVIEW`
        """
        ret_val = self._wrapper.open_mview(mode)
        return GXMVIEW(ret_val)




    def copy_to_map(self, map, mview, min_x, min_y, max_x, max_y, force_overwrite, new_view, problem_files):
        """
        Copy the `GX3DV`'s 3D `GXMVIEW` into a map.

        **Note:**

        A `GX3DV` packs all source files. This functions creates an unpacked map and
        unpacks the packed files in the same way that UnPackFilesEx in the `GXMAP` class does.
        """
        new_view.value, problem_files.value = self._wrapper.copy_to_map(map._wrapper, mview.encode(), min_x, min_y, max_x, max_y, force_overwrite, new_view.value.encode(), problem_files.value.encode())
        



    @classmethod
    def create_new(cls, file_name, mview):
        """
        Create a new `GX3DV`.
        """
        ret_val = gxapi_cy.Wrap3DV.create_new(GXContext._get_tls_geo(), file_name.encode(), mview._wrapper)
        return GX3DV(ret_val)



    @classmethod
    def open(cls, file_name):
        """
        Open an existing `GX3DV`.
        """
        ret_val = gxapi_cy.Wrap3DV.open(GXContext._get_tls_geo(), file_name.encode())
        return GX3DV(ret_val)



    @classmethod
    def from_map(cls, map):
        """
        Get an `GX3DV` from `GXMAP` handle (e.g. from `GXEMAP.lock` on open geosoft_3dv document in project)
        """
        ret_val = gxapi_cy.Wrap3DV.from_map(GXContext._get_tls_geo(), map._wrapper)
        return GX3DV(ret_val)




    def crc_3dv(self, crc, file):
        """
        Generate an XML CRC of a `GX3DV`
        """
        crc.value = self._wrapper.crc_3dv(crc.value, file.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer