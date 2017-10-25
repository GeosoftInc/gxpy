### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
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

    The :class:`GXDXFI` class is used for importing AutoCAD® dxf files into Geosoft maps.
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
    def null(cls) -> 'GXDXFI':
        """
        A null (undefined) instance of :class:`GXDXFI`
        
        :returns: A null :class:`GXDXFI`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXDXFI` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXDXFI`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: str) -> 'GXDXFI':
        ret_val = gxapi_cy.WrapDXFI.create(GXContext._get_tls_geo(), p1.encode())
        return GXDXFI(ret_val)





    @classmethod
    def dxf2_ply(cls, p1: 'GXPLY', p2: 'GXDXFI') -> None:
        gxapi_cy.WrapDXFI.dxf2_ply(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        




    def dxf2_view_ex(self, p2: 'GXMVIEW', p3: int, p4: int, p5: str, p6: int, p7: int) -> None:
        self._wrapper.dxf2_view_ex(p2._wrapper, p3, p4, p5.encode(), p6, p7)
        




    def get_range(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_range(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer