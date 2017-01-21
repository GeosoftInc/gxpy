#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXDATPtr GXARCDB_wrap_create_dat(GXARCDBPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXDATPtr ret = self->create_dat(arg1, arg2, arg3);
    return ret;
}
inline GXDATPtr GXARCDB_wrap_create_dat_3d(GXARCDBPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    GXDATPtr ret = self->create_dat_3d(arg1, arg2, arg3, arg4);
    return ret;
}
inline GXARCDBPtr GXARCDB_wrap_current()
{
    GXARCDBPtr ret = GXARCDB::current();
    return ret;
}
inline void GXARCDB_wrap_export_to_db(GXARCDBPtr self, GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    self->export_to_db(arg1, arg2, arg3);
}
inline void GXARCDB_wrap_field_lst(GXARCDBPtr self, GXLSTPtr arg1)
{
    self->field_lst(arg1);
}
inline GXARCDBPtr GXARCDB_wrap_from_i_unknown(int32_t arg1)
{
    GXARCDBPtr ret = GXARCDB::from_i_unknown(arg1);
    return ret;
}
inline void GXARCDB_wrap_get_ipj(GXARCDBPtr self, GXIPJPtr arg1)
{
    self->get_ipj(arg1);
}
inline int32_t GXARCDB_wrap_exist_field(GXARCDBPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->exist_field(arg1);
    return ret;
}
inline int32_t GXARCDB_wrap_get_i_unknown(GXARCDBPtr self)
{
    int32_t ret = self->get_i_unknown();
    return ret;
}
inline int32_t GXARCDB_wrap_import_chem_database_wizard(GXARCDBPtr self, const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = self->import_chem_database_wizard(arg1, (IMPCH_TYPE)arg2);
    return ret;
}
inline GXARCDBPtr GXARCDB_wrap_sel_tbl_ex_gui(int_ref& arg1)
{
    GXARCDBPtr ret = GXARCDB::sel_tbl_ex_gui((ARC_SELTBL_TYPE&)arg1);
    return ret;
}
inline GXARCDBPtr GXARCDB_wrap_sel_tbl_gui()
{
    GXARCDBPtr ret = GXARCDB::sel_tbl_gui();
    return ret;
}

void gxPythonImportGXARCDB()
{

    class_<GXARCDB, GXARCDBPtr> pyClass("GXARCDB",
                                        "\n.. parsed-literal::\n\n"
                                        "   The ARCDB class is used in ArcGIS to access table contents from\n"
                                        "   data sources and layers.\n\n"
                                        , no_init);

    pyClass.def("null", &GXARCDB::null, "null() -> GXARCDB\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXARCDB`\n\n:returns: A null :class:`geosoft.gxapi.GXARCDB`\n:rtype: :class:`geosoft.gxapi.GXARCDB`\n").staticmethod("null");
    pyClass.def("is_null", &GXARCDB::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXARCDB is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXARCDB`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXARCDB::_internal_handle);
    pyClass.def("create_dat", &GXARCDB_wrap_create_dat,
                "create_dat((str)arg1, (str)arg2, (str)arg3) -> GXDAT:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a handle to a ARCGIS table DAT 2D object\n\n"

                ":param arg1: Name of X field in table\n"
                ":type arg1: str\n"
                ":param arg2: Name of Y field in table\n"
                ":type arg2: str\n"
                ":param arg3: Name of Data field in table\n"
                ":type arg3: str\n"
                ":returns: DAT, terminates if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXDAT`\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               );
    pyClass.def("create_dat_3d", &GXARCDB_wrap_create_dat_3d,
                "create_dat_3d((str)arg1, (str)arg2, (str)arg3, (str)arg4) -> GXDAT:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a handle to a ARCGIS table DAT 3D object\n\n"

                ":param arg1: Name of X field in table\n"
                ":type arg1: str\n"
                ":param arg2: Name of Y field in table\n"
                ":type arg2: str\n"
                ":param arg3: Name of Z field in table\n"
                ":type arg3: str\n"
                ":param arg4: Name of Data field in table\n"
                ":type arg4: str\n"
                ":returns: DAT, terminates if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXDAT`\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               );
    pyClass.def("current", &GXARCDB_wrap_current,
                "current() -> GXARCDB:\n"

                "\n.. parsed-literal::\n\n"
                "   This method return a handle to the current table\n\n"

                ":returns: ARCDB Handle, \\ :func:`geosoft.gxapi.GXARCDB.null()`\\  if no table selected\n"
                ":rtype: :class:`geosoft.gxapi.GXARCDB`\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("current");
    pyClass.def("export_to_db", &GXARCDB_wrap_export_to_db,
                "export_to_db((GXDB)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export data from an ARCDB table into a group in a Geosoft GDB using a template.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: import template name\n"
                ":type arg2: str\n"
                ":param arg3: Oasis montaj line name to create (overrides template value)\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   1. The import template can be in the local directory or the GEOSOFT\n"
                "      directory.\n"
                "   \n"
                "   3. If the line already exists, the data will overwrite the existing data.\n\n"
               );
    pyClass.def("field_lst", &GXARCDB_wrap_field_lst,
                "field_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Place the list of field names in a LST.\n\n"

                ":param arg1: LST\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If Z or M values are supported by the table geometry the strings\n"
                "   \"<Z Values>\" and \"<M Values>\" will be added accordingly.\n\n"
               );
    pyClass.def("from_i_unknown", &GXARCDB_wrap_from_i_unknown,
                "from_i_unknown((int)arg1) -> GXARCDB:\n"

                "\n.. parsed-literal::\n\n"
                "   This method attempts to make a table handle from an IUnknown pointer\n"
                "   \n"
                "   Returns				 ARCDB Handle, \\ :func:`geosoft.gxapi.GXARCDB.null()`\\  if not successful\n\n"

                ":param arg1: IUnknown pointer\n"
                ":type arg1: int\n"
                ":rtype: :class:`geosoft.gxapi.GXARCDB`\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("from_i_unknown");
    pyClass.def("get_ipj", &GXARCDB_wrap_get_ipj,
                "get_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get georeference information from a table.\n\n"

                ":param arg1: IPJ to fill in\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the table does not have an IPJ, the IPJ that is\n"
                "   returned will have an unknown projection.\n\n"
               );
    pyClass.def("exist_field", &GXARCDB_wrap_exist_field,
                "exist_field((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method checks to see if the specified field exists\n"
                "   in the table.\n\n"

                ":param arg1: Name of Field\n"
                ":type arg1: str\n"
                ":returns: 0 - Field does not exist\n"
                "          1 - Field Exists\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               );
    pyClass.def("get_i_unknown", &GXARCDB_wrap_get_i_unknown,
                "get_i_unknown() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method gets the IUnknown pointer\n\n"

                ":returns: IUnknown pointer\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               );
    pyClass.def("import_chem_database_wizard", &GXARCDB_wrap_import_chem_database_wizard,
                "import_chem_database_wizard((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Template creation for importing geochem data.\n\n"

                ":param arg1: template to make\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`IMPCH_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: 0-OK 1-Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               );
    pyClass.def("sel_tbl_ex_gui", &GXARCDB_wrap_sel_tbl_ex_gui,
                "sel_tbl_ex_gui((int_ref)arg1) -> GXARCDB:\n"

                "\n.. parsed-literal::\n\n"
                "   Select table GUI with table type.\n\n"

                ":param arg1: \\ :ref:`ARC_SELTBL_TYPE`\\ \n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Handle to the table (Terminate on Error)\n"
                ":rtype: :class:`geosoft.gxapi.GXARCDB`\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("sel_tbl_ex_gui");
    pyClass.def("sel_tbl_gui", &GXARCDB_wrap_sel_tbl_gui,
                "sel_tbl_gui() -> GXARCDB:\n"

                "\n.. parsed-literal::\n\n"
                "   Select table GUI.\n\n"

                ":returns: Handle to the table\n"
                ":rtype: :class:`geosoft.gxapi.GXARCDB`\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Terminates with Cancel on cancel, returns ARCDB_NULL if there are no valid tables in current document.\n\n"
               ).staticmethod("sel_tbl_gui");

    scope().attr("ARC_SELTBL_STANDALONE") = (int32_t)0;
    scope().attr("ARC_SELTBL_FEATURELAYER") = (int32_t)1;
    scope().attr("ARC_SELTBL_CANCELED") = (int32_t)-1;

}
