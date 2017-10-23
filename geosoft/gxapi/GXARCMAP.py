### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXARCMAP:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapARCMAP(0)

    @classmethod
    def null(cls) -> 'GXARCMAP':
        """
        A null (undefined) instance of :class:`GXARCMAP`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXARCMAP` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXARCMAP`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def change_size(cls, p1: float, p2: float) -> None:
        gxapi_cy.WrapARCMAP.change_size(GXContext._get_tls_geo(), p1, p2)
        



    @classmethod
    def display_in_3d_view(cls, p1: str) -> None:
        gxapi_cy.WrapARCMAP.display_in_3d_view(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def export_feature_layer_by_name_to_3d_file(cls, p1: str, p2: str, p3: str, p4: str) -> None:
        gxapi_cy.WrapARCMAP.export_feature_layer_by_name_to_3d_file(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode())
        



    @classmethod
    def export_selected_feature_layer_to_3d_file(cls, p1: str) -> None:
        gxapi_cy.WrapARCMAP.export_selected_feature_layer_to_3d_file(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def get_current_document_info(cls, p1: str_ref, p2: str_ref, p3: str_ref) -> None:
        p1.value, p2.value, p3.value = gxapi_cy.WrapARCMAP.get_current_document_info(GXContext._get_tls_geo(), p1.value.encode(), p2.value.encode(), p3.value.encode())
        



    @classmethod
    def get_selected_layer_info(cls, p1: int, p2: str_ref, p3: str_ref) -> None:
        p2.value, p3.value = gxapi_cy.WrapARCMAP.get_selected_layer_info(GXContext._get_tls_geo(), p1, p2.value.encode(), p3.value.encode())
        



    @classmethod
    def get_number_of_selected_layers(cls) -> int:
        ret_val = gxapi_cy.WrapARCMAP.get_number_of_selected_layers(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def load_map(cls, p1: str, p2: str, p3: str, p4: int) -> int:
        ret_val = gxapi_cy.WrapARCMAP.load_map(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4)
        return ret_val



    @classmethod
    def load_map_ex(cls, p1: str, p2: str, p3: str, p4: str, p5: int) -> int:
        ret_val = gxapi_cy.WrapARCMAP.load_map_ex(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode(), p5)
        return ret_val



    @classmethod
    def load_shape(cls, p1: str, p2: int) -> int:
        ret_val = gxapi_cy.WrapARCMAP.load_shape(GXContext._get_tls_geo(), p1.encode(), p2)
        return ret_val



    @classmethod
    def load_spf(cls, p1: str, p2: int) -> int:
        ret_val = gxapi_cy.WrapARCMAP.load_spf(GXContext._get_tls_geo(), p1.encode(), p2)
        return ret_val



    @classmethod
    def load_lyr(cls, p1: str) -> None:
        gxapi_cy.WrapARCMAP.load_lyr(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def load_map(cls, p1: str, p2: str, p3: str, p4: str, p5: int, p6: int, p7: int) -> None:
        gxapi_cy.WrapARCMAP.load_map(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode(), p5, p6, p7)
        



    @classmethod
    def load_map_view(cls, p1: str, p2: str, p3: str, p4: int) -> None:
        gxapi_cy.WrapARCMAP.load_map_view(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4)
        



    @classmethod
    def load_raster(cls, p1: str) -> None:
        gxapi_cy.WrapARCMAP.load_raster(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def load_shape(cls, p1: str, p2: str, p3: str) -> None:
        gxapi_cy.WrapARCMAP.load_shape(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        



    @classmethod
    def map_view_to_shape(cls, p1: str, p2: str, p3: str, p4: 'GXLST') -> None:
        gxapi_cy.WrapARCMAP.map_view_to_shape(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4._wrapper)
        



    @classmethod
    def query_size(cls, p1: float_ref, p2: float_ref) -> None:
        p1.value, p2.value = gxapi_cy.WrapARCMAP.query_size(GXContext._get_tls_geo(), p1.value, p2.value)
        



    @classmethod
    def show_layer_by_name_in_3d(cls, p1: str, p2: str, p3: str) -> None:
        gxapi_cy.WrapARCMAP.show_layer_by_name_in_3d(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        



    @classmethod
    def show_selected_layers_in_3d(cls) -> None:
        gxapi_cy.WrapARCMAP.show_selected_layers_in_3d(GXContext._get_tls_geo())
        



    @classmethod
    def get_ipj_for_predefined_esri_gcs(cls, p1: 'GXIPJ', p2: int) -> None:
        gxapi_cy.WrapARCMAP.get_ipj_for_predefined_esri_gcs(GXContext._get_tls_geo(), p1._wrapper, p2)
        



    @classmethod
    def get_ipj_for_predefined_esri_pcs(cls, p1: 'GXIPJ', p2: int) -> None:
        gxapi_cy.WrapARCMAP.get_ipj_for_predefined_esri_pcs(GXContext._get_tls_geo(), p1._wrapper, p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer