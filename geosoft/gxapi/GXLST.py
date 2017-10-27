### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXLST:
    """
    GXLST class.

    The `GXLST <geosoft.gxapi.GXLST>` class is used to create and retrieve lists,
    and to perform specific actions on lists, including
    retrieving list items, sorting lists and adding or
    removing list items.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapLST(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXLST`
        
        :returns: A null `GXLST`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXLST` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXLST`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_item(self, name, val):
        """
        Adds an item to the end of the list.
        """
        self._wrapper.add_item(name.encode(), val.encode())
        




    def add_symb_item(self, name, symb):
        """
        Adds a channel/line/blob name and symbol to a list.

        **Note:**

        A number of `GXDB <geosoft.gxapi.GXDB>` functions return LSTs with the channel
        or line name in the "Name" part of a `GXLST <geosoft.gxapi.GXLST>`, and the
        handle (DB_SYMB) in the value part. This function lets
        you quickly add a new item without the need of coverting
        the handle into a string value.
        """
        self._wrapper.add_symb_item(name.encode(), symb)
        




    def add_unique_item(self, name, val):
        """
        Adds a unique item to the end of the list.

        **Note:**

        Existing items that match the name are first removed.
        """
        self._wrapper.add_unique_item(name.encode(), val.encode())
        




    def append(self, lst2):
        """
        Add the items in one list to another list.

        **Note:**

        Item names and values are added using "`add_unique_item <geosoft.gxapi.GXLST.add_unique_item>`",
        so that existing items with the same name are replaced, and if
        items are duplicated in the appended `GXLST <geosoft.gxapi.GXLST>`, the last one will be
        the one to remain after the process is complete.
        """
        self._wrapper.append(lst2._wrapper)
        



    @classmethod
    def assay_channel(cls):
        """
        Create a `GXLST <geosoft.gxapi.GXLST>` of assay channel mask strings from file.

        **Note:**

        Searches the local directory, then user\\etc, then \\etc to see
        if the file "assaylist.csv" exists.
        The file contains strings of those channel names which are
        to be interpreted as assay channels for geochemical processes.
        Items can be on the same line, separated by commas, or on
        separate lines (and combinations of both).
        If this function is used in combination with the lFindItemMask_LST
        function, then you can use mask-strings such as "``*ppm``"
        The following is a sample file:
        
        ``*ppm, *(ppm), *PPM, *(PPM), FeCl, MnO2``
        ``"Fe %"``
        ``FeO``
        
        If the file is not found, or if no items are parsed, the list
        is returned with zero size.
        
        See the "assaylist.csv" file in the oasismontaj\\etc directory
        for more details.

        .. seealso::

            `find_item_mask <geosoft.gxapi.GXLST.find_item_mask>`
        """
        ret_val = gxapi_cy.WrapLST.assay_channel(GXContext._get_tls_geo())
        return GXLST(ret_val)




    def clear(self):
        """
        Clear a list object.
        """
        self._wrapper.clear()
        




    def convert_from_csv_string(self, buff):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with items from a string.

        **Note:**

        Items in the input buffer must be separated with
        commas.
        Both the Name and Value in the list are set to the
        item.
        """
        self._wrapper.convert_from_csv_string(buff.encode())
        




    def copy(self, source):
        """
        Copy one `GXLST <geosoft.gxapi.GXLST>` object to another.
        """
        self._wrapper.copy(source._wrapper)
        



    @classmethod
    def create(cls, width):
        """
        creates a user controllable list. The list
        is empty when created.
        """
        ret_val = gxapi_cy.WrapLST.create(GXContext._get_tls_geo(), width)
        return GXLST(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create `GXLST <geosoft.gxapi.GXLST>` from serialized source.
        """
        ret_val = gxapi_cy.WrapLST.create_s(GXContext._get_tls_geo(), bf._wrapper)
        return GXLST(ret_val)




    def del_item(self, item):
        """
        Removes an item from the list. All items below
        it are shifted up one.
        """
        self._wrapper.del_item(item)
        






    def find_items(self, type, lst2, vv):
        """
        Searches a `GXLST <geosoft.gxapi.GXLST>` for items in a second `GXLST <geosoft.gxapi.GXLST>`, returns indices of those found.

        **Note:**

        This is a much more efficient way of determining if items in
        one `GXLST <geosoft.gxapi.GXLST>` are found in a second, than by calling `find_item <geosoft.gxapi.GXLST.find_item>`
        repeatedly in a loop.
        The returned INT `GXVV <geosoft.gxapi.GXVV>` contains the same number of items as
        the "search items" `GXLST <geosoft.gxapi.GXLST>`, and contains -1 for items where the
        value is not found, and the index of items that are found.
        Comparisons are case-tolerant.
        """
        self._wrapper.find_items(type, lst2._wrapper, vv._wrapper)
        




    def gt_item(self, type, item, buff):
        """
        This places the specified item into the buffer provided.

        **Note:**

        If item number is not in the list, the buffer will be "".
        """
        buff.value = self._wrapper.gt_item(type, item, buff.value.encode())
        




    def gt_symb_item(self, item, name, symb):
        """
        Returns a channel/line/blob name and symbol from a list.

        **Note:**

        A number of `GXDB <geosoft.gxapi.GXDB>` functions return LSTs with the channel
        or line name in the "Name" part of a `GXLST <geosoft.gxapi.GXLST>`, and the
        handle (DB_SYMB) in the value part. This function lets
        you quickly retrieve both the name and symbol handle
        for a given item, which needing to convert between types.
        """
        name.value, symb.value = self._wrapper.gt_symb_item(item, name.value.encode(), symb.value)
        




    def convert_to_csv_string(self, buff):
        """
        Load a string with names from a `GXLST <geosoft.gxapi.GXLST>`.

        **Note:**

        The list name values are put into a string,
        items separated by commas.
        """
        buff.value = self._wrapper.convert_to_csv_string(buff.value.encode())
        




    def find_item(self, type, name):
        """
        Searches the list for a specified item.

        **Note:**

        Comparisons are case-tolerant.
        """
        ret_val = self._wrapper.find_item(type, name.encode())
        return ret_val




    def find_item_mask(self, type, name):
        """
        Searches the list for a specified item, list contains masks.

        **Note:**

        Comparsions are case-intolerant (unlike `find_item <geosoft.gxapi.GXLST.find_item>`).
        This means items in the list such as "``*(ppm)``" will be
        found if the input search string is "Ni (ppm)" or "Ni(ppm)",
        but not if it is "Ni (PPM)", so you should include
        both "``*ppm*``" and "``*PPM*``".
        
        It is NOT the input string that should be the mask, but
        the `GXLST <geosoft.gxapi.GXLST>` items themselves
        
        This function was designed originally for geochemical
        processes in order to identify if a given channel name
        indicates that the channel should be given the "Assay" class.

        .. seealso::

            `assay_channel <geosoft.gxapi.GXLST.assay_channel>`
        """
        ret_val = self._wrapper.find_item_mask(type, name.encode())
        return ret_val




    def get_int(self, type, item):
        """
        Get an integer item.
        """
        ret_val = self._wrapper.get_int(type, item)
        return ret_val




    def insert_item(self, item, name, val):
        """
        Adds an item at a given location in the list.

        **Note:**

        Index must be 0 >= index >= list size.
        Items above the list index are shifted up one index value.
        """
        self._wrapper.insert_item(item, name.encode(), val.encode())
        




    def size(self):
        """
        Get the number of items in the list.
        """
        ret_val = self._wrapper.size()
        return ret_val




    def load_csv(self, csv, name_field, value_field):
        """
        Load a list with data from a CSV file

        **Note:**

        Both the Item and Value fields must be specified.
        The CSV file must be comma delimited, and have
        a header line with the field names.
        Leading and trailing spaces are removed in the names and values.
        """
        self._wrapper.load_csv(csv.encode(), name_field.encode(), value_field.encode())
        




    def load_file(self, file):
        """
        Set up a list from a list file.

        **Note:**

        A list file is an ASCII file that contains list entries.
        Each line for the file contains a list item name and an
        optional list item value.  The name and value must be
        delimited by a space, tab or comma.
        If the item name or value contains spaces, tabs or commas,
        it must be contined in quotes.
        blank lines and lines that begin with a '/' character are
        ignored.
        
        The default extension is .lst.  If the file cannot
        be found in the local directory, the GEOSOFT\\etc directory
        is searched.
        If it cannot be found, the list will be
        empty.  Not finding a file is not an error.
        """
        self._wrapper.load_file(file.encode())
        




    def resource(self, res):
        """
        Load a GX List Resource into this list object.  The
        entries are placed at the end of the list and are not
        sorted.
        """
        self._wrapper.resource(res.encode())
        




    def get_double(self, type, item):
        """
        Get a real item.
        """
        ret_val = self._wrapper.get_double(type, item)
        return ret_val




    def save_file(self, file):
        """
        Save a list to a file.

        **Note:**

        A list file is an ASCII file that contains list entries.
        Each line for the file contains a list item name and an
        optional list item value.  The name and value must be
        delimited by a space, tab or comma.
        If the item name or value contains spaces, tabs or commas,
        it must be contined in quotes.
        blank lines and lines that begin with a '/' character are
        ignored.
        
        The default extension is .lst.  If the file has a full path
        it will be created as specified.  Otherwise we look for the
        file in the local then the GEOSOFT\\etc directory.  If the file
        does not exist it will be created in the GEOSOFT\\etc directory.
        """
        self._wrapper.save_file(file.encode())
        




    def select_csv_string_items(self, buff, ls_to):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with items from a second `GXLST <geosoft.gxapi.GXLST>` found in a CSV string.

        **Note:**

        Items in the input string must be separated with
        commas. Parsing uses the sCommaTokens_GS function.
        Both the name and value of the input `GXLST <geosoft.gxapi.GXLST>` items whose
        name matches an item in the input string are
        copied to the output `GXLST <geosoft.gxapi.GXLST>`.
        Items are copied in the same order they appear in the
        input string. Items in the string not found in the input `GXLST <geosoft.gxapi.GXLST>`
        are ignored, and no error is registered.
        Item matches are case-tolerant.
        """
        self._wrapper.select_csv_string_items(buff.encode(), ls_to._wrapper)
        




    def serial(self, bf):
        """
        Serialize `GXLST <geosoft.gxapi.GXLST>` to a `GXBF <geosoft.gxapi.GXBF>`.
        """
        self._wrapper.serial(bf._wrapper)
        




    def set_item(self, type, item, buff):
        """
        Place an item at a specified point in the `GXLST <geosoft.gxapi.GXLST>`.

        **Note:**

        The existing item at the given index will be replaced.
        """
        self._wrapper.set_item(type, item, buff.encode())
        




    def sort(self, type, ord):
        """
        Sorts a list.
        """
        self._wrapper.sort(type, ord)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer