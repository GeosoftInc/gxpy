#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXVOX_wrap_calc_stats(GXVOXPtr self, GXSTPtr arg1)
{
    self->calc_stats(arg1);
}
inline GXVOXPtr GXVOX_wrap_create(const gx_string_type& arg1)
{
    GXVOXPtr ret = GXVOX::create(arg1);
    return ret;
}
inline GXPGPtr GXVOX_wrap_create_pg(GXVOXPtr self)
{
    GXPGPtr ret = self->create_pg();
    return ret;
}
inline GXPGPtr GXVOX_wrap_create_type_pg(GXVOXPtr self, int32_t arg1)
{
    GXPGPtr ret = self->create_type_pg((GS_TYPES)arg1);
    return ret;
}
inline void GXVOX_wrap_dump(GXVOXPtr self, const gx_string_type& arg1)
{
    self->dump(arg1);
}
inline void GXVOX_wrap_export_db(GXVOXPtr self, GXDBPtr arg1, const gx_string_type& arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    self->export_db(arg1, arg2, (VOX_DIRECTION)arg3, arg4, arg5, arg6, arg7);
}
inline void GXVOX_wrap_export_img(GXVOXPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->export_img(arg1, (VOX_DIR)arg2);
}
inline void GXVOX_wrap_export_to_grids(GXVOXPtr self, const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, double arg6, int32_t arg7)
{
    self->export_to_grids(arg1, (VOX_DIR)arg2, arg3, arg4, arg5, arg6, (VOX_SLICE_MODE)arg7);
}
inline void GXVOX_wrap_export_xml(const gx_string_type& arg1, int_ref& arg2, const gx_string_type& arg3)
{
    GXVOX::export_xml(arg1, arg2, arg3);
}
inline void GXVOX_wrap_export_seg_y(GXVOXPtr self, const gx_string_type& arg1, double arg2)
{
    self->export_seg_y(arg1, arg2);
}
inline void GXVOX_wrap_export_ji_gs_xml(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXVOX::export_ji_gs_xml(arg1, arg2);
}
inline void GXVOX_wrap_export_xyz(GXVOXPtr self, const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    self->export_xyz(arg1, (VOX_DIRECTION)arg2, arg3, arg4, arg5, arg6);
}
inline void GXVOX_wrap_filter(GXVOXPtr self, int32_t arg1, const gx_string_type& arg2, int32_t arg3, int32_t arg4, const gx_string_type& arg5)
{
    self->filter((VOX_FILTER3D)arg1, arg2, arg3, arg4, arg5);
}
inline void GXVOX_wrap_generate_db(const gx_string_type& arg1, GXDBPtr arg2, int32_t arg3)
{
    GXVOX::generate_db(arg1, arg2, arg3);
}
inline void GXVOX_wrap_generate_vector_voxel_from_db(const gx_string_type& arg1, GXDBPtr arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, double arg7, double arg8)
{
    GXVOX::generate_vector_voxel_from_db(arg1, arg2, (VOX_VECTORVOX_IMPORT)arg3, arg4, arg5, arg6, arg7, arg8);
}
inline GXVOXPtr GXVOX_wrap_generate_gocad(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXIPJPtr arg4)
{
    GXVOXPtr ret = GXVOX::generate_gocad(arg1, arg2, arg3, arg4);
    return ret;
}
inline GXVOXPtr GXVOX_wrap_generate_oriented_gocad(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXIPJPtr arg4, int32_t arg5)
{
    GXVOXPtr ret = GXVOX::generate_oriented_gocad(arg1, arg2, arg3, arg4, (VOX_GOCAD_ORIENTATION)arg5);
    return ret;
}
inline GXVOXPtr GXVOX_wrap_generate_pg(const gx_string_type& arg1, GXPGPtr arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, GXIPJPtr arg9, GXMETAPtr arg10)
{
    GXVOXPtr ret = GXVOX::generate_pg(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
    return ret;
}
inline GXVOXPtr GXVOX_wrap_generate_constant_value(const gx_string_type& arg1, double arg2, int32_t arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, int32_t arg10, int32_t arg11, int32_t arg12, GXIPJPtr arg13, GXMETAPtr arg14)
{
    GXVOXPtr ret = GXVOX::generate_constant_value(arg1, arg2, (GS_TYPES)arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14);
    return ret;
}
inline GXVOXPtr GXVOX_wrap_generate_pgvv(const gx_string_type& arg1, GXPGPtr arg2, double arg3, double arg4, double arg5, GXVVPtr arg6, GXVVPtr arg7, GXVVPtr arg8, GXIPJPtr arg9, GXMETAPtr arg10)
{
    GXVOXPtr ret = GXVOX::generate_pgvv(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
    return ret;
}
inline GXVOXPtr GXVOX_wrap_generate_constant_value_vv(const gx_string_type& arg1, double arg2, int32_t arg3, double arg4, double arg5, double arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, GXIPJPtr arg10, GXMETAPtr arg11)
{
    GXVOXPtr ret = GXVOX::generate_constant_value_vv(arg1, arg2, (GS_TYPES)arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
    return ret;
}
inline GXVOXPtr GXVOX_wrap_generate_ubc(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, double arg4, GXIPJPtr arg5)
{
    GXVOXPtr ret = GXVOX::generate_ubc(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline void GXVOX_wrap_generate_xyz(const gx_string_type& arg1, GXRAPtr arg2, int32_t arg3, GXIPJPtr arg4)
{
    GXVOX::generate_xyz(arg1, arg2, (GS_TYPES)arg3, arg4);
}
inline GXVOXPtr GXVOX_wrap_init_generate_by_subset_pg(int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    GXVOXPtr ret = GXVOX::init_generate_by_subset_pg((GS_TYPES)arg1, arg2, arg3, arg4);
    return ret;
}
inline void GXVOX_wrap_add_generate_by_subset_pg(GXVOXPtr self, GXPGPtr arg1, int32_t arg2, int32_t arg3)
{
    self->add_generate_by_subset_pg(arg1, (VOX_DIR)arg2, arg3);
}
inline void GXVOX_wrap_end_generate_by_subset_pg(GXVOXPtr self, const gx_string_type& arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, GXIPJPtr arg8, GXMETAPtr arg9)
{
    self->end_generate_by_subset_pg(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXVOX_wrap_get_area(GXVOXPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    self->get_area(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXVOX_wrap_get_gocad_location(GXVOXPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9, float_ref& arg10, float_ref& arg11, float_ref& arg12)
{
    self->get_gocad_location(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12);
}
inline void GXVOX_wrap_get_grid_section_cell_sizes(GXVOXPtr self, double arg1, float_ref& arg2, float_ref& arg3)
{
    self->get_grid_section_cell_sizes(arg1, arg2, arg3);
}
inline void GXVOX_wrap_get_info(GXVOXPtr self, int_ref& arg1, int_ref& arg2, int_ref& arg3, int_ref& arg4, int_ref& arg5)
{
    self->get_info(arg1, arg2, arg3, arg4, arg5);
}
inline void GXVOX_wrap_get_ipj(GXVOXPtr self, GXIPJPtr arg1)
{
    self->get_ipj(arg1);
}
inline void GXVOX_wrap_get_limits(GXVOXPtr self, int_ref& arg1, int_ref& arg2, int_ref& arg3, int_ref& arg4, int_ref& arg5, int_ref& arg6)
{
    self->get_limits(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXVOX_wrap_get_limits_xyz(GXVOXPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    self->get_limits_xyz(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXVOX_wrap_get_location(GXVOXPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6)
{
    self->get_location(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXVOX_wrap_get_location_points(GXVOXPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->get_location_points(arg1, arg2, arg3);
}
inline void GXVOX_wrap_get_meta(GXVOXPtr self, GXMETAPtr arg1)
{
    self->get_meta(arg1);
}
inline void GXVOX_wrap_get_double_location(GXVOXPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9, float_ref& arg10, float_ref& arg11, float_ref& arg12)
{
    self->get_double_location(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12);
}
inline void GXVOX_wrap_get_simple_location(GXVOXPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    self->get_simple_location(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline GXSTPtr GXVOX_wrap_get_stats(GXVOXPtr self)
{
    GXSTPtr ret = self->get_stats();
    return ret;
}
inline void GXVOX_wrap_get_tpat(GXVOXPtr self, GXTPATPtr arg1)
{
    self->get_tpat(arg1);
}
inline GXVOXPtr GXVOX_wrap_grid_points(const gx_string_type& arg1, const gx_string_type& arg2, double arg3, int32_t arg4, double arg5, double arg6, int32_t arg7, int32_t arg8, int32_t arg9, double arg10, double arg11, double arg12, double arg13, double arg14, int32_t arg15, GXVVPtr arg16, GXVVPtr arg17, GXVVPtr arg18, GXVVPtr arg19, GXIPJPtr arg20)
{
    GXVOXPtr ret = GXVOX::grid_points(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, (GS_TYPES)arg15, arg16, arg17, arg18, arg19, arg20);
    return ret;
}
inline GXVOXPtr GXVOX_wrap_grid_points_z(const gx_string_type& arg1, const gx_string_type& arg2, double arg3, const gx_string_type& arg4, int32_t arg5, double arg6, double arg7, int32_t arg8, int32_t arg9, int32_t arg10, double arg11, double arg12, double arg13, double arg14, double arg15, int32_t arg16, GXVVPtr arg17, GXVVPtr arg18, GXVVPtr arg19, GXVVPtr arg20, GXIPJPtr arg21)
{
    GXVOXPtr ret = GXVOX::grid_points_z(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, (GS_TYPES)arg16, arg17, arg18, arg19, arg20, arg21);
    return ret;
}
inline GXVOXPtr GXVOX_wrap_grid_points_z_ex(const gx_string_type& arg1, const gx_string_type& arg2, double arg3, const gx_string_type& arg4, int32_t arg5, double arg6, double arg7, int32_t arg8, int32_t arg9, int32_t arg10, double arg11, float_ref& arg12, float_ref& arg13, double arg14, float_ref& arg15, double arg16, double arg17, double arg18, double arg19, double arg20, int32_t arg21, GXVVPtr arg22, GXVVPtr arg23, GXVVPtr arg24, GXVVPtr arg25, GXIPJPtr arg26)
{
    GXVOXPtr ret = GXVOX::grid_points_z_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, (GS_TYPES)arg21, arg22, arg23, arg24, arg25, arg26);
    return ret;
}
inline int32_t GXVOX_wrap_can_append_to(GXVOXPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->can_append_to(arg1);
    return ret;
}
inline void GXVOX_wrap_get_cell_size_strings(GXVOXPtr self, str_ref& arg1, str_ref& arg2, str_ref& arg3, double arg4, double arg5, double arg6)
{
    self->get_cell_size_strings(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline int32_t GXVOX_wrap_is_thematic(GXVOXPtr self)
{
    int32_t ret = self->is_thematic();
    return ret;
}
inline int32_t GXVOX_wrap_is_vector_voxel(GXVOXPtr self)
{
    int32_t ret = self->is_vector_voxel();
    return ret;
}
inline int32_t GXVOX_wrap_set_cell_size_strings(GXVOXPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    int32_t ret = self->set_cell_size_strings(arg1, arg2, arg3);
    return ret;
}
inline GXVOXPtr GXVOX_wrap_list_gocad_properties(const gx_string_type& arg1, GXLSTPtr arg2)
{
    GXVOXPtr ret = GXVOX::list_gocad_properties(arg1, arg2);
    return ret;
}
inline GXVOXPtr GXVOX_wrap_log_grid_points_z_ex(const gx_string_type& arg1, const gx_string_type& arg2, double arg3, const gx_string_type& arg4, int32_t arg5, double arg6, double arg7, int32_t arg8, int32_t arg9, int32_t arg10, double arg11, float_ref& arg12, float_ref& arg13, double arg14, float_ref& arg15, double arg16, double arg17, double arg18, double arg19, double arg20, int32_t arg21, double arg22, int32_t arg23, GXVVPtr arg24, GXVVPtr arg25, GXVVPtr arg26, GXVVPtr arg27, GXIPJPtr arg28)
{
    GXVOXPtr ret = GXVOX::log_grid_points_z_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, (VOX_GRID_LOGOPT)arg21, arg22, (GS_TYPES)arg23, arg24, arg25, arg26, arg27, arg28);
    return ret;
}
inline GXVOXPtr GXVOX_wrap_krig(const gx_string_type& arg1, double arg2, int32_t arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7, GXIPJPtr arg8, GXREGPtr arg9)
{
    GXVOXPtr ret = GXVOX::krig(arg1, arg2, (GS_TYPES)arg3, arg4, arg5, arg6, arg7, arg8, arg9);
    return ret;
}
inline GXVOXPtr GXVOX_wrap_math(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, GXLSTPtr arg6)
{
    GXVOXPtr ret = GXVOX::math(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline void GXVOX_wrap_merge(GXVOXPtr self, GXVOXPtr arg1, GXREGPtr arg2, const gx_string_type& arg3)
{
    self->merge(arg1, arg2, arg3);
}
inline GXVOXPtr GXVOX_wrap_nearest_neighbour_grid(const gx_string_type& arg1, double arg2, double arg3, int32_t arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7, GXVVPtr arg8, GXIPJPtr arg9)
{
    GXVOXPtr ret = GXVOX::nearest_neighbour_grid(arg1, arg2, arg3, (GS_TYPES)arg4, arg5, arg6, arg7, arg8, arg9);
    return ret;
}
inline double GXVOX_wrap_compute_cell_size(double arg1, double arg2, double arg3, double arg4, double arg5, double arg6)
{
    double ret = GXVOX::compute_cell_size(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline void GXVOX_wrap_re_grid(GXVOXPtr self, GXVOXPtr arg1, GXREGPtr arg2, const gx_string_type& arg3)
{
    self->re_grid(arg1, arg2, arg3);
}
inline GXPGPtr GXVOX_wrap_resample_pg(GXVOXPtr self, GXIPJPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, int32_t arg8, int32_t arg9, int32_t arg10, double arg11, double arg12, int32_t arg13)
{
    GXPGPtr ret = self->resample_pg(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, (VOX_SLICE_MODE)arg13);
    return ret;
}
inline void GXVOX_wrap_rescale_cell_sizes(GXVOXPtr self, double arg1)
{
    self->rescale_cell_sizes(arg1);
}
inline void GXVOX_wrap_sample_cdi(GXVOXPtr self, GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7, int32_t arg8, const gx_string_type& arg9)
{
    self->sample_cdi(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXVOX_wrap_sample_cdi_to_topography(GXVOXPtr self, GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXVVPtr arg5, int32_t arg6, const gx_string_type& arg7, const gx_string_type& arg8)
{
    self->sample_cdi_to_topography(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXVOX_wrap_sample_vv(GXVOXPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, int32_t arg4, GXVVPtr arg5)
{
    self->sample_vv(arg1, arg2, arg3, arg4, arg5);
}
inline void GXVOX_wrap_set_ipj(GXVOXPtr self, GXIPJPtr arg1)
{
    self->set_ipj(arg1);
}
inline void GXVOX_wrap_set_location(GXVOXPtr self, double arg1, double arg2, double arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6)
{
    self->set_location(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXVOX_wrap_set_meta(GXVOXPtr self, GXMETAPtr arg1)
{
    self->set_meta(arg1);
}
inline void GXVOX_wrap_set_origin(GXVOXPtr self, int32_t arg1, double arg2, double arg3, double arg4)
{
    self->set_origin((VOX_ORIGIN)arg1, arg2, arg3, arg4);
}
inline void GXVOX_wrap_set_simple_location(GXVOXPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6)
{
    self->set_simple_location(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXVOX_wrap_set_tpat(GXVOXPtr self, GXTPATPtr arg1)
{
    self->set_tpat(arg1);
}
inline void GXVOX_wrap_slice_ipj(GXVOXPtr self, const gx_string_type& arg1, GXIPJPtr arg2, int32_t arg3, double arg4, double arg5, double arg6, double arg7, int32_t arg8, int32_t arg9)
{
    self->slice_ipj(arg1, arg2, (VOX_SLICE_MODE)arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXVOX_wrap_slice_multi_layer_ipj(GXVOXPtr self, const gx_string_type& arg1, GXIPJPtr arg2, int32_t arg3, double arg4, double arg5, double arg6, double arg7, int32_t arg8, int32_t arg9, int32_t arg10, double arg11, double arg12)
{
    self->slice_multi_layer_ipj(arg1, arg2, (VOX_SLICE_MODE)arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12);
}
inline void GXVOX_wrap_subset_to_double_extents(GXVOXPtr self, const gx_string_type& arg1)
{
    self->subset_to_double_extents(arg1);
}
inline void GXVOX_wrap_sync(const gx_string_type& arg1)
{
    GXVOX::sync(arg1);
}
inline void GXVOX_wrap_window_ply(GXVOXPtr self, GXPLYPtr arg1, int32_t arg2, double arg3, double arg4, const gx_string_type& arg5, int32_t arg6)
{
    self->window_ply(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXVOX_wrap_window_xyz(GXVOXPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, const gx_string_type& arg7, int32_t arg8)
{
    self->window_xyz(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXVOX_wrap_write_xml(GXVOXPtr self, const gx_string_type& arg1)
{
    self->write_xml(arg1);
}
inline void GXVOX_wrap_convert_numeric_to_thematic(GXVOXPtr self, GXVVPtr arg1, const gx_string_type& arg2)
{
    self->convert_numeric_to_thematic(arg1, arg2);
}
inline void GXVOX_wrap_convert_thematic_to_numeric(GXVOXPtr self, GXVVPtr arg1, const gx_string_type& arg2)
{
    self->convert_thematic_to_numeric(arg1, arg2);
}
inline void GXVOX_wrap_convert_velocity_to_density(GXVOXPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, const gx_string_type& arg9)
{
    self->convert_velocity_to_density(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXVOX_wrap_convert_velocity_in_range_to_density(GXVOXPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10, const gx_string_type& arg11)
{
    self->convert_velocity_in_range_to_density(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXVOX_wrap_convert_density_to_velocity(GXVOXPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10, const gx_string_type& arg11)
{
    self->convert_density_to_velocity(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXVOX_wrap_invert_z(GXVOXPtr self, const gx_string_type& arg1)
{
    self->invert_z(arg1);
}
inline void GXVOX_wrap_dw_grid_db(const gx_string_type& arg1, GXDBPtr arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, GXREGPtr arg7)
{
    GXVOX::dw_grid_db(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXVOX_wrap_tin_grid_db(const gx_string_type& arg1, GXDBPtr arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7, GXVVPtr arg8, GXREGPtr arg9)
{
    GXVOX::tin_grid_db(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}

void gxPythonImportGXVOX()
{

    class_<GXVOX, GXVOXPtr> pyClass("GXVOX",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		High Performance 3D Grid. Designed for accessing\n"
                                    "   		3D grids quickly using slices. It designed arround\n"
                                    "   		non-uniform multi-resolution  compressed storage.\n"
                                    "   		o sample a voxel at specific locations, use the VOXE class.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXVOX::null, "null() -> GXVOX\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXVOX`\n\n:returns: A null :class:`geosoft.gxapi.GXVOX`\n:rtype: :class:`geosoft.gxapi.GXVOX`\n").staticmethod("null");
    pyClass.def("is_null", &GXVOX::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXVOX is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXVOX`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXVOX::_internal_handle);
    pyClass.def("calc_stats", &GXVOX_wrap_calc_stats,
                "calc_stats((GXST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate Statistics\n\n"

                ":param arg1: ST Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("create", &GXVOX_wrap_create,
                "create((str)arg1) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a handle to an VOX object\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":returns: VOX handle, terminates if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_pg", &GXVOX_wrap_create_pg,
                "create_pg() -> GXPG:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a 3D PG from a VOX object\n\n"

                ":returns: PG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXPG`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("create_type_pg", &GXVOX_wrap_create_type_pg,
                "create_type_pg((int)arg1) -> GXPG:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a 3D PG from a VOX object with a specific Type\n\n"

                ":param arg1: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg1: int\n"
                ":returns: PG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXPG`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("dump", &GXVOX_wrap_dump,
                "dump((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export all layers of this VOX in all directions.\n\n"

                ":param arg1: Name of grids (each layers adds _Dir_Z to the name)\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("export_db", &GXVOX_wrap_export_db,
                "export_db((GXDB)arg1, (str)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a Voxel to a database\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Channel Name\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`VOX_DIRECTION`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Reverse X ? (0/1)\n"
                ":type arg4: int\n"
                ":param arg5: Reverse Y ? (0/1)\n"
                ":type arg5: int\n"
                ":param arg6: Reverse Z ? (0/1)\n"
                ":type arg6: int\n"
                ":param arg7: Write Dummies? (0/1)\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The database lines contain a slice of the voxel at a time.\n\n"
               );
    pyClass.def("export_img", &GXVOX_wrap_export_img,
                "export_img((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export all layers of this VOX into grid files.\n\n"

                ":param arg1: Name of grids (each layers adds _Number to the name)\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`VOX_DIR`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("export_to_grids", &GXVOX_wrap_export_to_grids,
                "export_to_grids((str)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (float)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export all layers of this VOX into grid files, with optional cell size.\n\n"

                ":param arg1: Name of grids (each layers adds _Number to the name)\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`VOX_DIR`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Starting index\n"
                ":type arg3: int\n"
                ":param arg4: Increment in index\n"
                ":type arg4: int\n"
                ":param arg5: Total number of grids (-1 or iDUMMY for all)\n"
                ":type arg5: int\n"
                ":param arg6: Cell size (can be GS_R8DM)\n"
                ":type arg6: float\n"
                ":param arg7: \\ :ref:`VOX_SLICE_MODE`\\ \n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the cell size is not specified, then:\n"
                "   					1. If the cell sizes are uniform in a given direction, that size is used\n"
                "   					2. If the cell sizes are variable in a given direction, then the smallest size is used\n"
                "   				\n\n"
               );
    pyClass.def("export_xml", &GXVOX_wrap_export_xml,
                "export_xml((str)arg1, (int_ref)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a VOX to a compressed XML file\n\n"

                ":param arg1: Voxel file name\n"
                ":type arg1: str\n"
                ":param arg2: CRC returned - not implemented - always returns 0.\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Output XML file\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("export_xml");
    pyClass.def("export_seg_y", &GXVOX_wrap_export_seg_y,
                "export_seg_y((str)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a voxel to a depth SEG-Y file\n\n"

                ":param arg1: SEG-Y filename to create\n"
                ":type arg1: str\n"
                ":param arg2: Sampling interval (can be GS_R8DM if input voxel has constant Z cell size)\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5\n\n"
               );
    pyClass.def("export_ji_gs_xml", &GXVOX_wrap_export_ji_gs_xml,
                "export_ji_gs_xml((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a VOX to a compressed XML file. Verbose version.\n\n"

                ":param arg1: Voxel file name\n"
                ":type arg1: str\n"
                ":param arg2: Output XML file\n"
                ":type arg2: str\n"
                ":returns: Exports all values and stats by JIG.\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4\n\n"
               ).staticmethod("export_ji_gs_xml");
    pyClass.def("export_xyz", &GXVOX_wrap_export_xyz,
                "export_xyz((str)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a Voxel to an XYZ File\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`VOX_DIRECTION`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Reverse X ? (0/1)\n"
                ":type arg3: int\n"
                ":param arg4: Reverse Y ? (0/1)\n"
                ":type arg4: int\n"
                ":param arg5: Reverse Z ? (0/1)\n"
                ":type arg5: int\n"
                ":param arg6: Write Dummies? (0/1)\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("filter", &GXVOX_wrap_filter,
                "filter((int)arg1, (str)arg2, (int)arg3, (int)arg4, (str)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply a 3D filter to a voxel.\n\n"

                ":param arg1: \\ :ref:`VOX_FILTER3D`\\ \n"
                ":type arg1: int\n"
                ":param arg2: filter file, if filter is VOX_FILTER3D_FILE\n"
                ":type arg2: str\n"
                ":param arg3: number of filter passes\n"
                ":type arg3: int\n"
                ":param arg4: (1: interpolate dummies)\n"
                ":type arg4: int\n"
                ":param arg5: Output voxel file name.\n"
                ":type arg5: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"
               );
    pyClass.def("generate_db", &GXVOX_wrap_generate_db,
                "generate_db((str)arg1, (GXDB)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a VOX from a Database\n\n"

                ":param arg1: Voxel Name\n"
                ":type arg1: str\n"
                ":param arg2: DB To import from\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg3: Symbol to import data from\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("generate_db");
    pyClass.def("generate_vector_voxel_from_db", &GXVOX_wrap_generate_vector_voxel_from_db,
                "generate_vector_voxel_from_db((str)arg1, (GXDB)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (float)arg7, (float)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a vector voxel VOX from a Database\n\n"

                ":param arg1: Voxel Name\n"
                ":type arg1: str\n"
                ":param arg2: DB To import from\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg3: \\ :ref:`VOX_VECTORVOX_IMPORT`\\ Import XYZ, UVW or Amplitude/Inclination/Declination channels\n"
                ":type arg3: int\n"
                ":param arg4: Symbol to import X, U or Amplitude data from\n"
                ":type arg4: int\n"
                ":param arg5: Symbol to import Y, V or Inclination data from\n"
                ":type arg5: int\n"
                ":param arg6: Symbol to import Z, W or Declination data from\n"
                ":type arg6: int\n"
                ":param arg7: Inclination value for VOX_VECTORVOX_UVW (-90° to 90°)\n"
                ":type arg7: float\n"
                ":param arg8: Declination value for VOX_VECTORVOX_UVW (-180° to 180°)\n"
                ":type arg8: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               ).staticmethod("generate_vector_voxel_from_db");
    pyClass.def("generate_gocad", &GXVOX_wrap_generate_gocad,
                "generate_gocad((str)arg1, (str)arg2, (str)arg3, (GXIPJ)arg4) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a VOX from a GOCAD File\n\n"

                ":param arg1: Name of output VOX\n"
                ":type arg1: str\n"
                ":param arg2: Name of GOCAD Voxel file\n"
                ":type arg2: str\n"
                ":param arg3: Propert name to import\n"
                ":type arg3: str\n"
                ":param arg4: IPJ\n"
                ":type arg4: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("generate_gocad");
    pyClass.def("generate_oriented_gocad", &GXVOX_wrap_generate_oriented_gocad,
                "generate_oriented_gocad((str)arg1, (str)arg2, (str)arg3, (GXIPJ)arg4, (int)arg5) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a VOX from a GOCAD File\n\n"

                ":param arg1: Name of output VOX\n"
                ":type arg1: str\n"
                ":param arg2: Name of GOCAD Voxel file\n"
                ":type arg2: str\n"
                ":param arg3: Propert name to import\n"
                ":type arg3: str\n"
                ":param arg4: IPJ\n"
                ":type arg4: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg5: \\ :ref:`VOX_GOCAD_ORIENTATION`\\ \n"
                ":type arg5: int\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Allows the Orientation flag to be specified.\n\n"
               ).staticmethod("generate_oriented_gocad");
    pyClass.def("generate_pg", &GXVOX_wrap_generate_pg,
                "generate_pg((str)arg1, (GXPG)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (GXIPJ)arg9, (GXMETA)arg10) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a VOX from a 3D Pager\n\n"

                ":param arg1: Name of output VOX\n"
                ":type arg1: str\n"
                ":param arg2: Pager with the Voxel Data\n"
                ":type arg2: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg3: Origin X\n"
                ":type arg3: float\n"
                ":param arg4: Origin Y\n"
                ":type arg4: float\n"
                ":param arg5: Origin Z\n"
                ":type arg5: float\n"
                ":param arg6: Cell Size X\n"
                ":type arg6: float\n"
                ":param arg7: Cell Size Y\n"
                ":type arg7: float\n"
                ":param arg8: Cell Size Z\n"
                ":type arg8: float\n"
                ":param arg9: Projection\n"
                ":type arg9: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg10: META data\n"
                ":type arg10: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("generate_pg");
    pyClass.def("generate_constant_value", &GXVOX_wrap_generate_constant_value,
                "generate_constant_value((str)arg1, (float)arg2, (int)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (int)arg10, (int)arg11, (int)arg12, (GXIPJ)arg13, (GXMETA)arg14) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a VOX with a constant value\n\n"

                ":param arg1: Name of output VOX\n"
                ":type arg1: str\n"
                ":param arg2: Value to use\n"
                ":type arg2: float\n"
                ":param arg3: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Origin X\n"
                ":type arg4: float\n"
                ":param arg5: Origin Y\n"
                ":type arg5: float\n"
                ":param arg6: Origin Z\n"
                ":type arg6: float\n"
                ":param arg7: Cell Size X\n"
                ":type arg7: float\n"
                ":param arg8: Cell Size Y\n"
                ":type arg8: float\n"
                ":param arg9: Cell Size Z\n"
                ":type arg9: float\n"
                ":param arg10: Cell Count X\n"
                ":type arg10: int\n"
                ":param arg11: Cell Count Y\n"
                ":type arg11: int\n"
                ":param arg12: Cell Count Z\n"
                ":type arg12: int\n"
                ":param arg13: Projection\n"
                ":type arg13: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg14: META data\n"
                ":type arg14: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("generate_constant_value");
    pyClass.def("generate_pgvv", &GXVOX_wrap_generate_pgvv,
                "generate_pgvv((str)arg1, (GXPG)arg2, (float)arg3, (float)arg4, (float)arg5, (GXVV)arg6, (GXVV)arg7, (GXVV)arg8, (GXIPJ)arg9, (GXMETA)arg10) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a VOX from a 3D Pager, cells sizes passed in VVs.\n\n"

                ":param arg1: Name of output VOX\n"
                ":type arg1: str\n"
                ":param arg2: Pager with the Voxel Data\n"
                ":type arg2: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg3: Origin X\n"
                ":type arg3: float\n"
                ":param arg4: Origin Y\n"
                ":type arg4: float\n"
                ":param arg5: Origin Z\n"
                ":type arg5: float\n"
                ":param arg6: Cell Sizes X\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Cell Sizes Y\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Cell Sizes Z\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Projection\n"
                ":type arg9: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg10: META data\n"
                ":type arg10: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The input cell size VVs' lengths must match the input PG dimensions.\n\n"
               ).staticmethod("generate_pgvv");
    pyClass.def("generate_constant_value_vv", &GXVOX_wrap_generate_constant_value_vv,
                "generate_constant_value_vv((str)arg1, (float)arg2, (int)arg3, (float)arg4, (float)arg5, (float)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (GXIPJ)arg10, (GXMETA)arg11) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a VOX with a constant value, cells sizes passed in VVs.\n\n"

                ":param arg1: Name of output VOX\n"
                ":type arg1: str\n"
                ":param arg2: The Value to use\n"
                ":type arg2: float\n"
                ":param arg3: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Origin X\n"
                ":type arg4: float\n"
                ":param arg5: Origin Y\n"
                ":type arg5: float\n"
                ":param arg6: Origin Z\n"
                ":type arg6: float\n"
                ":param arg7: Cell Sizes X\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Cell Sizes Y\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Cell Sizes Z\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Projection\n"
                ":type arg10: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg11: META data\n"
                ":type arg11: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("generate_constant_value_vv");
    pyClass.def("generate_ubc", &GXVOX_wrap_generate_ubc,
                "generate_ubc((str)arg1, (str)arg2, (str)arg3, (float)arg4, (GXIPJ)arg5) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a VOX from a UBC File\n\n"

                ":param arg1: Name of output VOX\n"
                ":type arg1: str\n"
                ":param arg2: Name of UBC Mesh File\n"
                ":type arg2: str\n"
                ":param arg3: Name of UBC Mod File\n"
                ":type arg3: str\n"
                ":param arg4: Dummy Value\n"
                ":type arg4: float\n"
                ":param arg5: Projection\n"
                ":type arg5: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("generate_ubc");
    pyClass.def("generate_xyz", &GXVOX_wrap_generate_xyz,
                "generate_xyz((str)arg1, (GXRA)arg2, (int)arg3, (GXIPJ)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a VOX from an XYZ File\n\n"

                ":param arg1: Voxel Name\n"
                ":type arg1: str\n"
                ":param arg2: RA To import from\n"
                ":type arg2: :class:`geosoft.gxapi.GXRA`\n"
                ":param arg3: Data Type \\ :ref:`GS_TYPES`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Projection\n"
                ":type arg4: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("generate_xyz");
    pyClass.def("init_generate_by_subset_pg", &GXVOX_wrap_init_generate_by_subset_pg,
                "init_generate_by_subset_pg((int)arg1, (int)arg2, (int)arg3, (int)arg4) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Initialize the generate of a VOX from a series of 3D subset pagers\n\n"

                ":param arg1: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Points in X\n"
                ":type arg2: int\n"
                ":param arg3: Points in Y\n"
                ":type arg3: int\n"
                ":param arg4: Points in Z\n"
                ":type arg4: int\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Call \\ :func:`geosoft.gxapi.GXVOX.init_generate_by_subset_pg`\\  first, then add a series of subset PGs using \\ :func:`geosoft.gxapi.GXVOX.add_generate_by_subset_pg`\\ , and finally\n"
                "   					serialize using \\ :func:`geosoft.gxapi.GXVOX.end_generate_by_subset_pg`\\ \n"
                "   				\n\n"
               ).staticmethod("init_generate_by_subset_pg");
    pyClass.def("add_generate_by_subset_pg", &GXVOX_wrap_add_generate_by_subset_pg,
                "add_generate_by_subset_pg((GXPG)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Add a subset 3D  pagers. These should be \"slabs\", 16 wide in the input direction, and the size of the\n"
                "   					full voxel in the other two directions.\n"
                "   				\n\n"

                ":param arg1: Subset pager with the Voxel Data\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Subset orientation - the \"16\" (thin) dimension is in the other axis.\\ :ref:`VOX_DIR`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Offset of the subset PG corner, along the \"thin\" dimension.\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					See \\ :func:`geosoft.gxapi.GXVOX.init_generate_by_subset_pg`\\  and \\ :func:`geosoft.gxapi.GXVOX.end_generate_by_subset_pg`\\ .\n"
                "   				\n\n"
               );
    pyClass.def("end_generate_by_subset_pg", &GXVOX_wrap_end_generate_by_subset_pg,
                "end_generate_by_subset_pg((str)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (GXIPJ)arg8, (GXMETA)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Output the voxel, after adding all the subset PGs.\n"
                "   				\n\n"

                ":param arg1: Name of output VOX\n"
                ":type arg1: str\n"
                ":param arg2: Origin X\n"
                ":type arg2: float\n"
                ":param arg3: Origin Y\n"
                ":type arg3: float\n"
                ":param arg4: Origin Z\n"
                ":type arg4: float\n"
                ":param arg5: Cell Size X\n"
                ":type arg5: float\n"
                ":param arg6: Cell Size Y\n"
                ":type arg6: float\n"
                ":param arg7: Cell Size Z\n"
                ":type arg7: float\n"
                ":param arg8: Projection\n"
                ":type arg8: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg9: META data\n"
                ":type arg9: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					You must begin by calling \\ :func:`geosoft.gxapi.GXVOX.init_generate_by_subset_pg`\\  and add data using \\ :func:`geosoft.gxapi.GXVOX.add_generate_by_subset_pg`\\ .\n"
                "   				\n\n"
               );
    pyClass.def("get_area", &GXVOX_wrap_get_area,
                "get_area((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the area of the voxel.\n\n"

                ":param arg1: Min X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Min Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Min Z\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Max X\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Max Y\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Max Z\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("get_gocad_location", &GXVOX_wrap_get_gocad_location,
                "get_gocad_location((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9, (float_ref)arg10, (float_ref)arg11, (float_ref)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the location of a voxel with origin and scaled xyz vectors for use with GOCAD.\n\n"

                ":param arg1: Origin X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Origin Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Origin Z\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: VectX X\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: VectX Y\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: VectX Z\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: VectY X\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: VectY Y\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: VectY Z\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: VectZ X\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: VectZ Y\n"
                ":type arg11: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg12: VectZ Z\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is used for GOCAD voxel calculations, and begins with the\n"
                "   					origin at (0,0,0), not the actual location of the corner point.\n"
                "   				\n\n"
               );
    pyClass.def("get_grid_section_cell_sizes", &GXVOX_wrap_get_grid_section_cell_sizes,
                "get_grid_section_cell_sizes((float)arg1, (float_ref)arg2, (float_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get default cell sizes in X and Y for a section grid.\n\n"

                ":param arg1: Input section azimuth (degrees CCW from North)\n"
                ":type arg1: float\n"
                ":param arg2: Returned X cell size (horizontal) in m\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Returned Y cell size (vertical) in m\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function determines default cell sizes for a vertical grid\n"
                "   					slicing a voxel. It tries to match the \"X\" and \"Y\" sizes (in the grid\n"
                "   					coordinates) with the projection of the voxel's cells onto the grid\n"
                "   					plane. It uses a few simple rules:\n"
                "   \n"
                "   					If the voxel is rotated about a horizontal axis (i.e. if its own \"Z\" axis\n"
                "   					is not vertical, then both cell sizes are set to the smallest voxel dimension\n"
                "   					(a single volume pixel) in X, Y and Z.\n"
                "   \n"
                "   					If the voxel is \"horizontal\", then the angle between the\n"
                "   					section azimuth and the voxel's own X and Y axes is used to\n"
                "   					calculate a value which varies between the minimum X size and the\n"
                "   					minimum Y size, and this is used for the grid's \"X\" cell size.\n"
                "   					(in other words, if the section is parallel to the voxel \"X\" axis,\n"
                "   					then the returned \"X\" cells size is equal to the voxel's minimum \"Y\" cell size.\n"
                "   					The grid's \"Y\" cell size is set to the voxel's minimum \"Z\" cell size.\n"
                "   				\n\n"
               );
    pyClass.def("get_info", &GXVOX_wrap_get_info,
                "get_info((int_ref)arg1, (int_ref)arg2, (int_ref)arg3, (int_ref)arg4, (int_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get information about a voxel.\n\n"

                ":param arg1: Data Type\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Array Size\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Elements in X\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Elements in Y\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: Elements in Z\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("get_ipj", &GXVOX_wrap_get_ipj,
                "get_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the projection of the voxel.\n\n"

                ":param arg1: IPJ object to save VOX's meta to\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("get_limits", &GXVOX_wrap_get_limits,
                "get_limits((int_ref)arg1, (int_ref)arg2, (int_ref)arg3, (int_ref)arg4, (int_ref)arg5, (int_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the range of indices with non-dummy data.\n\n"

                ":param arg1: Index of minimum valid data in X.\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Index of minimum valid data in Y.\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Index of minimum valid data in Z.\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Index of maximum valid data in X.\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: Index of maximum valid data in Y.\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Index of maximum valid data in Z.\n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Find the non-dummy volume of a VOX object. If the voxel is all dummies,\n"
                "   					returns iMAX for the minima, and iMIN for the maxima.\n"
                "   				\n\n"
               );
    pyClass.def("get_limits_xyz", &GXVOX_wrap_get_limits_xyz,
                "get_limits_xyz((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the range in true XYZ of non-dummy data.\n\n"

                ":param arg1: Minimum valid data in X.\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Minimum valid data in Y.\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Minimum valid data in Z.\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Maximum valid data in X.\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Maximum valid data in Y.\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Maximum valid data in Z.\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Find the non-dummy volume of a VOX in true (X, Y, Z). This method\n"
                "   					works for voxels which are rotated or oriented in 3D, and returns\n"
                "   					the true min and max X, Y and Z limits in the data.\n"
                "   					The bounds are the bounds for the voxel\n"
                "   					center points. If the voxel is all dummies,\n"
                "   					returns rMAX for the minima, and rMIN for the maxima.\n"
                "   				\n\n"
               );
    pyClass.def("get_location", &GXVOX_wrap_get_location,
                "get_location((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get Location information\n\n"

                ":param arg1: Origin X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Origin Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Origin Z\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Cell sizes in X\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Cell sizes in Y\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Cell sizes in Z\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("get_location_points", &GXVOX_wrap_get_location_points,
                "get_location_points((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the computed location points.\n\n"

                ":param arg1: Locations in X\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Locations in Y\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Locations in Z\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("get_meta", &GXVOX_wrap_get_meta,
                "get_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the metadata of a voxel.\n\n"

                ":param arg1: META object to save VOX's meta to\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("get_double_location", &GXVOX_wrap_get_double_location,
                "get_double_location((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9, (float_ref)arg10, (float_ref)arg11, (float_ref)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the location of a voxel with origin and scaled xyz vectors\n\n"

                ":param arg1: Origin X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Origin Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Origin Z\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: VectX X\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: VectX Y\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: VectX Z\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: VectY X\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: VectY Y\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: VectY Z\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: VectZ X\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: VectZ Y\n"
                ":type arg11: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg12: VectZ Z\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("get_simple_location", &GXVOX_wrap_get_simple_location,
                "get_simple_location((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get Simple Location information\n\n"

                ":param arg1: Origin X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Origin Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Origin Z\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Cell Sizes in X (rDUMMY if not uniform)\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Cell Sizes in Y (rDUMMY if not uniform)\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Cell Sizes in Z (rDUMMY if not uniform)\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("get_stats", &GXVOX_wrap_get_stats,
                "get_stats() -> GXST:\n"

                "\n.. parsed-literal::\n\n"
                "   Get precomputed statistics on this object.\n\n"

                ":returns: ST object\n"
                ":rtype: :class:`geosoft.gxapi.GXST`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("get_tpat", &GXVOX_wrap_get_tpat,
                "get_tpat((GXTPAT)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a copy of a thematic voxel's TPAT object.\n\n"

                ":param arg1: TPAT object to get\n"
                ":type arg1: :class:`geosoft.gxapi.GXTPAT`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Each row in the TPAT object corresponds to a stored index\n"
                "   					value in the thematic voxel. The TPAT should NOT be modified\n"
                "   					by the addition or deletion of items, if it is to be\n"
                "   					restored into the VOX object, but the CODE, LABEL, DESCRIPTION\n"
                "   					or COLOR info can be changed.\n"
                "   					The TPAT object is stored inside the VOX META object.\n"
                "   				\n\n"
               );
    pyClass.def("grid_points", &GXVOX_wrap_grid_points,
                "grid_points((str)arg1, (str)arg2, (float)arg3, (int)arg4, (float)arg5, (float)arg6, (int)arg7, (int)arg8, (int)arg9, (float)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14, (int)arg15, (GXVV)arg16, (GXVV)arg17, (GXVV)arg18, (GXVV)arg19, (GXIPJ)arg20) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Grid a VOX from point VV's.\n\n"

                ":param arg1: Name of output VOX\n"
                ":type arg1: str\n"
                ":param arg2: Name of error VOX (\"\" for none)\n"
                ":type arg2: str\n"
                ":param arg3: Cell size (DUMMY for default)\n"
                ":type arg3: float\n"
                ":param arg4: Variogram Only\n"
                ":type arg4: int\n"
                ":param arg5: Minimum Search Radius (DUMMY for none)\n"
                ":type arg5: float\n"
                ":param arg6: Maximum Search Radius (DUMMY for none)\n"
                ":type arg6: float\n"
                ":param arg7: Minimum Search Points\n"
                ":type arg7: int\n"
                ":param arg8: Maximum Search Points\n"
                ":type arg8: int\n"
                ":param arg9: Model number 1-power, 2-sperical, 3-gaussian, 4-exponential\n"
                ":type arg9: int\n"
                ":param arg10: Power\n"
                ":type arg10: float\n"
                ":param arg11: Slope\n"
                ":type arg11: float\n"
                ":param arg12: Range\n"
                ":type arg12: float\n"
                ":param arg13: Nugget\n"
                ":type arg13: float\n"
                ":param arg14: Sill\n"
                ":type arg14: float\n"
                ":param arg15: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg15: int\n"
                ":param arg16: X VV\n"
                ":type arg16: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg17: Y VV\n"
                ":type arg17: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg18: Z VV\n"
                ":type arg18: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg19: Data VV\n"
                ":type arg19: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg20: IPJ\n"
                ":type arg20: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("grid_points");
    pyClass.def("grid_points_z", &GXVOX_wrap_grid_points_z,
                "grid_points_z((str)arg1, (str)arg2, (float)arg3, (str)arg4, (int)arg5, (float)arg6, (float)arg7, (int)arg8, (int)arg9, (int)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14, (float)arg15, (int)arg16, (GXVV)arg17, (GXVV)arg18, (GXVV)arg19, (GXVV)arg20, (GXIPJ)arg21) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Grid a VOX from point VV's (using variable Z's)\n\n"

                ":param arg1: Name of output VOX\n"
                ":type arg1: str\n"
                ":param arg2: Name of error VOX (\"\" for none)\n"
                ":type arg2: str\n"
                ":param arg3: Cell size (DUMMY for default)\n"
                ":type arg3: float\n"
                ":param arg4: Cell size in Z (\"\" for default)\n"
                ":type arg4: str\n"
                ":param arg5: Variogram Only\n"
                ":type arg5: int\n"
                ":param arg6: Minimum Search Radius (DUMMY for none)\n"
                ":type arg6: float\n"
                ":param arg7: Maximum Search Radius (DUMMY for none)\n"
                ":type arg7: float\n"
                ":param arg8: Minimum Search Points\n"
                ":type arg8: int\n"
                ":param arg9: Maximum Search Points\n"
                ":type arg9: int\n"
                ":param arg10: Model number 1-power, 2-sperical, 3-gaussian, 4-exponential\n"
                ":type arg10: int\n"
                ":param arg11: Power\n"
                ":type arg11: float\n"
                ":param arg12: Slope\n"
                ":type arg12: float\n"
                ":param arg13: Range\n"
                ":type arg13: float\n"
                ":param arg14: Nugget\n"
                ":type arg14: float\n"
                ":param arg15: Sill\n"
                ":type arg15: float\n"
                ":param arg16: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg16: int\n"
                ":param arg17: X VV\n"
                ":type arg17: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg18: Y VV\n"
                ":type arg18: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg19: Z VV\n"
                ":type arg19: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg20: Data VV\n"
                ":type arg20: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg21: IPJ\n"
                ":type arg21: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               ).staticmethod("grid_points_z");
    pyClass.def("grid_points_z_ex", &GXVOX_wrap_grid_points_z_ex,
                "grid_points_z_ex((str)arg1, (str)arg2, (float)arg3, (str)arg4, (int)arg5, (float)arg6, (float)arg7, (int)arg8, (int)arg9, (int)arg10, (float)arg11, (float_ref)arg12, (float_ref)arg13, (float)arg14, (float_ref)arg15, (float)arg16, (float)arg17, (float)arg18, (float)arg19, (float)arg20, (int)arg21, (GXVV)arg22, (GXVV)arg23, (GXVV)arg24, (GXVV)arg25, (GXIPJ)arg26) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Grid a VOX from point VV's (using variable Z's)\n\n"

                ":param arg1: Name of output VOX\n"
                ":type arg1: str\n"
                ":param arg2: Name of error VOX (\"\" for none)\n"
                ":type arg2: str\n"
                ":param arg3: Cell size (DUMMY for default)\n"
                ":type arg3: float\n"
                ":param arg4: Cell size in Z (\"\" for default)\n"
                ":type arg4: str\n"
                ":param arg5: Variogram Only\n"
                ":type arg5: int\n"
                ":param arg6: Minimum Search Radius (DUMMY for none)\n"
                ":type arg6: float\n"
                ":param arg7: Maximum Search Radius (DUMMY for none)\n"
                ":type arg7: float\n"
                ":param arg8: Minimum Search Points\n"
                ":type arg8: int\n"
                ":param arg9: Maximum Search Points\n"
                ":type arg9: int\n"
                ":param arg10: Model number 1-power, 2-sperical, 3-gaussian, 4-exponential\n"
                ":type arg10: int\n"
                ":param arg11: Power\n"
                ":type arg11: float\n"
                ":param arg12: Slope\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg13: Range\n"
                ":type arg13: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg14: Nugget\n"
                ":type arg14: float\n"
                ":param arg15: Sill\n"
                ":type arg15: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg16: Strike\n"
                ":type arg16: float\n"
                ":param arg17: Dip\n"
                ":type arg17: float\n"
                ":param arg18: Plunge\n"
                ":type arg18: float\n"
                ":param arg19: Strike Weight\n"
                ":type arg19: float\n"
                ":param arg20: Dip Plane Weight\n"
                ":type arg20: float\n"
                ":param arg21: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg21: int\n"
                ":param arg22: X VV\n"
                ":type arg22: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg23: Y VV\n"
                ":type arg23: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg24: Z VV\n"
                ":type arg24: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg25: Data VV\n"
                ":type arg25: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg26: IPJ\n"
                ":type arg26: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               ).staticmethod("grid_points_z_ex");
    pyClass.def("can_append_to", &GXVOX_wrap_can_append_to,
                "can_append_to((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check if this voxel can append to a surface file.\n\n"

                ":param arg1: Surface file\n"
                ":type arg1: str\n"
                ":returns: 1 if can append\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               );
    pyClass.def("get_cell_size_strings", &GXVOX_wrap_get_cell_size_strings,
                "get_cell_size_strings((str_ref)arg1, (str_ref)arg2, (str_ref)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Location Strings\n\n"

                ":param arg1: X String\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: Y String\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Z String\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Scale to multiply X\n"
                ":type arg4: float\n"
                ":param arg5: Scale to multiply Y\n"
                ":type arg5: float\n"
                ":param arg6: Scale to multiply Z\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.1\n\n"
               );
    pyClass.def("is_thematic", &GXVOX_wrap_is_thematic,
                "is_thematic() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this a thematic voxel?\n\n"

                ":returns: 1 if VOX is thematic\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A thematic voxel is one where the stored integer values\n"
                "   					represent indices into an internally stored TPAT object.\n"
                "   					Thematic voxels contain their own color definitions, and\n"
                "   					normal numerical operations, such as applying ITRs for display,\n"
                "   					are not valid.\n"
                "   				\n\n"
               );
    pyClass.def("is_vector_voxel", &GXVOX_wrap_is_vector_voxel,
                "is_vector_voxel() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this a vector voxel?\n\n"

                ":returns: 1 if VOX is a vector voxel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A vector voxel is one where each data element consists of 3 4-byte float values.\n"
                "   					Vector voxels normally have the file type \"geosoft_vectorvoxel\".\n"
                "   				\n\n"
               );
    pyClass.def("set_cell_size_strings", &GXVOX_wrap_set_cell_size_strings,
                "set_cell_size_strings((str)arg1, (str)arg2, (str)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Location Strings\n\n"

                ":param arg1: X String\n"
                ":type arg1: str\n"
                ":param arg2: Y String\n"
                ":type arg2: str\n"
                ":param arg3: Z String\n"
                ":type arg3: str\n"
                ":returns: 0 - Ok\n"
                "          						1 - Invalid data\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.1\n\n"
               );
    pyClass.def("list_gocad_properties", &GXVOX_wrap_list_gocad_properties,
                "list_gocad_properties((str)arg1, (GXLST)arg2) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   List all the properties available in this GOCAD file.\n\n"

                ":param arg1: Name of GOCAD Voxel file\n"
                ":type arg1: str\n"
                ":param arg2: List object to populate\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("list_gocad_properties");
    pyClass.def("log_grid_points_z_ex", &GXVOX_wrap_log_grid_points_z_ex,
                "log_grid_points_z_ex((str)arg1, (str)arg2, (float)arg3, (str)arg4, (int)arg5, (float)arg6, (float)arg7, (int)arg8, (int)arg9, (int)arg10, (float)arg11, (float_ref)arg12, (float_ref)arg13, (float)arg14, (float_ref)arg15, (float)arg16, (float)arg17, (float)arg18, (float)arg19, (float)arg20, (int)arg21, (float)arg22, (int)arg23, (GXVV)arg24, (GXVV)arg25, (GXVV)arg26, (GXVV)arg27, (GXIPJ)arg28) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Log grid a VOX from point VV's (using variable Z's)\n\n"

                ":param arg1: Name of output VOX\n"
                ":type arg1: str\n"
                ":param arg2: Name of error VOX (\"\" for none)\n"
                ":type arg2: str\n"
                ":param arg3: Cell size (DUMMY for default)\n"
                ":type arg3: float\n"
                ":param arg4: Cell size in Z (\"\" for default)\n"
                ":type arg4: str\n"
                ":param arg5: Variogram Only\n"
                ":type arg5: int\n"
                ":param arg6: Minimum Search Radius (DUMMY for none)\n"
                ":type arg6: float\n"
                ":param arg7: Maximum Search Radius (DUMMY for none)\n"
                ":type arg7: float\n"
                ":param arg8: Minimum Search Points\n"
                ":type arg8: int\n"
                ":param arg9: Maximum Search Points\n"
                ":type arg9: int\n"
                ":param arg10: Model number 1-power, 2-sperical, 3-gaussian, 4-exponential\n"
                ":type arg10: int\n"
                ":param arg11: Power\n"
                ":type arg11: float\n"
                ":param arg12: Slope\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg13: Range\n"
                ":type arg13: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg14: Nugget\n"
                ":type arg14: float\n"
                ":param arg15: Sill\n"
                ":type arg15: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg16: Strike\n"
                ":type arg16: float\n"
                ":param arg17: Dip\n"
                ":type arg17: float\n"
                ":param arg18: Plunge\n"
                ":type arg18: float\n"
                ":param arg19: Strike Weight\n"
                ":type arg19: float\n"
                ":param arg20: Dip Plane Weight\n"
                ":type arg20: float\n"
                ":param arg21: \\ :ref:`VOX_GRID_LOGOPT`\\  Log Option\n"
                ":type arg21: int\n"
                ":param arg22: Minimum log\n"
                ":type arg22: float\n"
                ":param arg23: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg23: int\n"
                ":param arg24: X VV\n"
                ":type arg24: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg25: Y VV\n"
                ":type arg25: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg26: Z VV\n"
                ":type arg26: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg27: Data VV\n"
                ":type arg27: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg28: IPJ\n"
                ":type arg28: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               ).staticmethod("log_grid_points_z_ex");
    pyClass.def("krig", &GXVOX_wrap_krig,
                "krig((str)arg1, (float)arg2, (int)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7, (GXIPJ)arg8, (GXREG)arg9) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   A more compact and extensible form of \\ :func:`geosoft.gxapi.GXVOX.log_grid_points_z_ex`\\ .\n\n"

                ":param arg1: Name of output VOX\n"
                ":type arg1: str\n"
                ":param arg2: Cell size (DUMMY for default)\n"
                ":type arg2: float\n"
                ":param arg3: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg3: int\n"
                ":param arg4: X VV\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Y VV\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Z VV\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Data VV\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: IPJ\n"
                ":type arg8: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg9: REG\n"
                ":type arg9: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Optional Parameters.\n"
                "   \n"
                "   					If these values are not set in the REG, then default parameters will be used.\n"
                "   \n"
                "   					ERROR_VOXEL:		Name of error VOX (\"\" for none)\n"
                "   					CELLSIZEZ:      Z Cell size string (space delimited, \"\" for default)\n"
                "   					RADIUS_MIN:		Minimum Search Radius (REAL) (Default = 4) (Blanking Distance)\n"
                "   					RADIUS_MAX:		Maximum Search Radius (REAL) (Default = 16)\n"
                "   					SEARCH_MIN:		Minimum Search Points (INT) (Default = 16)\n"
                "   					SEARCH_MAX:		Maximum Search Points (INT) (Default = 32)\n"
                "   					VARIOGRAM_ONLY: Set to 1 to calculate the variogram only (INT) (Default = 0)\n"
                "   					MODEL:				Variogram Model number 1-power, 2-sperical, 3-gaussian, 4-exponential  (INT) (Default = 2)\n"
                "   					POWER:          Power (Default = DUMMY)\n"
                "   					SLOPE:          Slope (REAL) (if input is DUMMY, value calculated and set on return)\n"
                "   					RANGE:          Range (REAL) (if input is DUMMY, value calculated and set on return)\n"
                "   					SILL :          Sill (REAL) (if input is DUMMY, value calculated and set on return)\n"
                "   					STRIKE:				Strike (REAL) (Default = 0)\n"
                "   					DIP:					Dip (REAL)	(Default = 90)\n"
                "   					PLUNGE:				Plunge (REAL) (Default = 0)\n"
                "   					STRIKE WEIGHT:	Along-Strike Weight (REAL) (Default = 1)\n"
                "   					DIP_WEIGHT:      Down-Dip Weight (REAL) (Default = 1)\n"
                "   					LOG_OPT:			One of VOX_GRID_LOGOPT (Default = 0)\n"
                "   					MIN_LOG:			Log Minimum (REAL)	(Default = 1)\n"
                "   					MIN_X:				Minimum X (REAL) (default = DUMMY to determine from the data. If input, nearest lt. or eq. multiple of cell size chosen)\n"
                "   					MAX_X:				Maximum X (REAL) (default = DUMMY to determine from the data. If input, nearest gt. or eq. multiple of cell size chosen)\n"
                "   					MIN_Y:				Minimum Y (REAL) (default = DUMMY to determine from the data. If input, nearest lt. or eq. external multiple of cell size chosen)\n"
                "   					MAX_Y:				Maximum Y (REAL) (default = DUMMY to determine from the data. If input, nearest gt. or eq. multiple of cell size chosen)\n"
                "   					MIN_Z:				Minimum Z (REAL) (default = DUMMY to determine from the data. If input, nearest lt. or eq. multiple of cell size chosen)\n"
                "   					MAX_Z:				Maximum Z (REAL) (default = DUMMY to determine from the data. If input, nearest gt. or eq. multiple of cell size chosen)A more compact and extensible form of \\ :func:`geosoft.gxapi.GXVOX.log_grid_points_z_ex`\\ . Only the most\n"
                "   					basic parameters are entered directly. Optional parameters are passed via a REG object.\n"
                "   				\n\n"
               ).staticmethod("krig");
    pyClass.def("math", &GXVOX_wrap_math,
                "math((str)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (GXLST)arg6) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Produces a new voxes using a formula on existing voxels/Grids\n\n"

                ":param arg1: Master VOX Name\n"
                ":type arg1: str\n"
                ":param arg2: Master VOX Variable Name\n"
                ":type arg2: str\n"
                ":param arg3: Output VOX Name\n"
                ":type arg3: str\n"
                ":param arg4: Output VOX Variable Name\n"
                ":type arg4: str\n"
                ":param arg5: Formula\n"
                ":type arg5: str\n"
                ":param arg6: List of Voxels/Grids to use as inputs\n"
                ":type arg6: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: VOXEL handle\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The input voxels must all be of the same type.\n\n"
               ).staticmethod("math");
    pyClass.def("merge", &GXVOX_wrap_merge,
                "merge((GXVOX)arg1, (GXREG)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Merge two Voxels.\n\n"

                ":param arg1: VOX object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVOX`\n"
                ":param arg2: Parameters (see above)\n"
                ":type arg2: :class:`geosoft.gxapi.GXREG`\n"
                ":param arg3: Output voxel file name.\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"
               );
    pyClass.def("nearest_neighbour_grid", &GXVOX_wrap_nearest_neighbour_grid,
                "nearest_neighbour_grid((str)arg1, (float)arg2, (float)arg3, (int)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7, (GXVV)arg8, (GXIPJ)arg9) -> GXVOX:\n"

                "\n.. parsed-literal::\n\n"
                "   Grid a VOX from point VV's using the Nearest Neighbours method.\n\n"

                ":param arg1: Name of output VOX\n"
                ":type arg1: str\n"
                ":param arg2: Cell size (DUMMY for default)\n"
                ":type arg2: float\n"
                ":param arg3: Maximum radius (DUMMY for none)\n"
                ":type arg3: float\n"
                ":param arg4: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg4: int\n"
                ":param arg5: X VV\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Y VV\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Z VV\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Data VV\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: IPJ\n"
                ":type arg9: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: VOX Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVOX`\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("nearest_neighbour_grid");
    pyClass.def("compute_cell_size", &GXVOX_wrap_compute_cell_size,
                "compute_cell_size((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute the Cell size based on specific Area\n\n"

                ":param arg1: MinX\n"
                ":type arg1: float\n"
                ":param arg2: MinY\n"
                ":type arg2: float\n"
                ":param arg3: MinZ\n"
                ":type arg3: float\n"
                ":param arg4: MaxX\n"
                ":type arg4: float\n"
                ":param arg5: MaxY\n"
                ":type arg5: float\n"
                ":param arg6: MaxZ\n"
                ":type arg6: float\n"
                ":returns: Cell Size\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               ).staticmethod("compute_cell_size");
    pyClass.def("re_grid", &GXVOX_wrap_re_grid,
                "re_grid((GXVOX)arg1, (GXREG)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Regrid a Voxel.\n\n"

                ":param arg1: VOX object to regrid\n"
                ":type arg1: :class:`geosoft.gxapi.GXVOX`\n"
                ":param arg2: Parameters (not implemented)\n"
                ":type arg2: :class:`geosoft.gxapi.GXREG`\n"
                ":param arg3: Output voxel file name.\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"
               );
    pyClass.def("resample_pg", &GXVOX_wrap_resample_pg,
                "resample_pg((GXIPJ)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (int)arg8, (int)arg9, (int)arg10, (float)arg11, (float)arg12, (int)arg13) -> GXPG:\n"

                "\n.. parsed-literal::\n\n"
                "   Resample a voxel over an input volume to a PG.\n\n"

                ":param arg1: Projection to use for Origin, Spacing values\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: Origin X\n"
                ":type arg2: float\n"
                ":param arg3: Origin Y\n"
                ":type arg3: float\n"
                ":param arg4: Origin Z\n"
                ":type arg4: float\n"
                ":param arg5: Spacing in X\n"
                ":type arg5: float\n"
                ":param arg6: Spacing in Y\n"
                ":type arg6: float\n"
                ":param arg7: Spacing in Z\n"
                ":type arg7: float\n"
                ":param arg8: Samples in X\n"
                ":type arg8: int\n"
                ":param arg9: Samples in Y\n"
                ":type arg9: int\n"
                ":param arg10: Samples in Z\n"
                ":type arg10: int\n"
                ":param arg11: Minimum Z to resample (can be rDUMMY)\n"
                ":type arg11: float\n"
                ":param arg12: Maximum Z to resample (can be rDUMMY)\n"
                ":type arg12: float\n"
                ":param arg13: \\ :ref:`VOX_SLICE_MODE`\\ \n"
                ":type arg13: int\n"
                ":returns: PG object, terminates on error\n"
                ":rtype: :class:`geosoft.gxapi.GXPG`\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Creates and dummies a PG object based on the input\n"
                "   					dimensions, then resamples the voxel to the pager\n"
                "   					at the locations determined by input projection, origin and spacings.\n"
                "   				\n\n"
               );
    pyClass.def("rescale_cell_sizes", &GXVOX_wrap_rescale_cell_sizes,
                "rescale_cell_sizes((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Multiply all cell sizes by a fixed factor.\n\n"

                ":param arg1: Scaling factor (>0)\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is useful, for instance for converting sizes in one\n"
                "   					unit to sizes in another unit if changing the projection\n"
                "   					and the projection's unit changes, since the voxel inherits\n"
                "   					its projection's units.\n"
                "   				\n\n"
               );
    pyClass.def("sample_cdi", &GXVOX_wrap_sample_cdi,
                "sample_cdi((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7, (int)arg8, (str)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sample a voxel at locations/elevations in a CDI database.\n\n"

                ":param arg1: CDI Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line handle\n"
                ":type arg2: int\n"
                ":param arg3: X channel handle\n"
                ":type arg3: int\n"
                ":param arg4: Y channel handle\n"
                ":type arg4: int\n"
                ":param arg5: depth array channel handle\n"
                ":type arg5: int\n"
                ":param arg6: depths sign: 0 - positive down, 1 - negative down\n"
                ":type arg6: int\n"
                ":param arg7: elevation channel handle (can be NULLSYMB)\n"
                ":type arg7: int\n"
                ":param arg8: interpolation mode: 0 - linear, 1 - nearest\n"
                ":type arg8: int\n"
                ":param arg9: Output channel name\n"
                ":type arg9: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A \"CDI\" database does not need to be conductivity/depth.\n"
                "   					It normally contains an array channel of depth values for\n"
                "   					each (X, Y) location, with corresponding data array channels of\n"
                "   					values taken at those (X, Y, Z) locations.\n"
                "   					If the optional elevation channel is used, its value is used as an\n"
                "   					offset to the depth channel values. Depths are positive down by\n"
                "   					default; use the \"Negative depths down\" parameter if the depths\n"
                "   					become more negative as you go deeper.\n"
                "   				\n\n"
               );
    pyClass.def("sample_cdi_to_topography", &GXVOX_wrap_sample_cdi_to_topography,
                "sample_cdi_to_topography((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (GXVV)arg5, (int)arg6, (str)arg7, (str)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Sample a voxel at fixed elevations along a path in a CDI database, and output them to an array channel, deleting leading dummy values, and\n"
                "   					writing the elevation of the first non-dummy item to a topography channel.\n"
                "   				\n\n"

                ":param arg1: CDI Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line handle\n"
                ":type arg2: int\n"
                ":param arg3: X channel handle\n"
                ":type arg3: int\n"
                ":param arg4: Y channel handle\n"
                ":type arg4: int\n"
                ":param arg5: Z values to sample at each X, Y\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: interpolation mode: 0 - linear, 1 - nearest\n"
                ":type arg6: int\n"
                ":param arg7: Output data array channel name\n"
                ":type arg7: str\n"
                ":param arg8: Output topography channel name\n"
                ":type arg8: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2\n\n"
               );
    pyClass.def("sample_vv", &GXVOX_wrap_sample_vv,
                "sample_vv((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (int)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sample a voxel at multiple locations.\n\n"

                ":param arg1: X locations (input)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y locations (input)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z locations (input)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: interpolation mode: 0 - linear, 1 - nearest\n"
                ":type arg4: int\n"
                ":param arg5: returned values\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Sample at voxel at XYZ locations input in VVs. Values returned in a VV.\n"
                "   				\n\n"
               );
    pyClass.def("set_ipj", &GXVOX_wrap_set_ipj,
                "set_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the projection of the voxel.\n\n"

                ":param arg1: IPJ object to save VOX's meta to\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("set_location", &GXVOX_wrap_set_location,
                "set_location((float)arg1, (float)arg2, (float)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set Location information\n\n"

                ":param arg1: Origin X\n"
                ":type arg1: float\n"
                ":param arg2: Origin Y\n"
                ":type arg2: float\n"
                ":param arg3: Origin Z\n"
                ":type arg3: float\n"
                ":param arg4: Cell sizes in X\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Cell sizes in Y\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Cell sizes in Z\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("set_meta", &GXVOX_wrap_set_meta,
                "set_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the metadata of a voxel.\n\n"

                ":param arg1: META object to add to VOX's meta\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("set_origin", &GXVOX_wrap_set_origin,
                "set_origin((int)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Voxel Origin\n\n"

                ":param arg1: Type of origin being set \\ :ref:`VOX_ORIGIN`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Origin X\n"
                ":type arg2: float\n"
                ":param arg3: Origin Y\n"
                ":type arg3: float\n"
                ":param arg4: Origin Z\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.1\n\n"
               );
    pyClass.def("set_simple_location", &GXVOX_wrap_set_simple_location,
                "set_simple_location((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set Simple Location information\n\n"

                ":param arg1: Origin X\n"
                ":type arg1: float\n"
                ":param arg2: Origin Y\n"
                ":type arg2: float\n"
                ":param arg3: Origin Z\n"
                ":type arg3: float\n"
                ":param arg4: Cell Sizes in X (rDUMMY if not changed)\n"
                ":type arg4: float\n"
                ":param arg5: Cell Sizes in Y (rDUMMY if not changed)\n"
                ":type arg5: float\n"
                ":param arg6: Cell Sizes in Z (rDUMMY if not changed)\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("set_tpat", &GXVOX_wrap_set_tpat,
                "set_tpat((GXTPAT)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a thematic voxel's TPAT object.\n\n"

                ":param arg1: TPAT object to store\n"
                ":type arg1: :class:`geosoft.gxapi.GXTPAT`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Each row in the TPAT object corresponds to a stored index\n"
                "   					value in the thematic voxel. The TPAT should NOT be modified\n"
                "   					by the addition or deletion of items, if it is to be\n"
                "   					restored into the VOX object, but the CODE, LABEL, DESCRIPTION\n"
                "   					or COLOR info can be changed.\n"
                "   					The TPAT object is stored inside the VOX META object.\n"
                "   				\n\n"
               );
    pyClass.def("slice_ipj", &GXVOX_wrap_slice_ipj,
                "slice_ipj((str)arg1, (GXIPJ)arg2, (int)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (int)arg8, (int)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Extract a slice of a voxel based on an IPJ\n\n"

                ":param arg1: Grid Name\n"
                ":type arg1: str\n"
                ":param arg2: Grid IPJ (includes orientation, etc)\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg3: \\ :ref:`VOX_SLICE_MODE`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Grid Origin X\n"
                ":type arg4: float\n"
                ":param arg5: Grid Origin Y\n"
                ":type arg5: float\n"
                ":param arg6: Grid Cell Size in X\n"
                ":type arg6: float\n"
                ":param arg7: Grid Cell Size in Y\n"
                ":type arg7: float\n"
                ":param arg8: Grid cells in X\n"
                ":type arg8: int\n"
                ":param arg9: Grid cells in Y\n"
                ":type arg9: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("slice_multi_layer_ipj", &GXVOX_wrap_slice_multi_layer_ipj,
                "slice_multi_layer_ipj((str)arg1, (GXIPJ)arg2, (int)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (int)arg8, (int)arg9, (int)arg10, (float)arg11, (float)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Extract multiple slices of a voxel based on an IPJ\n\n"

                ":param arg1: Grid Name\n"
                ":type arg1: str\n"
                ":param arg2: Grid IPJ (includes orientation, etc)\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg3: \\ :ref:`VOX_SLICE_MODE`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Grid Origin X\n"
                ":type arg4: float\n"
                ":param arg5: Grid Origin Y\n"
                ":type arg5: float\n"
                ":param arg6: Grid Cell Size in X\n"
                ":type arg6: float\n"
                ":param arg7: Grid Cell Size in Y\n"
                ":type arg7: float\n"
                ":param arg8: Grid cells in X\n"
                ":type arg8: int\n"
                ":param arg9: Grid cells in Y\n"
                ":type arg9: int\n"
                ":param arg10: Number of layers to extract\n"
                ":type arg10: int\n"
                ":param arg11: Start elevation\n"
                ":type arg11: float\n"
                ":param arg12: Elevation increment\n"
                ":type arg12: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("subset_to_double_extents", &GXVOX_wrap_subset_to_double_extents,
                "subset_to_double_extents((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Subset a VOX to real extents.\n\n"

                ":param arg1: Output voxel file name.\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"
               );
    pyClass.def("sync", &GXVOX_wrap_sync,
                "sync((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Syncronize the Metadata for this Voxel\n\n"

                ":param arg1: voxel name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("sync");
    pyClass.def("window_ply", &GXVOX_wrap_window_ply,
                "window_ply((GXPLY)arg1, (int)arg2, (float)arg3, (float)arg4, (str)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Window a VOX to a PLY file and Z.\n\n"

                ":param arg1: PLY object\n"
                ":type arg1: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg2: Mask (0: inside PLY, 1: outside PLY)\n"
                ":type arg2: int\n"
                ":param arg3: Minimum Z (optional, rDUMMY for no minimum)\n"
                ":type arg3: float\n"
                ":param arg4: Maximum Z (optional, rDUMMY for no maximun)\n"
                ":type arg4: float\n"
                ":param arg5: Output voxel file name.\n"
                ":type arg5: str\n"
                ":param arg6: Clip extents to remove dummies (0: no (same size), 1: yes (smaller))\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The voxel is windowed horizontally to the input PLY file.\n"
                "   					Optionally, it will be windowed to the input Z range as well.\n"
                "   					The output can be clipped to the non-dummied cells.\n"
                "   				\n\n"
               );
    pyClass.def("window_xyz", &GXVOX_wrap_window_xyz,
                "window_xyz((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (str)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Window a VOX to ranges in X, Y and Z.\n\n"

                ":param arg1: Minimum X (optional, rDUMMY for no minimum)\n"
                ":type arg1: float\n"
                ":param arg2: Minimum Y (optional, rDUMMY for no minimum)\n"
                ":type arg2: float\n"
                ":param arg3: Minimum Z (optional, rDUMMY for no minimum)\n"
                ":type arg3: float\n"
                ":param arg4: Maximum X (optional, rDUMMY for no maximun)\n"
                ":type arg4: float\n"
                ":param arg5: Maximum Y (optional, rDUMMY for no maximun)\n"
                ":type arg5: float\n"
                ":param arg6: Maximum Z (optional, rDUMMY for no maximun)\n"
                ":type arg6: float\n"
                ":param arg7: Output voxel file name.\n"
                ":type arg7: str\n"
                ":param arg8: Clip extents to remove dummies (0: no (same size), 1: yes (smaller))\n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The six minima and maxima are optional.\n"
                "   					The output can be clipped to the non-dummied cells.\n"
                "   				\n\n"
               );
    pyClass.def("write_xml", &GXVOX_wrap_write_xml,
                "write_xml((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export the VOX to XML\n\n"

                ":param arg1: XML file to create\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("convert_numeric_to_thematic", &GXVOX_wrap_convert_numeric_to_thematic,
                "convert_numeric_to_thematic((GXVV)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert numeric voxel to thematic (lithology) voxel\n\n"

                ":param arg1: Translation VV handle.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Output voxel file name.\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4\n\n"
               );
    pyClass.def("convert_thematic_to_numeric", &GXVOX_wrap_convert_thematic_to_numeric,
                "convert_thematic_to_numeric((GXVV)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert thematic (lithology) voxel to numeric voxel\n\n"

                ":param arg1: Translation VV handle.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Output voxel file name.\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4\n\n"
               );
    pyClass.def("convert_velocity_to_density", &GXVOX_wrap_convert_velocity_to_density,
                "convert_velocity_to_density((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (str)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Produces a density voxel using the velocity values in this voxel.\n\n"

                ":param arg1: 1.0, if this voxel is in meters per second. Otherwise, a value by which each input cell is multiplied to convert it into meters per second.\n"
                ":type arg1: float\n"
                ":param arg2: Coefficient of fifth-order polynomial term.\n"
                ":type arg2: float\n"
                ":param arg3: Coefficient of fourth-order polynomial term.\n"
                ":type arg3: float\n"
                ":param arg4: Coefficient of third-order polynomial term.\n"
                ":type arg4: float\n"
                ":param arg5: Coefficient of second-order polynomial term.\n"
                ":type arg5: float\n"
                ":param arg6: Coefficient of first-order polynomial term.\n"
                ":type arg6: float\n"
                ":param arg7: Constant offset of output.\n"
                ":type arg7: float\n"
                ":param arg8: 1.0, to produce an output voxel that has units of g/cm^3. If different units are desired, pass in a different value, which will be multiplied into each output voxel cell.\n"
                ":type arg8: float\n"
                ":param arg9: Filename of the output voxel.\n"
                ":type arg9: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4\n\n"
               );
    pyClass.def("convert_velocity_in_range_to_density", &GXVOX_wrap_convert_velocity_in_range_to_density,
                "convert_velocity_in_range_to_density((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (str)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Produces a density voxel using the velocity values in this voxel, as long as the velocity values are in range.\n\n"

                ":param arg1: 1.0, if this voxel is in meters per second. Otherwise, a value by which each input cell is multiplied to convert it into meters per second.\n"
                ":type arg1: float\n"
                ":param arg2: Lower bound on velocity values, in meters per second. If the input value (after being pre-multiplied by dInputScalingFactor) is less than this value, the output cell value will be DUMMY.\n"
                ":type arg2: float\n"
                ":param arg3: Upper bound on velocity values, in meters per second. If the input value (after being pre-multiplied by dInputScalingFactor) is greater than this value, the output cell value will be DUMMY.\n"
                ":type arg3: float\n"
                ":param arg4: Coefficient of fifth-order polynomial term.\n"
                ":type arg4: float\n"
                ":param arg5: Coefficient of fourth-order polynomial term.\n"
                ":type arg5: float\n"
                ":param arg6: Coefficient of third-order polynomial term.\n"
                ":type arg6: float\n"
                ":param arg7: Coefficient of second-order polynomial term.\n"
                ":type arg7: float\n"
                ":param arg8: Coefficient of first-order polynomial term.\n"
                ":type arg8: float\n"
                ":param arg9: Constant offset of output.\n"
                ":type arg9: float\n"
                ":param arg10: 1.0, to produce an output voxel that has units of g/cm^3. If different units are desired, pass in a different value, which will be multiplied into each output voxel cell.\n"
                ":type arg10: float\n"
                ":param arg11: Filename of the output voxel.\n"
                ":type arg11: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4\n\n"
               );
    pyClass.def("convert_density_to_velocity", &GXVOX_wrap_convert_density_to_velocity,
                "convert_density_to_velocity((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (str)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Produces a velocity voxel using the density values in this voxel.\n\n"

                ":param arg1: 1.0, if this voxel is in g/cm^3. Otherwise, a value by which each input cell is multiplied to convert it into g/cm^3.\n"
                ":type arg1: float\n"
                ":param arg2: Lower bound on velocity values, in g/vm^3. If the input value (after being pre-multiplied by dInputScalingFactor) is less than this value, the output cell value will be DUMMY.\n"
                ":type arg2: float\n"
                ":param arg3: Upper bound on velocity values, in g/cm^3. If the input value (after being pre-multiplied by dInputScalingFactor) is greater than this value, the output cell value will be DUMMY.\n"
                ":type arg3: float\n"
                ":param arg4: Coefficient of fifth-order polynomial term.\n"
                ":type arg4: float\n"
                ":param arg5: Coefficient of fourth-order polynomial term.\n"
                ":type arg5: float\n"
                ":param arg6: Coefficient of third-order polynomial term.\n"
                ":type arg6: float\n"
                ":param arg7: Coefficient of second-order polynomial term.\n"
                ":type arg7: float\n"
                ":param arg8: Coefficient of first-order polynomial term.\n"
                ":type arg8: float\n"
                ":param arg9: Constant offset of output.\n"
                ":type arg9: float\n"
                ":param arg10: 1.0, to produce an output voxel that has units of meters per second. If different units are desired, pass in a different value, which will be multiplied into each output voxel cell.\n"
                ":type arg10: float\n"
                ":param arg11: Filename of the output voxel.\n"
                ":type arg11: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4\n\n"
               );
    pyClass.def("invert_z", &GXVOX_wrap_invert_z,
                "invert_z((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert an inverted voxel to normal orientation\n\n"

                ":param arg1: Output voxel file name.\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4\n\n"
               );
    pyClass.def("dw_grid_db", &GXVOX_wrap_dw_grid_db,
                "dw_grid_db((str)arg1, (GXDB)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (GXREG)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \\ :func:`geosoft.gxapi.GXVOX.dw_grid_db`\\      Inverse-distance weighting gridding method, DB version, 3D.\n\n"

                ":param arg1: Output voxel name\n"
                ":type arg1: str\n"
                ":param arg2: Database\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg3: X Channel [READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Channel [READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Z Channel [READONLY]\n"
                ":type arg5: int\n"
                ":param arg6: Data Channel [READONLY]\n"
                ":type arg6: int\n"
                ":param arg7: Parameters (see above)\n"
                ":type arg7: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					3D cells take on the averaged values within a search radius, weighted inversely by distance.\n"
                "   \n"
                "   					Weighting can be controlled using the power and slope properties;\n"
                "   \n"
                "   					weighting = 1 / (distance^wtpower + 1/slope) where distance is in\n"
                "   					units of grid cells (X dimenstion). Default is 0.0,\n"
                "   \n"
                "   					If the blanking distance is set, all cells whose center point is not within the blanking distance of\n"
                "   					at least one data point are set to dummy.\n"
                "   \n"
                "   					REG Parameters:\n"
                "   \n"
                "   					X0, Y0, Z0, DX, DY, DZ: Voxel origin, and cell sizes (required)\n"
                "   					WT_POWER (default=2), WT_SLOPE (default=1) Weighting function parameters\n"
                "   					SEARCH_RADIUS: Distance weighting limit (default = 4 \\ `*`\\  CUBE_ROOT(DX\\ `*`\\ DY\\ `*`\\ DZ))\n"
                "   					BLANKING_DISTANCE: Dummy values farther from data than this distance. (default = 4 \\ `*`\\  CUBE_ROOT(DX\\ `*`\\ DY\\ `*`\\ DZ))\n"
                "   					LOG: Apply log transform to input data before gridding (0:No (default), 1:Yes)?\n"
                "   					LOG_BASE: One of VV_LOG_BASE_10 (default) or VV_LOG_BASE_E\n"
                "   					LOG_NEGATIVE: One of VV_LOG_NEGATIVE_NO (default) or VV_LOG_NEGATIVE_YES\n"
                "   				\n\n"
               ).staticmethod("dw_grid_db");
    pyClass.def("tin_grid_db", &GXVOX_wrap_tin_grid_db,
                "tin_grid_db((str)arg1, (GXDB)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7, (GXVV)arg8, (GXREG)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \\ :func:`geosoft.gxapi.GXVOX.tin_grid_db`\\    TIN-Gridding, DB version, 3D.\n\n"

                ":param arg1: Output voxel name\n"
                ":type arg1: str\n"
                ":param arg2: Database\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg3: X Channel [READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Channel [READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Z Channel [READONLY]\n"
                ":type arg5: int\n"
                ":param arg6: Data Channel [READONLY]\n"
                ":type arg6: int\n"
                ":param arg7: Gridding method (0: Linear, 1: Natural Neighbour, 2: Nearest Neightbour\n"
                ":type arg7: int\n"
                ":param arg8: Z Cell sizes (bottom to top)\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Parameters (see above)\n"
                ":type arg9: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Designed for data in array channels position vertically at single XY locations.\n"
                "   					Creates a TIN using the XY locations and uses the coefficients for the top layer on\n"
                "   					each layer below to make it efficient.\n"
                "   \n"
                "   					REG Parameters:\n"
                "   \n"
                "   					X0, Y0, Z0, DX, DY, DZ: Voxel origin, and cell sizes (required)\n"
                "   					NX, NY, NZ: Voxel dimensions.\n"
                "   					DZ and NZ are used only if the input cell sizes VV is of zero length.\n"
                "   				\n\n"
               ).staticmethod("tin_grid_db");

    scope().attr("VOX_DIR_XY") = (int32_t)0;
    scope().attr("VOX_DIR_XZ") = (int32_t)1;
    scope().attr("VOX_DIR_YZ") = (int32_t)2;
    scope().attr("VOX_3D_DIR_XYZ") = (int32_t)0;
    scope().attr("VOX_3D_DIR_YXZ") = (int32_t)1;
    scope().attr("VOX_3D_DIR_XZY") = (int32_t)2;
    scope().attr("VOX_3D_DIR_YZX") = (int32_t)3;
    scope().attr("VOX_3D_DIR_ZXY") = (int32_t)4;
    scope().attr("VOX_3D_DIR_ZYX") = (int32_t)5;
    scope().attr("VOX_FILTER3D_FILE") = (int32_t)0;
    scope().attr("VOX_FILTER3D_SMOOTHING") = (int32_t)1;
    scope().attr("VOX_FILTER3D_LAPLACE") = (int32_t)2;
    scope().attr("VOX_FILTER3D_X_GRADIENT") = (int32_t)3;
    scope().attr("VOX_FILTER3D_Y_GRADIENT") = (int32_t)4;
    scope().attr("VOX_FILTER3D_Z_GRADIENT") = (int32_t)5;
    scope().attr("VOX_FILTER3D_TOTAL_GRADIENT") = (int32_t)6;
    scope().attr("VOX_GOCAD_ORIENTATIONS_NORMAL") = (int32_t)0;
    scope().attr("VOX_GOCAD_ORIENTATIONS_INVERTED") = (int32_t)1;
    scope().attr("VOX_GOCAD_ORIENTATIONS_NORMAL_ZFIRST") = (int32_t)2;
    scope().attr("VOX_GOCAD_ORIENTATIONS_INVERTED_ZFIRST") = (int32_t)3;
    scope().attr("VOX_GRID_LOGOPT_LINEAR") = (int32_t)0;
    scope().attr("VOX_GRID_LOGOPT_LOG_SAVELINEAR") = (int32_t)-1;
    scope().attr("VOX_GRID_LOGOPT_LOGLINEAR_SAVELINEAR") = (int32_t)-2;
    scope().attr("VOX_GRID_LOGOPT_LOG_SAVELOG") = (int32_t)1;
    scope().attr("VOX_GRID_LOGOPT_LOGLINEAR_SAVELOG") = (int32_t)2;
    scope().attr("VOX_ORIGIN_BOTTOM") = (int32_t)0;
    scope().attr("VOX_ORIGIN_TOP") = (int32_t)1;
    scope().attr("VOX_SLICE_MODE_LINEAR") = (int32_t)1;
    scope().attr("VOX_SLICE_MODE_NEAREST") = (int32_t)0;
    scope().attr("VOX_VECTORVOX_XYZ") = (int32_t)0;
    scope().attr("VOX_VECTORVOX_UVW") = (int32_t)1;
    scope().attr("VOX_VECTORVOX_AID") = (int32_t)2;

}
