### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXGIS:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapGIS(0)

    @classmethod
    def null(cls) -> 'GXGIS':
        """
        A null (undefined) instance of :class:`GXGIS`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXGIS` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXGIS`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, p1: str, p2: str, p3: int) -> 'GXGIS':
        ret_val = gxapi_cy.WrapGIS.create(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        return GXGIS(ret_val)




    def create_map2_d(self, p2: str, p3: float, p4: 'GXIPJ', p5: int) -> None:
        self._wrapper.create_map2_d(p2.encode(), p3, p4._wrapper, p5)
        






    def get_bpr_models_lst(self, p2: str, p3: 'GXLST') -> None:
        self._wrapper.get_bpr_models_lst(p2.encode(), p3._wrapper)
        




    def get_ipj(self) -> 'GXIPJ':
        ret_val = self._wrapper.get_ipj()
        return GXIPJ(ret_val)




    def get_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.get_meta(p2._wrapper)
        




    def get_range(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_range(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        



    @classmethod
    def datamine_type(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapGIS.datamine_type(GXContext._get_tls_geo(), p1.encode())
        return ret_val




    def get_file_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_file_name(p2.value.encode())
        



    @classmethod
    def is_mi_map_file(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapGIS.is_mi_map_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def is_mi_raster_tab_file(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapGIS.is_mi_raster_tab_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def is_mi_rotated_raster_tab_file(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapGIS.is_mi_rotated_raster_tab_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val




    def is_shp_file_3d(self) -> int:
        ret_val = self._wrapper.is_shp_file_3d()
        return ret_val




    def is_shp_file_point(self) -> int:
        ret_val = self._wrapper.is_shp_file_point()
        return ret_val




    def num_attribs(self) -> int:
        ret_val = self._wrapper.num_attribs()
        return ret_val




    def num_shapes(self) -> int:
        ret_val = self._wrapper.num_shapes()
        return ret_val



    @classmethod
    def scan_mi_raster_tab_file(cls, p1: str, p2: str_ref, p4: 'GXIPJ') -> None:
        p2.value = gxapi_cy.WrapGIS.scan_mi_raster_tab_file(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4._wrapper)
        




    def load_ascii(self, p2: 'GXWA') -> None:
        self._wrapper.load_ascii(p2._wrapper)
        




    def load_gdb(self, p2: 'GXDB') -> None:
        self._wrapper.load_gdb(p2._wrapper)
        




    def load_map(self, p2: 'GXMVIEW') -> None:
        self._wrapper.load_map(p2._wrapper)
        




    def load_map_ex(self, p2: 'GXMAP', p3: str) -> None:
        self._wrapper.load_map_ex(p2._wrapper, p3.encode())
        




    def load_meta_groups_map(self, p2: 'GXMVIEW', p3: 'GXMETA', p4: int, p5: str, p6: str) -> None:
        self._wrapper.load_meta_groups_map(p2._wrapper, p3._wrapper, p4, p5.encode(), p6.encode())
        




    def load_ply(self, p2: 'GXPLY') -> None:
        self._wrapper.load_ply(p2._wrapper)
        




    def load_shapes_gdb(self, p2: 'GXDB') -> None:
        self._wrapper.load_shapes_gdb(p2._wrapper)
        




    def set_dm_wireframe_pt_file(self, p2: str) -> None:
        self._wrapper.set_dm_wireframe_pt_file(p2.encode())
        




    def set_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.set_ipj(p2._wrapper)
        




    def set_lst(self, p2: 'GXLST') -> None:
        self._wrapper.set_lst(p2._wrapper)
        




    def set_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.set_meta(p2._wrapper)
        




    def set_triangulation_object_index(self, p2: int) -> None:
        self._wrapper.set_triangulation_object_index(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer