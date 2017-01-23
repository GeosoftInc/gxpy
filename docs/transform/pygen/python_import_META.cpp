#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline int32_t GXMETA_wrap_create_attrib(GXMETAPtr self, const gx_string_type& arg1, int32_t arg2, int32_t arg3)
{
    int32_t ret = self->create_attrib(arg1, arg2, arg3);
    return ret;
}
inline void GXMETA_wrap_delete_attrib(GXMETAPtr self, int32_t arg1)
{
    self->delete_attrib(arg1);
}
inline void GXMETA_wrap_set_attribute_editable(GXMETAPtr self, int32_t arg1, int32_t arg2)
{
    self->set_attribute_editable(arg1, arg2);
}
inline void GXMETA_wrap_set_attribute_visible(GXMETAPtr self, int32_t arg1, int32_t arg2)
{
    self->set_attribute_visible(arg1, arg2);
}
inline int32_t GXMETA_wrap_create_class(GXMETAPtr self, const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = self->create_class(arg1, arg2);
    return ret;
}
inline void GXMETA_wrap_delete_class(GXMETAPtr self, int32_t arg1)
{
    self->delete_class(arg1);
}
inline void GXMETA_wrap_copy(GXMETAPtr self, GXMETAPtr arg1)
{
    self->copy(arg1);
}
inline GXMETAPtr GXMETA_wrap_create()
{
    GXMETAPtr ret = GXMETA::create();
    return ret;
}
inline GXMETAPtr GXMETA_wrap_create_s(GXBFPtr arg1)
{
    GXMETAPtr ret = GXMETA::create_s(arg1);
    return ret;
}
inline void GXMETA_wrap_serial(GXMETAPtr self, GXBFPtr arg1)
{
    self->serial(arg1);
}
inline int32_t GXMETA_wrap_find_data(GXMETAPtr self, int32_t arg1, int32_t arg2)
{
    int32_t ret = self->find_data(arg1, arg2);
    return ret;
}
inline void GXMETA_wrap_get_attrib_bool(GXMETAPtr self, int32_t arg1, int32_t arg2, int_ref& arg3)
{
    self->get_attrib_bool(arg1, arg2, arg3);
}
inline void GXMETA_wrap_get_attrib_enum(GXMETAPtr self, int32_t arg1, int32_t arg2, int_ref& arg3)
{
    self->get_attrib_enum(arg1, arg2, arg3);
}
inline void GXMETA_wrap_get_attrib_int(GXMETAPtr self, int32_t arg1, int32_t arg2, int_ref& arg3)
{
    self->get_attrib_int(arg1, arg2, arg3);
}
inline void GXMETA_wrap_get_attrib_double(GXMETAPtr self, int32_t arg1, int32_t arg2, float_ref& arg3)
{
    self->get_attrib_double(arg1, arg2, arg3);
}
inline void GXMETA_wrap_get_attrib_string(GXMETAPtr self, int32_t arg1, int32_t arg2, str_ref& arg3)
{
    self->get_attrib_string(arg1, arg2, arg3);
}
inline bool GXMETA_wrap_has_value(GXMETAPtr self, int32_t arg1, int32_t arg2)
{
    bool ret = self->has_value(arg1, arg2);
    return ret;
}
inline void GXMETA_wrap_export_table_csv(GXMETAPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->export_table_csv(arg1, arg2);
}
inline void GXMETA_wrap_import_table_csv(GXMETAPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->import_table_csv(arg1, arg2);
}
inline void GXMETA_wrap_write_text(GXMETAPtr self, GXWAPtr arg1)
{
    self->write_text(arg1);
}
inline void GXMETA_wrap_delete_all_items(GXMETAPtr self, int32_t arg1)
{
    self->delete_all_items(arg1);
}
inline void GXMETA_wrap_delete_item(GXMETAPtr self, int32_t arg1)
{
    self->delete_item(arg1);
}
inline int32_t GXMETA_wrap_h_creat_item(GXMETAPtr self, const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = self->h_creat_item(arg1, arg2);
    return ret;
}
inline int32_t GXMETA_wrap_h_get_next_item(GXMETAPtr self, int32_t arg1, int32_t arg2)
{
    int32_t ret = self->h_get_next_item(arg1, arg2);
    return ret;
}
inline void GXMETA_wrap_get_attrib_obj(GXMETAPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    self->get_attrib_obj(arg1, arg2, arg3);
}
inline void GXMETA_wrap_set_attrib_obj(GXMETAPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    self->set_attrib_obj(arg1, arg2, arg3);
}
inline void GXMETA_wrap_set_attrib_bool(GXMETAPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    self->set_attrib_bool(arg1, arg2, arg3);
}
inline void GXMETA_wrap_set_attrib_enum(GXMETAPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    self->set_attrib_enum(arg1, arg2, arg3);
}
inline void GXMETA_wrap_set_attrib_int(GXMETAPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    self->set_attrib_int(arg1, arg2, arg3);
}
inline void GXMETA_wrap_set_attrib_double(GXMETAPtr self, int32_t arg1, int32_t arg2, double arg3)
{
    self->set_attrib_double(arg1, arg2, arg3);
}
inline void GXMETA_wrap_set_attrib_string(GXMETAPtr self, int32_t arg1, int32_t arg2, const gx_string_type& arg3)
{
    self->set_attrib_string(arg1, arg2, arg3);
}
inline void GXMETA_wrap_set_empty_attrib(GXMETAPtr self, int32_t arg1, int32_t arg2)
{
    self->set_empty_attrib(arg1, arg2);
}
inline int32_t GXMETA_wrap_h_copy_across_attribute(GXMETAPtr self, GXMETAPtr arg1, int32_t arg2)
{
    int32_t ret = self->h_copy_across_attribute(arg1, arg2);
    return ret;
}
inline int32_t GXMETA_wrap_h_copy_across_class(GXMETAPtr self, GXMETAPtr arg1, int32_t arg2)
{
    int32_t ret = self->h_copy_across_class(arg1, arg2);
    return ret;
}
inline int32_t GXMETA_wrap_h_copy_across_data(GXMETAPtr self, GXMETAPtr arg1, int32_t arg2)
{
    int32_t ret = self->h_copy_across_data(arg1, arg2);
    return ret;
}
inline int32_t GXMETA_wrap_h_copy_across_item(GXMETAPtr self, GXMETAPtr arg1, int32_t arg2)
{
    int32_t ret = self->h_copy_across_item(arg1, arg2);
    return ret;
}
inline int32_t GXMETA_wrap_h_copy_across_type(GXMETAPtr self, GXMETAPtr arg1, int32_t arg2)
{
    int32_t ret = self->h_copy_across_type(arg1, arg2);
    return ret;
}
inline void GXMETA_wrap_move_datas_across(GXMETAPtr self, GXMETAPtr arg1, int32_t arg2, int32_t arg3)
{
    self->move_datas_across(arg1, arg2, arg3);
}
inline int32_t GXMETA_wrap_create_type(GXMETAPtr self, const gx_string_type& arg1, int32_t arg2, int32_t arg3)
{
    int32_t ret = self->create_type(arg1, arg2, arg3);
    return ret;
}
inline void GXMETA_wrap_delete_data(GXMETAPtr self, int32_t arg1)
{
    self->delete_data(arg1);
}
inline void GXMETA_wrap_delete_type(GXMETAPtr self, int32_t arg1)
{
    self->delete_type(arg1);
}
inline void GXMETA_wrap_get_obj_name(GXMETAPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_obj_name(arg1, arg2);
}
inline int32_t GXMETA_wrap_resolve_umn(GXMETAPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->resolve_umn(arg1);
    return ret;
}

void gxPythonImportGXMETA()
{

    class_<GXMETA, GXMETAPtr> pyClass("GXMETA",
                                      "\n.. parsed-literal::\n\n"
                                      "   \n"
                                      "   		A META object contains hierarchical organized metadata\n"
                                      "   		of any type, including other objects.  META information\n"
                                      "   		is organized in an XML-like structure based on a data\n"
                                      "   		schema that describes the data hierarchy.   META objects\n"
                                      "   		are used by many entities that need to store metadata\n"
                                      "   		specific to the entities or to the application.\n"
                                      "   \n"
                                      "   		Metadata can be saved in databases and maps, as well as in\n"
                                      "   		channels, lines, views and groups.  Oasis montaj objects\n"
                                      "   		can be queried for their associated metadata, and if it\n"
                                      "   		exists, the metadata can be retrieved and utilized by\n"
                                      "   		other Oasis montaj processes.\n"
                                      "   	\n\n"
                                      , no_init);

    pyClass.def("null", &GXMETA::null, "null() -> GXMETA\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXMETA`\n\n:returns: A null :class:`geosoft.gxapi.GXMETA`\n:rtype: :class:`geosoft.gxapi.GXMETA`\n").staticmethod("null");
    pyClass.def("is_null", &GXMETA::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXMETA is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXMETA`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXMETA::_internal_handle);
    pyClass.def("create_attrib", &GXMETA_wrap_create_attrib,
                "create_attrib((str)arg1, (int)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an attribute\n\n"

                ":param arg1: Attribute Name\n"
                ":type arg1: str\n"
                ":param arg2: Parent class or \\ :ref:`META_CORE_CLASS`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Type of Attribute or \\ :ref:`META_CORE_TYPE`\\ \n"
                ":type arg3: int\n"
                ":returns: x - Attribute Token\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               );
    pyClass.def("delete_attrib", &GXMETA_wrap_delete_attrib,
                "delete_attrib((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete Attrib from META.\n\n"

                ":param arg1: Attrib to delete\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("set_attribute_editable", &GXMETA_wrap_set_attribute_editable,
                "set_attribute_editable((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Allow/disallow an attribute to be editable in the browser\n\n"

                ":param arg1: Attribute or \\ :ref:`META_CORE_ATTRIB`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Editable Flag\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("set_attribute_visible", &GXMETA_wrap_set_attribute_visible,
                "set_attribute_visible((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Allow/disallow an attribute to be visible in the browser\n\n"

                ":param arg1: Attribute or \\ :ref:`META_CORE_ATTRIB`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Editable Flag\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("create_class", &GXMETA_wrap_create_class,
                "create_class((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a class\n\n"

                ":param arg1: Class Name\n"
                ":type arg1: str\n"
                ":param arg2: Parent class or \\ :ref:`META_CORE_CLASS`\\ _Base\n"
                ":type arg2: int\n"
                ":returns: x - Class Token\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               );
    pyClass.def("delete_class", &GXMETA_wrap_delete_class,
                "delete_class((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete Class from META.\n\n"

                ":param arg1: Class to delete\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("copy", &GXMETA_wrap_copy,
                "copy((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a META to another\n\n"

                ":param arg1: Source META object.\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               );
    pyClass.def("create", &GXMETA_wrap_create,
                "create() -> GXMETA:\n"

                "\n.. parsed-literal::\n\n"
                "   Create\n\n"

                ":returns: META Object\n"
                ":rtype: :class:`geosoft.gxapi.GXMETA`\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"
               ).staticmethod("create");
    pyClass.def("create_s", &GXMETA_wrap_create_s,
                "create_s((GXBF)arg1) -> GXMETA:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a META Object from a BF\n\n"

                ":param arg1: BF to serialize from\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: META Object\n"
                ":rtype: :class:`geosoft.gxapi.GXMETA`\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               ).staticmethod("create_s");
    pyClass.def("serial", &GXMETA_wrap_serial,
                "serial((GXBF)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Serialize an META to a BF\n\n"

                ":param arg1: BF to serialize to\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               );
    pyClass.def("find_data", &GXMETA_wrap_find_data,
                "find_data((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Does this meta/attribute have a value ?\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Attribute\n"
                ":type arg2: int\n"
                ":returns: x  - Data Value\n"
                "          						\\ :ref:`H_META_INVALID_TOKEN`\\  - No\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("get_attrib_bool", &GXMETA_wrap_get_attrib_bool,
                "get_attrib_bool((int)arg1, (int)arg2, (int_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a boolean value to an attribute\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Attribute\n"
                ":type arg2: int\n"
                ":param arg3: Value to set\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("get_attrib_enum", &GXMETA_wrap_get_attrib_enum,
                "get_attrib_enum((int)arg1, (int)arg2, (int_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an enum value to an attribute (as an integer)\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Attribute\n"
                ":type arg2: int\n"
                ":param arg3: Value to set\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("get_attrib_int", &GXMETA_wrap_get_attrib_int,
                "get_attrib_int((int)arg1, (int)arg2, (int_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an integer value to an attribute\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Attribute\n"
                ":type arg2: int\n"
                ":param arg3: Value to set\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("get_attrib_double", &GXMETA_wrap_get_attrib_double,
                "get_attrib_double((int)arg1, (int)arg2, (float_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an integer value to an attribute\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Attribute\n"
                ":type arg2: int\n"
                ":param arg3: Value to set\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("get_attrib_string", &GXMETA_wrap_get_attrib_string,
                "get_attrib_string((int)arg1, (int)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a string value to an attribute\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Attribute\n"
                ":type arg2: int\n"
                ":param arg3: String value to get\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("has_value", &GXMETA_wrap_has_value,
                "has_value((int)arg1, (int)arg2) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Does this meta/attribute have a value set?\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Attribute\n"
                ":type arg2: int\n"
                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"
               );
    pyClass.def("export_table_csv", &GXMETA_wrap_export_table_csv,
                "export_table_csv((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export all items in a class as a CSV\n\n"

                ":param arg1: Class of items to export\n"
                ":type arg1: int\n"
                ":param arg2: Name of CSV file to produce\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"
               );
    pyClass.def("import_table_csv", &GXMETA_wrap_import_table_csv,
                "import_table_csv((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import a CSV into a class as items.\n\n"

                ":param arg1: Class to import into\n"
                ":type arg1: int\n"
                ":param arg2: Name of CSV file to load\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Field names in the CSV file that match attribute names in the class will be\n"
                "   					imported into table entries in the class.  Usually this will be used with\n"
                "   					a class created using the hCreateTable_SCHEMA method so that the contents of\n"
                "   					class can be viewed as a table.\n"
                "   				\n\n"
               );
    pyClass.def("write_text", &GXMETA_wrap_write_text,
                "write_text((GXWA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write the entire meta as a text file\n\n"

                ":param arg1: WA to write to\n"
                ":type arg1: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("delete_all_items", &GXMETA_wrap_delete_all_items,
                "delete_all_items((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete all items in this class.\n\n"

                ":param arg1: Class of items to delete\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"
               );
    pyClass.def("delete_item", &GXMETA_wrap_delete_item,
                "delete_item((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete item from META.\n\n"

                ":param arg1: Item to delete\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("h_creat_item", &GXMETA_wrap_h_creat_item,
                "h_creat_item((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates item in Class.\n\n"

                ":param arg1: Unique item Name\n"
                ":type arg1: str\n"
                ":param arg2: Class (can be root)\n"
                ":type arg2: int\n"
                ":returns: x                    - Next Item\n"
                "          						\\ :ref:`H_META_INVALID_TOKEN`\\  - Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("h_get_next_item", &GXMETA_wrap_h_get_next_item,
                "h_get_next_item((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Count the number of items in a class\n\n"

                ":param arg1: Class\n"
                ":type arg1: int\n"
                ":param arg2: Starting Item (must \\ :ref:`H_META_INVALID_TOKEN`\\  for first item)\n"
                ":type arg2: int\n"
                ":returns: x                    - Next Item\n"
                "          						\\ :ref:`H_META_INVALID_TOKEN`\\  - No more items\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );
    pyClass.def("get_attrib_obj", &GXMETA_wrap_get_attrib_obj,
                "get_attrib_obj((int)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an object from an attribute\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Attribute\n"
                ":type arg2: int\n"
                ":param arg3: Object to get info into\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("set_attrib_obj", &GXMETA_wrap_set_attrib_obj,
                "set_attrib_obj((int)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set an object to an attribute\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Attribute\n"
                ":type arg2: int\n"
                ":param arg3: Object to set\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("set_attrib_bool", &GXMETA_wrap_set_attrib_bool,
                "set_attrib_bool((int)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a boolean value to an attribute\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Attribute\n"
                ":type arg2: int\n"
                ":param arg3: Value to set\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("set_attrib_enum", &GXMETA_wrap_set_attrib_enum,
                "set_attrib_enum((int)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set an enum value to an attribute (as an integer)\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Attribute\n"
                ":type arg2: int\n"
                ":param arg3: Value to set\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("set_attrib_int", &GXMETA_wrap_set_attrib_int,
                "set_attrib_int((int)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set an integer value to an attribute\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Attribute\n"
                ":type arg2: int\n"
                ":param arg3: Value to set\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("set_attrib_double", &GXMETA_wrap_set_attrib_double,
                "set_attrib_double((int)arg1, (int)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set an integer value to an attribute\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Attribute\n"
                ":type arg2: int\n"
                ":param arg3: Value to set\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("set_attrib_string", &GXMETA_wrap_set_attrib_string,
                "set_attrib_string((int)arg1, (int)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a string value to an attribute\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Attribute\n"
                ":type arg2: int\n"
                ":param arg3: String value to set\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("set_empty_attrib", &GXMETA_wrap_set_empty_attrib,
                "set_empty_attrib((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set an empty attribute data holder\n\n"

                ":param arg1: MetaObject to set\n"
                ":type arg1: int\n"
                ":param arg2: Attribute MetaObject to set\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("h_copy_across_attribute", &GXMETA_wrap_h_copy_across_attribute,
                "h_copy_across_attribute((GXMETA)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy an Attribute from one META to another\n\n"

                ":param arg1: Source META object.\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg2: Attribute to copy\n"
                ":type arg2: int\n"
                ":returns: x                  - Handle of Attribute\n"
                "          						META_INVALID_TOKEN - No visible data\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("h_copy_across_class", &GXMETA_wrap_h_copy_across_class,
                "h_copy_across_class((GXMETA)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a Class from one META to another\n\n"

                ":param arg1: Source META object.\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg2: Class to copy\n"
                ":type arg2: int\n"
                ":returns: x                  - Handle of Class\n"
                "          						META_INVALID_TOKEN - No visible data anywhere\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This will copy all parent classes as well.\n\n"
               );
    pyClass.def("h_copy_across_data", &GXMETA_wrap_h_copy_across_data,
                "h_copy_across_data((GXMETA)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a Data value from one META to another\n\n"

                ":param arg1: Source META object.\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg2: Data value to copy\n"
                ":type arg2: int\n"
                ":returns: x                  - Handle of Data value\n"
                "          						META_INVALID_TOKEN - No visible data\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("h_copy_across_item", &GXMETA_wrap_h_copy_across_item,
                "h_copy_across_item((GXMETA)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy an Item from one META to another\n\n"

                ":param arg1: Source META object.\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg2: Item to copy\n"
                ":type arg2: int\n"
                ":returns: x                  - Handle of Item\n"
                "          						META_INVALID_TOKEN - No visible data\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("h_copy_across_type", &GXMETA_wrap_h_copy_across_type,
                "h_copy_across_type((GXMETA)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a Type from one META to another\n\n"

                ":param arg1: Source META object.\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg2: Type to copy\n"
                ":type arg2: int\n"
                ":returns: x                  - Handle of type\n"
                "          						META_INVALID_TOKEN - No visible data anywhere\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Classes and parent types will also be copied.\n\n"
               );
    pyClass.def("move_datas_across", &GXMETA_wrap_move_datas_across,
                "move_datas_across((GXMETA)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Moves data items from one META to another\n\n"

                ":param arg1: Source META Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg2: Object to copy data from\n"
                ":type arg2: int\n"
                ":param arg3: Object to copy data to\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               );
    pyClass.def("create_type", &GXMETA_wrap_create_type,
                "create_type((str)arg1, (int)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an attribute\n\n"

                ":param arg1: Attribute Name\n"
                ":type arg1: str\n"
                ":param arg2: Parent Class or \\ :ref:`META_CORE_CLASS`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Parent Type or \\ :ref:`META_CORE_TYPE`\\ \n"
                ":type arg3: int\n"
                ":returns: x - Type Token\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               );
    pyClass.def("delete_data", &GXMETA_wrap_delete_data,
                "delete_data((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete Data from META.\n\n"

                ":param arg1: Data to delete\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("delete_type", &GXMETA_wrap_delete_type,
                "delete_type((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete Type from META.\n\n"

                ":param arg1: Type to delete\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("get_obj_name", &GXMETA_wrap_get_obj_name,
                "get_obj_name((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the name of this item.\n\n"

                ":param arg1: Object\n"
                ":type arg1: int\n"
                ":param arg2: Name of object\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );
    pyClass.def("resolve_umn", &GXMETA_wrap_resolve_umn,
                "resolve_umn((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Resolve a Unique Meta Name (UMN) and find the token\n\n"

                ":param arg1: Unique Meta Name (UMN)\n"
                ":type arg1: str\n"
                ":returns: x                    - Token\n"
                "          						\\ :ref:`H_META_INVALID_TOKEN`\\  - Not found\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );

    scope().attr("H_META_INVALID_TOKEN") = (int32_t)-1;
    scope().attr("META_CORE_ATTRIB_Class_Description") = (int32_t)-300;
    scope().attr("META_CORE_ATTRIB_Class_Application") = (int32_t)-301;
    scope().attr("META_CORE_ATTRIB_Class_ReferenceURL") = (int32_t)-302;
    scope().attr("META_CORE_ATTRIB_Class_Type") = (int32_t)-303;
    scope().attr("META_CORE_ATTRIB_Type_Description") = (int32_t)-304;
    scope().attr("META_CORE_ATTRIB_Type_ReferenceURL") = (int32_t)-305;
    scope().attr("META_CORE_ATTRIB_Type_FixedSize") = (int32_t)-306;
    scope().attr("META_CORE_ATTRIB_Type_ByteOrder") = (int32_t)-307;
    scope().attr("META_CORE_ATTRIB_Type_MinValue") = (int32_t)-308;
    scope().attr("META_CORE_ATTRIB_Type_MaxValue") = (int32_t)-309;
    scope().attr("META_CORE_ATTRIB_Type_MaxSize") = (int32_t)-310;
    scope().attr("META_CORE_ATTRIB_Type_ObjectClass") = (int32_t)-311;
    scope().attr("META_CORE_ATTRIB_Type_hCreatS_Func") = (int32_t)-312;
    scope().attr("META_CORE_ATTRIB_Type_sSerial_Func") = (int32_t)-313;
    scope().attr("META_CORE_ATTRIB_Type_Enum_Value") = (int32_t)-314;
    scope().attr("META_CORE_ATTRIB_Attrib_Visible") = (int32_t)-315;
    scope().attr("META_CORE_ATTRIB_Attrib_Editable") = (int32_t)-316;
    scope().attr("META_CORE_ATTRIB_Attrib_FlatName") = (int32_t)-317;
    scope().attr("META_CORE_CLASS_Base") = (int32_t)-100;
    scope().attr("META_CORE_CLASS_Predefined") = (int32_t)-101;
    scope().attr("META_CORE_CLASS_Attributes") = (int32_t)-102;
    scope().attr("META_CORE_CLASS_ClassAttributes") = (int32_t)-103;
    scope().attr("META_CORE_CLASS_TypeAttributes") = (int32_t)-104;
    scope().attr("META_CORE_CLASS_ObjectAttributes") = (int32_t)-105;
    scope().attr("META_CORE_CLASS_EnumAttributes") = (int32_t)-106;
    scope().attr("META_CORE_CLASS_AttributeAttributes") = (int32_t)-107;
    scope().attr("META_CORE_CLASS_ItemAttributes") = (int32_t)-108;
    scope().attr("META_CORE_CLASS_Types") = (int32_t)-109;
    scope().attr("META_CORE_CLASS_Enums") = (int32_t)-110;
    scope().attr("META_CORE_CLASS_Enum_Bool") = (int32_t)-111;
    scope().attr("META_CORE_CLASS_Enum_ClassType") = (int32_t)-112;
    scope().attr("META_CORE_TYPE_Bytes") = (int32_t)-200;
    scope().attr("META_CORE_TYPE_Bool") = (int32_t)-201;
    scope().attr("META_CORE_TYPE_I1") = (int32_t)-202;
    scope().attr("META_CORE_TYPE_U1") = (int32_t)-203;
    scope().attr("META_CORE_TYPE_I2") = (int32_t)-204;
    scope().attr("META_CORE_TYPE_U2") = (int32_t)-205;
    scope().attr("META_CORE_TYPE_I4") = (int32_t)-206;
    scope().attr("META_CORE_TYPE_U4") = (int32_t)-207;
    scope().attr("META_CORE_TYPE_I8") = (int32_t)-208;
    scope().attr("META_CORE_TYPE_U8") = (int32_t)-209;
    scope().attr("META_CORE_TYPE_R4") = (int32_t)-210;
    scope().attr("META_CORE_TYPE_R8") = (int32_t)-211;
    scope().attr("META_CORE_TYPE_String") = (int32_t)-212;
    scope().attr("META_CORE_TYPE_Object") = (int32_t)-213;
    scope().attr("META_CORE_TYPE_Enum") = (int32_t)-214;
    scope().attr("META_CORE_TYPE_ClassType") = (int32_t)-215;

}
