### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVM:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVM(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXVM':
        """
        A null (undefined) instance of :class:`GXVM`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXVM` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXVM`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: int, p2: int) -> 'GXVM':
        ret_val = gxapi_cy.WrapVM.create(GXContext._get_tls_geo(), p1, p2)
        return GXVM(ret_val)



    @classmethod
    def create_ext(cls, p1: int, p2: int) -> 'GXVM':
        ret_val = gxapi_cy.WrapVM.create_ext(GXContext._get_tls_geo(), p1, p2)
        return GXVM(ret_val)






    def get_int(self, p2: int) -> int:
        ret_val = self._wrapper.get_int(p2)
        return ret_val




    def get_string(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_string(p2, p3.value.encode())
        




    def length(self) -> int:
        ret_val = self._wrapper.length()
        return ret_val




    def re_size(self, p2: int) -> None:
        self._wrapper.re_size(p2)
        




    def get_double(self, p2: int) -> float:
        ret_val = self._wrapper.get_double(p2)
        return ret_val




    def set_int(self, p2: int, p3: int) -> None:
        self._wrapper.set_int(p2, p3)
        




    def set_double(self, p2: int, p3: float) -> None:
        self._wrapper.set_double(p2, p3)
        




    def set_string(self, p2: int, p3: str) -> None:
        self._wrapper.set_string(p2, p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer