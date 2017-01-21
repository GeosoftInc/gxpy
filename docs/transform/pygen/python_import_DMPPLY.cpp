#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXDMPPLY_wrap_clear(GXDMPPLYPtr self)
{
    self->clear();
}
inline void GXDMPPLY_wrap_copy(GXDMPPLYPtr self, GXDMPPLYPtr arg1)
{
    self->copy(arg1);
}
inline GXDMPPLYPtr GXDMPPLY_wrap_create()
{
    GXDMPPLYPtr ret = GXDMPPLY::create();
    return ret;
}
inline void GXDMPPLY_wrap_get_azimuth(GXDMPPLYPtr self, int32_t arg1, float_ref& arg2)
{
    self->get_azimuth(arg1, arg2);
}
inline void GXDMPPLY_wrap_get_extents(GXDMPPLYPtr self, int32_t arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    self->get_extents(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXDMPPLY_wrap_get_joins(GXDMPPLYPtr self, int32_t arg1, GXVVPtr arg2)
{
    self->get_joins(arg1, arg2);
}
inline void GXDMPPLY_wrap_get_normal_vectors(GXDMPPLYPtr self, int32_t arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9, float_ref& arg10)
{
    self->get_normal_vectors(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXDMPPLY_wrap_get_poly(GXDMPPLYPtr self, int32_t arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4)
{
    self->get_poly(arg1, arg2, arg3, arg4);
}
inline void GXDMPPLY_wrap_get_swing(GXDMPPLYPtr self, int32_t arg1, float_ref& arg2)
{
    self->get_swing(arg1, arg2);
}
inline void GXDMPPLY_wrap_get_vertex(GXDMPPLYPtr self, int32_t arg1, int32_t arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    self->get_vertex(arg1, arg2, arg3, arg4, arg5);
}
inline int32_t GXDMPPLY_wrap_num_joins(GXDMPPLYPtr self)
{
    int32_t ret = self->num_joins();
    return ret;
}
inline int32_t GXDMPPLY_wrap_num_polys(GXDMPPLYPtr self)
{
    int32_t ret = self->num_polys();
    return ret;
}
inline int32_t GXDMPPLY_wrap_num_vertices(GXDMPPLYPtr self, int32_t arg1)
{
    int32_t ret = self->num_vertices(arg1);
    return ret;
}
inline void GXDMPPLY_wrap_load(GXDMPPLYPtr self, const gx_string_type& arg1)
{
    self->load(arg1);
}
inline void GXDMPPLY_wrap_move_vertex(GXDMPPLYPtr self, int32_t arg1, int32_t arg2, double arg3, double arg4, double arg5)
{
    self->move_vertex(arg1, arg2, arg3, arg4, arg5);
}
inline void GXDMPPLY_wrap_project_poly(GXDMPPLYPtr self, int32_t arg1, double arg2, double arg3, double arg4, double arg5, double arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9)
{
    self->project_poly(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXDMPPLY_wrap_re_project_poly(GXDMPPLYPtr self, int32_t arg1, double arg2, double arg3, double arg4, double arg5, GXVVPtr arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, GXVVPtr arg10)
{
    self->re_project_poly(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXDMPPLY_wrap_save(GXDMPPLYPtr self, const gx_string_type& arg1)
{
    self->save(arg1);
}
inline void GXDMPPLY_wrap_set_poly(GXDMPPLYPtr self, int32_t arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4)
{
    self->set_poly(arg1, arg2, arg3, arg4);
}

void gxPythonImportGXDMPPLY()
{

    class_<GXDMPPLY, GXDMPPLYPtr> pyClass("GXDMPPLY",
                                          "\n.. parsed-literal::\n\n"
                                          "   Datamine Multiple polygon object\n\n"
                                          , no_init);

    pyClass.def("null", &GXDMPPLY::null, "null() -> GXDMPPLY\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXDMPPLY`\n\n:returns: A null :class:`geosoft.gxapi.GXDMPPLY`\n:rtype: :class:`geosoft.gxapi.GXDMPPLY`\n").staticmethod("null");
    pyClass.def("is_null", &GXDMPPLY::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXDMPPLY is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXDMPPLY`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXDMPPLY::_internal_handle);
    pyClass.def("clear", &GXDMPPLY_wrap_clear,
                "clear() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clear/remove all polygons from the DMPPLY.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("copy", &GXDMPPLY_wrap_copy,
                "copy((GXDMPPLY)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy\n\n"

                ":param arg1: source\n"
                ":type arg1: :class:`geosoft.gxapi.GXDMPPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("create", &GXDMPPLY_wrap_create,
                "create() -> GXDMPPLY:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a DMPPLY object.\n\n"

                ":returns: DMPLY Object\n"
                ":rtype: :class:`geosoft.gxapi.GXDMPPLY`\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("get_azimuth", &GXDMPPLY_wrap_get_azimuth,
                "get_azimuth((int)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the azimuth of a given polygon.\n\n"

                ":param arg1: polygon number (1 to NP)\n"
                ":type arg1: int\n"
                ":param arg2: Azimuth (degrees) (o)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The azimuth is the equivalent section azimuth,\n"
                "   equal to the azimuth of the normal vector plus\n"
                "   90 degrees.\n\n"
               );
    pyClass.def("get_extents", &GXDMPPLY_wrap_get_extents,
                "get_extents((int)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the center, width and height of a given polygon.\n\n"

                ":param arg1: polygon number (1 to NP)\n"
                ":type arg1: int\n"
                ":param arg2: Center point X (o)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Center point Y (o)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Center point Z (o)\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Width of polygon (in its plane) (o)\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Height of polygon (Z extent) (o)\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("get_joins", &GXDMPPLY_wrap_get_joins,
                "get_joins((int)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get join lines for each vertex in a specific polygon.\n\n"

                ":param arg1: polygon number (1 to N)\n"
                ":type arg1: int\n"
                ":param arg2: INT VV of join indices (1 to NJoins).\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If a specific vertex is not joined, the returned value is 0.\n"
                "   If the vertex is joined, then the index of the join line (1 to NJoins)\n"
                "   is returned.\n\n"
               );
    pyClass.def("get_normal_vectors", &GXDMPPLY_wrap_get_normal_vectors,
                "get_normal_vectors((int)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9, (float_ref)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the normal vectors of a given polygon.\n\n"

                ":param arg1: polygon number (1 to NP)\n"
                ":type arg1: int\n"
                ":param arg2: X component (o) (Horizontal azimuth vector)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y component (o)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Z component (o)\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: X component (o) (Down-dip, in the vertical plane)\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Y component (o)\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Z component (o)\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: X component (o) (Normal vector)\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Y component (o)\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: Z component (o)\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Three normalized vectors are returned.\n"
                "   The first is horizontal, in the plane of the polygon.\n"
                "   The second is in the vertical plane, corresponding to the\n"
                "   \"down-dip\" direction.\n"
                "   The third is the normal vector to the polygon plane.\n\n"
               );
    pyClass.def("get_poly", &GXDMPPLY_wrap_get_poly,
                "get_poly((int)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a specific polygon from a DMPPLY object.\n\n"

                ":param arg1: polygon number (1 to NP) (i)\n"
                ":type arg1: int\n"
                ":param arg2: X Locations (o)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y Locations (o)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Z Locations (o)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of points from the VV length.\n\n"
               );
    pyClass.def("get_swing", &GXDMPPLY_wrap_get_swing,
                "get_swing((int)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the swing of a given polygon.\n\n"

                ":param arg1: polygon number (1 to NP)\n"
                ":type arg1: int\n"
                ":param arg2: Swing (degrees) (o)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The swing is the equivalent section swing,\n"
                "   equal to zero for vertical plates, and increasing\n"
                "   as the normal vector goes from horizontal upward.\n\n"
               );
    pyClass.def("get_vertex", &GXDMPPLY_wrap_get_vertex,
                "get_vertex((int)arg1, (int)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a vertex location from a DMPPLY object.\n\n"

                ":param arg1: polygon number (1 to NP)\n"
                ":type arg1: int\n"
                ":param arg2: vertex number (1 to NV)\n"
                ":type arg2: int\n"
                ":param arg3: X Location (o)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Y Location (o)\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Z Location (o)\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("num_joins", &GXDMPPLY_wrap_num_joins,
                "num_joins() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of joining lines in a DMPPLY object.\n\n"

                ":returns: Number of joining lines\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("num_polys", &GXDMPPLY_wrap_num_polys,
                "num_polys() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of polygons in a DMPPLY object.\n\n"

                ":returns: Number of polygons\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The value returned is the \"NP\" used in function descriptions\n"
                "   below.\n\n"
               );
    pyClass.def("num_vertices", &GXDMPPLY_wrap_num_vertices,
                "num_vertices((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of vertices in a polygon.\n\n"

                ":param arg1: polygon number (1 to NP)\n"
                ":type arg1: int\n"
                ":returns: Number of vertices in a polygon\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The value returned is the \"NV\" used in function descriptions\n"
                "   below.\n\n"
               );
    pyClass.def("load", &GXDMPPLY_wrap_load,
                "load((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads a Datamine polygon file.\n\n"

                ":param arg1: Name of the file to load\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("move_vertex", &GXDMPPLY_wrap_move_vertex,
                "move_vertex((int)arg1, (int)arg2, (float)arg3, (float)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Moves a vertex and any associated lines.\n\n"

                ":param arg1: polygon number (1 to NP)\n"
                ":type arg1: int\n"
                ":param arg2: vertex number (1 to NV)\n"
                ":type arg2: int\n"
                ":param arg3: new location X\n"
                ":type arg3: float\n"
                ":param arg4: new location Y\n"
                ":type arg4: float\n"
                ":param arg5: new location Z\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("project_poly", &GXDMPPLY_wrap_project_poly,
                "project_poly((int)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Project a polygon onto a vertical plane.\n\n"

                ":param arg1: polygon number (1 to NP)\n"
                ":type arg1: int\n"
                ":param arg2: X location of plane origin in 3D\n"
                ":type arg2: float\n"
                ":param arg3: Y location of plane origin in 3D\n"
                ":type arg3: float\n"
                ":param arg4: Z location of plane origin in 3D\n"
                ":type arg4: float\n"
                ":param arg5: azimuth of the plane in degrees\n"
                ":type arg5: float\n"
                ":param arg6: swing of the plane in degrees\n"
                ":type arg6: float\n"
                ":param arg7: X (horizontal along-section locations on vertical plane  (o)\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Y (vertical locations on vertical plane  (o)\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Z (horizontal distances perpendicular to the plane  (o)\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Gives the location in plane coordinates of a selected polygon,\n"
                "   after it has been projected perpendicularly onto the plane.\n"
                "   \n"
                "   Plane coodinates: X - horizontal in plane\n"
                "                     Y - \"vertical\" in plane (can be a swing)\n"
                "                     Z - horizontal, \"perpendicular\" to plane (RH)\n\n"
               );
    pyClass.def("re_project_poly", &GXDMPPLY_wrap_re_project_poly,
                "re_project_poly((int)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (GXVV)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (GXVV)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Recover polygon locations from 2D locations on vertical plane.\n\n"

                ":param arg1: polygon number (1 to lNP) (i)\n"
                ":type arg1: int\n"
                ":param arg2: X location of plane origin in 3D (i)\n"
                ":type arg2: float\n"
                ":param arg3: Y location of plane origin in 3D (i)\n"
                ":type arg3: float\n"
                ":param arg4: Z location of plane origin in 3D (i)\n"
                ":type arg4: float\n"
                ":param arg5: azimuth of the plane in degrees (i)\n"
                ":type arg5: float\n"
                ":param arg6: X locations on vertical plane  (i)\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Y (actually Z) locations on vertical plane  (i)\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: X Locations of polygon (o)\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Y Locations of polygon (o)\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Z Locations of polygon (o)\n"
                ":type arg10: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This is the inverse operation of \\ :func:`geosoft.gxapi.GXDMPPLY.project_poly`\\ .\n"
                "   \n"
                "   Input the 2D locations on the projected vertical plane. These locations\n"
                "   are projected back onto the original polygon plane.\n\n"
               );
    pyClass.def("save", &GXDMPPLY_wrap_save,
                "save((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save to a Datamine polygon file\n\n"

                ":param arg1: Name of the file to save to\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("set_poly", &GXDMPPLY_wrap_set_poly,
                "set_poly((int)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a specific polygon into a DMPPLY object.\n\n"

                ":param arg1: polygon number (1 to NP) (i)\n"
                ":type arg1: int\n"
                ":param arg2: X Locations (i)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y Locations (i)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Z Locations (i)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of points from the VV length.\n\n"
               );


}
