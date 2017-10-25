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
class GXPDF3D:
    """
    GXPDF3D class.

    The :class:`GXPDF3D` class provides the ability to create 3D PDFs.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPDF3D(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXPDF3D':
        """
        A null (undefined) instance of :class:`GXPDF3D`
        
        :returns: A null :class:`GXPDF3D`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXPDF3D` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXPDF3D`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def render(cls, p1: 'GXMVIEW', p2: str, p3: int, p4: int) -> None:
        gxapi_cy.WrapPDF3D.render(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4)
        



    @classmethod
    def render_to_page(cls, p1: 'GXMVIEW', p2: str, p3: int, p4: int, p5: int) -> None:
        gxapi_cy.WrapPDF3D.render_to_page(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5)
        



    @classmethod
    def export2_d(cls, p1: str, p2: str, p3: int, p4: int, p5: int) -> None:
        gxapi_cy.WrapPDF3D.export2_d(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4, p5)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer