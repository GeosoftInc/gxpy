### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXIGRF:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapIGRF(0)

    @classmethod
    def null(cls) -> 'GXIGRF':
        """
        A null (undefined) instance of :class:`GXIGRF`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXIGRF` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXIGRF`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def calc(self, p2: float, p3: float, p4: float, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p5.value, p6.value, p7.value = self._wrapper.calc(p2, p3, p4, p5.value, p6.value, p7.value)
        




    def calc_vv(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV') -> None:
        self._wrapper.calc_vv(p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def create(cls, p1: float, p2: int, p3: str) -> 'GXIGRF':
        ret_val = gxapi_cy.WrapIGRF.create(GXContext._get_tls_geo(), p2, p3.encode())
        return GXIGRF(ret_val)



    @classmethod
    def date_range(cls, p1: str, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = gxapi_cy.WrapIGRF.date_range(GXContext._get_tls_geo(), p2.value, p3.value)
        







### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer