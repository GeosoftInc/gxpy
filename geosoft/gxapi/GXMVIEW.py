### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXAGG import GXAGG
from .GXBF import GXBF
from .GXCSYMB import GXCSYMB
from .GXDATALINKD import GXDATALINKD
from .GXITR import GXITR
from .GXMAP import GXMAP
from .GXMETA import GXMETA
from .GXREG import GXREG
from .GXTPAT import GXTPAT
from .GXVECTOR3D import GXVECTOR3D
from .GXVOXD import GXVOXD
### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXMVIEW:
    """
    GXMVIEW class.

    A view (:class:`GXMVIEW` class) has a 2-D/3-D translation matrix, a map
    projection and a clip region.  A view contains any number of
    "groups", and each "group" contains one or more graphics
    elements (entities).  Different types of groups will contain
    different types of entities:

    **Note:**

    :class:`GXCSYMB` groups (color symbols) contain data and rules for
    presenting the data as color symbols.  See ColSymbol_MVIEW
    and the :class:`GXCSYMB` class.
    
    :class:`GXAGG` groups (aggregates) contain images.  See Aggregate_MVIEW
    and the :class:`GXAGG` class.
    
    PAGG groups (poly-aggregates) contain images with multiple
    frames that make up an animation.  See PolyAggregate_MVIEW
    and the PAGG class.
    
    Standard groups contain symbols, lines, polylines, and polygons.
    See StartGroup_MVIEW.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapMVIEW(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls) -> 'GXMVIEW':
        """
        A null (undefined) instance of :class:`GXMVIEW`
        
        :returns: A null :class:`GXMVIEW`
        """
        return cls()

    def is_null(self) -> bool:
        """
        Check if the instance of :class:`GXMVIEW` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`GXMVIEW`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# 3D Entity



    def box_3d(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None:
        self._wrapper.box_3d(p2, p3, p4, p5, p6, p7)
        




    def crc_view(self, p2: int_ref, p3: str) -> None:
        p2.value = self._wrapper.crc_view(p2.value, p3.encode())
        




    def crc_view_group(self, p2: str, p3: int_ref, p4: str) -> None:
        p3.value = self._wrapper.crc_view_group(p2.encode(), p3.value, p4.encode())
        




    def cylinder_3d(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: int) -> None:
        self._wrapper.cylinder_3d(p2, p3, p4, p5, p6, p7, p8, p9, p10)
        




    def draw_object_3d(self, p2: int, p3: int, p4: int, p5: int, p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: 'GXVV', p11: 'GXVV', p12: 'GXVV', p13: 'GXVV', p14: 'GXVV') -> None:
        self._wrapper.draw_object_3d(p2, p3, p4, p5, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10._wrapper, p11._wrapper, p12._wrapper, p13._wrapper, p14._wrapper)
        




    def draw_surface_3d_ex(self, p2: str, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXVV', p10: int, p11: 'GXVV', p12: 'GXVV', p13: 'GXVV', p14: 'GXIPJ') -> None:
        self._wrapper.draw_surface_3d_ex(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10, p11._wrapper, p12._wrapper, p13._wrapper, p14._wrapper)
        




    def draw_surface_3d_from_file(self, p2: str, p3: str) -> None:
        self._wrapper.draw_surface_3d_from_file(p2.encode(), p3.encode())
        



    @classmethod
    def font_weight_lst(cls, p1: 'GXLST') -> None:
        gxapi_cy.WrapMVIEW.font_weight_lst(GXContext._get_tls_geo(), p1._wrapper)
        




    def get_agg_file_names(self, p2: str, p3: 'GXVV') -> None:
        self._wrapper.get_agg_file_names(p2.encode(), p3._wrapper)
        




    def get_meta(self, p2: str, p3: str_ref) -> 'GXMETA':
        ret_val, p3.value = self._wrapper.get_meta(p2.encode(), p3.value.encode())
        return GXMETA(ret_val)




    def measure_text(self, p2: str, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref) -> None:
        p3.value, p4.value, p5.value, p6.value = self._wrapper.measure_text(p2.encode(), p3.value, p4.value, p5.value, p6.value)
        




    def point_3d(self, p2: float, p3: float, p4: float) -> None:
        self._wrapper.point_3d(p2, p3, p4)
        




    def poly_line_3d(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.poly_line_3d(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def relocate_group(self, p2: str, p3: float, p4: float, p5: float, p6: float, p7: int) -> None:
        self._wrapper.relocate_group(p2.encode(), p3, p4, p5, p6, p7)
        




    def set_meta(self, p2: str, p3: 'GXMETA', p4: str) -> None:
        self._wrapper.set_meta(p2.encode(), p3._wrapper, p4.encode())
        




    def sphere_3d(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.sphere_3d(p2, p3, p4, p5)
        




    def update_met_afrom_group(self, p2: str, p3: 'GXMETA') -> None:
        self._wrapper.update_met_afrom_group(p2.encode(), p3._wrapper)
        




# 3D Plane



    def delete_plane(self, p2: int, p3: int) -> None:
        self._wrapper.delete_plane(p2, p3)
        




    def get_plane_clip_ply(self, p2: int, p3: 'GXPLY') -> None:
        self._wrapper.get_plane_clip_ply(p2, p3._wrapper)
        




    def get_plane_equation(self, p2: int, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref, p10: float_ref, p11: float_ref) -> None:
        p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value = self._wrapper.get_plane_equation(p2, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value, p11.value)
        




    def get_view_plane_equation(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref, p10: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value = self._wrapper.get_view_plane_equation(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10.value)
        




    def create_plane(self, p2: str) -> int:
        ret_val = self._wrapper.create_plane(p2.encode())
        return ret_val




    def find_plane(self, p2: str) -> int:
        ret_val = self._wrapper.find_plane(p2.encode())
        return ret_val




    def get_def_plane(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_def_plane(p2.value.encode())
        




    def is_view_3d(self) -> int:
        ret_val = self._wrapper.is_view_3d()
        return ret_val




    def is_section(self) -> int:
        ret_val = self._wrapper.is_section()
        return ret_val




    def list_plane_groups(self, p2: int, p3: 'GXLST') -> None:
        self._wrapper.list_plane_groups(p2, p3._wrapper)
        




    def list_planes(self, p2: 'GXLST') -> None:
        self._wrapper.list_planes(p2._wrapper)
        




    def set_all_groups_to_plane(self, p2: int) -> None:
        self._wrapper.set_all_groups_to_plane(p2)
        




    def set_all_new_groups_to_plane(self, p2: int) -> None:
        self._wrapper.set_all_new_groups_to_plane(p2)
        




    def set_def_plane(self, p2: str) -> None:
        self._wrapper.set_def_plane(p2.encode())
        




    def set_group_to_plane(self, p2: int, p3: str) -> None:
        self._wrapper.set_group_to_plane(p2, p3.encode())
        




    def set_h_3dn(self, p2: 'GX3DN') -> None:
        self._wrapper.set_h_3dn(p2._wrapper)
        




    def get_3d_point_of_view(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_3d_point_of_view(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def set_3d_point_of_view(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None:
        self._wrapper.set_3d_point_of_view(p2, p3, p4, p5, p6, p7)
        




    def set_plane_clip_ply(self, p2: int, p3: 'GXPLY') -> None:
        self._wrapper.set_plane_clip_ply(p2, p3._wrapper)
        




    def set_plane_equation(self, p2: int, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: float) -> None:
        self._wrapper.set_plane_equation(p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)
        




    def set_plane_surface(self, p2: int, p3: str) -> None:
        self._wrapper.set_plane_surface(p2, p3.encode())
        




    def set_plane_surf_info(self, p2: int, p3: int, p4: float, p5: float, p6: float, p7: float) -> None:
        self._wrapper.set_plane_surf_info(p2, p3, p4, p5, p6, p7)
        




# 3D Rendering 2D



    def define_plane_3d(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float) -> None:
        self._wrapper.define_plane_3d(p2, p3, p4, p5, p6, p7, p8, p9, p10)
        




    def define_viewer_axis_3d(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None:
        self._wrapper.define_viewer_axis_3d(p2, p3, p4, p5, p6, p7)
        




    def define_viewer_plane_3d(self, p2: float, p3: float, p4: float) -> None:
        self._wrapper.define_viewer_plane_3d(p2, p3, p4)
        




# Clipping



    def clip_poly_ex(self, p2: 'GXVV', p3: 'GXVV', p4: int, p5: int) -> None:
        self._wrapper.clip_poly_ex(p2._wrapper, p3._wrapper, p4, p5)
        




    def clip_rect_ex(self, p2: float, p3: float, p4: float, p5: float, p6: int, p7: int) -> None:
        self._wrapper.clip_rect_ex(p2, p3, p4, p5, p6, p7)
        




    def clip_clear(self) -> None:
        self._wrapper.clip_clear()
        




    def clip_groups(self, p2: int) -> None:
        self._wrapper.clip_groups(p2)
        




    def clip_marked_groups(self, p2: int) -> None:
        self._wrapper.clip_marked_groups(p2)
        




    def clip_poly(self, p2: 'GXVV', p3: 'GXVV', p4: int) -> None:
        self._wrapper.clip_poly(p2._wrapper, p3._wrapper, p4)
        




    def clip_rect(self, p2: float, p3: float, p4: float, p5: float, p6: int) -> None:
        self._wrapper.clip_rect(p2, p3, p4, p5, p6)
        




    def delete_ext_clip_ply(self, p2: int) -> None:
        self._wrapper.delete_ext_clip_ply(p2)
        




    def ext_clip_ply_list(self, p2: 'GXLST') -> None:
        self._wrapper.ext_clip_ply_list(p2._wrapper)
        




    def get_clip_ply(self, p2: 'GXPLY') -> None:
        self._wrapper.get_clip_ply(p2._wrapper)
        




    def get_ext_clip_ply(self, p2: int, p3: 'GXPLY') -> None:
        self._wrapper.get_ext_clip_ply(p2, p3._wrapper)
        




    def get_group_ext_clip_ply(self, p2: str, p3: int_ref) -> None:
        p3.value = self._wrapper.get_group_ext_clip_ply(p2.encode(), p3.value)
        




    def get_ply(self, p2: 'GXPLY') -> None:
        self._wrapper.get_ply(p2._wrapper)
        




    def group_clip_mode(self, p2: int) -> None:
        self._wrapper.group_clip_mode(p2)
        




    def get_name_ext_clip_ply(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_name_ext_clip_ply(p2, p3.value.encode())
        




    def num_ext_clip_ply(self) -> int:
        ret_val = self._wrapper.num_ext_clip_ply()
        return ret_val




    def set_ext_clip_ply(self, p2: int, p3: str, p4: 'GXPLY') -> int:
        ret_val = self._wrapper.set_ext_clip_ply(p2, p3.encode(), p4._wrapper)
        return ret_val




    def set_clip_ply(self, p2: 'GXPLY') -> None:
        self._wrapper.set_clip_ply(p2._wrapper)
        




    def set_group_ext_clip_ply(self, p2: str, p3: int) -> None:
        self._wrapper.set_group_ext_clip_ply(p2.encode(), p3)
        




# Color


    @classmethod
    def color2_rgb(cls, p1: int, p2: int_ref, p3: int_ref, p4: int_ref) -> None:
        p2.value, p3.value, p4.value = gxapi_cy.WrapMVIEW.color2_rgb(GXContext._get_tls_geo(), p1, p2.value, p3.value, p4.value)
        



    @classmethod
    def color_descr(cls, p1: int, p2: str_ref) -> None:
        p2.value = gxapi_cy.WrapMVIEW.color_descr(GXContext._get_tls_geo(), p1, p2.value.encode())
        



    @classmethod
    def color(cls, p1: str) -> int:
        ret_val = gxapi_cy.WrapMVIEW.color(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def color_cmy(cls, p1: int, p2: int, p3: int) -> int:
        ret_val = gxapi_cy.WrapMVIEW.color_cmy(GXContext._get_tls_geo(), p1, p2, p3)
        return ret_val



    @classmethod
    def color_hsv(cls, p1: int, p2: int, p3: int) -> int:
        ret_val = gxapi_cy.WrapMVIEW.color_hsv(GXContext._get_tls_geo(), p1, p2, p3)
        return ret_val



    @classmethod
    def color_rgb(cls, p1: int, p2: int, p3: int) -> int:
        ret_val = gxapi_cy.WrapMVIEW.color_rgb(GXContext._get_tls_geo(), p1, p2, p3)
        return ret_val




# Drawing Attribute



    def clip_mode(self, p2: int) -> None:
        self._wrapper.clip_mode(p2)
        




    def fill_color(self, p2: int) -> None:
        self._wrapper.fill_color(p2)
        




    def line_color(self, p2: int) -> None:
        self._wrapper.line_color(p2)
        




    def line_smooth(self, p2: int) -> None:
        self._wrapper.line_smooth(p2)
        




    def line_style(self, p2: int, p3: float) -> None:
        self._wrapper.line_style(p2, p3)
        




    def line_thick(self, p2: float) -> None:
        self._wrapper.line_thick(p2)
        




    def pat_angle(self, p2: float) -> None:
        self._wrapper.pat_angle(p2)
        




    def pat_density(self, p2: float) -> None:
        self._wrapper.pat_density(p2)
        




    def pat_number(self, p2: int) -> None:
        self._wrapper.pat_number(p2)
        




    def pat_size(self, p2: float) -> None:
        self._wrapper.pat_size(p2)
        




    def pat_style(self, p2: int) -> None:
        self._wrapper.pat_style(p2)
        




    def pat_thick(self, p2: float) -> None:
        self._wrapper.pat_thick(p2)
        




    def symb_angle(self, p2: float) -> None:
        self._wrapper.symb_angle(p2)
        




    def symb_color(self, p2: int) -> None:
        self._wrapper.symb_color(p2)
        




    def symb_fill_color(self, p2: int) -> None:
        self._wrapper.symb_fill_color(p2)
        




    def symb_font(self, p2: str, p3: int, p4: int, p5: int) -> None:
        self._wrapper.symb_font(p2.encode(), p3, p4, p5)
        




    def symb_number(self, p2: int) -> None:
        self._wrapper.symb_number(p2)
        




    def symb_size(self, p2: float) -> None:
        self._wrapper.symb_size(p2)
        




    def text_angle(self, p2: float) -> None:
        self._wrapper.text_angle(p2)
        




    def text_color(self, p2: int) -> None:
        self._wrapper.text_color(p2)
        




    def text_font(self, p2: str, p3: int, p4: int, p5: int) -> None:
        self._wrapper.text_font(p2.encode(), p3, p4, p5)
        




    def text_ref(self, p2: int) -> None:
        self._wrapper.text_ref(p2)
        




    def text_size(self, p2: float) -> None:
        self._wrapper.text_size(p2)
        




    def transparency(self, p2: float) -> None:
        self._wrapper.transparency(p2)
        




    def z_value(self, p2: float) -> None:
        self._wrapper.z_value(p2)
        




# Drawing Entity



    def arc(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float) -> None:
        self._wrapper.arc(p2, p3, p4, p5, p6, p7, p8)
        




    def chord(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float) -> None:
        self._wrapper.chord(p2, p3, p4, p5, p6, p7, p8)
        




    def classified_symbols(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV', p5: float, p6: float, p7: str, p8: str, p9: str) -> None:
        self._wrapper.classified_symbols(p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7.encode(), p8.encode(), p9.encode())
        




    def complex_polygon(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.complex_polygon(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def ellipse(self, p2: float, p3: float, p4: float, p5: float, p6: float) -> None:
        self._wrapper.ellipse(p2, p3, p4, p5, p6)
        




    def line(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.line(p2, p3, p4, p5)
        




    def line_vv(self, p2: 'GXVV') -> None:
        self._wrapper.line_vv(p2._wrapper)
        




    def polygon_dm(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.polygon_dm(p2._wrapper, p3._wrapper)
        




    def polygon_ply(self, p2: 'GXPLY') -> None:
        self._wrapper.polygon_ply(p2._wrapper)
        




    def poly_line(self, p2: int, p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.poly_line(p2, p3._wrapper, p4._wrapper)
        




    def poly_line_dm(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.poly_line_dm(p2._wrapper, p3._wrapper)
        




    def poly_wrap(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.poly_wrap(p2._wrapper, p3._wrapper)
        




    def rectangle(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.rectangle(p2, p3, p4, p5)
        




    def segment(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float) -> None:
        self._wrapper.segment(p2, p3, p4, p5, p6, p7, p8)
        




    def size_symbols(self, p2: 'GXVV', p3: 'GXVV', p4: 'GXVV') -> None:
        self._wrapper.size_symbols(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def symbol(self, p2: float, p3: float) -> None:
        self._wrapper.symbol(p2, p3)
        




    def symbols(self, p2: 'GXVV', p3: 'GXVV') -> None:
        self._wrapper.symbols(p2._wrapper, p3._wrapper)
        




    def symbols_itr(self, p2: str, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV') -> None:
        self._wrapper.symbols_itr(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper)
        




    def text(self, p2: str, p3: float, p4: float) -> None:
        self._wrapper.text(p2.encode(), p3, p4)
        




# Drawing Object



    def aggregate(self, p2: 'GXAGG', p3: str) -> None:
        self._wrapper.aggregate(p2._wrapper, p3.encode())
        




    def get_aggregate(self, p2: int) -> 'GXAGG':
        ret_val = self._wrapper.get_aggregate(p2)
        return GXAGG(ret_val)




    def change_line_message(self, p2: str) -> None:
        self._wrapper.change_line_message(p2.encode())
        




    def col_symbol(self, p2: str, p3: 'GXCSYMB') -> None:
        self._wrapper.col_symbol(p2.encode(), p3._wrapper)
        




    def get_col_symbol(self, p2: int) -> 'GXCSYMB':
        ret_val = self._wrapper.get_col_symbol(p2)
        return GXCSYMB(ret_val)




    def datalinkd(self, p2: 'GXDATALINKD', p3: str) -> None:
        self._wrapper.datalinkd(p2._wrapper, p3.encode())
        




    def get_datalinkd(self, p2: int) -> 'GXDATALINKD':
        ret_val = self._wrapper.get_datalinkd(p2)
        return GXDATALINKD(ret_val)




    def easy_maker(self, p2: str, p3: str) -> None:
        self._wrapper.easy_maker(p2.encode(), p3.encode())
        




    def emf_object(self, p2: float, p3: float, p4: float, p5: float, p6: str) -> None:
        self._wrapper.emf_object(p2, p3, p4, p5, p6.encode())
        




    def external_string_object(self, p2: float, p3: float, p4: float, p5: float, p6: str, p7: str, p8: str) -> None:
        self._wrapper.external_string_object(p2, p3, p4, p5, p6.encode(), p7.encode(), p8.encode())
        




    def link(self, p2: 'GXDB', p3: str) -> None:
        self._wrapper.link(p2._wrapper, p3.encode())
        




    def maker(self, p2: int, p3: int, p4: str, p5: int, p6: str, p7: str) -> None:
        self._wrapper.maker(p2, p3, p4.encode(), p5, p6.encode(), p7.encode())
        




    def meta(self, p2: 'GXMETA', p3: str) -> None:
        self._wrapper.meta(p2._wrapper, p3.encode())
        




    def voxd(self, p2: 'GXVOXD', p3: str) -> None:
        self._wrapper.voxd(p2._wrapper, p3.encode())
        




    def get_voxd(self, p2: int) -> 'GXVOXD':
        ret_val = self._wrapper.get_voxd(p2)
        return GXVOXD(ret_val)




    def draw_vector_voxel_vectors(self, p2: 'GXVOX', p3: str, p4: 'GXITR', p5: float, p6: float, p7: float, p8: float, p9: int) -> None:
        self._wrapper.draw_vector_voxel_vectors(p2._wrapper, p3.encode(), p4._wrapper, p5, p6, p7, p8, p9)
        




    def get_vector_3d(self, p2: int) -> 'GXVECTOR3D':
        ret_val = self._wrapper.get_vector_3d(p2)
        return GXVECTOR3D(ret_val)




    def draw_vectors_3d(self, p2: str, p3: 'GXVV', p4: 'GXVV', p5: 'GXVV', p6: 'GXVV', p7: 'GXVV', p8: 'GXVV', p9: 'GXITR', p10: float, p11: float, p12: float) -> None:
        self._wrapper.draw_vectors_3d(p2.encode(), p3._wrapper, p4._wrapper, p5._wrapper, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper, p10, p11, p12)
        




# Group Methods



    def set_group_itr(self, p2: int, p3: 'GXITR') -> None:
        self._wrapper.set_group_itr(p2, p3._wrapper)
        




    def get_group_itr(self, p2: int) -> 'GXITR':
        ret_val = self._wrapper.get_group_itr(p2)
        return GXITR(ret_val)




    def group_itr_exists(self, p2: int) -> int:
        ret_val = self._wrapper.group_itr_exists(p2)
        return ret_val




    def delete_group_itr(self, p2: int) -> None:
        self._wrapper.delete_group_itr(p2)
        




    def set_group_tpat(self, p2: int, p3: 'GXTPAT') -> None:
        self._wrapper.set_group_tpat(p2, p3._wrapper)
        




    def get_group_tpat(self, p2: int) -> 'GXTPAT':
        ret_val = self._wrapper.get_group_tpat(p2)
        return GXTPAT(ret_val)




    def group_tpat_exists(self, p2: int) -> int:
        ret_val = self._wrapper.group_tpat_exists(p2)
        return ret_val




    def delete_group_tpat(self, p2: int) -> None:
        self._wrapper.delete_group_tpat(p2)
        




    def group_storage_exists(self, p2: int, p3: str) -> int:
        ret_val = self._wrapper.group_storage_exists(p2, p3.encode())
        return ret_val




    def read_group_storage(self, p2: int, p3: str) -> 'GXBF':
        ret_val = self._wrapper.read_group_storage(p2, p3.encode())
        return GXBF(ret_val)




    def delete_group_storage(self, p2: int, p3: str) -> None:
        self._wrapper.delete_group_storage(p2, p3.encode())
        




    def write_group_storage(self, p2: int, p3: str, p4: 'GXBF') -> None:
        self._wrapper.write_group_storage(p2, p3.encode(), p4._wrapper)
        




    def copy_marked_groups(self, p2: 'GXMVIEW') -> None:
        self._wrapper.copy_marked_groups(p2._wrapper)
        




    def copy_raw_marked_groups(self, p2: 'GXMVIEW') -> None:
        self._wrapper.copy_raw_marked_groups(p2._wrapper)
        




    def crc_group(self, p2: str, p3: int) -> int:
        ret_val = self._wrapper.crc_group(p2.encode(), p3)
        return ret_val




    def delete_group(self, p2: str) -> None:
        self._wrapper.delete_group(p2.encode())
        




    def del_marked_groups(self) -> None:
        self._wrapper.del_marked_groups()
        




    def get_group_extent(self, p2: str, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: int) -> None:
        p3.value, p4.value, p5.value, p6.value = self._wrapper.get_group_extent(p2.encode(), p3.value, p4.value, p5.value, p6.value, p7)
        




    def get_group_transparency(self, p2: str, p3: float_ref) -> None:
        p3.value = self._wrapper.get_group_transparency(p2.encode(), p3.value)
        




    def group_to_ply(self, p2: str, p3: 'GXPLY') -> None:
        self._wrapper.group_to_ply(p2.encode(), p3._wrapper)
        




    def hide_marked_groups(self, p2: int) -> None:
        self._wrapper.hide_marked_groups(p2)
        




    def hide_shadow2_d_interpretations(self, p2: int) -> None:
        self._wrapper.hide_shadow2_d_interpretations(p2)
        




    def exist_group(self, p2: str) -> int:
        ret_val = self._wrapper.exist_group(p2.encode())
        return ret_val




    def gen_new_group_name(self, p2: str, p3: str_ref) -> None:
        p3.value = self._wrapper.gen_new_group_name(p2.encode(), p3.value.encode())
        




    def is_group(self, p2: str, p3: int) -> int:
        ret_val = self._wrapper.is_group(p2.encode(), p3)
        return ret_val




    def is_group_empty(self, p2: str) -> int:
        ret_val = self._wrapper.is_group_empty(p2.encode())
        return ret_val




    def is_movable(self) -> int:
        ret_val = self._wrapper.is_movable()
        return ret_val




    def is_visible(self) -> int:
        ret_val = self._wrapper.is_visible()
        return ret_val




    def list_groups(self, p2: 'GXLST', p3: int) -> int:
        ret_val = self._wrapper.list_groups(p2._wrapper, p3)
        return ret_val




    def render_order(self) -> int:
        ret_val = self._wrapper.render_order()
        return ret_val




    def mark_all_groups(self, p2: int) -> None:
        self._wrapper.mark_all_groups(p2)
        




    def mark_empty_groups(self, p2: int) -> None:
        self._wrapper.mark_empty_groups(p2)
        




    def mark_group(self, p2: str, p3: int) -> None:
        self._wrapper.mark_group(p2.encode(), p3)
        




    def move_group_backward(self, p2: str) -> None:
        self._wrapper.move_group_backward(p2.encode())
        




    def move_group_forward(self, p2: str) -> None:
        self._wrapper.move_group_forward(p2.encode())
        




    def move_group_to_back(self, p2: str) -> None:
        self._wrapper.move_group_to_back(p2.encode())
        




    def move_group_to_front(self, p2: str) -> None:
        self._wrapper.move_group_to_front(p2.encode())
        




    def rename_group(self, p2: str, p3: str) -> None:
        self._wrapper.rename_group(p2.encode(), p3.encode())
        




    def set_group_moveable(self, p2: str, p3: int) -> None:
        self._wrapper.set_group_moveable(p2.encode(), p3)
        




    def set_group_transparency(self, p2: str, p3: float) -> None:
        self._wrapper.set_group_transparency(p2.encode(), p3)
        




    def set_mark_moveable(self, p2: int) -> None:
        self._wrapper.set_mark_moveable(p2)
        




    def set_movability(self, p2: int) -> None:
        self._wrapper.set_movability(p2)
        




    def set_render_order(self, p2: int) -> None:
        self._wrapper.set_render_order(p2)
        




    def set_visibility(self, p2: int) -> None:
        self._wrapper.set_visibility(p2)
        




    def start_group(self, p2: str, p3: int) -> None:
        self._wrapper.start_group(p2.encode(), p3)
        




    def get_group_guid(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.get_group_guid(p2, p3.value.encode())
        




    def find_group_by_guid(self, p2: str) -> int:
        ret_val = self._wrapper.find_group_by_guid(p2.encode())
        return ret_val




# Projection



    def set_working_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.set_working_ipj(p2._wrapper)
        




    def clear_esrild_ts(self) -> None:
        self._wrapper.clear_esrild_ts()
        




    def is_projection_empty(self) -> int:
        ret_val = self._wrapper.is_projection_empty()
        return ret_val




    def get_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.get_ipj(p2._wrapper)
        




    def get_user_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.get_user_ipj(p2._wrapper)
        




    def mode_pj(self, p2: int) -> None:
        self._wrapper.mode_pj(p2)
        




    def north(self) -> float:
        ret_val = self._wrapper.north()
        return ret_val




    def set_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.set_ipj(p2._wrapper)
        




    def set_user_ipj(self, p2: 'GXIPJ') -> None:
        self._wrapper.set_user_ipj(p2._wrapper)
        




# Render



    def get_3d_group_flags(self, p2: int) -> int:
        ret_val = self._wrapper.get_3d_group_flags(p2)
        return ret_val




    def set_3d_group_flags(self, p2: int, p3: int) -> None:
        self._wrapper.set_3d_group_flags(p2, p3)
        




    def get_group_freeze_scale(self, p2: int, p3: float_ref) -> None:
        p3.value = self._wrapper.get_group_freeze_scale(p2, p3.value)
        




    def set_freeze_scale(self, p2: float) -> None:
        self._wrapper.set_freeze_scale(p2)
        




    def set_group_freeze_scale(self, p2: int, p3: float) -> None:
        self._wrapper.set_group_freeze_scale(p2, p3)
        




    def find_group(self, p2: str) -> int:
        ret_val = self._wrapper.find_group(p2.encode())
        return ret_val




    def group_name(self, p2: int, p3: str_ref) -> None:
        p3.value = self._wrapper.group_name(p2, p3.value.encode())
        




    def render(self, p2: int, p3: int, p4: int, p5: int, p6: int, p7: float, p8: float, p9: float, p10: float) -> None:
        self._wrapper.render(p2, p3, p4, p5, p6, p7, p8, p9, p10)
        




# Utility Drawing



    def set_u_fac(self, p2: float) -> None:
        self._wrapper.set_u_fac(p2)
        




    def axis_x(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None:
        self._wrapper.axis_x(p2, p3, p4, p5, p6, p7)
        




    def axis_y(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None:
        self._wrapper.axis_y(p2, p3, p4, p5, p6, p7)
        




    def grid(self, p2: float, p3: float, p4: float, p5: float, p6: int) -> None:
        self._wrapper.grid(p2, p3, p4, p5, p6)
        




    def label_fid(self, p2: 'GXVV', p3: float, p4: float, p5: float, p6: float, p7: float) -> None:
        self._wrapper.label_fid(p2._wrapper, p3, p4, p5, p6, p7)
        




    def label_x(self, p2: float, p3: float, p4: float, p5: float, p6: int, p7: int, p8: int) -> None:
        self._wrapper.label_x(p2, p3, p4, p5, p6, p7, p8)
        




    def label_y(self, p2: float, p3: float, p4: float, p5: float, p6: int, p7: int, p8: int) -> None:
        self._wrapper.label_y(p2, p3, p4, p5, p6, p7, p8)
        



    @classmethod
    def optimum_tick(cls, p1: float, p2: float, p3: float_ref) -> None:
        p3.value = gxapi_cy.WrapMVIEW.optimum_tick(GXContext._get_tls_geo(), p1, p2, p3.value)
        




# View


    @classmethod
    def create(cls, p1: 'GXMAP', p2: str, p3: int) -> 'GXMVIEW':
        ret_val = gxapi_cy.WrapMVIEW.create(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3)
        return GXMVIEW(ret_val)



    @classmethod
    def create_crooked_section(cls, p1: 'GXMAP', p2: 'GXIPJ', p3: str, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: 'GXVV', p13: 'GXVV', p14: 'GXVV') -> 'GXMVIEW':
        ret_val = gxapi_cy.WrapMVIEW.create_crooked_section(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode(), p4, p5, p6, p7, p8, p9, p10, p11, p12._wrapper, p13._wrapper, p14._wrapper)
        return GXMVIEW(ret_val)



    @classmethod
    def create_crooked_section_data_profile(cls, p1: 'GXMAP', p2: 'GXIPJ', p3: str, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float, p10: float, p11: float, p12: int, p13: 'GXVV', p14: 'GXVV', p15: 'GXVV') -> 'GXMVIEW':
        ret_val = gxapi_cy.WrapMVIEW.create_crooked_section_data_profile(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.encode(), p4, p5, p6, p7, p8, p9, p10, p11, p12, p13._wrapper, p14._wrapper, p15._wrapper)
        return GXMVIEW(ret_val)






    def extent(self, p2: int, p3: int, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref) -> None:
        p4.value, p5.value, p6.value, p7.value = self._wrapper.extent(p2, p3, p4.value, p5.value, p6.value, p7.value)
        




    def get_map(self) -> 'GXMAP':
        ret_val = self._wrapper.get_map()
        return GXMAP(ret_val)




    def get_reg(self) -> 'GXREG':
        ret_val = self._wrapper.get_reg()
        return GXREG(ret_val)




    def get_name(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_name(p2.value.encode())
        




    def get_guid(self, p2: str_ref) -> None:
        p2.value = self._wrapper.get_guid(p2.value.encode())
        




# View Control



    def plot_to_view(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.plot_to_view(p2.value, p3.value)
        




    def set_thin_res(self, p2: float) -> None:
        self._wrapper.set_thin_res(p2)
        




    def view_to_plot(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.view_to_plot(p2.value, p3.value)
        




    def best_fit_window(self, p2: float_ref, p3: float_ref, p4: float_ref, p5: float_ref, p6: float_ref, p7: float_ref, p8: float_ref, p9: float_ref, p10: int) -> None:
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value = self._wrapper.best_fit_window(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value, p8.value, p9.value, p10)
        




    def fit_map_window_3d(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float) -> None:
        self._wrapper.fit_map_window_3d(p2, p3, p4, p5, p6, p7, p8, p9)
        




    def fit_window(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float) -> None:
        self._wrapper.fit_window(p2, p3, p4, p5, p6, p7, p8, p9)
        




    def get_class_name(self, p2: str, p3: str_ref) -> None:
        p3.value = self._wrapper.get_class_name(p2.encode(), p3.value.encode())
        




    def map_origin(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.map_origin(p2.value, p3.value)
        




    def re_scale(self, p2: float) -> None:
        self._wrapper.re_scale(p2)
        




    def get_map_scale(self) -> float:
        ret_val = self._wrapper.get_map_scale()
        return ret_val




    def scale_mm(self) -> float:
        ret_val = self._wrapper.scale_mm()
        return ret_val




    def scale_pj_mm(self) -> float:
        ret_val = self._wrapper.scale_pj_mm()
        return ret_val




    def scale_ymm(self) -> float:
        ret_val = self._wrapper.scale_ymm()
        return ret_val




    def scale_all_group(self, p2: float, p3: float) -> None:
        self._wrapper.scale_all_group(p2, p3)
        




    def scale_window(self, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float, p8: float, p9: float) -> None:
        self._wrapper.scale_window(p2, p3, p4, p5, p6, p7, p8, p9)
        




    def set_class_name(self, p2: str, p3: str) -> None:
        self._wrapper.set_class_name(p2.encode(), p3.encode())
        




    def set_window(self, p2: float, p3: float, p4: float, p5: float, p6: int) -> None:
        self._wrapper.set_window(p2, p3, p4, p5, p6)
        




    def tran_scale(self, p2: float, p3: float, p4: float, p5: float) -> None:
        self._wrapper.tran_scale(p2, p3, p4, p5)
        




    def user_to_view(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.user_to_view(p2.value, p3.value)
        




    def view_to_user(self, p2: float_ref, p3: float_ref) -> None:
        p2.value, p3.value = self._wrapper.view_to_user(p2.value, p3.value)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer