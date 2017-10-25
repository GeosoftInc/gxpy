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

    The :class:`geosoft.gxapi.GXLST` class is used to create and retrieve lists,
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
        A null (undefined) instance of :class:`geosoft.gxapi.GXLST`
        
        :returns: A null :class:`geosoft.gxapi.GXLST`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXLST` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXLST`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_item(self, p2, p3):
        """
        Adds an item to the end of the list.
        """
        self._wrapper.add_item(p2.encode(), p3.encode())
        




    def add_symb_item(self, p2, p3):
        """
        Adds a channel/line/blob name and symbol to a list.

        **Note:**

        A number of :class:`geosoft.gxapi.GXDB` functions return LSTs with the channel
        or line name in the "Name" part of a :class:`geosoft.gxapi.GXLST`, and the
        handle (DB_SYMB) in the value part. This function lets
        you quickly add a new item without the need of coverting
        the handle into a string value.
        """
        self._wrapper.add_symb_item(p2.encode(), p3)
        




    def add_unique_item(self, p2, p3):
        """
        Adds a unique item to the end of the list.

        **Note:**

        Existing items that match the name are first removed.
        """
        self._wrapper.add_unique_item(p2.encode(), p3.encode())
        




    def append(self, p2):
        """
        Add the items in one list to another list.

        **Note:**

        Item names and values are added using "AddUniqueItem_LST",
        so that existing items with the same name are replaced, and if
        items are duplicated in the appended :class:`geosoft.gxapi.GXLST`, the last one will be
        the one to remain after the process is complete.
        """
        self._wrapper.append(p2._wrapper)
        



    @classmethod
    def assay_channel(cls):
        """
        Create a :class:`geosoft.gxapi.GXLST` of assay channel mask strings from file.

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
        """
        ret_val = gxapi_cy.WrapLST.assay_channel(GXContext._get_tls_geo())
        return GXLST(ret_val)




    def clear(self):
        """
        Clear a list object.
        """
        self._wrapper.clear()
        




    def convert_from_csv_string(self, p2):
        """
        Load a :class:`geosoft.gxapi.GXLST` with items from a string.

        **Note:**

        Items in the input buffer must be separated with
        commas.
        Both the Name and Value in the list are set to the
        item.
        """
        self._wrapper.convert_from_csv_string(p2.encode())
        




    def copy(self, p2):
        """
        Copy one :class:`geosoft.gxapi.GXLST` object to another.
        """
        self._wrapper.copy(p2._wrapper)
        



    @classmethod
    def create(cls, p1):
        """
        creates a user controllable list. The list
        is empty when created.
        """
        ret_val = gxapi_cy.WrapLST.create(GXContext._get_tls_geo(), p1)
        return GXLST(ret_val)



    @classmethod
    def create_s(cls, p1):
        """
        Create :class:`geosoft.gxapi.GXLST` from serialized source.
        """
        ret_val = gxapi_cy.WrapLST.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXLST(ret_val)




    def del_item(self, p2):
        """
        Removes an item from the list. All items below
        it are shifted up one.
        """
        self._wrapper.del_item(p2)
        






    def find_items(self, p2, p3, p4):
        """
        Searches a :class:`geosoft.gxapi.GXLST` for items in a second :class:`geosoft.gxapi.GXLST`, returns indices of those found.

        **Note:**

        This is a much more efficient way of determining if items in
        one :class:`geosoft.gxapi.GXLST` are found in a second, than by calling iFindItem_LST
        repeatedly in a loop.
        The returned INT :class:`geosoft.gxapi.GXVV` contains the same number of items as
        the "search items" :class:`geosoft.gxapi.GXLST`, and contains -1 for items where the
        value is not found, and the index of items that are found.
        Comparisons are case-tolerant.
        """
        self._wrapper.find_items(p2, p3._wrapper, p4._wrapper)
        




    def gt_item(self, p2, p3, p4):
        """
        This places the specified item into the buffer provided.

        **Note:**

        If item number is not in the list, the buffer will be "".
        """
        p4.value = self._wrapper.gt_item(p2, p3, p4.value.encode())
        




    def gt_symb_item(self, p2, p3, p5):
        """
        Returns a channel/line/blob name and symbol from a list.

        **Note:**

        A number of :class:`geosoft.gxapi.GXDB` functions return LSTs with the channel
        or line name in the "Name" part of a :class:`geosoft.gxapi.GXLST`, and the
        handle (DB_SYMB) in the value part. This function lets
        you quickly retrieve both the name and symbol handle
        for a given item, which needing to convert between types.
        """
        p3.value, p5.value = self._wrapper.gt_symb_item(p2, p3.value.encode(), p5.value)
        




    def convert_to_csv_string(self, p2):
        """
        Load a string with names from a :class:`geosoft.gxapi.GXLST`.

        **Note:**

        The list name values are put into a string,
        items separated by commas.
        """
        p2.value = self._wrapper.convert_to_csv_string(p2.value.encode())
        




    def find_item(self, p2, p3):
        """
        Searches the list for a specified item.

        **Note:**

        Comparisons are case-tolerant.
        """
        ret_val = self._wrapper.find_item(p2, p3.encode())
        return ret_val




    def find_item_mask(self, p2, p3):
        """
        Searches the list for a specified item, list contains masks.

        **Note:**

        Comparsions are case-intolerant (unlike iFindItem_LST).
        This means items in the list such as "``*(ppm)``" will be
        found if the input search string is "Ni (ppm)" or "Ni(ppm)",
        but not if it is "Ni (PPM)", so you should include
        both "``*ppm*``" and "``*PPM*``".
        
        It is NOT the input string that should be the mask, but
        the :class:`geosoft.gxapi.GXLST` items themselves
        
        This function was designed originally for geochemical
        processes in order to identify if a given channel name
        indicates that the channel should be given the "Assay" class.
        """
        ret_val = self._wrapper.find_item_mask(p2, p3.encode())
        return ret_val




    def get_int(self, p2, p3):
        """
        Get an integer item.
        """
        ret_val = self._wrapper.get_int(p2, p3)
        return ret_val




    def insert_item(self, p2, p3, p4):
        """
        Adds an item at a given location in the list.

        **Note:**

        Index must be 0 >= index >= list size.
        Items above the list index are shifted up one index value.
        """
        self._wrapper.insert_item(p2, p3.encode(), p4.encode())
        




    def size(self):
        """
        Get the number of items in the list.
        """
        ret_val = self._wrapper.size()
        return ret_val




    def load_csv(self, p2, p3, p4):
        """
        Load a list with data from a CSV file

        **Note:**

        Both the Item and Value fields must be specified.
        The CSV file must be comma delimited, and have
        a header line with the field names.
        Leading and trailing spaces are removed in the names and values.
        """
        self._wrapper.load_csv(p2.encode(), p3.encode(), p4.encode())
        




    def load_file(self, p2):
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
        
        This function replaces the iLoadFile_LST function which
        actually always returned 0, or terminated on an error.
        """
        self._wrapper.load_file(p2.encode())
        




    def resource(self, p2):
        """
        Load a GX List Resource into this list object.  The
        entries are placed at the end of the list and are not
        sorted.
        """
        self._wrapper.resource(p2.encode())
        




    def get_double(self, p2, p3):
        """
        Get a real item.
        """
        ret_val = self._wrapper.get_double(p2, p3)
        return ret_val




    def save_file(self, p2):
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
        self._wrapper.save_file(p2.encode())
        




    def select_csv_string_items(self, p2, p3):
        """
        Load a :class:`geosoft.gxapi.GXLST` with items from a second :class:`geosoft.gxapi.GXLST` found in a CSV string.

        **Note:**

        Items in the input string must be separated with
        commas. Parsing uses the sCommaTokens_GS function.
        Both the name and value of the input :class:`geosoft.gxapi.GXLST` items whose
        name matches an item in the input string are
        copied to the output :class:`geosoft.gxapi.GXLST`.
        Items are copied in the same order they appear in the
        input string. Items in the string not found in the input :class:`geosoft.gxapi.GXLST`
        are ignored, and no error is registered.
        Item matches are case-tolerant.
        """
        self._wrapper.select_csv_string_items(p2.encode(), p3._wrapper)
        




    def serial(self, p2):
        """
        Serialize :class:`geosoft.gxapi.GXLST` to a :class:`geosoft.gxapi.GXBF`.
        """
        self._wrapper.serial(p2._wrapper)
        




    def set_item(self, p2, p3, p4):
        """
        Place an item at a specified point in the :class:`geosoft.gxapi.GXLST`.

        **Note:**

        The existing item at the given index will be replaced.
        """
        self._wrapper.set_item(p2, p3, p4.encode())
        




    def sort(self, p2, p3):
        """
        Sorts a list.
        """
        self._wrapper.sort(p2, p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer