#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXMVG_wrap_axis_x(GXMVGPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6)
{
    self->axis_x(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXMVG_wrap_axis_y(GXMVGPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6)
{
    self->axis_y(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline GXMVGPtr GXMVG_wrap_create(GXMAPPtr arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10)
{
    GXMVGPtr ret = GXMVG::create(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
    return ret;
}
inline GXMVIEWPtr GXMVG_wrap_get_mview(GXMVGPtr self)
{
    GXMVIEWPtr ret = self->get_mview();
    return ret;
}
inline void GXMVG_wrap_grid(GXMVGPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, int32_t arg7)
{
    self->grid(arg1, arg2, arg3, arg4, arg5, arg6, (MVG_GRID)arg7);
}
inline void GXMVG_wrap_label_x(GXMVGPtr self, double arg1, double arg2, double arg3, double arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    self->label_x(arg1, arg2, arg3, arg4, (MVG_LABEL_JUST)arg5, (MVG_LABEL_BOUND)arg6, (MVG_LABEL_ORIENT)arg7);
}
inline void GXMVG_wrap_label_y(GXMVGPtr self, double arg1, double arg2, double arg3, double arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    self->label_y(arg1, arg2, arg3, arg4, (MVG_LABEL_JUST)arg5, (MVG_LABEL_BOUND)arg6, (MVG_LABEL_ORIENT)arg7);
}
inline void GXMVG_wrap_poly_line_va(GXMVGPtr self, int32_t arg1, int32_t arg2, GXVVPtr arg3, GXVAPtr arg4, GXVVPtr arg5)
{
    self->poly_line_va((MVG_DRAW)arg1, (MVG_WRAP)arg2, arg3, arg4, arg5);
}
inline void GXMVG_wrap_poly_line_vv(GXMVGPtr self, int32_t arg1, int32_t arg2, GXVVPtr arg3, GXVVPtr arg4)
{
    self->poly_line_vv((MVG_DRAW)arg1, (MVG_WRAP)arg2, arg3, arg4);
}
inline void GXMVG_wrap_rescale_x_range(GXMVGPtr self, int32_t arg1, double arg2, double arg3, double arg4)
{
    self->rescale_x_range((MVG_SCALE)arg1, arg2, arg3, arg4);
}
inline void GXMVG_wrap_rescale_y_range(GXMVGPtr self, int32_t arg1, double arg2, double arg3, double arg4)
{
    self->rescale_y_range((MVG_SCALE)arg1, arg2, arg3, arg4);
}

void gxPythonImportGXMVG()
{

    class_<GXMVG, GXMVGPtr> pyClass("GXMVG",
                                    "\n.. parsed-literal::\n\n"
                                    "   The MVG class provides the ability to create view graphs.\n\n"
                                    , no_init);

    pyClass.def("null", &GXMVG::null, "null() -> GXMVG\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXMVG`\n\n:returns: A null :class:`geosoft.gxapi.GXMVG`\n:rtype: :class:`geosoft.gxapi.GXMVG`\n").staticmethod("null");
    pyClass.def("is_null", &GXMVG::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXMVG is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXMVG`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXMVG::_internal_handle);
    pyClass.def("axis_x", &GXMVG_wrap_axis_x,
                "axis_x((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw an X axis\n\n"

                ":param arg1: Y location in plot units (mm)\n"
                ":type arg1: float\n"
                ":param arg2: left  X (rescaling unit)\n"
                ":type arg2: float\n"
                ":param arg3: right X (rescaling unit)\n"
                ":type arg3: float\n"
                ":param arg4: major tick interval (rescaling unit). Ticks drawn in decades in LOG or LOGLINEAR scale\n"
                ":type arg4: float\n"
                ":param arg5: minor tick interval  (rescaling unit). Not used in LOG/LOGLINEAR\n"
                ":type arg5: float\n"
                ":param arg6: tick size in view units (mm) (negative for down ticks)\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   When Log annotation is applied, nice tick intervals will be\n"
                "   calculated\n"
                "   \n"
                "   Obsolete\n\n"
               );
    pyClass.def("axis_y", &GXMVG_wrap_axis_y,
                "axis_y((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a  Y axis\n\n"

                ":param arg1: X location in plot units (mm)\n"
                ":type arg1: float\n"
                ":param arg2: bottom Y (rescaling unit)\n"
                ":type arg2: float\n"
                ":param arg3: top Y (rescaling unit)\n"
                ":type arg3: float\n"
                ":param arg4: major tick interval (rescaling unit). Ticks drawn in decades in LOG or LOGLINEAR scale\n"
                ":type arg4: float\n"
                ":param arg5: minor tick interval  (rescaling unit). Not used in LOG/LOGLINEAR\n"
                ":type arg5: float\n"
                ":param arg6: tick size in plot units (mm)(negative for left ticks)\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   When Log annotation is applied, nice tick intervals will be\n"
                "   calculated\n"
                "   \n"
                "   Obsolete\n\n"
               );
    pyClass.def("create", &GXMVG_wrap_create,
                "create((GXMAP)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10) -> GXMVG:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a MVG object\n\n"

                ":param arg1: H_MAP handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: View Name\n"
                ":type arg2: str\n"
                ":param arg3: Minimum X in map unit (mm)\n"
                ":type arg3: float\n"
                ":param arg4: Minimum Y in map unit (mm)\n"
                ":type arg4: float\n"
                ":param arg5: Maximum X in map unit (mm)\n"
                ":type arg5: float\n"
                ":param arg6: Maximum Y in map unit (mm)\n"
                ":type arg6: float\n"
                ":param arg7: Minimum X in view unit (m for example)\n"
                ":type arg7: float\n"
                ":param arg8: Minimum Y in view unit\n"
                ":type arg8: float\n"
                ":param arg9: Maximum X in view unit\n"
                ":type arg9: float\n"
                ":param arg10: Maximum Y in view unit\n"
                ":type arg10: float\n"
                ":returns: MVG handle (NULL if error)\n"
                ":rtype: :class:`geosoft.gxapi.GXMVG`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Obsolete\n\n"
               ).staticmethod("create");
    pyClass.def("get_mview", &GXMVG_wrap_get_mview,
                "get_mview() -> GXMVIEW:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the MVIEW Handle of the Object.\n\n"

                ":returns: MVIEW Handle\n"
                ":rtype: :class:`geosoft.gxapi.GXMVIEW`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Obsolete\n\n"
               );
    pyClass.def("grid", &GXMVG_wrap_grid,
                "grid((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw a grid in the current MVG\n\n"

                ":param arg1: X position of 1st vertical grid line to draw (in rescaling unit)\n"
                ":type arg1: float\n"
                ":param arg2: Y position of 1st horizontal grid line to draw (in rescaling unit)\n"
                ":type arg2: float\n"
                ":param arg3: X grid increment of rescaled map unit (see above Rescaling functions)\n"
                ":type arg3: float\n"
                ":param arg4: Y grid increment of rescaled map unit (see above Rescaling functions)\n"
                ":type arg4: float\n"
                ":param arg5: X dot increment/cross X size of rescaled map unit\n"
                ":type arg5: float\n"
                ":param arg6: Y dot increment/cross Y size of rescaled map unit\n"
                ":type arg6: float\n"
                ":param arg7: \\ :ref:`MVG_GRID`\\ \n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The grid will be drawn in the current window.\n"
                "   \n"
                "   In the LOG and LOGLINEAR rescaling modes, grids will be\n"
                "   drawn in decades and the X/Y grid increments will be\n"
                "   ignored.  In addition, grid lines at 0 (zero) and LOGMIN will be drawn.\n"
                "   \n"
                "   Obsolete\n\n"
               );
    pyClass.def("label_x", &GXMVG_wrap_label_x,
                "label_x((float)arg1, (float)arg2, (float)arg3, (float)arg4, (int)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Label annotations on the X axis\n\n"

                ":param arg1: Y location in plot units (mm)\n"
                ":type arg1: float\n"
                ":param arg2: left  X (rescaling unit)\n"
                ":type arg2: float\n"
                ":param arg3: right X (rescaling unit)\n"
                ":type arg3: float\n"
                ":param arg4: major tick interval (ignored if in LOG or LOGLINEAR rescaling)\n"
                ":type arg4: float\n"
                ":param arg5: label justification \\ :ref:`MVG_LABEL_JUST`\\ \n"
                ":type arg5: int\n"
                ":param arg6: edge label bounding \\ :ref:`MVG_LABEL_BOUND`\\ \n"
                ":type arg6: int\n"
                ":param arg7: label orientation   \\ :ref:`MVG_LABEL_ORIENT`\\ \n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Label bounding will justify edge labels to be inside\n"
                "   the bar limits.\n"
                "   \n"
                "   When Log annotation is applied, labels will be drawn in decades.\n"
                "   \n"
                "   Obsolete\n\n"

                "\n.. seealso::\n\n"
                "   sAxisX_MVG\n\n"
               );
    pyClass.def("label_y", &GXMVG_wrap_label_y,
                "label_y((float)arg1, (float)arg2, (float)arg3, (float)arg4, (int)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Label annotations on the Y axis\n\n"

                ":param arg1: X location in plot units (mm)\n"
                ":type arg1: float\n"
                ":param arg2: bottom  Y (rescaling unit)\n"
                ":type arg2: float\n"
                ":param arg3: top Y (rescaling unit)\n"
                ":type arg3: float\n"
                ":param arg4: label interval (ignored if in LOG or LOGLINEAR rescaling)\n"
                ":type arg4: float\n"
                ":param arg5: label justification \\ :ref:`MVG_LABEL_JUST`\\ \n"
                ":type arg5: int\n"
                ":param arg6: edge label bounding \\ :ref:`MVG_LABEL_BOUND`\\ \n"
                ":type arg6: int\n"
                ":param arg7: label orientation   \\ :ref:`MVG_LABEL_ORIENT`\\ \n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Label bounding will justify edge labels to be inside\n"
                "   the bar limits.\n"
                "   \n"
                "   When Log annotation is applied, labels will be drawn in decades.\n"
                "   \n"
                "   Obsolete\n\n"

                "\n.. seealso::\n\n"
                "   sAxisY_MVG\n\n"
               );
    pyClass.def("poly_line_va", &GXMVG_wrap_poly_line_va,
                "poly_line_va((int)arg1, (int)arg2, (GXVV)arg3, (GXVA)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates PolyLines/polygons from VV and VA.\n\n"

                ":param arg1: \\ :ref:`MVG_DRAW`\\ \n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`MVG_WRAP`\\ \n"
                ":type arg2: int\n"
                ":param arg3: X VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Y VAs\n"
                ":type arg4: :class:`geosoft.gxapi.GXVA`\n"
                ":param arg5: VV containing list of VA ranges, such as 1,2 40 ... Entire VA is drawn if this VV is empty.\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the VV contains dummies, the polylines\n"
                "   will break at the dummies; the polygons\n"
                "   will skip the dummies.\n"
                "   \n"
                "   If wrapping is applied, POLYGON parameter is ignored and\n"
                "   only POLYLINES are drawn.\n"
                "   \n"
                "   Obsolete\n\n"
               );
    pyClass.def("poly_line_vv", &GXMVG_wrap_poly_line_vv,
                "poly_line_vv((int)arg1, (int)arg2, (GXVV)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates PolyLines/polygons from VV and VV.\n\n"

                ":param arg1: \\ :ref:`MVG_DRAW`\\ \n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`MVG_WRAP`\\ \n"
                ":type arg2: int\n"
                ":param arg3: X VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Y VV\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the VV contains dummies, the polylines\n"
                "   will break at the dummies; the polygons\n"
                "   will skip the dummies.\n"
                "   \n"
                "   If wrapping is applied, POLYGON parameter is ignored and\n"
                "   only POLYLINES are drawn.\n"
                "   \n"
                "   Obsolete\n\n"
               );
    pyClass.def("rescale_x_range", &GXMVG_wrap_rescale_x_range,
                "rescale_x_range((int)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Re-scale horizontal axis\n\n"

                ":param arg1: \\ :ref:`MVG_SCALE`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Scale information: new minimum X\n"
                ":type arg2: float\n"
                ":param arg3: Scale information: new maximum X\n"
                ":type arg3: float\n"
                ":param arg4: Scale information: minimum X to apply log10, it is defined only for LOGLINEAR scale\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   When RescaleX_MVG is used, only the scaling information\n"
                "   related to X axis will be considered\n"
                "   \n"
                "   Obsolete\n\n"
               );
    pyClass.def("rescale_y_range", &GXMVG_wrap_rescale_y_range,
                "rescale_y_range((int)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Re-scale vertical axis\n\n"

                ":param arg1: \\ :ref:`MVG_SCALE`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Scale information: new minimum Y\n"
                ":type arg2: float\n"
                ":param arg3: Scale information: new maximum Y\n"
                ":type arg3: float\n"
                ":param arg4: Scale information: minimum Y to apply log10, it is defined only for LOGLINEAR scale\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   When RescaleY_MVG is used, only the scaling information\n"
                "   related to Y axis will be considered\n"
                "   \n"
                "   Obsolete\n\n"
               );

    scope().attr("MVG_DRAW_POLYLINE") = (int32_t)0;
    scope().attr("MVG_DRAW_POLYGON") = (int32_t)1;
    scope().attr("MVG_GRID_DOT") = (int32_t)0;
    scope().attr("MVG_GRID_LINE") = (int32_t)1;
    scope().attr("MVG_GRID_CROSS") = (int32_t)2;
    scope().attr("MVG_LABEL_BOUND_NO") = (int32_t)0;
    scope().attr("MVG_LABEL_BOUND_YES") = (int32_t)1;
    scope().attr("MVG_LABEL_JUST_TOP") = (int32_t)0;
    scope().attr("MVG_LABEL_JUST_BOTTOM") = (int32_t)1;
    scope().attr("MVG_LABEL_JUST_LEFT") = (int32_t)2;
    scope().attr("MVG_LABEL_JUST_RIGHT") = (int32_t)3;
    scope().attr("MVG_LABEL_ORIENT_HORIZONTAL") = (int32_t)0;
    scope().attr("MVG_LABEL_ORIENT_TOP_RIGHT") = (int32_t)1;
    scope().attr("MVG_LABEL_ORIENT_TOP_LEFT") = (int32_t)2;
    scope().attr("MVG_SCALE_LINEAR") = (int32_t)0;
    scope().attr("MVG_SCALE_LOG") = (int32_t)1;
    scope().attr("MVG_SCALE_LOGLINEAR") = (int32_t)2;
    scope().attr("MVG_WRAP_NO") = (int32_t)0;
    scope().attr("MVG_WRAP_YES") = (int32_t)1;

}
