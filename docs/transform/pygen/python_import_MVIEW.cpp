#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXMVIEW_wrap_box_3d(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6)
{
    self->box_3d(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXMVIEW_wrap_crc_view(GXMVIEWPtr self, int_ref& arg1, const gx_string_type& arg2)
{
    self->crc_view(arg1, arg2);
}
inline void GXMVIEW_wrap_crc_view_group(GXMVIEWPtr self, const gx_string_type& arg1, int_ref& arg2, const gx_string_type& arg3)
{
    self->crc_view_group(arg1, arg2, arg3);
}
inline void GXMVIEW_wrap_cylinder_3d(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, int32_t arg9)
{
    self->cylinder_3d(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, (MVIEW_CYLINDER3D)arg9);
}
inline void GXMVIEW_wrap_draw_object_3d(GXMVIEWPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, GXVVPtr arg10, GXVVPtr arg11, GXVVPtr arg12, GXVVPtr arg13)
{
    self->draw_object_3d((MVIEW_DRAWOBJ3D_ENTITY)arg1, (MVIEW_DRAWOBJ3D_MODE)arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13);
}
inline void GXMVIEW_wrap_draw_surface_3d_ex(GXMVIEWPtr self, const gx_string_type& arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7, GXVVPtr arg8, int32_t arg9, GXVVPtr arg10, GXVVPtr arg11, GXVVPtr arg12, GXIPJPtr arg13)
{
    self->draw_surface_3d_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13);
}
inline void GXMVIEW_wrap_draw_surface_3d_from_file(GXMVIEWPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->draw_surface_3d_from_file(arg1, arg2);
}
inline void GXMVIEW_wrap_font_weight_lst(GXLSTPtr arg1)
{
    GXMVIEW::font_weight_lst(arg1);
}
inline void GXMVIEW_wrap_get_agg_file_names(GXMVIEWPtr self, const gx_string_type& arg1, GXVVPtr arg2)
{
    self->get_agg_file_names(arg1, arg2);
}
inline GXMETAPtr GXMVIEW_wrap_get_meta(GXMVIEWPtr self, const gx_string_type& arg1, str_ref& arg2)
{
    GXMETAPtr ret = self->get_meta(arg1, arg2);
    return ret;
}
inline void GXMVIEW_wrap_measure_text(GXMVIEWPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    self->measure_text(arg1, arg2, arg3, arg4, arg5);
}
inline void GXMVIEW_wrap_point_3d(GXMVIEWPtr self, double arg1, double arg2, double arg3)
{
    self->point_3d(arg1, arg2, arg3);
}
inline void GXMVIEW_wrap_poly_line_3d(GXMVIEWPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->poly_line_3d(arg1, arg2, arg3);
}
inline void GXMVIEW_wrap_relocate_group(GXMVIEWPtr self, const gx_string_type& arg1, double arg2, double arg3, double arg4, double arg5, int32_t arg6)
{
    self->relocate_group(arg1, arg2, arg3, arg4, arg5, (MVIEW_RELOCATE)arg6);
}
inline void GXMVIEW_wrap_set_meta(GXMVIEWPtr self, const gx_string_type& arg1, GXMETAPtr arg2, const gx_string_type& arg3)
{
    self->set_meta(arg1, arg2, arg3);
}
inline void GXMVIEW_wrap_sphere_3d(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->sphere_3d(arg1, arg2, arg3, arg4);
}
inline void GXMVIEW_wrap_update_met_afrom_group(GXMVIEWPtr self, const gx_string_type& arg1, GXMETAPtr arg2)
{
    self->update_met_afrom_group(arg1, arg2);
}
inline void GXMVIEW_wrap_delete_plane(GXMVIEWPtr self, int32_t arg1, int32_t arg2)
{
    self->delete_plane(arg1, arg2);
}
inline void GXMVIEW_wrap_get_plane_clip_ply(GXMVIEWPtr self, int32_t arg1, GXPLYPtr arg2)
{
    self->get_plane_clip_ply(arg1, arg2);
}
inline void GXMVIEW_wrap_get_plane_equation(GXMVIEWPtr self, int32_t arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9, float_ref& arg10)
{
    self->get_plane_equation(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXMVIEW_wrap_get_view_plane_equation(GXMVIEWPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9)
{
    self->get_view_plane_equation(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline int32_t GXMVIEW_wrap_create_plane(GXMVIEWPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->create_plane(arg1);
    return ret;
}
inline int32_t GXMVIEW_wrap_find_plane(GXMVIEWPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->find_plane(arg1);
    return ret;
}
inline void GXMVIEW_wrap_get_def_plane(GXMVIEWPtr self, str_ref& arg1)
{
    self->get_def_plane(arg1);
}
inline int32_t GXMVIEW_wrap_is_view_3d(GXMVIEWPtr self)
{
    int32_t ret = self->is_view_3d();
    return ret;
}
inline int32_t GXMVIEW_wrap_is_section(GXMVIEWPtr self)
{
    int32_t ret = self->is_section();
    return ret;
}
inline void GXMVIEW_wrap_list_plane_groups(GXMVIEWPtr self, int32_t arg1, GXLSTPtr arg2)
{
    self->list_plane_groups(arg1, arg2);
}
inline void GXMVIEW_wrap_list_planes(GXMVIEWPtr self, GXLSTPtr arg1)
{
    self->list_planes(arg1);
}
inline void GXMVIEW_wrap_set_all_groups_to_plane(GXMVIEWPtr self, int32_t arg1)
{
    self->set_all_groups_to_plane(arg1);
}
inline void GXMVIEW_wrap_set_all_new_groups_to_plane(GXMVIEWPtr self, int32_t arg1)
{
    self->set_all_new_groups_to_plane(arg1);
}
inline void GXMVIEW_wrap_set_def_plane(GXMVIEWPtr self, const gx_string_type& arg1)
{
    self->set_def_plane(arg1);
}
inline void GXMVIEW_wrap_set_group_to_plane(GXMVIEWPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_group_to_plane(arg1, arg2);
}
inline void GXMVIEW_wrap_set_h_3dn(GXMVIEWPtr self, GX3DNPtr arg1)
{
    self->set_h_3dn(arg1);
}
inline void GXMVIEW_wrap_set_plane_clip_ply(GXMVIEWPtr self, int32_t arg1, GXPLYPtr arg2)
{
    self->set_plane_clip_ply(arg1, arg2);
}
inline void GXMVIEW_wrap_set_plane_equation(GXMVIEWPtr self, int32_t arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10)
{
    self->set_plane_equation(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXMVIEW_wrap_set_plane_surface(GXMVIEWPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_plane_surface(arg1, arg2);
}
inline void GXMVIEW_wrap_set_plane_surf_info(GXMVIEWPtr self, int32_t arg1, int32_t arg2, double arg3, double arg4, double arg5, double arg6)
{
    self->set_plane_surf_info(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXMVIEW_wrap_define_plane_3d(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9)
{
    self->define_plane_3d(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXMVIEW_wrap_define_viewer_axis_3d(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6)
{
    self->define_viewer_axis_3d(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXMVIEW_wrap_define_viewer_plane_3d(GXMVIEWPtr self, double arg1, double arg2, double arg3)
{
    self->define_viewer_plane_3d(arg1, arg2, arg3);
}
inline void GXMVIEW_wrap_clip_poly_ex(GXMVIEWPtr self, GXVVPtr arg1, GXVVPtr arg2, int32_t arg3, int32_t arg4)
{
    self->clip_poly_ex(arg1, arg2, (MVIEW_UNIT)arg3, arg4);
}
inline void GXMVIEW_wrap_clip_rect_ex(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, int32_t arg5, int32_t arg6)
{
    self->clip_rect_ex(arg1, arg2, arg3, arg4, (MVIEW_UNIT)arg5, arg6);
}
inline void GXMVIEW_wrap_clip_clear(GXMVIEWPtr self)
{
    self->clip_clear();
}
inline void GXMVIEW_wrap_clip_groups(GXMVIEWPtr self, int32_t arg1)
{
    self->clip_groups((MVIEW_CLIP)arg1);
}
inline void GXMVIEW_wrap_clip_marked_groups(GXMVIEWPtr self, int32_t arg1)
{
    self->clip_marked_groups((MVIEW_CLIP)arg1);
}
inline void GXMVIEW_wrap_clip_poly(GXMVIEWPtr self, GXVVPtr arg1, GXVVPtr arg2, int32_t arg3)
{
    self->clip_poly(arg1, arg2, (MVIEW_UNIT)arg3);
}
inline void GXMVIEW_wrap_clip_rect(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, int32_t arg5)
{
    self->clip_rect(arg1, arg2, arg3, arg4, (MVIEW_UNIT)arg5);
}
inline void GXMVIEW_wrap_delete_ext_clip_ply(GXMVIEWPtr self, int32_t arg1)
{
    self->delete_ext_clip_ply(arg1);
}
inline void GXMVIEW_wrap_ext_clip_ply_list(GXMVIEWPtr self, GXLSTPtr arg1)
{
    self->ext_clip_ply_list(arg1);
}
inline void GXMVIEW_wrap_get_clip_ply(GXMVIEWPtr self, GXPLYPtr arg1)
{
    self->get_clip_ply(arg1);
}
inline void GXMVIEW_wrap_get_ext_clip_ply(GXMVIEWPtr self, int32_t arg1, GXPLYPtr arg2)
{
    self->get_ext_clip_ply(arg1, arg2);
}
inline void GXMVIEW_wrap_get_group_ext_clip_ply(GXMVIEWPtr self, const gx_string_type& arg1, int_ref& arg2)
{
    self->get_group_ext_clip_ply(arg1, arg2);
}
inline void GXMVIEW_wrap_get_ply(GXMVIEWPtr self, GXPLYPtr arg1)
{
    self->get_ply(arg1);
}
inline void GXMVIEW_wrap_group_clip_mode(GXMVIEWPtr self, int32_t arg1)
{
    self->group_clip_mode((MVIEW_CLIP)arg1);
}
inline void GXMVIEW_wrap_get_name_ext_clip_ply(GXMVIEWPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_name_ext_clip_ply(arg1, arg2);
}
inline int32_t GXMVIEW_wrap_num_ext_clip_ply(GXMVIEWPtr self)
{
    int32_t ret = self->num_ext_clip_ply();
    return ret;
}
inline int32_t GXMVIEW_wrap_set_ext_clip_ply(GXMVIEWPtr self, int32_t arg1, const gx_string_type& arg2, GXPLYPtr arg3)
{
    int32_t ret = self->set_ext_clip_ply(arg1, arg2, arg3);
    return ret;
}
inline void GXMVIEW_wrap_set_clip_ply(GXMVIEWPtr self, GXPLYPtr arg1)
{
    self->set_clip_ply(arg1);
}
inline void GXMVIEW_wrap_set_group_ext_clip_ply(GXMVIEWPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->set_group_ext_clip_ply(arg1, arg2);
}
inline void GXMVIEW_wrap_color2_rgb(int32_t arg1, int_ref& arg2, int_ref& arg3, int_ref& arg4)
{
    GXMVIEW::color2_rgb(arg1, arg2, arg3, arg4);
}
inline void GXMVIEW_wrap_color_descr(int32_t arg1, str_ref& arg2)
{
    GXMVIEW::color_descr(arg1, arg2);
}
inline int32_t GXMVIEW_wrap_color(const gx_string_type& arg1)
{
    int32_t ret = GXMVIEW::color(arg1);
    return ret;
}
inline int32_t GXMVIEW_wrap_color_cmy(int32_t arg1, int32_t arg2, int32_t arg3)
{
    int32_t ret = GXMVIEW::color_cmy(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXMVIEW_wrap_color_hsv(int32_t arg1, int32_t arg2, int32_t arg3)
{
    int32_t ret = GXMVIEW::color_hsv(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXMVIEW_wrap_color_rgb(int32_t arg1, int32_t arg2, int32_t arg3)
{
    int32_t ret = GXMVIEW::color_rgb(arg1, arg2, arg3);
    return ret;
}
inline void GXMVIEW_wrap_clip_mode(GXMVIEWPtr self, int32_t arg1)
{
    self->clip_mode((MVIEW_CLIP)arg1);
}
inline void GXMVIEW_wrap_fill_color(GXMVIEWPtr self, int32_t arg1)
{
    self->fill_color(arg1);
}
inline void GXMVIEW_wrap_line_color(GXMVIEWPtr self, int32_t arg1)
{
    self->line_color(arg1);
}
inline void GXMVIEW_wrap_line_smooth(GXMVIEWPtr self, int32_t arg1)
{
    self->line_smooth((MVIEW_SMOOTH)arg1);
}
inline void GXMVIEW_wrap_line_style(GXMVIEWPtr self, int32_t arg1, double arg2)
{
    self->line_style(arg1, arg2);
}
inline void GXMVIEW_wrap_line_thick(GXMVIEWPtr self, double arg1)
{
    self->line_thick(arg1);
}
inline void GXMVIEW_wrap_pat_angle(GXMVIEWPtr self, double arg1)
{
    self->pat_angle(arg1);
}
inline void GXMVIEW_wrap_pat_density(GXMVIEWPtr self, double arg1)
{
    self->pat_density(arg1);
}
inline void GXMVIEW_wrap_pat_number(GXMVIEWPtr self, int32_t arg1)
{
    self->pat_number(arg1);
}
inline void GXMVIEW_wrap_pat_size(GXMVIEWPtr self, double arg1)
{
    self->pat_size(arg1);
}
inline void GXMVIEW_wrap_pat_style(GXMVIEWPtr self, int32_t arg1)
{
    self->pat_style((MVIEW_TILE)arg1);
}
inline void GXMVIEW_wrap_pat_thick(GXMVIEWPtr self, double arg1)
{
    self->pat_thick(arg1);
}
inline void GXMVIEW_wrap_symb_angle(GXMVIEWPtr self, double arg1)
{
    self->symb_angle(arg1);
}
inline void GXMVIEW_wrap_symb_color(GXMVIEWPtr self, int32_t arg1)
{
    self->symb_color(arg1);
}
inline void GXMVIEW_wrap_symb_fill_color(GXMVIEWPtr self, int32_t arg1)
{
    self->symb_fill_color(arg1);
}
inline void GXMVIEW_wrap_symb_font(GXMVIEWPtr self, const gx_string_type& arg1, bool arg2, int32_t arg3, bool arg4)
{
    self->symb_font(arg1, arg2, (MVIEW_FONT_WEIGHT)arg3, arg4);
}
inline void GXMVIEW_wrap_symb_number(GXMVIEWPtr self, int32_t arg1)
{
    self->symb_number(arg1);
}
inline void GXMVIEW_wrap_symb_size(GXMVIEWPtr self, double arg1)
{
    self->symb_size(arg1);
}
inline void GXMVIEW_wrap_text_angle(GXMVIEWPtr self, double arg1)
{
    self->text_angle(arg1);
}
inline void GXMVIEW_wrap_text_color(GXMVIEWPtr self, int32_t arg1)
{
    self->text_color(arg1);
}
inline void GXMVIEW_wrap_text_font(GXMVIEWPtr self, const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    self->text_font(arg1, arg2, (MVIEW_FONT_WEIGHT)arg3, arg4);
}
inline void GXMVIEW_wrap_text_ref(GXMVIEWPtr self, int32_t arg1)
{
    self->text_ref((TEXT_REF)arg1);
}
inline void GXMVIEW_wrap_text_size(GXMVIEWPtr self, double arg1)
{
    self->text_size(arg1);
}
inline void GXMVIEW_wrap_transparency(GXMVIEWPtr self, double arg1)
{
    self->transparency(arg1);
}
inline void GXMVIEW_wrap_z_value(GXMVIEWPtr self, double arg1)
{
    self->z_value(arg1);
}
inline void GXMVIEW_wrap_arc(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7)
{
    self->arc(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXMVIEW_wrap_chord(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7)
{
    self->chord(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXMVIEW_wrap_classified_symbols(GXMVIEWPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, double arg4, double arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8)
{
    self->classified_symbols(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXMVIEW_wrap_complex_polygon(GXMVIEWPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->complex_polygon(arg1, arg2, arg3);
}
inline void GXMVIEW_wrap_ellipse(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, double arg5)
{
    self->ellipse(arg1, arg2, arg3, arg4, arg5);
}
inline void GXMVIEW_wrap_line(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->line(arg1, arg2, arg3, arg4);
}
inline void GXMVIEW_wrap_line_vv(GXMVIEWPtr self, GXVVPtr arg1)
{
    self->line_vv(arg1);
}
inline void GXMVIEW_wrap_polygon_dm(GXMVIEWPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->polygon_dm(arg1, arg2);
}
inline void GXMVIEW_wrap_polygon_ply(GXMVIEWPtr self, GXPLYPtr arg1)
{
    self->polygon_ply(arg1);
}
inline void GXMVIEW_wrap_poly_line(GXMVIEWPtr self, int32_t arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->poly_line((MVIEW_DRAW)arg1, arg2, arg3);
}
inline void GXMVIEW_wrap_poly_line_dm(GXMVIEWPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->poly_line_dm(arg1, arg2);
}
inline void GXMVIEW_wrap_poly_wrap(GXMVIEWPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->poly_wrap(arg1, arg2);
}
inline void GXMVIEW_wrap_rectangle(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->rectangle(arg1, arg2, arg3, arg4);
}
inline void GXMVIEW_wrap_segment(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7)
{
    self->segment(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXMVIEW_wrap_size_symbols(GXMVIEWPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->size_symbols(arg1, arg2, arg3);
}
inline void GXMVIEW_wrap_symbol(GXMVIEWPtr self, double arg1, double arg2)
{
    self->symbol(arg1, arg2);
}
inline void GXMVIEW_wrap_symbols(GXMVIEWPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->symbols(arg1, arg2);
}
inline void GXMVIEW_wrap_symbols_itr(GXMVIEWPtr self, const gx_string_type& arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4)
{
    self->symbols_itr(arg1, arg2, arg3, arg4);
}
inline void GXMVIEW_wrap_text(GXMVIEWPtr self, const gx_string_type& arg1, double arg2, double arg3)
{
    self->text(arg1, arg2, arg3);
}
inline void GXMVIEW_wrap_aggregate(GXMVIEWPtr self, GXAGGPtr arg1, const gx_string_type& arg2)
{
    self->aggregate(arg1, arg2);
}
inline void GXMVIEW_wrap_change_line_message(GXMVIEWPtr self, const gx_string_type& arg1)
{
    self->change_line_message(arg1);
}
inline void GXMVIEW_wrap_col_symbol(GXMVIEWPtr self, const gx_string_type& arg1, GXCSYMBPtr arg2)
{
    self->col_symbol(arg1, arg2);
}
inline void GXMVIEW_wrap_datalinkd(GXMVIEWPtr self, GXDATALINKDPtr arg1, const gx_string_type& arg2)
{
    self->datalinkd(arg1, arg2);
}
inline void GXMVIEW_wrap_easy_maker(GXMVIEWPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->easy_maker(arg1, arg2);
}
inline void GXMVIEW_wrap_emf_object(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, const gx_string_type& arg5)
{
    self->emf_object(arg1, arg2, arg3, arg4, arg5);
}
inline void GXMVIEW_wrap_external_string_object(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7)
{
    self->external_string_object(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXMVIEW_wrap_link(GXMVIEWPtr self, GXDBPtr arg1, const gx_string_type& arg2)
{
    self->link(arg1, arg2);
}
inline void GXMVIEW_wrap_maker(GXMVIEWPtr self, int32_t arg1, int32_t arg2, const gx_string_type& arg3, int32_t arg4, const gx_string_type& arg5, const gx_string_type& arg6)
{
    self->maker(arg1, arg2, arg3, (MAKER)arg4, arg5, arg6);
}
inline void GXMVIEW_wrap_meta(GXMVIEWPtr self, GXMETAPtr arg1, const gx_string_type& arg2)
{
    self->meta(arg1, arg2);
}
inline void GXMVIEW_wrap_voxd(GXMVIEWPtr self, GXVOXDPtr arg1, const gx_string_type& arg2)
{
    self->voxd(arg1, arg2);
}
inline GXVOXDPtr GXMVIEW_wrap_get_voxd(GXMVIEWPtr self, int32_t arg1)
{
    GXVOXDPtr ret = self->get_voxd(arg1);
    return ret;
}
inline void GXMVIEW_wrap_draw_vector_voxel_vectors(GXMVIEWPtr self, GXVOXPtr arg1, const gx_string_type& arg2, GXITRPtr arg3, double arg4, double arg5, double arg6, double arg7, int32_t arg8)
{
    self->draw_vector_voxel_vectors(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXMVIEW_wrap_draw_vectors_3d(GXMVIEWPtr self, const gx_string_type& arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7, GXITRPtr arg8, double arg9, double arg10, double arg11)
{
    self->draw_vectors_3d(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXMVIEW_wrap_copy_marked_groups(GXMVIEWPtr self, GXMVIEWPtr arg1)
{
    self->copy_marked_groups(arg1);
}
inline void GXMVIEW_wrap_copy_raw_marked_groups(GXMVIEWPtr self, GXMVIEWPtr arg1)
{
    self->copy_raw_marked_groups(arg1);
}
inline int32_t GXMVIEW_wrap_crc_group(GXMVIEWPtr self, const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = self->crc_group(arg1, arg2);
    return ret;
}
inline void GXMVIEW_wrap_delete_group(GXMVIEWPtr self, const gx_string_type& arg1)
{
    self->delete_group(arg1);
}
inline void GXMVIEW_wrap_del_marked_groups(GXMVIEWPtr self)
{
    self->del_marked_groups();
}
inline void GXMVIEW_wrap_get_group_extent(GXMVIEWPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, int32_t arg6)
{
    self->get_group_extent(arg1, arg2, arg3, arg4, arg5, (MVIEW_UNIT)arg6);
}
inline void GXMVIEW_wrap_get_group_transparency(GXMVIEWPtr self, const gx_string_type& arg1, float_ref& arg2)
{
    self->get_group_transparency(arg1, arg2);
}
inline void GXMVIEW_wrap_group_to_ply(GXMVIEWPtr self, const gx_string_type& arg1, GXPLYPtr arg2)
{
    self->group_to_ply(arg1, arg2);
}
inline void GXMVIEW_wrap_hide_marked_groups(GXMVIEWPtr self, int32_t arg1)
{
    self->hide_marked_groups((MVIEW_HIDE)arg1);
}
inline void GXMVIEW_wrap_hide_shadow2_d_interpretations(GXMVIEWPtr self, int32_t arg1)
{
    self->hide_shadow2_d_interpretations((MVIEW_HIDE)arg1);
}
inline int32_t GXMVIEW_wrap_exist_group(GXMVIEWPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->exist_group(arg1);
    return ret;
}
inline void GXMVIEW_wrap_gen_new_group_name(GXMVIEWPtr self, const gx_string_type& arg1, str_ref& arg2)
{
    self->gen_new_group_name(arg1, arg2);
}
inline int32_t GXMVIEW_wrap_is_group(GXMVIEWPtr self, const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = self->is_group(arg1, (MVIEW_IS)arg2);
    return ret;
}
inline int32_t GXMVIEW_wrap_is_group_empty(GXMVIEWPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->is_group_empty(arg1);
    return ret;
}
inline bool GXMVIEW_wrap_is_movable(GXMVIEWPtr self)
{
    bool ret = self->is_movable();
    return ret;
}
inline bool GXMVIEW_wrap_is_visible(GXMVIEWPtr self)
{
    bool ret = self->is_visible();
    return ret;
}
inline int32_t GXMVIEW_wrap_list_groups(GXMVIEWPtr self, GXLSTPtr arg1, int32_t arg2)
{
    int32_t ret = self->list_groups(arg1, (MVIEW_GROUP_LIST)arg2);
    return ret;
}
inline int32_t GXMVIEW_wrap_render_order(GXMVIEWPtr self)
{
    int32_t ret = self->render_order();
    return ret;
}
inline void GXMVIEW_wrap_mark_all_groups(GXMVIEWPtr self, int32_t arg1)
{
    self->mark_all_groups(arg1);
}
inline void GXMVIEW_wrap_mark_empty_groups(GXMVIEWPtr self, int32_t arg1)
{
    self->mark_empty_groups(arg1);
}
inline void GXMVIEW_wrap_mark_group(GXMVIEWPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->mark_group(arg1, arg2);
}
inline void GXMVIEW_wrap_move_group_backward(GXMVIEWPtr self, const gx_string_type& arg1)
{
    self->move_group_backward(arg1);
}
inline void GXMVIEW_wrap_move_group_forward(GXMVIEWPtr self, const gx_string_type& arg1)
{
    self->move_group_forward(arg1);
}
inline void GXMVIEW_wrap_move_group_to_back(GXMVIEWPtr self, const gx_string_type& arg1)
{
    self->move_group_to_back(arg1);
}
inline void GXMVIEW_wrap_move_group_to_front(GXMVIEWPtr self, const gx_string_type& arg1)
{
    self->move_group_to_front(arg1);
}
inline void GXMVIEW_wrap_rename_group(GXMVIEWPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->rename_group(arg1, arg2);
}
inline void GXMVIEW_wrap_set_group_moveable(GXMVIEWPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->set_group_moveable(arg1, arg2);
}
inline void GXMVIEW_wrap_set_group_transparency(GXMVIEWPtr self, const gx_string_type& arg1, double arg2)
{
    self->set_group_transparency(arg1, arg2);
}
inline void GXMVIEW_wrap_set_mark_moveable(GXMVIEWPtr self, int32_t arg1)
{
    self->set_mark_moveable(arg1);
}
inline void GXMVIEW_wrap_set_movability(GXMVIEWPtr self, bool arg1)
{
    self->set_movability(arg1);
}
inline void GXMVIEW_wrap_set_render_order(GXMVIEWPtr self, int32_t arg1)
{
    self->set_render_order(arg1);
}
inline void GXMVIEW_wrap_set_visibility(GXMVIEWPtr self, bool arg1)
{
    self->set_visibility(arg1);
}
inline void GXMVIEW_wrap_start_group(GXMVIEWPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->start_group(arg1, (MVIEW_GROUP)arg2);
}
inline void GXMVIEW_wrap_set_working_ipj(GXMVIEWPtr self, GXIPJPtr arg1)
{
    self->set_working_ipj(arg1);
}
inline void GXMVIEW_wrap_clear_esrild_ts(GXMVIEWPtr self)
{
    self->clear_esrild_ts();
}
inline int32_t GXMVIEW_wrap_is_projection_empty(GXMVIEWPtr self)
{
    int32_t ret = self->is_projection_empty();
    return ret;
}
inline void GXMVIEW_wrap_get_ipj(GXMVIEWPtr self, GXIPJPtr arg1)
{
    self->get_ipj(arg1);
}
inline void GXMVIEW_wrap_get_user_ipj(GXMVIEWPtr self, GXIPJPtr arg1)
{
    self->get_user_ipj(arg1);
}
inline void GXMVIEW_wrap_mode_pj(GXMVIEWPtr self, int32_t arg1)
{
    self->mode_pj((MVIEW_PJ)arg1);
}
inline double GXMVIEW_wrap_north(GXMVIEWPtr self)
{
    double ret = self->north();
    return ret;
}
inline void GXMVIEW_wrap_set_ipj(GXMVIEWPtr self, GXIPJPtr arg1)
{
    self->set_ipj(arg1);
}
inline void GXMVIEW_wrap_set_user_ipj(GXMVIEWPtr self, GXIPJPtr arg1)
{
    self->set_user_ipj(arg1);
}
inline int32_t GXMVIEW_wrap_get_3d_group_flags(GXMVIEWPtr self, int32_t arg1)
{
    MVIEW_3D_RENDER ret = self->get_3d_group_flags(arg1);
    return ret;
}
inline void GXMVIEW_wrap_set_3d_group_flags(GXMVIEWPtr self, int32_t arg1, int32_t arg2)
{
    self->set_3d_group_flags(arg1, (MVIEW_3D_RENDER)arg2);
}
inline void GXMVIEW_wrap_get_group_freeze_scale(GXMVIEWPtr self, int32_t arg1, float_ref& arg2)
{
    self->get_group_freeze_scale(arg1, arg2);
}
inline void GXMVIEW_wrap_set_freeze_scale(GXMVIEWPtr self, double arg1)
{
    self->set_freeze_scale(arg1);
}
inline void GXMVIEW_wrap_set_group_freeze_scale(GXMVIEWPtr self, int32_t arg1, double arg2)
{
    self->set_group_freeze_scale(arg1, arg2);
}
inline int32_t GXMVIEW_wrap_find_group(GXMVIEWPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->find_group(arg1);
    return ret;
}
inline void GXMVIEW_wrap_group_name(GXMVIEWPtr self, int32_t arg1, str_ref& arg2)
{
    self->group_name(arg1, arg2);
}
inline void GXMVIEW_wrap_render(GXMVIEWPtr self, HDC arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, double arg6, double arg7, double arg8, double arg9)
{
    self->render(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXMVIEW_wrap_set_u_fac(GXMVIEWPtr self, double arg1)
{
    self->set_u_fac(arg1);
}
inline void GXMVIEW_wrap_axis_x(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6)
{
    self->axis_x(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXMVIEW_wrap_axis_y(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6)
{
    self->axis_y(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXMVIEW_wrap_grid(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, int32_t arg5)
{
    self->grid(arg1, arg2, arg3, arg4, (MVIEW_GRID)arg5);
}
inline void GXMVIEW_wrap_label_fid(GXMVIEWPtr self, GXVVPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6)
{
    self->label_fid(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXMVIEW_wrap_label_x(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    self->label_x(arg1, arg2, arg3, arg4, (MVIEW_LABEL_JUST)arg5, (MVIEW_LABEL_BOUND)arg6, (MVIEW_LABEL_ORIENT)arg7);
}
inline void GXMVIEW_wrap_label_y(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    self->label_y(arg1, arg2, arg3, arg4, (MVIEW_LABEL_JUST)arg5, (MVIEW_LABEL_BOUND)arg6, (MVIEW_LABEL_ORIENT)arg7);
}
inline void GXMVIEW_wrap_optimum_tick(double arg1, double arg2, float_ref& arg3)
{
    GXMVIEW::optimum_tick(arg1, arg2, arg3);
}
inline GXMVIEWPtr GXMVIEW_wrap_create(GXMAPPtr arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXMVIEWPtr ret = GXMVIEW::create(arg1, arg2, (MVIEW_OPEN)arg3);
    return ret;
}
inline GXMVIEWPtr GXMVIEW_wrap_create_crooked_section(GXMAPPtr arg1, GXIPJPtr arg2, const gx_string_type& arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10, double arg11, GXVVPtr arg12, GXVVPtr arg13, GXVVPtr arg14)
{
    GXMVIEWPtr ret = GXMVIEW::create_crooked_section(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14);
    return ret;
}
inline GXMVIEWPtr GXMVIEW_wrap_create_crooked_section_data_profile(GXMAPPtr arg1, GXIPJPtr arg2, const gx_string_type& arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10, double arg11, int32_t arg12, GXVVPtr arg13, GXVVPtr arg14, GXVVPtr arg15)
{
    GXMVIEWPtr ret = GXMVIEW::create_crooked_section_data_profile(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15);
    return ret;
}
inline void GXMVIEW_wrap_extent(GXMVIEWPtr self, int32_t arg1, int32_t arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    self->extent((MVIEW_EXTENT)arg1, (MVIEW_EXTENT_UNIT)arg2, arg3, arg4, arg5, arg6);
}
inline GXMAPPtr GXMVIEW_wrap_get_map(GXMVIEWPtr self)
{
    GXMAPPtr ret = self->get_map();
    return ret;
}
inline GXREGPtr GXMVIEW_wrap_get_reg(GXMVIEWPtr self)
{
    GXREGPtr ret = self->get_reg();
    return ret;
}
inline void GXMVIEW_wrap_get_name(GXMVIEWPtr self, str_ref& arg1)
{
    self->get_name(arg1);
}
inline void GXMVIEW_wrap_plot_to_view(GXMVIEWPtr self, float_ref& arg1, float_ref& arg2)
{
    self->plot_to_view(arg1, arg2);
}
inline void GXMVIEW_wrap_set_thin_res(GXMVIEWPtr self, double arg1)
{
    self->set_thin_res(arg1);
}
inline void GXMVIEW_wrap_view_to_plot(GXMVIEWPtr self, float_ref& arg1, float_ref& arg2)
{
    self->view_to_plot(arg1, arg2);
}
inline void GXMVIEW_wrap_best_fit_window(GXMVIEWPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, int32_t arg9)
{
    self->best_fit_window(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, (MVIEW_FIT)arg9);
}
inline void GXMVIEW_wrap_fit_map_window_3d(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8)
{
    self->fit_map_window_3d(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXMVIEW_wrap_fit_window(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8)
{
    self->fit_window(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXMVIEW_wrap_get_class_name(GXMVIEWPtr self, const gx_string_type& arg1, str_ref& arg2)
{
    self->get_class_name(arg1, arg2);
}
inline void GXMVIEW_wrap_map_origin(GXMVIEWPtr self, float_ref& arg1, float_ref& arg2)
{
    self->map_origin(arg1, arg2);
}
inline void GXMVIEW_wrap_re_scale(GXMVIEWPtr self, double arg1)
{
    self->re_scale(arg1);
}
inline double GXMVIEW_wrap_get_map_scale(GXMVIEWPtr self)
{
    double ret = self->get_map_scale();
    return ret;
}
inline double GXMVIEW_wrap_scale_mm(GXMVIEWPtr self)
{
    double ret = self->scale_mm();
    return ret;
}
inline double GXMVIEW_wrap_scale_pj_mm(GXMVIEWPtr self)
{
    double ret = self->scale_pj_mm();
    return ret;
}
inline double GXMVIEW_wrap_scale_ymm(GXMVIEWPtr self)
{
    double ret = self->scale_ymm();
    return ret;
}
inline void GXMVIEW_wrap_scale_all_group(GXMVIEWPtr self, double arg1, double arg2)
{
    self->scale_all_group(arg1, arg2);
}
inline void GXMVIEW_wrap_scale_window(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8)
{
    self->scale_window(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXMVIEW_wrap_set_class_name(GXMVIEWPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->set_class_name(arg1, arg2);
}
inline void GXMVIEW_wrap_set_window(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4, int32_t arg5)
{
    self->set_window(arg1, arg2, arg3, arg4, (MVIEW_UNIT)arg5);
}
inline void GXMVIEW_wrap_tran_scale(GXMVIEWPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->tran_scale(arg1, arg2, arg3, arg4);
}
inline void GXMVIEW_wrap_user_to_view(GXMVIEWPtr self, float_ref& arg1, float_ref& arg2)
{
    self->user_to_view(arg1, arg2);
}
inline void GXMVIEW_wrap_view_to_user(GXMVIEWPtr self, float_ref& arg1, float_ref& arg2)
{
    self->view_to_user(arg1, arg2);
}

void gxPythonImportGXMVIEW()
{

    class_<GXMVIEW, GXMVIEWPtr> pyClass("GXMVIEW",
                                        "\n.. parsed-literal::\n\n"
                                        "   \n"
                                        "   		A view (MVIEW class) has a 2-D/3-D translation matrix, a map\n"
                                        "   		projection and a clip region.  A view contains any number of\n"
                                        "   		\"groups\", and each \"group\" contains one or more graphics\n"
                                        "   		elements (entities).  Different types of groups will contain\n"
                                        "   		different types of entities:\n"
                                        "   	\n\n"

                                        "\n\n**Note:**\n\n"

                                        "\n.. parsed-literal::\n\n"
                                        "   \n"
                                        "   		CSYMB groups (colour symbols) contain data and rules for\n"
                                        "   		presenting the data as colour symbols.  See \\ :func:`geosoft.gxapi.GXMVIEW.col_symbol`\\ \n"
                                        "   		and the CSYMB class.\n"
                                        "   \n"
                                        "   		AGG groups (aggregates) contain images.  See \\ :func:`geosoft.gxapi.GXMVIEW.aggregate`\\ \n"
                                        "   		and the AGG class.\n"
                                        "   \n"
                                        "   		PAGG groups (poly-aggregates) contain images with multiple\n"
                                        "   		frames that make up an animation.  See \\ :func:`geosoft.gxapi.GXMVIEW.poly_aggregate`\\ \n"
                                        "   		and the PAGG class.\n"
                                        "   \n"
                                        "   		Standard groups contain symbols, lines, polylines, and polygons.\n"
                                        "   		See \\ :func:`geosoft.gxapi.GXMVIEW.start_group`\\ .\n"
                                        "   	\n\n"
                                        , no_init);

    pyClass.def("null", &GXMVIEW::null, "null() -> GXMVIEW\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXMVIEW`\n\n:returns: A null :class:`geosoft.gxapi.GXMVIEW`\n:rtype: :class:`geosoft.gxapi.GXMVIEW`\n").staticmethod("null");
    pyClass.def("is_null", &GXMVIEW::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXMVIEW is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXMVIEW`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXMVIEW::_internal_handle);
    pyClass.def("box_3d", &GXMVIEW_wrap_box_3d,
                "box_3d((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a 3D box\n\n"

                ":param arg1: Min X\n"
                ":type arg1: float\n"
                ":param arg2: Min Y\n"
                ":type arg2: float\n"
                ":param arg3: Min Z\n"
                ":type arg3: float\n"
                ":param arg4: Max X\n"
                ":type arg4: float\n"
                ":param arg5: Max Y\n"
                ":type arg5: float\n"
                ":param arg6: Max Z\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Fill color is used to color the box.\n\n"
               );
    pyClass.def("crc_view", &GXMVIEW_wrap_crc_view,
                "crc_view((int_ref)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate an XML CRC of a View\n\n"

                ":param arg1: CRC returned\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Name of xml to generate (.zip added)\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("crc_view_group", &GXMVIEW_wrap_crc_view_group,
                "crc_view_group((str)arg1, (int_ref)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate an XML CRC of a Group\n\n"

                ":param arg1: Name of Group\n"
                ":type arg1: str\n"
                ":param arg2: CRC returned\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Name of xml to generate (.zip added)\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("cylinder_3d", &GXMVIEW_wrap_cylinder_3d,
                "cylinder_3d((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (int)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a 3D cylinder\n\n"

                ":param arg1: Start X\n"
                ":type arg1: float\n"
                ":param arg2: Start Y\n"
                ":type arg2: float\n"
                ":param arg3: Start Z\n"
                ":type arg3: float\n"
                ":param arg4: End X\n"
                ":type arg4: float\n"
                ":param arg5: End Y\n"
                ":type arg5: float\n"
                ":param arg6: End Z\n"
                ":type arg6: float\n"
                ":param arg7: Start Radius (can be zero)\n"
                ":type arg7: float\n"
                ":param arg8: End Radius (can be zero)\n"
                ":type arg8: float\n"
                ":param arg9: \\ :ref:`MVIEW_CYLINDER3D`\\ \n"
                ":type arg9: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The Fill color is used to color the cylinder.\n"
                "   					The flags determine if the cylinder is open and what\n"
                "   					end are closed. Note that you can create cones by\n"
                "   					specifying a 0 radius for one of the ends.\n"
                "   				\n\n"
               );
    pyClass.def("draw_object_3d", &GXMVIEW_wrap_draw_object_3d,
                "draw_object_3d((int)arg1, (int)arg2, (int)arg3, (int)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (GXVV)arg10, (GXVV)arg11, (GXVV)arg12, (GXVV)arg13) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a 3D object optimized for rendering\n\n"

                ":param arg1: \\ :ref:`MVIEW_DRAWOBJ3D_ENTITY`\\ \n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`MVIEW_DRAWOBJ3D_MODE`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Number of Objects\n"
                ":type arg3: int\n"
                ":param arg4: Default Count (if variable and not specified)\n"
                ":type arg4: int\n"
                ":param arg5: Verticies X\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Verticies Y\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Verticies Z\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Normals X (can be NULL)\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Normals Y (can be NULL)\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Normals Z (can be NULL)\n"
                ":type arg10: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg11: Colors VV (can be NULL)\n"
                ":type arg11: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg12: Index  VV (can be NULL)\n"
                ":type arg12: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg13: Count  VV (can be NULL)\n"
                ":type arg13: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("draw_surface_3d_ex", &GXMVIEW_wrap_draw_surface_3d_ex,
                "draw_surface_3d_ex((str)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7, (GXVV)arg8, (int)arg9, (GXVV)arg10, (GXVV)arg11, (GXVV)arg12, (GXIPJ)arg13) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a 3D object built from triangles\n\n"

                ":param arg1: Group name\n"
                ":type arg1: str\n"
                ":param arg2: Vertices X (GS_REAL)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Vertices Y (GS_REAL)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Vertices Z (GS_REAL)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Normals X (GS_REAL)\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Normals Y (GS_REAL)\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Normals Z (GS_REAL)\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Colors VV (GS_INT) [can be NULL]\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Color used if above VV is NULL [0 for MVIEW's fillcolor]\n"
                ":type arg9: int\n"
                ":param arg10: Triangles Point 1 (GS_INT)\n"
                ":type arg10: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg11: Triangles Point 2 (GS_INT)\n"
                ":type arg11: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg12: Triangles Point 3 (GS_INT)\n"
                ":type arg12: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg13: Native IPJ of 3D object\n"
                ":type arg13: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Provide one normal per vertex.\n"
                "   					Triangles are defined by indices into the set of vertices.\n"
                "   				\n\n"
               );
    pyClass.def("draw_surface_3d_from_file", &GXMVIEW_wrap_draw_surface_3d_from_file,
                "draw_surface_3d_from_file((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a 3D object from a surface file\n\n"

                ":param arg1: Group name\n"
                ":type arg1: str\n"
                ":param arg2: Surface file\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				\n\n"
               );
    pyClass.def("font_weight_lst", &GXMVIEW_wrap_font_weight_lst,
                "font_weight_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill a LST with the different font weights.\n\n"

                ":param arg1: LST object\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               ).staticmethod("font_weight_lst");
    pyClass.def("get_agg_file_names", &GXMVIEW_wrap_get_agg_file_names,
                "get_agg_file_names((str)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the names of grid files stored in an AGG.\n\n"

                ":param arg1: group name\n"
                ":type arg1: str\n"
                ":param arg2: returned string VV of type -STR_FILE\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The group must be an AGG group. Check this using\n"
                "   					\\ :func:`geosoft.gxapi.GXMVIEW.is_group`\\ (View, sGroup, MVIEW_IS_AGG).\n"
                "   				\n\n"
               );
    pyClass.def("get_meta", &GXMVIEW_wrap_get_meta,
                "get_meta((str)arg1, (str_ref)arg2) -> GXMETA:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieves Metadata from a group\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Meta name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: META Object\n"
                ":rtype: :class:`geosoft.gxapi.GXMETA`\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("measure_text", &GXMVIEW_wrap_measure_text,
                "measure_text((str)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute the bounding rectangle in view units of the text using the current attributes.\n\n"

                ":param arg1: Text string\n"
                ":type arg1: str\n"
                ":param arg2: X minimum\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y minimum\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: X maximum\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Y maximum\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Area will be 0 if error occured (does not fail).\n"
                "   					This will return the bounding rectangle as if the text was placed at 0,0 and adjusted according to\n"
                "   					the current text alignment and angle set for the view. Also see notes for \\ :func:`geosoft.gxapi.GXMVIEW.text_size`\\ .\n"
                "   				\n\n"
               );
    pyClass.def("point_3d", &GXMVIEW_wrap_point_3d,
                "point_3d((float)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a 3D point.\n\n"

                ":param arg1: X\n"
                ":type arg1: float\n"
                ":param arg2: Y\n"
                ":type arg2: float\n"
                ":param arg3: Z\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Line color and line thickness will affect rendering.\n\n"
               );
    pyClass.def("poly_line_3d", &GXMVIEW_wrap_poly_line_3d,
                "poly_line_3d((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a 3D polyline.\n\n"

                ":param arg1: X coordinates.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y coordinates.\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z coordinates.\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Dummies are not allowed in the line.\n"
                "   					Line Color, Thickness is supported on rendering\n"
                "   				\n\n"
               );
    pyClass.def("relocate_group", &GXMVIEW_wrap_relocate_group,
                "relocate_group((str)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Re-locate a group in a view.\n\n"

                ":param arg1: group name\n"
                ":type arg1: str\n"
                ":param arg2: area X minimum\n"
                ":type arg2: float\n"
                ":param arg3: area Y minimum\n"
                ":type arg3: float\n"
                ":param arg4: area X maximum\n"
                ":type arg4: float\n"
                ":param arg5: area Y maximum\n"
                ":type arg5: float\n"
                ":param arg6: \\ :ref:`MVIEW_RELOCATE`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_meta", &GXMVIEW_wrap_set_meta,
                "set_meta((str)arg1, (GXMETA)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Update the META in this group with the new meta object.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: META object\n"
                ":type arg2: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg3: Meta name of Object\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("sphere_3d", &GXMVIEW_wrap_sphere_3d,
                "sphere_3d((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a 3D sphere\n\n"

                ":param arg1: Center X\n"
                ":type arg1: float\n"
                ":param arg2: Center Y\n"
                ":type arg2: float\n"
                ":param arg3: Center Z\n"
                ":type arg3: float\n"
                ":param arg4: Radius\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Fill color is used to color the sphere.\n\n"
               );
    pyClass.def("update_met_afrom_group", &GXMVIEW_wrap_update_met_afrom_group,
                "update_met_afrom_group((str)arg1, (GXMETA)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill the META with group dataset information\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: META object to fill\n"
                ":type arg2: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("delete_plane", &GXMVIEW_wrap_delete_plane,
                "delete_plane((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete a plane in a view\n\n"

                ":param arg1: plane number to delete\n"
                ":type arg1: int\n"
                ":param arg2: TRUE to delete all groups on the plane\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the groups on the plane are not deleted, they will remain in the\n"
                "   					3D view as \"New\" groups but will be unassigned to a plane.  The\n"
                "   					SetAllNewGroupsToPlane  function can be used to assign these groups\n"
                "   					to a different plane.\n"
                "   				\n\n"
               );
    pyClass.def("get_plane_clip_ply", &GXMVIEW_wrap_get_plane_clip_ply,
                "get_plane_clip_ply((int)arg1, (GXPLY)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Plane Clip Region\n\n"

                ":param arg1: Plane index\n"
                ":type arg1: int\n"
                ":param arg2: Clip Region\n"
                ":type arg2: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   By default it is the View's Clip Region\n\n"
               );
    pyClass.def("get_plane_equation", &GXMVIEW_wrap_get_plane_equation,
                "get_plane_equation((int)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9, (float_ref)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the equation of a plane\n\n"

                ":param arg1: Plane index\n"
                ":type arg1: int\n"
                ":param arg2: Rotation about X (Y toward Z +ve, between -360 and 360)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Rotation about Y (Z toward X +ve, between -360 and 360)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Rotation about Z (Y toward X +ve, between -360 and 360)\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: X offset of plane\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Y offset of plane\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Z offset of plane\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: X scale\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Y scale\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: Z scale\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("get_view_plane_equation", &GXMVIEW_wrap_get_view_plane_equation,
                "get_view_plane_equation((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the View's Plane Equation\n\n"

                ":param arg1: Angle in X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Angle in Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Angle in Z\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Offset in X\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Offset in Y\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Offset in Z\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Scale in X\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Scale in Y\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Scale in Z\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("create_plane", &GXMVIEW_wrap_create_plane,
                "create_plane((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a 3D Plane for 2D Groups\n\n"

                ":param arg1: Name of Plane\n"
                ":type arg1: str\n"
                ":returns: x - Index of plane\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("find_plane", &GXMVIEW_wrap_find_plane,
                "find_plane((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Find a plane in a view\n\n"

                ":param arg1: name of the plane\n"
                ":type arg1: str\n"
                ":returns: Plane number, -1 if not found\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("get_def_plane", &GXMVIEW_wrap_get_def_plane,
                "get_def_plane((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the default drawing plane.\n\n"

                ":param arg1: name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					2D drawing to a 3D View will always be placed on the\n"
                "   					default drawing plane.  If no default drawing plane\n"
                "   					has been set, the first valid plane in the view is\n"
                "   					used as the default drawing plane.\n"
                "   				\n\n"
               );
    pyClass.def("is_view_3d", &GXMVIEW_wrap_is_view_3d,
                "is_view_3d() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is the view 3D?\n\n"

                ":returns: TRUE if view is 3D\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("is_section", &GXMVIEW_wrap_is_section,
                "is_section() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is the view a section view?\n\n"

                ":returns: TRUE if view is a section view.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Section views are recognized because their projection contains one of the following orientations:\n"
                "   \n"
                "   					IPJ_ORIENT_SECTION - Target-type sections with Z projection horizontally\n"
                "   					IPJ_ORIENT_SECTION_NORMAL - Like IPJ_ORIENT_SECTION, but Z projects\n"
                "   					perpendicular to the secton plane.\n"
                "   					IPJ_ORIENT_SECTION_CROOKED - Crooked sections\n"
                "   					IPJ_ORIENT_3D - Some Sections extracted from a voxel - e.g. VoxelToGrids,\n"
                "   					as the voxel can have any orientation in 3D.\n"
                "   				\n\n"
               );
    pyClass.def("list_plane_groups", &GXMVIEW_wrap_list_plane_groups,
                "list_plane_groups((int)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   List all groups in a specific plane of a 3D view\n\n"

                ":param arg1: plane number\n"
                ":type arg1: int\n"
                ":param arg2: List of plane names and numbers\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The group names are placed in the list names, group\n"
                "   					numbers are placed in the list values.\n"
                "   \n"
                "   					Groups are added to the end of the LST.\n"
                "   				\n\n"
               );
    pyClass.def("list_planes", &GXMVIEW_wrap_list_planes,
                "list_planes((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   List all planes in a 3D view\n\n"

                ":param arg1: List of plane names and numbers\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The plane names are placed in the list names, plane\n"
                "   					numbers are placed in the list values.\n"
                "   \n"
                "   					Planes are added to the end of the LST.\n"
                "   				\n\n"
               );
    pyClass.def("set_all_groups_to_plane", &GXMVIEW_wrap_set_all_groups_to_plane,
                "set_all_groups_to_plane((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set all groups to be within one plane\n\n"

                ":param arg1: Plane Index to set all groups to\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("set_all_new_groups_to_plane", &GXMVIEW_wrap_set_all_new_groups_to_plane,
                "set_all_new_groups_to_plane((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set all groups that are not in any plane to this plane\n\n"

                ":param arg1: Plane Index to set all groups to\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("set_def_plane", &GXMVIEW_wrap_set_def_plane,
                "set_def_plane((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the default drawing plane.\n\n"

                ":param arg1: name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					2D drawing to a 3D View will always be placed on the\n"
                "   					default drawing plane.  If no default drawing plane\n"
                "   					has been set, the first valid plane in the view is\n"
                "   					used as the default drawing plane.\n"
                "   				\n\n"
               );
    pyClass.def("set_group_to_plane", &GXMVIEW_wrap_set_group_to_plane,
                "set_group_to_plane((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a group to a plane\n\n"

                ":param arg1: Plane Index to set all groups to\n"
                ":type arg1: int\n"
                ":param arg2: Name of group to set\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("set_h_3dn", &GXMVIEW_wrap_set_h_3dn,
                "set_h_3dn((GX3DN)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the 3DN object for this view\n\n"

                ":param arg1: 3DN to set (NULL for 2D view)\n"
                ":type arg1: :class:`geosoft.gxapi.GX3DN`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   To make the view a 2D view, set a 3DN of NULL.\n\n"
               );
    pyClass.def("set_plane_clip_ply", &GXMVIEW_wrap_set_plane_clip_ply,
                "set_plane_clip_ply((int)arg1, (GXPLY)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Plane Clip Region\n\n"

                ":param arg1: Plane index\n"
                ":type arg1: int\n"
                ":param arg2: Clip Region\n"
                ":type arg2: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   By default it is the View's Clip Region\n\n"
               );
    pyClass.def("set_plane_equation", &GXMVIEW_wrap_set_plane_equation,
                "set_plane_equation((int)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the equation of a plane\n\n"

                ":param arg1: Plane index\n"
                ":type arg1: int\n"
                ":param arg2: Rotation about X (Z toward Y +ve, between -360 and 360)\n"
                ":type arg2: float\n"
                ":param arg3: Rotation about Y (Z toward X +ve, between -360 and 360)\n"
                ":type arg3: float\n"
                ":param arg4: Rotation about Z (Y toward X +ve, between -360 and 360)\n"
                ":type arg4: float\n"
                ":param arg5: X offset of plane\n"
                ":type arg5: float\n"
                ":param arg6: Y offset of plane\n"
                ":type arg6: float\n"
                ":param arg7: Z offset of plane\n"
                ":type arg7: float\n"
                ":param arg8: X scale\n"
                ":type arg8: float\n"
                ":param arg9: Y scale\n"
                ":type arg9: float\n"
                ":param arg10: Z scale\n"
                ":type arg10: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					For a grid with the \"Y\" axis giving elevation:\n"
                "   					use rotations = (-90, 0, 0) for a section with azimuth 90 (E-W)\n"
                "   					use rotations = (-90, 0, -90) for a section with azimuth 0 (N-S)\n"
                "   				\n\n"
               );
    pyClass.def("set_plane_surface", &GXMVIEW_wrap_set_plane_surface,
                "set_plane_surface((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the surface image of a plane\n\n"

                ":param arg1: Plane index\n"
                ":type arg1: int\n"
                ":param arg2: Optional surface image/grid name, can be NULL\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("set_plane_surf_info", &GXMVIEW_wrap_set_plane_surf_info,
                "set_plane_surf_info((int)arg1, (int)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the surface information\n\n"

                ":param arg1: Plane index\n"
                ":type arg1: int\n"
                ":param arg2: Sample rate (>=1)\n"
                ":type arg2: int\n"
                ":param arg3: Base\n"
                ":type arg3: float\n"
                ":param arg4: Scale\n"
                ":type arg4: float\n"
                ":param arg5: Min\n"
                ":type arg5: float\n"
                ":param arg6: Max\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("define_plane_3d", &GXMVIEW_wrap_define_plane_3d,
                "define_plane_3d((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Define a 2D drawing plane based on point and normal\n\n"

                ":param arg1: Center point X\n"
                ":type arg1: float\n"
                ":param arg2: Center point Y\n"
                ":type arg2: float\n"
                ":param arg3: Center point Z\n"
                ":type arg3: float\n"
                ":param arg4: X Vector X\n"
                ":type arg4: float\n"
                ":param arg5: X Vector Y\n"
                ":type arg5: float\n"
                ":param arg6: X Vector Z\n"
                ":type arg6: float\n"
                ":param arg7: Y Vector X\n"
                ":type arg7: float\n"
                ":param arg8: Y Vector Y\n"
                ":type arg8: float\n"
                ":param arg9: Y Vector Z\n"
                ":type arg9: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					2D rendering commands are translated to 3D commands\n"
                "   					based on the plane.\n"
                "   				\n\n"
               );
    pyClass.def("define_viewer_axis_3d", &GXMVIEW_wrap_define_viewer_axis_3d,
                "define_viewer_axis_3d((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Define a 2D drawing plane based on the user's view that\n"
                "   					oriented around the vector.\n"
                "   				\n\n"

                ":param arg1: Center point X\n"
                ":type arg1: float\n"
                ":param arg2: Center point Y\n"
                ":type arg2: float\n"
                ":param arg3: Center point Z\n"
                ":type arg3: float\n"
                ":param arg4: Directional Point X\n"
                ":type arg4: float\n"
                ":param arg5: Directional Point Y\n"
                ":type arg5: float\n"
                ":param arg6: Directional Point Z\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("define_viewer_plane_3d", &GXMVIEW_wrap_define_viewer_plane_3d,
                "define_viewer_plane_3d((float)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Define a 2D drawing plane based on the user's view.\n\n"

                ":param arg1: Center point X\n"
                ":type arg1: float\n"
                ":param arg2: Center point Y\n"
                ":type arg2: float\n"
                ":param arg3: Center point Z\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The plane is always facing the viewer. Otherwise the\n"
                "   					this is identical to the previous\n"
                "   				\n\n"
               );
    pyClass.def("clip_poly_ex", &GXMVIEW_wrap_clip_poly_ex,
                "clip_poly_ex((GXVV)arg1, (GXVV)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a polygon to the clip region.\n\n"

                ":param arg1: X VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: \\ :ref:`MVIEW_UNIT`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Exclude\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The polygon will be added to the current clip region.\n"
                "   					The VV's cannot have any dummy elements.\n"
                "   				\n\n"
               );
    pyClass.def("clip_rect_ex", &GXMVIEW_wrap_clip_rect_ex,
                "clip_rect_ex((float)arg1, (float)arg2, (float)arg3, (float)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a rectangle to the clip region.\n\n"

                ":param arg1: X minimum\n"
                ":type arg1: float\n"
                ":param arg2: Y minimum\n"
                ":type arg2: float\n"
                ":param arg3: X maximum\n"
                ":type arg3: float\n"
                ":param arg4: Y maximum\n"
                ":type arg4: float\n"
                ":param arg5: \\ :ref:`MVIEW_UNIT`\\ \n"
                ":type arg5: int\n"
                ":param arg6: Exclude\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The rectangle will be added to the current clip region.\n\n"
               );
    pyClass.def("clip_clear", &GXMVIEW_wrap_clip_clear,
                "clip_clear() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove/clear the view clip region.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("clip_groups", &GXMVIEW_wrap_clip_groups,
                "clip_groups((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Clipping mode on/off for all groups.\n\n"

                ":param arg1: \\ :ref:`MVIEW_CLIP`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("clip_marked_groups", &GXMVIEW_wrap_clip_marked_groups,
                "clip_marked_groups((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Clipping mode on/off for marked groups.\n\n"

                ":param arg1: \\ :ref:`MVIEW_CLIP`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("clip_poly", &GXMVIEW_wrap_clip_poly,
                "clip_poly((GXVV)arg1, (GXVV)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a polygon to the clip region.\n\n"

                ":param arg1: X VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: \\ :ref:`MVIEW_UNIT`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The polygon will be added to the current clip region.\n"
                "   					The VV's cannot have any dummy elements.\n"
                "   				\n\n"
               );
    pyClass.def("clip_rect", &GXMVIEW_wrap_clip_rect,
                "clip_rect((float)arg1, (float)arg2, (float)arg3, (float)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a rectangle to the clip region.\n\n"

                ":param arg1: X minimum\n"
                ":type arg1: float\n"
                ":param arg2: Y minimum\n"
                ":type arg2: float\n"
                ":param arg3: X maximum\n"
                ":type arg3: float\n"
                ":param arg4: Y maximum\n"
                ":type arg4: float\n"
                ":param arg5: \\ :ref:`MVIEW_UNIT`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The rectangle will be added to the current clip region.\n\n"
               );
    pyClass.def("delete_ext_clip_ply", &GXMVIEW_wrap_delete_ext_clip_ply,
                "delete_ext_clip_ply((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Deletes an extended clip PLY object used by this view.\n\n"

                ":param arg1: Extended ClipPLY number\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("ext_clip_ply_list", &GXMVIEW_wrap_ext_clip_ply_list,
                "ext_clip_ply_list((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the names of existing extended clip PLY objects in this view as list.\n\n"

                ":param arg1: LST\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("get_clip_ply", &GXMVIEW_wrap_get_clip_ply,
                "get_clip_ply((GXPLY)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get clipping polygons, in the user projection\n\n"

                ":param arg1: Poly\n"
                ":type arg1: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The returned PLY is recast into the User projection.\n"
                "   					For oriented views (especially sections), use\n"
                "   					\\ :func:`geosoft.gxapi.GXMVIEW.get_ply`\\ , which returns the Clip PLY in the view's native\n"
                "   					projection (e.g. the one set using \\ :func:`geosoft.gxapi.GXMVIEW.set_ipj`\\ ).\n"
                "   				\n\n"
               );
    pyClass.def("get_ext_clip_ply", &GXMVIEW_wrap_get_ext_clip_ply,
                "get_ext_clip_ply((int)arg1, (GXPLY)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an extended clip PLY object used by this view.\n\n"

                ":param arg1: Extended ClipPLY number\n"
                ":type arg1: int\n"
                ":param arg2: PLY object to get\n"
                ":type arg2: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("get_group_ext_clip_ply", &GXMVIEW_wrap_get_group_ext_clip_ply,
                "get_group_ext_clip_ply((str)arg1, (int_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets extended clip information for group in view.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Extended PLY number (returned, -1 if not set)\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("get_ply", &GXMVIEW_wrap_get_ply,
                "get_ply((GXPLY)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get clipping polygons, in the base projection\n\n"

                ":param arg1: Poly\n"
                ":type arg1: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This should be used to get the clipping polygon for\n"
                "   					oriented views (especially sections).\n"
                "   				\n\n"
               );
    pyClass.def("group_clip_mode", &GXMVIEW_wrap_group_clip_mode,
                "group_clip_mode((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Clipping mode on or off for new groups.\n\n"

                ":param arg1: \\ :ref:`MVIEW_CLIP`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   All new groups will be clipped.\n\n"
               );
    pyClass.def("get_name_ext_clip_ply", &GXMVIEW_wrap_get_name_ext_clip_ply,
                "get_name_ext_clip_ply((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the name of the extended clip PLY object in this view.\n\n"

                ":param arg1: Extended ClipPLY number\n"
                ":type arg1: int\n"
                ":param arg2: Name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("num_ext_clip_ply", &GXMVIEW_wrap_num_ext_clip_ply,
                "num_ext_clip_ply() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of extended clip PLY objects in this view.\n\n"

                ":returns: Number of PLYs\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("set_ext_clip_ply", &GXMVIEW_wrap_set_ext_clip_ply,
                "set_ext_clip_ply((int)arg1, (str)arg2, (GXPLY)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Set an extended clip PLY object used by this view.\n\n"

                ":param arg1: Extended ClipPLY number, If  >= iNumExtClipPLY_MVIEW(View) it will be added to the end of the current list\n"
                ":type arg1: int\n"
                ":param arg2: Name (Has to be unique, otherwise error will be returned)\n"
                ":type arg2: str\n"
                ":param arg3: PLY object to set, use (PLY)0 to rename an existing object\n"
                ":type arg3: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Index of new or changed PLY, -1 on error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("set_clip_ply", &GXMVIEW_wrap_set_clip_ply,
                "set_clip_ply((GXPLY)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set clipping region to a PLY\n\n"

                ":param arg1: Poly\n"
                ":type arg1: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_group_ext_clip_ply", &GXMVIEW_wrap_set_group_ext_clip_ply,
                "set_group_ext_clip_ply((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets extended clip information for group in view.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Extended PLY number (-1 to clear)\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("color2_rgb", &GXMVIEW_wrap_color2_rgb,
                "color2_rgb((int)arg1, (int_ref)arg2, (int_ref)arg3, (int_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert to RGB values.\n\n"

                ":param arg1: Color value\n"
                ":type arg1: int\n"
                ":param arg2: Red\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Green\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Blue\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Color component intensities will be in the range 0-255.\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.color`\\ \n\n"
               ).staticmethod("color2_rgb");
    pyClass.def("color_descr", &GXMVIEW_wrap_color_descr,
                "color_descr((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a colour to a colour string label\n\n"

                ":param arg1: COL_ANY variable\n"
                ":type arg1: int\n"
                ":param arg2: colour descriptor returned\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See \\ :func:`geosoft.gxapi.GXMVIEW.color`\\ .\n\n"
               ).staticmethod("color_descr");
    pyClass.def("color", &GXMVIEW_wrap_color,
                "color((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a color from a colour string label\n\n"

                ":param arg1: colour name string\n"
                ":type arg1: str\n"
                ":returns: colour int\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Colour strings may be \"R\",\"G\",\"B\",\"C\",\"M\",\"Y\",\n"
                "   					\"H\",\"S\",\"V\", or \"K\" or a combination of these\n"
                "   					characters, each followed by up to three digits\n"
                "   					specifying a number between 0 and 255.\n"
                "   					An empty string produce C_ANY_NONE.\n"
                "   \n"
                "   					You must stay in the same colour model, RGB, CMY,\n"
                "   					HSV or K.\n"
                "   \n"
                "   					For example \"R\", \"R127G22\", \"H255S127V32\"\n"
                "   \n"
                "   					Characters are not case sensitive.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   iColorXXX_MVIEW macros\n\n"
               ).staticmethod("color");
    pyClass.def("color_cmy", &GXMVIEW_wrap_color_cmy,
                "color_cmy((int)arg1, (int)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return CMY color.\n\n"

                ":param arg1: Cyan\n"
                ":type arg1: int\n"
                ":param arg2: Magenta\n"
                ":type arg2: int\n"
                ":param arg3: Yellow\n"
                ":type arg3: int\n"
                ":returns: colour int based on color model.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Color component intensities must be in the range 0-255.\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.color`\\ \n\n"
               ).staticmethod("color_cmy");
    pyClass.def("color_hsv", &GXMVIEW_wrap_color_hsv,
                "color_hsv((int)arg1, (int)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return HSV color.\n\n"

                ":param arg1: Hue\n"
                ":type arg1: int\n"
                ":param arg2: Saturation\n"
                ":type arg2: int\n"
                ":param arg3: Color\n"
                ":type arg3: int\n"
                ":returns: colour int based on color model.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Color component intensities must be in the range 0-255.\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.color`\\ \n\n"
               ).staticmethod("color_hsv");
    pyClass.def("color_rgb", &GXMVIEW_wrap_color_rgb,
                "color_rgb((int)arg1, (int)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return RGB color.\n\n"

                ":param arg1: Red\n"
                ":type arg1: int\n"
                ":param arg2: Green\n"
                ":type arg2: int\n"
                ":param arg3: Blue\n"
                ":type arg3: int\n"
                ":returns: colour int based on color model.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Color component intensities must be in the range 0-255.\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.color`\\ \n\n"
               ).staticmethod("color_rgb");
    pyClass.def("clip_mode", &GXMVIEW_wrap_clip_mode,
                "clip_mode((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the view clipping mode on or off.\n\n"

                ":param arg1: \\ :ref:`MVIEW_CLIP`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Entitles that follow in this group will be clipped\n"
                "   					or not clipped depending on this mode.\n"
                "   \n"
                "   					The montaj editor cannot change the clip mode of\n"
                "   					embedded clipped/unclipped enties that are controlled\n"
                "   					by this call.  Use the Group clipping functions\n"
                "   					instead.\n"
                "   \n"
                "   					It is highly recommended that you use the \\ :func:`geosoft.gxapi.GXMVIEW.group_clip_mode`\\ \n"
                "   					function to control clipping on a group-by-group basis, instead\n"
                "   					of using \\ :func:`geosoft.gxapi.GXMVIEW.clip_mode`\\  when inside a group, as it is impossible\n"
                "   					to determine the  true visible extents of a group. In such cases, the\n"
                "   					\"zoom to full map extents\" command may give incorrect results.\n"
                "   				\n\n"
               );
    pyClass.def("fill_color", &GXMVIEW_wrap_fill_color,
                "fill_color((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the fill color.\n\n"

                ":param arg1: color\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("line_color", &GXMVIEW_wrap_line_color,
                "line_color((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the line color.\n\n"

                ":param arg1: Color\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("line_smooth", &GXMVIEW_wrap_line_smooth,
                "line_smooth((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the line edge smoothing.\n\n"

                ":param arg1: \\ :ref:`MVIEW_SMOOTH`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("line_style", &GXMVIEW_wrap_line_style,
                "line_style((int)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the style of a line.\n\n"

                ":param arg1: Line Style #, see default.lpt\n"
                ":type arg1: int\n"
                ":param arg2: Pitch in view units\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Line styles are selected by ordinal value (line style #)\n"
                "   					from those defined in default.lpt.  If default.lpt does\n"
                "   					not have a the style specified, the file user.lpt is\n"
                "   					searched.  If this file does not contain the line style\n"
                "   					solid is assumed.\n"
                "   \n"
                "   					Note that line styles from default.lpt and user.lpt are\n"
                "   					read into the map at the time the map is created, not\n"
                "   					at display time.\n"
                "   				\n\n"
               );
    pyClass.def("line_thick", &GXMVIEW_wrap_line_thick,
                "line_thick((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the line thickness.\n\n"

                ":param arg1: line thickness in view space units\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("pat_angle", &GXMVIEW_wrap_pat_angle,
                "pat_angle((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the pattern angle\n\n"

                ":param arg1: Angle\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Allows the user to apply a rotation to the basic\n"
                "   					pattern. Care should be taken to ensure that the\n"
                "   					tiling remains continuous; i.e. if the pattern\n"
                "   					consists of horizontal lines, only angles of\n"
                "   					-90, 0, 90, 180 (etc.) would give seamless tiling.\n"
                "   					However, simple, closed figure, such as a star,\n"
                "   					could be given any angle.\n"
                "   					Rotations about the center point (0.5, 0.5) of the\n"
                "   					unit cell are performed prior to applying PatSize.\n"
                "   					The default value is 0.0.\n"
                "   					Setting an angle of -999 inititates the random angle\n"
                "   					feature, and each pattern tile is rotated to a different\n"
                "   					angle. Using this along with PatStyle(View, MVIEW_TILE_RANDOM)\n"
                "   					can give a \"hand-drawn\" effect to geological fills.\n"
                "   \n"
                "   					See the IMPORTANT note for sPatNumber_MVIEW().\n"
                "   				\n\n"
               );
    pyClass.def("pat_density", &GXMVIEW_wrap_pat_density,
                "pat_density((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the tiling density.\n\n"

                ":param arg1: Relative density (default = 1).\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This number is the ratio between the plotted unit cell size and the\n"
                "   					distance between the plotted tile centers. The default value is 1.\n"
                "   					A value larger than 1 increases the density of the pattern, while\n"
                "   					values less than 1 make the pattern more \"spread out\".\n"
                "   					This can be used along with sPatStyleMethod to create more complicated\n"
                "   					fills from simple patterns.\n"
                "   \n"
                "   					See the IMPORTANT note for sPatNumber_MVIEW().\n"
                "   				\n\n"
               );
    pyClass.def("pat_number", &GXMVIEW_wrap_pat_number,
                "pat_number((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the pattern number\n\n"

                ":param arg1: Pattern number\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Pattern 0 is solid fill.(default)\n"
                "   					Set the pattern colour using \\ :func:`geosoft.gxapi.GXMVIEW.fill_color`\\ .\n"
                "   \n"
                "   					Patterns are selected by ordinal value (pattern number)\n"
                "   					from those defined in default.pat.  If default.pat does\n"
                "   					not have a the pattern specified, the file user.pat is\n"
                "   					searched.  If this file does not contain the pattern\n"
                "   					solid is assumed.\n"
                "   \n"
                "   					Note that patterns from default.pat and user.pat are\n"
                "   					read into the map at the time the map is created, not\n"
                "   					at display time.\n"
                "   \n"
                "   					IMPORTANT: A call to this function resets all the various\n"
                "   					pattern attributes to those defined for the selected pattern.\n"
                "   					If you want to modify any attributes, call that function (e.g.\n"
                "   					sPatSize_MVIEW(), AFTER you call sPatNumber_MVIEW().\n"
                "   				\n\n"
               );
    pyClass.def("pat_size", &GXMVIEW_wrap_pat_size,
                "pat_size((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the pattern unit cell size (X)\n\n"

                ":param arg1: Pattern size in view units\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See the IMPORTANT note for sPatNumber_MVIEW().\n\n"
               );
    pyClass.def("pat_style", &GXMVIEW_wrap_pat_style,
                "pat_style((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the tiling method (i.e. rectangle, triangle)\n\n"

                ":param arg1: \\ :ref:`MVIEW_TILE`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Normally, the unit cell is duplicated across the fill area\n"
                "   					like floor tiles (MVIEW_TILE_RECTANGULAR).\n"
                "   					DIAGONAL tiling rotates the tiling positions (but not the tiles)\n"
                "   					by 45 degrees.\n"
                "   					TRIANGULAR tiling\n"
                "   					Offsets each succeeding row by half the unit cell size, and\n"
                "   					lessens the vertical offset, so that the unit cell centers\n"
                "   					form a triangular grid pattern.\n"
                "   					RANDOM tiling adds small random offsets in both directions to give\n"
                "   					the diffuse effect seen on many geological maps.\n"
                "   \n"
                "   					NOTE: Some patterns are designed to be interlocking and may only\n"
                "   					work \"correctly\" with one tiling method.\n"
                "   \n"
                "   					See the IMPORTANT note for sPatNumber_MVIEW().\n"
                "   				\n\n"
               );
    pyClass.def("pat_thick", &GXMVIEW_wrap_pat_thick,
                "pat_thick((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the pattern line thickness\n\n"

                ":param arg1: Line thickness as fraction of pattern size (ie. 0.05)\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See the IMPORTANT note for sPatNumber_MVIEW().\n\n"
               );
    pyClass.def("symb_angle", &GXMVIEW_wrap_symb_angle,
                "symb_angle((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Symb angle.\n\n"

                ":param arg1: angle in degrees CCW from +X\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("symb_color", &GXMVIEW_wrap_symb_color,
                "symb_color((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Symbol color.\n\n"

                ":param arg1: color\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("symb_fill_color", &GXMVIEW_wrap_symb_fill_color,
                "symb_fill_color((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Symbol color fill.\n\n"

                ":param arg1: Color\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("symb_font", &GXMVIEW_wrap_symb_font,
                "symb_font((str)arg1, (bool)arg2, (int)arg3, (bool)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the symbol font and style.\n\n"

                ":param arg1: face name\n"
                ":type arg1: str\n"
                ":param arg2: Geosoft font? bool\n"
                ":type arg2: bool\n"
                ":param arg3: \\ :ref:`MVIEW_FONT_WEIGHT`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Italic font? bool\n"
                ":type arg4: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the font cannot be found, the DEFAULT_SYMBOL_FONT\n"
                "   					specified in the [MONTAJ] section of GEOSOFT.INI\n"
                "   					will be used.\n"
                "   \n"
                "   					See \\ :func:`geosoft.gxapi.GXMVIEW.text_font`\\  for the font name syntax.\n"
                "   				\n\n"
               );
    pyClass.def("symb_number", &GXMVIEW_wrap_symb_number,
                "symb_number((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Symbol number.\n\n"

                ":param arg1: symbol number\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The lower 16 bits of the number is interpreted as UTF-16 with a valid Unicode character\n"
                "   					code point. GFN fonts wil produce valid symbols depending on the font for 0x01-0x7f and the degree,\n"
                "   					plus-minus and diameter symbol(latin small letter o with stroke) for 0xB0, 0xB1 and 0xF8 respectively.\n"
                "   \n"
                "   					It is possible to check if a character is valid using \\ :func:`geosoft.gxapi.GXUNC.is_valid_utf16_char`\\ . The high 16-bits are reserved\n"
                "   					for future use. Also see: \\ :func:`geosoft.gxapi.GXUNC.valid_symbol`\\  and \\ :func:`geosoft.gxapi.GXUNC.validate_symbols`\\ .\n"
                "   				\n\n"
               );
    pyClass.def("symb_size", &GXMVIEW_wrap_symb_size,
                "symb_size((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Symb size.\n\n"

                ":param arg1: size in view units\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("text_angle", &GXMVIEW_wrap_text_angle,
                "text_angle((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the text angle.\n\n"

                ":param arg1: angle in degrees CCW from +X\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("text_color", &GXMVIEW_wrap_text_color,
                "text_color((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Text color.\n\n"

                ":param arg1: color\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("text_font", &GXMVIEW_wrap_text_font,
                "text_font((str)arg1, (int)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the text font.\n\n"

                ":param arg1: Font face name\n"
                ":type arg1: str\n"
                ":param arg2: Geosoft font? (TRUE or FALSE)\n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`MVIEW_FONT_WEIGHT`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Italic font? (TRUE or FALSE)\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Font characteristics can be defined using the function parameters,\n"
                "   					or may be defined as decorations in the font name.  A decorated font\n"
                "   					name has the following format:\n"
                "   \n"
                "   					font_name(type,weight,italics,charset)\n"
                "   \n"
                "   					where\n"
                "   					type     - \"TT\" or \"GFN\"\n"
                "   					weight   - last word from MVIEW_FONT_WEIGHT_ (ie. \"LIGHT\")\n"
                "   					italics  - \"ITALICS\" for for italics\n"
                "   					charset  - Before version 6.2. this decoration was honoured and it affected the display\n"
                "   					of characters above ASCII 127. 6.2. introduced Unicode in the core\n"
                "   					montaj engine that eliminated the need for such a setting. All strings\n"
                "   					on the GX API level are encoded in UTF8 during runtime which makes it possible\n"
                "   					to represent all possible characters without using character sets. This decoration\n"
                "   					will now be ignored.\n"
                "   \n"
                "   					Qualifiers take precidence over passed parameters.\n"
                "   					The order of qualifiers is not relevant.\n"
                "   \n"
                "   					examples:\n"
                "   \n"
                "   					\"sr(GFN,ITALICS)\"  - geosoft GFN font, normal weight, italics\n"
                "   					\"Arial(TT,XBOLD)\"  - TrueType font, bold\n"
                "   					\"Times(TT,ITALICS,_EastEurope)\"\n"
                "   					- TrueType font, italics, Eastern Europe charcters\n"
                "   \n"
                "   					Decorated name qualifiers take precedence over passed parameters.\n"
                "   \n"
                "   					If the font cannot be found, or if \"Default\" is used, the DEFAULT_MAP_FONT\n"
                "   					specified in the [MONTAJ] section of GEOSOFT.INI\n"
                "   					will be used.\n"
                "   				\n\n"
               );
    pyClass.def("text_ref", &GXMVIEW_wrap_text_ref,
                "text_ref((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the text plot reference point.\n\n"

                ":param arg1: \\ :ref:`TEXT_REF`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("text_size", &GXMVIEW_wrap_text_size,
                "text_size((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the text size.\n\n"

                ":param arg1: size in view units\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Because views may have differing X and Y scales this size can only make sense in one of these directions\n"
                "   					otherwise text would appear warped on these kinds of views. The X direction was chosen to represent the\n"
                "   					font size. For instance if the X scale is 1 unit/mm and my Y scale is 2 units/mm a font size of 3.0 view\n"
                "   					units will result in un-rotated text that appears 6 view units or 3mm high in the Y direction.\n"
                "   \n"
                "   					Another important thing to keep in mind that this size represents what is known as the \"ascent\" height\n"
                "   					of the font. The full height of the text may be higher if characters with accents or lower extension\n"
                "   					(e.g. the lowercase y) appear in the text. For TrueType fonts the mapping system will do a best effort\n"
                "   					positioning and sizing of the text using the alignment set and information about the font that it queries\n"
                "   					from the operating system. For instance; if Arial text \"Blog\" is placed at (0,0) and the alignment\n"
                "   					setting is Left-Bottom the left side of the B should be aligned at 0 in the X direction and the\n"
                "   					bottom of all the letters except y will be at 0 in the Y direction. The lower part of the y will extend\n"
                "   					below 0 in the Y (this is known as the \"descent\" height of the font at this size). The letters B and l\n"
                "   					should be very close to the size set here (this may differ slightly for different fonts).\n"
                "   				\n\n"
               );
    pyClass.def("transparency", &GXMVIEW_wrap_transparency,
                "transparency((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the transparency for new objects.\n\n"

                ":param arg1: Transparency (1.0 - Opaque, 0.0 - Transparent)\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1.0 Renders completely opaque objects while 0.0 will be transparent.\n"
                "   					Objects written after this will have a combined transparency value with the\n"
                "   					group transparency if it is set (e.g. 0.5 for group and 0.8 stream will result in 0.4).\n"
                "   				\n\n"
               );
    pyClass.def("z_value", &GXMVIEW_wrap_z_value,
                "z_value((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets Z-value info.\n\n"

                ":param arg1: Z-Value\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This number is stored in map mainly for exports to other vector formats (e.g ShapeFiles)\n"
                "   					A contour map that's exported to a shape file will use this value as a Z-value attributes for its shapes.\n"
                "   				\n\n"
               );
    pyClass.def("arc", &GXMVIEW_wrap_arc,
                "arc((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw an arc.\n\n"

                ":param arg1: center x\n"
                ":type arg1: float\n"
                ":param arg2: center y\n"
                ":type arg2: float\n"
                ":param arg3: radius\n"
                ":type arg3: float\n"
                ":param arg4: ratio x/y\n"
                ":type arg4: float\n"
                ":param arg5: angle\n"
                ":type arg5: float\n"
                ":param arg6: start angle\n"
                ":type arg6: float\n"
                ":param arg7: end angle\n"
                ":type arg7: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("chord", &GXMVIEW_wrap_chord,
                "chord((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a filled arc.\n\n"

                ":param arg1: center x\n"
                ":type arg1: float\n"
                ":param arg2: center y\n"
                ":type arg2: float\n"
                ":param arg3: radius\n"
                ":type arg3: float\n"
                ":param arg4: ratio x/y\n"
                ":type arg4: float\n"
                ":param arg5: angle\n"
                ":type arg5: float\n"
                ":param arg6: start angle\n"
                ":type arg6: float\n"
                ":param arg7: end angle\n"
                ":type arg7: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("classified_symbols", &GXMVIEW_wrap_classified_symbols,
                "classified_symbols((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (float)arg4, (float)arg5, (str)arg6, (str)arg7, (str)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot classified symbols\n\n"

                ":param arg1: X VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Data VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: scale factor to convert mm to view units\n"
                ":type arg4: float\n"
                ":param arg5: Classified minimum Z to plot\n"
                ":type arg5: float\n"
                ":param arg6: comma delimited list of Z maximums\n"
                ":type arg6: str\n"
                ":param arg7: comma delimited list of sizes in mm\n"
                ":type arg7: str\n"
                ":param arg8: comma delimited list of colour strings\n"
                ":type arg8: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					For example, to plot three levels <95, 95-100 and\n"
                "   					100-120, three string arguments would be:\n"
                "   \n"
                "   					\"95,100,120\"      maximums of each class\n"
                "   					\"2.0,2.5,3.0\"     sizes in mm\n"
                "   					\"y,g,r\"           fill colours\n"
                "   				\n\n"
               );
    pyClass.def("complex_polygon", &GXMVIEW_wrap_complex_polygon,
                "complex_polygon((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a polygon with holes in it.\n\n"

                ":param arg1: VV of type int holding the number of points for each polygon\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: X coordinates.\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y coordinates.\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   You pass a VV with polygon sizes and 2 point vvs.\n\n"
               );
    pyClass.def("ellipse", &GXMVIEW_wrap_ellipse,
                "ellipse((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw an ellipse\n\n"

                ":param arg1: center x\n"
                ":type arg1: float\n"
                ":param arg2: center y\n"
                ":type arg2: float\n"
                ":param arg3: radius\n"
                ":type arg3: float\n"
                ":param arg4: ratio x/y\n"
                ":type arg4: float\n"
                ":param arg5: angle\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("line", &GXMVIEW_wrap_line,
                "line((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a line.\n\n"

                ":param arg1: x0\n"
                ":type arg1: float\n"
                ":param arg2: y0\n"
                ":type arg2: float\n"
                ":param arg3: x1\n"
                ":type arg3: float\n"
                ":param arg4: y1\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("line_vv", &GXMVIEW_wrap_line_vv,
                "line_vv((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw line segments stored in a GS_D2LINE VV.\n\n"

                ":param arg1: VV for GS_D2LINE\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("polygon_dm", &GXMVIEW_wrap_polygon_dm,
                "polygon_dm((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Like PolyLineDm, but draw polygons.\n\n"

                ":param arg1: X coordinates.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y coordinates.\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.6\n\n"
               );
    pyClass.def("polygon_ply", &GXMVIEW_wrap_polygon_ply,
                "polygon_ply((GXPLY)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a complex polygon from PLY.\n\n"

                ":param arg1: PLY\n"
                ":type arg1: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("poly_line", &GXMVIEW_wrap_poly_line,
                "poly_line((int)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a polyline or polygon (dummies deleted).\n\n"

                ":param arg1: \\ :ref:`MVIEW_DRAW`\\ \n"
                ":type arg1: int\n"
                ":param arg2: X coordinates.\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y coordinates.\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Dummies in X and/or Y VV are deleted and it results\n"
                "   					in 'solid' line. Using \\ :func:`geosoft.gxapi.GXMVIEW.poly_line_dm`\\  (below) function\n"
                "   					if gaps from dummies are to be kept.\n"
                "   				\n\n"
               );
    pyClass.def("poly_line_dm", &GXMVIEW_wrap_poly_line_dm,
                "poly_line_dm((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a polyline with gaps defined by dummies in X/Y VVs\n\n"

                ":param arg1: X coordinates.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y coordinates.\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("poly_wrap", &GXMVIEW_wrap_poly_wrap,
                "poly_wrap((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw wrapped polylines from X and Y VV's.\n\n"

                ":param arg1: X coordinates.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y coordinates.\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Convert a given VVy into a wrapped VVy using\n"
                "   					the current view window as the wrap region.\n"
                "   					Then draw polylines from it.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.poly_line`\\ \n\n"
               );
    pyClass.def("rectangle", &GXMVIEW_wrap_rectangle,
                "rectangle((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a rectangle.\n\n"

                ":param arg1: x0\n"
                ":type arg1: float\n"
                ":param arg2: y0\n"
                ":type arg2: float\n"
                ":param arg3: x1\n"
                ":type arg3: float\n"
                ":param arg4: y1\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("segment", &GXMVIEW_wrap_segment,
                "segment((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a filled segment of an ellipse.\n\n"

                ":param arg1: center x\n"
                ":type arg1: float\n"
                ":param arg2: center y\n"
                ":type arg2: float\n"
                ":param arg3: radius\n"
                ":type arg3: float\n"
                ":param arg4: ratio x/y\n"
                ":type arg4: float\n"
                ":param arg5: angle\n"
                ":type arg5: float\n"
                ":param arg6: start angle\n"
                ":type arg6: float\n"
                ":param arg7: end angle\n"
                ":type arg7: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"
               );
    pyClass.def("size_symbols", &GXMVIEW_wrap_size_symbols,
                "size_symbols((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot sized symbols\n\n"

                ":param arg1: X\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: symbol sizes (in view units)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("symbol", &GXMVIEW_wrap_symbol,
                "symbol((float)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot a symbol\n\n"

                ":param arg1: X\n"
                ":type arg1: float\n"
                ":param arg2: Y\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("symbols", &GXMVIEW_wrap_symbols,
                "symbols((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot symbols\n\n"

                ":param arg1: X\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("symbols_itr", &GXMVIEW_wrap_symbols_itr,
                "symbols_itr((str)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot symbols using an ITR\n\n"

                ":param arg1: ITR file name (ZON or ITR)\n"
                ":type arg1: str\n"
                ":param arg2: X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Z\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("text", &GXMVIEW_wrap_text,
                "text((str)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw text.\n\n"

                ":param arg1: text to plot\n"
                ":type arg1: str\n"
                ":param arg2: x location of text\n"
                ":type arg2: float\n"
                ":param arg3: y location of text\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("aggregate", &GXMVIEW_wrap_aggregate,
                "aggregate((GXAGG)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add an aggregate to a view.\n\n"

                ":param arg1: Aggregate\n"
                ":type arg1: :class:`geosoft.gxapi.GXAGG`\n"
                ":param arg2: Aggregate name Maximum length is MVIEW_NAME_LENGTH\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("change_line_message", &GXMVIEW_wrap_change_line_message,
                "change_line_message((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Change the specified line in a view.\n\n"

                ":param arg1: Change to this line\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The line name can be created by calling LineLabel_DB using\n"
                "   					DB_LINE_LABEL_FORMAT_LINK. This insures that the label is\n"
                "   					created is the same way as used in the database.\n"
                "   				\n\n"
               );
    pyClass.def("col_symbol", &GXMVIEW_wrap_col_symbol,
                "col_symbol((str)arg1, (GXCSYMB)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a colored symbol object to a view.\n\n"

                ":param arg1: Name of the color symbol group\n"
                ":type arg1: str\n"
                ":param arg2: CSYMB object\n"
                ":type arg2: :class:`geosoft.gxapi.GXCSYMB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("datalinkd", &GXMVIEW_wrap_datalinkd,
                "datalinkd((GXDATALINKD)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a Data Link Display (DATALINKD) object to the view.\n\n"

                ":param arg1: DATALINKD\n"
                ":type arg1: :class:`geosoft.gxapi.GXDATALINKD`\n"
                ":param arg2: name Maximum length is MVIEW_NAME_LENGTH\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               );
    pyClass.def("easy_maker", &GXMVIEW_wrap_easy_maker,
                "easy_maker((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Used for GX makers which use both maps and databases.\n\n"

                ":param arg1: Maker name, used in menu prompt\n"
                ":type arg1: str\n"
                ":param arg2: INI groups (terminate each with a \";\")\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("emf_object", &GXMVIEW_wrap_emf_object,
                "emf_object((float)arg1, (float)arg2, (float)arg3, (float)arg4, (str)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add an EMF file data object to the view.\n\n"

                ":param arg1: Min X\n"
                ":type arg1: float\n"
                ":param arg2: Min Y\n"
                ":type arg2: float\n"
                ":param arg3: Max X\n"
                ":type arg3: float\n"
                ":param arg4: Max Y\n"
                ":type arg4: float\n"
                ":param arg5: EMF File holding data\n"
                ":type arg5: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               );
    pyClass.def("external_string_object", &GXMVIEW_wrap_external_string_object,
                "external_string_object((float)arg1, (float)arg2, (float)arg3, (float)arg4, (str)arg5, (str)arg6, (str)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add an external string data object to the view.\n\n"

                ":param arg1: Min X\n"
                ":type arg1: float\n"
                ":param arg2: Min Y\n"
                ":type arg2: float\n"
                ":param arg3: Max X\n"
                ":type arg3: float\n"
                ":param arg4: Max Y\n"
                ":type arg4: float\n"
                ":param arg5: name of external object\n"
                ":type arg5: str\n"
                ":param arg6: class of external object\n"
                ":type arg6: str\n"
                ":param arg7: string data of external object\n"
                ":type arg7: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("link", &GXMVIEW_wrap_link,
                "link((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Make a link to a database.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Link name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("maker", &GXMVIEW_wrap_maker,
                "maker((int)arg1, (int)arg2, (str)arg3, (int)arg4, (str)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generates a Maker for the database and/or map.\n\n"

                ":param arg1: Database required? (0 = No, 1 = Yes)\n"
                ":type arg1: int\n"
                ":param arg2: Map required?      (0 = No, 1 = Yes)\n"
                ":type arg2: int\n"
                ":param arg3: Program name\n"
                ":type arg3: str\n"
                ":param arg4: \\ :ref:`MAKER`\\ \n"
                ":type arg4: int\n"
                ":param arg5: Maker name, used in menu prompt\n"
                ":type arg5: str\n"
                ":param arg6: INI groups (terminate each with a \";\")\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("meta", &GXMVIEW_wrap_meta,
                "meta((GXMETA)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Store Metadata in a group\n\n"

                ":param arg1: META object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg2: Menu name of Object\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );
    pyClass.def("voxd", &GXMVIEW_wrap_voxd,
                "voxd((GXVOXD)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a Voxel Display (VOXD) object to the view.\n\n"

                ":param arg1: VOXD\n"
                ":type arg1: :class:`geosoft.gxapi.GXVOXD`\n"
                ":param arg2: name Maximum length is MVIEW_NAME_LENGTH\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("get_voxd", &GXMVIEW_wrap_get_voxd,
                "get_voxd((int)arg1) -> GXVOXD:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an existing VOXD object from the view.\n\n"

                ":param arg1: group number\n"
                ":type arg1: int\n"
                ":returns: VOXD object - cache only - use immediately.\n"
                ":rtype: :class:`geosoft.gxapi.GXVOXD`\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"
               );
    pyClass.def("draw_vector_voxel_vectors", &GXMVIEW_wrap_draw_vector_voxel_vectors,
                "draw_vector_voxel_vectors((GXVOX)arg1, (str)arg2, (GXITR)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display vectors from a vector voxel in the view.\n\n"

                ":param arg1: VOX\n"
                ":type arg1: :class:`geosoft.gxapi.GXVOX`\n"
                ":param arg2: view group name Maximum length is MVIEW_NAME_LENGTH\n"
                ":type arg2: str\n"
                ":param arg3: Image transform - must contain zones\n"
                ":type arg3: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg4: Vector length scale factor - w.r.t. the voxel minimum horizontal cell size (default 1)\n"
                ":type arg4: float\n"
                ":param arg5: Ratio of the vector cone height to its base (default 4)\n"
                ":type arg5: float\n"
                ":param arg6: Ratio of maximum base size to minimum horizontal cell size (default 0.25)\n"
                ":type arg6: float\n"
                ":param arg7: Cutoff value - do not plot vectors with amplitudes less than this value (rDUMMY or 0 to plot all)\n"
                ":type arg7: float\n"
                ":param arg8: Maximum number of vectors - decimate as required to reduce (iDUMMY to plot all)\n"
                ":type arg8: int\n"
                ":returns: Each data value in a vector voxel contains X, Y and Z components of a vector. The amplitudes do NOT necessarily correspond to the spatial size of the voxel.\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.6.0\n\n"
               );
    pyClass.def("draw_vectors_3d", &GXMVIEW_wrap_draw_vectors_3d,
                "draw_vectors_3d((str)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7, (GXITR)arg8, (float)arg9, (float)arg10, (float)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display vectors in the view.\n\n"

                ":param arg1: view group name Maximum length is MVIEW_NAME_LENGTH\n"
                ":type arg1: str\n"
                ":param arg2: X locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y locations\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Z locations\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Vector X component\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Vector Y component\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Vector Z component\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Image transform - must contain zones\n"
                ":type arg8: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg9: Scale factor for the longest vector in map units / vector units. Vector lengths for the rest of the vectors scale by the square root of the vector amplitudes.\n"
                "             							This results in the apparent (viewed) area of the vector being proportional to the amplitude.\n"
                ":type arg9: float\n"
                ":param arg10: Ratio of the vector cone height to its base (default 4)\n"
                ":type arg10: float\n"
                ":param arg11: Maximum base size in view units. Leave blank (dummy) for no limit. If applied this can make larger vectors skinnier, but does not reduce the length, so they don't obscure other vectors as much.\n"
                ":type arg11: float\n"
                ":returns: Plot vectors as cones scaled in area to the maximum amplitude\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"
               );
    pyClass.def("copy_marked_groups", &GXMVIEW_wrap_copy_marked_groups,
                "copy_marked_groups((GXMVIEW)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copies all marked groups from one view into another view\n\n"

                ":param arg1: Destination MVIEW\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Projections in source and destination views are used to copy the\n"
                "   					entities. Entities are clipped by the destination view's clipping\n"
                "   					region.\n"
                "   				\n\n"
               );
    pyClass.def("copy_raw_marked_groups", &GXMVIEW_wrap_copy_raw_marked_groups,
                "copy_raw_marked_groups((GXMVIEW)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copies all marked groups raw from one view into another\n\n"

                ":param arg1: Destination MVIEW\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The projections, and clipping is completly ignored.\n\n"
               );
    pyClass.def("crc_group", &GXMVIEW_wrap_crc_group,
                "crc_group((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute CRC for a group.\n\n"

                ":param arg1: Group name\n"
                ":type arg1: str\n"
                ":param arg2: CRC to start (use \\ :ref:`CRC_INIT_VALUE`\\ )\n"
                ":type arg2: int\n"
                ":returns: CRC\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("delete_group", &GXMVIEW_wrap_delete_group,
                "delete_group((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete a group.\n\n"

                ":param arg1: Group name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Does nothing if the group does not already exist.\n\n"
               );
    pyClass.def("del_marked_groups", &GXMVIEW_wrap_del_marked_groups,
                "del_marked_groups() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete marked groups.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_group_extent", &GXMVIEW_wrap_get_group_extent,
                "get_group_extent((str)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get extent of a group in a view\n\n"

                ":param arg1: group name\n"
                ":type arg1: str\n"
                ":param arg2: Minimum X, returned\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Minimum Y, returned\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Maximum X, returned\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Maximum Y, returned\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: \\ :ref:`MVIEW_UNIT`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_group_transparency", &GXMVIEW_wrap_get_group_transparency,
                "get_group_transparency((str)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the transparency value of group\n\n"

                ":param arg1: Group name\n"
                ":type arg1: str\n"
                ":param arg2: Transparency (1.0 - Opaque, 0.0 - Transparent)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("group_to_ply", &GXMVIEW_wrap_group_to_ply,
                "group_to_ply((str)arg1, (GXPLY)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save all polygons in group into PLY obj.\n\n"

                ":param arg1: Group name\n"
                ":type arg1: str\n"
                ":param arg2: PLY to add to\n"
                ":type arg2: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The coordinates will be in the working coordinate system\n"
                "   					of the view.  The SetWorkingIPJ_MVIEW method can be used\n"
                "   					to change the working coordinate system. This function will\n"
                "   					return an empty PLY if the group is hidden.\n"
                "   				\n\n"
               );
    pyClass.def("hide_marked_groups", &GXMVIEW_wrap_hide_marked_groups,
                "hide_marked_groups((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Hide/Show marked groups.\n\n"

                ":param arg1: \\ :ref:`MVIEW_HIDE`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("hide_shadow2_d_interpretations", &GXMVIEW_wrap_hide_shadow2_d_interpretations,
                "hide_shadow2_d_interpretations((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Hide/Show 2d shadow interpretations.\n\n"

                ":param arg1: \\ :ref:`MVIEW_HIDE`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               );
    pyClass.def("exist_group", &GXMVIEW_wrap_exist_group,
                "exist_group((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Checks to see if a group exists.\n\n"

                ":param arg1: Group name\n"
                ":type arg1: str\n"
                ":returns: 0  - group does not exist.\n"
                "          						1  - group exists.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("gen_new_group_name", &GXMVIEW_wrap_gen_new_group_name,
                "gen_new_group_name((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Generate the name of a group from a base name that\n"
                "   					is new. (always unique and won't overwrite existing\n"
                "   					objects).\n"
                "   				\n\n"

                ":param arg1: Base Name of group\n"
                ":type arg1: str\n"
                ":param arg2: New Name of group\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"
               );
    pyClass.def("is_group", &GXMVIEW_wrap_is_group,
                "is_group((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Query a status or characteristic of a group\n\n"

                ":param arg1: group name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`MVIEW_IS`\\ \n"
                ":type arg2: int\n"
                ":returns: TRUE or FALSE (1 or 0)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"
               );
    pyClass.def("is_group_empty", &GXMVIEW_wrap_is_group_empty,
                "is_group_empty((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is the group empty?\n\n"

                ":param arg1: group name\n"
                ":type arg1: str\n"
                ":returns: TRUE or FALSE (1 or 0)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("is_movable", &GXMVIEW_wrap_is_movable,
                "is_movable() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this view movable?\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Views are always physically movable in the API, this\n"
                "   					flag is for preventing accidental moving in the GUI.\n"
                "   					By default views are not movable.\n"
                "   				\n\n"
               );
    pyClass.def("is_visible", &GXMVIEW_wrap_is_visible,
                "is_visible() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this view visible?\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("list_groups", &GXMVIEW_wrap_list_groups,
                "list_groups((GXLST)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of the groups in a view.\n\n"

                ":param arg1: list\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`MVIEW_GROUP_LIST`\\ \n"
                ":type arg2: int\n"
                ":returns: Number of groups in the list\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("render_order", &GXMVIEW_wrap_render_order,
                "render_order() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Query the view render order\n\n"

                ":returns: Render order\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Views with lower numbers should render first, iDUMMY is undefined\n\n"
               );
    pyClass.def("mark_all_groups", &GXMVIEW_wrap_mark_all_groups,
                "mark_all_groups((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Mark or unmark all groups.\n\n"

                ":param arg1: 0 - unmark, 1 - mark\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("mark_empty_groups", &GXMVIEW_wrap_mark_empty_groups,
                "mark_empty_groups((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Mark/unmark all empty groups.\n\n"

                ":param arg1: 0 - unmark, 1 - mark\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("mark_group", &GXMVIEW_wrap_mark_group,
                "mark_group((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Mark or unmark a specific group\n\n"

                ":param arg1: group name\n"
                ":type arg1: str\n"
                ":param arg2: 0 - unmark, 1 - mark\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("move_group_backward", &GXMVIEW_wrap_move_group_backward,
                "move_group_backward((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Move the group backward one position (render sooner).\n\n"

                ":param arg1: Group name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("move_group_forward", &GXMVIEW_wrap_move_group_forward,
                "move_group_forward((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Move the group forward one position (render later).\n\n"

                ":param arg1: Group name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("move_group_to_back", &GXMVIEW_wrap_move_group_to_back,
                "move_group_to_back((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Move the group to the back (render first).\n\n"

                ":param arg1: Group name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("move_group_to_front", &GXMVIEW_wrap_move_group_to_front,
                "move_group_to_front((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Move the group to the front (render last).\n\n"

                ":param arg1: Group name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("rename_group", &GXMVIEW_wrap_rename_group,
                "rename_group((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Rename a group.\n\n"

                ":param arg1: Old group name\n"
                ":type arg1: str\n"
                ":param arg2: New group name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Does nothing if the group does not already exist.\n\n"
               );
    pyClass.def("set_group_moveable", &GXMVIEW_wrap_set_group_moveable,
                "set_group_moveable((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the movable attribute of a group.\n\n"

                ":param arg1: group name\n"
                ":type arg1: str\n"
                ":param arg2: 0 - not movable, 1 - movable\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"
               );
    pyClass.def("set_group_transparency", &GXMVIEW_wrap_set_group_transparency,
                "set_group_transparency((str)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the transparency value of group\n\n"

                ":param arg1: Group name\n"
                ":type arg1: str\n"
                ":param arg2: Transparency  (1.0 - Opaque, 0.0 - Transparent)\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("set_mark_moveable", &GXMVIEW_wrap_set_mark_moveable,
                "set_mark_moveable((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the movable attribute of marked groups.\n\n"

                ":param arg1: 0 - not movable, 1 - movable\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"
               );
    pyClass.def("set_movability", &GXMVIEW_wrap_set_movability,
                "set_movability((bool)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the view movability\n\n"

                ":param arg1: bool\n"
                ":type arg1: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Views are always physically movable in the API, this\n"
                "   					flag is for preventing accidental moving in the GUI.\n"
                "   					By default views are not movable.\n"
                "   				\n\n"
               );
    pyClass.def("set_render_order", &GXMVIEW_wrap_set_render_order,
                "set_render_order((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the view render order\n\n"

                ":param arg1: Render order\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Views with lower numbers should render first, iDUMMY is undefined\n\n"
               );
    pyClass.def("set_visibility", &GXMVIEW_wrap_set_visibility,
                "set_visibility((bool)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the view visibility\n\n"

                ":param arg1: bool\n"
                ":type arg1: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("start_group", &GXMVIEW_wrap_start_group,
                "start_group((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Start a group.\n\n"

                ":param arg1: Group name, can be NULL, Maximum length is \\ :ref:`MVIEW_NAME_LENGTH`\\ \n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`MVIEW_GROUP`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Line and fill colours and thickness must be set\n"
                "   					before drawing to a group.\n"
                "   \n"
                "   					If the group name is NULL, output will be sent to\n"
                "   					the primary group stream and the \\ :ref:`MVIEW_GROUP`\\  is\n"
                "   					ignored.\n"
                "   \n"
                "   					Group names must be different from view names.\n"
                "   				\n\n"
               );
    pyClass.def("set_working_ipj", &GXMVIEW_wrap_set_working_ipj,
                "set_working_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the working projection of the view.\n\n"

                ":param arg1: The input projection\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The working projection is the coordinate system of coordinates drawn to\n"
                "   					the view.  The working coordinate system can be different than the view\n"
                "   					coordinate system, in which case the coordinates are re-projected to the\n"
                "   					view coordinate system before they are placed in the view.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.mode_pj`\\  to control use of the working projection.\n\n"
               );
    pyClass.def("clear_esrild_ts", &GXMVIEW_wrap_clear_esrild_ts,
                "clear_esrild_ts() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clear ESRI local datum transformations currently in use.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               );
    pyClass.def("is_projection_empty", &GXMVIEW_wrap_is_projection_empty,
                "is_projection_empty() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns 1 if the view projection and view user projection are both empty (undefined).\n\n"

                ":returns: 1 if the view projection and view user projection are both empty.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Use, for instance, to see if the map view contains projection information. The first time you add data that\n"
                "   				has projection information you should set up an empty view projection so that subsequent data added with a different\n"
                "   			   projection is properly displayed in relation to the initial data.\n\n"
               );
    pyClass.def("get_ipj", &GXMVIEW_wrap_get_ipj,
                "get_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the projection of the view.\n\n"

                ":param arg1: IPJ in which to place the view IPJ\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_user_ipj", &GXMVIEW_wrap_get_user_ipj,
                "get_user_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the user projection of the view.\n\n"

                ":param arg1: IPJ in which to place the view IPJ\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("mode_pj", &GXMVIEW_wrap_mode_pj,
                "mode_pj((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the working projection mode\n\n"

                ":param arg1: \\ :ref:`MVIEW_PJ`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This controls how your coordinates and attributes will be interpreted.\n"
                "   					A working projection must be set useing SetWorkingIPJ_MVIEW for this\n"
                "   					method to have any effect.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   SetWorkingIPJ\n\n"
               );
    pyClass.def("north", &GXMVIEW_wrap_north,
                "north() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns North direction at center of view.\n\n"

                ":returns: North direction id deg. azimuth relative to view Y.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					North is calculated from the IPJ North direction.\n"
                "   					It will be rDUMMY if IPJ is unknown.\n"
                "   				\n\n"
               );
    pyClass.def("set_ipj", &GXMVIEW_wrap_set_ipj,
                "set_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the projection of the view.\n\n"

                ":param arg1: IPJ to place in the view\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					As of v5.1.8, this function also sets the User IPJ,\n"
                "   					and automatically clears the WARP before doing so, so\n"
                "   					that instead of the following construction:\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXMVIEW.set_ipj`\\ (View,hIPJ);\n"
                "   					ClearWarp_IPJ(hIPJ);\n"
                "   					\\ :func:`geosoft.gxapi.GXMVIEW.set_user_ipj`\\ (View,hIPJ);\n"
                "   \n"
                "   					you can simply use:\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXMVIEW.set_ipj`\\ (View,hIPJ);\n"
                "   				\n\n"
               );
    pyClass.def("set_user_ipj", &GXMVIEW_wrap_set_user_ipj,
                "set_user_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the user projection of the view.\n\n"

                ":param arg1: IPJ to place in the view\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_3d_group_flags", &GXMVIEW_wrap_get_3d_group_flags,
                "get_3d_group_flags((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a 3D geometry group's 3D rendering flags.\n\n"

                ":param arg1: Group number\n"
                ":type arg1: int\n"
                ":returns: Combination of \\ :ref:`MVIEW_3D_RENDER`\\  flags or 0\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.1.0\n\n"
               );
    pyClass.def("set_3d_group_flags", &GXMVIEW_wrap_set_3d_group_flags,
                "set_3d_group_flags((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a 3D geometry group's 3D rendering flags.\n\n"

                ":param arg1: Group number\n"
                ":type arg1: int\n"
                ":param arg2: Combination of \\ :ref:`MVIEW_3D_RENDER`\\  flags or 0\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.1.0\n\n"
               );
    pyClass.def("get_group_freeze_scale", &GXMVIEW_wrap_get_group_freeze_scale,
                "get_group_freeze_scale((int)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a scale freezing value for the group (rDUMMY for disabled).\n\n"

                ":param arg1: Group number\n"
                ":type arg1: int\n"
                ":param arg2: Variable to fill with freeze scale\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("set_freeze_scale", &GXMVIEW_wrap_set_freeze_scale,
                "set_freeze_scale((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a scale freezing value into stream (rDUMMY for disabled).\n\n"

                ":param arg1: Freeze Scale value\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Objects written after this will override any scale freezing set for the group\n\n"
               );
    pyClass.def("set_group_freeze_scale", &GXMVIEW_wrap_set_group_freeze_scale,
                "set_group_freeze_scale((int)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a scale freezing value for the group (rDUMMY for disabled).\n\n"

                ":param arg1: Group number\n"
                ":type arg1: int\n"
                ":param arg2: Variable to fill with freeze scale\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("find_group", &GXMVIEW_wrap_find_group,
                "find_group((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Find a Group by name.\n\n"

                ":param arg1: Group name\n"
                ":type arg1: str\n"
                ":returns: Group Number.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("group_name", &GXMVIEW_wrap_group_name,
                "group_name((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a group name\n\n"

                ":param arg1: group number, error if not valid\n"
                ":type arg1: int\n"
                ":param arg2: Group Name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("render", &GXMVIEW_wrap_render,
                "render((HDC)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Render a specified area of view onto a Windows DC handle\n\n"

                ":param arg1: DC Handle\n"
                ":type arg1: :class:`geosoft.gxapi.HDC`\n"
                ":param arg2: left value of the render rect in Windows coordinates (bottom>top)\n"
                ":type arg2: int\n"
                ":param arg3: bottom value\n"
                ":type arg3: int\n"
                ":param arg4: right value\n"
                ":type arg4: int\n"
                ":param arg5: top value\n"
                ":type arg5: int\n"
                ":param arg6: area X minimum\n"
                ":type arg6: float\n"
                ":param arg7: area Y minimum\n"
                ":type arg7: float\n"
                ":param arg8: area X maximum\n"
                ":type arg8: float\n"
                ":param arg9: area Y maximum\n"
                ":type arg9: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               );
    pyClass.def("set_u_fac", &GXMVIEW_wrap_set_u_fac,
                "set_u_fac((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the unit conversion of a view.\n\n"

                ":param arg1: New UFac value\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("axis_x", &GXMVIEW_wrap_axis_x,
                "axis_x((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw an X axis\n\n"

                ":param arg1: Y location in view units\n"
                ":type arg1: float\n"
                ":param arg2: left  X\n"
                ":type arg2: float\n"
                ":param arg3: right X\n"
                ":type arg3: float\n"
                ":param arg4: major tick interval\n"
                ":type arg4: float\n"
                ":param arg5: minor tick interval (half size of major)\n"
                ":type arg5: float\n"
                ":param arg6: tick size in view units (negative for down ticks)\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   All coordinates are in view units.\n\n"

                "\n.. seealso::\n\n"
                "   rOptimumTick_MVIEW\n\n"
               );
    pyClass.def("axis_y", &GXMVIEW_wrap_axis_y,
                "axis_y((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a  Y axis\n\n"

                ":param arg1: X location in view units\n"
                ":type arg1: float\n"
                ":param arg2: bottom Y\n"
                ":type arg2: float\n"
                ":param arg3: top    Y\n"
                ":type arg3: float\n"
                ":param arg4: major tick interval\n"
                ":type arg4: float\n"
                ":param arg5: minor tick interval (half size of major)\n"
                ":type arg5: float\n"
                ":param arg6: tick size in view units (negative for left ticks)\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   All coordinates are in view units.\n\n"

                "\n.. seealso::\n\n"
                "   rOptimumTick_MVIEW\n\n"
               );
    pyClass.def("grid", &GXMVIEW_wrap_grid,
                "grid((float)arg1, (float)arg2, (float)arg3, (float)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a grid in the current window\n\n"

                ":param arg1: X grid increment\n"
                ":type arg1: float\n"
                ":param arg2: Y grid increment\n"
                ":type arg2: float\n"
                ":param arg3: dX dot increment/cross X size\n"
                ":type arg3: float\n"
                ":param arg4: dY dot increment/cross Y size\n"
                ":type arg4: float\n"
                ":param arg5: \\ :ref:`MVIEW_GRID`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The grid will be drawn in the current window specified\n"
                "   					by the last SetWindow call.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.axis_x`\\ , \\ :func:`geosoft.gxapi.GXMVIEW.axis_y`\\ , \\ :func:`geosoft.gxapi.GXMVIEW.optimum_tick`\\ \n\n"
               );
    pyClass.def("label_fid", &GXMVIEW_wrap_label_fid,
                "label_fid((GXVV)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Label fiducials on a profile\n\n"

                ":param arg1: X VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: fiducial start\n"
                ":type arg2: float\n"
                ":param arg3: fiducial increment\n"
                ":type arg3: float\n"
                ":param arg4: fiducial label interval, default 100.0\n"
                ":type arg4: float\n"
                ":param arg5: Y location in view unit\n"
                ":type arg5: float\n"
                ":param arg6: Y scale\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A 1mm long vertical tick is drawn at the place\n"
                "   					where a label is present. The label is drawn\n"
                "   					below the tick.\n"
                "   \n"
                "   					The incoming X VV is used to define the place for\n"
                "   					label.\n"
                "   				\n\n"
               );
    pyClass.def("label_x", &GXMVIEW_wrap_label_x,
                "label_x((float)arg1, (float)arg2, (float)arg3, (float)arg4, (int)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Label annotations on the X axis\n\n"

                ":param arg1: Y location in view units\n"
                ":type arg1: float\n"
                ":param arg2: left  X\n"
                ":type arg2: float\n"
                ":param arg3: right X\n"
                ":type arg3: float\n"
                ":param arg4: label interval\n"
                ":type arg4: float\n"
                ":param arg5: \\ :ref:`MVIEW_LABEL_JUST`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`MVIEW_LABEL_BOUND`\\ \n"
                ":type arg6: int\n"
                ":param arg7: \\ :ref:`MVIEW_LABEL_ORIENT`\\ \n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Label bounding will justify edge labels to be inside\n"
                "   					the bar limits. But bounding does not apply if\n"
                "   					labels are drawn vertically (top right or top left)\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.axis_x`\\ , \\ :func:`geosoft.gxapi.GXMVIEW.axis_y`\\ , \\ :func:`geosoft.gxapi.GXMVIEW.optimum_tick`\\ \n\n"
               );
    pyClass.def("label_y", &GXMVIEW_wrap_label_y,
                "label_y((float)arg1, (float)arg2, (float)arg3, (float)arg4, (int)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Label annotations on the Y axis\n\n"

                ":param arg1: X location in view units\n"
                ":type arg1: float\n"
                ":param arg2: bottom Y\n"
                ":type arg2: float\n"
                ":param arg3: top    Y\n"
                ":type arg3: float\n"
                ":param arg4: label interval\n"
                ":type arg4: float\n"
                ":param arg5: \\ :ref:`MVIEW_LABEL_JUST`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`MVIEW_LABEL_BOUND`\\ \n"
                ":type arg6: int\n"
                ":param arg7: \\ :ref:`MVIEW_LABEL_ORIENT`\\ \n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Label bounding will justify edge labels to be inside\n"
                "   					the bar limits. But bounding does not apply if\n"
                "   					labels are drawn vertically (top right or top left)\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.axis_x`\\ , \\ :func:`geosoft.gxapi.GXMVIEW.axis_y`\\ , \\ :func:`geosoft.gxapi.GXMVIEW.optimum_tick`\\ \n\n"
               );
    pyClass.def("optimum_tick", &GXMVIEW_wrap_optimum_tick,
                "optimum_tick((float)arg1, (float)arg2, (float_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return a default optimum tick interval\n\n"

                ":param arg1: minimum of range\n"
                ":type arg1: float\n"
                ":param arg2: maximum\n"
                ":type arg2: float\n"
                ":param arg3: optimum interval\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("optimum_tick");
    pyClass.def("create", &GXMVIEW_wrap_create,
                "create((GXMAP)arg1, (str)arg2, (int)arg3) -> GXMVIEW:\n"

                "\n.. parsed-literal::\n\n"
                "   Create MVIEW.\n\n"

                ":param arg1: MAP on which to place the view\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: View name (maximum MVIEW_NAME_LENGTH)\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`MVIEW_OPEN`\\ \n"
                ":type arg3: int\n"
                ":returns: MVIEW, aborts if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXMVIEW`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					View scaling is set to mm on the map and the view\n"
                "   					origin is set to the map origin.\n"
                "   				\n\n"
               ).staticmethod("create");
    pyClass.def("create_crooked_section", &GXMVIEW_wrap_create_crooked_section,
                "create_crooked_section((GXMAP)arg1, (GXIPJ)arg2, (str)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (float)arg11, (GXVV)arg12, (GXVV)arg13, (GXVV)arg14) -> GXMVIEW:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a new crooked section view.\n\n"

                ":param arg1: MAP Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: Geographic projection of input X, Y locations below (without orientation)\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg3: View Name\n"
                ":type arg3: str\n"
                ":param arg4: Base view bottom left corner X (mm)\n"
                ":type arg4: float\n"
                ":param arg5: Base view bottom left corner Y (mm)\n"
                ":type arg5: float\n"
                ":param arg6: Base view size in X (mm)\n"
                ":type arg6: float\n"
                ":param arg7: Base view size in Y (mm)\n"
                ":type arg7: float\n"
                ":param arg8: Map horizontal scale (X-axis)\n"
                ":type arg8: float\n"
                ":param arg9: Vertical exaggeration (1.0 is normal, must be >0.0)\n"
                ":type arg9: float\n"
                ":param arg10: Starting distance at the left side of the view.\n"
                ":type arg10: float\n"
                ":param arg11: Elevation at TOP of the view\n"
                ":type arg11: float\n"
                ":param arg12: Cumulative distances along the secton\n"
                ":type arg12: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg13: True X locations along the section\n"
                ":type arg13: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg14: True Y locations along the section\n"
                ":type arg14: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: MVIEW, aborts if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXMVIEW`\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A crooked section is a section running vertically beneath\n"
                "   					a path of (X, Y) locations, like a river. This view supports\n"
                "   					linking to other plan, section, or 3D views.\n"
                "   					The data view coordinates are set up so that vertical coordinate\n"
                "   					corresponds to elevation, and the X coordinate is the distance along\n"
                "   					the crooked feature, beginning at zero on the left, but the\n"
                "   					status bar will show the true (X, Y, Z) location.\n"
                "   \n"
                "   					If the scale is set to rDUMMY, then it will be calculated so that\n"
                "   					the points will all fit horizontally.\n"
                "   				\n\n"
               ).staticmethod("create_crooked_section");
    pyClass.def("create_crooked_section_data_profile", &GXMVIEW_wrap_create_crooked_section_data_profile,
                "create_crooked_section_data_profile((GXMAP)arg1, (GXIPJ)arg2, (str)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (float)arg11, (int)arg12, (GXVV)arg13, (GXVV)arg14, (GXVV)arg15) -> GXMVIEW:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a new crooked section data profile view.\n\n"

                ":param arg1: MAP Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: Geographic projection of input X, Y locations below (without orientation)\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg3: View Name\n"
                ":type arg3: str\n"
                ":param arg4: Base view bottom left corner X (mm)\n"
                ":type arg4: float\n"
                ":param arg5: Base view bottom left corner Y (mm)\n"
                ":type arg5: float\n"
                ":param arg6: Base view size in X (mm)\n"
                ":type arg6: float\n"
                ":param arg7: Base view size in Y (mm)\n"
                ":type arg7: float\n"
                ":param arg8: Map horizontal scale (X-axis)\n"
                ":type arg8: float\n"
                ":param arg9: Starting distance at the left side of the view.\n"
                ":type arg9: float\n"
                ":param arg10: Data value at bottom of the view\n"
                ":type arg10: float\n"
                ":param arg11: Data value at top of the view\n"
                ":type arg11: float\n"
                ":param arg12: Make logarithmic Y-axis (0:No, 1:Yes)?\n"
                ":type arg12: int\n"
                ":param arg13: Cumulative distances along the secton\n"
                ":type arg13: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg14: True X locations along the section\n"
                ":type arg14: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg15: True Y locations along the section\n"
                ":type arg15: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: MVIEW, aborts if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXMVIEW`\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is the same as \\ :func:`geosoft.gxapi.GXMVIEW.create_crooked_section`\\ , except that the\n"
                "   					vertical axis plots a data value, not elevation, and allows for\n"
                "   					logarithmic scaling.\n"
                "   \n"
                "   					See Also: \\ :func:`geosoft.gxapi.GXMVIEW.create_crooked_section`\\ .\n"
                "   				\n\n"
               ).staticmethod("create_crooked_section_data_profile");
    pyClass.def("extent", &GXMVIEW_wrap_extent,
                "extent((int)arg1, (int)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the view extents\n\n"

                ":param arg1: \\ :ref:`MVIEW_EXTENT`\\ \n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`MVIEW_EXTENT_UNIT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: X minimum\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Y minimum\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: X maximum\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Y maximum\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The CLIP region is the current view window or the limits\n"
                "   					of the current clip polygon.\n"
                "   \n"
                "   					If MVIEW_EXTENT_ALL is requested and the view has no groups, the\n"
                "   					clip extents are returned.\n"
                "   \n"
                "   					If clip extents are requested and there are no clip extents, an\n"
                "   					area 0.0,0.0 1.0,1.0 is returned.\n"
                "   \n"
                "   					The MVIEW_EXTENT_VISIBLE flag will return the union of the MVIEW_EXTENT_CLIP area and the\n"
                "   					extents of all non-masked visible groups in the view.\n"
                "   				\n\n"
               );
    pyClass.def("get_map", &GXMVIEW_wrap_get_map,
                "get_map() -> GXMAP:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the MAP of the view.\n\n"

                ":returns: The MAP of the View.\n"
                ":rtype: :class:`geosoft.gxapi.GXMAP`\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("get_reg", &GXMVIEW_wrap_get_reg,
                "get_reg() -> GXREG:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the REG of the view.\n\n"

                ":returns: The REG of the View.\n"
                ":rtype: :class:`geosoft.gxapi.GXREG`\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"
               );
    pyClass.def("get_name", &GXMVIEW_wrap_get_name,
                "get_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the name of a view.\n\n"

                ":param arg1: view name returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("plot_to_view", &GXMVIEW_wrap_plot_to_view,
                "plot_to_view((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a plot coordinate in mm to a VIEW coordinate.\n\n"

                ":param arg1: X in plot mm, returned in View coordinates\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y in plot mm, returned in View coordinates\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_thin_res", &GXMVIEW_wrap_set_thin_res,
                "set_thin_res((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set polyline/polygon thinning resolution\n\n"

                ":param arg1: Thinning resolution in mm, -1.0 to turn off.\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The thinning resolution controls the removal of\n"
                "   					redundant points from polylines and polygons.  Points\n"
                "   					that deviate from a straight line by less than the\n"
                "   					thinning resolution are removed.  This can significantly\n"
                "   					reduce the size of a MAP file.\n"
                "   					We recommend that you set the thinning resolution to\n"
                "   					0.02 mm.\n"
                "   \n"
                "   					By default, the thinning resolution is set to 0.05mm.\n"
                "   \n"
                "   					Set resolution to 0.0 to remove colinear points only.\n"
                "   \n"
                "   					To turn off thinning after turning it on, call\n"
                "   					SetThinRes_MVIEW with a resolution of -1.\n"
                "   				\n\n"
               );
    pyClass.def("view_to_plot", &GXMVIEW_wrap_view_to_plot,
                "view_to_plot((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a VIEW coordinate to a plot coordinate in mm.\n\n"

                ":param arg1: X in View, returned in mm from plot origin\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y in View, returned in mm from plot origin\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("best_fit_window", &GXMVIEW_wrap_best_fit_window,
                "best_fit_window((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (int)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Fit an area in ground coordinates centered to an area in mm on map or vise versa\n"
                "   					keeping X and Y scales the same.\n"
                "   				\n\n"

                ":param arg1: X minimum (mm) of the area in map relative to map origin\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y minimum  ..\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: X maximum  ..\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Y maximum  ..\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: min X in ground coordinate to fit to the area defined above\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: min Y in ground coordinate ..\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: max X in ground coordinate ..\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: max Y in ground coordinate ..\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: \\ :ref:`MVIEW_FIT`\\ \n"
                ":type arg9: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					X and Y scales will be redefined and units will remain unchanged.\n"
                "   					The final X and Y ranges (if changed) are returned.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.fit_window`\\ \n\n"
               );
    pyClass.def("fit_map_window_3d", &GXMVIEW_wrap_fit_map_window_3d,
                "fit_map_window_3d((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the 2D view window for a 3D view.\n\n"

                ":param arg1: X minimum (mm) of the area in map relative to map origin\n"
                ":type arg1: float\n"
                ":param arg2: Y minimum  ..\n"
                ":type arg2: float\n"
                ":param arg3: X maximum  ..\n"
                ":type arg3: float\n"
                ":param arg4: Y maximum  ..\n"
                ":type arg4: float\n"
                ":param arg5: min X in ground coordinate to fit to the area defined above\n"
                ":type arg5: float\n"
                ":param arg6: min Y in ground coordinate ..\n"
                ":type arg6: float\n"
                ":param arg7: max X in ground coordinate ..\n"
                ":type arg7: float\n"
                ":param arg8: max Y in ground coordinate ..\n"
                ":type arg8: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					3D views are placed in 2D maps within a 2D mapping window\n"
                "   					that is analgous to a 2D View.  This allows all 2D functions\n"
                "   					(such as changing a view location and size) to treat a 3D\n"
                "   					view just like a 2D view.\n"
                "   \n"
                "   					The \\ :func:`geosoft.gxapi.GXMVIEW.fit_map_window_3d`\\  function allows you to\n"
                "   					locate and set the \"apparent\" 2D mapping of a 3D view on\n"
                "   					the map. An intial map window is established\n"
                "   					as specified on the map, and the view scaling is\n"
                "   					established to fit the specified area within that\n"
                "   					map area.\n"
                "   				\n\n"
               );
    pyClass.def("fit_window", &GXMVIEW_wrap_fit_window,
                "fit_window((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fit an area in ground coordinates to an area in mm on map.\n\n"

                ":param arg1: X minimum (mm) of the area in map relative to map origin\n"
                ":type arg1: float\n"
                ":param arg2: Y minimum  ..\n"
                ":type arg2: float\n"
                ":param arg3: X maximum  ..\n"
                ":type arg3: float\n"
                ":param arg4: Y maximum  ..\n"
                ":type arg4: float\n"
                ":param arg5: min X in ground coordinate to fit to the area defined above\n"
                ":type arg5: float\n"
                ":param arg6: min Y in ground coordinate ..\n"
                ":type arg6: float\n"
                ":param arg7: max X in ground coordinate ..\n"
                ":type arg7: float\n"
                ":param arg8: max Y in ground coordinate ..\n"
                ":type arg8: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					X and Y scales will be redefined and the units will be set to <unknown>.\n"
                "   					Coordinate ranges must be greater than 0.0.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.set_window`\\ \n\n"
               );
    pyClass.def("get_class_name", &GXMVIEW_wrap_get_class_name,
                "get_class_name((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a class name.\n\n"

                ":param arg1: class\n"
                ":type arg1: str\n"
                ":param arg2: name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					MVIEW class names are intended to be used to record the\n"
                "   					names of certain classes in the view, such as \"Plane\"\n"
                "   					for the default drawing plane.\n"
                "   				\n\n"
               );
    pyClass.def("map_origin", &GXMVIEW_wrap_map_origin,
                "map_origin((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the map origin from a view\n\n"

                ":param arg1: Returned map origin - X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Returned map origin - Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("re_scale", &GXMVIEW_wrap_re_scale,
                "re_scale((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Change the scale of a view.\n\n"

                ":param arg1: scale factor (> 0.0)\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The view size is multiplied by the scale factor.\n"
                "   					The view location will move relative to the map origin\n"
                "   					by the scale factor.\n"
                "   				\n\n"
               );
    pyClass.def("get_map_scale", &GXMVIEW_wrap_get_map_scale,
                "get_map_scale() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the current map scale of the view\n\n"

                ":returns: The current map scale to 6 significant digits\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("scale_mm", &GXMVIEW_wrap_scale_mm,
                "scale_mm() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the horizontal scale in view X units/mm\n\n"

                ":returns: Returns horizontal scale in view X units/mm\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The scale factor is intended to be used by methods\n"
                "   					that would like to specify sizes in mm.  Examples\n"
                "   					would be text sizes, line thicknesses and line\n"
                "   					pitch.\n"
                "   				\n\n"
               );
    pyClass.def("scale_pj_mm", &GXMVIEW_wrap_scale_pj_mm,
                "scale_pj_mm() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get horizontal scale in projected user units/mm\n\n"

                ":returns: Returns horizontal scale in projected user units/mm\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The scale factor is intended to be used by methods\n"
                "   					that would like to specify sizes in mm.  Examples\n"
                "   					would be text sizes, line thicknesses and line\n"
                "   					pitch.\n"
                "   					Same as rScaleMM if working projection not defined\n"
                "   				\n\n"
               );
    pyClass.def("scale_ymm", &GXMVIEW_wrap_scale_ymm,
                "scale_ymm() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the vertical scale in Y units/mm\n\n"

                ":returns: Returns vertical scale in view Y units/mm\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The scale factor is intended to be used by methods\n"
                "   					that would like to specify sizes in mm.  Examples\n"
                "   					would be text sizes, line thicknesses and line\n"
                "   					pitch.\n"
                "   				\n\n"
               );
    pyClass.def("scale_all_group", &GXMVIEW_wrap_scale_all_group,
                "scale_all_group((float)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Scale all groups (except for GRID) in a view\n\n"

                ":param arg1: X scale\n"
                ":type arg1: float\n"
                ":param arg2: Y scale\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					X (and Y) scale is the ratio of the new dimension over\n"
                "   					the old dimension of a reference object. For example, if a horizontal\n"
                "   					straight line of 10m long becomes 20m, X scale should be 2.\n"
                "   \n"
                "   					The view is then scaled back so that the view occupies the same\n"
                "   					area size as before.  The view's clip area is updated as well.\n"
                "   				\n\n"
               );
    pyClass.def("scale_window", &GXMVIEW_wrap_scale_window,
                "scale_window((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Assign view coordinates to define a window.\n\n"

                ":param arg1: X minimum in view coordinates\n"
                ":type arg1: float\n"
                ":param arg2: Y minimum\n"
                ":type arg2: float\n"
                ":param arg3: X maximum\n"
                ":type arg3: float\n"
                ":param arg4: Y maximum\n"
                ":type arg4: float\n"
                ":param arg5: X minimum in plot coordinates\n"
                ":type arg5: float\n"
                ":param arg6: Y minimum\n"
                ":type arg6: float\n"
                ":param arg7: horizontal scale (view unit/plot unit in mm)\n"
                ":type arg7: float\n"
                ":param arg8: vertical scale\n"
                ":type arg8: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The provided coordinates are converted to map mm\n"
                "   					using the current view translation and scaling.\n"
                "   					SetWindow is effectively called.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.set_window`\\ , \\ :func:`geosoft.gxapi.GXMVIEW.scale_window`\\ , \\ :func:`geosoft.gxapi.GXMVIEW.tran_scale`\\ \n\n"
               );
    pyClass.def("set_class_name", &GXMVIEW_wrap_set_class_name,
                "set_class_name((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a class name.\n\n"

                ":param arg1: class\n"
                ":type arg1: str\n"
                ":param arg2: name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					MVIEW class names are intended to be used to record the\n"
                "   					names of certain classes in the view, such as \"Plane\"\n"
                "   					for the default drawing plane.\n"
                "   				\n\n"
               );
    pyClass.def("set_window", &GXMVIEW_wrap_set_window,
                "set_window((float)arg1, (float)arg2, (float)arg3, (float)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the view window\n\n"

                ":param arg1: X minimum\n"
                ":type arg1: float\n"
                ":param arg2: Y minimum\n"
                ":type arg2: float\n"
                ":param arg3: X maximum\n"
                ":type arg3: float\n"
                ":param arg4: Y maximum\n"
                ":type arg4: float\n"
                ":param arg5: \\ :ref:`MVIEW_UNIT`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The current clip region will be set to the clip\n"
                "   					window.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.fit_window`\\ , \\ :func:`geosoft.gxapi.GXMVIEW.scale_window`\\ , \\ :func:`geosoft.gxapi.GXMVIEW.extent`\\ .\n\n"
               );
    pyClass.def("tran_scale", &GXMVIEW_wrap_tran_scale,
                "tran_scale((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the view translation and scaling\n\n"

                ":param arg1: X origin (user X to be placed at map 0)\n"
                ":type arg1: float\n"
                ":param arg2: Y origin (user Y to be placed at map 0)\n"
                ":type arg2: float\n"
                ":param arg3: X mm/user unit\n"
                ":type arg3: float\n"
                ":param arg4: Y mm/user unit\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Warning. For reasons unknown (and maybe a bug), this\n"
                "   					function resets the view IPJ units. It is a good idea\n"
                "   					to call the SetUnits_IPJ function after calling this\n"
                "   					function in order to restore them. This will be addressed\n"
                "   					in v6.4.\n"
                "   				\n\n"
               );
    pyClass.def("user_to_view", &GXMVIEW_wrap_user_to_view,
                "user_to_view((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a USERplot in mm to a VIEW coordinate\n\n"

                ":param arg1: X in USER, returned in View coordinates\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y in USER, returned in View coordinates\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXMVIEW.set_user_ipj`\\ \n"
                "   					\\ :func:`geosoft.gxapi.GXMVIEW.get_user_ipj`\\ \n"
                "   				\n\n"
               );
    pyClass.def("view_to_user", &GXMVIEW_wrap_view_to_user,
                "view_to_user((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a VIEW coordinate to a USER coordinate.\n\n"

                ":param arg1: X in View, returned in user coordinates\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y in View, returned in user coordinates\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXMVIEW.set_user_ipj`\\ \n"
                "   					\\ :func:`geosoft.gxapi.GXMVIEW.get_user_ipj`\\ \n"
                "   				\n\n"
               );

    scope().attr("MAKER_GX") = (int32_t)0;
    scope().attr("CLIP_ON") = (int32_t)1;
    scope().attr("CLIP_OFF") = (int32_t)0;
    scope().attr("C_BLACK") = (int32_t)33554432;
    scope().attr("C_RED") = (int32_t)33554687;
    scope().attr("C_GREEN") = (int32_t)33619712;
    scope().attr("C_BLUE") = (int32_t)50266112;
    scope().attr("C_CYAN") = (int32_t)50331903;
    scope().attr("C_MAGENTA") = (int32_t)50396928;
    scope().attr("C_YELLOW") = (int32_t)67043328;
    scope().attr("C_GREY") = (int32_t)41975936;
    scope().attr("C_LT_RED") = (int32_t)54542336;
    scope().attr("C_LT_GREEN") = (int32_t)54526016;
    scope().attr("C_LT_BLUE") = (int32_t)50348096;
    scope().attr("C_LT_CYAN") = (int32_t)50331712;
    scope().attr("C_LT_MAGENTA") = (int32_t)50348032;
    scope().attr("C_LT_YELLOW") = (int32_t)54525952;
    scope().attr("C_LT_GREY") = (int32_t)54542400;
    scope().attr("C_GREY10") = (int32_t)51910680;
    scope().attr("C_GREY25") = (int32_t)54542400;
    scope().attr("C_GREY50") = (int32_t)41975936;
    scope().attr("C_WHITE") = (int32_t)50331648;
    scope().attr("C_TRANSPARENT") = (int32_t)0;
    scope().attr("MVIEW_CYLINDER3D_OPEN") = (int32_t)0;
    scope().attr("MVIEW_CYLINDER3D_CLOSESTART") = (int32_t)1;
    scope().attr("MVIEW_CYLINDER3D_CLOSEEND") = (int32_t)2;
    scope().attr("MVIEW_CYLINDER3D_CLOSEALL") = (int32_t)3;
    scope().attr("MVIEW_DRAW_POLYLINE") = (int32_t)0;
    scope().attr("MVIEW_DRAW_POLYGON") = (int32_t)1;
    scope().attr("MVIEW_DRAWOBJ3D_ENTITY_POINTS") = (int32_t)0;
    scope().attr("MVIEW_DRAWOBJ3D_ENTITY_LINES") = (int32_t)1;
    scope().attr("MVIEW_DRAWOBJ3D_ENTITY_LINE_STRIPS") = (int32_t)2;
    scope().attr("MVIEW_DRAWOBJ3D_ENTITY_LINE_LOOPS") = (int32_t)3;
    scope().attr("MVIEW_DRAWOBJ3D_ENTITY_TRIANGLES") = (int32_t)4;
    scope().attr("MVIEW_DRAWOBJ3D_ENTITY_TRIANGLE_STRIPS") = (int32_t)5;
    scope().attr("MVIEW_DRAWOBJ3D_ENTITY_TRIANGLE_FANS") = (int32_t)6;
    scope().attr("MVIEW_DRAWOBJ3D_ENTITY_QUADS") = (int32_t)7;
    scope().attr("MVIEW_DRAWOBJ3D_ENTITY_QUADS_STRIPS") = (int32_t)8;
    scope().attr("MVIEW_DRAWOBJ3D_ENTITY_POLYGONS") = (int32_t)9;
    scope().attr("MVIEW_DRAWOBJ3D_MODE_FLAT") = (int32_t)0;
    scope().attr("MVIEW_DRAWOBJ3D_MODE_SMOOTH") = (int32_t)1;
    scope().attr("MVIEW_EXTENT_ALL") = (int32_t)0;
    scope().attr("MVIEW_EXTENT_CLIP") = (int32_t)1;
    scope().attr("MVIEW_EXTENT_MAP") = (int32_t)2;
    scope().attr("MVIEW_EXTENT_VISIBLE") = (int32_t)3;
    scope().attr("MVIEW_FIT_MAP") = (int32_t)0;
    scope().attr("MVIEW_FIT_VIEW") = (int32_t)1;
    scope().attr("MVIEW_FONT_WEIGHT_NORMAL") = (int32_t)0;
    scope().attr("MVIEW_FONT_WEIGHT_ULTRALIGHT") = (int32_t)1;
    scope().attr("MVIEW_FONT_WEIGHT_LIGHT") = (int32_t)2;
    scope().attr("MVIEW_FONT_WEIGHT_MEDIUM") = (int32_t)3;
    scope().attr("MVIEW_FONT_WEIGHT_BOLD") = (int32_t)4;
    scope().attr("MVIEW_FONT_WEIGHT_XBOLD") = (int32_t)5;
    scope().attr("MVIEW_FONT_WEIGHT_XXBOLD") = (int32_t)6;
    scope().attr("MVIEW_GRID_DOT") = (int32_t)0;
    scope().attr("MVIEW_GRID_LINE") = (int32_t)1;
    scope().attr("MVIEW_GRID_CROSS") = (int32_t)2;
    scope().attr("MVIEW_GROUP_NEW") = (int32_t)1;
    scope().attr("MVIEW_GROUP_APPEND") = (int32_t)0;
    scope().attr("MVIEW_GROUP_LIST_ALL") = (int32_t)0;
    scope().attr("MVIEW_GROUP_LIST_MARKED") = (int32_t)1;
    scope().attr("MVIEW_GROUP_LIST_VISIBLE") = (int32_t)2;
    scope().attr("HIDE_ON") = (int32_t)1;
    scope().attr("HIDE_OFF") = (int32_t)0;
    scope().attr("MVIEW_IS_AGG") = (int32_t)0;
    scope().attr("MVIEW_IS_MOVABLE") = (int32_t)3;
    scope().attr("MVIEW_IS_CSYMB") = (int32_t)4;
    scope().attr("MVIEW_IS_LINKED") = (int32_t)5;
    scope().attr("MVIEW_IS_MADE") = (int32_t)6;
    scope().attr("MVIEW_IS_HIDDEN") = (int32_t)7;
    scope().attr("MVIEW_IS_CLIPPED") = (int32_t)8;
    scope().attr("MVIEW_IS_META") = (int32_t)9;
    scope().attr("MVIEW_IS_VOXD") = (int32_t)10;
    scope().attr("MVIEW_LABEL_BOUND_NO") = (int32_t)0;
    scope().attr("MVIEW_LABEL_BOUND_YES") = (int32_t)1;
    scope().attr("MVIEW_LABEL_JUST_TOP") = (int32_t)0;
    scope().attr("MVIEW_LABEL_JUST_BOTTOM") = (int32_t)1;
    scope().attr("MVIEW_LABEL_JUST_LEFT") = (int32_t)2;
    scope().attr("MVIEW_LABEL_JUST_RIGHT") = (int32_t)3;
    scope().attr("MVIEW_LABEL_ORIENT_HORIZONTAL") = (int32_t)0;
    scope().attr("MVIEW_LABEL_ORIENT_TOP_RIGHT") = (int32_t)1;
    scope().attr("MVIEW_LABEL_ORIENT_TOP_LEFT") = (int32_t)2;
    scope().attr("MVIEW_NAME_LENGTH") = (int32_t)1040;
    scope().attr("MVIEW_READ") = (int32_t)0;
    scope().attr("MVIEW_WRITENEW") = (int32_t)1;
    scope().attr("MVIEW_WRITEOLD") = (int32_t)2;
    scope().attr("MVIEW_PJ_OFF") = (int32_t)0;
    scope().attr("MVIEW_PJ_LOCATION") = (int32_t)1;
    scope().attr("MVIEW_PJ_ALL") = (int32_t)2;
    scope().attr("MVIEW_PJ_ON") = (int32_t)3;
    scope().attr("MVIEW_RELOCATE_FIT") = (int32_t)0;
    scope().attr("MVIEW_RELOCATE_ASPECT") = (int32_t)1;
    scope().attr("MVIEW_RELOCATE_ASPECT_CENTER") = (int32_t)2;
    scope().attr("MVIEW_SMOOTH_NEAREST") = (int32_t)0;
    scope().attr("MVIEW_SMOOTH_CUBIC") = (int32_t)1;
    scope().attr("MVIEW_SMOOTH_AKIMA") = (int32_t)2;
    scope().attr("MVIEW_TILE_RECTANGULAR") = (int32_t)0;
    scope().attr("MVIEW_TILE_DIAGONAL") = (int32_t)1;
    scope().attr("MVIEW_TILE_TRIANGULAR") = (int32_t)2;
    scope().attr("MVIEW_TILE_RANDOM") = (int32_t)3;
    scope().attr("MVIEW_UNIT_VIEW") = (int32_t)0;
    scope().attr("MVIEW_UNIT_PLOT") = (int32_t)1;
    scope().attr("MVIEW_UNIT_MM") = (int32_t)2;
    scope().attr("MVIEW_UNIT_VIEW_UNWARPED") = (int32_t)3;
    scope().attr("MVIEW_EXTENT_UNIT_VIEW") = (int32_t)0;
    scope().attr("MVIEW_EXTENT_UNIT_PLOT") = (int32_t)1;
    scope().attr("MVIEW_EXTENT_UNIT_MM") = (int32_t)2;
    scope().attr("MVIEW_EXTENT_UNIT_VIEW_UNWARPED") = (int32_t)3;
    scope().attr("TEXT_REF_BOTTOM_LEFT") = (int32_t)0;
    scope().attr("TEXT_REF_BOTTOM_CENTER") = (int32_t)1;
    scope().attr("TEXT_REF_BOTTOM_RIGHT") = (int32_t)2;
    scope().attr("TEXT_REF_MIDDLE_LEFT") = (int32_t)3;
    scope().attr("TEXT_REF_MIDDLE_CENTER") = (int32_t)4;
    scope().attr("TEXT_REF_MIDDLE_RIGHT") = (int32_t)5;
    scope().attr("TEXT_REF_TOP_LEFT") = (int32_t)6;
    scope().attr("TEXT_REF_TOP_CENTER") = (int32_t)7;
    scope().attr("TEXT_REF_TOP_RIGHT") = (int32_t)8;
    scope().attr("MVIEW_3D_RENDER_BACKFACES") = (int32_t)1;
    scope().attr("MVIEW_3D_DONT_SCALE_GEOMETRY") = (int32_t)2;

}
