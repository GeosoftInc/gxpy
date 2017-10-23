### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXGER:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapGER(0)

    @classmethod
    def null(cls) -> 'GXGER':
        """
        A null (undefined) instance of :class:`GXGER`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXGER` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXGER`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: str) -> 'GXGER':
        ret_val = gxapi_cy.WrapGER.create(GXContext._get_tls_geo(), p1.encode())
        return GXGER(ret_val)






    def get(self, p2: int, p3: str_ref) -> int:
        ret_val, p3.value = self._wrapper.get(p2, p3.value.encode())
        return ret_val




    def set_int(self, p2: str, p3: int) -> None:
        self._wrapper.set_int(p2.encode(), p3)
        




    def set_double(self, p2: str, p3: float) -> None:
        self._wrapper.set_double(p2.encode(), p3)
        




    def set_string(self, p2: str, p3: str) -> None:
        self._wrapper.set_string(p2.encode(), p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer