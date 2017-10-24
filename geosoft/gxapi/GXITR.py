### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXITR:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapITR(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXITR':
        """
        A null (undefined) instance of :class:`GXITR`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXITR` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXITR`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def change_brightness(self, p2: float) -> None:
        self._wrapper.change_brightness(p2)
        




    def color_vv(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.color_vv(p2._wrapper, p3._wrapper)
        




    def copy(self, p2: 'GXITR') -> None:
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls) -> 'GXITR':
        ret_val = gxapi_cy.WrapITR.create(GXContext._get_tls_geo())
        return GXITR(ret_val)



    @classmethod
    def create_file(cls, p1: str) -> 'GXITR':
        ret_val = gxapi_cy.WrapITR.create_file(GXContext._get_tls_geo(), p1.encode())
        return GXITR(ret_val)



    @classmethod
    def create_img(cls, p1: 'GXIMG', p2: str, p3: int, p4: float) -> 'GXITR':
        ret_val = gxapi_cy.WrapITR.create_img(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4)
        return GXITR(ret_val)



    @classmethod
    def create_map(cls, p1: 'GXMAP', p2: str) -> 'GXITR':
        ret_val = gxapi_cy.WrapITR.create_map(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return GXITR(ret_val)



    @classmethod
    def create_s(cls, p1: 'GXBF') -> 'GXITR':
        ret_val = gxapi_cy.WrapITR.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXITR(ret_val)






    def equal_area(self, p2: 'GXST', p3: float) -> None:
        self._wrapper.equal_area(p2._wrapper, p3)
        




    def get_data_limits(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.get_data_limits(p2.value, p3.value)
        




    def get_reg(self) -> 'GXREG':
        ret_val = self._wrapper.get_reg()
        return GXREG(ret_val)




    def get_zone_color(self, p2: int, p3: int_ref) -> None:
        p3.value = self._wrapper.get_zone_color(p2, p3.value)
        




    def color_value(self, p2: float) -> int:
        ret_val = self._wrapper.color_value(p2)
        return ret_val




    def get_size(self) -> int:
        ret_val = self._wrapper.get_size()
        return ret_val




    def get_zone_model_type(self) -> int:
        ret_val = self._wrapper.get_zone_model_type()
        return ret_val




    def linear(self, p2: float, p3: float, p4: float) -> None:
        self._wrapper.linear(p2, p3, p4)
        




    def load_a(self, p2: str) -> None:
        self._wrapper.load_a(p2.encode())
        




    def log_linear(self, p2: float, p3: float, p4: float) -> None:
        self._wrapper.log_linear(p2, p3, p4)
        




    def normal(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.normal(p2, p3, p4, p5)
        




    def power_zone(self, p2: int) -> None:
        self._wrapper.power_zone(p2)
        




    def get_brightness(self) -> float:
        ret_val = self._wrapper.get_brightness()
        return ret_val




    def get_zone_value(self, p2: int) -> float:
        ret_val = self._wrapper.get_zone_value(p2)
        return ret_val




    def save_a(self, p2: str) -> None:
        self._wrapper.save_a(p2.encode())
        




    def save_file(self, p2: str) -> None:
        self._wrapper.save_file(p2.encode())
        




    def serial(self, p2: 'GXBF') -> None:
        self._wrapper.serial(p2._wrapper)
        



    @classmethod
    def set_agg_map(cls, p1: 'GXMAP', p2: str, p3: 'GXITR') -> None:
        gxapi_cy.WrapITR.set_agg_map(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper)
        




    def set_bright_contrast(self, p2: float, p3: float) -> None:
        self._wrapper.set_bright_contrast(p2, p3)
        




    def set_color_model(self, p2: int) -> None:
        self._wrapper.set_color_model(p2)
        




    def set_data_limits(self, p2: float, p3: float) -> None:
        self._wrapper.set_data_limits(p2, p3)
        




    def set_size(self, p2: int) -> None:
        self._wrapper.set_size(p2)
        




    def set_zone_color(self, p2: int, p3: int) -> None:
        self._wrapper.set_zone_color(p2, p3)
        




    def set_zone_value(self, p2: int, p3: float) -> None:
        self._wrapper.set_zone_value(p2, p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer