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
class GXLST:
    """
    GXLST class.

    The :class:`GXLST` class is used to create and retrieve lists,
    and to perform specific actions on lists, including
    retrieving list items, sorting lists and adding or
    removing list items.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapLST(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXLST':
        """
        A null (undefined) instance of :class:`GXLST`
        
        :returns: A null :class:`GXLST`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXLST` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXLST`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_item(self, p2: str, p3: str) -> None:
        self._wrapper.add_item(p2.encode(), p3.encode())
        




    def add_symb_item(self, p2: str, p3: int) -> None:
        self._wrapper.add_symb_item(p2.encode(), p3)
        




    def add_unique_item(self, p2: str, p3: str) -> None:
        self._wrapper.add_unique_item(p2.encode(), p3.encode())
        




    def append(self, p2: 'GXLST') -> None:
        self._wrapper.append(p2._wrapper)
        



    @classmethod
    def assay_channel(cls) -> 'GXLST':
        ret_val = gxapi_cy.WrapLST.assay_channel(GXContext._get_tls_geo())
        return GXLST(ret_val)




    def clear(self) -> None:
        self._wrapper.clear()
        




    def convert_from_csv_string(self, p2: str) -> None:
        self._wrapper.convert_from_csv_string(p2.encode())
        




    def copy(self, p2: 'GXLST') -> None:
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls, p1: int) -> 'GXLST':
        ret_val = gxapi_cy.WrapLST.create(GXContext._get_tls_geo(), p1)
        return GXLST(ret_val)



    @classmethod
    def create_s(cls, p1: 'GXBF') -> 'GXLST':
        ret_val = gxapi_cy.WrapLST.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXLST(ret_val)




    def del_item(self, p2: int) -> None:
        self._wrapper.del_item(p2)
        






    def find_items(self, p2: int, p3: 'GXLST', p4: 'GXVV') -> None:
        self._wrapper.find_items(p2, p3._wrapper, p4._wrapper)
        




    def gt_item(self, p2: int, p3: int, p4: str_ref) -> None:
        p4.value = self._wrapper.gt_item(p2, p3, p4.value.encode())
        




    def gt_symb_item(self, p2: int, p3: str_ref, p5: int_ref) -> None:
        p3.value, p5.value = self._wrapper.gt_symb_item(p2, p3.value.encode(), p5.value)
        




    def convert_to_csv_string(self, p2: str_ref) -> None:
        p2.value = self._wrapper.convert_to_csv_string(p2.value.encode())
        




    def find_item(self, p2: int, p3: str) -> int:
        ret_val = self._wrapper.find_item(p2, p3.encode())
        return ret_val




    def find_item_mask(self, p2: int, p3: str) -> int:
        ret_val = self._wrapper.find_item_mask(p2, p3.encode())
        return ret_val




    def get_int(self, p2: int, p3: int) -> int:
        ret_val = self._wrapper.get_int(p2, p3)
        return ret_val




    def insert_item(self, p2: int, p3: str, p4: str) -> None:
        self._wrapper.insert_item(p2, p3.encode(), p4.encode())
        




    def size(self) -> int:
        ret_val = self._wrapper.size()
        return ret_val




    def load_csv(self, p2: str, p3: str, p4: str) -> None:
        self._wrapper.load_csv(p2.encode(), p3.encode(), p4.encode())
        




    def load_file(self, p2: str) -> None:
        self._wrapper.load_file(p2.encode())
        




    def resource(self, p2: str) -> None:
        self._wrapper.resource(p2.encode())
        




    def get_double(self, p2: int, p3: int) -> float:
        ret_val = self._wrapper.get_double(p2, p3)
        return ret_val




    def save_file(self, p2: str) -> None:
        self._wrapper.save_file(p2.encode())
        




    def select_csv_string_items(self, p2: str, p3: 'GXLST') -> None:
        self._wrapper.select_csv_string_items(p2.encode(), p3._wrapper)
        




    def serial(self, p2: 'GXBF') -> None:
        self._wrapper.serial(p2._wrapper)
        




    def set_item(self, p2: int, p3: int, p4: str) -> None:
        self._wrapper.set_item(p2, p3, p4.encode())
        




    def sort(self, p2: int, p3: int) -> None:
        self._wrapper.sort(p2, p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer