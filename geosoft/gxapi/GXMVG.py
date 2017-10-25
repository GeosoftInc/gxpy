### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXMVIEW import GXMVIEW
### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMVG:
    """
    GXMVG class.

    The :class:`GXMVG` class provides the ability to create view graphs.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMVG(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXMVG':
        """
        A null (undefined) instance of :class:`GXMVG`
        
        :returns: A null :class:`GXMVG`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXMVG` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXMVG`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def axis_x(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None:
        self._wrapper.axis_x(p2, p3, p4, p5, p6, p7)
        




    def axis_y(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None:
        self._wrapper.axis_y(p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def create(cls, p1: 'GXMAP', p2: str, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float) -> 'GXMVG':
        ret_val = gxapi_cy.WrapMVG.create(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6, p7, p8, p9, p10)
        return GXMVG(ret_val)






    def get_mview(self) -> 'GXMVIEW':
        ret_val = self._wrapper.get_mview()
        return GXMVIEW(ret_val)




    def grid(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: int) -> None:
        self._wrapper.grid(p2, p3, p4, p5, p6, p7, p8)
        




    def label_x(self, p2: float, p3: float, p4: float, p5: float, p6: int, p7: int, p8: int) -> None:
        self._wrapper.label_x(p2, p3, p4, p5, p6, p7, p8)
        




    def label_y(self, p2: float, p3: float, p4: float, p5: float, p6: int, p7: int, p8: int) -> None:
        self._wrapper.label_y(p2, p3, p4, p5, p6, p7, p8)
        




    def poly_line_va(self, p2: int, p3: int, p4: 'GXVV', p5: 'GXVA', p6: 'GXVV') -> None:
        self._wrapper.poly_line_va(p2, p3, p4._wrapper, p5._wrapper, p6._wrapper)
        




    def poly_line_vv(self, p2: int, p3: int, p4: 'GXVV', p5: 'GXVV') -> None:
        self._wrapper.poly_line_vv(p2, p3, p4._wrapper, p5._wrapper)
        




    def rescale_x_range(self, p2: int, p3: float, p4: float, p5: float) -> None:
        self._wrapper.rescale_x_range(p2, p3, p4, p5)
        




    def rescale_y_range(self, p2: int, p3: float, p4: float, p5: float) -> None:
        self._wrapper.rescale_y_range(p2, p3, p4, p5)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer