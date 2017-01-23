#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXMVU_wrap_arrow(GXMVIEWPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, int32_t arg8)
{
    GXMVU::arrow(arg1, arg2, arg3, arg4, arg5, arg6, arg7, (MVU_ARROW)arg8);
}
inline void GXMVU_wrap_arrow_vector_vv(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, double arg6, int32_t arg7, int32_t arg8, int32_t arg9, int32_t arg10, double arg11)
{
    GXMVU::arrow_vector_vv(arg1, arg2, arg3, arg4, arg5, arg6, (MVU_VPOS)arg7, (MVU_VSIZE)arg8, (MVU_VSTYLE)arg9, (MVU_VPOINT)arg10, arg11);
}
inline void GXMVU_wrap_bar_chart(GXMVIEWPtr arg1, const gx_string_type& arg2, GXDBPtr arg3, int32_t arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7, double arg8, const gx_string_type& arg9, double arg10, const gx_string_type& arg11, double arg12, double arg13, int32_t arg14, int32_t arg15, int32_t arg16, int32_t arg17, int32_t arg18, int32_t arg19, int32_t arg20, double arg21, double arg22, double arg23, double arg24, double arg25, double arg26, double arg27, double arg28)
{
    GXMVU::bar_chart(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, (BARCHART_LABEL)arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24, arg25, arg26, arg27, arg28);
}
inline void GXMVU_wrap_cdi_pixel_plot(GXMVIEWPtr arg1, const gx_string_type& arg2, GXVAPtr arg3, GXVAPtr arg4, GXVVPtr arg5, GXITRPtr arg6)
{
    GXMVU::cdi_pixel_plot(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXMVU_wrap_cdi_pixel_plot_3d(GXMVIEWPtr arg1, const gx_string_type& arg2, GXVAPtr arg3, GXVAPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXITRPtr arg7)
{
    GXMVU::cdi_pixel_plot_3d(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXMVU_wrap_color_bar(GXMVIEWPtr arg1, GXITRPtr arg2, int32_t arg3, double arg4, double arg5, double arg6, double arg7, double arg8)
{
    GXMVU::color_bar(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXMVU_wrap_color_bar2(GXMVIEWPtr arg1, GXITRPtr arg2, GXITRPtr arg3, int32_t arg4, double arg5, double arg6, double arg7, double arg8, double arg9)
{
    GXMVU::color_bar2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXMVU_wrap_color_bar2_style(GXMVIEWPtr arg1, GXITRPtr arg2, GXITRPtr arg3, int32_t arg4, double arg5, double arg6, double arg7, double arg8, double arg9, int32_t arg10)
{
    GXMVU::color_bar2_style(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (COLORBAR_STYLE)arg10);
}
inline void GXMVU_wrap_color_bar_hor(GXMVIEWPtr arg1, GXITRPtr arg2, int32_t arg3, double arg4, double arg5, double arg6, double arg7, double arg8, int32_t arg9)
{
    GXMVU::color_bar_hor(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, (COLORBAR_LABEL)arg9);
}
inline void GXMVU_wrap_color_bar_hor2(GXMVIEWPtr arg1, GXITRPtr arg2, GXITRPtr arg3, int32_t arg4, double arg5, double arg6, double arg7, double arg8, double arg9, int32_t arg10)
{
    GXMVU::color_bar_hor2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (COLORBAR_LABEL)arg10);
}
inline void GXMVU_wrap_color_bar_hor2_style(GXMVIEWPtr arg1, GXITRPtr arg2, GXITRPtr arg3, int32_t arg4, double arg5, double arg6, double arg7, double arg8, double arg9, int32_t arg10, int32_t arg11)
{
    GXMVU::color_bar_hor2_style(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (COLORBAR_STYLE)arg10, (COLORBAR_LABEL)arg11);
}
inline void GXMVU_wrap_color_bar_hor_style(GXMVIEWPtr arg1, GXITRPtr arg2, int32_t arg3, double arg4, double arg5, double arg6, double arg7, double arg8, int32_t arg9, int32_t arg10)
{
    GXMVU::color_bar_hor_style(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, (COLORBAR_STYLE)arg9, (COLORBAR_LABEL)arg10);
}
inline void GXMVU_wrap_color_bar_style(GXMVIEWPtr arg1, GXITRPtr arg2, int32_t arg3, double arg4, double arg5, double arg6, double arg7, double arg8, int32_t arg9)
{
    GXMVU::color_bar_style(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, (COLORBAR_STYLE)arg9);
}
inline void GXMVU_wrap_color_bar_reg(GXMVIEWPtr arg1, GXITRPtr arg2, GXITRPtr arg3, GXREGPtr arg4)
{
    GXMVU::color_bar_reg(arg1, arg2, arg3, arg4);
}
inline void GXMVU_wrap_contour(GXMVIEWPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXMVU::contour(arg1, arg2, arg3);
}
inline void GXMVU_wrap_contour_ply(GXMVIEWPtr arg1, GXPLYPtr arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    GXMVU::contour_ply(arg1, arg2, arg3, arg4);
}
inline void GXMVU_wrap_c_symb_legend(GXMVIEWPtr arg1, double arg2, double arg3, double arg4, double arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8)
{
    GXMVU::c_symb_legend(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXMVU_wrap_decay_curve(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVAPtr arg4, GXVAPtr arg5, int32_t arg6, double arg7, double arg8, int32_t arg9, int32_t arg10, double arg11, double arg12, double arg13, double arg14, double arg15, double arg16, double arg17, double arg18, double arg19, int32_t arg20, const gx_string_type& arg21)
{
    GXMVU::decay_curve(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21);
}
inline void GXMVU_wrap_direction_plot(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, double arg4, double arg5, int32_t arg6)
{
    GXMVU::direction_plot(arg1, arg2, arg3, arg4, arg5, (ARROW_ALIGNMENT)arg6);
}
inline void GXMVU_wrap_em_forward(GXMVIEWPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, int32_t arg8, double arg9, double arg10, double arg11, double arg12, GXVVPtr arg13, GXVVPtr arg14, GXVVPtr arg15, GXVVPtr arg16, int32_t arg17, int32_t arg18)
{
    GXMVU::em_forward(arg1, arg2, arg3, arg4, arg5, arg6, arg7, (EMLAY_GEOMETRY)arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18);
}
inline void GXMVU_wrap_export_datamine_string(GXMVIEWPtr arg1, GXLSTPtr arg2, const gx_string_type& arg3)
{
    GXMVU::export_datamine_string(arg1, arg2, arg3);
}
inline void GXMVU_wrap_export_dxf_3d(GXMVIEWPtr arg1, GXLSTPtr arg2, GXWAPtr arg3)
{
    GXMVU::export_dxf_3d(arg1, arg2, arg3);
}
inline void GXMVU_wrap_export_surpac_str(GXMVIEWPtr arg1, GXLSTPtr arg2, GXWAPtr arg3, GXWAPtr arg4)
{
    GXMVU::export_surpac_str(arg1, arg2, arg3, arg4);
}
inline void GXMVU_wrap_flight_plot(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, const gx_string_type& arg4, int32_t arg5, double arg6, int32_t arg7, double arg8, double arg9)
{
    GXMVU::flight_plot(arg1, arg2, arg3, arg4, (MVU_FLIGHT_LOCATE)arg5, arg6, arg7, arg8, arg9);
}
inline void GXMVU_wrap_gen_areas(GXMVIEWPtr arg1, const gx_string_type& arg2, GXVVPtr arg3, GXVVPtr arg4, double arg5)
{
    GXMVU::gen_areas(arg1, arg2, arg3, arg4, arg5);
}
inline void GXMVU_wrap_get_range_gocad_surface(const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7)
{
    GXMVU::get_range_gocad_surface(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXMVU_wrap_histogram(GXMVIEWPtr arg1, GXSTPtr arg2, GXSTPtr arg3, const gx_string_type& arg4, const gx_string_type& arg5, double arg6, double arg7, double arg8, double arg9, double arg10, double arg11, double arg12, double arg13, double arg14, int32_t arg15, int32_t arg16, int32_t arg17, GXSTPtr arg18)
{
    GXMVU::histogram(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18);
}
inline void GXMVU_wrap_histogram2(GXMVIEWPtr arg1, GXSTPtr arg2, GXSTPtr arg3, const gx_string_type& arg4, const gx_string_type& arg5, double arg6, const gx_string_type& arg7, double arg8, const gx_string_type& arg9, double arg10, double arg11, double arg12, double arg13, double arg14, double arg15, double arg16, double arg17, double arg18, int32_t arg19, int32_t arg20, int32_t arg21, GXSTPtr arg22, double arg23)
{
    GXMVU::histogram2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23);
}
inline void GXMVU_wrap_histogram3(GXMVIEWPtr arg1, GXSTPtr arg2, GXSTPtr arg3, const gx_string_type& arg4, const gx_string_type& arg5, double arg6, double arg7, double arg8, double arg9, double arg10, double arg11, double arg12, double arg13, double arg14, int32_t arg15, int32_t arg16, int32_t arg17, int32_t arg18, int32_t arg19, GXSTPtr arg20)
{
    GXMVU::histogram3(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20);
}
inline void GXMVU_wrap_histogram4(GXMVIEWPtr arg1, GXSTPtr arg2, GXSTPtr arg3, const gx_string_type& arg4, const gx_string_type& arg5, double arg6, double arg7, double arg8, double arg9, double arg10, double arg11, double arg12, double arg13, double arg14, int32_t arg15, int32_t arg16, int32_t arg17, int32_t arg18, int32_t arg19, int32_t arg20, GXSTPtr arg21)
{
    GXMVU::histogram4(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21);
}
inline void GXMVU_wrap_histogram5(GXMVIEWPtr arg1, GXSTPtr arg2, GXSTPtr arg3, const gx_string_type& arg4, const gx_string_type& arg5, double arg6, double arg7, double arg8, double arg9, double arg10, double arg11, double arg12, double arg13, double arg14, double arg15, int32_t arg16, int32_t arg17, int32_t arg18, int32_t arg19, int32_t arg20, int32_t arg21, GXSTPtr arg22, GXITRPtr arg23)
{
    GXMVU::histogram5(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23);
}
inline int32_t GXMVU_wrap_exportable_dxf_3d_groups_lst(GXMVIEWPtr arg1, GXLSTPtr arg2)
{
    int32_t ret = GXMVU::exportable_dxf_3d_groups_lst(arg1, arg2);
    return ret;
}
inline bool GXMVU_wrap_mapset_test(double arg1, double arg2, double arg3, double arg4, const gx_string_type& arg5, int32_t arg6, int32_t arg7, float_ref& arg8, double arg9, double arg10, double arg11, double arg12, double arg13, double arg14)
{
    bool ret = GXMVU::mapset_test(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14);
    return ret;
}
inline bool GXMVU_wrap_mapset2_test(double arg1, double arg2, double arg3, double arg4, const gx_string_type& arg5, int32_t arg6, int32_t arg7, float_ref& arg8, double arg9, double arg10, double arg11, double arg12, double arg13, double arg14, double arg15)
{
    bool ret = GXMVU::mapset2_test(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15);
    return ret;
}
inline void GXMVU_wrap_import_gocad_surface(GXMVIEWPtr arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXMVU::import_gocad_surface(arg1, arg2, arg3);
}
inline void GXMVU_wrap_load_plot(GXMAPPtr arg1, const gx_string_type& arg2)
{
    GXMVU::load_plot(arg1, arg2);
}
inline void GXMVU_wrap_map_from_plt(GXMAPPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, double arg5, double arg6)
{
    GXMVU::map_from_plt(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXMVU_wrap_map_mdf(GXMAPPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXMVU::map_mdf(arg1, arg2, arg3);
}
inline void GXMVU_wrap_mapset(GXMAPPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, double arg4, double arg5, double arg6, double arg7, const gx_string_type& arg8, int32_t arg9, int32_t arg10, double arg11, double arg12, double arg13, double arg14, double arg15, double arg16, double arg17)
{
    GXMVU::mapset(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17);
}
inline void GXMVU_wrap_mapset2(GXMAPPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, double arg4, double arg5, double arg6, double arg7, const gx_string_type& arg8, int32_t arg9, int32_t arg10, double arg11, double arg12, double arg13, double arg14, double arg15, double arg16, double arg17, double arg18)
{
    GXMVU::mapset2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18);
}
inline void GXMVU_wrap_mdf(GXMAPPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    GXMVU::mdf(arg1, arg2, arg3, arg4);
}
inline void GXMVU_wrap_path_plot(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, const gx_string_type& arg4, int32_t arg5, double arg6, int32_t arg7, double arg8, double arg9, double arg10)
{
    GXMVU::path_plot(arg1, arg2, arg3, arg4, (MVU_FLIGHT_LOCATE)arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXMVU_wrap_path_plot_ex(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, const gx_string_type& arg4, int32_t arg5, int32_t arg6, double arg7, int32_t arg8, double arg9, double arg10, double arg11)
{
    GXMVU::path_plot_ex(arg1, arg2, arg3, arg4, (MVU_FLIGHT_LOCATE)arg5, (MVU_FLIGHT_COMPASS)arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXMVU_wrap_path_plot_ex2(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, const gx_string_type& arg4, int32_t arg5, int32_t arg6, double arg7, int32_t arg8, double arg9, double arg10, double arg11, int32_t arg12)
{
    GXMVU::path_plot_ex2(arg1, arg2, arg3, arg4, (MVU_FLIGHT_LOCATE)arg5, (MVU_FLIGHT_COMPASS)arg6, arg7, arg8, arg9, arg10, arg11, (MVU_FLIGHT_DUMMIES)arg12);
}
inline void GXMVU_wrap_plot_voxel_surface(GXMVIEWPtr arg1, GXVOXPtr arg2, double arg3, int32_t arg4, double arg5)
{
    GXMVU::plot_voxel_surface(arg1, arg2, arg3, arg4, arg5);
}
inline void GXMVU_wrap_plot_voxel_surface2(GXMVIEWPtr arg1, GXVOXPtr arg2, double arg3, int32_t arg4, double arg5, double arg6, const gx_string_type& arg7)
{
    GXMVU::plot_voxel_surface2(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXMVU_wrap_generate_surface_from_voxel(GXMVIEWPtr arg1, GXVOXPtr arg2, int32_t arg3, int32_t arg4, double arg5, double arg6, int32_t arg7, double arg8, double arg9, const gx_string_type& arg10)
{
    GXMVU::generate_surface_from_voxel(arg1, arg2, (MVU_VOX_SURFACE_METHOD)arg3, (MVU_VOX_SURFACE_OPTION)arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXMVU_wrap_post(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, bool arg5, int32_t arg6, int32_t arg7, int32_t arg8, int32_t arg9, double arg10)
{
    GXMVU::post(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXMVU_wrap_post_ex(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, bool arg6, double arg7, double arg8, int32_t arg9, int32_t arg10, int32_t arg11, double arg12, double arg13, int32_t arg14, double arg15, int32_t arg16, double arg17, int32_t arg18, double arg19, int32_t arg20)
{
    GXMVU::post_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20);
}
inline void GXMVU_wrap_probability(GXMVIEWPtr arg1, GXSTPtr arg2, GXSTPtr arg3, const gx_string_type& arg4, const gx_string_type& arg5, int32_t arg6, double arg7, double arg8, double arg9, double arg10, double arg11, double arg12, double arg13, double arg14, int32_t arg15, int32_t arg16, int32_t arg17, GXITRPtr arg18)
{
    GXMVU::probability(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18);
}
inline void GXMVU_wrap_profile_plot(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, double arg5, int32_t arg6, double arg7, double arg8, double arg9, int32_t arg10)
{
    GXMVU::profile_plot(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXMVU_wrap_profile_plot_ex(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, double arg5, int32_t arg6, double arg7, double arg8, double arg9, int32_t arg10, int32_t arg11, double arg12, int32_t arg13, const gx_string_type& arg14, const gx_string_type& arg15)
{
    GXMVU::profile_plot_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15);
}
inline void GXMVU_wrap_prop_symb_legend(GXMVIEWPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6, int32_t arg7, double arg8, double arg9, const gx_string_type& arg10, const gx_string_type& arg11)
{
    GXMVU::prop_symb_legend(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXMVU_wrap_re_gen_areas(GXMVIEWPtr arg1, const gx_string_type& arg2)
{
    GXMVU::re_gen_areas(arg1, arg2);
}
inline void GXMVU_wrap_symb_off(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, double arg5, double arg6)
{
    GXMVU::symb_off(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXMVU_wrap_text_box(GXMVIEWPtr arg1, double arg2, double arg3, double arg4, double arg5, const gx_string_type& arg6, double arg7, int32_t arg8)
{
    GXMVU::text_box(arg1, arg2, arg3, arg4, arg5, arg6, arg7, (MVU_TEXTBOX)arg8);
}
inline void GXMVU_wrap_tick(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, double arg5, double arg6, double arg7, double arg8)
{
    GXMVU::tick(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXMVU_wrap_tick_ex(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, double arg5, double arg6, double arg7, double arg8, double arg9)
{
    GXMVU::tick_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXMVU_wrap_trnd_path(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, int32_t arg4, double arg5)
{
    GXMVU::trnd_path(arg1, arg2, arg3, arg4, arg5);
}

void gxPythonImportGXMVU()
{

    class_<GXMVU, boost::noncopyable> pyClass("GXMVU",
            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		A catchall library for methods using the MAP and MVIEW classes.\n"
            "   		These include drawing flight paths, legends, postings, and\n"
            "   		special objects such as histograms and bar charts.\n"
            "   	\n\n"
            , no_init);


    pyClass.def("arrow", &GXMVU_wrap_arrow,
                "arrow((GXMVIEW)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw an arrow.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Head X location\n"
                ":type arg2: float\n"
                ":param arg3: Head Y location\n"
                ":type arg3: float\n"
                ":param arg4: Tail X location\n"
                ":type arg4: float\n"
                ":param arg5: Tail Y location\n"
                ":type arg5: float\n"
                ":param arg6: See MVU_ARROW definitions for explanation\n"
                ":type arg6: float\n"
                ":param arg7: Angle of barbs with respect to the tail in degrees.\n"
                ":type arg7: float\n"
                ":param arg8: \\ :ref:`MVU_ARROW`\\ \n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("arrow");
    pyClass.def("arrow_vector_vv", &GXMVU_wrap_arrow_vector_vv,
                "arrow_vector_vv((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (float)arg6, (int)arg7, (int)arg8, (int)arg9, (int)arg10, (float)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw arrow vectors based on input VVs.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y locations\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: X Vector value (can be negative)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Y Vector value (can be negative)\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Scaling (units/mm)\n"
                ":type arg6: float\n"
                ":param arg7: \\ :ref:`MVU_VPOS`\\ \n"
                ":type arg7: int\n"
                ":param arg8: \\ :ref:`MVU_VSIZE`\\ \n"
                ":type arg8: int\n"
                ":param arg9: \\ :ref:`MVU_VSTYLE`\\ \n"
                ":type arg9: int\n"
                ":param arg10: \\ :ref:`MVU_VPOINT`\\ \n"
                ":type arg10: int\n"
                ":param arg11: line thickness (can be Dummy)\n"
                ":type arg11: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The locations are given in two VVs, and the directions\n"
                "   					in the two others. A wide range of sizes are available.\n"
                "   					If the scaling is set to rDUMMY, then arrows are automatically\n"
                "   					scaled so the largest is 1cm in length.\n"
                "   					If the line thickness is set to rDUMMY, the line thickness scales\n"
                "   					with the arrow size, and is 1/20 of the vector length.\n"
                "   				\n\n"
               ).staticmethod("arrow_vector_vv");
    pyClass.def("bar_chart", &GXMVU_wrap_bar_chart,
                "bar_chart((GXMVIEW)arg1, (str)arg2, (GXDB)arg3, (int)arg4, (str)arg5, (str)arg6, (str)arg7, (float)arg8, (str)arg9, (float)arg10, (str)arg11, (float)arg12, (float)arg13, (int)arg14, (int)arg15, (int)arg16, (int)arg17, (int)arg18, (int)arg19, (int)arg20, (float)arg21, (float)arg22, (float)arg23, (float)arg24, (float)arg25, (float)arg26, (float)arg27, (float)arg28) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot bar chart on a map.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Group name\n"
                ":type arg2: str\n"
                ":param arg3: Database handle\n"
                ":type arg3: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg4: Line handle\n"
                ":type arg4: int\n"
                ":param arg5: Horizontal (X) axis' channel name\n"
                ":type arg5: str\n"
                ":param arg6: List of channel names (comma separated)\n"
                ":type arg6: str\n"
                ":param arg7: X axis title\n"
                ":type arg7: str\n"
                ":param arg8: Text size for X axis\n"
                ":type arg8: float\n"
                ":param arg9: Y axis title\n"
                ":type arg9: str\n"
                ":param arg10: Text size for Y axis\n"
                ":type arg10: float\n"
                ":param arg11: Overall chart title\n"
                ":type arg11: str\n"
                ":param arg12: Text size for overall title\n"
                ":type arg12: float\n"
                ":param arg13: Bar width in mm\n"
                ":type arg13: float\n"
                ":param arg14: Distance based (1) or fiducial based (0)\n"
                ":type arg14: int\n"
                ":param arg15: \\ :ref:`BARCHART_LABEL`\\ \n"
                ":type arg15: int\n"
                ":param arg16: Draw ticks along X axis (1) or not (0)\n"
                ":type arg16: int\n"
                ":param arg17: Draw right vertical axis (1) or not\n"
                ":type arg17: int\n"
                ":param arg18: Draw top horizontal axis (1)\n"
                ":type arg18: int\n"
                ":param arg19: Draw bottom horizontal axis (1) or not\n"
                ":type arg19: int\n"
                ":param arg20: Draw surronding box (1) or not (0) The following 4 parameters are required if drawing the surronding box\n"
                ":type arg20: int\n"
                ":param arg21: Width in mm between left Y axis of bar chart with left surronding line\n"
                ":type arg21: float\n"
                ":param arg22: Width in mm between bottom X axis of bar chart with bottom surronding line\n"
                ":type arg22: float\n"
                ":param arg23: Width in mm between right Y axis of bar chart with right surronding line\n"
                ":type arg23: float\n"
                ":param arg24: Width in mm between top X axis of bar chart with top surronding line\n"
                ":type arg24: float\n"
                ":param arg25: X in mm (bottom left corner of bar chart)\n"
                ":type arg25: float\n"
                ":param arg26: Y in mm (bottom left corner of bar chart)\n"
                ":type arg26: float\n"
                ":param arg27: Width of the bar chart in mm\n"
                ":type arg27: float\n"
                ":param arg28: Height of the bar chart in mm\n"
                ":type arg28: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("bar_chart");
    pyClass.def("cdi_pixel_plot", &GXMVU_wrap_cdi_pixel_plot,
                "cdi_pixel_plot((GXMVIEW)arg1, (str)arg2, (GXVA)arg3, (GXVA)arg4, (GXVV)arg5, (GXITR)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a colour pixel-style plot of CDI data.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Name of the group to create\n"
                ":type arg2: str\n"
                ":param arg3: Data [lNR x lNC]\n"
                ":type arg3: :class:`geosoft.gxapi.GXVA`\n"
                ":param arg4: Elevations (Y) [lNR x lNC]\n"
                ":type arg4: :class:`geosoft.gxapi.GXVA`\n"
                ":param arg5: Position (X) [lNC]\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Data colour transform\n"
                ":type arg6: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Draws a single coloured rectangle for each data point in\n"
                "   					Conductivity-Depth data (for example). It is similar to the\n"
                "   					result you get if you plot a grid with Pixel=1, but in this\n"
                "   					data the row and column widths are not necessarily constant,\n"
                "   					and the data can move up and down with topography. The pixels\n"
                "   					are sized so that the boundaries are half-way between adjacent\n"
                "   					data, both vertically and horizontally.\n"
                "   				\n\n"
               ).staticmethod("cdi_pixel_plot");
    pyClass.def("cdi_pixel_plot_3d", &GXMVU_wrap_cdi_pixel_plot_3d,
                "cdi_pixel_plot_3d((GXMVIEW)arg1, (str)arg2, (GXVA)arg3, (GXVA)arg4, (GXVV)arg5, (GXVV)arg6, (GXITR)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a colour pixel-style plot of CDI data in a 3D view.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Name of the group to create\n"
                ":type arg2: str\n"
                ":param arg3: Data [lNR x lNC]\n"
                ":type arg3: :class:`geosoft.gxapi.GXVA`\n"
                ":param arg4: Elevations (Z) [lNR x lNC]\n"
                ":type arg4: :class:`geosoft.gxapi.GXVA`\n"
                ":param arg5: Position (X) [lNC]\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Position (Y) [lNC]\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Data colour transform\n"
                ":type arg7: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Similar to \\ :func:`geosoft.gxapi.GXMVU.cdi_pixel_plot`\\ , but plotted onto a series of\n"
                "   					plotting planes which hang from the XY path in 3D. Each vertical plane azimuth\n"
                "   					is defined by two adjacent points on the path. The colour \"pixel\" for each\n"
                "   					data point is plotted in two halves, with each half on adjacent plotting planes,\n"
                "   					with the bend at the data point.\n"
                "   				\n\n"
               ).staticmethod("cdi_pixel_plot_3d");
    pyClass.def("color_bar", &GXMVU_wrap_color_bar,
                "color_bar((GXMVIEW)arg1, (GXITR)arg2, (int)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a Color Bar in view\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Itr\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg3: decimals\n"
                ":type arg3: int\n"
                ":param arg4: annotation offset from box in mm.\n"
                ":type arg4: float\n"
                ":param arg5: box height\n"
                ":type arg5: float\n"
                ":param arg6: box width\n"
                ":type arg6: float\n"
                ":param arg7: X location (bottom left corner of colour boxes)\n"
                ":type arg7: float\n"
                ":param arg8: Y location\n"
                ":type arg8: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("color_bar");
    pyClass.def("color_bar2", &GXMVU_wrap_color_bar2,
                "color_bar2((GXMVIEW)arg1, (GXITR)arg2, (GXITR)arg3, (int)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a Color Bar from two ITR\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: ITR\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg3: Secondary ITR\n"
                ":type arg3: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg4: decimals\n"
                ":type arg4: int\n"
                ":param arg5: annotation size\n"
                ":type arg5: float\n"
                ":param arg6: box height\n"
                ":type arg6: float\n"
                ":param arg7: box width\n"
                ":type arg7: float\n"
                ":param arg8: X location (bottom left corner of colour boxes)\n"
                ":type arg8: float\n"
                ":param arg9: Y location\n"
                ":type arg9: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The secondary ITR is used to blend horizontally with the\n"
                "   					primary ITR in each box.\n"
                "   				\n\n"
               ).staticmethod("color_bar2");
    pyClass.def("color_bar2_style", &GXMVU_wrap_color_bar2_style,
                "color_bar2_style((GXMVIEW)arg1, (GXITR)arg2, (GXITR)arg3, (int)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (int)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a Color Bar from two ITRs with style options\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: ITR\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg3: Secondary ITR\n"
                ":type arg3: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg4: decimals\n"
                ":type arg4: int\n"
                ":param arg5: annotation size\n"
                ":type arg5: float\n"
                ":param arg6: box height\n"
                ":type arg6: float\n"
                ":param arg7: box width\n"
                ":type arg7: float\n"
                ":param arg8: X location (bottom left corner of colour boxes)\n"
                ":type arg8: float\n"
                ":param arg9: Y location\n"
                ":type arg9: float\n"
                ":param arg10: \\ :ref:`COLORBAR_STYLE`\\ \n"
                ":type arg10: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The secondary ITR is used to blend horizontally with the\n"
                "   					primary ITR in each box.\n"
                "   				\n\n"
               ).staticmethod("color_bar2_style");
    pyClass.def("color_bar_hor", &GXMVU_wrap_color_bar_hor,
                "color_bar_hor((GXMVIEW)arg1, (GXITR)arg2, (int)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (int)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a horizontal color bar in view\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Itr\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg3: decimals\n"
                ":type arg3: int\n"
                ":param arg4: annotation offset from box in mm (negative for labels below).\n"
                ":type arg4: float\n"
                ":param arg5: box width in mm\n"
                ":type arg5: float\n"
                ":param arg6: box height in mm\n"
                ":type arg6: float\n"
                ":param arg7: X location (bottom left corner of colour boxes) in mm\n"
                ":type arg7: float\n"
                ":param arg8: Y location in mm\n"
                ":type arg8: float\n"
                ":param arg9: \\ :ref:`COLORBAR_LABEL`\\ \n"
                ":type arg9: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The sign of the annotation offset determines whether labels are\n"
                "   					plotted above or below the colorbar. Labels above are text-justified\n"
                "   					to the bottom of the text, and labels below are text-justified to\n"
                "   					the top of the text.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVU.color_bar`\\ \n\n"
               ).staticmethod("color_bar_hor");
    pyClass.def("color_bar_hor2", &GXMVU_wrap_color_bar_hor2,
                "color_bar_hor2((GXMVIEW)arg1, (GXITR)arg2, (GXITR)arg3, (int)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (int)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a Horizontal Color Bar from two ITRs\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: ITR\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg3: Secondary ITR\n"
                ":type arg3: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg4: decimals\n"
                ":type arg4: int\n"
                ":param arg5: annotation size\n"
                ":type arg5: float\n"
                ":param arg6: box height\n"
                ":type arg6: float\n"
                ":param arg7: box width\n"
                ":type arg7: float\n"
                ":param arg8: X location (bottom left corner of colour boxes)\n"
                ":type arg8: float\n"
                ":param arg9: Y location\n"
                ":type arg9: float\n"
                ":param arg10: \\ :ref:`COLORBAR_LABEL`\\ \n"
                ":type arg10: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The secondary ITR is used to blend horizontally with the\n"
                "   					primary ITR in each box.\n"
                "   				\n\n"
               ).staticmethod("color_bar_hor2");
    pyClass.def("color_bar_hor2_style", &GXMVU_wrap_color_bar_hor2_style,
                "color_bar_hor2_style((GXMVIEW)arg1, (GXITR)arg2, (GXITR)arg3, (int)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (int)arg10, (int)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a Horizontal Color Bar from two ITRs with style options\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: ITR\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg3: Secondary ITR\n"
                ":type arg3: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg4: decimals\n"
                ":type arg4: int\n"
                ":param arg5: annotation size\n"
                ":type arg5: float\n"
                ":param arg6: box height\n"
                ":type arg6: float\n"
                ":param arg7: box width\n"
                ":type arg7: float\n"
                ":param arg8: X location (bottom left corner of colour boxes)\n"
                ":type arg8: float\n"
                ":param arg9: Y location\n"
                ":type arg9: float\n"
                ":param arg10: \\ :ref:`COLORBAR_STYLE`\\ \n"
                ":type arg10: int\n"
                ":param arg11: \\ :ref:`COLORBAR_LABEL`\\ \n"
                ":type arg11: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The secondary ITR is used to blend horizontally with the\n"
                "   					primary ITR in each box.\n"
                "   				\n\n"
               ).staticmethod("color_bar_hor2_style");
    pyClass.def("color_bar_hor_style", &GXMVU_wrap_color_bar_hor_style,
                "color_bar_hor_style((GXMVIEW)arg1, (GXITR)arg2, (int)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (int)arg9, (int)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a Horizontal Color Bar in view with style options\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Itr\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg3: decimals\n"
                ":type arg3: int\n"
                ":param arg4: annotation size\n"
                ":type arg4: float\n"
                ":param arg5: box height\n"
                ":type arg5: float\n"
                ":param arg6: box width\n"
                ":type arg6: float\n"
                ":param arg7: X location (bottom left corner of colour boxes)\n"
                ":type arg7: float\n"
                ":param arg8: Y location\n"
                ":type arg8: float\n"
                ":param arg9: \\ :ref:`COLORBAR_STYLE`\\ \n"
                ":type arg9: int\n"
                ":param arg10: \\ :ref:`COLORBAR_LABEL`\\ \n"
                ":type arg10: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               ).staticmethod("color_bar_hor_style");
    pyClass.def("color_bar_style", &GXMVU_wrap_color_bar_style,
                "color_bar_style((GXMVIEW)arg1, (GXITR)arg2, (int)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (int)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a Color Bar in view with style options\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Itr\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg3: decimals\n"
                ":type arg3: int\n"
                ":param arg4: annotation size\n"
                ":type arg4: float\n"
                ":param arg5: box height\n"
                ":type arg5: float\n"
                ":param arg6: box width\n"
                ":type arg6: float\n"
                ":param arg7: X location (bottom left corner of colour boxes)\n"
                ":type arg7: float\n"
                ":param arg8: Y location\n"
                ":type arg8: float\n"
                ":param arg9: \\ :ref:`COLORBAR_STYLE`\\ \n"
                ":type arg9: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("color_bar_style");
    pyClass.def("color_bar_reg", &GXMVU_wrap_color_bar_reg,
                "color_bar_reg((GXMVIEW)arg1, (GXITR)arg2, (GXITR)arg3, (GXREG)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a Color Bar in view\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Itr\n"
                ":type arg2: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg3: Optional 2nd Itr (can be null)\n"
                ":type arg3: :class:`geosoft.gxapi.GXITR`\n"
                ":param arg4: Parameters\n"
                ":type arg4: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					To allow for expansion, all parameters are passed inside the REG object.\n"
                "   \n"
                "   					BAR_ORIENTATION        one of MVU_ORIENTATION_XXX (DEFAULT = MVU_ORIENTATION_VERTICAL)\n"
                "   					DECIMALS					decimals in plotted values (see sFormatStr_GS for rules) (DEFAULT = 1)\n"
                "   					ANNOFF						annotation offset from bar (+/- determines side of the bar left/right and below/above)\n"
                "   					BOX_SIZE               box height (mm) (width for horizontal colour bar) (DEFAULT = 4)\n"
                "   					BAR_WIDTH              width (mm) (short dimension) of the colour bar (DEFAULT = 8)\n"
                "   					MINIMUM_GAP            Minimum space between annotations, otherwise drop annotations (DEFAULT = 0 mm)\n"
                "   					The actual height is over-estimated, so even with zero gap there will normally always be some space between labels.\n"
                "   					FIXED_INTERVAL         Preset interval for annotations scale (DEFAULT = DUMMY, use colour zones)\n"
                "   					FIXED_MINOR_INTERVAL   Preset minor interval for annotations scale (DEFAULT = DUMMY, if defined must be 1/10, 1/5, 1/4 or 1/2 of FIXED_INTERVAL)\n"
                "   					X								X location	(REQUIRED)\n"
                "   					Y								Y location	(REQUIRED)\n"
                "   					POST_MAXMIN            Post limit values at ends of the bar (0 or 1)? (DEFAULT = 0)\n"
                "   					DIVISION_STYLE         One of MVU_DIVISION_STYLE_XXX (DEFAULT = MVU_DIVISION_STYLE_LINES)\n"
                "   				\n\n"
               ).staticmethod("color_bar_reg");
    pyClass.def("contour", &GXMVU_wrap_contour,
                "contour((GXMVIEW)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a contour map.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Control file name\n"
                ":type arg2: str\n"
                ":param arg3: Grid file name\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("contour");
    pyClass.def("contour_ply", &GXMVU_wrap_contour_ply,
                "contour_ply((GXMVIEW)arg1, (GXPLY)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a contour map with clipped areas.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Clipping PLY\n"
                ":type arg2: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg3: Control file name\n"
                ":type arg3: str\n"
                ":param arg4: Grid file name\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The clipping PLY can include a surrounding inclusive polygon\n"
                "   					and zero, one or more interior exclusive polygons. Construct\n"
                "   					a PLY object using the \\ :func:`geosoft.gxapi.GXPLY.add_polygon_ex`\\  function, to add both\n"
                "   					inclusive (as the first PLY) and exclusive interior regions.\n"
                "   				\n\n"
               ).staticmethod("contour_ply");
    pyClass.def("c_symb_legend", &GXMVU_wrap_c_symb_legend,
                "c_symb_legend((GXMVIEW)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (str)arg6, (str)arg7, (str)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot a legend for the classified color symbols.\n\n"

                ":param arg1: MVIEW object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Plot origin X\n"
                ":type arg2: float\n"
                ":param arg3: Plot origin Y\n"
                ":type arg3: float\n"
                ":param arg4: Label Font size (mm)\n"
                ":type arg4: float\n"
                ":param arg5: Symbol scale factor\n"
                ":type arg5: float\n"
                ":param arg6: AGG, ITR or ZON file name\n"
                ":type arg6: str\n"
                ":param arg7: Plot title\n"
                ":type arg7: str\n"
                ":param arg8: Plot subtitle\n"
                ":type arg8: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the symbol size, colour, font etc are specified in\n"
                "   					the ITR's REG, then the Symbol scale factor is used\n"
                "   					allow the user to adjust the symbol sizes. They will be\n"
                "   					plotted at a size equal to the size in the REG times\n"
                "   					the scale factor.\n"
                "   					If no symbol size info can be found in the REG, then\n"
                "   					the symbol size is set equal to the Label Font Size.\n"
                "   					If no symbol font or number info is included in the\n"
                "   					REG, it is the programmer's responsibility to select\n"
                "   					the correct font and symbol before CSymbLegend is\n"
                "   					called. The same is true of the edge colour.\n"
                "   				\n\n"
               ).staticmethod("c_symb_legend");
    pyClass.def("decay_curve", &GXMVU_wrap_decay_curve,
                "decay_curve((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (GXVA)arg4, (GXVA)arg5, (int)arg6, (float)arg7, (float)arg8, (int)arg9, (int)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14, (float)arg15, (float)arg16, (float)arg17, (float)arg18, (float)arg19, (int)arg20, (str)arg21) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot decay curves at survey locations\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X coordinate VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y coordinate VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: VA channel to plot\n"
                ":type arg4: :class:`geosoft.gxapi.GXVA`\n"
                ":param arg5: VA channel as horizontal axis (normally time channel)\n"
                ":type arg5: :class:`geosoft.gxapi.GXVA`\n"
                ":param arg6: Log option: 0 linear (default), 1 logarithm, 2 log/linear\n"
                ":type arg6: int\n"
                ":param arg7: Min value to apply log (must be > 0.0)\n"
                ":type arg7: float\n"
                ":param arg8: Angle in degrees measured CCW from East of the map\n"
                ":type arg8: float\n"
                ":param arg9: Draw horizontal bar: 0 none, 1 bottom, 2 top, 3 both\n"
                ":type arg9: int\n"
                ":param arg10: Draw vertical bar:   0 none, 1 bottom, 2 top, 3 both\n"
                ":type arg10: int\n"
                ":param arg11: X offset in mm: Horizontal distance between survey location and origin of the box inside which decay curvey is drawn\n"
                ":type arg11: float\n"
                ":param arg12: Y offset in mm\n"
                ":type arg12: float\n"
                ":param arg13: Box width in mm:Decay curve at each survey location is drawn within this box\n"
                ":type arg13: float\n"
                ":param arg14: Box height in mm\n"
                ":type arg14: float\n"
                ":param arg15: Minimum value for X (horizontal axis)\n"
                ":type arg15: float\n"
                ":param arg16: Minimum value for Y (vertical axis)\n"
                ":type arg16: float\n"
                ":param arg17: X scale\n"
                ":type arg17: float\n"
                ":param arg18: Y scale\n"
                ":type arg18: float\n"
                ":param arg19: Line pitch, default is 5.0mm\n"
                ":type arg19: float\n"
                ":param arg20: line style\n"
                ":type arg20: int\n"
                ":param arg21: line color\n"
                ":type arg21: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Box width and height are used to draw horizontal and vertical\n"
                "   					bars. Curves outside the box are not clipped.\n"
                "   				\n\n"
               ).staticmethod("decay_curve");
    pyClass.def("direction_plot", &GXMVU_wrap_direction_plot,
                "direction_plot((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (float)arg4, (float)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot an arrow to indicate the direction of a flight line\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Arrow size in mm\n"
                ":type arg4: float\n"
                ":param arg5: Location to draw in mm - can be X or Y depending on next parameter\n"
                ":type arg5: float\n"
                ":param arg6: \\ :ref:`ARROW_ALIGNMENT`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					An arrow will be drawn in the direction from the first valid\n"
                "   					to the last points in the X and Y VVs.\n"
                "   				\n\n"
               ).staticmethod("direction_plot");
    pyClass.def("em_forward", &GXMVU_wrap_em_forward,
                "em_forward((GXMVIEW)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (int)arg8, (float)arg9, (float)arg10, (float)arg11, (float)arg12, (GXVV)arg13, (GXVV)arg14, (GXVV)arg15, (GXVV)arg16, (int)arg17, (int)arg18) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot an EM forward model against inverted data.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Plot X origin\n"
                ":type arg2: float\n"
                ":param arg3: Plot Y origin\n"
                ":type arg3: float\n"
                ":param arg4: Plot X size\n"
                ":type arg4: float\n"
                ":param arg5: Plot Y size\n"
                ":type arg5: float\n"
                ":param arg6: Coil Separation (m)\n"
                ":type arg6: float\n"
                ":param arg7: Coil Frequency (Hz)\n"
                ":type arg7: float\n"
                ":param arg8: \\ :ref:`EMLAY_GEOMETRY`\\ \n"
                ":type arg8: int\n"
                ":param arg9: Inverted or current resistivity\n"
                ":type arg9: float\n"
                ":param arg10: Inverted or current height\n"
                ":type arg10: float\n"
                ":param arg11: In-phase datum\n"
                ":type arg11: float\n"
                ":param arg12: Quadrature datum\n"
                ":type arg12: float\n"
                ":param arg13: Forward model resistivities\n"
                ":type arg13: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg14: Forward model heights\n"
                ":type arg14: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg15: Forward model In-phase (ppm)\n"
                ":type arg15: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg16: Forward model Quadrature (ppm)\n"
                ":type arg16: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg17: Plot resistivity as linear (0) or log (1)\n"
                ":type arg17: int\n"
                ":param arg18: Plot as function of resistivity (0) or height (1)\n"
                ":type arg18: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function is designed to display an inverted result beside\n"
                "   					the forward model curves. This is useful for trouble-shooting\n"
                "   					or understanding why a certain inversion result was obtained.\n"
                "   					The earth model is a simple halfspace.\n"
                "   					The forward model is plotted either as a function of\n"
                "   					resistivity at a single height, or as a function of height at\n"
                "   					a single resistivity. In either case, the relevant VVs must be\n"
                "   					completely filled (even if one is all the same value).\n"
                "   				\n\n"
               ).staticmethod("em_forward");
    pyClass.def("export_datamine_string", &GXMVU_wrap_export_datamine_string,
                "export_datamine_string((GXMVIEW)arg1, (GXLST)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export selected map groups in a map view to a Datamine coordinate string file.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: LST with group names in the name part of the LST.\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: Datamine string file (\\ `*`\\ .dm) to export to\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The lines, rectangles and polygons in the specified groups\n"
                "   					will be exported to a Datamine coordinate string (\\ `*`\\ .dm) file.\n"
                "   					The function attemps to duplicate the colours, etc. used.\n"
                "   					Complex polygon objects will be exported as independent\n"
                "   					single polygons.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXLST`\\  class\n\n"
               ).staticmethod("export_datamine_string");
    pyClass.def("export_dxf_3d", &GXMVU_wrap_export_dxf_3d,
                "export_dxf_3d((GXMVIEW)arg1, (GXLST)arg2, (GXWA)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export selected map groups in a map view to an AutoCAD 3D DXF file.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: LST with group names in the name part of the LST.\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: DXF file to export\n"
                ":type arg3: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Supported objects exported include lines, polygons, text.\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXLST`\\  class\n\n"
               ).staticmethod("export_dxf_3d");
    pyClass.def("export_surpac_str", &GXMVU_wrap_export_surpac_str,
                "export_surpac_str((GXMVIEW)arg1, (GXLST)arg2, (GXWA)arg3, (GXWA)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export selected map groups in a map view to a Surpac STR file.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: LST with group names in the name part of the LST.\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: STR file to export to\n"
                ":type arg3: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg4: Styles file to export to\n"
                ":type arg4: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The lines, rectangles and polygons in the specified groups\n"
                "   					will be exported to a Surpac STR file. An accompanying styles\n"
                "   					file will be created which will attempt to duplicate the\n"
                "   					colours, etc. used.\n"
                "   					Complex polygon objects will be exported as independent\n"
                "   					single polygons.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXLST`\\  class\n\n"
               ).staticmethod("export_surpac_str");
    pyClass.def("flight_plot", &GXMVU_wrap_flight_plot,
                "flight_plot((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (str)arg4, (int)arg5, (float)arg6, (int)arg7, (float)arg8, (float)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a flight line\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: line label\n"
                ":type arg4: str\n"
                ":param arg5: \\ :ref:`MVU_FLIGHT_LOCATE`\\ \n"
                ":type arg5: int\n"
                ":param arg6: lines steeper than this angle are considered vertical and the up label direction is used.\n"
                ":type arg6: float\n"
                ":param arg7: up label direction:   1 up is right, -1 up is left\n"
                ":type arg7: int\n"
                ":param arg8: along line label offset in mm.\n"
                ":type arg8: float\n"
                ":param arg9: perpendicular label offset mm.\n"
                ":type arg9: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Current line color, thickness and style are used to\n"
                "   					draw the line.\n"
                "   \n"
                "   					Current font, font colour and font style are used to\n"
                "   					annotate the line labels.\n"
                "   \n"
                "   					If current clipping is ON in the VIEW, lines will be\n"
                "   					clipped to the window before plotting.  In this case,\n"
                "   					labels should be located ABOVE or BELOW the line\n"
                "   					traces to prevent labels being clipped.\n"
                "   \n"
                "   					The offsets dOffA and dOffB control the vertical and\n"
                "   					horizontal label offsets with respect to the ends of\n"
                "   					the line trace and depending on the label location.\n"
                "   \n"
                "   					The vertical line reference angle dVerAng is used\n"
                "   					to determine if lines are considered vertical or\n"
                "   					horizontal.  Vertical lines use the sUp parameter\n"
                "   					to determine the label up direction.  Normally, use an\n"
                "   					angle of 60 degrees unless there are lines that run in\n"
                "   					this direction.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVU.path_plot`\\ \n\n"
               ).staticmethod("flight_plot");
    pyClass.def("gen_areas", &GXMVU_wrap_gen_areas,
                "gen_areas((GXMVIEW)arg1, (str)arg2, (GXVV)arg3, (GXVV)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate areas from an line group.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Group with lines\n"
                ":type arg2: str\n"
                ":param arg3: colours  (colour int)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: patterns (int), must be same length at colours\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: pattern size\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The specified line group will be used to create a new group that\n"
                "   					is composed of all the resolved polygonal areas in the line group.\n"
                "   					Each polygonal area is assigned a colour/pattern as specified in the\n"
                "   					colour and pattern VV's.  Colour/patterns are assigned in rotating\n"
                "   					sequence.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVU.re_gen_areas`\\ \n\n"
               ).staticmethod("gen_areas");
    pyClass.def("get_range_gocad_surface", &GXMVU_wrap_get_range_gocad_surface,
                "get_range_gocad_surface((str)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the XYZ range of a GOCAD surface.\n\n"

                ":param arg1: GOCAD file name\n"
                ":type arg1: str\n"
                ":param arg2: Min X value\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Min Y value\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Min Z value\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Max X value\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Max Y value\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Max Z value\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Required to set up a map view before doing the actual\n"
                "   					surface import.\n"
                "   				\n\n"
               ).staticmethod("get_range_gocad_surface");
    pyClass.def("histogram", &GXMVU_wrap_histogram,
                "histogram((GXMVIEW)arg1, (GXST)arg2, (GXST)arg3, (str)arg4, (str)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14, (int)arg15, (int)arg16, (int)arg17, (GXST)arg18) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot the histogram on a map.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: ST with summary stats of original data\n"
                ":type arg2: :class:`geosoft.gxapi.GXST`\n"
                ":param arg3: ST with histogram info of original or log10 data\n"
                ":type arg3: :class:`geosoft.gxapi.GXST`\n"
                ":param arg4: Title\n"
                ":type arg4: str\n"
                ":param arg5: unit\n"
                ":type arg5: str\n"
                ":param arg6: X in mm (bottom left corner of histogram box)\n"
                ":type arg6: float\n"
                ":param arg7: Y in mm (bottom left corner of histogram box)\n"
                ":type arg7: float\n"
                ":param arg8: box width in mm\n"
                ":type arg8: float\n"
                ":param arg9: box height in mm\n"
                ":type arg9: float\n"
                ":param arg10: Minimum X in data unit (bottom left corner of histogram boxes)\n"
                ":type arg10: float\n"
                ":param arg11: Minimum Y in data unit\n"
                ":type arg11: float\n"
                ":param arg12: box width in data unit\n"
                ":type arg12: float\n"
                ":param arg13: box height in data unit\n"
                ":type arg13: float\n"
                ":param arg14: width (mm) of the additional box for summary stats\n"
                ":type arg14: float\n"
                ":param arg15: Log horizontal axis: 0 - Normal, 1 - Log\n"
                ":type arg15: int\n"
                ":param arg16: Summary stats: 0 - do not draw, 1 - draw\n"
                ":type arg16: int\n"
                ":param arg17: Fill color\n"
                ":type arg17: int\n"
                ":param arg18: ST with histogram for box-whisker plot (-1 for no plot)\n"
                ":type arg18: :class:`geosoft.gxapi.GXST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function just calls \\ :func:`geosoft.gxapi.GXMVU.histogram2`\\  with decimals set\n"
                "   					to -7 (7 significant figures).\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVU.histogram2`\\ , \\ :func:`geosoft.gxapi.GXMVU.histogram3`\\ \n\n"
               ).staticmethod("histogram");
    pyClass.def("histogram2", &GXMVU_wrap_histogram2,
                "histogram2((GXMVIEW)arg1, (GXST)arg2, (GXST)arg3, (str)arg4, (str)arg5, (float)arg6, (str)arg7, (float)arg8, (str)arg9, (float)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14, (float)arg15, (float)arg16, (float)arg17, (float)arg18, (int)arg19, (int)arg20, (int)arg21, (GXST)arg22, (float)arg23) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot the histogram on a map.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: ST with summary stats of original data\n"
                ":type arg2: :class:`geosoft.gxapi.GXST`\n"
                ":param arg3: ST with histogram info of original or log10 data\n"
                ":type arg3: :class:`geosoft.gxapi.GXST`\n"
                ":param arg4: X axis title\n"
                ":type arg4: str\n"
                ":param arg5: Y axis title\n"
                ":type arg5: str\n"
                ":param arg6: Text size in mm for X/Y axis' titles. Accept dummy\n"
                ":type arg6: float\n"
                ":param arg7: Overall title. Plotted below X axis if X axis title is not given\n"
                ":type arg7: str\n"
                ":param arg8: Text size in mm for plot overall title. Accept dummy\n"
                ":type arg8: float\n"
                ":param arg9: unit\n"
                ":type arg9: str\n"
                ":param arg10: X in mm (bottom left corner of histogram box)\n"
                ":type arg10: float\n"
                ":param arg11: Y in mm (bottom left corner of histogram box)\n"
                ":type arg11: float\n"
                ":param arg12: box width in mm\n"
                ":type arg12: float\n"
                ":param arg13: box height in mm\n"
                ":type arg13: float\n"
                ":param arg14: Minimum X in data unit (bottom left corner of histogram boxes)\n"
                ":type arg14: float\n"
                ":param arg15: Minimum Y in data unit\n"
                ":type arg15: float\n"
                ":param arg16: box width in data unit\n"
                ":type arg16: float\n"
                ":param arg17: box height in data unit\n"
                ":type arg17: float\n"
                ":param arg18: width (mm) of the additional box for summary stats\n"
                ":type arg18: float\n"
                ":param arg19: Log horizontal axis: 0 - Normal, 1 - Log\n"
                ":type arg19: int\n"
                ":param arg20: Summary stats: 0 - do not draw, 1 - draw\n"
                ":type arg20: int\n"
                ":param arg21: Fill color\n"
                ":type arg21: int\n"
                ":param arg22: ST with histogram for box-wisker plot (-1 for no plot)\n"
                ":type arg22: :class:`geosoft.gxapi.GXST`\n"
                ":param arg23: X value (threshold value) to draw a vertical line (see notes)\n"
                ":type arg23: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A vertical line through from bottom to top horizontal axis is drawn\n"
                "   					Also a label 'Threshold value' is plotted against this line. However,\n"
                "   					None of them will be plotted if threshold value is dummy or outside\n"
                "   					the X data range.\n"
                "   				\n\n"
               ).staticmethod("histogram2");
    pyClass.def("histogram3", &GXMVU_wrap_histogram3,
                "histogram3((GXMVIEW)arg1, (GXST)arg2, (GXST)arg3, (str)arg4, (str)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14, (int)arg15, (int)arg16, (int)arg17, (int)arg18, (int)arg19, (GXST)arg20) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot the histogram on a map, specify decimals.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: ST with summary stats of original data\n"
                ":type arg2: :class:`geosoft.gxapi.GXST`\n"
                ":param arg3: ST with histogram info of original or log10 data\n"
                ":type arg3: :class:`geosoft.gxapi.GXST`\n"
                ":param arg4: Title\n"
                ":type arg4: str\n"
                ":param arg5: unit\n"
                ":type arg5: str\n"
                ":param arg6: X in mm (bottom left corner of histogram box)\n"
                ":type arg6: float\n"
                ":param arg7: Y in mm (bottom left corner of histogram box)\n"
                ":type arg7: float\n"
                ":param arg8: box width in mm\n"
                ":type arg8: float\n"
                ":param arg9: box height in mm\n"
                ":type arg9: float\n"
                ":param arg10: Minimum X in data unit (bottom left corner of histogram boxes)\n"
                ":type arg10: float\n"
                ":param arg11: Minimum Y in data unit\n"
                ":type arg11: float\n"
                ":param arg12: box width in data unit\n"
                ":type arg12: float\n"
                ":param arg13: box height in data unit\n"
                ":type arg13: float\n"
                ":param arg14: width (mm) of the additional box for summary stats\n"
                ":type arg14: float\n"
                ":param arg15: Log horizontal axis: 0 - Normal, 1 - Log\n"
                ":type arg15: int\n"
                ":param arg16: Summary stats: 0 - do not draw, 1 - draw\n"
                ":type arg16: int\n"
                ":param arg17: Fill color\n"
                ":type arg17: int\n"
                ":param arg18: Decimals for data, negative for sig. fig.\n"
                ":type arg18: int\n"
                ":param arg19: Decimals for stats, negative for sig. fig.\n"
                ":type arg19: int\n"
                ":param arg20: ST with histogram for box-whisker plot (-1 for no plot)\n"
                ":type arg20: :class:`geosoft.gxapi.GXST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("histogram3");
    pyClass.def("histogram4", &GXMVU_wrap_histogram4,
                "histogram4((GXMVIEW)arg1, (GXST)arg2, (GXST)arg3, (str)arg4, (str)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14, (int)arg15, (int)arg16, (int)arg17, (int)arg18, (int)arg19, (int)arg20, (GXST)arg21) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   As \\ :func:`geosoft.gxapi.GXMVU.histogram3`\\ , but allow probability scaling of percents.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: ST with summary stats of original data\n"
                ":type arg2: :class:`geosoft.gxapi.GXST`\n"
                ":param arg3: ST with histogram info of original or log10 data\n"
                ":type arg3: :class:`geosoft.gxapi.GXST`\n"
                ":param arg4: Title\n"
                ":type arg4: str\n"
                ":param arg5: unit\n"
                ":type arg5: str\n"
                ":param arg6: X in mm (bottom left corner of histogram box)\n"
                ":type arg6: float\n"
                ":param arg7: Y in mm (bottom left corner of histogram box)\n"
                ":type arg7: float\n"
                ":param arg8: box width in mm\n"
                ":type arg8: float\n"
                ":param arg9: box height in mm\n"
                ":type arg9: float\n"
                ":param arg10: Minimum X in data unit (bottom left corner of histogram boxes)\n"
                ":type arg10: float\n"
                ":param arg11: Minimum Y in data unit\n"
                ":type arg11: float\n"
                ":param arg12: box width in data unit\n"
                ":type arg12: float\n"
                ":param arg13: box height in data unit\n"
                ":type arg13: float\n"
                ":param arg14: width (mm) of the additional box for summary stats\n"
                ":type arg14: float\n"
                ":param arg15: Log horizontal axis: 0 - Normal, 1 - Log\n"
                ":type arg15: int\n"
                ":param arg16: Summary stats: 0 - do not draw, 1 - draw\n"
                ":type arg16: int\n"
                ":param arg17: Probability scaling: 0 - linear scale, 1 - scale as normal distribution\n"
                ":type arg17: int\n"
                ":param arg18: Fill color\n"
                ":type arg18: int\n"
                ":param arg19: Decimals for data, negative for sig. fig.\n"
                ":type arg19: int\n"
                ":param arg20: Decimals for stats, negative for sig. fig.\n"
                ":type arg20: int\n"
                ":param arg21: ST with histogram for box-whisker plot (-1 for no plot)\n"
                ":type arg21: :class:`geosoft.gxapi.GXST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("histogram4");
    pyClass.def("histogram5", &GXMVU_wrap_histogram5,
                "histogram5((GXMVIEW)arg1, (GXST)arg2, (GXST)arg3, (str)arg4, (str)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14, (float)arg15, (int)arg16, (int)arg17, (int)arg18, (int)arg19, (int)arg20, (int)arg21, (GXST)arg22, (GXITR)arg23) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   As \\ :func:`geosoft.gxapi.GXMVU.histogram4`\\ , but allow ITR to colour bars.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: ST with summary stats of original data\n"
                ":type arg2: :class:`geosoft.gxapi.GXST`\n"
                ":param arg3: ST with histogram info of original or log10 data\n"
                ":type arg3: :class:`geosoft.gxapi.GXST`\n"
                ":param arg4: Title\n"
                ":type arg4: str\n"
                ":param arg5: unit\n"
                ":type arg5: str\n"
                ":param arg6: [i] Lambda Value\n"
                ":type arg6: float\n"
                ":param arg7: X in mm (bottom left corner of histogram box)\n"
                ":type arg7: float\n"
                ":param arg8: Y in mm (bottom left corner of histogram box)\n"
                ":type arg8: float\n"
                ":param arg9: box width in mm\n"
                ":type arg9: float\n"
                ":param arg10: box height in mm\n"
                ":type arg10: float\n"
                ":param arg11: Minimum X in data unit (bottom left corner of histogram boxes)\n"
                ":type arg11: float\n"
                ":param arg12: Minimum Y in data unit\n"
                ":type arg12: float\n"
                ":param arg13: box width in data unit\n"
                ":type arg13: float\n"
                ":param arg14: box height in data unit\n"
                ":type arg14: float\n"
                ":param arg15: width (mm) of the additional box for summary stats\n"
                ":type arg15: float\n"
                ":param arg16: Log horizontal axis: 0 - Normal, 1 - Log, 2 - Lambda\n"
                ":type arg16: int\n"
                ":param arg17: Summary stats: 0 - do not draw, 1 - draw\n"
                ":type arg17: int\n"
                ":param arg18: Probability scaling: 0 - linear scale, 1 - scale as normal distribution\n"
                ":type arg18: int\n"
                ":param arg19: Fill color\n"
                ":type arg19: int\n"
                ":param arg20: Decimals for data, negative for sig. fig.\n"
                ":type arg20: int\n"
                ":param arg21: Decimals for stats, negative for sig. fig.\n"
                ":type arg21: int\n"
                ":param arg22: ST with histogram for box-whisker plot (-1 for no plot)\n"
                ":type arg22: :class:`geosoft.gxapi.GXST`\n"
                ":param arg23: ITR to colour bars.\n"
                ":type arg23: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The ITR can be empty (but must still be a valid ITR object).\n\n"
               ).staticmethod("histogram5");
    pyClass.def("exportable_dxf_3d_groups_lst", &GXMVU_wrap_exportable_dxf_3d_groups_lst,
                "exportable_dxf_3d_groups_lst((GXMVIEW)arg1, (GXLST)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return a LST of groups you can export using sExportDXF3D_MVU.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: LST with group names in the name part of the LST.\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: The number of groups in the LST.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns a list of visible groups that the DXF 3D export can\n"
                "   					export. Removes things like VOXD, AGG, and target\n"
                "   					groups starting with \"Dh\", which are typically plotted in 3D\n"
                "   					views on a reference plan oriented toward the user, and thus\n"
                "   					not exportable.\n"
                "   				\n\n"
               ).staticmethod("exportable_dxf_3d_groups_lst");
    pyClass.def("mapset_test", &GXMVU_wrap_mapset_test,
                "mapset_test((float)arg1, (float)arg2, (float)arg3, (float)arg4, (str)arg5, (int)arg6, (int)arg7, (float_ref)arg8, (float)arg9, (float)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Test function to ensure parameters to \\ :func:`geosoft.gxapi.GXMVU.mapset`\\  is sane\n\n"

                ":param arg1: Minimum X of map area (ground units)\n"
                ":type arg1: float\n"
                ":param arg2: Maximum X of map area (ground units)\n"
                ":type arg2: float\n"
                ":param arg3: Minimum Y of map area (ground units)\n"
                ":type arg3: float\n"
                ":param arg4: Maximum Y of map area (ground units)\n"
                ":type arg4: float\n"
                ":param arg5: Size of paper (e.g. A1, E, etc.)\n"
                ":type arg5: str\n"
                ":param arg6: Portrait map? (or landscape) (FALSE by default)\n"
                ":type arg6: int\n"
                ":param arg7: Map is exactly sized to area? (or trimmed to data and margins) (FALSE by default)\n"
                ":type arg7: int\n"
                ":param arg8: Map scale (rDummy for default)\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Conversion factor (to units/meter) (rDummy for default)\n"
                ":type arg9: float\n"
                ":param arg10: Minimum X of margin area (cm)\n"
                ":type arg10: float\n"
                ":param arg11: Maximum X of margin area (cm)\n"
                ":type arg11: float\n"
                ":param arg12: Minimum Y of margin area (cm)\n"
                ":type arg12: float\n"
                ":param arg13: Maximum Y of margin area (cm)\n"
                ":type arg13: float\n"
                ":param arg14: Inside edge (cm)\n"
                ":type arg14: float\n"
                ":returns: bool TRUE if the parameters are good.\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Use \\ :func:`geosoft.gxapi.GXSYS.show_error`\\  to display errors that may have been encountered. This function can also be used\n"
                "   					to calculate the default scale without creating a map.\n"
                "   				\n\n"
               ).staticmethod("mapset_test");
    pyClass.def("mapset2_test", &GXMVU_wrap_mapset2_test,
                "mapset2_test((float)arg1, (float)arg2, (float)arg3, (float)arg4, (str)arg5, (int)arg6, (int)arg7, (float_ref)arg8, (float)arg9, (float)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14, (float)arg15) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Test function to ensure parameters to \\ :func:`geosoft.gxapi.GXMVU.mapset`\\  is sane\n\n"

                ":param arg1: Minimum X of map area (ground units)\n"
                ":type arg1: float\n"
                ":param arg2: Maximum X of map area (ground units)\n"
                ":type arg2: float\n"
                ":param arg3: Minimum Y of map area (ground units)\n"
                ":type arg3: float\n"
                ":param arg4: Maximum Y of map area (ground units)\n"
                ":type arg4: float\n"
                ":param arg5: Size of paper (e.g. A1, E, etc.)\n"
                ":type arg5: str\n"
                ":param arg6: Portrait map? (or landscape) (FALSE by default)\n"
                ":type arg6: int\n"
                ":param arg7: Map is exactly sized to area? (or trimmed to data and margins) (FALSE by default)\n"
                ":type arg7: int\n"
                ":param arg8: Map scale (rDummy for default)\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Vertical exaggeration (Normally 1.0)\n"
                ":type arg9: float\n"
                ":param arg10: Conversion factor (to units/meter) (rDummy for default)\n"
                ":type arg10: float\n"
                ":param arg11: Minimum X of margin area (cm)\n"
                ":type arg11: float\n"
                ":param arg12: Maximum X of margin area (cm)\n"
                ":type arg12: float\n"
                ":param arg13: Minimum Y of margin area (cm)\n"
                ":type arg13: float\n"
                ":param arg14: Maximum Y of margin area (cm)\n"
                ":type arg14: float\n"
                ":param arg15: Inside edge (cm)\n"
                ":type arg15: float\n"
                ":returns: bool TRUE if the parameters are good.\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Same as \\ :func:`geosoft.gxapi.GXMVU.mapset_test`\\ , with vertical exaggeration.\n"
                "   				\n\n"
               ).staticmethod("mapset2_test");
    pyClass.def("import_gocad_surface", &GXMVU_wrap_import_gocad_surface,
                "import_gocad_surface((GXMVIEW)arg1, (str)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import and plot a GOCAD surface model.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: GOCAD file name\n"
                ":type arg2: str\n"
                ":param arg3: Color to plot (C_TRANSPARENT to use file-defined colour).\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The vertex normals are not included in the\n"
                "   					GOCAD import, but are calculated using\n"
                "   					the normal of each defined triangle, and taking the\n"
                "   					average when vertex is shared among more than one triangle.\n"
                "   				\n\n"
               ).staticmethod("import_gocad_surface");
    pyClass.def("load_plot", &GXMVU_wrap_load_plot,
                "load_plot((GXMAP)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a Geosoft PLT file into a MAP.\n\n"

                ":param arg1: Map handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: plot file name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("load_plot");
    pyClass.def("map_from_plt", &GXMVU_wrap_map_from_plt,
                "map_from_plt((GXMAP)arg1, (str)arg2, (str)arg3, (str)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a new map from a PLT file.\n\n"

                ":param arg1: MAP Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: Name to use for the base map view\n"
                ":type arg2: str\n"
                ":param arg3: Name to use for the data view\n"
                ":type arg3: str\n"
                ":param arg4: Plot file name\n"
                ":type arg4: str\n"
                ":param arg5: Map paper size in X direction (cm)\n"
                ":type arg5: float\n"
                ":param arg6: Map paper size in Y direction (cm)\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This only creates a map, it does not read the PLT into\n"
                "   					the map.  The base view and data view will be the same\n"
                "   					size.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVU.load_plot`\\ \n\n"
               ).staticmethod("map_from_plt");
    pyClass.def("map_mdf", &GXMVU_wrap_map_mdf,
                "map_mdf((GXMAP)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates an MDF from a Map.\n\n"

                ":param arg1: MAP Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: MDF file name\n"
                ":type arg2: str\n"
                ":param arg3: Data view name\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("map_mdf");
    pyClass.def("mapset", &GXMVU_wrap_mapset,
                "mapset((GXMAP)arg1, (str)arg2, (str)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (str)arg8, (int)arg9, (int)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14, (float)arg15, (float)arg16, (float)arg17) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a new map directly from parameters.\n\n"

                ":param arg1: MAP Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: Name to use for the base map view\n"
                ":type arg2: str\n"
                ":param arg3: Name to use for the data view\n"
                ":type arg3: str\n"
                ":param arg4: Minimum X of map area (ground units)\n"
                ":type arg4: float\n"
                ":param arg5: Maximum X of map area (ground units)\n"
                ":type arg5: float\n"
                ":param arg6: Minimum Y of map area (ground units)\n"
                ":type arg6: float\n"
                ":param arg7: Maximum Y of map area (ground units)\n"
                ":type arg7: float\n"
                ":param arg8: Size of paper (e.g. A1, E, etc.)\n"
                ":type arg8: str\n"
                ":param arg9: Portrait map? (or landscape) (FALSE by default)\n"
                ":type arg9: int\n"
                ":param arg10: Map is exactly sized to area? (or trimmed to data and margins) (FALSE by default)\n"
                ":type arg10: int\n"
                ":param arg11: Map scale (rDummy for default)\n"
                ":type arg11: float\n"
                ":param arg12: Conversion factor (to units/meter) (rDummy for default)\n"
                ":type arg12: float\n"
                ":param arg13: Minimum X of margin area (cm)\n"
                ":type arg13: float\n"
                ":param arg14: Maximum X of margin area (cm)\n"
                ":type arg14: float\n"
                ":param arg15: Minimum Y of margin area (cm)\n"
                ":type arg15: float\n"
                ":param arg16: Maximum Y of margin area (cm)\n"
                ":type arg16: float\n"
                ":param arg17: Inside edge (cm)\n"
                ":type arg17: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("mapset");
    pyClass.def("mapset2", &GXMVU_wrap_mapset2,
                "mapset2((GXMAP)arg1, (str)arg2, (str)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (str)arg8, (int)arg9, (int)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14, (float)arg15, (float)arg16, (float)arg17, (float)arg18) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXMVU.mapset`\\ , with vertical exaggeration.\n\n"

                ":param arg1: MAP Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: Name to use for the base map view\n"
                ":type arg2: str\n"
                ":param arg3: Name to use for the data view\n"
                ":type arg3: str\n"
                ":param arg4: Minimum X of map area (ground units)\n"
                ":type arg4: float\n"
                ":param arg5: Maximum X of map area (ground units)\n"
                ":type arg5: float\n"
                ":param arg6: Minimum Y of map area (ground units)\n"
                ":type arg6: float\n"
                ":param arg7: Maximum Y of map area (ground units)\n"
                ":type arg7: float\n"
                ":param arg8: Size of paper (e.g. A1, E, etc.)\n"
                ":type arg8: str\n"
                ":param arg9: Portrait map? (or landscape) (FALSE by default)\n"
                ":type arg9: int\n"
                ":param arg10: Map is exactly sized to area? (or trimmed to data and margins) (FALSE by default)\n"
                ":type arg10: int\n"
                ":param arg11: Map scale (rDummy for default)\n"
                ":type arg11: float\n"
                ":param arg12: Vertical Exaggeration (1.0 for none)\n"
                ":type arg12: float\n"
                ":param arg13: Conversion factor (to units/meter) (rDummy for default)\n"
                ":type arg13: float\n"
                ":param arg14: Minimum X of margin area (cm)\n"
                ":type arg14: float\n"
                ":param arg15: Maximum X of margin area (cm)\n"
                ":type arg15: float\n"
                ":param arg16: Minimum Y of margin area (cm)\n"
                ":type arg16: float\n"
                ":param arg17: Maximum Y of margin area (cm)\n"
                ":type arg17: float\n"
                ":param arg18: Inside edge (cm)\n"
                ":type arg18: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"
               ).staticmethod("mapset2");
    pyClass.def("mdf", &GXMVU_wrap_mdf,
                "mdf((GXMAP)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a new map from an MDF file.\n\n"

                ":param arg1: MAP Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: MDF file name\n"
                ":type arg2: str\n"
                ":param arg3: Name to use for the base map view\n"
                ":type arg3: str\n"
                ":param arg4: Name to use for the data view\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("mdf");
    pyClass.def("path_plot", &GXMVU_wrap_path_plot,
                "path_plot((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (str)arg4, (int)arg5, (float)arg6, (int)arg7, (float)arg8, (float)arg9, (float)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a flight line\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: line label\n"
                ":type arg4: str\n"
                ":param arg5: \\ :ref:`MVU_FLIGHT_LOCATE`\\ \n"
                ":type arg5: int\n"
                ":param arg6: lines steeper than this angle are considered vertical and the up label direction is used.\n"
                ":type arg6: float\n"
                ":param arg7: up label direction:   1 up is right -1 up is left\n"
                ":type arg7: int\n"
                ":param arg8: along line label offset in mm.\n"
                ":type arg8: float\n"
                ":param arg9: perpendicular label offset mm.\n"
                ":type arg9: float\n"
                ":param arg10: maximum gap before breaking line, 0.0 for no breaks.\n"
                ":type arg10: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					See \\ :func:`geosoft.gxapi.GXMVU.flight_plot`\\ .  This is the same except for the\n"
                "   					additional line gap parameter.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   FlighPlot_MVU\n\n"
               ).staticmethod("path_plot");
    pyClass.def("path_plot_ex", &GXMVU_wrap_path_plot_ex,
                "path_plot_ex((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (str)arg4, (int)arg5, (int)arg6, (float)arg7, (int)arg8, (float)arg9, (float)arg10, (float)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a flight line\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: line label\n"
                ":type arg4: str\n"
                ":param arg5: \\ :ref:`MVU_FLIGHT_LOCATE`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`MVU_FLIGHT_COMPASS`\\ \n"
                ":type arg6: int\n"
                ":param arg7: lines steeper than this angle are considered vertical and the up label direction is used.\n"
                ":type arg7: float\n"
                ":param arg8: up label direction:   1 up is right -1 up is left\n"
                ":type arg8: int\n"
                ":param arg9: along line label offset in mm.\n"
                ":type arg9: float\n"
                ":param arg10: perpendicular label offset mm.\n"
                ":type arg10: float\n"
                ":param arg11: maximum gap before breaking line, 0.0 for no breaks.\n"
                ":type arg11: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This is the same except for the additional line compass parameter.\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVU.path_plot`\\ \n\n"
               ).staticmethod("path_plot_ex");
    pyClass.def("path_plot_ex2", &GXMVU_wrap_path_plot_ex2,
                "path_plot_ex2((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (str)arg4, (int)arg5, (int)arg6, (float)arg7, (int)arg8, (float)arg9, (float)arg10, (float)arg11, (int)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a flight line\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: line label\n"
                ":type arg4: str\n"
                ":param arg5: \\ :ref:`MVU_FLIGHT_LOCATE`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`MVU_FLIGHT_COMPASS`\\ \n"
                ":type arg6: int\n"
                ":param arg7: lines steeper than this angle are considered vertical and the up label direction is used.\n"
                ":type arg7: float\n"
                ":param arg8: up label direction:   1 up is right -1 up is left\n"
                ":type arg8: int\n"
                ":param arg9: along line label offset in mm.\n"
                ":type arg9: float\n"
                ":param arg10: perpendicular label offset mm.\n"
                ":type arg10: float\n"
                ":param arg11: maximum gap before breaking line, 0.0 for no breaks.\n"
                ":type arg11: float\n"
                ":param arg12: \\ :ref:`MVU_FLIGHT_DUMMIES`\\ \n"
                ":type arg12: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This is the same except for the additional line dummies parameter.\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVU.path_plot_ex`\\ \n\n"
               ).staticmethod("path_plot_ex2");
    pyClass.def("plot_voxel_surface", &GXMVU_wrap_plot_voxel_surface,
                "plot_voxel_surface((GXMVIEW)arg1, (GXVOX)arg2, (float)arg3, (int)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Extract an iso-surface from a voxel and plot it to a 2D or 3D view.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Voxel model\n"
                ":type arg2: :class:`geosoft.gxapi.GXVOX`\n"
                ":param arg3: Iso-surface value\n"
                ":type arg3: float\n"
                ":param arg4: Drawing colour\n"
                ":type arg4: int\n"
                ":param arg5: Line thickness for line drawing, and 2D views.\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The Marching Cubes method of Lorensen and Cline, Computer Graphics, V21,\n"
                "   					Number 4, July 1987, is used to calculate a given iso-surface in a voxel\n"
                "   					model. The resulting surface is plotted to a 2D or 3D view. If the view\n"
                "   					is 2-D, then only the intersection of the surface with the 2D surface is\n"
                "   					plotted, using lines.\n"
                "   				\n\n"
               ).staticmethod("plot_voxel_surface");
    pyClass.def("plot_voxel_surface2", &GXMVU_wrap_plot_voxel_surface2,
                "plot_voxel_surface2((GXMVIEW)arg1, (GXVOX)arg2, (float)arg3, (int)arg4, (float)arg5, (float)arg6, (str)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Extract an iso-surface from a voxel and plot it to a 2D or 3D view.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Voxel model\n"
                ":type arg2: :class:`geosoft.gxapi.GXVOX`\n"
                ":param arg3: Iso-surface value\n"
                ":type arg3: float\n"
                ":param arg4: Drawing colour\n"
                ":type arg4: int\n"
                ":param arg5: Line thickness for line drawing, and 2D views.\n"
                ":type arg5: float\n"
                ":param arg6: Transparency (0 - transparent, 1 - opaque).\n"
                ":type arg6: float\n"
                ":param arg7: Iso-surface name\n"
                ":type arg7: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The Marching Cubes method of Lorensen and Cline, Computer Graphics, V21,\n"
                "   					Number 4, July 1987, is used to calculate a given iso-surface in a voxel\n"
                "   					model. The resulting surface is plotted to a 2D or 3D view. If the view\n"
                "   					is 2-D, then only the intersection of the surface with the 2D surface is\n"
                "   					plotted, using lines.\n"
                "   				\n\n"
               ).staticmethod("plot_voxel_surface2");
    pyClass.def("generate_surface_from_voxel", &GXMVU_wrap_generate_surface_from_voxel,
                "generate_surface_from_voxel((GXMVIEW)arg1, (GXVOX)arg2, (int)arg3, (int)arg4, (float)arg5, (float)arg6, (int)arg7, (float)arg8, (float)arg9, (str)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   TODO...\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Voxel model\n"
                ":type arg2: :class:`geosoft.gxapi.GXVOX`\n"
                ":param arg3: \\ :ref:`MVU_VOX_SURFACE_METHOD`\\ \n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`MVU_VOX_SURFACE_OPTION`\\ \n"
                ":type arg4: int\n"
                ":param arg5: TODO\n"
                ":type arg5: float\n"
                ":param arg6: TODO\n"
                ":type arg6: float\n"
                ":param arg7: Drawing colour\n"
                ":type arg7: int\n"
                ":param arg8: Line thickness for line drawing, and 2D views.\n"
                ":type arg8: float\n"
                ":param arg9: Transparency (0 - transparent, 1 - opaque).\n"
                ":type arg9: float\n"
                ":param arg10: Geosurface file\n"
                ":type arg10: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   TODO... Move to VOX method for surface generation only and use GeosurfaceD to display.\n\n"
               ).staticmethod("generate_surface_from_voxel");
    pyClass.def("post", &GXMVU_wrap_post,
                "post((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (bool)arg5, (int)arg6, (int)arg7, (int)arg8, (int)arg9, (float)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Post values on a map.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y locations\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Values to post\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Do not plot dummy values? bool\n"
                ":type arg5: bool\n"
                ":param arg6: Numb Size\n"
                ":type arg6: int\n"
                ":param arg7: Format\n"
                ":type arg7: int\n"
                ":param arg8: Decimals\n"
                ":type arg8: int\n"
                ":param arg9: Reference point number\n"
                ":type arg9: int\n"
                ":param arg10: Text angle\n"
                ":type arg10: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("post");
    pyClass.def("post_ex", &GXMVU_wrap_post_ex,
                "post_ex((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (bool)arg6, (float)arg7, (float)arg8, (int)arg9, (int)arg10, (int)arg11, (float)arg12, (float)arg13, (int)arg14, (float)arg15, (int)arg16, (float)arg17, (int)arg18, (float)arg19, (int)arg20) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Post values on a map with more paramters.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y locations\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Values to post\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Station\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Do not plot dummy values? bool\n"
                ":type arg6: bool\n"
                ":param arg7: Base to remove, default is 0.0\n"
                ":type arg7: float\n"
                ":param arg8: detection limit, can be GS_R8DM\n"
                ":type arg8: float\n"
                ":param arg9: Numb Size\n"
                ":type arg9: int\n"
                ":param arg10: Format\n"
                ":type arg10: int\n"
                ":param arg11: Decimals\n"
                ":type arg11: int\n"
                ":param arg12: Offset along line (right and above are positive)\n"
                ":type arg12: float\n"
                ":param arg13: Offset perpendicular to line\n"
                ":type arg13: float\n"
                ":param arg14: TRUE - Positive above, Negative below FALSE - All above.\n"
                ":type arg14: int\n"
                ":param arg15: Modulas on station vv\n"
                ":type arg15: float\n"
                ":param arg16: Reference point number\n"
                ":type arg16: int\n"
                ":param arg17: Text angle (degree, CCW from down-line)\n"
                ":type arg17: float\n"
                ":param arg18: Fixed angle ?\n"
                ":type arg18: int\n"
                ":param arg19: vertical reference angle\n"
                ":type arg19: float\n"
                ":param arg20: 1 up is right, -1 up is left\n"
                ":type arg20: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("post_ex");
    pyClass.def("probability", &GXMVU_wrap_probability,
                "probability((GXMVIEW)arg1, (GXST)arg2, (GXST)arg3, (str)arg4, (str)arg5, (int)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14, (int)arg15, (int)arg16, (int)arg17, (GXITR)arg18) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot a probability plot on a map.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: ST with summary stats of original data\n"
                ":type arg2: :class:`geosoft.gxapi.GXST`\n"
                ":param arg3: ST with histogram info of original or log10 data\n"
                ":type arg3: :class:`geosoft.gxapi.GXST`\n"
                ":param arg4: Title\n"
                ":type arg4: str\n"
                ":param arg5: unit\n"
                ":type arg5: str\n"
                ":param arg6: Transform type (0: Raw, 1: Log, 2: Lambda)\n"
                ":type arg6: int\n"
                ":param arg7: Lambda Value for lambda transform\n"
                ":type arg7: float\n"
                ":param arg8: X in mm (bottom left corner of histogram box)\n"
                ":type arg8: float\n"
                ":param arg9: Y in mm (bottom left corner of histogram box)\n"
                ":type arg9: float\n"
                ":param arg10: box width in mm\n"
                ":type arg10: float\n"
                ":param arg11: box height in mm\n"
                ":type arg11: float\n"
                ":param arg12: symbol size in mm\n"
                ":type arg12: float\n"
                ":param arg13: Sigma (X range is -sigma to sigma)\n"
                ":type arg13: float\n"
                ":param arg14: width (mm) of the additional box for summary stats\n"
                ":type arg14: float\n"
                ":param arg15: Summary stats: 0 - do not draw, 1 - draw\n"
                ":type arg15: int\n"
                ":param arg16: Decimals for data, negative for sig. fig.\n"
                ":type arg16: int\n"
                ":param arg17: Decimals for stats, negative for sig. fig.\n"
                ":type arg17: int\n"
                ":param arg18: ITR to colour symbols.\n"
                ":type arg18: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The ITR can be empty (but must still be a valid ITR object).\n\n"
               ).staticmethod("probability");
    pyClass.def("profile_plot", &GXMVU_wrap_profile_plot,
                "profile_plot((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (float)arg5, (int)arg6, (float)arg7, (float)arg8, (float)arg9, (int)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a profile along line trace\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Z\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: lines steeper than this angle are considered vertical and the up label direction is used.\n"
                ":type arg5: float\n"
                ":param arg6: up label direction:   1 up is right -1 up is left\n"
                ":type arg6: int\n"
                ":param arg7: Maximum gap in data to span (view units)\n"
                ":type arg7: float\n"
                ":param arg8: Z profile base, rDUMMY to use data minimum\n"
                ":type arg8: float\n"
                ":param arg9: Z scale in view units/Z unit\n"
                ":type arg9: float\n"
                ":param arg10: 1 to join profile to line ends.\n"
                ":type arg10: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Profiles will be drawn in the current line style.\n\n"
               ).staticmethod("profile_plot");
    pyClass.def("profile_plot_ex", &GXMVU_wrap_profile_plot_ex,
                "profile_plot_ex((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (float)arg5, (int)arg6, (float)arg7, (float)arg8, (float)arg9, (int)arg10, (int)arg11, (float)arg12, (int)arg13, (str)arg14, (str)arg15) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a profile along line trace with more parameters\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Z\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: lines steeper than this angle are considered vertical and the up label direction is used.\n"
                ":type arg5: float\n"
                ":param arg6: up label direction:   1 up is right -1 up is left\n"
                ":type arg6: int\n"
                ":param arg7: Maximum gap in data to span (view units)\n"
                ":type arg7: float\n"
                ":param arg8: Z profile base, rDUMMY to use data minimum\n"
                ":type arg8: float\n"
                ":param arg9: Z scale in view units/Z unit\n"
                ":type arg9: float\n"
                ":param arg10: 1 to join profile to line ends.\n"
                ":type arg10: int\n"
                ":param arg11: Log option: 0 linear (default), 1 logarithm, 2 log/linear\n"
                ":type arg11: int\n"
                ":param arg12: Log base\n"
                ":type arg12: float\n"
                ":param arg13: Smooth curve option: 0 no (default), 1 yes\n"
                ":type arg13: int\n"
                ":param arg14: positive fill color\n"
                ":type arg14: str\n"
                ":param arg15: negative fill color\n"
                ":type arg15: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Profiles will be drawn in the current line style.\n\n"
               ).staticmethod("profile_plot_ex");
    pyClass.def("prop_symb_legend", &GXMVU_wrap_prop_symb_legend,
                "prop_symb_legend((GXMVIEW)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (int)arg7, (float)arg8, (float)arg9, (str)arg10, (str)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a legend for proportional symbols.\n\n"

                ":param arg1: MVIEW object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Plot origin X\n"
                ":type arg2: float\n"
                ":param arg3: Plot origin Y\n"
                ":type arg3: float\n"
                ":param arg4: Label Font size (mm)\n"
                ":type arg4: float\n"
                ":param arg5: Symbol scale factor (data value/mm)\n"
                ":type arg5: float\n"
                ":param arg6: Base value to remove before scaling\n"
                ":type arg6: float\n"
                ":param arg7: Number of symbols\n"
                ":type arg7: int\n"
                ":param arg8: Starting symbol data value (>= Base value)\n"
                ":type arg8: float\n"
                ":param arg9: Data value increment (>0.0)\n"
                ":type arg9: float\n"
                ":param arg10: Plot title\n"
                ":type arg10: str\n"
                ":param arg11: Plot subtitle\n"
                ":type arg11: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					All symbol attributes, except for the size, are assumed\n"
                "   					to be defined (or defaults are used).\n"
                "   					Spacing is based on the maximum of the largest plotted symbol\n"
                "   					and the font size.\n"
                "   				\n\n"
               ).staticmethod("prop_symb_legend");
    pyClass.def("re_gen_areas", &GXMVU_wrap_re_gen_areas,
                "re_gen_areas((GXMVIEW)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Re-Generate from a line group and existing area group\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Group with lines\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The area group must exist and will be modified to match the current\n"
                "   					line group.\n"
                "   \n"
                "   					All non-polygon entities in the current area group will remain in the\n"
                "   					new area group.  All existing polygon groups will be used to determine\n"
                "   					the most likely attributes for the new polygon groups.\n"
                "   \n"
                "   					There must be existing polygon groups in the area group.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVU.gen_areas`\\ \n\n"
               ).staticmethod("re_gen_areas");
    pyClass.def("symb_off", &GXMVU_wrap_symb_off,
                "symb_off((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draws symbols with an offset and against a flag channel\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X, must be type of REAL\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y, must be type of REAL\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Flag VV, must be type of INT\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: X Offset\n"
                ":type arg5: float\n"
                ":param arg6: Y Offset\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Symbols are not plotted for positions where the flag VV\n"
                "   					value is 0 or iDUMMY.\n"
                "   				\n\n"
               ).staticmethod("symb_off");
    pyClass.def("text_box", &GXMVU_wrap_text_box,
                "text_box((GXMVIEW)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (str)arg6, (float)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a wrapped text box\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Min X\n"
                ":type arg2: float\n"
                ":param arg3: Min Y\n"
                ":type arg3: float\n"
                ":param arg4: Max X\n"
                ":type arg4: float\n"
                ":param arg5: Max Y\n"
                ":type arg5: float\n"
                ":param arg6: text\n"
                ":type arg6: str\n"
                ":param arg7: line spacing (1.2 good)\n"
                ":type arg7: float\n"
                ":param arg8: \\ :ref:`MVU_TEXTBOX`\\ \n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("text_box");
    pyClass.def("tick", &GXMVU_wrap_tick,
                "tick((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw line ticks on a map.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y locations\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Station\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Tick size\n"
                ":type arg5: float\n"
                ":param arg6: Tick modulus on station vv\n"
                ":type arg6: float\n"
                ":param arg7: Major tick size\n"
                ":type arg7: float\n"
                ":param arg8: Major tick modulus on station vv\n"
                ":type arg8: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("tick");
    pyClass.def("tick_ex", &GXMVU_wrap_tick_ex,
                "tick_ex((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXMVU.tick`\\ , with gap allowance.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y locations\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Station\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Tick size\n"
                ":type arg5: float\n"
                ":param arg6: Tick modulus on station vv\n"
                ":type arg6: float\n"
                ":param arg7: Major tick size\n"
                ":type arg7: float\n"
                ":param arg8: Major tick modulus on station vv\n"
                ":type arg8: float\n"
                ":param arg9: Maximum gap to span; set to 0 or rDUMMY to ignore all gaps.\n"
                ":type arg9: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("tick_ex");
    pyClass.def("trnd_path", &GXMVU_wrap_trnd_path,
                "trnd_path((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (int)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot min and max trend lines.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Minimum number of sections\n"
                ":type arg4: int\n"
                ":param arg5: Minimum length of sections\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Trend lines positions consist of X and Y VVs\n"
                "   					interspersed with dummies, which separate the\n"
                "   					individual trend sections.\n"
                "   					Set the minimum number of sections to > 0 to\n"
                "   					plot only the longer trend lines.\n"
                "   					(The number of sections in one trend section is\n"
                "   					equal to the number of points between dummies minus one.)\n"
                "   					Set the minimum distance to > 0 to\n"
                "   					plot only the longer trend lines.\n"
                "   				\n\n"
               ).staticmethod("trnd_path");

    scope().attr("EMLAY_V_COPLANAR") = (int32_t)0;
    scope().attr("EMLAY_H_COPLANAR") = (int32_t)1;
    scope().attr("EMLAY_V_COAXIAL") = (int32_t)2;
    scope().attr("ARROW_ALIGNMENT_HORIZONTAL") = (int32_t)0;
    scope().attr("ARROW_ALIGNMENT_VERTICAL") = (int32_t)1;
    scope().attr("BARCHART_LABEL_NO") = (int32_t)0;
    scope().attr("BARCHART_LABEL_BELOWX") = (int32_t)1;
    scope().attr("BARCHART_LABEL_ABOVEX") = (int32_t)2;
    scope().attr("BARCHART_LABEL_PEND") = (int32_t)3;
    scope().attr("BARCHART_LABEL_NEND") = (int32_t)4;
    scope().attr("BARCHART_LABEL_ALTERNAT1") = (int32_t)5;
    scope().attr("BARCHART_LABEL_ALTERNAT2") = (int32_t)6;
    scope().attr("COLORBAR_LABEL_HORIZONTAL") = (int32_t)0;
    scope().attr("COLORBAR_LABEL_VERTICAL") = (int32_t)1;
    scope().attr("COLORBAR_STYLE_NONE") = (int32_t)0;
    scope().attr("COLORBAR_STYLE_MAXMIN") = (int32_t)1;
    scope().attr("MVU_ORIENTATION_VERTICAL") = (int32_t)0;
    scope().attr("MVU_ORIENTATION_HORIZONTAL") = (int32_t)1;
    scope().attr("MVU_DIVISION_STYLE_NONE") = (int32_t)0;
    scope().attr("MVU_DIVISION_STYLE_LINES") = (int32_t)1;
    scope().attr("MVU_DIVISION_STYLE_TICS") = (int32_t)2;
    scope().attr("MVU_ARROW_SOLID") = (int32_t)1;
    scope().attr("MVU_ARROW_FIXED") = (int32_t)2;
    scope().attr("MVU_FLIGHT_COMPASS_NONE") = (int32_t)-1;
    scope().attr("MVU_FLIGHT_COMPASS_EAST") = (int32_t)0;
    scope().attr("MVU_FLIGHT_COMPASS_NORTH") = (int32_t)1;
    scope().attr("MVU_FLIGHT_COMPASS_WEST") = (int32_t)2;
    scope().attr("MVU_FLIGHT_COMPASS_SOUTH") = (int32_t)3;
    scope().attr("MVU_FLIGHT_DUMMIES_NOTINCLUDED") = (int32_t)0;
    scope().attr("MVU_FLIGHT_DUMMIES_INCLUDED") = (int32_t)1;
    scope().attr("MVU_FLIGHT_LOCATE_NONE") = (int32_t)0;
    scope().attr("MVU_FLIGHT_LOCATE_END") = (int32_t)1;
    scope().attr("MVU_FLIGHT_LOCATE_ABOVE") = (int32_t)2;
    scope().attr("MVU_FLIGHT_LOCATE_BELOW") = (int32_t)3;
    scope().attr("MVU_FLIGHT_DIRECTION") = (int32_t)8;
    scope().attr("MVU_VOX_SURFACE_METHOD_MARCHING_CUBES") = (int32_t)0;
    scope().attr("MVU_VOX_SURFACE_OPTION_OPEN") = (int32_t)0;
    scope().attr("MVU_VOX_SURFACE_OPTION_CLOSED") = (int32_t)1;
    scope().attr("MVU_TEXTBOX_LEFT") = (int32_t)0;
    scope().attr("MVU_TEXTBOX_CENTER") = (int32_t)1;
    scope().attr("MVU_TEXTBOX_RIGHT") = (int32_t)2;
    scope().attr("MVU_VPOINT_SHARP") = (int32_t)0;
    scope().attr("MVU_VPOINT_MEDIUM") = (int32_t)1;
    scope().attr("MVU_VPOINT_BLUNT") = (int32_t)2;
    scope().attr("MVU_VPOS_HEAD") = (int32_t)0;
    scope().attr("MVU_VPOS_MIDDLE") = (int32_t)1;
    scope().attr("MVU_VPOS_TAIL") = (int32_t)2;
    scope().attr("MVU_VSIZE_NOHEAD") = (int32_t)0;
    scope().attr("MVU_VSIZE_SMALLHEAD") = (int32_t)1;
    scope().attr("MVU_VSIZE_MEDIUMHEAD") = (int32_t)2;
    scope().attr("MVU_VSIZE_LARGEHEAD") = (int32_t)3;
    scope().attr("MVU_VSIZE_NOTAIL") = (int32_t)4;
    scope().attr("MVU_VSTYLE_LINES") = (int32_t)0;
    scope().attr("MVU_VSTYLE_BARB") = (int32_t)1;
    scope().attr("MVU_VSTYLE_TRIANGLE") = (int32_t)2;

}
