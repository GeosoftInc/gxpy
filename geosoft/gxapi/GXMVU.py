### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMVU:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMVU(0)

    @classmethod
    def null(cls) -> 'GXMVU':
        """
        A null (undefined) instance of :class:`GXMVU`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXMVU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXMVU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def arrow(cls, p1: 'GXMVIEW', p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: int) -> None:
        gxapi_cy.WrapMVU.arrow(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def arrow_vector_vv(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: float, p7: int, p8: int, p9: int, p10: int, p11: float) -> None:
        gxapi_cy.WrapMVU.arrow_vector_vv(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8, p9, p10, p11)
        



    @classmethod
    def bar_chart(cls, p1: 'GXMVIEW', p2: str, p3: 'GXDB', p4: int, p5: str, p6: str, p7: str, p8: float, p9: str, p10: float, p11: str, p12: float, p13: float, p14: int, p15: int, p16: int, p17: int, p18: int, p19: int, p20: int, p21: float, p22: float, p23: float, p24: float, p25: float, p26: float, p27: float, p28: float) -> None:
        gxapi_cy.WrapMVU.bar_chart(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4, p5.encode(), p6.encode(), p7.encode(), p8, p9.encode(), p10, p11.encode(), p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28)
        



    @classmethod
    def cdi_pixel_plot(cls, p1: 'GXMVIEW', p2: str, p3: 'GXVA', p4: 'GXVA', p5: 'GXVV', p6: 'GXITR') -> None:
        gxapi_cy.WrapMVU.cdi_pixel_plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper)
        



    @classmethod
    def cdi_pixel_plot_3d(cls, p1: 'GXMVIEW', p2: str, p3: 'GXVA', p4: 'GXVA', p5: 'GXVV', p6: 'GXVV', p7: 'GXITR') -> None:
        gxapi_cy.WrapMVU.cdi_pixel_plot_3d(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper)
        



    @classmethod
    def color_bar(cls, p1: 'GXMVIEW', p2: 'GXITR', p3: int, p4: float, p5: float, p6: float, p7: float, p8: float) -> None:
        gxapi_cy.WrapMVU.color_bar(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def color_bar2(cls, p1: 'GXMVIEW', p2: 'GXITR', p3: 'GXITR', p4: int, p5: float, p6: float, p7: float, p8: float, p9: float) -> None:
        gxapi_cy.WrapMVU.color_bar2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def color_bar2_style(cls, p1: 'GXMVIEW', p2: 'GXITR', p3: 'GXITR', p4: int, p5: float, p6: float, p7: float, p8: float, p9: float, p10: int) -> None:
        gxapi_cy.WrapMVU.color_bar2_style(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8, p9, p10)
        



    @classmethod
    def color_bar_hor(cls, p1: 'GXMVIEW', p2: 'GXITR', p3: int, p4: float, p5: float, p6: float, p7: float, p8: float, p9: int) -> None:
        gxapi_cy.WrapMVU.color_bar_hor(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def color_bar_hor2(cls, p1: 'GXMVIEW', p2: 'GXITR', p3: 'GXITR', p4: int, p5: float, p6: float, p7: float, p8: float, p9: float, p10: int) -> None:
        gxapi_cy.WrapMVU.color_bar_hor2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8, p9, p10)
        



    @classmethod
    def color_bar_hor2_style(cls, p1: 'GXMVIEW', p2: 'GXITR', p3: 'GXITR', p4: int, p5: float, p6: float, p7: float, p8: float, p9: float, p10: int, p11: int) -> None:
        gxapi_cy.WrapMVU.color_bar_hor2_style(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8, p9, p10, p11)
        



    @classmethod
    def color_bar_hor_style(cls, p1: 'GXMVIEW', p2: 'GXITR', p3: int, p4: float, p5: float, p6: float, p7: float, p8: float, p9: int, p10: int) -> None:
        gxapi_cy.WrapMVU.color_bar_hor_style(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7, p8, p9, p10)
        



    @classmethod
    def color_bar_style(cls, p1: 'GXMVIEW', p2: 'GXITR', p3: int, p4: float, p5: float, p6: float, p7: float, p8: float, p9: int) -> None:
        gxapi_cy.WrapMVU.color_bar_style(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def color_bar_reg(cls, p1: 'GXMVIEW', p2: 'GXITR', p3: 'GXITR', p4: 'GXREG') -> None:
        gxapi_cy.WrapMVU.color_bar_reg(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def contour(cls, p1: 'GXMVIEW', p2: str, p3: str) -> None:
        gxapi_cy.WrapMVU.contour(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode())
        



    @classmethod
    def contour_ply(cls, p1: 'GXMVIEW', p2: 'GXPLY', p3: str, p4: str) -> None:
        gxapi_cy.WrapMVU.contour_ply(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode(), p4.encode())
        



    @classmethod
    def c_symb_legend(cls, p1: 'GXMVIEW', p2: float, p3: float, p4: float, p5: float, p6: str, p7: str, p8: str) -> None:
        gxapi_cy.WrapMVU.c_symb_legend(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6.encode(), p7.encode(), p8.encode())
        



    @classmethod
    def decay_curve(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: 'GXVA', p5: 'GXVA', p6: int, p7: float, p8: float, p9: int, p10: int, p11: float, p12: float, p13: float, p14: float, p15: float, p16: float, p17: float, p18: float, p19: float, p20: int, p21: str) -> None:
        gxapi_cy.WrapMVU.decay_curve(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21.encode())
        



    @classmethod
    def direction_plot(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: float, p5: float, p6: int) -> None:
        gxapi_cy.WrapMVU.direction_plot(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6)
        



    @classmethod
    def em_forward(cls, p1: 'GXMVIEW', p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: int, p9: float, p10: float, p11: float, p12: float, p13: 'GXVV', p14: 'GXVV', p15: 'GXVV', p16: 'GXVV', p17: int, p18: int) -> None:
        gxapi_cy.WrapMVU.em_forward(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13._wrapper, p14._wrapper, p15._wrapper, p16._wrapper, p17, p18)
        



    @classmethod
    def export_datamine_string(cls, p1: 'GXMVIEW', p2: 'GXLST', p3: str) -> None:
        gxapi_cy.WrapMVU.export_datamine_string(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode())
        



    @classmethod
    def export_dxf_3d(cls, p1: 'GXMVIEW', p2: 'GXLST', p3: 'GXWA') -> None:
        gxapi_cy.WrapMVU.export_dxf_3d(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def export_surpac_str(cls, p1: 'GXMVIEW', p2: 'GXLST', p3: 'GXWA', p4: 'GXWA') -> None:
        gxapi_cy.WrapMVU.export_surpac_str(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def flight_plot(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: str, p5: int, p6: float, p7: int, p8: float, p9: float) -> None:
        gxapi_cy.WrapMVU.flight_plot(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5, p6, p7, p8, p9)
        



    @classmethod
    def gen_areas(cls, p1: 'GXMVIEW', p2: str, p3: 'GXVV', p4: 'GXVV', p5: float) -> None:
        gxapi_cy.WrapMVU.gen_areas(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4._wrapper, p5)
        



    @classmethod
    def get_range_gocad_surface(cls, p1: str, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = gxapi_cy.WrapMVU.get_range_gocad_surface(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        



    @classmethod
    def histogram(cls, p1: 'GXMVIEW', p2: 'GXST', p3: 'GXST', p4: str, p5: str, p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: float, p13: float, p14: float, p15: int, p16: int, p17: int, p18: 'GXST') -> None:
        gxapi_cy.WrapMVU.histogram(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5.encode(), p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18._wrapper)
        



    @classmethod
    def histogram2(cls, p1: 'GXMVIEW', p2: 'GXST', p3: 'GXST', p4: str, p5: str, p6: float, p7: str, p8: float, p9: str, p10: float, p11: float, p12: float, p13: float, p14: float, p15: float, p16: float, p17: float, p18: float, p19: int, p20: int, p21: int, p22: 'GXST', p23: float) -> None:
        gxapi_cy.WrapMVU.histogram2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5.encode(), p6, p7.encode(), p8, p9.encode(), p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22._wrapper, p23)
        



    @classmethod
    def histogram3(cls, p1: 'GXMVIEW', p2: 'GXST', p3: 'GXST', p4: str, p5: str, p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: float, p13: float, p14: float, p15: int, p16: int, p17: int, p18: int, p19: int, p20: 'GXST') -> None:
        gxapi_cy.WrapMVU.histogram3(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5.encode(), p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20._wrapper)
        



    @classmethod
    def histogram4(cls, p1: 'GXMVIEW', p2: 'GXST', p3: 'GXST', p4: str, p5: str, p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: float, p13: float, p14: float, p15: int, p16: int, p17: int, p18: int, p19: int, p20: int, p21: 'GXST') -> None:
        gxapi_cy.WrapMVU.histogram4(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5.encode(), p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21._wrapper)
        



    @classmethod
    def histogram5(cls, p1: 'GXMVIEW', p2: 'GXST', p3: 'GXST', p4: str, p5: str, p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: float, p13: float, p14: float, p15: float, p16: int, p17: int, p18: int, p19: int, p20: int, p21: int, p22: 'GXST', p23: 'GXITR') -> None:
        gxapi_cy.WrapMVU.histogram5(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5.encode(), p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22._wrapper, p23._wrapper)
        



    @classmethod
    def exportable_dxf_3d_groups_lst(cls, p1: 'GXMVIEW', p2: 'GXLST') -> int:
        ret_val = gxapi_cy.WrapMVU.exportable_dxf_3d_groups_lst(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        return ret_val



    @classmethod
    def mapset_test(cls, p1: float, p2: float, p3: float, p4: float, p5: str, p6: int, p7: int, p8: float_ref, p9: float, p10: float, p11: float, p12: float, p13: float, p14: float) -> int:
        ret_val, p8.value = gxapi_cy.WrapMVU.mapset_test(GXContext._get_tls_geo(), p1, p2, p3, p4, p5.encode(), p6, p7, p8.value, p9, p10, p11, p12, p13, p14)
        return ret_val



    @classmethod
    def mapset2_test(cls, p1: float, p2: float, p3: float, p4: float, p5: str, p6: int, p7: int, p8: float_ref, p9: float, p10: float, p11: float, p12: float, p13: float, p14: float, p15: float) -> int:
        ret_val, p8.value = gxapi_cy.WrapMVU.mapset2_test(GXContext._get_tls_geo(), p1, p2, p3, p4, p5.encode(), p6, p7, p8.value, p9, p10, p11, p12, p13, p14, p15)
        return ret_val



    @classmethod
    def import_gocad_surface(cls, p1: 'GXMVIEW', p2: str, p3: int) -> None:
        gxapi_cy.WrapMVU.import_gocad_surface(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3)
        



    @classmethod
    def load_plot(cls, p1: 'GXMAP', p2: str) -> None:
        gxapi_cy.WrapMVU.load_plot(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def map_from_plt(cls, p1: 'GXMAP', p2: str, p3: str, p4: str, p5: float, p6: float) -> None:
        gxapi_cy.WrapMVU.map_from_plt(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode(), p5, p6)
        



    @classmethod
    def map_mdf(cls, p1: 'GXMAP', p2: str, p3: str) -> None:
        gxapi_cy.WrapMVU.map_mdf(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode())
        



    @classmethod
    def mapset(cls, p1: 'GXMAP', p2: str, p3: str, p4: float, p5: float, p6: float, p7: float, p8: str, p9: int, p10: int, p11: float, p12: float, p13: float, p14: float, p15: float, p16: float, p17: float) -> None:
        gxapi_cy.WrapMVU.mapset(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4, p5, p6, p7, p8.encode(), p9, p10, p11, p12, p13, p14, p15, p16, p17)
        



    @classmethod
    def mapset2(cls, p1: 'GXMAP', p2: str, p3: str, p4: float, p5: float, p6: float, p7: float, p8: str, p9: int, p10: int, p11: float, p12: float, p13: float, p14: float, p15: float, p16: float, p17: float, p18: float) -> None:
        gxapi_cy.WrapMVU.mapset2(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4, p5, p6, p7, p8.encode(), p9, p10, p11, p12, p13, p14, p15, p16, p17, p18)
        



    @classmethod
    def mdf(cls, p1: 'GXMAP', p2: str, p3: str, p4: str) -> None:
        gxapi_cy.WrapMVU.mdf(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4.encode())
        



    @classmethod
    def path_plot(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: str, p5: int, p6: float, p7: int, p8: float, p9: float, p10: float) -> None:
        gxapi_cy.WrapMVU.path_plot(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5, p6, p7, p8, p9, p10)
        



    @classmethod
    def path_plot_ex(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: str, p5: int, p6: int, p7: float, p8: int, p9: float, p10: float, p11: float) -> None:
        gxapi_cy.WrapMVU.path_plot_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5, p6, p7, p8, p9, p10, p11)
        



    @classmethod
    def path_plot_ex2(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: str, p5: int, p6: int, p7: float, p8: int, p9: float, p10: float, p11: float, p12: int) -> None:
        gxapi_cy.WrapMVU.path_plot_ex2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5, p6, p7, p8, p9, p10, p11, p12)
        



    @classmethod
    def plot_voxel_surface(cls, p1: 'GXMVIEW', p2: 'GXVOX', p3: float, p4: int, p5: float) -> None:
        gxapi_cy.WrapMVU.plot_voxel_surface(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5)
        



    @classmethod
    def plot_voxel_surface2(cls, p1: 'GXMVIEW', p2: 'GXVOX', p3: float, p4: int, p5: float, p6: float, p7: str) -> None:
        gxapi_cy.WrapMVU.plot_voxel_surface2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7.encode())
        



    @classmethod
    def generate_surface_from_voxel(cls, p1: 'GXMVIEW', p2: 'GXVOX', p3: int, p4: int, p5: float, p6: float, p7: int, p8: float, p9: float, p10: str) -> None:
        gxapi_cy.WrapMVU.generate_surface_from_voxel(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7, p8, p9, p10.encode())
        



    @classmethod
    def post(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: int, p6: int, p7: int, p8: int, p9: int, p10: float) -> None:
        gxapi_cy.WrapMVU.post(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7, p8, p9, p10)
        



    @classmethod
    def post_ex(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: int, p7: float, p8: float, p9: int, p10: int, p11: int, p12: float, p13: float, p14: int, p15: float, p16: int, p17: float, p18: int, p19: float, p20: int) -> None:
        gxapi_cy.WrapMVU.post_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20)
        



    @classmethod
    def probability(cls, p1: 'GXMVIEW', p2: 'GXST', p3: 'GXST', p4: str, p5: str, p6: int, p7: float, p8: float, p9: float, p10: float, p11: float, p12: float, p13: float, p14: float, p15: int, p16: int, p17: int, p18: 'GXITR') -> None:
        gxapi_cy.WrapMVU.probability(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.encode(), p5.encode(), p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18._wrapper)
        



    @classmethod
    def profile_plot(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: float, p6: int, p7: float, p8: float, p9: float, p10: int) -> None:
        gxapi_cy.WrapMVU.profile_plot(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7, p8, p9, p10)
        



    @classmethod
    def profile_plot_ex(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: float, p6: int, p7: float, p8: float, p9: float, p10: int, p11: int, p12: float, p13: int, p14: str, p15: str) -> None:
        gxapi_cy.WrapMVU.profile_plot_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14.encode(), p15.encode())
        



    @classmethod
    def prop_symb_legend(cls, p1: 'GXMVIEW', p2: float, p3: float, p4: float, p5: float, p6: float, p7: int, p8: float, p9: float, p10: str, p11: str) -> None:
        gxapi_cy.WrapMVU.prop_symb_legend(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9, p10.encode(), p11.encode())
        



    @classmethod
    def re_gen_areas(cls, p1: 'GXMVIEW', p2: str) -> None:
        gxapi_cy.WrapMVU.re_gen_areas(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def symb_off(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: float, p6: float) -> None:
        gxapi_cy.WrapMVU.symb_off(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6)
        



    @classmethod
    def text_box(cls, p1: 'GXMVIEW', p2: float, p3: float, p4: float, p5: float, p6: str, p7: float, p8: int) -> None:
        gxapi_cy.WrapMVU.text_box(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6.encode(), p7, p8)
        



    @classmethod
    def tick(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: float, p6: float, p7: float, p8: float) -> None:
        gxapi_cy.WrapMVU.tick(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7, p8)
        



    @classmethod
    def tick_ex(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: float, p6: float, p7: float, p8: float, p9: float) -> None:
        gxapi_cy.WrapMVU.tick_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7, p8, p9)
        



    @classmethod
    def trnd_path(cls, p1: 'GXMVIEW', p2: 'GXVV', p3: 'GXVV', p4: int, p5: float) -> None:
        gxapi_cy.WrapMVU.trnd_path(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer