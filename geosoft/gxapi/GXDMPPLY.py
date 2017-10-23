### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDMPPLY:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDMPPLY(0)

    @classmethod
    def null(cls) -> 'GXDMPPLY':
        """
        A null (undefined) instance of :class:`GXDMPPLY`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXDMPPLY` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXDMPPLY`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clear(self) -> None:
        self._wrapper.clear()
        




    def copy(self, p2: 'GXDMPPLY') -> None:
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls) -> 'GXDMPPLY':
        ret_val = gxapi_cy.WrapDMPPLY.create(GXContext._get_tls_geo())
        return GXDMPPLY(ret_val)






    def get_azimuth(self, p2: int, p3: float_ref) -> None:
        p3.value = self._wrapper.get_azimuth(p2, p3.value)
        




    def get_extents(self, p2: int, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_extents(p2, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_joins(self, p2: int, p3: 'GXVV') -> None:
        self._wrapper.get_joins(p2, p3._wrapper)
        




    def get_normal_vectors(self, p2: int, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: float_ref) -> None:
        p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value = self._wrapper.get_normal_vectors(p2, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value)
        




    def get_poly(self, p2: int, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV') -> None:
        self._wrapper.get_poly(p2, p3._wrapper, p4._wrapper, p5._wrapper)
        




    def get_swing(self, p2: int, p3: float_ref) -> None:
        p3.value = self._wrapper.get_swing(p2, p3.value)
        




    def get_vertex(self, p2: int, p3: int, p4: float_ref, p5: float_ref, p6: float_ref) -> None:
        p4.value, p5.value, p6.value = self._wrapper.get_vertex(p2, p3, p4.value, p5.value, p6.value)
        




    def num_joins(self) -> int:
        ret_val = self._wrapper.num_joins()
        return ret_val




    def num_polys(self) -> int:
        ret_val = self._wrapper.num_polys()
        return ret_val




    def num_vertices(self, p2: int) -> int:
        ret_val = self._wrapper.num_vertices(p2)
        return ret_val




    def load(self, p2: str) -> None:
        self._wrapper.load(p2.encode())
        




    def move_vertex(self, p2: int, p3: int, p4: float, p5: float, p6: float) -> None:
        self._wrapper.move_vertex(p2, p3, p4, p5, p6)
        




    def project_poly(self, p2: int, p3: float, p4: float, p5: float, p6: float, p7: float, p8: 'GXVV', p9: 'GXVV', p10: 'GXVV') -> None:
        self._wrapper.project_poly(p2, p3, p4, p5, p6, p7, p8._wrapper, p9._wrapper, p10._wrapper)
        




    def re_project_poly(self, p2: int, p3: float, p4: float, p5: float, p6: float, p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: 'GXVV', p11: 'GXVV') -> None:
        self._wrapper.re_project_poly(p2, p3, p4, p5, p6, p7._wrapper, p8._wrapper, p9._wrapper, p10._wrapper, p11._wrapper)
        




    def save(self, p2: str) -> None:
        self._wrapper.save(p2.encode())
        




    def set_poly(self, p2: int, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV') -> None:
        self._wrapper.set_poly(p2, p3._wrapper, p4._wrapper, p5._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer