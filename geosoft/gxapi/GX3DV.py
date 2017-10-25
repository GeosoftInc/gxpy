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
    def null(cls) -> 'GX3DV':
        """
        A null (undefined) instance of :class:`GX3DV`
        
        :returns: A null :class:`GX3DV`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GX3DV` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GX3DV`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def open_mview(self, p2: int) -> 'GXMVIEW':
        ret_val = self._wrapper.open_mview(p2)
        return GXMVIEW(ret_val)




    def copy_to_map(self, p2: 'GXMAP', p3: str, p4: float, p5: float, p6: float, p7: float, p8: int, p9: str_ref, p11: str_ref) -> None:
        p9.value, p11.value = self._wrapper.copy_to_map(p2._wrapper, p3.encode(), p4, p5, p6, p7, p8, p9.value.encode(), p11.value.encode())
        



    @classmethod
    def create_new(cls, p1: str, p2: 'GXMVIEW') -> 'GX3DV':
        ret_val = gxapi_cy.Wrap3DV.create_new(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        return GX3DV(ret_val)



    @classmethod
    def open(cls, p1: str) -> 'GX3DV':
        ret_val = gxapi_cy.Wrap3DV.open(GXContext._get_tls_geo(), p1.encode())
        return GX3DV(ret_val)



    @classmethod
    def from_map(cls, p1: 'GXMAP') -> 'GX3DV':
        ret_val = gxapi_cy.Wrap3DV.from_map(GXContext._get_tls_geo(), p1._wrapper)
        return GX3DV(ret_val)




    def crc_3dv(self, p2: int_ref, p3: str) -> None:
        p2.value = self._wrapper.crc_3dv(p2.value, p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer