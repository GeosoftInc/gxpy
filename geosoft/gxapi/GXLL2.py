### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXLL2:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapLL2(0)

    @classmethod
    def null(cls) -> 'GXLL2':
        """
        A null (undefined) instance of :class:`GXLL2`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXLL2` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXLL2`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: float, p2: float, p3: float, p4: float, p5: int, p6: int, p7: 'GXIPJ', p8: 'GXIPJ') -> 'GXLL2':
        ret_val = gxapi_cy.WrapLL2.create(GXContext._get_tls_geo(), p2, p3, p4, p5, p6, p7, p8)
        return GXLL2(ret_val)






    def save(self, p2: str) -> None:
        self._wrapper.save(p2.encode())
        




    def set_row(self, p2: int, p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.set_row(p2, p3, p4)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer