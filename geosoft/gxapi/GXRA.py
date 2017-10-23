### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXRA:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapRA(0)

    @classmethod
    def null(cls) -> 'GXRA':
        """
        A null (undefined) instance of :class:`GXRA`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXRA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXRA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: str) -> 'GXRA':
        ret_val = gxapi_cy.WrapRA.create(GXContext._get_tls_geo())
        return GXRA(ret_val)



    @classmethod
    def create_sbf(cls, p1: 'GXSBF', p2: str) -> 'GXRA':
        ret_val = gxapi_cy.WrapRA.create_sbf(GXContext._get_tls_geo(), p2.encode())
        return GXRA(ret_val)






    def gets(self, p2: str_ref) -> int:
        ret_val, p2.value = self._wrapper.gets(p2.value.encode())
        return ret_val




    def len(self) -> int:
        ret_val = self._wrapper.len()
        return ret_val




    def line(self) -> int:
        ret_val = self._wrapper.line()
        return ret_val




    def seek(self, p2: int) -> int:
        ret_val = self._wrapper.seek(p2)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer