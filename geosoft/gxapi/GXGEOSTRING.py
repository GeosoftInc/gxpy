### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXGEOSTRING:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapGEOSTRING(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXGEOSTRING':
        """
        A null (undefined) instance of :class:`GXGEOSTRING`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXGEOSTRING` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXGEOSTRING`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def open(cls, p1: str, p2: int) -> 'GXGEOSTRING':
        ret_val = gxapi_cy.WrapGEOSTRING.open(GXContext._get_tls_geo(), p1.encode(), p2)
        return GXGEOSTRING(ret_val)






    def get_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.get_ipj(p2._wrapper)
        




    def get_features(self, p2: 'GXLST') -> None:
        self._wrapper.get_features(p2._wrapper)
        




    def get_sections(self, p2: 'GXLST') -> None:
        self._wrapper.get_sections(p2._wrapper)
        




    def get_all_shapes(self, p2: 'GXLST') -> None:
        self._wrapper.get_all_shapes(p2._wrapper)
        




    def get_shapes_for_feature(self, p2: str, p3: 'GXLST') -> None:
        self._wrapper.get_shapes_for_feature(p2.encode(), p3._wrapper)
        




    def get_shapes_for_section(self, p2: str, p3: 'GXLST') -> None:
        self._wrapper.get_shapes_for_section(p2.encode(), p3._wrapper)
        




    def get_shapes_for_feature_and_section(self, p2: str, p3: str, p4: 'GXLST') -> None:
        self._wrapper.get_shapes_for_feature_and_section(p2.encode(), p3.encode(), p4._wrapper)
        




    def get_feature_properties(self, p2: str, p3: str_ref, p5: str_ref, p7: int_ref, p8: int_ref, p9: float_ref, p10: float_ref, p11: float_ref, p12: int_ref, p13: int_ref, p14: int_ref, p15: float_ref, p16: float_ref, p17: int_ref) -> None:
        p3.value, p5.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value, p16.value, p17.value = self._wrapper.get_feature_properties(p2.encode(), p3.value.encode(), p5.value.encode(), p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value, p16.value, p17.value)
        




    def get_section_properties(self, p2: str, p3: str_ref, p5: str_ref, p7: int_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: float_ref, p12: float_ref, p13: float_ref, p14: float_ref, p15: float_ref, p16: float_ref) -> None:
        p3.value, p5.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value, p16.value = self._wrapper.get_section_properties(p2.encode(), p3.value.encode(), p5.value.encode(), p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value, p16.value)
        




    def get_shape_properties(self, p2: str, p3: str_ref, p5: str_ref, p7: 'GXVV', p8: 'GXVV', p9: 'GXVV') -> None:
        p3.value, p5.value = self._wrapper.get_shape_properties(p2.encode(), p3.value.encode(), p5.value.encode(), p7._wrapper, p8._wrapper, p9._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer