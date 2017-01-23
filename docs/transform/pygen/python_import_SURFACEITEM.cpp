#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXSURFACEITEMPtr GXSURFACEITEM_wrap_create(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSURFACEITEMPtr ret = GXSURFACEITEM::create(arg1, arg2);
    return ret;
}
inline void GXSURFACEITEM_wrap_get_guid(GXSURFACEITEMPtr self, str_ref& arg1)
{
    self->get_guid(arg1);
}
inline void GXSURFACEITEM_wrap_set_properties(GXSURFACEITEMPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, double arg5, const gx_string_type& arg6, const gx_string_type& arg7, double arg8)
{
    self->set_properties(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXSURFACEITEM_wrap_set_properties_ex(GXSURFACEITEMPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, double arg5, const gx_string_type& arg6, const gx_string_type& arg7, int32_t arg8, double arg9, double arg10)
{
    self->set_properties_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXSURFACEITEM_wrap_get_properties(GXSURFACEITEMPtr self, str_ref& arg1, str_ref& arg2, str_ref& arg3, str_ref& arg4, float_ref& arg5, str_ref& arg6, str_ref& arg7, float_ref& arg8)
{
    self->get_properties(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXSURFACEITEM_wrap_get_properties_ex(GXSURFACEITEMPtr self, str_ref& arg1, str_ref& arg2, str_ref& arg3, str_ref& arg4, float_ref& arg5, str_ref& arg6, str_ref& arg7, int_ref& arg8, float_ref& arg9, float_ref& arg10)
{
    self->get_properties_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXSURFACEITEM_wrap_set_default_render_properties(GXSURFACEITEMPtr self, int32_t arg1, double arg2, int32_t arg3)
{
    self->set_default_render_properties(arg1, arg2, (SURFACERENDER_MODE)arg3);
}
inline void GXSURFACEITEM_wrap_get_default_render_properties(GXSURFACEITEMPtr self, int_ref& arg1, float_ref& arg2, int_ref& arg3)
{
    self->get_default_render_properties(arg1, arg2, (SURFACERENDER_MODE&)arg3);
}
inline int32_t GXSURFACEITEM_wrap_num_components(GXSURFACEITEMPtr self)
{
    int32_t ret = self->num_components();
    return ret;
}
inline int32_t GXSURFACEITEM_wrap_add_mesh(GXSURFACEITEMPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6)
{
    int32_t ret = self->add_mesh(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline void GXSURFACEITEM_wrap_get_mesh(GXSURFACEITEMPtr self, int32_t arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7)
{
    self->get_mesh(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXSURFACEITEM_wrap_get_extents(GXSURFACEITEMPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    self->get_extents(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXSURFACEITEM_wrap_get_mesh_info(GXSURFACEITEMPtr self, int32_t arg1, bool_ref& arg2, int_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    self->get_mesh_info(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXSURFACEITEM_wrap_get_info(GXSURFACEITEMPtr self, bool_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4)
{
    self->get_info(arg1, arg2, arg3, arg4);
}
inline void GXSURFACEITEM_wrap_get_geometry_info(GXSURFACEITEMPtr self, int_ref& arg1, int_ref& arg2)
{
    self->get_geometry_info(arg1, arg2);
}
inline void GXSURFACEITEM_wrap_compute_extended_info(GXSURFACEITEMPtr self, int_ref& arg1, int_ref& arg2, int_ref& arg3, int_ref& arg4, int_ref& arg5, int_ref& arg6, int_ref& arg7)
{
    self->compute_extended_info(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}

void gxPythonImportGXSURFACEITEM()
{

    class_<GXSURFACEITEM, GXSURFACEITEMPtr> pyClass("GXSURFACEITEM",
            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		The SURFACEITEM allows you to create, read and alter Geosurface files (\\ `*`\\ .geosoft_surface).\n"
            "   		A Geosurface file can contain one or more surface items (see SURFACE class). A surface item can\n"
            "   		contains one or more triangular polyhedral meshes.\n"
            "   	\n\n"
            , no_init);

    pyClass.def("null", &GXSURFACEITEM::null, "null() -> GXSURFACEITEM\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXSURFACEITEM`\n\n:returns: A null :class:`geosoft.gxapi.GXSURFACEITEM`\n:rtype: :class:`geosoft.gxapi.GXSURFACEITEM`\n").staticmethod("null");
    pyClass.def("is_null", &GXSURFACEITEM::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXSURFACEITEM is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXSURFACEITEM`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXSURFACEITEM::_internal_handle);
    pyClass.def("create", &GXSURFACEITEM_wrap_create,
                "create((str)arg1, (str)arg2) -> GXSURFACEITEM:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a SURFACEITEM\n\n"

                ":param arg1: Type\n"
                ":type arg1: str\n"
                ":param arg2: Name\n"
                ":type arg2: str\n"
                ":returns: SURFACEITEM Object\n"
                ":rtype: :class:`geosoft.gxapi.GXSURFACEITEM`\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXSURFACEITEM.set_properties`\\  and \\ :func:`geosoft.gxapi.GXSURFACEITEM.set_default_render_properties`\\ \n\n"
               ).staticmethod("create");
    pyClass.def("get_guid", &GXSURFACEITEM_wrap_get_guid,
                "get_guid((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the GUID of the surface item.\n\n"

                ":param arg1: GUID\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The value returned by this call will not be valid for newly created items until after a call to \\ :func:`geosoft.gxapi.GXSURFACE.add_surface_item`\\ .\n\n"
               );
    pyClass.def("set_properties", &GXSURFACEITEM_wrap_set_properties,
                "set_properties((str)arg1, (str)arg2, (str)arg3, (str)arg4, (float)arg5, (str)arg6, (str)arg7, (float)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the properties of the surface item.\n\n"

                ":param arg1: Type\n"
                ":type arg1: str\n"
                ":param arg2: Name\n"
                ":type arg2: str\n"
                ":param arg3: SourceGuid\n"
                ":type arg3: str\n"
                ":param arg4: SourceName\n"
                ":type arg4: str\n"
                ":param arg5: SourceMeasure\n"
                ":type arg5: float\n"
                ":param arg6: SecondarySourceGuid\n"
                ":type arg6: str\n"
                ":param arg7: SecondarySourceName\n"
                ":type arg7: str\n"
                ":param arg8: SecondarySourceMeasure\n"
                ":type arg8: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXSYS.generate_guid`\\ \n\n"
               );
    pyClass.def("set_properties_ex", &GXSURFACEITEM_wrap_set_properties_ex,
                "set_properties_ex((str)arg1, (str)arg2, (str)arg3, (str)arg4, (float)arg5, (str)arg6, (str)arg7, (int)arg8, (float)arg9, (float)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the properties of the surface item (includes new properties introduced in 8.5).\n\n"

                ":param arg1: Type\n"
                ":type arg1: str\n"
                ":param arg2: Name\n"
                ":type arg2: str\n"
                ":param arg3: SourceGuid\n"
                ":type arg3: str\n"
                ":param arg4: SourceName\n"
                ":type arg4: str\n"
                ":param arg5: SourceMeasure\n"
                ":type arg5: float\n"
                ":param arg6: SecondarySourceGuid\n"
                ":type arg6: str\n"
                ":param arg7: SecondarySourceName\n"
                ":type arg7: str\n"
                ":param arg8: SecondarySourceOption\n"
                ":type arg8: int\n"
                ":param arg9: SecondarySourceMeasure\n"
                ":type arg9: float\n"
                ":param arg10: SecondarySourceMeasure2\n"
                ":type arg10: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXSYS.generate_guid`\\ \n\n"
               );
    pyClass.def("get_properties", &GXSURFACEITEM_wrap_get_properties,
                "get_properties((str_ref)arg1, (str_ref)arg2, (str_ref)arg3, (str_ref)arg4, (float_ref)arg5, (str_ref)arg6, (str_ref)arg7, (float_ref)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the properties of the surface item.\n\n"

                ":param arg1: Type\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: Name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: SourceGuid\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: SourceName\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: SourceMeasure\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: SecondarySourceGuid\n"
                ":type arg6: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg7: SecondarySourceName\n"
                ":type arg7: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg8: SecondarySourceMeasure\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_properties_ex", &GXSURFACEITEM_wrap_get_properties_ex,
                "get_properties_ex((str_ref)arg1, (str_ref)arg2, (str_ref)arg3, (str_ref)arg4, (float_ref)arg5, (str_ref)arg6, (str_ref)arg7, (int_ref)arg8, (float_ref)arg9, (float_ref)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the properties of the surface item  (includes new properties introduced in 8.5).\n\n"

                ":param arg1: Type\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: Name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: SourceGuid\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: SourceName\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: SourceMeasure\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: SecondarySourceGuid\n"
                ":type arg6: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg7: SecondarySourceName\n"
                ":type arg7: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg8: SecondarySourceOption\n"
                ":type arg8: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg9: SecondarySourceMeasure\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: SecondarySourceMeasure2\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               );
    pyClass.def("set_default_render_properties", &GXSURFACEITEM_wrap_set_default_render_properties,
                "set_default_render_properties((int)arg1, (float)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets default render properties of the surface item.\n\n"

                ":param arg1: Color\n"
                ":type arg1: int\n"
                ":param arg2: Transparency\n"
                ":type arg2: float\n"
                ":param arg3: \\ :ref:`SURFACERENDER_MODE`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.color`\\ \n\n"
               );
    pyClass.def("get_default_render_properties", &GXSURFACEITEM_wrap_get_default_render_properties,
                "get_default_render_properties((int_ref)arg1, (float_ref)arg2, (int_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets default render properties of the surface item.\n\n"

                ":param arg1: Color\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Transparency\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: \\ :ref:`SURFACERENDER_MODE`\\ \n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMVIEW.color`\\ \n\n"
               );
    pyClass.def("num_components", &GXSURFACEITEM_wrap_num_components,
                "num_components() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of components in the surface item.\n\n"

                ":returns: Number of components in the surface item.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("add_mesh", &GXSURFACEITEM_wrap_add_mesh,
                "add_mesh((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Adds a triangular polyhedral mesh component to the surface item.\n\n"

                ":param arg1: Vertices X location\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Vertices Y location\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Vertices Z location\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Triangles 1st Vertex\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Triangles 2nd Vertex\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Triangles 3rd Vertex\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: The index of the component added.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_mesh", &GXSURFACEITEM_wrap_get_mesh,
                "get_mesh((int)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets a triangular polyhedral mesh of a component in the surface item.\n\n"

                ":param arg1: Index of the component\n"
                ":type arg1: int\n"
                ":param arg2: Vertices X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Vertices Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Vertices Z\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Triangles 1st Vertex\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Triangles 2nd Vertex\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Triangles 3rd Vertex\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_extents", &GXSURFACEITEM_wrap_get_extents,
                "get_extents((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the spatial range of the the surface item.\n\n"

                ":param arg1: Minimum valid data in X.\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Minimum valid data in Y.\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Minimum valid data in Z.\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Maximum valid data in X.\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Maximum valid data in Y.\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Maximum valid data in Z.\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               );
    pyClass.def("get_mesh_info", &GXSURFACEITEM_wrap_get_mesh_info,
                "get_mesh_info((int)arg1, (bool_ref)arg2, (int_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets information about a triangular polyhedral mesh component in the surface item.\n\n"

                ":param arg1: Index of the component\n"
                ":type arg1: int\n"
                ":param arg2: bool indicating if mesh is closed\n"
                ":type arg2: :class:`geosoft.gxapi.bool_ref`\n"
                ":param arg3: number of inner components\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Area\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Volume\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Volume confidence interval\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_info", &GXSURFACEITEM_wrap_get_info,
                "get_info((bool_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets information about the surface item.\n\n"

                ":param arg1: bool indicating if all meshes in item is closed\n"
                ":type arg1: :class:`geosoft.gxapi.bool_ref`\n"
                ":param arg2: Area\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Volume\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Volume confidence interval\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               );
    pyClass.def("get_geometry_info", &GXSURFACEITEM_wrap_get_geometry_info,
                "get_geometry_info((int_ref)arg1, (int_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the total number of vertices and triangles of all mesh components in item.\n\n"

                ":param arg1: Total number of vertices\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Total number of triangles\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               );
    pyClass.def("compute_extended_info", &GXSURFACEITEM_wrap_compute_extended_info,
                "compute_extended_info((int_ref)arg1, (int_ref)arg2, (int_ref)arg3, (int_ref)arg4, (int_ref)arg5, (int_ref)arg6, (int_ref)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute more information (including validation) about of all mesh components in the surface item.\n\n"

                ":param arg1: Number of inner components (recomputed)\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Total number of valid vertices\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Total number of valid edges\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Total number of valid triangles\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: Number of inconsistent triangles\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Number of invalid triangles\n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg7: Number of self intersections\n"
                ":type arg7: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               );

    scope().attr("SURFACERENDER_SMOOTH") = (int32_t)0;
    scope().attr("SURFACERENDER_FILL") = (int32_t)1;
    scope().attr("SURFACERENDER_EDGES") = (int32_t)2;

}
