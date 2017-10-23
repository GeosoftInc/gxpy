### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXPJ:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPJ(0)

    @classmethod
    def null(cls) -> 'GXPJ':
        """
        A null (undefined) instance of :class:`GXPJ`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXPJ` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXPJ`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clip_ply(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: 'GXPLY') -> None:
        self._wrapper.clip_ply(p2, p3, p4, p5, p6, p7._wrapper)
        




    def convert_vv(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.convert_vv(p2._wrapper, p3._wrapper)
        




    def convert_vv3(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.convert_vv3(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def convert_xy(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.convert_xy(p2.value, p3.value)
        




    def convert_xy_from_xyz(self, p2: float_ref, p3: float_ref, p4: float) -> None:
        p2.value, p3.value = self._wrapper.convert_xy_from_xyz(p2.value, p3.value, p4)
        




    def convert_xyz(self, p2: float_ref, p3: float_ref, p4: float_ref) -> None:
        p2.value, p3.value, p4.value = self._wrapper.convert_xyz(p2.value, p3.value, p4.value)
        



    @classmethod
    def create(cls, p1: str, p2: str) -> 'GXPJ':
        ret_val = gxapi_cy.WrapPJ.create(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return GXPJ(ret_val)



    @classmethod
    def create_ipj(cls, p1: 'GXIPJ', p2: 'GXIPJ') -> 'GXPJ':
        ret_val = gxapi_cy.WrapPJ.create_ipj(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        return GXPJ(ret_val)



    @classmethod
    def create_rectified(cls, p1: float, p2: float, p3: float, p4: float, p5: float, p6: float, p7: int) -> 'GXPJ':
        ret_val = gxapi_cy.WrapPJ.create_rectified(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6, p7)
        return GXPJ(ret_val)






    def elevation(self) -> int:
        ret_val = self._wrapper.elevation()
        return ret_val




    def is_input_ll(self) -> int:
        ret_val = self._wrapper.is_input_ll()
        return ret_val




    def is_output_ll(self) -> int:
        ret_val = self._wrapper.is_output_ll()
        return ret_val




    def project_bounding_rectangle(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = self._wrapper.project_bounding_rectangle(p2.value, p3.value, p4.value, p5.value)
        




    def project_bounding_rectangle2(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float) -> None:
        p2.value, p3.value, p4.value, p5.value = self._wrapper.project_bounding_rectangle2(p2.value, p3.value, p4.value, p5.value, p6)
        




    def project_bounding_rectangle_res(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value = self._wrapper.project_bounding_rectangle_res(p2.value, p3.value, p4.value, p5.value, p6.value)
        




    def project_bounding_rectangle_res2(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value = self._wrapper.project_bounding_rectangle_res2(p2.value, p3.value, p4.value, p5.value, p6.value, p7)
        




    def project_limited_bounding_rectangle(self, p2: float, p3: float, p4: float, p5: float, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref) -> None:
        p6.value, p7.value, p8.value, p9.value = self._wrapper.project_limited_bounding_rectangle(p2, p3, p4, p5, p6.value, p7.value, p8.value, p9.value)
        




    def setup_ldt(self) -> None:
        self._wrapper.setup_ldt()
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer