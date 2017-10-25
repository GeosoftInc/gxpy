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

    The :class:`geosoft.gxapi.GXVA` class is the 2-Dimensional analogue to the :class:`geosoft.gxapi.GXVV` class.
    When displayed in a database, :class:`geosoft.gxapi.GXVA` objects are displayed graphically
    as profiles, one to a cell, and can also be displayed one column of
    data at a time by specifying an index; e.g. CH[0]. A :class:`geosoft.gxapi.GXVA` object is
    declared with a fixed number of columns, which cannot be altered.
    The number of rows, however can be changed, in the same way that
    the length of a :class:`geosoft.gxapi.GXVV` can be changed. Data can be added or extracted
    using VVs, either by row or column.
    
    A :class:`geosoft.gxapi.GXVA` is used to store an array of data in which each element may have
    multiple elements.  For example, 256-channel radiometric data can
    be stored in a :class:`geosoft.gxapi.GXVA` that is 256 elements wide.
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
        A null (undefined) instance of :class:`geosoft.gxapi.GXVA`
        
        :returns: A null :class:`geosoft.gxapi.GXVA`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXVA` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXVA`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def get_array(self, start_row, start_col, rows, cols, data, gs_type):
        """
        Get an array of data from a :class:`geosoft.gxapi.GXVA`.
        """
        self._wrapper.get_array(start_row, start_col, rows, cols, data, gs_type)
        




    def set_array(self, start_row, start_col, rows, cols, data, gs_type):
        """
        Set a range of data in an array
        """
        self._wrapper.set_array(start_row, start_col, rows, cols, data, gs_type)
        




    def add_elevations_vv_to_depths(self, p2, p3):
        """
        Add one :class:`geosoft.gxapi.GXVV` value to each row of the :class:`geosoft.gxapi.GXVA`, output true elevation.

        **Note:**

        Adds each value in an input elevation :class:`geosoft.gxapi.GXVV` to all the values at
        the same fid in a depths :class:`geosoft.gxapi.GXVA`. Includes an option for negative depths down
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
        Average elements in a :class:`geosoft.gxapi.GXVA` by row or column

        **Note:**

        The output :class:`geosoft.gxapi.GXVV` will be dimensioned by the number of
        rows or columns in the input :class:`geosoft.gxapi.GXVV` depending on the
        `VA_AVERAGE` setting.
        
        Dummies are not included in the average.
        """
        self._wrapper.average(p2._wrapper, p3)
        




    def copy(self, p2):
        """
        Copy one :class:`geosoft.gxapi.GXVA` to another.
        """
        self._wrapper.copy(p2._wrapper)
        




    def copy2(self, p2, p3, p4, p5, p6, p7, p8):
        """
        Copy part of a vector into part of another vector.

        **Note:**

        1. Unlike Copy_VA destination :class:`geosoft.gxapi.GXVA` is not reallocated, nor are
        the dimensions changed. The caller must make any desired changes.
        
        2. All :class:`geosoft.gxapi.GXVA` types are supported and will be converted using
        Convert_GS if necessary.
        """
        self._wrapper.copy2(p2, p3, p4._wrapper, p5, p6, p7, p8)
        



    @classmethod
    def create(cls, p1, p2, p3):
        """
        Create a :class:`geosoft.gxapi.GXVA`.
        """
        ret_val = gxapi_cy.WrapVA.create(GXContext._get_tls_geo(), p1, p2, p3)
        return GXVA(ret_val)



    @classmethod
    def create_ext(cls, p1, p2, p3):
        """
        Create a :class:`geosoft.gxapi.GXVA`, using one of the `GS_TYPES` special data types.

        **Note:**

        See Create_VV
        """
        ret_val = gxapi_cy.WrapVA.create_ext(GXContext._get_tls_geo(), p1, p2, p3)
        return GXVA(ret_val)



    @classmethod
    def create_vv(cls, p1, p2, p3):
        """
        Create a :class:`geosoft.gxapi.GXVA` using the data in a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        See Create_VV
        """
        ret_val = gxapi_cy.WrapVA.create_vv(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        return GXVA(ret_val)






    def get_full_vv(self):
        """
        Get the full :class:`geosoft.gxapi.GXVV` from the :class:`geosoft.gxapi.GXVA`.

        **Note:**

        No data is copied, this is the handle to the data :class:`geosoft.gxapi.GXVV` in the :class:`geosoft.gxapi.GXVA`.
        The fid start/increment of the :class:`geosoft.gxapi.GXVA` is passed to the :class:`geosoft.gxapi.GXVV` at the time
        of the call.  If a new :class:`geosoft.gxapi.GXVA` is read, you must call GetFull_VV_VA
        to get the new fid in the :class:`geosoft.gxapi.GXVV`.
        """
        ret_val = self._wrapper.get_full_vv()
        return GXVV(ret_val)




    def get_vv(self, p2, p3, p4):
        """
        Get a row or column of data as a :class:`geosoft.gxapi.GXVV` from an array.
        """
        self._wrapper.get_vv(p2, p3, p4._wrapper)
        




    def col(self):
        """
        Return number of columns in :class:`geosoft.gxapi.GXVA`

        **Note:**

        iLen_VA returns the number of rows.
        """
        ret_val = self._wrapper.col()
        return ret_val




    def get_int(self, p2, p3):
        """
        Get an integer element from a :class:`geosoft.gxapi.GXVA`.

        **Note:**

        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        ret_val = self._wrapper.get_int(p2, p3)
        return ret_val




    def get_string(self, p2, p3, p4):
        """
        Get a string element from a :class:`geosoft.gxapi.GXVA`.

        **Note:**

        Returns element wanted, :attr:`geosoft.gxapi.rDUMMY`, :attr:`geosoft.gxapi.iDUMMY` or blank string
        if the value is dummy or outside of the range of data.
        
        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        p4.value = self._wrapper.get_string(p2, p3, p4.value.encode())
        




    def len(self):
        """
        Return length (number of rows) in a :class:`geosoft.gxapi.GXVA`.

        **Note:**

        iCol_VA returns the number of columns.
        """
        ret_val = self._wrapper.len()
        return ret_val



    @classmethod
    def index_order(cls, p1, p2):
        """
        Reorder a :class:`geosoft.gxapi.GXVA` based on an index :class:`geosoft.gxapi.GXVV`

        **Note:**

        Given a row index :class:`geosoft.gxapi.GXVV` (of type INT), this method reorders a
        :class:`geosoft.gxapi.GXVA`. Please make sure that the index holds valid information.
        """
        gxapi_cy.WrapVA.index_order(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        




    def lookup_index(self, p2, p3):
        """
        Lookup a :class:`geosoft.gxapi.GXVA` from another :class:`geosoft.gxapi.GXVA` using an index :class:`geosoft.gxapi.GXVV`.

        **Note:**

        Fractional values in the :class:`geosoft.gxapi.GXVV` will interpolate between the value
        at the whole integer value and the next whole integer, dummy
        if outside the :class:`geosoft.gxapi.GXVA`.
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
        Re-sample a :class:`geosoft.gxapi.GXVA` to a new fid start/icrement
        """
        self._wrapper.re_fid(p2, p3, p4)
        




    def reverse(self):
        """
        Reverses the order of the rows in a :class:`geosoft.gxapi.GXVA`.
        """
        self._wrapper.reverse()
        




    def get_fid_incr(self):
        """
        Gets the Fiducial increment from a :class:`geosoft.gxapi.GXVA`
        """
        ret_val = self._wrapper.get_fid_incr()
        return ret_val




    def get_fid_start(self):
        """
        Gets the Fiducial start from a :class:`geosoft.gxapi.GXVA`
        """
        ret_val = self._wrapper.get_fid_start()
        return ret_val




    def get_double(self, p2, p3):
        """
        Get a real element from a :class:`geosoft.gxapi.GXVA`.

        **Note:**

        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        ret_val = self._wrapper.get_double(p2, p3)
        return ret_val




    def set_fid_incr(self, p2):
        """
        Sets the Fiducial increment of a :class:`geosoft.gxapi.GXVA`
        """
        self._wrapper.set_fid_incr(p2)
        




    def set_fid_start(self, p2):
        """
        Sets the Fiducial start of a :class:`geosoft.gxapi.GXVA`
        """
        self._wrapper.set_fid_start(p2)
        




    def set_int(self, p2, p3, p4):
        """
        Set an integer element in a :class:`geosoft.gxapi.GXVA`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current :class:`geosoft.gxapi.GXVA` length, the :class:`geosoft.gxapi.GXVA` length is
        increased.
        """
        self._wrapper.set_int(p2, p3, p4)
        




    def set_ln(self, p2):
        """
        Set the length (number of rows) of the :class:`geosoft.gxapi.GXVA`

        **Note:**

        The number of columns in a :class:`geosoft.gxapi.GXVA` is fixed, and cannot be
        altered once the :class:`geosoft.gxapi.GXVA` is created.
        """
        self._wrapper.set_ln(p2)
        




    def set_double(self, p2, p3, p4):
        """
        Set a real element in a :class:`geosoft.gxapi.GXVA`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current :class:`geosoft.gxapi.GXVA` length, the :class:`geosoft.gxapi.GXVA` length is
        increased.
        """
        self._wrapper.set_double(p2, p3, p4)
        




    def set_string(self, p2, p3, p4):
        """
        Set a string element in a :class:`geosoft.gxapi.GXVA`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current :class:`geosoft.gxapi.GXVA` length, the :class:`geosoft.gxapi.GXVA` length is
        increased.
        """
        self._wrapper.set_string(p2, p3, p4.encode())
        




    def set_vv(self, p2, p3, p4):
        """
        Set a row or column of data in an array from a :class:`geosoft.gxapi.GXVV`.
        """
        self._wrapper.set_vv(p2, p3, p4._wrapper)
        




    def trans(self, p2, p3):
        """
        Translate (:class:`geosoft.gxapi.GXVA` + base ) * mult

        **Note:**

        Supports all :class:`geosoft.gxapi.GXVA` types using an internal double :class:`geosoft.gxapi.GXVV`.
        """
        self._wrapper.trans(p2, p3)
        




    def window(self, p2, p3, p4):
        """
        Window a :class:`geosoft.gxapi.GXVA` to a :class:`geosoft.gxapi.GXVV` based in intergral frame

        **Note:**

        The defined window must be within the :class:`geosoft.gxapi.GXVA` element dimensions.
        The windowed result will be the simple sum of all
        values in the window.
        If any values are dummy, the result will be dummy.
        """
        self._wrapper.window(p2, p3, p4._wrapper)
        




    def window2(self, p2, p3, p4):
        """
        Window a :class:`geosoft.gxapi.GXVA` to a :class:`geosoft.gxapi.GXVV` based on fractional frame

        **Note:**

        The defined window must be within the :class:`geosoft.gxapi.GXVA` element dimensions.
        The windowed result will be the simple sum of all
        values in the window.
        If any values are dummy, the result will be dummy.
        """
        self._wrapper.window2(p2, p3, p4._wrapper)
        




    def check_for_repeating(self, p2, p3, p4, p5):
        """
        Window a :class:`geosoft.gxapi.GXVA` to a :class:`geosoft.gxapi.GXVV` based on fractional frame

        **Note:**

        Returns 1 if all rows contain values which match the input values.
        Optionally, row values can be offset by amounts specified with a secondary :class:`geosoft.gxapi.GXVV`.
        This function was designed to detect "depth" array channels, including those which might
        have been offset with topography on each row.
        An absolute tolerance can be specified to ignore numerical noise.
        """
        ret_val = self._wrapper.check_for_repeating(p2._wrapper, p3, p4._wrapper, p5)
        return ret_val




    def check_for_repeating2(self, p2, p3, p4, p5, p6, p7):
        """
        Window a :class:`geosoft.gxapi.GXVA` to a :class:`geosoft.gxapi.GXVV` based on fractional frame

        **Note:**

        Returns 1 if all rows contain values which match the input values.
        Optionally, row values can be offset by amounts specified with a secondary :class:`geosoft.gxapi.GXVV`.
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