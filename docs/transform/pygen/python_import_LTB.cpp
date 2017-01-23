#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXLTB_wrap_add_record(GXLTBPtr self, const gx_string_type& arg1, int_ref& arg2)
{
    self->add_record(arg1, arg2);
}
inline GXLTBPtr GXLTB_wrap_contract(GXLTBPtr self, GXLTBPtr arg1)
{
    GXLTBPtr ret = self->contract(arg1);
    return ret;
}
inline GXLTBPtr GXLTB_wrap_create(const gx_string_type& arg1, int32_t arg2, int32_t arg3, const gx_string_type& arg4)
{
    GXLTBPtr ret = GXLTB::create(arg1, (LTB_TYPE)arg2, (LTB_DELIM)arg3, arg4);
    return ret;
}
inline GXLTBPtr GXLTB_wrap_create_crypt(const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4, const gx_string_type& arg5, const gx_string_type& arg6)
{
    GXLTBPtr ret = GXLTB::create_crypt(arg1, (LTB_TYPE)arg2, (LTB_DELIM)arg3, (LTB_CASE)arg4, arg5, arg6);
    return ret;
}
inline GXLTBPtr GXLTB_wrap_create_ex(const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4, const gx_string_type& arg5)
{
    GXLTBPtr ret = GXLTB::create_ex(arg1, (LTB_TYPE)arg2, (LTB_DELIM)arg3, (LTB_CASE)arg4, arg5);
    return ret;
}
inline void GXLTB_wrap_delete_record(GXLTBPtr self, int32_t arg1)
{
    self->delete_record(arg1);
}
inline void GXLTB_wrap_get_con_lst(GXLTBPtr self, int32_t arg1, const gx_string_type& arg2, int32_t arg3, GXLSTPtr arg4)
{
    self->get_con_lst(arg1, arg2, (LTB_CONLST)arg3, arg4);
}
inline void GXLTB_wrap_get_lst(GXLTBPtr self, int32_t arg1, GXLSTPtr arg2)
{
    self->get_lst(arg1, arg2);
}
inline void GXLTB_wrap_get_lst2(GXLTBPtr self, int32_t arg1, int32_t arg2, GXLSTPtr arg3)
{
    self->get_lst2(arg1, arg2, arg3);
}
inline int32_t GXLTB_wrap_fields(GXLTBPtr self)
{
    int32_t ret = self->fields();
    return ret;
}
inline int32_t GXLTB_wrap_find_field(GXLTBPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->find_field(arg1);
    return ret;
}
inline int32_t GXLTB_wrap_find_key(GXLTBPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->find_key(arg1);
    return ret;
}
inline void GXLTB_wrap_get_field(GXLTBPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_field(arg1, arg2);
}
inline int32_t GXLTB_wrap_get_int(GXLTBPtr self, int32_t arg1, int32_t arg2)
{
    int32_t ret = self->get_int(arg1, arg2);
    return ret;
}
inline void GXLTB_wrap_get_string(GXLTBPtr self, int32_t arg1, int32_t arg2, str_ref& arg3)
{
    self->get_string(arg1, arg2, arg3);
}
inline void GXLTB_wrap_get_english_string(GXLTBPtr self, int32_t arg1, int32_t arg2, str_ref& arg3)
{
    self->get_english_string(arg1, arg2, arg3);
}
inline int32_t GXLTB_wrap_records(GXLTBPtr self)
{
    int32_t ret = self->records();
    return ret;
}
inline int32_t GXLTB_wrap_search(GXLTBPtr self, int32_t arg1, int32_t arg2, const gx_string_type& arg3)
{
    int32_t ret = self->search(arg1, arg2, arg3);
    return ret;
}
inline GXLTBPtr GXLTB_wrap_merge(GXLTBPtr self, GXLTBPtr arg1)
{
    GXLTBPtr ret = self->merge(arg1);
    return ret;
}
inline double GXLTB_wrap_get_double(GXLTBPtr self, int32_t arg1, int32_t arg2)
{
    double ret = self->get_double(arg1, arg2);
    return ret;
}
inline void GXLTB_wrap_save(GXLTBPtr self, const gx_string_type& arg1)
{
    self->save(arg1);
}
inline void GXLTB_wrap_save_crypt(GXLTBPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->save_crypt(arg1, arg2);
}
inline void GXLTB_wrap_set_int(GXLTBPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    self->set_int(arg1, arg2, arg3);
}
inline void GXLTB_wrap_set_double(GXLTBPtr self, int32_t arg1, int32_t arg2, double arg3)
{
    self->set_double(arg1, arg2, arg3);
}
inline void GXLTB_wrap_set_string(GXLTBPtr self, int32_t arg1, int32_t arg2, const gx_string_type& arg3)
{
    self->set_string(arg1, arg2, arg3);
}

void gxPythonImportGXLTB()
{

    class_<GXLTB, GXLTBPtr> pyClass("GXLTB",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		An LTB object is typically created from a CSV (comma-separated values)\n"
                                    "   		file, and is a table of information that may be accessed by row\n"
                                    "   		or column. The LTB class is recommended for use with small tables\n"
                                    "   		produced from short lists (of the order of 1000's or records) such\n"
                                    "   		as the different geographic projections and their defining parameters.\n"
                                    "   		Large tables, such as those required for table-lookup functions, should\n"
                                    "   		be accessed using the TB class.\n"
                                    "   	\n\n"

                                    "\n\n**Note:**\n\n"

                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		An LTB ASCII table file has the following structure:\n"
                                    "   \n"
                                    "   		/ comments\n"
                                    "   		key_name,col_1,col_2,col_3,etc...    /field names\n"
                                    "   		key_1,token,token,token,etc...       /data lines\n"
                                    "   		key_2,token,token,token,etc...\n"
                                    "   		etc...\n"
                                    "   \n"
                                    "   		The first column must be the key column (all entries unique).\n"
                                    "   \n"
                                    "   		The header line is optional and can be used to find entries.\n"
                                    "   \n"
                                    "   		Comment and empty lines are ignored.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXLTB::null, "null() -> GXLTB\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXLTB`\n\n:returns: A null :class:`geosoft.gxapi.GXLTB`\n:rtype: :class:`geosoft.gxapi.GXLTB`\n").staticmethod("null");
    pyClass.def("is_null", &GXLTB::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXLTB is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXLTB`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXLTB::_internal_handle);
    pyClass.def("add_record", &GXLTB_wrap_add_record,
                "add_record((str)arg1, (int_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a new record.\n\n"

                ":param arg1: key name\n"
                ":type arg1: str\n"
                ":param arg2: returned record number\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the record exists, the existing record is cleared\n"
                "   					and the record number is returned.\n"
                "   				\n\n"
               );
    pyClass.def("contract", &GXLTB_wrap_contract,
                "contract((GXLTB)arg1) -> GXLTB:\n"

                "\n.. parsed-literal::\n\n"
                "   Contract the contents of two same-key and same-fields tables.\n\n"

                ":param arg1: Contract LTB\n"
                ":type arg1: :class:`geosoft.gxapi.GXLTB`\n"
                ":returns: x    - Handle to LTB object\n"
                "          						NULL - Error of some kind\n"
                ":rtype: :class:`geosoft.gxapi.GXLTB`\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The \"Key\" of the child must be the same as the \"Key\" of the Master.\n"
                "   					The fields of two LTB must be the same.\n"
                "   \n"
                "   					Contracting takes place as follows:\n"
                "   \n"
                "   					1. The Master LTB is copied to the New LTB.\n"
                "   					2. All records in the contract LIB are deleted from the New LTB (if there are any)\n"
                "   					3. The New LTB is returned.\n"
                "   				\n\n"
               );
    pyClass.def("create", &GXLTB_wrap_create,
                "create((str)arg1, (int)arg2, (int)arg3, (str)arg4) -> GXLTB:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a LTB object from a file.\n\n"

                ":param arg1: file name, .csv assumed, searched locally then in GEOSOFT.\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`LTB_TYPE`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`LTB_DELIM`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Key to find if only one record required, \"\" to read entire table.\n"
                ":type arg4: str\n"
                ":returns: x    - Handle to LTB object\n"
                "          						NULL - Error of some kind\n"
                ":rtype: :class:`geosoft.gxapi.GXLTB`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the file has no header, field names are assumed to be \"0\", \"1\", etc.\n\n"
               ).staticmethod("create");
    pyClass.def("create_crypt", &GXLTB_wrap_create_crypt,
                "create_crypt((str)arg1, (int)arg2, (int)arg3, (int)arg4, (str)arg5, (str)arg6) -> GXLTB:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a LTB object from an encrypted file.\n\n"

                ":param arg1: file name, .csv assumed, searched locally then in GEOSOFT.\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`LTB_TYPE`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`LTB_DELIM`\\ \n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`LTB_CASE`\\ \n"
                ":type arg4: int\n"
                ":param arg5: Key to find if only one record required, \"\" to read entire table.\n"
                ":type arg5: str\n"
                ":param arg6: Decryption Key \\ :ref:`SYS_CRYPT_KEY`\\ \n"
                ":type arg6: str\n"
                ":returns: x    - Handle to LTB object\n"
                "          						NULL - Error of some kind\n"
                ":rtype: :class:`geosoft.gxapi.GXLTB`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the file has no header, field names are assumed to be \"0\", \"1\", etc.\n\n"
               ).staticmethod("create_crypt");
    pyClass.def("create_ex", &GXLTB_wrap_create_ex,
                "create_ex((str)arg1, (int)arg2, (int)arg3, (int)arg4, (str)arg5) -> GXLTB:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a LTB object from a file.\n\n"

                ":param arg1: file name, .csv assumed, searched locally then in GEOSOFT.\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`LTB_TYPE`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`LTB_DELIM`\\ \n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`LTB_CASE`\\ \n"
                ":type arg4: int\n"
                ":param arg5: Key to find if only one record required, \"\" to read entire table.\n"
                ":type arg5: str\n"
                ":returns: x    - Handle to LTB object\n"
                "          						NULL - Error of some kind\n"
                ":rtype: :class:`geosoft.gxapi.GXLTB`\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the file has no header, field names are assumed to be \"0\", \"1\", etc.\n\n"
               ).staticmethod("create_ex");
    pyClass.def("delete_record", &GXLTB_wrap_delete_record,
                "delete_record((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete a record.\n\n"

                ":param arg1: record number to delete\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Record numbers after the deleted record will be reduced\n"
                "   					by 1.\n"
                "   				\n\n"
               );
    pyClass.def("get_con_lst", &GXLTB_wrap_get_con_lst,
                "get_con_lst((int)arg1, (str)arg2, (int)arg3, (GXLST)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Populate a LST with LTB names from matching fields.\n\n"

                ":param arg1: field\n"
                ":type arg1: int\n"
                ":param arg2: string to match to field, must be lower-case\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`LTB_CONLST`\\ \n"
                ":type arg3: int\n"
                ":param arg4: list to populate\n"
                ":type arg4: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The LST object will be in the order of the file.\n"
                "   					The LST names will be the LTB key fields and the\n"
                "   					LST values will be the LTB record numbers.\n"
                "   				\n\n"
               );
    pyClass.def("get_lst", &GXLTB_wrap_get_lst,
                "get_lst((int)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Populate an LST with LTB names\n\n"

                ":param arg1: field to get, 0 for key field\n"
                ":type arg1: int\n"
                ":param arg2: list to populate\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The LST object will be in the order of the file.\n"
                "   					The LST names will be the LTB fields and the\n"
                "   					LST values will be the LTB record numbers.\n"
                "   				\n\n"
               );
    pyClass.def("get_lst2", &GXLTB_wrap_get_lst2,
                "get_lst2((int)arg1, (int)arg2, (GXLST)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Populate an LST with LTB names and values\n\n"

                ":param arg1: field for names, 0 for key field\n"
                ":type arg1: int\n"
                ":param arg2: field for values, 0 for key field\n"
                ":type arg2: int\n"
                ":param arg3: list to populate\n"
                ":type arg3: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The LST object will be in the order of the file.\n"
                "   					The LST names will come from the LTB name field and the\n"
                "   					LST values will come from value field specified.\n"
                "   				\n\n"
               );
    pyClass.def("fields", &GXLTB_wrap_fields,
                "fields() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get number of fields.\n\n"

                ":returns: number of fields in the LTB.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("find_field", &GXLTB_wrap_find_field,
                "find_field((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the field number for the specified field.\n\n"

                ":param arg1: field name\n"
                ":type arg1: str\n"
                ":returns: -1 if field does not exist.\n"
                "          						field number if field does exist.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("find_key", &GXLTB_wrap_find_key,
                "find_key((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the key index of a record.\n\n"

                ":param arg1: key name\n"
                ":type arg1: str\n"
                ":returns: -1 if key does not exist.\n"
                "          						record number if key does exist.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_field", &GXLTB_wrap_get_field,
                "get_field((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a field name by index.\n\n"

                ":param arg1: field number\n"
                ":type arg1: int\n"
                ":param arg2: returned field name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the record or field are out of range, an empty string is returned.\n\n"
               );
    pyClass.def("get_int", &GXLTB_wrap_get_int,
                "get_int((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a int entry from the LTB\n\n"

                ":param arg1: record number\n"
                ":type arg1: int\n"
                ":param arg2: field number\n"
                ":type arg2: int\n"
                ":returns: If the record or field are out of range,\n"
                "          						an empty string or dummy value is returned.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_string", &GXLTB_wrap_get_string,
                "get_string((int)arg1, (int)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an entry from the LTB\n\n"

                ":param arg1: record number\n"
                ":type arg1: int\n"
                ":param arg2: field number\n"
                ":type arg2: int\n"
                ":param arg3: returned field token\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the record or field are out of range,\n"
                "   					an empty string or dummy value is returned.\n"
                "   				\n\n"
               );
    pyClass.def("get_english_string", &GXLTB_wrap_get_english_string,
                "get_english_string((int)arg1, (int)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the English entry from the LTB\n\n"

                ":param arg1: record number\n"
                ":type arg1: int\n"
                ":param arg2: field number\n"
                ":type arg2: int\n"
                ":param arg3: returned field token\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the record or field are out of range,\n"
                "   					an empty string or dummy value is returned.\n"
                "   				\n\n"
               );
    pyClass.def("records", &GXLTB_wrap_records,
                "records() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get number of records in LTB.\n\n"

                ":returns: number of records in the LTB.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("search", &GXLTB_wrap_search,
                "search((int)arg1, (int)arg2, (str)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Search for a record containing field value\n\n"

                ":param arg1: search start record\n"
                ":type arg1: int\n"
                ":param arg2: field number\n"
                ":type arg2: int\n"
                ":param arg3: search string (case sensitive)\n"
                ":type arg3: str\n"
                ":returns: -1 if search failed.\n"
                "          						record number if search succeeds\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("merge", &GXLTB_wrap_merge,
                "merge((GXLTB)arg1) -> GXLTB:\n"

                "\n.. parsed-literal::\n\n"
                "   Merge the contents of two same-key tables.\n\n"

                ":param arg1: Child LTB\n"
                ":type arg1: :class:`geosoft.gxapi.GXLTB`\n"
                ":returns: x    - Handle to LTB object\n"
                "          						NULL - Error of some kind\n"
                ":rtype: :class:`geosoft.gxapi.GXLTB`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Merging takes place as follows:\n"
                "   \n"
                "   					1. The \"Key\" of the child must be the same as the \"Key\" of the Master.\n"
                "   					2. The fields of the Master LTB are collected in-order.\n"
                "   					3. Any new fields of the Child LTB are added to the end of the list.\n"
                "   					4. A new LTB is created to contain the new field list (in-order).\n"
                "   					5. The Child table contents are added to the New LTB.\n"
                "   					6. The Master table contents are added/replace the New LTB.\n"
                "   					7. The New LTB is returned.\n"
                "   \n"
                "   					If the fields of the Master and Child are the same, steps 4, 5, 6 are\n"
                "   					replaced by:\n"
                "   \n"
                "   					4. The Master LTB is copied to the New LTB.\n"
                "   					5. Any New records found in the child are added to the New LTB\n"
                "   				\n\n"
               );
    pyClass.def("get_double", &GXLTB_wrap_get_double,
                "get_double((int)arg1, (int)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a real entry from the LTB\n\n"

                ":param arg1: record number\n"
                ":type arg1: int\n"
                ":param arg2: field number\n"
                ":type arg2: int\n"
                ":returns: If the record or field are out of range,\n"
                "          						an empty string or dummy value is returned.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("save", &GXLTB_wrap_save,
                "save((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save LTB changes to existing or new file\n\n"

                ":param arg1: file name, .csv assumed.  If \"\", save to original file.\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("save_crypt", &GXLTB_wrap_save_crypt,
                "save_crypt((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save LTB to a new file using encryption\n\n"

                ":param arg1: file name, .csv assumed.  If \"\", save to original file.\n"
                ":type arg1: str\n"
                ":param arg2: encryption key  \\ :ref:`SYS_CRYPT_KEY`\\ \n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("set_int", &GXLTB_wrap_set_int,
                "set_int((int)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a long entry\n\n"

                ":param arg1: record number\n"
                ":type arg1: int\n"
                ":param arg2: field number\n"
                ":type arg2: int\n"
                ":param arg3: entry\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_double", &GXLTB_wrap_set_double,
                "set_double((int)arg1, (int)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a double entry\n\n"

                ":param arg1: record number\n"
                ":type arg1: int\n"
                ":param arg2: field number\n"
                ":type arg2: int\n"
                ":param arg3: entry\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_string", &GXLTB_wrap_set_string,
                "set_string((int)arg1, (int)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set an entry\n\n"

                ":param arg1: record number\n"
                ":type arg1: int\n"
                ":param arg2: field number\n"
                ":type arg2: int\n"
                ":param arg3: entry\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );

    scope().attr("LTB_CASE_INSENSITIVE") = (int32_t)0;
    scope().attr("LTB_CASE_SENSITIVE") = (int32_t)1;
    scope().attr("LTB_CONLST_EXACT") = (int32_t)0;
    scope().attr("LTB_CONLST_ANY") = (int32_t)1;
    scope().attr("LTB_DELIM_SPACE") = (int32_t)0;
    scope().attr("LTB_DELIM_COMMA") = (int32_t)1;
    scope().attr("LTB_DELIM_SPACECOMMA") = (int32_t)2;
    scope().attr("LTB_TYPE_HEADER") = (int32_t)0;
    scope().attr("LTB_TYPE_NOHEADER") = (int32_t)1;

}
