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
class GXBF:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapBF(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXBF':
        """
        A null (undefined) instance of :class:`GXBF`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXBF` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXBF`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def ch_size(self, p2: int) -> None:
        self._wrapper.ch_size(p2)
        




    def seek(self, p2: int, p3: int) -> None:
        self._wrapper.seek(p2, p3)
        




    def copy(self, p2: 'GXBF') -> None:
        self._wrapper.copy(p2._wrapper)
        




    def crc(self, p2: int, p3: int) -> int:
        ret_val = self._wrapper.crc(p2, p3)
        return ret_val



    @classmethod
    def create(cls, p1: str, p2: int) -> 'GXBF':
        ret_val = gxapi_cy.WrapBF.create(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXBF(ret_val)



    @classmethod
    def create_sbf(cls, p1: 'GXSBF', p2: str, p3: int) -> 'GXBF':
        ret_val = gxapi_cy.WrapBF.create_sbf(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3)
        return GXBF(ret_val)








    def eof(self) -> int:
        ret_val = self._wrapper.eof()
        return ret_val




    def query_write(self) -> int:
        ret_val = self._wrapper.query_write()
        return ret_val




    def read_binary_string(self, p2: int, p3: int, p4: str_ref) -> None:
        p4.value = self._wrapper.read_binary_string(p2, p3, p4.value.encode())
        




    def size(self) -> int:
        ret_val = self._wrapper.size()
        return ret_val




    def tell(self) -> int:
        ret_val = self._wrapper.tell()
        return ret_val




    def read_int(self, p2: int, p3: int_ref) -> None:
        p3.value = self._wrapper.read_int(p2, p3.value)
        




    def read_double(self, p2: int, p3: float_ref) -> None:
        p3.value = self._wrapper.read_double(p2, p3.value)
        




    def read_vv(self, p2: int, p3: 'GXVV') -> None:
        self._wrapper.read_vv(p2, p3._wrapper)
        




    def set_destroy_status(self, p2: int) -> None:
        self._wrapper.set_destroy_status(p2)
        




    def write_binary_string(self, p2: int, p3: str) -> None:
        self._wrapper.write_binary_string(p2, p3.encode())
        




    def write_data_null(self) -> None:
        self._wrapper.write_data_null()
        




    def write_int(self, p2: int, p3: int) -> None:
        self._wrapper.write_int(p2, p3)
        




    def write_double(self, p2: int, p3: float) -> None:
        self._wrapper.write_double(p2, p3)
        




    def write_vv(self, p2: int, p3: 'GXVV') -> None:
        self._wrapper.write_vv(p2, p3._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer