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
class GXLTB(gxapi_cy.WrapLTB):
    """
    GXLTB class.

    An `GXLTB <geosoft.gxapi.GXLTB>` object is typically created from a CSV (comma-separated values)
    file, and is a table of information that may be accessed by row
    or column. The `GXLTB <geosoft.gxapi.GXLTB>` class is recommended for use with small tables
    produced from short lists (of the order of 1000's or records) such
    as the different geographic projections and their defining parameters.
    Large tables, such as those required for table-lookup functions, should
    be accessed using the `GXTB <geosoft.gxapi.GXTB>` class.

    **Note:**

    An `GXLTB <geosoft.gxapi.GXLTB>` ASCII table file has the following structure:

    / comments
    key_name,col_1,col_2,col_3,etc...    /field names
    key_1,token,token,token,etc...       /data lines
    key_2,token,token,token,etc...
    etc...

    The first column must be the key column (all entries unique).

    The header line is optional and can be used to find entries.

    Comment and empty lines are ignored.
    """

    def __init__(self, handle=0):
        super(GXLTB, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXLTB <geosoft.gxapi.GXLTB>`
        
        :returns: A null `GXLTB <geosoft.gxapi.GXLTB>`
        :rtype:   GXLTB
        """
        return GXLTB()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def add_record(self, key, rec):
        """
        Add a new record.
        
        :param key:  Key name
        :param rec:  Returned record number
        :type  key:  str
        :type  rec:  int_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the record exists, the existing record is cleared
        and the record number is returned.
        """
        rec.value = self._add_record(key.encode(), rec.value)
        




    def contract(self, lt_bc):
        """
        Contract the contents of two same-key and same-fields tables.
        
        :param lt_bc:  Contract `GXLTB <geosoft.gxapi.GXLTB>`
        :type  lt_bc:  GXLTB

        :returns:      x    - Handle to `GXLTB <geosoft.gxapi.GXLTB>` object
                       NULL - Error of some kind
        :rtype:        GXLTB

        .. versionadded:: 5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The "Key" of the child must be the same as the "Key" of the Master.
        The fields of two `GXLTB <geosoft.gxapi.GXLTB>` must be the same.

        Contracting takes place as follows:

        1. The Master `GXLTB <geosoft.gxapi.GXLTB>` is copied to the New `GXLTB <geosoft.gxapi.GXLTB>`.
        2. All records in the contract LIB are deleted from the New `GXLTB <geosoft.gxapi.GXLTB>` (if there are any)
        3. The New `GXLTB <geosoft.gxapi.GXLTB>` is returned.
        """
        ret_val = self._contract(lt_bc)
        return GXLTB(ret_val)



    @classmethod
    def create(cls, file, type, delim, key):
        """
        Creates a `GXLTB <geosoft.gxapi.GXLTB>` object from a file.
        
        :param file:   File name, .csv assumed, searched locally then in GEOSOFT.
        :param type:   :ref:`LTB_TYPE`
        :param delim:  :ref:`LTB_DELIM`
        :param key:    Key to find if only one record required, "" to read entire table.
        :type  file:   str
        :type  type:   int
        :type  delim:  int
        :type  key:    str

        :returns:      x    - Handle to `GXLTB <geosoft.gxapi.GXLTB>` object
                       NULL - Error of some kind
        :rtype:        GXLTB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the file has no header, field names are assumed to be "0", "1", etc.
        """
        ret_val = gxapi_cy.WrapLTB._create(GXContext._get_tls_geo(), file.encode(), type, delim, key.encode())
        return GXLTB(ret_val)



    @classmethod
    def create_crypt(cls, file, type, delim, case_sensitive, key, crypt):
        """
        Creates a `GXLTB <geosoft.gxapi.GXLTB>` object from an encrypted file.
        
        :param file:            File name, .csv assumed, searched locally then in GEOSOFT.
        :param type:            :ref:`LTB_TYPE`
        :param delim:           :ref:`LTB_DELIM`
        :param case_sensitive:  :ref:`LTB_CASE`
        :param key:             Key to find if only one record required, "" to read entire table.
        :param crypt:           Decryption Key :ref:`SYS_CRYPT_KEY`
        :type  file:            str
        :type  type:            int
        :type  delim:           int
        :type  case_sensitive:  int
        :type  key:             str
        :type  crypt:           str

        :returns:               x    - Handle to `GXLTB <geosoft.gxapi.GXLTB>` object
                                NULL - Error of some kind
        :rtype:                 GXLTB

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the file has no header, field names are assumed to be "0", "1", etc.
        """
        ret_val = gxapi_cy.WrapLTB._create_crypt(GXContext._get_tls_geo(), file.encode(), type, delim, case_sensitive, key.encode(), crypt.encode())
        return GXLTB(ret_val)



    @classmethod
    def create_ex(cls, file, type, delim, case_sensitive, key):
        """
        Creates a `GXLTB <geosoft.gxapi.GXLTB>` object from a file.
        
        :param file:            File name, .csv assumed, searched locally then in GEOSOFT.
        :param type:            :ref:`LTB_TYPE`
        :param delim:           :ref:`LTB_DELIM`
        :param case_sensitive:  :ref:`LTB_CASE`
        :param key:             Key to find if only one record required, "" to read entire table.
        :type  file:            str
        :type  type:            int
        :type  delim:           int
        :type  case_sensitive:  int
        :type  key:             str

        :returns:               x    - Handle to `GXLTB <geosoft.gxapi.GXLTB>` object
                                NULL - Error of some kind
        :rtype:                 GXLTB

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the file has no header, field names are assumed to be "0", "1", etc.
        """
        ret_val = gxapi_cy.WrapLTB._create_ex(GXContext._get_tls_geo(), file.encode(), type, delim, case_sensitive, key.encode())
        return GXLTB(ret_val)




    def delete_record(self, rec):
        """
        Delete a record.
        
        :param rec:  Record number to delete
        :type  rec:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Record numbers after the deleted record will be reduced
        by 1.
        """
        self._delete_record(rec)
        






    def get_con_lst(self, fld, match, match_type, lst):
        """
        Populate a `GXLST <geosoft.gxapi.GXLST>` with `GXLTB <geosoft.gxapi.GXLTB>` names from matching fields.
        
        :param fld:         Field
        :param match:       String to match to field, must be lower-case
        :param match_type:  :ref:`LTB_CONLST`
        :param lst:         List to populate
        :type  fld:         int
        :type  match:       str
        :type  match_type:  int
        :type  lst:         GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXLST <geosoft.gxapi.GXLST>` object will be in the order of the file.
        The `GXLST <geosoft.gxapi.GXLST>` names will be the `GXLTB <geosoft.gxapi.GXLTB>` key fields and the
        `GXLST <geosoft.gxapi.GXLST>` values will be the `GXLTB <geosoft.gxapi.GXLTB>` record numbers.
        """
        self._get_con_lst(fld, match.encode(), match_type, lst)
        




    def get_lst(self, fld, lst):
        """
        Populate an `GXLST <geosoft.gxapi.GXLST>` with `GXLTB <geosoft.gxapi.GXLTB>` names
        
        :param fld:  Field to get, 0 for key field
        :param lst:  List to populate
        :type  fld:  int
        :type  lst:  GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXLST <geosoft.gxapi.GXLST>` object will be in the order of the file.
        The `GXLST <geosoft.gxapi.GXLST>` names will be the `GXLTB <geosoft.gxapi.GXLTB>` fields and the
        `GXLST <geosoft.gxapi.GXLST>` values will be the `GXLTB <geosoft.gxapi.GXLTB>` record numbers.
        """
        self._get_lst(fld, lst)
        




    def get_lst2(self, fld_n, fld_v, lst):
        """
        Populate an `GXLST <geosoft.gxapi.GXLST>` with `GXLTB <geosoft.gxapi.GXLTB>` names and values
        
        :param fld_n:  Field for names, 0 for key field
        :param fld_v:  Field for values, 0 for key field
        :param lst:    List to populate
        :type  fld_n:  int
        :type  fld_v:  int
        :type  lst:    GXLST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The `GXLST <geosoft.gxapi.GXLST>` object will be in the order of the file.
        The `GXLST <geosoft.gxapi.GXLST>` names will come from the `GXLTB <geosoft.gxapi.GXLTB>` name field and the
        `GXLST <geosoft.gxapi.GXLST>` values will come from value field specified.
        """
        self._get_lst2(fld_n, fld_v, lst)
        




    def fields(self):
        """
        Get number of fields.
        

        :returns:    Number of fields in the `GXLTB <geosoft.gxapi.GXLTB>`.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._fields()
        return ret_val




    def find_field(self, field):
        """
        Return the field number for the specified field.
        
        :param field:  Field name
        :type  field:  str

        :returns:      -1 if field does not exist.
                       field number if field does exist.
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._find_field(field.encode())
        return ret_val




    def find_key(self, key):
        """
        Return the key index of a record.
        
        :param key:  Key name
        :type  key:  str

        :returns:    -1 if key does not exist.
                     record number if key does exist.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._find_key(key.encode())
        return ret_val




    def get_field(self, field_num, field):
        """
        Get a field name by index.
        
        :param field_num:  Field number
        :param field:      Returned field name
        :type  field_num:  int
        :type  field:      str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the record or field are out of range, an empty string is returned.
        """
        field.value = self._get_field(field_num, field.value.encode())
        




    def get_int(self, record, field):
        """
        Get a int entry from the `GXLTB <geosoft.gxapi.GXLTB>`
        
        :param record:  Record number
        :param field:   Field number
        :type  record:  int
        :type  field:   int

        :returns:       If the record or field are out of range,
                        an empty string or dummy value is returned.
        :rtype:         int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_int(record, field)
        return ret_val




    def get_string(self, record, field, token):
        """
        Get an entry from the `GXLTB <geosoft.gxapi.GXLTB>`
        
        :param record:  Record number
        :param field:   Field number
        :param token:   Returned field token
        :type  record:  int
        :type  field:   int
        :type  token:   str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the record or field are out of range,
        an empty string or dummy value is returned.
        """
        token.value = self._get_string(record, field, token.value.encode())
        




    def get_english_string(self, record, field, token):
        """
        Get the English entry from the `GXLTB <geosoft.gxapi.GXLTB>`
        
        :param record:  Record number
        :param field:   Field number
        :param token:   Returned field token
        :type  record:  int
        :type  field:   int
        :type  token:   str_ref

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the record or field are out of range,
        an empty string or dummy value is returned.
        """
        token.value = self._get_english_string(record, field, token.value.encode())
        




    def records(self):
        """
        Get number of records in `GXLTB <geosoft.gxapi.GXLTB>`.
        

        :returns:    Number of records in the `GXLTB <geosoft.gxapi.GXLTB>`.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._records()
        return ret_val




    def search(self, rec, fld, field):
        """
        Search for a record containing field value
        
        :param rec:    Search start record
        :param fld:    Field number
        :param field:  Search string (case sensitive)
        :type  rec:    int
        :type  fld:    int
        :type  field:  str

        :returns:      -1 if search failed.
                       record number if search succeeds
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._search(rec, fld, field.encode())
        return ret_val




    def merge(self, lt_bc):
        """
        Merge the contents of two same-key tables.
        
        :param lt_bc:  Child `GXLTB <geosoft.gxapi.GXLTB>`
        :type  lt_bc:  GXLTB

        :returns:      x    - Handle to `GXLTB <geosoft.gxapi.GXLTB>` object
                       NULL - Error of some kind
        :rtype:        GXLTB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Merging takes place as follows:

        1. The "Key" of the child must be the same as the "Key" of the Master.
        2. The fields of the Master `GXLTB <geosoft.gxapi.GXLTB>` are collected in-order.
        3. Any new fields of the Child `GXLTB <geosoft.gxapi.GXLTB>` are added to the end of the list.
        4. A new `GXLTB <geosoft.gxapi.GXLTB>` is created to contain the new field list (in-order).
        5. The Child table contents are added to the New `GXLTB <geosoft.gxapi.GXLTB>`.
        6. The Master table contents are added/replace the New `GXLTB <geosoft.gxapi.GXLTB>`.
        7. The New `GXLTB <geosoft.gxapi.GXLTB>` is returned.

        If the fields of the Master and Child are the same, steps 4, 5, 6 are
        replaced by:

        4. The Master `GXLTB <geosoft.gxapi.GXLTB>` is copied to the New `GXLTB <geosoft.gxapi.GXLTB>`.
        5. Any New records found in the child are added to the New `GXLTB <geosoft.gxapi.GXLTB>`
        """
        ret_val = self._merge(lt_bc)
        return GXLTB(ret_val)




    def get_double(self, record, field):
        """
        Get a real entry from the `GXLTB <geosoft.gxapi.GXLTB>`
        
        :param record:  Record number
        :param field:   Field number
        :type  record:  int
        :type  field:   int

        :returns:       If the record or field are out of range,
                        an empty string or dummy value is returned.
        :rtype:         float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_double(record, field)
        return ret_val




    def save(self, file):
        """
        Save `GXLTB <geosoft.gxapi.GXLTB>` changes to existing or new file
        
        :param file:  File name, .csv assumed.  If "", save to original file.
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._save(file.encode())
        




    def save_crypt(self, file, crypt):
        """
        Save `GXLTB <geosoft.gxapi.GXLTB>` to a new file using encryption
        
        :param file:   File name, .csv assumed.  If "", save to original file.
        :param crypt:  Encryption key  :ref:`SYS_CRYPT_KEY`
        :type  file:   str
        :type  crypt:  str

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._save_crypt(file.encode(), crypt.encode())
        




    def set_int(self, record, field, data):
        """
        Set a long entry
        
        :param record:  Record number
        :param field:   Field number
        :param data:    Entry
        :type  record:  int
        :type  field:   int
        :type  data:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_int(record, field, data)
        




    def set_double(self, record, field, data):
        """
        Set a double entry
        
        :param record:  Record number
        :param field:   Field number
        :param data:    Entry
        :type  record:  int
        :type  field:   int
        :type  data:    float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_double(record, field, data)
        




    def set_string(self, record, field, token):
        """
        Set an entry
        
        :param record:  Record number
        :param field:   Field number
        :param token:   Entry
        :type  record:  int
        :type  field:   int
        :type  token:   str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_string(record, field, token.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer