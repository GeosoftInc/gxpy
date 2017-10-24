### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXWA:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapWA(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXWA':
        """
        A null (undefined) instance of :class:`GXWA`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXWA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXWA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def puts(self, p2: str) -> None:
        self._wrapper.puts(p2.encode())
        



    @classmethod
    def create(cls, p1: str, p2: int) -> 'GXWA':
        ret_val = gxapi_cy.WrapWA.create(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXWA(ret_val)



    @classmethod
    def create_ex(cls, p1: str, p2: int, p3: int) -> 'GXWA':
        ret_val = gxapi_cy.WrapWA.create_ex(GXContext._get_tls_geo(), p1.encode(), p2, p3)
        return GXWA(ret_val)



    @classmethod
    def create_sbf(cls, p1: 'GXSBF', p2: str, p3: int) -> 'GXWA':
        ret_val = gxapi_cy.WrapWA.create_sbf(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3)
        return GXWA(ret_val)



    @classmethod
    def create_sbf_ex(cls, p1: 'GXSBF', p2: str, p3: int, p4: int) -> 'GXWA':
        ret_val = gxapi_cy.WrapWA.create_sbf_ex(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4)
        return GXWA(ret_val)






    def new_line(self) -> None:
        self._wrapper.new_line()
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer