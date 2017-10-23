### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVOXD:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVOXD(0)

    @classmethod
    def null(cls) -> 'GXVOXD':
        """
        A null (undefined) instance of :class:`GXVOXD`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXVOXD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXVOXD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: 'GXVOX', p2: str, p3: int, p4: float) -> 'GXVOXD':
        ret_val = gxapi_cy.WrapVOXD.create(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4)
        return GXVOXD(ret_val)



    @classmethod
    def create_itr(cls, p1: 'GXVOX', p2: 'GXITR') -> 'GXVOXD':
        ret_val = gxapi_cy.WrapVOXD.create_itr(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        return GXVOXD(ret_val)



    @classmethod
    def create_thematic(cls, p1: 'GXVOX') -> 'GXVOXD':
        ret_val = gxapi_cy.WrapVOXD.create_thematic(GXContext._get_tls_geo(), p1._wrapper)
        return GXVOXD(ret_val)




    def is_thematic(self) -> int:
        ret_val = self._wrapper.is_thematic()
        return ret_val




    def get_thematic_info(self, p2: 'GXTPAT', p3: 'GXVV') -> None:
        self._wrapper.get_thematic_info(p2._wrapper, p3._wrapper)
        




    def set_thematic_selection(self, p2: 'GXVV') -> None:
        self._wrapper.set_thematic_selection(p2._wrapper)
        






    def get_draw_controls(self, p2: int_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value = self._wrapper.get_draw_controls(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value)
        




    def get_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_name(p2.value.encode())
        




    def get_itr(self, p2: 'GXITR') -> None:
        self._wrapper.get_itr(p2._wrapper)
        




    def get_shell_controls(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.get_shell_controls(p2.value, p3.value)
        




    def set_draw_controls(self, p2: int, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float) -> None:
        self._wrapper.set_draw_controls(p2, p3, p4, p5, p6, p7, p8, p9)
        




    def set_itr(self, p2: 'GXITR') -> None:
        self._wrapper.set_itr(p2._wrapper)
        




    def set_shell_controls(self, p2: float, p3: float) -> None:
        self._wrapper.set_shell_controls(p2, p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer