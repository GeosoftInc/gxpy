#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXDU_wrap_table_look1(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, const gx_string_type& arg5, const gx_string_type& arg6, int32_t arg7, double arg8, GXTBPtr arg9)
{
    GXDU::table_look1(arg1, arg2, arg3, arg4, arg5, arg6, (DU_LOOKUP)arg7, arg8, arg9);
}
inline void GXDU_wrap_table_look2(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8, int32_t arg9, double arg10, GXTBPtr arg11)
{
    GXDU::table_look2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, (DU_LOOKUP)arg9, arg10, arg11);
}
inline void GXDU_wrap_table_look_i2(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8, int32_t arg9, double arg10, GXTBPtr arg11)
{
    GXDU::table_look_i2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, (DU_LOOKUP)arg9, arg10, arg11);
}
inline void GXDU_wrap_table_look_r2(GXDBPtr arg1, int32_t arg2, double arg3, int32_t arg4, int32_t arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8, int32_t arg9, double arg10, GXTBPtr arg11)
{
    GXDU::table_look_r2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, (DU_LOOKUP)arg9, arg10, arg11);
}
inline void GXDU_wrap_ado_table_names(const gx_string_type& arg1, GXVVPtr arg2)
{
    GXDU::ado_table_names(arg1, arg2);
}
inline void GXDU_wrap_an_sig(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    GXDU::an_sig(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_append(GXDBPtr arg1, GXDBPtr arg2, int32_t arg3)
{
    GXDU::append(arg1, arg2, arg3);
}
inline void GXDU_wrap_avg_azimuth(GXDBPtr arg1, double arg2, float_ref& arg3)
{
    GXDU::avg_azimuth(arg1, arg2, arg3);
}
inline void GXDU_wrap_base_data(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, GXTBPtr arg6)
{
    GXDU::base_data(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_base_data_ex(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, GXTBPtr arg6, int32_t arg7)
{
    GXDU::base_data_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXDU_wrap_bound_line(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXPLYPtr arg5)
{
    GXDU::bound_line(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_bp_filt(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, double arg5, double arg6, int32_t arg7)
{
    GXDU::bp_filt(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXDU_wrap_break_line(GXDBPtr arg1, int32_t arg2, int32_t arg3)
{
    GXDU::break_line(arg1, arg2, arg3);
}
inline void GXDU_wrap_break_line2(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    GXDU::break_line2(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_break_line_to_groups(GXDBPtr arg1, int32_t arg2, int32_t arg3, const gx_string_type& arg4)
{
    GXDU::break_line_to_groups(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_break_line_to_groups2(GXDBPtr arg1, int32_t arg2, int32_t arg3, const gx_string_type& arg4, int32_t arg5)
{
    GXDU::break_line_to_groups2(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_b_spline(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, double arg5, double arg6, double arg7)
{
    GXDU::b_spline(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXDU_wrap_closest_point(GXDBPtr arg1, double arg2, double arg3, float_ref& arg4, float_ref& arg5, int_ref& arg6, float_ref& arg7)
{
    GXDU::closest_point(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXDU_wrap_copy_line(GXDBPtr arg1, int32_t arg2, int32_t arg3)
{
    GXDU::copy_line(arg1, arg2, arg3);
}
inline void GXDU_wrap_copy_line_across(GXDBPtr arg1, int32_t arg2, GXDBPtr arg3, int32_t arg4)
{
    GXDU::copy_line_across(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_copy_line_chan_across(GXDBPtr arg1, int32_t arg2, GXVVPtr arg3, GXDBPtr arg4, int32_t arg5)
{
    GXDU::copy_line_chan_across(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_copy_line_masked(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXDU::copy_line_masked(arg1, arg2, arg3, (VVU_PRUNE)arg4, arg5);
}
inline void GXDU_wrap_dao_table_names(const gx_string_type& arg1, const gx_string_type& arg2, GXVVPtr arg3)
{
    GXDU::dao_table_names(arg1, arg2, arg3);
}
inline void GXDU_wrap_decimate(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXDU::decimate(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_diff(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXDU::diff(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_distance(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXDU::distance(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_distance_3d(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    GXDU::distance_3d(arg1, arg2, arg3, arg4, arg5, (DU_DISTANCE_CHANNEL_TYPE)arg6, arg7);
}
inline void GXDU_wrap_distline(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, float_ref& arg5)
{
    GXDU::distline(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_dup_chan_locks(GXDBPtr arg1, GXDBPtr arg2)
{
    GXDU::dup_chan_locks(arg1, arg2);
}
inline void GXDU_wrap_dup_chans(GXDBPtr arg1, GXDBPtr arg2)
{
    GXDU::dup_chans(arg1, arg2);
}
inline void GXDU_wrap_edit_duplicates(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, double arg7)
{
    GXDU::edit_duplicates(arg1, arg2, arg3, arg4, (DB_DUP)arg5, (DB_DUPEDIT)arg6, arg7);
}
inline void GXDU_wrap_export1(GXDBPtr arg1, int32_t arg2, const gx_string_type& arg3, GXVVPtr arg4, int32_t arg5, const gx_string_type& arg6, int32_t arg7, int32_t arg8)
{
    GXDU::export1(arg1, (DU_EXPORT)arg2, arg3, arg4, (DU_CHANNELS)arg5, arg6, arg7, arg8);
}
inline void GXDU_wrap_export2(GXDBPtr arg1, int32_t arg2, const gx_string_type& arg3, GXVVPtr arg4, int32_t arg5, const gx_string_type& arg6, int32_t arg7, int32_t arg8, int32_t arg9)
{
    GXDU::export2(arg1, (DU_EXPORT)arg2, arg3, arg4, (DU_CHANNELS)arg5, arg6, arg7, arg8, arg9);
}
inline void GXDU_wrap_export_amira(GXDBPtr arg1, GXWAPtr arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8, const gx_string_type& arg9, const gx_string_type& arg10, const gx_string_type& arg11)
{
    GXDU::export_amira(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXDU_wrap_export_aseg(GXDBPtr arg1, const gx_string_type& arg2, GXVVPtr arg3, int32_t arg4, const gx_string_type& arg5, const gx_string_type& arg6)
{
    GXDU::export_aseg(arg1, arg2, arg3, (DU_CHANNELS)arg4, arg5, arg6);
}
inline void GXDU_wrap_export_aseg_proj(GXDBPtr arg1, const gx_string_type& arg2, GXVVPtr arg3, int32_t arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7, GXIPJPtr arg8)
{
    GXDU::export_aseg_proj(arg1, arg2, arg3, (DU_CHANNELS)arg4, arg5, arg6, arg7, arg8);
}
inline void GXDU_wrap_export_chan_crc(GXDBPtr arg1, int32_t arg2, int_ref& arg3, const gx_string_type& arg4)
{
    GXDU::export_chan_crc(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_export_csv(GXDBPtr arg1, const gx_string_type& arg2, GXVVPtr arg3, int32_t arg4, const gx_string_type& arg5, int32_t arg6, int32_t arg7)
{
    GXDU::export_csv(arg1, arg2, arg3, (DU_CHANNELS)arg4, arg5, arg6, arg7);
}
inline void GXDU_wrap_export_database_crc(GXDBPtr arg1, int_ref& arg2, const gx_string_type& arg3)
{
    GXDU::export_database_crc(arg1, arg2, arg3);
}
inline void GXDU_wrap_export_gbn(GXDBPtr arg1, GXVVPtr arg2, const gx_string_type& arg3)
{
    GXDU::export_gbn(arg1, arg2, arg3);
}
inline void GXDU_wrap_export_mdb(GXDBPtr arg1, const gx_string_type& arg2, GXVVPtr arg3, int32_t arg4, int32_t arg5, const gx_string_type& arg6)
{
    GXDU::export_mdb(arg1, arg2, arg3, (DU_CHANNELS)arg4, (DU_LINEOUT)arg5, arg6);
}
inline void GXDU_wrap_export_geodatabase(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXVVPtr arg4, int32_t arg5, int32_t arg6, int32_t arg7, const gx_string_type& arg8)
{
    GXDU::export_geodatabase(arg1, arg2, arg3, arg4, (DU_CHANNELS)arg5, (DU_FEATURE_TYPE_OUTPUT)arg6, (DU_LINEOUT)arg7, arg8);
}
inline int32_t GXDU_wrap_get_existing_feature_classes_in_geodatabase(GXDBPtr arg1, const gx_string_type& arg2, GXLSTPtr arg3, GXVVPtr arg4)
{
    int32_t ret = GXDU::get_existing_feature_classes_in_geodatabase(arg1, arg2, arg3, arg4);
    return ret;
}
inline void GXDU_wrap_export_shp(GXDBPtr arg1, const gx_string_type& arg2, GXVVPtr arg3, int32_t arg4, int32_t arg5, const gx_string_type& arg6, GXLSTPtr arg7)
{
    GXDU::export_shp(arg1, arg2, arg3, (DU_CHANNELS)arg4, (DU_LINEOUT)arg5, arg6, arg7);
}
inline void GXDU_wrap_export_xyz(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXDU::export_xyz(arg1, arg2, arg3);
}
inline void GXDU_wrap_export_xyz2(GXDBPtr arg1, GXWAPtr arg2, GXRAPtr arg3)
{
    GXDU::export_xyz2(arg1, arg2, arg3);
}
inline void GXDU_wrap_fft(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXDU::fft(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_filter(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXFLTPtr arg5)
{
    GXDU::filter(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_gen_lev(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, double arg4, int32_t arg5)
{
    GXDU::gen_lev(arg1, arg2, arg3, arg4, (DU_LEVEL)arg5);
}
inline void GXDU_wrap_gen_lev_db(GXDBPtr arg1, const gx_string_type& arg2, double arg3, int32_t arg4)
{
    GXDU::gen_lev_db(arg1, arg2, arg3, (DU_LEVEL)arg4);
}
inline void GXDU_wrap_gen_xyz_temp(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXDU::gen_xyz_temp(arg1, arg2);
}
inline void GXDU_wrap_get_xyz_num_fields(const gx_string_type& arg1, int_ref& arg2)
{
    GXDU::get_xyz_num_fields(arg1, arg2);
}
inline void GXDU_wrap_get_chan_data_lst(GXDBPtr arg1, int32_t arg2, int32_t arg3, GXLSTPtr arg4)
{
    GXDU::get_chan_data_lst(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_get_chan_data_vv(GXDBPtr arg1, int32_t arg2, int32_t arg3, GXVVPtr arg4)
{
    GXDU::get_chan_data_vv(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_gradient(GXDBPtr arg1, GXDBPtr arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7, int32_t arg8, int32_t arg9, double arg10, double arg11)
{
    GXDU::gradient(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXDU_wrap_grav_drift(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    GXDU::grav_drift(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXDU_wrap_grav_tide(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, double arg7, int32_t arg8)
{
    GXDU::grav_tide(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXDU_wrap_grid_load(GXDBPtr arg1, GXIMGPtr arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    GXDU::grid_load(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_grid_load_xyz(GXDBPtr arg1, GXIMGPtr arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7, int32_t arg8, int32_t arg9, int32_t arg10)
{
    GXDU::grid_load_xyz(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXDU_wrap_head(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXTBPtr arg5, double arg6)
{
    GXDU::head(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_import_bin3(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, str_ref& arg4, int32_t arg5, double arg6, GXWAPtr arg7)
{
    GXDU::import_bin3(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXDU_wrap_imp_cb_ply(GXDBPtr arg1, GXPJPtr arg2, const gx_string_type& arg3, int32_t arg4, int32_t arg5)
{
    GXDU::imp_cb_ply(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_import_ado(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5)
{
    GXDU::import_ado(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_import_all_ado(GXDBPtr arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXDU::import_all_ado(arg1, arg2, (DU_STORAGE)arg3);
}
inline void GXDU_wrap_import_all_dao(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4)
{
    GXDU::import_all_dao(arg1, arg2, arg3, (DU_STORAGE)arg4);
}
inline void GXDU_wrap_import_amira(GXDBPtr arg1, GXRAPtr arg2, GXWAPtr arg3)
{
    GXDU::import_amira(arg1, arg2, arg3);
}
inline void GXDU_wrap_import_aseg(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, int32_t arg6)
{
    GXDU::import_aseg(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_import_aseg_proj(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, int32_t arg6, const gx_string_type& arg7, const gx_string_type& arg8, const gx_string_type& arg9)
{
    GXDU::import_aseg_proj(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXDU_wrap_import_bin(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, int32_t arg5, double arg6)
{
    GXDU::import_bin(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_import_bin2(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, int32_t arg5, double arg6, GXWAPtr arg7)
{
    GXDU::import_bin2(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXDU_wrap_import_bin4(GXDBPtr arg1, int32_t arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, int32_t arg6, double arg7, GXWAPtr arg8)
{
    GXDU::import_bin4(arg1, (DU_IMPORT)arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXDU_wrap_import_daarc500_serial(GXDBPtr arg1, int32_t arg2, const gx_string_type& arg3, int32_t arg4, int32_t arg5)
{
    GXDU::import_daarc500_serial(arg1, arg2, arg3, arg4, (GU_DAARC500_DATATYPE)arg5);
}
inline void GXDU_wrap_import_daarc500_serial_gps(GXDBPtr arg1, int32_t arg2, const gx_string_type& arg3, int32_t arg4)
{
    GXDU::import_daarc500_serial_gps(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_import_dao(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6)
{
    GXDU::import_dao(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_import_esri(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    GXDU::import_esri(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_import_gbn(GXDBPtr arg1, const gx_string_type& arg2)
{
    GXDU::import_gbn(arg1, arg2);
}
inline void GXDU_wrap_import_oddf(GXDBPtr arg1, const gx_string_type& arg2)
{
    GXDU::import_oddf(arg1, arg2);
}
inline void GXDU_wrap_import_pico(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4)
{
    GXDU::import_pico(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_import_ubc_mod_msh(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4, double arg5)
{
    GXDU::import_ubc_mod_msh(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_import_usgs_post(GXDBPtr arg1, const gx_string_type& arg2)
{
    GXDU::import_usgs_post(arg1, arg2);
}
inline void GXDU_wrap_import_xyz(GXDBPtr arg1, int32_t arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    GXDU::import_xyz(arg1, (DU_IMPORT)arg2, arg3, arg4);
}
inline void GXDU_wrap_import_xyz2(GXDBPtr arg1, int32_t arg2, const gx_string_type& arg3, const gx_string_type& arg4, GXWAPtr arg5)
{
    GXDU::import_xyz2(arg1, (DU_IMPORT)arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_import_io_gas(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXDU::import_io_gas(arg1, arg2, arg3);
}
inline void GXDU_wrap_index_order(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    GXDU::index_order(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_interp(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    GXDU::interp(arg1, arg2, arg3, arg4, (DU_INTERP)arg5, (DU_INTERP_EDGE)arg6);
}
inline void GXDU_wrap_interp_gap(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7, int32_t arg8)
{
    GXDU::interp_gap(arg1, arg2, arg3, arg4, (DU_INTERP)arg5, (DU_INTERP_EDGE)arg6, arg7, arg8);
}
inline void GXDU_wrap_intersect(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, double arg5, const gx_string_type& arg6)
{
    GXDU::intersect(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_intersect_all(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, double arg5, const gx_string_type& arg6)
{
    GXDU::intersect_all(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_intersect_gd_bto_tbl(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXDU::intersect_gd_bto_tbl(arg1, arg2);
}
inline void GXDU_wrap_intersect_old(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, const gx_string_type& arg5, const gx_string_type& arg6)
{
    GXDU::intersect_old(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_intersect_tb_lto_gdb(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXDU::intersect_tb_lto_gdb(arg1, arg2);
}
inline void GXDU_wrap_lab_template(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3, const gx_string_type& arg4, int32_t arg5, int32_t arg6, int32_t arg7, int32_t arg8, int32_t arg9)
{
    GXDU::lab_template(arg1, arg2, (DU_LAB_TYPE)arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXDU_wrap_load_gravity(GXDBPtr arg1, GXREGPtr arg2, int32_t arg3, const gx_string_type& arg4)
{
    GXDU::load_gravity(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_load_ltb(GXDBPtr arg1, int32_t arg2, GXLTBPtr arg3, int32_t arg4)
{
    GXDU::load_ltb(arg1, arg2, arg3, (DU_LOADLTB)arg4);
}
inline void GXDU_wrap_make_fid(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    GXDU::make_fid(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_mask(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    GXDU::mask(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_math(GXDBPtr arg1, int32_t arg2, GXEXPPtr arg3)
{
    GXDU::math(arg1, arg2, arg3);
}
inline void GXDU_wrap_merge_line(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXDU::merge_line(arg1, arg2, arg3, arg4, (DU_MERGE)arg5);
}
inline void GXDU_wrap_mod_fid_range(GXDBPtr arg1, int32_t arg2, double arg3, double arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    GXDU::mod_fid_range(arg1, arg2, arg3, arg4, arg5, arg6, (DU_MODFID)arg7);
}
inline void GXDU_wrap_move(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    GXDU::move(arg1, arg2, arg3, arg4, arg5, (DU_MOVE)arg6);
}
inline void GXDU_wrap_nl_filt(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, double arg6)
{
    GXDU::nl_filt(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_normal(GXDBPtr arg1, int32_t arg2, bool arg3)
{
    GXDU::normal(arg1, arg2, arg3);
}
inline void GXDU_wrap_poly_fill(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, GXPLYPtr arg6, int32_t arg7)
{
    GXDU::poly_fill(arg1, arg2, arg3, arg4, arg5, arg6, (DU_FILL)arg7);
}
inline void GXDU_wrap_poly_mask(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, GXPLYPtr arg6, int32_t arg7)
{
    GXDU::poly_mask(arg1, arg2, arg3, arg4, arg5, arg6, (DU_MASK)arg7);
}
inline void GXDU_wrap_project_data(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, GXPJPtr arg7)
{
    GXDU::project_data(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXDU_wrap_project_xyz(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7, int32_t arg8, GXPJPtr arg9)
{
    GXDU::project_xyz(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXDU_wrap_proj_points(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7, int32_t arg8, int32_t arg9, int32_t arg10, int32_t arg11, int32_t arg12, int32_t arg13, int32_t arg14, int32_t arg15, int32_t arg16, int32_t arg17, int32_t arg18, int32_t arg19, int32_t arg20)
{
    GXDU::proj_points(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20);
}
inline void GXDU_wrap_qc_init_separation(GXDBPtr arg1, double arg2, double arg3)
{
    GXDU::qc_init_separation(arg1, arg2, arg3);
}
inline int32_t GXDU_wrap_qc_survey_plan(GXDBPtr arg1, GXWAPtr arg2, GXPLYPtr arg3, double arg4, double arg5, double arg6, double arg7, int32_t arg8, int32_t arg9, double arg10, double arg11, double arg12, double arg13, int32_t arg14, int32_t arg15, int32_t arg16, double arg17, double arg18)
{
    int32_t ret = GXDU::qc_survey_plan(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, (QC_PLAN_TYPE)arg16, arg17, arg18);
    return ret;
}
inline double GXDU_wrap_direction(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    double ret = GXDU::direction(arg1, arg2, arg3, arg4);
    return ret;
}
inline void GXDU_wrap_re_fid(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, double arg7, double arg8, double arg9)
{
    GXDU::re_fid(arg1, arg2, arg3, arg4, arg5, (DU_REFID)arg6, arg7, arg8, arg9);
}
inline void GXDU_wrap_re_fid_all_ch(GXDBPtr arg1, int32_t arg2, int32_t arg3)
{
    GXDU::re_fid_all_ch(arg1, arg2, arg3);
}
inline void GXDU_wrap_re_fid_ch(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    GXDU::re_fid_ch(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_rotate(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, double arg7, double arg8, double arg9)
{
    GXDU::rotate(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXDU_wrap_sample_gd(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, GXGDPtr arg6)
{
    GXDU::sample_gd(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_sample_img(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, GXIMGPtr arg6)
{
    GXDU::sample_img(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_sample_img_line_lst(GXDBPtr arg1, GXLSTPtr arg2, int32_t arg3, int32_t arg4, int32_t arg5, GXIMGPtr arg6)
{
    GXDU::sample_img_line_lst(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_scan_ado(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXDU::scan_ado(arg1, arg2, arg3);
}
inline void GXDU_wrap_scan_aseg(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    GXDU::scan_aseg(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_scan_dao(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    GXDU::scan_dao(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_scan_pico(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXDU::scan_pico(arg1, arg2);
}
inline void GXDU_wrap_sort(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    GXDU::sort(arg1, arg2, arg3, (DU_SORT)arg4);
}
inline void GXDU_wrap_sort_index(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXDU::sort_index(arg1, arg2, arg3, arg4, (DU_SORT)arg5);
}
inline void GXDU_wrap_sort_index2(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    GXDU::sort_index2(arg1, arg2, arg3, (DU_SORT)arg4, arg5, (DU_SORT)arg6, arg7);
}
inline void GXDU_wrap_split_line(GXDBPtr arg1, int32_t arg2, int32_t arg3, double arg4)
{
    GXDU::split_line(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_split_line2(GXDBPtr arg1, int32_t arg2, int32_t arg3, double arg4, int32_t arg5)
{
    GXDU::split_line2(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_split_line_xy(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, double arg6, double arg7, int32_t arg8, int_ref& arg9, int32_t arg10)
{
    GXDU::split_line_xy(arg1, arg2, arg3, arg4, arg5, arg6, arg7, (DU_SPLITLINE)arg8, arg9, arg10);
}
inline void GXDU_wrap_split_line_xy2(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, double arg6, double arg7, int32_t arg8, int_ref& arg9, int32_t arg10, int32_t arg11)
{
    GXDU::split_line_xy2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, (DU_SPLITLINE)arg8, arg9, arg10, arg11);
}
inline void GXDU_wrap_split_line_xy3(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, double arg6, double arg7, int32_t arg8, int_ref& arg9, int32_t arg10, int32_t arg11, int32_t arg12)
{
    GXDU::split_line_xy3(arg1, arg2, arg3, arg4, arg5, arg6, arg7, (DU_SPLITLINE)arg8, arg9, arg10, arg11, arg12);
}
inline void GXDU_wrap_split_line_by_direction(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, double arg5, double arg6, double arg7, double arg8, bool arg9, int32_t arg10, int_ref& arg11, int32_t arg12, int32_t arg13)
{
    GXDU::split_line_by_direction(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (DU_SPLITLINE)arg10, arg11, arg12, arg13);
}
inline void GXDU_wrap_split_line_by_direction2(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, double arg5, double arg6, double arg7, double arg8, bool arg9, int32_t arg10, int_ref& arg11, int32_t arg12, int32_t arg13, int32_t arg14)
{
    GXDU::split_line_by_direction2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (DU_SPLITLINE)arg10, arg11, arg12, arg13, arg14);
}
inline void GXDU_wrap_stat(GXDBPtr arg1, int32_t arg2, int32_t arg3, GXSTPtr arg4)
{
    GXDU::stat(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_table_line_fid(GXDBPtr arg1, int32_t arg2, int32_t arg3, GXTBPtr arg4, int32_t arg5)
{
    GXDU::table_line_fid(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_table_selected_lines_fid(GXDBPtr arg1, int32_t arg2, int32_t arg3, GXTBPtr arg4, int32_t arg5)
{
    GXDU::table_selected_lines_fid(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_time_constant(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7, int32_t arg8)
{
    GXDU::time_constant(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXDU_wrap_trend(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXDU::trend(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_update_intersect_db(GXDBPtr arg1, int32_t arg2, int32_t arg3, GXDBPtr arg4)
{
    GXDU::update_intersect_db(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_voxel_section(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXVOXPtr arg5, const gx_string_type& arg6, double arg7, double arg8, int32_t arg9)
{
    GXDU::voxel_section(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXDU_wrap_write_wa(GXDBPtr arg1, int32_t arg2, GXLSTPtr arg3, GXWAPtr arg4)
{
    GXDU::write_wa(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_xyz_line(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, double arg6)
{
    GXDU::xyz_line(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_xyz_line2(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, double arg6, double arg7)
{
    GXDU::xyz_line2(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXDU_wrap_xyz_line3(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, double arg6, double arg7, int32_t arg8)
{
    GXDU::xyz_line3(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXDU_wrap_z_mask(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, double arg5, double arg6)
{
    GXDU::z_mask(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDU_wrap_range_xy(GXDBPtr arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    GXDU::range_xy(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDU_wrap_range_xyz(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9, float_ref& arg10, int_ref& arg11)
{
    GXDU::range_xyz(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXDU_wrap_range_xyz_data(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9, float_ref& arg10, float_ref& arg11, float_ref& arg12, float_ref& arg13, int_ref& arg14)
{
    GXDU::range_xyz_data(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14);
}
inline void GXDU_wrap_create_drillhole_parameter_weight_constraint_database(GXDBPtr arg1, int32_t arg2, GXREGPtr arg3, const gx_string_type& arg4)
{
    GXDU::create_drillhole_parameter_weight_constraint_database(arg1, arg2, arg3, arg4);
}
inline void GXDU_wrap_calculate_draped_survey_altitude(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXIMGPtr arg5, int32_t arg6, double arg7, double arg8, double arg9, int32_t arg10, double arg11, double arg12)
{
    GXDU::calculate_draped_survey_altitude(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12);
}
inline void GXDU_wrap_calculate_draped_survey_altitude2(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXIMGPtr arg5, int32_t arg6, int32_t arg7, double arg8, double arg9, double arg10, double arg11, int32_t arg12, double arg13, double arg14)
{
    GXDU::calculate_draped_survey_altitude2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14);
}
inline void GXDU_wrap_direct_grid_data_to_voxel(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, const gx_string_type& arg6, double arg7, double arg8, double arg9, int32_t arg10, int32_t arg11, int32_t arg12, double arg13, double arg14, double arg15, int32_t arg16)
{
    GXDU::direct_grid_data_to_voxel(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, (DU_DIRECTGRID_METHOD)arg16);
}
inline void GXDU_wrap_direct_grid_item_counts_to_voxel(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, const gx_string_type& arg6, double arg7, double arg8, double arg9, int32_t arg10, int32_t arg11, int32_t arg12, double arg13, double arg14, double arg15, bool arg16)
{
    GXDU::direct_grid_item_counts_to_voxel(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16);
}

void gxPythonImportGXDU()
{

    class_<GXDU, boost::noncopyable> pyClass("GXDU",
            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		DU functions provide a variety of common utilities that can be applied\n"
            "   		efficiently to the contents of a database. Most DU library functions take\n"
            "   		as their first argument a DB object, and apply standard processes to data\n"
            "   		stored in an OASIS database, including import and export functions.\n"
            "   	\n\n"

            "\n\n**Note:**\n\n"

            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		The following defines are used by GX functions but are not required\n"
            "   		for any methods:\n"
            "   \n"
            "   		\\ :ref:`DU_LINES`\\ \n"
            "   	\n\n"
            , no_init);


    pyClass.def("table_look1", &GXDU_wrap_table_look1,
                "table_look1((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (str)arg5, (str)arg6, (int)arg7, (float)arg8, (GXTB)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new channel using a single reference table\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle\n"
                ":type arg2: int\n"
                ":param arg3: Lookup reference channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Output Channel Token     [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: Reference field name in table\n"
                ":type arg5: str\n"
                ":param arg6: Lookup output name in table\n"
                ":type arg6: str\n"
                ":param arg7: \\ :ref:`DU_LOOKUP`\\ \n"
                ":type arg7: int\n"
                ":param arg8: CLOSE lookup distance. If 0.0, distance is calculated from lookup reference channel.\n"
                ":type arg8: float\n"
                ":param arg9: TB table Object\n"
                ":type arg9: :class:`geosoft.gxapi.GXTB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Fails if table does not contain requested fields.\n"
                "   					The nominal data sample spacing for the CLOSE options is\n"
                "   					calculated by finding the fiducial increment the\n"
                "   					- primary index channel for Lookup1C_DU;\n"
                "   					- secondary index channel for Lookup2C_DU, LookupIValC_DU\n"
                "   					and LookupRValC_DU\n"
                "   				\n\n"
               ).staticmethod("table_look1");
    pyClass.def("table_look2", &GXDU_wrap_table_look2,
                "table_look2((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (str)arg6, (str)arg7, (str)arg8, (int)arg9, (float)arg10, (GXTB)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new channel using a double reference  table.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle\n"
                ":type arg2: int\n"
                ":param arg3: Primary reference channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Secondary reference channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Output channel [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: Primary reference field name in table\n"
                ":type arg6: str\n"
                ":param arg7: Secondary reference field name in table\n"
                ":type arg7: str\n"
                ":param arg8: Lookup result field name in table\n"
                ":type arg8: str\n"
                ":param arg9: \\ :ref:`DU_LOOKUP`\\ \n"
                ":type arg9: int\n"
                ":param arg10: CLOSE lookup distance.  If 0.0, distance is calculated from secondary reference channel.\n"
                ":type arg10: float\n"
                ":param arg11: Table Object\n"
                ":type arg11: :class:`geosoft.gxapi.GXTB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Fails if table does not contain requested fields.\n"
                "   					The nominal data sample spacing for the CLOSE options is\n"
                "   					calculated by finding the fiducial increment the\n"
                "   					- primary index channel for Lookup1C_DU;\n"
                "   					- secondary index channel for Lookup2C_DU, LookupIValC_DU\n"
                "   					and LookupRValC_DU\n"
                "   				\n\n"
               ).staticmethod("table_look2");
    pyClass.def("table_look_i2", &GXDU_wrap_table_look_i2,
                "table_look_i2((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (str)arg6, (str)arg7, (str)arg8, (int)arg9, (float)arg10, (GXTB)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Create a new channel using constant integer primary\n"
                "   					reference and a secondary reference table.\n"
                "   				\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle\n"
                ":type arg2: int\n"
                ":param arg3: Lookup primary reference value\n"
                ":type arg3: int\n"
                ":param arg4: Lookup secondary reference channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Output Channel Token [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: Primary reference field name in table\n"
                ":type arg6: str\n"
                ":param arg7: Secondary reference field name in table\n"
                ":type arg7: str\n"
                ":param arg8: Lookup result field name in table\n"
                ":type arg8: str\n"
                ":param arg9: \\ :ref:`DU_LOOKUP`\\ \n"
                ":type arg9: int\n"
                ":param arg10: CLOSE lookup distance.  If 0.0, distance calculated from secondary reference channel.\n"
                ":type arg10: float\n"
                ":param arg11: Table Object\n"
                ":type arg11: :class:`geosoft.gxapi.GXTB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Fails if table does not contain requested fields.\n"
                "   					The nominal data sample spacing for the CLOSE options is\n"
                "   					calculated by finding the fiducial increment the\n"
                "   					- primary index channel for Lookup1C_DU;\n"
                "   					- secondary index channel for Lookup2C_DU, LookupIValC_DU\n"
                "   					and LookupRValC_DU\n"
                "   				\n\n"
               ).staticmethod("table_look_i2");
    pyClass.def("table_look_r2", &GXDU_wrap_table_look_r2,
                "table_look_r2((GXDB)arg1, (int)arg2, (float)arg3, (int)arg4, (int)arg5, (str)arg6, (str)arg7, (str)arg8, (int)arg9, (float)arg10, (GXTB)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Create a new channel using a constant real primary\n"
                "   					reference and a secondary reference table.\n"
                "   				\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle\n"
                ":type arg2: int\n"
                ":param arg3: Primary reference value\n"
                ":type arg3: float\n"
                ":param arg4: Secondary reference value [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Output Channel Token [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: Primary reference field name in table\n"
                ":type arg6: str\n"
                ":param arg7: Secondary reference field name in table\n"
                ":type arg7: str\n"
                ":param arg8: Lookup result field name in table\n"
                ":type arg8: str\n"
                ":param arg9: \\ :ref:`DU_LOOKUP`\\ \n"
                ":type arg9: int\n"
                ":param arg10: CLOSE lookup distance.  If 0.0, distance calculated from secondary reference channel.\n"
                ":type arg10: float\n"
                ":param arg11: Table Object\n"
                ":type arg11: :class:`geosoft.gxapi.GXTB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Fails if table does not contain requested fields.\n"
                "   					The nominal data sample spacing for the CLOSE options is\n"
                "   					calculated by finding the fiducial increment the\n"
                "   					- primary index channel for Lookup1C_DU;\n"
                "   					- secondary index channel for Lookup2C_DU, LookupIValC_DU\n"
                "   					and LookupRValC_DU\n"
                "   				\n\n"
               ).staticmethod("table_look_r2");
    pyClass.def("ado_table_names", &GXDU_wrap_ado_table_names,
                "ado_table_names((str)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Scans a ADO-compliant database and returns the table names in a VV\n\n"

                ":param arg1: Database connection string\n"
                ":type arg1: str\n"
                ":param arg2: VV to return names in\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The VV must be created to hold strings of length\n"
                "   					STR_DB_SYMBOL; i.e. use\n"
                "   					Creat_VV(-STR_DB_SYMBOL, 0), or it will assert.\n"
                "   				\n\n"
               ).staticmethod("ado_table_names");
    pyClass.def("an_sig", &GXDU_wrap_an_sig,
                "an_sig((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the Analytic Signal of a channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line handle\n"
                ":type arg2: int\n"
                ":param arg3: Input channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Output Analytic Signal channel [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("an_sig");
    pyClass.def("append", &GXDU_wrap_append,
                "append((GXDB)arg1, (GXDB)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Append a source database onto a destination database.\n\n"

                ":param arg1: Source Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Destination Database\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg3: Ignore write protection on channels? (TRUE or FALSE)\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the source database and destination database have channels\n"
                "   					with the same name, then data is appended onto the end\n"
                "   					of the channel in lines which have the same number.\n"
                "   \n"
                "   					If a channel in the destination database is not also in the source\n"
                "   					database, it is ignored.\n"
                "   				\n\n"
               ).staticmethod("append");
    pyClass.def("avg_azimuth", &GXDU_wrap_avg_azimuth,
                "avg_azimuth((GXDB)arg1, (float)arg2, (float_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns average azimuth of selected lines.\n\n"

                ":param arg1: Database Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Precision in degrees (1 to 45)\n"
                ":type arg2: float\n"
                ":param arg3: Azimuth value returned\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Direction in degrees azimuth (clockwise relative\n"
                "   					the +Y direction). The result is in the range\n"
                "   					-90 < azimuth <= 90. The method handles lines going\n"
                "   					in opposite directions (they do not average to 0!)\n"
                "   					The method takes a precision, which is used to generate\n"
                "   					a series of \"test\" angles.\n"
                "   					The dot product of the line directions is taken\n"
                "   					with each of the test angles, and the absolute values summed.\n"
                "   					The maximum value occurs at the angle which most closely\n"
                "   					approximates the trend direction of the lines.\n"
                "   				\n\n"
               ).staticmethod("avg_azimuth");
    pyClass.def("base_data", &GXDU_wrap_base_data,
                "base_data((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (GXTB)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method corrects an entire database line using a\n"
                "   					time-based correction table. It is given 2 input channel\n"
                "   					tokens and 1 output channel token as well as the table\n"
                "   					object to use.\n"
                "   				\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle to apply correction to\n"
                ":type arg2: int\n"
                ":param arg3: Input Channel Token  [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Time Channel Token   [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Output Channel Token [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: Table Object (a Date/Time/Correction Table)\n"
                ":type arg6: :class:`geosoft.gxapi.GXTB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("base_data");
    pyClass.def("base_data_ex", &GXDU_wrap_base_data_ex,
                "base_data_ex((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (GXTB)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method corrects an entire database line using a\n"
                "   					time-based correction table. It is given 2 input channel\n"
                "   					tokens and 1 output channel token as well as the table\n"
                "   					object to use (table sort flag=1 for sort, =0 for no sort).\n"
                "   				\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle to apply correction to\n"
                ":type arg2: int\n"
                ":param arg3: Input Channel Token  [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Time Channel Token   [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Output Channel Token [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: Table Object (a Date/Time/Correction Table)\n"
                ":type arg6: :class:`geosoft.gxapi.GXTB`\n"
                ":param arg7: Table sort flag: 0 - do not sort, 1 - do sort.\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               ).staticmethod("base_data_ex");
    pyClass.def("bound_line", &GXDU_wrap_bound_line,
                "bound_line((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (GXPLY)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set map boundary clip limits.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle [DB_LOCK_READWRITE]\n"
                ":type arg2: int\n"
                ":param arg3: X Channel   [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Channel   [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Polygon Object to use\n"
                ":type arg5: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("bound_line");
    pyClass.def("bp_filt", &GXDU_wrap_bp_filt,
                "bp_filt((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (float)arg5, (float)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method applies a band-pass filter to the specified\n"
                "   					line/channel and places the output in the output channel.\n"
                "   				\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line handle\n"
                ":type arg2: int\n"
                ":param arg3: Input channel to filter [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Output filtered channel [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: Short wavelength cutoff, 0 for highpass\n"
                ":type arg5: float\n"
                ":param arg6: Long wavelength cutoff, 0 for lowpass\n"
                ":type arg6: float\n"
                ":param arg7: Filter Length, 0 for default length\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the short and long wavelengths are <= 0, the input channel\n"
                "   					is simply copied to the output channel without filtering.\n"
                "   				\n\n"
               ).staticmethod("bp_filt");
    pyClass.def("break_line", &GXDU_wrap_break_line,
                "break_line((GXDB)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Break up a line based on line numbers in a channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line to be broken up [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Channel containing line numbers [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("break_line");
    pyClass.def("break_line2", &GXDU_wrap_break_line2,
                "break_line2((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Break up a line based on line numbers in a channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line to be broken up [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Channel containing line numbers [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Reset starting fiducials to zero (0: No, 1: Yes)\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The same as BreakLine, but with an option to reset each line's starting fiducial to zero.\n\n"
               ).staticmethod("break_line2");
    pyClass.def("break_line_to_groups", &GXDU_wrap_break_line_to_groups,
                "break_line_to_groups((GXDB)arg1, (int)arg2, (int)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Break up a line into group-lines based on a channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line to be broken up [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Channel containing line numbers [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Class name for new group lines (can be \"\")\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The original line will be deleted.\n"
                "   					This is similar to \\ :func:`geosoft.gxapi.GXDU.break_line`\\ , but the output lines\n"
                "   					are \"group\" lines, without the line type letters at the\n"
                "   					start. (See db.gxh for information of Group Lines).\n"
                "   					All channels are associated with each group line, and the\n"
                "   					input class name is assigned to each group.\n"
                "   					Class names for\n"
                "   					groups ensure that (for instance) if you add a new channel to\n"
                "   					one group of a given class, it will get added to all other\n"
                "   					groups in the same class. If the class name is left empty, then\n"
                "   					this will NOT be true. (Groups without class names are treated\n"
                "   					as isolated entities for the purposes of channel loading).\n"
                "   				\n\n"
               ).staticmethod("break_line_to_groups");
    pyClass.def("break_line_to_groups2", &GXDU_wrap_break_line_to_groups2,
                "break_line_to_groups2((GXDB)arg1, (int)arg2, (int)arg3, (str)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Break up a line into group-lines based on a channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line to be broken up [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Channel containing line numbers [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Class name for new group lines (can be \"\")\n"
                ":type arg4: str\n"
                ":param arg5: Reset starting fiducials to zero (0: No, 1: Yes)\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The same as BreakLineToGroups, but with an option to reset each line's starting fiducial to zero.\n\n"
               ).staticmethod("break_line_to_groups2");
    pyClass.def("b_spline", &GXDU_wrap_b_spline,
                "b_spline((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (float)arg5, (float)arg6, (float)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   B-spline Interpolate a Channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line handle\n"
                ":type arg2: int\n"
                ":param arg3: Channel to interpolate [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Output interpolated channel [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: Data error (Std Dev > 0.0)\n"
                ":type arg5: float\n"
                ":param arg6: Roughness (Rou > 0.0)\n"
                ":type arg6: float\n"
                ":param arg7: Tension (0.<= Tension <=1.)\n"
                ":type arg7: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDU.trend`\\ \n\n"
               ).staticmethod("b_spline");
    pyClass.def("closest_point", &GXDU_wrap_closest_point,
                "closest_point((GXDB)arg1, (float)arg2, (float)arg3, (float_ref)arg4, (float_ref)arg5, (int_ref)arg6, (float_ref)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return closest data point to input location.\n\n"

                ":param arg1: DB\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: X location\n"
                ":type arg2: float\n"
                ":param arg3: Y location\n"
                ":type arg3: float\n"
                ":param arg4: located X location\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: located Y location\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: line for located point\n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg7: fiducial of located point\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Selected lines are scanned for the (X, Y) location\n"
                "   					which is closest to the input location.\n"
                "   					The line and fiducial of the point are returned.\n"
                "   \n"
                "   					Will register an error if no valid (X, Y) locations\n"
                "   					are found.\n"
                "   				\n\n"
               ).staticmethod("closest_point");
    pyClass.def("copy_line", &GXDU_wrap_copy_line,
                "copy_line((GXDB)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a line.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Input Line  [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Output Line [DB_LOCK_READWRITE]\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Existing channels in the output line will be replaced\n"
                "   					by copied channels.\n"
                "   				\n\n"
               ).staticmethod("copy_line");
    pyClass.def("copy_line_across", &GXDU_wrap_copy_line_across,
                "copy_line_across((GXDB)arg1, (int)arg2, (GXDB)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a line from one database to another.\n\n"

                ":param arg1: Input Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Input Line  [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Output Database\n"
                ":type arg3: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg4: Output Line [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Existing channels in the output line will be replaced\n"
                "   					by copied channels.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDU.copy_line_chan_across`\\  function\n\n"
               ).staticmethod("copy_line_across");
    pyClass.def("copy_line_chan_across", &GXDU_wrap_copy_line_chan_across,
                "copy_line_chan_across((GXDB)arg1, (int)arg2, (GXVV)arg3, (GXDB)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a list of channels in a line from one database to another.\n\n"

                ":param arg1: Input Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Input Line   [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: VV containing a list of channel symbols, must be of INT\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Output Database\n"
                ":type arg4: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg5: Output Line  [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Existing channels in the output line will be replaced\n"
                "   					by copied channels.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDU.copy_line_across`\\  function\n\n"
               ).staticmethod("copy_line_chan_across");
    pyClass.def("copy_line_masked", &GXDU_wrap_copy_line_masked,
                "copy_line_masked((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a line, prune items based on a mask channel\n\n"

                ":param arg1: Database Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Input  Line Symbol [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Mask Channel Symbol [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`VVU_PRUNE`\\ \n"
                ":type arg4: int\n"
                ":param arg5: Output Line Symbol [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The input line's channel data is ReFidded to the mask\n"
                "   					channel, and then pruned from the output line data,\n"
                "   					based on the value of the VVU_PRUNE_XXX variable.\n"
                "   					For VVU_PRUNE_DUMMY, only those items where the mask channel\n"
                "   					value is not a dummy are retained, while the complement\n"
                "   					is retained for VV_PRUNE_VALID.\n"
                "   				\n\n"
               ).staticmethod("copy_line_masked");
    pyClass.def("dao_table_names", &GXDU_wrap_dao_table_names,
                "dao_table_names((str)arg1, (str)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Scans a DAO-compliant database and returns the table names in a VV\n\n"

                ":param arg1: Database file name\n"
                ":type arg1: str\n"
                ":param arg2: Database Type\n"
                ":type arg2: str\n"
                ":param arg3: VV to return names in\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The VV must be created to hold strings of length\n"
                "   					STR_DB_SYMBOL; i.e. use\n"
                "   					Creat_VV(-STR_DB_SYMBOL, 0), or it will assert.\n"
                "   				\n\n"
               ).staticmethod("dao_table_names");
    pyClass.def("decimate", &GXDU_wrap_decimate,
                "decimate((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy and decimate a channel\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line handle\n"
                ":type arg2: int\n"
                ":param arg3: Origin Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Destination Channel [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: Decimation factor\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("decimate");
    pyClass.def("diff", &GXDU_wrap_diff,
                "diff((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate differences within a channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line handle\n"
                ":type arg2: int\n"
                ":param arg3: Origin Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Destination Channel [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: Number of differences\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Differences with dummies result in dummies.\n"
                "   					An even number of differences locates data accurately.\n"
                "   					An odd number of differences locates result 1/2 element lower\n"
                "   					in the VV.\n"
                "   				\n\n"
               ).staticmethod("diff");
    pyClass.def("distance", &GXDU_wrap_distance,
                "distance((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a distance channel from X and Y.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line symbol\n"
                ":type arg2: int\n"
                ":param arg3: X channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Output Distance channel [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("distance");
    pyClass.def("distance_3d", &GXDU_wrap_distance_3d,
                "distance_3d((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a distance channel from XY or XYZ with direction options.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line symbol\n"
                ":type arg2: int\n"
                ":param arg3: X channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Z channel [DB_LOCK_READONLY] (can be NULLSYMB)\n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`DU_DISTANCE_CHANNEL_TYPE`\\ \n"
                ":type arg6: int\n"
                ":param arg7: Output Distance channel [DB_LOCK_READWRITE]\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"
               ).staticmethod("distance_3d");
    pyClass.def("distline", &GXDU_wrap_distline,
                "distline((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (float_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate cummulative distance for a line.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line symbol\n"
                ":type arg2: int\n"
                ":param arg3: X channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Cummulative distance (retruned)\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("distline");
    pyClass.def("dup_chan_locks", &GXDU_wrap_dup_chan_locks,
                "dup_chan_locks((GXDB)arg1, (GXDB)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Duplicate all channels protect-info from input DB.\n\n"

                ":param arg1: Input Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Output Database handle.\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("dup_chan_locks");
    pyClass.def("dup_chans", &GXDU_wrap_dup_chans,
                "dup_chans((GXDB)arg1, (GXDB)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Duplicate all channels from input DB.\n\n"

                ":param arg1: Input Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Output Database handle.\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("dup_chans");
    pyClass.def("edit_duplicates", &GXDU_wrap_edit_duplicates,
                "edit_duplicates((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (float)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Edit duplicate readings at individual location\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line\n"
                ":type arg2: int\n"
                ":param arg3: Channel X, unlocked\n"
                ":type arg3: int\n"
                ":param arg4: Channel Y, unlocked\n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`DB_DUP`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`DB_DUPEDIT`\\ \n"
                ":type arg6: int\n"
                ":param arg7: Fiducial number (required if DB_DUPEDIT_SINGLE)\n"
                ":type arg7: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					All the channels must be of the same fid incr/start and length.\n"
                "   					Protected channels are modified automatically.\n"
                "   				\n\n"
               ).staticmethod("edit_duplicates");
    pyClass.def("export1", &GXDU_wrap_export1,
                "export1((GXDB)arg1, (int)arg2, (str)arg3, (GXVV)arg4, (int)arg5, (str)arg6, (int)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export to a specific format.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: \\ :ref:`DU_EXPORT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Current line\n"
                ":type arg3: str\n"
                ":param arg4: list of channels - channel symbols stored as INT\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: \\ :ref:`DU_CHANNELS`\\ \n"
                ":type arg5: int\n"
                ":param arg6: data file name\n"
                ":type arg6: str\n"
                ":param arg7: Write out dummies?\n"
                ":type arg7: int\n"
                ":param arg8: Include a header with channel names?\n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					For databases with both groups and lines:\n"
                "   					If both lines and groups are selected, save only the lines.\n"
                "   					If no lines are selected, (only groups), save the current line\n"
                "   					if it is (1) a group and (2) selected, else save the first selected\n"
                "   					group. ---\n"
                "   					Option to filter out data where one of the channels has a dummy in it.\n"
                "   					Option to allow a header with the channel names.\n"
                "   \n"
                "   					The DU_CHANNELS_DISPLAYED option can be used to export any selection of\n"
                "   					channels, listed by the symbols (DB_SYMB) values, cast to int values and\n"
                "   					stored in a VV.\n"
                "   				\n\n"
               ).staticmethod("export1");
    pyClass.def("export2", &GXDU_wrap_export2,
                "export2((GXDB)arg1, (int)arg2, (str)arg3, (GXVV)arg4, (int)arg5, (str)arg6, (int)arg7, (int)arg8, (int)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Like \\ :func:`geosoft.gxapi.GXDU.export1`\\ , but include line names as data.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: \\ :ref:`DU_EXPORT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Current line\n"
                ":type arg3: str\n"
                ":param arg4: list of channels - channel symbols stored as INT\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: \\ :ref:`DU_CHANNELS`\\ \n"
                ":type arg5: int\n"
                ":param arg6: data file name\n"
                ":type arg6: str\n"
                ":param arg7: Write out dummies?\n"
                ":type arg7: int\n"
                ":param arg8: Include a header with channel names?\n"
                ":type arg8: int\n"
                ":param arg9: Include line names as data?\n"
                ":type arg9: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					See \\ :func:`geosoft.gxapi.GXDU.export1`\\ .\n"
                "   					The line names are printed as the first column of data exported.\n"
                "   				\n\n"
               ).staticmethod("export2");
    pyClass.def("export_amira", &GXDU_wrap_export_amira,
                "export_amira((GXDB)arg1, (GXWA)arg2, (str)arg3, (str)arg4, (str)arg5, (str)arg6, (str)arg7, (str)arg8, (str)arg9, (str)arg10, (str)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export to database an AMIRA data file.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: AMIRA data file handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg3: Single column channel names, supporting comma (,) separated names of multiple channels, maximum 32 channels\n"
                ":type arg3: str\n"
                ":param arg4: VA channel name, required\n"
                ":type arg4: str\n"
                ":param arg5: Optional Time   channel name (must be VA channel and same array size as above VA channel)\n"
                ":type arg5: str\n"
                ":param arg6: Optional Errors channel name (must be VA channel and same array size as above VA channel)\n"
                ":type arg6: str\n"
                ":param arg7: Mandatory fields: DATATYPE\n"
                ":type arg7: str\n"
                ":param arg8: UNITS\n"
                ":type arg8: str\n"
                ":param arg9: CONFIG\n"
                ":type arg9: str\n"
                ":param arg10: INSTRUMENT\n"
                ":type arg10: str\n"
                ":param arg11: FREQUENCY\n"
                ":type arg11: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Other defined FIELDS stored in the database (see \\ :func:`geosoft.gxapi.GXDU.import_amira`\\  function)\n"
                "   					will be automatically included in the export\n"
                "   				\n\n"
               ).staticmethod("export_amira");
    pyClass.def("export_aseg", &GXDU_wrap_export_aseg,
                "export_aseg((GXDB)arg1, (str)arg2, (GXVV)arg3, (int)arg4, (str)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export to ASEG-GDF format file(s).\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Current line\n"
                ":type arg2: str\n"
                ":param arg3: Displayed channels\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: \\ :ref:`DU_CHANNELS`\\ \n"
                ":type arg4: int\n"
                ":param arg5: header file name\n"
                ":type arg5: str\n"
                ":param arg6: data file name\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					At least one of the header file\n"
                "   					or data file names must be set. (Unset names will get the\n"
                "   					same file name, but with the extensions .dfn (header) or\n"
                "   					.dat (data).\n"
                "   					For databases with both groups and lines:\n"
                "   					If both lines and groups are selected, save only the lines.\n"
                "   					If no lines are selected, (only groups), save the current line\n"
                "   					if it is (1) a group and (2) selected, else save the first selected\n"
                "   					group. ---\n"
                "   				\n\n"
               ).staticmethod("export_aseg");
    pyClass.def("export_aseg_proj", &GXDU_wrap_export_aseg_proj,
                "export_aseg_proj((GXDB)arg1, (str)arg2, (GXVV)arg3, (int)arg4, (str)arg5, (str)arg6, (str)arg7, (GXIPJ)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export to ASEG-GDF format file(s) (supports projections).\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Current line\n"
                ":type arg2: str\n"
                ":param arg3: Displayed channels\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: \\ :ref:`DU_CHANNELS`\\ \n"
                ":type arg4: int\n"
                ":param arg5: export header file name\n"
                ":type arg5: str\n"
                ":param arg6: export data file name\n"
                ":type arg6: str\n"
                ":param arg7: export projection file name\n"
                ":type arg7: str\n"
                ":param arg8: Projection handle\n"
                ":type arg8: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					At least one of the header file\n"
                "   					or data file names must be set. (Unset names will get the\n"
                "   					same file name, but with the extensions .dfn (header) or\n"
                "   					.dat (data).\n"
                "   					For databases with both groups and lines:\n"
                "   					If both lines and groups are selected, save only the lines.\n"
                "   					If no lines are selected, (only groups), save the current line\n"
                "   					if it is (1) a group and (2) selected, else save the first selected\n"
                "   					group. ---\n"
                "   \n"
                "   					This version supports projections\n"
                "   				\n\n"
               ).staticmethod("export_aseg_proj");
    pyClass.def("export_chan_crc", &GXDU_wrap_export_chan_crc,
                "export_chan_crc((GXDB)arg1, (int)arg2, (int_ref)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a channel as XML and compute a CRC value.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Channel\n"
                ":type arg2: int\n"
                ":param arg3: CRC Value returned\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: File name to generate with XML\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The output file is an XML describing the channel. The\n"
                "   					CRC is of the channel data ONLY. To compute a CRC of the\n"
                "   					full channel (include metadata) do a CRC of the generated\n"
                "   					file.\n"
                "   				\n\n"
               ).staticmethod("export_chan_crc");
    pyClass.def("export_csv", &GXDU_wrap_export_csv,
                "export_csv((GXDB)arg1, (str)arg2, (GXVV)arg3, (int)arg4, (str)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export to a CSV file.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Current line\n"
                ":type arg2: str\n"
                ":param arg3: Displayed channels\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: \\ :ref:`DU_CHANNELS`\\ \n"
                ":type arg4: int\n"
                ":param arg5: data file name\n"
                ":type arg5: str\n"
                ":param arg6: Write out dummies?\n"
                ":type arg6: int\n"
                ":param arg7: Include a header with channel names?\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					For databases with both groups and lines:\n"
                "   					If both lines and groups are selected, save only the lines.\n"
                "   					If no lines are selected, (only groups), save the current line\n"
                "   					if it is (1) a group and (2) selected, else save the first selected\n"
                "   					group. ---\n"
                "   					Option to filter out data where one of the channels has a dummy in it.\n"
                "   					Option to allow a header with the channel names.\n"
                "   				\n\n"
               ).staticmethod("export_csv");
    pyClass.def("export_database_crc", &GXDU_wrap_export_database_crc,
                "export_database_crc((GXDB)arg1, (int_ref)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a channel as XML and compute a CRC value.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: CRC Value returned\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: File name to generate with XML\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The output file is an XML describing the channel. The\n"
                "   					CRC is of the channel data ONLY. To compute a CRC of the\n"
                "   					full channel (include metadata) do a CRC of the generated\n"
                "   					file.\n"
                "   				\n\n"
               ).staticmethod("export_database_crc");
    pyClass.def("export_gbn", &GXDU_wrap_export_gbn,
                "export_gbn((GXDB)arg1, (GXVV)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export to a GBN data file.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: List of channels to export\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: export data file name\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The iDispChanList_DBE or \\ :func:`geosoft.gxapi.GXDB.symb_list`\\  methods can be\n"
                "   					used to obtain a list of channels.\n"
                "   				\n\n"
               ).staticmethod("export_gbn");
    pyClass.def("export_mdb", &GXDU_wrap_export_mdb,
                "export_mdb((GXDB)arg1, (str)arg2, (GXVV)arg3, (int)arg4, (int)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export to a Microsoft Access Database (MDB) file.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Current line\n"
                ":type arg2: str\n"
                ":param arg3: Displayed channels\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: \\ :ref:`DU_CHANNELS`\\ \n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`DU_LINEOUT`\\ \n"
                ":type arg5: int\n"
                ":param arg6: export data file name\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Similar to \\ :func:`geosoft.gxapi.GXDU.export_gbn`\\ , with the addition that\n"
                "   					Groups go to individual tables, and lines go to\n"
                "   					a single table, or individual tables, based on the\n"
                "   					value of \\ :ref:`DU_LINEOUT`\\ \n"
                "   				\n\n"
               ).staticmethod("export_mdb");
    pyClass.def("export_geodatabase", &GXDU_wrap_export_geodatabase,
                "export_geodatabase((GXDB)arg1, (str)arg2, (str)arg3, (GXVV)arg4, (int)arg5, (int)arg6, (int)arg7, (str)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export to a ESRI Geodatabase file.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Feature class name\n"
                ":type arg2: str\n"
                ":param arg3: Current line\n"
                ":type arg3: str\n"
                ":param arg4: Displayed channels\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: \\ :ref:`DU_CHANNELS`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`DU_FEATURE_TYPE_OUTPUT`\\ \n"
                ":type arg6: int\n"
                ":param arg7: \\ :ref:`DU_LINEOUT`\\ \n"
                ":type arg7: int\n"
                ":param arg8: export data file name\n"
                ":type arg8: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Similar to \\ :func:`geosoft.gxapi.GXDU.export_gbn`\\ , with the addition that\n"
                "   					Groups go to individual tables, and lines go to\n"
                "   					a single table, or individual tables, based on the\n"
                "   					value of \\ :ref:`DU_LINEOUT`\\ \n"
                "   				\n\n"
               ).staticmethod("export_geodatabase");
    pyClass.def("get_existing_feature_classes_in_geodatabase", &GXDU_wrap_get_existing_feature_classes_in_geodatabase,
                "get_existing_feature_classes_in_geodatabase((GXDB)arg1, (str)arg2, (GXLST)arg3, (GXVV)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Searches the geodatabases for an existing Feature class.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: File geodatabase\n"
                ":type arg2: str\n"
                ":param arg3: Feature class names to verify\n"
                ":type arg3: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg4: Output list of existing feature class names\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: 0 - Feature class does not exist\n"
                "          						1 - Feature class exists\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Searches the geodatabases for an existing Feature class\n"
                "   				\n\n"
               ).staticmethod("get_existing_feature_classes_in_geodatabase");
    pyClass.def("export_shp", &GXDU_wrap_export_shp,
                "export_shp((GXDB)arg1, (str)arg2, (GXVV)arg3, (int)arg4, (int)arg5, (str)arg6, (GXLST)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export to a shape file or files.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Current line\n"
                ":type arg2: str\n"
                ":param arg3: Displayed channels\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: \\ :ref:`DU_CHANNELS`\\ \n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`DU_LINEOUT`\\ \n"
                ":type arg5: int\n"
                ":param arg6: export shape file name or base filename (shp assumed if no extension given)\n"
                ":type arg6: str\n"
                ":param arg7: LST object will be filled with shape files created\n"
                ":type arg7: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Similar to \\ :func:`geosoft.gxapi.GXDU.export_mdb`\\ , with the addition that groups go to indiviual files\n"
                "   					with group name suffixes, and lines go to a single file, or multiple files\n"
                "   					with line name suffixes, based on the value of DU_LINEOUT.\n"
                "   				\n\n"
               ).staticmethod("export_shp");
    pyClass.def("export_xyz", &GXDU_wrap_export_xyz,
                "export_xyz((GXDB)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export XYZdata from a database to an XYZ file.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: export data file name\n"
                ":type arg2: str\n"
                ":param arg3: export template name\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1. The export template can be in the local directory or the GEOSOFT\n"
                "   					directory.  The import data file must include the path if it is not\n"
                "   					in the local directory.\n"
                "   \n"
                "   					2. Both the import template and data file must exist.\n"
                "   \n"
                "   					3. Sample Template file\n"
                "   \n"
                "   					[EXPORT XYZ]\n"
                "   					EXPORT     CHAN {,FORMAT} {,WIDTH} {,DECIMAL}\n"
                "   					WRITEDUMMY YES\n"
                "   					CLIPMAP    YES\n"
                "   					MAXPOINTS  1000\n"
                "   					INCREMENT  .5\n"
                "   \n"
                "   					4. This can be used to export a group, but the group must be the\n"
                "   					currently displayed line, and only that group will be exported.\n"
                "   				\n\n"
               ).staticmethod("export_xyz");
    pyClass.def("export_xyz2", &GXDU_wrap_export_xyz2,
                "export_xyz2((GXDB)arg1, (GXWA)arg2, (GXRA)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export XYZdata from a database to an XYZ file, using file handles.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: export data file WA handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg3: export template file RA handle\n"
                ":type arg3: :class:`geosoft.gxapi.GXRA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDU.export_xyz`\\ \n\n"
               ).staticmethod("export_xyz2");
    pyClass.def("fft", &GXDU_wrap_fft,
                "fft((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply an FFT to space data.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line handle\n"
                ":type arg2: int\n"
                ":param arg3: space Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: real Channel  [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: imaginary Channel [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("fft");
    pyClass.def("filter", &GXDU_wrap_filter,
                "filter((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (GXFLT)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply a convolution filter to a channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line handle\n"
                ":type arg2: int\n"
                ":param arg3: Input channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Output filtered channel [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: Filter handle (FLT)\n"
                ":type arg5: :class:`geosoft.gxapi.GXFLT`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("filter");
    pyClass.def("gen_lev", &GXDU_wrap_gen_lev,
                "gen_lev((GXDB)arg1, (str)arg2, (str)arg3, (float)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a Level table from an Intersection Table.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Input Table file Name\n"
                ":type arg2: str\n"
                ":param arg3: Output Table file Name\n"
                ":type arg3: str\n"
                ":param arg4: Max. gradient\n"
                ":type arg4: float\n"
                ":param arg5: \\ :ref:`DU_LEVEL`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("gen_lev");
    pyClass.def("gen_lev_db", &GXDU_wrap_gen_lev_db,
                "gen_lev_db((GXDB)arg1, (str)arg2, (float)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a Level table from an Intersection Database\n\n"

                ":param arg1: Input intersection database object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Output Table File Name\n"
                ":type arg2: str\n"
                ":param arg3: Max. gradient\n"
                ":type arg3: float\n"
                ":param arg4: \\ :ref:`DU_LEVEL`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Requires channels with the following names:\n"
                "   \n"
                "   					ine, TFid, TZ, TDZ\n"
                "   					Line, LFid, LZ, LDZ\n"
                "   					Mask\n"
                "   				\n\n"
               ).staticmethod("gen_lev_db");
    pyClass.def("gen_xyz_temp", &GXDU_wrap_gen_xyz_temp,
                "gen_xyz_temp((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate default XYZ template for a XYZ file.\n\n"

                ":param arg1: xyz file name\n"
                ":type arg1: str\n"
                ":param arg2: template file name to create\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("gen_xyz_temp");
    pyClass.def("get_xyz_num_fields", &GXDU_wrap_get_xyz_num_fields,
                "get_xyz_num_fields((str)arg1, (int_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of fields in the XYZ file.\n\n"

                ":param arg1: xyz file name\n"
                ":type arg1: str\n"
                ":param arg2: returned number of fields\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.1.0\n\n"
               ).staticmethod("get_xyz_num_fields");
    pyClass.def("get_chan_data_lst", &GXDU_wrap_get_chan_data_lst,
                "get_chan_data_lst((GXDB)arg1, (int)arg2, (int)arg3, (GXLST)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Populate a LST with unique items in a channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Data Channel\n"
                ":type arg2: int\n"
                ":param arg3: Mask Channel  (can be NULLSYMB)\n"
                ":type arg3: int\n"
                ":param arg4: LST object to populate\n"
                ":type arg4: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Items from all selected lines are collected,\n"
                "   					sorted, and duplicates removed. The output\n"
                "   					LST name and value are set to the item values.\n"
                "   					Non-string channels are converted internally to\n"
                "   					string values using Copy_VV,\n"
                "   					so results may differ from what\n"
                "   					you may expect given the current channel's display\n"
                "   					width and number of decimals.\n"
                "   					If a mask channel is selected, then only those items\n"
                "   					where the mask channel is not a dummy are collected.\n"
                "   				\n\n"
               ).staticmethod("get_chan_data_lst");
    pyClass.def("get_chan_data_vv", &GXDU_wrap_get_chan_data_vv,
                "get_chan_data_vv((GXDB)arg1, (int)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Populate a VV with unique items in a channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Channel\n"
                ":type arg2: int\n"
                ":param arg3: Mask Channel  (can be NULLSYMB)\n"
                ":type arg3: int\n"
                ":param arg4: VV object to populate\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Items from all selected lines are collected,\n"
                "   					sorted, and duplicates removed.\n"
                "   					The data is collected in the channel's data type,\n"
                "   					so normal \\ :func:`geosoft.gxapi.GXVV.sort`\\  rules apply.\n"
                "   					If the output VV and channel type are not the\n"
                "   					same, then the data is converted using the\n"
                "   					Copy_VV function, so see that for conversion rules.\n"
                "   					If a mask channel is selected, then only those items\n"
                "   					where the mask channel is not a dummy are collected.\n"
                "   				\n\n"
               ).staticmethod("get_chan_data_vv");
    pyClass.def("gradient", &GXDU_wrap_gradient,
                "gradient((GXDB)arg1, (GXDB)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7, (int)arg8, (int)arg9, (float)arg10, (float)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method takes 4 channels from input database and\n"
                "   					duplicats each line twice to output database)\n"
                "   					(input and Output can be the same channel).\n"
                "   				\n\n"

                ":param arg1: Database InPut\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: DAtabase Output\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg3: X Input Channel  [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Input Channel  [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Z Input Channel  [DB_LOCK_READONLY]\n"
                ":type arg5: int\n"
                ":param arg6: G Input Channel  [DB_LOCK_READONLY]\n"
                ":type arg6: int\n"
                ":param arg7: X Output Channel [DB_LOCK_READWRITE]\n"
                ":type arg7: int\n"
                ":param arg8: Y Output Channel [DB_LOCK_READWRITE]\n"
                ":type arg8: int\n"
                ":param arg9: Z Output Channel [DB_LOCK_READWRITE]\n"
                ":type arg9: int\n"
                ":param arg10: Angle\n"
                ":type arg10: float\n"
                ":param arg11: Width\n"
                ":type arg11: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("gradient");
    pyClass.def("grav_drift", &GXDU_wrap_grav_drift,
                "grav_drift((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate base loop closure and correct for drift.\n\n"

                ":param arg1: database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: line                    [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: date                    [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: local time (on date)    [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: reading                 [DB_LOCK_READONLY]\n"
                ":type arg5: int\n"
                ":param arg6: base                    [DB_LOCK_READWRITE]\n"
                ":type arg6: int\n"
                ":param arg7: closure error           [DB_LOCK_READWRITE]\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("grav_drift");
    pyClass.def("grav_tide", &GXDU_wrap_grav_tide,
                "grav_tide((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (float)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate earth tide gravity correction.\n\n"

                ":param arg1: database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: line\n"
                ":type arg2: int\n"
                ":param arg3: lat  [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: long [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: date [DB_LOCK_READONLY]\n"
                ":type arg5: int\n"
                ":param arg6: local time (on date) [DB_LOCK_READONLY]\n"
                ":type arg6: int\n"
                ":param arg7: GMT difference (added to time to give GMT)\n"
                ":type arg7: float\n"
                ":param arg8: calculated tide [DB_LOCK_READWRITE]\n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("grav_tide");
    pyClass.def("grid_load", &GXDU_wrap_grid_load,
                "grid_load((GXDB)arg1, (GXIMG)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load grid data to a database.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: grid img\n"
                ":type arg2: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg3: X decimation factor\n"
                ":type arg3: int\n"
                ":param arg4: Y decimation factor\n"
                ":type arg4: int\n"
                ":param arg5: 0 trim leading/trailing dummies (default), 1 trim all dummies, 2 leave all dummies\n"
                ":type arg5: int\n"
                ":param arg6: flag for creating index channel: 0 no (default), 1 yes.\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("grid_load");
    pyClass.def("grid_load_xyz", &GXDU_wrap_grid_load_xyz,
                "grid_load_xyz((GXDB)arg1, (GXIMG)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7, (int)arg8, (int)arg9, (int)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load grid data to a database using specified channels\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: grid img\n"
                ":type arg2: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg3: X Channel\n"
                ":type arg3: int\n"
                ":param arg4: Y Channel\n"
                ":type arg4: int\n"
                ":param arg5: Z Channel\n"
                ":type arg5: int\n"
                ":param arg6: Data Channel\n"
                ":type arg6: int\n"
                ":param arg7: X decimation factor\n"
                ":type arg7: int\n"
                ":param arg8: Y decimation factor\n"
                ":type arg8: int\n"
                ":param arg9: 0 trim leading/trailing dummies (default), 1 trim all dummies, 2 leave all dummies\n"
                ":type arg9: int\n"
                ":param arg10: flag for creating index channel: 0 no (default), 1 yes.\n"
                ":type arg10: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("grid_load_xyz");
    pyClass.def("head", &GXDU_wrap_head,
                "head((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (GXTB)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Applies a heading correction.\n\n"

                ":param arg1: database object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: line Symbol\n"
                ":type arg2: int\n"
                ":param arg3: channel to correct [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: corrected channel  [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: heading table\n"
                ":type arg5: :class:`geosoft.gxapi.GXTB`\n"
                ":param arg6: line direction\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Updates channel with Direction in degrees azimuth (counter-clockwise\n"
                "   					relative the +Y direction).\n"
                "   					GS_R8DM if the line has no data, or if there is a\n"
                "   					problem.\n"
                "   				\n\n"
               ).staticmethod("head");
    pyClass.def("import_bin3", &GXDU_wrap_import_bin3,
                "import_bin3((GXDB)arg1, (str)arg2, (str)arg3, (str_ref)arg4, (int)arg5, (float)arg6, (GXWA)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXDU.import_bin2`\\ , but returns the name of the imported line.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: import data file name\n"
                ":type arg2: str\n"
                ":param arg3: import template name\n"
                ":type arg3: str\n"
                ":param arg4: Optional Line name (on return, the actual line)\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: Optional Flight number\n"
                ":type arg5: int\n"
                ":param arg6: Optional date\n"
                ":type arg6: float\n"
                ":param arg7: WA\n"
                ":type arg7: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					See \\ :func:`geosoft.gxapi.GXDU.import_bin2`\\ . Because the name of the created line is\n"
                "   					not necessarily the value passed in (and the value passed in\n"
                "   					can be blank), this version returns the name of the line\n"
                "   					to which the data is actually imported.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDU.import_bin2`\\ \n\n"
               ).staticmethod("import_bin3");
    pyClass.def("imp_cb_ply", &GXDU_wrap_imp_cb_ply,
                "imp_cb_ply((GXDB)arg1, (GXPJ)arg2, (str)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import concession boundary polygon file into a database\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Projection Files Object\n"
                ":type arg2: :class:`geosoft.gxapi.GXPJ`\n"
                ":param arg3: import data file name\n"
                ":type arg3: str\n"
                ":param arg4: X channel handle\n"
                ":type arg4: int\n"
                ":param arg5: Y channel handle\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The polygon file is provided by Ana Christina in Brasil.\n\n"
               ).staticmethod("imp_cb_ply");
    pyClass.def("import_ado", &GXDU_wrap_import_ado,
                "import_ado((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import an external database table into a group using ADO.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: import database connection string       (overrides template value)\n"
                ":type arg2: str\n"
                ":param arg3: imported table in database file (overrides template value)\n"
                ":type arg3: str\n"
                ":param arg4: import template name\n"
                ":type arg4: str\n"
                ":param arg5: Oasis montaj line name to create (overrides template value)\n"
                ":type arg5: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1. The import template can be in the local directory or the GEOSOFT\n"
                "   					directory.\n"
                "   \n"
                "   					2. Only the import template must be specified. The database connection string,\n"
                "   					the database table and Oasis line name are normally taken from the template\n"
                "   					file itself, but if these values are provided, they will override those found in the template.\n"
                "   \n"
                "   					3. If the line already exists, the data will overwrite the existing data.\n"
                "   				\n\n"
               ).staticmethod("import_ado");
    pyClass.def("import_all_ado", &GXDU_wrap_import_all_ado,
                "import_all_ado((GXDB)arg1, (str)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import an entire external database using ADO.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: import database connection string\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`DU_STORAGE`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1. For group storage, the table names are imported \"as is\". For line storage,\n"
                "   					if the table names are valid Geosoft line names, they are used as is.\n"
                "   					Otherwise, line names will be created with type LINE_NORMAL, starting at\n"
                "   					L0 and incrementing by 10 (L10, L20 etc.)\n"
                "   \n"
                "   					2. If the line exists, the data will overwrite the existing data.\n"
                "   \n"
                "   					3. All tables and fields will be imported.\n"
                "   \n"
                "   					4. If connection string is of type \"FILENAME=...\" the connection will attempt to resolve\n"
                "   					it as a file database. (see also ODBCFileConnect_GUI)\n"
                "   				\n\n"
               ).staticmethod("import_all_ado");
    pyClass.def("import_all_dao", &GXDU_wrap_import_all_dao,
                "import_all_dao((GXDB)arg1, (str)arg2, (str)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import an entire external database using DAO.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: import data file name\n"
                ":type arg2: str\n"
                ":param arg3: database type\n"
                ":type arg3: str\n"
                ":param arg4: \\ :ref:`DU_STORAGE`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1. The file is assumed to be a DAO compliant database.\n"
                "   \n"
                "   					2. The import data file must include the path if it is not\n"
                "   					in the local directory.\n"
                "   \n"
                "   					3. For group storage, the table names are imported \"as is\". For line storage,\n"
                "   					if the table names are valid Geosoft line names, they are used as is.\n"
                "   					Otherwise, line names will be created with type LINE_NORMAL, starting at\n"
                "   					L0 and incrementing by 10 (L10, L20 etc.)\n"
                "   \n"
                "   					4. If the line exists, the data will overwrite the existing data.\n"
                "   \n"
                "   					5. All tables and fields will be imported.\n"
                "   \n"
                "   					6. The following are valid type strings for DAO:\n"
                "   \n"
                "   					MSJET       : Microsoft Access\n"
                "   					ODBC        : ODBC source\n"
                "   					dBASE III\n"
                "   					dBASE IV\n"
                "   					dBASE 5\n"
                "   					FoxPro 2.0\n"
                "   					FoxPro 2.5\n"
                "   					FoxPro 2.6\n"
                "   					Paradox 3.x\n"
                "   					Paradox 4.x\n"
                "   					Paradox 5.x\n"
                "   				\n\n"
               ).staticmethod("import_all_dao");
    pyClass.def("import_amira", &GXDU_wrap_import_amira,
                "import_amira((GXDB)arg1, (GXRA)arg2, (GXWA)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import an AMIRA data file.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: AMIRA data file handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXRA`\n"
                ":param arg3: Log file handle\n"
                ":type arg3: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					All the constant declarations are stored within the database\n"
                "   					under \\TEM\\CONSTANTS. The format is as follows:\n"
                "   \n"
                "   					1. Lines stored in the file beginning with \"/\" are comments\n"
                "   					2. Each constant occupies a line in the file. It uses the format:\n"
                "   					CONSTANT=VALUE\n"
                "   				\n\n"
               ).staticmethod("import_amira");
    pyClass.def("import_aseg", &GXDU_wrap_import_aseg,
                "import_aseg((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import an ASEG-GDF data file.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: template file name\n"
                ":type arg2: str\n"
                ":param arg3: header file name\n"
                ":type arg3: str\n"
                ":param arg4: data file name\n"
                ":type arg4: str\n"
                ":param arg5: Flight Line Channel name\n"
                ":type arg5: str\n"
                ":param arg6: Number of channels to import at one time\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("import_aseg");
    pyClass.def("import_aseg_proj", &GXDU_wrap_import_aseg_proj,
                "import_aseg_proj((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (int)arg6, (str)arg7, (str)arg8, (str)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import an ASEG-GDF data file (supports projections).\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: template file name\n"
                ":type arg2: str\n"
                ":param arg3: header file name\n"
                ":type arg3: str\n"
                ":param arg4: data file name\n"
                ":type arg4: str\n"
                ":param arg5: Flight Line Channel name\n"
                ":type arg5: str\n"
                ":param arg6: Number of channels to import at one time\n"
                ":type arg6: int\n"
                ":param arg7: projection file name\n"
                ":type arg7: str\n"
                ":param arg8: Channel pair to associate projection\n"
                ":type arg8: str\n"
                ":param arg9: Channel pair to associate projection\n"
                ":type arg9: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This version supports projections\n\n"
               ).staticmethod("import_aseg_proj");
    pyClass.def("import_bin", &GXDU_wrap_import_bin,
                "import_bin((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (int)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import blocked binary or archive ASCII data\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: import data file name\n"
                ":type arg2: str\n"
                ":param arg3: import template name\n"
                ":type arg3: str\n"
                ":param arg4: Optional Line name (see note 3.)\n"
                ":type arg4: str\n"
                ":param arg5: Optional Flight number\n"
                ":type arg5: int\n"
                ":param arg6: Optional date\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1. Binary import templates have extension .I2 by convention.  See\n"
                "   					BINARY.I2 for a description of the template format.\n"
                "   					Archive import templates have extension .I3 by convention. See\n"
                "   					ARCHIVE.I3 for a description of the template format.\n"
                "   \n"
                "   					2. Both the import template and data file must exist.\n"
                "   \n"
                "   					3. If a line already exists in the database, a new version is created\n"
                "   					unless a line name is passed in.  In this case, the specified name\n"
                "   					is used and the imported channels on the previous line will be\n"
                "   					destroyed.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDU.lab_template`\\ \n\n"
               ).staticmethod("import_bin");
    pyClass.def("import_bin2", &GXDU_wrap_import_bin2,
                "import_bin2((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (int)arg5, (float)arg6, (GXWA)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import blocked binary or archive ASCII data with data error display\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: import data file name\n"
                ":type arg2: str\n"
                ":param arg3: import template name\n"
                ":type arg3: str\n"
                ":param arg4: Optional Line name (see note 3.)\n"
                ":type arg4: str\n"
                ":param arg5: Optional Flight number\n"
                ":type arg5: int\n"
                ":param arg6: Optional date\n"
                ":type arg6: float\n"
                ":param arg7: WA\n"
                ":type arg7: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1. Binary import templates have extension .I2 by convention.  See\n"
                "   					BINARY.I2 for a description of the template format.\n"
                "   					Archive import templates have extension .I3 by convention. See\n"
                "   					ARCHIVE.I3 for a description of the template format.\n"
                "   \n"
                "   					2. Both the import template and data file must exist.\n"
                "   \n"
                "   					3. If a line already exists in the database, a new version is created\n"
                "   					unless a line name is passed in.  In this case, the specified name\n"
                "   					is used and the imported channels on the previous line will be\n"
                "   					destroyed.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDU.lab_template`\\ \n\n"
               ).staticmethod("import_bin2");
    pyClass.def("import_bin4", &GXDU_wrap_import_bin4,
                "import_bin4((GXDB)arg1, (int)arg2, (str)arg3, (str)arg4, (str)arg5, (int)arg6, (float)arg7, (GXWA)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXDU.import_bin2`\\  but with an import mode\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: \\ :ref:`DU_IMPORT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: import data file name\n"
                ":type arg3: str\n"
                ":param arg4: import template name\n"
                ":type arg4: str\n"
                ":param arg5: Optional Line name (see note 3.)\n"
                ":type arg5: str\n"
                ":param arg6: Optional Flight number\n"
                ":type arg6: int\n"
                ":param arg7: Optional date\n"
                ":type arg7: float\n"
                ":param arg8: WA\n"
                ":type arg8: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Same as \\ :func:`geosoft.gxapi.GXDU.import_bin2`\\  but with an import mode\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDU.import_bin2`\\ \n\n"
               ).staticmethod("import_bin4");
    pyClass.def("import_daarc500_serial", &GXDU_wrap_import_daarc500_serial,
                "import_daarc500_serial((GXDB)arg1, (int)arg2, (str)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import Serial data from the RMS Instruments DAARC500.\n\n"

                ":param arg1: Database object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Output line (DB_LOCK_READWRITE)\n"
                ":type arg2: int\n"
                ":param arg3: Name of file to import\n"
                ":type arg3: str\n"
                ":param arg4: Channel to import, 1-8\n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`GU_DAARC500_DATATYPE`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Imports data stored in a serial channel recorded\n"
                "   					by the RMS Instruments DAARC500 instrument, and outputs the data to\n"
                "   					a line in the database. The channels created depend on the input data type\n"
                "   				\n\n"
               ).staticmethod("import_daarc500_serial");
    pyClass.def("import_daarc500_serial_gps", &GXDU_wrap_import_daarc500_serial_gps,
                "import_daarc500_serial_gps((GXDB)arg1, (int)arg2, (str)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import Serial GPS data from the RMS Instruments DAARC500.\n\n"

                ":param arg1: Database object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Output line (DB_LOCK_READWRITE)\n"
                ":type arg2: int\n"
                ":param arg3: Name of file to import\n"
                ":type arg3: str\n"
                ":param arg4: Channel to import, 1-8\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Imports GPS data stored in a serial channel recorded\n"
                "   					by the RMS Instruments DAARC500 instrument, and outputs the data to\n"
                "   					a line in the database. Makes the following channels:\n"
                "   \n"
                "   					Fid, UTC_Time, Latitude, Longitude, Altitude, GPS_Quality,\n"
                "   					NumSat (Number of satellites), GPS_HDOP (Horizontal Dilution of Position),\n"
                "   					Undulation, GPS_DiffAge (Age of differential channel).\n"
                "   				\n\n"
               ).staticmethod("import_daarc500_serial_gps");
    pyClass.def("import_dao", &GXDU_wrap_import_dao,
                "import_dao((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import an external database table into a group using DAO.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: import database file name   (overrides template value)\n"
                ":type arg2: str\n"
                ":param arg3: import data file type       (overrides template value)\n"
                ":type arg3: str\n"
                ":param arg4: imported table in database file (overrides template value)\n"
                ":type arg4: str\n"
                ":param arg5: import template name\n"
                ":type arg5: str\n"
                ":param arg6: Oasis Montaj line name to create (overrides template value)\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1. The import template can be in the local directory or the GEOSOFT\n"
                "   					directory.  The import data file must include the path if it is not\n"
                "   					in the local directory.\n"
                "   \n"
                "   					2. Only the import template must be specified. The database file name,\n"
                "   					file type, the database table and Oasis line name are normally\n"
                "   					taken from the template file itself, but if these values are provided,\n"
                "   					they will override those found in the template.\n"
                "   \n"
                "   					3. If the line already exists, the data will overwrite the existing data.\n"
                "   				\n\n"
               ).staticmethod("import_dao");
    pyClass.def("import_esri", &GXDU_wrap_import_esri,
                "import_esri((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import an ArcGIS Geodatabase table or feature class into a GDB group\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: import database connection string (e.g. \"d:\\\\Personal\\\\test.mdb\\ `|`\\ Table\" or \"d:\\\\File\\\\test.gdb\\ `|`\\ FeatureClass, overrides template value)\n"
                ":type arg2: str\n"
                ":param arg3: import template name\n"
                ":type arg3: str\n"
                ":param arg4: Oasis montaj line name to create (overrides template value)\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1. The import template can be in the local directory or the GEOSOFT\n"
                "   					directory.\n"
                "   \n"
                "   					2. Only the import template must be specified. The Geodatabase connection string\n"
                "   					and Oasis line name are normally taken from the template file itself,\n"
                "   					but if these values are provided, they will override those found in the template.\n"
                "   \n"
                "   					3. If the line already exists, the data will overwrite the existing data.\n"
                "   				\n\n"
               ).staticmethod("import_esri");
    pyClass.def("import_gbn", &GXDU_wrap_import_gbn,
                "import_gbn((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import GBN data file.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: File name of the GBN file to import\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("import_gbn");
    pyClass.def("import_oddf", &GXDU_wrap_import_oddf,
                "import_oddf((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import ODDF data file.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: File name of the ODDF file to import\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("import_oddf");
    pyClass.def("import_pico", &GXDU_wrap_import_pico,
                "import_pico((GXDB)arg1, (str)arg2, (str)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import a Picodas data file.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: template file name\n"
                ":type arg2: str\n"
                ":param arg3: data file name\n"
                ":type arg3: str\n"
                ":param arg4: Number of channels to import at one time\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("import_pico");
    pyClass.def("import_ubc_mod_msh", &GXDU_wrap_import_ubc_mod_msh,
                "import_ubc_mod_msh((GXDB)arg1, (str)arg2, (str)arg3, (int)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import UBC Mod and Msh files.\n\n"

                ":param arg1: Database Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Mesh file\n"
                ":type arg2: str\n"
                ":param arg3: 1-5 Mod files, delimited with \"\\ `|`\\ \"\n"
                ":type arg3: str\n"
                ":param arg4: Import slice direction (0-2 for X,Y and Z)\n"
                ":type arg4: int\n"
                ":param arg5: Value to interpret as dummy\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Each slice in X,Y or Z is imported to its own line in the database\n"
                "   					beginning with L0.\n"
                "   				\n\n"
               ).staticmethod("import_ubc_mod_msh");
    pyClass.def("import_usgs_post", &GXDU_wrap_import_usgs_post,
                "import_usgs_post((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import USGS Post data file.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: File name of the USGS post file to import\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("import_usgs_post");
    pyClass.def("import_xyz", &GXDU_wrap_import_xyz,
                "import_xyz((GXDB)arg1, (int)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import XYZ data into the database.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: \\ :ref:`DU_IMPORT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: import data file name\n"
                ":type arg3: str\n"
                ":param arg4: import template name\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1. The import template can be in the local directory or the GEOSOFT\n"
                "   					directory.  The import data file must include the path if it is not\n"
                "   					in the local directory.\n"
                "   \n"
                "   					2. Both the import template and data file must exist.\n"
                "   				\n\n"
               ).staticmethod("import_xyz");
    pyClass.def("import_xyz2", &GXDU_wrap_import_xyz2,
                "import_xyz2((GXDB)arg1, (int)arg2, (str)arg3, (str)arg4, (GXWA)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import XYZ data into the database.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: \\ :ref:`DU_IMPORT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: import data file name\n"
                ":type arg3: str\n"
                ":param arg4: import template name\n"
                ":type arg4: str\n"
                ":param arg5: WA\n"
                ":type arg5: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1. The import template can be in the local directory or the GEOSOFT\n"
                "   					directory.  The import data file must include the path if it is not\n"
                "   					in the local directory.\n"
                "   \n"
                "   					2. Both the import template and data file must exist.\n"
                "   				\n\n"
               ).staticmethod("import_xyz2");
    pyClass.def("import_io_gas", &GXDU_wrap_import_io_gas,
                "import_io_gas((GXDB)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import data columns from an ioGAS data file.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Input data.csv file name\n"
                ":type arg2: str\n"
                ":param arg3: Input template file name\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1. All columns in the speficied ioGAS data file will be imported.\n"
                "   					2. If a line already exists, the data will overwrite the existing data.\n"
                "   				\n\n"
               ).staticmethod("import_io_gas");
    pyClass.def("index_order", &GXDU_wrap_index_order,
                "index_order((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Change the order of a channel using an index channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line symbol\n"
                ":type arg2: int\n"
                ":param arg3: ordered index channel (should be int) [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: channel to reorder [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("index_order");
    pyClass.def("interp", &GXDU_wrap_interp,
                "interp((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replace all dummies by interpolating from valid data.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line handle\n"
                ":type arg2: int\n"
                ":param arg3: Channel to interpolate [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Output interpolated channel [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`DU_INTERP`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`DU_INTERP_EDGE`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("interp");
    pyClass.def("interp_gap", &GXDU_wrap_interp_gap,
                "interp_gap((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replace all dummies by interpolating from valid data.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line handle\n"
                ":type arg2: int\n"
                ":param arg3: Channel to interpolate [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Output interpolated channel [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`DU_INTERP`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`DU_INTERP_EDGE`\\ \n"
                ":type arg6: int\n"
                ":param arg7: Maximum gap to interpolate (fiducials)\n"
                ":type arg7: int\n"
                ":param arg8: Maximum items to extend at ends.\n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("interp_gap");
    pyClass.def("intersect", &GXDU_wrap_intersect,
                "intersect((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (float)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create Tie Line & Normal Line intersect table.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: X Channel [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Y Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Z Channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Intersection tolerance\n"
                ":type arg5: float\n"
                ":param arg6: Output Table file Name\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("intersect");
    pyClass.def("intersect_all", &GXDU_wrap_intersect_all,
                "intersect_all((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (float)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create line intersect table from all lines.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: X Channel [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Y Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Z Channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Intersection tolerance\n"
                ":type arg5: float\n"
                ":param arg6: Output Table file Name\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("intersect_all");
    pyClass.def("intersect_gd_bto_tbl", &GXDU_wrap_intersect_gd_bto_tbl,
                "intersect_gd_bto_tbl((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new intersection table from an intersection database.\n\n"

                ":param arg1: Input Intersection Database name\n"
                ":type arg1: str\n"
                ":param arg2: Output intersection TBL\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the TBL exists, it is overwritten.\n\n"
               ).staticmethod("intersect_gd_bto_tbl");
    pyClass.def("intersect_old", &GXDU_wrap_intersect_old,
                "intersect_old((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (str)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Use existing intersection table and re-calculate miss-ties.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: X Channel [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Y Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Z Channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Input Table file name\n"
                ":type arg5: str\n"
                ":param arg6: Output Table file Name\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Reads intersection information from an existing intersect\n"
                "   					table and looks up the values at the intersections for the\n"
                "   					input Z channel. This makes it unnecessary to re-calculate\n"
                "   					the intersections every time if you want to determine\n"
                "   					miss-ties using different Z channels, or the same Z channel\n"
                "   					after processing levelling corrections. Existing intersections\n"
                "   					whose locations do not exist in the database are ignored.\n"
                "   				\n\n"
               ).staticmethod("intersect_old");
    pyClass.def("intersect_tb_lto_gdb", &GXDU_wrap_intersect_tb_lto_gdb,
                "intersect_tb_lto_gdb((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new intersection database from an intersection table.\n\n"

                ":param arg1: Input intersection TBL\n"
                ":type arg1: str\n"
                ":param arg2: Output Intersection Database name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the GDB exists, it is deleted, so it should not\n"
                "   					be loaded.\n"
                "   					The database is split by Tie lines (or whatever lines are found in column 3\n"
                "   					of the TBL file.\n"
                "   				\n\n"
               ).staticmethod("intersect_tb_lto_gdb");
    pyClass.def("lab_template", &GXDU_wrap_lab_template,
                "lab_template((str)arg1, (str)arg2, (int)arg3, (str)arg4, (int)arg5, (int)arg6, (int)arg7, (int)arg8, (int)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Makes a default template from a lab assay file.\n\n"

                ":param arg1: data file name\n"
                ":type arg1: str\n"
                ":param arg2: new template name\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`DU_LAB_TYPE`\\ \n"
                ":type arg3: int\n"
                ":param arg4: delimiter string\n"
                ":type arg4: str\n"
                ":param arg5: Offset to column labels line (0 for first line)\n"
                ":type arg5: int\n"
                ":param arg6: Offset to unit labels line, -1 if none\n"
                ":type arg6: int\n"
                ":param arg7: Offset to first line that contains data\n"
                ":type arg7: int\n"
                ":param arg8: Sample channel element type, recommend -10 for 10-character ASCII, or GS_LONG for numbers.\n"
                ":type arg8: int\n"
                ":param arg9: Default channel element type, recommend GS_FLOAT\n"
                ":type arg9: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The template can be used to import the file using\n"
                "   					sImportBIN_DU.\n"
                "   \n"
                "   					The first column is assumed to be the sample number.\n"
                "   \n"
                "   					If the unit label line is the same as the column label\n"
                "   					line, column labels are assummed to be followed by\n"
                "   					unit labels using the format \"Au-ppm\", \"Au ppm\" or\n"
                "   					\"Au(ppm)\".\n"
                "   \n"
                "   					The number of channels is determined from the number of\n"
                "   					columns in the data channel.  If there are more column\n"
                "   					labels or unit labels, the last labels are assumed to\n"
                "   					be correct.  If there are fewer line labels, default\n"
                "   					labels \"Col_n\", where n is the column number, will be\n"
                "   					created and no unit labels will be defined.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDU.import_bin`\\ \n\n"
               ).staticmethod("lab_template");
    pyClass.def("load_gravity", &GXDU_wrap_load_gravity,
                "load_gravity((GXDB)arg1, (GXREG)arg2, (int)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a gravity survey file\n\n"

                ":param arg1: database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: REG to hold constant data\n"
                ":type arg2: :class:`geosoft.gxapi.GXREG`\n"
                ":param arg3: line in which to load data\n"
                ":type arg3: int\n"
                ":param arg4: gravity data file\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					See GRAVITY.DAT for a description of the file format.\n"
                "   \n"
                "   					Existing data in the line will be replaced.\n"
                "   \n"
                "   					The following REG parameters will be set if they appear\n"
                "   					in the data file:\n"
                "   					default\n"
                "   					OPERATOR             \"\"\n"
                "   					DATE                 none\n"
                "   					INSTRUMENT           \"\"\n"
                "   					INSTRUMENT_SCALE     \"1.0\"\n"
                "   					BASE_GRAVITY         \"0.0\"\n"
                "   					FORMULA              \"1967\"\n"
                "   					GMT_DIFF             \"0.0\"\n"
                "   					DISTANCE_UNITS       \"m\"\n"
                "   					DENSITY_EARTH        \"2.67\"\n"
                "   					DENSITY_WATER        \"1.0\"\n"
                "   					DENSITY_ICE          \"0.95\"\n"
                "   					MAP_PROJECTION       \"\"\n"
                "   \n"
                "   					If the corresponding constant is not specified and the\n"
                "   					REG already has the constant defined, it is not changed.\n"
                "   					If the constant is not defined and it is not already in\n"
                "   					the REG, the indicated default will be set.\n"
                "   				\n\n"
               ).staticmethod("load_gravity");
    pyClass.def("load_ltb", &GXDU_wrap_load_ltb,
                "load_ltb((GXDB)arg1, (int)arg2, (GXLTB)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load LTB into a database line.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: line\n"
                ":type arg2: int\n"
                ":param arg3: table\n"
                ":type arg3: :class:`geosoft.gxapi.GXLTB`\n"
                ":param arg4: \\ :ref:`DU_LOADLTB`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A new channel will be created for all LTB fields\n"
                "   					that do not already exist.\n"
                "   					The LTB field type will be double if all entries can be\n"
                "   					converted to double, otherwise it will be a string type\n"
                "   					set to the larger of 16 characters or the longest string\n"
                "   					in the field.\n"
                "   \n"
                "   					For _APPEND, the LTB data is simply added the end of each\n"
                "   					channel.  \\ :func:`geosoft.gxapi.GXDU.re_fid_all_ch`\\  can be used to re-fid data to\n"
                "   					match a specifc channel and there-by case all channels to be\n"
                "   					the same length before appending data.\n"
                "   				\n\n"
               ).staticmethod("load_ltb");
    pyClass.def("make_fid", &GXDU_wrap_make_fid,
                "make_fid((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Make a fiducial channel based on an existing channel.\n\n"

                ":param arg1: database object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: line Symbol\n"
                ":type arg2: int\n"
                ":param arg3: base channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: new fiducial channel [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("make_fid");
    pyClass.def("mask", &GXDU_wrap_mask,
                "mask((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Mask dummies in one channel against another.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line handle\n"
                ":type arg2: int\n"
                ":param arg3: Channel to mask [DB_LOCK_READWRITE]\n"
                ":type arg3: int\n"
                ":param arg4: Mask channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("mask");
    pyClass.def("math", &GXDU_wrap_math,
                "math((GXDB)arg1, (int)arg2, (GXEXP)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply an expression to the database\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: line handle\n"
                ":type arg2: int\n"
                ":param arg3: math expression object (EXP)\n"
                ":type arg3: :class:`geosoft.gxapi.GXEXP`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The MATH_DU method will READWRITE lock channels on the left\n"
                "   					side of expressions and READONLY lock channels on the right\n"
                "   					side of expressions.  Channels are unlocked before returning.\n"
                "   					Therefore, channels on the left side of an expression cannot\n"
                "   					be locked READONLY because the \\ :func:`geosoft.gxapi.GXDU.math`\\  attempt to lock the\n"
                "   					channel READWRITE will fail.  Similarly, channels on the right\n"
                "   					side of an expression cannot be locked READWRITE because\n"
                "   					\\ :func:`geosoft.gxapi.GXDU.math`\\ 's attempt to lock the channels READONLY will fail.\n"
                "   \n"
                "   					If this is confusing, just make sure no channels used in the\n"
                "   					expression are locked before calling \\ :func:`geosoft.gxapi.GXDU.math`\\ .\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXEXP`\\ .GXH\n\n"
               ).staticmethod("math");
    pyClass.def("merge_line", &GXDU_wrap_merge_line,
                "merge_line((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Merge a line a the fiducial and copies any data past\n"
                "   					that fiducial into the new line.\n"
                "   				\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Input Line1 [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Input Line2 [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Output Line [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`DU_MERGE`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("merge_line");
    pyClass.def("mod_fid_range", &GXDU_wrap_mod_fid_range,
                "mod_fid_range((GXDB)arg1, (int)arg2, (float)arg3, (float)arg4, (int)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Insert/Append/Delete a range of fids.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: line\n"
                ":type arg2: int\n"
                ":param arg3: base fid start\n"
                ":type arg3: float\n"
                ":param arg4: base fid increment\n"
                ":type arg4: float\n"
                ":param arg5: start index (can be negative)\n"
                ":type arg5: int\n"
                ":param arg6: number of fids\n"
                ":type arg6: int\n"
                ":param arg7: \\ :ref:`DU_MODFID`\\ \n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Channels that do not have the same fid start or fid\n"
                "   					increment are not processed.\n"
                "   \n"
                "   					Protected channels are modified automatically.\n"
                "   				\n\n"
               ).staticmethod("mod_fid_range");
    pyClass.def("move", &GXDU_wrap_move,
                "move((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Move/correct a channel to a control channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle to Apply this to\n"
                ":type arg2: int\n"
                ":param arg3: Input channel   [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Control channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Result channel  [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`DU_MOVE`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The input channel is moved to the absolute location\n"
                "   					of the control channel.\n"
                "   				\n\n"
               ).staticmethod("move");
    pyClass.def("nl_filt", &GXDU_wrap_nl_filt,
                "nl_filt((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method applies a non-linear filter to the specified\n"
                "   					line/channel and places the output in the output channel.\n"
                "   				\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line handle\n"
                ":type arg2: int\n"
                ":param arg3: Channel to filter [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Output filtered channel [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: Filter Width\n"
                ":type arg5: int\n"
                ":param arg6: Filter Tolerance, 0 for 10% of Std. Dev.\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("nl_filt");
    pyClass.def("normal", &GXDU_wrap_normal,
                "normal((GXDB)arg1, (int)arg2, (bool)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set fid of all channels to match a specified channel.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Base Channel for normalization.  [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Ignore write protection on channels? bool\n"
                ":type arg3: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDU.re_fid_all_ch`\\ \n\n"
               ).staticmethod("normal");
    pyClass.def("poly_fill", &GXDU_wrap_poly_fill,
                "poly_fill((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (GXPLY)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill using a polygon with a value of 1.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle\n"
                ":type arg2: int\n"
                ":param arg3: X Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Channel to fill [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: Polygon Object to use\n"
                ":type arg6: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg7: \\ :ref:`DU_FILL`\\ \n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("poly_fill");
    pyClass.def("poly_mask", &GXDU_wrap_poly_mask,
                "poly_mask((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (GXPLY)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Mask against a polygon.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle\n"
                ":type arg2: int\n"
                ":param arg3: X Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Channel to mask [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: Polygon Object to use\n"
                ":type arg6: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg7: \\ :ref:`DU_MASK`\\ \n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("poly_mask");
    pyClass.def("project_data", &GXDU_wrap_project_data,
                "project_data((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (GXPJ)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Project X,Y channels\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle to project\n"
                ":type arg2: int\n"
                ":param arg3: X Input Channel  [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Input Channel  [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: X Output Channel [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: Y Output Channel [DB_LOCK_READWRITE]\n"
                ":type arg6: int\n"
                ":param arg7: Projection object to Apply\n"
                ":type arg7: :class:`geosoft.gxapi.GXPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Output channels can be the same as input channels\n\n"
               ).staticmethod("project_data");
    pyClass.def("project_xyz", &GXDU_wrap_project_xyz,
                "project_xyz((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7, (int)arg8, (GXPJ)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Project X,Y,Z channels from one system to another.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle to project\n"
                ":type arg2: int\n"
                ":param arg3: X Input Channel  [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Input Channel  [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Z Input Channel  [DB_LOCK_READONLY]\n"
                ":type arg5: int\n"
                ":param arg6: X Output Channel [DB_LOCK_READWRITE]\n"
                ":type arg6: int\n"
                ":param arg7: Y Output Channel [DB_LOCK_READWRITE]\n"
                ":type arg7: int\n"
                ":param arg8: Z Output Channel [DB_LOCK_READWRITE]\n"
                ":type arg8: int\n"
                ":param arg9: Projection object to Apply\n"
                ":type arg9: :class:`geosoft.gxapi.GXPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Output channels can be the same as input channels\n\n"
               ).staticmethod("project_xyz");
    pyClass.def("proj_points", &GXDU_wrap_proj_points,
                "proj_points((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7, (int)arg8, (int)arg9, (int)arg10, (int)arg11, (int)arg12, (int)arg13, (int)arg14, (int)arg15, (int)arg16, (int)arg17, (int)arg18, (int)arg19, (int)arg20) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Project X,Y(Z) channels with different projections\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle to project\n"
                ":type arg2: int\n"
                ":param arg3: X Input Channel  [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Input Channel  [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Z Input Channel  [DB_LOCK_READONLY] (can be DB_NULL_SYMB)\n"
                ":type arg5: int\n"
                ":param arg6: X Output Channel [DB_LOCK_READWRITE]\n"
                ":type arg6: int\n"
                ":param arg7: Y Output Channel [DB_LOCK_READWRITE]\n"
                ":type arg7: int\n"
                ":param arg8: Z Output Channel [DB_LOCK_READWRITE] (can be DB_NULL_SYMB)\n"
                ":type arg8: int\n"
                ":param arg9: Input Name Channel   [DB_LOCK_READONLY]\n"
                ":type arg9: int\n"
                ":param arg10: Input Datum Channel  [DB_LOCK_READONLY]\n"
                ":type arg10: int\n"
                ":param arg11: Input Method Channel [DB_LOCK_READONLY]\n"
                ":type arg11: int\n"
                ":param arg12: Input Unit Channel   [DB_LOCK_READONLY]\n"
                ":type arg12: int\n"
                ":param arg13: Input Local Datum Channel [DB_LOCK_READONLY]\n"
                ":type arg13: int\n"
                ":param arg14: Output Name Channel  [DB_LOCK_READONLY]\n"
                ":type arg14: int\n"
                ":param arg15: Output Datum Channel [DB_LOCK_READONLY]\n"
                ":type arg15: int\n"
                ":param arg16: Output Method Channel [DB_LOCK_READONLY]\n"
                ":type arg16: int\n"
                ":param arg17: Output Unit Channel  [DB_LOCK_READONLY]\n"
                ":type arg17: int\n"
                ":param arg18: Output Local Datum Channel [DB_LOCK_READONLY]\n"
                ":type arg18: int\n"
                ":param arg19: Error Channel [DB_LOCK_READWRITE]\n"
                ":type arg19: int\n"
                ":param arg20: Force Local Datum Shifts?\n"
                ":type arg20: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Output channels can be the same as input channels\n\n"
               ).staticmethod("proj_points");
    pyClass.def("qc_init_separation", &GXDU_wrap_qc_init_separation,
                "qc_init_separation((GXDB)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates the nearest line channels for line separation QC.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Nominal Line separation\n"
                ":type arg2: float\n"
                ":param arg3: Nominal Line direction\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This must be called before QCSeparation_DU. It uses a pager to\n"
                "   					establish the relative positions of the selected lines, then,\n"
                "   					for every point determines the closest point in another line to\n"
                "   					the left and to the right (as determined by looking in the\n"
                "   					direction of the line.) These distances are stored to two new\n"
                "   					channels in the database, \"Closest_Left\" and \"Closest_Right\"\n"
                "   				\n\n"
               ).staticmethod("qc_init_separation");
    pyClass.def("qc_survey_plan", &GXDU_wrap_qc_survey_plan,
                "qc_survey_plan((GXDB)arg1, (GXWA)arg2, (GXPLY)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (int)arg8, (int)arg9, (float)arg10, (float)arg11, (float)arg12, (float)arg13, (int)arg14, (int)arg15, (int)arg16, (float)arg17, (float)arg18) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a database containing proposed survey plan in a PLY\n\n"

                ":param arg1: Database to save proposed survey plan\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: WA to save survey plan summary\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg3: Boundary PLY\n"
                ":type arg3: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg4: Survey line spacing\n"
                ":type arg4: float\n"
                ":param arg5: Survey line azimuth\n"
                ":type arg5: float\n"
                ":param arg6: Survey line reference X coordinate\n"
                ":type arg6: float\n"
                ":param arg7: Survey line reference Y coordinate\n"
                ":type arg7: float\n"
                ":param arg8: Survey line starting number of LINES\n"
                ":type arg8: int\n"
                ":param arg9: Line number increment for survey line\n"
                ":type arg9: int\n"
                ":param arg10: Tie line spacing\n"
                ":type arg10: float\n"
                ":param arg11: Tie line azimuth\n"
                ":type arg11: float\n"
                ":param arg12: Tie line reference X coordinate\n"
                ":type arg12: float\n"
                ":param arg13: Tie line reference Y coordinate\n"
                ":type arg13: float\n"
                ":param arg14: Tie line starting number of LINES\n"
                ":type arg14: int\n"
                ":param arg15: Line number increment for Tie line\n"
                ":type arg15: int\n"
                ":param arg16: \\ :ref:`QC_PLAN_TYPE`\\ \n"
                ":type arg16: int\n"
                ":param arg17: Sample spacing (spacing between points in lines)\n"
                ":type arg17: float\n"
                ":param arg18: Spacing to extend lines outside polygon\n"
                ":type arg18: float\n"
                ":returns: Nothing\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The LINE on which has the reference (X,Y) will have the starting Line number\n"
                "   					The lines on the right hand side of the reference line (while looking\n"
                "   					into azimuth of ref. line) have increasing line numbers. The lines\n"
                "   					on the left hand side have the decreasing line numbers from the starting\n"
                "   					number. Returns an error code or 0 (if successful)\n"
                "   				\n\n"
               ).staticmethod("qc_survey_plan");
    pyClass.def("direction", &GXDU_wrap_direction,
                "direction((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the direction of a line.\n\n"

                ":param arg1: Database Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Symbol\n"
                ":type arg2: int\n"
                ":param arg3: X reference channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y reference channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":returns: direction in degrees azimuth (clockwise relative\n"
                "          						the +Y direction).\n"
                "          						GS_R8DM if the line has no data, or if there is a\n"
                "          						problem.  Problems will register errors.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The direction is calculated from the first and last\n"
                "   					non-dummy locations in the X and Y reference channels.\n"
                "   				\n\n"
               ).staticmethod("direction");
    pyClass.def("re_fid", &GXDU_wrap_re_fid,
                "re_fid((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (float)arg7, (float)arg8, (float)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Re-fid a channel based on a reference channel\n\n"

                ":param arg1: Database Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Symbol\n"
                ":type arg2: int\n"
                ":param arg3: Original Channel [DB_LOCK_READONLY]  \"Y\" values\n"
                ":type arg3: int\n"
                ":param arg4: Reference Channel [DB_LOCK_READONLY] \"X\" locations\n"
                ":type arg4: int\n"
                ":param arg5: Output Channel [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`DU_REFID`\\ \n"
                ":type arg6: int\n"
                ":param arg7: Start Fid, if GS_R8DM, use ref channel minimum\n"
                ":type arg7: float\n"
                ":param arg8: Fid increment, if GS_R8DM use nominal spacing of the reference channel.\n"
                ":type arg8: float\n"
                ":param arg9: Maximum gap to interpolate across\n"
                ":type arg9: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The original channel can be an array channel, in which case\n"
                "   					the columns (up to the number of columns available in the output)\n"
                "   					are individually interpolated. If the number of\n"
                "   					columns in the output channel is more than the input channel,\n"
                "   					the remaining columns are dummied.\n"
                "   \n"
                "   					This function is fundamentally different in behaviour from \\ :func:`geosoft.gxapi.GXDU.re_fid_ch`\\ .\n"
                "   					The values in the Reference channel in \\ :func:`geosoft.gxapi.GXDU.re_fid`\\  are the \"X\" locations\n"
                "   					corresponding to the \"Y\" locations in the \"Original Channel\". Output\n"
                "   					Channel values are calculated at the new \"X\" locations specified by\n"
                "   					the Start Fid and the Fid Increment.\n"
                "   				\n\n"
               ).staticmethod("re_fid");
    pyClass.def("re_fid_all_ch", &GXDU_wrap_re_fid_all_ch,
                "re_fid_all_ch((GXDB)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Simple re-fid of all channels based on a reference channel\n\n"

                ":param arg1: Database Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Symbol\n"
                ":type arg2: int\n"
                ":param arg3: Reference Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Channels can be array channels, in which case\n"
                "   					the columns are individually re-fidded.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDU.normal`\\ \n\n"
               ).staticmethod("re_fid_all_ch");
    pyClass.def("re_fid_ch", &GXDU_wrap_re_fid_ch,
                "re_fid_ch((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Simple re-fid of a channel based on a reference channel\n\n"

                ":param arg1: Database Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Symbol\n"
                ":type arg2: int\n"
                ":param arg3: Reference Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Channel to refid  [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The original channel can be an array channel, in which case\n"
                "   					the columns are individually re-fidded.\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXDU.re_fid_ch`\\  resamples the \"Channel to refid\" to the \"Reference Channel\" Fid\n"
                "   					range and increment.\n"
                "   				\n\n"
               ).staticmethod("re_fid_ch");
    pyClass.def("rotate", &GXDU_wrap_rotate,
                "rotate((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (float)arg7, (float)arg8, (float)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Rotate coordinates.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line symbol\n"
                ":type arg2: int\n"
                ":param arg3: input X channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: input Y channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: output X channel [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: output Y channel [DB_LOCK_READWRITE]\n"
                ":type arg6: int\n"
                ":param arg7: X point about which to rotate\n"
                ":type arg7: float\n"
                ":param arg8: Y of point about which to rotate\n"
                ":type arg8: float\n"
                ":param arg9: angle in degrees CCW\n"
                ":type arg9: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("rotate");
    pyClass.def("sample_gd", &GXDU_wrap_sample_gd,
                "sample_gd((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (GXGD)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sample a GD at a specified X and Y.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle to sample\n"
                ":type arg2: int\n"
                ":param arg3: X Input Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Input Channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Z Output Channel sampled from GD [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: Grid handle\n"
                ":type arg6: :class:`geosoft.gxapi.GXGD`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Values in result channel\n\n"
               ).staticmethod("sample_gd");
    pyClass.def("sample_img", &GXDU_wrap_sample_img,
                "sample_img((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (GXIMG)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sample a IMG at a specified X and Y.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle to sample\n"
                ":type arg2: int\n"
                ":param arg3: X Input Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Input Channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Z Output Channel sampled from IMG [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: IMG handle\n"
                ":type arg6: :class:`geosoft.gxapi.GXIMG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Values in result channel\n\n"
               ).staticmethod("sample_img");
    pyClass.def("sample_img_line_lst", &GXDU_wrap_sample_img_line_lst,
                "sample_img_line_lst((GXDB)arg1, (GXLST)arg2, (int)arg3, (int)arg4, (int)arg5, (GXIMG)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sample an IMG at a specified X and Y, for a LST of lines.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: LST of (Line Name, Line Handle) values to sample\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: X Input Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Input Channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Z Output Channel sampled from IMG [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: IMG handle\n"
                ":type arg6: :class:`geosoft.gxapi.GXIMG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Values in result channel\n\n"
               ).staticmethod("sample_img_line_lst");
    pyClass.def("scan_ado", &GXDU_wrap_scan_ado,
                "scan_ado((str)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Scans an external ADO database and generates a default template.\n\n"

                ":param arg1: Database connection string\n"
                ":type arg1: str\n"
                ":param arg2: Database Table Name\n"
                ":type arg2: str\n"
                ":param arg3: Template file name to Create\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   All the channels are listed\n\n"
               ).staticmethod("scan_ado");
    pyClass.def("scan_aseg", &GXDU_wrap_scan_aseg,
                "scan_aseg((str)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method scans an ASEG-GDF file and generates a default\n"
                "   					template listing all the channels and all the ALIAS lines.\n"
                "   				\n\n"

                ":param arg1: header file name\n"
                ":type arg1: str\n"
                ":param arg2: data file name\n"
                ":type arg2: str\n"
                ":param arg3: Flight Line Channel name\n"
                ":type arg3: str\n"
                ":param arg4: Template file name to Create\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("scan_aseg");
    pyClass.def("scan_dao", &GXDU_wrap_scan_dao,
                "scan_dao((str)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Scans an external DAO database and generates a default template.\n\n"

                ":param arg1: Database file name\n"
                ":type arg1: str\n"
                ":param arg2: Database Type\n"
                ":type arg2: str\n"
                ":param arg3: Database Table Name\n"
                ":type arg3: str\n"
                ":param arg4: Template file name to Create\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   All the channels are listed\n\n"
               ).staticmethod("scan_dao");
    pyClass.def("scan_pico", &GXDU_wrap_scan_pico,
                "scan_pico((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method scans a picodas file and generates a default\n"
                "   					template listing all the channels and all the ALIAS lines.\n"
                "   				\n\n"

                ":param arg1: Data file Name\n"
                ":type arg1: str\n"
                ":param arg2: Template file name to Create\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("scan_pico");
    pyClass.def("sort", &GXDU_wrap_sort,
                "sort((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sort the contents of a channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line symbol\n"
                ":type arg2: int\n"
                ":param arg3: channel to sort [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`DU_SORT`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("sort");
    pyClass.def("sort_index", &GXDU_wrap_sort_index,
                "sort_index((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an ordered index of the contents of a channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line symbol\n"
                ":type arg2: int\n"
                ":param arg3: channel to sort [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: output index channel (should be int) [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`DU_SORT`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("sort_index");
    pyClass.def("sort_index2", &GXDU_wrap_sort_index2,
                "sort_index2((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an ordered index from two channels\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line symbol\n"
                ":type arg2: int\n"
                ":param arg3: Sort by this channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`DU_SORT`\\ \n"
                ":type arg4: int\n"
                ":param arg5: Then by this channel [DB_LOCK_READONLY]\n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`DU_SORT`\\ \n"
                ":type arg6: int\n"
                ":param arg7: output index channel (should be int) [DB_LOCK_READWRITE]\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("sort_index2");
    pyClass.def("split_line", &GXDU_wrap_split_line,
                "split_line((GXDB)arg1, (int)arg2, (int)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Splits a line a the fiducial and copies any data past\n"
                "   					that fiducial into the new line.\n"
                "   				\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Input Line, will be reduced at fid  [DB_LOCK_READWRITE]\n"
                ":type arg2: int\n"
                ":param arg3: Output Line, will take data above fid [DB_LOCK_READWRITE]\n"
                ":type arg3: int\n"
                ":param arg4: Fid number of split\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("split_line");
    pyClass.def("split_line2", &GXDU_wrap_split_line2,
                "split_line2((GXDB)arg1, (int)arg2, (int)arg3, (float)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Splits a line a the fiducial and copies any data past\n"
                "   					that fiducial into the new line.\n"
                "   				\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Input Line, will be reduced at fid  [DB_LOCK_READWRITE]\n"
                ":type arg2: int\n"
                ":param arg3: Output Line, will take data above fid [DB_LOCK_READWRITE]\n"
                ":type arg3: int\n"
                ":param arg4: Fid number of split\n"
                ":type arg4: float\n"
                ":param arg5: Reset starting fiducials to zero (0: No, 1: Yes)\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The same as SplitLine, but with an option to reset each line's starting fiducial to zero.\n\n"
               ).staticmethod("split_line2");
    pyClass.def("split_line_xy", &GXDU_wrap_split_line_xy,
                "split_line_xy((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (float)arg6, (float)arg7, (int)arg8, (int_ref)arg9, (int)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Break up a line based on tolerance of lateral and horizontal distance, with\n"
                "   					options for the output line names.\n"
                "   				\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line to be broken up [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Channel X [DB_LOCK_READWRITE]\n"
                ":type arg3: int\n"
                ":param arg4: Channel Y [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: Line direction, 0-any, 1-X, 2-Y.\n"
                ":type arg5: int\n"
                ":param arg6: Lateral tolerance, DUMMY for the default (10% of the separation between the first two points.\n"
                ":type arg6: float\n"
                ":param arg7: Downline Tolerance, DUMMY for none\n"
                ":type arg7: float\n"
                ":param arg8: \\ :ref:`DU_SPLITLINE`\\ \n"
                ":type arg8: int\n"
                ":param arg9: First line in the sequence, for DU_SPLITLINE_SEQUENTIAL. On return, the next line in the sequence.\n"
                ":type arg9: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg10: Increment in the line number sequence, for DU_SPLITLINE_SEQUENTIAL\n"
                ":type arg10: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The original line will be deleted.\n\n"
               ).staticmethod("split_line_xy");
    pyClass.def("split_line_xy2", &GXDU_wrap_split_line_xy2,
                "split_line_xy2((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (float)arg6, (float)arg7, (int)arg8, (int_ref)arg9, (int)arg10, (int)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Break up a line based on tolerance of lateral and horizontal distance, with\n"
                "   					options for the output line names.\n"
                "   				\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line to be broken up [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Channel X [DB_LOCK_READWRITE]\n"
                ":type arg3: int\n"
                ":param arg4: Channel Y [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: Line direction, 0-any, 1-X, 2-Y.\n"
                ":type arg5: int\n"
                ":param arg6: Lateral tolerance, DUMMY for the default (10% of the separation between the first two points.\n"
                ":type arg6: float\n"
                ":param arg7: Downline Tolerance, DUMMY for none\n"
                ":type arg7: float\n"
                ":param arg8: \\ :ref:`DU_SPLITLINE`\\ \n"
                ":type arg8: int\n"
                ":param arg9: First line in the sequence, for DU_SPLITLINE_SEQUENTIAL. On return, the next line in the sequence.\n"
                ":type arg9: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg10: Increment in the line number sequence, for DU_SPLITLINE_SEQUENTIAL\n"
                ":type arg10: int\n"
                ":param arg11: Reset starting fiducials to zero (0: No, 1: Yes)\n"
                ":type arg11: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The same as SplitLineXY, but with an option to reset each line's starting fiducial to zero.\n\n"
               ).staticmethod("split_line_xy2");
    pyClass.def("split_line_xy3", &GXDU_wrap_split_line_xy3,
                "split_line_xy3((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (float)arg6, (float)arg7, (int)arg8, (int_ref)arg9, (int)arg10, (int)arg11, (int)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Break up a line based on tolerance of lateral and horizontal distance, with\n"
                "   					options for the output line names.\n"
                "   				\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line to be broken up [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Channel X [DB_LOCK_READWRITE]\n"
                ":type arg3: int\n"
                ":param arg4: Channel Y [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: Line direction, 0-any, 1-X, 2-Y.\n"
                ":type arg5: int\n"
                ":param arg6: Lateral tolerance, DUMMY for the default (10% of the separation between the first two points.\n"
                ":type arg6: float\n"
                ":param arg7: Downline Tolerance, DUMMY for none\n"
                ":type arg7: float\n"
                ":param arg8: \\ :ref:`DU_SPLITLINE`\\ \n"
                ":type arg8: int\n"
                ":param arg9: First line in the sequence, for DU_SPLITLINE_SEQUENTIAL. On return, the next line in the sequence.\n"
                ":type arg9: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg10: Increment in the line number sequence, for DU_SPLITLINE_SEQUENTIAL\n"
                ":type arg10: int\n"
                ":param arg11: Maintain line types for DU_SPLITLINE_SEQUENTIAL  (0: No, 1: Yes)\n"
                ":type arg11: int\n"
                ":param arg12: Reset starting fiducials to zero (0: No, 1: Yes)\n"
                ":type arg12: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The same as SplitLineXY2, but with the option to maintain line types when outputting sequentially numbered lines.\n\n"
               ).staticmethod("split_line_xy3");
    pyClass.def("split_line_by_direction", &GXDU_wrap_split_line_by_direction,
                "split_line_by_direction((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (bool)arg9, (int)arg10, (int_ref)arg11, (int)arg12, (int)arg13) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The line is split when the heading (calculated from the current X and Y channels) changes by more than a specified amount over\n"
                "   					a specified distance. Additional options to discard too-short lines\n"
                "   				\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line to be broken up [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: X Channel [DB_LOCK_READWRITE].\n"
                ":type arg3: int\n"
                ":param arg4: Y Channel [DB_LOCK_READWRITE].\n"
                ":type arg4: int\n"
                ":param arg5: Maximum angular change allowed (degrees)...\n"
                ":type arg5: float\n"
                ":param arg6: ...over a distance of\n"
                ":type arg6: float\n"
                ":param arg7: Delete lines shorter than (can be rDUMMY)\n"
                ":type arg7: float\n"
                ":param arg8: Break on data XY separation greater than (can be rDUMMY)\n"
                ":type arg8: float\n"
                ":param arg9: bool``True`` to save too-short segments as special lines, ``False`` to discard\n"
                ":type arg9: bool\n"
                ":param arg10: \\ :ref:`DU_SPLITLINE`\\  ONLY DU_SPLITLINEXY_SEQUENTIAL and DU_SPLITLINEXY_VERSIONS\n"
                ":type arg10: int\n"
                ":param arg11: First line in the sequence, for DU_SPLITLINE_SEQUENTIAL. On return, the next line in the sequence.\n"
                ":type arg11: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg12: Increment in the line number sequence, for DU_SPLITLINE_SEQUENTIAL\n"
                ":type arg12: int\n"
                ":param arg13: Reset starting fiducials to zero (0: No, 1: Yes)\n"
                ":type arg13: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Split a line based on changes in heading.\n\n"
               ).staticmethod("split_line_by_direction");
    pyClass.def("split_line_by_direction2", &GXDU_wrap_split_line_by_direction2,
                "split_line_by_direction2((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (bool)arg9, (int)arg10, (int_ref)arg11, (int)arg12, (int)arg13, (int)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The same as SplitLineByDirection, but with the option to maintain line types when outputting sequentially numbered lines.\n"
                "   				\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line to be broken up [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: X Channel [DB_LOCK_READWRITE].\n"
                ":type arg3: int\n"
                ":param arg4: Y Channel [DB_LOCK_READWRITE].\n"
                ":type arg4: int\n"
                ":param arg5: Maximum angular change allowed (degrees)...\n"
                ":type arg5: float\n"
                ":param arg6: ...over a distance of\n"
                ":type arg6: float\n"
                ":param arg7: Delete lines shorter than (can be rDUMMY)\n"
                ":type arg7: float\n"
                ":param arg8: Break on data XY separation greater than (can be rDUMMY)\n"
                ":type arg8: float\n"
                ":param arg9: bool``True`` to save too-short segments as special lines, ``False`` to discard\n"
                ":type arg9: bool\n"
                ":param arg10: \\ :ref:`DU_SPLITLINE`\\  ONLY DU_SPLITLINEXY_SEQUENTIAL and DU_SPLITLINEXY_VERSIONS\n"
                ":type arg10: int\n"
                ":param arg11: First line in the sequence, for DU_SPLITLINE_SEQUENTIAL. On return, the next line in the sequence.\n"
                ":type arg11: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg12: Increment in the line number sequence, for DU_SPLITLINE_SEQUENTIAL\n"
                ":type arg12: int\n"
                ":param arg13: Maintain line types for DU_SPLITLINE_SEQUENTIAL  (0: No, 1: Yes)\n"
                ":type arg13: int\n"
                ":param arg14: Reset starting fiducials to zero (0: No, 1: Yes)\n"
                ":type arg14: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Split a line based on changes in heading.\n\n"
               ).staticmethod("split_line_by_direction2");
    pyClass.def("stat", &GXDU_wrap_stat,
                "stat((GXDB)arg1, (int)arg2, (int)arg3, (GXST)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a data channel to a statistics object.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line handle\n"
                ":type arg2: int\n"
                ":param arg3: Channel handle [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Statistics handle\n"
                ":type arg4: :class:`geosoft.gxapi.GXST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the input channel is a VA (array) channel, then the columns set using\n"
                "   					\\ :func:`geosoft.gxapi.GXDB.set_va_windows`\\ () are used in the statistics; all columns are used by default.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXST`\\ \n\n"
               ).staticmethod("stat");
    pyClass.def("table_line_fid", &GXDU_wrap_table_line_fid,
                "table_line_fid((GXDB)arg1, (int)arg2, (int)arg3, (GXTB)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Place a Line/Fid information into a Channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Output channel [DB_LOCK_READWRITE]\n"
                ":type arg2: int\n"
                ":param arg3: Reference channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Table to Use\n"
                ":type arg4: :class:`geosoft.gxapi.GXTB`\n"
                ":param arg5: Table field wanted\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("table_line_fid");
    pyClass.def("table_selected_lines_fid", &GXDU_wrap_table_selected_lines_fid,
                "table_selected_lines_fid((GXDB)arg1, (int)arg2, (int)arg3, (GXTB)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Place a Line/Fid information into a Channel for the selected lines in the database.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Output channel [DB_LOCK_READWRITE]\n"
                ":type arg2: int\n"
                ":param arg3: Reference channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Table to Use\n"
                ":type arg4: :class:`geosoft.gxapi.GXTB`\n"
                ":param arg5: Table field wanted\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.1.0\n\n"
               ).staticmethod("table_selected_lines_fid");
    pyClass.def("time_constant", &GXDU_wrap_time_constant,
                "time_constant((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate TEM time constant (Tau)\n\n"

                ":param arg1: Database, required\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle, required\n"
                ":type arg2: int\n"
                ":param arg3: Response channel, required [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Time channel, required [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Output Time constant (Tau) channel, required [DB_LOCK_READWRITE]\n"
                ":type arg5: int\n"
                ":param arg6: Output Intercept channel, no output if NULLSYMB [DB_LOCK_READWRITE]\n"
                ":type arg6: int\n"
                ":param arg7: Output predicted response channel, no output if NULLSYMB [DB_LOCK_READWRITE] Result is based on least square fit from Tau and Intercept\n"
                ":type arg7: int\n"
                ":param arg8: Log option applied to time channel: 0 - linear, 1 - log10\n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					When DU_TIME_LOG option is used, Time channel will be converted\n"
                "   					with logarithmic before calculating time constant.\n"
                "   					Logarthmic conversion is always applied to the response channel.\n"
                "   				\n\n"
               ).staticmethod("time_constant");
    pyClass.def("trend", &GXDU_wrap_trend,
                "trend((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculates an n'th order trend of a data channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle to Apply this to\n"
                ":type arg2: int\n"
                ":param arg3: Input channel  [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Result channel [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: Trend Order, 0 to 9\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDU.b_spline`\\ \n\n"
               ).staticmethod("trend");
    pyClass.def("update_intersect_db", &GXDU_wrap_update_intersect_db,
                "update_intersect_db((GXDB)arg1, (int)arg2, (int)arg3, (GXDB)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Update the Z and DZ values in an intersection database, using the current database.\n\n"

                ":param arg1: Flight Database Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: X Channel [DB_LOCK_READONLY] (for location info)\n"
                ":type arg2: int\n"
                ":param arg3: Z Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Intersection database to update\n"
                ":type arg4: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Updates the TZ, TDZ, LZ and LDZ channels at the intersections,\n"
                "   					using the current flight database.\n"
                "   				\n\n"
               ).staticmethod("update_intersect_db");
    pyClass.def("voxel_section", &GXDU_wrap_voxel_section,
                "voxel_section((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (GXVOX)arg5, (str)arg6, (float)arg7, (float)arg8, (int)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Slice a voxel to a grid under a database line.\n\n"

                ":param arg1: Database Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Input  Line Symbol [READWRITE]\n"
                ":type arg2: int\n"
                ":param arg3: X Channel (DB_NO_SYMB if LineDir==0)\n"
                ":type arg3: int\n"
                ":param arg4: Y Channel (DB_NO_SYMB if LineDir==0)\n"
                ":type arg4: int\n"
                ":param arg5: Voxel to slice\n"
                ":type arg5: :class:`geosoft.gxapi.GXVOX`\n"
                ":param arg6: Output grid name\n"
                ":type arg6: str\n"
                ":param arg7: X cell size (horizontal)\n"
                ":type arg7: float\n"
                ":param arg8: Y cell size (vertical)\n"
                ":type arg8: float\n"
                ":param arg9: Interp: 1 - linear, 0 - nearest\n"
                ":type arg9: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Takes the first and XY locations in a line (using the\n"
                "   					current X and Y channels) and defines a section grid\n"
                "   					as a slice through a voxel file.\n"
                "   					The grid cell sizes can be left as GS_R8DM, in which\n"
                "   					case an attempt will be made to match the voxel cell\n"
                "   					size, based on the line azimuth, voxel rotation, etc.\n"
                "   \n"
                "   					If the slice does NOT intersect the voxel, or if\n"
                "   					there are fewer than 2 valid locations in the line,\n"
                "   					then no grid file is created, but there is no error.\n"
                "   					(This is to simplify creating multiple grids from\n"
                "   					at once, where not all may intersect).\n"
                "   				\n\n"
               ).staticmethod("voxel_section");
    pyClass.def("write_wa", &GXDU_wrap_write_wa,
                "write_wa((GXDB)arg1, (int)arg2, (GXLST)arg3, (GXWA)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write data to an ASCII file.\n\n"

                ":param arg1: database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: line symbol\n"
                ":type arg2: int\n"
                ":param arg3: list of channel names to write\n"
                ":type arg3: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg4: WA to write to\n"
                ":type arg4: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Channels to be written should be placed in a LST object.\n"
                "   \n"
                "   					Channels are written in the order of the list.  Only the\n"
                "   					channel names in the list are used.\n"
                "   \n"
                "   					Data is formated as in the channel definition and\n"
                "   					channels are separated by a single space character.\n"
                "   				\n\n"
               ).staticmethod("write_wa");
    pyClass.def("xyz_line", &GXDU_wrap_xyz_line,
                "xyz_line((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Break up a line based on tolerance of lateral distance.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line to be broken up\n"
                ":type arg2: int\n"
                ":param arg3: Channel X\n"
                ":type arg3: int\n"
                ":param arg4: Channel Y\n"
                ":type arg4: int\n"
                ":param arg5: Line direction, 0-any, 1-X, 2-Y.\n"
                ":type arg5: int\n"
                ":param arg6: Tolerance, DUMMY for the default (10% of the separation between the first two points.\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The original line will be deleted.\n\n"
               ).staticmethod("xyz_line");
    pyClass.def("xyz_line2", &GXDU_wrap_xyz_line2,
                "xyz_line2((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (float)arg6, (float)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Break up a line based on tolerance of lateral and horizontal distance.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line to be broken up [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Channel X [DB_LOCK_READWRITE]\n"
                ":type arg3: int\n"
                ":param arg4: Channel Y [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: Line direction, 0-any, 1-X, 2-Y.\n"
                ":type arg5: int\n"
                ":param arg6: Tolerance, DUMMY for the default (10% of the separation between the first two points.\n"
                ":type arg6: float\n"
                ":param arg7: Downline Tolerance, DUMMY for none\n"
                ":type arg7: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The original line will be deleted.\n\n"
               ).staticmethod("xyz_line2");
    pyClass.def("xyz_line3", &GXDU_wrap_xyz_line3,
                "xyz_line3((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (float)arg6, (float)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Break up a line based on tolerance of lateral and horizontal distance.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line to be broken up [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Channel X [DB_LOCK_READWRITE]\n"
                ":type arg3: int\n"
                ":param arg4: Channel Y [DB_LOCK_READWRITE]\n"
                ":type arg4: int\n"
                ":param arg5: Line direction, 0-any, 1-X, 2-Y.\n"
                ":type arg5: int\n"
                ":param arg6: Tolerance, DUMMY for the default (10% of the separation between the first two points.\n"
                ":type arg6: float\n"
                ":param arg7: Downline Tolerance, DUMMY for none\n"
                ":type arg7: float\n"
                ":param arg8: Reset starting fiducials to zero (0: No, 1: Yes)\n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The same as XyzLine2, but with an option to reset each line's starting fiducial to zero.\n\n"
               ).staticmethod("xyz_line3");
    pyClass.def("z_mask", &GXDU_wrap_z_mask,
                "z_mask((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Mask dummies in one channel against another(Z) with the range Zmin/Zmax.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line Handle\n"
                ":type arg2: int\n"
                ":param arg3: Channel to mask [DB_LOCK_READWRITE]\n"
                ":type arg3: int\n"
                ":param arg4: Mask Channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Min value of mask range\n"
                ":type arg5: float\n"
                ":param arg6: Max value of mask range\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("z_mask");
    pyClass.def("range_xy", &GXDU_wrap_range_xy,
                "range_xy((GXDB)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the range of X, and Y in the selected lines.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Minimum X (returned)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Minimum Y (returned)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Maximum X (returned)\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Maximum Y (returned)\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns the range in X and Y of the current X and Y channels.\n"
                "   					Returned values are dummy if no valid items are found.\n"
                "   				\n\n"
               ).staticmethod("range_xy");
    pyClass.def("range_xyz", &GXDU_wrap_range_xyz,
                "range_xyz((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9, (float_ref)arg10, (int_ref)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the range of X, Y and Z in selected lines.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: X Channel [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Y Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Z Channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Minimum X (returned)\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Minimum Y (returned)\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Minimum Z (returned)\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Maximum X (returned)\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Maximum Y (returned)\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: Maximum Z (returned)\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: Number of data values (returned)\n"
                ":type arg11: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The X, Y and Z channels should be normal (not array) channels.\n"
                "   					Only locations where all values are non-dummy are included in the calculation.\n"
                "   					If no non-dummy values are found, Dummy values are returned.\n"
                "   				\n\n"
               ).staticmethod("range_xyz");
    pyClass.def("range_xyz_data", &GXDU_wrap_range_xyz_data,
                "range_xyz_data((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9, (float_ref)arg10, (float_ref)arg11, (float_ref)arg12, (float_ref)arg13, (int_ref)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the range of X, Y, Z and Data values in selected lines.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: X Channel [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Y Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Z Channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Data Channel [DB_LOCK_READONLY]\n"
                ":type arg5: int\n"
                ":param arg6: Minimum X (returned)\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Minimum Y (returned)\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Minimum Z (returned)\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Minimum Data value (returned)\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: Maximum X (returned)\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: Maximum Y (returned)\n"
                ":type arg11: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg12: Maximum Z (returned)\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg13: Maximum Data value (returned)\n"
                ":type arg13: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg14: Number of data values (returned)\n"
                ":type arg14: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The Z and Data channels may be array channels, but both must have\n"
                "   					the same number of columns.\n"
                "   					Only values where all channels are non-dummy (or, for VA channels,\n"
                "   					where the Z or Data value are defined) are included in the calculation.\n"
                "   					If no non-dummy values are found, Dummy values are returned.\n"
                "   					This function is optimized for cases where Z and Data are array channels\n"
                "   					with many columns (e.g. 32 or more columns).\n"
                "   				\n\n"
               ).staticmethod("range_xyz_data");
    pyClass.def("create_drillhole_parameter_weight_constraint_database", &GXDU_wrap_create_drillhole_parameter_weight_constraint_database,
                "create_drillhole_parameter_weight_constraint_database((GXDB)arg1, (int)arg2, (GXREG)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Used for weighting inversion models.\n\n"

                ":param arg1: Database (selected lines used)\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Property channel handle [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Parameters (see notes)\n"
                ":type arg3: :class:`geosoft.gxapi.GXREG`\n"
                ":param arg4: Output database\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Control parameters are passed in the REG (to allow for future expansion without\n"
                "   					the need to modify the wrappers).\n"
                "   					The input drillhole database must contain current X, Y and Z channels.\n"
                "   					Drillhole data should be equally spaced (or nearly so) down the hole.\n"
                "   					Weights are calculated on a circle perpendicular to the hole at each point.\n"
                "   \n"
                "   					RADIUS - Maximum radius from drillhole to create weighting points (Default = 100).\n"
                "   					INCRMENENT - Grid cell size in weighting circle (Default = 10).\n"
                "   					MINIMUM - the minimum weighting value to apply, at the radius (Default = 0.0001).\n"
                "   					POWER - Exponential power to use in the weighting function (negative of this is used) (Default = 2).\n"
                "   				\n\n"
               ).staticmethod("create_drillhole_parameter_weight_constraint_database");
    pyClass.def("calculate_draped_survey_altitude", &GXDU_wrap_calculate_draped_survey_altitude,
                "calculate_draped_survey_altitude((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (GXIMG)arg5, (int)arg6, (float)arg7, (float)arg8, (float)arg9, (int)arg10, (float)arg11, (float)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate a draped flight path, enforcing maximum descent and ascent rates.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: X Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Topography grid\n"
                ":type arg5: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg6: Output draped altitude channel [DB_LOCK_READWRITE]\n"
                ":type arg6: int\n"
                ":param arg7: Maximum rate of ascent (%)\n"
                ":type arg7: float\n"
                ":param arg8: Maximum rate of descent (%)\n"
                ":type arg8: float\n"
                ":param arg9: Minimum terrain clearance (drape height)\n"
                ":type arg9: float\n"
                ":param arg10: Number of times to apply Hanning Filter\n"
                ":type arg10: int\n"
                ":param arg11: Width of Hanning Filter\n"
                ":type arg11: float\n"
                ":param arg12: Minimum radius of curvature down slopes and at valley bottoms (rDUMMY to disable)\n"
                ":type arg12: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Calculate a draped flight path, enforcing maximum descent and ascent rates. Additional Inputs are the sample distance along the line\n"
                "   					and a topography grid.\n"
                "   				\n\n"
               ).staticmethod("calculate_draped_survey_altitude");
    pyClass.def("calculate_draped_survey_altitude2", &GXDU_wrap_calculate_draped_survey_altitude2,
                "calculate_draped_survey_altitude2((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (GXIMG)arg5, (int)arg6, (int)arg7, (float)arg8, (float)arg9, (float)arg10, (float)arg11, (int)arg12, (float)arg13, (float)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate a draped flight path, enforcing maximum descent and ascent rates.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: X Channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Topography grid\n"
                ":type arg5: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg6: Output DEM channel [DB_LOCK_READWRITE] (can be NULLSYMB if not required)\n"
                ":type arg6: int\n"
                ":param arg7: Output draped altitude channel [DB_LOCK_READWRITE]\n"
                ":type arg7: int\n"
                ":param arg8: Maximum rate of ascent (%)\n"
                ":type arg8: float\n"
                ":param arg9: Maximum rate of descent (%)\n"
                ":type arg9: float\n"
                ":param arg10: Nominal terrain clearance (drape height)\n"
                ":type arg10: float\n"
                ":param arg11: Minimum terrain clearance (hard minimum drape height)\n"
                ":type arg11: float\n"
                ":param arg12: Number of times to apply Hanning Filter\n"
                ":type arg12: int\n"
                ":param arg13: Width of Hanning Filter\n"
                ":type arg13: float\n"
                ":param arg14: Minimum radius of curvature down slopes and at valley bottoms (rDUMMY to disable)\n"
                ":type arg14: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Calculate a draped flight path, enforcing maximum descent and ascent rates.\n"
                "   					Set both a nominal and minimum drape height.\n"
                "   					Additional Inputs are the sample distance along the line\n"
                "   					and a topography grid.\n"
                "   				\n\n"
               ).staticmethod("calculate_draped_survey_altitude2");
    pyClass.def("direct_grid_data_to_voxel", &GXDU_wrap_direct_grid_data_to_voxel,
                "direct_grid_data_to_voxel((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (str)arg6, (float)arg7, (float)arg8, (float)arg9, (int)arg10, (int)arg11, (int)arg12, (float)arg13, (float)arg14, (float)arg15, (int)arg16) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a voxel using direct gridding.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: X channel [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Y channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Z channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Data channel [DB_LOCK_READONLY]\n"
                ":type arg5: int\n"
                ":param arg6: Output voxel filename\n"
                ":type arg6: str\n"
                ":param arg7: Voxel origin X\n"
                ":type arg7: float\n"
                ":param arg8: Voxel origin Y\n"
                ":type arg8: float\n"
                ":param arg9: Voxel origin Z\n"
                ":type arg9: float\n"
                ":param arg10: Voxel cell count X\n"
                ":type arg10: int\n"
                ":param arg11: Voxel cell count Y\n"
                ":type arg11: int\n"
                ":param arg12: Voxel cell count Z\n"
                ":type arg12: int\n"
                ":param arg13: Voxel cell size X\n"
                ":type arg13: float\n"
                ":param arg14: Voxel cell size Y\n"
                ":type arg14: float\n"
                ":param arg15: Voxel cell size Z\n"
                ":type arg15: float\n"
                ":param arg16: \\ :ref:`DU_DIRECTGRID_METHOD`\\ \n"
                ":type arg16: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Z and Data channels may be array channels. If they are, the array sizes must match.\n\n"
               ).staticmethod("direct_grid_data_to_voxel");
    pyClass.def("direct_grid_item_counts_to_voxel", &GXDU_wrap_direct_grid_item_counts_to_voxel,
                "direct_grid_item_counts_to_voxel((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (str)arg6, (float)arg7, (float)arg8, (float)arg9, (int)arg10, (int)arg11, (int)arg12, (float)arg13, (float)arg14, (float)arg15, (bool)arg16) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a voxel using direct gridding containing the number of data points in each cell.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: X channel [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Y channel [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Z channel [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Data channel [DB_LOCK_READONLY]\n"
                ":type arg5: int\n"
                ":param arg6: Output voxel filename\n"
                ":type arg6: str\n"
                ":param arg7: Voxel origin X\n"
                ":type arg7: float\n"
                ":param arg8: Voxel origin Y\n"
                ":type arg8: float\n"
                ":param arg9: Voxel origin Z\n"
                ":type arg9: float\n"
                ":param arg10: Voxel cell count X\n"
                ":type arg10: int\n"
                ":param arg11: Voxel cell count Y\n"
                ":type arg11: int\n"
                ":param arg12: Voxel cell count Z\n"
                ":type arg12: int\n"
                ":param arg13: Voxel cell size X\n"
                ":type arg13: float\n"
                ":param arg14: Voxel cell size Y\n"
                ":type arg14: float\n"
                ":param arg15: Voxel cell size Z\n"
                ":type arg15: float\n"
                ":param arg16: Replace zero values in output with DUMMY? bool\n"
                ":type arg16: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Z and Data channels may be array channels. If they are, the array sizes must match.\n\n"
               ).staticmethod("direct_grid_item_counts_to_voxel");

    scope().attr("DB_DUP_FIRST") = (int32_t)1;
    scope().attr("DB_DUP_AVERAGE") = (int32_t)2;
    scope().attr("DB_DUP_MINIMUM") = (int32_t)3;
    scope().attr("DB_DUP_MAXIMUM") = (int32_t)4;
    scope().attr("DB_DUP_MEDIAN") = (int32_t)5;
    scope().attr("DB_DUP_LAST") = (int32_t)6;
    scope().attr("DB_DUPEDIT_SINGLE") = (int32_t)0;
    scope().attr("DB_DUPEDIT_ALL") = (int32_t)1;
    scope().attr("DU_CHANNELS_DISPLAYED") = (int32_t)0;
    scope().attr("DU_CHANNELS_ALL") = (int32_t)1;
    scope().attr("DU_EXPORT_CSV") = (int32_t)0;
    scope().attr("DU_EXPORT_ODDF") = (int32_t)1;
    scope().attr("DU_EXPORT_POST_PC") = (int32_t)2;
    scope().attr("DU_EXPORT_POST_UNIX") = (int32_t)3;
    scope().attr("DU_FILL_INSIDE") = (int32_t)0;
    scope().attr("DU_FILL_OUTSIDE") = (int32_t)1;
    scope().attr("DU_IMPORT_APPEND") = (int32_t)0;
    scope().attr("DU_IMPORT_REPLACE") = (int32_t)1;
    scope().attr("DU_IMPORT_MERGE") = (int32_t)2;
    scope().attr("DU_IMPORT_MERGE_APPEND") = (int32_t)3;
    scope().attr("DU_INTERP_NEAREST") = (int32_t)1;
    scope().attr("DU_INTERP_LINEAR") = (int32_t)2;
    scope().attr("DU_INTERP_CUBIC") = (int32_t)3;
    scope().attr("DU_INTERP_AKIMA") = (int32_t)4;
    scope().attr("DU_INTERP_PREDICT") = (int32_t)5;
    scope().attr("DU_INTERP_EDGE_NONE") = (int32_t)0;
    scope().attr("DU_INTERP_EDGE_SAME") = (int32_t)1;
    scope().attr("DU_INTERP_EDGE_NEAREST") = (int32_t)2;
    scope().attr("DU_INTERP_EDGE_LINEAR") = (int32_t)3;
    scope().attr("DU_LAB_TYPE_FREE") = (int32_t)1;
    scope().attr("DU_LAB_TYPE_COMMA") = (int32_t)2;
    scope().attr("DU_LEVEL_LINES") = (int32_t)0;
    scope().attr("DU_LEVEL_TIES") = (int32_t)1;
    scope().attr("DU_LEVEL_ALL") = (int32_t)2;
    scope().attr("DU_LINEOUT_SINGLE") = (int32_t)0;
    scope().attr("DU_LINEOUT_MULTIPLE") = (int32_t)1;
    scope().attr("DU_FEATURE_TYPE_OUTPUT_POINT") = (int32_t)0;
    scope().attr("DU_FEATURE_TYPE_OUTPUT_LINE") = (int32_t)1;
    scope().attr("DU_GEODATABASE_EXPORT_TYPE_OVERWRITE_GEODATABASE") = (int32_t)0;
    scope().attr("DU_GEODATABASE_EXPORT_TYPE_OVERWRITE_FEATURECLASS") = (int32_t)1;
    scope().attr("DU_GEODATABASE_EXPORT_TYPE_APPEND") = (int32_t)2;
    scope().attr("DU_LINES_DISPLAYED") = (int32_t)0;
    scope().attr("DU_LINES_SELECTED") = (int32_t)1;
    scope().attr("DU_LINES_ALL") = (int32_t)2;
    scope().attr("DU_LOADLTB_REPLACE") = (int32_t)0;
    scope().attr("DU_LOADLTB_APPEND") = (int32_t)1;
    scope().attr("DU_LOOKUP_EXACT") = (int32_t)0;
    scope().attr("DU_LOOKUP_NEAREST") = (int32_t)1;
    scope().attr("DU_LOOKUP_INTERPOLATE") = (int32_t)2;
    scope().attr("DU_LOOKUP_NEARESTCLOSE") = (int32_t)3;
    scope().attr("DU_LOOKUP_INTERPCLOSE") = (int32_t)4;
    scope().attr("DU_LOOKUP_INTERPOLATE_DUMMYOUTSIDE") = (int32_t)5;
    scope().attr("DU_LOOKUP_INTERPOLATE_CONSTOUTSIDE") = (int32_t)6;
    scope().attr("DU_LOOKUP_INTERPOLATE_EXTPLOUTSIDE") = (int32_t)7;
    scope().attr("DU_LOOKUP_MAXOPTION") = (int32_t)8;
    scope().attr("DU_MASK_INSIDE") = (int32_t)0;
    scope().attr("DU_MASK_OUTSIDE") = (int32_t)1;
    scope().attr("DU_MERGE_APPEND") = (int32_t)0;
    scope().attr("DU_MODFID_INSERT") = (int32_t)0;
    scope().attr("DU_MODFID_DELETE") = (int32_t)1;
    scope().attr("DU_MODFID_APPEND") = (int32_t)2;
    scope().attr("DU_MOVE_ABSOLUTE") = (int32_t)0;
    scope().attr("DU_MOVE_MINUS") = (int32_t)1;
    scope().attr("DU_MOVE_PLUS") = (int32_t)2;
    scope().attr("DU_MOVE_INTERP") = (int32_t)3;
    scope().attr("DU_REFID_LINEAR") = (int32_t)0;
    scope().attr("DU_REFID_MINCUR") = (int32_t)1;
    scope().attr("DU_REFID_AKIMA") = (int32_t)2;
    scope().attr("DU_REFID_NEAREST") = (int32_t)3;
    scope().attr("DU_SORT_ASCENDING") = (int32_t)0;
    scope().attr("DU_SORT_DESCENDING") = (int32_t)1;
    scope().attr("DU_SPLITLINE_XYPOSITION") = (int32_t)0;
    scope().attr("DU_SPLITLINE_SEQUENTIAL") = (int32_t)1;
    scope().attr("DU_SPLITLINE_TOVERSIONS") = (int32_t)2;
    scope().attr("DU_STORAGE_LINE") = (int32_t)0;
    scope().attr("DU_STORAGE_GROUP") = (int32_t)1;
    scope().attr("QC_PLAN_SURVEYLINE") = (int32_t)0;
    scope().attr("QC_PLAN_TIELINE") = (int32_t)1;
    scope().attr("QC_PLAN_BOTHLINES") = (int32_t)2;
    scope().attr("DU_DISTANCE_CHANNEL_MAINTAIN_DIRECTION") = (int32_t)0;
    scope().attr("DU_DISTANCE_CHANNEL_CARTESIAN_COORDINATES") = (int32_t)1;
    scope().attr("DU_DIRECTGRID_MIN") = (int32_t)0;
    scope().attr("DU_DIRECTGRID_MAX") = (int32_t)1;
    scope().attr("DU_DIRECTGRID_MEAN") = (int32_t)2;

}
