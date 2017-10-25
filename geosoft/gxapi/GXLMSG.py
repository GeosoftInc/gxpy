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
class GXLMSG:
    """
    GXLMSG class.

    Message class methods.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapLMSG(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXLMSG':
        """
        A null (undefined) instance of :class:`GXLMSG`
        
        :returns: A null :class:`GXLMSG`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXLMSG` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXLMSG`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def goto_point(cls, p1: float, p2: float, p3: float, p4: 'GXIPJ') -> None:
        gxapi_cy.WrapLMSG.goto_point(GXContext._get_tls_geo(), p1, p2, p3, p4._wrapper)
        



    @classmethod
    def view_area(cls, p1: float, p2: float, p3: float, p4: float, p5: 'GXIPJ') -> None:
        gxapi_cy.WrapLMSG.view_area(GXContext._get_tls_geo(), p1, p2, p3, p4, p5._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer