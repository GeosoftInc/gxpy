### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXREG:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapREG(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXREG':
        """
        A null (undefined) instance of :class:`GXREG`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXREG` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXREG`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clear(self) -> None:
        self._wrapper.clear()
        




    def copy(self, p2: 'GXREG') -> None:
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls, p1: int) -> 'GXREG':
        ret_val = gxapi_cy.WrapREG.create(GXContext._get_tls_geo(), p1)
        return GXREG(ret_val)



    @classmethod
    def create_s(cls, p1: 'GXBF') -> 'GXREG':
        ret_val = gxapi_cy.WrapREG.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXREG(ret_val)






    def get(self, p2: str, p3: str_ref) -> None:
        p3.value = self._wrapper.get(p2.encode(), p3.value.encode())
        




    def get_int(self, p2: str, p3: int_ref) -> None:
        p3.value = self._wrapper.get_int(p2.encode(), p3.value)
        




    def get_one(self, p2: int, p3: str_ref, p5: str_ref) -> None:
        p3.value, p5.value = self._wrapper.get_one(p2, p3.value.encode(), p5.value.encode())
        




    def get_double(self, p2: str, p3: float_ref) -> None:
        p3.value = self._wrapper.get_double(p2.encode(), p3.value)
        




    def entries(self) -> int:
        ret_val = self._wrapper.entries()
        return ret_val




    def load_ini(self, p2: str) -> None:
        self._wrapper.load_ini(p2.encode())
        




    def match_string(self, p2: str, p3: str_ref) -> None:
        p3.value = self._wrapper.match_string(p2.encode(), p3.value.encode())
        




    def merge(self, p2: 'GXREG', p3: int) -> None:
        self._wrapper.merge(p2._wrapper, p3)
        




    def save_ini(self, p2: str) -> None:
        self._wrapper.save_ini(p2.encode())
        




    def serial(self, p2: 'GXBF') -> None:
        self._wrapper.serial(p2._wrapper)
        




    def set(self, p2: str, p3: str) -> None:
        self._wrapper.set(p2.encode(), p3.encode())
        




    def set_int(self, p2: str, p3: int) -> None:
        self._wrapper.set_int(p2.encode(), p3)
        




    def set_double(self, p2: str, p3: float) -> None:
        self._wrapper.set_double(p2.encode(), p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer