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
class GXSTK:
    """
    GXSTK class.

    The :class:`GXSTK` class is used for plotting a single data profile in
    an :class:`GXMVIEW`. The :class:`GXMSTK` class (see :class:`GXMSTK`) is used to plot
    multiple :class:`GXSTK` objects to a single map.
    
    Use AddSTK_MSTK fuction to create a :class:`GXSTK` object before
    using functions in this file
    
    SEE :class:`GXMSTK` FILE FOR DETAILED DESCRIPTIONS OF ALL FUNCTION PARAMETERS.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSTK(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXSTK':
        """
        A null (undefined) instance of :class:`GXSTK`
        
        :returns: A null :class:`GXSTK`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXSTK` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXSTK`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def get_trans_parms(self, p2: int_ref, p3: float_ref, p4: 'GXVV', p5: 'GXVV', p6: int_ref, p7: float_ref, p8: 'GXVV', p9: 'GXVV') -> None:
        p2.value, p3.value, p6.value, p7.value = self._wrapper.get_trans_parms(p2.value, p3.value, p4._wrapper, p5._wrapper, p6.value, p7.value, p8._wrapper, p9._wrapper)
        




    def get_axis_format(self, p2: int) -> int:
        ret_val = self._wrapper.get_axis_format(p2)
        return ret_val




    def get_axis_parms(self, p2: int_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: str_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: int_ref, p12: int) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p8.value, p9.value, p10.value, p11.value = self._wrapper.get_axis_parms(p2.value, p3.value, p4.value, p5.value, p6.value.encode(), p8.value, p9.value, p10.value, p11.value, p12)
        




    def get_fid_parms(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: str_ref, p7: float_ref, p8: str_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p7.value, p8.value = self._wrapper.get_fid_parms(p2.value, p3.value, p4.value, p5.value.encode(), p7.value, p8.value.encode())
        




    def get_flag(self, p2: int) -> int:
        ret_val = self._wrapper.get_flag(p2)
        return ret_val




    def get_gen_parms(self, p2: str_ref, p4: str_ref, p6: str_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: float_ref, p12: float_ref, p13: float_ref, p14: float_ref, p15: float_ref) -> None:
        p2.value, p4.value, p6.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value = self._wrapper.get_gen_parms(p2.value.encode(), p4.value.encode(), p6.value.encode(), p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value)
        




    def get_grid_parms(self, p2: int_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: str_ref, p13: int) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value = self._wrapper.get_grid_parms(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value.encode(), p13)
        




    def get_label_parms(self, p2: int_ref, p3: float_ref, p4: int_ref, p5: float_ref, p6: int_ref, p7: float_ref, p8: str_ref, p10: float_ref, p11: str_ref, p13: int_ref, p14: int) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p10.value, p11.value, p13.value = self._wrapper.get_label_parms(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value.encode(), p10.value, p11.value.encode(), p13.value, p14)
        




    def get_profile(self, p2: int_ref, p3: float_ref, p4: float_ref, p5: str_ref, p7: int_ref, p8: int_ref, p9: int_ref, p10: 'GXVV', p11: str_ref, p13: int_ref, p14: str_ref, p16: float_ref, p17: str_ref, p19: int_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p7.value, p8.value, p9.value, p11.value, p13.value, p14.value, p16.value, p17.value, p19.value = self._wrapper.get_profile(p2.value, p3.value, p4.value, p5.value.encode(), p7.value, p8.value, p9.value, p10._wrapper, p11.value.encode(), p13.value, p14.value.encode(), p16.value, p17.value.encode(), p19.value)
        




    def get_profile_ex(self, p2: int_ref, p3: float_ref, p4: float_ref, p5: str_ref, p7: int_ref, p8: int_ref, p9: int_ref, p10: int_ref, p11: 'GXVV', p12: str_ref, p14: int_ref, p15: str_ref, p17: float_ref, p18: str_ref, p20: int_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p7.value, p8.value, p9.value, p10.value, p12.value, p14.value, p15.value, p17.value, p18.value, p20.value = self._wrapper.get_profile_ex(p2.value, p3.value, p4.value, p5.value.encode(), p7.value, p8.value, p9.value, p10.value, p11._wrapper, p12.value.encode(), p14.value, p15.value.encode(), p17.value, p18.value.encode(), p20.value)
        




    def get_symb_parms(self, p2: str_ref, p4: float_ref, p5: str_ref, p7: str_ref, p9: int_ref, p10: int_ref, p11: float_ref, p12: int_ref, p13: 'GXVV', p14: 'GXVV', p15: int_ref, p16: str_ref, p18: float_ref, p19: str_ref) -> None:
        p2.value, p4.value, p5.value, p7.value, p9.value, p10.value, p11.value, p12.value, p15.value, p16.value, p18.value, p19.value = self._wrapper.get_symb_parms(p2.value.encode(), p4.value, p5.value.encode(), p7.value.encode(), p9.value, p10.value, p11.value, p12.value, p13._wrapper, p14._wrapper, p15.value, p16.value.encode(), p18.value, p19.value.encode())
        




    def get_title_parms(self, p2: str_ref, p4: str_ref, p6: int_ref, p7: float_ref, p8: float_ref, p9: int_ref, p10: float_ref, p11: float_ref, p12: str_ref, p14: float_ref, p15: str_ref, p17: int) -> None:
        p2.value, p4.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p14.value, p15.value = self._wrapper.get_title_parms(p2.value.encode(), p4.value.encode(), p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value.encode(), p14.value, p15.value.encode(), p17)
        




    def set_flag(self, p2: int, p3: int) -> None:
        self._wrapper.set_flag(p2, p3)
        




    def set_array_colors(self, p2: 'GXITR') -> None:
        self._wrapper.set_array_colors(p2._wrapper)
        




    def set_axis_format(self, p2: int, p3: int) -> None:
        self._wrapper.set_axis_format(p2, p3)
        




    def set_axis_parms(self, p2: int, p3: float, p4: float, p5: float, p6: str, p7: float, p8: float, p9: float, p10: int, p11: int) -> None:
        self._wrapper.set_axis_parms(p2, p3, p4, p5, p6.encode(), p7, p8, p9, p10, p11)
        




    def set_fid_parms(self, p2: float, p3: float, p4: float, p5: str, p6: float, p7: str) -> None:
        self._wrapper.set_fid_parms(p2, p3, p4, p5.encode(), p6, p7.encode())
        




    def set_gen_parms(self, p2: str, p3: str, p4: str, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: float) -> None:
        self._wrapper.set_gen_parms(p2.encode(), p3.encode(), p4.encode(), p5, p6, p7, p8, p9, p10, p11, p12)
        




    def set_grid_parms(self, p2: int, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: str, p12: int) -> None:
        self._wrapper.set_grid_parms(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11.encode(), p12)
        




    def set_label_parms(self, p2: int, p3: float, p4: int, p5: float, p6: int, p7: float, p8: str, p9: float, p10: str, p11: int, p12: int) -> None:
        self._wrapper.set_label_parms(p2, p3, p4, p5, p6, p7, p8.encode(), p9, p10.encode(), p11, p12)
        




    def set_line_parm(self, p2: int) -> None:
        self._wrapper.set_line_parm(p2)
        




    def set_profile(self, p2: int, p3: float, p4: float, p5: str, p6: int, p7: int, p8: int, p9: 'GXVV', p10: str, p11: int, p12: str, p13: float, p14: str, p15: int) -> None:
        self._wrapper.set_profile(p2, p3, p4, p5.encode(), p6, p7, p8, p9._wrapper, p10.encode(), p11, p12.encode(), p13, p14.encode(), p15)
        




    def set_profile_ex(self, p2: int, p3: float, p4: float, p5: str, p6: int, p7: int, p8: int, p9: int, p10: 'GXVV', p11: str, p12: int, p13: str, p14: float, p15: str, p16: int) -> None:
        self._wrapper.set_profile_ex(p2, p3, p4, p5.encode(), p6, p7, p8, p9, p10._wrapper, p11.encode(), p12, p13.encode(), p14, p15.encode(), p16)
        




    def set_symb_parms(self, p2: str, p3: float, p4: str, p5: str, p6: int, p7: int, p8: float, p9: int, p10: 'GXVV', p11: 'GXVV', p12: int, p13: str, p14: float, p15: str) -> None:
        self._wrapper.set_symb_parms(p2.encode(), p3, p4.encode(), p5.encode(), p6, p7, p8, p9, p10._wrapper, p11._wrapper, p12, p13.encode(), p14, p15.encode())
        




    def set_title_parms(self, p2: str, p3: str, p4: int, p5: float, p6: float, p7: int, p8: float, p9: float, p10: str, p11: float, p12: str, p13: int) -> None:
        self._wrapper.set_title_parms(p2.encode(), p3.encode(), p4, p5, p6, p7, p8, p9, p10.encode(), p11, p12.encode(), p13)
        




    def set_trans_parms(self, p2: int, p3: float, p4: int, p5: int, p6: int, p7: float, p8: int, p9: int) -> None:
        self._wrapper.set_trans_parms(p2, p3, p4, p5, p6, p7, p8, p9)
        




    def set_va_index_start(self, p2: int) -> None:
        self._wrapper.set_va_index_start(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer