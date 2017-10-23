### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXLTB:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapLTB(0)

    @classmethod
    def null(cls) -> 'GXLTB':
        """
        A null (undefined) instance of :class:`GXLTB`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXLTB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXLTB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_record(self, p2: str, p3: int_ref) -> None:
        p3.value = self._wrapper.add_record(p2.encode(), p3.value)
        




    def contract(self, p2: 'GXLTB') -> 'GXLTB':
        ret_val = self._wrapper.contract(p2._wrapper)
        return GXLTB(ret_val)



    @classmethod
    def create(cls, p1: str, p2: int, p3: int, p4: str) -> 'GXLTB':
        ret_val = gxapi_cy.WrapLTB.create(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4.encode())
        return GXLTB(ret_val)



    @classmethod
    def create_crypt(cls, p1: str, p2: int, p3: int, p4: int, p5: str, p6: str) -> 'GXLTB':
        ret_val = gxapi_cy.WrapLTB.create_crypt(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5.encode(), p6.encode())
        return GXLTB(ret_val)



    @classmethod
    def create_ex(cls, p1: str, p2: int, p3: int, p4: int, p5: str) -> 'GXLTB':
        ret_val = gxapi_cy.WrapLTB.create_ex(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5.encode())
        return GXLTB(ret_val)




    def delete_record(self, p2: int) -> None:
        self._wrapper.delete_record(p2)
        






    def get_con_lst(self, p2: int, p3: str, p4: int, p5: 'GXLST') -> None:
        self._wrapper.get_con_lst(p2, p3.encode(), p4, p5._wrapper)
        




    def get_lst(self, p2: int, p3: 'GXLST') -> None:
        self._wrapper.get_lst(p2, p3._wrapper)
        




    def get_lst2(self, p2: int, p3: int, p4: 'GXLST') -> None:
        self._wrapper.get_lst2(p2, p3, p4._wrapper)
        




    def fields(self) -> int:
        ret_val = self._wrapper.fields()
        return ret_val




    def find_field(self, p2: str) -> int:
        ret_val = self._wrapper.find_field(p2.encode())
        return ret_val




    def find_key(self, p2: str) -> int:
        ret_val = self._wrapper.find_key(p2.encode())
        return ret_val




    def get_field(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_field(p2, p3.value.encode())
        




    def get_int(self, p2: int, p3: int) -> int:
        ret_val = self._wrapper.get_int(p2, p3)
        return ret_val




    def get_string(self, p2: int, p3: int, p4: str_ref) -> None:
        p4.value = self._wrapper.get_string(p2, p3, p4.value.encode())
        




    def get_english_string(self, p2: int, p3: int, p4: str_ref) -> None:
        p4.value = self._wrapper.get_english_string(p2, p3, p4.value.encode())
        




    def records(self) -> int:
        ret_val = self._wrapper.records()
        return ret_val




    def search(self, p2: int, p3: int, p4: str) -> int:
        ret_val = self._wrapper.search(p2, p3, p4.encode())
        return ret_val




    def merge(self, p2: 'GXLTB') -> 'GXLTB':
        ret_val = self._wrapper.merge(p2._wrapper)
        return GXLTB(ret_val)




    def get_double(self, p2: int, p3: int) -> float:
        ret_val = self._wrapper.get_double(p2, p3)
        return ret_val




    def save(self, p2: str) -> None:
        self._wrapper.save(p2.encode())
        




    def save_crypt(self, p2: str, p3: str) -> None:
        self._wrapper.save_crypt(p2.encode(), p3.encode())
        




    def set_int(self, p2: int, p3: int, p4: int) -> None:
        self._wrapper.set_int(p2, p3, p4)
        




    def set_double(self, p2: int, p3: int, p4: float) -> None:
        self._wrapper.set_double(p2, p3, p4)
        




    def set_string(self, p2: int, p3: int, p4: str) -> None:
        self._wrapper.set_string(p2, p3, p4.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer