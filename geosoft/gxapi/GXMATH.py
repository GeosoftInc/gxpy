### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMATH:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMATH(0)

    @classmethod
    def null(cls) -> 'GXMATH':
        """
        A null (undefined) instance of :class:`GXMATH`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXMATH` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXMATH`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def cross_product_(cls, p1: float, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float_ref, p8: float_ref, p9: float_ref) -> None:
        p7.value, p8.value, p9.value = gxapi_cy.WrapMATH.cross_product_(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6, p7.value, p8.value, p9.value)
        



    @classmethod
    def abs_(cls, p1: int) -> int:
        ret_val = gxapi_cy.WrapMATH.abs_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def and_(cls, p1: int, p2: int) -> int:
        ret_val = gxapi_cy.WrapMATH.and_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def mod_(cls, p1: int, p2: int) -> int:
        ret_val = gxapi_cy.WrapMATH.mod_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def or_(cls, p1: int, p2: int) -> int:
        ret_val = gxapi_cy.WrapMATH.or_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def round_(cls, p1: float) -> int:
        ret_val = gxapi_cy.WrapMATH.round_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def xor_(cls, p1: int, p2: int) -> int:
        ret_val = gxapi_cy.WrapMATH.xor_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def nicer_log_scale_(cls, p1: float_ref, p2: float_ref, p3: int) -> None:
        p1.value, p2.value = gxapi_cy.WrapMATH.nicer_log_scale_(GXContext._get_tls_geo(), p1.value, p2.value, p3)
        



    @classmethod
    def nicer_scale_(cls, p1: float_ref, p2: float_ref, p3: float_ref, p4: int_ref) -> None:
        p1.value, p2.value, p3.value, p4.value = gxapi_cy.WrapMATH.nicer_scale_(GXContext._get_tls_geo(), p1.value, p2.value, p3.value, p4.value)
        



    @classmethod
    def normalise_3d_(cls, p1: float_ref, p2: float_ref, p3: float_ref) -> None:
        p1.value, p2.value, p3.value = gxapi_cy.WrapMATH.normalise_3d_(GXContext._get_tls_geo(), p1.value, p2.value, p3.value)
        



    @classmethod
    def abs_(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapMATH.abs_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def arc_cos_(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapMATH.arc_cos_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def arc_sin_(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapMATH.arc_sin_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def arc_tan_(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapMATH.arc_tan_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def arc_tan2_(cls, p1: float, p2: float) -> float:
        ret_val = gxapi_cy.WrapMATH.arc_tan2_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def ceil_(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapMATH.ceil_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def cos_(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapMATH.cos_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def dot_product_3d_(cls, p1: float, p2: float, p3: float, p4: float, p5: float, p6: float) -> float:
        ret_val = gxapi_cy.WrapMATH.dot_product_3d_(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6)
        return ret_val



    @classmethod
    def exp_(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapMATH.exp_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def floor_(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapMATH.floor_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def hypot_(cls, p1: float, p2: float) -> float:
        ret_val = gxapi_cy.WrapMATH.hypot_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def lambda_trans_(cls, p1: float, p2: float) -> float:
        ret_val = gxapi_cy.WrapMATH.lambda_trans_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def lambda_trans_rev_(cls, p1: float, p2: float) -> float:
        ret_val = gxapi_cy.WrapMATH.lambda_trans_rev_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def log_(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapMATH.log_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def log10_(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapMATH.log10_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def log_z_(cls, p1: float, p2: int, p3: float) -> float:
        ret_val = gxapi_cy.WrapMATH.log_z_(GXContext._get_tls_geo(), p1, p2, p3)
        return ret_val



    @classmethod
    def mod_(cls, p1: float, p2: float) -> float:
        ret_val = gxapi_cy.WrapMATH.mod_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def rotate_vector_(cls, p1: float, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float_ref, p9: float_ref, p10: float_ref) -> None:
        p8.value, p9.value, p10.value = gxapi_cy.WrapMATH.rotate_vector_(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6, p7, p8.value, p9.value, p10.value)
        



    @classmethod
    def pow_(cls, p1: float, p2: float) -> float:
        ret_val = gxapi_cy.WrapMATH.pow_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def rand_(cls) -> float:
        ret_val = gxapi_cy.WrapMATH.rand_(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def round_(cls, p1: float, p2: int) -> float:
        ret_val = gxapi_cy.WrapMATH.round_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def sign_(cls, p1: float, p2: float) -> float:
        ret_val = gxapi_cy.WrapMATH.sign_(GXContext._get_tls_geo(), p1, p2)
        return ret_val



    @classmethod
    def sin_(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapMATH.sin_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def sqrt_(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapMATH.sqrt_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def tan_(cls, p1: float) -> float:
        ret_val = gxapi_cy.WrapMATH.tan_(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def un_log_z_(cls, p1: float, p2: int, p3: float) -> float:
        ret_val = gxapi_cy.WrapMATH.un_log_z_(GXContext._get_tls_geo(), p1, p2, p3)
        return ret_val



    @classmethod
    def s_rand_(cls) -> None:
        gxapi_cy.WrapMATH.s_rand_(GXContext._get_tls_geo())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer