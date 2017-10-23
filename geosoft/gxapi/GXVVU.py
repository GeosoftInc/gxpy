### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVVU:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVVU(0)

    @classmethod
    def null(cls) -> 'GXVVU':
        """
        A null (undefined) instance of :class:`GXVVU`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXVVU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXVVU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def average_repeat(cls, p1: 'GXVV', p2: 'GXVV') -> None:
        gxapi_cy.WrapVVU.average_repeat(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def average_repeat_ex(cls, p1: 'GXVV', p2: 'GXVV', p3: int) -> None:
        gxapi_cy.WrapVVU.average_repeat_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3)
        



    @classmethod
    def average_repeat2(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV') -> None:
        gxapi_cy.WrapVVU.average_repeat2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def average_repeat2_ex(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: int) -> None:
        gxapi_cy.WrapVVU.average_repeat2_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4)
        



    @classmethod
    def binary_search(cls, p1: 'GXVV', p2: float, p3: int_ref, p4: int_ref) -> None:
        p3.value, p4.value = gxapi_cy.WrapVVU.binary_search(GXContext._get_tls_geo(), p1._wrapper, p2, p3.value, p4.value)
        



    @classmethod
    def box_cox(cls, p1: 'GXVV', p2: float) -> None:
        gxapi_cy.WrapVVU.box_cox(GXContext._get_tls_geo(), p1._wrapper, p2)
        



    @classmethod
    def bp_filt(cls, p1: 'GXVV', p2: 'GXVV', p3: float, p4: float, p5: int) -> None:
        gxapi_cy.WrapVVU.bp_filt(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5)
        



    @classmethod
    def clip(cls, p1: 'GXVV', p2: float, p3: float, p4: int) -> None:
        gxapi_cy.WrapVVU.clip(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        



    @classmethod
    def clip_to_detect_limit(cls, p1: 'GXVV', p2: float, p3: int) -> None:
        gxapi_cy.WrapVVU.clip_to_detect_limit(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def decimate(cls, p1: 'GXVV', p2: int) -> None:
        gxapi_cy.WrapVVU.decimate(GXContext._get_tls_geo(), p1._wrapper, p2)
        



    @classmethod
    def deviation(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: float, p5: float, p6: float, p7: float, p8: int) -> None:
        gxapi_cy.WrapVVU.deviation(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8)
        



    @classmethod
    def distance(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: float, p5: float, p6: float, p7: float) -> None:
        gxapi_cy.WrapVVU.distance(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7)
        



    @classmethod
    def distance_non_cumulative(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: float, p5: float, p6: float, p7: float) -> None:
        gxapi_cy.WrapVVU.distance_non_cumulative(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7)
        



    @classmethod
    def distance_3d(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: float, p5: 'GXVV') -> None:
        gxapi_cy.WrapVVU.distance_3d(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5._wrapper)
        



    @classmethod
    def find_gaps_3d(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: float, p5: 'GXVV') -> None:
        gxapi_cy.WrapVVU.find_gaps_3d(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5._wrapper)
        



    @classmethod
    def dummy_range(cls, p1: 'GXVV', p2: float, p3: float, p4: int, p5: int) -> None:
        gxapi_cy.WrapVVU.dummy_range(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        



    @classmethod
    def dummy_range_ex(cls, p1: 'GXVV', p2: float, p3: float, p4: int, p5: int, p6: int) -> None:
        gxapi_cy.WrapVVU.dummy_range_ex(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6)
        



    @classmethod
    def dummy_repeat(cls, p1: 'GXVV', p2: int) -> None:
        gxapi_cy.WrapVVU.dummy_repeat(GXContext._get_tls_geo(), p1._wrapper, p2)
        



    @classmethod
    def dup_stats(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        gxapi_cy.WrapVVU.dup_stats(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def exp_dist(cls, p1: 'GXVV', p2: int, p3: float, p4: int) -> None:
        gxapi_cy.WrapVVU.exp_dist(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        



    @classmethod
    def filter(cls, p1: 'GXVV', p2: 'GXVV', p3: int) -> None:
        gxapi_cy.WrapVVU.filter(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3)
        



    @classmethod
    def find_string_items(cls, p1: 'GXVV', p2: 'GXVV', p3: int, p4: int, p5: int, p6: 'GXVV') -> None:
        gxapi_cy.WrapVVU.find_string_items(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6._wrapper)
        



    @classmethod
    def fractal_filter(cls, p1: 'GXVV', p2: int, p3: int, p4: 'GXVV') -> None:
        gxapi_cy.WrapVVU.fractal_filter(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4._wrapper)
        



    @classmethod
    def close_xy(cls, p1: 'GXVV', p2: 'GXVV', p3: float, p4: float) -> int:
        ret_val = gxapi_cy.WrapVVU.close_xy(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4)
        return ret_val



    @classmethod
    def close_xym(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: float, p5: float) -> int:
        ret_val = gxapi_cy.WrapVVU.close_xym(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5)
        return ret_val



    @classmethod
    def close_xyz(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: float, p5: float, p6: float) -> int:
        ret_val = gxapi_cy.WrapVVU.close_xyz(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6)
        return ret_val



    @classmethod
    def close_xyzm(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: float, p6: float, p7: float) -> int:
        ret_val = gxapi_cy.WrapVVU.close_xyzm(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7)
        return ret_val



    @classmethod
    def dummy_back_tracks(cls, p1: 'GXVV') -> int:
        ret_val = gxapi_cy.WrapVVU.dummy_back_tracks(GXContext._get_tls_geo(), p1._wrapper)
        return ret_val



    @classmethod
    def find_dummy(cls, p1: 'GXVV', p2: int, p3: int, p4: int, p5: int) -> int:
        ret_val = gxapi_cy.WrapVVU.find_dummy(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        return ret_val



    @classmethod
    def interp(cls, p1: 'GXVV', p2: int, p3: int) -> None:
        gxapi_cy.WrapVVU.interp(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def qc_fill_gaps(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: float) -> int:
        ret_val = gxapi_cy.WrapVVU.qc_fill_gaps(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5)
        return ret_val



    @classmethod
    def search_text(cls, p1: 'GXVV', p2: str, p3: int, p4: int, p5: int, p6: int) -> int:
        ret_val = gxapi_cy.WrapVVU.search_text(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6)
        return ret_val



    @classmethod
    def mask(cls, p1: 'GXVV', p2: 'GXVV') -> None:
        gxapi_cy.WrapVVU.mask(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def mask_and(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV') -> None:
        gxapi_cy.WrapVVU.mask_and(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def mask_or(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV') -> None:
        gxapi_cy.WrapVVU.mask_or(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def nl_filt(cls, p1: 'GXVV', p2: 'GXVV', p3: int, p4: float) -> None:
        gxapi_cy.WrapVVU.nl_filt(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4)
        



    @classmethod
    def noise_check(cls, p1: 'GXVV', p2: 'GXVV', p3: float, p4: int) -> None:
        gxapi_cy.WrapVVU.noise_check(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4)
        



    @classmethod
    def noise_check2(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: float, p5: int) -> None:
        gxapi_cy.WrapVVU.noise_check2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5)
        



    @classmethod
    def normal_dist(cls, p1: 'GXVV', p2: int, p3: float, p4: float, p5: int) -> None:
        gxapi_cy.WrapVVU.normal_dist(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        



    @classmethod
    def offset_circles(cls, p1: 'GXVV', p2: 'GXVV', p3: float, p4: float, p5: 'GXVV', p6: 'GXVV') -> None:
        gxapi_cy.WrapVVU.offset_circles(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5._wrapper, p6._wrapper)
        



    @classmethod
    def offset_correct(cls, p1: 'GXVV', p2: 'GXVV', p3: float, p4: int, p5: 'GXVV', p6: 'GXVV') -> None:
        gxapi_cy.WrapVVU.offset_correct(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5._wrapper, p6._wrapper)
        



    @classmethod
    def offset_correct2(cls, p1: 'GXVV', p2: 'GXVV', p3: float, p4: float, p5: 'GXVV', p6: 'GXVV') -> None:
        gxapi_cy.WrapVVU.offset_correct2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5._wrapper, p6._wrapper)
        



    @classmethod
    def offset_correct3(cls, p1: 'GXVV', p2: 'GXVV', p3: float, p4: float, p5: float, p6: 'GXVV', p7: 'GXVV') -> None:
        gxapi_cy.WrapVVU.offset_correct3(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6._wrapper, p7._wrapper)
        



    @classmethod
    def offset_correct_xyz(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: float, p5: float, p6: float, p7: float, p8: 'GXVV', p9: 'GXVV', p10: 'GXVV') -> None:
        gxapi_cy.WrapVVU.offset_correct_xyz(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8._wrapper, p9._wrapper, p10._wrapper)
        



    @classmethod
    def offset_rectangles(cls, p1: 'GXVV', p2: 'GXVV', p3: float, p4: float, p5: float, p6: 'GXVV', p7: 'GXVV') -> None:
        gxapi_cy.WrapVVU.offset_rectangles(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6._wrapper, p7._wrapper)
        



    @classmethod
    def pick_peak(cls, p1: 'GXVV', p2: 'GXVV', p3: float, p4: int) -> None:
        gxapi_cy.WrapVVU.pick_peak(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4)
        



    @classmethod
    def pick_peak2(cls, p1: 'GXVV', p2: 'GXVV', p3: float, p4: float) -> None:
        gxapi_cy.WrapVVU.pick_peak2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4)
        



    @classmethod
    def pick_peak3(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: float, p5: float, p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXVV') -> None:
        gxapi_cy.WrapVVU.pick_peak3(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper)
        



    @classmethod
    def poly_fill(cls, p1: 'GXVV', p2: int, p3: 'GXVV') -> None:
        gxapi_cy.WrapVVU.poly_fill(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper)
        



    @classmethod
    def poly_fill2(cls, p1: 'GXVV', p2: 'GXVV', p3: int, p4: 'GXVV') -> None:
        gxapi_cy.WrapVVU.poly_fill2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4._wrapper)
        



    @classmethod
    def polygon_mask(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: 'GXPLY', p5: int) -> None:
        gxapi_cy.WrapVVU.polygon_mask(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5)
        



    @classmethod
    def prune(cls, p1: 'GXVV', p2: 'GXVV', p3: int) -> None:
        gxapi_cy.WrapVVU.prune(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3)
        



    @classmethod
    def qc(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: float, p5: float, p6: float, p7: float, p8: int) -> None:
        gxapi_cy.WrapVVU.qc(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8)
        



    @classmethod
    def range_vector_mag(cls, p1: 'GXVV', p2: 'GXVV', p3: float_ref, p4: float_ref) -> None:
        p3.value, p4.value = gxapi_cy.WrapVVU.range_vector_mag(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.value, p4.value)
        



    @classmethod
    def regress(cls, p1: 'GXVV', p2: 'GXVV', p3: float_ref, p4: float_ref) -> None:
        p3.value, p4.value = gxapi_cy.WrapVVU.regress(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.value, p4.value)
        



    @classmethod
    def rel_var_dup(cls, p1: 'GXVV', p2: 'GXVV', p3: float_ref, p4: int_ref) -> None:
        p3.value, p4.value = gxapi_cy.WrapVVU.rel_var_dup(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.value, p4.value)
        



    @classmethod
    def remove_dummy(cls, p1: 'GXVV') -> None:
        gxapi_cy.WrapVVU.remove_dummy(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def remove_dummy2(cls, p1: 'GXVV', p2: 'GXVV') -> None:
        gxapi_cy.WrapVVU.remove_dummy2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def remove_dummy3(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV') -> None:
        gxapi_cy.WrapVVU.remove_dummy3(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def remove_dummy4(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        gxapi_cy.WrapVVU.remove_dummy4(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def remove_dup(cls, p1: 'GXVV', p2: 'GXVV', p3: int) -> None:
        gxapi_cy.WrapVVU.remove_dup(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3)
        



    @classmethod
    def remove_xy_dup(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: int) -> None:
        gxapi_cy.WrapVVU.remove_xy_dup(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4)
        



    @classmethod
    def remove_xy_dup_index(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV') -> None:
        gxapi_cy.WrapVVU.remove_xy_dup_index(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def rolling_stats(cls, p1: 'GXVV', p2: 'GXVV', p3: int, p4: int, p5: int) -> None:
        gxapi_cy.WrapVVU.rolling_stats(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5)
        



    @classmethod
    def search_replace(cls, p1: 'GXVV', p2: float, p3: float) -> None:
        gxapi_cy.WrapVVU.search_replace(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def search_replace_text(cls, p1: 'GXVV', p2: int, p3: int, p4: str, p5: str, p6: int) -> None:
        gxapi_cy.WrapVVU.search_replace_text(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4.encode(), p5.encode(), p6)
        



    @classmethod
    def search_replace_text_ex(cls, p1: 'GXVV', p2: int, p3: int, p4: str, p5: str, p6: int, p7: int_ref) -> None:
        p7.value = gxapi_cy.WrapVVU.search_replace_text_ex(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4.encode(), p5.encode(), p6, p7.value)
        



    @classmethod
    def spline(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: int, p5: float, p6: float, p7: float, p8: int, p9: int) -> None:
        gxapi_cy.WrapVVU.spline(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def spline2(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: int) -> None:
        gxapi_cy.WrapVVU.spline2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5)
        



    @classmethod
    def tokenize_to_values(cls, p1: 'GXVV', p2: str) -> int:
        ret_val = gxapi_cy.WrapVVU.tokenize_to_values(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return ret_val



    @classmethod
    def translate(cls, p1: 'GXVV', p2: float, p3: float) -> None:
        gxapi_cy.WrapVVU.translate(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def trend(cls, p1: 'GXVV', p2: int, p3: 'GXVV') -> None:
        gxapi_cy.WrapVVU.trend(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper)
        



    @classmethod
    def trend2(cls, p1: 'GXVV', p2: 'GXVV', p3: int, p4: 'GXVV') -> None:
        gxapi_cy.WrapVVU.trend2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4._wrapper)
        



    @classmethod
    def uniform_dist(cls, p1: 'GXVV', p2: int, p3: float, p4: float, p5: int) -> None:
        gxapi_cy.WrapVVU.uniform_dist(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer