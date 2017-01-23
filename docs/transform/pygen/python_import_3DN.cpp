#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GX3DN_wrap_copy(GX3DNPtr self, GX3DNPtr arg1)
{
    self->copy(arg1);
}
inline GX3DNPtr GX3DN_wrap_create()
{
    GX3DNPtr ret = GX3DN::create();
    return ret;
}
inline void GX3DN_wrap_get_point_of_view(GX3DNPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3)
{
    self->get_point_of_view(arg1, arg2, arg3);
}
inline void GX3DN_wrap_get_scale(GX3DNPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3)
{
    self->get_scale(arg1, arg2, arg3);
}
inline int32_t GX3DN_wrap_get_axis_color(GX3DNPtr self)
{
    int32_t ret = self->get_axis_color();
    return ret;
}
inline void GX3DN_wrap_get_axis_font(GX3DNPtr self, str_ref& arg1)
{
    self->get_axis_font(arg1);
}
inline int32_t GX3DN_wrap_get_background_color(GX3DNPtr self)
{
    int32_t ret = self->get_background_color();
    return ret;
}
inline void GX3DN_wrap_get_render_controls(GX3DNPtr self, int_ref& arg1, int_ref& arg2, str_ref& arg3, str_ref& arg4, str_ref& arg5)
{
    self->get_render_controls(arg1, arg2, arg3, arg4, arg5);
}
inline int32_t GX3DN_wrap_get_shading(GX3DNPtr self)
{
    int32_t ret = self->get_shading();
    return ret;
}
inline void GX3DN_wrap_set_axis_color(GX3DNPtr self, int32_t arg1)
{
    self->set_axis_color(arg1);
}
inline void GX3DN_wrap_set_axis_font(GX3DNPtr self, const gx_string_type& arg1)
{
    self->set_axis_font(arg1);
}
inline void GX3DN_wrap_set_background_color(GX3DNPtr self, int32_t arg1)
{
    self->set_background_color(arg1);
}
inline void GX3DN_wrap_set_point_of_view(GX3DNPtr self, double arg1, double arg2, double arg3)
{
    self->set_point_of_view(arg1, arg2, arg3);
}
inline void GX3DN_wrap_set_render_controls(GX3DNPtr self, int32_t arg1, int32_t arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5)
{
    self->set_render_controls(arg1, arg2, arg3, arg4, arg5);
}
inline void GX3DN_wrap_set_scale(GX3DNPtr self, double arg1, double arg2, double arg3)
{
    self->set_scale(arg1, arg2, arg3);
}
inline void GX3DN_wrap_set_shading(GX3DNPtr self, int32_t arg1)
{
    self->set_shading(arg1);
}

void gxPythonImportGX3DN()
{

    class_<GX3DN, GX3DNPtr> pyClass("GX3DN",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		This class manages the rendering of a 3D view. It allows\n"
                                    "   		the positioning of the camera, specification of the zoom\n"
                                    "   		as well as some rendering controls for the axis. It is\n"
                                    "   		directly releated to the MVIEW class.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GX3DN::null, "null() -> GX3DN\n\nA null (undefined) instance of :class:`geosoft.gxapi.GX3DN`\n\n:returns: A null :class:`geosoft.gxapi.GX3DN`\n:rtype: :class:`geosoft.gxapi.GX3DN`\n").staticmethod("null");
    pyClass.def("is_null", &GX3DN::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GX3DN is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GX3DN`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GX3DN::_internal_handle);
    pyClass.def("copy", &GX3DN_wrap_copy,
                "copy((GX3DN)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy one 3DN object to another.\n\n"

                ":param arg1: Source 3DN to Copy from\n"
                ":type arg1: :class:`geosoft.gxapi.GX3DN`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("create", &GX3DN_wrap_create,
                "create() -> GX3DN:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a 3DN.\n\n"

                ":returns: 3DN Object\n"
                ":rtype: :class:`geosoft.gxapi.GX3DN`\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               ).staticmethod("create");
    pyClass.def("get_point_of_view", &GX3DN_wrap_get_point_of_view,
                "get_point_of_view((float_ref)arg1, (float_ref)arg2, (float_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get location of the point we are looking from\n\n"

                ":param arg1: Distance from center relative to longest grid dimension (which is 1.0)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Declination, 0 to 360 CW from Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Inclination, -90 to +90\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("get_scale", &GX3DN_wrap_get_scale,
                "get_scale((float_ref)arg1, (float_ref)arg2, (float_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the axis relative scales.\n\n"

                ":param arg1: X Scale\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y Scale\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Z Scale\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("get_axis_color", &GX3DN_wrap_get_axis_color,
                "get_axis_color() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Axis draw color\n\n"

                ":returns: Axis Color\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("get_axis_font", &GX3DN_wrap_get_axis_font,
                "get_axis_font((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Axis font\n\n"

                ":param arg1: Font name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("get_background_color", &GX3DN_wrap_get_background_color,
                "get_background_color() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the window background color\n\n"

                ":returns: Background Color value\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("get_render_controls", &GX3DN_wrap_get_render_controls,
                "get_render_controls((int_ref)arg1, (int_ref)arg2, (str_ref)arg3, (str_ref)arg4, (str_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the rendering controls\n\n"

                ":param arg1: Render Bounding Box (0 or 1)\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Render Axis (0 or 1)\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Label for X axis\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Label for Y axis\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: Label for Z axis\n"
                ":type arg5: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("get_shading", &GX3DN_wrap_get_shading,
                "get_shading() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the shading control on or off\n\n"

                ":returns: Shading On/Off\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("set_axis_color", &GX3DN_wrap_set_axis_color,
                "set_axis_color((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Axis draw color\n\n"

                ":param arg1: Axis Color\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("set_axis_font", &GX3DN_wrap_set_axis_font,
                "set_axis_font((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Axis font\n\n"

                ":param arg1: Font name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("set_background_color", &GX3DN_wrap_set_background_color,
                "set_background_color((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the window background color\n\n"

                ":param arg1: Background Color\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("set_point_of_view", &GX3DN_wrap_set_point_of_view,
                "set_point_of_view((float)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set location of the point we are looking from\n\n"

                ":param arg1: Distance from center relative to longest grid dimension (which is 1.0)\n"
                ":type arg1: float\n"
                ":param arg2: Declination, 0 to 360 CW from Y\n"
                ":type arg2: float\n"
                ":param arg3: Inclination, -90 to +90\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("set_render_controls", &GX3DN_wrap_set_render_controls,
                "set_render_controls((int)arg1, (int)arg2, (str)arg3, (str)arg4, (str)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the rendering controls\n\n"

                ":param arg1: Render Bounding Box (0 or 1)\n"
                ":type arg1: int\n"
                ":param arg2: Render Axis (0 or 1)\n"
                ":type arg2: int\n"
                ":param arg3: Label for X axis\n"
                ":type arg3: str\n"
                ":param arg4: Label for Y axis\n"
                ":type arg4: str\n"
                ":param arg5: Label for Z axis\n"
                ":type arg5: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("set_scale", &GX3DN_wrap_set_scale,
                "set_scale((float)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the axis relative scales.\n\n"

                ":param arg1: X Scale (default 1.0)\n"
                ":type arg1: float\n"
                ":param arg2: Y Scale (default 1.0)\n"
                ":type arg2: float\n"
                ":param arg3: Z Scale (default 1.0)\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					By default all scales are equal (1.0). By setting\n"
                "   					these scales, relative adjustments to the overall\n"
                "   					view of the 3D objects can be made. Note that they\n"
                "   					are relative to each other. Thus, setting the scaling\n"
                "   					to 5,5,5 is the same as 1,1,1. This is typically used\n"
                "   					to exagerate one scale such as Z (1,1,5).\n"
                "   				\n\n"
               );
    pyClass.def("set_shading", &GX3DN_wrap_set_shading,
                "set_shading((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the shading control on or off\n\n"

                ":param arg1: 0: Off, 1:  On.\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );


}
