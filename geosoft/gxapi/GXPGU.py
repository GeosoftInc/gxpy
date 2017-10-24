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
class GXPGU:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapPGU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXPGU':
        """
        A null (undefined) instance of :class:`GXPGU`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXPGU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXPGU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# General


    @classmethod
    def bool_mask(cls, p1: 'GXPG', p2: str) -> None:
        gxapi_cy.WrapPGU.bool_mask(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def direct_gridding_dat(cls, p1: 'GXPG', p2: float, p3: float, p4: float, p5: float, p6: float, p7: 'GXDAT', p8: int) -> None:
        gxapi_cy.WrapPGU.direct_gridding_dat(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7._wrapper, p8)
        



    @classmethod
    def direct_gridding_dat_3d(cls, p1: 'GXPG', p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: 'GXDAT', p10: int) -> None:
        gxapi_cy.WrapPGU.direct_gridding_dat_3d(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9._wrapper, p10)
        



    @classmethod
    def direct_gridding_db(cls, p1: 'GXPG', p2: float, p3: float, p4: float, p5: float, p6: float, p7: 'GXDB', p8: int, p9: int, p10: int, p11: int) -> None:
        gxapi_cy.WrapPGU.direct_gridding_db(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7._wrapper, p8, p9, p10, p11)
        



    @classmethod
    def direct_gridding_db_3d(cls, p1: 'GXPG', p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: 'GXDB', p10: int, p11: int, p12: int, p13: int, p14: int) -> None:
        gxapi_cy.WrapPGU.direct_gridding_db_3d(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9._wrapper, p10, p11, p12, p13, p14)
        



    @classmethod
    def direct_gridding_vv(cls, p1: 'GXPG', p2: float, p3: float, p4: float, p5: float, p6: float, p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: int) -> None:
        gxapi_cy.WrapPGU.direct_gridding_vv(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7._wrapper, p8._wrapper, p9._wrapper, p10)
        



    @classmethod
    def expand(cls, p1: 'GXPG', p2: 'GXPG', p3: float, p4: int, p5: int, p6: int) -> None:
        gxapi_cy.WrapPGU.expand(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6)
        



    @classmethod
    def fill(cls, p1: 'GXPG', p2: int, p3: float, p4: int, p5: int, p6: int, p7: float, p8: float, p9: int, p10: int, p11: str) -> None:
        gxapi_cy.WrapPGU.fill(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11.encode())
        



    @classmethod
    def fill_value(cls, p1: 'GXPG', p2: float) -> None:
        gxapi_cy.WrapPGU.fill_value(GXContext._get_tls_geo(), p1._wrapper, p2)
        



    @classmethod
    def filt_sym(cls, p1: 'GXPG', p2: int, p3: int, p4: str, p5: int, p6: 'GXVV') -> None:
        gxapi_cy.WrapPGU.filt_sym(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4.encode(), p5, p6._wrapper)
        



    @classmethod
    def filt_sym5(cls, p1: 'GXPG', p2: int, p3: int, p4: str, p5: 'GXVV') -> None:
        gxapi_cy.WrapPGU.filt_sym5(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4.encode(), p5._wrapper)
        



    @classmethod
    def grid_peak(cls, p1: str, p2: int, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV') -> None:
        gxapi_cy.WrapPGU.grid_peak(GXContext._get_tls_geo(), p1.encode(), p2, p3._wrapper, p4._wrapper, p5._wrapper)
        



    @classmethod
    def dw_gridding_dat(cls, p1: 'GXPG', p2: 'GXDAT', p3: 'GXREG') -> None:
        gxapi_cy.WrapPGU.dw_gridding_dat(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def dw_gridding_dat_3d(cls, p1: 'GXPG', p2: 'GXDAT', p3: 'GXREG') -> None:
        gxapi_cy.WrapPGU.dw_gridding_dat_3d(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def dw_gridding_db(cls, p1: 'GXPG', p2: 'GXDB', p3: int, p4: int, p5: int, p6: 'GXREG') -> None:
        gxapi_cy.WrapPGU.dw_gridding_db(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6._wrapper)
        



    @classmethod
    def dw_gridding_db_3d(cls, p1: 'GXPG', p2: 'GXDB', p3: int, p4: int, p5: int, p6: int, p7: 'GXREG') -> None:
        gxapi_cy.WrapPGU.dw_gridding_db_3d(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6, p7._wrapper)
        



    @classmethod
    def dw_gridding_vv(cls, p1: 'GXPG', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: 'GXREG') -> None:
        gxapi_cy.WrapPGU.dw_gridding_vv(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper)
        



    @classmethod
    def numeric_to_thematic(cls, p1: 'GXPG', p2: 'GXVV', p3: 'GXPG') -> None:
        gxapi_cy.WrapPGU.numeric_to_thematic(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def peakedness(cls, p1: str, p2: int, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV') -> None:
        gxapi_cy.WrapPGU.peakedness(GXContext._get_tls_geo(), p1.encode(), p2, p3._wrapper, p4._wrapper, p5._wrapper)
        



    @classmethod
    def peakedness_grid(cls, p1: str, p2: str, p3: int, p4: float) -> None:
        gxapi_cy.WrapPGU.peakedness_grid(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4)
        



    @classmethod
    def ref_file(cls, p1: 'GXPG', p2: str) -> None:
        gxapi_cy.WrapPGU.ref_file(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def save_file(cls, p1: 'GXPG', p2: float, p3: float, p4: float, p5: float, p6: float, p7: 'GXTR', p8: 'GXIPJ', p9: str) -> None:
        gxapi_cy.WrapPGU.save_file(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6, p7._wrapper, p8._wrapper, p9.encode())
        



    @classmethod
    def thematic_to_numeric(cls, p1: 'GXPG', p2: 'GXVV', p3: 'GXPG') -> None:
        gxapi_cy.WrapPGU.thematic_to_numeric(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def trend(cls, p1: 'GXPG', p2: 'GXPG', p3: 'GXTR', p4: int, p5: int, p6: float, p7: float, p8: float, p9: float) -> None:
        gxapi_cy.WrapPGU.trend(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8, p9)
        




# Math Operations


    @classmethod
    def add_scalar(cls, p1: 'GXPG', p2: float) -> None:
        gxapi_cy.WrapPGU.add_scalar(GXContext._get_tls_geo(), p1._wrapper, p2)
        



    @classmethod
    def multiply_scalar(cls, p1: 'GXPG', p2: float) -> None:
        gxapi_cy.WrapPGU.multiply_scalar(GXContext._get_tls_geo(), p1._wrapper, p2)
        




# Matrix Operation


    @classmethod
    def correlation_matrix(cls, p1: 'GXPG', p2: 'GXPG') -> None:
        gxapi_cy.WrapPGU.correlation_matrix(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def correlation_matrix2(cls, p1: 'GXPG', p2: int, p3: 'GXPG') -> None:
        gxapi_cy.WrapPGU.correlation_matrix2(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper)
        



    @classmethod
    def invert_matrix(cls, p1: 'GXPG', p2: 'GXPG') -> None:
        gxapi_cy.WrapPGU.invert_matrix(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def jacobi(cls, p1: 'GXPG', p2: 'GXVV', p3: 'GXPG') -> None:
        gxapi_cy.WrapPGU.jacobi(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def lu_back_sub(cls, p1: 'GXPG', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        gxapi_cy.WrapPGU.lu_back_sub(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def lu_decomp(cls, p1: 'GXPG', p2: 'GXPG', p3: 'GXVV') -> None:
        gxapi_cy.WrapPGU.lu_decomp(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def matrix_mult(cls, p1: 'GXPG', p2: int, p3: 'GXPG', p4: int, p5: 'GXPG') -> None:
        gxapi_cy.WrapPGU.matrix_mult(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper, p4, p5._wrapper)
        



    @classmethod
    def matrix_vector_mult(cls, p1: 'GXPG', p2: 'GXVV', p3: 'GXVV') -> None:
        gxapi_cy.WrapPGU.matrix_vector_mult(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def sv_decompose(cls, p1: 'GXPG', p2: 'GXPG', p3: 'GXVV', p4: 'GXPG') -> None:
        gxapi_cy.WrapPGU.sv_decompose(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def sv_recompose(cls, p1: 'GXPG', p2: 'GXVV', p3: 'GXPG', p4: float, p5: 'GXPG') -> None:
        gxapi_cy.WrapPGU.sv_recompose(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5._wrapper)
        




# Principal Component Analysis


    @classmethod
    def pc_communality(cls, p1: 'GXPG', p2: 'GXVV') -> None:
        gxapi_cy.WrapPGU.pc_communality(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def pc_loadings(cls, p1: 'GXPG', p2: 'GXPG') -> None:
        gxapi_cy.WrapPGU.pc_loadings(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def pc_loadings2(cls, p1: 'GXPG', p2: 'GXPG') -> None:
        gxapi_cy.WrapPGU.pc_loadings2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def pc_scores(cls, p1: 'GXPG', p2: 'GXPG', p3: 'GXPG') -> None:
        gxapi_cy.WrapPGU.pc_scores(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def pc_standardize(cls, p1: 'GXPG', p2: 'GXVV', p3: 'GXVV', p4: int) -> None:
        gxapi_cy.WrapPGU.pc_standardize(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4)
        



    @classmethod
    def pc_standardize2(cls, p1: 'GXPG', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: int) -> None:
        gxapi_cy.WrapPGU.pc_standardize2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5)
        



    @classmethod
    def pc_transform(cls, p1: 'GXPG', p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: int) -> None:
        gxapi_cy.WrapPGU.pc_transform(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5)
        



    @classmethod
    def pc_varimax(cls, p1: 'GXPG', p2: 'GXPG') -> None:
        gxapi_cy.WrapPGU.pc_varimax(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        




# Specialized Operations


    @classmethod
    def maximum_terrain_steepness(cls, p1: 'GXPG', p2: int) -> float:
        ret_val = gxapi_cy.WrapPGU.maximum_terrain_steepness(GXContext._get_tls_geo(), p1._wrapper, p2)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer