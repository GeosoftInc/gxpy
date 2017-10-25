### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref

### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXTB:
    """
    GXTB class.

    The :class:`GXTB` class is a high-performance table class used to
    perform table-based processing, such as leveling data in
    an OASIS database. The :class:`GXLTB` class is recommended for use
    with small tables produced from short lists such as the
    different geographic projections and their defining parameters.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapTB(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXTB':
        """
        A null (undefined) instance of :class:`GXTB`
        
        :returns: A null :class:`GXTB`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXTB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXTB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def set_search_mode(self, p2: int) -> None:
        self._wrapper.set_search_mode(p2)
        



    @classmethod
    def create(cls, p1: str) -> 'GXTB':
        ret_val = gxapi_cy.WrapTB.create(GXContext._get_tls_geo(), p1.encode())
        return GXTB(ret_val)



    @classmethod
    def create_db(cls, p1: 'GXDB') -> 'GXTB':
        ret_val = gxapi_cy.WrapTB.create_db(GXContext._get_tls_geo(), p1._wrapper)
        return GXTB(ret_val)



    @classmethod
    def create_ltb(cls, p1: 'GXLTB') -> 'GXTB':
        ret_val = gxapi_cy.WrapTB.create_ltb(GXContext._get_tls_geo(), p1._wrapper)
        return GXTB(ret_val)






    def field(self, p2: str) -> int:
        ret_val = self._wrapper.field(p2.encode())
        return ret_val




    def get_string(self, p2: int, p3: int, p4: str_ref) -> None:
        p4.value = self._wrapper.get_string(p2, p3, p4.value.encode())
        




    def data_type(self, p2: int) -> int:
        ret_val = self._wrapper.data_type(p2)
        return ret_val




    def find_col_by_index(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.find_col_by_index(p2, p3.value.encode())
        




    def find_col_by_name(self, p2: str) -> int:
        ret_val = self._wrapper.find_col_by_name(p2.encode())
        return ret_val




    def format(self, p2: int) -> int:
        ret_val = self._wrapper.format(p2)
        return ret_val




    def get_int(self, p2: int, p3: int) -> int:
        ret_val = self._wrapper.get_int(p2, p3)
        return ret_val




    def num_columns(self) -> int:
        ret_val = self._wrapper.num_columns()
        return ret_val




    def num_rows(self) -> int:
        ret_val = self._wrapper.num_rows()
        return ret_val




    def load_db(self, p2: 'GXDB', p3: int) -> None:
        self._wrapper.load_db(p2._wrapper, p3)
        




    def get_double(self, p2: int, p3: int) -> float:
        ret_val = self._wrapper.get_double(p2, p3)
        return ret_val




    def save(self, p2: str) -> None:
        self._wrapper.save(p2.encode())
        




    def save_db(self, p2: 'GXDB', p3: int) -> None:
        self._wrapper.save_db(p2._wrapper, p3)
        




    def save_to_ascii(self, p2: str) -> None:
        self._wrapper.save_to_ascii(p2.encode())
        




    def set_int(self, p2: int, p3: int, p4: int) -> None:
        self._wrapper.set_int(p2, p3, p4)
        




    def set_double(self, p2: int, p3: int, p4: float) -> None:
        self._wrapper.set_double(p2, p3, p4)
        




    def set_string(self, p2: int, p3: int, p4: str) -> None:
        self._wrapper.set_string(p2, p3, p4.encode())
        




    def sort(self, p2: int) -> None:
        self._wrapper.sort(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer