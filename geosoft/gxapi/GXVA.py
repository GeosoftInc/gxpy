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

    The `GXVA` class is the 2-Dimensional analogue to the `GXVV` class.
    When displayed in a database, `GXVA` objects are displayed graphically
    as profiles, one to a cell, and can also be displayed one column of
    data at a time by specifying an index; e.g. CH[0]. A `GXVA` object is
    declared with a fixed number of columns, which cannot be altered.
    The number of rows, however can be changed, in the same way that
    the length of a `GXVV` can be changed. Data can be added or extracted
    using VVs, either by row or column.
    
    A `GXVA` is used to store an array of data in which each element may have
    multiple elements.  For example, 256-channel radiometric data can
    be stored in a `GXVA` that is 256 elements wide.
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
        Get an array of data from a `GXVA`.
        """
        self._wrapper.get_array(start_row, start_col, rows, cols, data, gs_type)
        




    def set_array(self, start_row, start_col, rows, cols, data, gs_type):
        """
        Set a range of data in an array
        """
        self._wrapper.set_array(start_row, start_col, rows, cols, data, gs_type)
        




    def add_elevations_vv_to_depths(self, p2, p3):
        """
        Add one `GXVV` value to each row of the `GXVA`, output true elevation.

        **Note:**

        Adds each value in an input elevation `GXVV` to all the values at
        the same fid in a depths `GXVA`. Includes an option for negative depths down
        (e.g. a relative level).
        """
        self._wrapper.add_elevations_vv_to_depths(p2._wrapper, p3)
        




    def append(self, p2):
        """
        Appends VAs

        **Note:**

        If the VAs have different numbers of columns, the smaller number
        is used in the copy operation.
        """
        self._wrapper.append(p2._wrapper)
        




    def average(self, p2, p3):
        """
        Average elements in a `GXVA` by row or column

        **Note:**

        The output `GXVV` will be dimensioned by the number of
        rows or columns in the input `GXVV` depending on the
        `VA_AVERAGE` setting.
        
        Dummies are not included in the average.
        """
        self._wrapper.average(p2._wrapper, p3)
        




    def copy(self, p2):
        """
        Copy one `GXVA` to another.
        """
        self._wrapper.copy(p2._wrapper)
        




    def copy2(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Copy part of a vector into part of another vector.

        **Note:**

        1. Unlike `copy` destination `GXVA` is not reallocated, nor are
        the dimensions changed. The caller must make any desired changes.
        
        2. All `GXVA` types are supported and will be converted using
        Convert_GS if necessary.
        """
        self._wrapper.copy2(p2, p3, p4._wrapper, p5, p6, p7, p8)
        



    @classmethod
    def create(cls, p1, p2, p3):
        """
        Create a `GXVA`.
        """
        ret_val = gxapi_cy.WrapVA.create(GXContext._get_tls_geo(), p1, p2, p3)
        return GXVA(ret_val)



    @classmethod
    def create_ext(cls, p1, p2, p3):
        """
        Create a `GXVA`, using one of the `GS_TYPES` special data types.

        **Note:**

        See `GXVV.create`
        """
        ret_val = gxapi_cy.WrapVA.create_ext(GXContext._get_tls_geo(), p1, p2, p3)
        return GXVA(ret_val)



    @classmethod
    def create_vv(cls, p1, p2, p3):
        """
        Create a `GXVA` using the data in a `GXVV`.

        **Note:**

        See `GXVV.create`
        """
        ret_val = gxapi_cy.WrapVA.create_vv(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        return GXVA(ret_val)






    def get_full_vv(self):
        """
        Get the full `GXVV` from the `GXVA`.

        **Note:**

        No data is copied, this is the handle to the data `GXVV` in the `GXVA`.
        The fid start/increment of the `GXVA` is passed to the `GXVV` at the time
        of the call.  If a new `GXVA` is read, you must call GetFull_VV_VA
        to get the new fid in the `GXVV`.
        """
        ret_val = self._wrapper.get_full_vv()
        return GXVV(ret_val)




    def get_vv(self, p2, p3, p4):
        """
        Get a row or column of data as a `GXVV` from an array.
        """
        self._wrapper.get_vv(p2, p3, p4._wrapper)
        




    def col(self):
        """
        Return number of columns in `GXVA`

        **Note:**

        `len` returns the number of rows.
        """
        ret_val = self._wrapper.col()
        return ret_val




    def get_int(self, p2, p3):
        """
        Get an integer element from a `GXVA`.

        **Note:**

        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        ret_val = self._wrapper.get_int(p2, p3)
        return ret_val




    def get_string(self, p2, p3, p4):
        """
        Get a string element from a `GXVA`.

        **Note:**

        Returns element wanted, `rDUMMY`, `iDUMMY` or blank string
        if the value is dummy or outside of the range of data.
        
        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        p4.value = self._wrapper.get_string(p2, p3, p4.value.encode())
        




    def len(self):
        """
        Return length (number of rows) in a `GXVA`.

        **Note:**

        `col` returns the number of columns.
        """
        ret_val = self._wrapper.len()
        return ret_val



    @classmethod
    def index_order(cls, p1, p2):
        """
        Reorder a `GXVA` based on an index `GXVV`

        **Note:**

        Given a row index `GXVV` (of type INT), this method reorders a
        `GXVA`. Please make sure that the index holds valid information.
        """
        gxapi_cy.WrapVA.index_order(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        




    def lookup_index(self, p2, p3):
        """
        Lookup a `GXVA` from another `GXVA` using an index `GXVV`.

        **Note:**

        Fractional values in the `GXVV` will interpolate between the value
        at the whole integer value and the next whole integer, dummy
        if outside the `GXVA`.
        """
        self._wrapper.lookup_index(p2._wrapper, p3._wrapper)
        




    def range_double(self, p2, p3):
        """
        Computes the minimum and maximum range of the data, in doubles,
        in a vector while ignoring dummies.
        """
        p2.value, p3.value = self._wrapper.range_double(p2.value, p3.value)
        




    def re_fid(self, p2, p3, p4):
        """
        Re-sample a `GXVA` to a new fid start/icrement
        """
        self._wrapper.re_fid(p2, p3, p4)
        




    def reverse(self):
        """
        Reverses the order of the rows in a `GXVA`.
        """
        self._wrapper.reverse()
        




    def get_fid_incr(self):
        """
        Gets the Fiducial increment from a `GXVA`
        """
        ret_val = self._wrapper.get_fid_incr()
        return ret_val




    def get_fid_start(self):
        """
        Gets the Fiducial start from a `GXVA`
        """
        ret_val = self._wrapper.get_fid_start()
        return ret_val




    def get_double(self, p2, p3):
        """
        Get a real element from a `GXVA`.

        **Note:**

        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        ret_val = self._wrapper.get_double(p2, p3)
        return ret_val




    def set_fid_incr(self, p2):
        """
        Sets the Fiducial increment of a `GXVA`
        """
        self._wrapper.set_fid_incr(p2)
        




    def set_fid_start(self, p2):
        """
        Sets the Fiducial start of a `GXVA`
        """
        self._wrapper.set_fid_start(p2)
        




    def set_int(self, p2, p3, p4):
        """
        Set an integer element in a `GXVA`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current `GXVA` length, the `GXVA` length is
        increased.
        """
        self._wrapper.set_int(p2, p3, p4)
        




    def set_ln(self, p2):
        """
        Set the length (number of rows) of the `GXVA`

        **Note:**

        The number of columns in a `GXVA` is fixed, and cannot be
        altered once the `GXVA` is created.
        """
        self._wrapper.set_ln(p2)
        




    def set_double(self, p2, p3, p4):
        """
        Set a real element in a `GXVA`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current `GXVA` length, the `GXVA` length is
        increased.
        """
        self._wrapper.set_double(p2, p3, p4)
        




    def set_string(self, p2, p3, p4):
        """
        Set a string element in a `GXVA`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current `GXVA` length, the `GXVA` length is
        increased.
        """
        self._wrapper.set_string(p2, p3, p4.encode())
        




    def set_vv(self, p2, p3, p4):
        """
        Set a row or column of data in an array from a `GXVV`.
        """
        self._wrapper.set_vv(p2, p3, p4._wrapper)
        




    def trans(self, p2, p3):
        """
        Translate (`GXVA` + base ) * mult

        **Note:**

        Supports all `GXVA` types using an internal double `GXVV`.
        """
        self._wrapper.trans(p2, p3)
        




    def window(self, p2, p3, p4):
        """
        Window a `GXVA` to a `GXVV` based in intergral frame

        **Note:**

        The defined window must be within the `GXVA` element dimensions.
        The windowed result will be the simple sum of all
        values in the window.
        If any values are dummy, the result will be dummy.
        """
        self._wrapper.window(p2, p3, p4._wrapper)
        




    def window2(self, p2, p3, p4):
        """
        Window a `GXVA` to a `GXVV` based on fractional frame

        **Note:**

        The defined window must be within the `GXVA` element dimensions.
        The windowed result will be the simple sum of all
        values in the window.
        If any values are dummy, the result will be dummy.
        """
        self._wrapper.window2(p2, p3, p4._wrapper)
        




    def check_for_repeating(self, p2, p3, p4, p5):
        """
        Window a `GXVA` to a `GXVV` based on fractional frame

        **Note:**

        Returns 1 if all rows contain values which match the input values.
        Optionally, row values can be offset by amounts specified with a secondary `GXVV`.
        This function was designed to detect "depth" array channels, including those which might
        have been offset with topography on each row.
        An absolute tolerance can be specified to ignore numerical noise.
        """
        ret_val = self._wrapper.check_for_repeating(p2._wrapper, p3, p4._wrapper, p5)
        return ret_val




    def check_for_repeating2(self, p2, p3, p4, p5, p6, p7):
        """
        Window a `GXVA` to a `GXVV` based on fractional frame

        **Note:**

        Returns 1 if all rows contain values which match the input values.
        Optionally, row values can be offset by amounts specified with a secondary `GXVV`.
        This function was designed to detect "depth" array channels, including those which might
        have been offset with topography on each row.
        An absolute tolerance can be specified to ignore numerical noise.
        This version returns the row and column index of first mismatch.
        """
        ret_val, p6.value, p7.value = self._wrapper.check_for_repeating2(p2._wrapper, p3, p4._wrapper, p5, p6.value, p7.value)
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