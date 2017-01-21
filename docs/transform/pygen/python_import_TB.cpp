#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXTB_wrap_set_search_mode(GXTBPtr self, int32_t arg1)
{
    self->set_search_mode((TB_SEARCH)arg1);
}
inline GXTBPtr GXTB_wrap_create(const gx_string_type& arg1)
{
    GXTBPtr ret = GXTB::create(arg1);
    return ret;
}
inline GXTBPtr GXTB_wrap_create_db(GXDBPtr arg1)
{
    GXTBPtr ret = GXTB::create_db(arg1);
    return ret;
}
inline GXTBPtr GXTB_wrap_create_ltb(GXLTBPtr arg1)
{
    GXTBPtr ret = GXTB::create_ltb(arg1);
    return ret;
}
inline int32_t GXTB_wrap_field(GXTBPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->field(arg1);
    return ret;
}
inline void GXTB_wrap_get_string(GXTBPtr self, int32_t arg1, int32_t arg2, str_ref& arg3)
{
    self->get_string(arg1, arg2, arg3);
}
inline int32_t GXTB_wrap_data_type(GXTBPtr self, int32_t arg1)
{
    DB_CATEGORY_CHAN ret = self->data_type(arg1);
    return ret;
}
inline void GXTB_wrap_find_col_by_index(GXTBPtr self, int32_t arg1, str_ref& arg2)
{
    self->find_col_by_index(arg1, arg2);
}
inline int32_t GXTB_wrap_find_col_by_name(GXTBPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->find_col_by_name(arg1);
    return ret;
}
inline int32_t GXTB_wrap_format(GXTBPtr self, int32_t arg1)
{
    DB_CHAN_FORMAT ret = self->format(arg1);
    return ret;
}
inline int32_t GXTB_wrap_get_int(GXTBPtr self, int32_t arg1, int32_t arg2)
{
    int32_t ret = self->get_int(arg1, arg2);
    return ret;
}
inline int32_t GXTB_wrap_num_columns(GXTBPtr self)
{
    int32_t ret = self->num_columns();
    return ret;
}
inline int32_t GXTB_wrap_num_rows(GXTBPtr self)
{
    int32_t ret = self->num_rows();
    return ret;
}
inline void GXTB_wrap_load_db(GXTBPtr self, GXDBPtr arg1, int32_t arg2)
{
    self->load_db(arg1, arg2);
}
inline double GXTB_wrap_get_double(GXTBPtr self, int32_t arg1, int32_t arg2)
{
    double ret = self->get_double(arg1, arg2);
    return ret;
}
inline void GXTB_wrap_save(GXTBPtr self, const gx_string_type& arg1)
{
    self->save(arg1);
}
inline void GXTB_wrap_save_db(GXTBPtr self, GXDBPtr arg1, int32_t arg2)
{
    self->save_db(arg1, arg2);
}
inline void GXTB_wrap_save_to_ascii(GXTBPtr self, const gx_string_type& arg1)
{
    self->save_to_ascii(arg1);
}
inline void GXTB_wrap_set_int(GXTBPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    self->set_int(arg1, arg2, arg3);
}
inline void GXTB_wrap_set_double(GXTBPtr self, int32_t arg1, int32_t arg2, double arg3)
{
    self->set_double(arg1, arg2, arg3);
}
inline void GXTB_wrap_set_string(GXTBPtr self, int32_t arg1, int32_t arg2, const gx_string_type& arg3)
{
    self->set_string(arg1, arg2, arg3);
}
inline void GXTB_wrap_sort(GXTBPtr self, int32_t arg1)
{
    self->sort(arg1);
}

void gxPythonImportGXTB()
{

    class_<GXTB, GXTBPtr> pyClass("GXTB",
                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		The TB class is a high-performance table class used to\n"
                                  "   		perform table-based processing, such as leveling data in\n"
                                  "   		an OASIS database. The LTB class is recommended for use\n"
                                  "   		with small tables produced from short lists such as the\n"
                                  "   		different geographic projections and their defining parameters.\n"
                                  "   	\n\n"
                                  , no_init);

    pyClass.def("null", &GXTB::null, "null() -> GXTB\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXTB`\n\n:returns: A null :class:`geosoft.gxapi.GXTB`\n:rtype: :class:`geosoft.gxapi.GXTB`\n").staticmethod("null");
    pyClass.def("is_null", &GXTB::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXTB is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXTB`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXTB::_internal_handle);
    pyClass.def("set_search_mode", &GXTB_wrap_set_search_mode,
                "set_search_mode((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the search mode of a table.\n\n"

                ":param arg1: \\ :ref:`TB_SEARCH`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If performance is an issue, you may want to test which search\n"
                "   					mode provides the best performance with typical data.\n"
                "   				\n\n"
               );
    pyClass.def("create", &GXTB_wrap_create,
                "create((str)arg1) -> GXTB:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads a table into memory and return a table handle.\n\n"

                ":param arg1: Name of the table file to load\n"
                ":type arg1: str\n"
                ":returns: TB Object\n"
                ":rtype: :class:`geosoft.gxapi.GXTB`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the table contains fewer data columns than are defined by the\n"
                "   					the table header, the TB object will read in the table and dummy\n"
                "   					the elements of the missing data columns.\n"
                "   				\n\n"
               ).staticmethod("create");
    pyClass.def("create_db", &GXTB_wrap_create_db,
                "create_db((GXDB)arg1) -> GXTB:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a table from a database.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: TB Object\n"
                ":rtype: :class:`geosoft.gxapi.GXTB`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The table will contain fields for all channels in\n"
                "   					the database.\n"
                "   \n"
                "   					The database is not loaded with data.  Use the \\ :func:`geosoft.gxapi.GXTB.load_db`\\ \n"
                "   					function to load data into the table.\n"
                "   				\n\n"
               ).staticmethod("create_db");
    pyClass.def("create_ltb", &GXTB_wrap_create_ltb,
                "create_ltb((GXLTB)arg1) -> GXTB:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a table from an LTB database.\n\n"

                ":param arg1: LTB object\n"
                ":type arg1: :class:`geosoft.gxapi.GXLTB`\n"
                ":returns: TB Object\n"
                ":rtype: :class:`geosoft.gxapi.GXTB`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_ltb");
    pyClass.def("field", &GXTB_wrap_field,
                "field((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a field handle.\n\n"

                ":param arg1: Field name\n"
                ":type arg1: str\n"
                ":returns: The handle to the field (must be present)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_string", &GXTB_wrap_get_string,
                "get_string((int)arg1, (int)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets a string value from a table element.\n\n"

                ":param arg1: Row of element to Get\n"
                ":type arg1: int\n"
                ":param arg2: Column of element to Get\n"
                ":type arg2: int\n"
                ":param arg3: returned string\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("data_type", &GXTB_wrap_data_type,
                "data_type((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the data type for the specified column.\n\n"

                ":param arg1: Column of element to Get\n"
                ":type arg1: int\n"
                ":returns: \\ :ref:`DB_CATEGORY_CHAN`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.1\n\n"
               );
    pyClass.def("find_col_by_index", &GXTB_wrap_find_col_by_index,
                "find_col_by_index((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Finds a column's name by its index.\n\n"

                ":param arg1: Index of column to find\n"
                ":type arg1: int\n"
                ":param arg2: Buffer for column name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("find_col_by_name", &GXTB_wrap_find_col_by_name,
                "find_col_by_name((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Finds a column's index by its name.\n\n"

                ":param arg1: Name of column to find\n"
                ":type arg1: str\n"
                ":returns: Index of column.\n"
                "          						-1 if not found.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("format", &GXTB_wrap_format,
                "format((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the channel format for the specified column.\n\n"

                ":param arg1: Column of element to Get\n"
                ":type arg1: int\n"
                ":returns: \\ :ref:`DB_CHAN_FORMAT`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.1\n\n"
               );
    pyClass.def("get_int", &GXTB_wrap_get_int,
                "get_int((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets an integer value from a table element.\n\n"

                ":param arg1: Row of element to Get\n"
                ":type arg1: int\n"
                ":param arg2: Column of element to Get\n"
                ":type arg2: int\n"
                ":returns: Value\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("num_columns", &GXTB_wrap_num_columns,
                "num_columns() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the number of data fields (columns) in a table.\n\n"

                ":returns: Number of columns\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("num_rows", &GXTB_wrap_num_rows,
                "num_rows() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the number of data rows in a table.\n\n"

                ":returns: Number of rows\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("load_db", &GXTB_wrap_load_db,
                "load_db((GXDB)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a database into a TB\n\n"

                ":param arg1: database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: line\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The line is appended to the data already in the table.\n\n"
               );
    pyClass.def("get_double", &GXTB_wrap_get_double,
                "get_double((int)arg1, (int)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets an real value from a table element.\n\n"

                ":param arg1: Row of element to Get\n"
                ":type arg1: int\n"
                ":param arg2: Column of element to Get\n"
                ":type arg2: int\n"
                ":returns: Value\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("save", &GXTB_wrap_save,
                "save((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Saves the data in a table to a file. The table header will be\n"
                "   					in ASCII and the data will be in BINARY format.\n"
                "   				\n\n"

                ":param arg1: Name of File to save table into\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("save_db", &GXTB_wrap_save_db,
                "save_db((GXDB)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save a TB in a database line\n\n"

                ":param arg1: database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: line\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Missing channels are created.\n"
                "   					Data in existing channels on the line will be replaced.\n"
                "   				\n\n"
               );
    pyClass.def("save_to_ascii", &GXTB_wrap_save_to_ascii,
                "save_to_ascii((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Saves the data in a table to a file. The table header will be\n"
                "   					in ASCII and the data will be in ASCII format.\n"
                "   				\n\n"

                ":param arg1: Name of File to save table into\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_int", &GXTB_wrap_set_int,
                "set_int((int)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets an integer value into a table element.\n\n"

                ":param arg1: Row of element to set\n"
                ":type arg1: int\n"
                ":param arg2: Column of element to set\n"
                ":type arg2: int\n"
                ":param arg3: Value to set\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The table field containing the element to be set MUST be\n"
                "   					of type GS_BYTE, GS_USHORT, GS_SHORT, or GS_LONG.\n"
                "   					If the field is GS_BYTE, GS_USHORT, or GS_LONG, the new data\n"
                "   					value will cause an overflow if the value is out of range of\n"
                "   					the data type. The new element value will then be invalid.\n"
                "   \n"
                "   					If the row of the new element exceeds the number of rows in\n"
                "   					the table, then the table will AUTOMATICALLY be EXPANDED to\n"
                "   					exactly as many rows needed to hold the new element. The new\n"
                "   					element is placed in the proper field of the last row, and\n"
                "   					all other field elements have invalid data. All fields of\n"
                "   					the new rows up to the new element's row will also contain\n"
                "   					invalid data.\n"
                "   				\n\n"
               );
    pyClass.def("set_double", &GXTB_wrap_set_double,
                "set_double((int)arg1, (int)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets an real value into a table element.\n\n"

                ":param arg1: Row of element to set\n"
                ":type arg1: int\n"
                ":param arg2: Column of element to set\n"
                ":type arg2: int\n"
                ":param arg3: Value to set\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The table field containing the element to be set MUST be\n"
                "   					of type GS_FLOAT or GS_DOUBLE.\n"
                "   					If the field is GS_FLOAT the new data value will cause an\n"
                "   					overflow if the value is out of range of the data type.\n"
                "   					The new element value will then be invalid.\n"
                "   \n"
                "   					If the row of the new element exceeds the number of rows in\n"
                "   					the table, then the table will AUTOMATICALLY be EXPANDED to\n"
                "   					exactly as many rows needed to hold the new element. The new\n"
                "   					element is placed in the proper field of the last row, and\n"
                "   					all other field elements have invalid data. All fields of\n"
                "   					the new rows up to the new element's row will also contain\n"
                "   					invalid data.\n"
                "   				\n\n"
               );
    pyClass.def("set_string", &GXTB_wrap_set_string,
                "set_string((int)arg1, (int)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets a string value into a table element.\n\n"

                ":param arg1: Row of element to set\n"
                ":type arg1: int\n"
                ":param arg2: Column of element to set\n"
                ":type arg2: int\n"
                ":param arg3: Value to set\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The table field containing the element to be set MUST be\n"
                "   					of 'string'.\n"
                "   \n"
                "   					If the row of the new element exceeds the number of rows in\n"
                "   					the table, then the table will AUTOMATICALLY be EXPANDED to\n"
                "   					exactly as many rows needed to hold the new element. The new\n"
                "   					element is placed in the proper field of the last row, and\n"
                "   					all other field elements have invalid data. All fields of\n"
                "   					the new rows up to the new element's row will also contain\n"
                "   					invalid data.\n"
                "   				\n\n"
               );
    pyClass.def("sort", &GXTB_wrap_sort,
                "sort((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sorts a table by a specified column.\n\n"

                ":param arg1: Index of data Column to sort table by\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the column to sort by contains duplicated values, the\n"
                "   					sorted table is NOT guaranteed to retain the ordering of\n"
                "   					the duplicated values/\n"
                "   					E.g. Given 2 rows of values:   xx   yy   1\n"
                "   					bb   aa   1\n"
                "   					If the table is sorted on column 3, the second row\n"
                "   					may or may not come after the first row in the sorted\n"
                "   					table.\n"
                "   				\n\n"
               );

    scope().attr("TB_SEARCH_BINARY") = (int32_t)0;
    scope().attr("TB_SEARCH_LINEAR") = (int32_t)1;

}
