### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref

### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
from . import gxapi_cy_extend
import numpy as np
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVV:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVV(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXVV':
        """
        A null (undefined) instance of :class:`GXVV`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXVV` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXVV`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def get_data(self, p2: int, p3: int, p4: type(bytearray), p5: int) -> int:
        ret_val = self._wrapper.get_data(p2, p3, p4, p5)
        return ret_val




    def set_data(self, p2: int, p3: int, p4: type(bytearray), p5: int) -> int:
        ret_val = self._wrapper.set_data(p2, p3, p4, p5)
        return ret_val




    def copy(self, p2: 'GXVV') -> None:
        self._wrapper.copy(p2._wrapper)
        




    def copy2(self, p2: int, p3: 'GXVV', p4: int, p5: int) -> None:
        self._wrapper.copy2(p2, p3._wrapper, p4, p5)
        




    def log(self, p2: int, p3: int, p4: float) -> None:
        self._wrapper.log(p2, p3, p4)
        




    def log_linear(self, p2: float) -> None:
        self._wrapper.log_linear(p2)
        




    def mask(self, p2: 'GXVV') -> None:
        self._wrapper.mask(p2._wrapper)
        




    def reverse(self) -> None:
        self._wrapper.reverse()
        




    def serial(self, p2: 'GXBF') -> None:
        self._wrapper.serial(p2._wrapper)
        




    def trans(self, p2: float, p3: float) -> None:
        self._wrapper.trans(p2, p3)
        




    def abs(self) -> None:
        self._wrapper.abs()
        




    def add(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.add(p2._wrapper, p3._wrapper)
        




    def add2(self, p2: float, p3: 'GXVV', p4: float, p5: 'GXVV') -> None:
        self._wrapper.add2(p2, p3._wrapper, p4, p5._wrapper)
        




    def append(self, p2: 'GXVV') -> None:
        self._wrapper.append(p2._wrapper)
        




    def crc(self, p2: int) -> int:
        ret_val = self._wrapper.crc(p2)
        return ret_val




    def crc_inexact(self, p2: int, p3: int, p4: int) -> int:
        ret_val = self._wrapper.crc_inexact(p2, p3, p4)
        return ret_val



    @classmethod
    def create(cls, p1: int, p2: int) -> 'GXVV':
        ret_val = gxapi_cy.WrapVV.create(GXContext._get_tls_geo(), p1, p2)
        return GXVV(ret_val)



    @classmethod
    def create_ext(cls, p1: int, p2: int) -> 'GXVV':
        ret_val = gxapi_cy.WrapVV.create_ext(GXContext._get_tls_geo(), p1, p2)
        return GXVV(ret_val)



    @classmethod
    def create_s(cls, p1: 'GXBF') -> 'GXVV':
        ret_val = gxapi_cy.WrapVV.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXVV(ret_val)






    def diff(self, p2: int) -> None:
        self._wrapper.diff(p2)
        




    def divide(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.divide(p2._wrapper, p3._wrapper)
        




    def fid_norm(self, p2: 'GXVV') -> None:
        self._wrapper.fid_norm(p2._wrapper)
        




    def fill_int(self, p2: int) -> None:
        self._wrapper.fill_int(p2)
        




    def fill_double(self, p2: float) -> None:
        self._wrapper.fill_double(p2)
        




    def fill_string(self, p2: str) -> None:
        self._wrapper.fill_string(p2.encode())
        




    def count_dummies(self, p2: int, p3: int) -> int:
        ret_val = self._wrapper.count_dummies(p2, p3)
        return ret_val




    def find_dum(self, p2: int, p3: int, p4: int, p5: int) -> int:
        ret_val = self._wrapper.find_dum(p2, p3, p4, p5)
        return ret_val




    def get_fid_expansion(self) -> int:
        ret_val = self._wrapper.get_fid_expansion()
        return ret_val




    def get_int(self, p2: int) -> int:
        ret_val = self._wrapper.get_int(p2)
        return ret_val




    def get_string(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_string(p2, p3.value.encode())
        




    def index_max(self, p2: float_ref) -> int:
        ret_val, p2.value = self._wrapper.index_max(p2.value)
        return ret_val




    def length(self) -> int:
        ret_val = self._wrapper.length()
        return ret_val




    def index_insert(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.index_insert(p2._wrapper, p3._wrapper)
        




    def index_order(self, p2: 'GXVV') -> None:
        self._wrapper.index_order(p2._wrapper)
        




    def init_index(self, p2: int) -> None:
        self._wrapper.init_index(p2)
        




    def inv_log(self, p2: int, p3: int, p4: float) -> None:
        self._wrapper.inv_log(p2, p3, p4)
        




    def order(self, p2: int_ref) -> int:
        ret_val, p2.value = self._wrapper.order(p2.value)
        return ret_val




    def lines_to_xy(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.lines_to_xy(p2._wrapper, p3._wrapper)
        




    def lookup_index(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.lookup_index(p2._wrapper, p3._wrapper)
        




    def make_mem_based(self) -> None:
        self._wrapper.make_mem_based()
        




    def mask_and(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.mask_and(p2._wrapper, p3._wrapper)
        




    def mask_or(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.mask_or(p2._wrapper, p3._wrapper)
        




    def mask_str(self, p2: 'GXVV', p3: str) -> None:
        self._wrapper.mask_str(p2._wrapper, p3.encode())
        




    def multiply(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.multiply(p2._wrapper, p3._wrapper)
        




    def amplitude_3d(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.amplitude_3d(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def polygon_mask(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXPLY', p5: int) -> None:
        self._wrapper.polygon_mask(p2._wrapper, p3._wrapper, p4._wrapper, p5)
        



    @classmethod
    def project(cls, p1: 'GXPJ', p2: 'GXVV', p3: 'GXVV') -> None:
        gxapi_cy.WrapVV.project(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def project_3d(cls, p1: 'GXPJ', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        gxapi_cy.WrapVV.project_3d(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        




    def range_double(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.range_double(p2.value, p3.value)
        




    def re_fid(self, p2: float, p3: float, p4: int) -> None:
        self._wrapper.re_fid(p2, p3, p4)
        




    def re_fid_vv(self, p2: 'GXVV') -> None:
        self._wrapper.re_fid_vv(p2._wrapper)
        




    def re_sample(self, p2: float, p3: float, p4: float, p5: float, p6: int, p7: int) -> None:
        self._wrapper.re_sample(p2, p3, p4, p5, p6, p7)
        




    def get_fid_incr(self) -> float:
        ret_val = self._wrapper.get_fid_incr()
        return ret_val




    def get_fid_start(self) -> float:
        ret_val = self._wrapper.get_fid_start()
        return ret_val




    def get_double(self, p2: int) -> float:
        ret_val = self._wrapper.get_double(p2)
        return ret_val




    def sum(self) -> float:
        ret_val = self._wrapper.sum()
        return ret_val




    def weighted_mean(self, p2: 'GXVV') -> float:
        ret_val = self._wrapper.weighted_mean(p2._wrapper)
        return ret_val




    def set_fid_expansion(self, p2: int) -> None:
        self._wrapper.set_fid_expansion(p2)
        




    def set_fid_incr(self, p2: float) -> None:
        self._wrapper.set_fid_incr(p2)
        




    def set_fid_start(self, p2: float) -> None:
        self._wrapper.set_fid_start(p2)
        




    def set_int(self, p2: int, p3: int) -> None:
        self._wrapper.set_int(p2, p3)
        




    def set_int_n(self, p2: int, p3: int, p4: int) -> None:
        self._wrapper.set_int_n(p2, p3, p4)
        




    def set_len(self, p2: int) -> None:
        self._wrapper.set_len(p2)
        




    def set_double(self, p2: int, p3: float) -> None:
        self._wrapper.set_double(p2, p3)
        




    def set_double_n(self, p2: int, p3: int, p4: float) -> None:
        self._wrapper.set_double_n(p2, p3, p4)
        




    def set_string(self, p2: int, p3: str) -> None:
        self._wrapper.set_string(p2, p3.encode())
        




    def set_string_n(self, p2: int, p3: int, p4: str) -> None:
        self._wrapper.set_string_n(p2, p3, p4.encode())
        




    def setup_index(self, p2: 'GXVV', p3: 'GXVV', p4: int, p5: float) -> None:
        self._wrapper.setup_index(p2._wrapper, p3._wrapper, p4, p5)
        




    def sort(self, p2: int) -> None:
        self._wrapper.sort(p2)
        




    def sort_index(self, p2: 'GXVV') -> None:
        self._wrapper.sort_index(p2._wrapper)
        




    def sort_index1(self, p2: 'GXVV', p3: int) -> None:
        self._wrapper.sort_index1(p2._wrapper, p3)
        




    def sort_index2(self, p2: 'GXVV', p3: 'GXVV', p4: int, p5: int) -> None:
        self._wrapper.sort_index2(p2._wrapper, p3._wrapper, p4, p5)
        




    def sort_index3(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: int, p6: int, p7: int) -> None:
        self._wrapper.sort_index3(p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7)
        




    def sort_index4(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: int, p7: int, p8: int, p9: int) -> None:
        self._wrapper.sort_index4(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8, p9)
        



    @classmethod
    def statistics(cls, p1: 'GXST', p2: 'GXVV') -> None:
        gxapi_cy.WrapVV.statistics(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        




    def subtract(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.subtract(p2._wrapper, p3._wrapper)
        




    def swap(self) -> None:
        self._wrapper.swap()
        




    def window(self, p2: float, p3: float, p4: int) -> None:
        self._wrapper.window(p2, p3, p4)
        




    def write_xml(self, p2: str, p3: int, p4: int) -> None:
        self._wrapper.write_xml(p2.encode(), p3, p4)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
    def get_data_np(self, start: int, num_elements: int, dtype: int):
        from .GXNumpy import gs_from_np
        gs_type = gs_from_np(dtype)
        r, a = self.get_data_array(start, num_elements, gs_type)
        return (r, np.asarray(a))

    def set_data_np(self, start: int, array: type(np.ndarray)):
        from .GXNumpy import gs_from_np
        gs_type = gs_from_np(array.dtype)
        num_elements = np.prod(array.shape)
        if not array.flags['C_CONTIGUOUS']:
            array = np.ascontiguousarray(array)
        #print("ENTER")
        #input()
        return self.set_data(start, num_elements, array.data.tobytes(), gs_type)
    
    def get_data_array(self, start: int, num_elements: int, gs_type: int):
        r, a = gxapi_cy_extend.WrapVVExtra.get_data_array_vv(GXContext._internal_p(), self._wrapper.handle, start, num_elements, gs_type)
        return (r, a)
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer