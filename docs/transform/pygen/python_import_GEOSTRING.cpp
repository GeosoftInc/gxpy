#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXGEOSTRINGPtr GXGEOSTRING_wrap_open(const gx_string_type& arg1, int32_t arg2)
{
    GXGEOSTRINGPtr ret = GXGEOSTRING::open(arg1, (GEOSTRING_OPEN)arg2);
    return ret;
}
inline void GXGEOSTRING_wrap_get_ipj(GXGEOSTRINGPtr self, GXIPJPtr arg1)
{
    self->get_ipj(arg1);
}
inline void GXGEOSTRING_wrap_get_features(GXGEOSTRINGPtr self, GXLSTPtr arg1)
{
    self->get_features(arg1);
}
inline void GXGEOSTRING_wrap_get_sections(GXGEOSTRINGPtr self, GXLSTPtr arg1)
{
    self->get_sections(arg1);
}
inline void GXGEOSTRING_wrap_get_all_shapes(GXGEOSTRINGPtr self, GXLSTPtr arg1)
{
    self->get_all_shapes(arg1);
}
inline void GXGEOSTRING_wrap_get_shapes_for_feature(GXGEOSTRINGPtr self, const gx_string_type& arg1, GXLSTPtr arg2)
{
    self->get_shapes_for_feature(arg1, arg2);
}
inline void GXGEOSTRING_wrap_get_shapes_for_section(GXGEOSTRINGPtr self, const gx_string_type& arg1, GXLSTPtr arg2)
{
    self->get_shapes_for_section(arg1, arg2);
}
inline void GXGEOSTRING_wrap_get_shapes_for_feature_and_section(GXGEOSTRINGPtr self, const gx_string_type& arg1, const gx_string_type& arg2, GXLSTPtr arg3)
{
    self->get_shapes_for_feature_and_section(arg1, arg2, arg3);
}
inline void GXGEOSTRING_wrap_get_feature_properties(GXGEOSTRINGPtr self, const gx_string_type& arg1, str_ref& arg2, str_ref& arg3, bool_ref& arg4, int_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, int_ref& arg9, int_ref& arg10, int_ref& arg11, float_ref& arg12, float_ref& arg13, int_ref& arg14)
{
    self->get_feature_properties(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14);
}
inline void GXGEOSTRING_wrap_get_section_properties(GXGEOSTRINGPtr self, const gx_string_type& arg1, str_ref& arg2, str_ref& arg3, int_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9, float_ref& arg10, float_ref& arg11, float_ref& arg12, float_ref& arg13)
{
    self->get_section_properties(arg1, arg2, arg3, (SECTION_ORIENTATION&)arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13);
}
inline void GXGEOSTRING_wrap_get_shape_properties(GXGEOSTRINGPtr self, const gx_string_type& arg1, str_ref& arg2, str_ref& arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6)
{
    self->get_shape_properties(arg1, arg2, arg3, arg4, arg5, arg6);
}

void gxPythonImportGXGEOSTRING()
{

    class_<GXGEOSTRING, GXGEOSTRINGPtr> pyClass("GXGEOSTRING",
            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		The GEOSTRING class is used to read information stored in Geostring files (\\ `*`\\ .geosoft_string). Geosoft geostrings are 3D vector files that store digitized interpretations drawn on section maps. Both polygon and polyline features can be stored in the same file. This API currently only provides read access, but read/write support could be added in the future.\n"
            "   	\n\n"
            , no_init);

    pyClass.def("null", &GXGEOSTRING::null, "null() -> GXGEOSTRING\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXGEOSTRING`\n\n:returns: A null :class:`geosoft.gxapi.GXGEOSTRING`\n:rtype: :class:`geosoft.gxapi.GXGEOSTRING`\n").staticmethod("null");
    pyClass.def("is_null", &GXGEOSTRING::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXGEOSTRING is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXGEOSTRING`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXGEOSTRING::_internal_handle);
    pyClass.def("open", &GXGEOSTRING_wrap_open,
                "open((str)arg1, (int)arg2) -> GXGEOSTRING:\n"

                "\n.. parsed-literal::\n\n"
                "   Open a Geostring file\n\n"

                ":param arg1: Geostring file name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`GEOSTRING_OPEN`\\ \n"
                ":type arg2: int\n"
                ":returns: GEOSTRING Object\n"
                ":rtype: :class:`geosoft.gxapi.GXGEOSTRING`\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("open");
    pyClass.def("get_ipj", &GXGEOSTRING_wrap_get_ipj,
                "get_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the coordinate system of the Geostring.\n\n"

                ":param arg1: IPJ in which to place the Geostring coordinate system\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_features", &GXGEOSTRING_wrap_get_features,
                "get_features((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the features\n\n"

                ":param arg1: LST to fill\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   List items are returned with feature GUID in name and feature name in value.\n\n"
               );
    pyClass.def("get_sections", &GXGEOSTRING_wrap_get_sections,
                "get_sections((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the sections\n\n"

                ":param arg1: LST to fill\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   List items are returned with section GUID in name and section name in value.\n\n"
               );
    pyClass.def("get_all_shapes", &GXGEOSTRING_wrap_get_all_shapes,
                "get_all_shapes((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the all shapes\n\n"

                ":param arg1: LST to fill\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_shapes_for_feature", &GXGEOSTRING_wrap_get_shapes_for_feature,
                "get_shapes_for_feature((str)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get all shapes linked to a specific feature\n\n"

                ":param arg1: Feature GUID\n"
                ":type arg1: str\n"
                ":param arg2: LST to fill\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_shapes_for_section", &GXGEOSTRING_wrap_get_shapes_for_section,
                "get_shapes_for_section((str)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get all shapes linked to a specific section\n\n"

                ":param arg1: Section GUID\n"
                ":type arg1: str\n"
                ":param arg2: LST to fill\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_shapes_for_feature_and_section", &GXGEOSTRING_wrap_get_shapes_for_feature_and_section,
                "get_shapes_for_feature_and_section((str)arg1, (str)arg2, (GXLST)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get all shapes linked to a specific feature and section\n\n"

                ":param arg1: Feature GUID\n"
                ":type arg1: str\n"
                ":param arg2: Section GUID\n"
                ":type arg2: str\n"
                ":param arg3: LST to fill\n"
                ":type arg3: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_feature_properties", &GXGEOSTRING_wrap_get_feature_properties,
                "get_feature_properties((str)arg1, (str_ref)arg2, (str_ref)arg3, (bool_ref)arg4, (int_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (int_ref)arg9, (int_ref)arg10, (int_ref)arg11, (float_ref)arg12, (float_ref)arg13, (int_ref)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a feature's properties\n\n"

                ":param arg1: Feature GUID\n"
                ":type arg1: str\n"
                ":param arg2: Name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Description\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: bool indicating if feature is decribed by polygons (shapes are polylines if not set)\n"
                ":type arg4: :class:`geosoft.gxapi.bool_ref`\n"
                ":param arg5: The fill pattern number (see PatNumber_MVIEW)\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: The fill pattern size (see PatSize_MVIEW)\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: The fill pattern thickness (see PatThick_MVIEW)\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: The fill pattern density (see PatDensity_MVIEW)\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: The fill color (an MVIEW color)\n"
                ":type arg9: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg10: The fill background color (an MVIEW color)\n"
                ":type arg10: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg11: The line style (see LineStyle_MVIEW)\n"
                ":type arg11: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg12: The line thickness (see LineThick_MVIEW)\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg13: The dash pattern pitch (see LineStyle_MVIEW)\n"
                ":type arg13: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg14: The line color (an MVIEW color)\n"
                ":type arg14: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_section_properties", &GXGEOSTRING_wrap_get_section_properties,
                "get_section_properties((str)arg1, (str_ref)arg2, (str_ref)arg3, (int_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9, (float_ref)arg10, (float_ref)arg11, (float_ref)arg12, (float_ref)arg13) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a section's properties\n\n"

                ":param arg1: Section GUID\n"
                ":type arg1: str\n"
                ":param arg2: Name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: ContainerName\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: \\ :ref:`SECTION_ORIENTATION`\\ \n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: Easting\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Northing\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Elevation\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Azimuth\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Swing\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: A in the scalar equation of best-fit plane describing the section\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: B in the scalar equation of best-fit plane describing the section\n"
                ":type arg11: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg12: C in the scalar equation of best-fit plane describing the section\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg13: D in the scalar equation of best-fit plane describing the section\n"
                ":type arg13: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_shape_properties", &GXGEOSTRING_wrap_get_shape_properties,
                "get_shape_properties((str)arg1, (str_ref)arg2, (str_ref)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a shape's properties\n\n"

                ":param arg1: Shape GUID\n"
                ":type arg1: str\n"
                ":param arg2: Feature GUID\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Section GUID\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Vertices X location\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Vertices Y location\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Vertices Z location\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );

    scope().attr("GEOSTRING_OPEN_READ") = (int32_t)0;
    scope().attr("GEOSTRING_OPEN_READWRITE") = (int32_t)1;
    scope().attr("SECTION_ORIENTATION_UNKNOWN") = (int32_t)0;
    scope().attr("SECTION_ORIENTATION_PLAN") = (int32_t)1;
    scope().attr("SECTION_ORIENTATION_SECTION") = (int32_t)2;
    scope().attr("SECTION_ORIENTATION_CROOKED") = (int32_t)2;
    scope().attr("SECTION_ORIENTATION_GMSYS") = (int32_t)2;

}
