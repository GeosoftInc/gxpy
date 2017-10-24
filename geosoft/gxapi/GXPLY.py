### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXPLY:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPLY(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXPLY':
        """
        A null (undefined) instance of :class:`GXPLY`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXPLY` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXPLY`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_polygon(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.add_polygon(p2._wrapper, p3._wrapper)
        




    def add_polygon_ex(self, p2: 'GXVV', p3: 'GXVV', p4: int) -> None:
        self._wrapper.add_polygon_ex(p2._wrapper, p3._wrapper, p4)
        




    def change_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.change_ipj(p2._wrapper)
        




    def clear(self) -> None:
        self._wrapper.clear()
        




    def copy(self, p2: 'GXPLY') -> None:
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls) -> 'GXPLY':
        ret_val = gxapi_cy.WrapPLY.create(GXContext._get_tls_geo())
        return GXPLY(ret_val)



    @classmethod
    def create_s(cls, p1: 'GXBF') -> 'GXPLY':
        ret_val = gxapi_cy.WrapPLY.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXPLY(ret_val)






    def extent(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = self._wrapper.extent(p2.value, p3.value, p4.value, p5.value)
        




    def get_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.get_ipj(p2._wrapper)
        




    def get_polygon(self, p2: 'GXVV', p3: 'GXVV', p4: int) -> None:
        self._wrapper.get_polygon(p2._wrapper, p3._wrapper, p4)
        




    def get_polygon_ex(self, p2: 'GXVV', p3: 'GXVV', p4: int, p5: int_ref) -> None:
        p5.value = self._wrapper.get_polygon_ex(p2._wrapper, p3._wrapper, p4, p5.value)
        




    def clip_area(self, p2: float, p3: float, p4: float, p5: float) -> int:
        ret_val = self._wrapper.clip_area(p2, p3, p4, p5)
        return ret_val




    def clip_line_int(self, p2: float, p3: float, p4: float, p5: float, p6: 'GXVV', p7: float, p8: int_ref) -> int:
        ret_val, p8.value = self._wrapper.clip_line_int(p2, p3, p4, p5, p6._wrapper, p7, p8.value)
        return ret_val




    def clip_ply(self, p2: 'GXPLY', p3: 'GXPLY') -> int:
        ret_val = self._wrapper.clip_ply(p2._wrapper, p3._wrapper)
        return ret_val




    def get_description(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_description(p2.value.encode())
        




    def num_poly(self) -> int:
        ret_val = self._wrapper.num_poly()
        return ret_val




    def load_table(self, p2: str) -> None:
        self._wrapper.load_table(p2.encode())
        




    def area(self) -> float:
        ret_val = self._wrapper.area()
        return ret_val




    def rectangle(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.rectangle(p2, p3, p4, p5)
        




    def rotate(self, p2: float, p3: float, p4: float) -> None:
        self._wrapper.rotate(p2, p3, p4)
        




    def save_table(self, p2: str) -> None:
        self._wrapper.save_table(p2.encode())
        




    def serial(self, p2: 'GXBF') -> None:
        self._wrapper.serial(p2._wrapper)
        




    def set_description(self, p2: str) -> None:
        self._wrapper.set_description(p2.encode())
        




    def set_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.set_ipj(p2._wrapper)
        




    def thin(self, p2: float) -> None:
        self._wrapper.thin(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer