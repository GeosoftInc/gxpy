#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXSHP_wrap_append_item(GXSHPPtr self)
{
    self->append_item();
}
inline GXSHPPtr GXSHP_wrap_create(const gx_string_type& arg1, int32_t arg2)
{
    GXSHPPtr ret = GXSHP::create(arg1, (SHP_GEOM_TYPE)arg2);
    return ret;
}
inline int32_t GXSHP_wrap_add_int_field(GXSHPPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->add_int_field(arg1);
    return ret;
}
inline int32_t GXSHP_wrap_add_double_field(GXSHPPtr self, const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = self->add_double_field(arg1, arg2);
    return ret;
}
inline int32_t GXSHP_wrap_add_string_field(GXSHPPtr self, const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = self->add_string_field(arg1, arg2);
    return ret;
}
inline int32_t GXSHP_wrap_find_field(GXSHPPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->find_field(arg1);
    return ret;
}
inline int32_t GXSHP_wrap_max_id_num(GXSHPPtr self)
{
    int32_t ret = self->max_id_num();
    return ret;
}
inline int32_t GXSHP_wrap_num_fields(GXSHPPtr self)
{
    int32_t ret = self->num_fields();
    return ret;
}
inline int32_t GXSHP_wrap_num_records(GXSHPPtr self)
{
    int32_t ret = self->num_records();
    return ret;
}
inline int32_t GXSHP_wrap_type(GXSHPPtr self)
{
    SHP_GEOM_TYPE ret = self->type();
    return ret;
}
inline GXSHPPtr GXSHP_wrap_open(const gx_string_type& arg1)
{
    GXSHPPtr ret = GXSHP::open(arg1);
    return ret;
}
inline void GXSHP_wrap_set_arc(GXSHPPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->set_arc(arg1, arg2);
}
inline void GXSHP_wrap_set_arc_z(GXSHPPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->set_arc_z(arg1, arg2, arg3);
}
inline void GXSHP_wrap_set_int(GXSHPPtr self, int32_t arg1, int32_t arg2)
{
    self->set_int(arg1, arg2);
}
inline void GXSHP_wrap_set_ipj(GXSHPPtr self, GXIPJPtr arg1)
{
    self->set_ipj(arg1);
}
inline void GXSHP_wrap_set_point(GXSHPPtr self, double arg1, double arg2)
{
    self->set_point(arg1, arg2);
}
inline void GXSHP_wrap_set_point_z(GXSHPPtr self, double arg1, double arg2, double arg3)
{
    self->set_point_z(arg1, arg2, arg3);
}
inline void GXSHP_wrap_set_polygon(GXSHPPtr self, GXVVPtr arg1, GXVVPtr arg2, bool arg3)
{
    self->set_polygon(arg1, arg2, arg3);
}
inline void GXSHP_wrap_set_polygon_z(GXSHPPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, bool arg4)
{
    self->set_polygon_z(arg1, arg2, arg3, arg4);
}
inline void GXSHP_wrap_set_double(GXSHPPtr self, int32_t arg1, double arg2)
{
    self->set_double(arg1, arg2);
}
inline void GXSHP_wrap_set_string(GXSHPPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_string(arg1, arg2);
}
inline void GXSHP_wrap_write_item(GXSHPPtr self)
{
    self->write_item();
}

void gxPythonImportGXSHP()
{

    class_<GXSHP, GXSHPPtr> pyClass("GXSHP",
                                    "\n.. parsed-literal::\n\n"
                                    "   The SHP class is used to create ESRI shape files.\n\n"

                                    "\n\n**Note:**\n\n"

                                    "\n.. parsed-literal::\n\n"
                                    "   Shape files contain a single \"geometry\" type, e.g.\n"
                                    "   points, arcs or polygons. They may be accompanied by\n"
                                    "   a DBF file containing attribute data.\n\n"
                                    , no_init);

    pyClass.def("null", &GXSHP::null, "null() -> GXSHP\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXSHP`\n\n:returns: A null :class:`geosoft.gxapi.GXSHP`\n:rtype: :class:`geosoft.gxapi.GXSHP`\n").staticmethod("null");
    pyClass.def("is_null", &GXSHP::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXSHP is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXSHP`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXSHP::_internal_handle);
    pyClass.def("append_item", &GXSHP_wrap_append_item,
                "append_item() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Append the current item and data to an old SHP object.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The currently stored SHP item and data are written to the\n"
                "   SHP geometry and data files. (If no data fields have been\n"
                "   defined, then the data file is not written).\n\n"
               );
    pyClass.def("create", &GXSHP_wrap_create,
                "create((str)arg1, (int)arg2) -> GXSHP:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new SHP object\n\n"

                ":param arg1: File name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`SHP_GEOM_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: SHP object\n"
                ":rtype: :class:`geosoft.gxapi.GXSHP`\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The file name is used to create the various files. The\n"
                "   file type and extension are added:\n"
                "   \n"
                "   e.g. \"filename.shp\",\n"
                "        \"filename.dbf\"\n"
                "   \n"
                "   The following geometry types are currently supported:\n"
                "   \n"
                "   Type                    Required geometry function.\n"
                "   \n"
                "   SHP_GEOM_TYPE_POINT     \\ :func:`geosoft.gxapi.GXSHP.set_point`\\ \n"
                "   SHP_GEOM_TYPE_ARC       \\ :func:`geosoft.gxapi.GXSHP.set_arc`\\ \n"
                "   SHP_GEOM_TYPE_POLYGON   \\ :func:`geosoft.gxapi.GXSHP.set_polygon`\\ \n"
                "   \n"
                "   SHP_GEOM_TYPE_POINTZ    \\ :func:`geosoft.gxapi.GXSHP.set_point_z`\\ \n"
                "   SHP_GEOM_TYPE_ARCZ      \\ :func:`geosoft.gxapi.GXSHP.set_arc_z`\\ \n"
                "   SHP_GEOM_TYPE_POLYGONZ  \\ :func:`geosoft.gxapi.GXSHP.set_polygon_z`\\ \n\n"
               ).staticmethod("create");
    pyClass.def("add_int_field", &GXSHP_wrap_add_int_field,
                "add_int_field((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Add an INT type data field to a shape file\n\n"

                ":param arg1: field name\n"
                ":type arg1: str\n"
                ":returns: Index of the new field\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The returned field index should be used with the SetXXX_SHP\n"
                "   functions to set individual data values.\n\n"
               );
    pyClass.def("add_double_field", &GXSHP_wrap_add_double_field,
                "add_double_field((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a REAL type data field to a shape file\n\n"

                ":param arg1: field name\n"
                ":type arg1: str\n"
                ":param arg2: number of decimal places\n"
                ":type arg2: int\n"
                ":returns: Index of the new field\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The returned field index should be used with the SetXXX_SHP\n"
                "   functions to set individual data values.\n\n"
               );
    pyClass.def("add_string_field", &GXSHP_wrap_add_string_field,
                "add_string_field((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a string type data field to a shape file\n\n"

                ":param arg1: field name\n"
                ":type arg1: str\n"
                ":param arg2: Maximum number of characters in the string\n"
                ":type arg2: int\n"
                ":returns: Index of the new field\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The returned field index should be used with the SetXXX_SHP\n"
                "   functions to set individual data values.\n\n"
               );
    pyClass.def("find_field", &GXSHP_wrap_find_field,
                "find_field((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the index for a data field.\n\n"

                ":param arg1: field name\n"
                ":type arg1: str\n"
                ":returns: The index, -1 if not found.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("max_id_num", &GXSHP_wrap_max_id_num,
                "max_id_num() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the max ID number.\n\n"

                ":returns: The max ID number.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("num_fields", &GXSHP_wrap_num_fields,
                "num_fields() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the field number.\n\n"

                ":returns: The field number.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("num_records", &GXSHP_wrap_num_records,
                "num_records() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the record number.\n\n"

                ":returns: The record number.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("type", &GXSHP_wrap_type,
                "type() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the SHP object's geometry type.\n\n"

                ":returns: the SHP object's geometry type (\\ :ref:`SHP_GEOM_TYPE`\\ )\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("open", &GXSHP_wrap_open,
                "open((str)arg1) -> GXSHP:\n"

                "\n.. parsed-literal::\n\n"
                "   Open an old SHP object\n\n"

                ":param arg1: File name\n"
                ":type arg1: str\n"
                ":returns: SHP object\n"
                ":rtype: :class:`geosoft.gxapi.GXSHP`\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               ).staticmethod("open");
    pyClass.def("set_arc", &GXSHP_wrap_set_arc,
                "set_arc((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write an XY arc (polyline) item.\n\n"

                ":param arg1: X locations\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Can ONLY be used for SHP_GEOM_TYPE_ARC files.\n\n"
               );
    pyClass.def("set_arc_z", &GXSHP_wrap_set_arc_z,
                "set_arc_z((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write an XYZ arc (polyline) item.\n\n"

                ":param arg1: X locations\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z locations\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Can ONLY be used for SHP_GEOM_TYPE_ARCZ files.\n\n"
               );
    pyClass.def("set_int", &GXSHP_wrap_set_int,
                "set_int((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a data value to a int.\n\n"

                ":param arg1: data field index\n"
                ":type arg1: int\n"
                ":param arg2: input int value\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The input value is converted to the field's data type.\n\n"
               );
    pyClass.def("set_ipj", &GXSHP_wrap_set_ipj,
                "set_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a SHP object's projection.\n\n"

                ":param arg1: input IPJ\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the SHP object has a projection, and it\n"
                "   is not IPJ_TYPE_NONE, then it will be output\n"
                "   to a file with the .prj extension when the\n"
                "   first object is output.\n"
                "   This function should be called BEFORE the first\n"
                "   object is written.\n\n"
               );
    pyClass.def("set_point", &GXSHP_wrap_set_point,
                "set_point((float)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write an XY point item.\n\n"

                ":param arg1: X location\n"
                ":type arg1: float\n"
                ":param arg2: Y location\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Can ONLY be used for SHP_GEOM_TYPE_POINT files.\n\n"
               );
    pyClass.def("set_point_z", &GXSHP_wrap_set_point_z,
                "set_point_z((float)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write an XYZ point item.\n\n"

                ":param arg1: X location\n"
                ":type arg1: float\n"
                ":param arg2: Y location\n"
                ":type arg2: float\n"
                ":param arg3: Z location\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Can ONLY be used for SHP_GEOM_TYPE_POINTZ files.\n\n"
               );
    pyClass.def("set_polygon", &GXSHP_wrap_set_polygon,
                "set_polygon((GXVV)arg1, (GXVV)arg2, (bool)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write an XY polygon item.\n\n"

                ":param arg1: X locations\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: bool ``True`` for outer ring polygon (inclusive/island), ``False`` for inner ring (exclusive/hole)\n"
                ":type arg3: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Can ONLY be used for SHP_GEOM_TYPE_POLYGON files.\n\n"
               );
    pyClass.def("set_polygon_z", &GXSHP_wrap_set_polygon_z,
                "set_polygon_z((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (bool)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write an XYZ polygon item.\n\n"

                ":param arg1: X locations\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z locations\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: bool ``True`` for outer ring polygon (inclusive/island), ``False`` for inner ring (exclusive/hole)\n"
                ":type arg4: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Can ONLY be used for SHP_GEOM_TYPE_POLYGONZ files.\n\n"
               );
    pyClass.def("set_double", &GXSHP_wrap_set_double,
                "set_double((int)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a data value to a real.\n\n"

                ":param arg1: data field index\n"
                ":type arg1: int\n"
                ":param arg2: input real value\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The input value is converted to the field's data type.\n\n"
               );
    pyClass.def("set_string", &GXSHP_wrap_set_string,
                "set_string((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a data value to a string.\n\n"

                ":param arg1: data field index\n"
                ":type arg1: int\n"
                ":param arg2: input string value\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The input string is converted to the field's data type.\n\n"
               );
    pyClass.def("write_item", &GXSHP_wrap_write_item,
                "write_item() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Output the current item and data.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The currently stored SHP item and data are written to the\n"
                "   SHP geometry and data files. (If no data fields have been\n"
                "   defined, then the data file is not written).\n\n"
               );

    scope().attr("SHP_GEOM_TYPE_POINT") = (int32_t)1;
    scope().attr("SHP_GEOM_TYPE_ARC") = (int32_t)3;
    scope().attr("SHP_GEOM_TYPE_POLYGON") = (int32_t)5;
    scope().attr("SHP_GEOM_TYPE_POINTZ") = (int32_t)11;
    scope().attr("SHP_GEOM_TYPE_ARCZ") = (int32_t)13;
    scope().attr("SHP_GEOM_TYPE_POLYGONZ") = (int32_t)15;

}
