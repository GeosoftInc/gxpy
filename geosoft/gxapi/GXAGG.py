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
class GXAGG:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapAGG(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXAGG':
        """
        A null (undefined) instance of :class:`GXAGG`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXAGG` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXAGG`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def set_model(self, p2: int) -> None:
        self._wrapper.set_model(p2)
        




    def change_brightness(self, p2: float) -> None:
        self._wrapper.change_brightness(p2)
        



    @classmethod
    def create(cls) -> 'GXAGG':
        ret_val = gxapi_cy.WrapAGG.create(GXContext._get_tls_geo())
        return GXAGG(ret_val)



    @classmethod
    def create_map(cls, p1: 'GXMAP', p2: str) -> 'GXAGG':
        ret_val = gxapi_cy.WrapAGG.create_map(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return GXAGG(ret_val)






    def get_layer_itr(self, p2: int, p3: 'GXITR') -> None:
        self._wrapper.get_layer_itr(p2, p3._wrapper)
        




    def list_img(self, p2: 'GXVV') -> int:
        ret_val = self._wrapper.list_img(p2._wrapper)
        return ret_val




    def num_layers(self) -> int:
        ret_val = self._wrapper.num_layers()
        return ret_val




    def layer_img(self, p2: str, p3: int, p4: str, p5: float) -> None:
        self._wrapper.layer_img(p2.encode(), p3, p4.encode(), p5)
        




    def layer_img_ex(self, p2: str, p3: int, p4: str, p5: float, p6: float, p7: float) -> None:
        self._wrapper.layer_img_ex(p2.encode(), p3, p4.encode(), p5, p6, p7)
        




    def layer_shade_img(self, p2: str, p3: str, p4: float, p5: float, p6: float_ref) -> None:
        p6.value = self._wrapper.layer_shade_img(p2.encode(), p3.encode(), p4, p5, p6.value)
        




    def get_brightness(self) -> float:
        ret_val = self._wrapper.get_brightness()
        return ret_val




    def set_layer_itr(self, p2: int, p3: 'GXITR') -> None:
        self._wrapper.set_layer_itr(p2, p3._wrapper)
        




    def set_render_method(self, p2: int) -> None:
        self._wrapper.set_render_method(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer