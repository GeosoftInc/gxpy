### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXIMG import GXIMG
### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXIMU:
    """
    GXIMU class.

    Not a class. This is a catch-all group of functions working
    on :class:`GXIMG` objects (see :class:`GXIMG`). Grid operations include masking,
    trending, windowing, expanding and grid stitching.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapIMU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXIMU':
        """
        A null (undefined) instance of :class:`GXIMU`
        
        :returns: A null :class:`GXIMU`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXIMU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXIMU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def agg_to_geo_color(cls, p1: 'GXAGG', p2: str, p3: 'GXIPJ', p4: float) -> None:
        gxapi_cy.WrapIMU.agg_to_geo_color(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4)
        



    @classmethod
    def crc(cls, p1: 'GXIMG', p2: int) -> int:
        ret_val = gxapi_cy.WrapIMU.crc(GXContext._get_tls_geo(), p1._wrapper, p2)
        return ret_val



    @classmethod
    def crc_grid(cls, p1: str, p2: int) -> int:
        ret_val = gxapi_cy.WrapIMU.crc_grid(GXContext._get_tls_geo(), p1.encode(), p2)
        return ret_val



    @classmethod
    def crc_grid_inexact(cls, p1: str, p2: int, p3: int, p4: int) -> int:
        ret_val = gxapi_cy.WrapIMU.crc_grid_inexact(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4)
        return ret_val



    @classmethod
    def crc_inexact(cls, p1: 'GXIMG', p2: int, p3: int, p4: int) -> int:
        ret_val = gxapi_cy.WrapIMU.crc_inexact(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        return ret_val



    @classmethod
    def export_grid_without_data_section_xml(cls, p1: str, p2: int_ref, p3: str) -> None:
        p2.value = gxapi_cy.WrapIMU.export_grid_without_data_section_xml(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.encode())
        



    @classmethod
    def export_grid_xml(cls, p1: str, p2: int_ref, p3: str) -> None:
        p2.value = gxapi_cy.WrapIMU.export_grid_xml(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.encode())
        



    @classmethod
    def export_raw_xml(cls, p1: 'GXIMG', p2: int_ref, p3: str) -> None:
        p2.value = gxapi_cy.WrapIMU.export_raw_xml(GXContext._get_tls_geo(), p1._wrapper, p2.value, p3.encode())
        



    @classmethod
    def export_xml(cls, p1: 'GXIMG', p2: int_ref, p3: str) -> None:
        p2.value = gxapi_cy.WrapIMU.export_xml(GXContext._get_tls_geo(), p1._wrapper, p2.value, p3.encode())
        



    @classmethod
    def get_zvv(cls, p1: 'GXIMG', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        gxapi_cy.WrapIMU.get_zvv(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def get_z_peaks_vv(cls, p1: 'GXIMG', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        gxapi_cy.WrapIMU.get_z_peaks_vv(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def grid_add(cls, p1: 'GXIMG', p2: float, p3: 'GXIMG', p4: float, p5: 'GXIMG') -> None:
        gxapi_cy.WrapIMU.grid_add(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper, p4, p5._wrapper)
        



    @classmethod
    def grid_agc(cls, p1: 'GXIMG', p2: 'GXIMG', p3: int, p4: float, p5: int) -> None:
        gxapi_cy.WrapIMU.grid_agc(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5)
        



    @classmethod
    def grid_bool(cls, p1: 'GXIMG', p2: 'GXIMG', p3: str, p4: int, p5: int, p6: int) -> None:
        gxapi_cy.WrapIMU.grid_bool(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode(), p4, p5, p6)
        



    @classmethod
    def grid_edge(cls, p1: str, p2: 'GXVV', p3: 'GXVV') -> None:
        gxapi_cy.WrapIMU.grid_edge(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3._wrapper)
        



    @classmethod
    def grid_edge_ply(cls, p1: 'GXIMG', p2: 'GXPLY', p3: int) -> None:
        gxapi_cy.WrapIMU.grid_edge_ply(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3)
        



    @classmethod
    def grid_expand(cls, p1: 'GXIMG', p2: str, p3: float, p4: int, p5: int, p6: int) -> None:
        gxapi_cy.WrapIMU.grid_expand(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6)
        



    @classmethod
    def grid_exp_fill(cls, p1: str, p2: str, p3: float, p4: int) -> None:
        gxapi_cy.WrapIMU.grid_exp_fill(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4)
        



    @classmethod
    def grid_fill(cls, p1: 'GXIMG', p2: 'GXIMG', p3: int, p4: int, p5: int, p6: int, p7: float, p8: float, p9: float, p10: int, p11: int) -> None:
        gxapi_cy.WrapIMU.grid_fill(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7, p8, p9, p10, p11)
        



    @classmethod
    def grid_filt(cls, p1: 'GXIMG', p2: 'GXIMG', p3: int, p4: float, p5: int, p6: int, p7: int, p8: str, p9: 'GXVV') -> None:
        gxapi_cy.WrapIMU.grid_filt(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7, p8.encode(), p9._wrapper)
        



    @classmethod
    def grid_head(cls, p1: str, p2: float, p3: float, p4: float, p5: float, p6: float) -> None:
        gxapi_cy.WrapIMU.grid_head(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6)
        



    @classmethod
    def grid_in_fill(cls, p1: 'GXIMG', p2: str, p3: int, p4: int) -> None:
        gxapi_cy.WrapIMU.grid_in_fill(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4)
        



    @classmethod
    def grid_mask(cls, p1: str, p2: str, p3: 'GXPLY', p4: int) -> None:
        gxapi_cy.WrapIMU.grid_mask(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper, p4)
        



    @classmethod
    def grid_peak(cls, p1: str, p2: int, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV') -> None:
        gxapi_cy.WrapIMU.grid_peak(GXContext._get_tls_geo(), p1.encode(), p2, p3._wrapper, p4._wrapper, p5._wrapper)
        



    @classmethod
    def grid_ply(cls, p1: 'GXIMG', p2: 'GXPLY', p3: int) -> None:
        gxapi_cy.WrapIMU.grid_ply(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3)
        



    @classmethod
    def grid_ply_ex(cls, p1: 'GXIMG', p2: 'GXPLY', p3: int, p4: int) -> None:
        gxapi_cy.WrapIMU.grid_ply_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4)
        



    @classmethod
    def grid_reproject_and_window(cls, p1: str, p2: str, p3: 'GXIPJ', p4: float, p5: float, p6: float, p7: float) -> None:
        gxapi_cy.WrapIMU.grid_reproject_and_window(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper, p4, p5, p6, p7)
        



    @classmethod
    def grid_resample(cls, p1: str, p2: str, p3: float, p4: float, p5: float, p6: float, p7: int, p8: int) -> None:
        gxapi_cy.WrapIMU.grid_resample(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def grid_resize(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapIMU.grid_resize(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def grid_shad(cls, p1: str, p2: str, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p3.value, p4.value, p5.value = gxapi_cy.WrapIMU.grid_shad(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value, p4.value, p5.value)
        



    @classmethod
    def grid_st(cls, p1: str, p2: 'GXST') -> None:
        gxapi_cy.WrapIMU.grid_st(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        



    @classmethod
    def grid_stat(cls, p1: str, p2: int_ref, p3: int_ref, p4: int_ref, p5: float_ref, p6: float_ref, p7: int_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: float_ref, p12: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value = gxapi_cy.WrapIMU.grid_stat(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value)
        



    @classmethod
    def grid_stat_comp(cls, p1: str, p2: int_ref, p3: int_ref, p4: int_ref, p5: float_ref, p6: float_ref, p7: int_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: float_ref, p12: float_ref, p13: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value = gxapi_cy.WrapIMU.grid_stat_comp(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value)
        



    @classmethod
    def grid_stat_ext(cls, p1: str, p2: int, p3: int_ref, p4: int_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref) -> None:
        p3.value, p4.value, p5.value, p6.value, p7.value, p8.value = gxapi_cy.WrapIMU.grid_stat_ext(GXContext._get_tls_geo(), p1.encode(), p2, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value)
        



    @classmethod
    def grid_stat_trend(cls, p1: str, p2: int_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = gxapi_cy.WrapIMU.grid_stat_trend(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value, p4.value, p5.value)
        



    @classmethod
    def grid_stat_trend_ext(cls, p1: str, p2: int_ref, p3: int_ref, p4: float_ref, p5: float_ref, p6: 'GXVM') -> None:
        p2.value, p3.value, p4.value, p5.value = gxapi_cy.WrapIMU.grid_stat_trend_ext(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value, p4.value, p5.value, p6._wrapper)
        



    @classmethod
    def slope_standard_deviation(cls, p1: 'GXIMG') -> float:
        ret_val = gxapi_cy.WrapIMU.slope_standard_deviation(GXContext._get_tls_geo(), p1._wrapper)
        return ret_val



    @classmethod
    def grid_stitch(cls, p1: str, p2: str, p3: str, p4: int, p5: int, p6: int, p7: int, p8: float, p9: int, p10: int, p11: 'GXPLY', p12: float, p13: int) -> None:
        gxapi_cy.WrapIMU.grid_stitch(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4, p5, p6, p7, p8, p9, p10, p11._wrapper, p12, p13)
        



    @classmethod
    def grid_stitch_ctl(cls, p1: str) -> None:
        gxapi_cy.WrapIMU.grid_stitch_ctl(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def grid_tiff(cls, p1: str, p2: str, p3: str, p4: int, p5: int, p6: int, p7: float, p8: int, p9: float) -> None:
        gxapi_cy.WrapIMU.grid_tiff(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def grid_trnd(cls, p1: 'GXIMG', p2: 'GXIMG', p3: int, p4: int, p5: int, p6: 'GXVM', p7: int) -> None:
        gxapi_cy.WrapIMU.grid_trnd(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6._wrapper, p7)
        



    @classmethod
    def grid_trns(cls, p1: str, p2: int) -> None:
        gxapi_cy.WrapIMU.grid_trns(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def grid_vd(cls, p1: 'GXIMG', p2: 'GXIMG') -> None:
        gxapi_cy.WrapIMU.grid_vd(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def grid_vol(cls, p1: 'GXIMG', p2: float, p3: float, p4: float_ref, p5: float_ref, p6: float_ref) -> None:
        p4.value, p5.value, p6.value = gxapi_cy.WrapIMU.grid_vol(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4.value, p5.value, p6.value)
        



    @classmethod
    def grid_wind(cls, p1: 'GXIMG', p2: str, p3: int, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: int, p12: int, p13: str) -> None:
        gxapi_cy.WrapIMU.grid_wind(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13.encode())
        



    @classmethod
    def grid_wind2(cls, p1: 'GXIMG', p2: str, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: int) -> None:
        gxapi_cy.WrapIMU.grid_wind2(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def grid_xyz(cls, p1: 'GXIMG', p2: str, p3: int, p4: int, p5: int, p6: int) -> None:
        gxapi_cy.WrapIMU.grid_xyz(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6)
        



    @classmethod
    def grid_type(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapIMU.grid_type(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def make_mi_tab_file(cls, p1: str) -> None:
        gxapi_cy.WrapIMU.make_mi_tab_file(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def make_mi_tabfrom_grid(cls, p1: str) -> None:
        gxapi_cy.WrapIMU.make_mi_tabfrom_grid(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def make_mi_tabfrom_map(cls, p1: str) -> None:
        gxapi_cy.WrapIMU.make_mi_tabfrom_map(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def mosaic(cls, p1: str, p2: str, p3: 'GXIPJ', p4: float) -> 'GXIMG':
        ret_val = gxapi_cy.WrapIMU.mosaic(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3._wrapper, p4)
        return GXIMG(ret_val)



    @classmethod
    def peak_size(cls, p1: str, p2: 'GXVV', p3: 'GXVV', p4: int, p5: float, p6: 'GXVV') -> None:
        gxapi_cy.WrapIMU.peak_size(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3._wrapper, p4, p5, p6._wrapper)
        



    @classmethod
    def peak_size2(cls, p1: str, p2: 'GXVV', p3: 'GXVV', p4: int, p5: 'GXVV') -> None:
        gxapi_cy.WrapIMU.peak_size2(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3._wrapper, p4, p5._wrapper)
        



    @classmethod
    def pigeon_hole(cls, p1: 'GXIMG', p2: 'GXVV', p3: 'GXVV', p4: int_ref) -> None:
        p4.value = gxapi_cy.WrapIMU.pigeon_hole(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4.value)
        



    @classmethod
    def profile(cls, p1: 'GXIMG', p2: float, p3: float, p4: float, p5: float, p6: float, p7: 'GXVV') -> None:
        gxapi_cy.WrapIMU.profile(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7._wrapper)
        



    @classmethod
    def profile_vv(cls, p1: 'GXIMG', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        gxapi_cy.WrapIMU.profile_vv(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def range_grids(cls, p1: str, p2: 'GXIPJ', p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref) -> None:
        p3.value, p4.value, p5.value, p6.value = gxapi_cy.WrapIMU.range_grids(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3.value, p4.value, p5.value, p6.value)
        



    @classmethod
    def range_ll(cls, p1: 'GXIMG', p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value = gxapi_cy.WrapIMU.range_ll(GXContext._get_tls_geo(), p1._wrapper, p2.value, p3.value, p4.value, p5.value)
        



    @classmethod
    def stat_window(cls, p1: 'GXIMG', p2: float, p3: float, p4: float, p5: float, p6: int, p7: 'GXST') -> None:
        gxapi_cy.WrapIMU.stat_window(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7._wrapper)
        



    @classmethod
    def update_ply(cls, p1: 'GXIMG', p2: 'GXPLY') -> None:
        gxapi_cy.WrapIMU.update_ply(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer