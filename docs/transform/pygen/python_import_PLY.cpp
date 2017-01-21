#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXPLY_wrap_add_polygon(GXPLYPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->add_polygon(arg1, arg2);
}
inline void GXPLY_wrap_add_polygon_ex(GXPLYPtr self, GXVVPtr arg1, GXVVPtr arg2, int32_t arg3)
{
    self->add_polygon_ex(arg1, arg2, arg3);
}
inline void GXPLY_wrap_change_ipj(GXPLYPtr self, GXIPJPtr arg1)
{
    self->change_ipj(arg1);
}
inline void GXPLY_wrap_clear(GXPLYPtr self)
{
    self->clear();
}
inline void GXPLY_wrap_copy(GXPLYPtr self, GXPLYPtr arg1)
{
    self->copy(arg1);
}
inline GXPLYPtr GXPLY_wrap_create()
{
    GXPLYPtr ret = GXPLY::create();
    return ret;
}
inline GXPLYPtr GXPLY_wrap_create_s(GXBFPtr arg1)
{
    GXPLYPtr ret = GXPLY::create_s(arg1);
    return ret;
}
inline void GXPLY_wrap_extent(GXPLYPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4)
{
    self->extent(arg1, arg2, arg3, arg4);
}
inline void GXPLY_wrap_get_ipj(GXPLYPtr self, GXIPJPtr arg1)
{
    self->get_ipj(arg1);
}
inline void GXPLY_wrap_get_polygon(GXPLYPtr self, GXVVPtr arg1, GXVVPtr arg2, int32_t arg3)
{
    self->get_polygon(arg1, arg2, arg3);
}
inline void GXPLY_wrap_get_polygon_ex(GXPLYPtr self, GXVVPtr arg1, GXVVPtr arg2, int32_t arg3, int_ref& arg4)
{
    self->get_polygon_ex(arg1, arg2, arg3, arg4);
}
inline int32_t GXPLY_wrap_clip_area(GXPLYPtr self, double arg1, double arg2, double arg3, double arg4)
{
    PLY_CLIP ret = self->clip_area(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXPLY_wrap_clip_line_int(GXPLYPtr self, double arg1, double arg2, double arg3, double arg4, GXVVPtr arg5, double arg6, int_ref& arg7)
{
    int32_t ret = self->clip_line_int(arg1, arg2, arg3, arg4, arg5, arg6, (PLY_LINE_CLIP&)arg7);
    return ret;
}
inline int32_t GXPLY_wrap_clip_ply(GXPLYPtr self, GXPLYPtr arg1, GXPLYPtr arg2)
{
    PLY_CLIP ret = self->clip_ply(arg1, arg2);
    return ret;
}
inline void GXPLY_wrap_get_description(GXPLYPtr self, str_ref& arg1)
{
    self->get_description(arg1);
}
inline int32_t GXPLY_wrap_num_poly(GXPLYPtr self)
{
    int32_t ret = self->num_poly();
    return ret;
}
inline void GXPLY_wrap_load_table(GXPLYPtr self, const gx_string_type& arg1)
{
    self->load_table(arg1);
}
inline double GXPLY_wrap_area(GXPLYPtr self)
{
    double ret = self->area();
    return ret;
}
inline void GXPLY_wrap_rectangle(GXPLYPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->rectangle(arg1, arg2, arg3, arg4);
}
inline void GXPLY_wrap_rotate(GXPLYPtr self, double arg1, double arg2, double arg3)
{
    self->rotate(arg1, arg2, arg3);
}
inline void GXPLY_wrap_save_table(GXPLYPtr self, const gx_string_type& arg1)
{
    self->save_table(arg1);
}
inline void GXPLY_wrap_serial(GXPLYPtr self, GXBFPtr arg1)
{
    self->serial(arg1);
}
inline void GXPLY_wrap_set_description(GXPLYPtr self, const gx_string_type& arg1)
{
    self->set_description(arg1);
}
inline void GXPLY_wrap_set_ipj(GXPLYPtr self, GXIPJPtr arg1)
{
    self->set_ipj(arg1);
}
inline void GXPLY_wrap_thin(GXPLYPtr self, double arg1)
{
    self->thin(arg1);
}

void gxPythonImportGXPLY()
{

    class_<GXPLY, GXPLYPtr> pyClass("GXPLY",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		The PLY object contains the definitions for one or more\n"
                                    "   		polygons, and does import and export of polygon files.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXPLY::null, "null() -> GXPLY\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXPLY`\n\n:returns: A null :class:`geosoft.gxapi.GXPLY`\n:rtype: :class:`geosoft.gxapi.GXPLY`\n").staticmethod("null");
    pyClass.def("is_null", &GXPLY::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXPLY is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXPLY`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXPLY::_internal_handle);
    pyClass.def("add_polygon", &GXPLY_wrap_add_polygon,
                "add_polygon((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a polygon to the polygon file.\n\n"

                ":param arg1: X VV.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV.\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("add_polygon_ex", &GXPLY_wrap_add_polygon_ex,
                "add_polygon_ex((GXVV)arg1, (GXVV)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a polygon to the polygon file.\n\n"

                ":param arg1: X VV.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV.\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: bExclude\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("change_ipj", &GXPLY_wrap_change_ipj,
                "change_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the projection.\n\n"

                ":param arg1: IPJ to place in the PLY\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The PLY is re-projected to the new projection.\n\n"
               );
    pyClass.def("clear", &GXPLY_wrap_clear,
                "clear() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clear/remove all polygons from the PLY.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               );
    pyClass.def("copy", &GXPLY_wrap_copy,
                "copy((GXPLY)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Destroys a PLY Object\n\n"

                ":param arg1: source\n"
                ":type arg1: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create", &GXPLY_wrap_create,
                "create() -> GXPLY:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a Polygon Object.\n\n"

                ":returns: PLY Handle\n"
                ":rtype: :class:`geosoft.gxapi.GXPLY`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_s", &GXPLY_wrap_create_s,
                "create_s((GXBF)arg1) -> GXPLY:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an PLY Object from a BF\n\n"

                ":param arg1: BF to serialize from\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: PLY Handle\n"
                ":rtype: :class:`geosoft.gxapi.GXPLY`\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               ).staticmethod("create_s");
    pyClass.def("extent", &GXPLY_wrap_extent,
                "extent((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the extent of the current polygon.\n\n"

                ":param arg1: Min X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Min Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Max X\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Max Y\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If there are no polygons in the PLY object, returns dummies.\n\n"
               );
    pyClass.def("get_ipj", &GXPLY_wrap_get_ipj,
                "get_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the projection.\n\n"

                ":param arg1: IPJ in which to place the PLY projection\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"
               );
    pyClass.def("get_polygon", &GXPLY_wrap_get_polygon,
                "get_polygon((GXVV)arg1, (GXVV)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a polygon from the PLY\n\n"

                ":param arg1: X VV.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV.\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: polygon number\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_polygon_ex", &GXPLY_wrap_get_polygon_ex,
                "get_polygon_ex((GXVV)arg1, (GXVV)arg2, (int)arg3, (int_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a polygon from the PLY\n\n"

                ":param arg1: X VV.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV.\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: polygon number\n"
                ":type arg3: int\n"
                ":param arg4: TRUE if exclusion polygon\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("clip_area", &GXPLY_wrap_clip_area,
                "clip_area((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Clip a polygon to an area\n\n"

                ":param arg1: min X\n"
                ":type arg1: float\n"
                ":param arg2: min Y\n"
                ":type arg2: float\n"
                ":param arg3: max X\n"
                ":type arg3: float\n"
                ":param arg4: max y\n"
                ":type arg4: float\n"
                ":returns: \\ :ref:`PLY_CLIP`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );
    pyClass.def("clip_line_int", &GXPLY_wrap_clip_line_int,
                "clip_line_int((float)arg1, (float)arg2, (float)arg3, (float)arg4, (GXVV)arg5, (float)arg6, (int_ref)arg7) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Clips a line in or out of the polygons for intersections (GS_DOUBLE).\n"
                "   					Intersections are returned as fiducials down the line stored in VV\n"
                "   					starting at the first point of the line.\n"
                "   					Examples:\n"
                "   					No intersection: PLY_LINE_CLIP_OUTSIDE, 0 intersections\n"
                "   					Starts outside, ends inside: PLY_LINE_CLIP_OUTSIDE, 1 intersection\n"
                "   					Starts outside, intersects then ends inside or outside: PLY_LINE_CLIP_OUTSIDE, 2 intersections\n"
                "   					Starts inside, ends inside : PLY_LINE_CLIP_INSIDE, 1 intersection (gives end-of-line)\n"
                "   					Starts inside, ends outside : PLY_LINE_CLIP_INSIDE, 1 intersection\n"
                "   				\n\n"

                ":param arg1: min X of line to clip\n"
                ":type arg1: float\n"
                ":param arg2: min Y of line to clip\n"
                ":type arg2: float\n"
                ":param arg3: max X of line to clip\n"
                ":type arg3: float\n"
                ":param arg4: max y of line to clip\n"
                ":type arg4: float\n"
                ":param arg5: DOUBLE VV holding intersection fids\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: data element increment (precision)\n"
                ":type arg6: float\n"
                ":param arg7: First point value (\\ :ref:`PLY_LINE_CLIP`\\  value)\n"
                ":type arg7: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0, Terminates on error (you can ignore this value)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("clip_ply", &GXPLY_wrap_clip_ply,
                "clip_ply((GXPLY)arg1, (GXPLY)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Clip one polygon against another\n\n"

                ":param arg1: polygon B\n"
                ":type arg1: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg2: resulting clipped region\n"
                ":type arg2: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: \\ :ref:`PLY_CLIP`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Resulting clipped polygon only has inclusive\n"
                "   					regions of the clipped area.  Exclusion polygons\n"
                "   					are treated as included areas.\n"
                "   				\n\n"
               );
    pyClass.def("get_description", &GXPLY_wrap_get_description,
                "get_description((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the PLY description string\n\n"

                ":param arg1: polygon description\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("num_poly", &GXPLY_wrap_num_poly,
                "num_poly() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of polygons.\n\n"

                ":returns: number of polygons in the PLY.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("load_table", &GXPLY_wrap_load_table,
                "load_table((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads Polygons from a Polygon file.\n\n"

                ":param arg1: Name of the polygon file File contains coordinates of one or more polygons\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("area", &GXPLY_wrap_area,
                "area() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute the Area of a polygon\n\n"

                ":returns: Area of a polygon\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Excluded polygons have negative area.\n\n"
               );
    pyClass.def("rectangle", &GXPLY_wrap_rectangle,
                "rectangle((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a polygon from a rectangular area.\n\n"

                ":param arg1: Min X\n"
                ":type arg1: float\n"
                ":param arg2: Min Y\n"
                ":type arg2: float\n"
                ":param arg3: Max X\n"
                ":type arg3: float\n"
                ":param arg4: Max Y\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"
               );
    pyClass.def("rotate", &GXPLY_wrap_rotate,
                "rotate((float)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Rotate a polygon about a point.\n\n"

                ":param arg1: Rotation point, X\n"
                ":type arg1: float\n"
                ":param arg2: Rotation point, Y\n"
                ":type arg2: float\n"
                ":param arg3: Rotation angle, CCW in degrees\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("save_table", &GXPLY_wrap_save_table,
                "save_table((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save Polygons to a Polygon file.\n\n"

                ":param arg1: Name of the polygon file\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("serial", &GXPLY_wrap_serial,
                "serial((GXBF)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Serialize an PLY to a BF\n\n"

                ":param arg1: BF to serialize to\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("set_description", &GXPLY_wrap_set_description,
                "set_description((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the PLY description string\n\n"

                ":param arg1: polygon description\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("set_ipj", &GXPLY_wrap_set_ipj,
                "set_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the projection.\n\n"

                ":param arg1: IPJ to place in the PLY\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This changes the projection information only.\n\n"
               );
    pyClass.def("thin", &GXPLY_wrap_thin,
                "thin((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Thin polygons to a desired resolution\n\n"

                ":param arg1: thining resolution\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Points on the polygon that deviate from a line drawn between\n"
                "   					neighboring points by more than the thining resolution will\n"
                "   					be removed.\n"
                "   				\n\n"
               );

    scope().attr("PLY_CLIP_NO_INTERSECT") = (int32_t)0;
    scope().attr("PLY_CLIP_INTERSECT") = (int32_t)1;
    scope().attr("PLY_CLIP_A_IN_B") = (int32_t)2;
    scope().attr("PLY_CLIP_B_IN_A") = (int32_t)3;
    scope().attr("PLY_LINE_CLIP_INSIDE") = (int32_t)0;
    scope().attr("PLY_LINE_CLIP_NO_INTERSECT") = (int32_t)0;
    scope().attr("PLY_LINE_CLIP_OUTSIDE") = (int32_t)1;
    scope().attr("PLY_LINE_CLIP_ERROR") = (int32_t)2;

}
