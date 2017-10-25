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
class GXARCSYS:
    """
    GXARCSYS class.

    This library is not a class. It contains various general
    system utilities used by the Geosoft extensions for ArcGIS.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapARCSYS(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXARCSYS':
        """
        A null (undefined) instance of :class:`GXARCSYS`
        
        :returns: A null :class:`GXARCSYS`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXARCSYS` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXARCSYS`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def get_browse_loc(cls, p1: str_ref) -> None:
        p1.value = gxapi_cy.WrapARCSYS.get_browse_loc(GXContext._get_tls_geo(), p1.value.encode())
        



    @classmethod
    def get_current_doc(cls, p1: str_ref) -> None:
        p1.value = gxapi_cy.WrapARCSYS.get_current_doc(GXContext._get_tls_geo(), p1.value.encode())
        



    @classmethod
    def set_browse_loc(cls, p1: str) -> None:
        gxapi_cy.WrapARCSYS.set_browse_loc(GXContext._get_tls_geo(), p1.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer