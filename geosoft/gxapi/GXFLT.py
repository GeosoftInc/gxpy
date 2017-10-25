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
class GXFLT:
    """
    GXFLT class.

    The :class:`GXFLT` class allows the application of user-defined convolution filters to data in an OASIS database
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapFLT(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXFLT':
        """
        A null (undefined) instance of :class:`GXFLT`
        
        :returns: A null :class:`GXFLT`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXFLT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXFLT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapFLT.create(GXContext._get_tls_geo(), p1.encode())
        return ret_val





    @classmethod
    def load(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapFLT.load(GXContext._get_tls_geo(), p1.encode())
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer