### extends 'class_empty.py'
from . import gxapi_cy

from geosoft.gxapi import GXContext, int_ref, float_ref, str_ref

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXIPJ:
    """
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapIPJ(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXIPJ':
        """
        A null (undefined) instance of :class:`GXIPJ`
        
        :returns: A null :class:`GX3DN`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXIPJ` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXIPJ`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clear_warp(self) -> None:
        self._wrapper.clear_warp()
        




    def make_geographic(self) -> None:
        self._wrapper.make_geographic()
        




    def make_wgs84(self) -> None:
        self._wrapper.make_wgs84()
        




    def set_units(self, p2: float, p3: str) -> None:
        self._wrapper.set_units(p2, p3.encode())
        




    def add_exagg_warp(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None:
        self._wrapper.add_exagg_warp(p2, p3, p4, p5, p6, p7)
        




    def add_log_warp(self, p2: int, p3: int) -> None:
        self._wrapper.add_log_warp(p2, p3)
        




    def add_matrix_warp(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: float, p13: float, p14: float, p15: float, p16: float, p17: float) -> None:
        self._wrapper.add_matrix_warp(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17)
        




    def add_warp(self, p2: int, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: 'GXVV') -> None:
        self._wrapper.add_warp(p2, p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper)
        




    def clear_coordinate_system(self) -> None:
        self._wrapper.clear_coordinate_system()
        




    def clear_orientation(self) -> None:
        self._wrapper.clear_orientation()
        




    def convert_orientation_warp_vv(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: int) -> None:
        self._wrapper.convert_orientation_warp_vv(p2._wrapper, p3._wrapper, p4._wrapper, p5)
        




    def copy(self, p2: 'GXIPJ') -> None:
        self._wrapper.copy(p2._wrapper)
        




    def copy_projection(self, p2: 'GXIPJ') -> None:
        self._wrapper.copy_projection(p2._wrapper)
        



    @classmethod
    def create(cls) -> 'GXIPJ':
        ret_val = gxapi_cy.WrapIPJ.create(GXContext._get_tls_geo())
        return GXIPJ(ret_val)



    @classmethod
    def create_s(cls, p1: 'GXBF') -> 'GXIPJ':
        ret_val = gxapi_cy.WrapIPJ.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXIPJ(ret_val)



    @classmethod
    def create_xml(cls, p1: str) -> 'GXIPJ':
        ret_val = gxapi_cy.WrapIPJ.create_xml(GXContext._get_tls_geo(), p1.encode())
        return GXIPJ(ret_val)






    def get_3d_view(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref, p10: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value = self._wrapper.get_3d_view(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value)
        




    def get_3d_view_ex(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: int_ref, p12: int_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value = self._wrapper.get_3d_view_ex(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value)
        




    def get_crooked_section_view_v_vs(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: int_ref) -> None:
        p5.value = self._wrapper.get_crooked_section_view_v_vs(p2._wrapper, p3._wrapper, p4._wrapper, p5.value)
        



    @classmethod
    def get_list(cls, p1: int, p2: str, p3: 'GXLST') -> None:
        gxapi_cy.WrapIPJ.get_list(GXContext._get_tls_geo(), p1, p2.encode(), p3._wrapper)
        




    def get_orientation_info(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_orientation_info(p2.value, p3.value, p4.value, p5.value, p6.value)
        




    def get_plane_equation(self, p2: float, p3: float, p4: float, p5: float, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: float_ref, p12: float_ref, p13: float_ref, p14: float_ref) -> None:
        p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value = self._wrapper.get_plane_equation(p2, p3, p4, p5, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value)
        




    def get_plane_equation2(self, p2: 'GXIPJ', p3: float, p4: float, p5: float, p6: float, p7: float_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: float_ref, p12: float_ref, p13: float_ref, p14: float_ref, p15: float_ref) -> None:
        p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value = self._wrapper.get_plane_equation2(p2._wrapper, p3, p4, p5, p6, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value)
        




    def compare_datums(self, p2: 'GXIPJ') -> int:
        ret_val = self._wrapper.compare_datums(p2._wrapper)
        return ret_val




    def convert_warp(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: int) -> int:
        ret_val, p2.value, p3.value, p4.value = self._wrapper.convert_warp(p2.value, p3.value, p4.value, p5)
        return ret_val




    def convert_warp_vv(self, p2: 'GXVV', p3: 'GXVV', p4: int) -> int:
        ret_val = self._wrapper.convert_warp_vv(p2._wrapper, p3._wrapper, p4)
        return ret_val




    def coordinate_systems_are_the_same(self, p2: 'GXIPJ') -> int:
        ret_val = self._wrapper.coordinate_systems_are_the_same(p2._wrapper)
        return ret_val




    def coordinate_systems_are_the_same_within_a_small_tolerance(self, p2: 'GXIPJ') -> int:
        ret_val = self._wrapper.coordinate_systems_are_the_same_within_a_small_tolerance(p2._wrapper)
        return ret_val




    def get_display_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_display_name(p2.value.encode())
        




    def get_esri(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_esri(p2.value.encode())
        




    def get_gxf(self, p2: str_ref, p3: str_ref, p4: str_ref, p5: str_ref, p6: str_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value = self._wrapper.get_gxf(p2.value.encode(), p3.value.encode(), p4.value.encode(), p5.value.encode(), p6.value.encode())
        




    def get_mi_coord_sys(self, p2: str_ref, p4: str_ref) -> None:
        p2.value, p4.value = self._wrapper.get_mi_coord_sys(p2.value.encode(), p4.value.encode())
        




    def get_name(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_name(p2, p3.value.encode())
        




    def set_vcs(self, p2: str) -> None:
        self._wrapper.set_vcs(p2.encode())
        




    def get_orientation(self) -> int:
        ret_val = self._wrapper.get_orientation()
        return ret_val




    def get_orientation_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_orientation_name(p2.value.encode())
        




    def get_units(self, p2: float_ref, p3: str_ref) -> None:
        p2.value, p3.value = self._wrapper.get_units(p2.value, p3.value.encode())
        




    def get_xml(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_xml(p2.value.encode())
        




    def has_projection(self) -> int:
        ret_val = self._wrapper.has_projection()
        return ret_val




    def is_3d_inverted(self) -> int:
        ret_val = self._wrapper.is_3d_inverted()
        return ret_val




    def is_3d_inverted_angles(self) -> int:
        ret_val = self._wrapper.is_3d_inverted_angles()
        return ret_val




    def is_geographic(self) -> int:
        ret_val = self._wrapper.is_geographic()
        return ret_val




    def orientations_are_the_same(self, p2: 'GXIPJ') -> int:
        ret_val = self._wrapper.orientations_are_the_same(p2._wrapper)
        return ret_val




    def orientations_are_the_same_within_a_small_tolerance(self, p2: 'GXIPJ') -> int:
        ret_val = self._wrapper.orientations_are_the_same_within_a_small_tolerance(p2._wrapper)
        return ret_val




    def has_section_orientation(self) -> int:
        ret_val = self._wrapper.has_section_orientation()
        return ret_val




    def projection_type_is_fully_supported(self) -> int:
        ret_val = self._wrapper.projection_type_is_fully_supported()
        return ret_val




    def set_gxf_safe(self, p2: str, p3: str, p4: str, p5: str, p6: str) -> int:
        ret_val = self._wrapper.set_gxf_safe(p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6.encode())
        return ret_val




    def source_type(self) -> int:
        ret_val = self._wrapper.source_type()
        return ret_val




    def support_datum_transform(self, p2: 'GXIPJ') -> int:
        ret_val = self._wrapper.support_datum_transform(p2._wrapper)
        return ret_val



    @classmethod
    def unit_name(cls, p1: float, p2: int, p3: str_ref) -> None:
        p3.value = gxapi_cy.WrapIPJ.unit_name(GXContext._get_tls_geo(), p1, p2, p3.value.encode())
        




    def warped(self) -> int:
        ret_val = self._wrapper.warped()
        return ret_val




    def warps_are_the_same(self, p2: 'GXIPJ') -> int:
        ret_val = self._wrapper.warps_are_the_same(p2._wrapper)
        return ret_val




    def warps_are_the_same_within_a_small_tolerance(self, p2: 'GXIPJ') -> int:
        ret_val = self._wrapper.warps_are_the_same_within_a_small_tolerance(p2._wrapper)
        return ret_val




    def warp_type(self) -> int:
        ret_val = self._wrapper.warp_type()
        return ret_val




    def make_projected(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.make_projected(p2, p3, p4, p5)
        




    def new_box_resolution(self, p2: 'GXIPJ', p3: float, p4: float, p5: float, p6: float, p7: float, p8: float_ref, p9: float_ref, p10: float_ref) -> None:
        p8.value, p9.value, p10.value = self._wrapper.new_box_resolution(p2._wrapper, p3, p4, p5, p6, p7, p8.value, p9.value, p10.value)
        




    def read(self, p2: int, p3: str, p4: str, p5: str) -> None:
        self._wrapper.read(p2, p3.encode(), p4.encode(), p5.encode())
        




    def get_method_parm(self, p2: int) -> float:
        ret_val = self._wrapper.get_method_parm(p2)
        return ret_val




    def get_north_azimuth(self, p2: float, p3: float) -> float:
        ret_val = self._wrapper.get_north_azimuth(p2, p3)
        return ret_val



    @classmethod
    def unit_scale(cls, p1: str, p2: float) -> float:
        ret_val = gxapi_cy.WrapIPJ.unit_scale(GXContext._get_tls_geo(), p1.encode(), p2)
        return ret_val




    def serial(self, p2: 'GXBF') -> None:
        self._wrapper.serial(p2._wrapper)
        




    def serial_fgdcxml(self, p2: str) -> None:
        self._wrapper.serial_fgdcxml(p2.encode())
        




    def serial_isoxml(self, p2: str) -> None:
        self._wrapper.serial_isoxml(p2.encode())
        




    def serial_xml(self, p2: str) -> None:
        self._wrapper.serial_xml(p2.encode())
        




    def set_3d_inverted(self, p2: int) -> None:
        self._wrapper.set_3d_inverted(p2)
        




    def set_3d_inverted_angles(self, p2: int) -> None:
        self._wrapper.set_3d_inverted_angles(p2)
        




    def set_3d_view(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float) -> None:
        self._wrapper.set_3d_view(p2, p3, p4, p5, p6, p7, p8, p9, p10)
        




    def set_3d_view_ex(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: int, p12: int) -> None:
        self._wrapper.set_3d_view_ex(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12)
        




    def set_3d_view_from_axes(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: float, p13: float) -> None:
        self._wrapper.set_3d_view_from_axes(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
        




    def set_crooked_section_view(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: int) -> None:
        self._wrapper.set_crooked_section_view(p2._wrapper, p3._wrapper, p4._wrapper, p5)
        




    def set_depth_section_view(self, p2: float) -> None:
        self._wrapper.set_depth_section_view(p2)
        




    def set_esri(self, p2: str) -> None:
        self._wrapper.set_esri(p2.encode())
        




    def set_gxf(self, p2: str, p3: str, p4: str, p5: str, p6: str) -> None:
        self._wrapper.set_gxf(p2.encode(), p3.encode(), p4.encode(), p5.encode(), p6.encode())
        




    def set_method_parm(self, p2: int, p3: float) -> None:
        self._wrapper.set_method_parm(p2, p3)
        




    def set_mi_coord_sys(self, p2: str, p3: str) -> None:
        self._wrapper.set_mi_coord_sys(p2.encode(), p3.encode())
        




    def set_normal_section_view(self, p2: float, p3: float, p4: float, p5: float, p6: float) -> None:
        self._wrapper.set_normal_section_view(p2, p3, p4, p5, p6)
        




    def set_plan_view(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.set_plan_view(p2, p3, p4, p5)
        




    def set_section_view(self, p2: float, p3: float, p4: float, p5: float, p6: float) -> None:
        self._wrapper.set_section_view(p2, p3, p4, p5, p6)
        




    def set_wms_coord_sys(self, p2: str, p3: float, p4: float, p5: float, p6: float) -> None:
        self._wrapper.set_wms_coord_sys(p2.encode(), p3, p4, p5, p6)
        




    def set_xml(self, p2: str) -> None:
        self._wrapper.set_xml(p2.encode())
        




    def get_3d_matrix_orientation(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: float_ref, p12: float_ref, p13: float_ref, p14: float_ref, p15: float_ref, p16: float_ref, p17: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value, p16.value, p17.value = self._wrapper.get_3d_matrix_orientation(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value, p12.value, p13.value, p14.value, p15.value, p16.value, p17.value)
        




    def set_3d_matrix_orientation(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: float, p13: float, p14: float, p15: float, p16: float, p17: float) -> None:
        self._wrapper.set_3d_matrix_orientation(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17)
        




    def reproject_section_grid(self, p2: 'GXIPJ', p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.reproject_section_grid(p2._wrapper, p3.value, p4.value, p5.value, p6.value, p7.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer