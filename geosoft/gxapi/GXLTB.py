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

    An `GXLTB` object is typically created from a CSV (comma-separated values)
    file, and is a table of information that may be accessed by row
    or column. The `GXLTB` class is recommended for use with small tables
    produced from short lists (of the order of 1000's or records) such
    as the different geographic projections and their defining parameters.
    Large tables, such as those required for table-lookup functions, should
    be accessed using the `GXTB` class.

    **Note:**

    An `GXLTB` ASCII table file has the following structure:
    
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
        A null (undefined) instance of `GXLTB`
        
        :returns: A null `GXLTB`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXLTB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXLTB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def add_record(self, key, rec):
        """
        Add a new record.

        **Note:**

        If the record exists, the existing record is cleared
        and the record number is returned.
        """
        rec.value = self._wrapper.add_record(key.encode(), rec.value)
        




    def contract(self, lt_bc):
        """
        Contract the contents of two same-key and same-fields tables.

        **Note:**

        The "Key" of the child must be the same as the "Key" of the Master.
        The fields of two `GXLTB` must be the same.
        
        Contracting takes place as follows:
        
        1. The Master `GXLTB` is copied to the New `GXLTB`.
        2. All records in the contract LIB are deleted from the New `GXLTB` (if there are any)
        3. The New `GXLTB` is returned.
        """
        ret_val = self._wrapper.contract(lt_bc._wrapper)
        return GXLTB(ret_val)



    @classmethod
    def create(cls, file, type, delim, key):
        """
        Creates a `GXLTB` object from a file.

        **Note:**

        If the file has no header, field names are assumed to be "0", "1", etc.
        """
        ret_val = gxapi_cy.WrapLTB.create(GXContext._get_tls_geo(), file.encode(), type, delim, key.encode())
        return GXLTB(ret_val)



    @classmethod
    def create_crypt(cls, file, type, delim, case, key, crypt):
        """
        Creates a `GXLTB` object from an encrypted file.

        **Note:**

        If the file has no header, field names are assumed to be "0", "1", etc.
        """
        ret_val = gxapi_cy.WrapLTB.create_crypt(GXContext._get_tls_geo(), file.encode(), type, delim, case, key.encode(), crypt.encode())
        return GXLTB(ret_val)



    @classmethod
    def create_ex(cls, file, type, delim, case, key):
        """
        Creates a `GXLTB` object from a file.

        **Note:**

        If the file has no header, field names are assumed to be "0", "1", etc.
        """
        ret_val = gxapi_cy.WrapLTB.create_ex(GXContext._get_tls_geo(), file.encode(), type, delim, case, key.encode())
        return GXLTB(ret_val)




    def delete_record(self, rec):
        """
        Delete a record.

        **Note:**

        Record numbers after the deleted record will be reduced
        by 1.
        """
        self._wrapper.delete_record(rec)
        






    def get_con_lst(self, fld, match, match_type, lst):
        """
        Populate a `GXLST` with `GXLTB` names from matching fields.

        **Note:**

        The `GXLST` object will be in the order of the file.
        The `GXLST` names will be the `GXLTB` key fields and the
        `GXLST` values will be the `GXLTB` record numbers.
        """
        self._wrapper.get_con_lst(fld, match.encode(), match_type, lst._wrapper)
        




    def get_lst(self, fld, lst):
        """
        Populate an `GXLST` with `GXLTB` names

        **Note:**

        The `GXLST` object will be in the order of the file.
        The `GXLST` names will be the `GXLTB` fields and the
        `GXLST` values will be the `GXLTB` record numbers.
        """
        self._wrapper.get_lst(fld, lst._wrapper)
        




    def get_lst2(self, fld_n, fld_v, lst):
        """
        Populate an `GXLST` with `GXLTB` names and values

        **Note:**

        The `GXLST` object will be in the order of the file.
        The `GXLST` names will come from the `GXLTB` name field and the
        `GXLST` values will come from value field specified.
        """
        self._wrapper.get_lst2(fld_n, fld_v, lst._wrapper)
        




    def fields(self):
        """
        Get number of fields.
        """
        ret_val = self._wrapper.fields()
        return ret_val




    def find_field(self, field):
        """
        Return the field number for the specified field.
        """
        ret_val = self._wrapper.find_field(field.encode())
        return ret_val




    def find_key(self, key):
        """
        Return the key index of a record.
        """
        ret_val = self._wrapper.find_key(key.encode())
        return ret_val




    def get_field(self, field_num, field):
        """
        Get a field name by index.

        **Note:**

        If the record or field are out of range, an empty string is returned.
        """
        field.value = self._wrapper.get_field(field_num, field.value.encode())
        




    def get_int(self, record, field):
        """
        Get a int entry from the `GXLTB`
        """
        ret_val = self._wrapper.get_int(record, field)
        return ret_val




    def get_string(self, record, field, token):
        """
        Get an entry from the `GXLTB`

        **Note:**

        If the record or field are out of range,
        an empty string or dummy value is returned.
        """
        token.value = self._wrapper.get_string(record, field, token.value.encode())
        




    def get_english_string(self, record, field, token):
        """
        Get the English entry from the `GXLTB`

        **Note:**

        If the record or field are out of range,
        an empty string or dummy value is returned.
        """
        token.value = self._wrapper.get_english_string(record, field, token.value.encode())
        




    def records(self):
        """
        Get number of records in `GXLTB`.
        """
        ret_val = self._wrapper.records()
        return ret_val




    def search(self, rec, fld, field):
        """
        Search for a record containing field value
        """
        ret_val = self._wrapper.search(rec, fld, field.encode())
        return ret_val




    def merge(self, lt_bc):
        """
        Merge the contents of two same-key tables.

        **Note:**

        Merging takes place as follows:
        
        1. The "Key" of the child must be the same as the "Key" of the Master.
        2. The fields of the Master `GXLTB` are collected in-order.
        3. Any new fields of the Child `GXLTB` are added to the end of the list.
        4. A new `GXLTB` is created to contain the new field list (in-order).
        5. The Child table contents are added to the New `GXLTB`.
        6. The Master table contents are added/replace the New `GXLTB`.
        7. The New `GXLTB` is returned.
        
        If the fields of the Master and Child are the same, steps 4, 5, 6 are
        replaced by:
        
        4. The Master `GXLTB` is copied to the New `GXLTB`.
        5. Any New records found in the child are added to the New `GXLTB`
        """
        ret_val = self._wrapper.merge(lt_bc._wrapper)
        return GXLTB(ret_val)




    def get_double(self, record, field):
        """
        Get a real entry from the `GXLTB`
        """
        ret_val = self._wrapper.get_double(record, field)
        return ret_val




    def save(self, file):
        """
        Save `GXLTB` changes to existing or new file
        """
        self._wrapper.save(file.encode())
        




    def save_crypt(self, file, crypt):
        """
        Save `GXLTB` to a new file using encryption
        """
        self._wrapper.save_crypt(file.encode(), crypt.encode())
        




    def set_int(self, record, field, data):
        """
        Set a long entry
        """
        self._wrapper.set_int(record, field, data)
        




    def set_double(self, record, field, data):
        """
        Set a double entry
        """
        self._wrapper.set_double(record, field, data)
        




    def set_string(self, record, field, token):
        """
        Set an entry
        """
        self._wrapper.set_string(record, field, token.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer