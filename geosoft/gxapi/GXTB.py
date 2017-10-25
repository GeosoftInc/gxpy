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
class GXTB:
    """
    GXTB class.

    The `GXTB` class is a high-performance table class used to
    perform table-based processing, such as leveling data in
    an OASIS database. The `GXLTB` class is recommended for use
    with small tables produced from short lists such as the
    different geographic projections and their defining parameters.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapTB(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXTB`
        
        :returns: A null `GXTB`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXTB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXTB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def set_search_mode(self, p2):
        """
        Set the search mode of a table.

        **Note:**

        If performance is an issue, you may want to test which search
        mode provides the best performance with typical data.
        """
        self._wrapper.set_search_mode(p2)
        



    @classmethod
    def create(cls, p1):
        """
        Loads a table into memory and return a table handle.

        **Note:**

        If the table contains fewer data columns than are defined by the
        the table header, the `GXTB` object will read in the table and dummy
        the elements of the missing data columns.
        """
        ret_val = gxapi_cy.WrapTB.create(GXContext._get_tls_geo(), p1.encode())
        return GXTB(ret_val)



    @classmethod
    def create_db(cls, p1):
        """
        Create a table from a database.

        **Note:**

        The table will contain fields for all channels in
        the database.
        
        The database is not loaded with data.  Use the `load_db`
        function to load data into the table.
        """
        ret_val = gxapi_cy.WrapTB.create_db(GXContext._get_tls_geo(), p1._wrapper)
        return GXTB(ret_val)



    @classmethod
    def create_ltb(cls, p1):
        """
        Create a table from an `GXLTB` database.
        """
        ret_val = gxapi_cy.WrapTB.create_ltb(GXContext._get_tls_geo(), p1._wrapper)
        return GXTB(ret_val)






    def field(self, p2):
        """
        Get a field handle.
        """
        ret_val = self._wrapper.field(p2.encode())
        return ret_val




    def get_string(self, p2, p3, p4):
        """
        Gets a string value from a table element.
        """
        p4.value = self._wrapper.get_string(p2, p3, p4.value.encode())
        




    def data_type(self, p2):
        """
        Returns the data type for the specified column.
        """
        ret_val = self._wrapper.data_type(p2)
        return ret_val




    def find_col_by_index(self, p2, p3):
        """
        Finds a column's name by its index.
        """
        p3.value = self._wrapper.find_col_by_index(p2, p3.value.encode())
        




    def find_col_by_name(self, p2):
        """
        Finds a column's index by its name.
        """
        ret_val = self._wrapper.find_col_by_name(p2.encode())
        return ret_val




    def format(self, p2):
        """
        Returns the channel format for the specified column.
        """
        ret_val = self._wrapper.format(p2)
        return ret_val




    def get_int(self, p2, p3):
        """
        Gets an integer value from a table element.
        """
        ret_val = self._wrapper.get_int(p2, p3)
        return ret_val




    def num_columns(self):
        """
        Gets the number of data fields (columns) in a table.
        """
        ret_val = self._wrapper.num_columns()
        return ret_val




    def num_rows(self):
        """
        Gets the number of data rows in a table.
        """
        ret_val = self._wrapper.num_rows()
        return ret_val




    def load_db(self, p2, p3):
        """
        Load a database into a `GXTB`

        **Note:**

        The line is appended to the data already in the table.
        """
        self._wrapper.load_db(p2._wrapper, p3)
        




    def get_double(self, p2, p3):
        """
        Gets an real value from a table element.
        """
        ret_val = self._wrapper.get_double(p2, p3)
        return ret_val




    def save(self, p2):
        """
        Saves the data in a table to a file. The table header will be
        in ASCII and the data will be in BINARY format.
        """
        self._wrapper.save(p2.encode())
        




    def save_db(self, p2, p3):
        """
        Save a `GXTB` in a database line

        **Note:**

        Missing channels are created.
        Data in existing channels on the line will be replaced.
        """
        self._wrapper.save_db(p2._wrapper, p3)
        




    def save_to_ascii(self, p2):
        """
        Saves the data in a table to a file. The table header will be
        in ASCII and the data will be in ASCII format.
        """
        self._wrapper.save_to_ascii(p2.encode())
        




    def set_int(self, p2, p3, p4):
        """
        Sets an integer value into a table element.

        **Note:**

        The table field containing the element to be set MUST be
        of type `GS_BYTE`, `GS_USHORT`, `GS_SHORT`, or `GS_LONG`.
        If the field is `GS_BYTE`, `GS_USHORT`, or `GS_LONG`, the new data
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
        self._wrapper.set_int(p2, p3, p4)
        




    def set_double(self, p2, p3, p4):
        """
        Sets an real value into a table element.

        **Note:**

        The table field containing the element to be set MUST be
        of type `GS_FLOAT` or `GS_DOUBLE`.
        If the field is `GS_FLOAT` the new data value will cause an
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
        self._wrapper.set_double(p2, p3, p4)
        




    def set_string(self, p2, p3, p4):
        """
        Sets a string value into a table element.

        **Note:**

        The table field containing the element to be set MUST be
        of 'string'.
        
        If the row of the new element exceeds the number of rows in
        the table, then the table will AUTOMATICALLY be EXPANDED to
        exactly as many rows needed to hold the new element. The new
        element is placed in the proper field of the last row, and
        all other field elements have invalid data. All fields of
        the new rows up to the new element's row will also contain
        invalid data.
        """
        self._wrapper.set_string(p2, p3, p4.encode())
        




    def sort(self, p2):
        """
        Sorts a table by a specified column.

        **Note:**

        If the column to sort by contains duplicated values, the
        sorted table is NOT guaranteed to retain the ordering of
        the duplicated values/
        E.g. Given 2 rows of values:   xx   yy   1
        bb   aa   1
        If the table is sorted on column 3, the second row
        may or may not come after the first row in the sorted
        table.
        """
        self._wrapper.sort(p2)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer