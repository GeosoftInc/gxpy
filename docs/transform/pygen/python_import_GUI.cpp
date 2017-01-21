#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline int32_t GXGUI_wrap_create_wnd_from_hwnd(HWND arg1)
{
    int32_t ret = GXGUI::create_wnd_from_hwnd(arg1);
    return ret;
}
inline void GXGUI_wrap_fft2_spec_filter(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXGUI::fft2_spec_filter(arg1, arg2);
}
inline int32_t GXGUI_wrap_get_parent_wnd()
{
    int32_t ret = GXGUI::get_parent_wnd();
    return ret;
}
inline void GXGUI_wrap_get_printer_lst(GXLSTPtr arg1)
{
    GXGUI::get_printer_lst(arg1);
}
inline int32_t GXGUI_wrap_get_window_state()
{
    WINDOW_STATE ret = GXGUI::get_window_state();
    return ret;
}
inline void GXGUI_wrap_set_window_state(int32_t arg1)
{
    GXGUI::set_window_state((WINDOW_STATE)arg1);
}
inline void GXGUI_wrap_get_window_position(int_ref& arg1, int_ref& arg2, int_ref& arg3, int_ref& arg4, int_ref& arg5)
{
    GXGUI::get_window_position(arg1, arg2, arg3, arg4, (WINDOW_STATE&)arg5);
}
inline void GXGUI_wrap_set_window_position(int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXGUI::set_window_position(arg1, arg2, arg3, arg4, (WINDOW_STATE)arg5);
}
inline void GXGUI_wrap_get_client_window_area(int_ref& arg1, int_ref& arg2, int_ref& arg3, int_ref& arg4)
{
    GXGUI::get_client_window_area(arg1, arg2, arg3, arg4);
}
inline void GXGUI_wrap_grid_stat_hist(const gx_string_type& arg1)
{
    GXGUI::grid_stat_hist(arg1);
}
inline void GXGUI_wrap_voxel_stat_hist(const gx_string_type& arg1)
{
    GXGUI::voxel_stat_hist(arg1);
}
inline int32_t GXGUI_wrap_color_form(int_ref& arg1, int32_t arg2)
{
    int32_t ret = GXGUI::color_form(arg1, arg2);
    return ret;
}
inline int32_t GXGUI_wrap_color_transform(GXITRPtr arg1, GXSTPtr arg2)
{
    int32_t ret = GXGUI::color_transform(arg1, arg2);
    return ret;
}
inline int32_t GXGUI_wrap_coord_sys_wizard(GXIPJPtr arg1, int32_t arg2, int32_t arg3, const gx_string_type& arg4, const gx_string_type& arg5)
{
    int32_t ret = GXGUI::coord_sys_wizard(arg1, arg2, (COORDSYS_MODE)arg3, arg4, arg5);
    return ret;
}
inline int32_t GXGUI_wrap_coord_sys_wizard_licensed(GXIPJPtr arg1, int32_t arg2, int32_t arg3, const gx_string_type& arg4, const gx_string_type& arg5)
{
    int32_t ret = GXGUI::coord_sys_wizard_licensed(arg1, arg2, (COORDSYS_MODE)arg3, arg4, arg5);
    return ret;
}
inline int32_t GXGUI_wrap_coord_sys_wizard_grid(GXIPJPtr arg1, GXIPJPtr arg2, int32_t arg3, int32_t arg4, const gx_string_type& arg5, const gx_string_type& arg6, int32_t arg7, int32_t arg8, float_ref& arg9, float_ref& arg10, float_ref& arg11, float_ref& arg12, float_ref& arg13)
{
    int32_t ret = GXGUI::coord_sys_wizard_grid(arg1, arg2, arg3, (COORDSYS_MODE)arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13);
    return ret;
}
inline int32_t GXGUI_wrap_database_type(const gx_string_type& arg1, str_ref& arg2)
{
    int32_t ret = GXGUI::database_type(arg1, arg2);
    return ret;
}
inline int32_t GXGUI_wrap_datamine_type(const gx_string_type& arg1, int_ref& arg2)
{
    int32_t ret = GXGUI::datamine_type(arg1, arg2);
    return ret;
}
inline int32_t GXGUI_wrap_export_xyz_template_editor(GXDBPtr arg1, const gx_string_type& arg2, int32_t arg3)
{
    int32_t ret = GXGUI::export_xyz_template_editor(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXGUI_wrap_export_xyz_template_editor_ex(GXEDBPtr arg1, str_ref& arg2)
{
    int32_t ret = GXGUI::export_xyz_template_editor_ex(arg1, arg2);
    return ret;
}
inline int32_t GXGUI_wrap_file_filter_index(const gx_string_type& arg1)
{
    FILE_FILTER ret = GXGUI::file_filter_index(arg1);
    return ret;
}
inline int32_t GXGUI_wrap_gcs_datum_warning_shp(const gx_string_type& arg1, GXIPJPtr arg2)
{
    int32_t ret = GXGUI::gcs_datum_warning_shp(arg1, arg2);
    return ret;
}
inline int32_t GXGUI_wrap_gcs_datum_warning_shpdb_ex(GXLSTPtr arg1, GXLSTPtr arg2, GXLSTPtr arg3, GXDBPtr arg4)
{
    int32_t ret = GXGUI::gcs_datum_warning_shpdb_ex(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXGUI_wrap_gcs_datum_warning_shp_ex(GXLSTPtr arg1, GXLSTPtr arg2, GXLSTPtr arg3, GXMVIEWPtr arg4)
{
    int32_t ret = GXGUI::gcs_datum_warning_shp_ex(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXGUI_wrap_get_area_of_interest(float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, GXPLYPtr arg5, GXIPJPtr arg6)
{
    AOI_RETURN_STATE ret = GXGUI::get_area_of_interest(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline int32_t GXGUI_wrap_get_area_of_interest_3d(float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, GXPLYPtr arg7, GXIPJPtr arg8)
{
    AOI_RETURN_STATE ret = GXGUI::get_area_of_interest_3d(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
    return ret;
}
inline void GXGUI_wrap_get_dat_defaults(int32_t arg1, int32_t arg2, str_ref& arg3, str_ref& arg4)
{
    GXGUI::get_dat_defaults((DAT_TYPE)arg1, (FILE_FORM)arg2, arg3, arg4);
}
inline void GXGUI_wrap_get_file_filter(int32_t arg1, str_ref& arg2, str_ref& arg3, str_ref& arg4, int_ref& arg5)
{
    GXGUI::get_file_filter((FILE_FILTER)arg1, arg2, arg3, arg4, (GS_DIRECTORY&)arg5);
}
inline void GXGUI_wrap_get_gs_directory(int32_t arg1, str_ref& arg2)
{
    GXGUI::get_gs_directory((GS_DIRECTORY)arg1, arg2);
}
inline int32_t GXGUI_wrap_browse_dir(const gx_string_type& arg1, const gx_string_type& arg2, str_ref& arg3)
{
    int32_t ret = GXGUI::browse_dir(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXGUI_wrap_color_transform_ex(GXITRPtr arg1, GXSTPtr arg2, int32_t arg3, int32_t arg4, str_ref& arg5)
{
    int32_t ret = GXGUI::color_transform_ex(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline int32_t GXGUI_wrap_cumulative_percent(str_ref& arg1, GXITRPtr arg2)
{
    int32_t ret = GXGUI::cumulative_percent(arg1, arg2);
    return ret;
}
inline int32_t GXGUI_wrap_dat_file_form(const gx_string_type& arg1, const gx_string_type& arg2, str_ref& arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    int32_t ret = GXGUI::dat_file_form(arg1, arg2, arg3, (DAT_TYPE)arg4, (FILE_FORM)arg5, arg6);
    return ret;
}
inline int32_t GXGUI_wrap_gen_file_form(const gx_string_type& arg1, GXVVPtr arg2, int32_t arg3, const gx_string_type& arg4, str_ref& arg5, int32_t arg6, int32_t arg7)
{
    int32_t ret = GXGUI::gen_file_form(arg1, arg2, (FILE_FILTER)arg3, arg4, arg5, (FILE_FORM)arg6, arg7);
    return ret;
}
inline int32_t GXGUI_wrap_import_drill_database_ado2(const gx_string_type& arg1, str_ref& arg2, str_ref& arg3, int_ref& arg4, GXREGPtr arg5)
{
    int32_t ret = GXGUI::import_drill_database_ado2(arg1, arg2, arg3, (DH_DATA&)arg4, arg5);
    return ret;
}
inline int32_t GXGUI_wrap_import_drill_database_esri(const gx_string_type& arg1, str_ref& arg2, str_ref& arg3, int_ref& arg4, bool arg5, GXREGPtr arg6)
{
    int32_t ret = GXGUI::import_drill_database_esri(arg1, arg2, arg3, (DH_DATA&)arg4, arg5, arg6);
    return ret;
}
inline int32_t GXGUI_wrap_import_drill_database_odbc(str_ref& arg1, str_ref& arg2, str_ref& arg3, int_ref& arg4, GXREGPtr arg5)
{
    int32_t ret = GXGUI::import_drill_database_odbc(arg1, arg2, arg3, (DH_DATA&)arg4, arg5);
    return ret;
}
inline int32_t GXGUI_wrap_import_drill_database_odbc_maxwell(str_ref& arg1, str_ref& arg2, str_ref& arg3, int_ref& arg4, GXREGPtr arg5)
{
    int32_t ret = GXGUI::import_drill_database_odbc_maxwell(arg1, arg2, arg3, (DH_DATA&)arg4, arg5);
    return ret;
}
inline int32_t GXGUI_wrap_import_ascii_wizard(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXGUI::import_ascii_wizard(arg1, arg2);
    return ret;
}
inline int32_t GXGUI_wrap_import_chem_database(const gx_string_type& arg1, const gx_string_type& arg2, str_ref& arg3, int32_t arg4)
{
    int32_t ret = GXGUI::import_chem_database(arg1, arg2, arg3, (IMPCH_TYPE)arg4);
    return ret;
}
inline int32_t GXGUI_wrap_import_chem_database_ado(const gx_string_type& arg1, const gx_string_type& arg2, str_ref& arg3, int32_t arg4)
{
    int32_t ret = GXGUI::import_chem_database_ado(arg1, arg2, arg3, (IMPCH_TYPE)arg4);
    return ret;
}
inline int32_t GXGUI_wrap_import_database(const gx_string_type& arg1, const gx_string_type& arg2, str_ref& arg3)
{
    int32_t ret = GXGUI::import_database(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXGUI_wrap_import_database_ado(const gx_string_type& arg1, const gx_string_type& arg2, str_ref& arg3)
{
    int32_t ret = GXGUI::import_database_ado(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXGUI_wrap_import_database_sql(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, str_ref& arg4)
{
    int32_t ret = GXGUI::import_database_sql(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXGUI_wrap_import_database_sqlado(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, str_ref& arg4)
{
    int32_t ret = GXGUI::import_database_sqlado(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXGUI_wrap_import_drill_database_ado(const gx_string_type& arg1, const gx_string_type& arg2, str_ref& arg3, int_ref& arg4, GXREGPtr arg5)
{
    int32_t ret = GXGUI::import_drill_database_ado(arg1, arg2, arg3, (DH_DATA&)arg4, arg5);
    return ret;
}
inline int32_t GXGUI_wrap_import_template_sql(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    int32_t ret = GXGUI::import_template_sql(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXGUI_wrap_import_template_sqlado(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    int32_t ret = GXGUI::import_template_sqlado(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXGUI_wrap_import_xyz_template_editor(GXDBPtr arg1, const gx_string_type& arg2, int32_t arg3, const gx_string_type& arg4)
{
    int32_t ret = GXGUI::import_xyz_template_editor(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXGUI_wrap_odbc_file_connect(const gx_string_type& arg1, str_ref& arg2, int32_t arg3, str_ref& arg4)
{
    int32_t ret = GXGUI::odbc_file_connect(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXGUI_wrap_symbol_form(str_ref& arg1, bool_ref& arg2, int_ref& arg3, int_ref& arg4, float_ref& arg5, float_ref& arg6, int_ref& arg7, int_ref& arg8)
{
    int32_t ret = GXGUI::symbol_form(arg1, arg2, (MVIEW_FONT_WEIGHT&)arg3, arg4, arg5, arg6, arg7, arg8);
    return ret;
}
inline int32_t GXGUI_wrap_meta_data_tool(GXMETAPtr arg1, int32_t arg2, int32_t arg3)
{
    int32_t ret = GXGUI::meta_data_tool(arg1, arg2, arg3);
    return ret;
}
inline void GXGUI_wrap_import_chem_wizard(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXGUI::import_chem_wizard(arg1, arg2, (IMPCH_TYPE)arg3);
}
inline void GXGUI_wrap_import_drill_wizard(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4, int_ref& arg5, GXREGPtr arg6)
{
    GXGUI::import_drill_wizard(arg1, arg2, arg3, arg4, (DH_DATA&)arg5, arg6);
}
inline void GXGUI_wrap_internet_trust()
{
    GXGUI::internet_trust();
}
inline int32_t GXGUI_wrap_pattern_form(int_ref& arg1, float_ref& arg2, int_ref& arg3, float_ref& arg4, int_ref& arg5, int_ref& arg6)
{
    int32_t ret = GXGUI::pattern_form(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline int32_t GXGUI_wrap_line_pattern_form(int_ref& arg1, float_ref& arg2, float_ref& arg3, int_ref& arg4)
{
    int32_t ret = GXGUI::line_pattern_form(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXGUI_wrap_two_panel_selection(GXLSTPtr arg1, GXLSTPtr arg2, const gx_string_type& arg3)
{
    int32_t ret = GXGUI::two_panel_selection(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXGUI_wrap_two_panel_selection2(GXLSTPtr arg1, GXLSTPtr arg2, const gx_string_type& arg3)
{
    int32_t ret = GXGUI::two_panel_selection2(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXGUI_wrap_two_panel_selection_ex(GXLSTPtr arg1, GXLSTPtr arg2, int32_t arg3, int32_t arg4, const gx_string_type& arg5)
{
    int32_t ret = GXGUI::two_panel_selection_ex(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline int32_t GXGUI_wrap_two_panel_selection_ex2(GXLSTPtr arg1, GXLSTPtr arg2, int32_t arg3, int32_t arg4, const gx_string_type& arg5, const gx_string_type& arg6)
{
    int32_t ret = GXGUI::two_panel_selection_ex2(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline void GXGUI_wrap_launch_single_geo_dotnetx_tool(const gx_string_type& arg1, const gx_string_type& arg2, GXMETAPtr arg3)
{
    GXGUI::launch_single_geo_dotnetx_tool(arg1, arg2, arg3);
}
inline void GXGUI_wrap_launch_geo_dotnetx_tool(const gx_string_type& arg1, const gx_string_type& arg2, GXMETAPtr arg3)
{
    GXGUI::launch_geo_dotnetx_tool(arg1, arg2, arg3);
}
inline void GXGUI_wrap_launch_geo_x_tool(const gx_string_type& arg1, const gx_string_type& arg2, GXMETAPtr arg3)
{
    GXGUI::launch_geo_x_tool(arg1, arg2, arg3);
}
inline void GXGUI_wrap_launch_single_geo_dotnetx_tool_ex(const gx_string_type& arg1, const gx_string_type& arg2, GXMETAPtr arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    GXGUI::launch_single_geo_dotnetx_tool_ex(arg1, arg2, arg3, (XTOOL_ALIGN)arg4, (XTOOL_DOCK)arg5, arg6, arg7);
}
inline void GXGUI_wrap_launch_geo_dotnetx_tool_ex(const gx_string_type& arg1, const gx_string_type& arg2, GXMETAPtr arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    GXGUI::launch_geo_dotnetx_tool_ex(arg1, arg2, arg3, (XTOOL_ALIGN)arg4, (XTOOL_DOCK)arg5, arg6, arg7);
}
inline void GXGUI_wrap_launch_geo_x_tool_ex(const gx_string_type& arg1, const gx_string_type& arg2, GXMETAPtr arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    GXGUI::launch_geo_x_tool_ex(arg1, arg2, arg3, (XTOOL_ALIGN)arg4, (XTOOL_DOCK)arg5, arg6, arg7);
}
inline void GXGUI_wrap_meta_data_viewer(GXMETAPtr arg1, int32_t arg2, int32_t arg3)
{
    GXGUI::meta_data_viewer(arg1, arg2, arg3);
}
inline void GXGUI_wrap_print_file(const gx_string_type& arg1)
{
    GXGUI::print_file(arg1);
}
inline void GXGUI_wrap_render_pattern(HDC arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, double arg7, int32_t arg8, double arg9, int32_t arg10, int32_t arg11, int32_t arg12, int32_t arg13, int32_t arg14)
{
    GXGUI::render_pattern(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14);
}
inline void GXGUI_wrap_render_line_pattern(HDC arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, double arg7, double arg8, int32_t arg9, int32_t arg10, int32_t arg11, int32_t arg12)
{
    GXGUI::render_line_pattern(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12);
}
inline void GXGUI_wrap_set_parent_wnd(int32_t arg1)
{
    GXGUI::set_parent_wnd(arg1);
}
inline void GXGUI_wrap_set_printer(const gx_string_type& arg1)
{
    GXGUI::set_printer(arg1);
}
inline void GXGUI_wrap_set_prog_always_on(bool arg1)
{
    GXGUI::set_prog_always_on(arg1);
}
inline void GXGUI_wrap_show_direct_hist(double arg1, double arg2, double arg3, double arg4, double arg5, int32_t arg6, GXVVPtr arg7)
{
    GXGUI::show_direct_hist(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXGUI_wrap_show_hist(GXSTPtr arg1)
{
    GXGUI::show_hist(arg1);
}
inline void GXGUI_wrap_simple_map_dialog(GXMAPPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXGUI::simple_map_dialog(arg1, arg2, arg3);
}
inline void GXGUI_wrap_thematic_voxel_info(GXVOXPtr arg1)
{
    GXGUI::thematic_voxel_info(arg1);
}
inline void GXGUI_wrap_show_3d_viewer_dialog(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXGUI::show_3d_viewer_dialog(arg1, arg2, arg3);
}

void gxPythonImportGXGUI()
{

    class_<GXGUI, boost::noncopyable> pyClass("GXGUI",
            "\n.. parsed-literal::\n\n"
            "   These are graphical functions that typically create a\n"
            "   dialog-style window for a specific function. Examples include\n"
            "   file import wizards, and the Histogram and Scatter tools.\n\n"
            , no_init);


    pyClass.def("create_wnd_from_hwnd", &GXGUI_wrap_create_wnd_from_hwnd,
                "create_wnd_from_hwnd((HWND)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a standard WND object from an HWND.\n\n"

                ":param arg1: HWND Handle\n"
                ":type arg1: :class:`geosoft.gxapi.HWND`\n"
                ":returns: x - WND object created\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The object returned must be destroyed by the\n"
                "   destroy object call.\n\n"
               ).staticmethod("create_wnd_from_hwnd");
    pyClass.def("fft2_spec_filter", &GXGUI_wrap_fft2_spec_filter,
                "fft2_spec_filter((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Interactive FFT2 radially averaged power spectrum filter\n\n"

                ":param arg1: Name of the input spectrum file\n"
                ":type arg1: str\n"
                ":param arg2: Name of the output control file\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("fft2_spec_filter");
    pyClass.def("get_parent_wnd", &GXGUI_wrap_get_parent_wnd,
                "get_parent_wnd() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the current parent window\n\n"

                ":returns: Parent window.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_parent_wnd");
    pyClass.def("get_printer_lst", &GXGUI_wrap_get_printer_lst,
                "get_printer_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets a list of all printers.\n\n"

                ":param arg1: List to place into\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_printer_lst");
    pyClass.def("get_window_state", &GXGUI_wrap_get_window_state,
                "get_window_state() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve the current state of the oasis Montaj window\n\n"

                ":returns: \\ :ref:`WINDOW_STATE`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("get_window_state");
    pyClass.def("set_window_state", &GXGUI_wrap_set_window_state,
                "set_window_state((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Changes the state of the oasis Montaj window\n\n"

                ":param arg1: \\ :ref:`WINDOW_STATE`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("set_window_state");
    pyClass.def("get_window_position", &GXGUI_wrap_get_window_position,
                "get_window_position((int_ref)arg1, (int_ref)arg2, (int_ref)arg3, (int_ref)arg4, (int_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the oasis Montaj window's position state\n\n"

                ":param arg1: Window left position\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Window top position\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Window right position\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Window bottom position\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: Window state \\ :ref:`WINDOW_STATE`\\ \n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("get_window_position");
    pyClass.def("set_window_position", &GXGUI_wrap_set_window_position,
                "set_window_position((int)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the oasis Montaj window's position and state\n\n"

                ":param arg1: Window left position\n"
                ":type arg1: int\n"
                ":param arg2: Window top position\n"
                ":type arg2: int\n"
                ":param arg3: Window right position\n"
                ":type arg3: int\n"
                ":param arg4: Window bottom position\n"
                ":type arg4: int\n"
                ":param arg5: Window state \\ :ref:`WINDOW_STATE`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("set_window_position");
    pyClass.def("get_client_window_area", &GXGUI_wrap_get_client_window_area,
                "get_client_window_area((int_ref)arg1, (int_ref)arg2, (int_ref)arg3, (int_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the location of the oasis montaj client window.\n\n"

                ":param arg1: X Min returned (0)\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Y Min returned (0)\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: X Max returned (width)\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Y Max returned (height)\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Returns the coordinates of the client window area (where MDI document windows are placed).\n"
                "   				 The returned coordinates are 0,0 for the minimum X and Y and the window width\n"
                "   				 width and height for the maximum X and Y.\n"
                "   			 \n\n"
               ).staticmethod("get_client_window_area");
    pyClass.def("grid_stat_hist", &GXGUI_wrap_grid_stat_hist,
                "grid_stat_hist((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display Histogram of grid\n\n"

                ":param arg1: Name of the grid to get stats from\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("grid_stat_hist");
    pyClass.def("voxel_stat_hist", &GXGUI_wrap_voxel_stat_hist,
                "voxel_stat_hist((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display Histogram of Voxel\n\n"

                ":param arg1: Name of the Voxel to get stats from\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("voxel_stat_hist");
    pyClass.def("color_form", &GXGUI_wrap_color_form,
                "color_form((int_ref)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Select a colour.\n\n"

                ":param arg1: Colour (modified)\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Ask about C_TRANSPARENT if white is selected (1: yes, 0: no)?\n"
                ":type arg2: int\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Colour value is set on input, and new value returned.\n"
                "   If the input colour type is C_TRANSPARENT, then the color\n"
                "   is set to white, if any other type is input the output is\n"
                "   guaranteed to be of the same type.\n"
                "   \n"
                "   If the third flag is ``True`` is used, then on exit, if white is\n"
                "   selected, the user is prompted: 'Do you want white (Yes) or\n"
                "   \"None\" (No) ?' and the colour is converted as requested.\n"
                "   If this is not the case, the C_TRANSPARENT is converted\n"
                "   to white (if \"Ok\" is selected) and no choice is offered.\n\n"
               ).staticmethod("color_form");
    pyClass.def("color_transform", &GXGUI_wrap_color_transform,
                "color_transform((GXITR)arg1, (GXST)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Define an ITR of up to 8 zones.\n\n"

                ":param arg1: ITR object (modified)\n"
                ":type arg1: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg2: ST object (input)\n"
                ":type arg2: :class:`geosoft.gxapi.GXST`\n"
                ":returns: 0 if OK\n"
                "          1 if user cancels\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The statistics object is required in order to determine\n"
                "   data ranges, percentiles, etc. Create it using\n"
                "   \\ :func:`geosoft.gxapi.GXST.create_exact`\\ , or be sure to enable histogram statistics.\n\n"
               ).staticmethod("color_transform");
    pyClass.def("coord_sys_wizard", &GXGUI_wrap_coord_sys_wizard,
                "coord_sys_wizard((GXIPJ)arg1, (int)arg2, (int)arg3, (str)arg4, (str)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch the coordinate system definition/display GUI.\n\n"

                ":param arg1: IPJ object\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: Editable IPJ (0:No, 1:Yes)\n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`COORDSYS_MODE`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Data source label\n"
                ":type arg4: str\n"
                ":param arg5: Data source\n"
                ":type arg5: str\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Launches the new GX.Net single-dialog coordinate system\n"
                "   definition dialog. The input IPJ is modified on return\n"
                "   if OK is selected (and the editable parameter is 1).\n"
                "   The \"Data source label\" and \"Data source\" is information displayed\n"
                "   in the dialog for the user to know where the IPJ came from (e.g. \"Grid: X.grd\")\n\n"
               ).staticmethod("coord_sys_wizard");
    pyClass.def("coord_sys_wizard_licensed", &GXGUI_wrap_coord_sys_wizard_licensed,
                "coord_sys_wizard_licensed((GXIPJ)arg1, (int)arg2, (int)arg3, (str)arg4, (str)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch the coordinate system definition/display GUI.\n\n"

                ":param arg1: IPJ object\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: Editable IPJ (0:No, 1:Yes)\n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`COORDSYS_MODE`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Data source label\n"
                ":type arg4: str\n"
                ":param arg5: Data source\n"
                ":type arg5: str\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXGUI.coord_sys_wizard_licensed`\\  but will always be editable. The other\n"
                "   method is not editable in the viewer while this one is.\n\n"
               ).staticmethod("coord_sys_wizard_licensed");
    pyClass.def("coord_sys_wizard_grid", &GXGUI_wrap_coord_sys_wizard_grid,
                "coord_sys_wizard_grid((GXIPJ)arg1, (GXIPJ)arg2, (int)arg3, (int)arg4, (str)arg5, (str)arg6, (int)arg7, (int)arg8, (float_ref)arg9, (float_ref)arg10, (float_ref)arg11, (float_ref)arg12, (float_ref)arg13) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch the coordinate system definition/display GUI.\n\n"

                ":param arg1: original grid IPJ object\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: source (target) grid IPJ object. This is supplied so the modified orientation can be calculated and displayed.\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg3: Editable IPJ (0:No, 1:Yes)\n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`COORDSYS_MODE`\\ \n"
                ":type arg4: int\n"
                ":param arg5: Data source label\n"
                ":type arg5: str\n"
                ":param arg6: Data source\n"
                ":type arg6: str\n"
                ":param arg7: Number of cells in X\n"
                ":type arg7: int\n"
                ":param arg8: Number of cells in Y\n"
                ":type arg8: int\n"
                ":param arg9: Grid orgin X (grid's own coordinate system)\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: Grid orgin Y (grid's own coordinate system)\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: Grid cell size X\n"
                ":type arg11: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg12: Grid cell size Y\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg13: Grid rotation angle (degrees CCW)\n"
                ":type arg13: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 - Ok\n"
                "          					 1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Same as \\ :func:`geosoft.gxapi.GXGUI.coord_sys_wizard_licensed`\\  but allows the original grid info to be adjusted\n"
                "   				 when projections on section or oriented plan grids are modified.\n"
                "   				 In the tool, it is the \"modified\" orientation required to keep the edited projection's grid\n"
                "   				 in the same location as it was in the target projection.\n"
                "   			 \n\n"
               ).staticmethod("coord_sys_wizard_grid");
    pyClass.def("database_type", &GXGUI_wrap_database_type,
                "database_type((str)arg1, (str_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the type string of an external DAO database.\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":param arg2: database type (returned)\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 - OK\n"
                "          -1 - Cancel\n"
                "          terminates on error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the file extension is \"mdb\", then an MSJET (Microsoft Access)\n"
                "   database is assumed. If the file name is \"ODBC\", then \"ODBC\" is\n"
                "   returned as the type. Otherwise, a dialog appears listing the\n"
                "   other valid DAO database types.\n\n"
               ).staticmethod("database_type");
    pyClass.def("datamine_type", &GXGUI_wrap_datamine_type,
                "datamine_type((str)arg1, (int_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the type of a Datamine file.\n\n"

                ":param arg1: File Name (for display purposes only)\n"
                ":type arg1: str\n"
                ":param arg2: \n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - OK\n"
                "          -1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Often, a Datamine file can be opened a number of different ways\n"
                "   (e.g. as a string file or a as wireframe (point) file.\n"
                "   The following function checks to see if there is a choice to be made\n"
                "   between types supported by Geosoft for import. If not, it just returns\n"
                "   the original type \"hint\" from Datamine. If there is a choice, it puts up\n"
                "   a dialog with the choices for the user to pick from.\n"
                "   Do a bit-wise AND with the returned type to determine the file type\n"
                "   (or the type selected).\n"
                "   \n"
                "   Currently supported overlapping types/choices:\n"
                "   \n"
                "   dmString\n"
                "   dmWireframePoint\n\n"
               ).staticmethod("datamine_type");
    pyClass.def("export_xyz_template_editor", &GXGUI_wrap_export_xyz_template_editor,
                "export_xyz_template_editor((GXDB)arg1, (str)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Allows the user to edit XYZ export template\n"
                "   using a complex dialog. The Template name\n"
                "   may change during editing.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Name of the Template (can change)\n"
                ":type arg2: str\n"
                ":param arg3: Size of the Template\n"
                ":type arg3: int\n"
                ":returns: 0 - OK\n"
                "          1 - Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Only uses the current DB. This function does\n"
                "   not exactly work as supposed to. Instead of using\n"
                "   the EDB handle passed to it, it only will use\n"
                "   the current DB. Please see ExportXYXTemplateEditorEx_GUI\n"
                "   for an updated function.\n\n"
               ).staticmethod("export_xyz_template_editor");
    pyClass.def("export_xyz_template_editor_ex", &GXGUI_wrap_export_xyz_template_editor_ex,
                "export_xyz_template_editor_ex((GXEDB)arg1, (str_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Allows the user to edit an XYZ export template\n"
                "   using a complex dialog. The template name\n"
                "   may change during editing.\n\n"

                ":param arg1: EDB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXEDB`\n"
                ":param arg2: Template name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 - OK\n"
                "          1 - Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Will use the EDB passed in. This function replaces\n"
                "   the 'buggy' function \\ :func:`geosoft.gxapi.GXGUI.export_xyz_template_editor`\\ .\n"
                "   This extended function actually uses the EDB handle\n"
                "   passed to it and not just the current DB.\n\n"
               ).staticmethod("export_xyz_template_editor_ex");
    pyClass.def("file_filter_index", &GXGUI_wrap_file_filter_index,
                "file_filter_index((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the FILE_FILTER_XXX value for a file filter string.\n\n"

                ":param arg1: Input filter string\n"
                ":type arg1: str\n"
                ":returns: \\ :ref:`FILE_FILTER`\\ , -1 if not found\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   For example, if \"Database (\\ `*`\\ .gdb)\" is input,\n"
                "   then the FILE_FILTER_GDB value is returned.\n\n"
               ).staticmethod("file_filter_index");
    pyClass.def("gcs_datum_warning_shp", &GXGUI_wrap_gcs_datum_warning_shp,
                "gcs_datum_warning_shp((str)arg1, (GXIPJ)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch the GCS Datum Warning dialogue for SHP files.\n\n"

                ":param arg1: Data source\n"
                ":type arg1: str\n"
                ":param arg2: IPJ object\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Runs the GCS Warning dialogue with one data source\n\n"
               ).staticmethod("gcs_datum_warning_shp");
    pyClass.def("gcs_datum_warning_shpdb_ex", &GXGUI_wrap_gcs_datum_warning_shpdb_ex,
                "gcs_datum_warning_shpdb_ex((GXLST)arg1, (GXLST)arg2, (GXLST)arg3, (GXDB)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch the GCS Datum Warning dialogue for SHP files (Database).\n\n"

                ":param arg1: Data source names\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: Corresponding datum names\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: Returned corresponding LDT names\n"
                ":type arg3: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg4: DB\n"
                ":type arg4: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Runs the GCS Warning dialogue with multiple data sources (Database)\n\n"
               ).staticmethod("gcs_datum_warning_shpdb_ex");
    pyClass.def("gcs_datum_warning_shp_ex", &GXGUI_wrap_gcs_datum_warning_shp_ex,
                "gcs_datum_warning_shp_ex((GXLST)arg1, (GXLST)arg2, (GXLST)arg3, (GXMVIEW)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch the GCS Datum Warning dialogue for SHP files.\n\n"

                ":param arg1: Data source names\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: Corresponding datum names\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: Returned corresponding LDT names\n"
                ":type arg3: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg4: MVIEW\n"
                ":type arg4: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Runs the GCS Warning dialogue with multiple data sources\n\n"
               ).staticmethod("gcs_datum_warning_shp_ex");
    pyClass.def("get_area_of_interest", &GXGUI_wrap_get_area_of_interest,
                "get_area_of_interest((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (GXPLY)arg5, (GXIPJ)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the current area of interest from the application.\n\n"

                ":param arg1: AOI Area Min X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: AOI Area Min Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: AOI Area Max X\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: AOI Area Max y\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: AOI Bounding PLY (Filled if available, otherwise empty)\n"
                ":type arg5: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg6: AOI Bounding IPJ\n"
                ":type arg6: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: \\ :ref:`AOI_RETURN_STATE`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Depending on what is currently visible on screen and\n"
                "   the defined coordinate system the user may be prompted\n"
                "   by a warning and optionaly cancel the process.\n\n"
               ).staticmethod("get_area_of_interest");
    pyClass.def("get_area_of_interest_3d", &GXGUI_wrap_get_area_of_interest_3d,
                "get_area_of_interest_3d((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (GXPLY)arg7, (GXIPJ)arg8) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the current area of interest from the application in 3D.\n\n"

                ":param arg1: AOI Area Min X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: AOI Area Min Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: AOI Area Min Z\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: AOI Area Max X\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: AOI Area Max y\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: AOI Area Max Z\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: AOI Bounding PLY (Filled if available, otherwise empty)\n"
                ":type arg7: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg8: AOI Bounding IPJ\n"
                ":type arg8: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: \\ :ref:`AOI_RETURN_STATE`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Depending on what is currently visible on screen and\n"
                "   the defined coordinate system the user may be prompted\n"
                "   by a warning and optionaly cancel the process.\n\n"
               ).staticmethod("get_area_of_interest_3d");
    pyClass.def("get_dat_defaults", &GXGUI_wrap_get_dat_defaults,
                "get_dat_defaults((int)arg1, (int)arg2, (str_ref)arg3, (str_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the user default extension and qualifier for grids/images.\n\n"

                ":param arg1: \\ :ref:`DAT_TYPE`\\ \n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`FILE_FORM`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Returned default extension (e.g. \"grd\")\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Returned default qualifier (e.g. \"GRD\")\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The default grid/image filters are normally stored in\n"
                "   \"MONTAJ.DEFAULT_XGD_IN\" and \"MONTAJ.DEFAULT_XGD_OUT\"\n"
                "   \n"
                "   If no filter is defined, or the filter is not found\n"
                "   then \"grd\" and \"GRD\" are returned as the default extension\n"
                "   and qualifier.\n\n"
               ).staticmethod("get_dat_defaults");
    pyClass.def("get_file_filter", &GXGUI_wrap_get_file_filter,
                "get_file_filter((int)arg1, (str_ref)arg2, (str_ref)arg3, (str_ref)arg4, (int_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the defined filter, mask, extension and directory for an input filter.\n\n"

                ":param arg1: \\ :ref:`FILE_FILTER`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Returned file filter string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Returned file mask string\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Returned file extension\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: \\ :ref:`GS_DIRECTORY`\\  Returned directory.\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the four parts of the file filter;\n"
                "   e.g. for FILE_FILTER_GDB it returns:\n"
                "   \n"
                "   Filter:    \"Database (\\ `*`\\ .gdb)\"\n"
                "   Mask:      \"\\ `*`\\ .gdb\"\n"
                "   Extension: \"gdb\"\n"
                "   Directory: \"GS_DIRECTORY_NONE\"\n"
                "   \n"
                "   This function is useful for constuction open/save dialog\n"
                "   file filters, especially in GX.Net functions.\n\n"
               ).staticmethod("get_file_filter");
    pyClass.def("get_gs_directory", &GXGUI_wrap_get_gs_directory,
                "get_gs_directory((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the directory path for value of GS_DIRECTORY.\n\n"

                ":param arg1: \\ :ref:`GS_DIRECTORY`\\  Returned directory.\n"
                ":type arg1: int\n"
                ":param arg2: Returned directory path\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works along with the \\ :func:`geosoft.gxapi.GXGUI.get_file_filter`\\  function. Note that\n"
                "   most values of FILE_FILTER_XXX will return GS_DIRECTORY_NONE,\n"
                "   and give the current workspace directory.\n"
                "   \n"
                "   This function is useful for constuction open/save dialog\n"
                "   file filters, especially in GX.Net functions.\n\n"
               ).staticmethod("get_gs_directory");
    pyClass.def("browse_dir", &GXGUI_wrap_browse_dir,
                "browse_dir((str)arg1, (str)arg2, (str_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Browses for a specific directory.\n\n"

                ":param arg1: Title of the Form\n"
                ":type arg1: str\n"
                ":param arg2: Default path (Can be \"\")\n"
                ":type arg2: str\n"
                ":param arg3: Result Path Buffer (default on input)\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("browse_dir");
    pyClass.def("color_transform_ex", &GXGUI_wrap_color_transform_ex,
                "color_transform_ex((GXITR)arg1, (GXST)arg2, (int)arg3, (int)arg4, (str_ref)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Define an ITR of up to 12 zones, with file load/save buttons.\n\n"

                ":param arg1: ITR object (modified)\n"
                ":type arg1: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg2: ST object (input)\n"
                ":type arg2: :class:`geosoft.gxapi.GXST`\n"
                ":param arg3: Max number of zones (8 or 12)\n"
                ":type arg3: int\n"
                ":param arg4: Show file load/save buttons (TRUE or FALSE)?\n"
                ":type arg4: int\n"
                ":param arg5: Default colour transform file name\n"
                ":type arg5: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 if OK\n"
                "          1 if user cancels\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The statistics object is required in order to determine\n"
                "   data ranges, percentiles, etc. Create it using\n"
                "   \\ :func:`geosoft.gxapi.GXST.create_exact`\\ , or be sure to enable histogram statistics.\n"
                "   The colour transform file name is used as the default when the save\n"
                "   button is pushed, and is updated both after the load and save buttons\n"
                "   are pushed by the value input or selected by the user.\n\n"
               ).staticmethod("color_transform_ex");
    pyClass.def("cumulative_percent", &GXGUI_wrap_cumulative_percent,
                "cumulative_percent((str_ref)arg1, (GXITR)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Define a percent-based ITR of up to 12 zones.\n\n"

                ":param arg1: Default colour transform file name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: ITR object (returned)\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: 0 if OK\n"
                "          1 if user cancels\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The ITR values are interpreted as cumulative percent values, using\n"
                "   the \"PERCENT=1\" value in the ITR's REG.\n"
                "   \n"
                "   Note that processes using ITRs do not automatically know to convert between\n"
                "   percent values and \"actual\" data values. The REG \"PERCENT\" value is simply\n"
                "   a flag to indicate to a user that the values are intended to be in the range\n"
                "   from 0 < x < 100. The ITR should not, therefore, be applied directly to data\n"
                "   unless that data is already given in percent.\n"
                "   \n"
                "   If the file name is defined on input, the initial ITR will be loaded from it.\n"
                "   If it is left blank, a default 5-colour transform with\n"
                "   The colour transform file name is used as the default when the save\n"
                "   button is pushed, and is updated both after the load and save buttons\n"
                "   are pushed by the value input or selected by the user.\n\n"
               ).staticmethod("cumulative_percent");
    pyClass.def("dat_file_form", &GXGUI_wrap_dat_file_form,
                "dat_file_form((str)arg1, (str)arg2, (str_ref)arg3, (int)arg4, (int)arg5, (int)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Grid and Image file Open/Save Form for Multiple/Single file selections\n\n"

                ":param arg1: Title of the Form\n"
                ":type arg1: str\n"
                ":param arg2: Default value\n"
                ":type arg2: str\n"
                ":param arg3: Where the file name(s) is returned\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: \\ :ref:`DAT_TYPE`\\ \n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`FILE_FORM`\\ \n"
                ":type arg5: int\n"
                ":param arg6: Allow Multiple file selections = TRUE Single   file selections = FALSE\n"
                ":type arg6: int\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Remember to make the string size big enough for multiple file\n"
                "   selections. In the case of multiple selections the names will be separated\n"
                "   by a semicolon and only the first file will contain the full path.\n"
                "   \n"
                "   When using the multiple flag on any of these functions please be aware that\n"
                "   the string returned will be in the format:\n"
                "   drive:\\path1\\path2\\name.grid\\ `|`\\ name2.grid\\ `|`\\ name3.grid(QUALIFIERS)\n"
                "   All grids are required to be of the same type.\n\n"
               ).staticmethod("dat_file_form");
    pyClass.def("gen_file_form", &GXGUI_wrap_gen_file_form,
                "gen_file_form((str)arg1, (GXVV)arg2, (int)arg3, (str)arg4, (str_ref)arg5, (int)arg6, (int)arg7) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   General file Open/Save Form for Multiple/Single file selections and multiple filter capability\n\n"

                ":param arg1: Title of the Form\n"
                ":type arg1: str\n"
                ":param arg2: INT VV of file filters to use \\ :ref:`FILE_FILTER`\\  The first one is default, can pass (VV) 0 for to use next parameter.\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: \\ :ref:`FILE_FILTER`\\  (ignored if parameter above is not zero)\n"
                ":type arg3: int\n"
                ":param arg4: Default value\n"
                ":type arg4: str\n"
                ":param arg5: Where the file name(s) is returned\n"
                ":type arg5: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg6: \\ :ref:`FILE_FORM`\\ \n"
                ":type arg6: int\n"
                ":param arg7: Allow Multiple file selections = TRUE Single   file selections = FALSE\n"
                ":type arg7: int\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Remember to make the string size big enough for multiple file\n"
                "   selections. In the case of multiple selections the names will be separated\n"
                "   by a semicolon and only the first file will contain the full path.\n"
                "   \n"
                "   Defined Functions     The following four functions are handy defines and simply pass the appropriate\n"
                "   parameter.\n"
                "   \n"
                "   iFileOpen_GUI\n"
                "   iFileSave_GUI\n"
                "   iMultiFileOpen_GUI\n"
                "   iMultiFileSave_GUI\n\n"
               ).staticmethod("gen_file_form");
    pyClass.def("import_drill_database_ado2", &GXGUI_wrap_import_drill_database_ado2,
                "import_drill_database_ado2((str)arg1, (str_ref)arg2, (str_ref)arg3, (int_ref)arg4, (GXREG)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXGUI.import_drill_database_ado`\\ , but template name is returned.\n\n"

                ":param arg1: External database connection string (Blank for OLEDB Wizard)\n"
                ":type arg1: str\n"
                ":param arg2: template to make (if left blank, the created template name is returned)\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Name of table\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Type of import returned \\ :ref:`DH_DATA`\\ \n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: Drill Hole Object REG handle\n"
                ":type arg5: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: 0 - OK\n"
                "          -1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If it is not defined on input, the template name is set\n"
                "   to be the Wholeplot table name; e.g.\n"
                "   \"HOLESURVEY.i4\" for \"Project_HOLESURVEY\"\n\n"
               ).staticmethod("import_drill_database_ado2");
    pyClass.def("import_drill_database_esri", &GXGUI_wrap_import_drill_database_esri,
                "import_drill_database_esri((str)arg1, (str_ref)arg2, (str_ref)arg3, (int_ref)arg4, (bool)arg5, (GXREG)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as iImportDrillDatabaseADO2_GUI, but from an ArcGIS Geodatabase\n\n"

                ":param arg1: External database connection string  (e.g. \"d:\\\\Personal\\\\test.mdb\\ `|`\\ Table\" or \"d:\\\\File\\\\test.gdb\\ `|`\\ TableX\\ `|`\\ FeatureClassY)\"\n"
                ":type arg1: str\n"
                ":param arg2: template to make (if left blank, the created template name is returned)\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Name of table\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Type of import returned \\ :ref:`DH_DATA`\\ \n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: bool Geosoft Geochemistry Database?\n"
                ":type arg5: bool\n"
                ":param arg6: Drill Hole Object REG handle\n"
                ":type arg6: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: 0 - OK\n"
                "          -1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If it is not defined on input, the template name is set\n"
                "   to be the Wholeplot table name; e.g.\n"
                "   \"HOLESURVEY.i4\" for \"Project_HOLESURVEY\"\n\n"
               ).staticmethod("import_drill_database_esri");
    pyClass.def("import_drill_database_odbc", &GXGUI_wrap_import_drill_database_odbc,
                "import_drill_database_odbc((str_ref)arg1, (str_ref)arg2, (str_ref)arg3, (int_ref)arg4, (GXREG)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a template file for importing drill holes\n"
                "   from ODBC database data.\n\n"

                ":param arg1: connection string\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: template to make\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Name of table\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Type of import returned \\ :ref:`DH_DATA`\\ \n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: Drill Hole Object REG handle\n"
                ":type arg5: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: 0 - OK\n"
                "          -1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the input connection string is empty (\"\"), then the ODBC connection dialogs\n"
                "   will appear (e.g. to connect to a machine database) before the import wizard\n"
                "   is run. The connect string used for this connection is then returned.\n"
                "   This string can then be used on input to skip the ODBC connection dialogs and\n"
                "   go straight to the Wholeplot import wizard.\n"
                "   Because the name of the database is not necessarily known, the template name is created\n"
                "   from the name of the table opened - e.g. \"HOLELOCATION.i4\".\n\n"
               ).staticmethod("import_drill_database_odbc");
    pyClass.def("import_drill_database_odbc_maxwell", &GXGUI_wrap_import_drill_database_odbc_maxwell,
                "import_drill_database_odbc_maxwell((str_ref)arg1, (str_ref)arg2, (str_ref)arg3, (int_ref)arg4, (GXREG)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXGUI.import_drill_database_odbc`\\  but customized for Maxwell.\n\n"

                ":param arg1: connection string\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: template to make\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Name of table\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Type of import returned \\ :ref:`DH_DATA`\\ \n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: Drill Hole Object REG handle\n"
                ":type arg5: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: 0-OK 1-Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXGUI.import_drill_database_odbc`\\  but customized for Maxwell.\n\n"
               ).staticmethod("import_drill_database_odbc_maxwell");
    pyClass.def("import_ascii_wizard", &GXGUI_wrap_import_ascii_wizard,
                "import_ascii_wizard((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a template file from a gui.\n\n"

                ":param arg1: data file name\n"
                ":type arg1: str\n"
                ":param arg2: template to make\n"
                ":type arg2: str\n"
                ":returns: 0 - OK\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("import_ascii_wizard");
    pyClass.def("import_chem_database", &GXGUI_wrap_import_chem_database,
                "import_chem_database((str)arg1, (str)arg2, (str_ref)arg3, (int)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a template file for importing Geochems Database.\n\n"

                ":param arg1: data file name\n"
                ":type arg1: str\n"
                ":param arg2: template to make\n"
                ":type arg2: str\n"
                ":param arg3: Name of table\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: \\ :ref:`IMPCH_TYPE`\\ \n"
                ":type arg4: int\n"
                ":returns: 0 - OK\n"
                "          -1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("import_chem_database");
    pyClass.def("import_chem_database_ado", &GXGUI_wrap_import_chem_database_ado,
                "import_chem_database_ado((str)arg1, (str)arg2, (str_ref)arg3, (int)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Improved template creation for importing geochem database (ADO).\n\n"

                ":param arg1: External database connection string (Blank for OLEDB Wizard)\n"
                ":type arg1: str\n"
                ":param arg2: template to make\n"
                ":type arg2: str\n"
                ":param arg3: Name of table\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: \\ :ref:`IMPCH_TYPE`\\ \n"
                ":type arg4: int\n"
                ":returns: 0 - OK\n"
                "          -1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This is an improved version of ImportChemDatabase_GUI using the\n"
                "   new ADO technology, as opposed to DAO. Use in conjuction with\n"
                "   \\ :func:`geosoft.gxapi.GXDU.import_ado`\\ . See also ImportDatabaseADO_GUI.\n\n"
               ).staticmethod("import_chem_database_ado");
    pyClass.def("import_database", &GXGUI_wrap_import_database,
                "import_database((str)arg1, (str)arg2, (str_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create template to import an external database table.\n\n"

                ":param arg1: External database file name\n"
                ":type arg1: str\n"
                ":param arg2: Template to make\n"
                ":type arg2: str\n"
                ":param arg3: Name of table imported (returned)\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 - OK\n"
                "          -1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This is used to select a single database table, and\n"
                "   selected fields from that table. If the database is not\n"
                "   Microsoft Access (type .mdb), an introductory dialog\n"
                "   requests the file type.\n"
                "   This function DOES NOT import the table itself, but\n"
                "   creates an import template which may be used to import\n"
                "   the table (see \\ :func:`geosoft.gxapi.GXDU.import_dao`\\ ()).\n\n"
               ).staticmethod("import_database");
    pyClass.def("import_database_ado", &GXGUI_wrap_import_database_ado,
                "import_database_ado((str)arg1, (str)arg2, (str_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create template to import an external database table (ADO Version).\n\n"

                ":param arg1: External database connection string (Blank for OLEDB Wizard)\n"
                ":type arg1: str\n"
                ":param arg2: Template to make\n"
                ":type arg2: str\n"
                ":param arg3: Name of table imported (returned)\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 - OK\n"
                "          -1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   1. This is used to select a single database table, and\n"
                "      selected fields from that table.\n"
                "   \n"
                "   2. This function DOES NOT import the table itself, but\n"
                "      creates an import template which may be used to import\n"
                "      the table (see \\ :func:`geosoft.gxapi.GXDU.import_ado`\\ ()).\n"
                "   \n"
                "   3. If connection string is of type \"FILENAME=...\" the connection will attempt to resolve\n"
                "      it as a file database. (see also ODBCFileConnect_GUI)\n\n"
               ).staticmethod("import_database_ado");
    pyClass.def("import_database_sql", &GXGUI_wrap_import_database_sql,
                "import_database_sql((str)arg1, (str)arg2, (str)arg3, (str_ref)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create template to import an external database table,\n"
                "   created using SQL.\n\n"

                ":param arg1: External database file name\n"
                ":type arg1: str\n"
                ":param arg2: Text file with SQL queries to use, (\"\" - get from database)\n"
                ":type arg2: str\n"
                ":param arg3: Import template to make\n"
                ":type arg3: str\n"
                ":param arg4: Name of table imported (returned)\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 - OK\n"
                "          -1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   1. This is used to build an Oasis montaj group (line) from\n"
                "      one or more database tables and fields, by selecting from\n"
                "      one or more SQL selection queries. The list of queries\n"
                "      is read from a text file with the following syntax:\n"
                "   \n"
                "      Query_Name_1\n"
                "      Query...\n"
                "      Query... (continued)\n"
                "      ...\n"
                "      ...\n"
                "      END_QUERY\n"
                "      Query_Name_2\n"
                "      etc.\n"
                "   \n"
                "   2. Each query has a title line, the query itself, then the\n"
                "      \"END_QUERY\" line to finish.  The title of a subsequent query\n"
                "      is on the line after an \"END_QUERY\" line.\n"
                "   \n"
                "   3. If the text file parameter is left blank (\"\"), then\n"
                "      selection queries in the database itself are listed.\n"
                "      In addition to the pre-defined queries, there is a\n"
                "      \"User Defined\" query which may be filled in by the user.\n"
                "   \n"
                "   4. This function DOES NOT import the table itself, but\n"
                "      creates an import template which may be used to import\n"
                "      the data (see \\ :func:`geosoft.gxapi.GXDU.import_dao`\\ ()).\n"
                "   \n"
                "   5. If connection string is of type \"FILENAME=...\" the connection will attempt to resolve\n"
                "      it as a file database. (see also ODBCFileConnect_GUI)\n\n"
               ).staticmethod("import_database_sql");
    pyClass.def("import_database_sqlado", &GXGUI_wrap_import_database_sqlado,
                "import_database_sqlado((str)arg1, (str)arg2, (str)arg3, (str_ref)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create template to import an external database table,\n"
                "   created using SQL (New ADO Version).\n\n"

                ":param arg1: External database connection string (Blank for OLEDB Wizard)\n"
                ":type arg1: str\n"
                ":param arg2: Text file with SQL queries to use, (\"\" - get from database)\n"
                ":type arg2: str\n"
                ":param arg3: Import template to make\n"
                ":type arg3: str\n"
                ":param arg4: Name of table imported (returned)\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 - OK\n"
                "          -1 Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This is used to build an Oasis montaj group (line) from\n"
                "   one or more database tables and fields, by selecting from\n"
                "   one or more SQL selection queries. The list of queries\n"
                "   is read from a text file with the following syntax:\n"
                "   \n"
                "   Query_Name_1\n"
                "   Query...\n"
                "   Query... (continued)\n"
                "   ...\n"
                "   ...\n"
                "   END_QUERY\n"
                "   Query_Name_2\n"
                "   etc.\n"
                "   \n"
                "   Each query has a title line, the query itself, then the\n"
                "   \"END_QUERY\" line to finish.  The title of a subsequent query\n"
                "   is on the line after an \"END_QUERY\" line.\n"
                "   \n"
                "   If the text file parameter is left blank (\"\"), then\n"
                "   selection queries in the database itself are listed.\n"
                "   In addition to the pre-defined queries, there is a\n"
                "   \"User Defined\" query which may be filled in by the user.\n"
                "   \n"
                "   This function DOES NOT import the table itself, but\n"
                "   creates an import template which may be used to import\n"
                "   the data (see \\ :func:`geosoft.gxapi.GXDU.import_dao`\\ ()).\n\n"
               ).staticmethod("import_database_sqlado");
    pyClass.def("import_drill_database_ado", &GXGUI_wrap_import_drill_database_ado,
                "import_drill_database_ado((str)arg1, (str)arg2, (str_ref)arg3, (int_ref)arg4, (GXREG)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a template file for importing drill holes.\n\n"

                ":param arg1: External database connection string (Blank for OLEDB Wizard)\n"
                ":type arg1: str\n"
                ":param arg2: template to make\n"
                ":type arg2: str\n"
                ":param arg3: Name of table\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Type of import returned \\ :ref:`DH_DATA`\\ \n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: Drill Hole Object REG handle\n"
                ":type arg5: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: 0 - OK\n"
                "          -1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This is an improved version of ImportDrillDatabase_GUI using the\n"
                "   new ADO technology, as opposed to DAO. Use in conjuction with\n"
                "   \\ :func:`geosoft.gxapi.GXDU.import_ado`\\ . See also ImportDatabaseADO_GUI.\n\n"
               ).staticmethod("import_drill_database_ado");
    pyClass.def("import_template_sql", &GXGUI_wrap_import_template_sql,
                "import_template_sql((str)arg1, (str)arg2, (str)arg3, (str)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create template to import an external database table; provide query.\n\n"

                ":param arg1: External database file name\n"
                ":type arg1: str\n"
                ":param arg2: Import template to make\n"
                ":type arg2: str\n"
                ":param arg3: SQL selection query to run on database\n"
                ":type arg3: str\n"
                ":param arg4: Name of Oasis table to create\n"
                ":type arg4: str\n"
                ":returns: 0 - OK\n"
                "          -1 Cancel\n"
                "          terminates on error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This is similar to ImportDatabaseSQL_GUI, but dispenses with\n"
                "   the dialog offering a selection of queries. Instead, the\n"
                "   user supplies the query as a string.\n"
                "   \n"
                "   This function DOES NOT import the table itself, but\n"
                "   creates an import template which may be used to import\n"
                "   the data (see \\ :func:`geosoft.gxapi.GXDU.import_dao`\\ ()).\n\n"
               ).staticmethod("import_template_sql");
    pyClass.def("import_template_sqlado", &GXGUI_wrap_import_template_sqlado,
                "import_template_sqlado((str)arg1, (str)arg2, (str)arg3, (str)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create template to import an external database table; provide query.\n\n"

                ":param arg1: External database connection string (Blank for OLEDB Wizard)\n"
                ":type arg1: str\n"
                ":param arg2: Import template to make\n"
                ":type arg2: str\n"
                ":param arg3: SQL selection query to run on database\n"
                ":type arg3: str\n"
                ":param arg4: Name of Oasis table to create\n"
                ":type arg4: str\n"
                ":returns: 0 - OK\n"
                "          -1 - Cancel\n"
                "          terminates on error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This is similar to ImportDatabaseSQL_GUI, but dispenses with\n"
                "   the dialog offering a selection of queries. Instead, the\n"
                "   user supplies the query as a string.\n"
                "   \n"
                "   This function DOES NOT import the table itself, but\n"
                "   creates an import template which may be used to import\n"
                "   the data (see \\ :func:`geosoft.gxapi.GXDU.import_ado`\\ ()).\n\n"
               ).staticmethod("import_template_sqlado");
    pyClass.def("import_xyz_template_editor", &GXGUI_wrap_import_xyz_template_editor,
                "import_xyz_template_editor((GXDB)arg1, (str)arg2, (int)arg3, (str)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Allows the user to edit XYZ import templates\n"
                "   using a complex dialog. The Template name\n"
                "   may change during editing.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Name of the Template (can change)\n"
                ":type arg2: str\n"
                ":param arg3: Size of the Template\n"
                ":type arg3: int\n"
                ":param arg4: Name of the XYZ file to base it on\n"
                ":type arg4: str\n"
                ":returns: 0 - OK\n"
                "          1 - Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("import_xyz_template_editor");
    pyClass.def("odbc_file_connect", &GXGUI_wrap_odbc_file_connect,
                "odbc_file_connect((str)arg1, (str_ref)arg2, (int)arg3, (str_ref)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the connection string for a file database as well as optional table name and FileUsage attribute\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":param arg2: Connection string (returned)\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: File Usage (0 - ODBC drivers not queried, 1 - Directory containing tables, 2 - File containing tables)\n"
                ":type arg3: int\n"
                ":param arg4: Table name of file (returned if plUsage==1)\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 - OK\n"
                "          -1 - Cancel\n"
                "          terminates on error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the file extension is \"mdb\" or \"xls\" then a Microsoft Access\n"
                "   or Excel database is assumed. Otherwise, a dialog appears listing\n"
                "   the installed ODBC file database drivers. If the driver takes a\n"
                "   directory as a database (FileUsage==1) the table name is also\n"
                "   returned. This is needed because the table name may or may not include\n"
                "   the file extension.\n\n"
               ).staticmethod("odbc_file_connect");
    pyClass.def("symbol_form", &GXGUI_wrap_symbol_form,
                "symbol_form((str_ref)arg1, (bool_ref)arg2, (int_ref)arg3, (int_ref)arg4, (float_ref)arg5, (float_ref)arg6, (int_ref)arg7, (int_ref)arg8) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   - Select a symbol.\n\n"

                ":param arg1: Symbol font file name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: Geosoft font? bool\n"
                ":type arg2: :class:`geosoft.gxapi.bool_ref`\n"
                ":param arg3: weight \\ :ref:`MVIEW_FONT_WEIGHT`\\ \n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: symbol number\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: symbol size\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: symbol angle\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: edge colour\n"
                ":type arg7: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg8: fill colour\n"
                ":type arg8: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Symbols are set on input, and new values returned.\n\n"
               ).staticmethod("symbol_form");
    pyClass.def("meta_data_tool", &GXGUI_wrap_meta_data_tool,
                "meta_data_tool((GXMETA)arg1, (int)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Edit a META object\n\n"

                ":param arg1: Meta object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg2: Root Token, H_META_INVALID_TOKEN for root\n"
                ":type arg2: int\n"
                ":param arg3: Display schema information ?\n"
                ":type arg3: int\n"
                ":returns: 0         - OK\n"
                "          non-zero  - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("meta_data_tool");
    pyClass.def("import_chem_wizard", &GXGUI_wrap_import_chem_wizard,
                "import_chem_wizard((str)arg1, (str)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a template file for importing geochems.\n\n"

                ":param arg1: data file name\n"
                ":type arg1: str\n"
                ":param arg2: template to make\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`IMPCH_TYPE`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("import_chem_wizard");
    pyClass.def("import_drill_wizard", &GXGUI_wrap_import_drill_wizard,
                "import_drill_wizard((str)arg1, (str)arg2, (str)arg3, (int)arg4, (int_ref)arg5, (GXREG)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a template file for importing drill holes.\n\n"

                ":param arg1: data file name\n"
                ":type arg1: str\n"
                ":param arg2: template to make\n"
                ":type arg2: str\n"
                ":param arg3: Name of table\n"
                ":type arg3: str\n"
                ":param arg4: Size of table name string\n"
                ":type arg4: int\n"
                ":param arg5: Type of import returned \\ :ref:`DH_DATA`\\ \n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Drill Hole Object REG handle\n"
                ":type arg6: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("import_drill_wizard");
    pyClass.def("internet_trust", &GXGUI_wrap_internet_trust,
                "internet_trust() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Change the Internet Trust Relationships\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("internet_trust");
    pyClass.def("pattern_form", &GXGUI_wrap_pattern_form,
                "pattern_form((int_ref)arg1, (float_ref)arg2, (int_ref)arg3, (float_ref)arg4, (int_ref)arg5, (int_ref)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   - Select a pattern.\n\n"

                ":param arg1: Current Pattern\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Current Size,           // returned\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Current Thick (0-100)   // returned\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Current Density,        // returned\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Current Pattern Color   // passed in and returned\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Current Background Color  // passed in and returned; can be C_TRANSPARENT\n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Pattern values set on input, and new values returned.\n"
                "   Solid fill is indicated by Pattern number 0.\n"
                "   \n"
                "   Returned Values (not set on input)\n"
                "   \n"
                "   Size:    pattern tile size in mm.\n"
                "   Thick:   pattern line thickness in percent of the tile size.\n"
                "            valid range is 0-100.\n"
                "   Density: Tile spacing. A value of 1 means tiles are laid with no overlap.\n"
                "            A value of 2 means they overlap each other.\n"
                "   \n"
                "   The pattern Angle and Style parameters are not user-definable.\n\n"
               ).staticmethod("pattern_form");
    pyClass.def("line_pattern_form", &GXGUI_wrap_line_pattern_form,
                "line_pattern_form((int_ref)arg1, (float_ref)arg2, (float_ref)arg3, (int_ref)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Select a line pattern.\n\n"

                ":param arg1: Current Pattern\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Current Thickness\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Current Pitch\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Current Pattern Color\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          					1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXGUI.pattern_form`\\  but for line patterns.\n\n"
               ).staticmethod("line_pattern_form");
    pyClass.def("two_panel_selection", &GXGUI_wrap_two_panel_selection,
                "two_panel_selection((GXLST)arg1, (GXLST)arg2, (str)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   General purpose two-panel selection.\n\n"

                ":param arg1: All available items for selection.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: Selections (altered on output)\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: Title for dialog\n"
                ":type arg3: str\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Takes as input two LSTs, one contains all available items,\n"
                "   the second currently selected items. These are processed,\n"
                "   and in the left panel are displayed all items in the first\n"
                "   LST not in the selection LST, and on the right all items\n"
                "   in the first LST which are in the selection LST. (Items in\n"
                "   the selection LST NOT in the first LST are ignored).\n"
                "   Once the user has finalized the selections, the final selections\n"
                "   are returned in the selection LST.\n"
                "   \n"
                "   Selections and display are based on the LST_ITEM_NAME part of the\n"
                "   LST item, but on export both the LST_ITEM_NAME and LST_ITEM_VALUE\n"
                "   elements of the selected items from the first LST are transferred\n"
                "   to the second list for output.\n"
                "   \n"
                "   The sConvertToCSV_LST and sConvertFromCSV_LST functions in lst.h\n"
                "   can be used to convert the selection LSTs to forms that can be\n"
                "   stored and retrieved from GX parameters (or REG or INI, etc.).\n\n"
               ).staticmethod("two_panel_selection");
    pyClass.def("two_panel_selection2", &GXGUI_wrap_two_panel_selection2,
                "two_panel_selection2((GXLST)arg1, (GXLST)arg2, (str)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Two-panel selection, items not sorted alphabetically.\n\n"

                ":param arg1: All available items for selection.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: Selections (altered on output)\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: Title for dialog\n"
                ":type arg3: str\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXGUI.two_panel_selection`\\ , but the items in the\n"
                "   two lists are not sorted alphabetically, but are ordered\n"
                "   exactly as input, and when an item is selected it is\n"
                "   added at the end of the lists.\n\n"
               ).staticmethod("two_panel_selection2");
    pyClass.def("two_panel_selection_ex", &GXGUI_wrap_two_panel_selection_ex,
                "two_panel_selection_ex((GXLST)arg1, (GXLST)arg2, (int)arg3, (int)arg4, (str)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Two-panel selection; options for sort and ability to select no items.\n\n"

                ":param arg1: All available items for selection.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: Selections (altered on output)\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: Sort items alphabetically (0:No, 1:Yes)\n"
                ":type arg3: int\n"
                ":param arg4: Allow no items selected (0:No, 1:Yes)\n"
                ":type arg4: int\n"
                ":param arg5: Title for dialog\n"
                ":type arg5: str\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXGUI.two_panel_selection`\\ , but the items in the\n"
                "   two lists are not sorted alphabetically, but are ordered\n"
                "   exactly as input, and when an item is selected it is\n"
                "   added at the end of the lists.\n\n"
               ).staticmethod("two_panel_selection_ex");
    pyClass.def("two_panel_selection_ex2", &GXGUI_wrap_two_panel_selection_ex2,
                "two_panel_selection_ex2((GXLST)arg1, (GXLST)arg2, (int)arg3, (int)arg4, (str)arg5, (str)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Two-panel selection; extended options including a help link.\n\n"

                ":param arg1: All available items for selection.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: Selections (altered on output)\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: Sort items alphabetically (0:No, 1:Yes)\n"
                ":type arg3: int\n"
                ":param arg4: Allow no items selected (0:No, 1:Yes)\n"
                ":type arg4: int\n"
                ":param arg5: Title for dialog\n"
                ":type arg5: str\n"
                ":param arg6: Help link\n"
                ":type arg6: str\n"
                ":returns: 0 - Ok\n"
                "          1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXGUI.two_panel_selection_ex`\\ , but user can specify a help\n"
                "   link.\n\n"
               ).staticmethod("two_panel_selection_ex2");
    pyClass.def("launch_single_geo_dotnetx_tool", &GXGUI_wrap_launch_single_geo_dotnetx_tool,
                "launch_single_geo_dotnetx_tool((str)arg1, (str)arg2, (GXMETA)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch a user created .Net GEOXTOOL ensuring a single instance.\n\n"

                ":param arg1: Assembly name\n"
                ":type arg1: str\n"
                ":param arg2: Control Class Name\n"
                ":type arg2: str\n"
                ":param arg3: META Handle (holding tool configuration data)\n"
                ":type arg3: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("launch_single_geo_dotnetx_tool");
    pyClass.def("launch_geo_dotnetx_tool", &GXGUI_wrap_launch_geo_dotnetx_tool,
                "launch_geo_dotnetx_tool((str)arg1, (str)arg2, (GXMETA)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch a user created .Net GEOXTOOL.\n\n"

                ":param arg1: Assembly name\n"
                ":type arg1: str\n"
                ":param arg2: Control Class Name\n"
                ":type arg2: str\n"
                ":param arg3: META Handle (holding tool configuration data)\n"
                ":type arg3: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("launch_geo_dotnetx_tool");
    pyClass.def("launch_geo_x_tool", &GXGUI_wrap_launch_geo_x_tool,
                "launch_geo_x_tool((str)arg1, (str)arg2, (GXMETA)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch a user created GEOXTOOL.\n\n"

                ":param arg1: DLL name\n"
                ":type arg1: str\n"
                ":param arg2: Function Name\n"
                ":type arg2: str\n"
                ":param arg3: META Handle (holding tool configuration data)\n"
                ":type arg3: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("launch_geo_x_tool");
    pyClass.def("launch_single_geo_dotnetx_tool_ex", &GXGUI_wrap_launch_single_geo_dotnetx_tool_ex,
                "launch_single_geo_dotnetx_tool_ex((str)arg1, (str)arg2, (GXMETA)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch a user created .Net GEOXTOOL ensuring a single instance.\n\n"

                ":param arg1: Assembly name\n"
                ":type arg1: str\n"
                ":param arg2: Control Class Name\n"
                ":type arg2: str\n"
                ":param arg3: META Handle (holding tool configuration data)\n"
                ":type arg3: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg4: \\ :ref:`XTOOL_ALIGN`\\  (can specify one or more or XTOOL_ALIGN_ANY)\n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`XTOOL_DOCK`\\ \n"
                ":type arg5: int\n"
                ":param arg6: Default width\n"
                ":type arg6: int\n"
                ":param arg7: Default height\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("launch_single_geo_dotnetx_tool_ex");
    pyClass.def("launch_geo_dotnetx_tool_ex", &GXGUI_wrap_launch_geo_dotnetx_tool_ex,
                "launch_geo_dotnetx_tool_ex((str)arg1, (str)arg2, (GXMETA)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch a user created .Net GEOXTOOL.\n\n"

                ":param arg1: Assembly name\n"
                ":type arg1: str\n"
                ":param arg2: Control Class Name\n"
                ":type arg2: str\n"
                ":param arg3: META Handle (holding tool configuration data)\n"
                ":type arg3: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg4: \\ :ref:`XTOOL_ALIGN`\\  (can specify one or more or XTOOL_ALIGN_ANY)\n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`XTOOL_DOCK`\\ \n"
                ":type arg5: int\n"
                ":param arg6: Default width\n"
                ":type arg6: int\n"
                ":param arg7: Default height\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("launch_geo_dotnetx_tool_ex");
    pyClass.def("launch_geo_x_tool_ex", &GXGUI_wrap_launch_geo_x_tool_ex,
                "launch_geo_x_tool_ex((str)arg1, (str)arg2, (GXMETA)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch a user created GEOXTOOL.\n\n"

                ":param arg1: DLL name\n"
                ":type arg1: str\n"
                ":param arg2: Function Name\n"
                ":type arg2: str\n"
                ":param arg3: META Handle (holding tool configuration data)\n"
                ":type arg3: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg4: \\ :ref:`XTOOL_ALIGN`\\  (can specify one or more or XTOOL_ALIGN_ANY)\n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`XTOOL_DOCK`\\ \n"
                ":type arg5: int\n"
                ":param arg6: Default width\n"
                ":type arg6: int\n"
                ":param arg7: Default height\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("launch_geo_x_tool_ex");
    pyClass.def("meta_data_viewer", &GXGUI_wrap_meta_data_viewer,
                "meta_data_viewer((GXMETA)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   View a META object\n\n"

                ":param arg1: Meta object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg2: Root Token, H_META_INVALID_TOKEN for root\n"
                ":type arg2: int\n"
                ":param arg3: Display schema information ?\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("meta_data_viewer");
    pyClass.def("print_file", &GXGUI_wrap_print_file,
                "print_file((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Prints a file to current printer\n\n"

                ":param arg1: Filename string\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("print_file");
    pyClass.def("render_pattern", &GXGUI_wrap_render_pattern,
                "render_pattern((HDC)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (float)arg7, (int)arg8, (float)arg9, (int)arg10, (int)arg11, (int)arg12, (int)arg13, (int)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   - Render a pattern.\n\n"

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
                ":param arg6: pattern number\n"
                ":type arg6: int\n"
                ":param arg7: pattern Size,           // input GS_R8DM to use default\n"
                ":type arg7: float\n"
                ":param arg8: pattern Thick (0-100)   // input GS_S4DM to use default\n"
                ":type arg8: int\n"
                ":param arg9: pattern Density,        // input GS_R8DM to use default\n"
                ":type arg9: float\n"
                ":param arg10: pattern Pattern Color	  // input GS_S4DM to use default\n"
                ":type arg10: int\n"
                ":param arg11: pattern Background Color // input GS_S4DM to use default; can be C_TRANSPARENT\n"
                ":type arg11: int\n"
                ":param arg12: is this window enabled?\n"
                ":type arg12: int\n"
                ":param arg13: is this a button?\n"
                ":type arg13: int\n"
                ":param arg14: is this window selected?\n"
                ":type arg14: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Renders a Geosoft pattern to a Windows DC.\n\n"
               ).staticmethod("render_pattern");
    pyClass.def("render_line_pattern", &GXGUI_wrap_render_line_pattern,
                "render_line_pattern((HDC)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (float)arg7, (float)arg8, (int)arg9, (int)arg10, (int)arg11, (int)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Render a line pattern.\n\n"

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
                ":param arg6: pattern number\n"
                ":type arg6: int\n"
                ":param arg7: pattern thickness\n"
                ":type arg7: float\n"
                ":param arg8: pattern pitch\n"
                ":type arg8: float\n"
                ":param arg9: pattern colour\n"
                ":type arg9: int\n"
                ":param arg10: is this window enabled?\n"
                ":type arg10: int\n"
                ":param arg11: is this a button?\n"
                ":type arg11: int\n"
                ":param arg12: is this window selected?\n"
                ":type arg12: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXGUI.render_pattern`\\  but for line patterns.\n\n"
               ).staticmethod("render_line_pattern");
    pyClass.def("set_parent_wnd", &GXGUI_wrap_set_parent_wnd,
                "set_parent_wnd((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the current parent WND\n\n"

                ":param arg1: New Parent Window\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The parent WND is used by all modal dialogs as a\n"
                "   parent to ensure the dialog is correctly modal.\n\n"
               ).staticmethod("set_parent_wnd");
    pyClass.def("set_printer", &GXGUI_wrap_set_printer,
                "set_printer((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the Printer.\n\n"

                ":param arg1: Printer Name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("set_printer");
    pyClass.def("set_prog_always_on", &GXGUI_wrap_set_prog_always_on,
                "set_prog_always_on((bool)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Ability to set the progress bar to stay visible even\n"
                "   if main application is processing messages\n\n"

                ":param arg1: bool Should progress bar remain visible\n"
                ":type arg1: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   In montaj the progress bar is hidden when the main window\n"
                "   start processing messages. This is not always desirable\n"
                "   in some 3rd party apps, hence this function.\n\n"
               ).staticmethod("set_prog_always_on");
    pyClass.def("show_direct_hist", &GXGUI_wrap_show_direct_hist,
                "show_direct_hist((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (int)arg6, (GXVV)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display Histogram of data directly\n\n"

                ":param arg1: Min    Value to display\n"
                ":type arg1: float\n"
                ":param arg2: Max    Value to display\n"
                ":type arg2: float\n"
                ":param arg3: Mean   Value to display\n"
                ":type arg3: float\n"
                ":param arg4: StdDev Value to display\n"
                ":type arg4: float\n"
                ":param arg5: Median Value to display\n"
                ":type arg5: float\n"
                ":param arg6: Items  Number of items this comprises\n"
                ":type arg6: int\n"
                ":param arg7: VV holding hist counts\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("show_direct_hist");
    pyClass.def("show_hist", &GXGUI_wrap_show_hist,
                "show_hist((GXST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display Histogram of data from ST\n\n"

                ":param arg1: Statistics obj\n"
                ":type arg1: :class:`geosoft.gxapi.GXST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("show_hist");
    pyClass.def("simple_map_dialog", &GXGUI_wrap_simple_map_dialog,
                "simple_map_dialog((GXMAP)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   General purpose map display GUI with no interaction.\n\n"

                ":param arg1: MAP object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: Title\n"
                ":type arg2: str\n"
                ":param arg3: HelpID\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function displays a map in a simple resizable dialog that fits the map into it.\n"
                "   It is generally useful to display temporary maps as graphs (e.g. variograms).\n\n"
               ).staticmethod("simple_map_dialog");
    pyClass.def("thematic_voxel_info", &GXGUI_wrap_thematic_voxel_info,
                "thematic_voxel_info((GXVOX)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display GX.Net thematic voxel info GUI.\n\n"

                ":param arg1: VOX object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVOX`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Displays the thematic voxel codes, colours, total volume for\n"
                "   each code, and number of valid items (cubes) for each code.\n"
                "   This is a replacement for the numeric stats done on normal\n"
                "   numerical voxel grids.\n\n"
               ).staticmethod("thematic_voxel_info");
    pyClass.def("show_3d_viewer_dialog", &GXGUI_wrap_show_3d_viewer_dialog,
                "show_3d_viewer_dialog((str)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display a 3D viewer dialog\n\n"

                ":param arg1: Title\n"
                ":type arg1: str\n"
                ":param arg2: Map name\n"
                ":type arg2: str\n"
                ":param arg3: View name\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Any changes made to the map will be persisted.\n\n"
               ).staticmethod("show_3d_viewer_dialog");

    scope().attr("AOI_RETURN_CANCEL") = (int32_t)-1;
    scope().attr("AOI_RETURN_NODEFINE") = (int32_t)0;
    scope().attr("AOI_RETURN_DEFINE") = (int32_t)1;
    scope().attr("COORDSYS_MODE_ALL") = (int32_t)0;
    scope().attr("COORDSYS_MODE_GCS") = (int32_t)1;
    scope().attr("COORDSYS_MODE_PCS") = (int32_t)2;
    scope().attr("COORDSYS_MODE_GCS_PCS") = (int32_t)3;
    scope().attr("COORDSYS_MODE_PCS_UNKNOWN") = (int32_t)4;
    scope().attr("DAT_TYPE_GRID") = (int32_t)0;
    scope().attr("DAT_TYPE_IMAGE") = (int32_t)1;
    scope().attr("DAT_TYPE_GRID_AND_IMAGE") = (int32_t)2;
    scope().attr("FILE_FILTER_ALL") = (int32_t)1;
    scope().attr("FILE_FILTER_GDB") = (int32_t)2;
    scope().attr("FILE_FILTER_GX") = (int32_t)3;
    scope().attr("FILE_FILTER_GS") = (int32_t)4;
    scope().attr("FILE_FILTER_INI") = (int32_t)5;
    scope().attr("FILE_FILTER_OMN") = (int32_t)6;
    scope().attr("FILE_FILTER_VU") = (int32_t)7;
    scope().attr("FILE_FILTER_MAP") = (int32_t)8;
    scope().attr("FILE_FILTER_PRJ") = (int32_t)9;
    scope().attr("FILE_FILTER_CON") = (int32_t)10;
    scope().attr("FILE_FILTER_MNU") = (int32_t)11;
    scope().attr("FILE_FILTER_PDF") = (int32_t)12;
    scope().attr("FILE_FILTER_PLT") = (int32_t)13;
    scope().attr("FILE_FILTER_GWS") = (int32_t)14;
    scope().attr("FILE_FILTER_AGG") = (int32_t)15;
    scope().attr("FILE_FILTER_TBL") = (int32_t)16;
    scope().attr("FILE_FILTER_ZON") = (int32_t)17;
    scope().attr("FILE_FILTER_ITR") = (int32_t)18;
    scope().attr("FILE_FILTER_DXF") = (int32_t)19;
    scope().attr("FILE_FILTER_TIF") = (int32_t)20;
    scope().attr("FILE_FILTER_EMF") = (int32_t)21;
    scope().attr("FILE_FILTER_BMP") = (int32_t)22;
    scope().attr("FILE_FILTER_LUT") = (int32_t)23;
    scope().attr("FILE_FILTER_PNG") = (int32_t)24;
    scope().attr("FILE_FILTER_JPG") = (int32_t)25;
    scope().attr("FILE_FILTER_PCX") = (int32_t)26;
    scope().attr("FILE_FILTER_GIF") = (int32_t)27;
    scope().attr("FILE_FILTER_GRD") = (int32_t)28;
    scope().attr("FILE_FILTER_ERS") = (int32_t)29;
    scope().attr("FILE_FILTER_EPS") = (int32_t)30;
    scope().attr("FILE_FILTER_SHP") = (int32_t)31;
    scope().attr("FILE_FILTER_CGM") = (int32_t)32;
    scope().attr("FILE_FILTER_TAB") = (int32_t)33;
    scope().attr("FILE_FILTER_COMPS") = (int32_t)34;
    scope().attr("FILE_FILTER_CSV") = (int32_t)35;
    scope().attr("FILE_FILTER_GPF") = (int32_t)36;
    scope().attr("FILE_FILTER_PLY") = (int32_t)37;
    scope().attr("FILE_FILTER_STM") = (int32_t)38;
    scope().attr("FILE_FILTER_TTM") = (int32_t)39;
    scope().attr("FILE_FILTER_XYZ") = (int32_t)40;
    scope().attr("FILE_FILTER_BAR") = (int32_t)41;
    scope().attr("FILE_FILTER_GEOSOFT_LICENSE") = (int32_t)42;
    scope().attr("FILE_FILTER_XML") = (int32_t)43;
    scope().attr("FILE_FILTER_GXNET") = (int32_t)44;
    scope().attr("FILE_FILTER_ECW") = (int32_t)45;
    scope().attr("FILE_FILTER_J2K") = (int32_t)46;
    scope().attr("FILE_FILTER_JP2") = (int32_t)47;
    scope().attr("FILE_FILTER_SEL") = (int32_t)48;
    scope().attr("FILE_FILTER_SVG") = (int32_t)49;
    scope().attr("FILE_FILTER_SVZ") = (int32_t)50;
    scope().attr("FILE_FILTER_WRP") = (int32_t)51;
    scope().attr("FILE_FILTER_MAPPLOT") = (int32_t)52;
    scope().attr("FILE_FILTER_DTM") = (int32_t)53;
    scope().attr("FILE_FILTER_VOXEL") = (int32_t)54;
    scope().attr("FILE_FILTER_MAPTEMPLATE") = (int32_t)55;
    scope().attr("FILE_FILTER_ACTION") = (int32_t)56;
    scope().attr("FILE_FILTER_DM") = (int32_t)57;
    scope().attr("FILE_FILTER_KML") = (int32_t)58;
    scope().attr("FILE_FILTER_KMZ") = (int32_t)59;
    scope().attr("FILE_FILTER_TARGET_PLAN") = (int32_t)60;
    scope().attr("FILE_FILTER_TARGET_SECTION") = (int32_t)61;
    scope().attr("FILE_FILTER_TARGET_STRIPLOG") = (int32_t)62;
    scope().attr("FILE_FILTER_TARGET_3D") = (int32_t)63;
    scope().attr("FILE_FILTER_ARGIS_LYR") = (int32_t)64;
    scope().attr("FILE_FILTER_ARGIS_MXD") = (int32_t)65;
    scope().attr("FILE_FILTER_GOCAD_TS") = (int32_t)66;
    scope().attr("FILE_FILTER_LST") = (int32_t)67;
    scope().attr("FILE_FILTER_ECS") = (int32_t)68;
    scope().attr("FILE_FILTER_TARGET_FENCE") = (int32_t)69;
    scope().attr("FILE_FILTER_GMS3D") = (int32_t)70;
    scope().attr("FILE_FILTER_BT2") = (int32_t)71;
    scope().attr("FILE_FILTER_BPR") = (int32_t)72;
    scope().attr("FILE_FILTER_BPR2") = (int32_t)73;
    scope().attr("FILE_FILTER_XLS") = (int32_t)74;
    scope().attr("FILE_FILTER_XLSX") = (int32_t)75;
    scope().attr("FILE_FILTER_MDB") = (int32_t)76;
    scope().attr("FILE_FILTER_ACCDB") = (int32_t)77;
    scope().attr("FILE_FILTER_INTERSECTION_TBL") = (int32_t)78;
    scope().attr("FILE_FILTER_UBC_CON") = (int32_t)79;
    scope().attr("FILE_FILTER_UBC_CHG") = (int32_t)80;
    scope().attr("FILE_FILTER_UBC_MSH") = (int32_t)81;
    scope().attr("FILE_FILTER_UBC_MSH_DAT") = (int32_t)82;
    scope().attr("FILE_FILTER_UBC_TOPO_DAT") = (int32_t)83;
    scope().attr("FILE_FILTER_UBC_TOPO_XYZ") = (int32_t)84;
    scope().attr("FILE_FILTER_XYZ_TEMPLATE_I0") = (int32_t)85;
    scope().attr("FILE_FILTER_PICO_TEMPLATE_I1") = (int32_t)86;
    scope().attr("FILE_FILTER_BB_TEMPLATE_I2") = (int32_t)87;
    scope().attr("FILE_FILTER_ASCII_TEMPLATE_I3") = (int32_t)88;
    scope().attr("FILE_FILTER_ODBC_TEMPLATE_I4") = (int32_t)89;
    scope().attr("FILE_FILTER_EXP") = (int32_t)90;
    scope().attr("FILE_FILTER_SEGY") = (int32_t)91;
    scope().attr("FILE_FILTER_DAARC500") = (int32_t)92;
    scope().attr("FILE_FILTER_TXT") = (int32_t)93;
    scope().attr("FILE_FILTER_VOXEL_INVERSION") = (int32_t)94;
    scope().attr("FILE_FILTER_GMS") = (int32_t)95;
    scope().attr("FILE_FILTER_FLT3D") = (int32_t)96;
    scope().attr("FILE_FILTER_RESOURCE_PACK") = (int32_t)97;
    scope().attr("FILE_FILTER_GEOSTRING") = (int32_t)98;
    scope().attr("FILE_FILTER_GEOSURFACE") = (int32_t)99;
    scope().attr("FILE_FILTER_GEOSOFT3DV") = (int32_t)100;
    scope().attr("FILE_FILTER_VECTORVOXEL") = (int32_t)101;
    scope().attr("FILE_FILTER_FLT") = (int32_t)102;
    scope().attr("FILE_FILTER_XYZ_TEMPLATE_O0") = (int32_t)103;
    scope().attr("FILE_FILTER_GMS2D") = (int32_t)104;
    scope().attr("FILE_FILTER_IP_DATABASE_TEMPLATE") = (int32_t)105;
    scope().attr("FILE_FILTER_GEOSOFT_RESOURCE_MODULE") = (int32_t)106;
    scope().attr("FILE_FILTER_VT") = (int32_t)107;
    scope().attr("FILE_FILTER_INT") = (int32_t)108;
    scope().attr("FILE_FILTER_SGT") = (int32_t)109;
    scope().attr("FILE_FILTER_IMGVIEW") = (int32_t)110;
    scope().attr("FILE_FILTER_ZIP") = (int32_t)111;
    scope().attr("FILE_FILTER_GPS_TABLE") = (int32_t)112;
    scope().attr("FILE_FILTER_VULCAN_TRIANGULATION") = (int32_t)113;
    scope().attr("FILE_FILTER_VULCAN_BLOCK_MODEL") = (int32_t)114;
    scope().attr("FILE_FILTER_PRJVIEW") = (int32_t)115;
    scope().attr("FILE_FILTER_LEAPFROG_MODEL") = (int32_t)116;
    scope().attr("FILE_FILTER_IOGAS") = (int32_t)117;
    scope().attr("FILE_FILTER_ASEG_ESF") = (int32_t)118;
    scope().attr("FILE_FILTER_LACOSTE_DAT") = (int32_t)119;
    scope().attr("FILE_FILTER_VAR") = (int32_t)120;
    scope().attr("FILE_FILTER_P190") = (int32_t)121;
    scope().attr("FILE_FILTER_UBC_OBS_DAT") = (int32_t)122;
    scope().attr("FILE_FILTER_UBC_LOC") = (int32_t)123;
    scope().attr("FILE_FORM_OPEN") = (int32_t)0;
    scope().attr("FILE_FORM_SAVE") = (int32_t)1;
    scope().attr("GS_DIRECTORY_NONE") = (int32_t)0;
    scope().attr("GS_DIRECTORY_GEOSOFT") = (int32_t)1;
    scope().attr("GS_DIRECTORY_BIN") = (int32_t)2;
    scope().attr("GS_DIRECTORY_GER") = (int32_t)3;
    scope().attr("GS_DIRECTORY_OMN") = (int32_t)4;
    scope().attr("GS_DIRECTORY_TBL") = (int32_t)5;
    scope().attr("GS_DIRECTORY_FONTS") = (int32_t)6;
    scope().attr("GS_DIRECTORY_GX") = (int32_t)7;
    scope().attr("GS_DIRECTORY_GS") = (int32_t)8;
    scope().attr("GS_DIRECTORY_APPS") = (int32_t)9;
    scope().attr("GS_DIRECTORY_ETC") = (int32_t)10;
    scope().attr("GS_DIRECTORY_HLP") = (int32_t)11;
    scope().attr("GS_DIRECTORY_GXDEV") = (int32_t)12;
    scope().attr("GS_DIRECTORY_COMPONENT") = (int32_t)13;
    scope().attr("GS_DIRECTORY_CSV") = (int32_t)14;
    scope().attr("GS_DIRECTORY_LIC") = (int32_t)15;
    scope().attr("GS_DIRECTORY_INI") = (int32_t)16;
    scope().attr("GS_DIRECTORY_TEMP") = (int32_t)17;
    scope().attr("GS_DIRECTORY_UETC") = (int32_t)18;
    scope().attr("GS_DIRECTORY_UMAPTEMPLATE") = (int32_t)19;
    scope().attr("GS_DIRECTORY_COMPONENT_SCRIPTS") = (int32_t)50;
    scope().attr("GS_DIRECTORY_COMPONENT_HTML") = (int32_t)51;
    scope().attr("GS_DIRECTORY_IMG") = (int32_t)52;
    scope().attr("GS_DIRECTORY_BAR") = (int32_t)53;
    scope().attr("GS_DIRECTORY_GXNET") = (int32_t)54;
    scope().attr("GS_DIRECTORY_MAPTEMPLATE") = (int32_t)55;
    scope().attr("IMPCH_TYPE_DATA") = (int32_t)0;
    scope().attr("IMPCH_TYPE_ASSAY") = (int32_t)1;
    scope().attr("WINDOW_RESTORE") = (int32_t)0;
    scope().attr("WINDOW_MINIMIZE") = (int32_t)1;
    scope().attr("WINDOW_MAXIMIZE") = (int32_t)2;
    scope().attr("XTOOL_ALIGN_LEFT") = (int32_t)1;
    scope().attr("XTOOL_ALIGN_TOP") = (int32_t)2;
    scope().attr("XTOOL_ALIGN_RIGHT") = (int32_t)4;
    scope().attr("XTOOL_ALIGN_BOTTOM") = (int32_t)8;
    scope().attr("XTOOL_ALIGN_ANY") = (int32_t)15;
    scope().attr("XTOOL_DOCK_TOP") = (int32_t)1;
    scope().attr("XTOOL_DOCK_LEFT") = (int32_t)2;
    scope().attr("XTOOL_DOCK_RIGHT") = (int32_t)3;
    scope().attr("XTOOL_DOCK_BOTTOM") = (int32_t)4;
    scope().attr("XTOOL_DOCK_FLOAT") = (int32_t)5;

}
