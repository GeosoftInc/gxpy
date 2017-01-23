#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline int32_t GXDH_wrap_is_esri()
{
    int32_t ret = GXDH::is_esri();
    return ret;
}
inline void GXDH_wrap_creat_chan_lst(GXDHPtr self, GXLSTPtr arg1)
{
    self->creat_chan_lst(arg1);
}
inline void GXDH_wrap_depth_data_lst(GXDHPtr self, GXLSTPtr arg1)
{
    self->depth_data_lst(arg1);
}
inline void GXDH_wrap_from_to_data_lst(GXDHPtr self, const gx_string_type& arg1, GXLSTPtr arg2)
{
    self->from_to_data_lst(arg1, arg2);
}
inline void GXDH_wrap_get_geology_contacts(GXDHPtr self, GXLSTPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4, double arg5, GXVVPtr arg6, GXVVPtr arg7, GXVVPtr arg8)
{
    self->get_geology_contacts(arg1, arg2, arg3, (DH_SURFACE)arg4, arg5, arg6, arg7, arg8);
}
inline void GXDH_wrap_get_oriented_core_dip_dir(GXDHPtr self, GXLSTPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4, const gx_string_type& arg5, const gx_string_type& arg6)
{
    self->get_oriented_core_dip_dir(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDH_wrap_get_unique_channel_items(GXDHPtr self, const gx_string_type& arg1, int32_t arg2, GXVVPtr arg3)
{
    self->get_unique_channel_items(arg1, arg2, arg3);
}
inline void GXDH_wrap_get_unique_channel_items_from_collar(GXDHPtr self, const gx_string_type& arg1, int32_t arg2, GXVVPtr arg3)
{
    self->get_unique_channel_items_from_collar(arg1, arg2, arg3);
}
inline int32_t GXDH_wrap_chan_type(GXDHPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->chan_type(arg1);
    return ret;
}
inline int32_t GXDH_wrap_find_hole_intersection(GXDHPtr self, int32_t arg1, GXIMGPtr arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    int32_t ret = self->find_hole_intersection(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline void GXDH_wrap_get_chan_code_info(GXDHPtr self, const gx_string_type& arg1, int_ref& arg2, str_ref& arg3)
{
    self->get_chan_code_info(arg1, arg2, arg3);
}
inline int32_t GXDH_wrap_grid_intersection(GXDHPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, const gx_string_type& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9)
{
    int32_t ret = self->grid_intersection(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
    return ret;
}
inline void GXDH_wrap_litho_grid_3d(GXDHPtr self, const gx_string_type& arg1, GXTPATPtr arg2, const gx_string_type& arg3, double arg4, double arg5, double arg6, int32_t arg7, GXREGPtr arg8, int32_t arg9)
{
    self->litho_grid_3d(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXDH_wrap_numeric_chan_lst(GXDHPtr self, GXLSTPtr arg1)
{
    self->numeric_chan_lst(arg1);
}
inline void GXDH_wrap_numeric_from_to_data_lst(GXDHPtr self, const gx_string_type& arg1, GXLSTPtr arg2)
{
    self->numeric_from_to_data_lst(arg1, arg2);
}
inline void GXDH_wrap_punch_grid_holes(GXDHPtr self, GXIMGPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, double arg5)
{
    self->punch_grid_holes(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDH_wrap_string_chan_lst(GXDHPtr self, GXLSTPtr arg1)
{
    self->string_chan_lst(arg1);
}
inline void GXDH_wrap_string_from_to_data_lst(GXDHPtr self, const gx_string_type& arg1, GXLSTPtr arg2)
{
    self->string_from_to_data_lst(arg1, arg2);
}
inline GXDBPtr GXDH_wrap_h_assay_db(GXDHPtr self, int32_t arg1)
{
    GXDBPtr ret = self->h_assay_db(arg1);
    return ret;
}
inline int32_t GXDH_wrap_h_assay_symb(GXDHPtr self, int32_t arg1, int32_t arg2)
{
    int32_t ret = self->h_assay_symb(arg1, arg2);
    return ret;
}
inline GXDBPtr GXDH_wrap_h_collar_db(GXDHPtr self)
{
    GXDBPtr ret = self->h_collar_db();
    return ret;
}
inline int32_t GXDH_wrap_h_collar_symb(GXDHPtr self)
{
    int32_t ret = self->h_collar_symb();
    return ret;
}
inline GXDBPtr GXDH_wrap_h_dip_az_survey_db(GXDHPtr self)
{
    GXDBPtr ret = self->h_dip_az_survey_db();
    return ret;
}
inline int32_t GXDH_wrap_h_dip_az_survey_symb(GXDHPtr self, int32_t arg1)
{
    int32_t ret = self->h_dip_az_survey_symb(arg1);
    return ret;
}
inline GXDBPtr GXDH_wrap_h_en_survey_db(GXDHPtr self)
{
    GXDBPtr ret = self->h_en_survey_db();
    return ret;
}
inline int32_t GXDH_wrap_h_en_survey_symb(GXDHPtr self, int32_t arg1)
{
    int32_t ret = self->h_en_survey_symb(arg1);
    return ret;
}
inline void GXDH_wrap_add_survey_table(GXDHPtr self, int32_t arg1)
{
    self->add_survey_table(arg1);
}
inline void GXDH_wrap_assay_hole_lst(GXDHPtr self, int32_t arg1, GXLSTPtr arg2)
{
    self->assay_hole_lst(arg1, arg2);
}
inline void GXDH_wrap_assay_lst(GXDHPtr self, GXLSTPtr arg1)
{
    self->assay_lst(arg1);
}
inline void GXDH_wrap_auto_select_holes(int32_t arg1)
{
    GXDH::auto_select_holes(arg1);
}
inline void GXDH_wrap_clean(GXDHPtr self)
{
    self->clean();
}
inline void GXDH_wrap_composite_db(GXDHPtr self, GXDBPtr arg1, GXDBPtr arg2, int32_t arg3, int32_t arg4, double arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8, double arg9, double arg10, double arg11, int32_t arg12, const gx_string_type& arg13)
{
    self->composite_db(arg1, arg2, (DH_COMPSTDB_HOLSEL)arg3, (DH_COMPSTDB_INTSEL)arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13);
}
inline void GXDH_wrap_compute_hole_xyz(GXDHPtr self, int32_t arg1)
{
    self->compute_hole_xyz(arg1);
}
inline void GXDH_wrap_compute_sel_extent(GXDHPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    self->compute_sel_extent(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDH_wrap_compute_xyz(GXDHPtr self)
{
    self->compute_xyz();
}
inline void GXDH_wrap_convert_old_line_names(GXDBPtr arg1, GXLSTPtr arg2)
{
    GXDH::convert_old_line_names(arg1, arg2);
}
inline GXDHPtr GXDH_wrap_create(const gx_string_type& arg1)
{
    GXDHPtr ret = GXDH::create(arg1);
    return ret;
}
inline void GXDH_wrap_create_default_job(GXDHPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->create_default_job(arg1, (DH_PLOT)arg2);
}
inline GXDHPtr GXDH_wrap_create_external(const gx_string_type& arg1)
{
    GXDHPtr ret = GXDH::create_external(arg1);
    return ret;
}
inline GXDHPtr GXDH_wrap_current()
{
    GXDHPtr ret = GXDH::current();
    return ret;
}
inline void GXDH_wrap_datamine_to_csv(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXDH::datamine_to_csv(arg1, arg2);
}
inline void GXDH_wrap_delete_holes(GXDHPtr self, GXLSTPtr arg1)
{
    self->delete_holes(arg1);
}
inline void GXDH_wrap_export_file(GXDHPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->export_file(arg1, (DH_EXP)arg2);
}
inline void GXDH_wrap_export_geodatabase_lst(GXDHPtr self, GXLSTPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, str_ref& arg4, bool arg5)
{
    self->export_geodatabase_lst(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDH_wrap_export_las(GXDHPtr self, int32_t arg1, int32_t arg2, double arg3, const gx_string_type& arg4)
{
    self->export_las(arg1, arg2, arg3, arg4);
}
inline void GXDH_wrap_export_lst(GXDHPtr self, GXLSTPtr arg1, const gx_string_type& arg2, int32_t arg3)
{
    self->export_lst(arg1, arg2, (DH_EXP)arg3);
}
inline void GXDH_wrap_flush_select(GXDHPtr self)
{
    self->flush_select();
}
inline void GXDH_wrap_get_databases_vv(GXDHPtr self, GXVVPtr arg1)
{
    self->get_databases_vv(arg1);
}
inline void GXDH_wrap_get_databases_sorted_vv(GXDHPtr self, GXVVPtr arg1)
{
    self->get_databases_sorted_vv(arg1);
}
inline void GXDH_wrap_get_data_type(GXDHPtr self, GXDBPtr arg1, int_ref& arg2)
{
    self->get_data_type(arg1, (DH_DATA&)arg2);
}
inline void GXDH_wrap_get_default_section(GXDHPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    self->get_default_section(arg1, arg2, arg3, arg4, arg5);
}
inline int32_t GXDH_wrap_get_hole_group(GXDHPtr self, int32_t arg1, const gx_string_type& arg2)
{
    int32_t ret = self->get_hole_group(arg1, arg2);
    return ret;
}
inline void GXDH_wrap_get_hole_survey(GXDHPtr self, int32_t arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5)
{
    self->get_hole_survey(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDH_wrap_get_ipj(GXDHPtr self, GXIPJPtr arg1)
{
    self->get_ipj(arg1);
}
inline void GXDH_wrap_get_map_names_vv(GXDHPtr self, GXVVPtr arg1)
{
    self->get_map_names_vv(arg1);
}
inline GXMAPPtr GXDH_wrap_get_map(GXDHPtr self, int32_t arg1)
{
    GXMAPPtr ret = self->get_map(arg1);
    return ret;
}
inline int32_t GXDH_wrap_get_num_maps(GXDHPtr self)
{
    int32_t ret = self->get_num_maps();
    return ret;
}
inline GXREGPtr GXDH_wrap_get_reg(GXDHPtr self)
{
    GXREGPtr ret = self->get_reg();
    return ret;
}
inline void GXDH_wrap_get_selected_holes_vv(GXDHPtr self, GXVVPtr arg1)
{
    self->get_selected_holes_vv(arg1);
}
inline void GXDH_wrap_get_table_default_chan_lst(GXLSTPtr arg1, int32_t arg2)
{
    GXDH::get_table_default_chan_lst(arg1, (DH_DATA)arg2);
}
inline void GXDH_wrap_hole_lst(GXDHPtr self, GXLSTPtr arg1)
{
    self->hole_lst(arg1);
}
inline void GXDH_wrap_hole_lst2(GXDHPtr self, GXLSTPtr arg1)
{
    self->hole_lst2(arg1);
}
inline int32_t GXDH_wrap_add_hole(GXDHPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->add_hole(arg1);
    return ret;
}
inline int32_t GXDH_wrap_clean_will_delete_db(GXDHPtr self)
{
    int32_t ret = self->clean_will_delete_db();
    return ret;
}
inline int32_t GXDH_wrap_compositing_tool_gui(GXDHPtr self, GXMAPPtr arg1, double arg2, double arg3, double arg4)
{
    DH_COMP_CHOICE ret = self->compositing_tool_gui(arg1, arg2, arg3, arg4);
    return ret;
}
inline void GXDH_wrap_create_collar_table(const gx_string_type& arg1, int32_t arg2, str_ref& arg3)
{
    GXDH::create_collar_table(arg1, arg2, arg3);
}
inline void GXDH_wrap_create_collar_table_dir(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3, str_ref& arg4)
{
    GXDH::create_collar_table_dir(arg1, arg2, arg3, arg4);
}
inline int32_t GXDH_wrap_delete_will_delete_db(GXDHPtr self, GXLSTPtr arg1)
{
    int32_t ret = self->delete_will_delete_db(arg1);
    return ret;
}
inline int32_t GXDH_wrap_find_hole(GXDHPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->find_hole(arg1);
    return ret;
}
inline void GXDH_wrap_get_collar_table_db(GXDHPtr self, str_ref& arg1)
{
    self->get_collar_table_db(arg1);
}
inline void GXDH_wrap_get_info(GXDHPtr self, int32_t arg1, const gx_string_type& arg2, str_ref& arg3)
{
    self->get_info(arg1, arg2, arg3);
}
inline void GXDH_wrap_get_project_name(GXDHPtr self, str_ref& arg1)
{
    self->get_project_name(arg1);
}
inline void GXDH_wrap_get_section_id(double arg1, double arg2, double arg3, str_ref& arg4)
{
    GXDH::get_section_id(arg1, arg2, arg3, arg4);
}
inline int32_t GXDH_wrap_get_template_blob(GXDBPtr arg1, const gx_string_type& arg2, int_ref& arg3)
{
    int32_t ret = GXDH::get_template_blob(arg1, arg2, (DH_DATA&)arg3);
    return ret;
}
inline void GXDH_wrap_get_template_info(const gx_string_type& arg1, int_ref& arg2, str_ref& arg3, str_ref& arg4)
{
    GXDH::get_template_info(arg1, (DH_DATA&)arg2, arg3, arg4);
}
inline void GXDH_wrap_get_template_info_ex(const gx_string_type& arg1, int_ref& arg2, str_ref& arg3, str_ref& arg4, GXLSTPtr arg5)
{
    GXDH::get_template_info_ex(arg1, (DH_DATA&)arg2, arg3, arg4, arg5);
}
inline void GXDH_wrap_get_units(GXDHPtr self, str_ref& arg1, float_ref& arg2)
{
    self->get_units(arg1, arg2);
}
inline bool GXDH_wrap_have_current()
{
    bool ret = GXDH::have_current();
    return ret;
}
inline bool GXDH_wrap_have_current2(str_ref& arg1)
{
    bool ret = GXDH::have_current2(arg1);
    return ret;
}
inline int32_t GXDH_wrap_holes(GXDHPtr self)
{
    int32_t ret = self->holes();
    return ret;
}
inline int32_t GXDH_wrap_hole_select_from_list_gui(GXLSTPtr arg1, GXLSTPtr arg2)
{
    int32_t ret = GXDH::hole_select_from_list_gui(arg1, arg2);
    return ret;
}
inline int32_t GXDH_wrap_hole_selection_tool_gui(GXDHPtr self)
{
    int32_t ret = self->hole_selection_tool_gui();
    return ret;
}
inline int32_t GXDH_wrap_modify3d_gui(GXDHPtr self, const gx_string_type& arg1, int_ref& arg2)
{
    int32_t ret = self->modify3d_gui(arg1, arg2);
    return ret;
}
inline int32_t GXDH_wrap_modify_crooked_section_holes_gui(GXDHPtr self, const gx_string_type& arg1, int_ref& arg2)
{
    int32_t ret = self->modify_crooked_section_holes_gui(arg1, arg2);
    return ret;
}
inline int32_t GXDH_wrap_modify_fence_gui(GXDHPtr self, const gx_string_type& arg1, int_ref& arg2)
{
    int32_t ret = self->modify_fence_gui(arg1, (DH_SECT_PAGE&)arg2);
    return ret;
}
inline int32_t GXDH_wrap_modify_hole_traces_3dgui(GXDHPtr self, const gx_string_type& arg1, int_ref& arg2)
{
    int32_t ret = self->modify_hole_traces_3dgui(arg1, arg2);
    return ret;
}
inline int32_t GXDH_wrap_modify_hole_traces_gui(GXDHPtr self, const gx_string_type& arg1, int_ref& arg2)
{
    int32_t ret = self->modify_hole_traces_gui(arg1, arg2);
    return ret;
}
inline int32_t GXDH_wrap_modify_hole_traces_gui2(GXDHPtr self, const gx_string_type& arg1, int32_t arg2, int_ref& arg3)
{
    int32_t ret = self->modify_hole_traces_gui2(arg1, (DH_PLOT)arg2, arg3);
    return ret;
}
inline int32_t GXDH_wrap_modify_plan_gui(GXDHPtr self, const gx_string_type& arg1, int_ref& arg2)
{
    int32_t ret = self->modify_plan_gui(arg1, (DH_SECT_PAGE&)arg2);
    return ret;
}
inline int32_t GXDH_wrap_modify_plan_holes_gui(GXDHPtr self, const gx_string_type& arg1, int_ref& arg2)
{
    int32_t ret = self->modify_plan_holes_gui(arg1, arg2);
    return ret;
}
inline int32_t GXDH_wrap_modify_rock_codes_gui(const gx_string_type& arg1)
{
    int32_t ret = GXDH::modify_rock_codes_gui(arg1);
    return ret;
}
inline int32_t GXDH_wrap_modify_rock_codes_gui2(GXDBPtr arg1, const gx_string_type& arg2)
{
    int32_t ret = GXDH::modify_rock_codes_gui2(arg1, arg2);
    return ret;
}
inline int32_t GXDH_wrap_modify_section_gui(GXDHPtr self, const gx_string_type& arg1, int_ref& arg2)
{
    int32_t ret = self->modify_section_gui(arg1, (DH_SECT_PAGE&)arg2);
    return ret;
}
inline int32_t GXDH_wrap_modify_section_holes_gui(GXDHPtr self, const gx_string_type& arg1, int_ref& arg2)
{
    int32_t ret = self->modify_section_holes_gui(arg1, arg2);
    return ret;
}
inline int32_t GXDH_wrap_modify_stacked_section_gui(GXDHPtr self, const gx_string_type& arg1, int_ref& arg2)
{
    int32_t ret = self->modify_stacked_section_gui(arg1, (DH_SECT_PAGE&)arg2);
    return ret;
}
inline int32_t GXDH_wrap_modify_strip_log_gui(GXDHPtr self, const gx_string_type& arg1, int_ref& arg2)
{
    int32_t ret = self->modify_strip_log_gui(arg1, (DH_SECT_PAGE&)arg2);
    return ret;
}
inline int32_t GXDH_wrap_modify_structure_codes_gui(const gx_string_type& arg1)
{
    int32_t ret = GXDH::modify_structure_codes_gui(arg1);
    return ret;
}
inline int32_t GXDH_wrap_modify_structure_codes_gui2(GXDBPtr arg1, const gx_string_type& arg2)
{
    int32_t ret = GXDH::modify_structure_codes_gui2(arg1, arg2);
    return ret;
}
inline void GXDH_wrap_import2(const gx_string_type& arg1, GXDBPtr arg2, int32_t arg3, int32_t arg4, const gx_string_type& arg5, int32_t arg6, const gx_string_type& arg7)
{
    GXDH::import2(arg1, arg2, arg3, arg4, arg5, (DH_DATA)arg6, arg7);
}
inline void GXDH_wrap_import_las(GXDHPtr self, const gx_string_type& arg1, const gx_string_type& arg2, double arg3, int32_t arg4, GXWAPtr arg5)
{
    self->import_las(arg1, arg2, arg3, arg4, arg5);
}
inline int32_t GXDH_wrap_num_assays(GXDHPtr self)
{
    int32_t ret = self->num_assays();
    return ret;
}
inline int32_t GXDH_wrap_num_selected_holes(GXDHPtr self)
{
    int32_t ret = self->num_selected_holes();
    return ret;
}
inline int32_t GXDH_wrap_qa_dip_az_curvature_lst(GXDHPtr self, GXLSTPtr arg1, double arg2, GXWAPtr arg3)
{
    int32_t ret = self->qa_dip_az_curvature_lst(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXDH_wrap_qa_dip_az_survey_lst(GXDHPtr self, GXLSTPtr arg1, GXWAPtr arg2)
{
    int32_t ret = self->qa_dip_az_survey_lst(arg1, arg2);
    return ret;
}
inline int32_t GXDH_wrap_qa_east_north_curvature_lst(GXDHPtr self, GXLSTPtr arg1, double arg2, GXWAPtr arg3)
{
    int32_t ret = self->qa_east_north_curvature_lst(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXDH_wrap_qa_east_north_survey_lst(GXDHPtr self, GXLSTPtr arg1, GXWAPtr arg2)
{
    int32_t ret = self->qa_east_north_survey_lst(arg1, arg2);
    return ret;
}
inline int32_t GXDH_wrap_slice_selection_tool_gui(GXDHPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, float_ref& arg9, float_ref& arg10, float_ref& arg11, float_ref& arg12)
{
    int32_t ret = self->slice_selection_tool_gui(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12);
    return ret;
}
inline int32_t GXDH_wrap_update_survey_from_collar(GXDHPtr self, int32_t arg1)
{
    int32_t ret = self->update_survey_from_collar(arg1);
    return ret;
}
inline void GXDH_wrap_load_data_parameters_ini(GXDHPtr self, GXDBPtr arg1, const gx_string_type& arg2)
{
    self->load_data_parameters_ini(arg1, arg2);
}
inline void GXDH_wrap_load_plot_parameters(GXDHPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->load_plot_parameters(arg1, (DH_PLOT)arg2);
}
inline void GXDH_wrap_load_select(GXDHPtr self, const gx_string_type& arg1)
{
    self->load_select(arg1);
}
inline void GXDH_wrap_mask_ply(GXDHPtr self, GXPLYPtr arg1, GXIPJPtr arg2, double arg3, const gx_string_type& arg4, int32_t arg5, int32_t arg6)
{
    self->mask_ply(arg1, arg2, arg3, arg4, (DH_HOLES)arg5, (DH_MASK)arg6);
}
inline GXDHPtr GXDH_wrap_open(const gx_string_type& arg1)
{
    GXDHPtr ret = GXDH::open(arg1);
    return ret;
}
inline void GXDH_wrap_open_job(GXDHPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->open_job(arg1, (DH_PLOT)arg2);
}
inline void GXDH_wrap_plot_hole_traces(GXDHPtr self, GXMAPPtr arg1, const gx_string_type& arg2)
{
    self->plot_hole_traces(arg1, arg2);
}
inline void GXDH_wrap_plot_hole_traces_3d(GXDHPtr self, GXMVIEWPtr arg1, const gx_string_type& arg2)
{
    self->plot_hole_traces_3d(arg1, arg2);
}
inline void GXDH_wrap_plot_symbols_3d(GXDHPtr self, GXMVIEWPtr arg1, const gx_string_type& arg2)
{
    self->plot_symbols_3d(arg1, arg2);
}
inline void GXDH_wrap_qa_collar(GXDHPtr self, GXWAPtr arg1)
{
    self->qa_collar(arg1);
}
inline void GXDH_wrap_qa_collar_lst(GXDHPtr self, GXLSTPtr arg1, GXWAPtr arg2)
{
    self->qa_collar_lst(arg1, arg2);
}
inline void GXDH_wrap_qa_dip_az_curvature(GXDHPtr self, GXWAPtr arg1, double arg2)
{
    self->qa_dip_az_curvature(arg1, arg2);
}
inline void GXDH_wrap_qa_dip_az_curvature2(GXDHPtr self, GXWAPtr arg1, double arg2, const gx_string_type& arg3)
{
    self->qa_dip_az_curvature2(arg1, arg2, arg3);
}
inline void GXDH_wrap_qa_dip_az_survey(GXDHPtr self, GXDBPtr arg1, GXWAPtr arg2, int32_t arg3, const gx_string_type& arg4)
{
    self->qa_dip_az_survey(arg1, arg2, arg3, arg4);
}
inline void GXDH_wrap_qa_east_north_curvature(GXDHPtr self, GXWAPtr arg1, double arg2)
{
    self->qa_east_north_curvature(arg1, arg2);
}
inline void GXDH_wrap_qa_east_north_curvature2(GXDHPtr self, GXWAPtr arg1, double arg2, const gx_string_type& arg3)
{
    self->qa_east_north_curvature2(arg1, arg2, arg3);
}
inline void GXDH_wrap_qa_east_north_survey(GXDHPtr self, GXDBPtr arg1, GXWAPtr arg2, int32_t arg3, const gx_string_type& arg4)
{
    self->qa_east_north_survey(arg1, arg2, arg3, arg4);
}
inline void GXDH_wrap_qa_from_to_data(GXDHPtr self, GXDBPtr arg1, GXWAPtr arg2, int32_t arg3, const gx_string_type& arg4)
{
    self->qa_from_to_data(arg1, arg2, arg3, arg4);
}
inline void GXDH_wrap_qa_point_data(GXDHPtr self, GXDBPtr arg1, GXWAPtr arg2, int32_t arg3, const gx_string_type& arg4)
{
    self->qa_point_data(arg1, arg2, arg3, arg4);
}
inline void GXDH_wrap_qa_write_unregistered_holes(GXDHPtr self, GXDBPtr arg1, GXWAPtr arg2)
{
    self->qa_write_unregistered_holes(arg1, arg2);
}
inline void GXDH_wrap_replot_holes(GXDHPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->replot_holes(arg1, (DH_PLOT)arg2);
}
inline void GXDH_wrap_plot_holes_on_section(GXDHPtr self, const gx_string_type& arg1, int32_t arg2, const gx_string_type& arg3)
{
    self->plot_holes_on_section(arg1, (DH_PLOT)arg2, arg3);
}
inline void GXDH_wrap_re_survey_east_north(GXDHPtr self, const gx_string_type& arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, double arg6, double arg7, double arg8, double arg9, float_ref& arg10)
{
    self->re_survey_east_north(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXDH_wrap_re_survey_pol_fit(GXDHPtr self, const gx_string_type& arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10, int32_t arg11, int32_t arg12, GXVVPtr arg13, GXVVPtr arg14, GXVVPtr arg15, GXVVPtr arg16)
{
    self->re_survey_pol_fit(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, (DIP_CONVENTION)arg11, arg12, arg13, arg14, arg15, arg16);
}
inline void GXDH_wrap_re_survey_rad_curve(GXDHPtr self, const gx_string_type& arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10, int32_t arg11, GXVVPtr arg12, GXVVPtr arg13, GXVVPtr arg14, GXVVPtr arg15)
{
    self->re_survey_rad_curve(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, (DIP_CONVENTION)arg11, arg12, arg13, arg14, arg15);
}
inline void GXDH_wrap_re_survey_straight(GXDHPtr self, const gx_string_type& arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, int32_t arg10, GXVVPtr arg11, GXVVPtr arg12, GXVVPtr arg13, GXVVPtr arg14)
{
    self->re_survey_straight(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (DIP_CONVENTION)arg10, arg11, arg12, arg13, arg14);
}
inline void GXDH_wrap_re_survey_straight_seg(GXDHPtr self, const gx_string_type& arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10, int32_t arg11, GXVVPtr arg12, GXVVPtr arg13, GXVVPtr arg14, GXVVPtr arg15)
{
    self->re_survey_straight_seg(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, (DIP_CONVENTION)arg11, arg12, arg13, arg14, arg15);
}
inline void GXDH_wrap_save_data_parameters_ini(GXDHPtr self, GXDBPtr arg1, const gx_string_type& arg2)
{
    self->save_data_parameters_ini(arg1, arg2);
}
inline void GXDH_wrap_save_job(GXDHPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->save_job(arg1, (DH_PLOT)arg2);
}
inline void GXDH_wrap_save_select(GXDHPtr self, const gx_string_type& arg1)
{
    self->save_select(arg1);
}
inline void GXDH_wrap_section_window_size_mm(GXDHPtr self, float_ref& arg1, float_ref& arg2)
{
    self->section_window_size_mm(arg1, arg2);
}
inline void GXDH_wrap_select_all_holes(GXDHPtr self)
{
    self->select_all_holes();
}
inline void GXDH_wrap_select_holes(GXDHPtr self, GXVVPtr arg1, int32_t arg2)
{
    self->select_holes(arg1, arg2);
}
inline void GXDH_wrap_select_name(GXDHPtr self, const gx_string_type& arg1, int32_t arg2, int32_t arg3)
{
    self->select_name(arg1, arg2, arg3);
}
inline void GXDH_wrap_select_ply(GXDHPtr self, GXPLYPtr arg1)
{
    self->select_ply(arg1);
}
inline void GXDH_wrap_select_ply2(GXDHPtr self, GXPLYPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    self->select_ply2(arg1, arg2, arg3, arg4);
}
inline void GXDH_wrap_set_crooked_section_ipj(GXDHPtr self, GXIPJPtr arg1)
{
    self->set_crooked_section_ipj(arg1);
}
inline void GXDH_wrap_set_current_view_name(GXDHPtr self, const gx_string_type& arg1)
{
    self->set_current_view_name(arg1);
}
inline void GXDH_wrap_set_info(GXDHPtr self, int32_t arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    self->set_info(arg1, arg2, arg3);
}
inline void GXDH_wrap_set_ipj(GXDHPtr self, GXIPJPtr arg1)
{
    self->set_ipj(arg1);
}
inline void GXDH_wrap_set_map(GXDHPtr self, GXMAPPtr arg1)
{
    self->set_map(arg1);
}
inline void GXDH_wrap_set_new_ipj(GXDHPtr self, const gx_string_type& arg1)
{
    self->set_new_ipj(arg1);
}
inline void GXDH_wrap_set_selected_holes_vv(GXDHPtr self, GXVVPtr arg1, int32_t arg2)
{
    self->set_selected_holes_vv(arg1, arg2);
}
inline void GXDH_wrap_set_template_blob(GXDBPtr arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXDH::set_template_blob(arg1, arg2, (DH_DATA)arg3);
}
inline void GXDH_wrap_significant_intersections_db(GXDHPtr self, GXDBPtr arg1, GXDBPtr arg2, int32_t arg3, const gx_string_type& arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10, double arg11)
{
    self->significant_intersections_db(arg1, arg2, (DH_COMPSTDB_HOLSEL)arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXDH_wrap_test_import_las(GXDHPtr self, const gx_string_type& arg1, const gx_string_type& arg2, double arg3, GXWAPtr arg4, int_ref& arg5)
{
    self->test_import_las(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDH_wrap_un_select_all_holes(GXDHPtr self)
{
    self->un_select_all_holes();
}
inline void GXDH_wrap_un_selected_hole_lst(GXDHPtr self, GXLSTPtr arg1)
{
    self->un_selected_hole_lst(arg1);
}
inline void GXDH_wrap_update_collar_table(GXDHPtr self)
{
    self->update_collar_table();
}
inline void GXDH_wrap_update_hole_extent(GXDHPtr self, int32_t arg1)
{
    self->update_hole_extent(arg1);
}
inline void GXDH_wrap_wholeplot(GXDHPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->wholeplot(arg1, (DH_PLOT)arg2);
}
inline void GXDH_wrap_surface_intersections(GXDHPtr self, GXDBPtr arg1, const gx_string_type& arg2, int32_t arg3)
{
    self->surface_intersections(arg1, arg2, arg3);
}

void gxPythonImportGXDH()
{

    class_<GXDH, GXDHPtr> pyClass("GXDH",
                                  "\n.. parsed-literal::\n\n"
                                  "   This class is used for importing and interacting with Drill Hole\n"
                                  "   data files. For detailed information on Drill Hole data,\n"
                                  "   see the documentation for Wholeplot.\n\n"

                                  "\n\n**Note:**\n\n"

                                  "\n.. parsed-literal::\n\n"
                                  "   The DH class has some defines not used by any functions.\n"
                                  "       \\ :ref:`DH_DEFINE_PLAN`\\ \n"
                                  "       \\ :ref:`DH_DEFINE_SECT`\\ \n\n"
                                  , no_init);

    pyClass.def("null", &GXDH::null, "null() -> GXDH\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXDH`\n\n:returns: A null :class:`geosoft.gxapi.GXDH`\n:rtype: :class:`geosoft.gxapi.GXDH`\n").staticmethod("null");
    pyClass.def("is_null", &GXDH::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXDH is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXDH`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXDH::_internal_handle);
    pyClass.def("is_esri", &GXDH_wrap_is_esri,
                "is_esri() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Running inside ArcGIS?\n\n"

                ":returns: 0 - if No\n"
                "          1 - if Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               ).staticmethod("is_esri");
    pyClass.def("creat_chan_lst", &GXDH_wrap_creat_chan_lst,
                "creat_chan_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fills a LST with available string and numeric channel code values.\n\n"

                ":param arg1: LST to fill with channel code values.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Channel codes are in the format \"[Assay] Au\", where the name in\n"
                "   the square brackets is descriptive part of the project database\n"
                "   containing the given channel name. The above code might refer to\n"
                "   the \"Au\" channel in the \"Tutorial_Assay.gdb\" database.\n\n"
               );
    pyClass.def("depth_data_lst", &GXDH_wrap_depth_data_lst,
                "depth_data_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fills a LST with available channel code values from Depth databases.\n\n"

                ":param arg1: LST to fill with channel code values.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Channel codes are in the format \"[Assay] Au\", where the name in\n"
                "   the square brackets is descriptive part of the project database\n"
                "   containing the given channel name. The above code might refer to\n"
                "   the \"Au\" channel in the \"Tutorial_Assay.gdb\" database.\n\n"
               );
    pyClass.def("from_to_data_lst", &GXDH_wrap_from_to_data_lst,
                "from_to_data_lst((str)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fills a LST with available string and numeric channel code values from From-To databases.\n\n"

                ":param arg1: Assay dataset (\"\" for all)\n"
                ":type arg1: str\n"
                ":param arg2: LST to fill with channel code values.\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Channel codes are in the format \"[Assay] Au\", where the name in\n"
                "   the square brackets is descriptive part of the project database\n"
                "   containing the given channel name. The above code might refer to\n"
                "   the \"Au\" channel in the \"Tutorial_Assay.gdb\" database.\n\n"
               );
    pyClass.def("get_geology_contacts", &GXDH_wrap_get_geology_contacts,
                "get_geology_contacts((GXLST)arg1, (str)arg2, (str)arg3, (int)arg4, (float)arg5, (GXVV)arg6, (GXVV)arg7, (GXVV)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return XYZ locations of top or bottom geological surfaces\n\n"

                ":param arg1: LST of holes to check\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: Channel code\n"
                ":type arg2: str\n"
                ":param arg3: Geology item\n"
                ":type arg3: str\n"
                ":param arg4: \\ :ref:`DH_SURFACE`\\  Surface selection (top or bottom)\n"
                ":type arg4: int\n"
                ":param arg5: Max gap to skip when compositing (GS_R8DM for none)\n"
                ":type arg5: float\n"
                ":param arg6: X locations of the contact\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Y locations of the contact\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Z locations of the contact\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   For the input LST of holes, returns XYZ location of top or bottom\n"
                "   contact with the input geology. Those selected holes which do NOT\n"
                "   have contacts, return rDUMMY for the corresponding locations.\n\n"
               );
    pyClass.def("get_oriented_core_dip_dir", &GXDH_wrap_get_oriented_core_dip_dir,
                "get_oriented_core_dip_dir((GXLST)arg1, (str)arg2, (str)arg3, (int)arg4, (str)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Converted alpha/beta values in oriented cores to dip/dip direction.\n\n"

                ":param arg1: List of holes to process (e.g. from HoleLST_DH)\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: Channel code for input alpha data\n"
                ":type arg2: str\n"
                ":param arg3: Channel code for input beta data\n"
                ":type arg3: str\n"
                ":param arg4: 1: Top of core reference 0: Bottom of core reference\n"
                ":type arg4: int\n"
                ":param arg5: Channel name for output dip data\n"
                ":type arg5: str\n"
                ":param arg6: Channel name for output dip direction\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The input data are the oriented core alpha and beta values, using either\n"
                "   top or bottom reference. The values for each hole in the LST are converted\n"
                "   to \"absolute\" dip and dip-direction values, using the resurveyed hole\n"
                "   orientations at each depth.\n"
                "   The alpha and beta data must be from the same database, and the output\n"
                "   dip and dip/dir channels are written to the same database.\n\n"
               );
    pyClass.def("get_unique_channel_items", &GXDH_wrap_get_unique_channel_items,
                "get_unique_channel_items((str)arg1, (int)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return a VV with unique items in a channel.\n\n"

                ":param arg1: Channel code\n"
                ":type arg1: str\n"
                ":param arg2: Selected holes (1), All holes (0)\n"
                ":type arg2: int\n"
                ":param arg3: VV filled with items (converted to this VV type)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Finds and sorts all the unique non-dummy items for the selected channel.\n\n"
               );
    pyClass.def("get_unique_channel_items_from_collar", &GXDH_wrap_get_unique_channel_items_from_collar,
                "get_unique_channel_items_from_collar((str)arg1, (int)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return a VV with unique items in a channel.\n\n"

                ":param arg1: Channel\n"
                ":type arg1: str\n"
                ":param arg2: Selected holes (1), All holes (0)\n"
                ":type arg2: int\n"
                ":param arg3: VV filled with items (converted to this VV type)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Finds and sorts all the unique non-dummy items for the selected channel.\n\n"
               );
    pyClass.def("chan_type", &GXDH_wrap_chan_type,
                "chan_type((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the data type for a channel code.\n\n"

                ":param arg1: Channel code\n"
                ":type arg1: str\n"
                ":returns: Channel data type\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Finds and sorts all the unique non-dummy items for the selected channel.\n\n"
               );
    pyClass.def("find_hole_intersection", &GXDH_wrap_find_hole_intersection,
                "find_hole_intersection((int)arg1, (GXIMG)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return XYZ locations of the intersection of a hole with a DEM grid.\n\n"

                ":param arg1: Hole index\n"
                ":type arg1: int\n"
                ":param arg2: DEM Grid\n"
                ":type arg2: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg3: Returned X location\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Returned Y location\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Returned Z location\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 1 if intersection found\n"
                "          0 if no intersection found\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Input the hole index and an IMG object. Returns XYZ location\n"
                "   of the hole intersection with the DEM. Interpolation inside the DEM\n"
                "   uses the native IMG interp method. If no intersection is found the\n"
                "   returned XYZ locations are rDUMMY.\n\n"
               );
    pyClass.def("get_chan_code_info", &GXDH_wrap_get_chan_code_info,
                "get_chan_code_info((str)arg1, (int_ref)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the assay database index and channel name from a channel code string.\n\n"

                ":param arg1: Input channel code \"[Assay] channel\"\n"
                ":type arg1: str\n"
                ":param arg2: Returned assay database index\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: channel name\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The input channel code is in the form \"[Assay] channel\"\n\n"
               );
    pyClass.def("grid_intersection", &GXDH_wrap_grid_intersection,
                "grid_intersection((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (str)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Algorithm to determine the intersection of a straight hole with a surface (DEM) grid.\n\n"

                ":param arg1: Input location on hole X\n"
                ":type arg1: float\n"
                ":param arg2: Input location on hole Y\n"
                ":type arg2: float\n"
                ":param arg3: Input location on hole Z\n"
                ":type arg3: float\n"
                ":param arg4: Dip (positive up) in degrees\n"
                ":type arg4: float\n"
                ":param arg5: Azimuth in degrees\n"
                ":type arg5: float\n"
                ":param arg6: DEM grid\n"
                ":type arg6: str\n"
                ":param arg7: returned intersection point X\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: returned intersection point Y\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: returned intersection point Z\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 1 if an intersection is found, 0 if not.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Given a point on the hole and the straight hole dip and azimuth,\n"
                "   ocate (an) intersection point with the input DEM grid.\n\n"
               );
    pyClass.def("litho_grid_3d", &GXDH_wrap_litho_grid_3d,
                "litho_grid_3d((str)arg1, (GXTPAT)arg2, (str)arg3, (float)arg4, (float)arg5, (float)arg6, (int)arg7, (GXREG)arg8, (int)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a lithology voxel grid with lith codes mapped to single values.\n\n"

                ":param arg1: Lithology channel code\n"
                ":type arg1: str\n"
                ":param arg2: Codes, colours etc.\n"
                ":type arg2: :class:`geosoft.gxapi.GXTPAT`\n"
                ":param arg3: Name of VOX Persistent Storage file\n"
                ":type arg3: str\n"
                ":param arg4: Cell Size (GS_R8DM for automatic calculation)\n"
                ":type arg4: float\n"
                ":param arg5: Max gap to skip when compositing (GS_R8DM for none)\n"
                ":type arg5: float\n"
                ":param arg6: Non-contact radius.\n"
                ":type arg6: float\n"
                ":param arg7: Gridding type (0: Rangrid, 1: TinGrid)\n"
                ":type arg7: int\n"
                ":param arg8: Rangrid control REG (see RGRD class for parameters)\n"
                ":type arg8: :class:`geosoft.gxapi.GXREG`\n"
                ":param arg9: Retain top/bottom grids?\n"
                ":type arg9: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Values in the input channel are assigned the index of the corresponding\n"
                "   item found in the input TPAT.\n"
                "   The compositing gap refers to the size of gaps in the data (either\n"
                "   a blank lithology or missing from-to interval) which will be ignored\n"
                "   when compositing lithologies into contiguous from-to intervals.\n"
                "   The non-contact radius is used to dummy out the level grids around holes\n"
                "   where the gridded lithology is not found. If not specified (dummy) then\n"
                "   half the distance to the nearest contacting hole is used.\n\n"
               );
    pyClass.def("numeric_chan_lst", &GXDH_wrap_numeric_chan_lst,
                "numeric_chan_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fills a LST with available numeric channel code values.\n\n"

                ":param arg1: LST to fill with channel code values.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Channel codes are in the format \"[Assay] Au\", where the name in\n"
                "   the square brackets is descriptive part of the project database\n"
                "   containing the given channel name. The above code might refer to\n"
                "   the \"Au\" channel in the \"Tutorial_Assay.gdb\" database.\n\n"
               );
    pyClass.def("numeric_from_to_data_lst", &GXDH_wrap_numeric_from_to_data_lst,
                "numeric_from_to_data_lst((str)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fills a LST with available numeric channel code values from From-To databases..\n\n"

                ":param arg1: Assay dataset (\"\" for all)\n"
                ":type arg1: str\n"
                ":param arg2: LST to fill with channel code values.\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Channel codes are in the format \"[Assay] Au\", where the name in\n"
                "   the square brackets is descriptive part of the project database\n"
                "   containing the given channel name. The above code might refer to\n"
                "   the \"Au\" channel in the \"Tutorial_Assay.gdb\" database.\n\n"
               );
    pyClass.def("punch_grid_holes", &GXDH_wrap_punch_grid_holes,
                "punch_grid_holes((GXIMG)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy out locations in a grid around non-contact holes.\n\n"

                ":param arg1: DEM grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: X locations of the contacts\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y locations of the contacts\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Z locations of the contacts\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Blanking distance\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Grid is dummied out to the blanking distance around holes where\n"
                "   the input Z value is dummy. If a contacting hole is closer then\n"
                "   twice the blanking distance, the blanking distance is reduced\n"
                "   accordingly. Distances are measured horizontally (e.g. Z is ignored).\n"
                "   If the blanking distance is zero or dummy, the distance is\n"
                "   automatically set to half the distance to the closest hole intersection.\n\n"
               );
    pyClass.def("string_chan_lst", &GXDH_wrap_string_chan_lst,
                "string_chan_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fills a LST with available string channel code values.\n\n"

                ":param arg1: LST to fill with channel code values.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Channel codes are in the format \"[Assay] Au\", where the name in\n"
                "   the square brackets is descriptive part of the project database\n"
                "   containing the given channel name. The above code might refer to\n"
                "   the \"Au\" channel in the \"Tutorial_Assay.gdb\" database.\n\n"
               );
    pyClass.def("string_from_to_data_lst", &GXDH_wrap_string_from_to_data_lst,
                "string_from_to_data_lst((str)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fills a LST with available string-type channel code values from From-To databases.\n\n"

                ":param arg1: Assay dataset (\"\" for all)\n"
                ":type arg1: str\n"
                ":param arg2: LST to fill with channel code values.\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Channel codes are in the format \"[Geology] Lithology\", where the name in\n"
                "   the square brackets is descriptive part of the project database\n"
                "   containing the given channel name. The above code might refer to\n"
                "   the \"Lithology\" channel in the \"Tutorial_Geology.gdb\" database.\n\n"
               );
    pyClass.def("h_assay_db", &GXDH_wrap_h_assay_db,
                "h_assay_db((int)arg1) -> GXDB:\n"

                "\n.. parsed-literal::\n\n"
                "   Database for an assay data set.\n\n"

                ":param arg1: Assay dataset number\n"
                ":type arg1: int\n"
                ":returns: x - DB\n"
                "          \\ :func:`geosoft.gxapi.GXDB.null()`\\  if no assay data (no error registered)\n"
                ":rtype: :class:`geosoft.gxapi.GXDB`\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works for both single and multiple DB Wholeplots.\n\n"
               );
    pyClass.def("h_assay_symb", &GXDH_wrap_h_assay_symb,
                "h_assay_symb((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Line/Group symbol for a specific assay data set hole.\n\n"

                ":param arg1: Assay dataset number\n"
                ":type arg1: int\n"
                ":param arg2: hole index number\n"
                ":type arg2: int\n"
                ":returns: x - DB_SYMB\n"
                "          NULLSYMB if no survey data for this hole (no error registered)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works for both single and multiple DB Wholeplots.\n\n"
               );
    pyClass.def("h_collar_db", &GXDH_wrap_h_collar_db,
                "h_collar_db() -> GXDB:\n"

                "\n.. parsed-literal::\n\n"
                "   Database for the collar table.\n\n"

                ":returns: x - DB\n"
                "          \\ :func:`geosoft.gxapi.GXDB.null()`\\  if no collar table (no error registered)\n"
                ":rtype: :class:`geosoft.gxapi.GXDB`\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works for both single and multiple DB Wholeplots.\n\n"
               );
    pyClass.def("h_collar_symb", &GXDH_wrap_h_collar_symb,
                "h_collar_symb() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Line/Group symbol for the collar table.\n\n"

                ":returns: x - DB_SYMB\n"
                "          NULLSYMB if no collar table (no error registered)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works for both single and multiple DB Wholeplots.\n\n"
               );
    pyClass.def("h_dip_az_survey_db", &GXDH_wrap_h_dip_az_survey_db,
                "h_dip_az_survey_db() -> GXDB:\n"

                "\n.. parsed-literal::\n\n"
                "   Database for the Dip-Azimuth survey data\n\n"

                ":returns: x - DB\n"
                "          \\ :func:`geosoft.gxapi.GXDB.null()`\\  if no dip-azimuth survey data (no error registered)\n"
                ":rtype: :class:`geosoft.gxapi.GXDB`\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works for both single and multiple DB Wholeplots.\n\n"
               );
    pyClass.def("h_dip_az_survey_symb", &GXDH_wrap_h_dip_az_survey_symb,
                "h_dip_az_survey_symb((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Line/Group symbol for a specific hole Dip-Azimuth survey.\n\n"

                ":param arg1: hole index number\n"
                ":type arg1: int\n"
                ":returns: x - DB_SYMB\n"
                "          NULLSYMB if no Dip-Azimuth survey data for this hole (no error registered)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works for both single and multiple DB Wholeplots.\n\n"
               );
    pyClass.def("h_en_survey_db", &GXDH_wrap_h_en_survey_db,
                "h_en_survey_db() -> GXDB:\n"

                "\n.. parsed-literal::\n\n"
                "   Database for the East-North survey data\n\n"

                ":returns: x - DB\n"
                "          \\ :func:`geosoft.gxapi.GXDB.null()`\\  if no East-North survey data (no error registered)\n"
                ":rtype: :class:`geosoft.gxapi.GXDB`\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works for both single and multiple DB Wholeplots.\n\n"
               );
    pyClass.def("h_en_survey_symb", &GXDH_wrap_h_en_survey_symb,
                "h_en_survey_symb((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Line/Group symbol for a specific hole East-North survey.\n\n"

                ":param arg1: hole index number\n"
                ":type arg1: int\n"
                ":returns: x - DB_SYMB\n"
                "          NULLSYMB if no EN survey data for this hole (no error registered)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works for both single and multiple DB Wholeplots.\n\n"
               );
    pyClass.def("add_survey_table", &GXDH_wrap_add_survey_table,
                "add_survey_table((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a survey table for a new hole.\n\n"

                ":param arg1: Hole index\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The information is created from the collar table info.\n"
                "   If the survey info already exists, does nothing.\n\n"
               );
    pyClass.def("assay_hole_lst", &GXDH_wrap_assay_hole_lst,
                "assay_hole_lst((int)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Populate an LST with holes in an assay database\n\n"

                ":param arg1: index of the assay database\n"
                ":type arg1: int\n"
                ":param arg2: LST handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("assay_lst", &GXDH_wrap_assay_lst,
                "assay_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the LST of from-to and point assay datasets\n\n"

                ":param arg1: LST to be populated\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Assay dataset name is given as LST_ITEM_NAME\n"
                "   Assay dataset number is given as LST_ITEM_VALUE\n"
                "   Returns an empty LST if no datasets.\n\n"
               );
    pyClass.def("auto_select_holes", &GXDH_wrap_auto_select_holes,
                "auto_select_holes((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Use automatic hole selection based on slice.\n\n"

                ":param arg1: Turn on (TRUE) or off (FALSE)\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("auto_select_holes");
    pyClass.def("clean", &GXDH_wrap_clean,
                "clean() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete extraneous holes from project databases.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Removes from Project databases any lines not connected to\n"
                "   a line found in the collar table list.\n"
                "   If all the database lines would be removed, the database is\n"
                "   simply deleted.\n\n"
               );
    pyClass.def("composite_db", &GXDH_wrap_composite_db,
                "composite_db((GXDB)arg1, (GXDB)arg2, (int)arg3, (int)arg4, (float)arg5, (str)arg6, (str)arg7, (str)arg8, (float)arg9, (float)arg10, (float)arg11, (int)arg12, (str)arg13) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Make a composite database\n\n"

                ":param arg1: Input assay DB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: output composite DB object\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg3: \\ :ref:`DH_COMPSTDB_HOLSEL`\\ \n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`DH_COMPSTDB_INTSEL`\\ \n"
                ":type arg4: int\n"
                ":param arg5: fixed interval length\n"
                ":type arg5: float\n"
                ":param arg6: name of lithology cannel\n"
                ":type arg6: str\n"
                ":param arg7: name of interval file\n"
                ":type arg7: str\n"
                ":param arg8: name of Weight channel\n"
                ":type arg8: str\n"
                ":param arg9: dRej1Val for intervals short than, (GS_R8DM for no action)\n"
                ":type arg9: float\n"
                ":param arg10: dRej2Val for intervals gap greater than, (GS_R8DM for no action)\n"
                ":type arg10: float\n"
                ":param arg11: dRej3Val for Rej3Ch with Rej3Op, (GS_R8DM for no action)\n"
                ":type arg11: float\n"
                ":param arg12: dRej3Op: 0: >, 1: >=, 2: <, 3: <=\n"
                ":type arg12: int\n"
                ":param arg13: name of Rej3Ch channel\n"
                ":type arg13: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               );
    pyClass.def("compute_hole_xyz", &GXDH_wrap_compute_hole_xyz,
                "compute_hole_xyz((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Computes XYZ for survey and assay data for a single hole.\n\n"

                ":param arg1: Hole index\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"
               );
    pyClass.def("compute_sel_extent", &GXDH_wrap_compute_sel_extent,
                "compute_sel_extent((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Computes the extents for selected holes.\n\n"

                ":param arg1: East Min\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: East Max\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: North Min\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: North Max\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Elev Min\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Elev Max\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("compute_xyz", &GXDH_wrap_compute_xyz,
                "compute_xyz() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Computes XYZ for survey and assay data.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("convert_old_line_names", &GXDH_wrap_convert_old_line_names,
                "convert_old_line_names((GXDB)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert old \"DD001.Assay\" type lines to \"DD001\"\n\n"

                ":param arg1: DH object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Names to convert (call SymbLST_DB).\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The input LST must be filled using a function like \\ :func:`geosoft.gxapi.GXDB.symb_lst`\\ , which\n"
                "   puts the name and symbol into the LST items.\n"
                "   Any names with a period are truncated at the period, and\n"
                "   the line name in the database is changed to the new name\n"
                "   (just the hole name).\n"
                "   The LST is modified to have the new names.\n"
                "   A value is put into the DB REG \"DH_CONVERTED_NAMES\" parameter so\n"
                "   this process is done only once on a database.\n"
                "   \n"
                "   DO NOT use on old-style single-database Wholeplot projects.\n\n"
               ).staticmethod("convert_old_line_names");
    pyClass.def("create", &GXDH_wrap_create,
                "create((str)arg1) -> GXDH:\n"

                "\n.. parsed-literal::\n\n"
                "   Create DH.\n\n"

                ":param arg1: Name of current database\n"
                ":type arg1: str\n"
                ":returns: DH Object\n"
                ":rtype: :class:`geosoft.gxapi.GXDH`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_default_job", &GXDH_wrap_create_default_job,
                "create_default_job((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a default job from scratch.\n\n"

                ":param arg1: File name of the INI file to create (forces correct suffix)\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_PLOT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("create_external", &GXDH_wrap_create_external,
                "create_external((str)arg1) -> GXDH:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a DH from an external process (no montaj running).\n\n"

                ":param arg1: Name of example project database\n"
                ":type arg1: str\n"
                ":returns: DH Object\n"
                ":rtype: :class:`geosoft.gxapi.GXDH`\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The regular \\ :func:`geosoft.gxapi.GXDH.create`\\  assumes a workspace is open and creates\n"
                "   the project from the databases which are currently loaded.\n"
                "   This function instead creates the project from all projects\n"
                "   in the input databases's directory.\n\n"
               ).staticmethod("create_external");
    pyClass.def("current", &GXDH_wrap_current,
                "current() -> GXDH:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a drill project from current environment.\n\n"

                ":returns: DH Object\n"
                ":rtype: :class:`geosoft.gxapi.GXDH`\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If no DH database is open the Open DH Project GUI will be displayed which may be\n"
                "   cancelled by the user in which case the GX will terminate with cancel.\n\n"
               ).staticmethod("current");
    pyClass.def("datamine_to_csv", &GXDH_wrap_datamine_to_csv,
                "datamine_to_csv((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a Datamine drillhole file to CSV files ready for import.\n\n"

                ":param arg1: Datamine database file to import (\\ `*`\\ .dm)\n"
                ":type arg1: str\n"
                ":param arg2: Drillhole project name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Creates three CSV files and the accompanying template files\n"
                "   ready for batch ASCII import into a drill project.\n"
                "      Project_Collar.csv, .i3\n"
                "      Project_Survey.csv, .i3\n"
                "      Project_Assay.csv,  .i3\n\n"
               ).staticmethod("datamine_to_csv");
    pyClass.def("delete_holes", &GXDH_wrap_delete_holes,
                "delete_holes((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete a list of holes from the project.\n\n"

                ":param arg1: LST of holes to delete\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Removes all lines in the input LST from DH project databases.\n"
                "   If all the database lines would be removed, the database is\n"
                "   simply deleted.\n\n"
               );
    pyClass.def("export_file", &GXDH_wrap_export_file,
                "export_file((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Exports a Drill Hole database to an external file.\n\n"

                ":param arg1: File name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_EXP`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("export_geodatabase_lst", &GXDH_wrap_export_geodatabase_lst,
                "export_geodatabase_lst((GXLST)arg1, (str)arg2, (str)arg3, (str_ref)arg4, (bool)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Exports whole or part of a Drill Hole database to an ArcGIS Geodatabase as feature class(es).\n\n"

                ":param arg1: Hole Names in the Name and Value parts of the LST\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: File name (.pdb folder for File Geodatabase or .sde connector for SDE)\n"
                ":type arg2: str\n"
                ":param arg3: String to prefix dataset names with\n"
                ":type arg3: str\n"
                ":param arg4: Feature class name to export (pass empty for all or name of table, will contain the name of the output dataset for if a rename occurs)\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: bool Overwrite existing feature classes? Pass ``False`` to create copies.\n"
                ":type arg5: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   A table with metadata about the created feature classes will be written to the Geodatabase. This table will have the same\n"
                "   name with the postfix \"_Metadata\" attached\n\n"
               );
    pyClass.def("export_las", &GXDH_wrap_export_las,
                "export_las((int)arg1, (int)arg2, (float)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Exports a Drill Hole database to a LAS v2 file.\n\n"

                ":param arg1: Assay database index\n"
                ":type arg1: int\n"
                ":param arg2: Hole index\n"
                ":type arg2: int\n"
                ":param arg3: Interval for output\n"
                ":type arg3: float\n"
                ":param arg4: File name\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               );
    pyClass.def("export_lst", &GXDH_wrap_export_lst,
                "export_lst((GXLST)arg1, (str)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Exports a LST of holes in a Drill Hole database to an external file.\n\n"

                ":param arg1: Hole Names in the Name and Value parts of the LST\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: File name\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`DH_EXP`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Use functions like \\ :func:`geosoft.gxapi.GXDB.selected_line_lst`\\  to construct the LST\n\n"
               );
    pyClass.def("flush_select", &GXDH_wrap_flush_select,
                "flush_select() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Flush all selections to database selection engine.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_databases_vv", &GXDH_wrap_get_databases_vv,
                "get_databases_vv((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the names of the project databases in a VV.\n\n"

                ":param arg1: VV of type -STR_FILE\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("get_databases_sorted_vv", &GXDH_wrap_get_databases_sorted_vv,
                "get_databases_sorted_vv((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the names of the project databases in a VV, same as \\ :func:`geosoft.gxapi.GXDH.get_databases_vv`\\  but the list is sorted alphabetically.\n\n"

                ":param arg1: VV of type -STR_FILE\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"
               );
    pyClass.def("get_data_type", &GXDH_wrap_get_data_type,
                "get_data_type((GXDB)arg1, (int_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the type of data in a Wholeplot database.\n\n"

                ":param arg1: DB Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: \\ :ref:`DH_DATA`\\ \n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Returns DH_DATA_UNKNOWN if it can't determine the type.\n\n"
               );
    pyClass.def("get_default_section", &GXDH_wrap_get_default_section,
                "get_default_section((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Computes default section azimuths, extents for selected holes.\n\n"

                ":param arg1: azimuth of section (returned)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: corner X (Easting) of section (returned)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: corner Y (Northing) of section (returned)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: section length (returned)\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: section width (returned)\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_hole_group", &GXDH_wrap_get_hole_group,
                "get_hole_group((int)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Group symbol for this hole/table combination.\n\n"

                ":param arg1: Hole index\n"
                ":type arg1: int\n"
                ":param arg2: Table Name\n"
                ":type arg2: str\n"
                ":returns: Hole Symbol\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_hole_survey", &GXDH_wrap_get_hole_survey,
                "get_hole_survey((int)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Survey information of a Hole.\n\n"

                ":param arg1: Hole index\n"
                ":type arg1: int\n"
                ":param arg2: X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Z\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Depth\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_ipj", &GXDH_wrap_get_ipj,
                "get_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the project IPJ.\n\n"

                ":param arg1: IPJ Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The projection for the project is the projection stored\n"
                "   in the DH_EAST channel in the collar table.\n\n"
               );
    pyClass.def("get_map_names_vv", &GXDH_wrap_get_map_names_vv,
                "get_map_names_vv((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get plotted map names.\n\n"

                ":param arg1: returned map names (string type VV)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This will return the currently plotted map name(s)\n"
                "   in a VV. This should only be called after a call\n"
                "   to \\ :func:`geosoft.gxapi.GXDH.wholeplot`\\ . The VV size is set to the number\n"
                "   of maps created.\n\n"
               );
    pyClass.def("get_map", &GXDH_wrap_get_map,
                "get_map((int)arg1) -> GXMAP:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a plotting map\n\n"

                ":param arg1: Map Index\n"
                ":type arg1: int\n"
                ":returns: MAP Object\n"
                ":rtype: :class:`geosoft.gxapi.GXMAP`\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"
               );
    pyClass.def("get_num_maps", &GXDH_wrap_get_num_maps,
                "get_num_maps() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number plotting maps\n\n"

                ":returns: Number of plotting maps\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"
               );
    pyClass.def("get_reg", &GXDH_wrap_get_reg,
                "get_reg() -> GXREG:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the REG Object used in this project.\n\n"

                ":returns: REG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXREG`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_selected_holes_vv", &GXDH_wrap_get_selected_holes_vv,
                "get_selected_holes_vv((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Populate a VV with the indices of all selected holes\n\n"

                ":param arg1: Returned hole indices (must be type INT)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               );
    pyClass.def("get_table_default_chan_lst", &GXDH_wrap_get_table_default_chan_lst,
                "get_table_default_chan_lst((GXLST)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return list of default channels by collar/assay/survey table type.\n\n"

                ":param arg1: LST handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`DH_DATA`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Fills a LST with the default channel names created according to\n"
                "   type (Collar, Survey, Assay). Value is in the LST_ITEM_NAME part.\n\n"
               ).staticmethod("get_table_default_chan_lst");
    pyClass.def("hole_lst", &GXDH_wrap_hole_lst,
                "hole_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Populate an LST with the list of the selected holes\n\n"

                ":param arg1: LST handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("hole_lst2", &GXDH_wrap_hole_lst2,
                "hole_lst2((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Populate an LST with the list of all the holes\n\n"

                ":param arg1: LST handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("add_hole", &GXDH_wrap_add_hole,
                "add_hole((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a hole and return it's index.\n\n"

                ":param arg1: Name of hole\n"
                ":type arg1: str\n"
                ":returns: x  - Hole index\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("clean_will_delete_db", &GXDH_wrap_clean_will_delete_db,
                "clean_will_delete_db() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   See if \"cleaning\" will delete project databases.\n\n"

                ":returns: 1 if calling Clean_DH will remove all \"lines\" from\n"
                "              one of the DH project databases.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("compositing_tool_gui", &GXDH_wrap_compositing_tool_gui,
                "compositing_tool_gui((GXMAP)arg1, (float)arg2, (float)arg3, (float)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Annotate a strip log map using the compositing tool.\n\n"

                ":param arg1: Current strip log map\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: X location on map of selected strip\n"
                ":type arg2: float\n"
                ":param arg3: Y End of hole interval in view coords\n"
                ":type arg3: float\n"
                ":param arg4: Y Other end of hole interval in view coords\n"
                ":type arg4: float\n"
                ":returns: \\ :ref:`DH_COMP_CHOICE`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If any of the input X or Y values are dummies the tool uses default values.\n\n"
               );
    pyClass.def("create_collar_table", &GXDH_wrap_create_collar_table,
                "create_collar_table((str)arg1, (int)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a collar table DB with channels set up.\n\n"

                ":param arg1: Project name\n"
                ":type arg1: str\n"
                ":param arg2: Number of channels\n"
                ":type arg2: int\n"
                ":param arg3: Collar table name (returned)\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The database name will be of the form\n"
                "   \n"
                "   \"d:\\directory\\Project_Collar.gdb\"\n\n"
               ).staticmethod("create_collar_table");
    pyClass.def("create_collar_table_dir", &GXDH_wrap_create_collar_table_dir,
                "create_collar_table_dir((str)arg1, (str)arg2, (int)arg3, (str_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a collar table in the specified directory.\n\n"

                ":param arg1: Project name\n"
                ":type arg1: str\n"
                ":param arg2: Directory to create project in\n"
                ":type arg2: str\n"
                ":param arg3: Number of channels\n"
                ":type arg3: int\n"
                ":param arg4: Collar table name (returned)\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The database name will be of the form\n"
                "   \n"
                "   \"d:\\directory\\Project_Collar.gdb\"\n\n"
               ).staticmethod("create_collar_table_dir");
    pyClass.def("delete_will_delete_db", &GXDH_wrap_delete_will_delete_db,
                "delete_will_delete_db((GXLST)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   See if deleting holes will delete project databases.\n\n"

                ":param arg1: LST of holes to delete\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: 1 if deleting the LST of holes will remove all \"lines\" from\n"
                "          one of the DH project databases.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("find_hole", &GXDH_wrap_find_hole,
                "find_hole((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Find a hole and return it's index.\n\n"

                ":param arg1: Name of hole\n"
                ":type arg1: str\n"
                ":returns: x  - Hole index\n"
                "          -1 - Not found\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_collar_table_db", &GXDH_wrap_get_collar_table_db,
                "get_collar_table_db((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the name of the database containing the collar table.\n\n"

                ":param arg1: returned file name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("get_info", &GXDH_wrap_get_info,
                "get_info((int)arg1, (str)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get Collar Information.\n\n"

                ":param arg1: hole index\n"
                ":type arg1: int\n"
                ":param arg2: Name of information\n"
                ":type arg2: str\n"
                ":param arg3: buffer to place information\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the DH_ELEV channel is requested it will also\n"
                "   search for the DH_RL channel, which is the new\n"
                "   name for the collar elevation.\n\n"
               );
    pyClass.def("get_project_name", &GXDH_wrap_get_project_name,
                "get_project_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Wholeplot project name.\n\n"

                ":param arg1: returned string\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("get_section_id", &GXDH_wrap_get_section_id,
                "get_section_id((float)arg1, (float)arg2, (float)arg3, (str_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a section ID based on its location\n\n"

                ":param arg1: Section Azimuth\n"
                ":type arg1: float\n"
                ":param arg2: Section Easting\n"
                ":type arg2: float\n"
                ":param arg3: Section Northing\n"
                ":type arg3: float\n"
                ":param arg4: Section ID\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               ).staticmethod("get_section_id");
    pyClass.def("get_template_blob", &GXDH_wrap_get_template_blob,
                "get_template_blob((GXDB)arg1, (str)arg2, (int_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve the import template from the database.\n\n"

                ":param arg1: DB Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Name of template file to extract to.\n"
                ":type arg2: str\n"
                ":param arg3: The stored import template type \\ :ref:`DH_DATA`\\ \n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0: No template stored in the database\n"
                "          1: Template retrieved and written to a file.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The template can be retrieved in order to refresh the\n"
                "   database with a call to the DHIMPORT.GX.\n"
                "   \n"
                "   The import types correspond to the DHIMPORT.IMPTYPE variable:\n"
                "   0: ASCII, 1: Database/XLS, 2: ODBC\n"
                "   \n"
                "   If no template blob exists, templ\n\n"
               ).staticmethod("get_template_blob");
    pyClass.def("get_template_info", &GXDH_wrap_get_template_info,
                "get_template_info((str)arg1, (int_ref)arg2, (str_ref)arg3, (str_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve the file, DH Table name and type from an import template.\n\n"

                ":param arg1: Template name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_DATA`\\ \n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: File name (blank for ODBC, or undefined).\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Table name (blank for DH_DATA_UNKNOWN, or undefined).\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   As of version 6.0, the import templates (\\ `*`\\ .i3, \\ `*`\\ .i4) produced\n"
                "   by the Wholeplot import wizards contain the following lines:\n"
                "   \n"
                "    FILE assay.txt  (except for ODBC)\n"
                "    DRILLTYPE 3\n"
                "    DRILLTABLE Assay\n"
                "   \n"
                "   The FILE is normally the input file name, except for ODBC, where it\n"
                "   is not defined.\n"
                "   The DRILLTYPE is one of DH_DATA_XXX, and the DRILLTABLE\n"
                "   is the name of the Wholeplot database table; e.g. Project_Assay.gdb\n"
                "   in the above case. The DRILLTABLE is only included in the template\n"
                "   for DH_DATA_FROMTO and DH_DATA_POINT, but this function will\n"
                "   return the appropriate table names (e.g. Collar, Survey, ENSurvey)\n"
                "   for the other types.\n"
                "   If the DRILLTYPE is NOT found in the template, a value of\n"
                "   DH_DATA_UNKNOWN is returned for the data type; likely an indication that this\n"
                "   is not a new-style template produced by Wholeplot.\n\n"
               ).staticmethod("get_template_info");
    pyClass.def("get_template_info_ex", &GXDH_wrap_get_template_info_ex,
                "get_template_info_ex((str)arg1, (int_ref)arg2, (str_ref)arg3, (str_ref)arg4, (GXLST)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve the file, DH Table name, type and channel list from an import template.\n\n"

                ":param arg1: Template name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_DATA`\\ \n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: File name (blank for ODBC, or undefined).\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Table name (blank for DH_DATA_UNKNOWN, or undefined).\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: Channel list (returned)\n"
                ":type arg5: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   As of version 6.0, the import templates (\\ `*`\\ .i3, \\ `*`\\ .i4) produced\n"
                "   by the Wholeplot import wizards contain the following lines:\n"
                "   \n"
                "    FILE assay.txt  (except for ODBC)\n"
                "    DRILLTYPE 3\n"
                "    DRILLTABLE Assay\n"
                "   \n"
                "   The FILE is normally the input file name, except for ODBC, where it\n"
                "   is not defined.\n"
                "   The DRILLTYPE is one of DH_DATA_XXX, and the DRILLTABLE\n"
                "   is the name of the Wholeplot database table; e.g. Project_Assay.gdb\n"
                "   in the above case. The DRILLTABLE is only included in the template\n"
                "   for DH_DATA_FROMTO and DH_DATA_POINT, but this function will\n"
                "   return the appropriate table names (e.g. Collar, Survey, ENSurvey)\n"
                "   for the other types.\n"
                "   If the DRILLTYPE is NOT found in the template, a value of\n"
                "   DH_DATA_UNKNOWN is returned for the data type; likely an indication that this\n"
                "   is not a new-style template produced by Wholeplot.\n"
                "   This version also returns a list of the channels in the template checks can be made to\n"
                "   see if the import will exceed the database channel limit.\n\n"
               ).staticmethod("get_template_info_ex");
    pyClass.def("get_units", &GXDH_wrap_get_units,
                "get_units((str_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the positional units and conversion factor to m.\n\n"

                ":param arg1: Units (i.e. \"m\")\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: conversion (units/m)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("have_current", &GXDH_wrap_have_current,
                "have_current() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns true if a drill project is loaded\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               ).staticmethod("have_current");
    pyClass.def("have_current2", &GXDH_wrap_have_current2,
                "have_current2((str_ref)arg1) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns true if a drill project is loaded, and the collar database if it is loaded.\n\n"

                ":param arg1: Collar table name (returned)\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               ).staticmethod("have_current2");
    pyClass.def("holes", &GXDH_wrap_holes,
                "holes() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return number of holes.\n\n"

                ":returns: x  - Number of holes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("hole_select_from_list_gui", &GXDH_wrap_hole_select_from_list_gui,
                "hole_select_from_list_gui((GXLST)arg1, (GXLST)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Select/Deselect holes using the two-panel selection tool.\n\n"

                ":param arg1: All holes\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: Selected holes\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: 0  - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("hole_select_from_list_gui");
    pyClass.def("hole_selection_tool_gui", &GXDH_wrap_hole_selection_tool_gui,
                "hole_selection_tool_gui() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Select/Deselect holes using plan map tool.\n\n"

                ":returns: 0  - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               );
    pyClass.def("modify3d_gui", &GXDH_wrap_modify3d_gui,
                "modify3d_gui((str)arg1, (int_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify parameters for a 3D plot.\n\n"

                ":param arg1: Job Name   (\\ `*`\\ .in3)\n"
                ":type arg1: str\n"
                ":param arg2: Page to open GUI on\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("modify_crooked_section_holes_gui", &GXDH_wrap_modify_crooked_section_holes_gui,
                "modify_crooked_section_holes_gui((str)arg1, (int_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify parameters to replot holes and hole data to an existing crooked section map.\n\n"

                ":param arg1: Job Name (\\ `*`\\ .ins)\n"
                ":type arg1: str\n"
                ":param arg2: Tab page ID.\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Will plot to an empty crooked section.\n\n"
               );
    pyClass.def("modify_fence_gui", &GXDH_wrap_modify_fence_gui,
                "modify_fence_gui((str)arg1, (int_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify parameters for a section plot.\n\n"

                ":param arg1: Job Name (\\ `*`\\ .ins)\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_SECT_PAGE`\\ \n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          1 - Interactively define a fence.\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The fence section function.\n\n"
               );
    pyClass.def("modify_hole_traces_3dgui", &GXDH_wrap_modify_hole_traces_3dgui,
                "modify_hole_traces_3dgui((str)arg1, (int_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify parameters for a hole traces plot to an existing 3D view.\n\n"

                ":param arg1: Job Name\n"
                ":type arg1: str\n"
                ":param arg2: Page to open GUI on\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               );
    pyClass.def("modify_hole_traces_gui", &GXDH_wrap_modify_hole_traces_gui,
                "modify_hole_traces_gui((str)arg1, (int_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify parameters for a hole traces plot to a current map.\n\n"

                ":param arg1: Job Name\n"
                ":type arg1: str\n"
                ":param arg2: Page to open GUI on\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("modify_hole_traces_gui2", &GXDH_wrap_modify_hole_traces_gui2,
                "modify_hole_traces_gui2((str)arg1, (int)arg2, (int_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify parameters for a hole traces plot to a current plan or section view.\n\n"

                ":param arg1: Job Name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_PLOT`\\  One of DH_PLOT_PLAN or DH_PLOT_SECTION\n"
                ":type arg2: int\n"
                ":param arg3: Page to open GUI on\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          					 -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Currently supports DH_PLOT_PLAN and DH_PLOT_SECTION\n\n"
               );
    pyClass.def("modify_plan_gui", &GXDH_wrap_modify_plan_gui,
                "modify_plan_gui((str)arg1, (int_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify parameters for a plan plot.\n\n"

                ":param arg1: Job Name (\\ `*`\\ .inp)\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_SECT_PAGE`\\ \n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("modify_plan_holes_gui", &GXDH_wrap_modify_plan_holes_gui,
                "modify_plan_holes_gui((str)arg1, (int_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify parameters to replot holes and hole data to an existing plan map.\n\n"

                ":param arg1: Job Name (\\ `*`\\ .ins)\n"
                ":type arg1: str\n"
                ":param arg2: Tab Page ID\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Modifies only hole trace, hole data, topo, voxel slice data.\n\n"
               );
    pyClass.def("modify_rock_codes_gui", &GXDH_wrap_modify_rock_codes_gui,
                "modify_rock_codes_gui((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify/create a rock codes file.\n\n"

                ":param arg1: File name\n"
                ":type arg1: str\n"
                ":returns: 0 - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               ).staticmethod("modify_rock_codes_gui");
    pyClass.def("modify_rock_codes_gui2", &GXDH_wrap_modify_rock_codes_gui2,
                "modify_rock_codes_gui2((GXDB)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify/create a rock codes file, channel population option.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: File name\n"
                ":type arg2: str\n"
                ":returns: 0 - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Same as above, but passes the current database so that\n"
                "   the \"Populate from channel\" button can be used to\n"
                "   automatically populate the rock code list. The database\n"
                "   should be a Wholeplot database.\n\n"
               ).staticmethod("modify_rock_codes_gui2");
    pyClass.def("modify_section_gui", &GXDH_wrap_modify_section_gui,
                "modify_section_gui((str)arg1, (int_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify parameters for a section plot.\n\n"

                ":param arg1: Job Name (\\ `*`\\ .ins)\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_SECT_PAGE`\\ \n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          1 - Interactively define a NS section\n"
                "          2 - Interactively define an EW section\n"
                "          3 - Interactively define an angled section\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The stacked section function uses the same control file\n"
                "   format, but the plotting of profiles and plan views is\n"
                "   disabled, and if multiple sections are requested, they\n"
                "   are plotted in a stack on the left side of the same map,\n"
                "   not to individual maps.\n\n"
               );
    pyClass.def("modify_section_holes_gui", &GXDH_wrap_modify_section_holes_gui,
                "modify_section_holes_gui((str)arg1, (int_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify parameters to replot holes and hole data to an existing section map.\n\n"

                ":param arg1: Job Name (\\ `*`\\ .ins)\n"
                ":type arg1: str\n"
                ":param arg2: Tab page ID.\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works for both regular and stacked sections.\n"
                "   Modifies only hole trace, hole data, topo, voxel slice data.\n\n"
               );
    pyClass.def("modify_stacked_section_gui", &GXDH_wrap_modify_stacked_section_gui,
                "modify_stacked_section_gui((str)arg1, (int_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify parameters for a section plot.\n\n"

                ":param arg1: Job Name (\\ `*`\\ .ins)\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_SECT_PAGE`\\ \n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          1 - Interactively define a NS section\n"
                "          2 - Interactively define an EW section\n"
                "          3 - Interactively define an angled section\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The stacked section function uses the same control file\n"
                "   format, but the plotting of profiles and plan views is\n"
                "   disabled, and if multiple sections are requested, they\n"
                "   are plotted in a stack on the left side of the same map,\n"
                "   not to individual maps.\n\n"
               );
    pyClass.def("modify_strip_log_gui", &GXDH_wrap_modify_strip_log_gui,
                "modify_strip_log_gui((str)arg1, (int_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify parameters for a strip log plot.\n\n"

                ":param arg1: Job Name   (\\ `*`\\ .inl)\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_SECT_PAGE`\\ \n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );
    pyClass.def("modify_structure_codes_gui", &GXDH_wrap_modify_structure_codes_gui,
                "modify_structure_codes_gui((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify/create a structure codes file.\n\n"

                ":param arg1: File name\n"
                ":type arg1: str\n"
                ":returns: 0 - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               ).staticmethod("modify_structure_codes_gui");
    pyClass.def("modify_structure_codes_gui2", &GXDH_wrap_modify_structure_codes_gui2,
                "modify_structure_codes_gui2((GXDB)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify/create a structure codes file, channel population option.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: File name\n"
                ":type arg2: str\n"
                ":returns: 0 - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Same as above, but passes the current database so that\n"
                "   the \"Populate from channel\" button can be used to\n"
                "   automatically populate the structure code list. The database\n"
                "   should be a Wholeplot database.\n\n"
               ).staticmethod("modify_structure_codes_gui2");
    pyClass.def("import2", &GXDH_wrap_import2,
                "import2((str)arg1, (GXDB)arg2, (int)arg3, (int)arg4, (str)arg5, (int)arg6, (str)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports data into a Drill Hole Database (obsolete).\n\n"

                ":param arg1: Drill project name\n"
                ":type arg1: str\n"
                ":param arg2: DB Handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg3: Line\n"
                ":type arg3: int\n"
                ":param arg4: Hole channel\n"
                ":type arg4: int\n"
                ":param arg5: Table\n"
                ":type arg5: str\n"
                ":param arg6: \\ :ref:`DH_DATA`\\ \n"
                ":type arg6: int\n"
                ":param arg7: Log file name\n"
                ":type arg7: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("import2");
    pyClass.def("import_las", &GXDH_wrap_import_las,
                "import_las((str)arg1, (str)arg2, (float)arg3, (int)arg4, (GXWA)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports LAS Data into a DH database\n\n"

                ":param arg1: Assay database to use\n"
                ":type arg1: str\n"
                ":param arg2: LAS file name\n"
                ":type arg2: str\n"
                ":param arg3: Averaging/desampling interval (cm)\n"
                ":type arg3: float\n"
                ":param arg4: Interpolation method\n"
                ":type arg4: int\n"
                ":param arg5: Log file handle\n"
                ":type arg5: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The argument for the assay database is the file name\n"
                "   without the project name and underscore, e.g. for\n"
                "   \"Project_Assay.gdb\" use \"Assay\"\n\n"
               );
    pyClass.def("num_assays", &GXDH_wrap_num_assays,
                "num_assays() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Number of assay datasets.\n\n"

                ":returns: The number of assay datasets.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works for both single and multiple DB Wholeplots.\n\n"
               );
    pyClass.def("num_selected_holes", &GXDH_wrap_num_selected_holes,
                "num_selected_holes() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns number of selected holes.\n\n"

                ":returns: The number of selected holes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("qa_dip_az_curvature_lst", &GXDH_wrap_qa_dip_az_curvature_lst,
                "qa_dip_az_curvature_lst((GXLST)arg1, (float)arg2, (GXWA)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Do QA/QC Curvature checking on Dip Azimuth data for holes in a LST.\n\n"

                ":param arg1: LST of holes (name, index)\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: Dip/Azimuth curvature tolerance (degree per meter)\n"
                ":type arg2: float\n"
                ":param arg3: WA Handle to write to\n"
                ":type arg3: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: The number of holes found and checked.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Checks all holes with Dip-Azimuth survey data\n\n"
               );
    pyClass.def("qa_dip_az_survey_lst", &GXDH_wrap_qa_dip_az_survey_lst,
                "qa_dip_az_survey_lst((GXLST)arg1, (GXWA)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Do QA/QC on Dip/Az Survey data for holes in a LST.\n\n"

                ":param arg1: LST of holes (Name, Index)\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: WA Handle to write to\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: The number of holes found and checked.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Error if no Dip-Azimuth survey database, or if\n"
                "   a requested hole does not exist in the drill project.\n\n"
               );
    pyClass.def("qa_east_north_curvature_lst", &GXDH_wrap_qa_east_north_curvature_lst,
                "qa_east_north_curvature_lst((GXLST)arg1, (float)arg2, (GXWA)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Do QA/QC Curvature checking on Dip Azimuth data for holes in a LST.\n\n"

                ":param arg1: LST of holes (name, index)\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: Dip/Azimuth curvature tolerance (degree per meter)\n"
                ":type arg2: float\n"
                ":param arg3: WA Handle\n"
                ":type arg3: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: The number of holes found and checked.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Checks all holes with East-North survey data\n\n"
               );
    pyClass.def("qa_east_north_survey_lst", &GXDH_wrap_qa_east_north_survey_lst,
                "qa_east_north_survey_lst((GXLST)arg1, (GXWA)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Do QA/QC on East/North Survey data for holes in a LST.\n\n"

                ":param arg1: LST of holes (Name, Index)\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: WA Handle to write to\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: The number of holes found and checked.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Error if no East-North survey database, or if\n"
                "   a requested hole does not exist in the drill project.\n\n"
               );
    pyClass.def("slice_selection_tool_gui", &GXDH_wrap_slice_selection_tool_gui,
                "slice_selection_tool_gui((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float_ref)arg9, (float_ref)arg10, (float_ref)arg11, (float_ref)arg12) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Select a slice with the holes in context. An optional 4 point area of interest (AOI) can be added to be represented in the UI too.\n\n"

                ":param arg1: 1st Corner of AOI - X\n"
                ":type arg1: float\n"
                ":param arg2: 1st Corner of AOI - Y\n"
                ":type arg2: float\n"
                ":param arg3: 2nd Corner of AOI - X\n"
                ":type arg3: float\n"
                ":param arg4: 2nd Corner of AOI - Y\n"
                ":type arg4: float\n"
                ":param arg5: 3rd Corner of AOI - X\n"
                ":type arg5: float\n"
                ":param arg6: 3rd Corner of AOI - Y\n"
                ":type arg6: float\n"
                ":param arg7: 4th Corner of AOI - X\n"
                ":type arg7: float\n"
                ":param arg8: 4th Corner of AOI - Y\n"
                ":type arg8: float\n"
                ":param arg9: Returned slice 1st point - X\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: Returned slice 1st point - Y\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: Returned slice 2nd point - X\n"
                ":type arg11: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg12: Returned slice 2nd point - Y\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0  - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("update_survey_from_collar", &GXDH_wrap_update_survey_from_collar,
                "update_survey_from_collar((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Update the Survey table from the collar info.\n\n"

                ":param arg1: hole index\n"
                ":type arg1: int\n"
                ":returns: 0 - No change; there is no survey table, the table was empty, or values were same as collar\n"
                "          1 - Survey table updated; values changed and there is just one row.\n"
                "          2 - Survey table unchanged; there was more than one row in the table, and values were different\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Call when the collar values are edited to update the survey table\n"
                "   values. If the survey contains more than one row, then no changes\n"
                "   are applied, and no warning or error is registered.\n\n"
               );
    pyClass.def("load_data_parameters_ini", &GXDH_wrap_load_data_parameters_ini,
                "load_data_parameters_ini((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load data parameters from INI files..\n\n"

                ":param arg1: Source database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Directory to store INI files\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Wholeplot data graphing parameters for each channel are stored\n"
                "   in the channel REG. This function lets a user transfer pre-defined\n"
                "   settings to individual INI files (eg. cu.ini).\n\n"
               );
    pyClass.def("load_plot_parameters", &GXDH_wrap_load_plot_parameters,
                "load_plot_parameters((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load parameters from a Job into the Drill object.\n\n"

                ":param arg1: The job file file to read\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_PLOT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("load_select", &GXDH_wrap_load_select,
                "load_select((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load selections to from a file.\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("mask_ply", &GXDH_wrap_mask_ply,
                "mask_ply((GXPLY)arg1, (GXIPJ)arg2, (float)arg3, (str)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set mask channel based on view selection polygon.\n\n"

                ":param arg1: Masking polygon\n"
                ":type arg1: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg2: Projection from data to polygon coordinates\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg3: Slice thickness - rDUMMY for no limiting thickness\n"
                ":type arg3: float\n"
                ":param arg4: name of mask channel\n"
                ":type arg4: str\n"
                ":param arg5: \\ :ref:`DH_HOLES`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`DH_MASK`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Data values inside the polygon area, and within the slice thickness\n"
                "   have their mask channel values set to 1.\n"
                "   If the specified mask channel does not exist, it is created.\n"
                "   DH_MASK_NEW --- Mask is created new for each selected hole\n"
                "   DH_MASK_APPEND --- Current selection is added to previous.\n\n"
               );
    pyClass.def("open", &GXDH_wrap_open,
                "open((str)arg1) -> GXDH:\n"

                "\n.. parsed-literal::\n\n"
                "   Open DH from collar database and load all associated databases.\n\n"

                ":param arg1: Name of collar database\n"
                ":type arg1: str\n"
                ":returns: DH Object\n"
                ":rtype: :class:`geosoft.gxapi.GXDH`\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               ).staticmethod("open");
    pyClass.def("open_job", &GXDH_wrap_open_job,
                "open_job((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Open a DH plotting job\n\n"

                ":param arg1: job file name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_PLOT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("plot_hole_traces", &GXDH_wrap_plot_hole_traces,
                "plot_hole_traces((GXMAP)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot hole traces to a regular (plan) map.\n\n"

                ":param arg1: Map handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: Parameter file (INI) name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Both the hole traces and data can be plotted.\n"
                "   The DHPLANHOLES GX uses the default plan map parameter file\n"
                "   \"_plan.inp\".\n\n"
               );
    pyClass.def("plot_hole_traces_3d", &GXDH_wrap_plot_hole_traces_3d,
                "plot_hole_traces_3d((GXMVIEW)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot hole traces to an existing 3D map view.\n\n"

                ":param arg1: Existing 3D map view\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Parameter file (INI) name (normally \\ `*`\\ .in3)\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Both the hole traces and data can be plotted.\n"
                "   The DH3DHOLES GX uses the default 3D map parameter file\n"
                "   \"_3D.in3\".\n\n"
               );
    pyClass.def("plot_symbols_3d", &GXDH_wrap_plot_symbols_3d,
                "plot_symbols_3d((GXMVIEW)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot 3D symbols to an existing 3D map view.\n\n"

                ":param arg1: Existing 3D map view\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Parameter file (INI) name (normally \\ `*`\\ .in3)\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.1.0\n\n"
               );
    pyClass.def("qa_collar", &GXDH_wrap_qa_collar,
                "qa_collar((GXWA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Do QA/QC on Hole Collar data.\n\n"

                ":param arg1: WA Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );
    pyClass.def("qa_collar_lst", &GXDH_wrap_qa_collar_lst,
                "qa_collar_lst((GXLST)arg1, (GXWA)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Do QA/QC on Hole Collar data - LST of holes.\n\n"

                ":param arg1: LST of holes (Name, Index)\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: WA Handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.1\n\n"
               );
    pyClass.def("qa_dip_az_curvature", &GXDH_wrap_qa_dip_az_curvature,
                "qa_dip_az_curvature((GXWA)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Do QA/QC Curvature checking on Dip Azimuth data.\n\n"

                ":param arg1: WA Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg2: Dip/Azimuth curvature tolerance (degree per meter)\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Checks all holes with Dip-Azimuth survey data\n\n"
               );
    pyClass.def("qa_dip_az_curvature2", &GXDH_wrap_qa_dip_az_curvature2,
                "qa_dip_az_curvature2((GXWA)arg1, (float)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Do QA/QC Curvature checking on Dip Azimuth data for a single hole.\n\n"

                ":param arg1: WA Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg2: Dip/Azimuth curvature tolerance (degree per meter)\n"
                ":type arg2: float\n"
                ":param arg3: Hole name\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Checks single hole with Dip-Azimuth survey data\n\n"
               );
    pyClass.def("qa_dip_az_survey", &GXDH_wrap_qa_dip_az_survey,
                "qa_dip_az_survey((GXDB)arg1, (GXWA)arg2, (int)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Do QA/QC on Dip/Az Survey data.\n\n"

                ":param arg1: DB Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: WA Handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg3: Line\n"
                ":type arg3: int\n"
                ":param arg4: Current hole Name\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Error if no Dip-Azimuth survey database, or if\n"
                "   the requested line does not exist in the database.\n\n"
               );
    pyClass.def("qa_east_north_curvature", &GXDH_wrap_qa_east_north_curvature,
                "qa_east_north_curvature((GXWA)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Do QA/QC Curvature checking on Dip Azimuth data.\n\n"

                ":param arg1: WA Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg2: Dip/Azimuth curvature tolerance (degree per meter)\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Checks all holes with East-North survey data\n\n"
               );
    pyClass.def("qa_east_north_curvature2", &GXDH_wrap_qa_east_north_curvature2,
                "qa_east_north_curvature2((GXWA)arg1, (float)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Do QA/QC Curvature checking on Dip Azimuth data for a single hole.\n\n"

                ":param arg1: WA Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg2: Dip/Azimuth curvature tolerance (degree per meter)\n"
                ":type arg2: float\n"
                ":param arg3: Hole name\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Checks single holes with East-North survey data\n\n"
               );
    pyClass.def("qa_east_north_survey", &GXDH_wrap_qa_east_north_survey,
                "qa_east_north_survey((GXDB)arg1, (GXWA)arg2, (int)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Do QA/QC on East/North Survey data.\n\n"

                ":param arg1: DB Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: WA Handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg3: Line\n"
                ":type arg3: int\n"
                ":param arg4: Current hole Name\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Error if no East-North survey database, or if\n"
                "   the requested line does not exist in the database.\n\n"
               );
    pyClass.def("qa_from_to_data", &GXDH_wrap_qa_from_to_data,
                "qa_from_to_data((GXDB)arg1, (GXWA)arg2, (int)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Do QA/QC on From/To data.\n\n"

                ":param arg1: DB Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: WA Handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg3: Line\n"
                ":type arg3: int\n"
                ":param arg4: Current hole Name\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );
    pyClass.def("qa_point_data", &GXDH_wrap_qa_point_data,
                "qa_point_data((GXDB)arg1, (GXWA)arg2, (int)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Do QA/QC on Point data.\n\n"

                ":param arg1: DB Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: WA Handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg3: Line\n"
                ":type arg3: int\n"
                ":param arg4: Current hole Name\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );
    pyClass.def("qa_write_unregistered_holes", &GXDH_wrap_qa_write_unregistered_holes,
                "qa_write_unregistered_holes((GXDB)arg1, (GXWA)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write out unregistered holes in a database.\n\n"

                ":param arg1: DB Handle (not the collar table)\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: WA Handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Looks at each line in a database and sees if it is listed in\n"
                "   the collar tables' hole list.\n\n"
               );
    pyClass.def("replot_holes", &GXDH_wrap_replot_holes,
                "replot_holes((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replot holes on an existing drill map.\n\n"

                ":param arg1: Parameter (INI) name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_PLOT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The parameter file must correspond to the plot Type.\n"
                "   The hDH->hMAP value must be set first, using \\ :func:`geosoft.gxapi.GXDH.set_map`\\ ().\n"
                "   Overwrites existing hole and hole data groups.\n"
                "   Replots the legend if the legend is enabled.\n"
                "   This should only be used on a slightly modified version of the\n"
                "   INI file used to create the existing map, or things may not\n"
                "   work out (e.g. bad locations etc).\n\n"
               );
    pyClass.def("plot_holes_on_section", &GXDH_wrap_plot_holes_on_section,
                "plot_holes_on_section((str)arg1, (int)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot the currently selected holes on an existing section view.\n\n"

                ":param arg1: Parameter (INI) name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_PLOT`\\  Section plot type (DH_PLOT_SECTION or DH_PLOT_SECTION_CROOKED\n"
                ":type arg2: int\n"
                ":param arg3: View name\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				Plot the currently selected holes to a section view.\n"
                "   			 \n\n"
               );
    pyClass.def("re_survey_east_north", &GXDH_wrap_re_survey_east_north,
                "re_survey_east_north((str)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float_ref)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Resurvey an East-North-RL survey.\n\n"

                ":param arg1: Hole ID (for error messages)\n"
                ":type arg1: str\n"
                ":param arg2: input East\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: input North\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: input RL\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: returned depths down the hole\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: input collar East\n"
                ":type arg6: float\n"
                ":param arg7: input collar North\n"
                ":type arg7: float\n"
                ":param arg8: input collar RL\n"
                ":type arg8: float\n"
                ":param arg9: input top of hole depth\n"
                ":type arg9: float\n"
                ":param arg10: returned bottom depth\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Re-interpolates in X, Y and Z to proper depth interval\n"
                "   and returns depths for each point\n\n"
               );
    pyClass.def("re_survey_pol_fit", &GXDH_wrap_re_survey_pol_fit,
                "re_survey_pol_fit((str)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (int)arg11, (int)arg12, (GXVV)arg13, (GXVV)arg14, (GXVV)arg15, (GXVV)arg16) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Use the polynomial fit resurveying method.\n\n"

                ":param arg1: Hole ID (used for error messages)\n"
                ":type arg1: str\n"
                ":param arg2: Dip\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Azimuth\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Depth\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Collar X (easting) (depth = 0)\n"
                ":type arg5: float\n"
                ":param arg6: Collar Y (northing)(depth = 0)\n"
                ":type arg6: float\n"
                ":param arg7: Collar Z (elevation) (depth = 0)\n"
                ":type arg7: float\n"
                ":param arg8: Minimum hole depth to start output values\n"
                ":type arg8: float\n"
                ":param arg9: Maximum hole depth for output values\n"
                ":type arg9: float\n"
                ":param arg10: Increment for output values\n"
                ":type arg10: float\n"
                ":param arg11: \\ :ref:`DIP_CONVENTION`\\ \n"
                ":type arg11: int\n"
                ":param arg12: Polynomial order\n"
                ":type arg12: int\n"
                ":param arg13: X (Easting) - Output\n"
                ":type arg13: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg14: Y (Northin) - Output\n"
                ":type arg14: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg15: Z (Elevation) - Output\n"
                ":type arg15: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg16: Depths - Output\n"
                ":type arg16: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Uses the polynomial fit method to calculate (X, Y, Z)\n"
                "   locations down the hole from azimuth, dip, depth values.\n"
                "   The collar is assumed to be at zero depth, and depth is the\n"
                "   measure distance down the hole (even if it's horizontal).\n"
                "   A negative dip convention means vertical down is -90 degrees.\n"
                "   The polynomial order must be in the range 1-20, with 5 being adequate\n"
                "   for most smoothly curving holes. The order is reduced to no more than\n"
                "   the number of input points.\n\n"
               );
    pyClass.def("re_survey_rad_curve", &GXDH_wrap_re_survey_rad_curve,
                "re_survey_rad_curve((str)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (int)arg11, (GXVV)arg12, (GXVV)arg13, (GXVV)arg14, (GXVV)arg15) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Use radius of curvature resurveying method.\n\n"

                ":param arg1: Hole ID (used for error messages)\n"
                ":type arg1: str\n"
                ":param arg2: Dip\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Azimuth\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Depth\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Collar X (easting) (depth = 0)\n"
                ":type arg5: float\n"
                ":param arg6: Collar Y (northing)(depth = 0)\n"
                ":type arg6: float\n"
                ":param arg7: Collar Z (elevation) (depth = 0)\n"
                ":type arg7: float\n"
                ":param arg8: Minimum hole depth to start output values\n"
                ":type arg8: float\n"
                ":param arg9: Maximum hole depth for output values\n"
                ":type arg9: float\n"
                ":param arg10: Increment for output values\n"
                ":type arg10: float\n"
                ":param arg11: \\ :ref:`DIP_CONVENTION`\\ \n"
                ":type arg11: int\n"
                ":param arg12: X (Easting) - Output\n"
                ":type arg12: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg13: Y (Northin) - Output\n"
                ":type arg13: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg14: Z (Elevation) - Output\n"
                ":type arg14: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg15: Depths - Output\n"
                ":type arg15: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Uses the Radius of curvature method to calculate (X, Y, Z)\n"
                "   locations down the hole from azimuth, dip, depth values.\n"
                "   The collar is assumed to be at zero depth, and depth is the\n"
                "   measure distance down the hole (even if it's horizontal).\n"
                "   A negative dip convention means vertical down is -90 degrees.\n\n"
               );
    pyClass.def("re_survey_straight", &GXDH_wrap_re_survey_straight,
                "re_survey_straight((str)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (int)arg10, (GXVV)arg11, (GXVV)arg12, (GXVV)arg13, (GXVV)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Resurvey a straight hole.\n\n"

                ":param arg1: Hole ID (used for error messages)\n"
                ":type arg1: str\n"
                ":param arg2: Collar Dip\n"
                ":type arg2: float\n"
                ":param arg3: Collar Azimuth\n"
                ":type arg3: float\n"
                ":param arg4: Collar X (easting) (depth = 0)\n"
                ":type arg4: float\n"
                ":param arg5: Collar Y (northing)(depth = 0)\n"
                ":type arg5: float\n"
                ":param arg6: Collar Z (elevation) (depth = 0)\n"
                ":type arg6: float\n"
                ":param arg7: Minimum hole depth to start output values\n"
                ":type arg7: float\n"
                ":param arg8: Maximum hole depth for output values\n"
                ":type arg8: float\n"
                ":param arg9: Increment for output values\n"
                ":type arg9: float\n"
                ":param arg10: \\ :ref:`DIP_CONVENTION`\\ \n"
                ":type arg10: int\n"
                ":param arg11: X (Easting) - Output\n"
                ":type arg11: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg12: Y (Northin) - Output\n"
                ":type arg12: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg13: Z (Elevation) - Output\n"
                ":type arg13: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg14: Depths - Output\n"
                ":type arg14: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Assumes a straight hole to calculate (X, Y, Z)\n"
                "   locations down the hole from azimuth, dip, depth values.\n"
                "   The collar is assumed to be at zero depth, and depth is the\n"
                "   measure distance down the hole (even if it's horizontal).\n"
                "   A negative dip convention means vertical down is -90 degrees.\n\n"
               );
    pyClass.def("re_survey_straight_seg", &GXDH_wrap_re_survey_straight_seg,
                "re_survey_straight_seg((str)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (int)arg11, (GXVV)arg12, (GXVV)arg13, (GXVV)arg14, (GXVV)arg15) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Resurvey a hole with straight segments between locations.\n\n"

                ":param arg1: Hole ID (used for error messages)\n"
                ":type arg1: str\n"
                ":param arg2: Dip\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Azimuth\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Depth\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Collar X (easting) (depth = 0)\n"
                ":type arg5: float\n"
                ":param arg6: Collar Y (northing)(depth = 0)\n"
                ":type arg6: float\n"
                ":param arg7: Collar Z (elevation) (depth = 0)\n"
                ":type arg7: float\n"
                ":param arg8: Minimum hole depth to start output values\n"
                ":type arg8: float\n"
                ":param arg9: Maximum hole depth for output values\n"
                ":type arg9: float\n"
                ":param arg10: Increment for output values\n"
                ":type arg10: float\n"
                ":param arg11: \\ :ref:`DIP_CONVENTION`\\ \n"
                ":type arg11: int\n"
                ":param arg12: X (Easting) - Output\n"
                ":type arg12: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg13: Y (Northin) - Output\n"
                ":type arg13: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg14: Z (Elevation) - Output\n"
                ":type arg14: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg15: Depths - Output\n"
                ":type arg15: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate (X, Y, Z) locations down the hole from azimuth, dip,\n"
                "   depth values, assuming each segment is straight, and the hole\n"
                "   bends at each successive azimuth, dip, depth value.\n"
                "   The collar is assumed to be at zero depth, and depth is the\n"
                "   measure distance down the hole (even if it's horizontal).\n"
                "   A negative dip convention means vertical down is -90 degrees.\n\n"
               );
    pyClass.def("save_data_parameters_ini", &GXDH_wrap_save_data_parameters_ini,
                "save_data_parameters_ini((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save data parameters to INI files..\n\n"

                ":param arg1: Source database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Directory to store INI files\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Wholeplot data graphing parameters for each channel are stored\n"
                "   in the channel REG. This function lets a user transfer pre-defined\n"
                "   settings to individual INI files (eg. cu.ini).\n"
                "   As of v6.3, the DH object is NOT required for this function, and\n"
                "   is, in fact, ignored.\n\n"
               );
    pyClass.def("save_job", &GXDH_wrap_save_job,
                "save_job((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save a DH plotting job\n\n"

                ":param arg1: job file name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_PLOT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("save_select", &GXDH_wrap_save_select,
                "save_select((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Saves current selections to a file.\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("section_window_size_mm", &GXDH_wrap_section_window_size_mm,
                "section_window_size_mm((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Deterine the size, in mm, of the section window\n\n"

                ":param arg1: X size in mm.\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y size in mm.\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Given the current selection of windows (e.g. legend, plan),\n"
                "   paper size and orientation, return the size in mm of the\n"
                "   window used for plotting the section.\n\n"
               );
    pyClass.def("select_all_holes", &GXDH_wrap_select_all_holes,
                "select_all_holes() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Select all the holes in a Drill hole project.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("select_holes", &GXDH_wrap_select_holes,
                "select_holes((GXVV)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Select holes by hole indices.\n\n"

                ":param arg1: INT VV with hole indices.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: 0 - deselect, 1 - select\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Indices less than 0 are skipped. This lets you use this function\n"
                "   after a call to \\ :func:`geosoft.gxapi.GXLST.find_items`\\ , which returns -1 for indices not located.\n\n"
               );
    pyClass.def("select_name", &GXDH_wrap_select_name,
                "select_name((str)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Select holes using a name mask.\n\n"

                ":param arg1: mask\n"
                ":type arg1: str\n"
                ":param arg2: 0 - deselect, 1 - select\n"
                ":type arg2: int\n"
                ":param arg3: 0 - overwrite, 1 - append\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Overwrite mode - all selections tested and selected or not selected\n"
                "   Append mode    - only holes matching the mask are selected or not selected.\n\n"
               );
    pyClass.def("select_ply", &GXDH_wrap_select_ply,
                "select_ply((GXPLY)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Select all holes in PLY (Polygon) object.\n\n"

                ":param arg1: Polygon object\n"
                ":type arg1: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function operates the same as the call:\n"
                "   \n"
                "   \\ :func:`geosoft.gxapi.GXDH.select_ply2`\\ (Drill, 1, 0, 0);\n\n"
               );
    pyClass.def("select_ply2", &GXDH_wrap_select_ply2,
                "select_ply2((GXPLY)arg1, (int)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Select holes in PLY (Polygon) object with options.\n\n"

                ":param arg1: Polygon object\n"
                ":type arg1: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg2: Select (0) or Deselect (1)\n"
                ":type arg2: int\n"
                ":param arg3: Region (0: inside, 1: outside)\n"
                ":type arg3: int\n"
                ":param arg4: Mode (0: Append, 1: New)\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The various selection options give the following results:\n"
                "   \n"
                "   New/Select/inside: Unselect all holes, then\n"
                "                      select all holes inside the polygon.\n"
                "   New/Select/outside: Unselect all holes, then\n"
                "                      select all holes outside the polygon.\n"
                "   New/Deselect/inside: Select all holes, then\n"
                "                      deselect all holes inside the polygon.\n"
                "   New/Deselect/outside: Select all holes, then\n"
                "                      deselect all holes outside the polygon.\n"
                "   \n"
                "   Append/Select/inside: Select all holes inside the polygon.\n"
                "                         Leave selections outside as is.\n"
                "   Append/Select/outside: Select all holes outside the polygon.\n"
                "                         Leave selections inside as is.\n"
                "   Append/Deselect/inside: Deselect all holes inside the polygon\n"
                "                         Leave selections outside as is.\n"
                "   Append/Deselect/outside: Deselect all holes outside the polygon.\n"
                "                         Leave selections inside as is.\n\n"
               );
    pyClass.def("set_crooked_section_ipj", &GXDH_wrap_set_crooked_section_ipj,
                "set_crooked_section_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Pass the Crooked projection required for plotting to a crooked section.\n\n"

                ":param arg1: Crooked Section IPJ\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This might be extracted from an existing crooked section view, or created from a database line.\n\n"
               );
    pyClass.def("set_current_view_name", &GXDH_wrap_set_current_view_name,
                "set_current_view_name((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the current map view name.\n\n"

                ":param arg1: View name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Can be used to specify the name of the view to plot into.\n\n"
               );
    pyClass.def("set_info", &GXDH_wrap_set_info,
                "set_info((int)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set Collar Information.\n\n"

                ":param arg1: hole index\n"
                ":type arg1: int\n"
                ":param arg2: Name of information\n"
                ":type arg2: str\n"
                ":param arg3: Information\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the DH_ELEV channel is requested it will also\n"
                "   search for the DH_RL channel, which is the new\n"
                "   name for the collar elevation.\n\n"
               );
    pyClass.def("set_ipj", &GXDH_wrap_set_ipj,
                "set_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the project IPJ.\n\n"

                ":param arg1: IPJ Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The projection for the project is the projection stored\n"
                "   in the DH_EAST channel in the collar table. This\n"
                "   function sets the projection of the (DH_EAST, DH_NORTH)\n"
                "   channel pairs in each of the project databases to the\n"
                "   input IPJ.\n"
                "   The input IPJ cannot be a geographic coordinate system\n"
                "   or this call will fail with an error message.\n\n"
               );
    pyClass.def("set_map", &GXDH_wrap_set_map,
                "set_map((GXMAP)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Store the current MAP to the DH object.\n\n"

                ":param arg1: IPJ Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Use this before calling the ReplotHoles functions,\n"
                "   so that, instead of creating a new map, the plotting\n"
                "   functions use the existing one.\n\n"
               );
    pyClass.def("set_new_ipj", &GXDH_wrap_set_new_ipj,
                "set_new_ipj((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a new project database projection to collar table projection.\n\n"

                ":param arg1: project database name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the IPJ of the collar table current x channel and copies it\n"
                "   into the named database (as long as it is in the project!)\n\n"
               );
    pyClass.def("set_selected_holes_vv", &GXDH_wrap_set_selected_holes_vv,
                "set_selected_holes_vv((GXVV)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set hole selection using hole indices.\n\n"

                ":param arg1: Input hole indices (must be type INT)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: 0 - overwrite, 1 - append\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               );
    pyClass.def("set_template_blob", &GXDH_wrap_set_template_blob,
                "set_template_blob((GXDB)arg1, (str)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Store the import template to the database.\n\n"

                ":param arg1: DB Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Import template name\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`DH_DATA`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The template can later be retrieved in order to refresh the\n"
                "   database with a call to the DHIMPORT.GX.\n"
                "   \n"
                "   The import types correspond to the DHIMPORT.IMPTYPE variable:\n"
                "   0: ASCII, 1: Database/XLS, 2: ODBC\n\n"
               ).staticmethod("set_template_blob");
    pyClass.def("significant_intersections_db", &GXDH_wrap_significant_intersections_db,
                "significant_intersections_db((GXDB)arg1, (GXDB)arg2, (int)arg3, (str)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (float)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Make a report of Significant Intersections\n\n"

                ":param arg1: Input assay DB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: output composite DB object\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg3: \\ :ref:`DH_COMPSTDB_HOLSEL`\\ \n"
                ":type arg3: int\n"
                ":param arg4: The primary assay channel.\n"
                ":type arg4: str\n"
                ":param arg5: Minimum Cut off grade for Primary Assay\n"
                ":type arg5: float\n"
                ":param arg6: Maximum Cut off grade for Primary Assay\n"
                ":type arg6: float\n"
                ":param arg7: Minimum Composite Length\n"
                ":type arg7: float\n"
                ":param arg8: Minimum Composite thickness\n"
                ":type arg8: float\n"
                ":param arg9: Maximum Internal Dilution\n"
                ":type arg9: float\n"
                ":param arg10: Minimum diluted grade\n"
                ":type arg10: float\n"
                ":param arg11: Grade for Missing Assays\n"
                ":type arg11: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("test_import_las", &GXDH_wrap_test_import_las,
                "test_import_las((str)arg1, (str)arg2, (float)arg3, (GXWA)arg4, (int_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Tests import of LAS Data for problems.\n\n"

                ":param arg1: Assay table name\n"
                ":type arg1: str\n"
                ":param arg2: LAS file name\n"
                ":type arg2: str\n"
                ":param arg3: averaging/desampling interval\n"
                ":type arg3: float\n"
                ":param arg4: Log file handle\n"
                ":type arg4: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg5: 1 returned if problems found\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See \\ :func:`geosoft.gxapi.GXDH.import_las`\\ .\n"
                "   Determines if the import of the LAS data will result in data\n"
                "   being overwritten, interpolated or resampled. Warnings are written to a log\n"
                "   file, as in sImportLAS_DH. Warnings are not registered in cases\n"
                "   where data is merely extended at the start or the end with dummies\n"
                "   to match a different interval down the hole.\n\n"
               );
    pyClass.def("un_select_all_holes", &GXDH_wrap_un_select_all_holes,
                "un_select_all_holes() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unselect all the holes in a Drill hole project.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("un_selected_hole_lst", &GXDH_wrap_un_selected_hole_lst,
                "un_selected_hole_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Populate an LST with the list of the unselected holes\n\n"

                ":param arg1: LST handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("update_collar_table", &GXDH_wrap_update_collar_table,
                "update_collar_table() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Update all collar table information.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("update_hole_extent", &GXDH_wrap_update_hole_extent,
                "update_hole_extent((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Update extents for one hole.\n\n"

                ":param arg1: hole index\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("wholeplot", &GXDH_wrap_wholeplot,
                "wholeplot((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Run a Wholeplot plot job.\n\n"

                ":param arg1: Parameter (INI) name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DH_PLOT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The parameter file must correspond to the plot Type. The INI file\n"
                "   contains settings for all of the non-database data related\n"
                "   parameters (e.g. Map template, scale, boundaries,\n"
                "   section definitions, hole trace parameters etc...)\n\n"
               );
    pyClass.def("surface_intersections", &GXDH_wrap_surface_intersections,
                "surface_intersections((GXDB)arg1, (str)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Determine intersections of drillholes with a surface.\n\n"

                ":param arg1: Output DB Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Input surface file\n"
                ":type arg2: str\n"
                ":param arg3: Selected holes (1), All holes (0)\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"
               );

    scope().attr("DH_DEFAULT_ROCKCODE_FILE") = "agso.csv";
    scope().attr("DH_DEFAULT_STRUCTURECODE_FILE") = "structcodes.csv";
    scope().attr("STR_DH_HOLES") = (int32_t)1048576;
    scope().attr("DH_COMP_DONE") = (int32_t)0;
    scope().attr("DH_COMP_CANCEL") = (int32_t)-1;
    scope().attr("DH_COMP_SELECT") = (int32_t)1;
    scope().attr("DH_COMP_REFRESH") = (int32_t)2;
    scope().attr("DH_COMPSTDB_HOLSEL_ALL") = (int32_t)0;
    scope().attr("DH_COMPSTDB_HOLSEL_SELECTED") = (int32_t)1;
    scope().attr("DH_COMPSTDB_INTSEL_FIXED") = (int32_t)0;
    scope().attr("DH_COMPSTDB_INTSEL_LITHOLOGY") = (int32_t)1;
    scope().attr("DH_COMPSTDB_INTSEL_BESTFITLITH") = (int32_t)2;
    scope().attr("DH_COMPSTDB_INTSEL_INTFILE") = (int32_t)3;
    scope().attr("DH_DATA_DIPAZIMUTH") = (int32_t)0;
    scope().attr("DH_DATA_EASTNORTH") = (int32_t)1;
    scope().attr("DH_DATA_FROMTO") = (int32_t)2;
    scope().attr("DH_DATA_POINT") = (int32_t)3;
    scope().attr("DH_DATA_COLLAR") = (int32_t)4;
    scope().attr("DH_DATA_UNKNOWN") = (int32_t)100;
    scope().attr("DH_DEFINE_PLAN") = (int32_t)1;
    scope().attr("DH_DEFINE_SECT_NS") = (int32_t)1;
    scope().attr("DH_DEFINE_SECT_EW") = (int32_t)2;
    scope().attr("DH_DEFINE_SECT_ANGLED") = (int32_t)3;
    scope().attr("DH_EXP_CSV") = (int32_t)0;
    scope().attr("DH_EXP_ASCII") = (int32_t)1;
    scope().attr("DH_EXP_ACCESS") = (int32_t)2;
    scope().attr("DH_EXP_SHP") = (int32_t)3;
    scope().attr("DH_EXP_SURPAC") = (int32_t)4;
    scope().attr("DH_EXP_SHP_TRACES") = (int32_t)5;
    scope().attr("DH_HOLES_ALL") = (int32_t)0;
    scope().attr("DH_HOLES_SELECTED") = (int32_t)1;
    scope().attr("DH_MASK_APPEND") = (int32_t)0;
    scope().attr("DH_MASK_NEW") = (int32_t)1;
    scope().attr("DH_PLOT_PLAN") = (int32_t)0;
    scope().attr("DH_PLOT_SECTION") = (int32_t)1;
    scope().attr("DH_PLOT_STRIPLOG") = (int32_t)2;
    scope().attr("DH_PLOT_HOLE_TRACES") = (int32_t)3;
    scope().attr("DH_PLOT_3D") = (int32_t)4;
    scope().attr("DH_PLOT_SECTION_STACK") = (int32_t)5;
    scope().attr("DH_PLOT_SECTION_FENCE") = (int32_t)6;
    scope().attr("DH_PLOT_SECTION_CROOKED") = (int32_t)7;
    scope().attr("DH_SECT_PAGE_SECTION") = (int32_t)1;
    scope().attr("DH_SURFACE_FIRST_LAYER_FROM") = (int32_t)0;
    scope().attr("DH_SURFACE_FIRST_LAYER_TO") = (int32_t)1;
    scope().attr("DH_SURFACE_SECOND_LAYER_FROM") = (int32_t)2;
    scope().attr("DH_SURFACE_SECOND_LAYER_TO") = (int32_t)3;
    scope().attr("DH_SURFACE_LAST_LAYER_FROM") = (int32_t)4;
    scope().attr("DH_SURFACE_LAST_LAYER_TO") = (int32_t)5;
    scope().attr("DIP_CONVENTION_NEGATIVE") = (int32_t)-1;
    scope().attr("DIP_CONVENTION_POSITIVE") = (int32_t)1;

}
