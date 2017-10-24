### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMAPL:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMAPL(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXMAPL':
        """
        A null (undefined) instance of :class:`GXMAPL`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXMAPL` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXMAPL`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: str, p2: str, p3: int) -> 'GXMAPL':
        ret_val = gxapi_cy.WrapMAPL.create(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        return GXMAPL(ret_val)



    @classmethod
    def create_reg(cls, p1: str, p2: str, p3: int, p4: 'GXREG') -> 'GXMAPL':
        ret_val = gxapi_cy.WrapMAPL.create_reg(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4._wrapper)
        return GXMAPL(ret_val)






    def process(self, p2: 'GXMAP') -> None:
        self._wrapper.process(p2._wrapper)
        




    def replace_string(self, p2: str, p3: str) -> None:
        self._wrapper.replace_string(p2.encode(), p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer