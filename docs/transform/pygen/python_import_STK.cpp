#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXSTK_wrap_get_trans_parms(GXSTKPtr self, int_ref& arg1, float_ref& arg2, GXVVPtr arg3, GXVVPtr arg4, int_ref& arg5, float_ref& arg6, GXVVPtr arg7, GXVVPtr arg8)
{
    self->get_trans_parms(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline int32_t GXSTK_wrap_get_axis_format(GXSTKPtr self, int32_t arg1)
{
    DB_CHAN_FORMAT ret = self->get_axis_format((STK_AXIS)arg1);
    return ret;
}
inline void GXSTK_wrap_get_axis_parms(GXSTKPtr self, int_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, str_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, int_ref& arg9, int32_t arg10)
{
    self->get_axis_parms(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (STK_AXIS)arg10);
}
inline void GXSTK_wrap_get_fid_parms(GXSTKPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, str_ref& arg4, float_ref& arg5, str_ref& arg6)
{
    self->get_fid_parms(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline int32_t GXSTK_wrap_get_flag(GXSTKPtr self, int32_t arg1)
{
    int32_t ret = self->get_flag((STK_FLAG)arg1);
    return ret;
}
inline void GXSTK_wrap_get_gen_parms(GXSTKPtr self, str_ref& arg1, str_ref& arg2, str_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9, float_ref& arg10, float_ref& arg11)
{
    self->get_gen_parms(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXSTK_wrap_get_grid_parms(GXSTKPtr self, int_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9, str_ref& arg10, int32_t arg11)
{
    self->get_grid_parms(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, (STK_GRID)arg11);
}
inline void GXSTK_wrap_get_label_parms(GXSTKPtr self, int_ref& arg1, float_ref& arg2, int_ref& arg3, float_ref& arg4, int_ref& arg5, float_ref& arg6, str_ref& arg7, float_ref& arg8, str_ref& arg9, int_ref& arg10, int32_t arg11)
{
    self->get_label_parms(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, (STK_AXIS)arg11);
}
inline void GXSTK_wrap_get_profile(GXSTKPtr self, int_ref& arg1, float_ref& arg2, float_ref& arg3, str_ref& arg4, int_ref& arg5, int_ref& arg6, int_ref& arg7, GXVVPtr arg8, str_ref& arg9, int_ref& arg10, str_ref& arg11, float_ref& arg12, str_ref& arg13, int_ref& arg14)
{
    self->get_profile(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14);
}
inline void GXSTK_wrap_get_profile_ex(GXSTKPtr self, int_ref& arg1, float_ref& arg2, float_ref& arg3, str_ref& arg4, int_ref& arg5, int_ref& arg6, int_ref& arg7, int_ref& arg8, GXVVPtr arg9, str_ref& arg10, int_ref& arg11, str_ref& arg12, float_ref& arg13, str_ref& arg14, int_ref& arg15)
{
    self->get_profile_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15);
}
inline void GXSTK_wrap_get_symb_parms(GXSTKPtr self, str_ref& arg1, float_ref& arg2, str_ref& arg3, str_ref& arg4, int_ref& arg5, int_ref& arg6, float_ref& arg7, int_ref& arg8, GXVVPtr arg9, GXVVPtr arg10, int_ref& arg11, str_ref& arg12, float_ref& arg13, str_ref& arg14)
{
    self->get_symb_parms(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14);
}
inline void GXSTK_wrap_get_title_parms(GXSTKPtr self, str_ref& arg1, str_ref& arg2, int_ref& arg3, float_ref& arg4, float_ref& arg5, int_ref& arg6, float_ref& arg7, float_ref& arg8, str_ref& arg9, float_ref& arg10, str_ref& arg11, int32_t arg12)
{
    self->get_title_parms(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, (STK_AXIS)arg12);
}
inline void GXSTK_wrap_set_flag(GXSTKPtr self, int32_t arg1, int32_t arg2)
{
    self->set_flag(arg1, (STK_FLAG)arg2);
}
inline void GXSTK_wrap_set_array_colors(GXSTKPtr self, GXITRPtr arg1)
{
    self->set_array_colors(arg1);
}
inline void GXSTK_wrap_set_axis_format(GXSTKPtr self, int32_t arg1, int32_t arg2)
{
    self->set_axis_format((DB_CHAN_FORMAT)arg1, (STK_AXIS)arg2);
}
inline void GXSTK_wrap_set_axis_parms(GXSTKPtr self, int32_t arg1, double arg2, double arg3, double arg4, const gx_string_type& arg5, double arg6, double arg7, double arg8, int32_t arg9, int32_t arg10)
{
    self->set_axis_parms(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (STK_AXIS)arg10);
}
inline void GXSTK_wrap_set_fid_parms(GXSTKPtr self, double arg1, double arg2, double arg3, const gx_string_type& arg4, double arg5, const gx_string_type& arg6)
{
    self->set_fid_parms(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXSTK_wrap_set_gen_parms(GXSTKPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10, double arg11)
{
    self->set_gen_parms(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXSTK_wrap_set_grid_parms(GXSTKPtr self, int32_t arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, const gx_string_type& arg10, int32_t arg11)
{
    self->set_grid_parms(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, (STK_GRID)arg11);
}
inline void GXSTK_wrap_set_label_parms(GXSTKPtr self, int32_t arg1, double arg2, int32_t arg3, double arg4, int32_t arg5, double arg6, const gx_string_type& arg7, double arg8, const gx_string_type& arg9, int32_t arg10, int32_t arg11)
{
    self->set_label_parms(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, (STK_AXIS)arg11);
}
inline void GXSTK_wrap_set_line_parm(GXSTKPtr self, int32_t arg1)
{
    self->set_line_parm(arg1);
}
inline void GXSTK_wrap_set_profile(GXSTKPtr self, int32_t arg1, double arg2, double arg3, const gx_string_type& arg4, int32_t arg5, int32_t arg6, int32_t arg7, GXVVPtr arg8, const gx_string_type& arg9, int32_t arg10, const gx_string_type& arg11, double arg12, const gx_string_type& arg13, int32_t arg14)
{
    self->set_profile(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14);
}
inline void GXSTK_wrap_set_profile_ex(GXSTKPtr self, int32_t arg1, double arg2, double arg3, const gx_string_type& arg4, int32_t arg5, int32_t arg6, int32_t arg7, int32_t arg8, GXVVPtr arg9, const gx_string_type& arg10, int32_t arg11, const gx_string_type& arg12, double arg13, const gx_string_type& arg14, int32_t arg15)
{
    self->set_profile_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15);
}
inline void GXSTK_wrap_set_symb_parms(GXSTKPtr self, const gx_string_type& arg1, double arg2, const gx_string_type& arg3, const gx_string_type& arg4, int32_t arg5, int32_t arg6, double arg7, int32_t arg8, GXVVPtr arg9, GXVVPtr arg10, int32_t arg11, const gx_string_type& arg12, double arg13, const gx_string_type& arg14)
{
    self->set_symb_parms(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14);
}
inline void GXSTK_wrap_set_title_parms(GXSTKPtr self, const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3, double arg4, double arg5, int32_t arg6, double arg7, double arg8, const gx_string_type& arg9, double arg10, const gx_string_type& arg11, int32_t arg12)
{
    self->set_title_parms(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, (STK_AXIS)arg12);
}
inline void GXSTK_wrap_set_trans_parms(GXSTKPtr self, int32_t arg1, double arg2, int32_t arg3, int32_t arg4, int32_t arg5, double arg6, int32_t arg7, int32_t arg8)
{
    self->set_trans_parms(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXSTK_wrap_set_va_index_start(GXSTKPtr self, int32_t arg1)
{
    self->set_va_index_start(arg1);
}

void gxPythonImportGXSTK()
{

    class_<GXSTK, GXSTKPtr> pyClass("GXSTK",
                                    "\n.. parsed-literal::\n\n"
                                    "   The STK class is used for plotting a single data profile in\n"
                                    "   an MVIEW. The MSTK class (see MSTK.GXH) is used to plot\n"
                                    "   multiple STK objects to a single map.\n"
                                    "   \n"
                                    "   Use \\ :func:`geosoft.gxapi.GXMSTK.add_stk`\\  fuction to create a STK object before\n"
                                    "   using functions in this file\n"
                                    "   \n"
                                    "   SEE MSTK FILE FOR DETAILED DESCRIPTIONS OF ALL FUNCTION PARAMETERS.\n\n"
                                    , no_init);

    pyClass.def("null", &GXSTK::null, "null() -> GXSTK\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXSTK`\n\n:returns: A null :class:`geosoft.gxapi.GXSTK`\n:rtype: :class:`geosoft.gxapi.GXSTK`\n").staticmethod("null");
    pyClass.def("is_null", &GXSTK::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXSTK is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXSTK`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXSTK::_internal_handle);
    pyClass.def("get_trans_parms", &GXSTK_wrap_get_trans_parms,
                "get_trans_parms((int_ref)arg1, (float_ref)arg2, (GXVV)arg3, (GXVV)arg4, (int_ref)arg5, (float_ref)arg6, (GXVV)arg7, (GXVV)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get transformation parameters in STK object\n\n"

                ":param arg1: Type of transformation for horizontal axis\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Minimum value to apply logarithmic\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Comma separated parameters defining linear compress data range\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Comma separated parameters defining scaling factors for\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Type of scaling for vertical axis\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Minimum value to apply logarithmic\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Comma separated parameters defining linear compress data range\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Comma separated parameters defining scaling factors for\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See above full description of each parameters\n"
                "   VV's for X channel transformation can be NULL if the\n"
                "   transformation is log or loglinear. The same for Y channel.\n"
                "   \n"
                "   See MSTK for detailed description of all function parameters\n\n"
               );
    pyClass.def("get_axis_format", &GXSTK_wrap_get_axis_format,
                "get_axis_format((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get axis number display format.\n\n"

                ":param arg1: \\ :ref:`STK_AXIS`\\ \n"
                ":type arg1: int\n"
                ":returns: The current format - \\ :ref:`DB_CHAN_FORMAT`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   By default, DB_CHAN_FORMAT_NORMAL\n\n"
               );
    pyClass.def("get_axis_parms", &GXSTK_wrap_get_axis_parms,
                "get_axis_parms((int_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (str_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (int_ref)arg9, (int)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get parameters in STK object relating drawing X/Y axis\n\n"

                ":param arg1: ?BARDRAW: Bottom and/or Top, or Left and/or Right\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Bottom Y/Left X location\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Top Y/Right X location\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: ?BARLINETHICK  - Line thickness in mm. Default is 0.05\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: ?BARCOLOR      - Line color string in RGB model. Default is black\n"
                ":type arg5: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg6: ?BARTICKINTEERVAL\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Major tick size in mm for bottom/left axis bar.\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Major tick size in mm for top/right axis bar.\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: ?BARMINORTICK  - Number of minor ticks. (0) none, (-1) automatic\n"
                ":type arg9: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg10: \\ :ref:`STK_AXIS`\\ \n"
                ":type arg10: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n"
                "   ? mark in the note represent either X and Y\n\n"
               );
    pyClass.def("get_fid_parms", &GXSTK_wrap_get_fid_parms,
                "get_fid_parms((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (str_ref)arg4, (float_ref)arg5, (str_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get parameters in STK object relating drawing fid ticks\n\n"

                ":param arg1: Y location in data unit to draw Fid ticks. Default is the bottom of the stack\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Fid tick size in mm. Default is 2.0mm\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Fid interval to draw ticks. Nice number is calculated by default\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Font to use to label fids. Default is use 'default' font set in Montaj\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: Text size in mm to label fids. Default is 5mm\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Text color string in RGB model. Default is black\n"
                ":type arg6: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n\n"
               );
    pyClass.def("get_flag", &GXSTK_wrap_get_flag,
                "get_flag((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get flag indicating part of STK object is to be drawn or not\n\n"

                ":param arg1: \\ :ref:`STK_FLAG`\\ \n"
                ":type arg1: int\n"
                ":returns: FALSE (0) if part of the object is not to be drawn\n"
                "          TRUE  (1) if part of the object is drawn\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               );
    pyClass.def("get_gen_parms", &GXSTK_wrap_get_gen_parms,
                "get_gen_parms((str_ref)arg1, (str_ref)arg2, (str_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9, (float_ref)arg10, (float_ref)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get general parameters in STK object\n\n"

                ":param arg1: X channel name, REQUIRED\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: Y channel name, REQUIRED\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Group name\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: X scale (map scale, units/metre), REQUIRED\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Y scale (plot scale, units/mm), REQUIRED\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Minimum X value (data unit) to draw\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Maximum X value (data unit) to draw\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Minimum Y value (data unit) to draw\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Minimum horizontal location in mm of the stack on the map\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: Minimum vertical location in mm on the map\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: Profile height in mm on the map, must be > 0.0\n"
                ":type arg11: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n\n"
               );
    pyClass.def("get_grid_parms", &GXSTK_wrap_get_grid_parms,
                "get_grid_parms((int_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9, (str_ref)arg10, (int)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get background grid parameters in STK object\n\n"

                ":param arg1: Type of grid to draw:\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Minimum X in ground unit to draw grid\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Maximum X in ground unit to draw grid\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Minimum Y in ground unit to draw grid\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Maximum Y in ground unit to draw grid\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Line thickness in mm. Default is 0.01mm\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Cross size or separation between dots in mm.\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Separation between vertical grid lines.\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Separation between horizontal grid lines.\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: Grid line color string in RGB model. Default is black\n"
                ":type arg10: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg11: \\ :ref:`STK_GRID`\\ \n"
                ":type arg11: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n"
                "   ? mark in the note represent either X and Y\n\n"
               );
    pyClass.def("get_label_parms", &GXSTK_wrap_get_label_parms,
                "get_label_parms((int_ref)arg1, (float_ref)arg2, (int_ref)arg3, (float_ref)arg4, (int_ref)arg5, (float_ref)arg6, (str_ref)arg7, (float_ref)arg8, (str_ref)arg9, (int_ref)arg10, (int)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get parameters in STK object relating X/Y axis labels\n\n"

                ":param arg1: Which axes to draw: Bottom/Top or Left/Right axes\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Bottom or Left axis label location\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Bottom or Left labels orientation.\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Top or Right axis label location\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Top or Right axis label orientation\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Label interval. Default is to use related axis tick interval\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Font to use to label. Default is use 'default' font set in Montaj\n"
                ":type arg7: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg8: Text size in mm to draw profile labels. Default is 5mm\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Text color string in RGB model. Default is black\n"
                ":type arg9: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg10: ?LABELBOUND    - Edge bound.  0 - No\n"
                ":type arg10: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg11: \\ :ref:`STK_AXIS`\\ \n"
                ":type arg11: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n"
                "   ? mark in the note represent either X and Y\n"
                "   Sets the label format to GSF_NORMAL. To override this,\n"
                "   use the \\ :func:`geosoft.gxapi.GXSTK.set_axis_format`\\  function AFTER calling this.\n\n"
               );
    pyClass.def("get_profile", &GXSTK_wrap_get_profile,
                "get_profile((int_ref)arg1, (float_ref)arg2, (float_ref)arg3, (str_ref)arg4, (int_ref)arg5, (int_ref)arg6, (int_ref)arg7, (GXVV)arg8, (str_ref)arg9, (int_ref)arg10, (str_ref)arg11, (float_ref)arg12, (str_ref)arg13, (int_ref)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get profile parameters in STK object\n\n"

                ":param arg1: Profile line type.    1 - solid (default)\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Patterned line pitch in mm. Default is 10 mm\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Line thickness in mm. Default is 0.05mm\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Color string in RGB model. Default is black\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: Wrap option\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Clip option\n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg7: Plot smoothed polyline.\n"
                ":type arg7: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg8: Only use for VA channels. NULL is acceptable which means all profiles in the VA are plotted. VV type of INT (integer)\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Characters string to label profiles\n"
                ":type arg9: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg10: Reference location to draw label.\n"
                ":type arg10: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg11: Font to use to draw profile labels. Default is use 'default' font set in Montaj\n"
                ":type arg11: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg12: Text size in mm to draw profile labels. Default is 5mm\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg13: Text color string in RGB model. Default is black\n"
                ":type arg13: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg14: Include VA column numbers as part of the profile label 0 - no, 1 - yes\n"
                ":type arg14: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n\n"
               );
    pyClass.def("get_profile_ex", &GXSTK_wrap_get_profile_ex,
                "get_profile_ex((int_ref)arg1, (float_ref)arg2, (float_ref)arg3, (str_ref)arg4, (int_ref)arg5, (int_ref)arg6, (int_ref)arg7, (int_ref)arg8, (GXVV)arg9, (str_ref)arg10, (int_ref)arg11, (str_ref)arg12, (float_ref)arg13, (str_ref)arg14, (int_ref)arg15) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get profile parameters in STK object (added Break on dummy option)\n\n"

                ":param arg1: Profile line type.    1 - solid (default)\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Patterned line pitch in mm. Default is 10 mm\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Line thickness in mm. Default is 0.05mm\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Color string in RGB model. Default is black\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: Break on dummy option\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Wrap option\n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg7: Clip option\n"
                ":type arg7: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg8: Plot smoothed polyline.\n"
                ":type arg8: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg9: Only use for VA channels. NULL is acceptable which means all profiles in the VA are plotted. VV type of INT (integer)\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Characters string to label profiles\n"
                ":type arg10: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg11: Reference location to draw label.\n"
                ":type arg11: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg12: Font to use to draw profile labels. Default is use 'default' font set in Montaj\n"
                ":type arg12: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg13: Text size in mm to draw profile labels. Default is 5mm\n"
                ":type arg13: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg14: Text color string in RGB model. Default is black\n"
                ":type arg14: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg15: Include VA column numbers as part of the profile label 0 - no, 1 - yes\n"
                ":type arg15: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n\n"
               );
    pyClass.def("get_symb_parms", &GXSTK_wrap_get_symb_parms,
                "get_symb_parms((str_ref)arg1, (float_ref)arg2, (str_ref)arg3, (str_ref)arg4, (int_ref)arg5, (int_ref)arg6, (float_ref)arg7, (int_ref)arg8, (GXVV)arg9, (GXVV)arg10, (int_ref)arg11, (str_ref)arg12, (float_ref)arg13, (str_ref)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get parameters in STK object relating drawing symbols\n\n"

                ":param arg1: Font to use to draw symbols. Default is use 'symbols.gfn' font\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: Symbol size in mm. Default is 5mm\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Edge color string in RGB model. Default is black\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Fill color string in RGB model. Default is black\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: Wrap option\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Clip option\n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg7: Y location to draw symbols. Default is to use the data from Y channel\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Number of levels to draw symbols\n"
                ":type arg8: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg9: Y values to define data ranges for each symbol types Type of REAL\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Symbol numbers (given in the symbol font) to draw, default is 20 TYPE of INT\n"
                ":type arg10: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg11: Draw symbols ID (1) or not (0)\n"
                ":type arg11: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg12: Font to use to draw symbol ID (A,B,C...). Default is use 'default'\n"
                ":type arg12: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg13: Text size in mm to draw profile labels. Default is 5mm\n"
                ":type arg13: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg14: Text color string in RGB model. Default is black\n"
                ":type arg14: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n\n"
               );
    pyClass.def("get_title_parms", &GXSTK_wrap_get_title_parms,
                "get_title_parms((str_ref)arg1, (str_ref)arg2, (int_ref)arg3, (float_ref)arg4, (float_ref)arg5, (int_ref)arg6, (float_ref)arg7, (float_ref)arg8, (str_ref)arg9, (float_ref)arg10, (str_ref)arg11, (int)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get parameters in STK object relating X/Y axis titles\n\n"

                ":param arg1: Title for bottom X axis/left Y axis. Default is no title.\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: Title for top X axis/right Y axis. Default is no title.\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Bottom/Left axis title orientation.\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: X location to draw bottom/left axis title\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Y location to draw bottom/left axis title\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Top/Right axis title orientation.\n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg7: X location to draw top/right axis title\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Y location to draw top/right axis title\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Font to draw titles. Default is use 'default' font set in Montaj\n"
                ":type arg9: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg10: Text size in mm to draw titles. Default is 5mm\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: Text color string in RGB model. Default is black\n"
                ":type arg11: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg12: \\ :ref:`STK_AXIS`\\ \n"
                ":type arg12: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n"
                "   ? mark in the note represent either X and Y\n\n"
               );
    pyClass.def("set_flag", &GXSTK_wrap_set_flag,
                "set_flag((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set flag indicating part of STK object is to be drawn or not\n\n"

                ":param arg1: Flag to set (0 or 1)\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`STK_FLAG`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_array_colors", &GXSTK_wrap_set_array_colors,
                "set_array_colors((GXITR)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set colours for individual channels in a VA, via an ITR\n\n"

                ":param arg1: ITR object for colours\n"
                ":type arg1: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The ITR is consulted by taking the channel index and dividing\n"
                "   by the number of channels; hence the ITR maximum values should\n"
                "   be in the range: 0 > values >= 1.0.\n\n"
               );
    pyClass.def("set_axis_format", &GXSTK_wrap_set_axis_format,
                "set_axis_format((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set axis number display format.\n\n"

                ":param arg1: \\ :ref:`DB_CHAN_FORMAT`\\ \n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`STK_AXIS`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   By default, DB_CHAN_FORMAT_NORMAL is used to display the values,\n"
                "   or for values > 1.e7, DB_CHAN_FORMAT_EXP.\n\n"
               );
    pyClass.def("set_axis_parms", &GXSTK_wrap_set_axis_parms,
                "set_axis_parms((int)arg1, (float)arg2, (float)arg3, (float)arg4, (str)arg5, (float)arg6, (float)arg7, (float)arg8, (int)arg9, (int)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set parameters in STK object relating drawing X/Y axis\n\n"

                ":param arg1: ?BARDRAW\n"
                ":type arg1: int\n"
                ":param arg2: Bottom Y/Left X location\n"
                ":type arg2: float\n"
                ":param arg3: Top Y/Right X location\n"
                ":type arg3: float\n"
                ":param arg4: ?BARLINETHICK  - Line thickness in mm. Default is 0.05\n"
                ":type arg4: float\n"
                ":param arg5: ?BARCOLOR      - Line color string in RGB model. Default is black\n"
                ":type arg5: str\n"
                ":param arg6: ?BARTICKINTEERVAL\n"
                ":type arg6: float\n"
                ":param arg7: Major tick size in mm for bottom/left axis bar.\n"
                ":type arg7: float\n"
                ":param arg8: Major tick size in mm for top/right axis bar.\n"
                ":type arg8: float\n"
                ":param arg9: ?BARMINORTICK  - Number of minor ticks. (0) none, (-1) automatic\n"
                ":type arg9: int\n"
                ":param arg10: \\ :ref:`STK_AXIS`\\ \n"
                ":type arg10: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n"
                "   ? mark in the note represent either X and Y\n\n"
               );
    pyClass.def("set_fid_parms", &GXSTK_wrap_set_fid_parms,
                "set_fid_parms((float)arg1, (float)arg2, (float)arg3, (str)arg4, (float)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set parameters in STK object relating drawing fid ticks\n\n"

                ":param arg1: Y location in data unit to draw Fid ticks. Default is the bottom of the stack\n"
                ":type arg1: float\n"
                ":param arg2: Fid tick size in mm. Default is 2.0mm\n"
                ":type arg2: float\n"
                ":param arg3: Fid interval to draw ticks. Nice number is calculated by default\n"
                ":type arg3: float\n"
                ":param arg4: Font to use to label fids. Default is use 'default' font set in Montaj\n"
                ":type arg4: str\n"
                ":param arg5: Text size in mm to label fids. Default is 5mm\n"
                ":type arg5: float\n"
                ":param arg6: Text color string in RGB model. Default is black\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n\n"
               );
    pyClass.def("set_gen_parms", &GXSTK_wrap_set_gen_parms,
                "set_gen_parms((str)arg1, (str)arg2, (str)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (float)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set general parameters in STK object\n\n"

                ":param arg1: X channel name, REQUIRED\n"
                ":type arg1: str\n"
                ":param arg2: Y channel name, REQUIRED\n"
                ":type arg2: str\n"
                ":param arg3: Group name\n"
                ":type arg3: str\n"
                ":param arg4: X scale (map scale, units/metre), REQUIRED\n"
                ":type arg4: float\n"
                ":param arg5: Y scale (plot scale, units/mm), REQUIRED\n"
                ":type arg5: float\n"
                ":param arg6: Minimum X value (data unit) to draw\n"
                ":type arg6: float\n"
                ":param arg7: Maximum X value (data unit) to draw\n"
                ":type arg7: float\n"
                ":param arg8: Minimum Y value (data unit) to draw\n"
                ":type arg8: float\n"
                ":param arg9: Minimum horizontal location in mm of the stack on the map\n"
                ":type arg9: float\n"
                ":param arg10: Minimum vertical location in mm on the map\n"
                ":type arg10: float\n"
                ":param arg11: Profile height in mm on the map, must be > 0.0\n"
                ":type arg11: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n\n"
               );
    pyClass.def("set_grid_parms", &GXSTK_wrap_set_grid_parms,
                "set_grid_parms((int)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (str)arg10, (int)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set background grid parameters in STK object\n\n"

                ":param arg1: Type of grid to draw:\n"
                ":type arg1: int\n"
                ":param arg2: Minimum X in ground unit to draw grid\n"
                ":type arg2: float\n"
                ":param arg3: Maximum X in ground unit to draw grid\n"
                ":type arg3: float\n"
                ":param arg4: Minimum Y in ground unit to draw grid\n"
                ":type arg4: float\n"
                ":param arg5: Maximum Y in ground unit to draw grid\n"
                ":type arg5: float\n"
                ":param arg6: Line thickness in mm. Default is 0.01mm\n"
                ":type arg6: float\n"
                ":param arg7: Cross size or separation between dots in mm.\n"
                ":type arg7: float\n"
                ":param arg8: Separation between vertical grid lines.\n"
                ":type arg8: float\n"
                ":param arg9: Separation between horizontal grid lines.\n"
                ":type arg9: float\n"
                ":param arg10: Grid line color string in RGB model. Default is black\n"
                ":type arg10: str\n"
                ":param arg11: \\ :ref:`STK_GRID`\\ \n"
                ":type arg11: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n"
                "   ? mark in the note represent either X and Y\n\n"
               );
    pyClass.def("set_label_parms", &GXSTK_wrap_set_label_parms,
                "set_label_parms((int)arg1, (float)arg2, (int)arg3, (float)arg4, (int)arg5, (float)arg6, (str)arg7, (float)arg8, (str)arg9, (int)arg10, (int)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set parameters in STK object relating X/Y axis labels\n\n"

                ":param arg1: Bottom/Top or Left/Right axes\n"
                ":type arg1: int\n"
                ":param arg2: Bottom or Left axis label location\n"
                ":type arg2: float\n"
                ":param arg3: Bottom or Left labels orientation.\n"
                ":type arg3: int\n"
                ":param arg4: Top or Right axis label location\n"
                ":type arg4: float\n"
                ":param arg5: Top or Right axis label orientation\n"
                ":type arg5: int\n"
                ":param arg6: Label interval. Default is to use related axis tick interval\n"
                ":type arg6: float\n"
                ":param arg7: Font to use to label. Default is use 'default' font set in Montaj\n"
                ":type arg7: str\n"
                ":param arg8: Text size in mm to draw profile labels. Default is 5mm\n"
                ":type arg8: float\n"
                ":param arg9: Text color string in RGB model. Default is black\n"
                ":type arg9: str\n"
                ":param arg10: ?LABELBOUND    - Edge bound.  0 - No\n"
                ":type arg10: int\n"
                ":param arg11: \\ :ref:`STK_AXIS`\\ \n"
                ":type arg11: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n"
                "   ? mark in the note represent either X and Y\n"
                "   Sets the label format to GSF_NORMAL. To override this,\n"
                "   use the \\ :func:`geosoft.gxapi.GXSTK.set_axis_format`\\  function AFTER calling this.\n\n"
               );
    pyClass.def("set_line_parm", &GXSTK_wrap_set_line_parm,
                "set_line_parm((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set line parameter (of Y Chan) in STK object\n\n"

                ":param arg1: Line symb\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n\n"
               );
    pyClass.def("set_profile", &GXSTK_wrap_set_profile,
                "set_profile((int)arg1, (float)arg2, (float)arg3, (str)arg4, (int)arg5, (int)arg6, (int)arg7, (GXVV)arg8, (str)arg9, (int)arg10, (str)arg11, (float)arg12, (str)arg13, (int)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set profile parameters in STK object\n\n"

                ":param arg1: Profile line type.    1 - solid (default)\n"
                ":type arg1: int\n"
                ":param arg2: Patterned line pitch in mm. Default is 10 mm\n"
                ":type arg2: float\n"
                ":param arg3: Line thickness in mm. Default is 0.05mm\n"
                ":type arg3: float\n"
                ":param arg4: Color string in RGB model. Default is black\n"
                ":type arg4: str\n"
                ":param arg5: Wrap option\n"
                ":type arg5: int\n"
                ":param arg6: Clip option\n"
                ":type arg6: int\n"
                ":param arg7: Plot smoothed polyline.\n"
                ":type arg7: int\n"
                ":param arg8: Integers starting from 0 indicating windows in VA channel to draw VV type of INT (integer)\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Characters string to label profiles\n"
                ":type arg9: str\n"
                ":param arg10: Reference location to draw label.\n"
                ":type arg10: int\n"
                ":param arg11: Font to use to draw profile labels. Default is use 'default' font set in Montaj\n"
                ":type arg11: str\n"
                ":param arg12: Text size in mm to draw profile labels. Default is 5mm\n"
                ":type arg12: float\n"
                ":param arg13: Text color string in RGB model. Default is black\n"
                ":type arg13: str\n"
                ":param arg14: Include VA column numbers as part of the profile label 0 - no, 1 - yes\n"
                ":type arg14: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n\n"
               );
    pyClass.def("set_profile_ex", &GXSTK_wrap_set_profile_ex,
                "set_profile_ex((int)arg1, (float)arg2, (float)arg3, (str)arg4, (int)arg5, (int)arg6, (int)arg7, (int)arg8, (GXVV)arg9, (str)arg10, (int)arg11, (str)arg12, (float)arg13, (str)arg14, (int)arg15) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set profile parameters in STK object (added Break on dummy option)\n\n"

                ":param arg1: Profile line type.    1 - solid (default)\n"
                ":type arg1: int\n"
                ":param arg2: Patterned line pitch in mm. Default is 10 mm\n"
                ":type arg2: float\n"
                ":param arg3: Line thickness in mm. Default is 0.05mm\n"
                ":type arg3: float\n"
                ":param arg4: Color string in RGB model. Default is black\n"
                ":type arg4: str\n"
                ":param arg5: Break on dummy option\n"
                ":type arg5: int\n"
                ":param arg6: Wrap option\n"
                ":type arg6: int\n"
                ":param arg7: Clip option\n"
                ":type arg7: int\n"
                ":param arg8: Plot smoothed polyline.\n"
                ":type arg8: int\n"
                ":param arg9: Integers starting from 0 indicating windows in VA channel to draw VV type of INT (integer)\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Characters string to label profiles\n"
                ":type arg10: str\n"
                ":param arg11: Reference location to draw label.\n"
                ":type arg11: int\n"
                ":param arg12: Font to use to draw profile labels. Default is use 'default' font set in Montaj\n"
                ":type arg12: str\n"
                ":param arg13: Text size in mm to draw profile labels. Default is 5mm\n"
                ":type arg13: float\n"
                ":param arg14: Text color string in RGB model. Default is black\n"
                ":type arg14: str\n"
                ":param arg15: Include VA column numbers as part of the profile label 0 - no, 1 - yes\n"
                ":type arg15: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n\n"
               );
    pyClass.def("set_symb_parms", &GXSTK_wrap_set_symb_parms,
                "set_symb_parms((str)arg1, (float)arg2, (str)arg3, (str)arg4, (int)arg5, (int)arg6, (float)arg7, (int)arg8, (GXVV)arg9, (GXVV)arg10, (int)arg11, (str)arg12, (float)arg13, (str)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set parameters in STK object relating drawing symbols\n\n"

                ":param arg1: Font to use to draw symbols. Default is use 'symbols.gfn' font\n"
                ":type arg1: str\n"
                ":param arg2: Symbol size in mm. Default is 5mm\n"
                ":type arg2: float\n"
                ":param arg3: Edge color string in RGB model. Default is black\n"
                ":type arg3: str\n"
                ":param arg4: Fill color string in RGB model. Default is black\n"
                ":type arg4: str\n"
                ":param arg5: Wrap option\n"
                ":type arg5: int\n"
                ":param arg6: Clip option\n"
                ":type arg6: int\n"
                ":param arg7: Y location to draw symbols. Default is to use the data from Y channel\n"
                ":type arg7: float\n"
                ":param arg8: Number of symbols levels\n"
                ":type arg8: int\n"
                ":param arg9: Y values to define data ranges for each symbol types Type of REAL\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Symbol numbers (given in the symbol font) to draw Type of INT\n"
                ":type arg10: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg11: Draw symbols ID (1) or not (0)\n"
                ":type arg11: int\n"
                ":param arg12: Font to use to draw symbol ID (A,B,C...). Default is use 'default'\n"
                ":type arg12: str\n"
                ":param arg13: Text size in mm to draw profile labels. Default is 5mm\n"
                ":type arg13: float\n"
                ":param arg14: Text color string in RGB model. Default is black\n"
                ":type arg14: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n\n"
               );
    pyClass.def("set_title_parms", &GXSTK_wrap_set_title_parms,
                "set_title_parms((str)arg1, (str)arg2, (int)arg3, (float)arg4, (float)arg5, (int)arg6, (float)arg7, (float)arg8, (str)arg9, (float)arg10, (str)arg11, (int)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set parameters in STK object relating X/Y axis titles\n\n"

                ":param arg1: Title for bottom X axis/left Y axis. Default is no title.\n"
                ":type arg1: str\n"
                ":param arg2: Title for top X axis/right Y axis. Default is no title.\n"
                ":type arg2: str\n"
                ":param arg3: Bottom/Left axis title orientation.\n"
                ":type arg3: int\n"
                ":param arg4: X location to draw bottom/left axis title\n"
                ":type arg4: float\n"
                ":param arg5: Y location to draw bottom/left axis title\n"
                ":type arg5: float\n"
                ":param arg6: Top/Right axis title orientation.\n"
                ":type arg6: int\n"
                ":param arg7: X location to draw top/right axis title\n"
                ":type arg7: float\n"
                ":param arg8: Y location to draw top/right axis title\n"
                ":type arg8: float\n"
                ":param arg9: Font to draw titles. Default is use 'default' font set in Montaj\n"
                ":type arg9: str\n"
                ":param arg10: Text size in mm to draw titles. Default is 5mm\n"
                ":type arg10: float\n"
                ":param arg11: Text color string in RGB model. Default is black\n"
                ":type arg11: str\n"
                ":param arg12: \\ :ref:`STK_AXIS`\\ \n"
                ":type arg12: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See MSTK for detailed description of all function parameters\n"
                "   ? mark in the note represent either X and Y\n\n"
               );
    pyClass.def("set_trans_parms", &GXSTK_wrap_set_trans_parms,
                "set_trans_parms((int)arg1, (float)arg2, (int)arg3, (int)arg4, (int)arg5, (float)arg6, (int)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set transformation parameters in STK object\n\n"

                ":param arg1: Type of transformation for horizontal axis\n"
                ":type arg1: int\n"
                ":param arg2: Minimum value to apply logarithmic\n"
                ":type arg2: float\n"
                ":param arg3: future use\n"
                ":type arg3: int\n"
                ":param arg4: future use\n"
                ":type arg4: int\n"
                ":param arg5: Type of scaling for vertical axis\n"
                ":type arg5: int\n"
                ":param arg6: Minimum value to apply logarithmic\n"
                ":type arg6: float\n"
                ":param arg7: future use\n"
                ":type arg7: int\n"
                ":param arg8: future use\n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See above full description of each parameters\n"
                "   VV's for X channel transformation can be NULL if the\n"
                "   transformation is log or loglinear. The same for Y channel.\n"
                "   See MSTK for detailed description of all function parameters\n\n"
               );
    pyClass.def("set_va_index_start", &GXSTK_wrap_set_va_index_start,
                "set_va_index_start((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Start array profile index labels at 0 or 1.\n\n"

                ":param arg1: Starting index (0 or 1)\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   By default, the index labels for array channel profiles\n"
                "   begin at 0. Use this function to start them at either 0\n"
                "   or 1.\n\n"
               );

    scope().attr("STK_AXIS_X") = (int32_t)0;
    scope().attr("STK_AXIS_Y") = (int32_t)1;
    scope().attr("STK_FLAG_PROFILE") = (int32_t)0;
    scope().attr("STK_FLAG_FID") = (int32_t)1;
    scope().attr("STK_FLAG_SYMBOL") = (int32_t)2;
    scope().attr("STK_FLAG_XBAR") = (int32_t)3;
    scope().attr("STK_FLAG_XLABEL") = (int32_t)4;
    scope().attr("STK_FLAG_XTITLE") = (int32_t)5;
    scope().attr("STK_FLAG_YBAR") = (int32_t)6;
    scope().attr("STK_FLAG_YLABEL") = (int32_t)7;
    scope().attr("STK_FLAG_YTITLE") = (int32_t)8;
    scope().attr("STK_FLAG_GRID1") = (int32_t)9;
    scope().attr("STK_FLAG_GRID2") = (int32_t)10;
    scope().attr("STK_GRID_PRIMARY") = (int32_t)0;
    scope().attr("STK_GRID_SECONDARY") = (int32_t)1;

}
