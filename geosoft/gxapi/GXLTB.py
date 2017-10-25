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
class GXLTB:
    """
    GXLTB class.

    An :class:`geosoft.gxapi.GXLTB` object is typically created from a CSV (comma-separated values)
    file, and is a table of information that may be accessed by row
    or column. The :class:`geosoft.gxapi.GXLTB` class is recommended for use with small tables
    produced from short lists (of the order of 1000's or records) such
    as the different geographic projections and their defining parameters.
    Large tables, such as those required for table-lookup functions, should
    be accessed using the :class:`geosoft.gxapi.GXTB` class.

    **Note:**

    An :class:`geosoft.gxapi.GXLTB` ASCII table file has the following structure:
    
    / comments
    key_name,col_1,col_2,col_3,etc...    /field names
    key_1,token,token,token,etc...       /data lines
    key_2,token,token,token,etc...
    etc...
    
    The first column must be the key column (all entries unique).
    
    The header line is optional and can be used to find entries.
    
    Comment and empty lines are ignored.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapLTB(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXLTB`
        
        :returns: A null :class:`geosoft.gxapi.GXLTB`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXLTB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXLTB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_record(self, p2, p3):
        """
        Add a new record.

        **Note:**

        If the record exists, the existing record is cleared
        and the record number is returned.
        """
        p3.value = self._wrapper.add_record(p2.encode(), p3.value)
        




    def contract(self, p2):
        """
        Contract the contents of two same-key and same-fields tables.

        **Note:**

        The "Key" of the child must be the same as the "Key" of the Master.
        The fields of two :class:`geosoft.gxapi.GXLTB` must be the same.
        
        Contracting takes place as follows:
        
        1. The Master :class:`geosoft.gxapi.GXLTB` is copied to the New :class:`geosoft.gxapi.GXLTB`.
        2. All records in the contract LIB are deleted from the New :class:`geosoft.gxapi.GXLTB` (if there are any)
        3. The New :class:`geosoft.gxapi.GXLTB` is returned.
        """
        ret_val = self._wrapper.contract(p2._wrapper)
        return GXLTB(ret_val)



    @classmethod
    def create(cls, p1, p2, p3, p4):
        """
        Creates a :class:`geosoft.gxapi.GXLTB` object from a file.

        **Note:**

        If the file has no header, field names are assumed to be "0", "1", etc.
        """
        ret_val = gxapi_cy.WrapLTB.create(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4.encode())
        return GXLTB(ret_val)



    @classmethod
    def create_crypt(cls, p1, p2, p3, p4, p5, p6):
        """
        Creates a :class:`geosoft.gxapi.GXLTB` object from an encrypted file.

        **Note:**

        If the file has no header, field names are assumed to be "0", "1", etc.
        """
        ret_val = gxapi_cy.WrapLTB.create_crypt(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5.encode(), p6.encode())
        return GXLTB(ret_val)



    @classmethod
    def create_ex(cls, p1, p2, p3, p4, p5):
        """
        Creates a :class:`geosoft.gxapi.GXLTB` object from a file.

        **Note:**

        If the file has no header, field names are assumed to be "0", "1", etc.
        """
        ret_val = gxapi_cy.WrapLTB.create_ex(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5.encode())
        return GXLTB(ret_val)




    def delete_record(self, p2):
        """
        Delete a record.

        **Note:**

        Record numbers after the deleted record will be reduced
        by 1.
        """
        self._wrapper.delete_record(p2)
        






    def get_con_lst(self, p2, p3, p4, p5):
        """
        Populate a :class:`geosoft.gxapi.GXLST` with :class:`geosoft.gxapi.GXLTB` names from matching fields.

        **Note:**

        The :class:`geosoft.gxapi.GXLST` object will be in the order of the file.
        The :class:`geosoft.gxapi.GXLST` names will be the :class:`geosoft.gxapi.GXLTB` key fields and the
        :class:`geosoft.gxapi.GXLST` values will be the :class:`geosoft.gxapi.GXLTB` record numbers.
        """
        self._wrapper.get_con_lst(p2, p3.encode(), p4, p5._wrapper)
        




    def get_lst(self, p2, p3):
        """
        Populate an :class:`geosoft.gxapi.GXLST` with :class:`geosoft.gxapi.GXLTB` names

        **Note:**

        The :class:`geosoft.gxapi.GXLST` object will be in the order of the file.
        The :class:`geosoft.gxapi.GXLST` names will be the :class:`geosoft.gxapi.GXLTB` fields and the
        :class:`geosoft.gxapi.GXLST` values will be the :class:`geosoft.gxapi.GXLTB` record numbers.
        """
        self._wrapper.get_lst(p2, p3._wrapper)
        




    def get_lst2(self, p2, p3, p4):
        """
        Populate an :class:`geosoft.gxapi.GXLST` with :class:`geosoft.gxapi.GXLTB` names and values

        **Note:**

        The :class:`geosoft.gxapi.GXLST` object will be in the order of the file.
        The :class:`geosoft.gxapi.GXLST` names will come from the :class:`geosoft.gxapi.GXLTB` name field and the
        :class:`geosoft.gxapi.GXLST` values will come from value field specified.
        """
        self._wrapper.get_lst2(p2, p3, p4._wrapper)
        




    def fields(self):
        """
        Get number of fields.
        """
        ret_val = self._wrapper.fields()
        return ret_val




    def find_field(self, p2):
        """
        Return the field number for the specified field.
        """
        ret_val = self._wrapper.find_field(p2.encode())
        return ret_val




    def find_key(self, p2):
        """
        Return the key index of a record.
        """
        ret_val = self._wrapper.find_key(p2.encode())
        return ret_val




    def get_field(self, p2, p3):
        """
        Get a field name by index.

        **Note:**

        If the record or field are out of range, an empty string is returned.
        """
        p3.value = self._wrapper.get_field(p2, p3.value.encode())
        




    def get_int(self, p2, p3):
        """
        Get a int entry from the :class:`geosoft.gxapi.GXLTB`
        """
        ret_val = self._wrapper.get_int(p2, p3)
        return ret_val




    def get_string(self, p2, p3, p4):
        """
        Get an entry from the :class:`geosoft.gxapi.GXLTB`

        **Note:**

        If the record or field are out of range,
        an empty string or dummy value is returned.
        """
        p4.value = self._wrapper.get_string(p2, p3, p4.value.encode())
        




    def get_english_string(self, p2, p3, p4):
        """
        Get the English entry from the :class:`geosoft.gxapi.GXLTB`

        **Note:**

        If the record or field are out of range,
        an empty string or dummy value is returned.
        """
        p4.value = self._wrapper.get_english_string(p2, p3, p4.value.encode())
        




    def records(self):
        """
        Get number of records in :class:`geosoft.gxapi.GXLTB`.
        """
        ret_val = self._wrapper.records()
        return ret_val




    def search(self, p2, p3, p4):
        """
        Search for a record containing field value
        """
        ret_val = self._wrapper.search(p2, p3, p4.encode())
        return ret_val




    def merge(self, p2):
        """
        Merge the contents of two same-key tables.

        **Note:**

        Merging takes place as follows:
        
        1. The "Key" of the child must be the same as the "Key" of the Master.
        2. The fields of the Master :class:`geosoft.gxapi.GXLTB` are collected in-order.
        3. Any new fields of the Child :class:`geosoft.gxapi.GXLTB` are added to the end of the list.
        4. A new :class:`geosoft.gxapi.GXLTB` is created to contain the new field list (in-order).
        5. The Child table contents are added to the New :class:`geosoft.gxapi.GXLTB`.
        6. The Master table contents are added/replace the New :class:`geosoft.gxapi.GXLTB`.
        7. The New :class:`geosoft.gxapi.GXLTB` is returned.
        
        If the fields of the Master and Child are the same, steps 4, 5, 6 are
        replaced by:
        
        4. The Master :class:`geosoft.gxapi.GXLTB` is copied to the New :class:`geosoft.gxapi.GXLTB`.
        5. Any New records found in the child are added to the New :class:`geosoft.gxapi.GXLTB`
        """
        ret_val = self._wrapper.merge(p2._wrapper)
        return GXLTB(ret_val)




    def get_double(self, p2, p3):
        """
        Get a real entry from the :class:`geosoft.gxapi.GXLTB`
        """
        ret_val = self._wrapper.get_double(p2, p3)
        return ret_val




    def save(self, p2):
        """
        Save :class:`geosoft.gxapi.GXLTB` changes to existing or new file
        """
        self._wrapper.save(p2.encode())
        




    def save_crypt(self, p2, p3):
        """
        Save :class:`geosoft.gxapi.GXLTB` to a new file using encryption
        """
        self._wrapper.save_crypt(p2.encode(), p3.encode())
        




    def set_int(self, p2, p3, p4):
        """
        Set a long entry
        """
        self._wrapper.set_int(p2, p3, p4)
        




    def set_double(self, p2, p3, p4):
        """
        Set a double entry
        """
        self._wrapper.set_double(p2, p3, p4)
        




    def set_string(self, p2, p3, p4):
        """
        Set an entry
        """
        self._wrapper.set_string(p2, p3, p4.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer