### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXSURFACEITEM:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSURFACEITEM(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXSURFACEITEM':
        """
        A null (undefined) instance of :class:`GXSURFACEITEM`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXSURFACEITEM` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXSURFACEITEM`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: str, p2: str) -> 'GXSURFACEITEM':
        ret_val = gxapi_cy.WrapSURFACEITEM.create(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return GXSURFACEITEM(ret_val)






    def get_guid(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_guid(p2.value.encode())
        




    def set_properties(self, p2: str, p3: str, p4: str, p5: str, p6: float, p7: str, p8: str, p9: float) -> None:
        self._wrapper.set_properties(p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6, p7.encode(), p8.encode(), p9)
        




    def set_properties_ex(self, p2: str, p3: str, p4: str, p5: str, p6: float, p7: str, p8: str, p9: int, p10: float, p11: float) -> None:
        self._wrapper.set_properties_ex(p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6, p7.encode(), p8.encode(), p9, p10, p11)
        




    def get_properties(self, p2: str_ref, p4: str_ref, p6: str_ref, p8: str_ref, p10: float_ref, p11: str_ref, p13: str_ref, p15: float_ref) -> None:
        p2.value, p4.value, p6.value, p8.value, p10.value, p11.value, p13.value, p15.value = self._wrapper.get_properties(p2.value.encode(), p4.value.encode(), p6.value.encode(), p8.value.encode(), p10.value, p11.value.encode(), p13.value.encode(), p15.value)
        




    def get_properties_ex(self, p2: str_ref, p4: str_ref, p6: str_ref, p8: str_ref, p10: float_ref, p11: str_ref, p13: str_ref, p15: int_ref, p16: float_ref, p17: float_ref) -> None:
        p2.value, p4.value, p6.value, p8.value, p10.value, p11.value, p13.value, p15.value, p16.value, p17.value = self._wrapper.get_properties_ex(p2.value.encode(), p4.value.encode(), p6.value.encode(), p8.value.encode(), p10.value, p11.value.encode(), p13.value.encode(), p15.value, p16.value, p17.value)
        




    def set_default_render_properties(self, p2: int, p3: float, p4: int) -> None:
        self._wrapper.set_default_render_properties(p2, p3, p4)
        




    def get_default_render_properties(self, p2: int_ref, p3: float_ref, p4: int_ref) -> None:
        p2.value, p3.value, p4.value = self._wrapper.get_default_render_properties(p2.value, p3.value, p4.value)
        




    def num_components(self) -> int:
        ret_val = self._wrapper.num_components()
        return ret_val




    def add_mesh(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV') -> int:
        ret_val = self._wrapper.add_mesh(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper)
        return ret_val




    def get_mesh(self, p2: int, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: 'GXVV') -> None:
        self._wrapper.get_mesh(p2, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper)
        




    def get_extents(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_extents(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_mesh_info(self, p2: int, p3: int_ref, p4: int_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_mesh_info(p2, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_info(self, p2: int_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_info(p2.value, p3.value, p4.value, p5.value)
        




    def get_geometry_info(self, p2: int_ref, p3: int_ref) -> None:
        p2.value, p3.value = self._wrapper.get_geometry_info(p2.value, p3.value)
        




    def compute_extended_info(self, p2: int_ref, p3: int_ref, p4: int_ref, p5: int_ref, p6: int_ref, p7: int_ref, p8: int_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value = self._wrapper.compute_extended_info(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer