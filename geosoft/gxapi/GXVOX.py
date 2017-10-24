### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVOX:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVOX(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXVOX':
        """
        A null (undefined) instance of :class:`GXVOX`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXVOX` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXVOX`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def calc_stats(self, p2: 'GXST') -> None:
        self._wrapper.calc_stats(p2._wrapper)
        



    @classmethod
    def create(cls, p1: str) -> 'GXVOX':
        ret_val = gxapi_cy.WrapVOX.create(GXContext._get_tls_geo(), p1.encode())
        return GXVOX(ret_val)




    def create_pg(self) -> 'GXPG':
        ret_val = self._wrapper.create_pg()
        return GXPG(ret_val)




    def create_type_pg(self, p2: int) -> 'GXPG':
        ret_val = self._wrapper.create_type_pg(p2)
        return GXPG(ret_val)






    def dump(self, p2: str) -> None:
        self._wrapper.dump(p2.encode())
        




    def export_img(self, p2: str, p3: int) -> None:
        self._wrapper.export_img(p2.encode(), p3)
        




    def export_to_grids(self, p2: str, p3: int, p4: int, p5: int, p6: int, p7: float, p8: int) -> None:
        self._wrapper.export_to_grids(p2.encode(), p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def export_xml(cls, p1: str, p2: int_ref, p3: str) -> None:
        p2.value = gxapi_cy.WrapVOX.export_xml(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.encode())
        




    def export_seg_y(self, p2: str, p3: float) -> None:
        self._wrapper.export_seg_y(p2.encode(), p3)
        



    @classmethod
    def export_ji_gs_xml(cls, p1: str, p2: str) -> None:
        gxapi_cy.WrapVOX.export_ji_gs_xml(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        




    def export_xyz(self, p2: str, p3: int, p4: int, p5: int, p6: int, p7: int) -> None:
        self._wrapper.export_xyz(p2.encode(), p3, p4, p5, p6, p7)
        




    def filter(self, p2: int, p3: str, p4: int, p5: int, p6: str) -> None:
        self._wrapper.filter(p2, p3.encode(), p4, p5, p6.encode())
        



    @classmethod
    def generate_db(cls, p1: str, p2: 'GXDB', p3: int) -> None:
        gxapi_cy.WrapVOX.generate_db(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3)
        



    @classmethod
    def generate_vector_voxel_from_db(cls, p1: str, p2: 'GXDB', p3: int, p4: int, p5: int, p6: int, p7: float, p8: float) -> None:
        gxapi_cy.WrapVOX.generate_vector_voxel_from_db(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def generate_pg(cls, p1: str, p2: 'GXPG', p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: 'GXIPJ', p10: 'GXMETA') -> 'GXVOX':
        ret_val = gxapi_cy.WrapVOX.generate_pg(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6, p7, p8, p9._wrapper, p10._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_constant_value(cls, p1: str, p2: float, p3: int, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: int, p11: int, p12: int, p13: 'GXIPJ', p14: 'GXMETA') -> 'GXVOX':
        ret_val = gxapi_cy.WrapVOX.generate_constant_value(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13._wrapper, p14._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_pgvv(cls, p1: str, p2: 'GXPG', p3: float, p4: float, p5: float, p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXIPJ', p10: 'GXMETA') -> 'GXVOX':
        ret_val = gxapi_cy.WrapVOX.generate_pgvv(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_constant_value_vv(cls, p1: str, p2: float, p3: int, p4: float, p5: float, p6: float, p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: 'GXIPJ', p11: 'GXMETA') -> 'GXVOX':
        ret_val = gxapi_cy.WrapVOX.generate_constant_value_vv(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7._wrapper, p8._wrapper, p9._wrapper, p10._wrapper, p11._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def init_generate_by_subset_pg(cls, p1: int, p2: int, p3: int, p4: int) -> 'GXVOX':
        ret_val = gxapi_cy.WrapVOX.init_generate_by_subset_pg(GXContext._get_tls_geo(), p1, p2, p3, p4)
        return GXVOX(ret_val)




    def add_generate_by_subset_pg(self, p2: 'GXPG', p3: int, p4: int) -> None:
        self._wrapper.add_generate_by_subset_pg(p2._wrapper, p3, p4)
        




    def end_generate_by_subset_pg(self, p2: str, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: 'GXIPJ', p10: 'GXMETA') -> None:
        self._wrapper.end_generate_by_subset_pg(p2.encode(), p3, p4, p5, p6, p7, p8, p9._wrapper, p10._wrapper)
        




    def get_area(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_area(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_gocad_location(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: float_ref, p12: float_ref, p13: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value = self._wrapper.get_gocad_location(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value)
        




    def get_grid_section_cell_sizes(self, p2: float, p3: float_ref, p4: float_ref) -> None:
        p3.value, p4.value = self._wrapper.get_grid_section_cell_sizes(p2, p3.value, p4.value)
        




    def get_info(self, p2: int_ref, p3: int_ref, p4: int_ref, p5: int_ref, p6: int_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_info(p2.value, p3.value, p4.value, p5.value, p6.value)
        




    def get_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.get_ipj(p2._wrapper)
        




    def get_limits(self, p2: int_ref, p3: int_ref, p4: int_ref, p5: int_ref, p6: int_ref, p7: int_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_limits(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_limits_xyz(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_limits_xyz(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_location(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: 'GXVV', p6: 'GXVV', p7: 'GXVV') -> None:
        p2.value, p3.value, p4.value = self._wrapper.get_location(p2.value, p3.value, p4.value, p5._wrapper, p6._wrapper, p7._wrapper)
        




    def get_location_points(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.get_location_points(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def get_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.get_meta(p2._wrapper)
        




    def get_double_location(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: float_ref, p12: float_ref, p13: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value = self._wrapper.get_double_location(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value)
        




    def get_simple_location(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_simple_location(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def get_stats(self) -> 'GXST':
        ret_val = self._wrapper.get_stats()
        return GXST(ret_val)




    def get_tpat(self, p2: 'GXTPAT') -> None:
        self._wrapper.get_tpat(p2._wrapper)
        



    @classmethod
    def grid_points(cls, p1: str, p2: str, p3: float, p4: int, p5: float, p6: float, p7: int, p8: int, p9: int, p10: float, p11: float, p12: float, p13: float, p14: float, p15: int, p16: 'GXVV', p17: 'GXVV', p18: 'GXVV', p19: 'GXVV', p20: 'GXIPJ') -> 'GXVOX':
        ret_val = gxapi_cy.WrapVOX.grid_points(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16._wrapper, p17._wrapper, p18._wrapper, p19._wrapper, p20._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def grid_points_z(cls, p1: str, p2: str, p3: float, p4: str, p5: int, p6: float, p7: float, p8: int, p9: int, p10: int, p11: float, p12: float, p13: float, p14: float, p15: float, p16: int, p17: 'GXVV', p18: 'GXVV', p19: 'GXVV', p20: 'GXVV', p21: 'GXIPJ') -> 'GXVOX':
        ret_val = gxapi_cy.WrapVOX.grid_points_z(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4.encode(), p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17._wrapper, p18._wrapper, p19._wrapper, p20._wrapper, p21._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def grid_points_z_ex(cls, p1: str, p2: str, p3: float, p4: str, p5: int, p6: float, p7: float, p8: int, p9: int, p10: int, p11: float, p12: float_ref, p13: float_ref, p14: float, p15: float_ref, p16: float, p17: float, p18: float, p19: float, p20: float, p21: int, p22: 'GXVV', p23: 'GXVV', p24: 'GXVV', p25: 'GXVV', p26: 'GXIPJ') -> 'GXVOX':
        ret_val, p12.value, p13.value, p15.value = gxapi_cy.WrapVOX.grid_points_z_ex(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4.encode(), p5, p6, p7, p8, p9, p10, p11, p12.value, p13.value, p14, p15.value, p16, p17, p18, p19, p20, p21, p22._wrapper, p23._wrapper, p24._wrapper, p25._wrapper, p26._wrapper)
        return GXVOX(ret_val)




    def can_append_to(self, p2: str) -> int:
        ret_val = self._wrapper.can_append_to(p2.encode())
        return ret_val




    def get_cell_size_strings(self, p2: str_ref, p4: str_ref, p6: str_ref, p8: float, p9: float, p10: float) -> None:
        p2.value, p4.value, p6.value = self._wrapper.get_cell_size_strings(p2.value.encode(), p4.value.encode(), p6.value.encode(), p8, p9, p10)
        




    def is_thematic(self) -> int:
        ret_val = self._wrapper.is_thematic()
        return ret_val




    def is_vector_voxel(self) -> int:
        ret_val = self._wrapper.is_vector_voxel()
        return ret_val




    def set_cell_size_strings(self, p2: str, p3: str, p4: str) -> int:
        ret_val = self._wrapper.set_cell_size_strings(p2.encode(), p3.encode(), p4.encode())
        return ret_val



    @classmethod
    def log_grid_points_z_ex(cls, p1: str, p2: str, p3: float, p4: str, p5: int, p6: float, p7: float, p8: int, p9: int, p10: int, p11: float, p12: float_ref, p13: float_ref, p14: float, p15: float_ref, p16: float, p17: float, p18: float, p19: float, p20: float, p21: int, p22: float, p23: int, p24: 'GXVV', p25: 'GXVV', p26: 'GXVV', p27: 'GXVV', p28: 'GXIPJ') -> 'GXVOX':
        ret_val, p12.value, p13.value, p15.value = gxapi_cy.WrapVOX.log_grid_points_z_ex(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3, p4.encode(), p5, p6, p7, p8, p9, p10, p11, p12.value, p13.value, p14, p15.value, p16, p17, p18, p19, p20, p21, p22, p23, p24._wrapper, p25._wrapper, p26._wrapper, p27._wrapper, p28._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def krig(cls, p1: str, p2: float, p3: int, p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: 'GXIPJ', p9: 'GXREG') -> 'GXVOX':
        ret_val = gxapi_cy.WrapVOX.krig(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def math(cls, p1: str, p2: str, p3: str, p4: str, p5: str, p6: 'GXLST') -> 'GXVOX':
        ret_val = gxapi_cy.WrapVOX.math(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6._wrapper)
        return GXVOX(ret_val)




    def merge(self, p2: 'GXVOX', p3: 'GXREG', p4: str) -> None:
        self._wrapper.merge(p2._wrapper, p3._wrapper, p4.encode())
        



    @classmethod
    def nearest_neighbour_grid(cls, p1: str, p2: float, p3: float, p4: int, p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXIPJ') -> 'GXVOX':
        ret_val = gxapi_cy.WrapVOX.nearest_neighbour_grid(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def compute_cell_size(cls, p1: float, p2: float, p3: float, p4: float, p5: float, p6: float) -> float:
        ret_val = gxapi_cy.WrapVOX.compute_cell_size(GXContext._get_tls_geo(), p1, p2, p3, p4, p5, p6)
        return ret_val




    def re_grid(self, p2: 'GXVOX', p3: 'GXREG', p4: str) -> None:
        self._wrapper.re_grid(p2._wrapper, p3._wrapper, p4.encode())
        




    def resample_pg(self, p2: 'GXIPJ', p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: int, p10: int, p11: int, p12: float, p13: float, p14: int) -> 'GXPG':
        ret_val = self._wrapper.resample_pg(p2._wrapper, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14)
        return GXPG(ret_val)




    def rescale_cell_sizes(self, p2: float) -> None:
        self._wrapper.rescale_cell_sizes(p2)
        




    def sample_cdi(self, p2: 'GXDB', p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: str) -> None:
        self._wrapper.sample_cdi(p2._wrapper, p3, p4, p5, p6, p7, p8, p9, p10.encode())
        




    def sample_cdi_to_topography(self, p2: 'GXDB', p3: int, p4: int, p5: int, p6: 'GXVV', p7: int, p8: str, p9: str) -> None:
        self._wrapper.sample_cdi_to_topography(p2._wrapper, p3, p4, p5, p6._wrapper, p7, p8.encode(), p9.encode())
        




    def sample_vv(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: int, p6: 'GXVV') -> None:
        self._wrapper.sample_vv(p2._wrapper, p3._wrapper, p4._wrapper, p5, p6._wrapper)
        




    def set_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.set_ipj(p2._wrapper)
        




    def set_location(self, p2: float, p3: float, p4: float, p5: 'GXVV', p6: 'GXVV', p7: 'GXVV') -> None:
        self._wrapper.set_location(p2, p3, p4, p5._wrapper, p6._wrapper, p7._wrapper)
        




    def set_meta(self, p2: 'GXMETA') -> None:
        self._wrapper.set_meta(p2._wrapper)
        




    def set_origin(self, p2: int, p3: float, p4: float, p5: float) -> None:
        self._wrapper.set_origin(p2, p3, p4, p5)
        




    def set_simple_location(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None:
        self._wrapper.set_simple_location(p2, p3, p4, p5, p6, p7)
        




    def set_tpat(self, p2: 'GXTPAT') -> None:
        self._wrapper.set_tpat(p2._wrapper)
        




    def slice_ipj(self, p2: str, p3: 'GXIPJ', p4: int, p5: float, p6: float, p7: float, p8: float, p9: int, p10: int) -> None:
        self._wrapper.slice_ipj(p2.encode(), p3._wrapper, p4, p5, p6, p7, p8, p9, p10)
        




    def slice_multi_layer_ipj(self, p2: str, p3: 'GXIPJ', p4: int, p5: float, p6: float, p7: float, p8: float, p9: int, p10: int, p11: int, p12: float, p13: float) -> None:
        self._wrapper.slice_multi_layer_ipj(p2.encode(), p3._wrapper, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        




    def subset_to_double_extents(self, p2: str) -> None:
        self._wrapper.subset_to_double_extents(p2.encode())
        



    @classmethod
    def sync(cls, p1: str) -> None:
        gxapi_cy.WrapVOX.sync(GXContext._get_tls_geo(), p1.encode())
        




    def window_ply(self, p2: 'GXPLY', p3: int, p4: float, p5: float, p6: str, p7: int) -> None:
        self._wrapper.window_ply(p2._wrapper, p3, p4, p5, p6.encode(), p7)
        




    def window_xyz(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: str, p9: int) -> None:
        self._wrapper.window_xyz(p2, p3, p4, p5, p6, p7, p8.encode(), p9)
        




    def write_xml(self, p2: str) -> None:
        self._wrapper.write_xml(p2.encode())
        




    def convert_numeric_to_thematic(self, p2: 'GXVV', p3: str) -> None:
        self._wrapper.convert_numeric_to_thematic(p2._wrapper, p3.encode())
        




    def convert_thematic_to_numeric(self, p2: 'GXVV', p3: str) -> None:
        self._wrapper.convert_thematic_to_numeric(p2._wrapper, p3.encode())
        




    def convert_velocity_to_density(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: str) -> None:
        self._wrapper.convert_velocity_to_density(p2, p3, p4, p5, p6, p7, p8, p9, p10.encode())
        




    def convert_velocity_in_range_to_density(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: str) -> None:
        self._wrapper.convert_velocity_in_range_to_density(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12.encode())
        




    def convert_density_to_velocity(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: str) -> None:
        self._wrapper.convert_density_to_velocity(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12.encode())
        




    def invert_z(self, p2: str) -> None:
        self._wrapper.invert_z(p2.encode())
        



    @classmethod
    def dw_grid_db(cls, p1: str, p2: 'GXDB', p3: int, p4: int, p5: int, p6: int, p7: 'GXREG') -> None:
        gxapi_cy.WrapVOX.dw_grid_db(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6, p7._wrapper)
        



    @classmethod
    def tin_grid_db(cls, p1: str, p2: 'GXDB', p3: int, p4: int, p5: int, p6: int, p7: int, p8: 'GXVV', p9: 'GXREG') -> None:
        gxapi_cy.WrapVOX.tin_grid_db(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4, p5, p6, p7, p8._wrapper, p9._wrapper)
        



    @classmethod
    def get_multi_voxset_guid(cls, p1: str, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapVOX.get_multi_voxset_guid(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def generate_gocad(cls, p1: str, p2: str, p3: str, p4: 'GXIPJ') -> 'GXVOX':
        ret_val = gxapi_cy.WrapVOX.generate_gocad(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_oriented_gocad(cls, p1: str, p2: str, p3: str, p4: 'GXIPJ', p5: int) -> 'GXVOX':
        ret_val = gxapi_cy.WrapVOX.generate_oriented_gocad(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4._wrapper, p5)
        return GXVOX(ret_val)



    @classmethod
    def generate_ubc(cls, p1: str, p2: str, p3: str, p4: float, p5: 'GXIPJ') -> 'GXVOX':
        ret_val = gxapi_cy.WrapVOX.generate_ubc(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4, p5._wrapper)
        return GXVOX(ret_val)



    @classmethod
    def generate_xyz(cls, p1: str, p2: 'GXRA', p3: int, p4: 'GXIPJ') -> None:
        gxapi_cy.WrapVOX.generate_xyz(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3, p4._wrapper)
        



    @classmethod
    def list_gocad_properties(cls, p1: str, p2: 'GXLST') -> None:
        gxapi_cy.WrapVOX.list_gocad_properties(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        




    def export_db(self, p2: 'GXDB', p3: str, p4: int, p5: int, p6: int, p7: int, p8: int) -> None:
        self._wrapper.export_db(p2._wrapper, p3.encode(), p4, p5, p6, p7, p8)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer