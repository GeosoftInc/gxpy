### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDGW:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDGW(0)

    @classmethod
    def null(cls) -> 'GXDGW':
        """
        A null (undefined) instance of :class:`GXDGW`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXDGW` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXDGW`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: str) -> 'GXDGW':
        ret_val = gxapi_cy.WrapDGW.create(GXContext._get_tls_geo())
        return GXDGW(ret_val)






    def get_info_meta(self, p2: int, p3: int, p4: 'GXMETA', p5: int, p6: int) -> None:
        self._wrapper.get_info_meta(p2, p3, p4, p5, p6)
        




    def get_info_sys(self, p2: int, p3: int, p4: str, p5: str) -> None:
        self._wrapper.get_info_sys(p2, p3, p4.encode(), p5.encode())
        




    def get_list(self, p2: int) -> 'GXLST':
        ret_val = self._wrapper.get_list(p2)
        return GXLST(ret_val)




    def gt_info(self, p2: int, p3: int, p4: str_ref) -> None:
        p4.value = self._wrapper.gt_info(p2, p3, p4.value.encode())
        




    def run_dialogue(self) -> int:
        ret_val = self._wrapper.run_dialogue()
        return ret_val




    def set_info(self, p2: int, p3: int, p4: str) -> None:
        self._wrapper.set_info(p2, p3, p4.encode())
        




    def set_info_meta(self, p2: int, p3: int, p4: 'GXMETA', p5: int, p6: int) -> None:
        self._wrapper.set_info_meta(p2, p3, p4, p5, p6)
        




    def set_info_sys(self, p2: int, p3: int, p4: str, p5: str) -> None:
        self._wrapper.set_info_sys(p2, p3, p4.encode(), p5.encode())
        




    def set_title(self, p2: str) -> None:
        self._wrapper.set_title(p2.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer