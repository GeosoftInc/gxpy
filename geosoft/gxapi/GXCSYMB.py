### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXCSYMB:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapCSYMB(0)

    @classmethod
    def null(cls) -> 'GXCSYMB':
        """
        A null (undefined) instance of :class:`GXCSYMB`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXCSYMB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXCSYMB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def set_angle(self, p2: float) -> None:
        self._wrapper.set_angle(p2)
        




    def set_base(self, p2: float) -> None:
        self._wrapper.set_base(p2)
        




    def set_dynamic_col(self, p2: int) -> None:
        self._wrapper.set_dynamic_col(p2)
        




    def set_fixed(self, p2: int) -> None:
        self._wrapper.set_fixed(p2)
        




    def set_number(self, p2: int) -> None:
        self._wrapper.set_number(p2)
        




    def set_scale(self, p2: float) -> None:
        self._wrapper.set_scale(p2)
        




    def add_data(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.add_data(p2, p3, p4)
        



    @classmethod
    def create(cls, p1: str) -> 'GXCSYMB':
        ret_val = gxapi_cy.WrapCSYMB.create(GXContext._get_tls_geo())
        return GXCSYMB(ret_val)






    def get_itr(self, p2: 'GXITR') -> None:
        self._wrapper.get_itr(p2)
        




    def set_font(self, p2: str, p3: int, p4: int, p5: int) -> None:
        self._wrapper.set_font(p2.encode(), p3, p4, p5)
        




    def set_static_col(self, p2: int, p3: int) -> None:
        self._wrapper.set_static_col(p2, p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer