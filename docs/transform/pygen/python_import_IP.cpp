#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXIP_wrap_convert_ubcip2_d_to_grid(const gx_string_type& arg1, GXPGPtr arg2, GXVVPtr arg3, GXVVPtr arg4, double arg5, double arg6, double arg7, double arg8, int32_t arg9)
{
    GXIP::convert_ubcip2_d_to_grid(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXIP_wrap_create_default_job(GXIPPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->create_default_job(arg1, (IP_PLOT)arg2);
}
inline void GXIP_wrap_export_ubcip3(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6, double arg7)
{
    self->export_ubcip3(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXIP_wrap_export_ubcip_control(const gx_string_type& arg1, int32_t arg2, int32_t arg3, double arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8, const gx_string_type& arg9, const gx_string_type& arg10, const gx_string_type& arg11, const gx_string_type& arg12)
{
    GXIP::export_ubcip_control(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12);
}
inline void GXIP_wrap_export_ubcip_control_v5(const gx_string_type& arg1, int32_t arg2, double arg3, const gx_string_type& arg4, const gx_string_type& arg5, int32_t arg6, const gx_string_type& arg7, int32_t arg8, const gx_string_type& arg9, int32_t arg10, const gx_string_type& arg11, int32_t arg12, const gx_string_type& arg13, int32_t arg14, const gx_string_type& arg15, const gx_string_type& arg16)
{
    GXIP::export_ubcip_control_v5(arg1, arg2, arg3, arg4, arg5, (IP_UBC_CONTROL)arg6, arg7, (IP_UBC_CONTROL)arg8, arg9, (IP_UBC_CONTROL)arg10, arg11, (IP_UBC_CONTROL)arg12, arg13, (IP_UBC_CONTROL)arg14, arg15, arg16);
}
inline void GXIP_wrap_export_ubc_res3(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7, double arg8)
{
    self->export_ubc_res3(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXIP_wrap_export_ubc_res_control(const gx_string_type& arg1, int32_t arg2, int32_t arg3, double arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8, double arg9, const gx_string_type& arg10, const gx_string_type& arg11)
{
    GXIP::export_ubc_res_control(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXIP_wrap_export_ubc_res_control_v5(const gx_string_type& arg1, int32_t arg2, double arg3, const gx_string_type& arg4, const gx_string_type& arg5, int32_t arg6, const gx_string_type& arg7, int32_t arg8, const gx_string_type& arg9, int32_t arg10, const gx_string_type& arg11, int32_t arg12, const gx_string_type& arg13, const gx_string_type& arg14)
{
    GXIP::export_ubc_res_control_v5(arg1, arg2, arg3, arg4, arg5, (IP_UBC_CONTROL)arg6, arg7, (IP_UBC_CONTROL)arg8, arg9, (IP_UBC_CONTROL)arg10, arg11, (IP_UBC_CONTROL)arg12, arg13, arg14);
}
inline void GXIP_wrap_export_data_to_ubc_3d(GXIPPtr self, GXDBPtr arg1, GXLSTPtr arg2, int32_t arg3, int32_t arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7, int32_t arg8, const gx_string_type& arg9, const gx_string_type& arg10)
{
    self->export_data_to_ubc_3d(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline GXPGPtr GXIP_wrap_import_ubc2_dmod(const gx_string_type& arg1, int32_t arg2)
{
    GXPGPtr ret = GXIP::import_ubc2_dmod(arg1, arg2);
    return ret;
}
inline void GXIP_wrap_import_ubc2_dmsh(const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, GXVVPtr arg4, GXVVPtr arg5)
{
    GXIP::import_ubc2_dmsh(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIP_wrap_import_ubc2_d_topo(const gx_string_type& arg1, float_ref& arg2, GXVVPtr arg3, GXVVPtr arg4)
{
    GXIP::import_ubc2_d_topo(arg1, arg2, arg3, arg4);
}
inline void GXIP_wrap_open_job(GXIPPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->open_job(arg1, (IP_PLOT)arg2);
}
inline void GXIP_wrap_save_job(GXIPPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->save_job(arg1, (IP_PLOT)arg2);
}
inline GXPGPtr GXIP_wrap_trim_ubc2_d_model(GXPGPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXVVPtr arg5, GXVVPtr arg6, float_ref& arg7)
{
    GXPGPtr ret = GXIP::trim_ubc2_d_model(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
    return ret;
}
inline void GXIP_wrap_write_distant_electrodes(GXIPPtr self, GXDBPtr arg1)
{
    self->write_distant_electrodes(arg1);
}
inline void GXIP_wrap_write_distant_electrodes_lst(GXIPPtr self, GXDBPtr arg1, GXLSTPtr arg2)
{
    self->write_distant_electrodes_lst(arg1, arg2);
}
inline void GXIP_wrap_average_duplicates_qc(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4)
{
    self->average_duplicates_qc(arg1, arg2, arg3, (IP_DUPLICATE)arg4);
}
inline GXIPPtr GXIP_wrap_create()
{
    GXIPPtr ret = GXIP::create();
    return ret;
}
inline void GXIP_wrap_export_i2_x(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8, const gx_string_type& arg9, const gx_string_type& arg10, const gx_string_type& arg11)
{
    self->export_i2_x(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXIP_wrap_export_ipdata(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    self->export_ipdata(arg1, arg2, arg3);
}
inline void GXIP_wrap_export_ipdata_dir(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    self->export_ipdata_dir(arg1, arg2, arg3, arg4);
}
inline void GXIP_wrap_export_ipred(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, int32_t arg5, const gx_string_type& arg6, double arg7, double arg8, int32_t arg9)
{
    self->export_ipred(arg1, arg2, arg3, arg4, (IP_FILTER)arg5, arg6, arg7, arg8, arg9);
}
inline void GXIP_wrap_export_ipred_dir(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, int32_t arg5, const gx_string_type& arg6, double arg7, double arg8, int32_t arg9, const gx_string_type& arg10)
{
    self->export_ipred_dir(arg1, arg2, arg3, arg4, (IP_FILTER)arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXIP_wrap_export_line_ipdata(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    self->export_line_ipdata(arg1, arg2, arg3, arg4);
}
inline void GXIP_wrap_export_sgdf(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    self->export_sgdf(arg1, arg2, arg3, arg4);
}
inline void GXIP_wrap_get_n_value_lst(GXIPPtr self, GXDBPtr arg1, GXLSTPtr arg2)
{
    self->get_n_value_lst(arg1, arg2);
}
inline void GXIP_wrap_get_topo_line(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, GXVVPtr arg6)
{
    self->get_topo_line(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline int32_t GXIP_wrap_get_chan_domain(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2)
{
    IP_DOMAIN ret = self->get_chan_domain(arg1, arg2);
    return ret;
}
inline void GXIP_wrap_get_chan_label(const gx_string_type& arg1, str_ref& arg2, str_ref& arg3)
{
    GXIP::get_chan_label(arg1, arg2, arg3);
}
inline void GXIP_wrap_get_channel_info(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, int_ref& arg3, float_ref& arg4, int_ref& arg5, GXVVPtr arg6)
{
    self->get_channel_info(arg1, arg2, (IP_DOMAIN&)arg3, arg4, arg5, arg6);
}
inline void GXIP_wrap_set_channel_info(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, int32_t arg3, double arg4, int32_t arg5, GXVVPtr arg6)
{
    self->set_channel_info(arg1, arg2, (IP_DOMAIN)arg3, arg4, arg5, arg6);
}
inline void GXIP_wrap_import_dump(GXIPPtr self, int32_t arg1, GXDBPtr arg2, const gx_string_type& arg3)
{
    self->import_dump((IP_SYS)arg1, arg2, arg3);
}
inline void GXIP_wrap_import_grid(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    self->import_grid(arg1, arg2, arg3);
}
inline void GXIP_wrap_import_i2_x(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8, const gx_string_type& arg9, const gx_string_type& arg10, const gx_string_type& arg11, int32_t arg12)
{
    self->import_i2_x(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, (IP_I2XIMPMODE)arg12);
}
inline void GXIP_wrap_import_i2_x_ex(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8, const gx_string_type& arg9, const gx_string_type& arg10, const gx_string_type& arg11, const gx_string_type& arg12, const gx_string_type& arg13, int32_t arg14)
{
    self->import_i2_x_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, (IP_I2XIMPMODE)arg14);
}
inline void GXIP_wrap_import_instrumentation_gdd(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2)
{
    self->import_instrumentation_gdd(arg1, arg2);
}
inline void GXIP_wrap_import_ipdata(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    self->import_ipdata(arg1, arg2, arg3);
}
inline void GXIP_wrap_import_ipdata2(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    self->import_ipdata2(arg1, arg2, arg3, arg4);
}
inline void GXIP_wrap_import_ipred(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    self->import_ipred(arg1, arg2, arg3);
}
inline void GXIP_wrap_import_merge_ipred(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    self->import_merge_ipred(arg1, arg2, arg3);
}
inline void GXIP_wrap_import_sgdf(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2)
{
    self->import_sgdf(arg1, arg2);
}
inline void GXIP_wrap_import_topo_csv(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2)
{
    self->import_topo_csv(arg1, arg2);
}
inline void GXIP_wrap_import_topo_grid(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2)
{
    self->import_topo_grid(arg1, arg2);
}
inline void GXIP_wrap_import_zonge_avg(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, double arg3, int32_t arg4, double arg5)
{
    self->import_zonge_avg(arg1, arg2, arg3, (IP_STNSCALE)arg4, arg5);
}
inline void GXIP_wrap_import_zonge_fld(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, int32_t arg3, double arg4)
{
    self->import_zonge_fld(arg1, arg2, (IP_STNSCALE)arg3, arg4);
}
inline void GXIP_wrap_new_xy_database(GXIPPtr self, GXDBPtr arg1, GXDBPtr arg2, GXVVPtr arg3, const gx_string_type& arg4, double arg5)
{
    self->new_xy_database(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIP_wrap_pseudo_plot(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    self->pseudo_plot(arg1, arg2, arg3, arg4);
}
inline void GXIP_wrap_pseudo_plot2(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5)
{
    self->pseudo_plot2(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIP_wrap_pseudo_plot2_dir(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6)
{
    self->pseudo_plot2_dir(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXIP_wrap_ps_stack(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    self->ps_stack(arg1, arg2, arg3, arg4);
}
inline void GXIP_wrap_ps_stack2(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4, const gx_string_type& arg5)
{
    self->ps_stack2(arg1, arg2, arg3, (IP_STACK_TYPE)arg4, arg5);
}
inline void GXIP_wrap_ps_stack2_dir(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4, const gx_string_type& arg5, const gx_string_type& arg6)
{
    self->ps_stack2_dir(arg1, arg2, arg3, (IP_STACK_TYPE)arg4, arg5, arg6);
}
inline void GXIP_wrap_qc_chan_lst(GXIPPtr self, GXDBPtr arg1, GXLSTPtr arg2)
{
    self->qc_chan_lst(arg1, arg2);
}
inline void GXIP_wrap_recalculate(GXIPPtr self, GXDBPtr arg1)
{
    self->recalculate(arg1);
}
inline void GXIP_wrap_recalculate_ex(GXIPPtr self, GXDBPtr arg1, int32_t arg2)
{
    self->recalculate_ex(arg1, arg2);
}
inline void GXIP_wrap_recalculate_z(GXIPPtr self, GXDBPtr arg1)
{
    self->recalculate_z(arg1);
}
inline void GXIP_wrap_set_import_mode(GXIPPtr self, int32_t arg1)
{
    self->set_import_mode(arg1);
}
inline void GXIP_wrap_window(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    self->window(arg1, arg2, arg3, arg4);
}
inline void GXIP_wrap_winnow_chan_list(GXLSTPtr arg1)
{
    GXIP::winnow_chan_list(arg1);
}
inline void GXIP_wrap_winnow_chan_list2(GXLSTPtr arg1, GXDBPtr arg2)
{
    GXIP::winnow_chan_list2(arg1, arg2);
}
inline int32_t GXIP_wrap_is_valid_line(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2)
{
    int32_t ret = self->is_valid_line(arg1, arg2);
    return ret;
}
inline int32_t GXIP_wrap_line_array_type(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2)
{
    IP_ARRAY ret = self->line_array_type(arg1, arg2);
    return ret;
}
inline double GXIP_wrap_a_spacing(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2)
{
    double ret = self->a_spacing(arg1, arg2);
    return ret;
}
inline int32_t GXIP_wrap_pldp_convention(GXIPPtr self)
{
    IP_PLDP_CONV ret = self->pldp_convention();
    return ret;
}
inline void GXIP_wrap_get_electrode_locations_and_mask_values(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, int32_t arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7)
{
    self->get_electrode_locations_and_mask_values(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXIP_wrap_set_electrode_mask_values(GXIPPtr self, GXDBPtr arg1, const gx_string_type& arg2, int32_t arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7)
{
    self->set_electrode_mask_values(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}

void gxPythonImportGXIP()
{

    class_<GXIP, GXIPPtr> pyClass("GXIP",
                                  "\n.. parsed-literal::\n\n"
                                  "   This class is used in the IP System for the import, export\n"
                                  "   and processing of Induced Polarization data.\n\n"

                                  "\n\n**Note:**\n\n"

                                  "\n.. parsed-literal::\n\n"
                                  "   The following defines are used in GX code but are not\n"
                                  "   part of any functions:\n"
                                  "   \n"
                                  "   \\ :ref:`IP_ARRAY`\\ \n"
                                  "   \\ :ref:`IP_CHANNELS`\\ \n"
                                  "   \\ :ref:`IP_LINES`\\ \n\n"
                                  , no_init);

    pyClass.def("null", &GXIP::null, "null() -> GXIP\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXIP`\n\n:returns: A null :class:`geosoft.gxapi.GXIP`\n:rtype: :class:`geosoft.gxapi.GXIP`\n").staticmethod("null");
    pyClass.def("is_null", &GXIP::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXIP is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXIP`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXIP::_internal_handle);
    pyClass.def("convert_ubcip2_d_to_grid", &GXIP_wrap_convert_ubcip2_d_to_grid,
                "convert_ubcip2_d_to_grid((str)arg1, (GXPG)arg2, (GXVV)arg3, (GXVV)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (int)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a UBC 2D model to a regular grid.\n\n"

                ":param arg1: Output grid file name\n"
                ":type arg1: str\n"
                ":param arg2: Model data\n"
                ":type arg2: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg3: Model cells sizes (input)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Model cells sizes (input)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Top-left corner X\n"
                ":type arg5: float\n"
                ":param arg6: Top-left corner Z\n"
                ":type arg6: float\n"
                ":param arg7: Output grid cell size in X\n"
                ":type arg7: float\n"
                ":param arg8: Output grid cell size in Z\n"
                ":type arg8: float\n"
                ":param arg9: Output reciprocal of values (0:No, 1:Yes) for resistivity?\n"
                ":type arg9: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Uses TIN gridding to sample the model.\n"
                "   By setting the final value, a resistivity grid can be\n"
                "   created from conductivity data.\n\n"
               ).staticmethod("convert_ubcip2_d_to_grid");
    pyClass.def("create_default_job", &GXIP_wrap_create_default_job,
                "create_default_job((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a default job from scratch.\n\n"

                ":param arg1: File name of the INI file to create (forces correct suffix)\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`IP_PLOT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               );
    pyClass.def("export_ubcip3", &GXIP_wrap_export_ubcip3,
                "export_ubcip3((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (str)arg6, (float)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export of IP data to UBC format.\n\n"

                ":param arg1: DB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Output line name\n"
                ":type arg2: str\n"
                ":param arg3: Output IP channel name\n"
                ":type arg3: str\n"
                ":param arg4: Output error channel name (\"\" for none)\n"
                ":type arg4: str\n"
                ":param arg5: Output OBS file name\n"
                ":type arg5: str\n"
                ":param arg6: Output TOPO file name\n"
                ":type arg6: str\n"
                ":param arg7: version number (3 or 5)\n"
                ":type arg7: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Outputs a \\ `*`\\ .DAT\" file of the survey data for use in the\n"
                "   				 UBC 2D inversion programme IPINV2D.\n"
                "   				 Include error channel output and version-specific formatting.\n"
                "   			 \n\n"
               );
    pyClass.def("export_ubcip_control", &GXIP_wrap_export_ubcip_control,
                "export_ubcip_control((str)arg1, (int)arg2, (int)arg3, (float)arg4, (str)arg5, (str)arg6, (str)arg7, (str)arg8, (str)arg9, (str)arg10, (str)arg11, (str)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a control file for using in the UBC IPINV2D programme.\n\n"

                ":param arg1: Output control file name\n"
                ":type arg1: str\n"
                ":param arg2: niter\n"
                ":type arg2: int\n"
                ":param arg3: irest\n"
                ":type arg3: int\n"
                ":param arg4: chifact\n"
                ":type arg4: float\n"
                ":param arg5: IP obs file\n"
                ":type arg5: str\n"
                ":param arg6: conductivity file\n"
                ":type arg6: str\n"
                ":param arg7: mesh file\n"
                ":type arg7: str\n"
                ":param arg8: topography file\n"
                ":type arg8: str\n"
                ":param arg9: initial model file\n"
                ":type arg9: str\n"
                ":param arg10: reference model\n"
                ":type arg10: str\n"
                ":param arg11: alphas\n"
                ":type arg11: str\n"
                ":param arg12: weights file\n"
                ":type arg12: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 UBC Version 3 Control file.\n"
                "   				 Outputs a control file for use in the\n"
                "   				 UBC 2D IP inversion programme IPINV2D.\n"
                "   			 \n\n"
               ).staticmethod("export_ubcip_control");
    pyClass.def("export_ubcip_control_v5", &GXIP_wrap_export_ubcip_control_v5,
                "export_ubcip_control_v5((str)arg1, (int)arg2, (float)arg3, (str)arg4, (str)arg5, (int)arg6, (str)arg7, (int)arg8, (str)arg9, (int)arg10, (str)arg11, (int)arg12, (str)arg13, (int)arg14, (str)arg15, (str)arg16) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a control file for using in the UBC IPINV2D programme.\n\n"

                ":param arg1: Output control file name\n"
                ":type arg1: str\n"
                ":param arg2: niter\n"
                ":type arg2: int\n"
                ":param arg3: chifact\n"
                ":type arg3: float\n"
                ":param arg4: RES obs file\n"
                ":type arg4: str\n"
                ":param arg5: topography file (required)\n"
                ":type arg5: str\n"
                ":param arg6: Conductivity type \\ :ref:`IP_UBC_CONTROL`\\  FILE or VALUE\n"
                ":type arg6: int\n"
                ":param arg7: Conductivity file (can be \"\") or value\n"
                ":type arg7: str\n"
                ":param arg8: Mesh type \\ :ref:`IP_UBC_CONTROL`\\  FILE, VALUE or DEFAULT\n"
                ":type arg8: int\n"
                ":param arg9: mesh file (can be \"\") or value\n"
                ":type arg9: str\n"
                ":param arg10: Initial model type \\ :ref:`IP_UBC_CONTROL`\\  FILE, VALUE or DEFAULT\n"
                ":type arg10: int\n"
                ":param arg11: initial model file (can be \"\") or value\n"
                ":type arg11: str\n"
                ":param arg12: Reference model type \\ :ref:`IP_UBC_CONTROL`\\  FILE, VALUE or DEFAULT\n"
                ":type arg12: int\n"
                ":param arg13: reference model file (can be \"\") or value(\n"
                ":type arg13: str\n"
                ":param arg14: Alphas type \\ :ref:`IP_UBC_CONTROL`\\  FILE, VALUE, LENGTH or DEFAULT\n"
                ":type arg14: int\n"
                ":param arg15: alphas  file (can be \"\"), value or length\n"
                ":type arg15: str\n"
                ":param arg16: weights file\n"
                ":type arg16: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   			  UBC Version 5 Control file.\n"
                "   			  \n\n"
               ).staticmethod("export_ubcip_control_v5");
    pyClass.def("export_ubc_res3", &GXIP_wrap_export_ubc_res3,
                "export_ubc_res3((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (str)arg6, (str)arg7, (float)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export of IP Resistivity data to UBC format.\n\n"

                ":param arg1: DB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Output line name\n"
                ":type arg2: str\n"
                ":param arg3: Output voltage channel name\n"
                ":type arg3: str\n"
                ":param arg4: Output current channel name\n"
                ":type arg4: str\n"
                ":param arg5: Output error channel name (\"\" for none)\n"
                ":type arg5: str\n"
                ":param arg6: Output OBS file name\n"
                ":type arg6: str\n"
                ":param arg7: Output TOPO file name\n"
                ":type arg7: str\n"
                ":param arg8: version number (3 or 5)\n"
                ":type arg8: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Outputs a \\ `*`\\ .DAT\" file of the survey data for use in the\n"
                "   				 UBC 2D inversion programme DCINV2D.\n"
                "   				 Voltage and current channels should be in units such that\n"
                "   				 V/I gives volts/amp (or mV/mA).\n"
                "   			 \n\n"
               );
    pyClass.def("export_ubc_res_control", &GXIP_wrap_export_ubc_res_control,
                "export_ubc_res_control((str)arg1, (int)arg2, (int)arg3, (float)arg4, (str)arg5, (str)arg6, (str)arg7, (str)arg8, (float)arg9, (str)arg10, (str)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a control file for using in the UBC DCINV2D programme.\n\n"

                ":param arg1: Output control file name\n"
                ":type arg1: str\n"
                ":param arg2: niter\n"
                ":type arg2: int\n"
                ":param arg3: irest\n"
                ":type arg3: int\n"
                ":param arg4: chifact\n"
                ":type arg4: float\n"
                ":param arg5: RES obs file\n"
                ":type arg5: str\n"
                ":param arg6: mesh file\n"
                ":type arg6: str\n"
                ":param arg7: topography file (required)\n"
                ":type arg7: str\n"
                ":param arg8: initial model file (can be \"\" or \"NULL\")\n"
                ":type arg8: str\n"
                ":param arg9: reference model conductivity\n"
                ":type arg9: float\n"
                ":param arg10: alphas\n"
                ":type arg10: str\n"
                ":param arg11: weights file\n"
                ":type arg11: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 UBC Version 3.\n"
                "   				 Outputs a control file for use in the\n"
                "   				 UBC 2D resistivity inversion programme DCINV2D.\n"
                "   				 Superceded by ExportUBCResControl2_IP, which has a selection for output version number.\n"
                "   			 \n\n"
               ).staticmethod("export_ubc_res_control");
    pyClass.def("export_ubc_res_control_v5", &GXIP_wrap_export_ubc_res_control_v5,
                "export_ubc_res_control_v5((str)arg1, (int)arg2, (float)arg3, (str)arg4, (str)arg5, (int)arg6, (str)arg7, (int)arg8, (str)arg9, (int)arg10, (str)arg11, (int)arg12, (str)arg13, (str)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a control file for using in the UBC DCINV2D programme.\n\n"

                ":param arg1: Output control file name\n"
                ":type arg1: str\n"
                ":param arg2: niter\n"
                ":type arg2: int\n"
                ":param arg3: chifact\n"
                ":type arg3: float\n"
                ":param arg4: RES obs file\n"
                ":type arg4: str\n"
                ":param arg5: topography file (required)\n"
                ":type arg5: str\n"
                ":param arg6: Mesh type \\ :ref:`IP_UBC_CONTROL`\\  FILE, VALUE or DEFAULT\n"
                ":type arg6: int\n"
                ":param arg7: mesh file (can be \"\") or value\n"
                ":type arg7: str\n"
                ":param arg8: Initial model type \\ :ref:`IP_UBC_CONTROL`\\  FILE, VALUE or DEFAULT\n"
                ":type arg8: int\n"
                ":param arg9: initial model file (can be \"\") or value\n"
                ":type arg9: str\n"
                ":param arg10: Reference model type \\ :ref:`IP_UBC_CONTROL`\\  FILE, VALUE or DEFAULT\n"
                ":type arg10: int\n"
                ":param arg11: reference model file (can be \"\") or value(\n"
                ":type arg11: str\n"
                ":param arg12: Alphas type \\ :ref:`IP_UBC_CONTROL`\\  FILE, VALUE, LENGTH or DEFAULT\n"
                ":type arg12: int\n"
                ":param arg13: alphas  file (can be \"\"), value or length\n"
                ":type arg13: str\n"
                ":param arg14: weights file\n"
                ":type arg14: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   UBC Version 5\n"
                "   			  Outputs a control file for use in the\n"
                "   UBC 2D resistivity inversion programme DCINV2D.\n\n"
               ).staticmethod("export_ubc_res_control_v5");
    pyClass.def("export_data_to_ubc_3d", &GXIP_wrap_export_data_to_ubc_3d,
                "export_data_to_ubc_3d((GXDB)arg1, (GXLST)arg2, (int)arg3, (int)arg4, (str)arg5, (str)arg6, (str)arg7, (int)arg8, (str)arg9, (str)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export of IP data to UBC 3D IP format.\n\n"

                ":param arg1: DB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Lines to export (Name, Symbol)\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: Locations only (0: No, 1: Yes)?\n"
                ":type arg3: int\n"
                ":param arg4: Include Z values (0: No, 1: Yes)?\n"
                ":type arg4: int\n"
                ":param arg5: IP channel name (can be \"\" if exporting locations only)\n"
                ":type arg5: str\n"
                ":param arg6: Error channel name (can be \"\" if exporting locations only)\n"
                ":type arg6: str\n"
                ":param arg7: Mask channel name (can be \"\")\n"
                ":type arg7: str\n"
                ":param arg8: IPTYPE (1: Vp, 2: Chargeability)\n"
                ":type arg8: int\n"
                ":param arg9: Comments (can be \"\")\n"
                ":type arg9: str\n"
                ":param arg10: Output OBS file name\n"
                ":type arg10: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "             Outputs a \\ `*`\\ .DAT\" file of the survey data for use in the\n"
                "             UBC IP 3D inversion programmes.\n"
                "           \n\n"
               );
    pyClass.def("import_ubc2_dmod", &GXIP_wrap_import_ubc2_dmod,
                "import_ubc2_dmod((str)arg1, (int)arg2) -> GXPG:\n"

                "\n.. parsed-literal::\n\n"
                "   Import a MOD file from the UBC IPINV2D programme.\n\n"

                ":param arg1: UBC MOD file name to import\n"
                ":type arg1: str\n"
                ":param arg2: 0 - CON, 1 - CHG\n"
                ":type arg2: int\n"
                ":returns: PG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXPG`\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Imports the MOD file values to a PG object.\n"
                "   The CON/CHG selection is necessary because the import sets\n"
                "   padding values to dummies based on the type of file.\n\n"
               ).staticmethod("import_ubc2_dmod");
    pyClass.def("import_ubc2_dmsh", &GXIP_wrap_import_ubc2_dmsh,
                "import_ubc2_dmsh((str)arg1, (float_ref)arg2, (float_ref)arg3, (GXVV)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import a MSH file from the UBC IPINV2D programme.\n\n"

                ":param arg1: UBC MSH file to import\n"
                ":type arg1: str\n"
                ":param arg2: Returned origin X (top left corner)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Returned origin Z (top left corner)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Cell widths  (left to right) (real)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Cell heights (top down) (real)\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Imports the MSH file geometry.\n\n"
               ).staticmethod("import_ubc2_dmsh");
    pyClass.def("import_ubc2_d_topo", &GXIP_wrap_import_ubc2_d_topo,
                "import_ubc2_d_topo((str)arg1, (float_ref)arg2, (GXVV)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import a Topography file from the UBC IPINV2D programme.\n\n"

                ":param arg1: UBC Topo file to import\n"
                ":type arg1: str\n"
                ":param arg2: Returned top of mesh elevation\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Topography X values\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Topography Z values (elevations)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Imports the maximum elevation (top of mesh)\n"
                "   as well as the topo (X, Z) values.\n\n"
               ).staticmethod("import_ubc2_d_topo");
    pyClass.def("open_job", &GXIP_wrap_open_job,
                "open_job((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Open a IP plotting job\n\n"

                ":param arg1: job file name\n"
                ":type arg1: str\n"
                ":param arg2: Job type \\ :ref:`IP_PLOT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               );
    pyClass.def("save_job", &GXIP_wrap_save_job,
                "save_job((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save a IP plotting job\n\n"

                ":param arg1: job file name\n"
                ":type arg1: str\n"
                ":param arg2: Job type  \\ :ref:`IP_PLOT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               );
    pyClass.def("trim_ubc2_d_model", &GXIP_wrap_trim_ubc2_d_model,
                "trim_ubc2_d_model((GXPG)arg1, (int)arg2, (int)arg3, (int)arg4, (GXVV)arg5, (GXVV)arg6, (float_ref)arg7) -> GXPG:\n"

                "\n.. parsed-literal::\n\n"
                "   Trim the padding cells from the UBC IPINV2D Model.\n\n"

                ":param arg1: Input model (unchanged)\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Cells to remove on left\n"
                ":type arg2: int\n"
                ":param arg3: Cells to remove on right\n"
                ":type arg3: int\n"
                ":param arg4: Cells to remove on the bottom\n"
                ":type arg4: int\n"
                ":param arg5: Column widths (modified)\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Row heights (modified)\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Top left corner X (modified)\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: PG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXPG`\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The cells are removed from the left, right and bottom.\n"
                "   The returned PG is the trimmed version.\n"
                "   The input cell size VVs are also trimmed to match,\n"
                "   and the origin is updated (still upper left corner).\n\n"
               ).staticmethod("trim_ubc2_d_model");
    pyClass.def("write_distant_electrodes", &GXIP_wrap_write_distant_electrodes,
                "write_distant_electrodes((GXDB)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write distant electrode locations to channels\n\n"

                ":param arg1: DB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Writes values for ALL lines.\n\n"
               );
    pyClass.def("write_distant_electrodes_lst", &GXIP_wrap_write_distant_electrodes_lst,
                "write_distant_electrodes_lst((GXDB)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write distant electrode locations to channels for a LST of lines\n\n"

                ":param arg1: DB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Lines to write out\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Writes values for lines in the input LST.\n\n"
               );
    pyClass.def("average_duplicates_qc", &GXIP_wrap_average_duplicates_qc,
                "average_duplicates_qc((GXDB)arg1, (str)arg2, (str)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Average duplicate samples in a database.\n\n"

                ":param arg1: Database to export from\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Mask or reference channel (required)\n"
                ":type arg2: str\n"
                ":param arg3: QC channel (can be left blank)\n"
                ":type arg3: str\n"
                ":param arg4: \\ :ref:`IP_DUPLICATE`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Averages all values with shared station and N values,\n"
                "   as long as the mask channel is defined at that FID.\n"
                "   Previous averaged values (IP_DATA_AVG) are overwritten according to the\n"
                "   overwrite flag.\n"
                "   If the QC channel is selected, only those rows of data where the QC channel\n"
                "   value is \"1\" will be included in the average.\n\n"
               );
    pyClass.def("create", &GXIP_wrap_create,
                "create() -> GXIP:\n"

                "\n.. parsed-literal::\n\n"
                "   Create IP.\n\n"

                ":returns: IP Object\n"
                ":rtype: :class:`geosoft.gxapi.GXIP`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("export_i2_x", &GXIP_wrap_export_i2_x,
                "export_i2_x((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (str)arg6, (str)arg7, (str)arg8, (str)arg9, (str)arg10, (str)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export line(s) to an Interpex RESIX I2X format file.\n\n"

                ":param arg1: Database to export from\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Name of the file\n"
                ":type arg2: str\n"
                ":param arg3: Name of the line\n"
                ":type arg3: str\n"
                ":param arg4: Resistivity (data) channel\n"
                ":type arg4: str\n"
                ":param arg5: IP (data) channel (can be \"\")\n"
                ":type arg5: str\n"
                ":param arg6: Image model resistivity channel (can be \"\")\n"
                ":type arg6: str\n"
                ":param arg7: Image model IP channel (can be \"\")\n"
                ":type arg7: str\n"
                ":param arg8: Image model synthetic resistivity channel (can be \"\")\n"
                ":type arg8: str\n"
                ":param arg9: Image model synthetic IP channel (can be \"\")\n"
                ":type arg9: str\n"
                ":param arg10: Resistivity (polygon) channel (can be \"\")\n"
                ":type arg10: str\n"
                ":param arg11: IP (polygon) channel (can be \"\")\n"
                ":type arg11: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Exports a line to an \".I2X\" file.\n\n"
               );
    pyClass.def("export_ipdata", &GXIP_wrap_export_ipdata,
                "export_ipdata((GXDB)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Exports data in the Geosoft IPDATA format.\n\n"

                ":param arg1: Database to export from\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Channel to export\n"
                ":type arg2: str\n"
                ":param arg3: Title for IPDATA files\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("export_ipdata_dir", &GXIP_wrap_export_ipdata_dir,
                "export_ipdata_dir((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Exports data in the Geosoft IPDATA format in the specified directory\n\n"

                ":param arg1: Database to export from\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Channel to export\n"
                ":type arg2: str\n"
                ":param arg3: Title for IPDATA files\n"
                ":type arg3: str\n"
                ":param arg4: Directory for IPDATA files\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               );
    pyClass.def("export_ipred", &GXIP_wrap_export_ipred,
                "export_ipred((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (int)arg5, (str)arg6, (float)arg7, (float)arg8, (int)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Exports pseudo-section in the Geosoft IPRED format.\n\n"

                ":param arg1: Database to export from\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Title for first line of file\n"
                ":type arg2: str\n"
                ":param arg3: Channel to process\n"
                ":type arg3: str\n"
                ":param arg4: File suffix (type)\n"
                ":type arg4: str\n"
                ":param arg5: \\ :ref:`IP_FILTER`\\ \n"
                ":type arg5: int\n"
                ":param arg6: The Fraser Filter weights\n"
                ":type arg6: str\n"
                ":param arg7: First Station position (rDUMMY for default)\n"
                ":type arg7: float\n"
                ":param arg8: Last Station position  (rDUMMY for default)\n"
                ":type arg8: float\n"
                ":param arg9: Maximum n spacing\n"
                ":type arg9: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Fraser Filter weights apply to each N expansion above,\n"
                "   and are listed as w1,w2,w3,...   Unspecified values beyond\n"
                "   the list's end are set to 1.0.\n\n"
               );
    pyClass.def("export_ipred_dir", &GXIP_wrap_export_ipred_dir,
                "export_ipred_dir((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (int)arg5, (str)arg6, (float)arg7, (float)arg8, (int)arg9, (str)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Exports pseudo-section in the Geosoft IPRED format in the specified directory\n\n"

                ":param arg1: Database to export from\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Title for first line of file\n"
                ":type arg2: str\n"
                ":param arg3: Channel to process\n"
                ":type arg3: str\n"
                ":param arg4: File suffix (type)\n"
                ":type arg4: str\n"
                ":param arg5: \\ :ref:`IP_FILTER`\\ \n"
                ":type arg5: int\n"
                ":param arg6: The Fraser Filter weights\n"
                ":type arg6: str\n"
                ":param arg7: First Station position (rDUMMY for default)\n"
                ":type arg7: float\n"
                ":param arg8: Last Station position  (rDUMMY for default)\n"
                ":type arg8: float\n"
                ":param arg9: Maximum n spacing\n"
                ":type arg9: int\n"
                ":param arg10: Directory to export to\n"
                ":type arg10: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Fraser Filter weights apply to each N expansion above,\n"
                "   and are listed as w1,w2,w3,...   Unspecified values beyond\n"
                "   the list's end are set to 1.0.\n\n"
               );
    pyClass.def("export_line_ipdata", &GXIP_wrap_export_line_ipdata,
                "export_line_ipdata((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Exports one line of data in the Geosoft IPDATA format.\n\n"

                ":param arg1: Database to export from\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line to export\n"
                ":type arg2: str\n"
                ":param arg3: Channel to export\n"
                ":type arg3: str\n"
                ":param arg4: Title for IPDATA files\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               );
    pyClass.def("export_sgdf", &GXIP_wrap_export_sgdf,
                "export_sgdf((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Exports data to a Scintrex Geophysical Data Format file.\n\n"

                ":param arg1: Database to export from\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: SGDF file to create\n"
                ":type arg2: str\n"
                ":param arg3: Time Domain channel or Frequency Amplitude Channel\n"
                ":type arg3: str\n"
                ":param arg4: Frequency Domain Phase channel (optional)\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_n_value_lst", &GXIP_wrap_get_n_value_lst,
                "get_n_value_lst((GXDB)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill a list with unique N values in selected lines.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: LST object\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               );
    pyClass.def("get_topo_line", &GXIP_wrap_get_topo_line,
                "get_topo_line((GXDB)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get topography values for a line.\n\n"

                ":param arg1: Database to import data to\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line name\n"
                ":type arg2: str\n"
                ":param arg3: Starting \"X\" (station) value (rDUMMY for default)\n"
                ":type arg3: float\n"
                ":param arg4: Ending \"X\" (station) value (rDUMMY for default)\n"
                ":type arg4: float\n"
                ":param arg5: \"X\" increment along the line (rDUMMY for default = half \"A\" separation)\n"
                ":type arg5: float\n"
                ":param arg6: Returned topography values\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If topography info is available, returns values calculated for\n"
                "   the input line. If no topography is available, returned values\n"
                "   will be dummies. Values between actual data are interpolated using\n"
                "   the Akima spline. Ends are extrapolated using the end data points.\n\n"
               );
    pyClass.def("get_chan_domain", &GXIP_wrap_get_chan_domain,
                "get_chan_domain((GXDB)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this channel registered as a Time or Frequency domain channel?\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: channel to check\n"
                ":type arg2: str\n"
                ":returns: \\ :ref:`IP_DOMAIN`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               );
    pyClass.def("get_chan_label", &GXIP_wrap_get_chan_label,
                "get_chan_label((str)arg1, (str_ref)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the default label and units for a given channel.\n\n"

                ":param arg1: Input channel\n"
                ":type arg1: str\n"
                ":param arg2: Returned label\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Returned units\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_chan_label");
    pyClass.def("get_channel_info", &GXIP_wrap_get_channel_info,
                "get_channel_info((GXDB)arg1, (str)arg2, (int_ref)arg3, (float_ref)arg4, (int_ref)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Time Windows or Frequency info from a channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: channel to check\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`IP_DOMAIN`\\ \n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Delay or Base Frequency\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Number of time windows or frequencies\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Time windows or frequencies\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"
               );
    pyClass.def("set_channel_info", &GXIP_wrap_set_channel_info,
                "set_channel_info((GXDB)arg1, (str)arg2, (int)arg3, (float)arg4, (int)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set Time Windows or Frequency info for a channel.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: channel to check\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`IP_DOMAIN`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Delay or Base Frequency\n"
                ":type arg4: float\n"
                ":param arg5: Number of time windows or frequencies\n"
                ":type arg5: int\n"
                ":param arg6: Time windows or frequencies\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"
               );
    pyClass.def("import_dump", &GXIP_wrap_import_dump,
                "import_dump((int)arg1, (GXDB)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports data from an IP instrument dump file.\n\n"

                ":param arg1: \\ :ref:`IP_SYS`\\ \n"
                ":type arg1: int\n"
                ":param arg2: DB Handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg3: Dump file name\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("import_grid", &GXIP_wrap_import_grid,
                "import_grid((GXDB)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports data from a grid\n\n"

                ":param arg1: Database to import data to\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: The name of the grid file, with decorations\n"
                ":type arg2: str\n"
                ":param arg3: The name of the channel to import to\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Data is imported to the specified channel.\n"
                "   The values are interpolated at each row's X and Y\n"
                "   positions.\n\n"
               );
    pyClass.def("import_i2_x", &GXIP_wrap_import_i2_x,
                "import_i2_x((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (str)arg6, (str)arg7, (str)arg8, (str)arg9, (str)arg10, (str)arg11, (int)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports an Interpex RESIX I2X format file to a line.\n\n"

                ":param arg1: Database to import to\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Name of file to import\n"
                ":type arg2: str\n"
                ":param arg3: Line to import to\n"
                ":type arg3: str\n"
                ":param arg4: Resistivity (data) channel\n"
                ":type arg4: str\n"
                ":param arg5: IP (data) channel (can be \"\")\n"
                ":type arg5: str\n"
                ":param arg6: Image model resistivity channel (can be \"\")\n"
                ":type arg6: str\n"
                ":param arg7: Image model IP channel (can be \"\")\n"
                ":type arg7: str\n"
                ":param arg8: Image model synthetic resistivity channel (can be \"\")\n"
                ":type arg8: str\n"
                ":param arg9: Image model synthetic IP channel (can be \"\")\n"
                ":type arg9: str\n"
                ":param arg10: Resistivity (polygon) channel (can be \"\")\n"
                ":type arg10: str\n"
                ":param arg11: IP (polygon) channel (can be \"\")\n"
                ":type arg11: str\n"
                ":param arg12: \\ :ref:`IP_I2XIMPMODE`\\ \n"
                ":type arg12: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Imports a single \".I2X\" file to a specified line.\n"
                "   If the line does not exist, it will be created.\n\n"
               );
    pyClass.def("import_i2_x_ex", &GXIP_wrap_import_i2_x_ex,
                "import_i2_x_ex((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (str)arg6, (str)arg7, (str)arg8, (str)arg9, (str)arg10, (str)arg11, (str)arg12, (str)arg13, (int)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXIP.import_i2_x`\\ , with Zonge data imported as well.\n\n"

                ":param arg1: Database to import to\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Name of file to import\n"
                ":type arg2: str\n"
                ":param arg3: Line to import to\n"
                ":type arg3: str\n"
                ":param arg4: Resistivity (data) channel\n"
                ":type arg4: str\n"
                ":param arg5: IP (data) channel (can be \"\")\n"
                ":type arg5: str\n"
                ":param arg6: Image model resistivity channel (can be \"\")\n"
                ":type arg6: str\n"
                ":param arg7: Image model IP channel (can be \"\")\n"
                ":type arg7: str\n"
                ":param arg8: Image model synthetic resistivity channel (can be \"\")\n"
                ":type arg8: str\n"
                ":param arg9: Image model synthetic IP channel (can be \"\")\n"
                ":type arg9: str\n"
                ":param arg10: Resistivity (polygon) channel (can be \"\")\n"
                ":type arg10: str\n"
                ":param arg11: IP (polygon) channel (can be \"\")\n"
                ":type arg11: str\n"
                ":param arg12: Zonge Resistivity channel (can be \"\")\n"
                ":type arg12: str\n"
                ":param arg13: Zonge IP channel (can be \"\")\n"
                ":type arg13: str\n"
                ":param arg14: \\ :ref:`IP_I2XIMPMODE`\\ \n"
                ":type arg14: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Imports a single \".I2X\" file to a specified line.\n"
                "   If the line does not exist, it will be created.\n\n"
               );
    pyClass.def("import_instrumentation_gdd", &GXIP_wrap_import_instrumentation_gdd,
                "import_instrumentation_gdd((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports an Instrumentation GDD format file.\n\n"

                ":param arg1: Database to import to\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: GDD file name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               );
    pyClass.def("import_ipdata", &GXIP_wrap_import_ipdata,
                "import_ipdata((GXDB)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports data in the Geosoft IPDATA format.\n\n"

                ":param arg1: Database to import to\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: IPDATA file name\n"
                ":type arg2: str\n"
                ":param arg3: Channel to import to\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("import_ipdata2", &GXIP_wrap_import_ipdata2,
                "import_ipdata2((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports data in the Geosoft IPDATA format - up to two arrays.\n\n"

                ":param arg1: Database to import to\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: IPDATA file name\n"
                ":type arg2: str\n"
                ":param arg3: Channel to import to (default is \"IP\")\n"
                ":type arg3: str\n"
                ":param arg4: (optional) Second channel to import to\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The second channel may be specified for frequency domain data sets\n"
                "   with two array channels; e.g. amplitude and phase, or real and\n"
                "   imaginary parts. If the second channel is specified, and no\n"
                "   time or frequncy information is specified in the header (using\n"
                "   the T= or F= fields) then the import is assumed to be frequency\n"
                "   domain.\n\n"
               );
    pyClass.def("import_ipred", &GXIP_wrap_import_ipred,
                "import_ipred((GXDB)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports data from the Geosoft IPRED format.\n\n"

                ":param arg1: Database to import to\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: File to import from\n"
                ":type arg2: str\n"
                ":param arg3: Channel to import\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This import produces a limited IP data set with no Current \"I\",\n"
                "   Voltage \"Vp\" or Apparent Resistivity \"ResApp\" values.\n\n"
               );
    pyClass.def("import_merge_ipred", &GXIP_wrap_import_merge_ipred,
                "import_merge_ipred((GXDB)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports IPRED data to an existing line.\n\n"

                ":param arg1: Database to import to\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: File to import from\n"
                ":type arg2: str\n"
                ":param arg3: Channel to import\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Exits with error if the line does not exist.\n"
                "   Data is merged on basis of Stn and N value.\n\n"
               );
    pyClass.def("import_sgdf", &GXIP_wrap_import_sgdf,
                "import_sgdf((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports data from a Scintrex Geophysical Data Format file.\n\n"

                ":param arg1: Database to import to\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: SGDF file name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("import_topo_csv", &GXIP_wrap_import_topo_csv,
                "import_topo_csv((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports topography data from a CSV line-station file\n\n"

                ":param arg1: Database to calculate topography for\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: The name of CSV file\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The elevation of each point in the current database\n"
                "   is interpolated from the input topography values.\n\n"
               );
    pyClass.def("import_topo_grid", &GXIP_wrap_import_topo_grid,
                "import_topo_grid((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports topography data from a grid\n\n"

                ":param arg1: Database to calculate topography for\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: The name of the grid file, with decorations\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The elevation of each point in the current database\n"
                "   is interpolated from the input topography grid.\n\n"
               );
    pyClass.def("import_zonge_avg", &GXIP_wrap_import_zonge_avg,
                "import_zonge_avg((GXDB)arg1, (str)arg2, (float)arg3, (int)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports a Zonge AVG format file.\n\n"

                ":param arg1: Database to import to\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: FLD file name\n"
                ":type arg2: str\n"
                ":param arg3: Line number (will be scaled if applicable)\n"
                ":type arg3: float\n"
                ":param arg4: \\ :ref:`IP_STNSCALE`\\ \n"
                ":type arg4: int\n"
                ":param arg5: Line, station multiplier (for IP_STNSCALE_VALUE)\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See \\ :func:`geosoft.gxapi.GXIP.import_zonge_fld`\\ \n\n"
               );
    pyClass.def("import_zonge_fld", &GXIP_wrap_import_zonge_fld,
                "import_zonge_fld((GXDB)arg1, (str)arg2, (int)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Imports a Zonge FLD format file.\n\n"

                ":param arg1: Database to import to\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: FLD file name\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`IP_STNSCALE`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Line, station multiplier (for IP_STNSCALE_VALUE)\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Zonge Line and Station numbers may not be the X or Y position\n"
                "   values, and a conversion is required.\n"
                "   The line direction is taken from the IP setup values.\n\n"
               );
    pyClass.def("new_xy_database", &GXIP_wrap_new_xy_database,
                "new_xy_database((GXDB)arg1, (GXDB)arg2, (GXVV)arg3, (str)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a subset database using a mask channel, \"N\" value\n\n"

                ":param arg1: DB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: New DB object\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg3: Channel list\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Mask channel\n"
                ":type arg4: str\n"
                ":param arg5: \"N\" Value\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   A mask channel can be used to select a subset of the data.\n"
                "   A single N value can also be selected (Dummy for all).\n\n"
               );
    pyClass.def("pseudo_plot", &GXIP_wrap_pseudo_plot,
                "pseudo_plot((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create pseudo-sections of a single line using a control file.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: \"IPPLOT\" INI file name\n"
                ":type arg2: str\n"
                ":param arg3: current line name\n"
                ":type arg3: str\n"
                ":param arg4: map name to create\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The control file is created using the IPPLTCON GX. It may then\n"
                "   be modified by hand as required.\n\n"
               );
    pyClass.def("pseudo_plot2", &GXIP_wrap_pseudo_plot2,
                "pseudo_plot2((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXIP.pseudo_plot`\\ , but specify a tag for grids created.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: \"IPPLOT\" INI file name\n"
                ":type arg2: str\n"
                ":param arg3: current line name\n"
                ":type arg3: str\n"
                ":param arg4: tag for created grids\n"
                ":type arg4: str\n"
                ":param arg5: map name to create\n"
                ":type arg5: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The control file is created using the IPPLTCON GX. It may then\n"
                "   be modified by hand as required.\n\n"
               );
    pyClass.def("pseudo_plot2_dir", &GXIP_wrap_pseudo_plot2_dir,
                "pseudo_plot2_dir((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXIP.pseudo_plot2`\\ , but with directory specified.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: \"IPPLOT\" INI file name\n"
                ":type arg2: str\n"
                ":param arg3: current line name\n"
                ":type arg3: str\n"
                ":param arg4: tag for created grids\n"
                ":type arg4: str\n"
                ":param arg5: map name to create\n"
                ":type arg5: str\n"
                ":param arg6: directory to create files\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The control file is created using the IPPLTCON GX. It may then\n"
                "   be modified by hand as required.\n\n"
               );
    pyClass.def("ps_stack", &GXIP_wrap_ps_stack,
                "ps_stack((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a stacked pseudo-section plot using a control file.\n\n"

                ":param arg1: DB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: channel to plot\n"
                ":type arg2: str\n"
                ":param arg3: \"IPPLOT\" INI file name\n"
                ":type arg3: str\n"
                ":param arg4: map name to create\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The control file is created using the IPSTAKCON GX. It may then\n"
                "   be modified by hand as required.\n\n"
               );
    pyClass.def("ps_stack2", &GXIP_wrap_ps_stack2,
                "ps_stack2((GXDB)arg1, (str)arg2, (str)arg3, (int)arg4, (str)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   As \\ :func:`geosoft.gxapi.GXIP.ps_stack`\\ , but select section spacing option.\n\n"

                ":param arg1: DB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: channel to plot\n"
                ":type arg2: str\n"
                ":param arg3: \"IPPLOT\" INI file name\n"
                ":type arg3: str\n"
                ":param arg4: \\ :ref:`IP_STACK_TYPE`\\ \n"
                ":type arg4: int\n"
                ":param arg5: map name to create\n"
                ":type arg5: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("ps_stack2_dir", &GXIP_wrap_ps_stack2_dir,
                "ps_stack2_dir((GXDB)arg1, (str)arg2, (str)arg3, (int)arg4, (str)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXIP.pseudo_plot2`\\ , but with directory specified.\n\n"

                ":param arg1: DB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: channel to plot\n"
                ":type arg2: str\n"
                ":param arg3: \"IPPLOT\" INI file name\n"
                ":type arg3: str\n"
                ":param arg4: \\ :ref:`IP_STACK_TYPE`\\ \n"
                ":type arg4: int\n"
                ":param arg5: map name to create\n"
                ":type arg5: str\n"
                ":param arg6: directory to create files\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               );
    pyClass.def("qc_chan_lst", &GXIP_wrap_qc_chan_lst,
                "qc_chan_lst((GXDB)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill a list with QC channels.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: LST object\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Searches for the following QC channels existing in a database:\n"
                "   QC, QC_RES.\n\n"
               );
    pyClass.def("recalculate", &GXIP_wrap_recalculate,
                "recalculate((GXDB)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Recalculate derived channel values.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function recalculates \"derived\" channel values from\n"
                "   \"core\" data.\n"
                "   1. Recalculates the \"STN\" and \"N\" channels, using the TX1,\n"
                "      TX2, RX1 and RX2 channels (depending on the system).\n"
                "   2. Recalculates the apparent resistivity \"ResCalc\",\n"
                "      average \"IP_Avg\" and metal factor \"MF\" channels\n"
                "   3. Recalculates the \"X\" and \"Y\" channels. One of these will\n"
                "      be equal to \"STN\", the other to the internally stored\n"
                "      line number for the current line.\n"
                "   4. Recalculate the \"Z\" channel, based on the current \"Topo\"\n"
                "      channel, and the \"N\" values.\n"
                "   \n"
                "   Warning: If you make a change to an electrode location, you\n"
                "   would have to call \\ :func:`geosoft.gxapi.GXIP.recalculate`\\ , then recalculate \"Topo\"\n"
                "   (since the X and Y values would have changed), then call\n"
                "   \\ :func:`geosoft.gxapi.GXIP.recalculate_z`\\ , since \"Z\" values are based on \"Topo\" values.\n\n"
               );
    pyClass.def("recalculate_ex", &GXIP_wrap_recalculate_ex,
                "recalculate_ex((GXDB)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Recalculate derived channel values, with option for including/excluding location calculations.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Recalculate XYZ locations (TRUE or FALSE)?\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See \\ :func:`geosoft.gxapi.GXIP.recalculate`\\ . This version allows you to suppress the recalculation of the\n"
                "   current X, Y and Z channel values from the station locations.\n\n"
               );
    pyClass.def("recalculate_z", &GXIP_wrap_recalculate_z,
                "recalculate_z((GXDB)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Recalculate Z channel values.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The \"Z\" channel values are calculated as follows:\n"
                "   If the \"Topo\" value is defined, then\n"
                "   Z = Topo - 0.5\\ `*`\\ N\\ `*`\\ A, where \"N\" is the N-spacing, and\n"
                "   A is the A-spacing. If the Topography is not defined, then\n"
                "   it is assumed to be equal to 0.\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXIP.recalculate`\\ \n\n"
               );
    pyClass.def("set_import_mode", &GXIP_wrap_set_import_mode,
                "set_import_mode((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   When importing data to a line, set append/overwrite mode.\n\n"

                ":param arg1: 0: Overwrite, 1: Append\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   By default, importing data overwrites existing data.\n"
                "   Call this function before doing the import in order\n"
                "   to append imported data to existing data.\n"
                "   \"Short\" data channels will be dummied to the existing\n"
                "   data length before the new data is appended.\n\n"
               );
    pyClass.def("window", &GXIP_wrap_window,
                "window((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Window an IP array channel to produce a normal channel.\n\n"

                ":param arg1: DB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: VA channel to use\n"
                ":type arg2: str\n"
                ":param arg3: New channel\n"
                ":type arg3: str\n"
                ":param arg4: Window list\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The array channels cannot be used directly to produce sections.\n"
                "   \\ :func:`geosoft.gxapi.GXIP.window`\\  allows the user to select one or more of the windows\n"
                "   and create a new channel. In time domain, if more than one channel\n"
                "   is selected a weighted sum is performed, according to window widths.\n"
                "   In frequency domain a simple sum is performed.\n"
                "   Window List Syntax:\n\n"
               );
    pyClass.def("winnow_chan_list", &GXIP_wrap_winnow_chan_list,
                "winnow_chan_list((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Removes obviously non-pseudo-section type channels from list.\n\n"

                ":param arg1: List of channels\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("winnow_chan_list");
    pyClass.def("winnow_chan_list2", &GXIP_wrap_winnow_chan_list2,
                "winnow_chan_list2((GXLST)arg1, (GXDB)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXIP.winnow_chan_list`\\ , but removes current X,Y,Z.\n\n"

                ":param arg1: List of channels\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: Database\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               ).staticmethod("winnow_chan_list2");
    pyClass.def("is_valid_line", &GXIP_wrap_is_valid_line,
                "is_valid_line((GXDB)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   See if a given database line is registered for the IP system\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line name\n"
                ":type arg2: str\n"
                ":returns: 1 if the line is a valid IP line, 0 if not\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"
               );
    pyClass.def("line_array_type", &GXIP_wrap_line_array_type,
                "line_array_type((GXDB)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the type of IP array for the input line. If necessary, first imports the specified line into the IP object\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line name\n"
                ":type arg2: str\n"
                ":returns: \\ :ref:`IP_ARRAY`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"
               );
    pyClass.def("a_spacing", &GXIP_wrap_a_spacing,
                "a_spacing((GXDB)arg1, (str)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the A-Spacing for the input line. If necessary, first imports the specified line into the IP object.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line name\n"
                ":type arg2: str\n"
                ":returns: The A-Spacing value. If there are multiple A-Spacings, the base or smallest value.\n"
                "          				 This value could be rDUMMY for some arrays (such as 3D) where no A-Spacing is explicitly defined.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"
               );
    pyClass.def("pldp_convention", &GXIP_wrap_pldp_convention,
                "pldp_convention() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the user's plot point convention for pole-dipole arrays.\n\n"

                ":returns: The user's PLDP plot point convention \\ :ref:`IP_PLDP_CONV`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"
               );
    pyClass.def("get_electrode_locations_and_mask_values", &GXIP_wrap_get_electrode_locations_and_mask_values,
                "get_electrode_locations_and_mask_values((GXDB)arg1, (str)arg2, (int)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get unique electrodes, along with current mask info.\n\n"

                ":param arg1: DB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line name (\"\" for all selected lines)\n"
                ":type arg2: str\n"
                ":param arg3: Electrode type. 0:Tx, 1:Rx\n"
                ":type arg3: int\n"
                ":param arg4: X locations\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Y locations\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Off-time QC channel values (\"QC\")\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: On-time QC channel values (\"QC_RES\")\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 The mask values are determined from the first row where a given electrode is found.\n"
                "   				 Values returned for all currently selected lines.\n"
                "   			 \n\n"
               );
    pyClass.def("set_electrode_mask_values", &GXIP_wrap_set_electrode_mask_values,
                "set_electrode_mask_values((GXDB)arg1, (str)arg2, (int)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set unique electrodes, along with current mask info.\n\n"

                ":param arg1: DB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line name (\"\" for all selected lines)\n"
                ":type arg2: str\n"
                ":param arg3: Electrode type. 0:Tx, 1:Rx\n"
                ":type arg3: int\n"
                ":param arg4: X locations\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Y locations\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Off-time QC channel values (\"QC\")\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: On-time QC channel values (\"QC_RES\")\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Mask values are set for all included electrode locations, currently selected lines.\n"
                "   			 \n\n"
               );

    scope().attr("IP_ARRAY_DPDP") = (int32_t)0;
    scope().attr("IP_ARRAY_PLDP") = (int32_t)1;
    scope().attr("IP_ARRAY_PLPL") = (int32_t)2;
    scope().attr("IP_ARRAY_GRAD") = (int32_t)3;
    scope().attr("IP_ARRAY_WENNER") = (int32_t)5;
    scope().attr("IP_ARRAY_SCHLUMBERGER") = (int32_t)6;
    scope().attr("IP_ARRAY_UNKNOWN") = (int32_t)7;
    scope().attr("IP_ARRAY_3D") = (int32_t)9;
    scope().attr("IP_ARRAY_3D_PLDP") = (int32_t)10;
    scope().attr("IP_ARRAY_3D_PLPL") = (int32_t)11;
    scope().attr("IP_CHANNELS_DISPLAYED") = (int32_t)0;
    scope().attr("IP_CHANNELS_SELECTED") = (int32_t)1;
    scope().attr("IP_CHANNELS_ALL") = (int32_t)2;
    scope().attr("IP_DOMAIN_NONE") = (int32_t)-1;
    scope().attr("IP_DOMAIN_TIME") = (int32_t)0;
    scope().attr("IP_DOMAIN_FREQUENCY") = (int32_t)1;
    scope().attr("IP_DOMAIN_BOTH") = (int32_t)2;
    scope().attr("IP_DUPLICATE_APPEND") = (int32_t)0;
    scope().attr("IP_DUPLICATE_OVERWRITE") = (int32_t)1;
    scope().attr("IP_FILTER_PANTLEG") = (int32_t)1;
    scope().attr("IP_FILTER_PANTLEGP") = (int32_t)2;
    scope().attr("IP_FILTER_PYRIAMID") = (int32_t)3;
    scope().attr("IP_FILTER_PYRIAMIDP") = (int32_t)4;
    scope().attr("IP_I2XIMPMODE_REPLACE") = (int32_t)0;
    scope().attr("IP_I2XIMPMODE_MERGE") = (int32_t)1;
    scope().attr("IP_I2XINV_IMAGE") = (int32_t)0;
    scope().attr("IP_I2XINV_ZONGE") = (int32_t)1;
    scope().attr("IP_LINES_DISPLAYED") = (int32_t)0;
    scope().attr("IP_LINES_SELECTED") = (int32_t)1;
    scope().attr("IP_LINES_ALL") = (int32_t)2;
    scope().attr("IP_PLOT_PSEUDOSECTION") = (int32_t)0;
    scope().attr("IP_PLOT_STACKEDSECTION") = (int32_t)1;
    scope().attr("IP_STACK_TYPE_MAP") = (int32_t)0;
    scope().attr("IP_STACK_TYPE_EQUAL") = (int32_t)1;
    scope().attr("IP_STACK_TYPE_GEOGRAPHIC") = (int32_t)2;
    scope().attr("IP_STNSCALE_NONE") = (int32_t)0;
    scope().attr("IP_STNSCALE_ASPACE") = (int32_t)1;
    scope().attr("IP_STNSCALE_VALUE") = (int32_t)2;
    scope().attr("IP_STNSCALE_FILE") = (int32_t)3;
    scope().attr("IP_SYS_IPDATA") = (int32_t)0;
    scope().attr("IP_SYS_IP2") = (int32_t)1;
    scope().attr("IP_SYS_IP6") = (int32_t)2;
    scope().attr("IP_SYS_IP10") = (int32_t)3;
    scope().attr("IP_SYS_SYSCALR2") = (int32_t)4;
    scope().attr("IP_SYS_IPR11") = (int32_t)5;
    scope().attr("IP_SYS_IPR12") = (int32_t)6;
    scope().attr("IP_SYS_PHOENIX") = (int32_t)7;
    scope().attr("IP_SYS_PHOENIX_V2") = (int32_t)8;
    scope().attr("IP_SYS_ELREC_PRO") = (int32_t)9;
    scope().attr("IP_UBC_CONTROL_NONE") = (int32_t)-1;
    scope().attr("IP_UBC_CONTROL_DEFAULT") = (int32_t)0;
    scope().attr("IP_UBC_CONTROL_FILE") = (int32_t)1;
    scope().attr("IP_UBC_CONTROL_VALUE") = (int32_t)2;
    scope().attr("IP_UBC_CONTROL_LENGTH") = (int32_t)3;
    scope().attr("IP_PLDP_CONV_CLOSE_RX") = (int32_t)0;
    scope().attr("IP_PLDP_CONV_MID_RX") = (int32_t)1;
    scope().attr("IP_PLDP_CONV_DISTANT_RX") = (int32_t)2;

}
