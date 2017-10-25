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
class GXEXT:
    """
    GXEXT class.

    External (plug-in) image methods.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapEXT(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXEXT':
        """
        A null (undefined) instance of :class:`GXEXT`
        
        :returns: A null :class:`GXEXT`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXEXT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXEXT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def get_info(cls, p1: str, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: 'GXIPJ') -> None:
        p2.value, p3.value, p4.value, p5.value = gxapi_cy.WrapEXT.get_info(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value, p4.value, p5.value, p6._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer