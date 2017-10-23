### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVA:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVA(0)

    @classmethod
    def null(cls) -> 'GXVA':
        """
        A null (undefined) instance of :class:`GXVA`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXVA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXVA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def get_array(self, p2: int, p3: int, p4: int, p5: int, p6: type(bytearray), p7: int) -> int:
        ret_val = self._wrapper.get_array(p2, p3, p4, p5, p6, p7)
        return ret_val




    def set_array(self, p2: int, p3: int, p4: int, p5: int, p6: type(bytearray), p7: int) -> int:
        ret_val = self._wrapper.set_array(p2, p3, p4, p5, p6, p7)
        return ret_val




    def add_elevations_vv_to_depths(self, p2: 'GXVV', p3: int) -> None:
        self._wrapper.add_elevations_vv_to_depths(p2, p3)
        




    def append(self, p2: 'GXVA') -> None:
        self._wrapper.append(p2)
        




    def average(self, p2: 'GXVV', p3: int) -> None:
        self._wrapper.average(p2, p3)
        




    def copy(self, p2: 'GXVA') -> None:
        self._wrapper.copy(p2)
        




    def copy2(self, p2: int, p3: int, p4: 'GXVA', p5: int, p6: int, p7: int, p8: int) -> None:
        self._wrapper.copy2(p2, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def create(cls, p1: int, p2: int, p3: int) -> 'GXVA':
        ret_val = gxapi_cy.WrapVA.create(GXContext._get_tls_geo(), p2, p3)
        return GXVA(ret_val)



    @classmethod
    def create_ext(cls, p1: int, p2: int, p3: int) -> 'GXVA':
        ret_val = gxapi_cy.WrapVA.create_ext(GXContext._get_tls_geo(), p2, p3)
        return GXVA(ret_val)



    @classmethod
    def create_vv(cls, p1: 'GXVV', p2: int, p3: int) -> 'GXVA':
        ret_val = gxapi_cy.WrapVA.create_vv(GXContext._get_tls_geo(), p2, p3)
        return GXVA(ret_val)






    def get_full_vv(self) -> 'GXVV':
        ret_val = self._wrapper.get_full_vv()
        return GXVV(ret_val)




    def get_vv(self, p2: int, p3: int, p4: 'GXVV') -> None:
        self._wrapper.get_vv(p2, p3, p4)
        




    def col(self) -> int:
        ret_val = self._wrapper.col()
        return ret_val




    def get_int(self, p2: int, p3: int) -> int:
        ret_val = self._wrapper.get_int(p2, p3)
        return ret_val




    def get_string(self, p2: int, p3: int, p4: str_ref) -> None:
        p4.value = self._wrapper.get_string(p2, p3, p4.value.encode())
        




    def len(self) -> int:
        ret_val = self._wrapper.len()
        return ret_val



    @classmethod
    def index_order(cls, p1: 'GXVV', p2: 'GXVA') -> None:
        gxapi_cy.WrapVA.index_order(GXContext._get_tls_geo(), p2)
        




    def lookup_index(self, p2: 'GXVV', p3: 'GXVA') -> None:
        self._wrapper.lookup_index(p2, p3)
        




    def range_double(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.range_double(p2.value, p3.value)
        




    def re_fid(self, p2: float, p3: float, p4: int) -> None:
        self._wrapper.re_fid(p2, p3, p4)
        




    def reverse(self) -> None:
        self._wrapper.reverse()
        




    def get_fid_incr(self) -> float:
        ret_val = self._wrapper.get_fid_incr()
        return ret_val




    def get_fid_start(self) -> float:
        ret_val = self._wrapper.get_fid_start()
        return ret_val




    def get_double(self, p2: int, p3: int) -> float:
        ret_val = self._wrapper.get_double(p2, p3)
        return ret_val




    def set_fid_incr(self, p2: float) -> None:
        self._wrapper.set_fid_incr(p2)
        




    def set_fid_start(self, p2: float) -> None:
        self._wrapper.set_fid_start(p2)
        




    def set_int(self, p2: int, p3: int, p4: int) -> None:
        self._wrapper.set_int(p2, p3, p4)
        




    def set_ln(self, p2: int) -> None:
        self._wrapper.set_ln(p2)
        




    def set_double(self, p2: int, p3: int, p4: float) -> None:
        self._wrapper.set_double(p2, p3, p4)
        




    def set_string(self, p2: int, p3: int, p4: str) -> None:
        self._wrapper.set_string(p2, p3, p4.encode())
        




    def set_vv(self, p2: int, p3: int, p4: 'GXVV') -> None:
        self._wrapper.set_vv(p2, p3, p4)
        




    def trans(self, p2: float, p3: float) -> None:
        self._wrapper.trans(p2, p3)
        




    def window(self, p2: int, p3: int, p4: 'GXVV') -> None:
        self._wrapper.window(p2, p3, p4)
        




    def window2(self, p2: float, p3: float, p4: 'GXVV') -> None:
        self._wrapper.window2(p2, p3, p4)
        




    def check_for_repeating(self, p2: 'GXVV', p3: int, p4: 'GXVV', p5: float) -> int:
        ret_val = self._wrapper.check_for_repeating(p2, p3, p4, p5)
        return ret_val




    def check_for_repeating2(self, p2: 'GXVV', p3: int, p4: 'GXVV', p5: float, p6: int_ref, p7: int_ref) -> int:
        ret_val, p6.value, p7.value = self._wrapper.check_for_repeating2(p2, p3, p4, p5, p6.value, p7.value)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer