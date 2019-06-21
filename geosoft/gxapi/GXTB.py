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
class GXTB(gxapi_cy.WrapTB):
    """
    GXTB class.

    The `GXTB <geosoft.gxapi.GXTB>` class is a high-performance table class used to
    perform table-based processing, such as leveling data in
    an OASIS database. The `GXLTB <geosoft.gxapi.GXLTB>` class is recommended for use
    with small tables produced from short lists such as the
    different geographic projections and their defining parameters.
    """

    def __init__(self, handle=0):
        super(GXTB, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTB <geosoft.gxapi.GXTB>`
        
        :returns: A null `GXTB <geosoft.gxapi.GXTB>`
        :rtype:   GXTB
        """
        return GXTB()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def set_search_mode(self, mode):
        """
        Set the search mode of a table.
        
        :param mode:  :ref:`TB_SEARCH`
        :type  mode:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If performance is an issue, you may want to test which search
        mode provides the best performance with typical data.
        """
        self._set_search_mode(mode)
        




    def set_sort_mode(self, mode):
        """
        Set the sort mode of a table.
        
        :param mode:  :ref:`TB_SORT`
        :type  mode:  int

        .. versionadded:: 9.3.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_sort_mode(mode)
        



    @classmethod
    def create(cls, name):
        """
        Loads a table into memory and return a table handle.
        
        :param name:  Name of the table file to load
        :type  name:  str

        :returns:     `GXTB <geosoft.gxapi.GXTB>` Object
        :rtype:       GXTB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the table contains fewer data columns than are defined by the
        the table header, the `GXTB <geosoft.gxapi.GXTB>` object will read in the table and dummy
        the elements of the missing data columns.
        """
        ret_val = gxapi_cy.WrapTB._create(GXContext._get_tls_geo(), name.encode())
        return GXTB(ret_val)



    @classmethod
    def create_db(cls, db):
        """
        Create a table from a database.
        
        :param db:  Database
        :type  db:  GXDB

        :returns:    `GXTB <geosoft.gxapi.GXTB>` Object
        :rtype:      GXTB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The table will contain fields for all channels in
        the database.

        The database is not loaded with data.  Use the `load_db <geosoft.gxapi.GXTB.load_db>`
        function to load data into the table.
        """
        ret_val = gxapi_cy.WrapTB._create_db(GXContext._get_tls_geo(), db)
        return GXTB(ret_val)



    @classmethod
    def create_ltb(cls, ltb):
        """
        Create a table from an `GXLTB <geosoft.gxapi.GXLTB>` database.
        
        :param ltb:  `GXLTB <geosoft.gxapi.GXLTB>` object
        :type  ltb:  GXLTB

        :returns:    `GXTB <geosoft.gxapi.GXTB>` Object
        :rtype:      GXTB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapTB._create_ltb(GXContext._get_tls_geo(), ltb)
        return GXTB(ret_val)






    def field(self, name):
        """
        Get a field handle.
        
        :param name:  Field name
        :type  name:  str

        :returns:     The handle to the field (must be present)
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._field(name.encode())
        return ret_val




    def get_string(self, row, col, val):
        """
        Gets a string value from a table element.
        
        :param row:  Row of element to Get
        :param col:  Column of element to Get
        :param val:  Returned string
        :type  row:  int
        :type  col:  int
        :type  val:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        val.value = self._get_string(row, col, val.value.encode())
        




    def data_type(self, col):
        """
        Returns the data type for the specified column.
        
        :param col:  Column of element to Get
        :type  col:  int

        :returns:    :ref:`DB_CATEGORY_CHAN`
        :rtype:      int

        .. versionadded:: 5.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._data_type(col)
        return ret_val




    def find_col_by_index(self, idx, name):
        """
        Finds a column's name by its index.
        
        :param idx:   Index of column to find
        :param name:  Buffer for column name
        :type  idx:   int
        :type  name:  str_ref

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        name.value = self._find_col_by_index(idx, name.value.encode())
        




    def find_col_by_name(self, name):
        """
        Finds a column's index by its name.
        
        :param name:  Name of column to find
        :type  name:  str

        :returns:     Index of column.
                      -1 if not found.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._find_col_by_name(name.encode())
        return ret_val




    def format(self, col):
        """
        Returns the channel format for the specified column.
        
        :param col:  Column of element to Get
        :type  col:  int

        :returns:    :ref:`DB_CHAN_FORMAT`
        :rtype:      int

        .. versionadded:: 5.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._format(col)
        return ret_val




    def get_int(self, row, col):
        """
        Gets an integer value from a table element.
        
        :param row:  Row of element to Get
        :param col:  Column of element to Get
        :type  row:  int
        :type  col:  int

        :returns:    Value
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_int(row, col)
        return ret_val




    def num_columns(self):
        """
        Gets the number of data fields (columns) in a table.
        

        :returns:    Number of columns
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._num_columns()
        return ret_val




    def num_rows(self):
        """
        Gets the number of data rows in a table.
        

        :returns:    Number of rows
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._num_rows()
        return ret_val




    def load_db(self, db, line):
        """
        Load a database into a `GXTB <geosoft.gxapi.GXTB>`
        
        :param db:    Database
        :param line:  Line
        :type  db:    GXDB
        :type  line:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The line is appended to the data already in the table.
        """
        self._load_db(db, line)
        




    def get_double(self, row, col):
        """
        Gets an real value from a table element.
        
        :param row:  Row of element to Get
        :param col:  Column of element to Get
        :type  row:  int
        :type  col:  int

        :returns:    Value
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_double(row, col)
        return ret_val




    def save(self, name):
        """
        Saves the data in a table to a file. The table header will be
        in ASCII and the data will be in BINARY format.
        
        :param name:  Name of File to save table into
        :type  name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._save(name.encode())
        




    def save_db(self, db, line):
        """
        Save a `GXTB <geosoft.gxapi.GXTB>` in a database line
        
        :param db:    Database
        :param line:  Line
        :type  db:    GXDB
        :type  line:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Missing channels are created.
        Data in existing channels on the line will be replaced.
        """
        self._save_db(db, line)
        




    def save_to_ascii(self, name):
        """
        Saves the data in a table to a file. The table header will be
        in ASCII and the data will be in ASCII format.
        
        :param name:  Name of File to save table into
        :type  name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._save_to_ascii(name.encode())
        




    def set_int(self, row, col, val):
        """
        Sets an integer value into a table element.
        
        :param row:  Row of element to set
        :param col:  Column of element to set
        :param val:  Value to set
        :type  row:  int
        :type  col:  int
        :type  val:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The table field containing the element to be set MUST be
        of type `GS_BYTE <geosoft.gxapi.GS_BYTE>`, `GS_USHORT <geosoft.gxapi.GS_USHORT>`, `GS_SHORT <geosoft.gxapi.GS_SHORT>`, or `GS_LONG <geosoft.gxapi.GS_LONG>`.
        If the field is `GS_BYTE <geosoft.gxapi.GS_BYTE>`, `GS_USHORT <geosoft.gxapi.GS_USHORT>`, or `GS_LONG <geosoft.gxapi.GS_LONG>`, the new data
        value will cause an overflow if the value is out of range of
        the data type. The new element value will then be invalid.

        If the row of the new element exceeds the number of rows in
        the table, then the table will AUTOMATICALLY be EXPANDED to
        exactly as many rows needed to hold the new element. The new
        element is placed in the proper field of the last row, and
        all other field elements have invalid data. All fields of
        the new rows up to the new element's row will also contain
        invalid data.
        """
        self._set_int(row, col, val)
        




    def set_double(self, row, col, val):
        """
        Sets an real value into a table element.
        
        :param row:  Row of element to set
        :param col:  Column of element to set
        :param val:  Value to set
        :type  row:  int
        :type  col:  int
        :type  val:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The table field containing the element to be set MUST be
        of type `GS_FLOAT <geosoft.gxapi.GS_FLOAT>` or `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`.
        If the field is `GS_FLOAT <geosoft.gxapi.GS_FLOAT>` the new data value will cause an
        overflow if the value is out of range of the data type.
        The new element value will then be invalid.

        If the row of the new element exceeds the number of rows in
        the table, then the table will AUTOMATICALLY be EXPANDED to
        exactly as many rows needed to hold the new element. The new
        element is placed in the proper field of the last row, and
        all other field elements have invalid data. All fields of
        the new rows up to the new element's row will also contain
        invalid data.
        """
        self._set_double(row, col, val)
        




    def set_string(self, row, col, val):
        """
        Sets a string value into a table element.
        
        :param row:  Row of element to set
        :param col:  Column of element to set
        :param val:  Value to set
        :type  row:  int
        :type  col:  int
        :type  val:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The table field containing the element to be set MUST be
        of 'string'.

        If the row of the new element exceeds the number of rows in
        the table, then the table will AUTOMATICALLY be EXPANDED to
        exactly as many rows needed to hold the new element. The new
        element is placed in the proper field of the last row, and
        all other field elements have invalid data. All fields of
        the new rows up to the new element's row will also contain
        invalid data.
        """
        self._set_string(row, col, val.encode())
        




    def sort(self, col):
        """
        Sorts a table by a specified column.
        
        :param col:  Index of data Column to sort table by
        :type  col:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the column to sort by contains duplicated values, the
        sorted table is NOT guaranteed to retain the ordering of
        the duplicated values/
        E.g. Given 2 rows of values:   xx   yy   1
        bb   aa   1
        If the table is sorted on column 3, the second row
        may or may not come after the first row in the sorted
        table.
        """
        self._sort(col)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer