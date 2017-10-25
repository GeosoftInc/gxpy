### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXMVIEW import GXMVIEW
### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXE3DV:
    """
    GXE3DV class.

    Methods to manipulate an active 3D View
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapE3DV(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXE3DV':
        """
        A null (undefined) instance of :class:`GXE3DV`
        
        :returns: A null :class:`GXE3DV`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXE3DV` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXE3DV`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def get_data_view(self) -> 'GXMVIEW':
        ret_val = self._wrapper.get_data_view()
        return GXMVIEW(ret_val)




    def get_base_view(self) -> 'GXMVIEW':
        ret_val = self._wrapper.get_base_view()
        return GXMVIEW(ret_val)





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer