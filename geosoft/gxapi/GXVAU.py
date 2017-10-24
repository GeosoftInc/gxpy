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
class GXVAU:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVAU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXVAU':
        """
        A null (undefined) instance of :class:`GXVAU`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXVAU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXVAU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def prune(cls, p1: 'GXVA', p2: 'GXVV', p3: int) -> None:
        gxapi_cy.WrapVAU.prune(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3)
        



    @classmethod
    def total_vector(cls, p1: 'GXVA', p2: 'GXVA', p3: 'GXVA', p4: 'GXVA') -> None:
        gxapi_cy.WrapVAU.total_vector(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer