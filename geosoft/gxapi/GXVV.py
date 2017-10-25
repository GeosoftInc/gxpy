### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
from . import gxapi_cy_extend
import numpy as np
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVV:
    """
    GXVV class.

    The :class:`geosoft.gxapi.GXVV` class stores very long vector (array) data (such
    as channel data from an OASIS database) in memory and
    performs specific actions on the data. This set of
    functions is similar to the :class:`geosoft.gxapi.GXVM` functions except that
    you cannot access data directly and therefore you cannot
    use a :class:`geosoft.gxapi.GXVV` to pass data to an external (non-Geosoft)
    Dynamic Link Library (DLL) object function.
    
    If you want to pass data to a DLL, you must move a subset
    of the data stored in memory to a small vector object and
    then use the GetPtrVM_GEO function to pass a pointer to the
    data on to the external function.
    
    See :class:`geosoft.gxapi.GXVVU` for more utility methods.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVV(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXVV`
        
        :returns: A null :class:`geosoft.gxapi.GXVV`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXVV` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXVV`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def get_data(self, start, elements, data, gs_type):
        """
        Copy data from user memory to a :class:`geosoft.gxapi.GXVV`
        """
        self._wrapper.get_data(start, elements, data, gs_type)
        




    def set_data(self, start, elements, data, gs_type):
        """
        Copy data from user memory to a :class:`geosoft.gxapi.GXVV`
        """
        self._wrapper.set_data(start, elements, data, gs_type)
        




    def copy(self, p2):
        """
        Copy one :class:`geosoft.gxapi.GXVV` to another.
        """
        self._wrapper.copy(p2._wrapper)
        




    def copy2(self, p2, p3, p4, p5):
        """
        Copy part of a vector into part of another vector.

        **Note:**

        1. Unlike Copy_VV destination :class:`geosoft.gxapi.GXVV` is not reallocated, nor is
        the length changed. The caller must make any desired changes.
        
        2. All :class:`geosoft.gxapi.GXVV` types are supported and will be converted using
        Convert_GS if necessary.
        """
        self._wrapper.copy2(p2, p3._wrapper, p4, p5)
        




    def log(self, p2, p3, p4):
        """
        Apply log to the vv.

        **Note:**

        Minimum value will be defaulted to 1.0 if it is 0.0 or
        less than 0.0
        """
        self._wrapper.log(p2, p3, p4)
        




    def log_linear(self, p2):
        """
        Take the log10 or original value of a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        If the data is in the range +/- minimum value,
        it is left alone. Otherwise, the result is calculated as
        
        d = dMin * (log10(fabs(d)/dMin)+1.0)
        
        Sign is reapplied to d.
        
        Minimum value will be defaulted to 1.0 if it is negative
        or 0.
        """
        self._wrapper.log_linear(p2)
        




    def mask(self, p2):
        """
        Mask one :class:`geosoft.gxapi.GXVV` against another.

        **Note:**

        All elements in the mask :class:`geosoft.gxapi.GXVV` that are dummies will replace
        the value in the original :class:`geosoft.gxapi.GXVV` with a dummy.
        
        The modified :class:`geosoft.gxapi.GXVV` will always be the same length as the mask
        :class:`geosoft.gxapi.GXVV` after this call.  If the mask is longer than the target,
        the target will be lengthenned with dummies.
        """
        self._wrapper.mask(p2._wrapper)
        




    def reverse(self):
        """
        Reverses the order of the data in a :class:`geosoft.gxapi.GXVV`.
        """
        self._wrapper.reverse()
        




    def serial(self, p2):
        """
        Serialize
        """
        self._wrapper.serial(p2._wrapper)
        




    def trans(self, p2, p3):
        """
        Translate (:class:`geosoft.gxapi.GXVV` + base ) * mult

        **Note:**

        All :class:`geosoft.gxapi.GXVV` types now supported.
        """
        self._wrapper.trans(p2, p3)
        




    def abs(self):
        """
        Take the absolute value of values in a :class:`geosoft.gxapi.GXVV`.
        """
        self._wrapper.abs()
        




    def add(self, p2, p3):
        """
        Add two VVs: VV_A + VV_B = VV_C
        """
        self._wrapper.add(p2._wrapper, p3._wrapper)
        




    def add2(self, p2, p3, p4, p5):
        """
        Add two VVs with linear factors: VV_A*f1 + VV_B*f2 = VV_C

        **Note:**

        The multipliers must be defined and within the :attr:`geosoft.gxapi.GS_R8MN` :attr:`geosoft.gxapi.GS_R8MX` range.
        """
        self._wrapper.add2(p2, p3._wrapper, p4, p5._wrapper)
        




    def append(self, p2):
        """
        Appends :class:`geosoft.gxapi.GXVV`'s
        """
        self._wrapper.append(p2._wrapper)
        




    def crc(self, p2):
        """
        Compute the CRC value of a :class:`geosoft.gxapi.GXVV`.
        """
        ret_val = self._wrapper.crc(p2)
        return ret_val




    def crc_inexact(self, p2, p3, p4):
        """
        Compute the CRC value of a :class:`geosoft.gxapi.GXVV` and allows you to specify
        number of bits of floats/doubles to drop so that the CRC
        will be same even of this are changed.

        **Note:**

        Very usefull for testing where the last bits of accuracy
        are not as important.
        """
        ret_val = self._wrapper.crc_inexact(p2, p3, p4)
        return ret_val



    @classmethod
    def create(cls, p1, p2):
        """
        Create a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        To set the fiducial start and increment for the data in the :class:`geosoft.gxapi.GXVV`
        you need to call SetFidStart_VV and SetFidIncr_VV.
        
        If you are basing the :class:`geosoft.gxapi.GXVV` data on fiducial information from a
        different :class:`geosoft.gxapi.GXVV`, call GetFidStart_VV and GetFidIncr_VV to obtain
        that :class:`geosoft.gxapi.GXVV`'s fiducial information. Do this prior to setting the
        new :class:`geosoft.gxapi.GXVV`'s fiducial start and increment.
        
        If you do not know the required length for a :class:`geosoft.gxapi.GXVV`, use 0
        and the :class:`geosoft.gxapi.GXVV` length will be adjusted as needed.  This is
        a bit less efficient than setting the length when you
        know it.
        """
        ret_val = gxapi_cy.WrapVV.create(GXContext._get_tls_geo(), p1, p2)
        return GXVV(ret_val)



    @classmethod
    def create_ext(cls, p1, p2):
        """
        Create a :class:`geosoft.gxapi.GXVV`, using one of the `GS_TYPES` special data types.

        **Note:**

        See Create_VV
        
        Do not use data type flags: :attr:`geosoft.gxapi.GS_INT` or :attr:`geosoft.gxapi.GS_REAL` on CreateExt(),
        this will result in a respective data type of unsigned byte or
        short for the :class:`geosoft.gxapi.GXVV`.
        """
        ret_val = gxapi_cy.WrapVV.create_ext(GXContext._get_tls_geo(), p1, p2)
        return GXVV(ret_val)



    @classmethod
    def create_s(cls, p1):
        """
        Create a :class:`geosoft.gxapi.GXVV`  from serialized source.
        """
        ret_val = gxapi_cy.WrapVV.create_s(GXContext._get_tls_geo(), p1._wrapper)
        return GXVV(ret_val)






    def diff(self, p2):
        """
        Calculate differences.

        **Note:**

        Differences with dummies result in dummies.
        An even number of differences locates data accurately.
        An odd number of differences locates result 1/2 element lower
        in the :class:`geosoft.gxapi.GXVV`.
        """
        self._wrapper.diff(p2)
        




    def divide(self, p2, p3):
        """
        Divide one :class:`geosoft.gxapi.GXVV` by another: VV_A / VV_B = VV_C
        """
        self._wrapper.divide(p2._wrapper, p3._wrapper)
        




    def fid_norm(self, p2):
        """
        Re-sample a pair of :class:`geosoft.gxapi.GXVV`'s to match each other.

        **Note:**

        Both :class:`geosoft.gxapi.GXVV`'s will return with the same start
        fid and fid increment.  The smaller start fid
        and fid increment will be used.
        """
        self._wrapper.fid_norm(p2._wrapper)
        




    def fill_int(self, p2):
        """
        Fill a :class:`geosoft.gxapi.GXVV` with an int value.
        """
        self._wrapper.fill_int(p2)
        




    def fill_double(self, p2):
        """
        Fill a :class:`geosoft.gxapi.GXVV` with a real value.
        """
        self._wrapper.fill_double(p2)
        




    def fill_string(self, p2):
        """
        Fill a :class:`geosoft.gxapi.GXVV` with a string value.
        """
        self._wrapper.fill_string(p2.encode())
        




    def count_dummies(self, p2, p3):
        """
        Count the number of dummies in a :class:`geosoft.gxapi.GXVV`
        """
        ret_val = self._wrapper.count_dummies(p2, p3)
        return ret_val




    def find_dum(self, p2, p3, p4, p5):
        """
        Finds the first dummy or non-dummy value in a :class:`geosoft.gxapi.GXVV`

        **Note:**

        If a decreasing order search is performed, it will start
        at the highest element specified. (Conversely, an increasing
        order starts at the lowest element specified.)
        """
        ret_val = self._wrapper.find_dum(p2, p3, p4, p5)
        return ret_val




    def get_fid_expansion(self):
        """
        Gets the Fiducial expansion from a :class:`geosoft.gxapi.GXVV`
        """
        ret_val = self._wrapper.get_fid_expansion()
        return ret_val




    def get_int(self, p2):
        """
        Get an integer element from a :class:`geosoft.gxapi.GXVV`.
        """
        ret_val = self._wrapper.get_int(p2)
        return ret_val




    def get_string(self, p2, p3):
        """
        Get a string element from a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        Returns Element wanted, or blank string
        if the value is dummy or outside of the range of data.
        
        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        p3.value = self._wrapper.get_string(p2, p3.value.encode())
        




    def index_max(self, p2):
        """
        Get the index where the maximum value occurs.

        **Note:**

        If more than one value has the same maximum value, the index of the
        first is returned.
        """
        ret_val, p2.value = self._wrapper.index_max(p2.value)
        return ret_val




    def length(self):
        """
        Returns current :class:`geosoft.gxapi.GXVV` length.
        """
        ret_val = self._wrapper.length()
        return ret_val




    def index_insert(self, p2, p3):
        """
        Insert items into a :class:`geosoft.gxapi.GXVV` using an index :class:`geosoft.gxapi.GXVV`.

        **Note:**

        The items in the input data :class:`geosoft.gxapi.GXVV` are inserted into
        the output :class:`geosoft.gxapi.GXVV` using the indices in the index :class:`geosoft.gxapi.GXVV`.
        Values not referenced are not altered, so the output
        :class:`geosoft.gxapi.GXVV` should be pre-initialized. The output :class:`geosoft.gxapi.GXVV` length
        will NOT be changed, and index values referencing
        beyond the end of the output :class:`geosoft.gxapi.GXVV` data will return an
        error.
        
        This function is useful when working with channel data that include
        dummies, but where the dummies must be removed before processing.
        Create and initialize an index (0, 1, 2...) :class:`geosoft.gxapi.GXVV`, using the InitIndex_VV
        function, and when you remove
        the dummies, remove the corresponding index values as well.
        After processing, init a :class:`geosoft.gxapi.GXVV` to dummies, then use IndexInsert_VV to
        put the processed values at the correct locations in the data :class:`geosoft.gxapi.GXVV`
        before you write it back to the channel.
        """
        self._wrapper.index_insert(p2._wrapper, p3._wrapper)
        




    def index_order(self, p2):
        """
        Reorder a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        Given an index :class:`geosoft.gxapi.GXVV` (of type INT), this method reorders a
        :class:`geosoft.gxapi.GXVV`. Please make sure that the index holds valid information.
        """
        self._wrapper.index_order(p2._wrapper)
        




    def init_index(self, p2):
        """
        Initialize an index :class:`geosoft.gxapi.GXVV` to values 0, 1, 2, etc...

        **Note:**

        Populates a :class:`geosoft.gxapi.GXVV` with the values 0, 1, 2, 3, 4 etc., to be
        used for various indexing functions, such as IndexInsert_VV or
        IndexOrder_VV.
        """
        self._wrapper.init_index(p2)
        




    def inv_log(self, p2, p3, p4):
        """
        Inverse of the Log_VV function.

        **Note:**

        This is the inverse function for Log_VV, with the same inputs.
        
        NEGATIVE_NO    - will not return values smaller than the input minimum
        NEGATIVE_YES   - if the data is in the range +/- minimum,
        it is left alone.  Otherwise, the sign is removed,
        the minimum is subtracted, the log of the minimum is added,
        and the exponential (base e or base 10) is taken of the
        sum. The sign is then reapplied.
        Minimum value will be defaulted to 1.0 if it is 0.0 or
        less than 0.0
        """
        self._wrapper.inv_log(p2, p3, p4)
        




    def order(self, p2):
        """
        Identifies the data size order of the elements.
        """
        ret_val, p2.value = self._wrapper.order(p2.value)
        return ret_val




    def lines_to_xy(self, p2, p3):
        """
        Convert a 2D Line segment :class:`geosoft.gxapi.GXVV` into X and Y VVs.

        **Note:**

        Some GX functions (such as GetVoronoiEdges_TIN) return
        a special :class:`geosoft.gxapi.GXVV` where each element contains the start and end
        points of lines, (X_1, Y_1) and (X_2, Y_2).
        This GX dumps the individual X and Y values into individual
        X and Y VVs of type :attr:`geosoft.gxapi.GS_DOUBLE` (REAL). N lines produces 2*N
        X and Y values.
        """
        self._wrapper.lines_to_xy(p2._wrapper, p3._wrapper)
        




    def lookup_index(self, p2, p3):
        """
        Lookup a :class:`geosoft.gxapi.GXVV` from another :class:`geosoft.gxapi.GXVV` using an index :class:`geosoft.gxapi.GXVV`.

        **Note:**

        This method assigns index values of 0.0, 1.0, 2.0 etc. to the individual
        values in the input Data :class:`geosoft.gxapi.GXVV`, and uses linear interpolation to calculate the values of
        Result :class:`geosoft.gxapi.GXVV` at the input indices contained in the Index :class:`geosoft.gxapi.GXVV`.
        
        If the input Data :class:`geosoft.gxapi.GXVV` is string type, then only values at the integral index values
        are returned.
        
        See also SetupIndex_VV for an example of how this can be implemented.
        """
        self._wrapper.lookup_index(p2._wrapper, p3._wrapper)
        




    def make_mem_based(self):
        """
        Make this :class:`geosoft.gxapi.GXVV` use regular instead of virtual memory.

        **Note:**

        This function should be called immediately aftter
        Create_VV.
        
        Normal VVs are optimised to prevent thrashing, and to
        efficiently support many extremely large VVs, although
        there is a small performance penalty.
        This function is intended for :class:`geosoft.gxapi.GXVV`'s that you know can be
        handled by the operating system virtual memory manager,
        and will be used heavily.  By using a memory based :class:`geosoft.gxapi.GXVV`, you
        can achieve some performance improvements provided your
        application does not cause the memory manager to "thrash".
        
        External programs that use the GX API may prefer to use
        memory-based :class:`geosoft.gxapi.GXVV`'s because you can get direct access to
        the :class:`geosoft.gxapi.GXVV` through the GetPtrVV_GEO function (see gx_extern.h).
        """
        self._wrapper.make_mem_based()
        




    def mask_and(self, p2, p3):
        """
        Create mask from logical AND of two VVs.

        **Note:**

        If both values are non-dummies, then result is 1, else dummy.
        """
        self._wrapper.mask_and(p2._wrapper, p3._wrapper)
        




    def mask_or(self, p2, p3):
        """
        Create mask from logical OR of two VVs.

        **Note:**

        If either values is non-dummy, then result is 1, else dummy.
        """
        self._wrapper.mask_or(p2._wrapper, p3._wrapper)
        




    def mask_str(self, p2, p3):
        """
        Mask one :class:`geosoft.gxapi.GXVV` against another using a string.

        **Note:**

        All elements in the mask :class:`geosoft.gxapi.GXVV` that are same as string will replace
        the original :class:`geosoft.gxapi.GXVV` with a 1.
        
        The modified :class:`geosoft.gxapi.GXVV` will always be expanded to the MaskVV size but
        not shortened after this call.  If the mask is longer than the target,
        the target will be lengthenned with dummies before applying the mask.
        """
        self._wrapper.mask_str(p2._wrapper, p3.encode())
        




    def multiply(self, p2, p3):
        """
        Multiply two VVs: VV_A * VV_B = VV_C
        """
        self._wrapper.multiply(p2._wrapper, p3._wrapper)
        




    def amplitude_3d(self, p2, p3, p4):
        """
        Calculate the 3D length for XYZ component VVs
        """
        self._wrapper.amplitude_3d(p2._wrapper, p3._wrapper, p4._wrapper)
        




    def polygon_mask(self, p2, p3, p4, p5):
        """
        Mask a :class:`geosoft.gxapi.GXVV` using XY data and a polygon

        **Note:**

        The VVs has to be the same length
        """
        self._wrapper.polygon_mask(p2._wrapper, p3._wrapper, p4._wrapper, p5)
        



    @classmethod
    def project(cls, p1, p2, p3):
        """
        This method projects an X and Y :class:`geosoft.gxapi.GXVV`.

        **Note:**

        This function is equivalent to ConvertVV_PJ.
        """
        gxapi_cy.WrapVV.project(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def project_3d(cls, p1, p2, p3, p4):
        """
        This method projects an X,Y,Z :class:`geosoft.gxapi.GXVV`.

        **Note:**

        This function is equivalent to ConvertVV3_PJ.
        """
        gxapi_cy.WrapVV.project_3d(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        




    def range_double(self, p2, p3):
        """
        Get the min. and max. values of a :class:`geosoft.gxapi.GXVV` while ignoring dummies.

        **Note:**

        Minimum and maximum become :attr:`geosoft.gxapi.GS_R8DM` if entire :class:`geosoft.gxapi.GXVV` is dummy.
        """
        p2.value, p3.value = self._wrapper.range_double(p2.value, p3.value)
        




    def re_fid(self, p2, p3, p4):
        """
        Re-sample a :class:`geosoft.gxapi.GXVV` to a new fid start/icrement
        """
        self._wrapper.re_fid(p2, p3, p4)
        




    def re_fid_vv(self, p2):
        """
        Re-sample a :class:`geosoft.gxapi.GXVV` to match another :class:`geosoft.gxapi.GXVV`.

        **Note:**

        This method will honor the :class:`geosoft.gxapi.GXVV` FID Expansion and will expand/contract
        :class:`geosoft.gxapi.GXVV`'s based on this flag if it is used.
        """
        self._wrapper.re_fid_vv(p2._wrapper)
        




    def re_sample(self, p2, p3, p4, p5, p6, p7):
        """
        Resamples a :class:`geosoft.gxapi.GXVV` from one fid/incr to another fid/incr.
        """
        self._wrapper.re_sample(p2, p3, p4, p5, p6, p7)
        




    def get_fid_incr(self):
        """
        Gets the Fiducial increment from a :class:`geosoft.gxapi.GXVV`
        """
        ret_val = self._wrapper.get_fid_incr()
        return ret_val




    def get_fid_start(self):
        """
        Gets the Fiducial start from a :class:`geosoft.gxapi.GXVV`
        """
        ret_val = self._wrapper.get_fid_start()
        return ret_val




    def get_double(self, p2):
        """
        Get a real element from a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        ret_val = self._wrapper.get_double(p2)
        return ret_val




    def sum(self):
        """
        Calculate the sum of the values in a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        Dummy value is treated as Zero(0)
        """
        ret_val = self._wrapper.sum()
        return ret_val




    def weighted_mean(self, p2):
        """
        Calculate the weighted average of the values.

        **Note:**

        Dummy values are ignored.
        """
        ret_val = self._wrapper.weighted_mean(p2._wrapper)
        return ret_val




    def set_fid_expansion(self, p2):
        """
        Sets the Fiducial expansion from a :class:`geosoft.gxapi.GXVV`
        """
        self._wrapper.set_fid_expansion(p2)
        




    def set_fid_incr(self, p2):
        """
        Sets the Fiducial increment of a :class:`geosoft.gxapi.GXVV`
        """
        self._wrapper.set_fid_incr(p2)
        




    def set_fid_start(self, p2):
        """
        Sets the Fiducial start of a :class:`geosoft.gxapi.GXVV`
        """
        self._wrapper.set_fid_start(p2)
        




    def set_int(self, p2, p3):
        """
        Set an integer element in a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current :class:`geosoft.gxapi.GXVV` length, the :class:`geosoft.gxapi.GXVV` length is
        increased.
        It is good practice to set the length ahead of time to the
        expected maximum value, as some :class:`geosoft.gxapi.GXVV` processes rely on the
        current maximum length of the :class:`geosoft.gxapi.GXVV` when you pass it in as an
        argument, and unexpected results may occur if the length is
        not what you expect it to be because of dynamic allocation at
        an earlier time.
        """
        self._wrapper.set_int(p2, p3)
        




    def set_int_n(self, p2, p3, p4):
        """
        Set N integer elements in a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current :class:`geosoft.gxapi.GXVV` length, the :class:`geosoft.gxapi.GXVV` length is
        increased.
        """
        self._wrapper.set_int_n(p2, p3, p4)
        




    def set_len(self, p2):
        """
        Set the length of a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        If increasing the :class:`geosoft.gxapi.GXVV` size, new elements are set to dummies.
        
        It is good practice to set the length ahead of time to the
        expected maximum value, as some :class:`geosoft.gxapi.GXVV` processes rely on the
        current maximum length of the :class:`geosoft.gxapi.GXVV` when you pass it in as an
        argument, and unexpected results may occur if the length is
        not what you expect it to be because of dynamic allocation at
        an earlier time.
        """
        self._wrapper.set_len(p2)
        




    def set_double(self, p2, p3):
        """
        Set a real element in a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current :class:`geosoft.gxapi.GXVV` length, the :class:`geosoft.gxapi.GXVV` length is
        increased.
        It is good practice to set the length ahead of time to the
        expected maximum value, as some :class:`geosoft.gxapi.GXVV` processes rely on the
        current maximum length of the :class:`geosoft.gxapi.GXVV` when you pass it in as an
        argument, and unexpected results may occur if the length is
        not what you expect it to be because of dynamic allocation at
        an earlier time.
        """
        self._wrapper.set_double(p2, p3)
        




    def set_double_n(self, p2, p3, p4):
        """
        Set N real elements in a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current :class:`geosoft.gxapi.GXVV` length, the :class:`geosoft.gxapi.GXVV` length is
        increased.
        """
        self._wrapper.set_double_n(p2, p3, p4)
        




    def set_string(self, p2, p3):
        """
        Set a string element in a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current :class:`geosoft.gxapi.GXVV` length, the :class:`geosoft.gxapi.GXVV` length is
        increased.
        It is good practice to set the length ahead of time to the
        expected maximum value, as some :class:`geosoft.gxapi.GXVV` processes rely on the
        current maximum length of the :class:`geosoft.gxapi.GXVV` when you pass it in as an
        argument, and unexpected results may occur if the length is
        not what you expect it to be because of dynamic allocation at
        an earlier time.
        """
        self._wrapper.set_string(p2, p3.encode())
        




    def set_string_n(self, p2, p3, p4):
        """
        Set N string elements in a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        Element being set cannot be < 0.
        If the element is > current :class:`geosoft.gxapi.GXVV` length, the :class:`geosoft.gxapi.GXVV` length is
        increased.
        """
        self._wrapper.set_string_n(p2, p3, p4.encode())
        




    def setup_index(self, p2, p3, p4, p5):
        """
        Setup an index :class:`geosoft.gxapi.GXVV` from VV1 to VV2.

        **Note:**

        The input reference :class:`geosoft.gxapi.GXVV` must be in ascending numerical order.
        If your reference data is NOT ordered, then use the the
        SortIndex1_VV function to create an order index, then sort
        both the reference and data VVs using this index :class:`geosoft.gxapi.GXVV` before
        you call SetupIndex_VV.
        
        Example: You have a reference data set taken at specific times, hVVt, hVVy
        and you want to calculate/estimate/interpolate the values hVVy2 at a second set
        of times hVVt2
        
        Step 1: Create an index, hVVi, type :attr:`geosoft.gxapi.GS_DOUBLE`, and call SetupIndex_VV.
        
        e.g. : SetupIndex_VV(hVVt, hVVt2, hVVi, VV_LOOKUP_XXX, rSpacing);
        
        Internally, this assigns index values of 0.0, 1.0, 2.0 etc. to the individual
        values in hVVt, then, depending on the lookup method chosen, assigns
        fractional index values to the input values in hVVt2.
        
        Step 2: To determine what the lookup values hVVy2 should be at times hVVt2,
        call the sLookupIndex_VV function:
        
        e.g. : LookupIndex_VV(hVVy, hVVi, hVVy2);
        
        Internally, this assigns index values of 0.0, 1.0, 2.0 etc. to the individual
        values in hVVy, and uses linear interpolation to calculate the values of
        hVVy2 at the input indices contained in hVVi.
        """
        self._wrapper.setup_index(p2._wrapper, p3._wrapper, p4, p5)
        




    def sort(self, p2):
        """
        Sort a :class:`geosoft.gxapi.GXVV`.
        """
        self._wrapper.sort(p2)
        




    def sort_index(self, p2):
        """
        Sort index :class:`geosoft.gxapi.GXVV` based on a data :class:`geosoft.gxapi.GXVV`.

        **Note:**

        Create an Index :class:`geosoft.gxapi.GXVV` (of type :attr:`geosoft.gxapi.GS_LONG`) based on a data :class:`geosoft.gxapi.GXVV`.
        This index vv can then be used by the IndexOrder method
        to order a group of :class:`geosoft.gxapi.GXVV`'s.
        """
        self._wrapper.sort_index(p2._wrapper)
        




    def sort_index1(self, p2, p3):
        """
        Sort index :class:`geosoft.gxapi.GXVV` based on 1 data :class:`geosoft.gxapi.GXVV` - set orders.

        **Note:**

        Create an Index :class:`geosoft.gxapi.GXVV` (of type :attr:`geosoft.gxapi.GS_LONG`) based on a data :class:`geosoft.gxapi.GXVV`.
        This index vv can then be used by the IndexOrder method
        to order a group of :class:`geosoft.gxapi.GXVV`'s. The individual VVs may be ordered
        in ascending or descending order.
        If the primary :class:`geosoft.gxapi.GXVV` values of two indices are the same, then
        the secondary :class:`geosoft.gxapi.GXVV` values are compared. If the secondary values
        are the same, the ternary values are compared, etc.
        """
        self._wrapper.sort_index1(p2._wrapper, p3)
        




    def sort_index2(self, p2, p3, p4, p5):
        """
        Sort index :class:`geosoft.gxapi.GXVV` based on 2 data VVs - set orders.

        **Note:**

        Create an Index :class:`geosoft.gxapi.GXVV` (of type :attr:`geosoft.gxapi.GS_LONG`) based on a data :class:`geosoft.gxapi.GXVV`.
        This index vv can then be used by the IndexOrder method
        to order a group of :class:`geosoft.gxapi.GXVV`'s. The individual VVs may be ordered
        in ascending or descending order.
        If the primary :class:`geosoft.gxapi.GXVV` values of two indices are the same, then
        the secondary :class:`geosoft.gxapi.GXVV` values are compared. If the secondary values
        are the same, the ternary values are compared, etc
        """
        self._wrapper.sort_index2(p2._wrapper, p3._wrapper, p4, p5)
        




    def sort_index3(self, p2, p3, p4, p5, p6, p7):
        """
        Sort index :class:`geosoft.gxapi.GXVV` based on 3 data VVs - set orders.

        **Note:**

        Create an Index :class:`geosoft.gxapi.GXVV` (of type :attr:`geosoft.gxapi.GS_LONG`) based on a data :class:`geosoft.gxapi.GXVV`.
        This index vv can then be used by the IndexOrder method
        to order a group of :class:`geosoft.gxapi.GXVV`'s. The individual VVs may be ordered
        in ascending or descending order.
        If the primary :class:`geosoft.gxapi.GXVV` values of two indices are the same, then
        the secondary :class:`geosoft.gxapi.GXVV` values are compared. If the secondary values
        are the same, the third values are compared, etc
        """
        self._wrapper.sort_index3(p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7)
        




    def sort_index4(self, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Sort index :class:`geosoft.gxapi.GXVV` based on 4 data VVs - set orders.

        **Note:**

        Create an Index :class:`geosoft.gxapi.GXVV` (of type :attr:`geosoft.gxapi.GS_LONG`) based on a data :class:`geosoft.gxapi.GXVV`.
        This index vv can then be used by the IndexOrder method
        to order a group of :class:`geosoft.gxapi.GXVV`'s. The individual VVs may be ordered
        in ascending or descending order.
        If the primary :class:`geosoft.gxapi.GXVV` values of two indices are the same, then
        the secondary :class:`geosoft.gxapi.GXVV` values are compared. If the secondary values
        are the same, the third values are compared, etc
        """
        self._wrapper.sort_index4(p2._wrapper, p3._wrapper, p4._wrapper, p5._wrapper, p6, p7, p8, p9)
        



    @classmethod
    def statistics(cls, p1, p2):
        """
        Add a :class:`geosoft.gxapi.GXVV` to a :class:`geosoft.gxapi.GXST`.
        """
        gxapi_cy.WrapVV.statistics(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        




    def subtract(self, p2, p3):
        """
        Subtract one :class:`geosoft.gxapi.GXVV` from another: VV_A - VV_B = VV_C
        """
        self._wrapper.subtract(p2._wrapper, p3._wrapper)
        




    def swap(self):
        """
        Swaps the bytes of the SHORT, USHORT, LONG, FLOAT and DOUBLE vv's.
        Other vv's are not affected by this method. This is used
        primarily with changing the order of bytes for other machine
        created data.
        """
        self._wrapper.swap()
        




    def window(self, p2, p3, p4):
        """
        Limit the elements of a vv to a range.
        """
        self._wrapper.window(p2, p3, p4)
        




    def write_xml(self, p2, p3, p4):
        """
        Write the :class:`geosoft.gxapi.GXVV` data as an XML object with bytes and formating.
        """
        self._wrapper.write_xml(p2.encode(), p3, p4)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
    def get_data_np(self, start: int, num_elements: int, np_dtype: type(np.dtype)):
        from .GXNumpy import gs_from_np
        gs_type = gs_from_np(np_dtype)
        return np.asarray(self.get_data_array(start, num_elements, gs_type))

    def set_data_np(self, start: int, np_array: type(np.ndarray)):
        from .GXNumpy import gs_from_np
        gs_type = gs_from_np(np_array.dtype)
        num_elements = np.prod(np_array.shape)
        if not np_array.flags['C_CONTIGUOUS']:
            np_array = np.ascontiguousarray(np_array)
        self.set_data(start, num_elements, np_array.data.tobytes(), gs_type)
    
    def get_data_array(self, start: int, num_elements: int, gs_type: int):
        return gxapi_cy_extend.GXMemMethods.get_data_array_vv(GXContext._internal_p(), self._wrapper.handle, start, num_elements, gs_type)
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer