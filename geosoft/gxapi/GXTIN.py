### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXTIN:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapTIN(0)

    @classmethod
    def null(cls) -> 'GXTIN':
        """
        A null (undefined) instance of :class:`GXTIN`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXTIN` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXTIN`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def copy(self, p2: 'GXTIN') -> None:
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV') -> 'GXTIN':
        ret_val = gxapi_cy.WrapTIN.create(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        return GXTIN(ret_val)



    @classmethod
    def create_s(cls, p1: 'GXBF') -> 'GXTIN':
        ret_val = gxapi_cy.WrapTIN.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXTIN(ret_val)





    @classmethod
    def export_xml(cls, p1: str, p2: int_ref, p3: str) -> None:
        p2.value = gxapi_cy.WrapTIN.export_xml(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.encode())
        




    def get_convex_hull(self, p2: 'GXPLY') -> None:
        self._wrapper.get_convex_hull(p2._wrapper)
        




    def get_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.get_ipj(p2._wrapper)
        




    def get_joins(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.get_joins(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def get_mesh(self, p2: 'GXVV') -> None:
        self._wrapper.get_mesh(p2._wrapper)
        




    def get_nodes(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.get_nodes(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def get_triangles(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.get_triangles(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def get_triangle(self, p2: int, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref) -> None:
        p3.value, p4.value, p5.value, p6.value, p7.value, p8.value = self._wrapper.get_triangle(p2, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value)
        




    def get_voronoi_edges(self, p2: 'GXVV') -> None:
        self._wrapper.get_voronoi_edges(p2._wrapper)
        




    def is_z_valued(self) -> int:
        ret_val = self._wrapper.is_z_valued()
        return ret_val




    def locate_triangle(self, p2: int, p3: float, p4: float) -> int:
        ret_val = self._wrapper.locate_triangle(p2, p3, p4)
        return ret_val




    def nodes(self) -> int:
        ret_val = self._wrapper.nodes()
        return ret_val




    def interp_vv(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.interp_vv(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def triangles(self) -> int:
        ret_val = self._wrapper.triangles()
        return ret_val




    def linear_interp_vv(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.linear_interp_vv(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def nearest_vv(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.nearest_vv(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def range_xy(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = self._wrapper.range_xy(p2.value, p3.value, p4.value, p5.value)
        




    def serial(self, p2: 'GXBF') -> None:
        self._wrapper.serial(p2._wrapper)
        




    def set_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.set_ipj(p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer