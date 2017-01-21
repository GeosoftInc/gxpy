#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXDB_wrap_create_dup(GXDBPtr self, const gx_string_type& arg1)
{
    self->create_dup(arg1);
}
inline void GXDB_wrap_create_dup_comp(GXDBPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->create_dup_comp(arg1, (DB_COMP)arg2);
}
inline int32_t GXDB_wrap_dup_symb_across(GXDBPtr self, GXDBPtr arg1, int32_t arg2)
{
    int32_t ret = self->dup_symb_across(arg1, arg2);
    return ret;
}
inline void GXDB_wrap_easy_maker_symb(GXDBPtr self, int32_t arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    self->easy_maker_symb(arg1, arg2, arg3);
}
inline void GXDB_wrap_get_chan_str(GXDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3, str_ref& arg4)
{
    self->get_chan_str(arg1, arg2, arg3, arg4);
}
inline void GXDB_wrap_get_chan_vv(GXDBPtr self, int32_t arg1, int32_t arg2, GXVVPtr arg3)
{
    self->get_chan_vv(arg1, arg2, arg3);
}
inline void GXDB_wrap_get_chan_vv_expanded(GXDBPtr self, int32_t arg1, int32_t arg2, GXVVPtr arg3)
{
    self->get_chan_vv_expanded(arg1, arg2, arg3);
}
inline void GXDB_wrap_get_ipj(GXDBPtr self, int32_t arg1, GXIPJPtr arg2)
{
    self->get_ipj(arg1, arg2);
}
inline void GXDB_wrap_get_itr(GXDBPtr self, int32_t arg1, GXITRPtr arg2)
{
    self->get_itr(arg1, arg2);
}
inline void GXDB_wrap_get_reg_symb(GXDBPtr self, int32_t arg1, GXREGPtr arg2)
{
    self->get_reg_symb(arg1, arg2);
}
inline void GXDB_wrap_get_reg_symb_setting(GXDBPtr self, int32_t arg1, const gx_string_type& arg2, str_ref& arg3)
{
    self->get_reg_symb_setting(arg1, arg2, arg3);
}
inline void GXDB_wrap_get_va_chan_vv(GXDBPtr self, int32_t arg1, int32_t arg2, GXVVPtr arg3, int32_t arg4, int32_t arg5)
{
    self->get_va_chan_vv(arg1, arg2, arg3, arg4, arg5);
}
inline int32_t GXDB_wrap_blobs_max(GXDBPtr self)
{
    int32_t ret = self->blobs_max();
    return ret;
}
inline int32_t GXDB_wrap_chans_max(GXDBPtr self)
{
    int32_t ret = self->chans_max();
    return ret;
}
inline void GXDB_wrap_format_chan(GXDBPtr self, int32_t arg1, double arg2, str_ref& arg3)
{
    self->format_chan(arg1, arg2, arg3);
}
inline int32_t GXDB_wrap_get_chan_array_size(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->get_chan_array_size(arg1);
    return ret;
}
inline void GXDB_wrap_get_chan_class(GXDBPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_chan_class(arg1, arg2);
}
inline int32_t GXDB_wrap_get_chan_decimal(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->get_chan_decimal(arg1);
    return ret;
}
inline int32_t GXDB_wrap_get_chan_format(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->get_chan_format(arg1);
    return ret;
}
inline int32_t GXDB_wrap_get_chan_int(GXDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    int32_t ret = self->get_chan_int(arg1, arg2, arg3);
    return ret;
}
inline void GXDB_wrap_get_chan_label(GXDBPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_chan_label(arg1, arg2);
}
inline void GXDB_wrap_get_chan_name(GXDBPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_chan_name(arg1, arg2);
}
inline int32_t GXDB_wrap_get_chan_protect(GXDBPtr self, int32_t arg1)
{
    DB_CHAN_PROTECTION ret = self->get_chan_protect(arg1);
    return ret;
}
inline int32_t GXDB_wrap_get_chan_type(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->get_chan_type(arg1);
    return ret;
}
inline void GXDB_wrap_get_chan_unit(GXDBPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_chan_unit(arg1, arg2);
}
inline int32_t GXDB_wrap_get_chan_width(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->get_chan_width(arg1);
    return ret;
}
inline void GXDB_wrap_get_name(GXDBPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_name((DB_NAME)arg1, arg2);
}
inline int32_t GXDB_wrap_get_reg_symb_setting_int(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    int32_t ret = self->get_reg_symb_setting_int(arg1, arg2);
    return ret;
}
inline void GXDB_wrap_get_symb_name(GXDBPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_symb_name(arg1, arg2);
}
inline int32_t GXDB_wrap_have_itr(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->have_itr(arg1);
    return ret;
}
inline int32_t GXDB_wrap_coord_pair(GXDBPtr self, const gx_string_type& arg1, str_ref& arg2)
{
    DB_COORDPAIR ret = self->coord_pair(arg1, arg2);
    return ret;
}
inline int32_t GXDB_wrap_lines_max(GXDBPtr self)
{
    int32_t ret = self->lines_max();
    return ret;
}
inline int32_t GXDB_wrap_users_max(GXDBPtr self)
{
    int32_t ret = self->users_max();
    return ret;
}
inline void GXDB_wrap_maker_symb(GXDBPtr self, int32_t arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    self->maker_symb(arg1, arg2, arg3, arg4);
}
inline void GXDB_wrap_put_chan_vv(GXDBPtr self, int32_t arg1, int32_t arg2, GXVVPtr arg3)
{
    self->put_chan_vv(arg1, arg2, arg3);
}
inline void GXDB_wrap_put_va_chan_vv(GXDBPtr self, int32_t arg1, int32_t arg2, GXVVPtr arg3, int32_t arg4, int32_t arg5)
{
    self->put_va_chan_vv(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDB_wrap_read_blob_bf(GXDBPtr self, int32_t arg1, GXBFPtr arg2)
{
    self->read_blob_bf(arg1, arg2);
}
inline double GXDB_wrap_get_chan_double(GXDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    double ret = self->get_chan_double(arg1, arg2, arg3);
    return ret;
}
inline double GXDB_wrap_get_reg_symb_setting_double(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    double ret = self->get_reg_symb_setting_double(arg1, arg2);
    return ret;
}
inline void GXDB_wrap_set_all_chan_protect(GXDBPtr self, int32_t arg1)
{
    self->set_all_chan_protect((DB_CHAN_PROTECTION)arg1);
}
inline void GXDB_wrap_set_chan_class(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_chan_class(arg1, arg2);
}
inline void GXDB_wrap_set_chan_decimal(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    self->set_chan_decimal(arg1, arg2);
}
inline void GXDB_wrap_set_chan_format(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    self->set_chan_format(arg1, (DB_CHAN_FORMAT)arg2);
}
inline void GXDB_wrap_set_chan_int(GXDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    self->set_chan_int(arg1, arg2, arg3, arg4);
}
inline void GXDB_wrap_set_chan_label(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_chan_label(arg1, arg2);
}
inline void GXDB_wrap_set_chan_name(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_chan_name(arg1, arg2);
}
inline void GXDB_wrap_set_chan_protect(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    self->set_chan_protect(arg1, (DB_CHAN_PROTECTION)arg2);
}
inline void GXDB_wrap_set_chan_double(GXDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3, double arg4)
{
    self->set_chan_double(arg1, arg2, arg3, arg4);
}
inline void GXDB_wrap_set_chan_str(GXDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3, const gx_string_type& arg4)
{
    self->set_chan_str(arg1, arg2, arg3, arg4);
}
inline void GXDB_wrap_set_chan_unit(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_chan_unit(arg1, arg2);
}
inline void GXDB_wrap_set_chan_width(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    self->set_chan_width(arg1, arg2);
}
inline void GXDB_wrap_set_ipj(GXDBPtr self, int32_t arg1, int32_t arg2, GXIPJPtr arg3)
{
    self->set_ipj(arg1, arg2, arg3);
}
inline void GXDB_wrap_set_itr(GXDBPtr self, int32_t arg1, GXITRPtr arg2)
{
    self->set_itr(arg1, arg2);
}
inline void GXDB_wrap_set_reg_symb(GXDBPtr self, int32_t arg1, GXREGPtr arg2)
{
    self->set_reg_symb(arg1, arg2);
}
inline void GXDB_wrap_set_reg_symb_setting(GXDBPtr self, int32_t arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    self->set_reg_symb_setting(arg1, arg2, arg3);
}
inline void GXDB_wrap_write_blob_bf(GXDBPtr self, int32_t arg1, GXBFPtr arg2)
{
    self->write_blob_bf(arg1, arg2);
}
inline void GXDB_wrap_commit(GXDBPtr self)
{
    self->commit();
}
inline void GXDB_wrap_compact(GXDBPtr self)
{
    self->compact();
}
inline void GXDB_wrap_create(const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, const gx_string_type& arg7, const gx_string_type& arg8)
{
    GXDB::create(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXDB_wrap_create_comp(const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, const gx_string_type& arg7, const gx_string_type& arg8, int32_t arg9, int32_t arg10)
{
    GXDB::create_comp(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (DB_COMP)arg10);
}
inline void GXDB_wrap_create_ex(const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, const gx_string_type& arg7, const gx_string_type& arg8, int32_t arg9)
{
    GXDB::create_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXDB_wrap_del_line0(GXDBPtr self)
{
    self->del_line0();
}
inline void GXDB_wrap_discard(GXDBPtr self)
{
    self->discard();
}
inline void GXDB_wrap_grow(const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    GXDB::grow(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline bool GXDB_wrap_can_open(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    bool ret = GXDB::can_open(arg1, arg2, arg3);
    return ret;
}
inline bool GXDB_wrap_can_open_read_only(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    bool ret = GXDB::can_open_read_only(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXDB_wrap_check(GXDBPtr self)
{
    int32_t ret = self->check();
    return ret;
}
inline int32_t GXDB_wrap_is_empty(GXDBPtr self)
{
    int32_t ret = self->is_empty();
    return ret;
}
inline int32_t GXDB_wrap_is_line_empty(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->is_line_empty(arg1);
    return ret;
}
inline GXDBPtr GXDB_wrap_open(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXDBPtr ret = GXDB::open(arg1, arg2, arg3);
    return ret;
}
inline GXDBPtr GXDB_wrap_open_read_only(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXDBPtr ret = GXDB::open_read_only(arg1, arg2, arg3);
    return ret;
}
inline void GXDB_wrap_repair(const gx_string_type& arg1)
{
    GXDB::repair(arg1);
}
inline void GXDB_wrap_sync(GXDBPtr self)
{
    self->sync();
}
inline void GXDB_wrap_copy_data(GXDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    self->copy_data(arg1, arg2, arg3);
}
inline int32_t GXDB_wrap_get_col_va(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->get_col_va(arg1);
    return ret;
}
inline int32_t GXDB_wrap_get_channel_length(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    int32_t ret = self->get_channel_length(arg1, arg2);
    return ret;
}
inline double GXDB_wrap_get_fid_incr(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    double ret = self->get_fid_incr(arg1, arg2);
    return ret;
}
inline double GXDB_wrap_get_fid_start(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    double ret = self->get_fid_start(arg1, arg2);
    return ret;
}
inline void GXDB_wrap_set_fid(GXDBPtr self, int32_t arg1, int32_t arg2, double arg3, double arg4)
{
    self->set_fid(arg1, arg2, arg3, arg4);
}
inline void GXDB_wrap_window_va_ch(GXDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    self->window_va_ch(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDB_wrap_window_va_ch2(GXDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3, GXVVPtr arg4)
{
    self->window_va_ch2(arg1, arg2, arg3, arg4);
}
inline void GXDB_wrap_set_line_selection(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    self->set_line_selection(arg1, (DB_LINE_SELECT)arg2);
}
inline int32_t GXDB_wrap_get_line_selection(GXDBPtr self, int32_t arg1)
{
    DB_LINE_SELECT ret = self->get_line_selection(arg1);
    return ret;
}
inline int32_t GXDB_wrap_first_sel_line(GXDBPtr self)
{
    int32_t ret = self->first_sel_line();
    return ret;
}
inline void GXDB_wrap_get_line_map_fid(GXDBPtr self, int32_t arg1, float_ref& arg2, float_ref& arg3)
{
    self->get_line_map_fid(arg1, arg2, arg3);
}
inline int32_t GXDB_wrap_get_select(GXDBPtr self)
{
    int32_t ret = self->get_select();
    return ret;
}
inline int32_t GXDB_wrap_count_sel_lines(GXDBPtr self)
{
    int32_t ret = self->count_sel_lines();
    return ret;
}
inline int32_t GXDB_wrap_is_chan_name(const gx_string_type& arg1)
{
    int32_t ret = GXDB::is_chan_name(arg1);
    return ret;
}
inline int32_t GXDB_wrap_is_chan_valid(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->is_chan_valid(arg1);
    return ret;
}
inline int32_t GXDB_wrap_is_line_name(const gx_string_type& arg1)
{
    int32_t ret = GXDB::is_line_name(arg1);
    return ret;
}
inline int32_t GXDB_wrap_is_line_valid(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->is_line_valid(arg1);
    return ret;
}
inline int32_t GXDB_wrap_line_category(GXDBPtr self, int32_t arg1)
{
    DB_CATEGORY_LINE ret = self->line_category(arg1);
    return ret;
}
inline int32_t GXDB_wrap_line_flight(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->line_flight(arg1);
    return ret;
}
inline void GXDB_wrap_line_label(GXDBPtr self, int32_t arg1, str_ref& arg2, int32_t arg3)
{
    self->line_label(arg1, arg2, (DB_LINE_LABEL_FORMAT)arg3);
}
inline int32_t GXDB_wrap_line_number(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->line_number(arg1);
    return ret;
}
inline void GXDB_wrap_line_number2(GXDBPtr self, int32_t arg1, str_ref& arg2)
{
    self->line_number2(arg1, arg2);
}
inline int32_t GXDB_wrap_line_type(GXDBPtr self, int32_t arg1)
{
    DB_LINE_TYPE ret = self->line_type(arg1);
    return ret;
}
inline int32_t GXDB_wrap_line_version(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->line_version(arg1);
    return ret;
}
inline void GXDB_wrap_set_line_name(int32_t arg1, int32_t arg2, int32_t arg3, str_ref& arg4)
{
    GXDB::set_line_name(arg1, arg2, arg3, arg4);
}
inline void GXDB_wrap_set_line_name2(const gx_string_type& arg1, int32_t arg2, int32_t arg3, str_ref& arg4)
{
    GXDB::set_line_name2(arg1, arg2, arg3, arg4);
}
inline void GXDB_wrap_load_select(GXDBPtr self, const gx_string_type& arg1)
{
    self->load_select(arg1);
}
inline int32_t GXDB_wrap_next_sel_line(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->next_sel_line(arg1);
    return ret;
}
inline double GXDB_wrap_line_bearing(GXDBPtr self, int32_t arg1)
{
    double ret = self->line_bearing(arg1);
    return ret;
}
inline double GXDB_wrap_line_date(GXDBPtr self, int32_t arg1)
{
    double ret = self->line_date(arg1);
    return ret;
}
inline void GXDB_wrap_save_select(GXDBPtr self, const gx_string_type& arg1)
{
    self->save_select(arg1);
}
inline void GXDB_wrap_select(GXDBPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->select(arg1, (DB_LINE_SELECT)arg2);
}
inline void GXDB_wrap_set_line_bearing(GXDBPtr self, int32_t arg1, double arg2)
{
    self->set_line_bearing(arg1, arg2);
}
inline void GXDB_wrap_set_line_date(GXDBPtr self, int32_t arg1, double arg2)
{
    self->set_line_date(arg1, arg2);
}
inline void GXDB_wrap_set_line_flight(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    self->set_line_flight(arg1, arg2);
}
inline void GXDB_wrap_set_line_map_fid(GXDBPtr self, int32_t arg1, double arg2, double arg3)
{
    self->set_line_map_fid(arg1, arg2, arg3);
}
inline void GXDB_wrap_set_line_num(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    self->set_line_num(arg1, arg2);
}
inline void GXDB_wrap_set_line_type(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    self->set_line_type(arg1, (DB_LINE_TYPE)arg2);
}
inline void GXDB_wrap_set_line_ver(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    self->set_line_ver(arg1, arg2);
}
inline void GXDB_wrap_set_select(GXDBPtr self, int32_t arg1)
{
    self->set_select(arg1);
}
inline void GXDB_wrap_get_meta(GXDBPtr self, GXMETAPtr arg1)
{
    self->get_meta(arg1);
}
inline void GXDB_wrap_set_meta(GXDBPtr self, GXMETAPtr arg1)
{
    self->set_meta(arg1);
}
inline void GXDB_wrap_array_lst(GXDBPtr self, GXLSTPtr arg1)
{
    self->array_lst(arg1);
}
inline void GXDB_wrap_array_size_lst(GXDBPtr self, int32_t arg1, GXLSTPtr arg2)
{
    self->array_size_lst(arg1, arg2);
}
inline void GXDB_wrap_chan_lst(GXDBPtr self, GXLSTPtr arg1)
{
    self->chan_lst(arg1);
}
inline void GXDB_wrap_normal_chan_lst(GXDBPtr self, GXLSTPtr arg1)
{
    self->normal_chan_lst(arg1);
}
inline void GXDB_wrap_class_chan_lst(GXDBPtr self, GXLSTPtr arg1, const gx_string_type& arg2)
{
    self->class_chan_lst(arg1, arg2);
}
inline void GXDB_wrap_class_group_lst(GXDBPtr self, GXLSTPtr arg1, const gx_string_type& arg2)
{
    self->class_group_lst(arg1, arg2);
}
inline int32_t GXDB_wrap_create_symb(GXDBPtr self, const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    int32_t ret = self->create_symb(arg1, (DB_SYMB_TYPE)arg2, (DB_OWN)arg3, arg4);
    return ret;
}
inline int32_t GXDB_wrap_create_symb_ex(GXDBPtr self, const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    int32_t ret = self->create_symb_ex(arg1, (DB_SYMB_TYPE)arg2, (DB_OWN)arg3, arg4, arg5);
    return ret;
}
inline void GXDB_wrap_csv_chan_lst(GXDBPtr self, GXLSTPtr arg1, const gx_string_type& arg2)
{
    self->csv_chan_lst(arg1, arg2);
}
inline void GXDB_wrap_delete_symb(GXDBPtr self, int32_t arg1)
{
    self->delete_symb(arg1);
}
inline int32_t GXDB_wrap_dup_line_symb(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    int32_t ret = self->dup_line_symb(arg1, arg2);
    return ret;
}
inline int32_t GXDB_wrap_dup_symb(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    int32_t ret = self->dup_symb(arg1, arg2);
    return ret;
}
inline int32_t GXDB_wrap_dup_symb_no_lock(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    int32_t ret = self->dup_symb_no_lock(arg1, arg2);
    return ret;
}
inline int32_t GXDB_wrap_find_chan(GXDBPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->find_chan(arg1);
    return ret;
}
inline int32_t GXDB_wrap_find_symb(GXDBPtr self, const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = self->find_symb(arg1, (DB_SYMB_TYPE)arg2);
    return ret;
}
inline void GXDB_wrap_get_chan_order_lst(GXDBPtr self, GXLSTPtr arg1)
{
    self->get_chan_order_lst(arg1);
}
inline int32_t GXDB_wrap_get_xyz_chan_symb(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->get_xyz_chan_symb((DB_CHAN_SYMBOL)arg1);
    return ret;
}
inline int32_t GXDB_wrap_class_chan_list(GXDBPtr self, GXVVPtr arg1, const gx_string_type& arg2)
{
    int32_t ret = self->class_chan_list(arg1, arg2);
    return ret;
}
inline int32_t GXDB_wrap_exist_chan(GXDBPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->exist_chan(arg1);
    return ret;
}
inline int32_t GXDB_wrap_exist_symb(GXDBPtr self, const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = self->exist_symb(arg1, (DB_SYMB_TYPE)arg2);
    return ret;
}
inline int32_t GXDB_wrap_valid_symb(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    int32_t ret = self->valid_symb(arg1, (DB_SYMB_TYPE)arg2);
    return ret;
}
inline int32_t GXDB_wrap_get_symb_lock(GXDBPtr self, int32_t arg1)
{
    DB_LOCK ret = self->get_symb_lock(arg1);
    return ret;
}
inline void GXDB_wrap_get_xyz_chan(GXDBPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_xyz_chan((DB_CHAN_SYMBOL)arg1, arg2);
}
inline int32_t GXDB_wrap_symb_list(GXDBPtr self, GXVVPtr arg1, int32_t arg2)
{
    int32_t ret = self->symb_list(arg1, (DB_SYMB_TYPE)arg2);
    return ret;
}
inline void GXDB_wrap_line_lst(GXDBPtr self, GXLSTPtr arg1)
{
    self->line_lst(arg1);
}
inline void GXDB_wrap_lock_symb(GXDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    self->lock_symb(arg1, (DB_LOCK)arg2, (DB_WAIT)arg3);
}
inline void GXDB_wrap_mask_chan_lst(GXDBPtr self, GXLSTPtr arg1)
{
    self->mask_chan_lst(arg1);
}
inline void GXDB_wrap_selected_line_lst(GXDBPtr self, GXLSTPtr arg1)
{
    self->selected_line_lst(arg1);
}
inline void GXDB_wrap_set_chan_order_lst(GXDBPtr self, GXLSTPtr arg1)
{
    self->set_chan_order_lst(arg1);
}
inline void GXDB_wrap_set_xyz_chan(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_xyz_chan((DB_CHAN_SYMBOL)arg1, arg2);
}
inline void GXDB_wrap_string_chan_lst(GXDBPtr self, GXLSTPtr arg1)
{
    self->string_chan_lst(arg1);
}
inline void GXDB_wrap_symb_lst(GXDBPtr self, GXLSTPtr arg1, int32_t arg2)
{
    self->symb_lst(arg1, (DB_SYMB_TYPE)arg2);
}
inline void GXDB_wrap_un_lock_all_symb(GXDBPtr self)
{
    self->un_lock_all_symb();
}
inline void GXDB_wrap_un_lock_symb(GXDBPtr self, int32_t arg1)
{
    self->un_lock_symb(arg1);
}
inline void GXDB_wrap_add_associated_load(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    self->add_associated_load(arg1, arg2);
}
inline void GXDB_wrap_add_comment(GXDBPtr self, const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    self->add_comment(arg1, arg2, arg3);
}
inline void GXDB_wrap_add_int_comment(GXDBPtr self, const gx_string_type& arg1, int32_t arg2, bool arg3)
{
    self->add_int_comment(arg1, arg2, arg3);
}
inline void GXDB_wrap_add_double_comment(GXDBPtr self, const gx_string_type& arg1, double arg2, bool arg3)
{
    self->add_double_comment(arg1, arg2, arg3);
}
inline void GXDB_wrap_add_time_comment(GXDBPtr self, const gx_string_type& arg1, bool arg2)
{
    self->add_time_comment(arg1, arg2);
}
inline void GXDB_wrap_associate(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    self->associate(arg1, arg2);
}
inline void GXDB_wrap_associate_all(GXDBPtr self, int32_t arg1)
{
    self->associate_all(arg1);
}
inline void GXDB_wrap_associate_class(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->associate_class(arg1, arg2);
}
inline void GXDB_wrap_gen_valid_chan_symb(const gx_string_type& arg1, str_ref& arg2)
{
    GXDB::gen_valid_chan_symb(arg1, arg2);
}
inline void GXDB_wrap_gen_valid_line_symb(const gx_string_type& arg1, str_ref& arg2)
{
    GXDB::gen_valid_line_symb(arg1, arg2);
}
inline void GXDB_wrap_get_chan_va(GXDBPtr self, int32_t arg1, int32_t arg2, GXVAPtr arg3)
{
    self->get_chan_va(arg1, arg2, arg3);
}
inline void GXDB_wrap_get_va_scaling(GXDBPtr self, int32_t arg1, float_ref& arg2, float_ref& arg3)
{
    self->get_va_scaling(arg1, arg2, arg3);
}
inline void GXDB_wrap_get_va_windows(GXDBPtr self, int32_t arg1, int_ref& arg2, int_ref& arg3)
{
    self->get_va_windows(arg1, arg2, arg3);
}
inline void GXDB_wrap_set_va_base_coordinate_info(GXDBPtr self, int32_t arg1, int32_t arg2, double arg3, GXVVPtr arg4, const gx_string_type& arg5, bool arg6)
{
    self->set_va_base_coordinate_info(arg1, (DB_ARRAY_BASETYPE)arg2, arg3, arg4, arg5, arg6);
}
inline void GXDB_wrap_get_va_base_coordinate_info(GXDBPtr self, int32_t arg1, int_ref& arg2, float_ref& arg3, GXVVPtr arg4, str_ref& arg5)
{
    self->get_va_base_coordinate_info(arg1, (DB_ARRAY_BASETYPE&)arg2, arg3, arg4, arg5);
}
inline void GXDB_wrap_get_group_class(GXDBPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_group_class(arg1, arg2);
}
inline int32_t GXDB_wrap_get_info(GXDBPtr self, int32_t arg1)
{
    int32_t ret = self->get_info((DB_INFO)arg1);
    return ret;
}
inline void GXDB_wrap_get_va_prof_color_file(GXDBPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_va_prof_color_file(arg1, arg2);
}
inline void GXDB_wrap_get_va_prof_sect_option(GXDBPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_va_prof_sect_option(arg1, arg2);
}
inline void GXDB_wrap_get_va_sect_color_file(GXDBPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_va_sect_color_file(arg1, arg2);
}
inline int32_t GXDB_wrap_is_associated(GXDBPtr self, int32_t arg1, int32_t arg2)
{
    int32_t ret = self->is_associated(arg1, arg2);
    return ret;
}
inline int32_t GXDB_wrap_is_wholeplot(GXDBPtr self)
{
    int32_t ret = self->is_wholeplot();
    return ret;
}
inline void GXDB_wrap_put_chan_va(GXDBPtr self, int32_t arg1, int32_t arg2, GXVAPtr arg3)
{
    self->put_chan_va(arg1, arg2, arg3);
}
inline void GXDB_wrap_set_group_class(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_group_class(arg1, arg2);
}
inline void GXDB_wrap_set_va_prof_color_file(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_va_prof_color_file(arg1, arg2);
}
inline void GXDB_wrap_set_va_prof_sect_option(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_va_prof_sect_option(arg1, arg2);
}
inline void GXDB_wrap_set_va_scaling(GXDBPtr self, int32_t arg1, double arg2, double arg3)
{
    self->set_va_scaling(arg1, arg2, arg3);
}
inline void GXDB_wrap_set_va_sect_color_file(GXDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_va_sect_color_file(arg1, arg2);
}
inline void GXDB_wrap_set_va_windows(GXDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    self->set_va_windows(arg1, arg2, arg3);
}

void gxPythonImportGXDB()
{

    class_<GXDB, GXDBPtr> pyClass("GXDB",
                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		The DB class is used to create, open and work with databases and database symbols.\n"
                                  "   		Database symbols are objects inside databases, such as lines, channels and blobs\n"
                                  "   	\n\n"

                                  "\n\n**Note:**\n\n"

                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		The follwing defines are not used by any methods but are\n"
                                  "   		used by GX's:\n"
                                  "   \n"
                                  "   		\\ :ref:`DB_ACTIVITY_BLOB`\\ \n"
                                  "   	\n\n"
                                  , no_init);

    pyClass.def("null", &GXDB::null, "null() -> GXDB\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXDB`\n\n:returns: A null :class:`geosoft.gxapi.GXDB`\n:rtype: :class:`geosoft.gxapi.GXDB`\n").staticmethod("null");
    pyClass.def("is_null", &GXDB::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXDB is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXDB`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXDB::_internal_handle);
    pyClass.def("create_dup", &GXDB_wrap_create_dup,
                "create_dup((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method makes a brand new database identical to the input\n"
                "   					Database in-size.\n"
                "   					The database is opened in ReadWrite Mode.\n"
                "   				\n\n"

                ":param arg1: name of the Database File to Create\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create_dup_comp", &GXDB_wrap_create_dup_comp,
                "create_dup_comp((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method makes a brand new database identical to the input\n"
                "   					Database in-size except it changes the compression.\n"
                "   					The database is opened in ReadWrite Mode.\n"
                "   				\n\n"

                ":param arg1: name of the Database File to Create\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DB_COMP`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("dup_symb_across", &GXDB_wrap_dup_symb_across,
                "dup_symb_across((GXDB)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Create a new Symbol by duplicating an existing symbol.\n"
                "   					exactly the same type but in output database. The symbol must\n"
                "   					not already exist in the output database.\n"
                "   				\n\n"

                ":param arg1: Database output\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Symbol Handle to duplicate\n"
                ":type arg2: int\n"
                ":returns: New Symbol Handle\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("easy_maker_symb", &GXDB_wrap_easy_maker_symb,
                "easy_maker_symb((int)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Adds a Maker to the database symbol based on current GX\n\n"

                ":param arg1: Symbol to create maker for\n"
                ":type arg1: int\n"
                ":param arg2: Maker name, used in menu prompt\n"
                ":type arg2: str\n"
                ":param arg3: INI groups (terminate each with a \";\")\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_chan_str", &GXDB_wrap_get_chan_str,
                "get_chan_str((int)arg1, (int)arg2, (int)arg3, (str_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get individual elements in a channel.\n\n"

                ":param arg1: line\n"
                ":type arg1: int\n"
                ":param arg2: channel\n"
                ":type arg2: int\n"
                ":param arg3: index\n"
                ":type arg3: int\n"
                ":param arg4: string\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					These methods are slow and should only be used when\n"
                "   					performance is not an issue.\n"
                "   				\n\n"
               );
    pyClass.def("get_chan_vv", &GXDB_wrap_get_chan_vv,
                "get_chan_vv((int)arg1, (int)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Place the contents of a channel in a VV.\n\n"

                ":param arg1: Line\n"
                ":type arg1: int\n"
                ":param arg2: Channel\n"
                ":type arg2: int\n"
                ":param arg3: VV in which to place the data\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If a VA channel is specified, then element [0] of this\n"
                "   					VA channel is used to populated the VV.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXVV`\\  class.\n\n"
               );
    pyClass.def("get_chan_vv_expanded", &GXDB_wrap_get_chan_vv_expanded,
                "get_chan_vv_expanded((int)arg1, (int)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Read a channel into a VV. If the channel is a VA channel it is\n"
                "   					treaded as a VV channel with multiple values per fid and the FID expation\n"
                "   					is set to the array size.\n"
                "   				\n\n"

                ":param arg1: Line\n"
                ":type arg1: int\n"
                ":param arg2: Channel\n"
                ":type arg2: int\n"
                ":param arg3: VV in which to place the data\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method is to be used in conjunction with the \\ :func:`geosoft.gxapi.GXVV.re_fid_vv`\\  method\n"
                "   					that will honor the FID Expansion setting.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXVV`\\  class.\n\n"
               );
    pyClass.def("get_ipj", &GXDB_wrap_get_ipj,
                "get_ipj((int)arg1, (GXIPJ)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get georeference information in an IPJ.\n\n"

                ":param arg1: Symbol\n"
                ":type arg1: int\n"
                ":param arg2: IPJ to fill in\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the channel does not have an IPJ, the IPJ that is\n"
                "   					returned will have an unknown projection.\n"
                "   				\n\n"
               );
    pyClass.def("get_itr", &GXDB_wrap_get_itr,
                "get_itr((int)arg1, (GXITR)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get ITR for a channel.\n\n"

                ":param arg1: channel\n"
                ":type arg1: int\n"
                ":param arg2: ITR to fill in\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If a channel does not have an ITR, \\ :func:`geosoft.gxapi.GXDB.get_itr`\\  will not change\n"
                "   					the passed ITR.\n"
                "   					Channel must be locked for READONLY or READWRITE.\n"
                "   				\n\n"
               );
    pyClass.def("get_reg_symb", &GXDB_wrap_get_reg_symb,
                "get_reg_symb((int)arg1, (GXREG)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a REG object from a symbol\n\n"

                ":param arg1: Symbol, \\ :ref:`NULLSYMB`\\  for the database REG\n"
                ":type arg1: int\n"
                ":param arg2: REG to copy data into\n"
                ":type arg2: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_reg_symb_setting", &GXDB_wrap_get_reg_symb_setting,
                "get_reg_symb_setting((int)arg1, (str)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a REG string setting from a symbol reg\n\n"

                ":param arg1: Symbol, \\ :ref:`NULLSYMB`\\  for the database REG\n"
                ":type arg1: int\n"
                ":param arg2: REG entry name\n"
                ":type arg2: str\n"
                ":param arg3: returned setting\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The symbol REG is used to store a variety of attribute\n"
                "   					about the symbol.  Following a conventionally used entries:\n"
                "   \n"
                "   					UNITS                   - channel units\n"
                "   					CLASS                   - symbol class name (i.e. \"Assay\")\n"
                "   					_PJ_ipj                 - projection blob name\n"
                "   					_PJ_x                   - projection coordinate pair\n"
                "   					_PJ_y\n"
                "   					_PJ_name                - projection GXF-style info\n"
                "   					_PJ_ellipsoid\n"
                "   					_PJ_projection\n"
                "   					_PJ_units\n"
                "   					_PJ_datum_transform\n"
                "   \n"
                "   					This is a convenient but low-performance way to get/set REG\n"
                "   					settings.  If performance is an issue, and more than one\n"
                "   					setting is to be Get and or Set, use the REG directly.\n"
                "   				\n\n"
               );
    pyClass.def("get_va_chan_vv", &GXDB_wrap_get_va_chan_vv,
                "get_va_chan_vv((int)arg1, (int)arg2, (GXVV)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Place the contents of a specific part of a channel in a VV.\n\n"

                ":param arg1: Line\n"
                ":type arg1: int\n"
                ":param arg2: Channel\n"
                ":type arg2: int\n"
                ":param arg3: VV in which to place the data\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Offset\n"
                ":type arg4: int\n"
                ":param arg5: Number to Write\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If a VA channel is specified, then element [0] of this\n"
                "   					VA channel is used to populated the VV.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXVV`\\  class.\n\n"
               );
    pyClass.def("blobs_max", &GXDB_wrap_blobs_max,
                "blobs_max() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets Maximum Number of Blobs in the Database\n\n"

                ":returns: Maximum Number of Blobs in the Database\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("chans_max", &GXDB_wrap_chans_max,
                "chans_max() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets Maximum Number of Channels in the Database\n\n"

                ":returns: Maximum Number of Channels in the Database\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("format_chan", &GXDB_wrap_format_chan,
                "format_chan((int)arg1, (float)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Format a real value based on a channel format.\n\n"

                ":param arg1: channel handle\n"
                ":type arg1: int\n"
                ":param arg2: value to format\n"
                ":type arg2: float\n"
                ":param arg3: string\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the passed string is too short, the result will be\n"
                "   					\"\\ `*`\\ \\ `*`\\ \".\n"
                "   				\n\n"
               );
    pyClass.def("get_chan_array_size", &GXDB_wrap_get_chan_array_size,
                "get_chan_array_size((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method Gets a channel's array size for a\n"
                "   					given channel handle.\n"
                "   				\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":returns: Channel type\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               );
    pyClass.def("get_chan_class", &GXDB_wrap_get_chan_class,
                "get_chan_class((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method gets a channel's label\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":param arg2: returned class into\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The channel label is stored in the \"CLASS\" parameter\n"
                "   					of the channel reg. If no class is defined, then an\n"
                "   					empty string is returned.\n"
                "   					The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n"
                "   				\n\n"
               );
    pyClass.def("get_chan_decimal", &GXDB_wrap_get_chan_decimal,
                "get_chan_decimal((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method gets a channel's number of digits displayed\n"
                "   					to the right of the decimal point.\n"
                "   				\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":returns: Number of digits displayed to right of decimal\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("get_chan_format", &GXDB_wrap_get_chan_format,
                "get_chan_format((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method Gets a channel's display format for a\n"
                "   					given channel handle.\n"
                "   				\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":returns: Channel display format\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The returned format is one of the \\ :ref:`DB_CHAN_FORMAT`\\ .\n"
                "   					The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n"
                "   				\n\n"
               );
    pyClass.def("get_chan_int", &GXDB_wrap_get_chan_int,
                "get_chan_int((int)arg1, (int)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get individual elements in a channel.\n\n"

                ":param arg1: line\n"
                ":type arg1: int\n"
                ":param arg2: channel\n"
                ":type arg2: int\n"
                ":param arg3: index\n"
                ":type arg3: int\n"
                ":returns: Value, or dummy if out of range.\n"
                "          						For settings, terminates if error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					These methods are slow and should only be used when\n"
                "   					performance is not an issue.\n"
                "   				\n\n"
               );
    pyClass.def("get_chan_label", &GXDB_wrap_get_chan_label,
                "get_chan_label((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method gets a channel's label\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":param arg2: returned label into\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The channel label is stored in the \"LABEL\" parameter\n"
                "   					of the channel reg.  If the setting is empty, the\n"
                "   					channel name is returned.\n"
                "   					The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n"
                "   				\n\n"
               );
    pyClass.def("get_chan_name", &GXDB_wrap_get_chan_name,
                "get_chan_name((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method Gets a channel's name for a\n"
                "   					given channel handle.\n"
                "   				\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":param arg2: string to place name into\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("get_chan_protect", &GXDB_wrap_get_chan_protect,
                "get_chan_protect((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method gets a channel's read-only protection status.\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":returns: \\ :ref:`DB_CHAN_PROTECTION`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("get_chan_type", &GXDB_wrap_get_chan_type,
                "get_chan_type((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method Gets a channel's type for a\n"
                "   					given channel handle.\n"
                "   				\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":returns: Channel type\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The type returned is one of the \\ :ref:`DB_CATEGORY_CHAN`\\ .\n"
                "   					Use the GS_SIMPLE_TYPE() macro to convert to INT,REAL\n"
                "   					or string types.\n"
                "   					The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n"
                "   				\n\n"
               );
    pyClass.def("get_chan_unit", &GXDB_wrap_get_chan_unit,
                "get_chan_unit((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method Gets a channel's unit\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":param arg2: string to place unit into\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The unit label is stored in the \"UNITS\" parameter\n"
                "   					of the channel reg.\n"
                "   					The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n"
                "   				\n\n"
               );
    pyClass.def("get_chan_width", &GXDB_wrap_get_chan_width,
                "get_chan_width((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method gets a channel's display width for a\n"
                "   					given channel handle.\n"
                "   				\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":returns: Channel display width\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("get_name", &GXDB_wrap_get_name,
                "get_name((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets a name from the database.\n\n"

                ":param arg1: \\ :ref:`DB_NAME`\\ \n"
                ":type arg1: int\n"
                ":param arg2: name returned\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_reg_symb_setting_int", &GXDB_wrap_get_reg_symb_setting_int,
                "get_reg_symb_setting_int((int)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an integer-valued REG setting from a symbol reg\n\n"

                ":param arg1: Symbol, \\ :ref:`NULLSYMB`\\  for the database REG\n"
                ":type arg1: int\n"
                ":param arg2: REG entry name\n"
                ":type arg2: str\n"
                ":returns: The setting, or iDUMMY if not found or not convertable.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Same as \\ :func:`geosoft.gxapi.GXDB.get_reg_symb_setting`\\ , but converts\n"
                "   					the setting automatically to an integer value.\n"
                "   \n"
                "   					This is a convenient but low-performance way to get/set REG\n"
                "   					settings.  If performance is an issue, and more than one\n"
                "   					setting is to be Get and or Set, use the REG directly.\n"
                "   				\n\n"
               );
    pyClass.def("get_symb_name", &GXDB_wrap_get_symb_name,
                "get_symb_name((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method gets a symbol's name\n\n"

                ":param arg1: Symbol handle\n"
                ":type arg1: int\n"
                ":param arg2: string to place name into\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					See GetChanName_DB for more information\n"
                "   					The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n"
                "   				\n\n"
               );
    pyClass.def("have_itr", &GXDB_wrap_have_itr,
                "have_itr((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns TRUE if channel has an ITR.\n\n"

                ":param arg1: channel\n"
                ":type arg1: int\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If a channel has an ITR, the ITR colours are  used to\n"
                "   					display channel values in the spreadsheet.\n"
                "   \n"
                "   					If a channel does not have an ITR, \\ :func:`geosoft.gxapi.GXDB.get_itr`\\  will not change\n"
                "   					the passed ITR.\n"
                "   				\n\n"
               );
    pyClass.def("coord_pair", &GXDB_wrap_coord_pair,
                "coord_pair((str)arg1, (str_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the matching coordinate pair of a channel.\n\n"

                ":param arg1: channel name\n"
                ":type arg1: str\n"
                ":param arg2: string in which to place paired channel name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: \\ :ref:`DB_COORDPAIR`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the channel does not have a matching coordinate\n"
                "   					pair, or of the channel does not exist, the returned\n"
                "   					string will be empty.\n"
                "   				\n\n"
               );
    pyClass.def("lines_max", &GXDB_wrap_lines_max,
                "lines_max() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets Maximum number of lines in the database\n\n"

                ":returns: Maximum number of lines in the database\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("users_max", &GXDB_wrap_users_max,
                "users_max() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets Maximum number of Users\n\n"

                ":returns: Maximum number of Users\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("maker_symb", &GXDB_wrap_maker_symb,
                "maker_symb((int)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Adds a Maker to the database symbol\n\n"

                ":param arg1: Symbol to create maker for\n"
                ":type arg1: int\n"
                ":param arg2: Name of program\n"
                ":type arg2: str\n"
                ":param arg3: Maker name, used in menu prompt\n"
                ":type arg3: str\n"
                ":param arg4: INI groups (terminate each with a \";\")\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("put_chan_vv", &GXDB_wrap_put_chan_vv,
                "put_chan_vv((int)arg1, (int)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Place the contents of a VV in a channel.\n\n"

                ":param arg1: Line\n"
                ":type arg1: int\n"
                ":param arg2: Channel\n"
                ":type arg2: int\n"
                ":param arg3: VV from which to get the data\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If a VA channel is specified, then element [0] of this\n"
                "   					VA channel will be populated with the VV.\n"
                "   \n"
                "   					There is a limit of 2000 elements for non-licensed users.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXVV`\\  class.\n\n"
               );
    pyClass.def("put_va_chan_vv", &GXDB_wrap_put_va_chan_vv,
                "put_va_chan_vv((int)arg1, (int)arg2, (GXVV)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Place the contents of a VV at a specific part of a channel.\n\n"

                ":param arg1: Line\n"
                ":type arg1: int\n"
                ":param arg2: Channel\n"
                ":type arg2: int\n"
                ":param arg3: VV from which to get the data\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Offset\n"
                ":type arg4: int\n"
                ":param arg5: Number to Write\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If a VA channel is specified, then element [0] of this\n"
                "   					VA channel will be populated with the VV.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXVV`\\  class.\n\n"
               );
    pyClass.def("read_blob_bf", &GXDB_wrap_read_blob_bf,
                "read_blob_bf((int)arg1, (GXBF)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Read a blob from a database into a file.\n\n"

                ":param arg1: Blob (DB_SYMB_BLOB) to read into BF from database\n"
                ":type arg1: int\n"
                ":param arg2: File to read blob from\n"
                ":type arg2: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_chan_double", &GXDB_wrap_get_chan_double,
                "get_chan_double((int)arg1, (int)arg2, (int)arg3) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get individual elements in a channel.\n\n"

                ":param arg1: line\n"
                ":type arg1: int\n"
                ":param arg2: channel\n"
                ":type arg2: int\n"
                ":param arg3: index\n"
                ":type arg3: int\n"
                ":returns: Value, or dummy if out of range.\n"
                "          						For settings, terminates if error.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					These methods are slow and should only be used when\n"
                "   					performance is not an issue.\n"
                "   				\n\n"
               );
    pyClass.def("get_reg_symb_setting_double", &GXDB_wrap_get_reg_symb_setting_double,
                "get_reg_symb_setting_double((int)arg1, (str)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a real-valued REG setting from a symbol reg\n\n"

                ":param arg1: Symbol, \\ :ref:`NULLSYMB`\\  for the database REG\n"
                ":type arg1: int\n"
                ":param arg2: REG entry name\n"
                ":type arg2: str\n"
                ":returns: The setting, or rDUMMY if not found or not convertable.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Same as \\ :func:`geosoft.gxapi.GXDB.get_reg_symb_setting`\\ , but converts\n"
                "   					the setting automatically to a real value.\n"
                "   \n"
                "   					This is a convenient but low-performance way to get/set REG\n"
                "   					settings.  If performance is an issue, and more than one\n"
                "   					setting is to be Get and or Set, use the REG directly.\n"
                "   				\n\n"
               );
    pyClass.def("set_all_chan_protect", &GXDB_wrap_set_all_chan_protect,
                "set_all_chan_protect((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method sets all the channels' read-only protection status.\n\n"

                ":param arg1: \\ :ref:`DB_CHAN_PROTECTION`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Value to set must be either DB_CHAN_PROTECTED or\n"
                "   					DB_CHAN_UNPROTECTED\n"
                "   					This method does its own channel locking/unlocking.\n"
                "   					Channels already lock DB_LOCK_READONLY are ignored.\n"
                "   				\n\n"
               );
    pyClass.def("set_chan_class", &GXDB_wrap_set_chan_class,
                "set_chan_class((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a channel class\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":param arg2: class\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The channel class is stored in the \"CLASS\" parameter\n"
                "   					of the channel reg.\n"
                "   					The channel must be locked DB_LOCK_READWRITE\n"
                "   				\n\n"
               );
    pyClass.def("set_chan_decimal", &GXDB_wrap_set_chan_decimal,
                "set_chan_decimal((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method sets a channel's number of digits displayed\n"
                "   					to the right of the decimal point.\n"
                "   				\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":param arg2: Number of digits to display right of the decimal\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The number of display digits must be from 0 to 50.\n"
                "   					The channel must be locked DB_LOCK_READWRITE\n"
                "   				\n\n"
               );
    pyClass.def("set_chan_format", &GXDB_wrap_set_chan_format,
                "set_chan_format((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method sets a channel's display format.\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DB_CHAN_FORMAT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("set_chan_int", &GXDB_wrap_set_chan_int,
                "set_chan_int((int)arg1, (int)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set individual elements in a channel.\n\n"

                ":param arg1: line\n"
                ":type arg1: int\n"
                ":param arg2: channel\n"
                ":type arg2: int\n"
                ":param arg3: index\n"
                ":type arg3: int\n"
                ":param arg4: value\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					These methods are slow and should only be used when\n"
                "   					performance is not an issue.\n"
                "   				\n\n"
               );
    pyClass.def("set_chan_label", &GXDB_wrap_set_chan_label,
                "set_chan_label((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a channel label\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":param arg2: label\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The channel label is stored in the \"LABEL\" parameter\n"
                "   					of the channel reg.\n"
                "   					The channel must be locked DB_LOCK_READWRITE\n"
                "   				\n\n"
               );
    pyClass.def("set_chan_name", &GXDB_wrap_set_chan_name,
                "set_chan_name((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method sets a channel's name.\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":param arg2: string to set channel name to\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("set_chan_protect", &GXDB_wrap_set_chan_protect,
                "set_chan_protect((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method sets a channel's read-only protection\n"
                "   					status.\n"
                "   				\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DB_CHAN_PROTECTION`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Value to set must be either DB_CHAN_PROTECTED or\n"
                "   					DB_CHAN_UNPROTECTED\n"
                "   					The channel must be locked DB_LOCK_READWRITE\n"
                "   				\n\n"
               );
    pyClass.def("set_chan_double", &GXDB_wrap_set_chan_double,
                "set_chan_double((int)arg1, (int)arg2, (int)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set individual elements in a channel.\n\n"

                ":param arg1: line\n"
                ":type arg1: int\n"
                ":param arg2: channel\n"
                ":type arg2: int\n"
                ":param arg3: index\n"
                ":type arg3: int\n"
                ":param arg4: value\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					These methods are slow and should only be used when\n"
                "   					performance is not an issue.\n"
                "   				\n\n"
               );
    pyClass.def("set_chan_str", &GXDB_wrap_set_chan_str,
                "set_chan_str((int)arg1, (int)arg2, (int)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set individual elements in a channel.\n\n"

                ":param arg1: line\n"
                ":type arg1: int\n"
                ":param arg2: channel\n"
                ":type arg2: int\n"
                ":param arg3: index\n"
                ":type arg3: int\n"
                ":param arg4: string\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					These methods are slow and should only be used when\n"
                "   					performance is not an issue.\n"
                "   				\n\n"
               );
    pyClass.def("set_chan_unit", &GXDB_wrap_set_chan_unit,
                "set_chan_unit((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method sets a channel's unit for a\n"
                "   					given channel handle.\n"
                "   				\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":param arg2: string to put channel unit\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("set_chan_width", &GXDB_wrap_set_chan_width,
                "set_chan_width((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method sets a channel's display width\n\n"

                ":param arg1: Channel handle\n"
                ":type arg1: int\n"
                ":param arg2: Display width\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The number of display digits must be from 0 to 50.\n"
                "   					The channel must be locked DB_LOCK_READWRITE\n"
                "   				\n\n"
               );
    pyClass.def("set_ipj", &GXDB_wrap_set_ipj,
                "set_ipj((int)arg1, (int)arg2, (GXIPJ)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a REG object into a symbol\n\n"

                ":param arg1: X channel\n"
                ":type arg1: int\n"
                ":param arg2: Y channel\n"
                ":type arg2: int\n"
                ":param arg3: IPJ\n"
                ":type arg3: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_itr", &GXDB_wrap_set_itr,
                "set_itr((int)arg1, (GXITR)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set ITR for a channel.\n\n"

                ":param arg1: channel\n"
                ":type arg1: int\n"
                ":param arg2: ITR to fill in\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Use \\ :func:`geosoft.gxapi.GXITR.null()`\\  to clear the channel ITR.\n"
                "   					Channel must be locked for READONLY or READWRITE.\n"
                "   				\n\n"
               );
    pyClass.def("set_reg_symb", &GXDB_wrap_set_reg_symb,
                "set_reg_symb((int)arg1, (GXREG)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a REG object into a symbol\n\n"

                ":param arg1: Symbol, \\ :ref:`NULLSYMB`\\  for the database REG\n"
                ":type arg1: int\n"
                ":param arg2: REG to set into Blob\n"
                ":type arg2: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_reg_symb_setting", &GXDB_wrap_set_reg_symb_setting,
                "set_reg_symb_setting((int)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a REG string setting in a symbol reg\n\n"

                ":param arg1: Symbol, \\ :ref:`NULLSYMB`\\  for the database REG\n"
                ":type arg1: int\n"
                ":param arg2: REG entry name\n"
                ":type arg2: str\n"
                ":param arg3: setting\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The symbol REG is used to store a variety of attribute\n"
                "   					about the symbol.  Following a conventionally used entries:\n"
                "   \n"
                "   					UNITS                   - channel units\n"
                "   					CLASS                   - symbol class name (i.e. \"Assay\")\n"
                "   					_PJ_ipj                 - projection blob name\n"
                "   					_PJ_x                   - projection coordinate pair\n"
                "   					_PJ_y\n"
                "   					_PJ_name                - projection GXF-style info\n"
                "   					_PJ_ellipsoid\n"
                "   					_PJ_projection\n"
                "   					_PJ_units\n"
                "   					_PJ_datum_transform\n"
                "   \n"
                "   					This is a convenient but low-performance way to get/set REG\n"
                "   					settings.  If performance is an issue, and more than one\n"
                "   					setting is to be Get and or Set, use the REG directly.\n"
                "   				\n\n"
               );
    pyClass.def("write_blob_bf", &GXDB_wrap_write_blob_bf,
                "write_blob_bf((int)arg1, (GXBF)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write a blob from a file into a database.\n\n"

                ":param arg1: Blob (DB_SYMB_BLOB) to write into database from file\n"
                ":type arg1: int\n"
                ":param arg2: File to write blob into\n"
                ":type arg2: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("commit", &GXDB_wrap_commit,
                "commit() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method forces all changes to the database to be saved.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("compact", &GXDB_wrap_compact,
                "compact() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Removes any extra space from the database. This will\n"
                "   					reduce the database to its smallest size.\n"
                "   				\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("create", &GXDB_wrap_create,
                "create((str)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (str)arg7, (str)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method makes a brand new database of the specified size.\n"
                "   					The database is opened in ReadWrite Mode.\n"
                "   				\n\n"

                ":param arg1: name of the Database File to Create\n"
                ":type arg1: str\n"
                ":param arg2: Max Lines in the Database    (200)\n"
                ":type arg2: int\n"
                ":param arg3: Max Channels in the Database (50)\n"
                ":type arg3: int\n"
                ":param arg4: Max Blobs in the Database    (Channels+Lines+20)\n"
                ":type arg4: int\n"
                ":param arg5: Max Users in the Database    (10)\n"
                ":type arg5: int\n"
                ":param arg6: Number of Erase Caches       (100)\n"
                ":type arg6: int\n"
                ":param arg7: Name of the Super User       \"SUPER\"\n"
                ":type arg7: str\n"
                ":param arg8: Password of the Super User   \"\"\n"
                ":type arg8: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_comp", &GXDB_wrap_create_comp,
                "create_comp((str)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (str)arg7, (str)arg8, (int)arg9, (int)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method makes a brand new database of the specified size.\n"
                "   					The database is opened in ReadWrite Mode. Also allows you to\n"
                "   					set paging size and the Compression Level.\n"
                "   				\n\n"

                ":param arg1: name of the Database File to Create\n"
                ":type arg1: str\n"
                ":param arg2: Max Lines in the Database    (200)\n"
                ":type arg2: int\n"
                ":param arg3: Max Channels in the Database (50)\n"
                ":type arg3: int\n"
                ":param arg4: Max Blobs in the Database    (Channels+Lines+20)\n"
                ":type arg4: int\n"
                ":param arg5: Max Users in the Database    (10)\n"
                ":type arg5: int\n"
                ":param arg6: Number of Erase Caches       (100)\n"
                ":type arg6: int\n"
                ":param arg7: Name of the Super User       \"SUPER\"\n"
                ":type arg7: str\n"
                ":param arg8: Password of the Super User   \"\"\n"
                ":type arg8: str\n"
                ":param arg9: Page Size Must be (64,128,256,512,1024,2048,4096) normally 1024\n"
                ":type arg9: int\n"
                ":param arg10: \\ :ref:`DB_COMP`\\ \n"
                ":type arg10: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_comp");
    pyClass.def("create_ex", &GXDB_wrap_create_ex,
                "create_ex((str)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (str)arg7, (str)arg8, (int)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method makes a brand new database of the specified size.\n"
                "   					The database is opened in ReadWrite Mode. Also allows you to\n"
                "   					set paging size.\n"
                "   				\n\n"

                ":param arg1: name of the Database File to Create\n"
                ":type arg1: str\n"
                ":param arg2: Max Lines in the Database    (200)\n"
                ":type arg2: int\n"
                ":param arg3: Max Channels in the Database (50)\n"
                ":type arg3: int\n"
                ":param arg4: Max Blobs in the Database    (Channels+Lines+20)\n"
                ":type arg4: int\n"
                ":param arg5: Max Users in the Database    (10)\n"
                ":type arg5: int\n"
                ":param arg6: Number of Erase Caches       (100)\n"
                ":type arg6: int\n"
                ":param arg7: Name of the Super User       \"SUPER\"\n"
                ":type arg7: str\n"
                ":param arg8: Password of the Super User   \"\"\n"
                ":type arg8: str\n"
                ":param arg9: Page Size Must be (64,128,256,512,1024,2048,4096) normally 1024\n"
                ":type arg9: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_ex");
    pyClass.def("del_line0", &GXDB_wrap_del_line0,
                "del_line0() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete Empty Line 0.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A new database is created with a single, empty line L0, but many processes\n"
                "   					create databases then create their own lines, so the empty line L0 may remain\n"
                "   					after the process finishes. This function will delete a line L0\n"
                "   					a) If it exists and is empty\n"
                "   					b) It is not the only line in the database.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXEDB.del_line0`\\  - deletes an empty line 0 from the currently edited database.\n\n"
               );
    pyClass.def("discard", &GXDB_wrap_discard,
                "discard() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method discards all changes made to the database since\n"
                "   					the last commit or opening.\n"
                "   				\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("grow", &GXDB_wrap_grow,
                "grow((str)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Enlarges the database.\n\n"

                ":param arg1: name of the Database File to Create\n"
                ":type arg1: str\n"
                ":param arg2: Max Lines in the Database    (200)\n"
                ":type arg2: int\n"
                ":param arg3: Max Channels in the Database (50)\n"
                ":type arg3: int\n"
                ":param arg4: Max Blobs in the Database    (Channels+Lines+20)\n"
                ":type arg4: int\n"
                ":param arg5: Max Users in the Database    (10)\n"
                ":type arg5: int\n"
                ":param arg6: Number of Erase Caches       (100)\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               ).staticmethod("grow");
    pyClass.def("can_open", &GXDB_wrap_can_open,
                "can_open((str)arg1, (str)arg2, (str)arg3) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   This method checks whether it is possible to open a database.\n\n"

                ":param arg1: name of the Database File to Open\n"
                ":type arg1: str\n"
                ":param arg2: Name of the user (\"SUPER\" normally)\n"
                ":type arg2: str\n"
                ":param arg3: Password of the user (\"\" normally)\n"
                ":type arg3: str\n"
                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method is useful to determine if another session already locked a database.\n"
                "   					By using this method before an \\ :func:`geosoft.gxapi.GXDB.open`\\  a GX may handle errors like this more gracefully.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDB.open`\\ , \\ :func:`geosoft.gxapi.GXDB.open_read_only`\\ , \\ :func:`geosoft.gxapi.GXDB.can_open_read_only`\\ \n\n"
               ).staticmethod("can_open");
    pyClass.def("can_open_read_only", &GXDB_wrap_can_open_read_only,
                "can_open_read_only((str)arg1, (str)arg2, (str)arg3) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   This method checks whether it is possible to open a database in read-only mode.\n\n"

                ":param arg1: name of the Database File to Open\n"
                ":type arg1: str\n"
                ":param arg2: Name of the user (\"SUPER\" normally)\n"
                ":type arg2: str\n"
                ":param arg3: Password of the user (\"\" normally)\n"
                ":type arg3: str\n"
                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 6.4.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method is useful to determine if another session already locked a database.\n"
                "   					By using this method before an \\ :func:`geosoft.gxapi.GXDB.open_read_only`\\  a GX may handle errors like this more gracefully.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDB.open`\\ , \\ :func:`geosoft.gxapi.GXDB.open_read_only`\\ , \\ :func:`geosoft.gxapi.GXDB.can_open`\\ \n\n"
               ).staticmethod("can_open_read_only");
    pyClass.def("check", &GXDB_wrap_check,
                "check() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Does an integrity check of the data in the database to\n"
                "   					ensure it is valid.\n"
                "   				\n\n"

                ":returns: 0 - Ok\n"
                "          						1 - Invalid Blocks in the Database\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               );
    pyClass.def("is_empty", &GXDB_wrap_is_empty,
                "is_empty() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   See if a database contains only empty lines.\n\n"

                ":returns: 1 if the database contains only empty lines.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function does not check for other information or blobs,\n"
                "   					it merely looks at all lines in the database to see if they\n"
                "   					are empty. If all are empty, it returns 1.\n"
                "   				\n\n"
               );
    pyClass.def("is_line_empty", &GXDB_wrap_is_line_empty,
                "is_line_empty((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   See if a specific line in the database is empty.\n\n"

                ":param arg1: Line symbol\n"
                ":type arg1: int\n"
                ":returns: 1 if the database contains only empty lines.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               );
    pyClass.def("open", &GXDB_wrap_open,
                "open((str)arg1, (str)arg2, (str)arg3) -> GXDB:\n"

                "\n.. parsed-literal::\n\n"
                "   This method opens a database.\n\n"

                ":param arg1: name of the Database File to Open\n"
                ":type arg1: str\n"
                ":param arg2: Name of the user (\"SUPER\" normally)\n"
                ":type arg2: str\n"
                ":param arg3: Password of the user (\"\" normally)\n"
                ":type arg3: str\n"
                ":returns: DB Object\n"
                ":rtype: :class:`geosoft.gxapi.GXDB`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDB.open_read_only`\\ , \\ :func:`geosoft.gxapi.GXDB.can_open`\\ , \\ :func:`geosoft.gxapi.GXDB.can_open_read_only`\\ \n\n"
               ).staticmethod("open");
    pyClass.def("open_read_only", &GXDB_wrap_open_read_only,
                "open_read_only((str)arg1, (str)arg2, (str)arg3) -> GXDB:\n"

                "\n.. parsed-literal::\n\n"
                "   This method opens a database.\n\n"

                ":param arg1: name of the Database File to Open\n"
                ":type arg1: str\n"
                ":param arg2: Name of the user (\"SUPER\" normally)\n"
                ":type arg2: str\n"
                ":param arg3: Password of the user (\"\" normally)\n"
                ":type arg3: str\n"
                ":returns: DB Object\n"
                ":rtype: :class:`geosoft.gxapi.GXDB`\n"
                "\n"

                "\n.. versionadded:: 6.4.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method is useful to open multiple reader instances on the same database. This call will fail\n"
                "   					if a DB has already been opened with \\ :func:`geosoft.gxapi.GXDB.open`\\  or locked in the application with \\ :func:`geosoft.gxapi.GXEDB.lock`\\ .\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDB.open`\\ , \\ :func:`geosoft.gxapi.GXDB.can_open`\\ , \\ :func:`geosoft.gxapi.GXDB.can_open_read_only`\\ \n\n"
               ).staticmethod("open_read_only");
    pyClass.def("repair", &GXDB_wrap_repair,
                "repair((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Cleans the database by removing invalid blocks\n\n"

                ":param arg1: name of the Database File to Create\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               ).staticmethod("repair");
    pyClass.def("sync", &GXDB_wrap_sync,
                "sync() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Syncronize the Metadata from this database to the XML\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("copy_data", &GXDB_wrap_copy_data,
                "copy_data((int)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method copies the data from one channel to another on\n"
                "   					on the specified line. The data is converted if such\n"
                "   					conversion in neccessary.\n"
                "   				\n\n"

                ":param arg1: Line\n"
                ":type arg1: int\n"
                ":param arg2: Channel to Copy Data From\n"
                ":type arg2: int\n"
                ":param arg3: Channel to Copy Data To\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					All the data in the destination channel is destroyed along\n"
                "   					with the fiducial start and increment.\n"
                "   				\n\n"
               );
    pyClass.def("get_col_va", &GXDB_wrap_get_col_va,
                "get_col_va((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the # of columns in a VA channel.\n\n"

                ":param arg1: Channel (read locked)\n"
                ":type arg1: int\n"
                ":returns: # of columns\n"
                "          						0 if error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the channel is VV, this function returns 1.\n\n"
               );
    pyClass.def("get_channel_length", &GXDB_wrap_get_channel_length,
                "get_channel_length((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the # of elements in a channel.\n\n"

                ":param arg1: Line    (read or write locked)\n"
                ":type arg1: int\n"
                ":param arg2: Channel (read or write locked)\n"
                ":type arg2: int\n"
                ":returns: # of elements\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns the actual number of data items (rows) in a channel. For VA channels no correction is\n"
                "   					necessary for the number of columns (which was true of the obsoleted function \\ :func:`geosoft.gxapi.GXDB.get_length`\\ ).\n"
                "   				\n\n"
               );
    pyClass.def("get_fid_incr", &GXDB_wrap_get_fid_incr,
                "get_fid_incr((int)arg1, (int)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method returns the fiducial increment value of a\n"
                "   					specified Channel.\n"
                "   				\n\n"

                ":param arg1: Line (read or write locked)\n"
                ":type arg1: int\n"
                ":param arg2: Channel (read locked)\n"
                ":type arg2: int\n"
                ":returns: Fiducial Start.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_fid_start", &GXDB_wrap_get_fid_start,
                "get_fid_start((int)arg1, (int)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method returns the fiducial start value of a\n"
                "   					specified Channel.\n"
                "   				\n\n"

                ":param arg1: Line (read or write locked)\n"
                ":type arg1: int\n"
                ":param arg2: Channel (read locked)\n"
                ":type arg2: int\n"
                ":returns: Fiducial Start.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_fid", &GXDB_wrap_set_fid,
                "set_fid((int)arg1, (int)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method allows the user to set the fiducial start and\n"
                "   					increment of a channel. The Increment should never be 0.\n"
                "   				\n\n"

                ":param arg1: Line (read or write locked)\n"
                ":type arg1: int\n"
                ":param arg2: Channel to set fiducial (write locked)\n"
                ":type arg2: int\n"
                ":param arg3: Start Fiducial Value\n"
                ":type arg3: float\n"
                ":param arg4: Increment Fiducial Value\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("window_va_ch", &GXDB_wrap_window_va_ch,
                "window_va_ch((int)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a window of data in a channel into a new channel\n\n"

                ":param arg1: Line symbol\n"
                ":type arg1: int\n"
                ":param arg2: Original channel\n"
                ":type arg2: int\n"
                ":param arg3: Output channel\n"
                ":type arg3: int\n"
                ":param arg4: Start column number to copy, 0 is first column\n"
                ":type arg4: int\n"
                ":param arg5: End column number to copy\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function normally used for VA channels. A copy of the\n"
                "   					original channel will be made if start and end column\n"
                "   					numbers to copy are dummies.\n"
                "   					All the columns including start and end columns will be copied\n"
                "   				\n\n"
               );
    pyClass.def("window_va_ch2", &GXDB_wrap_window_va_ch2,
                "window_va_ch2((int)arg1, (int)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a windowed version of data in a channel into a new channel\n\n"

                ":param arg1: Line symbol\n"
                ":type arg1: int\n"
                ":param arg2: Original channel\n"
                ":type arg2: int\n"
                ":param arg3: Output channel\n"
                ":type arg3: int\n"
                ":param arg4: VV containing 0/1 values for each channel.\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Similar to \\ :func:`geosoft.gxapi.GXDB.window_va_ch`\\ , but the input and output channels must\n"
                "   					contain the same number of columns. The input VV tells which columns\n"
                "   					to copy over; 0 values indicate that the output column is to be\n"
                "   					dummied, and non-zero values indicate the column is to be copied.\n"
                "   					The VV length must be the same as the number of columns.\n"
                "   				\n\n"
               );
    pyClass.def("set_line_selection", &GXDB_wrap_set_line_selection,
                "set_line_selection((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Set the selection status for a line.\n"
                "   				\n\n"

                ":param arg1: Handle of line to select/deselect\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DB_LINE_SELECT`\\ \n"
                ":type arg2: int\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               );
    pyClass.def("get_line_selection", &GXDB_wrap_get_line_selection,
                "get_line_selection((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Get the selection status for a line.\n"
                "   				\n\n"

                ":param arg1: Line handle\n"
                ":type arg1: int\n"
                ":returns: One of \\ :ref:`DB_LINE_SELECT`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               );
    pyClass.def("first_sel_line", &GXDB_wrap_first_sel_line,
                "first_sel_line() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method will return a handle to the first selected\n"
                "   					line in the database.\n"
                "   				\n\n"

                ":returns: Line Handle (use iIsLineValid method to see if valid)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_line_map_fid", &GXDB_wrap_get_line_map_fid,
                "get_line_map_fid((int)arg1, (float_ref)arg2, (float_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method gets a line map clip fiducial.\n\n"

                ":param arg1: Line handle to look at\n"
                ":type arg1: int\n"
                ":param arg2: Start Fid\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: End Fid\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("get_select", &GXDB_wrap_get_select,
                "get_select() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the Line Selections.\n\n"

                ":returns: Selections Object.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("count_sel_lines", &GXDB_wrap_count_sel_lines,
                "count_sel_lines() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method counts the number of selected lines in\n"
                "   					the database.\n"
                "   				\n\n"

                ":returns: x - Number of selected lines in the database\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("is_chan_name", &GXDB_wrap_is_chan_name,
                "is_chan_name((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this a valid channel name?\n\n"

                ":param arg1: Name to test\n"
                ":type arg1: str\n"
                ":returns: 1 if it is a valid channel name\n"
                "          						0 if it is not a valid channel name\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Channel names must only contain alpha-numeric characters or the\n"
                "   					underscore character \"_\", and the first letter must be a letter\n"
                "   					or an underscore.\n"
                "   				\n\n"
               ).staticmethod("is_chan_name");
    pyClass.def("is_chan_valid", &GXDB_wrap_is_chan_valid,
                "is_chan_valid((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method checks to see if the channel handle is a\n"
                "   					valid channel.\n"
                "   				\n\n"

                ":param arg1: Channel handle to check\n"
                ":type arg1: int\n"
                ":returns: 0 - Not a valid channel\n"
                "          						1 - Valid\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("is_line_name", &GXDB_wrap_is_line_name,
                "is_line_name((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this a valid line name.\n\n"

                ":param arg1: Name to test\n"
                ":type arg1: str\n"
                ":returns: 1 if it is a valid line name\n"
                "          						0 if it is not a valid line name\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("is_line_name");
    pyClass.def("is_line_valid", &GXDB_wrap_is_line_valid,
                "is_line_valid((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method checks to see if the line handle returned by\n"
                "   					the Line methods is a valid line.\n"
                "   				\n\n"

                ":param arg1: Line handle to check\n"
                ":type arg1: int\n"
                ":returns: 0 - Not a valid line\n"
                "          						1 - Valid\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("line_category", &GXDB_wrap_line_category,
                "line_category((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the category (group, line) of a line.\n\n"

                ":param arg1: Line handle to look at\n"
                ":type arg1: int\n"
                ":returns: \\ :ref:`DB_CATEGORY_LINE`\\  or iDUMMY.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("line_flight", &GXDB_wrap_line_flight,
                "line_flight((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the flight number of a line.\n\n"

                ":param arg1: Line handle to look at\n"
                ":type arg1: int\n"
                ":returns: Line Flight Number.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("line_label", &GXDB_wrap_line_label,
                "line_label((int)arg1, (str_ref)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a line label\n\n"

                ":param arg1: line symbol\n"
                ":type arg1: int\n"
                ":param arg2: string in which to place label\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: \\ :ref:`DB_LINE_LABEL_FORMAT`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Label formats.\n"
                "   \n"
                "   					example full format is\n"
                "   					\"L1023.4 13\"   type \"L\"\n"
                "   					number \"1023\"\n"
                "   					version \"4\"\n"
                "   					flight \"13\"\n"
                "   \n"
                "   					formats can be added to get combined format\n"
                "   \n"
                "   					Use LINK format to create a database link label.\n"
                "   				\n\n"
               );
    pyClass.def("line_number", &GXDB_wrap_line_number,
                "line_number((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the number of a line.\n\n"

                ":param arg1: Line handle to look at\n"
                ":type arg1: int\n"
                ":returns: Line Number.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("line_number2", &GXDB_wrap_line_number2,
                "line_number2((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the string form of the line number (can be alphanumeric)\n\n"

                ":param arg1: Line handle to look at\n"
                ":type arg1: int\n"
                ":param arg2: Line number\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("line_type", &GXDB_wrap_line_type,
                "line_type((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the type of a line.\n\n"

                ":param arg1: Line handle to look at\n"
                ":type arg1: int\n"
                ":returns: \\ :ref:`DB_LINE_TYPE`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("line_version", &GXDB_wrap_line_version,
                "line_version((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the version number of a line.\n\n"

                ":param arg1: Line handle to look at\n"
                ":type arg1: int\n"
                ":returns: Line Number.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("set_line_name", &GXDB_wrap_set_line_name,
                "set_line_name((int)arg1, (int)arg2, (int)arg3, (str_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method sets up a line name given the line's number,\n"
                "   					type, and version.\n"
                "   				\n\n"

                ":param arg1: Line number\n"
                ":type arg1: int\n"
                ":param arg2: Line type\n"
                ":type arg2: int\n"
                ":param arg3: Line version\n"
                ":type arg3: int\n"
                ":param arg4: String to set line name to\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This MUST be called to generate a line name when calls\n"
                "   					are made to \\ :func:`geosoft.gxapi.GXDB.exist_symb`\\ , \\ :func:`geosoft.gxapi.GXDB.create_symb`\\  or \\ :func:`geosoft.gxapi.GXDB.delete_symb`\\ \n"
                "   					for an operation on a line.\n"
                "   					See also SetLineName2_DB.\n"
                "   				\n\n"
               ).staticmethod("set_line_name");
    pyClass.def("set_line_name2", &GXDB_wrap_set_line_name2,
                "set_line_name2((str)arg1, (int)arg2, (int)arg3, (str_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Like SetLineName_DB, but can use alphanumeric for line number\n\n"

                ":param arg1: Line number (alphanumeric)\n"
                ":type arg1: str\n"
                ":param arg2: Line type\n"
                ":type arg2: int\n"
                ":param arg3: Line version\n"
                ":type arg3: int\n"
                ":param arg4: String to set line name to\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This MUST be called to generate a line name when calls\n"
                "   					are made to \\ :func:`geosoft.gxapi.GXDB.exist_symb`\\ , \\ :func:`geosoft.gxapi.GXDB.create_symb`\\  or \\ :func:`geosoft.gxapi.GXDB.delete_symb`\\ \n"
                "   					for an operation on a line.\n"
                "   					The line number can be any combination of letters and numbers,\n"
                "   					i.e. XU324, 98765, A, 23NGV etc.\n"
                "   				\n\n"
               ).staticmethod("set_line_name2");
    pyClass.def("load_select", &GXDB_wrap_load_select,
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
    pyClass.def("next_sel_line", &GXDB_wrap_next_sel_line,
                "next_sel_line((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method will advance to the next selected line based\n"
                "   					on the currently selected line handle.\n"
                "   				\n\n"

                ":param arg1: Previous Line\n"
                ":type arg1: int\n"
                ":returns: Line Handle (use iIsLineValid method to see if valid).\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("line_bearing", &GXDB_wrap_line_bearing,
                "line_bearing((int)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the bearing of a line.\n\n"

                ":param arg1: Line handle to look at\n"
                ":type arg1: int\n"
                ":returns: Bearing value, rDUMMY if not set.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n"
                "   \n"
                "   					This function simply returns a value set using the \\ :func:`geosoft.gxapi.GXDB.set_line_bearing`\\ \n"
                "   					function. It returns rDUMMY for line categories other than\n"
                "   					DB_CATEGORY_LINE_FLIGHT.\n"
                "   \n"
                "   					To calculate the line azimuth based on the first and\n"
                "   					last non-dummy locations, use the \\ :func:`geosoft.gxapi.GXDU.direction`\\  function.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDB.set_line_bearing`\\ , \\ :func:`geosoft.gxapi.GXDU.direction`\\ \n\n"
               );
    pyClass.def("line_date", &GXDB_wrap_line_date,
                "line_date((int)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the date of a line.\n\n"

                ":param arg1: Line handle to look at\n"
                ":type arg1: int\n"
                ":returns: Date value.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READONLY or DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("save_select", &GXDB_wrap_save_select,
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
    pyClass.def("select", &GXDB_wrap_select,
                "select((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Select/deselect lines based on selection string\n\n"

                ":param arg1: Selection\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DB_LINE_SELECT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Selections/deselections are cumulative. If lines had already\n"
                "   					been selected, then any further selection/deselection will\n"
                "   					affect that set of selections.\n"
                "   \n"
                "   					E.g. \"L99:800\" is the string to select all normal lines from\n"
                "   					99 to 800. If \\ :func:`geosoft.gxapi.GXDB.select`\\  is called again to select \"L1000\",\n"
                "   					then lines 99 to 800 and 1000 would all be selected.\n"
                "   \n"
                "   					Use a \"T\" prefix for Tie lines.\n"
                "   					Use an \"F\" prefix to specify lines of a specific flight.\n"
                "   					E.g. \"F10\" would select all lines of flight 10.\n"
                "   					Use an empty string (\"\") to select/deselect ALL lines.\n"
                "   				\n\n"
               );
    pyClass.def("set_line_bearing", &GXDB_wrap_set_line_bearing,
                "set_line_bearing((int)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets a line's bearing.\n\n"

                ":param arg1: Line handle\n"
                ":type arg1: int\n"
                ":param arg2: Value to set bearing to\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The channel must be locked DB_LOCK_READWRITE\n"
                "   \n"
                "   					This function simply sets a value in the line's metadata\n"
                "   					that is retrieved using the \\ :func:`geosoft.gxapi.GXDB.line_bearing`\\ \n"
                "   					function. It terminates for line categories other than\n"
                "   					DB_CATEGORY_LINE_FLIGHT.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDB.line_bearing`\\ , \\ :func:`geosoft.gxapi.GXDU.direction`\\ \n\n"
               );
    pyClass.def("set_line_date", &GXDB_wrap_set_line_date,
                "set_line_date((int)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method sets a line's date.\n\n"

                ":param arg1: Line handle\n"
                ":type arg1: int\n"
                ":param arg2: Value to set date to\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("set_line_flight", &GXDB_wrap_set_line_flight,
                "set_line_flight((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method sets a line's flight.\n\n"

                ":param arg1: Line handle\n"
                ":type arg1: int\n"
                ":param arg2: Value to set line flight to\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("set_line_map_fid", &GXDB_wrap_set_line_map_fid,
                "set_line_map_fid((int)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method changes a line map clip fiducial.\n\n"

                ":param arg1: Line handle to look at\n"
                ":type arg1: int\n"
                ":param arg2: Start Fid\n"
                ":type arg2: float\n"
                ":param arg3: End Fid\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					for full range, set Start Fid to rMIN and End Fid to rMAX.\n"
                "   					for no data, set Start and End Fids to rDUMMY.\n"
                "   				\n\n"
               );
    pyClass.def("set_line_num", &GXDB_wrap_set_line_num,
                "set_line_num((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method sets a line's number.\n\n"

                ":param arg1: Line handle\n"
                ":type arg1: int\n"
                ":param arg2: Value to set line number to\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("set_line_type", &GXDB_wrap_set_line_type,
                "set_line_type((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method sets a line's type.\n\n"

                ":param arg1: Line handle\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DB_LINE_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("set_line_ver", &GXDB_wrap_set_line_ver,
                "set_line_ver((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method sets a line's version.\n\n"

                ":param arg1: Line handle\n"
                ":type arg1: int\n"
                ":param arg2: Value to set line version to\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The channel must be locked DB_LOCK_READWRITE\n\n"
               );
    pyClass.def("set_select", &GXDB_wrap_set_select,
                "set_select((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the Line Selections.\n\n"

                ":param arg1: Selections\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This method also destroys the DB_SELECT object.\n\n"
               );
    pyClass.def("get_meta", &GXDB_wrap_get_meta,
                "get_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the metadata of a database.\n\n"

                ":param arg1: Meta object to fill with database's meta\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"
               );
    pyClass.def("set_meta", &GXDB_wrap_set_meta,
                "set_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the metadata of a database.\n\n"

                ":param arg1: Meta object to add to database's meta\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"
               );
    pyClass.def("array_lst", &GXDB_wrap_array_lst,
                "array_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LST object with array (VA) channel symbols.\n\n"

                ":param arg1: List to Populate\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("array_size_lst", &GXDB_wrap_array_size_lst,
                "array_size_lst((int)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LST object with array (VA) channel symbols with a particular number of columns.\n\n"

                ":param arg1: Number of columns in array ( > 1 )\n"
                ":type arg1: int\n"
                ":param arg2: List to Populate\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"
               );
    pyClass.def("chan_lst", &GXDB_wrap_chan_lst,
                "chan_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LST with database channels.\n\n"

                ":param arg1: List to Populate\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Populates a LST with channel symbols.\n"
                "   					The name is put into the \"Name\" part of the LST (0),\n"
                "   					and the handle, an integer value written as a string, is\n"
                "   					placed in the value part of the LST (1).\n"
                "   					Array channels are included, as well as virtual channels (array channel single columns loaded in the database like \\\"Chan[1]\\\".\n"
                "   \n"
                "   					The LST is cleared first, and the items are sorted by name.\n"
                "   				\n\n"
               );
    pyClass.def("normal_chan_lst", &GXDB_wrap_normal_chan_lst,
                "normal_chan_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LST with non-array database channels.\n\n"

                ":param arg1: List to Populate\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Like \\ :func:`geosoft.gxapi.GXDB.chan_lst`\\ , but does not include array channels or virtual channels.\n\n"
               );
    pyClass.def("class_chan_lst", &GXDB_wrap_class_chan_lst,
                "class_chan_lst((GXLST)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LST with channels in a particular class.\n\n"

                ":param arg1: LST object to populate\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: CLASS name for the channel (\"\" for all)\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The Name of the symbol is placed in the\n"
                "   					item name and the item value is set to the symbol handle.\n"
                "   					Only channels with the given class name are included,\n"
                "   					e.g. use \"ASSAY\" for assay channels in CHIMERA.\n"
                "   \n"
                "   					The LST is cleared first, and the items are sorted by name.\n"
                "   				\n\n"
               );
    pyClass.def("class_group_lst", &GXDB_wrap_class_group_lst,
                "class_group_lst((GXLST)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LST with group lines in a particular class.\n\n"

                ":param arg1: LST object to populate\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: CLASS name for the group (\"\" for all)\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The Name of the symbol is placed in the\n"
                "   					item name and the item value is set to the symbol handle.\n"
                "   					Only group lines with the given class name are included,\n"
                "   					e.g. use \"TARGETS\" for UX-Detect Target groups.\n"
                "   \n"
                "   					The LST is cleared first, and the items are sorted by name.\n"
                "   				\n\n"
               );
    pyClass.def("create_symb", &GXDB_wrap_create_symb,
                "create_symb((str)arg1, (int)arg2, (int)arg3, (int)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new Symbol.\n\n"

                ":param arg1: Symbol Name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DB_SYMB_TYPE`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`DB_OWN`\\ \n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`DB_CATEGORY_USER`\\ , \\ :ref:`DB_CATEGORY_LINE`\\ , \\ :ref:`DB_CATEGORY_CHAN`\\ , \\ :ref:`DB_CATEGORY_BLOB`\\ \n"
                ":type arg4: int\n"
                ":returns: DB_SYMB Object\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If symbol already exits, and it is the same type\n"
                "   					simply returns a handle to the existing symbol.\n"
                "   \n"
                "   					This method simple calls \\ :func:`geosoft.gxapi.GXDB.create_symb_ex`\\  with the\n"
                "   					extra info set to 1.\n"
                "   \n"
                "   					STRING-type channels: To create a string-type channel,\n"
                "   					enter a negative number for the channel category below.\n"
                "   					For instance, \"-32\" will create a string channel with\n"
                "   					32 characters per item.\n"
                "   \n"
                "   					BLOBS: Blobs (Binary Large Objects) can be used for storing\n"
                "   					miscellaneous data which does not fit well into any of the\n"
                "   					other various storage objects, such as a REG. Generally,\n"
                "   					one or more objects is serialized to a BF object, which\n"
                "   					is then written to the blob using the sWriteBlobBF_DB()\n"
                "   					function. Retrieval is done in the reverse order, using\n"
                "   					sWriteBlobBF_DB() first, then extracting the objects from the\n"
                "   					BF object.\n"
                "   					To avoid namespace problems, Geosoft reserves the following\n"
                "   					name prefixes:\n"
                "   \n"
                "   					OE.   (Core functions)\n"
                "   					GS.   (Applications)\n"
                "   					CS.   (Custom Solutions applications)\n"
                "   \n"
                "   					Programmers should avoid using the above prefixes as the starting\n"
                "   					letters of their blob names to avoid any possible conflicts.\n"
                "   				\n\n"
               );
    pyClass.def("create_symb_ex", &GXDB_wrap_create_symb_ex,
                "create_symb_ex((str)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new Symbol.\n\n"

                ":param arg1: Symbol Name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DB_SYMB_TYPE`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`DB_OWN`\\ \n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`DB_CATEGORY_USER`\\ , \\ :ref:`DB_CATEGORY_LINE`\\ , \\ :ref:`DB_CATEGORY_CHAN`\\ , \\ :ref:`DB_CATEGORY_BLOB`\\ \n"
                ":type arg4: int\n"
                ":param arg5: Extra info, which depends on \\ :ref:`DB_SYMB_TYPE`\\  DB_SYMB_CHAN - element width for a VA channel ignores for all other \\ :ref:`DB_SYMB_TYPE`\\  types\n"
                ":type arg5: int\n"
                ":returns: DB_SYMB handle.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If symbol already exits it is returned.\n"
                "   \n"
                "   					STRING-type channels: To create a string-type channel,\n"
                "   					enter a negative number for the channel category below.\n"
                "   					For instance, \"-32\" will create a string channel with\n"
                "   					32 characters per item.\n"
                "   \n"
                "   					Symbol name for DB_CATEGORY_LINE_FLIGHT must conform to\n"
                "   					the following line naming syntax:\n"
                "   \n"
                "   					[type][number.version:flight]\n"
                "   \n"
                "   					Type can be: L - normal line\n"
                "   					B - base line\n"
                "   					T - tie line\n"
                "   					R - trend line\n"
                "   					S - test line\n"
                "   					P - special line\n"
                "   \n"
                "   					Examples: L100,\n"
                "   					T100.1:16\n"
                "   \n"
                "   					Note the \"Flight\" is any whole number that may be useful\n"
                "   					to differentiate processing tasks.\n"
                "   \n"
                "   					The ability to create a VA channel is not available in the\n"
                "   					free interface and requires a Montaj license.\n"
                "   				\n\n"
               );
    pyClass.def("csv_chan_lst", &GXDB_wrap_csv_chan_lst,
                "csv_chan_lst((GXLST)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LST with channels in a comma-separated list.\n\n"

                ":param arg1: LST object to populate\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: comma-separated list of channels\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The Name of the symbol is placed in the\n"
                "   					item name and the item value is set to the symbol handle.\n"
                "   					Only channels in the list which are present in the database\n"
                "   					are included.\n"
                "   \n"
                "   					The LST is cleared first.\n"
                "   				\n\n"
               );
    pyClass.def("delete_symb", &GXDB_wrap_delete_symb,
                "delete_symb((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method destroys a symbol in the database and all\n"
                "   					the data associated with it. The symbol's lock is\n"
                "   					automatically removed.\n"
                "   				\n\n"

                ":param arg1: Symbol to Delete (must be READWRITE locked)\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("dup_line_symb", &GXDB_wrap_dup_line_symb,
                "dup_line_symb((int)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Duplicate a line symbol from a group or line symbol.\n"
                "   					The new name must not already exist in the database.\n"
                "   				\n\n"

                ":param arg1: Symbol Handle to duplicate\n"
                ":type arg1: int\n"
                ":param arg2: Name of the New Symbol\n"
                ":type arg2: str\n"
                ":returns: New Symbol Handle\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("dup_symb", &GXDB_wrap_dup_symb,
                "dup_symb((int)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   New Symbol by duplicating an existing symbol, LOCKED\n\n"

                ":param arg1: Symbol Handle to duplicate\n"
                ":type arg1: int\n"
                ":param arg2: Name of the New Symbol\n"
                ":type arg2: str\n"
                ":returns: New Symbol Handle\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The symbol will be locked READWRITE.\n"
                "   					The new name must not already exist in the database.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDB.dup_symb_no_lock`\\ \n\n"
               );
    pyClass.def("dup_symb_no_lock", &GXDB_wrap_dup_symb_no_lock,
                "dup_symb_no_lock((int)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   New Symbol by duplicating an existing symbol, NO LOCK.\n\n"

                ":param arg1: Symbol Handle to duplicate\n"
                ":type arg1: int\n"
                ":param arg2: Name of the New Symbol\n"
                ":type arg2: str\n"
                ":returns: New Symbol Handle\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The symbol will be NOT be locked.\n"
                "   					The new name must not already exist in the database.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDB.dup_symb`\\ \n\n"
               );
    pyClass.def("find_chan", &GXDB_wrap_find_chan,
                "find_chan((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get handle to the specified channel.\n\n"

                ":param arg1: Name of channel\n"
                ":type arg1: str\n"
                ":returns: Channel Handle, \\ :ref:`NULLSYMB`\\  if not defined\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					To work with a specific column from a VA channel,\n"
                "   					specify the VA element number in square brackets as part\n"
                "   					of the VA channel name (e.g. \"EM[3]\" will treat the fourth\n"
                "   					column of the VA channel as a VV).\n"
                "   \n"
                "   					See notes for \\ :func:`geosoft.gxapi.GXDB.find_symb`\\ .\n"
                "   					Introduced in v5.1.3.\n"
                "   					The new \\ :func:`geosoft.gxapi.GXDB.find_chan`\\  searches using the exact channel name.\n"
                "   				\n\n"
               );
    pyClass.def("find_symb", &GXDB_wrap_find_symb,
                "find_symb((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get handle to the specified symbol.\n\n"

                ":param arg1: Name of symbol\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DB_SYMB_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: Symbol Handle, \\ :ref:`NULLSYMB`\\  if not defined\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					To work with a specific column from a VA channel,\n"
                "   					specify the VA element number in square brackets as part\n"
                "   					of the VA channel name (e.g. \"EM[3]\" will treat the fourth\n"
                "   					column of the VA channel as a VV).\n"
                "   \n"
                "   					For backward compatibility with GXs not employing the\n"
                "   					\\ :func:`geosoft.gxapi.GXDB.get_xyz_chan_symb`\\  function, the following behaviour has\n"
                "   					been introduced as of v5.1.3:  (also true for \"Y\").\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXDB.find_symb`\\ (hDB, \"X\", DB_SYMB_CHAN) is now equivalent to:\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXDB.get_xyz_chan_symb`\\ (hDB, DB_CHAN_X);\n"
                "   \n"
                "   					In other words, the current X or Y is searched for, not\n"
                "   					necessarily the literal \"X\" or \"Y\". This ensures that newer\n"
                "   					databases, which might have \"Easting\" and \"Northing\"\n"
                "   					(or other similar names) instead of \"X\" and \"Y\" will still\n"
                "   					work with older GXs expecting \"X\" and \"Y\".\n"
                "   \n"
                "   					The new \\ :func:`geosoft.gxapi.GXDB.find_chan`\\  searches using the exact channel name.\n"
                "   				\n\n"
               );
    pyClass.def("get_chan_order_lst", &GXDB_wrap_get_chan_order_lst,
                "get_chan_order_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method gets the channel display order for a\n"
                "   					database. The list will be stored in an LST object.\n"
                "   					In order to modify this displayed channels list,\n"
                "   					call \\ :func:`geosoft.gxapi.GXDB.set_chan_order_lst`\\  after.\n"
                "   				\n\n"

                ":param arg1: LST object to populate\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"
               );
    pyClass.def("get_xyz_chan_symb", &GXDB_wrap_get_xyz_chan_symb,
                "get_xyz_chan_symb((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Searches for current X, Y or Z channel symbol\n\n"

                ":param arg1: \\ :ref:`DB_CHAN_SYMBOL`\\ \n"
                ":type arg1: int\n"
                ":returns: x - Symbol Handle\n"
                "          						\\ :ref:`NULLSYMB`\\  - Symbol not found\n"
                "          \n"
                "          						searches for the \"current\" X, Y or Z channel.\n"
                "          						If none is defined, then looks for \"X\", \"Y\" or \"Z\" channel\n"
                "          						If the channel is defined, but not present, returns \\ :ref:`NULLSYMB`\\ .\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );
    pyClass.def("class_chan_list", &GXDB_wrap_class_chan_list,
                "class_chan_list((GXVV)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Place a list of channels for a given class in a VV.\n\n"

                ":param arg1: VV to populate, must be type INT.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Class name to match (\"\" for all)\n"
                ":type arg2: str\n"
                ":returns: Number of symbols.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method generates a list of symbols in the database\n"
                "   					and places their handles into a VV. The list is not\n"
                "   					sorted.\n"
                "   					Only channels with the given class name are included,\n"
                "   					e.g. use \"ASSAY\" for assay channels used in CHIMERA.\n"
                "   				\n\n"
               );
    pyClass.def("exist_chan", &GXDB_wrap_exist_chan,
                "exist_chan((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   See if the specified channel exists in the database.\n\n"

                ":param arg1: Name of Channel\n"
                ":type arg1: str\n"
                ":returns: 0 - Symbol does not exist in the database\n"
                "          						1 - Symbol Exists\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					See notes for \\ :func:`geosoft.gxapi.GXDB.exist_symb`\\ .\n"
                "   					Introduced in v5.1.3.\n"
                "   					\\ :func:`geosoft.gxapi.GXDB.exist_chan`\\  searches using the exact channel name.\n"
                "   				\n\n"
               );
    pyClass.def("exist_symb", &GXDB_wrap_exist_symb,
                "exist_symb((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method checks to see if the specified symbol exists\n"
                "   					in the database.\n"
                "   				\n\n"

                ":param arg1: Name of Symbol\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`DB_SYMB_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: 0 - Symbol does not exist in the database\n"
                "          						1 - Symbol Exists\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					For backward compatibility with GXs not employing the\n"
                "   					GetXYZChan_DB function, the following behaviour has\n"
                "   					been introduced as of v5.1.3:  (also true for \"Y\").\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXDB.exist_symb`\\ (hDB, \"X\", DB_SYMB_CHAN) is now equivalent to:\n"
                "   \n"
                "   					GetXYZChan_DB(hDB, DB_CHAN_X, sXCh);\n"
                "   					\\ :func:`geosoft.gxapi.GXDB.exist_symb`\\ (hDB, sXCh, DB_SYMB_CHAN);\n"
                "   \n"
                "   					In other words, the current X or Y is searched for, not\n"
                "   					necessarily the literal \"X\" or \"Y\". This ensures that newer\n"
                "   					databases, which might have \"Easting\" and \"Northing\"\n"
                "   					(or other similar names) instead of \"X\" and \"Y\" will still\n"
                "   					work with older GXs expecting \"X\" and \"Y\".\n"
                "   \n"
                "   					The new \\ :func:`geosoft.gxapi.GXDB.exist_chan`\\  searches using the exact channel name.\n"
                "   				\n\n"
               );
    pyClass.def("valid_symb", &GXDB_wrap_valid_symb,
                "valid_symb((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method checks to see if the specified symbol is a valid symbol in the database.\n"
                "   				\n\n"

                ":param arg1: Symbol to check\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DB_SYMB_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: 0 - Invalid symbol \n"
                "          						1 - Symbol is valid\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.1.0\n\n"
               );
    pyClass.def("get_symb_lock", &GXDB_wrap_get_symb_lock,
                "get_symb_lock((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Determines if a symbol is locked\n\n"

                ":param arg1: Symbol to Lock\n"
                ":type arg1: int\n"
                ":returns: \\ :ref:`DB_LOCK`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("get_xyz_chan", &GXDB_wrap_get_xyz_chan,
                "get_xyz_chan((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets current X, Y or Z channel name\n\n"

                ":param arg1: \\ :ref:`DB_CHAN_SYMBOL`\\ \n"
                ":type arg1: int\n"
                ":param arg2: returned name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					searches for the \"current\" X, Y or Z channel.\n"
                "   					If none is defined, then returns \"X\", \"Y\" or \"Z\".\n"
                "   				\n\n"
               );
    pyClass.def("symb_list", &GXDB_wrap_symb_list,
                "symb_list((GXVV)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Place a list of symbols in a VV.\n\n"

                ":param arg1: VV to populate, must be type INT.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: \\ :ref:`DB_SYMB_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: Number of symbols.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("line_lst", &GXDB_wrap_line_lst,
                "line_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LST with database lines.\n\n"

                ":param arg1: List to Populate\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Populates a LST with channel symbols.\n"
                "   					The name is put into the \"Name\" part of the LST (0),\n"
                "   					and the handle, an integer value written as a string, is\n"
                "   					placed in the value part of the LST (1).\n"
                "   					The LST is cleared first, and the items are sorted in logical line order.\n"
                "   				\n\n"
               );
    pyClass.def("lock_symb", &GXDB_wrap_lock_symb,
                "lock_symb((int)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Locks a symbol for READONLY or READWRITE.\n\n"

                ":param arg1: Symbol to Lock\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DB_LOCK`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`DB_WAIT`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("mask_chan_lst", &GXDB_wrap_mask_chan_lst,
                "mask_chan_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LST with mask channels.\n\n"

                ":param arg1: LST object to populate\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Loads a LST with all channels with CLASS \"MASK\", as well\n"
                "   					as all channels containing the string \"MASK\", as long\n"
                "   					as the CLASS for these channels is not set to something\n"
                "   					other than \"\" or \"MASK\".\n"
                "   \n"
                "   					This function is a duplicate of the \\ :func:`geosoft.gxapi.GXCHIMERA.mask_chan_lst`\\ \n"
                "   					function, and can be used if CHIMERA is not installed.\n"
                "   \n"
                "   					The LST is cleared first, and the items are sorted by name.\n"
                "   					\"None\" is added at the end, with a handle value of \"-1\".\n"
                "   				\n\n"
               );
    pyClass.def("selected_line_lst", &GXDB_wrap_selected_line_lst,
                "selected_line_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LST with the selected lines.\n\n"

                ":param arg1: List to Populate\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method populates a LST object with all of the symbols\n"
                "   					of the selected lines in the database.\n"
                "   					The name is put into the \"Name\" part of the LST (0),\n"
                "   					and the handle, an integer value written as a string, is\n"
                "   					placed in the value part of the LST (1).\n"
                "   \n"
                "   					Symbols are automatically sorted in logical line order.\n"
                "   				\n\n"
               );
    pyClass.def("set_chan_order_lst", &GXDB_wrap_set_chan_order_lst,
                "set_chan_order_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method sets the channel display order for a\n"
                "   					database. The list to modify will be stored in an LST\n"
                "   					object. Call \\ :func:`geosoft.gxapi.GXDB.get_chan_order_lst`\\  to populate the LST.\n"
                "   				\n\n"

                ":param arg1: LST object to modify\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"
               );
    pyClass.def("set_xyz_chan", &GXDB_wrap_set_xyz_chan,
                "set_xyz_chan((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets current X, Y or Z channel name\n\n"

                ":param arg1: \\ :ref:`DB_CHAN_SYMBOL`\\ \n"
                ":type arg1: int\n"
                ":param arg2: channel name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the value specified is \"\", the internally stored value\n"
                "   					is cleared, and GetXYZChan_DB will return \"X\", \"Y\" or \"Z\"\n"
                "   \n"
                "   					This can be used, for instance, to make \"Easting\" and \"Northing\"\n"
                "   					the current X and Y channels, and have GXs using the\n"
                "   					\\ :func:`geosoft.gxapi.GXDB.get_xyz_chan_symb`\\  function to load \"X\" and \"Y\" work as desired.\n"
                "   				\n\n"
               );
    pyClass.def("string_chan_lst", &GXDB_wrap_string_chan_lst,
                "string_chan_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LST with string-type channels.\n\n"

                ":param arg1: LST object to populate\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The Name of the symbol is placed in the\n"
                "   					item name and the item value is set to the symbol handle.\n"
                "   					Only channels with the string-type data (sChanType_DB < 0)\n"
                "   					are included.\n"
                "   \n"
                "   					The LST is cleared first, and the items are sorted by name.\n"
                "   				\n\n"
               );
    pyClass.def("symb_lst", &GXDB_wrap_symb_lst,
                "symb_lst((GXLST)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Populate a LST with database symbols.\n\n"

                ":param arg1: List to Populate\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`DB_SYMB_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Populates a LST with channel, line, blob or user symbols.\n"
                "   					The name is put into the \"Name\" part of the LST (0),\n"
                "   					and the handle, an integer value written as a string, is\n"
                "   					placed in the value part of the LST (1).\n"
                "   \n"
                "   					Line symbols are automatically sorted in logical line order.\n"
                "   \n"
                "   					NOTE: The LST is NOT cleared before being filled. If you\n"
                "   					want to clear the LST and get sorted values, use the\n"
                "   					\\ :func:`geosoft.gxapi.GXDB.chan_lst`\\  and \\ :func:`geosoft.gxapi.GXDB.line_lst`\\  functions.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDB.chan_lst`\\ , \\ :func:`geosoft.gxapi.GXDB.line_lst`\\ , \\ :func:`geosoft.gxapi.GXDB.selected_line_lst`\\ \n\n"
               );
    pyClass.def("un_lock_all_symb", &GXDB_wrap_un_lock_all_symb,
                "un_lock_all_symb() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   UnLocks all symbols.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("un_lock_symb", &GXDB_wrap_un_lock_symb,
                "un_lock_symb((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   UnLocks a symbol.\n\n"

                ":param arg1: Symbol to Lock\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("add_associated_load", &GXDB_wrap_add_associated_load,
                "add_associated_load((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add this channel to the auto-load feature of the group.\n\n"

                ":param arg1: Line\n"
                ":type arg1: int\n"
                ":param arg2: Channel\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the channel is not yet associated, it is first associated.\n"
                "   					If the channel is already in the associated-load list, this\n"
                "   					does nothing.\n"
                "   \n"
                "   					As of v6.0, the load-status of channels is no longer stored\n"
                "   					in the database, but in the project, so this function is\n"
                "   					equivalent to calling \\ :func:`geosoft.gxapi.GXDB.associate`\\ .\n"
                "   				\n\n"
               );
    pyClass.def("add_comment", &GXDB_wrap_add_comment,
                "add_comment((str)arg1, (str)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a comment with a string to the activity log of the database.\n\n"

                ":param arg1: Comment\n"
                ":type arg1: str\n"
                ":param arg2: String\n"
                ":type arg2: str\n"
                ":param arg3: Indent comment one tab? (TRUE or FALSE)\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The comment is written in the form:\n"
                "   \n"
                "   					Comment: String2\n"
                "   \n"
                "   					and is followed by a carriage return.\n"
                "   					The activity log is created automatically if it does not exist.\n"
                "   				\n\n"
               );
    pyClass.def("add_int_comment", &GXDB_wrap_add_int_comment,
                "add_int_comment((str)arg1, (int)arg2, (bool)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a comment with an integer to the activity log of the database.\n\n"

                ":param arg1: Comment\n"
                ":type arg1: str\n"
                ":param arg2: value\n"
                ":type arg2: int\n"
                ":param arg3: Indent comment one tab? bool\n"
                ":type arg3: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The comment is written in the form:\n"
                "   \n"
                "   					Comment: Value\n"
                "   \n"
                "   					and is followed by a carriage return.\n"
                "   					The activity log is created automatically if it does not exist.\n"
                "   \n"
                "   					See Notes in \\ :func:`geosoft.gxapi.GXDB.add_comment`\\ .\n"
                "   				\n\n"
               );
    pyClass.def("add_double_comment", &GXDB_wrap_add_double_comment,
                "add_double_comment((str)arg1, (float)arg2, (bool)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a comment with a float value to the activity log of the database.\n\n"

                ":param arg1: Comment\n"
                ":type arg1: str\n"
                ":param arg2: Value\n"
                ":type arg2: float\n"
                ":param arg3: Indent comment one tab? bool\n"
                ":type arg3: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The comment is written in the form:\n"
                "   \n"
                "   					Comment: Value\n"
                "   \n"
                "   					and if followed by a carriage return.\n"
                "   					The activity log is created automatically if it does not exist.\n"
                "   \n"
                "   					See Notes in \\ :func:`geosoft.gxapi.GXDB.add_comment`\\ .\n"
                "   				\n\n"
               );
    pyClass.def("add_time_comment", &GXDB_wrap_add_time_comment,
                "add_time_comment((str)arg1, (bool)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a comment with the date and time to the activity log of the database.\n\n"

                ":param arg1: Comment\n"
                ":type arg1: str\n"
                ":param arg2: Indent comment one tab? bool\n"
                ":type arg2: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The comment is written in the form:\n"
                "   \n"
                "   					Comment: 2001/12/31 23:59:59\n"
                "   \n"
                "   					and is followed by a carriage return.\n"
                "   					The activity log is created automatically if it does not exist.\n"
                "   \n"
                "   					See Notes in \\ :func:`geosoft.gxapi.GXDB.add_comment`\\ .\n"
                "   				\n\n"
               );
    pyClass.def("associate", &GXDB_wrap_associate,
                "associate((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Associate a channel with a group.\n\n"

                ":param arg1: group line\n"
                ":type arg1: int\n"
                ":param arg2: Channel\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If it is already associated, or if the group has no\n"
                "   					defined group class, does nothing.\n"
                "   \n"
                "   					As of v6.3, if a group line has no class defined, then ALL\n"
                "   					channels are assumed to be associated with it. This means\n"
                "   					that you need to associate a new channel with a group only in\n"
                "   					those cases where the group class is defined.\n"
                "   \n"
                "   					If this function is used on a group with a group class, then\n"
                "   					the channel is added to class's association list, and the\n"
                "   					channel will be recognized as being associated with all\n"
                "   					groups of that class.\n"
                "   				\n\n"
               );
    pyClass.def("associate_all", &GXDB_wrap_associate_all,
                "associate_all((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Associate all channels with a group.\n\n"

                ":param arg1: group line\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					As of v6.3, if a group line has no class defined, then ALL\n"
                "   					channels are already assumed to be associated with it, and this\n"
                "   					function does nothing.\n"
                "   				\n\n"
               );
    pyClass.def("associate_class", &GXDB_wrap_associate_class,
                "associate_class((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Associate a channel with all groups of a specific class.\n\n"

                ":param arg1: Channel\n"
                ":type arg1: int\n"
                ":param arg2: Class name of groups to associate the channel with. (Must be defined).\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					As of v6.3, if a group line has no class defined, then ALL\n"
                "   					channels are automatically assumed to be associated with it.\n"
                "   				\n\n"
               );
    pyClass.def("gen_valid_chan_symb", &GXDB_wrap_gen_valid_chan_symb,
                "gen_valid_chan_symb((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a valid channel name from a name candidate\n\n"

                ":param arg1: Input string\n"
                ":type arg1: str\n"
                ":param arg2: Outout string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("gen_valid_chan_symb");
    pyClass.def("gen_valid_line_symb", &GXDB_wrap_gen_valid_line_symb,
                "gen_valid_line_symb((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a valid line symb name string from given string.\n\n"

                ":param arg1: Input string\n"
                ":type arg1: str\n"
                ":param arg2: Outout string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The returned name is either the same size as the input\n"
                "   					or shorter. Escapes, leading and trailing spaces are removed, then\n"
                "   					all illegal characters are replaced with an underscore.\n"
                "   				\n\n"
               ).staticmethod("gen_valid_line_symb");
    pyClass.def("get_chan_va", &GXDB_wrap_get_chan_va,
                "get_chan_va((int)arg1, (int)arg2, (GXVA)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Place the contents of a channel in a VA.\n\n"

                ":param arg1: Line\n"
                ":type arg1: int\n"
                ":param arg2: Channel\n"
                ":type arg2: int\n"
                ":param arg3: VA in which to place the data\n"
                ":type arg3: :class:`geosoft.gxapi.GXVA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXVA`\\  class.\n\n"
               );
    pyClass.def("get_va_scaling", &GXDB_wrap_get_va_scaling,
                "get_va_scaling((int)arg1, (float_ref)arg2, (float_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get base and range for VA channel cell display.\n\n"

                ":param arg1: channel (Locked DB_LOCK_READWRITE)\n"
                ":type arg1: int\n"
                ":param arg2: Base value (rDummy for none)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Range value (rDummy for none)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See \\ :func:`geosoft.gxapi.GXDB.set_va_scaling`\\ .\n\n"
               );
    pyClass.def("get_va_windows", &GXDB_wrap_get_va_windows,
                "get_va_windows((int)arg1, (int_ref)arg2, (int_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the range of windows displayed for a VA channel.\n\n"

                ":param arg1: channel (Locked DB_LOCK_READWRITE)\n"
                ":type arg1: int\n"
                ":param arg2: First window (0 to N-2, iDummy for default)\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Last window (1 to N-1, iDummy for default)\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See \\ :func:`geosoft.gxapi.GXDB.set_va_windows`\\ .\n\n"
               );
    pyClass.def("set_va_base_coordinate_info", &GXDB_wrap_set_va_base_coordinate_info,
                "set_va_base_coordinate_info((int)arg1, (int)arg2, (float)arg3, (GXVV)arg4, (str)arg5, (bool)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the array channel base coordinate type, offset and values.\n\n"

                ":param arg1: channel (Locked DB_LOCK_READWRITE)\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DB_ARRAY_BASETYPE`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Optional offset or base frequency\n"
                ":type arg3: float\n"
                ":param arg4: Values (one per array channel column) (REAL)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Units\n"
                ":type arg5: str\n"
                ":param arg6: Allow changes to existing values?bool\n"
                ":type arg6: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See \\ :func:`geosoft.gxapi.GXDB.get_va_base_coordinate_info`\\ .\n\n"
               );
    pyClass.def("get_va_base_coordinate_info", &GXDB_wrap_get_va_base_coordinate_info,
                "get_va_base_coordinate_info((int)arg1, (int_ref)arg2, (float_ref)arg3, (GXVV)arg4, (str_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the array channel base coordinate type, offset and values.\n\n"

                ":param arg1: channel (Locked DB_LOCK_READONLY)\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DB_ARRAY_BASETYPE`\\ \n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Optional offset or base frequency\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Values (one per array channel column) (REAL)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Units\n"
                ":type arg5: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See \\ :func:`geosoft.gxapi.GXDB.set_va_base_coordinate_info`\\ .\n\n"
               );
    pyClass.def("get_group_class", &GXDB_wrap_get_group_class,
                "get_group_class((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Class name for a group line.\n\n"

                ":param arg1: Group line - DB_LOCK_READWRITE or DB_LOCK_READONLY\n"
                ":type arg1: int\n"
                ":param arg2: returned class name - max size = DB_GROUP_CLASS_SIZE - 1\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method fails if the line is not a group line.\n"
                "   					Group classes are used to identify group lines used for\n"
                "   					special purposes, e.g.: \"COLLAR\" for the Wholeplot collar table,\n"
                "   					or \"TARGETS\" for the UX-Detect Targets list.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDB.line_category`\\  - to see if a line is a group line.\n\n"
               );
    pyClass.def("get_info", &GXDB_wrap_get_info,
                "get_info((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get information about the database.\n\n"

                ":param arg1: \\ :ref:`DB_INFO`\\ \n"
                ":type arg1: int\n"
                ":returns: x - Return Value\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("get_va_prof_color_file", &GXDB_wrap_get_va_prof_color_file,
                "get_va_prof_color_file((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get colours for a VA channel when displayed in the profile window.\n\n"

                ":param arg1: channel (Locked DB_LOCK_READWRITE)\n"
                ":type arg1: int\n"
                ":param arg2: zone file name, \"\" to clear.\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See \\ :func:`geosoft.gxapi.GXDB.set_va_prof_color_file`\\ .\n\n"
               );
    pyClass.def("get_va_prof_sect_option", &GXDB_wrap_get_va_prof_sect_option,
                "get_va_prof_sect_option((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the display options of VA channels\n\n"

                ":param arg1: channel (Locked DB_LOCK_READWRITE)\n"
                ":type arg1: int\n"
                ":param arg2: Option  \"Profile\", \"Section\" or \"Section and Profile\"\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("get_va_sect_color_file", &GXDB_wrap_get_va_sect_color_file,
                "get_va_sect_color_file((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get colours for a VA channel when displayed section in the profile window.\n\n"

                ":param arg1: channel (Locked DB_LOCK_READWRITE)\n"
                ":type arg1: int\n"
                ":param arg2: zone file name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Fails in the channel is not an array channel\n\n"
               );
    pyClass.def("is_associated", &GXDB_wrap_is_associated,
                "is_associated((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check to see if a channel is associated with group.\n\n"

                ":param arg1: Line\n"
                ":type arg1: int\n"
                ":param arg2: Channel\n"
                ":type arg2: int\n"
                ":returns: 0 if not a group line, or if the channel is not associated.\n"
                "          \n"
                "          						As of v6.3, if a group line has no class defined, then ALL\n"
                "          						channels are automatically assumed to be associated with it.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );
    pyClass.def("is_wholeplot", &GXDB_wrap_is_wholeplot,
                "is_wholeplot() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this a Wholeplot database?\n\n"

                ":returns: 1 if it is a Wholeplot database\n"
                "          						0 if it is not.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Currently checks to see if the DH_COLLAR line exists.\n\n"
               );
    pyClass.def("put_chan_va", &GXDB_wrap_put_chan_va,
                "put_chan_va((int)arg1, (int)arg2, (GXVA)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Place the contents of a VA in a channel.\n\n"

                ":param arg1: Line\n"
                ":type arg1: int\n"
                ":param arg2: Channel\n"
                ":type arg2: int\n"
                ":param arg3: VA from which to get the data\n"
                ":type arg3: :class:`geosoft.gxapi.GXVA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXVA`\\  class.\n\n"
               );
    pyClass.def("set_group_class", &GXDB_wrap_set_group_class,
                "set_group_class((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Class name for a group line.\n\n"

                ":param arg1: Group line - DB_LOCK_READWRITE\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`DB_GROUP_CLASS_SIZE`\\ \n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method fails if the line is not a group line.\n"
                "   					Group classes are used to identify group lines used for\n"
                "   					special purposes. All group lines with the same class share\n"
                "   					the same list of associated channels.\n"
                "   \n"
                "   					As of v6.3, if a group line has no class defined, then ALL\n"
                "   					channels are assumed to be associated with it. This means\n"
                "   					that a group class should only be defined when you wish to\n"
                "   					associate a subset of the available channels to group line.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXDB.line_category`\\  - to see if a line is a group line.\n"
                "   					\\ :func:`geosoft.gxapi.GXDB.associate`\\  - Associate a channel with a group.\n"
                "   				\n\n"
               );
    pyClass.def("set_va_prof_color_file", &GXDB_wrap_set_va_prof_color_file,
                "set_va_prof_color_file((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set colours for a VA channel when displayed in the profile window.\n\n"

                ":param arg1: channel (Locked DB_LOCK_READWRITE)\n"
                ":type arg1: int\n"
                ":param arg2: zone file name, \"\" to clear.\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Fails in the channel is not an array channel, if the\n"
                "   					file does not exist, or if it is not a valid colour zone file.\n"
                "   \n"
                "   					The individual columns in the array channel are displayed using the input\n"
                "   					zone file colours. A linear ITR from 0 to 1 is created on the colour zones\n"
                "   					to map to individual channel indices (expressed as a fraction as shown below).\n"
                "   \n"
                "   					For instance, for a file with 8 colours the ranges are as follows:\n"
                "   \n"
                "   					Colour Range\n"
                "   					Colour 1    0        > value >=  0.125\n"
                "   					Colour 2    0.125    > value >=  0.25\n"
                "   					Colour 3    0.25     > value >=  0.375\n"
                "   					Colour 4    0.375    > value >=  0.5\n"
                "   					Colour 5    0.5      > value >=  0.625\n"
                "   					Colour 6    0.625    > value >=  0.75\n"
                "   					Colour 7    0.75     > value >=  0.875\n"
                "   					Colour 8    0.875    > value >=  1.0\n"
                "   \n"
                "   					When an array channel is displayed, the index of each element (column) is mapped\n"
                "   					into the corresponding range above using the following formula:\n"
                "   \n"
                "   					value = (column index) / (# of columns - 1)\n"
                "   \n"
                "   					For an array with 8 columns, you get the following values:\n"
                "   \n"
                "   					Column   Value    Colour\n"
                "   					0        0        1\n"
                "   					1        0.14     2\n"
                "   					2        0.28     3\n"
                "   					3        0.43     4\n"
                "   					4        0.57     5\n"
                "   					5        0.71     6\n"
                "   					6        0.86     7\n"
                "   					7        1.0      8\n"
                "   \n"
                "   					The colour file search path is: Local directory, then oasismontaj\\tbl.\n"
                "   				\n\n"
               );
    pyClass.def("set_va_prof_sect_option", &GXDB_wrap_set_va_prof_sect_option,
                "set_va_prof_sect_option((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the display options of VA channels\n\n"

                ":param arg1: channel (Locked DB_LOCK_READWRITE)\n"
                ":type arg1: int\n"
                ":param arg2: Option  \"Profile\", \"Section\" or \"Section and Profile\"\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("set_va_scaling", &GXDB_wrap_set_va_scaling,
                "set_va_scaling((int)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set base and range for VA channel cell display.\n\n"

                ":param arg1: channel (Locked DB_LOCK_READWRITE)\n"
                ":type arg1: int\n"
                ":param arg2: Base value (rDummy for none)\n"
                ":type arg2: float\n"
                ":param arg3: Range value (rDummy for none)\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					By default, VA profiles autoscale to fit in the database cell.\n"
                "   					This lets the user set a single base and range for all cells.\n"
                "   					If either input is a dummy, both are set as dummies, and autoscaling\n"
                "   					is used.\n"
                "   				\n\n"
               );
    pyClass.def("set_va_sect_color_file", &GXDB_wrap_set_va_sect_color_file,
                "set_va_sect_color_file((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set colours for a VA channel when displayed section in the profile window.\n\n"

                ":param arg1: channel (Locked DB_LOCK_READWRITE)\n"
                ":type arg1: int\n"
                ":param arg2: zone file name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Fails in the channel is not an array channel, if the\n"
                "   					file does not exist, or if it is not a valid colour zone file.\n"
                "   				\n\n"
               );
    pyClass.def("set_va_windows", &GXDB_wrap_set_va_windows,
                "set_va_windows((int)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the range of windows to display for a VA channel.\n\n"

                ":param arg1: channel (Locked DB_LOCK_READWRITE)\n"
                ":type arg1: int\n"
                ":param arg2: First window (0 to N-1, iDummy for default)\n"
                ":type arg2: int\n"
                ":param arg3: Last window (0 to N-1, iDummy for default)\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Use to display a subset of the VA channel windows in the GDB.\n"
                "   					Windows index from 0.\n"
                "   				\n\n"
               );

    scope().attr("DB_ACTIVITY_BLOB") = "OE.DB_ACTIVITY_LOG";
    scope().attr("DB_CATEGORY_BLOB_NORMAL") = (int32_t)0;
    scope().attr("DB_CATEGORY_CHAN_BYTE") = (int32_t)0;
    scope().attr("DB_CATEGORY_CHAN_USHORT") = (int32_t)1;
    scope().attr("DB_CATEGORY_CHAN_SHORT") = (int32_t)2;
    scope().attr("DB_CATEGORY_CHAN_LONG") = (int32_t)3;
    scope().attr("DB_CATEGORY_CHAN_FLOAT") = (int32_t)4;
    scope().attr("DB_CATEGORY_CHAN_DOUBLE") = (int32_t)5;
    scope().attr("DB_CATEGORY_CHAN_UBYTE") = (int32_t)6;
    scope().attr("DB_CATEGORY_CHAN_ULONG") = (int32_t)7;
    scope().attr("DB_CATEGORY_CHAN_LONG64") = (int32_t)8;
    scope().attr("DB_CATEGORY_CHAN_ULONG64") = (int32_t)9;
    scope().attr("DB_CATEGORY_LINE_FLIGHT") = (int32_t)100;
    scope().attr("DB_CATEGORY_LINE_GROUP") = (int32_t)200;
    scope().attr("DB_CATEGORY_LINE_NORMAL") = (int32_t)100;
    scope().attr("DB_CATEGORY_USER_NORMAL") = (int32_t)0;
    scope().attr("DB_CHAN_FORMAT_NORMAL") = (int32_t)0;
    scope().attr("DB_CHAN_FORMAT_EXP") = (int32_t)1;
    scope().attr("DB_CHAN_FORMAT_TIME") = (int32_t)2;
    scope().attr("DB_CHAN_FORMAT_DATE") = (int32_t)3;
    scope().attr("DB_CHAN_FORMAT_GEOGR") = (int32_t)4;
    scope().attr("DB_CHAN_FORMAT_SIGDIG") = (int32_t)5;
    scope().attr("DB_CHAN_FORMAT_HEX") = (int32_t)6;
    scope().attr("DB_CHAN_UNPROTECTED") = (int32_t)0;
    scope().attr("DB_CHAN_PROTECTED") = (int32_t)1;
    scope().attr("DB_CHAN_X") = (int32_t)0;
    scope().attr("DB_CHAN_Y") = (int32_t)1;
    scope().attr("DB_CHAN_Z") = (int32_t)2;
    scope().attr("DB_COMP_NONE") = (int32_t)0;
    scope().attr("DB_COMP_SPEED") = (int32_t)1;
    scope().attr("DB_COMP_SIZE") = (int32_t)2;
    scope().attr("DB_COORDPAIR_NONE") = (int32_t)0;
    scope().attr("DB_COORDPAIR_X") = (int32_t)1;
    scope().attr("DB_COORDPAIR_Y") = (int32_t)2;
    scope().attr("DB_GROUP_CLASS_SIZE") = (int32_t)16;
    scope().attr("DB_INFO_BLOBS_MAX") = (int32_t)0;
    scope().attr("DB_INFO_LINES_MAX") = (int32_t)1;
    scope().attr("DB_INFO_CHANS_MAX") = (int32_t)2;
    scope().attr("DB_INFO_USERS_MAX") = (int32_t)3;
    scope().attr("DB_INFO_BLOBS_USED") = (int32_t)4;
    scope().attr("DB_INFO_LINES_USED") = (int32_t)5;
    scope().attr("DB_INFO_CHANS_USED") = (int32_t)6;
    scope().attr("DB_INFO_USERS_USED") = (int32_t)7;
    scope().attr("DB_INFO_PAGE_SIZE") = (int32_t)8;
    scope().attr("DB_INFO_DATA_SIZE") = (int32_t)9;
    scope().attr("DB_INFO_LOST_SIZE") = (int32_t)10;
    scope().attr("DB_INFO_FREE_SIZE") = (int32_t)11;
    scope().attr("DB_INFO_COMP_LEVEL") = (int32_t)16;
    scope().attr("DB_INFO_BLOB_SIZE") = (int32_t)19;
    scope().attr("DB_INFO_FILE_SIZE") = (int32_t)17;
    scope().attr("DB_INFO_INDEX_SIZE") = (int32_t)18;
    scope().attr("DB_INFO_MAX_BLOCK_SIZE") = (int32_t)20;
    scope().attr("DB_INFO_CHANGESLOST") = (int32_t)21;
    scope().attr("DB_LINE_LABEL_FORMAT_LINE") = (int32_t)1;
    scope().attr("DB_LINE_LABEL_FORMAT_VERSION") = (int32_t)2;
    scope().attr("DB_LINE_LABEL_FORMAT_TYPE") = (int32_t)4;
    scope().attr("DB_LINE_LABEL_FORMAT_FLIGHT") = (int32_t)8;
    scope().attr("DB_LINE_LABEL_FORMAT_FULL") = (int32_t)15;
    scope().attr("DB_LINE_LABEL_FORMAT_DATE") = (int32_t)16;
    scope().attr("DB_LINE_LABEL_FORMAT_LINK") = (int32_t)7;
    scope().attr("DB_LINE_SELECT_INCLUDE") = (int32_t)0;
    scope().attr("DB_LINE_SELECT_EXCLUDE") = (int32_t)1;
    scope().attr("DB_LINE_TYPE_NORMAL") = (int32_t)0;
    scope().attr("DB_LINE_TYPE_BASE") = (int32_t)1;
    scope().attr("DB_LINE_TYPE_TIE") = (int32_t)2;
    scope().attr("DB_LINE_TYPE_TEST") = (int32_t)3;
    scope().attr("DB_LINE_TYPE_TREND") = (int32_t)4;
    scope().attr("DB_LINE_TYPE_SPECIAL") = (int32_t)5;
    scope().attr("DB_LINE_TYPE_RANDOM") = (int32_t)6;
    scope().attr("DB_LOCK_NONE") = (int32_t)-1;
    scope().attr("DB_LOCK_READONLY") = (int32_t)0;
    scope().attr("DB_LOCK_READWRITE") = (int32_t)1;
    scope().attr("DB_NAME_FILE") = (int32_t)0;
    scope().attr("DB_OWN_SHARED") = (int32_t)0;
    scope().attr("DB_OWN_USER") = (int32_t)1;
    scope().attr("DB_SYMB_BLOB") = (int32_t)0;
    scope().attr("DB_SYMB_LINE") = (int32_t)1;
    scope().attr("DB_SYMB_CHAN") = (int32_t)2;
    scope().attr("DB_SYMB_USER") = (int32_t)3;
    scope().attr("DB_SYMB_NAME_SIZE") = (int32_t)64;
    scope().attr("DB_WAIT_NONE") = (int32_t)0;
    scope().attr("DB_WAIT_INFINITY") = (int32_t)-1;
    scope().attr("DB_ARRAY_BASETYPE_NONE") = (int32_t)0;
    scope().attr("DB_ARRAY_BASETYPE_TIME_WINDOWS") = (int32_t)1;
    scope().attr("DB_ARRAY_BASETYPE_TIMES") = (int32_t)2;
    scope().attr("DB_ARRAY_BASETYPE_FREQUENCIES") = (int32_t)3;
    scope().attr("DB_ARRAY_BASETYPE_ELEVATIONS") = (int32_t)4;
    scope().attr("DB_ARRAY_BASETYPE_DEPTHS") = (int32_t)5;
    scope().attr("DB_ARRAY_BASETYPE_VELOCITIES") = (int32_t)6;
    scope().attr("DB_ARRAY_BASETYPE_DISCRETE_TIME_WINDOWS") = (int32_t)7;
    scope().attr("NULLSYMB") = (int32_t)-1;

}
