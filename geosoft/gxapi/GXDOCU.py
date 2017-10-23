### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDOCU:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDOCU(0)

    @classmethod
    def null(cls) -> 'GXDOCU':
        """
        A null (undefined) instance of :class:`GXDOCU`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXDOCU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXDOCU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def copy(self, p2: 'GXDOCU') -> None:
        self._wrapper.copy(p2)
        



    @classmethod
    def create(cls) -> 'GXDOCU':
        ret_val = gxapi_cy.WrapDOCU.create(GXContext._get_tls_geo())
        return GXDOCU(ret_val)



    @classmethod
    def create_s(cls, p1: 'GXBF') -> 'GXDOCU':
        ret_val = gxapi_cy.WrapDOCU.create_s(GXContext._get_tls_geo())
        return GXDOCU(ret_val)






    def get_file(self, p2: str) -> None:
        self._wrapper.get_file(p2.encode())
        




    def get_file_meta(self, p2: str) -> None:
        self._wrapper.get_file_meta(p2.encode())
        




    def get_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.get_meta(p2)
        




    def doc_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.doc_name(p2.value.encode())
        




    def file_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.file_name(p2.value.encode())
        




    def have_meta(self) -> int:
        ret_val = self._wrapper.have_meta()
        return ret_val




    def is_reference(self) -> int:
        ret_val = self._wrapper.is_reference()
        return ret_val




    def open(self, p2: int) -> None:
        self._wrapper.open(p2)
        




    def serial(self, p2: 'GXBF') -> None:
        self._wrapper.serial(p2)
        




    def set_file(self, p2: str, p3: str, p4: str) -> None:
        self._wrapper.set_file(p2.encode(), p3.encode(), p4.encode())
        




    def set_file_meta(self, p2: str, p3: str, p4: str) -> None:
        self._wrapper.set_file_meta(p2.encode(), p3.encode(), p4.encode())
        




    def set_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.set_meta(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer