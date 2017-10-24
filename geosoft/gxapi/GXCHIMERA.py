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
class GXCHIMERA:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapCHIMERA(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXCHIMERA':
        """
        A null (undefined) instance of :class:`GXCHIMERA`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXCHIMERA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXCHIMERA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def bar_plot(cls, p1: 'GXMVIEW', p2: str, p3: str, p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: int, p9: int, p10: float, p11: float) -> None:
        gxapi_cy.WrapCHIMERA.bar_plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8, p9, p10, p11)
        



    @classmethod
    def categorize_by_value(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV') -> None:
        gxapi_cy.WrapCHIMERA.categorize_by_value(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def categorize_by_value_det_limit(cls, p1: 'GXVV', p2: 'GXVV', p3: float, p4: 'GXVV') -> None:
        gxapi_cy.WrapCHIMERA.categorize_by_value_det_limit(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4._wrapper)
        



    @classmethod
    def clip_to_detect_limit(cls, p1: 'GXVV', p2: float, p3: int) -> None:
        gxapi_cy.WrapCHIMERA.clip_to_detect_limit(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def draw_circle_offset_markers(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: float) -> None:
        gxapi_cy.WrapCHIMERA.draw_circle_offset_markers(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6)
        



    @classmethod
    def draw_rectangle_offset_markers(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: float, p7: float, p8: float) -> None:
        gxapi_cy.WrapCHIMERA.draw_rectangle_offset_markers(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8)
        



    @classmethod
    def duplicate_chem(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: int, p4: float, p5: int, p6: 'GXVV', p7: str, p8: str, p9: float, p10: float, p11: float, p12: float) -> None:
        gxapi_cy.WrapCHIMERA.duplicate_chem(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6._wrapper, p7.encode(), p8.encode(), p9, p10, p11, p12)
        



    @classmethod
    def duplicate_chem_view(cls, p1: 'GXMAP', p2: str, p3: str, p4: 'GXIPJ', p5: 'GXVV', p6: int, p7: float, p8: int, p9: 'GXVV', p10: str, p11: str, p12: 'GXVV', p13: 'GXVV', p14: 'GXVV', p15: 'GXDB', p16: float_ref, p17: float_ref) -> None:
        p16.value, p17.value = gxapi_cy.WrapCHIMERA.duplicate_chem_view(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4._wrapper, p5._wrapper, p6, p7, p8, p9._wrapper, p10.encode(), p11.encode(), p12._wrapper, p13._wrapper, p14._wrapper, p15._wrapper, p16.value, p17.value)
        



    @classmethod
    def get_expression_data_vv(cls, p1: 'GXDB', p2: int, p3: str, p4: str, p5: str, p6: 'GXVV') -> None:
        gxapi_cy.WrapCHIMERA.get_expression_data_vv(GXContext._get_tls_geo(), p1._wrapper, p2, p3.encode(), p4.encode(), p5.encode(), p6._wrapper)
        



    @classmethod
    def get_lithogeochem_data(cls, p1: 'GXDB', p2: 'GXLST', p3: int, p4: 'GXVV', p5: int, p6: 'GXVV', p7: int, p8: 'GXVV', p9: 'GXVV', p10: 'GXVV', p11: 'GXVV', p12: 'GXVV', p13: 'GXVV', p14: 'GXVV') -> None:
        gxapi_cy.WrapCHIMERA.get_lithogeochem_data(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4._wrapper, p5, p6._wrapper, p7, p8._wrapper, p9._wrapper, p10._wrapper, p11._wrapper, p12._wrapper, p13._wrapper, p14._wrapper)
        



    @classmethod
    def get_transform(cls, p1: 'GXDB', p2: str, p3: int, p4: int_ref, p5: float_ref) -> None:
        p4.value, p5.value = gxapi_cy.WrapCHIMERA.get_transform(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4.value, p5.value)
        



    @classmethod
    def is_acquire_chan(cls, p1: str, p2: str_ref, p4: str_ref, p6: float_ref, p7: int_ref) -> int:
        ret_val, p2.value, p4.value, p6.value, p7.value = gxapi_cy.WrapCHIMERA.is_acquire_chan(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4.value.encode(), p6.value, p7.value)
        return ret_val



    @classmethod
    def is_element(cls, p1: str, p2: int) -> int:
        ret_val = gxapi_cy.WrapCHIMERA.is_element(GXContext._get_tls_geo(), p1.encode(), p2)
        return ret_val



    @classmethod
    def launch_histogram(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapCHIMERA.launch_histogram(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def launch_probability(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapCHIMERA.launch_probability(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def launch_scatter(cls, p1: str) -> None:
        gxapi_cy.WrapCHIMERA.launch_scatter(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def launch_triplot(cls, p1: str) -> None:
        gxapi_cy.WrapCHIMERA.launch_triplot(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def mask_chan_lst(cls, p1: 'GXDB', p2: 'GXLST') -> None:
        gxapi_cy.WrapCHIMERA.mask_chan_lst(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def ordered_channel_lst(cls, p1: 'GXDB', p2: 'GXLST') -> None:
        gxapi_cy.WrapCHIMERA.ordered_channel_lst(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def pie_plot(cls, p1: 'GXMVIEW', p2: str, p3: str, p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: int, p9: int, p10: float, p11: float) -> None:
        gxapi_cy.WrapCHIMERA.pie_plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8, p9, p10, p11)
        



    @classmethod
    def pie_plot2(cls, p1: 'GXMVIEW', p2: str, p3: str, p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: int, p9: int, p10: float, p11: float, p12: float) -> None:
        gxapi_cy.WrapCHIMERA.pie_plot2(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8, p9, p10, p11, p12)
        



    @classmethod
    def plot_string_classified_symbols_legend_from_class_file(cls, p1: 'GXMVIEW', p2: str, p3: float, p4: float, p5: float, p6: str, p7: 'GXVV') -> None:
        gxapi_cy.WrapCHIMERA.plot_string_classified_symbols_legend_from_class_file(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6.encode(), p7._wrapper)
        



    @classmethod
    def atomic_weight(cls, p1: str) -> float:
        ret_val = gxapi_cy.WrapCHIMERA.atomic_weight(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def rose_plot(cls, p1: 'GXMVIEW', p2: str, p3: str, p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: int, p9: int, p10: float) -> None:
        gxapi_cy.WrapCHIMERA.rose_plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8, p9, p10)
        



    @classmethod
    def rose_plot2(cls, p1: 'GXMVIEW', p2: str, p3: str, p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: int, p9: int, p10: float, p11: float) -> None:
        gxapi_cy.WrapCHIMERA.rose_plot2(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8, p9, p10, p11)
        



    @classmethod
    def scatter2(cls, p1: 'GXMVIEW', p2: str, p3: float, p4: float, p5: float, p6: float, p7: 'GXVV', p8: 'GXVV', p9: str, p10: 'GXVV', p11: 'GXVV', p12: 'GXVV', p13: int, p14: str, p15: str, p16: str, p17: str, p18: float, p19: float, p20: float, p21: float, p22: float, p23: float, p24: float, p25: float, p26: int, p27: int, p28: int, p29: int, p30: int, p31: int) -> None:
        gxapi_cy.WrapCHIMERA.scatter2(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6, p7._wrapper, p8._wrapper, p9.encode(), p10._wrapper, p11._wrapper, p12._wrapper, p13, p14.encode(), p15.encode(), p16.encode(), p17.encode(), p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31)
        



    @classmethod
    def fixed_symbol_scatter_plot(cls, p1: 'GXMVIEW', p2: str, p3: float, p4: float, p5: float, p6: float, p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: int, p11: str, p12: int, p13: float, p14: float, p15: int, p16: int, p17: 'GXDB', p18: 'GXVV', p19: 'GXVV', p20: int, p21: str, p22: str, p23: str, p24: str, p25: float, p26: float, p27: float, p28: float, p29: int, p30: int, p31: str) -> None:
        gxapi_cy.WrapCHIMERA.fixed_symbol_scatter_plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6, p7._wrapper, p8._wrapper, p9._wrapper, p10, p11.encode(), p12, p13, p14, p15, p16, p17._wrapper, p18._wrapper, p19._wrapper, p20, p21.encode(), p22.encode(), p23.encode(), p24.encode(), p25, p26, p27, p28, p29, p30, p31.encode())
        



    @classmethod
    def zone_coloured_scatter_plot(cls, p1: 'GXMVIEW', p2: str, p3: float, p4: float, p5: float, p6: float, p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: int, p11: 'GXVV', p12: str, p13: str, p14: int, p15: float, p16: float, p17: int, p18: int, p19: int, p20: 'GXDB', p21: 'GXVV', p22: 'GXVV', p23: int, p24: str, p25: str, p26: str, p27: str, p28: float, p29: float, p30: float, p31: float, p32: int, p33: int, p34: str) -> None:
        gxapi_cy.WrapCHIMERA.zone_coloured_scatter_plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6, p7._wrapper, p8._wrapper, p9._wrapper, p10, p11._wrapper, p12.encode(), p13.encode(), p14, p15, p16, p17, p18, p19, p20._wrapper, p21._wrapper, p22._wrapper, p23, p24.encode(), p25.encode(), p26.encode(), p27.encode(), p28, p29, p30, p31, p32, p33, p34.encode())
        



    @classmethod
    def string_classified_scatter_plot(cls, p1: 'GXMVIEW', p2: str, p3: float, p4: float, p5: float, p6: float, p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: int, p11: 'GXVV', p12: str, p13: float, p14: 'GXDB', p15: 'GXVV', p16: 'GXVV', p17: int, p18: str, p19: str, p20: str, p21: str, p22: float, p23: float, p24: float, p25: float, p26: int, p27: int, p28: str) -> None:
        gxapi_cy.WrapCHIMERA.string_classified_scatter_plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6, p7._wrapper, p8._wrapper, p9._wrapper, p10, p11._wrapper, p12.encode(), p13, p14._wrapper, p15._wrapper, p16._wrapper, p17, p18.encode(), p19.encode(), p20.encode(), p21.encode(), p22, p23, p24, p25, p26, p27, p28.encode())
        



    @classmethod
    def set_lithogeochem_data(cls, p1: 'GXDB', p2: 'GXLST', p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: 'GXVV') -> None:
        gxapi_cy.WrapCHIMERA.set_lithogeochem_data(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10._wrapper)
        



    @classmethod
    def stacked_bar_plot(cls, p1: 'GXMVIEW', p2: str, p3: str, p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: int, p9: int, p10: float, p11: float) -> None:
        gxapi_cy.WrapCHIMERA.stacked_bar_plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8, p9, p10, p11)
        



    @classmethod
    def standard(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: int, p4: float, p5: float, p6: float, p7: str, p8: str, p9: float, p10: float, p11: float, p12: float) -> None:
        gxapi_cy.WrapCHIMERA.standard(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7.encode(), p8.encode(), p9, p10, p11, p12)
        



    @classmethod
    def standard_view(cls, p1: 'GXMAP', p2: str, p3: str, p4: 'GXIPJ', p5: 'GXVV', p6: int, p7: float, p8: float, p9: float, p10: str, p11: str, p12: float, p13: 'GXVV', p14: 'GXVV', p15: 'GXVV', p16: 'GXDB', p17: float_ref, p18: float_ref) -> None:
        p17.value, p18.value = gxapi_cy.WrapCHIMERA.standard_view(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4._wrapper, p5._wrapper, p6, p7, p8, p9, p10.encode(), p11.encode(), p12, p13._wrapper, p14._wrapper, p15._wrapper, p16._wrapper, p17.value, p18.value)
        



    @classmethod
    def tri_plot2(cls, p1: 'GXMVIEW', p2: str, p3: float, p4: float, p5: float, p6: float, p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: 'GXVV', p11: str, p12: 'GXVV', p13: 'GXVV', p14: 'GXVV', p15: str, p16: str, p17: str, p18: float, p19: float, p20: float, p21: float, p22: float, p23: float, p24: int, p25: int, p26: int, p27: int, p28: int, p29: int, p30: int, p31: float, p32: float) -> None:
        gxapi_cy.WrapCHIMERA.tri_plot2(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6, p7._wrapper, p8._wrapper, p9._wrapper, p10._wrapper, p11.encode(), p12._wrapper, p13._wrapper, p14._wrapper, p15.encode(), p16.encode(), p17.encode(), p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32)
        



    @classmethod
    def fixed_symbol_tri_plot(cls, p1: 'GXMVIEW', p2: str, p3: float, p4: float, p5: float, p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: int, p11: str, p12: int, p13: float, p14: float, p15: int, p16: int, p17: 'GXDB', p18: 'GXVV', p19: 'GXVV', p20: str, p21: str, p22: str, p23: int, p24: float, p25: float, p26: str) -> None:
        gxapi_cy.WrapCHIMERA.fixed_symbol_tri_plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10, p11.encode(), p12, p13, p14, p15, p16, p17._wrapper, p18._wrapper, p19._wrapper, p20.encode(), p21.encode(), p22.encode(), p23, p24, p25, p26.encode())
        



    @classmethod
    def zone_coloured_tri_plot(cls, p1: 'GXMVIEW', p2: str, p3: float, p4: float, p5: float, p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: int, p11: 'GXVV', p12: str, p13: str, p14: int, p15: float, p16: float, p17: int, p18: int, p19: int, p20: 'GXDB', p21: 'GXVV', p22: 'GXVV', p23: str, p24: str, p25: str, p26: int, p27: float, p28: float, p29: str) -> None:
        gxapi_cy.WrapCHIMERA.zone_coloured_tri_plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10, p11._wrapper, p12.encode(), p13.encode(), p14, p15, p16, p17, p18, p19, p20._wrapper, p21._wrapper, p22._wrapper, p23.encode(), p24.encode(), p25.encode(), p26, p27, p28, p29.encode())
        



    @classmethod
    def string_classified_tri_plot(cls, p1: 'GXMVIEW', p2: str, p3: float, p4: float, p5: float, p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: int, p11: 'GXVV', p12: str, p13: float, p14: 'GXDB', p15: 'GXVV', p16: 'GXVV', p17: str, p18: str, p19: str, p20: int, p21: float, p22: float, p23: str) -> None:
        gxapi_cy.WrapCHIMERA.string_classified_tri_plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10, p11._wrapper, p12.encode(), p13, p14._wrapper, p15._wrapper, p16._wrapper, p17.encode(), p18.encode(), p19.encode(), p20, p21, p22, p23.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer