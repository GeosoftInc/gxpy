### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXTEST:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapTEST(0)

    @classmethod
    def null(cls) -> 'GXTEST':
        """
        A null (undefined) instance of :class:`GXTEST`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXTEST` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXTEST`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def enable_disable_arc_engine_license(cls, p1: int) -> None:
        gxapi_cy.WrapTEST.enable_disable_arc_engine_license(GXContext._get_tls_geo())
        



    @classmethod
    def arc_engine_license(cls) -> int:
        ret_val = gxapi_cy.WrapTEST.arc_engine_license(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def test_mode(cls) -> int:
        ret_val = gxapi_cy.WrapTEST.test_mode(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def wrapper_test(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapTEST.wrapper_test(GXContext._get_tls_geo(), p2.encode())
        



    @classmethod
    def core_class(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapTEST.core_class(GXContext._get_tls_geo(), p2.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer