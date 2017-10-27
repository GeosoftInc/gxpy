### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
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
        """
        self._wrapper.get_array(start_row, start_col, rows, cols, data, gs_type)
        




    def set_array(self, start_row, start_col, rows, cols, data, gs_type):
        """
        Set a range of data in an array
        """
        self._wrapper.set_array(start_row, start_col, rows, cols, data, gs_type)
        




    def add_elevations_vv_to_depths(self, vv, negative_depths):
        """
        Add one `GXVV <geosoft.gxapi.GXVV>` value to each row of the `GXVA <geosoft.gxapi.GXVA>`, output true elevation.

        **Note:**

        Adds each value in an input elevation `GXVV <geosoft.gxapi.GXVV>` to all the values at
        the same fid in a depths `GXVA <geosoft.gxapi.GXVA>`. Includes an option for negative depths down
        (e.g. a relative level).
        """
        self._wrapper.add_elevations_vv_to_depths(vv._wrapper, negative_depths)
        




    def append(self, v_aa):
        """
        Appends VAs

        **Note:**

        If the VAs have different numbers of columns, the smaller number
        is used in the copy operation.
        """
        self._wrapper.append(v_aa._wrapper)
        




    def average(self, vv, rc):
        """
        Average elements in a `GXVA <geosoft.gxapi.GXVA>` by row or column

        **Note:**

        The output `GXVV <geosoft.gxapi.GXVV>` will be dimensioned by the number of
        rows or columns in the input `GXVV <geosoft.gxapi.GXVV>` depending on the
        `VA_AVERAGE_` setting.
        
        Dummies are not included in the average.
        """
        self._wrapper.average(vv._wrapper, rc)
        




    def copy(self, v_as):
        """
        Copy one `GXVA <geosoft.gxapi.GXVA>` to another.
        """
        self._wrapper.copy(v_as._wrapper)
        




    def copy2(self, d_row, d_col, v_as, s_row, s_col, rows, cols):
        """
        Copy part of a vector into part of another vector.

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
        """
        ret_val = gxapi_cy.WrapVA.create(GXContext._get_tls_geo(), type, rows, cols)
        return GXVA(ret_val)



    @classmethod
    def create_ext(cls, type, rows, cols):
        """
        Create a `GXVA <geosoft.gxapi.GXVA>`, using one of the `GS_TYPES_` special data types.

        **Note:**

        See `GXVV.create <geosoft.gxapi.GXVV.create>`
        """
        ret_val = gxapi_cy.WrapVA.create_ext(GXContext._get_tls_geo(), type, rows, cols)
        return GXVA(ret_val)



    @classmethod
    def create_vv(cls, vv, rows, columns):
        """
        Create a `GXVA <geosoft.gxapi.GXVA>` using the data in a `GXVV <geosoft.gxapi.GXVV>`.

        **Note:**

        See `GXVV.create <geosoft.gxapi.GXVV.create>`
        """
        ret_val = gxapi_cy.WrapVA.create_vv(GXContext._get_tls_geo(), vv._wrapper, rows, columns)
        return GXVA(ret_val)






    def get_full_vv(self):
        """
        Get the full `GXVV <geosoft.gxapi.GXVV>` from the `GXVA <geosoft.gxapi.GXVA>`.

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
        """
        self._wrapper.get_vv(no, row_col, vv._wrapper)
        




    def col(self):
        """
        Return number of columns in `GXVA <geosoft.gxapi.GXVA>`

        **Note:**

        `len <geosoft.gxapi.GXVA.len>` returns the number of rows.
        """
        ret_val = self._wrapper.col()
        return ret_val




    def get_int(self, row, col):
        """
        Get an integer element from a `GXVA <geosoft.gxapi.GXVA>`.

        **Note:**

        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        ret_val = self._wrapper.get_int(row, col)
        return ret_val




    def get_string(self, row, col, str_val):
        """
        Get a string element from a `GXVA <geosoft.gxapi.GXVA>`.

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

        **Note:**

        `col <geosoft.gxapi.GXVA.col>` returns the number of columns.
        """
        ret_val = self._wrapper.len()
        return ret_val



    @classmethod
    def index_order(cls, vv, va):
        """
        Reorder a `GXVA <geosoft.gxapi.GXVA>` based on an index `GXVV <geosoft.gxapi.GXVV>`

        **Note:**

        Given a row index `GXVV <geosoft.gxapi.GXVV>` (of type INT), this method reorders a
        `GXVA <geosoft.gxapi.GXVA>`. Please make sure that the index holds valid information.
        """
        gxapi_cy.WrapVA.index_order(GXContext._get_tls_geo(), vv._wrapper, va._wrapper)
        




    def lookup_index(self, vvi, var):
        """
        Lookup a `GXVA <geosoft.gxapi.GXVA>` from another `GXVA <geosoft.gxapi.GXVA>` using an index `GXVV <geosoft.gxapi.GXVV>`.

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
        """
        min.value, max.value = self._wrapper.range_double(min.value, max.value)
        




    def re_fid(self, start, incr, length):
        """
        Re-sample a `GXVA <geosoft.gxapi.GXVA>` to a new fid start/icrement
        """
        self._wrapper.re_fid(start, incr, length)
        




    def reverse(self):
        """
        Reverses the order of the rows in a `GXVA <geosoft.gxapi.GXVA>`.
        """
        self._wrapper.reverse()
        




    def get_fid_incr(self):
        """
        Gets the Fiducial increment from a `GXVA <geosoft.gxapi.GXVA>`
        """
        ret_val = self._wrapper.get_fid_incr()
        return ret_val




    def get_fid_start(self):
        """
        Gets the Fiducial start from a `GXVA <geosoft.gxapi.GXVA>`
        """
        ret_val = self._wrapper.get_fid_start()
        return ret_val




    def get_double(self, row, col):
        """
        Get a real element from a `GXVA <geosoft.gxapi.GXVA>`.

        **Note:**

        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        ret_val = self._wrapper.get_double(row, col)
        return ret_val




    def set_fid_incr(self, incr):
        """
        Sets the Fiducial increment of a `GXVA <geosoft.gxapi.GXVA>`
        """
        self._wrapper.set_fid_incr(incr)
        




    def set_fid_start(self, start):
        """
        Sets the Fiducial start of a `GXVA <geosoft.gxapi.GXVA>`
        """
        self._wrapper.set_fid_start(start)
        




    def set_int(self, row, col, value):
        """
        Set an integer element in a `GXVA <geosoft.gxapi.GXVA>`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current `GXVA <geosoft.gxapi.GXVA>` length, the `GXVA <geosoft.gxapi.GXVA>` length is
        increased.
        """
        self._wrapper.set_int(row, col, value)
        




    def set_ln(self, rows):
        """
        Set the length (number of rows) of the `GXVA <geosoft.gxapi.GXVA>`

        **Note:**

        The number of columns in a `GXVA <geosoft.gxapi.GXVA>` is fixed, and cannot be
        altered once the `GXVA <geosoft.gxapi.GXVA>` is created.
        """
        self._wrapper.set_ln(rows)
        




    def set_double(self, row, col, value):
        """
        Set a real element in a `GXVA <geosoft.gxapi.GXVA>`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current `GXVA <geosoft.gxapi.GXVA>` length, the `GXVA <geosoft.gxapi.GXVA>` length is
        increased.
        """
        self._wrapper.set_double(row, col, value)
        




    def set_string(self, row, col, value):
        """
        Set a string element in a `GXVA <geosoft.gxapi.GXVA>`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current `GXVA <geosoft.gxapi.GXVA>` length, the `GXVA <geosoft.gxapi.GXVA>` length is
        increased.
        """
        self._wrapper.set_string(row, col, value.encode())
        




    def set_vv(self, no, row_col, vv):
        """
        Set a row or column of data in an array from a `GXVV <geosoft.gxapi.GXVV>`.
        """
        self._wrapper.set_vv(no, row_col, vv._wrapper)
        




    def trans(self, base, mult):
        """
        Translate (`GXVA <geosoft.gxapi.GXVA>` + base ) * mult

        **Note:**

        Supports all `GXVA <geosoft.gxapi.GXVA>` types using an internal double `GXVV <geosoft.gxapi.GXVV>`.
        """
        self._wrapper.trans(base, mult)
        




    def window(self, start, count, vv):
        """
        Window a `GXVA <geosoft.gxapi.GXVA>` to a `GXVV <geosoft.gxapi.GXVV>` based in intergral frame

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