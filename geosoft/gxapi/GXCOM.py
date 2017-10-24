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
class GXCOM:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapCOM(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXCOM':
        """
        A null (undefined) instance of :class:`GXCOM`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXCOM` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXCOM`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: str, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> 'GXCOM':
        ret_val = gxapi_cy.WrapCOM.create(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7)
        return GXCOM(ret_val)



    @classmethod
    def create_no_terminate(cls, p1: str, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int) -> 'GXCOM':
        ret_val = gxapi_cy.WrapCOM.create_no_terminate(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7)
        return GXCOM(ret_val)






    def read_line_no_terminate(self, p2: str_ref) -> int:
        ret_val, p2.value = self._wrapper.read_line_no_terminate(p2.value.encode())
        return ret_val




    def read_chars_no_terminate(self, p2: str_ref) -> int:
        ret_val, p2.value = self._wrapper.read_chars_no_terminate(p2.value.encode())
        return ret_val




    def read_line(self, p2: str_ref) -> None:
        p2.value = self._wrapper.read_line(p2.value.encode())
        




    def write_chars_no_terminate(self, p2: str) -> int:
        ret_val = self._wrapper.write_chars_no_terminate(p2.encode())
        return ret_val




    def purge_comm(self) -> None:
        self._wrapper.purge_comm()
        




    def read_chars(self, p2: str_ref) -> None:
        p2.value = self._wrapper.read_chars(p2.value.encode())
        




    def read_em61_lines_wa(self, p2: int, p3: 'GXWA') -> None:
        self._wrapper.read_em61_lines_wa(p2, p3._wrapper)
        




    def read_file2_wa(self, p2: 'GXWA') -> None:
        self._wrapper.read_file2_wa(p2._wrapper)
        




    def read_lines_wa(self, p2: int, p3: 'GXWA') -> None:
        self._wrapper.read_lines_wa(p2, p3._wrapper)
        




    def set_time_out(self, p2: int) -> None:
        self._wrapper.set_time_out(p2)
        




    def write_chars(self, p2: str) -> None:
        self._wrapper.write_chars(p2.encode())
        




    def write_line(self, p2: str) -> None:
        self._wrapper.write_line(p2.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer