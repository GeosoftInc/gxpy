### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDATALINKD:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDATALINKD(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXDATALINKD':
        """
        A null (undefined) instance of :class:`GXDATALINKD`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXDATALINKD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXDATALINKD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create_arc_lyr(cls, p1: str) -> 'GXDATALINKD':
        ret_val = gxapi_cy.WrapDATALINKD.create_arc_lyr(GXContext._get_tls_geo(), p1.encode())
        return GXDATALINKD(ret_val)



    @classmethod
    def create_arc_lyr_ex(cls, p1: str, p2: int) -> 'GXDATALINKD':
        ret_val = gxapi_cy.WrapDATALINKD.create_arc_lyr_ex(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXDATALINKD(ret_val)



    @classmethod
    def create_arc_lyr_from_tmp(cls, p1: str) -> 'GXDATALINKD':
        ret_val = gxapi_cy.WrapDATALINKD.create_arc_lyr_from_tmp(GXContext._get_tls_geo(), p1.encode())
        return GXDATALINKD(ret_val)



    @classmethod
    def create_arc_lyr_from_tmp_ex(cls, p1: str, p2: int) -> 'GXDATALINKD':
        ret_val = gxapi_cy.WrapDATALINKD.create_arc_lyr_from_tmp_ex(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXDATALINKD(ret_val)



    @classmethod
    def create_bing(cls, p1: int) -> 'GXDATALINKD':
        ret_val = gxapi_cy.WrapDATALINKD.create_bing(GXContext._get_tls_geo(), p1)
        return GXDATALINKD(ret_val)






    def get_extents(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_extents(p2.value, p3.value, p4.value, p5.value)
        




    def get_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.get_ipj(p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer