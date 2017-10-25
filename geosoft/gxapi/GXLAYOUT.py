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
class GXLAYOUT:
    """
    GXLAYOUT class.

    Layout class for generic relative layout calculation
    
    The relative layout algorithm allows a logical organization of layout rectangles.
    You can set constraints with English-like semantics. For example:
    
    "Set the left side of rectangle 1 equal to the right side of rectangle 2 plus 10 pixels."
    "Set the bottom of rectangle 1 to 25 percent of the height of rectangle 2."
    "Move node 1 such that its bottom is equal to the top of rectangle 2 minus 10 pixels."
    
    The last constraint set would enjoy priority over any others as it would be
    the last one that would influence the rectangle calculations. See the notes for iSetConstraint
    for more details.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapLAYOUT(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXLAYOUT':
        """
        A null (undefined) instance of :class:`GXLAYOUT`
        
        :returns: A null :class:`GXLAYOUT`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXLAYOUT` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXLAYOUT`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def calculate_rects(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = self._wrapper.calculate_rects(p2.value, p3.value, p4.value, p5.value)
        




    def clear_all(self) -> None:
        self._wrapper.clear_all()
        




    def clear_constraints(self) -> None:
        self._wrapper.clear_constraints()
        



    @classmethod
    def create(cls, p1: int, p2: str) -> 'GXLAYOUT':
        ret_val = gxapi_cy.WrapLAYOUT.create(GXContext._get_tls_geo(), p1, p2.encode())
        return GXLAYOUT(ret_val)






    def get_rectangle(self, p2: int, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref) -> None:
        p3.value, p4.value, p5.value, p6.value = self._wrapper.get_rectangle(p2, p3.value, p4.value, p5.value, p6.value)
        




    def get_rect_name(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_rect_name(p2, p3.value.encode())
        




    def add_constraint(self, p2: int, p3: int, p4: int, p5: int, p6: float, p7: float) -> int:
        ret_val = self._wrapper.add_constraint(p2, p3, p4, p5, p6, p7)
        return ret_val




    def add_rectangle(self, p2: float, p3: float, p4: float, p5: float) -> int:
        ret_val = self._wrapper.add_rectangle(p2, p3, p4, p5)
        return ret_val




    def num_rectangles(self) -> int:
        ret_val = self._wrapper.num_rectangles()
        return ret_val




    def set_rectangle(self, p2: int, p3: float, p4: float, p5: float, p6: float) -> None:
        self._wrapper.set_rectangle(p2, p3, p4, p5, p6)
        




    def set_rectangle_name(self, p2: int, p3: str) -> None:
        self._wrapper.set_rectangle_name(p2, p3.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer