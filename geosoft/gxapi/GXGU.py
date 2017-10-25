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
class GXGU:
    """
    GXGU class.

    Not a class. A catch-all group of functions performing
    various geophysical processes, including the calculation
    of simple EM model responses, certain instrument dump
    file imports, and 2D Euler deconvolution.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapGU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXGU':
        """
        A null (undefined) instance of :class:`GXGU`
        
        :returns: A null :class:`GXGU`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXGU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXGU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def dipole_mag(cls, p1: str, p2: float, p3: float, p4: int, p5: int, p6: float, p7: float) -> None:
        gxapi_cy.WrapGU.dipole_mag(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def em_half_space_inv(cls, p1: float, p2: float, p3: int, p4: float, p5: float, p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: int, p11: int, p12: float) -> None:
        gxapi_cy.WrapGU.em_half_space_inv(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10, p11, p12)
        



    @classmethod
    def em_half_space_vv(cls, p1: float, p2: float, p3: int, p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV') -> None:
        gxapi_cy.WrapGU.em_half_space_vv(GXContext._get_tls_geo(), p1, p2, p3, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper)
        



    @classmethod
    def geometrics2_db(cls, p1: 'GXDB', p2: 'GXRA', p3: 'GXWA', p4: int, p5: int, p6: int, p7: int, p8: float, p9: float, p10: float, p11: float) -> None:
        gxapi_cy.WrapGU.geometrics2_db(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8, p9, p10, p11)
        



    @classmethod
    def geometrics2_tbl(cls, p1: 'GXRA', p2: 'GXWA', p3: 'GXWA') -> None:
        gxapi_cy.WrapGU.geometrics2_tbl(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def geometrics_qc(cls, p1: 'GXWA', p2: str, p3: 'GXVV', p4: float, p5: float, p6: float, p7: 'GXVV', p8: 'GXVV') -> None:
        gxapi_cy.WrapGU.geometrics_qc(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3._wrapper, p4, p5, p6, p7._wrapper, p8._wrapper)
        



    @classmethod
    def geonics3138_dump2_db(cls, p1: 'GXDB', p2: 'GXRA', p3: 'GXRA', p4: 'GXWA', p5: float, p6: float) -> None:
        gxapi_cy.WrapGU.geonics3138_dump2_db(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6)
        



    @classmethod
    def geonics61_dump2_db(cls, p1: 'GXDB', p2: 'GXRA', p3: 'GXWA', p4: float, p5: float) -> None:
        gxapi_cy.WrapGU.geonics61_dump2_db(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5)
        



    @classmethod
    def geonics_dat2_db(cls, p1: 'GXDB', p2: 'GXRA', p3: 'GXWA', p4: float, p5: float) -> None:
        gxapi_cy.WrapGU.geonics_dat2_db(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5)
        



    @classmethod
    def gr_curv_cor(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV') -> None:
        gxapi_cy.WrapGU.gr_curv_cor(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def gr_curv_cor_ex(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV', p4: float) -> None:
        gxapi_cy.WrapGU.gr_curv_cor_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4)
        



    @classmethod
    def gr_demvv(cls, p1: 'GXIMG', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        gxapi_cy.WrapGU.gr_demvv(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def gr_test(cls, p1: float, p2: float, p3: float, p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXVV') -> None:
        gxapi_cy.WrapGU.gr_test(GXContext._get_tls_geo(), p1, p2, p3, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper)
        



    @classmethod
    def gravity_still_reading_correction(cls, p1: 'GXDB', p2: int, p3: int, p4: int, p5: str, p6: int) -> None:
        gxapi_cy.WrapGU.gravity_still_reading_correction(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5.encode(), p6)
        



    @classmethod
    def em_layer(cls, p1: float, p2: float, p3: float, p4: int, p5: int, p6: 'GXVV', p7: 'GXVV', p8: float_ref, p9: float_ref) -> int:
        ret_val, p8.value, p9.value = gxapi_cy.WrapGU.em_layer(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6._wrapper, p7._wrapper, p8.value, p9.value)
        return ret_val



    @classmethod
    def em_plate(cls, p1: float, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: int, p11: 'GXVV', p12: int, p13: float, p14: float, p15: float, p16: 'GXVV', p17: 'GXVV', p18: 'GXVV', p19: 'GXVV', p20: 'GXVV', p21: 'GXVV') -> int:
        ret_val = gxapi_cy.WrapGU.em_plate(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11._wrapper, p12, p13, p14, p15, p16._wrapper, p17._wrapper, p18._wrapper, p19._wrapper, p20._wrapper, p21._wrapper)
        return ret_val



    @classmethod
    def gen_ux_detect_symbols_group_name(cls, p1: str, p2: str, p3: str_ref) -> None:
        p3.value = gxapi_cy.WrapGU.gen_ux_detect_symbols_group_name(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode())
        



    @classmethod
    def import_daarc500_ethernet(cls, p1: str, p2: str, p3: int_ref) -> None:
        p3.value = gxapi_cy.WrapGU.import_daarc500_ethernet(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value)
        



    @classmethod
    def import_daarc500_serial(cls, p1: str, p2: int, p3: str, p4: int_ref) -> None:
        p4.value = gxapi_cy.WrapGU.import_daarc500_serial(GXContext._get_tls_geo(), p1.encode(), p2, p3.encode(), p4.value)
        



    @classmethod
    def import_p190(cls, p1: 'GXDB', p2: str, p3: str, p4: 'GXWA') -> None:
        gxapi_cy.WrapGU.import_p190(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3.encode(), p4._wrapper)
        



    @classmethod
    def lag_daarc500_gps(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXVV') -> None:
        gxapi_cy.WrapGU.lag_daarc500_gps(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def maxwell_plate_corners(cls, p1: float, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float_ref, p10: float_ref, p11: float_ref, p12: float_ref, p13: float_ref, p14: float_ref, p15: float_ref, p16: float_ref, p17: float_ref, p18: float_ref, p19: float_ref, p20: float_ref) -> None:
        p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value, p16.value, p17.value, p18.value, p19.value, p20.value = gxapi_cy.WrapGU.maxwell_plate_corners(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6, p7, p8, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value, p16.value, p17.value, p18.value, p19.value, p20.value)
        



    @classmethod
    def scan_daarc500_ethernet(cls, p1: str, p2: int_ref, p3: int_ref) -> None:
        p2.value, p3.value = gxapi_cy.WrapGU.scan_daarc500_ethernet(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value)
        



    @classmethod
    def scan_daarc500_serial(cls, p1: str, p2: 'GXVV', p3: 'GXVV') -> None:
        gxapi_cy.WrapGU.scan_daarc500_serial(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3._wrapper)
        



    @classmethod
    def vv_euler(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXIMG', p4: 'GXIMG', p5: 'GXIMG', p6: 'GXIMG', p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: 'GXVV', p11: 'GXVV', p12: 'GXVV', p13: int, p14: float, p15: float, p16: int) -> None:
        gxapi_cy.WrapGU.vv_euler(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10._wrapper, p11._wrapper, p12._wrapper, p13, p14, p15, p16)
        



    @classmethod
    def vv_euler2(cls, p1: 'GXVV', p2: 'GXVV', p3: 'GXIMG', p4: 'GXIMG', p5: 'GXIMG', p6: 'GXIMG', p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: 'GXVV', p11: 'GXVV', p12: 'GXVV', p13: 'GXVV', p14: float, p15: float, p16: int) -> None:
        gxapi_cy.WrapGU.vv_euler2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10._wrapper, p11._wrapper, p12._wrapper, p13._wrapper, p14, p15, p16)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer