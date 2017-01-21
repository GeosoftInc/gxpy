#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXTIN_wrap_copy(GXTINPtr self, GXTINPtr arg1)
{
    self->copy(arg1);
}
inline GXTINPtr GXTIN_wrap_create(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    GXTINPtr ret = GXTIN::create(arg1, arg2, arg3);
    return ret;
}
inline GXTINPtr GXTIN_wrap_create_s(GXBFPtr arg1)
{
    GXTINPtr ret = GXTIN::create_s(arg1);
    return ret;
}
inline void GXTIN_wrap_export_xml(const gx_string_type& arg1, int_ref& arg2, const gx_string_type& arg3)
{
    GXTIN::export_xml(arg1, arg2, arg3);
}
inline void GXTIN_wrap_get_convex_hull(GXTINPtr self, GXPLYPtr arg1)
{
    self->get_convex_hull(arg1);
}
inline void GXTIN_wrap_get_ipj(GXTINPtr self, GXIPJPtr arg1)
{
    self->get_ipj(arg1);
}
inline void GXTIN_wrap_get_joins(GXTINPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->get_joins(arg1, arg2, arg3);
}
inline void GXTIN_wrap_get_mesh(GXTINPtr self, GXVVPtr arg1)
{
    self->get_mesh(arg1);
}
inline void GXTIN_wrap_get_nodes(GXTINPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->get_nodes(arg1, arg2, arg3);
}
inline void GXTIN_wrap_get_triangles(GXTINPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->get_triangles(arg1, arg2, arg3);
}
inline void GXTIN_wrap_get_triangle(GXTINPtr self, int32_t arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7)
{
    self->get_triangle(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXTIN_wrap_get_voronoi_edges(GXTINPtr self, GXVVPtr arg1)
{
    self->get_voronoi_edges(arg1);
}
inline int32_t GXTIN_wrap_is_z_valued(GXTINPtr self)
{
    int32_t ret = self->is_z_valued();
    return ret;
}
inline int32_t GXTIN_wrap_locate_triangle(GXTINPtr self, int32_t arg1, double arg2, double arg3)
{
    int32_t ret = self->locate_triangle(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXTIN_wrap_nodes(GXTINPtr self)
{
    int32_t ret = self->nodes();
    return ret;
}
inline void GXTIN_wrap_interp_vv(GXTINPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->interp_vv(arg1, arg2, arg3);
}
inline int32_t GXTIN_wrap_triangles(GXTINPtr self)
{
    int32_t ret = self->triangles();
    return ret;
}
inline void GXTIN_wrap_linear_interp_vv(GXTINPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->linear_interp_vv(arg1, arg2, arg3);
}
inline void GXTIN_wrap_nearest_vv(GXTINPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->nearest_vv(arg1, arg2, arg3);
}
inline void GXTIN_wrap_range_xy(GXTINPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4)
{
    self->range_xy(arg1, arg2, arg3, arg4);
}
inline void GXTIN_wrap_serial(GXTINPtr self, GXBFPtr arg1)
{
    self->serial(arg1);
}
inline void GXTIN_wrap_set_ipj(GXTINPtr self, GXIPJPtr arg1)
{
    self->set_ipj(arg1);
}

void gxPythonImportGXTIN()
{

    class_<GXTIN, GXTINPtr> pyClass("GXTIN",
                                    "\n.. parsed-literal::\n\n"
                                    "   The TIN class calculates the Delaunay triangulation of the\n"
                                    "   positions in a database. This is the \"best\" set of triangles\n"
                                    "   that can be formed from irregularly distributed points. The\n"
                                    "   serialized TIN files can be used for gridding using the\n"
                                    "   Tin-based Nearest Neighbour Algorithm, or for plotting the\n"
                                    "   Delaunay triangles or Voronoi cells to a map.\n\n"
                                    , no_init);

    pyClass.def("null", &GXTIN::null, "null() -> GXTIN\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXTIN`\n\n:returns: A null :class:`geosoft.gxapi.GXTIN`\n:rtype: :class:`geosoft.gxapi.GXTIN`\n").staticmethod("null");
    pyClass.def("is_null", &GXTIN::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXTIN is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXTIN`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXTIN::_internal_handle);
    pyClass.def("copy", &GXTIN_wrap_copy,
                "copy((GXTIN)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy TIN\n\n"

                ":param arg1: source TIN\n"
                ":type arg1: :class:`geosoft.gxapi.GXTIN`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create", &GXTIN_wrap_create,
                "create((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> GXTIN:\n"

                "\n.. parsed-literal::\n\n"
                "   This method creates a TIN object.\n\n"

                ":param arg1: X positions\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y positions\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z values (optional)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: TIN Object\n"
                ":rtype: :class:`geosoft.gxapi.GXTIN`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   CreateTIN does the TIN calculation.\n"
                "   The Z values are not required, and a 0-length VV can be used to indicate\n"
                "   the values are not to be used.\n\n"
               ).staticmethod("create");
    pyClass.def("create_s", &GXTIN_wrap_create_s,
                "create_s((GXBF)arg1) -> GXTIN:\n"

                "\n.. parsed-literal::\n\n"
                "   Create TIN from a serialized source\n\n"

                ":param arg1: BF from which to read TIN\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: TIN Object\n"
                ":rtype: :class:`geosoft.gxapi.GXTIN`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_s");
    pyClass.def("export_xml", &GXTIN_wrap_export_xml,
                "export_xml((str)arg1, (int_ref)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a TIN object as XML\n\n"

                ":param arg1: TIN file\n"
                ":type arg1: str\n"
                ":param arg2: CRC returned (Currently this is not implemented)\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Output XML file\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               ).staticmethod("export_xml");
    pyClass.def("get_convex_hull", &GXTIN_wrap_get_convex_hull,
                "get_convex_hull((GXPLY)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the convex hull of the TIN.\n\n"

                ":param arg1: PLY object\n"
                ":type arg1: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The convex hull is the outside boundary of the\n"
                "   triangulated region.\n\n"
               );
    pyClass.def("get_ipj", &GXTIN_wrap_get_ipj,
                "get_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the projection.\n\n"

                ":param arg1: IPJ in which to place the TIN projection\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.3\n\n"
               );
    pyClass.def("get_joins", &GXTIN_wrap_get_joins,
                "get_joins((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get joins from a TIN mesh.\n\n"

                ":param arg1: Joins VV (adjacent nodes)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Index VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Number VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The join information is returned in three VVs.\n"
                "   - The joins VV is a list off the adjacent nodes for\n"
                "     each node, arranged for 1st node, 2nd node etc.\n"
                "   - The index VV gives the starting index in the\n"
                "     joins VV for the adjacent nodes to each node.\n"
                "   - The number VV gives the number of adjacent nodes\n"
                "     for each node.\n"
                "   All VVs must be type GS_LONG.\n\n"
               );
    pyClass.def("get_mesh", &GXTIN_wrap_get_mesh,
                "get_mesh((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get lines from a TIN mesh.\n\n"

                ":param arg1: VV of type GS_D2LINE (returned)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_nodes", &GXTIN_wrap_get_nodes,
                "get_nodes((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the X,Y locations and Z values of the TIN nodes.\n\n"

                ":param arg1: X VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If this is not a Z-valued TIN, the Z values will\n"
                "   be dummies.\n\n"
               );
    pyClass.def("get_triangles", &GXTIN_wrap_get_triangles,
                "get_triangles((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the triangle nodes.\n\n"

                ":param arg1: Node 1 VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Node 2 VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Node3 VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_triangle", &GXTIN_wrap_get_triangle,
                "get_triangle((int)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the locations of the vertices of a specific triangle\n\n"

                ":param arg1: triangle index [0...N-1]\n"
                ":type arg1: int\n"
                ":param arg2: X0\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y0\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: X1\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Y1\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: X2\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Y2\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_voronoi_edges", &GXTIN_wrap_get_voronoi_edges,
                "get_voronoi_edges((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get line segments defining Voronoi cells.\n\n"

                ":param arg1: VV of GS_D2LINE type (create with type -32)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("is_z_valued", &GXTIN_wrap_is_z_valued,
                "is_z_valued() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Does the TIN contain Z values with each X,Y?\n\n"

                ":returns: Returns ``True`` if Z values are defined in the TIN\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("locate_triangle", &GXTIN_wrap_locate_triangle,
                "locate_triangle((int)arg1, (float)arg2, (float)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the index of the triangle containing X, Y.\n\n"

                ":param arg1: seed triangle (can be iDummy or <0)\n"
                ":type arg1: int\n"
                ":param arg2: target X location\n"
                ":type arg2: float\n"
                ":param arg3: target Y location\n"
                ":type arg3: float\n"
                ":returns: The index of the triangle containing X, Y.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Index returned begins at 0, but could be negative.\n"
                "   -1 If X,Y is not contained in a triangle (or triangle not found)\n"
                "   -2 If the location is on an edge\n"
                "      This is for \"fall-back\" purposes only.\n"
                "   	Frequently edge positions are located as being part of\n"
                "      a triangle, so do not rely on this result to determine\n"
                "      if a node position is on an edge.\n"
                "   -3 If the location is a vertex.\n"
                "      This is for \"fall-back\" purposes only in the code.\n"
                "      Normal operation is to include a node position\n"
                "      inside a triangle, so do not rely on this result to determine\n"
                "      if a node position is input.		  \n"
                "   		  \n\n"
               );
    pyClass.def("nodes", &GXTIN_wrap_nodes,
                "nodes() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the number of nodes in the TIN\n\n"

                ":returns: The number of nodes in the TIN\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("interp_vv", &GXTIN_wrap_interp_vv,
                "interp_vv((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Interp TINned values using the natural neighbour method.\n\n"

                ":param arg1: VV X locations to interpolate (GS_DOUBLE)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV Y locations to interpolate (GS_DOUBLE)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: VV Interpolated Z values (GS_DOUBLE)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The TIN have been created using max length = rDUMMY to\n"
                "   ensure that the TIN has a convex hull (otherwise the\n"
                "   routine that locates the triangle for a given location may fail).\n"
                "   The TIN must also have been created using the Z values.\n"
                "   Values located outside the convex hull are set to rDUMMY.\n"
                "   The method is based on the following paper:\n"
                "   \n"
                "   Sambridge, M., Braun, J., and McQueen, H., 1995,\n"
                "   Geophysical parameterization and interpolation of irregular\n"
                "   data using natural neighbours:\n"
                "   Geophysical Journal International, 122 p. 837-857.\n\n"
               );
    pyClass.def("triangles", &GXTIN_wrap_triangles,
                "triangles() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the number of triangles in the TIN.\n\n"

                ":returns: The number of triangles in the TIN\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("linear_interp_vv", &GXTIN_wrap_linear_interp_vv,
                "linear_interp_vv((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Interp TINned values using the linear interpolation\n\n"

                ":param arg1: VV X locations to interpolate (GS_DOUBLE)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV Y locations to interpolate (GS_DOUBLE)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: VV Interpolated Z values (GS_DOUBLE)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The TIN have been created using max length = rDUMMY to\n"
                "   ensure that the TIN has a convex hull (otherwise the\n"
                "   routine that locates the triangle for a given location may fail).\n"
                "   The TIN must also have been created using the Z values.\n"
                "   Values located outside the convex hull are set to rDUMMY.\n"
                "   \n"
                "   The values are set assuming that each TIN triangle defines a\n"
                "   plane.\n\n"
               );
    pyClass.def("nearest_vv", &GXTIN_wrap_nearest_vv,
                "nearest_vv((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Interp TINned values using the nearest neighbour.\n\n"

                ":param arg1: VV X locations to interpolate (GS_DOUBLE)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV Y locations to interpolate (GS_DOUBLE)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: VV Interpolated Z values (GS_DOUBLE)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The TIN have been created using max length = rDUMMY to\n"
                "   ensure that the TIN has a convex hull (otherwise the\n"
                "   routine that locates the triangle for a given location may fail).\n"
                "   The TIN must also have been created using the Z values.\n"
                "   Values located outside the convex hull are set to rDUMMY.\n"
                "   \n"
                "   Within each voronoi triangle, the Z value of node closest to the input\n"
                "   X,Y location is returned.\n\n"
               );
    pyClass.def("range_xy", &GXTIN_wrap_range_xy,
                "range_xy((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the range in X and Y of the TINned region.\n\n"

                ":param arg1: Min X  (returned)\n"
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
                "   The TINned range is the range of X and Y covered by\n"
                "   the TIN triangles. It can thus be less than the full\n"
                "   X and Y range of the nodes themselves, if a full\n"
                "   convex hull is not calculated.\n\n"
               );
    pyClass.def("serial", &GXTIN_wrap_serial,
                "serial((GXBF)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Serialize TIN\n\n"

                ":param arg1: BF in which to write TIN\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_ipj", &GXTIN_wrap_set_ipj,
                "set_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the projection.\n\n"

                ":param arg1: IPJ to place in the TIN\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.3\n\n"
               );


}
