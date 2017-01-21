#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXCHIMERA_wrap_bar_plot(GXMVIEWPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7, int32_t arg8, int32_t arg9, double arg10, double arg11)
{
    GXCHIMERA::bar_plot(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXCHIMERA_wrap_categorize_by_value(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    GXCHIMERA::categorize_by_value(arg1, arg2, arg3);
}
inline void GXCHIMERA_wrap_categorize_by_value_det_limit(GXVVPtr arg1, GXVVPtr arg2, double arg3, GXVVPtr arg4)
{
    GXCHIMERA::categorize_by_value_det_limit(arg1, arg2, arg3, arg4);
}
inline void GXCHIMERA_wrap_clip_to_detect_limit(GXVVPtr arg1, double arg2, int32_t arg3)
{
    GXCHIMERA::clip_to_detect_limit(arg1, arg2, arg3);
}
inline void GXCHIMERA_wrap_draw_circle_offset_markers(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, double arg6)
{
    GXCHIMERA::draw_circle_offset_markers(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXCHIMERA_wrap_draw_rectangle_offset_markers(GXMVIEWPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, double arg6, double arg7, double arg8)
{
    GXCHIMERA::draw_rectangle_offset_markers(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXCHIMERA_wrap_duplicate_chem(GXMVIEWPtr arg1, GXVVPtr arg2, int32_t arg3, double arg4, int32_t arg5, GXVVPtr arg6, const gx_string_type& arg7, const gx_string_type& arg8, double arg9, double arg10, double arg11, double arg12)
{
    GXCHIMERA::duplicate_chem(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12);
}
inline void GXCHIMERA_wrap_duplicate_chem_view(GXMAPPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXIPJPtr arg4, GXVVPtr arg5, int32_t arg6, double arg7, int32_t arg8, GXVVPtr arg9, const gx_string_type& arg10, const gx_string_type& arg11, GXVVPtr arg12, GXVVPtr arg13, GXVVPtr arg14, GXDBPtr arg15, float_ref& arg16, float_ref& arg17)
{
    GXCHIMERA::duplicate_chem_view(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17);
}
inline void GXCHIMERA_wrap_get_expression_data_vv(GXDBPtr arg1, int32_t arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, GXVVPtr arg6)
{
    GXCHIMERA::get_expression_data_vv(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXCHIMERA_wrap_get_lithogeochem_data(GXDBPtr arg1, GXLSTPtr arg2, int32_t arg3, GXVVPtr arg4, int32_t arg5, GXVVPtr arg6, int32_t arg7, GXVVPtr arg8, GXVVPtr arg9, GXVVPtr arg10, GXVVPtr arg11, GXVVPtr arg12, GXVVPtr arg13, GXVVPtr arg14)
{
    GXCHIMERA::get_lithogeochem_data(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14);
}
inline void GXCHIMERA_wrap_get_transform(GXDBPtr arg1, const gx_string_type& arg2, int32_t arg3, int_ref& arg4, float_ref& arg5)
{
    GXCHIMERA::get_transform(arg1, arg2, arg3, arg4, arg5);
}
inline bool GXCHIMERA_wrap_is_acquire_chan(const gx_string_type& arg1, str_ref& arg2, str_ref& arg3, float_ref& arg4, bool_ref& arg5)
{
    bool ret = GXCHIMERA::is_acquire_chan(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline bool GXCHIMERA_wrap_is_element(const gx_string_type& arg1, int32_t arg2)
{
    bool ret = GXCHIMERA::is_element(arg1, (STR_CASE)arg2);
    return ret;
}
inline void GXCHIMERA_wrap_launch_histogram(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXCHIMERA::launch_histogram(arg1, arg2);
}
inline void GXCHIMERA_wrap_launch_probability(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXCHIMERA::launch_probability(arg1, arg2);
}
inline void GXCHIMERA_wrap_launch_scatter(const gx_string_type& arg1)
{
    GXCHIMERA::launch_scatter(arg1);
}
inline void GXCHIMERA_wrap_launch_triplot(const gx_string_type& arg1)
{
    GXCHIMERA::launch_triplot(arg1);
}
inline void GXCHIMERA_wrap_mask_chan_lst(GXDBPtr arg1, GXLSTPtr arg2)
{
    GXCHIMERA::mask_chan_lst(arg1, arg2);
}
inline void GXCHIMERA_wrap_ordered_channel_lst(GXDBPtr arg1, GXLSTPtr arg2)
{
    GXCHIMERA::ordered_channel_lst(arg1, arg2);
}
inline void GXCHIMERA_wrap_pie_plot(GXMVIEWPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7, int32_t arg8, int32_t arg9, double arg10, double arg11)
{
    GXCHIMERA::pie_plot(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXCHIMERA_wrap_pie_plot2(GXMVIEWPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7, int32_t arg8, int32_t arg9, double arg10, double arg11, double arg12)
{
    GXCHIMERA::pie_plot2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12);
}
inline void GXCHIMERA_wrap_plot_string_classified_symbols_legend_from_class_file(GXMVIEWPtr arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, const gx_string_type& arg6, GXVVPtr arg7)
{
    GXCHIMERA::plot_string_classified_symbols_legend_from_class_file(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline double GXCHIMERA_wrap_atomic_weight(const gx_string_type& arg1)
{
    double ret = GXCHIMERA::atomic_weight(arg1);
    return ret;
}
inline void GXCHIMERA_wrap_rose_plot(GXMVIEWPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7, int32_t arg8, int32_t arg9, double arg10)
{
    GXCHIMERA::rose_plot(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXCHIMERA_wrap_rose_plot2(GXMVIEWPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7, int32_t arg8, int32_t arg9, double arg10, double arg11)
{
    GXCHIMERA::rose_plot2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXCHIMERA_wrap_scatter2(GXMVIEWPtr arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, double arg6, GXVVPtr arg7, GXVVPtr arg8, const gx_string_type& arg9, GXVVPtr arg10, GXVVPtr arg11, GXVVPtr arg12, int32_t arg13, const gx_string_type& arg14, const gx_string_type& arg15, const gx_string_type& arg16, const gx_string_type& arg17, double arg18, double arg19, double arg20, double arg21, double arg22, double arg23, double arg24, double arg25, int32_t arg26, int32_t arg27, int32_t arg28, int32_t arg29, int32_t arg30, int32_t arg31)
{
    GXCHIMERA::scatter2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24, arg25, arg26, arg27, arg28, arg29, arg30, arg31);
}
inline void GXCHIMERA_wrap_fixed_symbol_scatter_plot(GXMVIEWPtr arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, double arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, int32_t arg10, const gx_string_type& arg11, int32_t arg12, double arg13, double arg14, int32_t arg15, int32_t arg16, GXDBPtr arg17, GXVVPtr arg18, GXVVPtr arg19, int32_t arg20, const gx_string_type& arg21, const gx_string_type& arg22, const gx_string_type& arg23, const gx_string_type& arg24, double arg25, double arg26, double arg27, double arg28, int32_t arg29, int32_t arg30, const gx_string_type& arg31)
{
    GXCHIMERA::fixed_symbol_scatter_plot(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24, arg25, arg26, arg27, arg28, arg29, arg30, arg31);
}
inline void GXCHIMERA_wrap_zone_coloured_scatter_plot(GXMVIEWPtr arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, double arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, int32_t arg10, GXVVPtr arg11, const gx_string_type& arg12, const gx_string_type& arg13, int32_t arg14, double arg15, double arg16, int32_t arg17, int32_t arg18, int32_t arg19, GXDBPtr arg20, GXVVPtr arg21, GXVVPtr arg22, int32_t arg23, const gx_string_type& arg24, const gx_string_type& arg25, const gx_string_type& arg26, const gx_string_type& arg27, double arg28, double arg29, double arg30, double arg31, int32_t arg32, int32_t arg33, const gx_string_type& arg34)
{
    GXCHIMERA::zone_coloured_scatter_plot(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24, arg25, arg26, arg27, arg28, arg29, arg30, arg31, arg32, arg33, arg34);
}
inline void GXCHIMERA_wrap_string_classified_scatter_plot(GXMVIEWPtr arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, double arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, int32_t arg10, GXVVPtr arg11, const gx_string_type& arg12, double arg13, GXDBPtr arg14, GXVVPtr arg15, GXVVPtr arg16, int32_t arg17, const gx_string_type& arg18, const gx_string_type& arg19, const gx_string_type& arg20, const gx_string_type& arg21, double arg22, double arg23, double arg24, double arg25, int32_t arg26, int32_t arg27, const gx_string_type& arg28)
{
    GXCHIMERA::string_classified_scatter_plot(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24, arg25, arg26, arg27, arg28);
}
inline void GXCHIMERA_wrap_set_lithogeochem_data(GXDBPtr arg1, GXLSTPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, GXVVPtr arg10)
{
    GXCHIMERA::set_lithogeochem_data(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXCHIMERA_wrap_stacked_bar_plot(GXMVIEWPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7, int32_t arg8, int32_t arg9, double arg10, double arg11)
{
    GXCHIMERA::stacked_bar_plot(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXCHIMERA_wrap_standard(GXMVIEWPtr arg1, GXVVPtr arg2, int32_t arg3, double arg4, double arg5, double arg6, const gx_string_type& arg7, const gx_string_type& arg8, double arg9, double arg10, double arg11, double arg12)
{
    GXCHIMERA::standard(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12);
}
inline void GXCHIMERA_wrap_standard_view(GXMAPPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXIPJPtr arg4, GXVVPtr arg5, int32_t arg6, double arg7, double arg8, double arg9, const gx_string_type& arg10, const gx_string_type& arg11, double arg12, GXVVPtr arg13, GXVVPtr arg14, GXVVPtr arg15, GXDBPtr arg16, float_ref& arg17, float_ref& arg18)
{
    GXCHIMERA::standard_view(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18);
}
inline void GXCHIMERA_wrap_tri_plot2(GXMVIEWPtr arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, double arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, GXVVPtr arg10, const gx_string_type& arg11, GXVVPtr arg12, GXVVPtr arg13, GXVVPtr arg14, const gx_string_type& arg15, const gx_string_type& arg16, const gx_string_type& arg17, double arg18, double arg19, double arg20, double arg21, double arg22, double arg23, int32_t arg24, int32_t arg25, int32_t arg26, int32_t arg27, int32_t arg28, int32_t arg29, int32_t arg30, double arg31, double arg32)
{
    GXCHIMERA::tri_plot2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24, arg25, arg26, arg27, arg28, arg29, arg30, arg31, arg32);
}
inline void GXCHIMERA_wrap_fixed_symbol_tri_plot(GXMVIEWPtr arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, GXVVPtr arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, int32_t arg10, const gx_string_type& arg11, int32_t arg12, double arg13, double arg14, int32_t arg15, int32_t arg16, GXDBPtr arg17, GXVVPtr arg18, GXVVPtr arg19, const gx_string_type& arg20, const gx_string_type& arg21, const gx_string_type& arg22, int32_t arg23, double arg24, double arg25, const gx_string_type& arg26)
{
    GXCHIMERA::fixed_symbol_tri_plot(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24, arg25, arg26);
}
inline void GXCHIMERA_wrap_zone_coloured_tri_plot(GXMVIEWPtr arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, GXVVPtr arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, int32_t arg10, GXVVPtr arg11, const gx_string_type& arg12, const gx_string_type& arg13, int32_t arg14, double arg15, double arg16, int32_t arg17, int32_t arg18, int32_t arg19, GXDBPtr arg20, GXVVPtr arg21, GXVVPtr arg22, const gx_string_type& arg23, const gx_string_type& arg24, const gx_string_type& arg25, int32_t arg26, double arg27, double arg28, const gx_string_type& arg29)
{
    GXCHIMERA::zone_coloured_tri_plot(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23, arg24, arg25, arg26, arg27, arg28, arg29);
}
inline void GXCHIMERA_wrap_string_classified_tri_plot(GXMVIEWPtr arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, GXVVPtr arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, int32_t arg10, GXVVPtr arg11, const gx_string_type& arg12, double arg13, GXDBPtr arg14, GXVVPtr arg15, GXVVPtr arg16, const gx_string_type& arg17, const gx_string_type& arg18, const gx_string_type& arg19, int32_t arg20, double arg21, double arg22, const gx_string_type& arg23)
{
    GXCHIMERA::string_classified_tri_plot(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22, arg23);
}

void gxPythonImportGXCHIMERA()
{

    class_<GXCHIMERA, boost::noncopyable> pyClass("GXCHIMERA",
            "\n.. parsed-literal::\n\n"
            "   CHIMERA GX function library.\n\n"
            , no_init);


    pyClass.def("bar_plot", &GXCHIMERA_wrap_bar_plot,
                "bar_plot((GXMVIEW)arg1, (str)arg2, (str)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7, (int)arg8, (int)arg9, (float)arg10, (float)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot a Bar plot of up to 8 channels.\n\n"

                ":param arg1: View object to plot to\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Data group name\n"
                ":type arg2: str\n"
                ":param arg3: Offset group name\n"
                ":type arg3: str\n"
                ":param arg4: X locations\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Y locations\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Data handles, stored as INT values\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Colours\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Colour for edges\n"
                ":type arg8: int\n"
                ":param arg9: Offset symbols (0: No, 1: Yes)\n"
                ":type arg9: int\n"
                ":param arg10: Offset symbol size\n"
                ":type arg10: float\n"
                ":param arg11: Single bar width in data units.\n"
                ":type arg11: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The number of channels is taken from the Data handles VV.\n"
                "   Plots a bar plot with the center of the \"X\" axis at the symbol location.\n"
                "   See the note on offset symbols in \\ :func:`geosoft.gxapi.GXCHIMERA.rose_plot`\\ \n\n"
               ).staticmethod("bar_plot");
    pyClass.def("categorize_by_value", &GXCHIMERA_wrap_categorize_by_value,
                "categorize_by_value((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Transform values to the index of input data ranges.\n\n"

                ":param arg1: Input range minima\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Input data VV.      (REAL)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Output (altered) VV.(REAL)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   A list of minima (e.g.  M1, M2, M3, M4, M5) is input.\n"
                "   A list of values V is input and transformed to outputs N in the following manner:\n"
                "   \n"
                "   if(V) >= M5) N = 5\n"
                "   else if(V) >= M4) N = 4\n"
                "   ...\n"
                "   ...\n"
                "   else if(V) >= M1) N = 1\n"
                "   else N = 0\n\n"
               ).staticmethod("categorize_by_value");
    pyClass.def("categorize_by_value_det_limit", &GXCHIMERA_wrap_categorize_by_value_det_limit,
                "categorize_by_value_det_limit((GXVV)arg1, (GXVV)arg2, (float)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Transform values to the index of input data ranges, with detection limit.\n\n"

                ":param arg1: Input range minima\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Input data VV.      (REAL)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Detection limit (can be rDUMMY)\n"
                ":type arg3: float\n"
                ":param arg4: Output (altered) VV.(REAL)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXCHIMERA.categorize_by_value`\\ , but if the\n"
                "   input value is less than the detection limit,\n"
                "   the output value is set to zero.\n\n"
               ).staticmethod("categorize_by_value_det_limit");
    pyClass.def("clip_to_detect_limit", &GXCHIMERA_wrap_clip_to_detect_limit,
                "clip_to_detect_limit((GXVV)arg1, (float)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply detection limit clipping of data.\n\n"

                ":param arg1: Input data vv (altered).\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Detection limit\n"
                ":type arg2: float\n"
                ":param arg3: Auto-convert negatives?\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Flow:\n"
                "   \n"
                "   1. If auto-converting negatives, then all negative values\n"
                "       are replaced by -0.5\\ `*`\\ value, and detection limit is ignored.\n"
                "   \n"
                "   2. If not auto-converting negatives, and the detection limit is not\n"
                "      rDUMMY, then values less than the detection limit are converted to\n"
                "      one-half the detection limit.\n\n"
               ).staticmethod("clip_to_detect_limit");
    pyClass.def("draw_circle_offset_markers", &GXCHIMERA_wrap_draw_circle_offset_markers,
                "draw_circle_offset_markers((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plots location marker and joining line for circle offset symbols\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Original (marker) X location\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Original (marker) Y location\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Offset (new) X location\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Offset (new) Y location\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Marker symbol radius\n"
                ":type arg6: float\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Draws black filled circle (symbols.gfn #7) and a joining line.\n\n"
               ).staticmethod("draw_circle_offset_markers");
    pyClass.def("draw_rectangle_offset_markers", &GXCHIMERA_wrap_draw_rectangle_offset_markers,
                "draw_rectangle_offset_markers((GXMVIEW)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (float)arg6, (float)arg7, (float)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plots location marker and joining line for rectangle offset symbols\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Original (marker) X location\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Original (marker) Y location\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Offset (new) X location\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Offset (new) Y location\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Offset symbol width\n"
                ":type arg6: float\n"
                ":param arg7: Offset symbol height\n"
                ":type arg7: float\n"
                ":param arg8: Marker symbol radius\n"
                ":type arg8: float\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Draws black filled circle (symbols.gfn #7) and a joining line.\n\n"
               ).staticmethod("draw_rectangle_offset_markers");
    pyClass.def("duplicate_chem", &GXCHIMERA_wrap_duplicate_chem,
                "duplicate_chem((GXMVIEW)arg1, (GXVV)arg2, (int)arg3, (float)arg4, (int)arg5, (GXVV)arg6, (str)arg7, (str)arg8, (float)arg9, (float)arg10, (float)arg11, (float)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot an ASSAY Duplicate result in a graph window.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Duplicate data\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: log-transform: 0 - linear, 1 - log\n"
                ":type arg3: int\n"
                ":param arg4: Detect Limit\n"
                ":type arg4: float\n"
                ":param arg5: number of old samples in the VV\n"
                ":type arg5: int\n"
                ":param arg6: tolerances (1-5 values)\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Title\n"
                ":type arg7: str\n"
                ":param arg8: Unit\n"
                ":type arg8: str\n"
                ":param arg9: X location (bottom left corner of graph)\n"
                ":type arg9: float\n"
                ":param arg10: Y location\n"
                ":type arg10: float\n"
                ":param arg11: graph width\n"
                ":type arg11: float\n"
                ":param arg12: graph height\n"
                ":type arg12: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"
               ).staticmethod("duplicate_chem");
    pyClass.def("duplicate_chem_view", &GXCHIMERA_wrap_duplicate_chem_view,
                "duplicate_chem_view((GXMAP)arg1, (str)arg2, (str)arg3, (GXIPJ)arg4, (GXVV)arg5, (int)arg6, (float)arg7, (int)arg8, (GXVV)arg9, (str)arg10, (str)arg11, (GXVV)arg12, (GXVV)arg13, (GXVV)arg14, (GXDB)arg15, (float_ref)arg16, (float_ref)arg17) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot an ASSAY Duplicate result in a new view.\n\n"

                ":param arg1: Map\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: New view name\n"
                ":type arg2: str\n"
                ":param arg3: New group name\n"
                ":type arg3: str\n"
                ":param arg4: IPJ\n"
                ":type arg4: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg5: Duplicate data\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: log-transform: 0 - linear, 1 - log\n"
                ":type arg6: int\n"
                ":param arg7: Detect Limit\n"
                ":type arg7: float\n"
                ":param arg8: number of old samples in the VV\n"
                ":type arg8: int\n"
                ":param arg9: tolerances (1-5 values)\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Title\n"
                ":type arg10: str\n"
                ":param arg11: Unit\n"
                ":type arg11: str\n"
                ":param arg12: VV X\n"
                ":type arg12: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg13: VV Line\n"
                ":type arg13: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg14: VV Fid\n"
                ":type arg14: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg15: Database\n"
                ":type arg15: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg16: Returned MinY\n"
                ":type arg16: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg17: Returned MaxY\n"
                ":type arg17: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"
               ).staticmethod("duplicate_chem_view");
    pyClass.def("get_expression_data_vv", &GXCHIMERA_wrap_get_expression_data_vv,
                "get_expression_data_vv((GXDB)arg1, (int)arg2, (str)arg3, (str)arg4, (str)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get data from a line using a channel expression.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Line to read\n"
                ":type arg2: int\n"
                ":param arg3: geochem stage (just \"raw data stage\" for now).\n"
                ":type arg3: str\n"
                ":param arg4: channel expression\n"
                ":type arg4: str\n"
                ":param arg5: INI file name with required units (e.g. PARAMETER.CU=\"ppm\") (optional)\n"
                ":type arg5: str\n"
                ":param arg6: Returned data\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Input a channel expression. Units for individual channels\n"
                "   are stored in the input INI. Returns a VV for the given line\n"
                "   with the calculated expression values.\n\n"
               ).staticmethod("get_expression_data_vv");
    pyClass.def("get_lithogeochem_data", &GXCHIMERA_wrap_get_lithogeochem_data,
                "get_lithogeochem_data((GXDB)arg1, (GXLST)arg2, (int)arg3, (GXVV)arg4, (int)arg5, (GXVV)arg6, (int)arg7, (GXVV)arg8, (GXVV)arg9, (GXVV)arg10, (GXVV)arg11, (GXVV)arg12, (GXVV)arg13, (GXVV)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get all rows of non-dummy data in a database.\n\n"

                ":param arg1: [i] database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: [i] channels of data to get\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: [i] mask channel (can be NULLSYMB)\n"
                ":type arg3: int\n"
                ":param arg4: [i] transforms to apply\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: [i] remove dummy rows?\n"
                ":type arg5: int\n"
                ":param arg6: [i] dummy row if this channel value is dummy (0:No, 1:Yes)? Effective only if \"remove dummy rows\" value is TRUE\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: [i] warn if rows removed because of dummy data items?\n"
                ":type arg7: int\n"
                ":param arg8: [o] (INT) returned data - one VV handle per channel\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: [o] line symbols selected\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: [o] number of original data items in each line\n"
                ":type arg10: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg11: [o] number of non-dummy rows\n"
                ":type arg11: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg12: [o] indices into original data\n"
                ":type arg12: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg13: [o] Fid Starts (REAL)\n"
                ":type arg13: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg14: [o] Fid Increments (REAL)\n"
                ":type arg14: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function is a quick way to get all rows\n"
                "   of data, guaranteeing no dummy items.\n"
                "   Book-keeping VVs returned let you easily\n"
                "   write back results to new channels in the\n"
                "   correct locations.\n"
                "   Set the \"Dummy Row\" VV to 1 if you wish to\n"
                "   remove any row where a value for the corresponding\n"
                "   channel is a dummy.\n"
                "   \n"
                "   Transforms to apply:\n"
                "   \n"
                "   -1 - Channel default (will be either raw or log)\n"
                "   0 - Raw Transform\n"
                "   1 - Log transform: base e with log min = CHIMERA_LOG_MIN\n"
                "   2 - Lambda transform\n\n"
               ).staticmethod("get_lithogeochem_data");
    pyClass.def("get_transform", &GXCHIMERA_wrap_get_transform,
                "get_transform((GXDB)arg1, (str)arg2, (int)arg3, (int_ref)arg4, (float_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get channel transform options and lambda values.\n\n"

                ":param arg1: DB handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Channel name\n"
                ":type arg2: str\n"
                ":param arg3: Transform option: -1, 0, 1 or 2\n"
                ":type arg3: int\n"
                ":param arg4: returned transform used\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: returned lambda value for option==2\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the lambda transform is requested, the channel\n"
                "   must have the lambda value defined.\n"
                "   \n"
                "   Input Transform options\n"
                "   \n"
                "   -1 - Channel default (will be either raw or log)\n"
                "   0 - Raw Transform\n"
                "   1 - Log transform: base e with log min = CHIMERA_LOG_MIN\n"
                "   2 - Lambda transform\n\n"
               ).staticmethod("get_transform");
    pyClass.def("is_acquire_chan", &GXCHIMERA_wrap_is_acquire_chan,
                "is_acquire_chan((str)arg1, (str_ref)arg2, (str_ref)arg3, (float_ref)arg4, (bool_ref)arg5) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this channel in acQuire format (e.g. \"Ag_ppm_4AWR\")\n\n"

                ":param arg1: string to test\n"
                ":type arg1: str\n"
                ":param arg2: returned channel name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: returned units\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: units factor (e.g. ppm = 1.e-6)\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: bool is this an oxide?\n"
                ":type arg5: :class:`geosoft.gxapi.bool_ref`\n"
                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Expressions can take acQuire-type named channels\n"
                "   if the exact element/oxide is not found. This function\n"
                "   extracts the channel name, and units from an acQuire-formatted\n"
                "   channel name.\n\n"
               ).staticmethod("is_acquire_chan");
    pyClass.def("is_element", &GXCHIMERA_wrap_is_element,
                "is_element((str)arg1, (int)arg2) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Tests a string to see if it is an element symbol\n\n"

                ":param arg1: string to test\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`STR_CASE`\\ \n"
                ":type arg2: int\n"
                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Suggested use - testing to see if a channel name is an\n"
                "   element so that the \"ASSAY\" class can be set.\n\n"
               ).staticmethod("is_element");
    pyClass.def("launch_histogram", &GXCHIMERA_wrap_launch_histogram,
                "launch_histogram((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch histogram tool on a database.\n\n"

                ":param arg1: Database name\n"
                ":type arg1: str\n"
                ":param arg2: First chan name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The database should be a currently open database.\n"
                "   This function supercedes \\ :func:`geosoft.gxapi.GXEDB.launch_histogram`\\ , (which now\n"
                "   just gets the name of the EDB and calls this function).\n\n"
               ).staticmethod("launch_histogram");
    pyClass.def("launch_probability", &GXCHIMERA_wrap_launch_probability,
                "launch_probability((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch probability tool on a database.\n\n"

                ":param arg1: Database name\n"
                ":type arg1: str\n"
                ":param arg2: First chan name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The database should be a currently open database.\n\n"
               ).staticmethod("launch_probability");
    pyClass.def("launch_scatter", &GXCHIMERA_wrap_launch_scatter,
                "launch_scatter((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch scatter tool on a database.\n\n"

                ":param arg1: Database name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The scatter tool uses the following INI parameters\n"
                "   \n"
                "   SCATTER.STM       name of the scatter template,\"none\" for none\n"
                "   SCATTER.STM_NAME  name of last template section, \"\" for none.\n"
                "   SCATTER.X         name of channel to display in X\n"
                "   SCATTER.Y         name of channel to display in Y\n"
                "   SCATTER.MASK      name of channel to use for mask\n"
                "   \n"
                "   The database should be a currently open database.\n"
                "   This function supercedes \\ :func:`geosoft.gxapi.GXEDB.launch_scatter`\\ , (which now\n"
                "   just gets the name of the EDB and calls this function).\n\n"
               ).staticmethod("launch_scatter");
    pyClass.def("launch_triplot", &GXCHIMERA_wrap_launch_triplot,
                "launch_triplot((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch Triplot tool on a database.\n\n"

                ":param arg1: Database name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Triplot tool uses the following INI parameters\n"
                "   \n"
                "            TRIPLOT.TTM       name of the triplot template,\"none\" for none\n"
                "            TRIPLOT.TTM_NAME  name of last template section, \"\" for none.\n"
                "            TRIPLOT.X         name of channel to display in X\n"
                "            TRIPLOT.Y         name of channel to display in Y\n"
                "            TRIPLOT.Z         name of channel to display in Z\n"
                "            TRIPLOT.MASK      name of channel to use for mask\n"
                "   \n"
                "   The database should be a currently open database.\n\n"
               ).staticmethod("launch_triplot");
    pyClass.def("mask_chan_lst", &GXCHIMERA_wrap_mask_chan_lst,
                "mask_chan_lst((GXDB)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LST with mask channels.\n\n"

                ":param arg1: hDB - Database Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: LST object to populate\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Loads a LST with all channels with CLASS \"MASK\", as well\n"
                "   as all channels containing the string \"MASK\", as long\n"
                "   as the CLASS for these channels is not set to something\n"
                "   other than \"\" or \"MASK\".\n"
                "   \n"
                "   This function has been duplicated by \\ :func:`geosoft.gxapi.GXDB.mask_chan_lst`\\ , which\n"
                "   is safe to use in applications which do not have CHIMERA loaded.\n\n"
               ).staticmethod("mask_chan_lst");
    pyClass.def("ordered_channel_lst", &GXCHIMERA_wrap_ordered_channel_lst,
                "ordered_channel_lst((GXDB)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill a list with the channels in the preferred order.\n\n"

                ":param arg1: hDB - Database Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: LST object to populate [recommended 2\\ `*`\\ STR_DB_SYMBOL]\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Loads a LST with all channels in the preferred order:\n"
                "   \n"
                "   First:  Sample, E, N, assay channels,\n"
                "   Middle: Data from survey (other channels),\n"
                "   Last:   Duplicate, Standard, Chemmask (and other masks), weight, lab, batch\n"
                "   \n"
                "   If the input LST object has values, it is used as the channel LST,\n"
                "   otherwise, get all the database channels. (This allows you to pass in\n"
                "   the currently displayed channels and only reload those).\n\n"
               ).staticmethod("ordered_channel_lst");
    pyClass.def("pie_plot", &GXCHIMERA_wrap_pie_plot,
                "pie_plot((GXMVIEW)arg1, (str)arg2, (str)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7, (int)arg8, (int)arg9, (float)arg10, (float)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot a Pie plot of up to 8 channels.\n\n"

                ":param arg1: View object to plot to\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Data group name\n"
                ":type arg2: str\n"
                ":param arg3: Offset group name\n"
                ":type arg3: str\n"
                ":param arg4: X locations\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Y locations\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Data handles, stored as INT values\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Colours\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Colour for edges\n"
                ":type arg8: int\n"
                ":param arg9: Offset symbols (0: No, 1: Yes)\n"
                ":type arg9: int\n"
                ":param arg10: Offset symbol size\n"
                ":type arg10: float\n"
                ":param arg11: Pie plot radius in data units.\n"
                ":type arg11: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The number of channels is taken from the Data handles VV.\n"
                "   The values in each data VV are summed and the pie arc is\n"
                "   is given by the percent contribution of each consituent.\n"
                "   See the note on offset symbols in \\ :func:`geosoft.gxapi.GXCHIMERA.rose_plot`\\ \n\n"
               ).staticmethod("pie_plot");
    pyClass.def("pie_plot2", &GXCHIMERA_wrap_pie_plot2,
                "pie_plot2((GXMVIEW)arg1, (str)arg2, (str)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7, (int)arg8, (int)arg9, (float)arg10, (float)arg11, (float)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXCHIMERA.pie_plot`\\ , with a starting angle.\n\n"

                ":param arg1: View object to plot to\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Data group name\n"
                ":type arg2: str\n"
                ":param arg3: Offset group name\n"
                ":type arg3: str\n"
                ":param arg4: X locations\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Y locations\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Data handles, stored as INT values\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Colours\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Colour for edges\n"
                ":type arg8: int\n"
                ":param arg9: Offset symbols (0: No, 1: Yes)\n"
                ":type arg9: int\n"
                ":param arg10: Offset symbol size\n"
                ":type arg10: float\n"
                ":param arg11: Pie plot radius in data units.\n"
                ":type arg11: float\n"
                ":param arg12: Starting angle in degrees CCW from horizontal (rDUMMY gives 0.0)\n"
                ":type arg12: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The starting angle is the location of the edge of the first pie\n"
                "   slice, counted in degrees counter-clockwise from horizontal\n"
                "   (3 o'clock). Zero degrees gives the same plot as \\ :func:`geosoft.gxapi.GXCHIMERA.pie_plot`\\ .\n\n"
               ).staticmethod("pie_plot2");
    pyClass.def("plot_string_classified_symbols_legend_from_class_file", &GXCHIMERA_wrap_plot_string_classified_symbols_legend_from_class_file,
                "plot_string_classified_symbols_legend_from_class_file((GXMVIEW)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (str)arg6, (GXVV)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot legend for the string classified symbols\n\n"

                ":param arg1: Map view object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: title\n"
                ":type arg2: str\n"
                ":param arg3: left side X location\n"
                ":type arg3: float\n"
                ":param arg4: bottom Y bound\n"
                ":type arg4: float\n"
                ":param arg5: top Y bound\n"
                ":type arg5: float\n"
                ":param arg6: Class file name (TPAT)\n"
                ":type arg6: str\n"
                ":param arg7: Class indices  (INT VV)\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Plot in a legend the classes in the class file found in the input class indices.\n"
                "   			 \n\n"
               ).staticmethod("plot_string_classified_symbols_legend_from_class_file");
    pyClass.def("atomic_weight", &GXCHIMERA_wrap_atomic_weight,
                "atomic_weight((str)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the atomic weight of a particular element.\n\n"

                ":param arg1: element name (case insensitive)\n"
                ":type arg1: str\n"
                ":returns: The atomic weight of the given element.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.4.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the input string is not an element symbol (elements in the range\n"
                "   1-92, \"H\" to \"U\"), then returns a dummy (GS_R8DM).\n\n"
               ).staticmethod("atomic_weight");
    pyClass.def("rose_plot", &GXCHIMERA_wrap_rose_plot,
                "rose_plot((GXMVIEW)arg1, (str)arg2, (str)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7, (int)arg8, (int)arg9, (float)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot a Rose plot of up to 8 channels.\n\n"

                ":param arg1: View object to plot to\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Data group name\n"
                ":type arg2: str\n"
                ":param arg3: Offset group name\n"
                ":type arg3: str\n"
                ":param arg4: X locations\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Y locations\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Data handles, stored as INT values\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Colours\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Colour for edges\n"
                ":type arg8: int\n"
                ":param arg9: Offset symbols (0: No, 1: Yes)\n"
                ":type arg9: int\n"
                ":param arg10: Offset symbol size\n"
                ":type arg10: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The number of channels is taken from the Data handles VV.\n"
                "   The values in each data VV give the radius, in view units,\n"
                "   of the sector arc to plots. Values <=0 or dummies are not\n"
                "   plotted.\n"
                "   \n"
                "   Offset symbols: When selected, the symbols plot without\n"
                "   overlap, away from the original locations. The original\n"
                "   location is marked with a small symbol and a line joins the\n"
                "   original position and the relocated symbol.\n"
                "   Care should be taken when choosing the symbol size, because\n"
                "   if the point density is too high, all the points will get\n"
                "   pushed to the outside edge and your plot will look like a\n"
                "   hedgehog (it also takes a lot longer!).\n\n"
               ).staticmethod("rose_plot");
    pyClass.def("rose_plot2", &GXCHIMERA_wrap_rose_plot2,
                "rose_plot2((GXMVIEW)arg1, (str)arg2, (str)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7, (int)arg8, (int)arg9, (float)arg10, (float)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXCHIMERA.rose_plot`\\ , with a starting angle.\n\n"

                ":param arg1: View object to plot to\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Data group name\n"
                ":type arg2: str\n"
                ":param arg3: Offset group name\n"
                ":type arg3: str\n"
                ":param arg4: X locations\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Y locations\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Data handles, stored as INT values\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Colours\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Colour for edges\n"
                ":type arg8: int\n"
                ":param arg9: Offset symbols (0: No, 1: Yes)\n"
                ":type arg9: int\n"
                ":param arg10: Offset symbol size\n"
                ":type arg10: float\n"
                ":param arg11: Starting angle in degrees CCW from horizontal (rDUMMY gives 0.0)\n"
                ":type arg11: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The starting angle is the location of the edge of the first pie\n"
                "   slice, counted in degrees counter-clockwise from horizontal\n"
                "   (3 o'clock). Zero degrees gives the same plot as \\ :func:`geosoft.gxapi.GXCHIMERA.rose_plot`\\ .\n\n"
               ).staticmethod("rose_plot2");
    pyClass.def("scatter2", &GXCHIMERA_wrap_scatter2,
                "scatter2((GXMVIEW)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (GXVV)arg7, (GXVV)arg8, (str)arg9, (GXVV)arg10, (GXVV)arg11, (GXVV)arg12, (int)arg13, (str)arg14, (str)arg15, (str)arg16, (str)arg17, (float)arg18, (float)arg19, (float)arg20, (float)arg21, (float)arg22, (float)arg23, (float)arg24, (float)arg25, (int)arg26, (int)arg27, (int)arg28, (int)arg29, (int)arg30, (int)arg31) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot the scatter plot on a map using symbol number, size and color VVs.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Title\n"
                ":type arg2: str\n"
                ":param arg3: X location (bottom left corner of box)\n"
                ":type arg3: float\n"
                ":param arg4: Y location\n"
                ":type arg4: float\n"
                ":param arg5: box width\n"
                ":type arg5: float\n"
                ":param arg6: box height\n"
                ":type arg6: float\n"
                ":param arg7: Horizontal channel\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Vertical channel\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: decorated font name, \"\" for default symbol font (normally symbols.gfn)\n"
                ":type arg9: str\n"
                ":param arg10: Symbol numbers\n"
                ":type arg10: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg11: Symbol sizes\n"
                ":type arg11: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg12: Colours  if symbol number or colour == 0, do not plot\n"
                ":type arg12: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg13: Annotation style 0 - outside, 1 - inside\n"
                ":type arg13: int\n"
                ":param arg14: Horizontal channel name\n"
                ":type arg14: str\n"
                ":param arg15: Vertical channel name\n"
                ":type arg15: str\n"
                ":param arg16: Horizontal channel units\n"
                ":type arg16: str\n"
                ":param arg17: Vertical channel units\n"
                ":type arg17: str\n"
                ":param arg18: Min. Horizontal value, rDUMMY for default\n"
                ":type arg18: float\n"
                ":param arg19: Max. Horizontal value\n"
                ":type arg19: float\n"
                ":param arg20: Min. Vertical value\n"
                ":type arg20: float\n"
                ":param arg21: Max. Vertical value\n"
                ":type arg21: float\n"
                ":param arg22: Min. Horizontal range value\n"
                ":type arg22: float\n"
                ":param arg23: Max. Horizontal range value\n"
                ":type arg23: float\n"
                ":param arg24: Min. Vertical range value\n"
                ":type arg24: float\n"
                ":param arg25: Max. Vertical range value\n"
                ":type arg25: float\n"
                ":param arg26: Use Min Horz. Range selection?\n"
                ":type arg26: int\n"
                ":param arg27: Use Max Horz. Range selection?\n"
                ":type arg27: int\n"
                ":param arg28: Use Min Vert. Range selection?\n"
                ":type arg28: int\n"
                ":param arg29: Use Max Vert. Range selection?\n"
                ":type arg29: int\n"
                ":param arg30: horizontal axis scaling: 0 - linear, 1 - log\n"
                ":type arg30: int\n"
                ":param arg31: vertical axis scaling\n"
                ":type arg31: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 The view scaling is not altered with any projection. The base view\n"
                "   				 is best as the input.\n"
                "   			 \n\n"
               ).staticmethod("scatter2");
    pyClass.def("fixed_symbol_scatter_plot", &GXCHIMERA_wrap_fixed_symbol_scatter_plot,
                "fixed_symbol_scatter_plot((GXMVIEW)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (int)arg10, (str)arg11, (int)arg12, (float)arg13, (float)arg14, (int)arg15, (int)arg16, (GXDB)arg17, (GXVV)arg18, (GXVV)arg19, (int)arg20, (str)arg21, (str)arg22, (str)arg23, (str)arg24, (float)arg25, (float)arg26, (float)arg27, (float)arg28, (int)arg29, (int)arg30, (str)arg31) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Plot a scatter plot using a single fixed symbol.\n"
                "   				 Optional data masking with masking colour.\n"
                "   				 Optioinal database linking.\n"
                "   			 \n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Title\n"
                ":type arg2: str\n"
                ":param arg3: X location (bottom left corner of box)\n"
                ":type arg3: float\n"
                ":param arg4: Y location\n"
                ":type arg4: float\n"
                ":param arg5: box width\n"
                ":type arg5: float\n"
                ":param arg6: box height\n"
                ":type arg6: float\n"
                ":param arg7: Horizontal channel data\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Vertical channel data\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Mask channel data (can be NULL)\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Mask colour; overrides symbol colour where mask data is not dummy. Set to iColor_MVIEW(\"\") to not plot.\n"
                ":type arg10: int\n"
                ":param arg11: decorated font name, \"\" for default symbol font (normally symbols.gfn)\n"
                ":type arg11: str\n"
                ":param arg12: Symbol number (>=0)\n"
                ":type arg12: int\n"
                ":param arg13: Symbol size ( >=0)\n"
                ":type arg13: float\n"
                ":param arg14: Symbol angle (-360 to 360)\n"
                ":type arg14: float\n"
                ":param arg15: Symbol colour\n"
                ":type arg15: int\n"
                ":param arg16: Symbol fill colour\n"
                ":type arg16: int\n"
                ":param arg17: Database (source of data)\n"
                ":type arg17: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg18: Line handles for data\n"
                ":type arg18: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg19: Fid values for data\n"
                ":type arg19: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg20: Annotation style 0 - outside, 1 - inside\n"
                ":type arg20: int\n"
                ":param arg21: Horizontal channel name\n"
                ":type arg21: str\n"
                ":param arg22: Vertical channel name\n"
                ":type arg22: str\n"
                ":param arg23: Horizontal channel units\n"
                ":type arg23: str\n"
                ":param arg24: Vertical channel units\n"
                ":type arg24: str\n"
                ":param arg25: Min. Horizontal value, rDUMMY for default\n"
                ":type arg25: float\n"
                ":param arg26: Max. Horizontal value\n"
                ":type arg26: float\n"
                ":param arg27: Min. Vertical value\n"
                ":type arg27: float\n"
                ":param arg28: Max. Vertical value\n"
                ":type arg28: float\n"
                ":param arg29: horizontal axis scaling: 0 - linear, 1 - log\n"
                ":type arg29: int\n"
                ":param arg30: vertical axis scaling\n"
                ":type arg30: int\n"
                ":param arg31: plot overlay (\"\" for none)\n"
                ":type arg31: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Plot a scatter plot using a single fixed symbol.\n"
                "   			 \n\n"
               ).staticmethod("fixed_symbol_scatter_plot");
    pyClass.def("zone_coloured_scatter_plot", &GXCHIMERA_wrap_zone_coloured_scatter_plot,
                "zone_coloured_scatter_plot((GXMVIEW)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (int)arg10, (GXVV)arg11, (str)arg12, (str)arg13, (int)arg14, (float)arg15, (float)arg16, (int)arg17, (int)arg18, (int)arg19, (GXDB)arg20, (GXVV)arg21, (GXVV)arg22, (int)arg23, (str)arg24, (str)arg25, (str)arg26, (str)arg27, (float)arg28, (float)arg29, (float)arg30, (float)arg31, (int)arg32, (int)arg33, (str)arg34) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Plot a scatter plot using colours based on a zone file.\n"
                "   				 Optional data masking with masking colour.\n"
                "   				 Optioinal database linking.\n"
                "   			 \n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Title\n"
                ":type arg2: str\n"
                ":param arg3: X location (bottom left corner of box)\n"
                ":type arg3: float\n"
                ":param arg4: Y location\n"
                ":type arg4: float\n"
                ":param arg5: box width\n"
                ":type arg5: float\n"
                ":param arg6: box height\n"
                ":type arg6: float\n"
                ":param arg7: Horizontal channel data\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Vertical channel data\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Mask channel data (can be NULL)\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Mask colour; overrides symbol colour where mask data is not dummy. Set to iColor_MVIEW(\"\") to not plot.\n"
                ":type arg10: int\n"
                ":param arg11: Zone channel data\n"
                ":type arg11: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg12: Zone file name\n"
                ":type arg12: str\n"
                ":param arg13: decorated font name, \"\" for default symbol font (normally symbols.gfn)\n"
                ":type arg13: str\n"
                ":param arg14: Symbol number (>=0)\n"
                ":type arg14: int\n"
                ":param arg15: Symbol size ( >=0)\n"
                ":type arg15: float\n"
                ":param arg16: Symbol angle (-360 to 360)\n"
                ":type arg16: float\n"
                ":param arg17: Symbol colour\n"
                ":type arg17: int\n"
                ":param arg18: Symbol fill colour\n"
                ":type arg18: int\n"
                ":param arg19: Fix symbol edge colour?\n"
                ":type arg19: int\n"
                ":param arg20: Database (source of data)\n"
                ":type arg20: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg21: Line handles for data\n"
                ":type arg21: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg22: Fid values for data\n"
                ":type arg22: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg23: Annotation style 0 - outside, 1 - inside\n"
                ":type arg23: int\n"
                ":param arg24: Horizontal channel name\n"
                ":type arg24: str\n"
                ":param arg25: Vertical channel name\n"
                ":type arg25: str\n"
                ":param arg26: Horizontal channel units\n"
                ":type arg26: str\n"
                ":param arg27: Vertical channel units\n"
                ":type arg27: str\n"
                ":param arg28: Min. Horizontal value, rDUMMY for default\n"
                ":type arg28: float\n"
                ":param arg29: Max. Horizontal value\n"
                ":type arg29: float\n"
                ":param arg30: Min. Vertical value\n"
                ":type arg30: float\n"
                ":param arg31: Max. Vertical value\n"
                ":type arg31: float\n"
                ":param arg32: horizontal axis scaling: 0 - linear, 1 - log\n"
                ":type arg32: int\n"
                ":param arg33: vertical axis scaling\n"
                ":type arg33: int\n"
                ":param arg34: plot overlay (\"\" for none)\n"
                ":type arg34: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Plot a scatter plot using colours based on a zone file.\n"
                "   			 \n\n"
               ).staticmethod("zone_coloured_scatter_plot");
    pyClass.def("string_classified_scatter_plot", &GXCHIMERA_wrap_string_classified_scatter_plot,
                "string_classified_scatter_plot((GXMVIEW)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (int)arg10, (GXVV)arg11, (str)arg12, (float)arg13, (GXDB)arg14, (GXVV)arg15, (GXVV)arg16, (int)arg17, (str)arg18, (str)arg19, (str)arg20, (str)arg21, (float)arg22, (float)arg23, (float)arg24, (float)arg25, (int)arg26, (int)arg27, (str)arg28) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Plot a scatter plot using symbols based on a symbol class file.\n"
                "   				 Optional data masking with masking colour.\n"
                "   				 Optioinal database linking.\n"
                "   			 \n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Title\n"
                ":type arg2: str\n"
                ":param arg3: X location (bottom left corner of box)\n"
                ":type arg3: float\n"
                ":param arg4: Y location\n"
                ":type arg4: float\n"
                ":param arg5: box width\n"
                ":type arg5: float\n"
                ":param arg6: box height\n"
                ":type arg6: float\n"
                ":param arg7: Horizontal channel data\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Vertical channel data\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Mask channel data\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Mask colour; overrides symbol colour. Set to iColor_MVIEW(\"\") to not plot.\n"
                ":type arg10: int\n"
                ":param arg11: Class channel data\n"
                ":type arg11: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg12: Class file (TPAT) name.\n"
                ":type arg12: str\n"
                ":param arg13: Symbol size override. Set to 0.0 to use class file symbol sizes.\n"
                ":type arg13: float\n"
                ":param arg14: Database (source of data)\n"
                ":type arg14: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg15: Line handles for data\n"
                ":type arg15: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg16: Fid values for data\n"
                ":type arg16: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg17: Annotation style 0 - outside, 1 - inside\n"
                ":type arg17: int\n"
                ":param arg18: Horizontal channel name\n"
                ":type arg18: str\n"
                ":param arg19: Vertical channel name\n"
                ":type arg19: str\n"
                ":param arg20: Horizontal channel units\n"
                ":type arg20: str\n"
                ":param arg21: Vertical channel units\n"
                ":type arg21: str\n"
                ":param arg22: Min. Horizontal value, rDUMMY for default\n"
                ":type arg22: float\n"
                ":param arg23: Max. Horizontal value\n"
                ":type arg23: float\n"
                ":param arg24: Min. Vertical value\n"
                ":type arg24: float\n"
                ":param arg25: Max. Vertical value\n"
                ":type arg25: float\n"
                ":param arg26: horizontal axis scaling: 0 - linear, 1 - log\n"
                ":type arg26: int\n"
                ":param arg27: vertical axis scaling\n"
                ":type arg27: int\n"
                ":param arg28: plot overlay (\"\" for none)\n"
                ":type arg28: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Plot a scatter plot using symbols based on a symbol class file.\n"
                "   			 \n\n"
               ).staticmethod("string_classified_scatter_plot");
    pyClass.def("set_lithogeochem_data", &GXCHIMERA_wrap_set_lithogeochem_data,
                "set_lithogeochem_data((GXDB)arg1, (GXLST)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (GXVV)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set data back into a database.\n\n"

                ":param arg1: [i] database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: [i] channels of data to set\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: [i] (INT) input data - one VV handle per channel\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: [i] line symbols selected\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: [i] number of original data items in each line\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: [i] number of non-dummy rows\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: [i] indices into original data\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: [i] Fid Starts (REAL)\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: [i] Fid Increments (REAL)\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: [i] init channel values to dummies first (0:No, 1:Yes)?\n"
                ":type arg10: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function would normally be called after\n"
                "   AAGetLithogeochemData_CHIMERA to write processed values\n"
                "   back into a database, in the correct lines,\n"
                "   and in the correct fiducial locations wrt the\n"
                "   other data. The book-keeping VVs would all be\n"
                "   set up in AAGetLithogeochemData_CHIMERA.\n"
                "   \n"
                "   Values NOT in the data (missing indices) will\n"
                "   be initialized to dummy if the channel is new,\n"
                "   or if the value in the last VV below is set to 1.\n"
                "   \n"
                "   New channel types will be set using the data VV type.\n"
                "   Any meta data (CLASS, display formats) should be set separately.\n\n"
               ).staticmethod("set_lithogeochem_data");
    pyClass.def("stacked_bar_plot", &GXCHIMERA_wrap_stacked_bar_plot,
                "stacked_bar_plot((GXMVIEW)arg1, (str)arg2, (str)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7, (int)arg8, (int)arg9, (float)arg10, (float)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot a Bar plot of up to 8 channels, bars stacked on each other\n\n"

                ":param arg1: View object to plot to\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Data group name\n"
                ":type arg2: str\n"
                ":param arg3: Offset group name\n"
                ":type arg3: str\n"
                ":param arg4: X locations\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Y locations\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Data handles, stored as INT values\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Colours\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Colour for edges\n"
                ":type arg8: int\n"
                ":param arg9: Offset symbols (0: No, 1: Yes)\n"
                ":type arg9: int\n"
                ":param arg10: Offset symbol size\n"
                ":type arg10: float\n"
                ":param arg11: Single bar width in data units.\n"
                ":type arg11: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The number of channels is taken from the Data handles VV.\n"
                "   Plots a bar plot with the center of the \"X\" axis at the symbol location.\n"
                "   See the note on offset symbols in \\ :func:`geosoft.gxapi.GXCHIMERA.rose_plot`\\ \n\n"
               ).staticmethod("stacked_bar_plot");
    pyClass.def("standard", &GXCHIMERA_wrap_standard,
                "standard((GXMVIEW)arg1, (GXVV)arg2, (int)arg3, (float)arg4, (float)arg5, (float)arg6, (str)arg7, (str)arg8, (float)arg9, (float)arg10, (float)arg11, (float)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot ASSAY Standard result in a graph window.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: standard data\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: number of old samples in the VV\n"
                ":type arg3: int\n"
                ":param arg4: tolerance as a function of std dev\n"
                ":type arg4: float\n"
                ":param arg5: minimum acceptable value\n"
                ":type arg5: float\n"
                ":param arg6: maximum acceptable value\n"
                ":type arg6: float\n"
                ":param arg7: Title\n"
                ":type arg7: str\n"
                ":param arg8: Unit\n"
                ":type arg8: str\n"
                ":param arg9: X location (bottom left corner of graph)\n"
                ":type arg9: float\n"
                ":param arg10: Y location\n"
                ":type arg10: float\n"
                ":param arg11: graph width\n"
                ":type arg11: float\n"
                ":param arg12: graph height\n"
                ":type arg12: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the tolerance is rDUMMY, then the minimum and maximum\n"
                "   values are used, and must be specified.\n\n"
               ).staticmethod("standard");
    pyClass.def("standard_view", &GXCHIMERA_wrap_standard_view,
                "standard_view((GXMAP)arg1, (str)arg2, (str)arg3, (GXIPJ)arg4, (GXVV)arg5, (int)arg6, (float)arg7, (float)arg8, (float)arg9, (str)arg10, (str)arg11, (float)arg12, (GXVV)arg13, (GXVV)arg14, (GXVV)arg15, (GXDB)arg16, (float_ref)arg17, (float_ref)arg18) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot ASSAY Standard result in a graph window.\n\n"

                ":param arg1: Map\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: New view name\n"
                ":type arg2: str\n"
                ":param arg3: New group name\n"
                ":type arg3: str\n"
                ":param arg4: IPJ\n"
                ":type arg4: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg5: standard data (VV Y)\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: number of old samples in the VV\n"
                ":type arg6: int\n"
                ":param arg7: tolerance as a function of std dev\n"
                ":type arg7: float\n"
                ":param arg8: minimum acceptable value\n"
                ":type arg8: float\n"
                ":param arg9: maximum acceptable value\n"
                ":type arg9: float\n"
                ":param arg10: Title\n"
                ":type arg10: str\n"
                ":param arg11: Unit\n"
                ":type arg11: str\n"
                ":param arg12: Size X\n"
                ":type arg12: float\n"
                ":param arg13: VV X\n"
                ":type arg13: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg14: VV Line\n"
                ":type arg14: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg15: VV Fid\n"
                ":type arg15: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg16: Database\n"
                ":type arg16: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg17: Returned MinY\n"
                ":type arg17: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg18: Returned MaxY\n"
                ":type arg18: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXCHIMERA.standard`\\  but plot in a new view.\n\n"
               ).staticmethod("standard_view");
    pyClass.def("tri_plot2", &GXCHIMERA_wrap_tri_plot2,
                "tri_plot2((GXMVIEW)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (GXVV)arg10, (str)arg11, (GXVV)arg12, (GXVV)arg13, (GXVV)arg14, (str)arg15, (str)arg16, (str)arg17, (float)arg18, (float)arg19, (float)arg20, (float)arg21, (float)arg22, (float)arg23, (int)arg24, (int)arg25, (int)arg26, (int)arg27, (int)arg28, (int)arg29, (int)arg30, (float)arg31, (float)arg32) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot the TriPlot on a map using symbol number, size and color VVs.\n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Title\n"
                ":type arg2: str\n"
                ":param arg3: X location (bottom left corner of box)\n"
                ":type arg3: float\n"
                ":param arg4: Y location\n"
                ":type arg4: float\n"
                ":param arg5: box width\n"
                ":type arg5: float\n"
                ":param arg6: box height\n"
                ":type arg6: float\n"
                ":param arg7: X channel\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Y channel\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Z channel\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Mask channel\n"
                ":type arg10: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg11: decorated font name, \"\" for default symbol font (normally symbols.gfn)\n"
                ":type arg11: str\n"
                ":param arg12: Symbol numbers\n"
                ":type arg12: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg13: Symbol sizes\n"
                ":type arg13: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg14: Colours  if symbol number or colour == 0, do not plot\n"
                ":type arg14: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg15: X channel name\n"
                ":type arg15: str\n"
                ":param arg16: Y channel name\n"
                ":type arg16: str\n"
                ":param arg17: Z channel name\n"
                ":type arg17: str\n"
                ":param arg18: Min. X range value\n"
                ":type arg18: float\n"
                ":param arg19: Max. X range value\n"
                ":type arg19: float\n"
                ":param arg20: Min. Y range value\n"
                ":type arg20: float\n"
                ":param arg21: Max. Y range value\n"
                ":type arg21: float\n"
                ":param arg22: Min. Z range value\n"
                ":type arg22: float\n"
                ":param arg23: Max. Z range value\n"
                ":type arg23: float\n"
                ":param arg24: Use Min X Range selection?\n"
                ":type arg24: int\n"
                ":param arg25: Use Max X Range selection?\n"
                ":type arg25: int\n"
                ":param arg26: Use Min Y Range selection?\n"
                ":type arg26: int\n"
                ":param arg27: Use Max Y Range selection?\n"
                ":type arg27: int\n"
                ":param arg28: Use Min Z Range selection?\n"
                ":type arg28: int\n"
                ":param arg29: Use Max Z Range selection?\n"
                ":type arg29: int\n"
                ":param arg30: Plot Grid lines? (0: Just outside edge tics, 1: Grid lines).\n"
                ":type arg30: int\n"
                ":param arg31: Tic Increment (in percent)\n"
                ":type arg31: float\n"
                ":param arg32: Grid increment (in percent)\n"
                ":type arg32: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The mask channel VV is used for plotting precedence; those points with\n"
                "   mask = dummy are plotted first, then overwritten with the non-masked\n"
                "   values, so you don't get \"good\" points being covered up by masked values.\n"
                "   The view scaling is not altered with any projection. The base view\n"
                "   is best as the input.\n\n"
               ).staticmethod("tri_plot2");
    pyClass.def("fixed_symbol_tri_plot", &GXCHIMERA_wrap_fixed_symbol_tri_plot,
                "fixed_symbol_tri_plot((GXMVIEW)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (GXVV)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (int)arg10, (str)arg11, (int)arg12, (float)arg13, (float)arg14, (int)arg15, (int)arg16, (GXDB)arg17, (GXVV)arg18, (GXVV)arg19, (str)arg20, (str)arg21, (str)arg22, (int)arg23, (float)arg24, (float)arg25, (str)arg26) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Plot a tri-plot using a single fixed symbol.\n"
                "   				 Optional data masking with masking colour.\n"
                "   				 Optioinal database linking.\n"
                "   			 \n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Title\n"
                ":type arg2: str\n"
                ":param arg3: X location (bottom left corner of box)\n"
                ":type arg3: float\n"
                ":param arg4: Y location\n"
                ":type arg4: float\n"
                ":param arg5: Triangle side length\n"
                ":type arg5: float\n"
                ":param arg6: X channel data\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Y channel data\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Z channel data\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Mask channel data\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Mask colour; overrides symbol colour where mask data is not dummy. Set to iColor_MVIEW(\"\") to not plot.\n"
                ":type arg10: int\n"
                ":param arg11: decorated font name, \"\" for default symbol font (normally symbols.gfn)\n"
                ":type arg11: str\n"
                ":param arg12: Symbol number (>=0)\n"
                ":type arg12: int\n"
                ":param arg13: Symbol size ( >=0)\n"
                ":type arg13: float\n"
                ":param arg14: Symbol angle (-360 to 360)\n"
                ":type arg14: float\n"
                ":param arg15: Symbol colour\n"
                ":type arg15: int\n"
                ":param arg16: Symbol fill colour\n"
                ":type arg16: int\n"
                ":param arg17: Database (source of data)\n"
                ":type arg17: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg18: Line handles for data\n"
                ":type arg18: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg19: Fid values for data\n"
                ":type arg19: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg20: X channel name\n"
                ":type arg20: str\n"
                ":param arg21: Y channel name\n"
                ":type arg21: str\n"
                ":param arg22: Z channel name\n"
                ":type arg22: str\n"
                ":param arg23: Plot Grid lines? (0: Just outside edge tics, 1: Grid lines).\n"
                ":type arg23: int\n"
                ":param arg24: Tic Increment (in percent)\n"
                ":type arg24: float\n"
                ":param arg25: Grid increment (in percent)\n"
                ":type arg25: float\n"
                ":param arg26: plot overlay (\"\" for none)\n"
                ":type arg26: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Plot a tri plot using a single fixed symbol.\n"
                "   			 \n\n"
               ).staticmethod("fixed_symbol_tri_plot");
    pyClass.def("zone_coloured_tri_plot", &GXCHIMERA_wrap_zone_coloured_tri_plot,
                "zone_coloured_tri_plot((GXMVIEW)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (GXVV)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (int)arg10, (GXVV)arg11, (str)arg12, (str)arg13, (int)arg14, (float)arg15, (float)arg16, (int)arg17, (int)arg18, (int)arg19, (GXDB)arg20, (GXVV)arg21, (GXVV)arg22, (str)arg23, (str)arg24, (str)arg25, (int)arg26, (float)arg27, (float)arg28, (str)arg29) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Plot a tri-plot using colours based on a zone file.\n"
                "   				 Optional data masking with masking colour.\n"
                "   				 Optioinal database linking.\n"
                "   			 \n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Title\n"
                ":type arg2: str\n"
                ":param arg3: X location (bottom left corner of box)\n"
                ":type arg3: float\n"
                ":param arg4: Y location\n"
                ":type arg4: float\n"
                ":param arg5: Triangle side length\n"
                ":type arg5: float\n"
                ":param arg6: X channel data\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Y channel data\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Z channel data\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Mask channel data\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Mask colour; overrides symbol colour where mask data is not dummy. Set to iColor_MVIEW(\"\") to not plot.\n"
                ":type arg10: int\n"
                ":param arg11: Zone channel data\n"
                ":type arg11: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg12: Zone file name\n"
                ":type arg12: str\n"
                ":param arg13: decorated font name, \"\" for default symbol font (normally symbols.gfn)\n"
                ":type arg13: str\n"
                ":param arg14: Symbol number (>=0)\n"
                ":type arg14: int\n"
                ":param arg15: Symbol size ( >=0)\n"
                ":type arg15: float\n"
                ":param arg16: Symbol angle (-360 to 360)\n"
                ":type arg16: float\n"
                ":param arg17: Symbol colour\n"
                ":type arg17: int\n"
                ":param arg18: Symbol fill colour\n"
                ":type arg18: int\n"
                ":param arg19: Fix symbol edge colour?\n"
                ":type arg19: int\n"
                ":param arg20: Database (source of data)\n"
                ":type arg20: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg21: Line handles for data\n"
                ":type arg21: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg22: Fid values for data\n"
                ":type arg22: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg23: X channel name\n"
                ":type arg23: str\n"
                ":param arg24: Y channel name\n"
                ":type arg24: str\n"
                ":param arg25: Z channel name\n"
                ":type arg25: str\n"
                ":param arg26: Plot Grid lines? (0: Just outside edge tics, 1: Grid lines).\n"
                ":type arg26: int\n"
                ":param arg27: Tic Increment (in percent)\n"
                ":type arg27: float\n"
                ":param arg28: Grid increment (in percent)\n"
                ":type arg28: float\n"
                ":param arg29: plot overlay (\"\" for none)\n"
                ":type arg29: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Plot a tri plot using colours based on a zone file.\n"
                "   			 \n\n"
               ).staticmethod("zone_coloured_tri_plot");
    pyClass.def("string_classified_tri_plot", &GXCHIMERA_wrap_string_classified_tri_plot,
                "string_classified_tri_plot((GXMVIEW)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (GXVV)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (int)arg10, (GXVV)arg11, (str)arg12, (float)arg13, (GXDB)arg14, (GXVV)arg15, (GXVV)arg16, (str)arg17, (str)arg18, (str)arg19, (int)arg20, (float)arg21, (float)arg22, (str)arg23) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Plot a tri-plot using symbols based on a symbol class file.\n"
                "   				 Optional data masking with masking colour.\n"
                "   				 Optioinal database linking.\n"
                "   			 \n\n"

                ":param arg1: View\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: Title\n"
                ":type arg2: str\n"
                ":param arg3: X location (bottom left corner of box)\n"
                ":type arg3: float\n"
                ":param arg4: Y location\n"
                ":type arg4: float\n"
                ":param arg5: Triangle side length\n"
                ":type arg5: float\n"
                ":param arg6: X channel data\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Y channel data\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Z channel data\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Mask channel data\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Mask colour; overrides symbol colour. Set to iColor_MVIEW(\"\") to not plot.\n"
                ":type arg10: int\n"
                ":param arg11: Class channel data\n"
                ":type arg11: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg12: Class file (TPAT) name.\n"
                ":type arg12: str\n"
                ":param arg13: Symbol size override. Set to 0.0 to use class file symbol sizes.\n"
                ":type arg13: float\n"
                ":param arg14: Database (source of data)\n"
                ":type arg14: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg15: Line handles for data\n"
                ":type arg15: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg16: Fid values for data\n"
                ":type arg16: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg17: X channel name\n"
                ":type arg17: str\n"
                ":param arg18: Y channel name\n"
                ":type arg18: str\n"
                ":param arg19: Z channel name\n"
                ":type arg19: str\n"
                ":param arg20: Plot Grid lines? (0: Just outside edge tics, 1: Grid lines).\n"
                ":type arg20: int\n"
                ":param arg21: Tic Increment (in percent)\n"
                ":type arg21: float\n"
                ":param arg22: Grid increment (in percent)\n"
                ":type arg22: float\n"
                ":param arg23: plot overlay (\"\" for none)\n"
                ":type arg23: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Plot a tri-plot using symbols based on a symbol class file.\n"
                "   			 \n\n"
               ).staticmethod("string_classified_tri_plot");

    scope().attr("CHIMERA_MAX_CHAN") = (int32_t)128;
    scope().attr("CHIMERA_PLOT_ROSE") = (int32_t)0;
    scope().attr("CHIMERA_PLOT_PIE") = (int32_t)1;
    scope().attr("CHIMERA_PLOT_BAR") = (int32_t)2;

}
