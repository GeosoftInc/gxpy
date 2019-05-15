### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXLST(gxapi_cy.WrapLST):
    """
    GXLST class.

    The `GXLST <geosoft.gxapi.GXLST>` class is used to create and retrieve lists,
    and to perform specific actions on lists, including
    retrieving list items, sorting lists and adding or
    removing list items.
    """

    def __init__(self, handle=0):
        super(GXLST, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXLST <geosoft.gxapi.GXLST>`
        
        :returns: A null `GXLST <geosoft.gxapi.GXLST>`
        :rtype:   GXLST
        """
        return GXLST()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def add_item(self, name, val):
        """
        Adds an item to the end of the list.
        
        :param name:  Name of the Item
        :param val:   Value of the Item
        :type  name:  str
        :type  val:   str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._add_item(name.encode(), val.encode())
        




    def add_symb_item(self, name, symb):
        """
        Adds a channel/line/blob name and symbol to a list.
        
        :param name:  Name of the channel, line or blob symbol
        :param symb:  Symbol handle
        :type  name:  str
        :type  symb:  int

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A number of `GXDB <geosoft.gxapi.GXDB>` functions return LSTs with the channel
        or line name in the "Name" part of a `GXLST <geosoft.gxapi.GXLST>`, and the
        handle (DB_SYMB) in the value part. This function lets
        you quickly add a new item without the need of coverting
        the handle into a string value.
        """
        self._add_symb_item(name.encode(), symb)
        




    def add_unique_item(self, name, val):
        """
        Adds a unique item to the end of the list.
        
        :param name:  Name of the Item
        :param val:   Value of the Item
        :type  name:  str
        :type  val:   str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Existing items that match the name are first removed.
        """
        self._add_unique_item(name.encode(), val.encode())
        




    def append(self, lst2):
        """
        Add the items in one list to another list.
        
        :param lst2:  List to append to the above `GXLST <geosoft.gxapi.GXLST>`.
        :type  lst2:  GXLST

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Item names and values are added using "`add_unique_item <geosoft.gxapi.GXLST.add_unique_item>`",
        so that existing items with the same name are replaced, and if
        items are duplicated in the appended `GXLST <geosoft.gxapi.GXLST>`, the last one will be
        the one to remain after the process is complete.
        """
        self._append(lst2)
        



    @classmethod
    def assay_channel(cls):
        """
        Create a `GXLST <geosoft.gxapi.GXLST>` of assay channel mask strings from file.
        

        :returns:    `GXLST <geosoft.gxapi.GXLST>` Object
        :rtype:      GXLST

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Searches the local directory, then user\\etc, then \\etc to see
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
        ret_val = gxapi_cy.WrapLST._assay_channel(GXContext._get_tls_geo())
        return GXLST(ret_val)




    def clear(self):
        """
        Clear a list object.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._clear()
        




    def convert_from_csv_string(self, buff):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with items from a string.
        
        :param buff:  Comma separated items
        :type  buff:  str

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Items in the input buffer must be separated with
        commas.
        Both the Name and Value in the list are set to the
        item.
        """
        self._convert_from_csv_string(buff.encode())
        




    def copy(self, source):
        """
        Copy one `GXLST <geosoft.gxapi.GXLST>` object to another.
        
        :param source:  Source List to Copy from
        :type  source:  GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._copy(source)
        



    @classmethod
    def create(cls, width):
        """
        creates a user controllable list. The list
        is empty when created.
        
        :param width:  Width of the list to make. This number should be large enough for both the item name and the item value.  Must be > 2 and <= 4096.
        :type  width:  int

        :returns:      Handle to the List Object.
        :rtype:        GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapLST._create(GXContext._get_tls_geo(), width)
        return GXLST(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create `GXLST <geosoft.gxapi.GXLST>` from serialized source.
        
        :type  bf:  GXBF

        :returns:    `GXLST <geosoft.gxapi.GXLST>` object
        :rtype:      GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapLST._create_s(GXContext._get_tls_geo(), bf)
        return GXLST(ret_val)




    def del_item(self, item):
        """
        Removes an item from the list. All items below
        it are shifted up one.
        
        :param item:  Item Number to Delete
        :type  item:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._del_item(item)
        






    def find_items(self, type, lst2, vv):
        """
        Searches a `GXLST <geosoft.gxapi.GXLST>` for items in a second `GXLST <geosoft.gxapi.GXLST>`, returns indices of those found.
        
        :param type:  :ref:`LST_ITEM` data to do the search on
        :param lst2:  Items to search for
        :param vv:    `GS_LONG <geosoft.gxapi.GS_LONG>` `GXVV <geosoft.gxapi.GXVV>` of returned indices into the first `GXLST <geosoft.gxapi.GXLST>`.
        :type  type:  int
        :type  lst2:  GXLST
        :type  vv:    GXVV

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is a much more efficient way of determining if items in
        one `GXLST <geosoft.gxapi.GXLST>` are found in a second, than by calling `find_item <geosoft.gxapi.GXLST.find_item>`
        repeatedly in a loop.
        The returned INT `GXVV <geosoft.gxapi.GXVV>` contains the same number of items as
        the "search items" `GXLST <geosoft.gxapi.GXLST>`, and contains -1 for items where the
        value is not found, and the index of items that are found.
        Comparisons are case-tolerant.
        """
        self._find_items(type, lst2, vv)
        




    def gt_item(self, type, item, buff):
        """
        This places the specified item into the buffer provided.
        
        :param type:  :ref:`LST_ITEM` data to retrieve
        :param item:  Item Number to Get
        :param buff:  Buffer to Place Item Into
        :type  type:  int
        :type  item:  int
        :type  buff:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If item number is not in the list, the buffer will be "".
        """
        buff.value = self._gt_item(type, item, buff.value.encode())
        




    def gt_symb_item(self, item, name, symb):
        """
        Returns a channel/line/blob name and symbol from a list.
        
        :param item:  Item number to get
        :param name:  Buffer to Place Symbol name into
        :param symb:  Symbol handle
        :type  item:  int
        :type  name:  str_ref
        :type  symb:  int_ref

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A number of `GXDB <geosoft.gxapi.GXDB>` functions return LSTs with the channel
        or line name in the "Name" part of a `GXLST <geosoft.gxapi.GXLST>`, and the
        handle (DB_SYMB) in the value part. This function lets
        you quickly retrieve both the name and symbol handle
        for a given item, which needing to convert between types.
        """
        name.value, symb.value = self._gt_symb_item(item, name.value.encode(), symb.value)
        




    def convert_to_csv_string(self, buff):
        """
        Load a string with names from a `GXLST <geosoft.gxapi.GXLST>`.
        
        :param buff:  Buffer to add items to
        :type  buff:  str_ref

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The list name values are put into a string,
        items separated by commas.
        """
        buff.value = self._convert_to_csv_string(buff.value.encode())
        




    def find_item(self, type, name):
        """
        Searches the list for a specified item.
        
        :param type:  :ref:`LST_ITEM` data to do the search on
        :param name:  String to Search For
        :type  type:  int
        :type  name:  str

        :returns:     x  - Item Number
                      -1 - Not Found
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Comparisons are case-tolerant.
        """
        ret_val = self._find_item(type, name.encode())
        return ret_val




    def find_item_mask(self, type, name):
        """
        Searches the list for a specified item, list contains masks.
        
        :param type:  :ref:`LST_ITEM` data to search
        :param name:  String to try `GXLST <geosoft.gxapi.GXLST>` mask items on Search For
        :type  type:  int
        :type  name:  str

        :returns:     x  - Item Number
                      -1 - Not Found
        :rtype:       int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Comparsions are case-intolerant (unlike `find_item <geosoft.gxapi.GXLST.find_item>`).
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
        ret_val = self._find_item_mask(type, name.encode())
        return ret_val




    def get_int(self, type, item):
        """
        Get an integer item.
        
        :param type:  :ref:`LST_ITEM` data to retrieve
        :param item:  Item Number to Get
        :type  type:  int
        :type  item:  int

        :returns:     Integer, `iDUMMY <geosoft.gxapi.iDUMMY>` if conversion fails or string is empty.
        :rtype:       int

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_int(type, item)
        return ret_val




    def insert_item(self, item, name, val):
        """
        Adds an item at a given location in the list.
        
        :param item:  Item index
        :param name:  Name of the Item
        :param val:   Value of the Item
        :type  item:  int
        :type  name:  str
        :type  val:   str

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Index must be 0 >= index >= list size.
        Items above the list index are shifted up one index value.
        """
        self._insert_item(item, name.encode(), val.encode())
        




    def size(self):
        """
        Get the number of items in the list.
        

        :returns:    x - Number of items in the list.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._size()
        return ret_val




    def load_csv(self, csv, name_field, value_field):
        """
        Load a list with data from a CSV file
        
        :param csv:          The CSV file
        :param name_field:   Column label for the item name
        :param value_field:  Column label for the item value
        :type  csv:          str
        :type  name_field:   str
        :type  value_field:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Both the Item and Value fields must be specified.
        The CSV file must be comma delimited, and have
        a header line with the field names.
        Leading and trailing spaces are removed in the names and values.
        """
        self._load_csv(csv.encode(), name_field.encode(), value_field.encode())
        




    def load_file(self, file):
        """
        Set up a list from a list file.
        
        :param file:  Name of the file
        :type  file:  str

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A list file is an ASCII file that contains list entries.
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
        self._load_file(file.encode())
        




    def resource(self, res):
        """
        Load a GX List Resource into this list object.  The
        entries are placed at the end of the list and are not
        sorted.
        
        :param res:  Name of the Resource
        :type  res:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._resource(res.encode())
        




    def get_double(self, type, item):
        """
        Get a real item.
        
        :param type:  :ref:`LST_ITEM` data to retrieve
        :param item:  Item Number to Get
        :type  type:  int
        :type  item:  int

        :returns:     Real, `rDUMMY <geosoft.gxapi.rDUMMY>` if conversion fails or string is empty.
        :rtype:       float

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_double(type, item)
        return ret_val




    def save_file(self, file):
        """
        Save a list to a file.
        
        :param file:  Name of the file
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** A list file is an ASCII file that contains list entries.
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
        self._save_file(file.encode())
        




    def select_csv_string_items(self, buff, ls_to):
        """
        Load a `GXLST <geosoft.gxapi.GXLST>` with items from a second `GXLST <geosoft.gxapi.GXLST>` found in a CSV string.
        
        :param buff:   Comma separated item names
        :param ls_to:  `GXLST <geosoft.gxapi.GXLST>` to add selected items to
        :type  buff:   str
        :type  ls_to:  GXLST

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Items in the input string must be separated with
        commas. Parsing uses the sCommaTokens_GS function.
        Both the name and value of the input `GXLST <geosoft.gxapi.GXLST>` items whose
        name matches an item in the input string are
        copied to the output `GXLST <geosoft.gxapi.GXLST>`.
        Items are copied in the same order they appear in the
        input string. Items in the string not found in the input `GXLST <geosoft.gxapi.GXLST>`
        are ignored, and no error is registered.
        Item matches are case-tolerant.
        """
        self._select_csv_string_items(buff.encode(), ls_to)
        




    def serial(self, bf):
        """
        Serialize `GXLST <geosoft.gxapi.GXLST>` to a `GXBF <geosoft.gxapi.GXBF>`.
        
        :type  bf:   GXBF

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._serial(bf)
        




    def set_item(self, type, item, buff):
        """
        Place an item at a specified point in the `GXLST <geosoft.gxapi.GXLST>`.
        
        :param type:  :ref:`LST_ITEM` data to insert
        :param item:  Item Number to Set
        :param buff:  Item to Set
        :type  type:  int
        :type  item:  int
        :type  buff:  str

        .. versionadded:: 5.1.5

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The existing item at the given index will be replaced.
        """
        self._set_item(type, item, buff.encode())
        




    def sort(self, type, ord):
        """
        Sorts a list.
        
        :param type:  :ref:`LST_ITEM` data to sort on
        :param ord:   0 - Ascending, 1 - Decending
        :type  type:  int
        :type  ord:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._sort(type, ord)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer