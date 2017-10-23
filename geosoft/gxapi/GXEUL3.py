### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXEUL3:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapEUL3(0)

    @classmethod
    def null(cls) -> 'GXEUL3':
        """
        A null (undefined) instance of :class:`GXEUL3`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXEUL3` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXEUL3`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def destr(self) -> None:
        self._wrapper.destr()
        



    @classmethod
    def creat(cls, p1: 'GXIMG', p2: 'GXIMG', p3: 'GXIMG', p4: 'GXIMG', p5: int, p6: float, p7: float, p8: float, p9: int, p10: float, p11: float) -> 'GXEUL3':
        ret_val = gxapi_cy.WrapEUL3.creat(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7, p8, p9, p10, p11)
        return GXEUL3(ret_val)




    def get_result(self, p2: 'GXVV', p3: int) -> None:
        self._wrapper.get_result(p2._wrapper, p3)
        




    def write(self, p2: str) -> None:
        self._wrapper.write(p2.encode())
        



    @classmethod
    def ex_euler_derive(cls, p1: 'GXVV', p2: float, p3: 'GXVV', p4: int, p5: 'GXVV', p6: 'GXVV', p7: int) -> int:
        ret_val = gxapi_cy.WrapEUL3.ex_euler_derive(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper, p4, p5._wrapper, p6._wrapper, p7)
        return ret_val



    @classmethod
    def ex_euler_calc(cls, p1: int, p2: float, p3: int, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: int, p12: 'GXVV', p13: 'GXVV', p14: 'GXVV', p15: 'GXVV', p16: int, p17: 'GXVV', p18: 'GXVV', p19: 'GXVV', p20: 'GXVV') -> int:
        ret_val = gxapi_cy.WrapEUL3.ex_euler_calc(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12._wrapper, p13._wrapper, p14._wrapper, p15._wrapper, p16, p17._wrapper, p18._wrapper, p19._wrapper, p20._wrapper)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer