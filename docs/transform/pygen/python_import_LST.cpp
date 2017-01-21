#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXLST_wrap_add_item(GXLSTPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->add_item(arg1, arg2);
}
inline void GXLST_wrap_add_symb_item(GXLSTPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->add_symb_item(arg1, arg2);
}
inline void GXLST_wrap_add_unique_item(GXLSTPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->add_unique_item(arg1, arg2);
}
inline void GXLST_wrap_append(GXLSTPtr self, GXLSTPtr arg1)
{
    self->append(arg1);
}
inline GXLSTPtr GXLST_wrap_assay_channel()
{
    GXLSTPtr ret = GXLST::assay_channel();
    return ret;
}
inline void GXLST_wrap_clear(GXLSTPtr self)
{
    self->clear();
}
inline void GXLST_wrap_convert_from_csv_string(GXLSTPtr self, const gx_string_type& arg1)
{
    self->convert_from_csv_string(arg1);
}
inline void GXLST_wrap_copy(GXLSTPtr self, GXLSTPtr arg1)
{
    self->copy(arg1);
}
inline GXLSTPtr GXLST_wrap_create(int32_t arg1)
{
    GXLSTPtr ret = GXLST::create(arg1);
    return ret;
}
inline GXLSTPtr GXLST_wrap_create_s(GXBFPtr arg1)
{
    GXLSTPtr ret = GXLST::create_s(arg1);
    return ret;
}
inline void GXLST_wrap_del_item(GXLSTPtr self, int32_t arg1)
{
    self->del_item(arg1);
}
inline void GXLST_wrap_find_items(GXLSTPtr self, int32_t arg1, GXLSTPtr arg2, GXVVPtr arg3)
{
    self->find_items((LST_ITEM)arg1, arg2, arg3);
}
inline void GXLST_wrap_gt_item(GXLSTPtr self, int32_t arg1, int32_t arg2, str_ref& arg3)
{
    self->gt_item((LST_ITEM)arg1, arg2, arg3);
}
inline void GXLST_wrap_gt_symb_item(GXLSTPtr self, int32_t arg1, str_ref& arg2, int_ref& arg3)
{
    self->gt_symb_item(arg1, arg2, arg3);
}
inline void GXLST_wrap_convert_to_csv_string(GXLSTPtr self, str_ref& arg1)
{
    self->convert_to_csv_string(arg1);
}
inline int32_t GXLST_wrap_find_item(GXLSTPtr self, int32_t arg1, const gx_string_type& arg2)
{
    int32_t ret = self->find_item((LST_ITEM)arg1, arg2);
    return ret;
}
inline int32_t GXLST_wrap_find_item_mask(GXLSTPtr self, int32_t arg1, const gx_string_type& arg2)
{
    int32_t ret = self->find_item_mask((LST_ITEM)arg1, arg2);
    return ret;
}
inline int32_t GXLST_wrap_get_int(GXLSTPtr self, int32_t arg1, int32_t arg2)
{
    int32_t ret = self->get_int((LST_ITEM)arg1, arg2);
    return ret;
}
inline void GXLST_wrap_insert_item(GXLSTPtr self, int32_t arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    self->insert_item(arg1, arg2, arg3);
}
inline int32_t GXLST_wrap_size(GXLSTPtr self)
{
    int32_t ret = self->size();
    return ret;
}
inline void GXLST_wrap_load_csv(GXLSTPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    self->load_csv(arg1, arg2, arg3);
}
inline void GXLST_wrap_load_file(GXLSTPtr self, const gx_string_type& arg1)
{
    self->load_file(arg1);
}
inline void GXLST_wrap_resource(GXLSTPtr self, const gx_string_type& arg1)
{
    self->resource(arg1);
}
inline double GXLST_wrap_get_double(GXLSTPtr self, int32_t arg1, int32_t arg2)
{
    double ret = self->get_double((LST_ITEM)arg1, arg2);
    return ret;
}
inline void GXLST_wrap_save_file(GXLSTPtr self, const gx_string_type& arg1)
{
    self->save_file(arg1);
}
inline void GXLST_wrap_select_csv_string_items(GXLSTPtr self, const gx_string_type& arg1, GXLSTPtr arg2)
{
    self->select_csv_string_items(arg1, arg2);
}
inline void GXLST_wrap_serial(GXLSTPtr self, GXBFPtr arg1)
{
    self->serial(arg1);
}
inline void GXLST_wrap_set_item(GXLSTPtr self, int32_t arg1, int32_t arg2, const gx_string_type& arg3)
{
    self->set_item((LST_ITEM)arg1, arg2, arg3);
}
inline void GXLST_wrap_sort(GXLSTPtr self, int32_t arg1, int32_t arg2)
{
    self->sort((LST_ITEM)arg1, arg2);
}

void gxPythonImportGXLST()
{

    class_<GXLST, GXLSTPtr> pyClass("GXLST",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		The LST class is used to create and retrieve lists,\n"
                                    "   		and to perform specific actions on lists, including\n"
                                    "   		retrieving list items, sorting lists and adding or\n"
                                    "   		removing list items.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXLST::null, "null() -> GXLST\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXLST`\n\n:returns: A null :class:`geosoft.gxapi.GXLST`\n:rtype: :class:`geosoft.gxapi.GXLST`\n").staticmethod("null");
    pyClass.def("is_null", &GXLST::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXLST is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXLST`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXLST::_internal_handle);
    pyClass.def("add_item", &GXLST_wrap_add_item,
                "add_item((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Adds an item to the end of the list.\n\n"

                ":param arg1: Name of the Item\n"
                ":type arg1: str\n"
                ":param arg2: Value of the Item\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("add_symb_item", &GXLST_wrap_add_symb_item,
                "add_symb_item((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Adds a channel/line/blob name and symbol to a list.\n\n"

                ":param arg1: Name of the channel, line or blob symbol\n"
                ":type arg1: str\n"
                ":param arg2: symbol handle\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A number of DB functions return LSTs with the channel\n"
                "   					or line name in the \"Name\" part of a LST, and the\n"
                "   					handle (DB_SYMB) in the value part. This function lets\n"
                "   					you quickly add a new item without the need of coverting\n"
                "   					the handle into a string value.\n"
                "   				\n\n"
               );
    pyClass.def("add_unique_item", &GXLST_wrap_add_unique_item,
                "add_unique_item((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Adds a unique item to the end of the list.\n\n"

                ":param arg1: Name of the Item\n"
                ":type arg1: str\n"
                ":param arg2: Value of the Item\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Existing items that match the name are first removed.\n\n"
               );
    pyClass.def("append", &GXLST_wrap_append,
                "append((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add the items in one list to another list.\n\n"

                ":param arg1: List to append to the above LST.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Item names and values are added using \"\\ :func:`geosoft.gxapi.GXLST.add_unique_item`\\ \",\n"
                "   					so that existing items with the same name are replaced, and if\n"
                "   					items are duplicated in the appended LST, the last one will be\n"
                "   					the one to remain after the process is complete.\n"
                "   				\n\n"
               );
    pyClass.def("assay_channel", &GXLST_wrap_assay_channel,
                "assay_channel() -> GXLST:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a LST of assay channel mask strings from file.\n\n"

                ":returns: LST Object\n"
                ":rtype: :class:`geosoft.gxapi.GXLST`\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Searches the local directory, then user\\etc, then \\etc to see\n"
                "   					if the file \"assaylist.csv\" exists.\n"
                "   					The file contains strings of those channel names which are\n"
                "   					to be interpreted as assay channels for geochemical processes.\n"
                "   					Items can be on the same line, separated by commas, or on\n"
                "   					separate lines (and combinations of both).\n"
                "   					If this function is used in combination with the lFindItemMask_LST\n"
                "   					function, then you can use mask-strings such as \"\\ `*`\\ ppm\"\n"
                "   					The following is a sample file:\n"
                "   \n"
                "   					\\ `*`\\ ppm, \\ `*`\\ (ppm), \\ `*`\\ PPM, \\ `*`\\ (PPM), FeCl, MnO2\n"
                "   					\"Fe %\"\n"
                "   					FeO\n"
                "   \n"
                "   					If the file is not found, or if no items are parsed, the list\n"
                "   					is returned with zero size.\n"
                "   \n"
                "   					See the \"assaylist.csv\" file in the oasismontaj\\etc directory\n"
                "   					for more details.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXLST.find_item_mask`\\ \n\n"
               ).staticmethod("assay_channel");
    pyClass.def("clear", &GXLST_wrap_clear,
                "clear() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clear a list object.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("convert_from_csv_string", &GXLST_wrap_convert_from_csv_string,
                "convert_from_csv_string((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LST with items from a string.\n\n"

                ":param arg1: Comma separated items\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Items in the input buffer must be separated with\n"
                "   					commas.\n"
                "   					Both the Name and Value in the list are set to the\n"
                "   					item.\n"
                "   				\n\n"
               );
    pyClass.def("copy", &GXLST_wrap_copy,
                "copy((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy one LST object to another.\n\n"

                ":param arg1: Source List to Copy from\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create", &GXLST_wrap_create,
                "create((int)arg1) -> GXLST:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					creates a user controllable list. The list\n"
                "   					is empty when created.\n"
                "   				\n\n"

                ":param arg1: Width of the list to make. This number should be large enough for both the item name and the item value.  Must be > 2 and <= 4096.\n"
                ":type arg1: int\n"
                ":returns: Handle to the List Object.\n"
                ":rtype: :class:`geosoft.gxapi.GXLST`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_s", &GXLST_wrap_create_s,
                "create_s((GXBF)arg1) -> GXLST:\n"

                "\n.. parsed-literal::\n\n"
                "   Create LST from serialized source.\n\n"

                ":param arg1: BF\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: LST object\n"
                ":rtype: :class:`geosoft.gxapi.GXLST`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_s");
    pyClass.def("del_item", &GXLST_wrap_del_item,
                "del_item((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Removes an item from the list. All items below\n"
                "   					it are shifted up one.\n"
                "   				\n\n"

                ":param arg1: Item Number to Delete\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("find_items", &GXLST_wrap_find_items,
                "find_items((int)arg1, (GXLST)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Searches a LST for items in a second LST, returns indices of those found.\n\n"

                ":param arg1: \\ :ref:`LST_ITEM`\\  data to do the search on\n"
                ":type arg1: int\n"
                ":param arg2: Items to search for\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: GS_LONG VV of returned indices into the first LST.\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is a much more efficient way of determining if items in\n"
                "   					one LST are found in a second, than by calling \\ :func:`geosoft.gxapi.GXLST.find_item`\\ \n"
                "   					repeatedly in a loop.\n"
                "   					The returned INT VV contains the same number of items as\n"
                "   					the \"search items\" LST, and contains -1 for items where the\n"
                "   					value is not found, and the index of items that are found.\n"
                "   					Comparisons are case-tolerant.\n"
                "   				\n\n"
               );
    pyClass.def("gt_item", &GXLST_wrap_gt_item,
                "gt_item((int)arg1, (int)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This places the specified item into the buffer provided.\n\n"

                ":param arg1: \\ :ref:`LST_ITEM`\\  data to retrieve\n"
                ":type arg1: int\n"
                ":param arg2: Item Number to Get\n"
                ":type arg2: int\n"
                ":param arg3: Buffer to Place Item Into\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If item number is not in the list, the buffer will be \"\".\n\n"
               );
    pyClass.def("gt_symb_item", &GXLST_wrap_gt_symb_item,
                "gt_symb_item((int)arg1, (str_ref)arg2, (int_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns a channel/line/blob name and symbol from a list.\n\n"

                ":param arg1: Item number to get\n"
                ":type arg1: int\n"
                ":param arg2: Buffer to Place Symbol name into\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Symbol handle\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A number of DB functions return LSTs with the channel\n"
                "   					or line name in the \"Name\" part of a LST, and the\n"
                "   					handle (DB_SYMB) in the value part. This function lets\n"
                "   					you quickly retrieve both the name and symbol handle\n"
                "   					for a given item, which needing to convert between types.\n"
                "   				\n\n"
               );
    pyClass.def("convert_to_csv_string", &GXLST_wrap_convert_to_csv_string,
                "convert_to_csv_string((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a string with names from a LST.\n\n"

                ":param arg1: Buffer to add items to\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The list name values are put into a string,\n"
                "   					items separated by commas.\n"
                "   				\n\n"
               );
    pyClass.def("find_item", &GXLST_wrap_find_item,
                "find_item((int)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Searches the list for a specified item.\n\n"

                ":param arg1: \\ :ref:`LST_ITEM`\\  data to do the search on\n"
                ":type arg1: int\n"
                ":param arg2: String to Search For\n"
                ":type arg2: str\n"
                ":returns: x  - Item Number\n"
                "          						-1 - Not Found\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Comparisons are case-tolerant.\n\n"
               );
    pyClass.def("find_item_mask", &GXLST_wrap_find_item_mask,
                "find_item_mask((int)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Searches the list for a specified item, list contains masks.\n\n"

                ":param arg1: \\ :ref:`LST_ITEM`\\  data to search\n"
                ":type arg1: int\n"
                ":param arg2: String to try LST mask items on Search For\n"
                ":type arg2: str\n"
                ":returns: x  - Item Number\n"
                "          						-1 - Not Found\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Comparsions are case-intolerant (unlike \\ :func:`geosoft.gxapi.GXLST.find_item`\\ ).\n"
                "   					This means items in the list such as \"\\ `*`\\ (ppm)\" will be\n"
                "   					found if the input search string is \"Ni (ppm)\" or \"Ni(ppm)\",\n"
                "   					but not if it is \"Ni (PPM)\", so you should include\n"
                "   					both \"\\ `*`\\ ppm\\ `*`\\ \" and \"\\ `*`\\ PPM\\ `*`\\ \".\n"
                "   \n"
                "   					It is NOT the input string that should be the mask, but\n"
                "   					the LST items themselves\n"
                "   \n"
                "   					This function was designed originally for geochemical\n"
                "   					processes in order to identify if a given channel name\n"
                "   					indicates that the channel should be given the \"Assay\" class.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXLST.assay_channel`\\ \n\n"
               );
    pyClass.def("get_int", &GXLST_wrap_get_int,
                "get_int((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an integer item.\n\n"

                ":param arg1: \\ :ref:`LST_ITEM`\\  data to retrieve\n"
                ":type arg1: int\n"
                ":param arg2: Item Number to Get\n"
                ":type arg2: int\n"
                ":returns: integer, iDUMMY if conversion fails or string is empty.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("insert_item", &GXLST_wrap_insert_item,
                "insert_item((int)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Adds an item at a given location in the list.\n\n"

                ":param arg1: Item index\n"
                ":type arg1: int\n"
                ":param arg2: Name of the Item\n"
                ":type arg2: str\n"
                ":param arg3: Value of the Item\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Index must be 0 >= index >= list size.\n"
                "   					Items above the list index are shifted up one index value.\n"
                "   				\n\n"
               );
    pyClass.def("size", &GXLST_wrap_size,
                "size() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of items in the list.\n\n"

                ":returns: x - Number of items in the list.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("load_csv", &GXLST_wrap_load_csv,
                "load_csv((str)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a list with data from a CSV file\n\n"

                ":param arg1: The CSV file\n"
                ":type arg1: str\n"
                ":param arg2: column label for the item name\n"
                ":type arg2: str\n"
                ":param arg3: column label for the item value\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Both the Item and Value fields must be specified.\n"
                "   					The CSV file must be comma delimited, and have\n"
                "   					a header line with the field names.\n"
                "   					Leading and trailing spaces are removed in the names and values.\n"
                "   				\n\n"
               );
    pyClass.def("load_file", &GXLST_wrap_load_file,
                "load_file((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set up a list from a list file.\n\n"

                ":param arg1: name of the file\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A list file is an ASCII file that contains list entries.\n"
                "   					Each line for the file contains a list item name and an\n"
                "   					optional list item value.  The name and value must be\n"
                "   					delimited by a space, tab or comma.\n"
                "   					If the item name or value contains spaces, tabs or commas,\n"
                "   					it must be contined in quotes.\n"
                "   					blank lines and lines that begin with a '/' character are\n"
                "   					ignored.\n"
                "   \n"
                "   					The default extension is .lst.  If the file cannot\n"
                "   					be found in the local directory, the GEOSOFT\\etc directory\n"
                "   					is searched.\n"
                "   					If it cannot be found, the list will be\n"
                "   					empty.  Not finding a file is not an error.\n"
                "   \n"
                "   					This function replaces the \\ :func:`geosoft.gxapi.GXLST.load_file`\\  function which\n"
                "   					actually always returned 0, or terminated on an error.\n"
                "   				\n\n"
               );
    pyClass.def("resource", &GXLST_wrap_resource,
                "resource((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Load a GX List Resource into this list object.  The\n"
                "   					entries are placed at the end of the list and are not\n"
                "   					sorted.\n"
                "   				\n\n"

                ":param arg1: Name of the Resource\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_double", &GXLST_wrap_get_double,
                "get_double((int)arg1, (int)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a real item.\n\n"

                ":param arg1: \\ :ref:`LST_ITEM`\\  data to retrieve\n"
                ":type arg1: int\n"
                ":param arg2: Item Number to Get\n"
                ":type arg2: int\n"
                ":returns: real, rDUMMY if conversion fails or string is empty.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("save_file", &GXLST_wrap_save_file,
                "save_file((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save a list to a file.\n\n"

                ":param arg1: name of the file\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A list file is an ASCII file that contains list entries.\n"
                "   					Each line for the file contains a list item name and an\n"
                "   					optional list item value.  The name and value must be\n"
                "   					delimited by a space, tab or comma.\n"
                "   					If the item name or value contains spaces, tabs or commas,\n"
                "   					it must be contined in quotes.\n"
                "   					blank lines and lines that begin with a '/' character are\n"
                "   					ignored.\n"
                "   \n"
                "   					The default extension is .lst.  If the file has a full path\n"
                "   					it will be created as specified.  Otherwise we look for the\n"
                "   					file in the local then the GEOSOFT\\etc directory.  If the file\n"
                "   					does not exist it will be created in the GEOSOFT\\etc directory.\n"
                "   				\n\n"
               );
    pyClass.def("select_csv_string_items", &GXLST_wrap_select_csv_string_items,
                "select_csv_string_items((str)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LST with items from a second LST found in a CSV string.\n\n"

                ":param arg1: Comma separated item names\n"
                ":type arg1: str\n"
                ":param arg2: LST to add selected items to\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Items in the input string must be separated with\n"
                "   					commas. Parsing uses the sCommaTokens_GS function.\n"
                "   					Both the name and value of the input LST items whose\n"
                "   					name matches an item in the input string are\n"
                "   					copied to the output LST.\n"
                "   					Items are copied in the same order they appear in the\n"
                "   					input string. Items in the string not found in the input LST\n"
                "   					are ignored, and no error is registered.\n"
                "   					Item matches are case-tolerant.\n"
                "   				\n\n"
               );
    pyClass.def("serial", &GXLST_wrap_serial,
                "serial((GXBF)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Serialize LST to a BF.\n\n"

                ":param arg1: BF\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_item", &GXLST_wrap_set_item,
                "set_item((int)arg1, (int)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Place an item at a specified point in the LST.\n\n"

                ":param arg1: \\ :ref:`LST_ITEM`\\  data to insert\n"
                ":type arg1: int\n"
                ":param arg2: Item Number to Set\n"
                ":type arg2: int\n"
                ":param arg3: Item to Set\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The existing item at the given index will be replaced.\n\n"
               );
    pyClass.def("sort", &GXLST_wrap_sort,
                "sort((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sorts a list.\n\n"

                ":param arg1: \\ :ref:`LST_ITEM`\\  data to sort on\n"
                ":type arg1: int\n"
                ":param arg2: 0 - Ascending, 1 - Decending\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );

    scope().attr("LST_ITEM_NAME") = (int32_t)0;
    scope().attr("LST_ITEM_VALUE") = (int32_t)1;

}
