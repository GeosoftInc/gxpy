#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXSYS_wrap_break_date(double arg1, int_ref& arg2, int_ref& arg3, int_ref& arg4)
{
    GXSYS::break_date(arg1, arg2, arg3, arg4);
}
inline int32_t GXSYS_wrap_dateto_long(double arg1)
{
    int32_t ret = GXSYS::dateto_long(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_timeto_long(double arg1)
{
    int32_t ret = GXSYS::timeto_long(arg1);
    return ret;
}
inline double GXSYS_wrap_date()
{
    double ret = GXSYS::date();
    return ret;
}
inline double GXSYS_wrap_longto_date(int32_t arg1)
{
    double ret = GXSYS::longto_date(arg1);
    return ret;
}
inline double GXSYS_wrap_longto_time(int32_t arg1)
{
    double ret = GXSYS::longto_time(arg1);
    return ret;
}
inline double GXSYS_wrap_make_date(int32_t arg1, int32_t arg2, int32_t arg3)
{
    double ret = GXSYS::make_date(arg1, arg2, arg3);
    return ret;
}
inline double GXSYS_wrap_secondsto_time(double arg1)
{
    double ret = GXSYS::secondsto_time(arg1);
    return ret;
}
inline double GXSYS_wrap_time()
{
    double ret = GXSYS::time();
    return ret;
}
inline double GXSYS_wrap_timeto_seconds(double arg1)
{
    double ret = GXSYS::timeto_seconds(arg1);
    return ret;
}
inline double GXSYS_wrap_utc_date()
{
    double ret = GXSYS::utc_date();
    return ret;
}
inline double GXSYS_wrap_utc_time()
{
    double ret = GXSYS::utc_time();
    return ret;
}
inline int32_t GXSYS_wrap_exist_env(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::exist_env(arg1);
    return ret;
}
inline void GXSYS_wrap_get_env(const gx_string_type& arg1, str_ref& arg2)
{
    GXSYS::get_env(arg1, arg2);
}
inline void GXSYS_wrap_set_env(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSYS::set_env(arg1, arg2);
}
inline int32_t GXSYS_wrap_clear_err_ap()
{
    int32_t ret = GXSYS::clear_err_ap();
    return ret;
}
inline int32_t GXSYS_wrap_get_top_error_ap()
{
    int32_t ret = GXSYS::get_top_error_ap();
    return ret;
}
inline void GXSYS_wrap_get_error_message_ap(int32_t arg1, str_ref& arg2)
{
    GXSYS::get_error_message_ap(arg1, arg2);
}
inline int32_t GXSYS_wrap_num_errors_ap()
{
    int32_t ret = GXSYS::num_errors_ap();
    return ret;
}
inline void GXSYS_wrap_set_server_messages_ap(int32_t arg1)
{
    GXSYS::set_server_messages_ap(arg1);
}
inline int32_t GXSYS_wrap_run(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    int32_t ret = GXSYS::run(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXSYS_wrap_run_gs(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::run_gs(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_run_gx(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::run_gx(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_run_gx_ex(const gx_string_type& arg1, int_ref& arg2)
{
    int32_t ret = GXSYS::run_gx_ex(arg1, arg2);
    return ret;
}
inline int32_t GXSYS_wrap_run_pdf(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSYS::run_pdf(arg1, arg2);
    return ret;
}
inline int32_t GXSYS_wrap_shell_execute(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, int32_t arg5)
{
    int32_t ret = GXSYS::shell_execute(arg1, arg2, arg3, arg4, (SHELL_EXECUTE)arg5);
    return ret;
}
inline void GXSYS_wrap_set_return(int32_t arg1)
{
    GXSYS::set_return(arg1);
}
inline void GXSYS_wrap_do_command(const gx_string_type& arg1)
{
    GXSYS::do_command(arg1);
}
inline void GXSYS_wrap_error(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXSYS::error(arg1, arg2, arg3);
}
inline void GXSYS_wrap_error_tag(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSYS::error_tag(arg1, arg2);
}
inline int32_t GXSYS_wrap__assert_gx(int32_t arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    int32_t ret = GXSYS::_assert_gx(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXSYS_wrap_ole_automation(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    int32_t ret = GXSYS::ole_automation(arg1, arg2, arg3);
    return ret;
}
inline void GXSYS_wrap_save_log(const gx_string_type& arg1)
{
    GXSYS::save_log(arg1);
}
inline void GXSYS_wrap_show_error()
{
    GXSYS::show_error();
}
inline void GXSYS_wrap_terminate(const gx_string_type& arg1)
{
    GXSYS::terminate(arg1);
}
inline int32_t GXSYS_wrap_crc_file(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::crc_file(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_crc_file_offset(const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = GXSYS::crc_file_offset(arg1, arg2);
    return ret;
}
inline void GXSYS_wrap_file_ren(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSYS::file_ren(arg1, arg2);
}
inline void GXSYS_wrap_find_files_vv(GXVVPtr arg1, const gx_string_type& arg2)
{
    GXSYS::find_files_vv(arg1, arg2);
}
inline void GXSYS_wrap_absolute_file_name(const gx_string_type& arg1, str_ref& arg2)
{
    GXSYS::absolute_file_name(arg1, arg2);
}
inline int32_t GXSYS_wrap_copy_file(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSYS::copy_file(arg1, arg2);
    return ret;
}
inline int32_t GXSYS_wrap_delete_file(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::delete_file(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_delete_gi_file(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::delete_gi_file(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_delete_grid_file(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::delete_grid_file(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_dir_exist(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::dir_exist(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_file_exist(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::file_exist(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_file_size(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::file_size(arg1);
    return ret;
}
inline bool GXSYS_wrap_file_writable(const gx_string_type& arg1)
{
    bool ret = GXSYS::file_writable(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_find_path(const gx_string_type& arg1, int32_t arg2, str_ref& arg3)
{
    int32_t ret = GXSYS::find_path(arg1, (SYS_SEARCH_PATH)arg2, arg3);
    return ret;
}
inline int32_t GXSYS_wrap_find_path_ex(const gx_string_type& arg1, int32_t arg2, int32_t arg3, str_ref& arg4)
{
    int32_t ret = GXSYS::find_path_ex(arg1, (SYS_SEARCH_PATH)arg2, (GEO_DIRECTORY)arg3, arg4);
    return ret;
}
inline void GXSYS_wrap_get_directory(int32_t arg1, str_ref& arg2)
{
    GXSYS::get_directory((SYS_DIR)arg1, arg2);
}
inline void GXSYS_wrap_get_path(int32_t arg1, str_ref& arg2)
{
    GXSYS::get_path((SYS_PATH)arg1, arg2);
}
inline void GXSYS_wrap_get_windows_dir(str_ref& arg1)
{
    GXSYS::get_windows_dir(arg1);
}
inline int32_t GXSYS_wrap_make_dir(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::make_dir(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_make_file_readonly(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::make_file_readonly(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_make_file_writable(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::make_file_writable(arg1);
    return ret;
}
inline void GXSYS_wrap_relative_file_name(const gx_string_type& arg1, str_ref& arg2)
{
    GXSYS::relative_file_name(arg1, arg2);
}
inline void GXSYS_wrap_short_path_file_name(const gx_string_type& arg1, str_ref& arg2)
{
    GXSYS::short_path_file_name(arg1, arg2);
}
inline void GXSYS_wrap_temp_file_ext(const gx_string_type& arg1, str_ref& arg2)
{
    GXSYS::temp_file_ext(arg1, arg2);
}
inline void GXSYS_wrap_temp_file_name(const gx_string_type& arg1, str_ref& arg2)
{
    GXSYS::temp_file_name(arg1, arg2);
}
inline void GXSYS_wrap_transfer_path(const gx_string_type& arg1, str_ref& arg2)
{
    GXSYS::transfer_path(arg1, arg2);
}
inline int32_t GXSYS_wrap_valid_file_name(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::valid_file_name(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_write_in_dir(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::write_in_dir(arg1);
    return ret;
}
inline double GXSYS_wrap_file_date(const gx_string_type& arg1)
{
    double ret = GXSYS::file_date(arg1);
    return ret;
}
inline double GXSYS_wrap_file_time(const gx_string_type& arg1)
{
    double ret = GXSYS::file_time(arg1);
    return ret;
}
inline double GXSYS_wrap_utc_file_date(const gx_string_type& arg1)
{
    double ret = GXSYS::utc_file_date(arg1);
    return ret;
}
inline double GXSYS_wrap_utc_file_time(const gx_string_type& arg1)
{
    double ret = GXSYS::utc_file_time(arg1);
    return ret;
}
inline void GXSYS_wrap_get_settings_meta(GXMETAPtr arg1)
{
    GXSYS::get_settings_meta(arg1);
}
inline void GXSYS_wrap_global_reset(const gx_string_type& arg1)
{
    GXSYS::global_reset(arg1);
}
inline void GXSYS_wrap_global_set(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSYS::global_set(arg1, arg2);
}
inline void GXSYS_wrap_global_write(const gx_string_type& arg1)
{
    GXSYS::global_write(arg1);
}
inline int32_t GXSYS_wrap_global(const gx_string_type& arg1, str_ref& arg2)
{
    int32_t ret = GXSYS::global(arg1, arg2);
    return ret;
}
inline void GXSYS_wrap_reset_settings()
{
    GXSYS::reset_settings();
}
inline void GXSYS_wrap_set_settings_meta(GXMETAPtr arg1)
{
    GXSYS::set_settings_meta(arg1);
}
inline int32_t GXSYS_wrap_check_arc_license()
{
    int32_t ret = GXSYS::check_arc_license();
    return ret;
}
inline int32_t GXSYS_wrap_check_arc_license_ex(str_ref& arg1)
{
    ARC_LICENSE ret = GXSYS::check_arc_license_ex(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_check_intrinsic(int32_t arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSYS::check_intrinsic(arg1, arg2);
    return ret;
}
inline int32_t GXSYS_wrap_get_geodist()
{
    int32_t ret = GXSYS::get_geodist();
    return ret;
}
inline void GXSYS_wrap_get_license_class(str_ref& arg1)
{
    GXSYS::get_license_class(arg1);
}
inline void GXSYS_wrap_get_licensed_user(str_ref& arg1, str_ref& arg2)
{
    GXSYS::get_licensed_user(arg1, arg2);
}
inline void GXSYS_wrap_add_lineage_parameter(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSYS::add_lineage_parameter(arg1, arg2);
}
inline void GXSYS_wrap_add_lineage_source(int32_t arg1, const gx_string_type& arg2)
{
    GXSYS::add_lineage_source((SYS_LINEAGE_SOURCE)arg1, arg2);
}
inline void GXSYS_wrap_clear_lineage_parameters()
{
    GXSYS::clear_lineage_parameters();
}
inline void GXSYS_wrap_clear_lineage_sources()
{
    GXSYS::clear_lineage_sources();
}
inline void GXSYS_wrap_copy_geo_file(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSYS::copy_geo_file(arg1, arg2);
}
inline void GXSYS_wrap_backup_geo_file(const gx_string_type& arg1, str_ref& arg2)
{
    GXSYS::backup_geo_file(arg1, arg2);
}
inline void GXSYS_wrap_remove_lineage_output(const gx_string_type& arg1)
{
    GXSYS::remove_lineage_output(arg1);
}
inline void GXSYS_wrap_remove_lineage_parameter(const gx_string_type& arg1)
{
    GXSYS::remove_lineage_parameter(arg1);
}
inline void GXSYS_wrap_remove_lineage_source(const gx_string_type& arg1)
{
    GXSYS::remove_lineage_source(arg1);
}
inline void GXSYS_wrap_restore_geo_file(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSYS::restore_geo_file(arg1, arg2);
}
inline void GXSYS_wrap_set_lineage_description(const gx_string_type& arg1)
{
    GXSYS::set_lineage_description(arg1);
}
inline void GXSYS_wrap_set_lineage_display_name(const gx_string_type& arg1)
{
    GXSYS::set_lineage_display_name(arg1);
}
inline void GXSYS_wrap_set_lineage_name(const gx_string_type& arg1)
{
    GXSYS::set_lineage_name(arg1);
}
inline void GXSYS_wrap_clear_menus(int32_t arg1)
{
    GXSYS::clear_menus((SYS_MENU_CLEAR)arg1);
}
inline void GXSYS_wrap_get_loaded_menus(GXLSTPtr arg1, GXLSTPtr arg2, GXLSTPtr arg3)
{
    GXSYS::get_loaded_menus(arg1, arg2, arg3);
}
inline void GXSYS_wrap_set_loaded_menus(GXLSTPtr arg1, GXLSTPtr arg2, GXLSTPtr arg3)
{
    GXSYS::set_loaded_menus(arg1, arg2, arg3);
}
inline void GXSYS_wrap_get_entitlement_rights(GXLSTPtr arg1)
{
    GXSYS::get_entitlement_rights(arg1);
}
inline void GXSYS_wrap_generate_guid(str_ref& arg1)
{
    GXSYS::generate_guid(arg1);
}
inline void GXSYS_wrap_clipboard_to_file(const gx_string_type& arg1)
{
    GXSYS::clipboard_to_file(arg1);
}
inline GXRAPtr GXSYS_wrap_create_clipboard_ra()
{
    GXRAPtr ret = GXSYS::create_clipboard_ra();
    return ret;
}
inline GXWAPtr GXSYS_wrap_create_clipboard_wa()
{
    GXWAPtr ret = GXSYS::create_clipboard_wa();
    return ret;
}
inline void GXSYS_wrap_emf_object_size(const gx_string_type& arg1, float_ref& arg2, float_ref& arg3)
{
    GXSYS::emf_object_size(arg1, arg2, arg3);
}
inline void GXSYS_wrap_file_to_clipboard(const gx_string_type& arg1)
{
    GXSYS::file_to_clipboard(arg1);
}
inline void GXSYS_wrap_font_lst(GXLSTPtr arg1, int32_t arg2)
{
    GXSYS::font_lst(arg1, (SYS_FONT)arg2);
}
inline int32_t GXSYS_wrap_get_dot_net_gx_entries(const gx_string_type& arg1, str_ref& arg2)
{
    int32_t ret = GXSYS::get_dot_net_gx_entries(arg1, arg2);
    return ret;
}
inline void GXSYS_wrap_send_general_message(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSYS::send_general_message(arg1, arg2);
}
inline void GXSYS_wrap_write_debug_log(const gx_string_type& arg1)
{
    GXSYS::write_debug_log(arg1);
}
inline int32_t GXSYS_wrap_get_thread_id()
{
    int32_t ret = GXSYS::get_thread_id();
    return ret;
}
inline void GXSYS_wrap_run_multi_user_script(const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    GXSYS::run_multi_user_script(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXSYS_wrap_clear_group(const gx_string_type& arg1)
{
    GXSYS::clear_group(arg1);
}
inline void GXSYS_wrap_clear_group_parm(const gx_string_type& arg1)
{
    GXSYS::clear_group_parm(arg1);
}
inline void GXSYS_wrap_clear_parm()
{
    GXSYS::clear_parm();
}
inline void GXSYS_wrap_default_int(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXSYS::default_int(arg1, arg2, arg3);
}
inline void GXSYS_wrap_default_double(const gx_string_type& arg1, const gx_string_type& arg2, double arg3)
{
    GXSYS::default_double(arg1, arg2, arg3);
}
inline void GXSYS_wrap_default_string(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXSYS::default_string(arg1, arg2, arg3);
}
inline void GXSYS_wrap_get_pattern(const gx_string_type& arg1, int_ref& arg2, float_ref& arg3, int_ref& arg4, float_ref& arg5, int_ref& arg6, int_ref& arg7)
{
    GXSYS::get_pattern(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXSYS_wrap_get_reg(GXREGPtr arg1, const gx_string_type& arg2)
{
    GXSYS::get_reg(arg1, arg2);
}
inline void GXSYS_wrap_gt_string(const gx_string_type& arg1, const gx_string_type& arg2, str_ref& arg3)
{
    GXSYS::gt_string(arg1, arg2, arg3);
}
inline int32_t GXSYS_wrap_exist_int(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSYS::exist_int(arg1, arg2);
    return ret;
}
inline int32_t GXSYS_wrap_exist_double(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSYS::exist_double(arg1, arg2);
    return ret;
}
inline int32_t GXSYS_wrap_exist_string(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSYS::exist_string(arg1, arg2);
    return ret;
}
inline int32_t GXSYS_wrap_get_int(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSYS::get_int(arg1, arg2);
    return ret;
}
inline int32_t GXSYS_wrap_get_yes_no(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSYS::get_yes_no(arg1, arg2);
    return ret;
}
inline void GXSYS_wrap_replace_string(const gx_string_type& arg1, str_ref& arg2, const gx_string_type& arg3)
{
    GXSYS::replace_string(arg1, arg2, arg3);
}
inline void GXSYS_wrap_load_parm(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSYS::load_parm(arg1, arg2);
}
inline double GXSYS_wrap_get_double(const gx_string_type& arg1, const gx_string_type& arg2)
{
    double ret = GXSYS::get_double(arg1, arg2);
    return ret;
}
inline void GXSYS_wrap_save_parm(const gx_string_type& arg1, int32_t arg2, const gx_string_type& arg3)
{
    GXSYS::save_parm(arg1, arg2, arg3);
}
inline void GXSYS_wrap_filter_parm_group(const gx_string_type& arg1, int32_t arg2)
{
    GXSYS::filter_parm_group(arg1, arg2);
}
inline void GXSYS_wrap_set_int(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXSYS::set_int(arg1, arg2, arg3);
}
inline void GXSYS_wrap_set_pattern(const gx_string_type& arg1, int32_t arg2, double arg3, int32_t arg4, double arg5, int32_t arg6, int32_t arg7)
{
    GXSYS::set_pattern(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXSYS_wrap_set_double(const gx_string_type& arg1, const gx_string_type& arg2, double arg3)
{
    GXSYS::set_double(arg1, arg2, arg3);
}
inline void GXSYS_wrap_set_reg(GXREGPtr arg1)
{
    GXSYS::set_reg(arg1);
}
inline void GXSYS_wrap_set_string(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXSYS::set_string(arg1, arg2, arg3);
}
inline int32_t GXSYS_wrap_check_stop()
{
    int32_t ret = GXSYS::check_stop();
    return ret;
}
inline int32_t GXSYS_wrap_prog_state()
{
    int32_t ret = GXSYS::prog_state();
    return ret;
}
inline void GXSYS_wrap_prog_name(const gx_string_type& arg1, int32_t arg2)
{
    GXSYS::prog_name(arg1, arg2);
}
inline void GXSYS_wrap_progress(int32_t arg1)
{
    GXSYS::progress(arg1);
}
inline void GXSYS_wrap_prog_update(int32_t arg1)
{
    GXSYS::prog_update(arg1);
}
inline void GXSYS_wrap_prog_update_l(int32_t arg1, int32_t arg2)
{
    GXSYS::prog_update_l(arg1, arg2);
}
inline void GXSYS_wrap_get_sys_info(int32_t arg1, str_ref& arg2)
{
    GXSYS::get_sys_info((SYS_INFO)arg1, arg2);
}
inline int32_t GXSYS_wrap_registry_get_val(int32_t arg1, const gx_string_type& arg2, const gx_string_type& arg3, str_ref& arg4)
{
    int32_t ret = GXSYS::registry_get_val((REG_DOMAIN)arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXSYS_wrap_registry_delete_key(int32_t arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSYS::registry_delete_key((REG_DOMAIN)arg1, arg2);
    return ret;
}
inline int32_t GXSYS_wrap_registry_delete_val(int32_t arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    int32_t ret = GXSYS::registry_delete_val((REG_DOMAIN)arg1, arg2, arg3);
    return ret;
}
inline void GXSYS_wrap_registry_set_val(int32_t arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    GXSYS::registry_set_val((REG_DOMAIN)arg1, arg2, arg3, arg4);
}
inline void GXSYS_wrap_destroy_ptmp(int32_t arg1)
{
    GXSYS::destroy_ptmp(arg1);
}
inline void GXSYS_wrap_get_ptmp(int32_t arg1)
{
    GXSYS::get_ptmp(arg1);
}
inline int32_t GXSYS_wrap_save_ptmp(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::save_ptmp(arg1);
    return ret;
}
inline void GXSYS_wrap__abort(const gx_string_type& arg1)
{
    GXSYS::_abort(arg1);
}
inline void GXSYS_wrap__assert(int32_t arg1)
{
    GXSYS::_assert(arg1);
}
inline void GXSYS_wrap__exit()
{
    GXSYS::_exit();
}
inline void GXSYS_wrap__cancel()
{
    GXSYS::_cancel();
}
inline int32_t GXSYS_wrap_delay(double arg1)
{
    int32_t ret = GXSYS::delay(arg1);
    return ret;
}
inline int32_t GXSYS_wrap_get_timer(int32_t arg1, float_ref& arg2, float_ref& arg3)
{
    int32_t ret = GXSYS::get_timer(arg1, arg2, arg3);
    return ret;
}
inline void GXSYS_wrap_display_help(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSYS::display_help(arg1, arg2);
}
inline void GXSYS_wrap_display_help_topic(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSYS::display_help_topic(arg1, arg2);
}
inline void GXSYS_wrap_display_int(const gx_string_type& arg1, int32_t arg2)
{
    GXSYS::display_int(arg1, arg2);
}
inline void GXSYS_wrap_display_message(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSYS::display_message(arg1, arg2);
}
inline void GXSYS_wrap_display_double(const gx_string_type& arg1, double arg2)
{
    GXSYS::display_double(arg1, arg2);
}
inline int32_t GXSYS_wrap_display_question(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSYS::display_question(arg1, arg2);
    return ret;
}
inline int32_t GXSYS_wrap_display_question_with_cancel(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSYS::display_question_with_cancel(arg1, arg2);
    return ret;
}
inline int32_t GXSYS_wrap_interactive()
{
    int32_t ret = GXSYS::interactive();
    return ret;
}
inline int32_t GXSYS_wrap_prompt(const gx_string_type& arg1, str_ref& arg2)
{
    int32_t ret = GXSYS::prompt(arg1, arg2);
    return ret;
}
inline int32_t GXSYS_wrap_script()
{
    int32_t ret = GXSYS::script();
    return ret;
}
inline int32_t GXSYS_wrap_script_record()
{
    int32_t ret = GXSYS::script_record();
    return ret;
}
inline void GXSYS_wrap_set_cursor(const gx_string_type& arg1)
{
    GXSYS::set_cursor(arg1);
}
inline void GXSYS_wrap_set_info_line(const gx_string_type& arg1)
{
    GXSYS::set_info_line(arg1);
}
inline void GXSYS_wrap_set_interactive(int32_t arg1)
{
    GXSYS::set_interactive(arg1);
}
inline void GXSYS_wrap_get_workspace_reg(GXREGPtr arg1)
{
    GXSYS::get_workspace_reg(arg1);
}
inline void GXSYS_wrap_set_workspace_reg(GXREGPtr arg1)
{
    GXSYS::set_workspace_reg(arg1);
}
inline void GXSYS_wrap_encrypt_string(const gx_string_type& arg1, str_ref& arg2, int32_t arg3)
{
    GXSYS::encrypt_string(arg1, arg2, (SYS_ENCRYPTION_KEY)arg3);
}
inline void GXSYS_wrap_decrypt_string(const gx_string_type& arg1, str_ref& arg2, int32_t arg3)
{
    GXSYS::decrypt_string(arg1, arg2, (SYS_ENCRYPTION_KEY)arg3);
}
inline int32_t GXSYS_wrap_is_encrypted_string(const gx_string_type& arg1)
{
    int32_t ret = GXSYS::is_encrypted_string(arg1);
    return ret;
}
inline void GXSYS_wrap_disable_gx_debugger()
{
    GXSYS::disable_gx_debugger();
}
inline void GXSYS_wrap_enable_gx_debugger(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSYS::enable_gx_debugger(arg1, arg2);
}

void gxPythonImportGXSYS()
{

    class_<GXSYS, boost::noncopyable> pyClass("GXSYS",
            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		The SYS library functions perform a wide range functions,\n"
            "   		including the storage and retrieval of named parameters\n"
            "   		from the current workspace; writing messages to the user;\n"
            "   		display of progress bars; retrieving file, date and time\n"
            "   		information from the operating system; and providing warning\n"
            "   		and error handling functions.\n"
            "   	\n\n"

            "\n\n**Note:**\n\n"

            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		PARAMETER CONTROL FUNCTIONS\n"
            "   \n"
            "   		Parameters can be named with an index extension.\n"
            "   		For example, a parameter could be named as \"PARM[1]\".\n"
            "   		The index can be a positive number, or it can be a '\\ `*`\\ '.\n"
            "   \n"
            "   		If the index is a '\\ `*`\\ ' in \"\\ :func:`geosoft.gxapi.GXSYS.set_string`\\ \", then the value string\n"
            "   		will be parsed into multiple values. Commas are assumed to be delimiters.\n"
            "   \n"
            "   		E.g.\n"
            "   \n"
            "   		\\ :func:`geosoft.gxapi.GXSYS.set_string`\\ (\"group1\",\n"
            "   		\"multiparm[\\ `*`\\ ]\",\n"
            "   		\"value1,\\\"value,2\\\",\\\"value 3\\\",  value4  ,\\\"value 5 \\\"\");\n"
            "   \n"
            "   		This call will set   multiparm[0] =\"value1\"\n"
            "   		multiparm[1] =\"value,2\"\n"
            "   		multiparm[2] =\"value 3\"\n"
            "   		multiparm[3] =\"value4\"\n"
            "   		multiparm[4] =\"value 5\"\n"
            "   \n"
            "   		To read a parameter, name the parameter with the index.  Thre is no\n"
            "   		looped-reading ability.  For example:\n"
            "   \n"
            "   		GetString_SYS(\"group1\",\"multiparm[3]\",sSetting);\n"
            "   \n"
            "   		returns sSetting = \"value4\"\n"
            "   	\n\n"
            , no_init);


    pyClass.def("break_date", &GXSYS_wrap_break_date,
                "break_date((float)arg1, (int_ref)arg2, (int_ref)arg3, (int_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Breaks a decimal date value into year, month and day.\n\n"

                ":param arg1: date value to break\n"
                ":type arg1: float\n"
                ":param arg2: year\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: month (0-11)\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: day   (0-30)\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               ).staticmethod("break_date");
    pyClass.def("dateto_long", &GXSYS_wrap_dateto_long,
                "dateto_long((float)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Converts a double date to a value representing total\n"
                "   					days elapsed since day 0 of year 0. This uses the\n"
                "   					Numerical Receipies Julian function.\n"
                "   				\n\n"

                ":param arg1: date\n"
                ":type arg1: float\n"
                ":returns: x - Days\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("dateto_long");
    pyClass.def("timeto_long", &GXSYS_wrap_timeto_long,
                "timeto_long((float)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Converts decimal hours to seconds in a day.\n\n"

                ":param arg1: Time\n"
                ":type arg1: float\n"
                ":returns: x - Seconds (integer)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("timeto_long");
    pyClass.def("date", &GXSYS_wrap_date,
                "date() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the current date in decimal years.\n\n"

                ":returns: Date in decimal years.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The FormatDate_STR function can be used to convert a date to\n"
                "   					a string.\n"
                "   				\n\n"
               ).staticmethod("date");
    pyClass.def("longto_date", &GXSYS_wrap_longto_date,
                "longto_date((int)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Converts a value representing total days elapsed since\n"
                "   					day 0 of year 0 to a geosoft date. This uses the\n"
                "   					Numerical Receipies Julian function.\n"
                "   				\n\n"

                ":param arg1: day\n"
                ":type arg1: int\n"
                ":returns: x - Date\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("longto_date");
    pyClass.def("longto_time", &GXSYS_wrap_longto_time,
                "longto_time((int)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Converts seconds to decimal hours.\n\n"

                ":param arg1: seconds\n"
                ":type arg1: int\n"
                ":returns: x - Time\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("longto_time");
    pyClass.def("make_date", &GXSYS_wrap_make_date,
                "make_date((int)arg1, (int)arg2, (int)arg3) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the decimal date given the year, month and day.\n\n"

                ":param arg1: year\n"
                ":type arg1: int\n"
                ":param arg2: month (0-11)\n"
                ":type arg2: int\n"
                ":param arg3: day   (0-30)\n"
                ":type arg3: int\n"
                ":returns: Date in decimal years.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               ).staticmethod("make_date");
    pyClass.def("secondsto_time", &GXSYS_wrap_secondsto_time,
                "secondsto_time((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Converts fractional seconds to decimal hours.\n\n"

                ":param arg1: seconds\n"
                ":type arg1: float\n"
                ":returns: x - Time\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("secondsto_time");
    pyClass.def("time", &GXSYS_wrap_time,
                "time() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the current time in decimal hours.\n\n"

                ":returns: Time in decimal hours.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The FormatTime_STR function can be used to convert a time to\n"
                "   					a string.\n"
                "   				\n\n"
               ).staticmethod("time");
    pyClass.def("timeto_seconds", &GXSYS_wrap_timeto_seconds,
                "timeto_seconds((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Converts decimal hours to seconds in a day fractional\n\n"

                ":param arg1: Time\n"
                ":type arg1: float\n"
                ":returns: x - Number of seconds with fractions\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("timeto_seconds");
    pyClass.def("utc_date", &GXSYS_wrap_utc_date,
                "utc_date() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the current UTC date in decimal years.\n\n"

                ":returns: Date in decimal years.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The FormatDate_STR function can be used to convert a date to\n"
                "   					a string.\n"
                "   				\n\n"
               ).staticmethod("utc_date");
    pyClass.def("utc_time", &GXSYS_wrap_utc_time,
                "utc_time() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the current UTC time in decimal hours.\n\n"

                ":returns: Time in decimal hours.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The FormatTime_STR function can be used to convert a time to\n"
                "   					a string.\n"
                "   				\n\n"
               ).staticmethod("utc_time");
    pyClass.def("exist_env", &GXSYS_wrap_exist_env,
                "exist_env((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check if setting exists in environment.\n\n"

                ":param arg1: setting\n"
                ":type arg1: str\n"
                ":returns: 1 - Yes\n"
                "          						0 - No\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("exist_env");
    pyClass.def("get_env", &GXSYS_wrap_get_env,
                "get_env((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an environment setting.\n\n"

                ":param arg1: setting\n"
                ":type arg1: str\n"
                ":param arg2: value string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_env");
    pyClass.def("set_env", &GXSYS_wrap_set_env,
                "set_env((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set an environment setting.\n\n"

                ":param arg1: setting\n"
                ":type arg1: str\n"
                ":param arg2: value\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("set_env");
    pyClass.def("clear_err_ap", &GXSYS_wrap_clear_err_ap,
                "clear_err_ap() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method is called at to clear all registered errors.\n\n"

                ":returns: 0 - Successful\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               ).staticmethod("clear_err_ap");
    pyClass.def("get_top_error_ap", &GXSYS_wrap_get_top_error_ap,
                "get_top_error_ap() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the error number of the last registered error.\n\n"

                ":returns: The top error number registered, 0 if none registered.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("get_top_error_ap");
    pyClass.def("get_error_message_ap", &GXSYS_wrap_get_error_message_ap,
                "get_error_message_ap((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the error message text as a string.\n\n"

                ":param arg1: the error index (0 to N-1, where N=number of registered errors)\n"
                ":type arg1: int\n"
                ":param arg2: Buffer to return message in\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This wrapper is mostly for use outside of GXs,\n"
                "   					because in general if an error is registered in a GX\n"
                "   					the GX would terminate before it could be called.\n"
                "   					Use \\ :func:`geosoft.gxapi.GXSYS.num_errors_ap`\\  to get the number of registered errors.\n"
                "   				\n\n"
               ).staticmethod("get_error_message_ap");
    pyClass.def("num_errors_ap", &GXSYS_wrap_num_errors_ap,
                "num_errors_ap() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the number of registered errors.\n\n"

                ":returns: The number of registered errors.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This wrapper is mostly for use outside of GXs,\n"
                "   					because in general if an error is registered in a GX\n"
                "   					the GX would terminate before it could be called.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   GetErrorMessageAP_SYS\n\n"
               ).staticmethod("num_errors_ap");
    pyClass.def("set_server_messages_ap", &GXSYS_wrap_set_server_messages_ap,
                "set_server_messages_ap((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Control the server message handling.\n\n"

                ":param arg1: 1 - Display messages, 0 - messages reported as errors\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Should be set to false when dialogs should not\n"
                "   					appear. This setting is thread specific.\n"
                "   				\n\n"
               ).staticmethod("set_server_messages_ap");
    pyClass.def("run", &GXSYS_wrap_run,
                "run((str)arg1, (str)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Run a command line process.\n\n"

                ":param arg1: command name\n"
                ":type arg1: str\n"
                ":param arg2: command line arguments\n"
                ":type arg2: str\n"
                ":param arg3: Flags \\ :ref:`SYS_RUN_TYPE`\\  \\ :ref:`SYS_RUN_DISPLAY`\\  \\ :ref:`SYS_RUN_HOLD`\\  \\ :ref:`SYS_RUN_WIN`\\ \n"
                ":type arg3: int\n"
                ":returns: -1 if failed to execute task\n"
                "          						Exit status of the task\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The Default option for each define below is the first one\n"
                "   					and is set to 0.\n"
                "   \n"
                "   					We look for the command object in the following order:\n"
                "   \n"
                "   					1. the local working directory\n"
                "   					2. the <geosoft>\\bin directory\n"
                "   					3. the system path\n"
                "   				\n\n"
               ).staticmethod("run");
    pyClass.def("run_gs", &GXSYS_wrap_run_gs,
                "run_gs((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Run a GS.\n\n"

                ":param arg1: name of GS to run.\n"
                ":type arg1: str\n"
                ":returns: Exit status of the GS\n"
                "          						-1 cancelled\n"
                "          						0 success\n"
                "          						1 ended with an error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXSYS.set_interactive`\\ , \\ :func:`geosoft.gxapi.GXSYS.run_gx`\\ \n\n"
               ).staticmethod("run_gs");
    pyClass.def("run_gx", &GXSYS_wrap_run_gx,
                "run_gx((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Run a GX.\n\n"

                ":param arg1: name of GX to run.\n"
                ":type arg1: str\n"
                ":returns: Exit status of the GX:\n"
                "          						-1 cancelled\n"
                "          						0 success\n"
                "          						1 ended with an error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the called GX returns an error, they will not be\n"
                "   					displayed until the \"top\" calling GX terminates, unless you\n"
                "   					call \\ :func:`geosoft.gxapi.GXSYS.show_error`\\ ().\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXSYS.run_gx_ex`\\ , \\ :func:`geosoft.gxapi.GXSYS.set_interactive`\\  and \\ :func:`geosoft.gxapi.GXSYS.run_gs`\\ \n\n"
               ).staticmethod("run_gx");
    pyClass.def("run_gx_ex", &GXSYS_wrap_run_gx_ex,
                "run_gx_ex((str)arg1, (int_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Run a GX.\n\n"

                ":param arg1: name of GX to run.\n"
                ":type arg1: str\n"
                ":param arg2: return value set in the child GX (0 by default)\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Exit status of the GX:\n"
                "          						-1 cancelled\n"
                "          						0 success\n"
                "          						1 ended with an error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXSYS.run_gx`\\ , \\ :func:`geosoft.gxapi.GXSYS.set_return`\\ \n\n"
               ).staticmethod("run_gx_ex");
    pyClass.def("run_pdf", &GXSYS_wrap_run_pdf,
                "run_pdf((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Run a PDF.\n\n"

                ":param arg1: group name, can be \"\".\n"
                ":type arg1: str\n"
                ":param arg2: pdf name    (.pdf assumed)\n"
                ":type arg2: str\n"
                ":returns: Exit status of the task, 0 usually means success.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The group name of the PDF variables will be \"group_pdf\",\n"
                "   					where \"group\" is the name given in the first argument,\n"
                "   					and \"pdf\" is the root PDF file name.\n"
                "   				\n\n"
               ).staticmethod("run_pdf");
    pyClass.def("shell_execute", &GXSYS_wrap_shell_execute,
                "shell_execute((str)arg1, (str)arg2, (str)arg3, (str)arg4, (int)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   MS ShellExecute function\n\n"

                ":param arg1: Verb\n"
                ":type arg1: str\n"
                ":param arg2: File\n"
                ":type arg2: str\n"
                ":param arg3: Parameters\n"
                ":type arg3: str\n"
                ":param arg4: Directory\n"
                ":type arg4: str\n"
                ":param arg5: \\ :ref:`SHELL_EXECUTE`\\ \n"
                ":type arg5: int\n"
                ":returns: return value of ShellExecute command\n"
                "          \n"
                "          						See                ShellExecute description in MSDN\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Examples\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXSYS.shell_execute`\\ (open;http://www.geosoft.com);\n"
                "   					\\ :func:`geosoft.gxapi.GXSYS.shell_execute`\\ (open;\"mailto:geonet@lists.geosoft.com\");\n"
                "   					\\ :func:`geosoft.gxapi.GXSYS.shell_execute`\\ (open;\"mailto:majordomo@lists.geosoft.com?body=UNSUBSCRIBE%20gxnet\");\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXSYS.do_command`\\ \n\n"
               ).staticmethod("shell_execute");
    pyClass.def("set_return", &GXSYS_wrap_set_return,
                "set_return((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the return value of a GX.\n\n"

                ":param arg1: Return Value\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This value is returned in the \\ :func:`geosoft.gxapi.GXSYS.run_gx_ex`\\  call only.\n\n"
               ).staticmethod("set_return");
    pyClass.def("do_command", &GXSYS_wrap_do_command,
                "do_command((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Execute an Oasis montaj command.\n\n"

                ":param arg1: Command\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Commands syntax:  \"[type] command\"\n"
                "   \n"
                "   					type     command\n"
                "   					----     -------\n"
                "   					ID       Internal Menu Command\n"
                "   					See \"Internal Menu Commands\" in GX Developer documentation.\n"
                "   					GX       gx file name\n"
                "   					GS       gs file name\n"
                "   					DOTNET   dll file name\n"
                "   					Use qualifiers to specify class and method e.g. [DOTNET] geogxnet.dll(Geosoft.GX.NewGDB.NewGDB;Run)\n"
                "   					PDF      pdf file name\n"
                "   					DOS      DOS style command\n"
                "   					HLP      help file name\n"
                "   \n"
                "   					The must be ONE space between the \"]\" and the command.  For example:\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXSYS.do_command`\\ (\"[ID] ID_EDIT_SELECT\");  // bring up the line edit tool\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   ShellExecute_SYS\n\n"
               ).staticmethod("do_command");
    pyClass.def("error", &GXSYS_wrap_error,
                "error((str)arg1, (str)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Register an error message\n\n"

                ":param arg1: your error file name, \"\" if none.\n"
                ":type arg1: str\n"
                ":param arg2: module name in which error occured.\n"
                ":type arg2: str\n"
                ":param arg3: error number\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Use this function to register your own error\n"
                "   					messages when an error occurs in your code.  Your\n"
                "   					errors can be provided in your own GER file.  See\n"
                "   					GEOSOFT.GER for an example of the GER file format.\n"
                "   \n"
                "   					If the error # is not found in your error file, the\n"
                "   					OE32.GER file, then the GEOSOFT.GER file will be\n"
                "   					searched.\n"
                "   				\n\n"
               ).staticmethod("error");
    pyClass.def("error_tag", &GXSYS_wrap_error_tag,
                "error_tag((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set an error message tag string\n\n"

                ":param arg1: tag string, ie \"%1\".\n"
                ":type arg1: str\n"
                ":param arg2: string to replace the tag.\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Use this method to replace tag strings in your error\n"
                "   					message text with run-time information.  For example,\n"
                "   					Geosoft error messages often use the tag strings \"%1\",\n"
                "   					\"%2\", etc. as place holders to be replaced by a string\n"
                "   					which is only known at run-time.\n"
                "   				\n\n"
               ).staticmethod("error_tag");
    pyClass.def("assert_gx", &GXSYS_wrap__assert_gx,
                "assert_gx((int)arg1, (str)arg2, (str)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   DLL function argument error assertion\n\n"

                ":param arg1: boolean expression (ie. (dB != 0.0) )\n"
                ":type arg1: int\n"
                ":param arg2: module name\n"
                ":type arg2: str\n"
                ":param arg3: argument name\n"
                ":type arg3: str\n"
                ":returns: 0 assertion passed\n"
                "          						1 assertion failed\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Use this function to evaluate errors in passed\n"
                "   					function arguments.  Functions called by GX programs\n"
                "   					should be tolerant of all errors in the passed argument\n"
                "   					list.  The \\ :func:`geosoft.gxapi.GXSYS.assert_gx`\\  can be used to test each\n"
                "   					argument before doing any work in the function.  If\n"
                "   					an assertion fails, an error will be registered with\n"
                "   					the name of the function and the parameter name and\n"
                "   					a 1 will be returned.  The caller should immediatley\n"
                "   					cleaning up (if necessary) and return.\n"
                "   \n"
                "   					You could also test the validity of arguments and call\n"
                "   					the \\ :func:`geosoft.gxapi.GXSYS.error`\\ , \\ :func:`geosoft.gxapi.GXSYS.error_tag`\\  and \\ :func:`geosoft.gxapi.GXSYS.terminate`\\ \n"
                "   					functions if you would like to provide a more specific\n"
                "   					error message.\n"
                "   				\n\n"
               ).staticmethod("assert_gx");
    pyClass.def("ole_automation", &GXSYS_wrap_ole_automation,
                "ole_automation((str)arg1, (str)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Call OLE Automation designed to be called from Montaj.\n\n"

                ":param arg1: Object Name\n"
                ":type arg1: str\n"
                ":param arg2: Info String\n"
                ":type arg2: str\n"
                ":param arg3: Info Int\n"
                ":type arg3: int\n"
                ":returns: Return from automation engine.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("ole_automation");
    pyClass.def("save_log", &GXSYS_wrap_save_log,
                "save_log((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Saves the main log file to another file.\n\n"

                ":param arg1: output file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("save_log");
    pyClass.def("show_error", &GXSYS_wrap_show_error,
                "show_error() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display any errors to the user.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If you call a GX from another GX using \\ :func:`geosoft.gxapi.GXSYS.run_gx`\\ , and\n"
                "   					the called GX registers errors, they will not be displayed\n"
                "   					until after the \"top\" GX exits.\n"
                "   					If you wish to continue without exiting, call this function\n"
                "   					so that errors are displayed immediately to the user. For\n"
                "   					instance, when creating a new map from inside another GX:\n"
                "   \n"
                "   					--- Run NEWMAP wizard. Keep trying if something is wrong (like a\n"
                "   					too-small map scale), but exit if the user cancels (iRet==-1) ---\n"
                "   \n"
                "   					do {\n"
                "   					iRet = \\ :func:`geosoft.gxapi.GXSYS.run_gx`\\ (\"newmap.gx\");\n"
                "   					if(iRet==1) \\ :func:`geosoft.gxapi.GXSYS.show_error`\\ ();     // Dump errors.\n"
                "   					} while(iRet==1);\n"
                "   \n"
                "   					This wrapper is not intended for use outside a GX, because it\n"
                "   					uses the GX run-time machinery to display the error messages.\n"
                "   				\n\n"
               ).staticmethod("show_error");
    pyClass.def("terminate", &GXSYS_wrap_terminate,
                "terminate((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   DLL error termination\n\n"

                ":param arg1: module name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Call this function immediately before returning to\n"
                "   					the caller after an error has occured inside the\n"
                "   					DLL.  If an error has occured, you should clean-up\n"
                "   					(free memory, close files), call \\ :func:`geosoft.gxapi.GXSYS.error`\\  to register\n"
                "   					your own error messages, call \\ :func:`geosoft.gxapi.GXSYS.error_tag`\\  to set any\n"
                "   					error message tags, call \\ :func:`geosoft.gxapi.GXSYS.terminate`\\  and return.\n"
                "   \n"
                "   					Geosoft functions that detect an error will have\n"
                "   					already registered their own errors and called\n"
                "   					\\ :func:`geosoft.gxapi.GXSYS.terminate`\\ .\n"
                "   				\n\n"
               ).staticmethod("terminate");
    pyClass.def("crc_file", &GXSYS_wrap_crc_file,
                "crc_file((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute the CRC of a file\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":returns: CRC Value\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               ).staticmethod("crc_file");
    pyClass.def("crc_file_offset", &GXSYS_wrap_crc_file_offset,
                "crc_file_offset((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute the CRC of a file with an Offset\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":param arg2: Offset in the file (0 for start)\n"
                ":type arg2: int\n"
                ":returns: CRC Value\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               ).staticmethod("crc_file_offset");
    pyClass.def("file_ren", &GXSYS_wrap_file_ren,
                "file_ren((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Rename a file\n\n"

                ":param arg1: Old file name\n"
                ":type arg1: str\n"
                ":param arg2: New file name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("file_ren");
    pyClass.def("find_files_vv", &GXSYS_wrap_find_files_vv,
                "find_files_vv((GXVV)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill a VV with files matching an input file mask.\n\n"

                ":param arg1: VV object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: File mask to match\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Fill a VV with files matching the input file mask.\n"
                "   					The VV should be of string type.\n"
                "   				\n\n"
               ).staticmethod("find_files_vv");
    pyClass.def("absolute_file_name", &GXSYS_wrap_absolute_file_name,
                "absolute_file_name((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert an abbreviated path name to a full path name.\n\n"

                ":param arg1: Input file name to resolve\n"
                ":type arg1: str\n"
                ":param arg2: Output name, can be the same as input\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is mainly intended to convert \".\\name\" to a full\n"
                "   					name at run-time.\n"
                "   				\n\n"
               ).staticmethod("absolute_file_name");
    pyClass.def("copy_file", &GXSYS_wrap_copy_file,
                "copy_file((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a file.\n\n"

                ":param arg1: source file\n"
                ":type arg1: str\n"
                ":param arg2: destination file\n"
                ":type arg2: str\n"
                ":returns: 0 if file copied ok.\n"
                "          						1 if unable to copy file or source file not found.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               ).staticmethod("copy_file");
    pyClass.def("delete_file", &GXSYS_wrap_delete_file,
                "delete_file((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete a file.\n\n"

                ":param arg1: name of file to delete\n"
                ":type arg1: str\n"
                ":returns: 0 if file deleted.\n"
                "          						1 if unable to find file or delete file.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("delete_file");
    pyClass.def("delete_gi_file", &GXSYS_wrap_delete_gi_file,
                "delete_gi_file((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete the GI file associated with a grid.\n\n"

                ":param arg1: name of grid file to delete\n"
                ":type arg1: str\n"
                ":returns: 0 if file deleted.\n"
                "          						1 if file is not found, or found but could not be deleted.\n"
                "          \n"
                "          						This is a \"one-line\" function to take a grid file name,\n"
                "          						remove the qualifiers, add the \".gi\" and delete the file.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("delete_gi_file");
    pyClass.def("delete_grid_file", &GXSYS_wrap_delete_grid_file,
                "delete_grid_file((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete a grid file and its associated GI and XML files.\n\n"

                ":param arg1: name of grid file to delete\n"
                ":type arg1: str\n"
                ":returns: 0 if grid file deleted.\n"
                "          						1 if grid file not found or if one or more files is found but could not be deleted.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Deletes the grid file first, and, if they exist, the associated GI\n"
                "   					and XML files.\n"
                "   					No error is registered if a file is not found or cannot be deleted.\n"
                "   				\n\n"
               ).staticmethod("delete_grid_file");
    pyClass.def("dir_exist", &GXSYS_wrap_dir_exist,
                "dir_exist((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check to see if a directory exists\n\n"

                ":param arg1: Name of directory to check\n"
                ":type arg1: str\n"
                ":returns: 0 - Directory doesn't exist\n"
                "          						1 - Directory exists\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("dir_exist");
    pyClass.def("file_exist", &GXSYS_wrap_file_exist,
                "file_exist((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check to see if a file exists\n\n"

                ":param arg1: Name of file to check\n"
                ":type arg1: str\n"
                ":returns: 0 - File doesn't exist\n"
                "          						1 - File exists\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Use the FULL path for the file name. If the full\n"
                "   					path is not specified, then the current working\n"
                "   					directory is used for the path.\n"
                "   				\n\n"
               ).staticmethod("file_exist");
    pyClass.def("file_size", &GXSYS_wrap_file_size,
                "file_size((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns size of a file.\n\n"

                ":param arg1: name of file\n"
                ":type arg1: str\n"
                ":returns: 0 none/error\n"
                "          						x Size\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("file_size");
    pyClass.def("file_writable", &GXSYS_wrap_file_writable,
                "file_writable((str)arg1) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Check if a file can be created or opened in read-write mode\n"
                "   					at a specific location\n"
                "   				\n\n"

                ":param arg1: File path name to check\n"
                ":type arg1: str\n"
                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("file_writable");
    pyClass.def("find_path", &GXSYS_wrap_find_path,
                "find_path((str)arg1, (int)arg2, (str_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get full path for a file with Geosoft subdirectory parameter.\n\n"

                ":param arg1: File to get path name for\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`SYS_SEARCH_PATH`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Buffer to place path name into\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 if file found.\n"
                "          						1 if file not found.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Directories can be resolved from the Environment section of the\n"
                "   					Geosoft registry, or from system environment variables that are\n"
                "   					not defined in the Geosoft Environment registry.  The following\n"
                "   					file prefixes will be replaced by the environment settings:\n"
                "   \n"
                "   					<geosoft>      the main Geosoft installation directory\n"
                "   					<geosoft2>     the secondary Geosoft installation directory\n"
                "   					<geotemp>      the Geosoft temporary file directory\n"
                "   					<windows>      the operating system Windows directory\n"
                "   					<system>       the operating system system directory\n"
                "   					<other>        other environment variables\n"
                "   				\n\n"
               ).staticmethod("find_path");
    pyClass.def("find_path_ex", &GXSYS_wrap_find_path_ex,
                "find_path_ex((str)arg1, (int)arg2, (int)arg3, (str_ref)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get full path for a file.\n\n"

                ":param arg1: File to get path name for\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`SYS_SEARCH_PATH`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`GEO_DIRECTORY`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Buffer to place path name into\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 if file found.\n"
                "          						1 if file not found.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Directories can be resolved from the Environment section of the\n"
                "   					Geosoft registry, or from system environment variables that are\n"
                "   					not defined in the Geosoft Environment registry.  The following\n"
                "   					file prefixes will be replaced by the environment settings:\n"
                "   \n"
                "   					<geosoft>      the main Geosoft installation directory\n"
                "   					<geosoft2>     the secondary Geosoft installation directory\n"
                "   					<geotemp>      the Geosoft temporary file directory\n"
                "   					<windows>      the operating system Windows directory\n"
                "   					<system>       the operating system system directory\n"
                "   					<other>        other environment variable\n"
                "   				\n\n"
               ).staticmethod("find_path_ex");
    pyClass.def("get_directory", &GXSYS_wrap_get_directory,
                "get_directory((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a directory path\n\n"

                ":param arg1: \\ :ref:`SYS_DIR`\\ \n"
                ":type arg1: int\n"
                ":param arg2: returned directory path string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The path will always end with the file separator character\n\n"
               ).staticmethod("get_directory");
    pyClass.def("get_path", &GXSYS_wrap_get_path,
                "get_path((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a Geosoft path\n\n"

                ":param arg1: \\ :ref:`SYS_PATH`\\ \n"
                ":type arg1: int\n"
                ":param arg2: string in which to place path\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The path name will have a directory separator at the end.\n\n"
               ).staticmethod("get_path");
    pyClass.def("get_windows_dir", &GXSYS_wrap_get_windows_dir,
                "get_windows_dir((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Windows directory path\n\n"

                ":param arg1: Buff for directory path string\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_windows_dir");
    pyClass.def("make_dir", &GXSYS_wrap_make_dir,
                "make_dir((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a directory.\n\n"

                ":param arg1: Name of directory\n"
                ":type arg1: str\n"
                ":returns: 0 - Directory made\n"
                "          						1 - Directory cannot be made\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("make_dir");
    pyClass.def("make_file_readonly", &GXSYS_wrap_make_file_readonly,
                "make_file_readonly((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a file's read-only attribute.\n\n"

                ":param arg1: name of file\n"
                ":type arg1: str\n"
                ":returns: 0 if read-only attribute successfully set,\n"
                "          						1 if attribute change fails.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("make_file_readonly");
    pyClass.def("make_file_writable", &GXSYS_wrap_make_file_writable,
                "make_file_writable((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Removes a file's read-only attribute.\n\n"

                ":param arg1: name of file\n"
                ":type arg1: str\n"
                ":returns: 0 if read-only attribute successfully removed,\n"
                "          						1 if attribute change fails.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("make_file_writable");
    pyClass.def("relative_file_name", &GXSYS_wrap_relative_file_name,
                "relative_file_name((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a file name to a relative abbreviated path name\n\n"

                ":param arg1: Input file name to resolve\n"
                ":type arg1: str\n"
                ":param arg2: Output name, can be the same as input\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This will produce relative paths based on the workspace\n"
                "   					directory into \".\\name\".\n"
                "   				\n\n"
               ).staticmethod("relative_file_name");
    pyClass.def("short_path_file_name", &GXSYS_wrap_short_path_file_name,
                "short_path_file_name((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Obtains the short path form of a specified input path.\n\n"

                ":param arg1: Input file name to resolve\n"
                ":type arg1: str\n"
                ":param arg2: Output name, can be the same as input\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("short_path_file_name");
    pyClass.def("temp_file_ext", &GXSYS_wrap_temp_file_ext,
                "temp_file_ext((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a unique file name for this extension in the temp directory.\n\n"

                ":param arg1: Input Extesion (without .)\n"
                ":type arg1: str\n"
                ":param arg2: Output name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This is useful for created a unique tempory name for a file in the Geosoft temporary directory.\n\n"
               ).staticmethod("temp_file_ext");
    pyClass.def("temp_file_name", &GXSYS_wrap_temp_file_name,
                "temp_file_name((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a file name for this file in the temp directory.\n\n"

                ":param arg1: Input file name to resolve (path is removed)\n"
                ":type arg1: str\n"
                ":param arg2: Output name, can be the same as input\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is useful for created a unique tempory name for a file in the Geosoft temporary directory.\n"
                "   \n"
                "   					From version 7.0 The file extension will match the input file, but the\n"
                "   					filename itself will be a process and thread unique value to ensure that\n"
                "   					clashes does not happen.\n"
                "   				\n\n"
               ).staticmethod("temp_file_name");
    pyClass.def("transfer_path", &GXSYS_wrap_transfer_path,
                "transfer_path((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Transfers file path to new file name.\n\n"

                ":param arg1: input file path/name\n"
                ":type arg1: str\n"
                ":param arg2: output file name with path transfered\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The path and volume of from the input string is added to\n"
                "   					file name from the output string.\n"
                "   				\n\n"
               ).staticmethod("transfer_path");
    pyClass.def("valid_file_name", &GXSYS_wrap_valid_file_name,
                "valid_file_name((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check to see if a file name valid\n\n"

                ":param arg1: Name of file to check\n"
                ":type arg1: str\n"
                ":returns: 0 - File name is not valid\n"
                "          						1 - File name is valid\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Use the FULL path for the file name. If the full\n"
                "   					path is not specified, then the current working\n"
                "   					directory is used for the path.\n"
                "   				\n\n"
               ).staticmethod("valid_file_name");
    pyClass.def("write_in_dir", &GXSYS_wrap_write_in_dir,
                "write_in_dir((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Can I create files in this directory ?\n\n"

                ":param arg1: Name of directory to check\n"
                ":type arg1: str\n"
                ":returns: 0 - Directory doesn't allow write of does not exist\n"
                "          						1 - Directory allows writes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("write_in_dir");
    pyClass.def("file_date", &GXSYS_wrap_file_date,
                "file_date((str)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   File creation date in decimal years.\n\n"

                ":param arg1: file name\n"
                ":type arg1: str\n"
                ":returns: Date in decimal years, rDUMMY if the file does not exist.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The FormatDate_STR function can be used to convert a date\n"
                "   					to a string.\n"
                "   				\n\n"
               ).staticmethod("file_date");
    pyClass.def("file_time", &GXSYS_wrap_file_time,
                "file_time((str)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   File creation time in decimal hours.\n\n"

                ":param arg1: file name\n"
                ":type arg1: str\n"
                ":returns: Date in decimal hours, rDUMMY if the file does not exist.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The FormatTime_STR function can be used to convert a time\n"
                "   					to a string.\n"
                "   				\n\n"
               ).staticmethod("file_time");
    pyClass.def("utc_file_date", &GXSYS_wrap_utc_file_date,
                "utc_file_date((str)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   File creation UTC date in decimal years.\n\n"

                ":param arg1: file name\n"
                ":type arg1: str\n"
                ":returns: Date in decimal years, rDUMMY if the file does not exist.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The FormatDate_STR function can be used to convert a date\n"
                "   					to a string.\n"
                "   				\n\n"
               ).staticmethod("utc_file_date");
    pyClass.def("utc_file_time", &GXSYS_wrap_utc_file_time,
                "utc_file_time((str)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   File creation UTC time in decimal hours.\n\n"

                ":param arg1: file name\n"
                ":type arg1: str\n"
                ":returns: Date in decimal hours, rDUMMY if the file does not exist.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The FormatTime_STR function can be used to convert a time\n"
                "   					to a string.\n"
                "   				\n\n"
               ).staticmethod("utc_file_time");
    pyClass.def("get_settings_meta", &GXSYS_wrap_get_settings_meta,
                "get_settings_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the settings metadata object.\n\n"

                ":param arg1: META object to store the settings metadata in\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               ).staticmethod("get_settings_meta");
    pyClass.def("global_reset", &GXSYS_wrap_global_reset,
                "global_reset((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reset the global parameters.\n\n"

                ":param arg1: new INI file name, if \"\", use default.\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("global_reset");
    pyClass.def("global_set", &GXSYS_wrap_global_set,
                "global_set((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a global parameter setting.\n\n"

                ":param arg1: Name of the Parameter\n"
                ":type arg1: str\n"
                ":param arg2: Setting\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("global_set");
    pyClass.def("global_write", &GXSYS_wrap_global_write,
                "global_write((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify the global parameters.\n\n"

                ":param arg1: Global INI file, if \"\" use default.\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the global parameters have been changed, use\n"
                "   					this function to make the changes permanent,\n"
                "   				\n\n"
               ).staticmethod("global_write");
    pyClass.def("global", &GXSYS_wrap_global,
                "global((str)arg1, (str_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a global parameter setting.\n\n"

                ":param arg1: Name of the Parameter\n"
                ":type arg1: str\n"
                ":param arg2: Setting returned\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 if parameter found.\n"
                "          						1 if parameter not found or not set.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The returned string will be empty if the parameter is\n"
                "   					not found.\n"
                "   \n"
                "   					Parameters are derived from GEOSOFT.INI.\n"
                "   					This is a standard Windows style INI\n"
                "   					file that contains [GROUPS], PARAMETERS and SETTINGS\n"
                "   					as follows\n"
                "   \n"
                "   					[GROUP1]\n"
                "   					PARAM1=setting1\n"
                "   					PARAM2 setting2\n"
                "   					PARAM3 \"setting3 is text\"\n"
                "   \n"
                "   					To retrieve an entry, specify the group.parameter.  For\n"
                "   					example, iGlobal_SYS(\"GROUP1.PARAM3\",sSetting) will\n"
                "   					retrieve the string \"setting is text\".  The double\n"
                "   					quotes will not appear in the setting.\n"
                "   				\n\n"
               ).staticmethod("global");
    pyClass.def("reset_settings", &GXSYS_wrap_reset_settings,
                "reset_settings() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Resets the GX_HELP settings in the geosoft.ini file\n"
                "   					after changes have been made.\n"
                "   				\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               ).staticmethod("reset_settings");
    pyClass.def("set_settings_meta", &GXSYS_wrap_set_settings_meta,
                "set_settings_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the settings metadata object.\n\n"

                ":param arg1: META object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               ).staticmethod("set_settings_meta");
    pyClass.def("check_arc_license", &GXSYS_wrap_check_arc_license,
                "check_arc_license() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check to see if a ESRI ArcEngine or ArcView license is available\n\n"

                ":returns: 1 - Licenced\n"
                "          						0 - Not licenced\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               ).staticmethod("check_arc_license");
    pyClass.def("check_arc_license_ex", &GXSYS_wrap_check_arc_license_ex,
                "check_arc_license_ex((str_ref)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check to see if a ESRI ArcEngine or ArcView license is available, returns type and version of available engine.\n\n"

                ":param arg1: Version String\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: \\ :ref:`ARC_LICENSE`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("check_arc_license_ex");
    pyClass.def("check_intrinsic", &GXSYS_wrap_check_intrinsic,
                "check_intrinsic((int)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check to see if an intrinsic object is licensed\n\n"

                ":param arg1: Intrinsic Class Number\n"
                ":type arg1: int\n"
                ":param arg2: Intrinsic Name (must be exact)\n"
                ":type arg2: str\n"
                ":returns: 1 - Licenced\n"
                "          						0 - Not licenced\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               ).staticmethod("check_intrinsic");
    pyClass.def("get_geodist", &GXSYS_wrap_get_geodist,
                "get_geodist() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Gets a global flag that indicates whether we are\n"
                "   					running within the geodist library\n"
                "   				\n\n"

                ":returns: 0 - Geodist not loaded, 1 - Geodist loaded\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("get_geodist");
    pyClass.def("get_license_class", &GXSYS_wrap_get_license_class,
                "get_license_class((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the current application license class.\n\n"

                ":param arg1: Class String\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					String may be one of :  \"ArcGIS\"\n"
                "   					\"OasisMontaj\"\n"
                "   					\"DapServer\"\n"
                "   				\n\n"
               ).staticmethod("get_license_class");
    pyClass.def("get_licensed_user", &GXSYS_wrap_get_licensed_user,
                "get_licensed_user((str_ref)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the licensed user name and Company\n\n"

                ":param arg1: User Name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: Company Name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               ).staticmethod("get_licensed_user");
    pyClass.def("add_lineage_parameter", &GXSYS_wrap_add_lineage_parameter,
                "add_lineage_parameter((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a parameter to the current lineage object\n\n"

                ":param arg1: Paramter Name\n"
                ":type arg1: str\n"
                ":param arg2: Parameter Value\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("add_lineage_parameter");
    pyClass.def("add_lineage_source", &GXSYS_wrap_add_lineage_source,
                "add_lineage_source((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a source to the current lineage object\n\n"

                ":param arg1: \\ :ref:`SYS_LINEAGE_SOURCE`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Source Name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("add_lineage_source");
    pyClass.def("clear_lineage_parameters", &GXSYS_wrap_clear_lineage_parameters,
                "clear_lineage_parameters() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clear all the lineage parameters\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("clear_lineage_parameters");
    pyClass.def("clear_lineage_sources", &GXSYS_wrap_clear_lineage_sources,
                "clear_lineage_sources() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clear all the lineage sources\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("clear_lineage_sources");
    pyClass.def("copy_geo_file", &GXSYS_wrap_copy_geo_file,
                "copy_geo_file((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a Geosoft data file and all associated files to a new folder\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":param arg2: target directory\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Grids are copied and the GI's are maintained - note that support\n"
                "   					for non-geosoft grids is limited since this method does not\n"
                "   					guarantee all grid files besides the main one are copied.\n"
                "   				\n\n"
               ).staticmethod("copy_geo_file");
    pyClass.def("backup_geo_file", &GXSYS_wrap_backup_geo_file,
                "backup_geo_file((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Backup a Geosoft data file and all associated files to a temporary folder.\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":param arg2: Buffer to place the target name into\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Grids are copied and the GI's are maintained - note that support\n"
                "   					for non-geosoft grids is limited since this method does not\n"
                "   					guarantee all grid files besides the main one are copied.\n"
                "   				\n\n"
               ).staticmethod("backup_geo_file");
    pyClass.def("remove_lineage_output", &GXSYS_wrap_remove_lineage_output,
                "remove_lineage_output((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove an output from the current lineage object\n\n"

                ":param arg1: Source Name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.1\n\n"
               ).staticmethod("remove_lineage_output");
    pyClass.def("remove_lineage_parameter", &GXSYS_wrap_remove_lineage_parameter,
                "remove_lineage_parameter((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove a parameter in the current lineage object\n\n"

                ":param arg1: Paramter Name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("remove_lineage_parameter");
    pyClass.def("remove_lineage_source", &GXSYS_wrap_remove_lineage_source,
                "remove_lineage_source((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove a source from the current lineage object\n\n"

                ":param arg1: Source Name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("remove_lineage_source");
    pyClass.def("restore_geo_file", &GXSYS_wrap_restore_geo_file,
                "restore_geo_file((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Backup a Geosoft data file and all associated files to original location\n\n"

                ":param arg1: Backup File Name\n"
                ":type arg1: str\n"
                ":param arg2: Original file name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Grids are copied and the GI's are maintained - note that support\n"
                "   					for non-geosoft grids is limited since this method does not\n"
                "   					guarantee all grid files besides the main one are copied.\n"
                "   				\n\n"
               ).staticmethod("restore_geo_file");
    pyClass.def("set_lineage_description", &GXSYS_wrap_set_lineage_description,
                "set_lineage_description((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the description for the current lineage object\n\n"

                ":param arg1: Description\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("set_lineage_description");
    pyClass.def("set_lineage_display_name", &GXSYS_wrap_set_lineage_display_name,
                "set_lineage_display_name((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the display name for the current lineage object\n\n"

                ":param arg1: DisplayName\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("set_lineage_display_name");
    pyClass.def("set_lineage_name", &GXSYS_wrap_set_lineage_name,
                "set_lineage_name((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the name for the current lineage object\n\n"

                ":param arg1: Name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("set_lineage_name");
    pyClass.def("clear_menus", &GXSYS_wrap_clear_menus,
                "clear_menus((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clear all menus\n\n"

                ":param arg1: \\ :ref:`SYS_MENU_CLEAR`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("clear_menus");
    pyClass.def("get_loaded_menus", &GXSYS_wrap_get_loaded_menus,
                "get_loaded_menus((GXLST)arg1, (GXLST)arg2, (GXLST)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the loaded menus.\n\n"

                ":param arg1: default menus (typically a single entry based on product)\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: loaded menus\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: loaded user menus\n"
                ":type arg3: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The names of the LSTs contain the menus and the values contain any exclusions. Exlusions \n"
                "   					are semicolon separated top level menu names and/or toolbar.geobar file names.\n"
                "   				\n\n"
               ).staticmethod("get_loaded_menus");
    pyClass.def("set_loaded_menus", &GXSYS_wrap_set_loaded_menus,
                "set_loaded_menus((GXLST)arg1, (GXLST)arg2, (GXLST)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a list of menus\n\n"

                ":param arg1: default menus (typically a single entry based on product, do not change the name returned by GetLoadedMenus_SYS)\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: loaded menus\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: loaded user menus\n"
                ":type arg3: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The names of the LSTs contain the menus and the values contain any exclusions. Exlusions \n"
                "   					are semicolon separated top level menu names and/or toolbar.geobar file names.\n"
                "   				\n\n"
               ).staticmethod("set_loaded_menus");
    pyClass.def("get_entitlement_rights", &GXSYS_wrap_get_entitlement_rights,
                "get_entitlement_rights((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Entitlement Rights\n\n"

                ":param arg1: Rights\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("get_entitlement_rights");
    pyClass.def("generate_guid", &GXSYS_wrap_generate_guid,
                "generate_guid((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Genrates a GUID string (e.g. {4FEDE8BF-CDAB-430A-8026-1CCC0EC0A2EB})\n\n"

                ":param arg1: GUID\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("generate_guid");
    pyClass.def("clipboard_to_file", &GXSYS_wrap_clipboard_to_file,
                "clipboard_to_file((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy text from the clipboard to a file.\n\n"

                ":param arg1: File name to place it into\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("clipboard_to_file");
    pyClass.def("create_clipboard_ra", &GXSYS_wrap_create_clipboard_ra,
                "create_clipboard_ra() -> GXRA:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a RA to read text from the clipboard.\n\n"

                ":returns: RA to use for reading.\n"
                ":rtype: :class:`geosoft.gxapi.GXRA`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Destroy the RA as soon as possible. As long as it\n"
                "   					open the clipboard is not accessible from any\n"
                "   					application.\n"
                "   				\n\n"
               ).staticmethod("create_clipboard_ra");
    pyClass.def("create_clipboard_wa", &GXSYS_wrap_create_clipboard_wa,
                "create_clipboard_wa() -> GXWA:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a WA to write text on the clipboard.\n\n"

                ":returns: WA to use for reading.\n"
                ":rtype: :class:`geosoft.gxapi.GXWA`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Destroy the WA as soon as possible. As long as it\n"
                "   					open the clipboard is not accessible from any\n"
                "   					application.\n"
                "   				\n\n"
               ).staticmethod("create_clipboard_wa");
    pyClass.def("emf_object_size", &GXSYS_wrap_emf_object_size,
                "emf_object_size((str)arg1, (float_ref)arg2, (float_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the size of an EMF object\n\n"

                ":param arg1: EMF File holding data\n"
                ":type arg1: str\n"
                ":param arg2: Size X\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Size Y\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               ).staticmethod("emf_object_size");
    pyClass.def("file_to_clipboard", &GXSYS_wrap_file_to_clipboard,
                "file_to_clipboard((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a text file onto the clipboard as text.\n\n"

                ":param arg1: File place into clipboard\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("file_to_clipboard");
    pyClass.def("font_lst", &GXSYS_wrap_font_lst,
                "font_lst((GXLST)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   List all Windows and geosoft fonts.\n\n"

                ":param arg1: List Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`SYS_FONT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					To get TT and GFN fonts, call twice with the same list\n"
                "   					and SYS_FONT_TT, then SYS_FONT_GFN, or vice-versa to\n"
                "   					change order of listing.\n"
                "   				\n\n"
               ).staticmethod("font_lst");
    pyClass.def("get_dot_net_gx_entries", &GXSYS_wrap_get_dot_net_gx_entries,
                "get_dot_net_gx_entries((str)arg1, (str_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Get the list of entry points that this assembly has\n"
                "   					exposed to Oasis montaj.\n"
                "   				\n\n"

                ":param arg1: name of .NET GX assembly\n"
                ":type arg1: str\n"
                ":param arg2: buffer to place list of entries in\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0  success\n"
                "          						1  error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The list of entry points are passed back as one\n"
                "   					string with each entry point seperated by a semi-colon.\n"
                "   					For example: NewGDB\\ `|`\\ Run;NewGDB\\ `|`\\ RunEx\n"
                "   				\n\n"
               ).staticmethod("get_dot_net_gx_entries");
    pyClass.def("send_general_message", &GXSYS_wrap_send_general_message,
                "send_general_message((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Send a general information message to all listners\n\n"

                ":param arg1: Message Class\n"
                ":type arg1: str\n"
                ":param arg2: Message Info\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("send_general_message");
    pyClass.def("write_debug_log", &GXSYS_wrap_write_debug_log,
                "write_debug_log((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method writes out information to the output\n"
                "   					debugging log file (in temp folder) or output window.\n"
                "   				\n\n"

                ":param arg1: String to Write out\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("write_debug_log");
    pyClass.def("get_thread_id", &GXSYS_wrap_get_thread_id,
                "get_thread_id() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the ID the current thread.\n\n"

                ":returns: x - ID\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   In a single threaded application this will always be 0.\n\n"
               ).staticmethod("get_thread_id");
    pyClass.def("run_multi_user_script", &GXSYS_wrap_run_multi_user_script,
                "run_multi_user_script((str)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Execute a script using multithreaded users\n\n"

                ":param arg1: Script to run\n"
                ":type arg1: str\n"
                ":param arg2: Number of users to run\n"
                ":type arg2: int\n"
                ":param arg3: Number of iterations to run (for each user)\n"
                ":type arg3: int\n"
                ":param arg4: Minimum wait time between iterations (0 for none)\n"
                ":type arg4: int\n"
                ":param arg5: Maximum wait time between iterations (0 for none)\n"
                ":type arg5: int\n"
                ":param arg6: Ramp up time for users (0 for all users start immediatly)\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					No access is provided in the script to EMAPS\n"
                "   					or EDBS. Users must ensure that the resources\n"
                "   					that are shared are protected.\n"
                "   				\n\n"
               ).staticmethod("run_multi_user_script");
    pyClass.def("clear_group", &GXSYS_wrap_clear_group,
                "clear_group((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clear current contents of a group\n\n"

                ":param arg1: group to clear\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("clear_group");
    pyClass.def("clear_group_parm", &GXSYS_wrap_clear_group_parm,
                "clear_group_parm((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clears all paramters in a specified group.\n\n"

                ":param arg1: string\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               ).staticmethod("clear_group_parm");
    pyClass.def("clear_parm", &GXSYS_wrap_clear_parm,
                "clear_parm() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clears all paramters.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("clear_parm");
    pyClass.def("default_int", &GXSYS_wrap_default_int,
                "default_int((str)arg1, (str)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Allows a default int to be set.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Parameter Name\n"
                ":type arg2: str\n"
                ":param arg3: Int Value to Set\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The value will only be set if there is no existing\n"
                "   					setting.\n"
                "   				\n\n"
               ).staticmethod("default_int");
    pyClass.def("default_double", &GXSYS_wrap_default_double,
                "default_double((str)arg1, (str)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Allows a default real to be set.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Parameter Name\n"
                ":type arg2: str\n"
                ":param arg3: Real Value to Set\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The value will only be set if there is no existing\n"
                "   					setting.\n"
                "   				\n\n"
               ).staticmethod("default_double");
    pyClass.def("default_string", &GXSYS_wrap_default_string,
                "default_string((str)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Allows a default string to be set.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Parameter Name\n"
                ":type arg2: str\n"
                ":param arg3: String to Set it To\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The value will only be set if there is no existing\n"
                "   					setting.\n"
                "   				\n\n"
               ).staticmethod("default_string");
    pyClass.def("get_pattern", &GXSYS_wrap_get_pattern,
                "get_pattern((str)arg1, (int_ref)arg2, (float_ref)arg3, (int_ref)arg4, (float_ref)arg5, (int_ref)arg6, (int_ref)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets pattern parameters from the parameter block.\n\n"

                ":param arg1: Input group name\n"
                ":type arg1: str\n"
                ":param arg2: Pattern\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Size,\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Thick (0-100)\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: Density,\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Pattern Color\n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg7: Background Color\n"
                ":type arg7: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Gets all the user-definable pattern parameters from\n"
                "   					a specified group. Parameters are:\n"
                "   					\"PAT_NUMBER\"    0 is solid fill (default)\n"
                "   					\"PAT_SIZE\"      pattern tile size in mm. (can return iDUMMY)\n"
                "   					\"PAT_THICKNESS\" pattern line thickness in percent of the tile size.\n"
                "   					valid range is 0-100.\n"
                "   					\"PAT_DENSITY\"   Tile spacing. A value of 1 means tiles are laid with no overlap.\n"
                "   					A value of 2 means they overlap each other.\n"
                "   					\"PAT_COLOR\"     The colour value.\n"
                "   					\"PAT_BACKCOLOR\" Background colour value.\n"
                "   \n"
                "   					Returned values may be DUMMY, but will be acceptable for use with\n"
                "   					the \\ :func:`geosoft.gxapi.GXGUI.color_form`\\  function, to set defaults.\n"
                "   				\n\n"
               ).staticmethod("get_pattern");
    pyClass.def("get_reg", &GXSYS_wrap_get_reg,
                "get_reg((GXREG)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get REG parameters.\n\n"

                ":param arg1: REG to add parameters to\n"
                ":type arg1: :class:`geosoft.gxapi.GXREG`\n"
                ":param arg2: group name wanted\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_reg");
    pyClass.def("gt_string", &GXSYS_wrap_gt_string,
                "gt_string((str)arg1, (str)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns a string in the parameter block.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Parameter Name\n"
                ":type arg2: str\n"
                ":param arg3: Buffer to place the string into\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the setting exits it is placed in the buffer, otherwise\n"
                "   					the buffer will have zero length\n"
                "   				\n\n"
               ).staticmethod("gt_string");
    pyClass.def("exist_int", &GXSYS_wrap_exist_int,
                "exist_int((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method checks to see if a int parameter exists.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Parameter Name\n"
                ":type arg2: str\n"
                ":returns: 1 - Yes\n"
                "          						0 - No\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               ).staticmethod("exist_int");
    pyClass.def("exist_double", &GXSYS_wrap_exist_double,
                "exist_double((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method checks to see if a real parameter exists.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Parameter Name\n"
                ":type arg2: str\n"
                ":returns: 1 - Yes\n"
                "          						0 - No\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               ).staticmethod("exist_double");
    pyClass.def("exist_string", &GXSYS_wrap_exist_string,
                "exist_string((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method checks to see if a string parameter exists.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Parameter Name\n"
                ":type arg2: str\n"
                ":returns: 1 - Yes\n"
                "          						0 - No\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               ).staticmethod("exist_string");
    pyClass.def("get_int", &GXSYS_wrap_get_int,
                "get_int((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns an int from the parameter block.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Parameter Name\n"
                ":type arg2: str\n"
                ":returns: Int Value, iDUMMY if the parameter is not set.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               ).staticmethod("get_int");
    pyClass.def("get_yes_no", &GXSYS_wrap_get_yes_no,
                "get_yes_no((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check a YES/NO Setting\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Parameter Name\n"
                ":type arg2: str\n"
                ":returns: 1 - if first char in setting is a \"Y\" or\"y\"\n"
                "          						0 - Otherwise\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_yes_no");
    pyClass.def("replace_string", &GXSYS_wrap_replace_string,
                "replace_string((str)arg1, (str_ref)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replace \"% %\" tokens in a string with parameter values\n\n"

                ":param arg1: String to filter replace\n"
                ":type arg1: str\n"
                ":param arg2: Output string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Default group name\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If parameter does not exist, the token is removed.  Full parameter names,\n"
                "   					such as \"%group.name%\", are used as-is.  Partial parameter names, such as\n"
                "   					\"%name%\" will have the default group attached.\n"
                "   				\n\n"
               ).staticmethod("replace_string");
    pyClass.def("load_parm", &GXSYS_wrap_load_parm,
                "load_parm((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reads parameters from a file.\n\n"

                ":param arg1: Name of the File to read from\n"
                ":type arg1: str\n"
                ":param arg2: Group Name to write read (\"\" for all groups)\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("load_parm");
    pyClass.def("get_double", &GXSYS_wrap_get_double,
                "get_double((str)arg1, (str)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns a real from the parameter block.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Parameter Name\n"
                ":type arg2: str\n"
                ":returns: Real Value, rDUMMY if parameter not set.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               ).staticmethod("get_double");
    pyClass.def("save_parm", &GXSYS_wrap_save_parm,
                "save_parm((str)arg1, (int)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Writes out one group (or all groups) to a file.\n\n"

                ":param arg1: Name of the File\n"
                ":type arg1: str\n"
                ":param arg2: 0 - New file, 1 - Append\n"
                ":type arg2: int\n"
                ":param arg3: Group Name to write out (\"\" for all groups)\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("save_parm");
    pyClass.def("filter_parm_group", &GXSYS_wrap_filter_parm_group,
                "filter_parm_group((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Controls filtering of specific group during logging.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: 0 - Clear filter, 1 - Add filter\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This is useful to prevent certain utility GX parameters from being recorded during GS script runs where the parameters does not influence the actual script execution.\n\n"
               ).staticmethod("filter_parm_group");
    pyClass.def("set_int", &GXSYS_wrap_set_int,
                "set_int((str)arg1, (str)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method sets an int in the parameter block.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Parameter Name\n"
                ":type arg2: str\n"
                ":param arg3: Int Value to Set\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("set_int");
    pyClass.def("set_pattern", &GXSYS_wrap_set_pattern,
                "set_pattern((str)arg1, (int)arg2, (float)arg3, (int)arg4, (float)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets pattern parameters in the parameter block.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Pattern\n"
                ":type arg2: int\n"
                ":param arg3: Size. Input GS_R8DM to use default\n"
                ":type arg3: float\n"
                ":param arg4: Thickness (0-100).  Input GS_S4DM to use default\n"
                ":type arg4: int\n"
                ":param arg5: Density. Input GS_R8DM to use default\n"
                ":type arg5: float\n"
                ":param arg6: Pattern Color\n"
                ":type arg6: int\n"
                ":param arg7: Background Color. Can be C_TRANSPARENT\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Sets all the user-definable pattern parameters to\n"
                "   					a specified group. Parameters are:\n"
                "   					\"PAT_NUMBER\"    0 is solid fill\n"
                "   					\"PAT_SIZE\"      pattern tile size in mm.\n"
                "   					\"PAT_THICKNESS\" pattern line thickness in percent of the tile size.\n"
                "   					valid range is 0-100.\n"
                "   					\"PAT_DENSITY\"   Tile spacing. A value of 1 means tiles are laid with no overlap.\n"
                "   					A value of 2 means they overlap each other.\n"
                "   					\"PAT_COLOR\"     The colour value.\n"
                "   					\"PAT_BACKCOLOR\" Background colour value.\n"
                "   \n"
                "   					Input values may be DUMMY.\n"
                "   \n"
                "   					Designed for use along with the sPatternForm_GUI function.\n"
                "   				\n\n"
               ).staticmethod("set_pattern");
    pyClass.def("set_double", &GXSYS_wrap_set_double,
                "set_double((str)arg1, (str)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method Sets a real in the parameter block.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Parameter Name\n"
                ":type arg2: str\n"
                ":param arg3: Real\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("set_double");
    pyClass.def("set_reg", &GXSYS_wrap_set_reg,
                "set_reg((GXREG)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy contents of a REG to current parameters.\n\n"

                ":param arg1: REG object\n"
                ":type arg1: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("set_reg");
    pyClass.def("set_string", &GXSYS_wrap_set_string,
                "set_string((str)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method sets a string in the parameter block.\n\n"

                ":param arg1: Group Name\n"
                ":type arg1: str\n"
                ":param arg2: Parameter Name\n"
                ":type arg2: str\n"
                ":param arg3: String to Set it To\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("set_string");
    pyClass.def("check_stop", &GXSYS_wrap_check_stop,
                "check_stop() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method is called at convenient points in the\n"
                "   					GX code to check if the user has asked the script\n"
                "   					to stop running. This method should be called by\n"
                "   					any GX program that may take a while to complete.\n"
                "   				\n\n"

                ":returns: 0 - No\n"
                "          						1 - Yes, Terminate processing.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("check_stop");
    pyClass.def("prog_state", &GXSYS_wrap_prog_state,
                "prog_state() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return current progress state (On/Off)\n\n"

                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is useful, for instance, when calling one GX from another,\n"
                "   					especially if it is called multiple times in a loop.\n"
                "   					The called GX may turn the progress ON/OFF on its own, which\n"
                "   					means any progress tracking in the calling GX is disrupted.\n"
                "   					The called GX should use this function to determine the original\n"
                "   					progress state, and not turn off progress if it was already on.\n"
                "   \n"
                "   					Returns				 0 - Progress is on\n"
                "   					- Progress is off\n"
                "   				\n\n"
               ).staticmethod("prog_state");
    pyClass.def("prog_name", &GXSYS_wrap_prog_name,
                "prog_name((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method allows you to name the current process being\n"
                "   					displayed by the progress bar. This method has no affect\n"
                "   					if no progress bar exists.\n"
                "   				\n\n"

                ":param arg1: New Process Name\n"
                ":type arg1: str\n"
                ":param arg2: 0 - Change the Name but do not change the percentage 1 - Change the Name and Reset Percent to 0 2 - Change the Name but no Percent Bar\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("prog_name");
    pyClass.def("progress", &GXSYS_wrap_progress,
                "progress((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method allows you to turn on the Progress BAR ON/OFF.\n"
                "   					Once the progress bar is on, use the UpdateProg method\n"
                "   					to drive it.\n"
                "   				\n\n"

                ":param arg1: 0 - Turn Progress Bar OFF 1 - Turn Progress Bar ON\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("progress");
    pyClass.def("prog_update", &GXSYS_wrap_prog_update,
                "prog_update((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method drives the Progress Bar. It is passed\n"
                "   					a percentage and will update the bar to reflect that\n"
                "   					percentage.\n"
                "   				\n\n"

                ":param arg1: Percentage Completed (0-100).\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("prog_update");
    pyClass.def("prog_update_l", &GXSYS_wrap_prog_update_l,
                "prog_update_l((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Updates progress bar based on count and maxcount.\n\n"

                ":param arg1: count\n"
                ":type arg1: int\n"
                ":param arg2: max count >= count\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("prog_update_l");
    pyClass.def("get_sys_info", &GXSYS_wrap_get_sys_info,
                "get_sys_info((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get system information\n\n"

                ":param arg1: \\ :ref:`SYS_INFO`\\ \n"
                ":type arg1: int\n"
                ":param arg2: returned setting\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_sys_info");
    pyClass.def("registry_get_val", &GXSYS_wrap_registry_get_val,
                "registry_get_val((int)arg1, (str)arg2, (str)arg3, (str_ref)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a registry value\n\n"

                ":param arg1: \\ :ref:`REG_DOMAIN`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Key to set\n"
                ":type arg2: str\n"
                ":param arg3: Value name within key\n"
                ":type arg3: str\n"
                ":param arg4: String for value data\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 if value exists\n"
                "          						1 if value does not exist\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               ).staticmethod("registry_get_val");
    pyClass.def("registry_delete_key", &GXSYS_wrap_registry_delete_key,
                "registry_delete_key((int)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete a registry value\n\n"

                ":param arg1: \\ :ref:`REG_DOMAIN`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Key to delete\n"
                ":type arg2: str\n"
                ":returns: 0 - Ok\n"
                "          						1 - Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   All sub-keys and values will be deleted if they exist.\n\n"
               ).staticmethod("registry_delete_key");
    pyClass.def("registry_delete_val", &GXSYS_wrap_registry_delete_val,
                "registry_delete_val((int)arg1, (str)arg2, (str)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete a registry value\n\n"

                ":param arg1: \\ :ref:`REG_DOMAIN`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Key\n"
                ":type arg2: str\n"
                ":param arg3: Name of value to delete\n"
                ":type arg3: str\n"
                ":returns: 0 - Ok\n"
                "          						1 - Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("registry_delete_val");
    pyClass.def("registry_set_val", &GXSYS_wrap_registry_set_val,
                "registry_set_val((int)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set/create a registry value\n\n"

                ":param arg1: \\ :ref:`REG_DOMAIN`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Key to set\n"
                ":type arg2: str\n"
                ":param arg3: Name of Subkey within key\n"
                ":type arg3: str\n"
                ":param arg4: Value for Subkey\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function will create the subkey and key if either do not\n"
                "   					already exist.\n"
                "   				\n\n"
               ).staticmethod("registry_set_val");
    pyClass.def("destroy_ptmp", &GXSYS_wrap_destroy_ptmp,
                "destroy_ptmp((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Destroy PTMP.\n\n"

                ":param arg1: PTMP object to destroy\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("destroy_ptmp");
    pyClass.def("get_ptmp", &GXSYS_wrap_get_ptmp,
                "get_ptmp((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get temporary saves copy of parameter block.\n\n"

                ":param arg1: saved with Save_PTMP_SYS\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXSYS.save_ptmp`\\ , \\ :func:`geosoft.gxapi.GXSYS.destroy_ptmp`\\ \n\n"
               ).staticmethod("get_ptmp");
    pyClass.def("save_ptmp", &GXSYS_wrap_save_ptmp,
                "save_ptmp((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Save a temporary copy of the parameter block.\n\n"

                ":param arg1: Group Name to save, \"\" for everything.\n"
                ":type arg1: str\n"
                ":returns: PTMP handle.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   All PTMP instances will be destroyed on exit.\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXSYS.get_ptmp`\\ , \\ :func:`geosoft.gxapi.GXSYS.destroy_ptmp`\\ \n\n"
               ).staticmethod("save_ptmp");
    pyClass.def("abort", &GXSYS_wrap__abort,
                "abort((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method terminates the execution of a script. A message\n"
                "   					giving the reason for the abort will be displayed along with\n"
                "   					the line number where we stopped in the script.\n"
                "   				\n\n"

                ":param arg1: Message to display\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("abort");
    pyClass.def("assert", &GXSYS_wrap__assert,
                "assert((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Abort with GX line number if not true.\n\n"

                ":param arg1: Expression to evaluate (0 aborts)\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("assert");
    pyClass.def("exit", &GXSYS_wrap__exit,
                "exit() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method terminates the execution of a script in  a regular\n"
                "   					fashion with no error messages displayed.\n"
                "   				\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("exit");
    pyClass.def("cancel", &GXSYS_wrap__cancel,
                "cancel() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method indicates that the GX program terminated without\n"
                "   					doing anything of interest and should be ignored.  In\n"
                "   					particular, the GX will not be logged in a recorded GS.\n"
                "   				\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("cancel");
    pyClass.def("delay", &GXSYS_wrap_delay,
                "delay((float)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Idle delay method.\n\n"

                ":param arg1: Decimal Seconds to delay\n"
                ":type arg1: float\n"
                ":returns: success if the delay has elapsed.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               ).staticmethod("delay");
    pyClass.def("get_timer", &GXSYS_wrap_get_timer,
                "get_timer((int)arg1, (float_ref)arg2, (float_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   return the elapsed time since the established time.\n\n"

                ":param arg1: 1 - set start time, 0 - return elapsed time\n"
                ":type arg1: int\n"
                ":param arg2: start time in seconds\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: elapsed time in seconds\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: success if the delay has elapsed.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1st time through call the method with a flag of 1 to identify\n"
                "   					the count start time, subsequent times the time will be the time\n"
                "   					elapsed since the queried start time.  Do so by settign the flag to 0.\n"
                "   				\n\n"
               ).staticmethod("get_timer");
    pyClass.def("display_help", &GXSYS_wrap_display_help,
                "display_help((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display the help dialog with the specified topic highlighted\n\n"

                ":param arg1: Group string to lookup in gxhelp.ini\n"
                ":type arg1: str\n"
                ":param arg2: Index string to lookup in gxhelp.ini\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("display_help");
    pyClass.def("display_help_topic", &GXSYS_wrap_display_help_topic,
                "display_help_topic((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display the help dialog without topic lookup in INI files\n\n"

                ":param arg1: Help File (blank for default)\n"
                ":type arg1: str\n"
                ":param arg2: Help Topic\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("display_help_topic");
    pyClass.def("display_int", &GXSYS_wrap_display_int,
                "display_int((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display an integer.\n\n"

                ":param arg1: Title of the Window\n"
                ":type arg1: str\n"
                ":param arg2: number\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("display_int");
    pyClass.def("display_message", &GXSYS_wrap_display_message,
                "display_message((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display a user message.\n\n"

                ":param arg1: Title of the Window\n"
                ":type arg1: str\n"
                ":param arg2: Message String\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("display_message");
    pyClass.def("display_double", &GXSYS_wrap_display_double,
                "display_double((str)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display a real number.\n\n"

                ":param arg1: Title of the Window\n"
                ":type arg1: str\n"
                ":param arg2: Number\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("display_double");
    pyClass.def("display_question", &GXSYS_wrap_display_question,
                "display_question((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Display a YES/NO type question. This method waits\n"
                "   					for the user to hit YES or NO.\n"
                "   				\n\n"

                ":param arg1: Title of the window\n"
                ":type arg1: str\n"
                ":param arg2: Message String\n"
                ":type arg2: str\n"
                ":returns: 0 - user selected No\n"
                "          						1 - user selected YES\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("display_question");
    pyClass.def("display_question_with_cancel", &GXSYS_wrap_display_question_with_cancel,
                "display_question_with_cancel((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Display a YES/NO/CANCEL type question. This method waits\n"
                "   					for the user to hit YES or NO or CANCEL.\n"
                "   				\n\n"

                ":param arg1: Title of the window\n"
                ":type arg1: str\n"
                ":param arg2: Message String\n"
                ":type arg2: str\n"
                ":returns: 0 - user selected No\n"
                "          						1 - user selected YES\n"
                "          						2 - user selected CANCEL\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("display_question_with_cancel");
    pyClass.def("interactive", &GXSYS_wrap_interactive,
                "interactive() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Checks to see if you should run interactively.\n\n"

                ":returns: 0 - Run in batch mode only\n"
                "          						1 - Run Interactively only\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("interactive");
    pyClass.def("prompt", &GXSYS_wrap_prompt,
                "prompt((str)arg1, (str_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Asks the User to enter a string.\n\n"

                ":param arg1: Title of the window\n"
                ":type arg1: str\n"
                ":param arg2: Buffer to place the user's string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 - User hit OK\n"
                "          						1 - user hit CANCEL\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The User string is displayed as the default value in the prompt.\n"
                "   					Empty the user string if no default is needed.\n"
                "   				\n\n"
               ).staticmethod("prompt");
    pyClass.def("script", &GXSYS_wrap_script,
                "script() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Checks to see if we are running inside OMS (script mode)\n\n"

                ":returns: 0 - Normal mode\n"
                "          						1 - Scripting mode\n"
                "          \n"
                "          						A number of functions can only be run from inside Oasis montaj\n"
                "          						(such as GetDisplayAreaRaw_EMAP), because they require an actual\n"
                "          						window object, such as an editable database or map. Use this\n"
                "          						function to prevent calls\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               ).staticmethod("script");
    pyClass.def("script_record", &GXSYS_wrap_script_record,
                "script_record() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Checks to see if we are in scripting recording mode\n\n"

                ":returns: 0 - Normal mode\n"
                "          						1 - Recording mode\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("script_record");
    pyClass.def("set_cursor", &GXSYS_wrap_set_cursor,
                "set_cursor((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the cursor on the display.\n\n"

                ":param arg1: Cursor Names\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Possible Cursors:\n"
                "   					Normal, Horiz, Vert, Moving, Cross, Hand, NoEdit, Sun,\n"
                "   					View, Group, ViewSel, GroupSel, BoxSelect, Shadow, Link,\n"
                "   					Line, PolyLine, Polygon, Ellipse, Rectangle, Text, Symbol,\n"
                "   					Zoom, Pan, Rotate, InteractiveZoom, PolyFill, GetFill,\n"
                "   					SnapPoint, SnapLine, SnapOnPoint, SnapOnLine, NPolygon,\n"
                "   					ExcludeRect, ExcludePoly, ExcludeNPoly, AddVertex, DelVertex, GeneralAdd and GeneralDelete\n"
                "   				\n\n"
               ).staticmethod("set_cursor");
    pyClass.def("set_info_line", &GXSYS_wrap_set_info_line,
                "set_info_line((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Display a message on the information line at the left\n"
                "   					bottom corner of the OAISIS montaj application.\n"
                "   				\n\n"

                ":param arg1: Message String\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("set_info_line");
    pyClass.def("set_interactive", &GXSYS_wrap_set_interactive,
                "set_interactive((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the interactive mode.\n\n"

                ":param arg1: 0 - interactive off 1 - interative on\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Call to \\ :func:`geosoft.gxapi.GXSYS.interactive`\\  will return the value\n"
                "   					set here.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXSYS.interactive`\\ , \\ :func:`geosoft.gxapi.GXSYS.run_gx`\\  and \\ :func:`geosoft.gxapi.GXSYS.run_gs`\\ \n\n"
               ).staticmethod("set_interactive");
    pyClass.def("get_workspace_reg", &GXSYS_wrap_get_workspace_reg,
                "get_workspace_reg((GXREG)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a copy of the workspace REG;\n\n"

                ":param arg1: REG object\n"
                ":type arg1: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The workspace REG is separate from the reg used\n"
                "   					to store SYS parameters.\n"
                "   \n"
                "   					Because \\ :func:`geosoft.gxapi.GXSYS.get_workspace_reg`\\  returns a copy of the\n"
                "   					workspace REG, and not the workspace REG itself,\n"
                "   					you must call \\ :func:`geosoft.gxapi.GXSYS.set_workspace_reg`\\  if you make changes\n"
                "   					to your own REG object and you wish them to take\n"
                "   					effect in the workspace REG.\n"
                "   				\n\n"
               ).staticmethod("get_workspace_reg");
    pyClass.def("set_workspace_reg", &GXSYS_wrap_set_workspace_reg,
                "set_workspace_reg((GXREG)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the workspace REG;\n\n"

                ":param arg1: REG object\n"
                ":type arg1: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The workspace REG is separate from the reg used\n"
                "   					to store SYS parameters.\n"
                "   \n"
                "   					Because \\ :func:`geosoft.gxapi.GXSYS.get_workspace_reg`\\  returns a copy of the\n"
                "   					workspace REG, and not the workspace REG itself,\n"
                "   					you must call \\ :func:`geosoft.gxapi.GXSYS.set_workspace_reg`\\  if you make changes\n"
                "   					to your own REG object and you wish them to take\n"
                "   					effect in the workspace REG\n"
                "   				\n\n"
               ).staticmethod("set_workspace_reg");
    pyClass.def("encrypt_string", &GXSYS_wrap_encrypt_string,
                "encrypt_string((str)arg1, (str_ref)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Encrypts a string for secure storage in configuration files\n"
                "   					or in the workspace parameters.\n"
                "   				\n\n"

                ":param arg1: Input string for encryption.\n"
                ":type arg1: str\n"
                ":param arg2: Output buffer for encrypted result.\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: \\ :ref:`SYS_ENCRYPTION_KEY`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing.\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("encrypt_string");
    pyClass.def("decrypt_string", &GXSYS_wrap_decrypt_string,
                "decrypt_string((str)arg1, (str_ref)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Decrypts a string that has been previously encrypted by \\ :func:`geosoft.gxapi.GXSYS.encrypt_string`\\ ().\n"
                "   				\n\n"

                ":param arg1: Input string for decryption.\n"
                ":type arg1: str\n"
                ":param arg2: Output buffer for decrypted result.\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: \\ :ref:`SYS_ENCRYPTION_KEY`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing.\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("decrypt_string");
    pyClass.def("is_encrypted_string", &GXSYS_wrap_is_encrypted_string,
                "is_encrypted_string((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Checks whether the specified string was encrypted by \\ :func:`geosoft.gxapi.GXSYS.encrypt_string`\\ ().\n"
                "   				\n\n"

                ":param arg1: Input string to inspect.\n"
                ":type arg1: str\n"
                ":returns: 0 (false) or non-zero (true)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("is_encrypted_string");
    pyClass.def("disable_gx_debugger", &GXSYS_wrap_disable_gx_debugger,
                "disable_gx_debugger() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Disable GX Debugger GUI if active\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   All breakpoints will be cleared by this call.\n\n"
               ).staticmethod("disable_gx_debugger");
    pyClass.def("enable_gx_debugger", &GXSYS_wrap_enable_gx_debugger,
                "enable_gx_debugger((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Enable GX Debugger GUI\n\n"

                ":param arg1: path that will be scanned recursively for GXC source files\n"
                ":type arg1: str\n"
                ":param arg2: name of gx where first breakpoint should be set\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Takes as input two strings one a path that will be scanned\n"
                "   					recursively for GXC source files and a second string without\n"
                "   					a path of the GX where the first breakpoint should be set in (i.e. \"gxname.gx\").\n"
                "   					The source of the GX should be found in the path (e.g. <path>\\somewhere\\gxname.gxc)\n"
                "   					and a breakpoint will be set on the first executing line of this GX. Make sure the\n"
                "   					GX binary is newer than the source file, otherwise unexpected results may occur. As\n"
                "   					soon as the GX is run the GUI will become visible and it will be possible to set more\n"
                "   					breakpoints in any of the GXC files found in the path.\n"
                "   				\n\n"
               ).staticmethod("enable_gx_debugger");

    scope().attr("ARC_LICENSE_ENGINENOTPRESENT") = (int32_t)0;
    scope().attr("ARC_LICENSE_DESKTOPENGINE") = (int32_t)1;
    scope().attr("ARC_LICENSE_ARCVIEW") = (int32_t)2;
    scope().attr("ARC_LICENSE_ARCEDITOR") = (int32_t)3;
    scope().attr("ARC_LICENSE_ARCINFO") = (int32_t)4;
    scope().attr("ARC_LICENSE_ARCSERVER") = (int32_t)5;
    scope().attr("GEO_DIRECTORY_NONE") = (int32_t)0;
    scope().attr("GEO_DIRECTORY_GEOSOFT") = (int32_t)1;
    scope().attr("GEO_DIRECTORY_BIN") = (int32_t)2;
    scope().attr("GEO_DIRECTORY_GER") = (int32_t)3;
    scope().attr("GEO_DIRECTORY_OMN") = (int32_t)4;
    scope().attr("GEO_DIRECTORY_TBL") = (int32_t)5;
    scope().attr("GEO_DIRECTORY_FONTS") = (int32_t)6;
    scope().attr("GEO_DIRECTORY_GX") = (int32_t)7;
    scope().attr("GEO_DIRECTORY_GS") = (int32_t)8;
    scope().attr("GEO_DIRECTORY_APPS") = (int32_t)9;
    scope().attr("GEO_DIRECTORY_ETC") = (int32_t)10;
    scope().attr("GEO_DIRECTORY_HLP") = (int32_t)11;
    scope().attr("GEO_DIRECTORY_USER_CSV") = (int32_t)14;
    scope().attr("GEO_DIRECTORY_USER_LIC") = (int32_t)15;
    scope().attr("GEO_DIRECTORY_USER_INI") = (int32_t)16;
    scope().attr("GEO_DIRECTORY_USER_TEMP") = (int32_t)17;
    scope().attr("GEO_DIRECTORY_USER_ETC") = (int32_t)18;
    scope().attr("GEO_DIRECTORY_IMG") = (int32_t)19;
    scope().attr("GEO_DIRECTORY_BAR") = (int32_t)20;
    scope().attr("GEO_DIRECTORY_MAPTEMPLATE") = (int32_t)22;
    scope().attr("GEO_DIRECTORY_USER_MAPTEMPLATE") = (int32_t)23;
    scope().attr("GEO_DIRECTORY_PYGX") = (int32_t)24;
    scope().attr("GEO_DIRECTORY_USER_PYGX") = (int32_t)25;
    scope().attr("GEO_DIRECTORY_USER_GX") = (int32_t)26;
    scope().attr("REG_DOMAIN_MACHINE") = (int32_t)0;
    scope().attr("REG_DOMAIN_USER") = (int32_t)1;
    scope().attr("SW_HIDE") = (int32_t)0;
    scope().attr("SW_SHOWNORMAL") = (int32_t)1;
    scope().attr("SW_SHOWMINIMIZED") = (int32_t)2;
    scope().attr("SW_SHOWMAXIMIZED") = (int32_t)3;
    scope().attr("SW_SHOWNOACTIVATE") = (int32_t)4;
    scope().attr("SW_SHOW") = (int32_t)5;
    scope().attr("SW_MINIMIZE") = (int32_t)6;
    scope().attr("SW_SHOWMINNOACTIVE") = (int32_t)7;
    scope().attr("SW_SHOWNA") = (int32_t)8;
    scope().attr("SW_RESTORE") = (int32_t)9;
    scope().attr("SW_SHOWDEFAULT") = (int32_t)10;
    scope().attr("SW_FORCEMINIMIZE") = (int32_t)11;
    scope().attr("SYS_DIR_LOCAL") = (int32_t)0;
    scope().attr("SYS_DIR_GEOSOFT") = (int32_t)1;
    scope().attr("SYS_DIR_USER") = (int32_t)2;
    scope().attr("SYS_DIR_GEOTEMP") = (int32_t)3;
    scope().attr("SYS_DIR_WINDOWS") = (int32_t)4;
    scope().attr("SYS_DIR_SYSTEM") = (int32_t)5;
    scope().attr("SYS_DIR_LICENSE") = (int32_t)6;
    scope().attr("SYS_DIR_RESOURCEFILES") = (int32_t)7;
    scope().attr("SYS_DIR_GEOSOFT_BAR") = (int32_t)100;
    scope().attr("SYS_DIR_GEOSOFT_BIN") = (int32_t)101;
    scope().attr("SYS_DIR_GEOSOFT_CSV") = (int32_t)102;
    scope().attr("SYS_DIR_GEOSOFT_CSV_ALIASES") = (int32_t)103;
    scope().attr("SYS_DIR_GEOSOFT_DATA") = (int32_t)104;
    scope().attr("SYS_DIR_GEOSOFT_DBG") = (int32_t)105;
    scope().attr("SYS_DIR_GEOSOFT_ENCRYPTEDFILES") = (int32_t)106;
    scope().attr("SYS_DIR_GEOSOFT_ETC") = (int32_t)107;
    scope().attr("SYS_DIR_GEOSOFT_FONTS") = (int32_t)108;
    scope().attr("SYS_DIR_GEOSOFT_GER") = (int32_t)109;
    scope().attr("SYS_DIR_GEOSOFT_GS") = (int32_t)110;
    scope().attr("SYS_DIR_GEOSOFT_GX") = (int32_t)111;
    scope().attr("SYS_DIR_GEOSOFT_HLP") = (int32_t)112;
    scope().attr("SYS_DIR_GEOSOFT_IMG") = (int32_t)113;
    scope().attr("SYS_DIR_GEOSOFT_INI") = (int32_t)114;
    scope().attr("SYS_DIR_GEOSOFT_MAPTEMPLATE") = (int32_t)115;
    scope().attr("SYS_DIR_GEOSOFT_OMN") = (int32_t)116;
    scope().attr("SYS_DIR_GEOSOFT_PAGE") = (int32_t)117;
    scope().attr("SYS_DIR_GEOSOFT_SCHEMA") = (int32_t)118;
    scope().attr("SYS_DIR_GEOSOFT_SPEC_INI") = (int32_t)119;
    scope().attr("SYS_DIR_GEOSOFT_STYLESHEETS") = (int32_t)120;
    scope().attr("SYS_DIR_GEOSOFT_TBL") = (int32_t)121;
    scope().attr("SYS_DIR_USER_CSV") = (int32_t)200;
    scope().attr("SYS_DIR_USER_ETC") = (int32_t)201;
    scope().attr("SYS_DIR_USER_GS") = (int32_t)202;
    scope().attr("SYS_DIR_USER_HLP") = (int32_t)203;
    scope().attr("SYS_DIR_USER_INI") = (int32_t)204;
    scope().attr("SYS_DIR_USER_LIC") = (int32_t)205;
    scope().attr("SYS_DIR_USER_MAPTEMPLATE") = (int32_t)206;
    scope().attr("SYS_DIR_USER_OMN") = (int32_t)207;
    scope().attr("SYS_DIR_USER_BAR") = (int32_t)214;
    scope().attr("SYS_DIR_USER_IMG") = (int32_t)215;
    scope().attr("SYS_DIR_USER_STACKS") = (int32_t)209;
    scope().attr("SYS_DIR_USER_TEMP") = (int32_t)210;
    scope().attr("SYS_DIR_USER_SERVICES") = (int32_t)211;
    scope().attr("SYS_DIR_USER_STYLESHEETS") = (int32_t)212;
    scope().attr("SYS_FONT_GFN") = (int32_t)1;
    scope().attr("SYS_FONT_TT") = (int32_t)0;
    scope().attr("SYS_INFO_VERSION_MAJOR") = (int32_t)0;
    scope().attr("SYS_INFO_VERSION_MINOR") = (int32_t)1;
    scope().attr("SYS_INFO_VERSION_SP") = (int32_t)2;
    scope().attr("SYS_INFO_BUILD_NUMBER") = (int32_t)3;
    scope().attr("SYS_INFO_BUILD_LABEL") = (int32_t)4;
    scope().attr("SYS_INFO_VERSION_LABEL") = (int32_t)5;
    scope().attr("SYS_INFO_PRODUCTNAME") = (int32_t)6;
    scope().attr("SYS_INFO_SERVERNAME") = (int32_t)7;
    scope().attr("SYS_INFO_LEGALCOPYRIGHT") = (int32_t)8;
    scope().attr("SYS_INFO_REGISTRY") = (int32_t)9;
    scope().attr("SYS_INFO_REGISTRY_ENVIRONMENT") = (int32_t)10;
    scope().attr("SYS_INFO_REGISTRY_SUPPORT") = (int32_t)11;
    scope().attr("SYS_INFO_REGISTRY_INTERAPP") = (int32_t)12;
    scope().attr("SYS_INFO_OIS_REGISTRY") = (int32_t)13;
    scope().attr("SYS_INFO_TEST_REGISTRY") = (int32_t)14;
    scope().attr("SYS_LINEAGE_SOURCE_MAP") = (int32_t)0;
    scope().attr("SYS_LINEAGE_SOURCE_MXD") = (int32_t)1;
    scope().attr("SYS_LINEAGE_SOURCE_DB") = (int32_t)2;
    scope().attr("SYS_LINEAGE_SOURCE_MAPTEMPLATE") = (int32_t)3;
    scope().attr("SYS_LINEAGE_SOURCE_GRID") = (int32_t)4;
    scope().attr("SYS_LINEAGE_SOURCE_VOXEL") = (int32_t)5;
    scope().attr("SYS_MENU_CLEAR_ALL") = (int32_t)0;
    scope().attr("SYS_MENU_CLEAR_DEFAULT") = (int32_t)1;
    scope().attr("SYS_PATH_LOCAL") = (int32_t)0;
    scope().attr("SYS_PATH_GEOSOFT") = (int32_t)1;
    scope().attr("SYS_PATH_GEOSOFT_USER") = (int32_t)2;
    scope().attr("SYS_PATH_GEOTEMP") = (int32_t)3;
    scope().attr("SYS_PATH_WINDOWS") = (int32_t)4;
    scope().attr("SYS_PATH_SYSTEM") = (int32_t)5;
    scope().attr("SYS_PATH_LICENSE") = (int32_t)6;
    scope().attr("SYS_PATH_RESOURCEFILES") = (int32_t)7;
    scope().attr("SYS_PATH_GEOSOFT_BAR") = (int32_t)100;
    scope().attr("SYS_PATH_GEOSOFT_BIN") = (int32_t)101;
    scope().attr("SYS_PATH_GEOSOFT_CSV") = (int32_t)102;
    scope().attr("SYS_PATH_GEOSOFT_CSV_ALIASES") = (int32_t)103;
    scope().attr("SYS_PATH_GEOSOFT_DATA") = (int32_t)104;
    scope().attr("SYS_PATH_GEOSOFT_DBG") = (int32_t)105;
    scope().attr("SYS_PATH_GEOSOFT_ENCRYPTEDFILES") = (int32_t)106;
    scope().attr("SYS_PATH_GEOSOFT_ETC") = (int32_t)107;
    scope().attr("SYS_PATH_GEOSOFT_FONTS") = (int32_t)108;
    scope().attr("SYS_PATH_GEOSOFT_GER") = (int32_t)109;
    scope().attr("SYS_PATH_GEOSOFT_GS") = (int32_t)110;
    scope().attr("SYS_PATH_GEOSOFT_PYGX") = (int32_t)126;
    scope().attr("SYS_PATH_GEOSOFT_GX") = (int32_t)111;
    scope().attr("SYS_PATH_GEOSOFT_HLP") = (int32_t)112;
    scope().attr("SYS_PATH_GEOSOFT_IMG") = (int32_t)113;
    scope().attr("SYS_PATH_GEOSOFT_INI") = (int32_t)114;
    scope().attr("SYS_PATH_GEOSOFT_MAPTEMPLATE") = (int32_t)115;
    scope().attr("SYS_PATH_GEOSOFT_OMN") = (int32_t)116;
    scope().attr("SYS_PATH_GEOSOFT_PAGE") = (int32_t)117;
    scope().attr("SYS_PATH_GEOSOFT_SCHEMA") = (int32_t)118;
    scope().attr("SYS_PATH_GEOSOFT_SPEC_INI") = (int32_t)119;
    scope().attr("SYS_PATH_GEOSOFT_STYLESHEETS") = (int32_t)120;
    scope().attr("SYS_PATH_GEOSOFT_TBL") = (int32_t)121;
    scope().attr("SYS_PATH_GEOSOFT_USER_CSV") = (int32_t)200;
    scope().attr("SYS_PATH_GEOSOFT_USER_ETC") = (int32_t)201;
    scope().attr("SYS_PATH_GEOSOFT_USER_GS") = (int32_t)202;
    scope().attr("SYS_PATH_GEOSOFT_USER_GX") = (int32_t)217;
    scope().attr("SYS_PATH_GEOSOFT_USER_PYGX") = (int32_t)216;
    scope().attr("SYS_PATH_GEOSOFT_USER_HLP") = (int32_t)203;
    scope().attr("SYS_PATH_GEOSOFT_USER_INI") = (int32_t)204;
    scope().attr("SYS_PATH_GEOSOFT_USER_LIC") = (int32_t)205;
    scope().attr("SYS_PATH_GEOSOFT_USER_MAPTEMPLATE") = (int32_t)206;
    scope().attr("SYS_PATH_GEOSOFT_USER_OMN") = (int32_t)207;
    scope().attr("SYS_PATH_GEOSOFT_USER_STACKS") = (int32_t)209;
    scope().attr("SYS_PATH_GEOSOFT_USER_TEMP") = (int32_t)210;
    scope().attr("SYS_PATH_USER_SERVICES") = (int32_t)211;
    scope().attr("SYS_PATH_USER_STYLESHEETS") = (int32_t)212;
    scope().attr("SYS_RUN_DISPLAY_WINDOW") = (int32_t)0;
    scope().attr("SYS_RUN_DISPLAY_MINIMIZE") = (int32_t)8;
    scope().attr("SYS_RUN_DISPLAY_FULLSCREEN") = (int32_t)16;
    scope().attr("SYS_RUN_HOLD_NEVER") = (int32_t)0;
    scope().attr("SYS_RUN_HOLD_ONERROR") = (int32_t)512;
    scope().attr("SYS_RUN_HOLD_ALWAYS") = (int32_t)1024;
    scope().attr("SYS_RUN_TYPE_DOS") = (int32_t)1;
    scope().attr("SYS_RUN_TYPE_EXE") = (int32_t)0;
    scope().attr("SYS_RUN_TYPE_WINDOWS") = (int32_t)2;
    scope().attr("SYS_RUN_WIN_NOWAIT") = (int32_t)0;
    scope().attr("SYS_RUN_WIN_WAIT") = (int32_t)2048;
    scope().attr("FIND_LOCAL_GEOSOFT") = (int32_t)0;
    scope().attr("FIND_GEOSOFT") = (int32_t)1;
    scope().attr("FIND_LOCAL") = (int32_t)2;
    scope().attr("FIND_SHORT") = (int32_t)1024;
    scope().attr("SYS_ENCRYPTION_KEY_GEOSOFT_ID") = (int32_t)0;
    scope().attr("SYS_ENCRYPTION_KEY_GLOBAL_ID") = (int32_t)1;

}
