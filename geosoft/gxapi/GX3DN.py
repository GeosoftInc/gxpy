### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GX3DN:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.Wrap3DN(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GX3DN':
        """
        A null (undefined) instance of :class:`GX3DN`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GX3DN` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GX3DN`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def copy(self, p2: 'GX3DN') -> None:
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls) -> 'GX3DN':
        ret_val = gxapi_cy.Wrap3DN.create(GXContext._get_tls_geo())
        return GX3DN(ret_val)






    def get_point_of_view(self, p2: float_ref, p3: float_ref, p4: float_ref) -> None:
        p2.value, p3.value, p4.value = self._wrapper.get_point_of_view(p2.value, p3.value, p4.value)
        




    def get_scale(self, p2: float_ref, p3: float_ref, p4: float_ref) -> None:
        p2.value, p3.value, p4.value = self._wrapper.get_scale(p2.value, p3.value, p4.value)
        




    def get_axis_color(self) -> int:
        ret_val = self._wrapper.get_axis_color()
        return ret_val




    def get_axis_font(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_axis_font(p2.value.encode())
        




    def get_background_color(self) -> int:
        ret_val = self._wrapper.get_background_color()
        return ret_val




    def get_render_controls(self, p2: int_ref, p3: int_ref, p4: str_ref, p6: str_ref, p8: str_ref) -> None:
        p2.value, p3.value, p4.value, p6.value, p8.value = self._wrapper.get_render_controls(p2.value, p3.value, p4.value.encode(), p6.value.encode(), p8.value.encode())
        




    def get_shading(self) -> int:
        ret_val = self._wrapper.get_shading()
        return ret_val




    def set_axis_color(self, p2: int) -> None:
        self._wrapper.set_axis_color(p2)
        




    def set_axis_font(self, p2: str) -> None:
        self._wrapper.set_axis_font(p2.encode())
        




    def set_background_color(self, p2: int) -> None:
        self._wrapper.set_background_color(p2)
        




    def set_point_of_view(self, p2: float, p3: float, p4: float) -> None:
        self._wrapper.set_point_of_view(p2, p3, p4)
        




    def set_render_controls(self, p2: int, p3: int, p4: str, p5: str, p6: str) -> None:
        self._wrapper.set_render_controls(p2, p3, p4.encode(), p5.encode(), p6.encode())
        




    def set_scale(self, p2: float, p3: float, p4: float) -> None:
        self._wrapper.set_scale(p2, p3, p4)
        




    def set_shading(self, p2: int) -> None:
        self._wrapper.set_shading(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
    def test(self):
        print("test")
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer