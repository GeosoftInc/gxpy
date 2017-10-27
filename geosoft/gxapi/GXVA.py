### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXVV import GXVV


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
import numpy as np
from . import gxapi_cy_extend
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVA:
    """
    GXVA class.

    The `GXVA <geosoft.gxapi.GXVA>` class is the 2-Dimensional analogue to the `GXVV <geosoft.gxapi.GXVV>` class.
    When displayed in a database, `GXVA <geosoft.gxapi.GXVA>` objects are displayed graphically
    as profiles, one to a cell, and can also be displayed one column of
    data at a time by specifying an index; e.g. CH[0]. A `GXVA <geosoft.gxapi.GXVA>` object is
    declared with a fixed number of columns, which cannot be altered.
    The number of rows, however can be changed, in the same way that
    the length of a `GXVV <geosoft.gxapi.GXVV>` can be changed. Data can be added or extracted
    using VVs, either by row or column.
    
    A `GXVA <geosoft.gxapi.GXVA>` is used to store an array of data in which each element may have
    multiple elements.  For example, 256-channel radiometric data can
    be stored in a `GXVA <geosoft.gxapi.GXVA>` that is 256 elements wide.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVA(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVA`
        
        :returns: A null `GXVA`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXVA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXVA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def get_array(self, start_row, start_col, rows, cols, data, gs_type):
        """
        Get an array of data from a `GXVA <geosoft.gxapi.GXVA>`.
        
        :param start_row:  Starting Row
        :param start_col:  Starting Column
        :param rows:       # rows
        :param cols:       # cols
        :param data:       Data buffer to copy `GXVA <geosoft.gxapi.GXVA>` data into
        :param gs_type:    `GS_TYPES`
        :type  start_row:  int
        :type  start_col:  int
        :type  rows:       int
        :type  cols:       int
        :type  data:       bytearray
        :type  gs_type:    int

        .. versionadded:: 5.0
        """
        self._wrapper.get_array(start_row, start_col, rows, cols, data, gs_type)
        




    def set_array(self, start_row, start_col, rows, cols, data, gs_type):
        """
        Set a range of data in an array
        
        :param start_row:  Starting Row
        :param start_col:  Starting Column
        :param rows:       # rows
        :param cols:       # cols
        :param data:       Data buffer to copy into `GXVA <geosoft.gxapi.GXVA>`
        :param gs_type:    `GS_TYPES`
        :type  start_row:  int
        :type  start_col:  int
        :type  rows:       int
        :type  cols:       int
        :type  data:       bytearray
        :type  gs_type:    int

        .. versionadded:: 5.0
        """
        self._wrapper.set_array(start_row, start_col, rows, cols, data, gs_type)
        




    def add_elevations_vv_to_depths(self, vv, negative_depths):
        """
        Add one `GXVV <geosoft.gxapi.GXVV>` value to each row of the `GXVA <geosoft.gxapi.GXVA>`, output true elevation.
        
        :param vv:               Elevations to add
        :param negative_depths:  Use negative `GXVA <geosoft.gxapi.GXVA>` depths (0:No, 1:Yes)?
        :type  vv:               GXVV
        :type  negative_depths:  int

        .. versionadded:: 7.2

        **Note:**

        Adds each value in an input elevation `GXVV <geosoft.gxapi.GXVV>` to all the values at
        the same fid in a depths `GXVA <geosoft.gxapi.GXVA>`. Includes an option for negative depths down
        (e.g. a relative level).
        """
        self._wrapper.add_elevations_vv_to_depths(vv._wrapper, negative_depths)
        




    def append(self, v_aa):
        """
        Appends VAs
        
        :param v_aa:  `GXVA <geosoft.gxapi.GXVA>` to append
        :type  v_aa:  GXVA

        .. versionadded:: 5.1.3

        **Note:**

        If the VAs have different numbers of columns, the smaller number
        is used in the copy operation.
        """
        self._wrapper.append(v_aa._wrapper)
        




    def average(self, vv, rc):
        """
        Average elements in a `GXVA <geosoft.gxapi.GXVA>` by row or column
        
        :param vv:  `GXVV <geosoft.gxapi.GXVV>` in which to place average results
        :param rc:  `VA_AVERAGE`
        :type  vv:  GXVV
        :type  rc:  int

        .. versionadded:: 5.0

        **Note:**

        The output `GXVV <geosoft.gxapi.GXVV>` will be dimensioned by the number of
        rows or columns in the input `GXVV <geosoft.gxapi.GXVV>` depending on the
        `VA_AVERAGE` setting.
        
        Dummies are not included in the average.
        """
        self._wrapper.average(vv._wrapper, rc)
        




    def copy(self, v_as):
        """
        Copy one `GXVA <geosoft.gxapi.GXVA>` to another.
        
        :param v_as:  source
        :type  v_as:  GXVA

        .. versionadded:: 5.0
        """
        self._wrapper.copy(v_as._wrapper)
        




    def copy2(self, d_row, d_col, v_as, s_row, s_col, rows, cols):
        """
        Copy part of a vector into part of another vector.
        
        :param d_row:  Destination start row
        :param d_col:  Destination start column
        :param v_as:   Source `GXVA <geosoft.gxapi.GXVA>` (can be the same as Destination)
        :param s_row:  Source start row
        :param s_col:  Source start column
        :param rows:   Number of rows
        :param cols:   Number of columns
        :type  d_row:  int
        :type  d_col:  int
        :type  v_as:   GXVA
        :type  s_row:  int
        :type  s_col:  int
        :type  rows:   int
        :type  cols:   int

        .. versionadded:: 5.0

        **Note:**

        1. Unlike `copy <geosoft.gxapi.GXVA.copy>` destination `GXVA <geosoft.gxapi.GXVA>` is not reallocated, nor are
        the dimensions changed. The caller must make any desired changes.
        
        2. All `GXVA <geosoft.gxapi.GXVA>` types are supported and will be converted using
        Convert_GS if necessary.
        """
        self._wrapper.copy2(d_row, d_col, v_as._wrapper, s_row, s_col, rows, cols)
        



    @classmethod
    def create(cls, type, rows, cols):
        """
        Create a `GXVA <geosoft.gxapi.GXVA>`.
        
        :param type:  `GEO_VAR`
        :param rows:  Maximum number of rows in the `GXVA <geosoft.gxapi.GXVA>`, >= 0
        :param cols:  Number of columns in the `GXVA <geosoft.gxapi.GXVA>`, > 0
        :type  type:  int
        :type  rows:  int
        :type  cols:  int

        :returns:     `GXVA <geosoft.gxapi.GXVA>` Object
        :rtype:       GXVA

        .. versionadded:: 5.0
        """
        ret_val = gxapi_cy.WrapVA.create(GXContext._get_tls_geo(), type, rows, cols)
        return GXVA(ret_val)



    @classmethod
    def create_ext(cls, type, rows, cols):
        """
        Create a `GXVA <geosoft.gxapi.GXVA>`, using one of the `GS_TYPES` special data types.
        
        :param type:  `GS_TYPES`
        :param rows:  Maximum number of rows in the `GXVA <geosoft.gxapi.GXVA>`, >= 0
        :param cols:  Number of columns in the `GXVA <geosoft.gxapi.GXVA>`, > 0
        :type  type:  int
        :type  rows:  int
        :type  cols:  int

        :returns:     `GXVA <geosoft.gxapi.GXVA>`, aborts if creation fails
        :rtype:       GXVA

        .. versionadded:: 5.0

        **Note:**

        See `GXVV.create <geosoft.gxapi.GXVV.create>`
        """
        ret_val = gxapi_cy.WrapVA.create_ext(GXContext._get_tls_geo(), type, rows, cols)
        return GXVA(ret_val)



    @classmethod
    def create_vv(cls, vv, rows, columns):
        """
        Create a `GXVA <geosoft.gxapi.GXVA>` using the data in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vv:       `GXVV <geosoft.gxapi.GXVV>` with the data
        :param rows:     # of rows
        :param columns:  # of columns
        :type  vv:       GXVV
        :type  rows:     int
        :type  columns:  int

        :returns:        `GXVA <geosoft.gxapi.GXVA>`, aborts if creation fails
        :rtype:          GXVA

        .. versionadded:: 7.2.1

        **Note:**

        See `GXVV.create <geosoft.gxapi.GXVV.create>`
        """
        ret_val = gxapi_cy.WrapVA.create_vv(GXContext._get_tls_geo(), vv._wrapper, rows, columns)
        return GXVA(ret_val)






    def get_full_vv(self):
        """
        Get the full `GXVV <geosoft.gxapi.GXVV>` from the `GXVA <geosoft.gxapi.GXVA>`.
        

        :returns:    `GXVV <geosoft.gxapi.GXVV>` Object
        :rtype:      GXVV

        .. versionadded:: 5.0

        **Note:**

        No data is copied, this is the handle to the data `GXVV <geosoft.gxapi.GXVV>` in the `GXVA <geosoft.gxapi.GXVA>`.
        The fid start/increment of the `GXVA <geosoft.gxapi.GXVA>` is passed to the `GXVV <geosoft.gxapi.GXVV>` at the time
        of the call.  If a new `GXVA <geosoft.gxapi.GXVA>` is read, you must call GetFull_VV_VA
        to get the new fid in the `GXVV <geosoft.gxapi.GXVV>`.
        """
        ret_val = self._wrapper.get_full_vv()
        return GXVV(ret_val)




    def get_vv(self, no, row_col, vv):
        """
        Get a row or column of data as a `GXVV <geosoft.gxapi.GXVV>` from an array.
        
        :param no:       Row or Column # (0 is first)
        :param row_col:  `VA_OBJECT`
        :param vv:       `GXVV <geosoft.gxapi.GXVV>` in which to place data
        :type  no:       int
        :type  row_col:  int
        :type  vv:       GXVV

        .. versionadded:: 5.0
        """
        self._wrapper.get_vv(no, row_col, vv._wrapper)
        




    def col(self):
        """
        Return number of columns in `GXVA <geosoft.gxapi.GXVA>`
        

        :returns:    Columns in `GXVA <geosoft.gxapi.GXVA>`
        :rtype:      int

        .. versionadded:: 5.0

        **Note:**

        `len <geosoft.gxapi.GXVA.len>` returns the number of rows.
        """
        ret_val = self._wrapper.col()
        return ret_val




    def get_int(self, row, col):
        """
        Get an integer element from a `GXVA <geosoft.gxapi.GXVA>`.
        
        :param row:  Row
        :param col:  Column
        :type  row:  int
        :type  col:  int

        :returns:    Element wanted, `rDUMMY <geosoft.gxapi.rDUMMY>`, `iDUMMY <geosoft.gxapi.iDUMMY>` or blank string
                     if the value is dummy or outside of the range of data.
        :rtype:      int

        .. versionadded:: 5.0

        **Note:**

        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        ret_val = self._wrapper.get_int(row, col)
        return ret_val




    def get_string(self, row, col, str_val):
        """
        Get a string element from a `GXVA <geosoft.gxapi.GXVA>`.
        
        :param row:      Row
        :param col:      Column
        :param str_val:  String in which to place element
        :type  row:      int
        :type  col:      int
        :type  str_val:  str_ref

        .. versionadded:: 5.0

        **Note:**

        Returns element wanted, `rDUMMY <geosoft.gxapi.rDUMMY>`, `iDUMMY <geosoft.gxapi.iDUMMY>` or blank string
        if the value is dummy or outside of the range of data.
        
        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        str_val.value = self._wrapper.get_string(row, col, str_val.value.encode())
        




    def len(self):
        """
        Return length (number of rows) in a `GXVA <geosoft.gxapi.GXVA>`.
        

        :returns:    Length of `GXVA <geosoft.gxapi.GXVA>`
        :rtype:      int

        .. versionadded:: 5.0

        **Note:**

        `col <geosoft.gxapi.GXVA.col>` returns the number of columns.
        """
        ret_val = self._wrapper.len()
        return ret_val



    @classmethod
    def index_order(cls, vv, va):
        """
        Reorder a `GXVA <geosoft.gxapi.GXVA>` based on an index `GXVV <geosoft.gxapi.GXVV>`
        
        :param vv:  Index `GXVV <geosoft.gxapi.GXVV>` of type INT
        :param va:  `GXVA <geosoft.gxapi.GXVA>` to order
        :type  vv:  GXVV
        :type  va:  GXVA

        .. versionadded:: 5.1

        **Note:**

        Given a row index `GXVV <geosoft.gxapi.GXVV>` (of type INT), this method reorders a
        `GXVA <geosoft.gxapi.GXVA>`. Please make sure that the index holds valid information.
        """
        gxapi_cy.WrapVA.index_order(GXContext._get_tls_geo(), vv._wrapper, va._wrapper)
        




    def lookup_index(self, vvi, var):
        """
        Lookup a `GXVA <geosoft.gxapi.GXVA>` from another `GXVA <geosoft.gxapi.GXVA>` using an index `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vvi:  Index `GXVV <geosoft.gxapi.GXVV>` of REAL
        :param var:  `GXVA <geosoft.gxapi.GXVA>` to output results (same type as Data `GXVA <geosoft.gxapi.GXVA>`)
        :type  vvi:  GXVV
        :type  var:  GXVA

        .. versionadded:: 6.4.2

        **Note:**

        Fractional values in the `GXVV <geosoft.gxapi.GXVV>` will interpolate between the value
        at the whole integer value and the next whole integer, dummy
        if outside the `GXVA <geosoft.gxapi.GXVA>`.
        """
        self._wrapper.lookup_index(vvi._wrapper, var._wrapper)
        




    def range_double(self, min, max):
        """
        Computes the minimum and maximum range of the data, in doubles,
        in a vector while ignoring dummies.
        
        :param min:  Minimum value - returned
        :param max:  Maximum value - returned
        :type  min:  float_ref
        :type  max:  float_ref

        .. versionadded:: 5.0
        """
        min.value, max.value = self._wrapper.range_double(min.value, max.value)
        




    def re_fid(self, start, incr, length):
        """
        Re-sample a `GXVA <geosoft.gxapi.GXVA>` to a new fid start/icrement
        
        :param start:   New fid start
        :param incr:    New fid increment
        :param length:  New length
        :type  start:   float
        :type  incr:    float
        :type  length:  int

        .. versionadded:: 5.0
        """
        self._wrapper.re_fid(start, incr, length)
        




    def reverse(self):
        """
        Reverses the order of the rows in a `GXVA <geosoft.gxapi.GXVA>`.
        

        .. versionadded:: 5.1.5
        """
        self._wrapper.reverse()
        




    def get_fid_incr(self):
        """
        Gets the Fiducial increment from a `GXVA <geosoft.gxapi.GXVA>`
        

        :returns:    Fiducial increment of the `GXVA <geosoft.gxapi.GXVA>`.
        :rtype:      float

        .. versionadded:: 5.0
        """
        ret_val = self._wrapper.get_fid_incr()
        return ret_val




    def get_fid_start(self):
        """
        Gets the Fiducial start from a `GXVA <geosoft.gxapi.GXVA>`
        

        :returns:    Fiducial start of the `GXVA <geosoft.gxapi.GXVA>`.
        :rtype:      float

        .. versionadded:: 5.0
        """
        ret_val = self._wrapper.get_fid_start()
        return ret_val




    def get_double(self, row, col):
        """
        Get a real element from a `GXVA <geosoft.gxapi.GXVA>`.
        
        :param row:  Row
        :param col:  Column
        :type  row:  int
        :type  col:  int

        :returns:    Element wanted, `rDUMMY <geosoft.gxapi.rDUMMY>`, `iDUMMY <geosoft.gxapi.iDUMMY>` or blank string
                     if the value is dummy or outside of the range of data.
        :rtype:      float

        .. versionadded:: 5.0

        **Note:**

        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        ret_val = self._wrapper.get_double(row, col)
        return ret_val




    def set_fid_incr(self, incr):
        """
        Sets the Fiducial increment of a `GXVA <geosoft.gxapi.GXVA>`
        
        :param incr:  New increment
        :type  incr:  float

        .. versionadded:: 5.0
        """
        self._wrapper.set_fid_incr(incr)
        




    def set_fid_start(self, start):
        """
        Sets the Fiducial start of a `GXVA <geosoft.gxapi.GXVA>`
        
        :param start:  New start
        :type  start:  float

        .. versionadded:: 5.0
        """
        self._wrapper.set_fid_start(start)
        




    def set_int(self, row, col, value):
        """
        Set an integer element in a `GXVA <geosoft.gxapi.GXVA>`.
        
        :param row:    Row
        :param col:    Column
        :param value:  Value to set
        :type  row:    int
        :type  col:    int
        :type  value:  int

        .. versionadded:: 5.0

        **Note:**

        Element being set cannot be < 0.
        If the element is > current `GXVA <geosoft.gxapi.GXVA>` length, the `GXVA <geosoft.gxapi.GXVA>` length is
        increased.
        """
        self._wrapper.set_int(row, col, value)
        




    def set_ln(self, rows):
        """
        Set the length (number of rows) of the `GXVA <geosoft.gxapi.GXVA>`
        
        :param rows:  Length
        :type  rows:  int

        .. versionadded:: 5.0

        **Note:**

        The number of columns in a `GXVA <geosoft.gxapi.GXVA>` is fixed, and cannot be
        altered once the `GXVA <geosoft.gxapi.GXVA>` is created.
        """
        self._wrapper.set_ln(rows)
        




    def set_double(self, row, col, value):
        """
        Set a real element in a `GXVA <geosoft.gxapi.GXVA>`.
        
        :param row:    Row
        :param col:    Column
        :param value:  Value to set
        :type  row:    int
        :type  col:    int
        :type  value:  float

        .. versionadded:: 5.0

        **Note:**

        Element being set cannot be < 0.
        If the element is > current `GXVA <geosoft.gxapi.GXVA>` length, the `GXVA <geosoft.gxapi.GXVA>` length is
        increased.
        """
        self._wrapper.set_double(row, col, value)
        




    def set_string(self, row, col, value):
        """
        Set a string element in a `GXVA <geosoft.gxapi.GXVA>`.
        
        :param row:    Row
        :param col:    Column
        :param value:  String to set
        :type  row:    int
        :type  col:    int
        :type  value:  str

        .. versionadded:: 5.0

        **Note:**

        Element being set cannot be < 0.
        If the element is > current `GXVA <geosoft.gxapi.GXVA>` length, the `GXVA <geosoft.gxapi.GXVA>` length is
        increased.
        """
        self._wrapper.set_string(row, col, value.encode())
        




    def set_vv(self, no, row_col, vv):
        """
        Set a row or column of data in an array from a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param no:       Row or Column # (0 is first)
        :param row_col:  `VA_OBJECT`
        :param vv:       `GXVV <geosoft.gxapi.GXVV>` from which to get data
        :type  no:       int
        :type  row_col:  int
        :type  vv:       GXVV

        .. versionadded:: 5.0
        """
        self._wrapper.set_vv(no, row_col, vv._wrapper)
        




    def trans(self, base, mult):
        """
        Translate (`GXVA <geosoft.gxapi.GXVA>` + base ) * mult
        
        :param base:  Base value
        :param mult:  Mult value
        :type  base:  float
        :type  mult:  float

        .. versionadded:: 7.2

        **Note:**

        Supports all `GXVA <geosoft.gxapi.GXVA>` types using an internal double `GXVV <geosoft.gxapi.GXVV>`.
        """
        self._wrapper.trans(base, mult)
        




    def window(self, start, count, vv):
        """
        Window a `GXVA <geosoft.gxapi.GXVA>` to a `GXVV <geosoft.gxapi.GXVV>` based in intergral frame
        
        :param start:  First element in the window
        :param count:  Number of elements in the window
        :param vv:     `GXVV <geosoft.gxapi.GXVV>` in which to place results
        :type  start:  int
        :type  count:  int
        :type  vv:     GXVV

        .. versionadded:: 5.0

        **Note:**

        The defined window must be within the `GXVA <geosoft.gxapi.GXVA>` element dimensions.
        The windowed result will be the simple sum of all
        values in the window.
        If any values are dummy, the result will be dummy.
        """
        self._wrapper.window(start, count, vv._wrapper)
        




    def window2(self, start, end, vv):
        """
        Window a `GXVA <geosoft.gxapi.GXVA>` to a `GXVV <geosoft.gxapi.GXVV>` based on fractional frame
        
        :param start:  Start point (from 0.0)
        :param end:    End point (< `GXVA <geosoft.gxapi.GXVA>` elements - 1.0)
        :param vv:     `GXVV <geosoft.gxapi.GXVV>` in which to place results
        :type  start:  float
        :type  end:    float
        :type  vv:     GXVV

        .. versionadded:: 5.0

        **Note:**

        The defined window must be within the `GXVA <geosoft.gxapi.GXVA>` element dimensions.
        The windowed result will be the simple sum of all
        values in the window.
        If any values are dummy, the result will be dummy.
        """
        self._wrapper.window2(start, end, vv._wrapper)
        




    def check_for_repeating(self, vv_t, subtract_vv, vv_sub, tol):
        """
        Window a `GXVA <geosoft.gxapi.GXVA>` to a `GXVV <geosoft.gxapi.GXVV>` based on fractional frame
        
        :param vv_t:         Items to test for repeats (length equal to the number of columns in the `GXVA <geosoft.gxapi.GXVA>`)
        :param subtract_vv:  If set to 1, subtract single values in the following `GXVV <geosoft.gxapi.GXVV>` from every array row item before testing (e.g. an elevation value)
        :param vv_sub:       Values to subtract from each row before doing the comparison test (length equal to the length of the `GXVA <geosoft.gxapi.GXVA>`). Can be VV_NULL (-1) if above subtraction parameter is zero
        :param tol:          Comparison tolerance - set to zero or dummy for exact match
        :type  vv_t:         GXVV
        :type  subtract_vv:  int
        :type  vv_sub:       GXVV
        :type  tol:          float

        :returns:            1 if rows repeat, 0 if not.
        :rtype:              int

        .. versionadded:: 8.2

        **Note:**

        Returns 1 if all rows contain values which match the input values.
        Optionally, row values can be offset by amounts specified with a secondary `GXVV <geosoft.gxapi.GXVV>`.
        This function was designed to detect "depth" array channels, including those which might
        have been offset with topography on each row.
        An absolute tolerance can be specified to ignore numerical noise.
        """
        ret_val = self._wrapper.check_for_repeating(vv_t._wrapper, subtract_vv, vv_sub._wrapper, tol)
        return ret_val




    def check_for_repeating2(self, vv_t, subtract_vv, vv_sub, tol, bad_row, bad_col):
        """
        Window a `GXVA <geosoft.gxapi.GXVA>` to a `GXVV <geosoft.gxapi.GXVV>` based on fractional frame
        
        :param vv_t:         Items to test for repeats (length equal to the number of columns in the `GXVA <geosoft.gxapi.GXVA>`)
        :param subtract_vv:  If set to 1, subtract single values in the following `GXVV <geosoft.gxapi.GXVV>` from every array row item before testing (e.g. an elevation value)
        :param vv_sub:       Values to subtract from each row before doing the comparison test (length equal to the length of the `GXVA <geosoft.gxapi.GXVA>`). Can be VV_NULL (-1) if above subtraction parameter is zero
        :param tol:          Comparison tolerance - set to zero or dummy for exact match
        :param bad_row:      Row index of first mismatch
        :param bad_col:      Column index of first mismatch
        :type  vv_t:         GXVV
        :type  subtract_vv:  int
        :type  vv_sub:       GXVV
        :type  tol:          float
        :type  bad_row:      int_ref
        :type  bad_col:      int_ref

        :returns:            1 if rows repeat, 0 if not.
        :rtype:              int

        .. versionadded:: 8.2

        **Note:**

        Returns 1 if all rows contain values which match the input values.
        Optionally, row values can be offset by amounts specified with a secondary `GXVV <geosoft.gxapi.GXVV>`.
        This function was designed to detect "depth" array channels, including those which might
        have been offset with topography on each row.
        An absolute tolerance can be specified to ignore numerical noise.
        This version returns the row and column index of first mismatch.
        """
        ret_val, bad_row.value, bad_col.value = self._wrapper.check_for_repeating2(vv_t._wrapper, subtract_vv, vv_sub._wrapper, tol, bad_row.value, bad_col.value)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
    def get_array_np(self, start_row: int, start_col: int, rows: int, cols: int, np_dtype: type(np.dtype)):
        from .GXNumpy import gs_from_np
        gs_type = gs_from_np(np_dtype)
        return np.asarray(self.get_data_array(start_row, start_col, rows, cols, gs_type))

    def set_array_np(self, start_row: int, start_col: int, np_array: type(np.ndarray)):
        from .GXNumpy import gs_from_np
        gs_type = gs_from_np(np_array.dtype)
        if np_array.ndim != 2:
            raise GXAPIError("Only 2D Numpy arrays supported for this method");
        rows = np_array.shape[0];
        columns = np_array.shape[1];
        if not np_array.flags['C_CONTIGUOUS']:
            np_array = np.ascontiguousarray(np_array)
        self.set_array(start_row, start_col, rows, columns, np_array.data.tobytes(), gs_type)
    
    def get_data_array(self, start_row: int, start_col: int, rows: int, cols: int, gs_type: int):
        return gxapi_cy_extend.GXMemMethods.get_array_data_va(GXContext._internal_p(), self._wrapper.handle, start_row, start_col, rows, cols, gs_type)
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer