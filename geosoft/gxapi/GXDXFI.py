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
class GXDXFI:
    """
    GXDXFI class.

    The `GXDXFI` class is used for importing AutoCAD® dxf files into Geosoft maps.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDXFI(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDXFI`
        
        :returns: A null `GXDXFI`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXDXFI` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXDXFI`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, name):
        """
        Create `GXDXFI`.
        """
        ret_val = gxapi_cy.WrapDXFI.create(GXContext._get_tls_geo(), name.encode())
        return GXDXFI(ret_val)





    @classmethod
    def dxf2_ply(cls, ply, dxfi):
        """
        Convert a DXF file to a `GXPLY` object
        """
        gxapi_cy.WrapDXFI.dxf2_ply(GXContext._get_tls_geo(), ply._wrapper, dxfi._wrapper)
        




    def dxf2_view_ex(self, view, max_pen, pb_group, group, pb_one_color, color):
        """
        Draw entities in a DXF file to a view in a map
        """
        self._wrapper.dxf2_view_ex(view._wrapper, max_pen, pb_group, group.encode(), pb_one_color, color)
        




    def get_range(self, min_x, max_x, min_y, max_y, min_z, max_z):
        """
        Get DXF data range
        """
        min_x.value, max_x.value, min_y.value, max_y.value, min_z.value, max_z.value = self._wrapper.get_range(min_x.value, max_x.value, min_y.value, max_y.value, min_z.value, max_z.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer