### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
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
class GXVV(gxapi_cy.WrapVV):
    """
    GXVV class.

    The `GXVV <geosoft.gxapi.GXVV>` class stores very long vector (array) data (such
    as channel data from an OASIS database) in memory and
    performs specific actions on the data. This set of
    functions is similar to the `GXVM <geosoft.gxapi.GXVM>` functions except that
    you cannot access data directly and therefore you cannot
    use a `GXVV <geosoft.gxapi.GXVV>` to pass data to an external (non-Geosoft)
    Dynamic Link Library (DLL) object function.

    If you want to pass data to a DLL, you must move a subset
    of the data stored in memory to a small vector object and
    then use the `GXGEO.get_ptr_vm <geosoft.gxapi.GXGEO.get_ptr_vm>` function to pass a pointer to the
    data on to the external function.

    See `GXVVU <geosoft.gxapi.GXVVU>` for more utility methods.
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVV <geosoft.gxapi.GXVV>`
        
        :returns: A null `GXVV <geosoft.gxapi.GXVV>`
        :rtype:   GXVV
        """
        return GXVV()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def get_data(self, start, elements, data, gs_type):
        """
        Copy data from user memory to a `GXVV <geosoft.gxapi.GXVV>`
        
        :param start:     Start Location
        :param elements:  Number of Elements
        :param data:      Data buffer copy data into from `GXVV <geosoft.gxapi.GXVV>`
        :param gs_type:   :ref:`GS_TYPES`
        :type  start:     int
        :type  elements:  int
        :type  data:      bytearray
        :type  gs_type:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._get_data(start, elements, data, gs_type)
        




    def set_data(self, start, elements, data, gs_type):
        """
        Copy data from user memory to a `GXVV <geosoft.gxapi.GXVV>`
        
        :param start:     Start Location
        :param elements:  Number of Elements
        :param data:      Data buffer to copy into into `GXVV <geosoft.gxapi.GXVV>`
        :param gs_type:   :ref:`GS_TYPES`
        :type  start:     int
        :type  elements:  int
        :type  data:      bytearray
        :type  gs_type:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_data(start, elements, data, gs_type)
        




    def copy(self, vv_s):
        """
        Copy one `GXVV <geosoft.gxapi.GXVV>` to another.
        
        :param vv_s:  Source
        :type  vv_s:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._copy(vv_s)
        




    def copy2(self, dest, vv_s, source, n):
        """
        Copy part of a vector into part of another vector.
        
        :param dest:    Destination start element
        :param vv_s:    Source `GXVV <geosoft.gxapi.GXVV>` (can be the same as Destination)
        :param source:  Source start element
        :param n:       Number of points
        :type  dest:    int
        :type  vv_s:    GXVV
        :type  source:  int
        :type  n:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1. Unlike Copy_VV destination `GXVV <geosoft.gxapi.GXVV>` is not reallocated, nor is
        the length changed. The caller must make any desired changes.

        2. All `GXVV <geosoft.gxapi.GXVV>` types are supported and will be converted using
        Convert_GS if necessary.
        """
        self._copy2(dest, vv_s, source, n)
        




    def log(self, log_base, log_mode, log_min):
        """
        Apply log to the vv.
        
        :param log_base:  :ref:`VV_LOG_BASE`
        :param log_mode:  :ref:`VV_LOGMODE`
        :param log_min:   Minimum value for :ref:`VV_LOG_NEGATIVE`
        :type  log_base:  int
        :type  log_mode:  int
        :type  log_min:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Minimum value will be defaulted to 1.0 if it is 0.0 or
        less than 0.0
        """
        self._log(log_base, log_mode, log_min)
        




    def log_linear(self, log_min):
        """
        Take the log10 or original value of a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param log_min:  Minimum value
        :type  log_min:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the data is in the range +/- minimum value,
        it is left alone. Otherwise, the result is calculated as

        ::

             d = dMin * (log10(fabs(d)/dMin)+1.0)

        Sign is reapplied to d.

        Minimum value will be defaulted to 1.0 if it is negative
        or 0.
        """
        self._log_linear(log_min)
        




    def mask(self, vv_m):
        """
        Mask one `GXVV <geosoft.gxapi.GXVV>` against another.
        
        :param vv_m:  Mask `GXVV <geosoft.gxapi.GXVV>`
        :type  vv_m:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All elements in the mask `GXVV <geosoft.gxapi.GXVV>` that are dummies will replace
        the value in the original `GXVV <geosoft.gxapi.GXVV>` with a dummy.

        The modified `GXVV <geosoft.gxapi.GXVV>` will always be the same length as the mask
        `GXVV <geosoft.gxapi.GXVV>` after this call.  If the mask is longer than the target,
        the target will be lengthenned with dummies.
        """
        self._mask(vv_m)
        




    def reverse(self):
        """
        Reverses the order of the data in a `GXVV <geosoft.gxapi.GXVV>`.
        

        .. versionadded:: 5.1.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._reverse()
        




    def serial(self, bf):
        """
        Serialize
        
        :type  bf:   GXBF

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._serial(bf)
        




    def trans(self, base, mult):
        """
        Translate (`GXVV <geosoft.gxapi.GXVV>` + base ) * mult
        
        :param base:  Base value
        :param mult:  Mult value
        :type  base:  float
        :type  mult:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All `GXVV <geosoft.gxapi.GXVV>` types now supported.
        """
        self._trans(base, mult)
        




    def abs(self):
        """
        Take the absolute value of values in a `GXVV <geosoft.gxapi.GXVV>`.
        

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._abs()
        




    def add(self, vv_b, vv_c):
        """
        Add two VVs: VV_A + VV_B = VV_C
        
        :param vv_b:  `GXVV <geosoft.gxapi.GXVV>` B
        :param vv_c:  `GXVV <geosoft.gxapi.GXVV>` C (returned), C = A + B
        :type  vv_b:  GXVV
        :type  vv_c:  GXVV

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._add(vv_b, vv_c)
        




    def add2(self, f1, vv_b, f2, vv_c):
        """
        Add two VVs with linear factors: VV_A*f1 + VV_B*f2 = VV_C
        
        :param f1:    Multiplier f1 for A
        :param vv_b:  `GXVV <geosoft.gxapi.GXVV>` B
        :param f2:    Multiplier f2 for B
        :param vv_c:  `GXVV <geosoft.gxapi.GXVV>` C (returned), C = A*f1 + B*f2
        :type  f1:    float
        :type  vv_b:  GXVV
        :type  f2:    float
        :type  vv_c:  GXVV

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The multipliers must be defined and within the `GS_R8MN <geosoft.gxapi.GS_R8MN>` `GS_R8MX <geosoft.gxapi.GS_R8MX>` range.
        """
        self._add2(f1, vv_b, f2, vv_c)
        




    def append(self, vv_a):
        """
        Appends `GXVV <geosoft.gxapi.GXVV>`'s
        
        :param vv_a:  `GXVV <geosoft.gxapi.GXVV>` to append
        :type  vv_a:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._append(vv_a)
        




    def crc(self, pul_crc):
        """
        Compute the CRC value of a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param pul_crc:  Previous CRC `CRC_INIT_VALUE <geosoft.gxapi.CRC_INIT_VALUE>`
        :type  pul_crc:  int

        :returns:        CRC Value
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._crc(pul_crc)
        return ret_val




    def crc_inexact(self, pul_crc, float_bits, double_bits):
        """
        Compute the CRC value of a `GXVV <geosoft.gxapi.GXVV>` and allows you to specify
        number of bits of floats/doubles to drop so that the CRC
        will be same even of this are changed.
        
        :param pul_crc:      Previous CRC `CRC_INIT_VALUE <geosoft.gxapi.CRC_INIT_VALUE>`
        :param float_bits:   :ref:`VV_FLOAT_CRC_BITS`
        :param double_bits:  :ref:`VV_DOUBLE_CRC_BITS`
        :type  pul_crc:      int
        :type  float_bits:   int
        :type  double_bits:  int

        :returns:            CRC Value
        :rtype:              int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Very useful for testing where the last bits of accuracy
        are not as important.
        """
        ret_val = self._crc_inexact(pul_crc, float_bits, double_bits)
        return ret_val



    @classmethod
    def create(cls, type, elements):
        """
        Create a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param type:      :ref:`GEO_VAR`
        :param elements:  Maximum number of elements in the `GXVV <geosoft.gxapi.GXVV>`, >= 0
        :type  type:      int
        :type  elements:  int

        :returns:         `GXVV <geosoft.gxapi.GXVV>` Object
        :rtype:           GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** To set the fiducial start and increment for the data in the `GXVV <geosoft.gxapi.GXVV>`
        you need to call `set_fid_start <geosoft.gxapi.GXVV.set_fid_start>` and `set_fid_incr <geosoft.gxapi.GXVV.set_fid_incr>`.

        If you are basing the `GXVV <geosoft.gxapi.GXVV>` data on fiducial information from a
        different `GXVV <geosoft.gxapi.GXVV>`, call GetFidStart_VV and GetFidIncr_VV to obtain
        that `GXVV <geosoft.gxapi.GXVV>`'s fiducial information. Do this prior to setting the
        new `GXVV <geosoft.gxapi.GXVV>`'s fiducial start and increment.

        If you do not know the required length for a `GXVV <geosoft.gxapi.GXVV>`, use 0
        and the `GXVV <geosoft.gxapi.GXVV>` length will be adjusted as needed.  This is
        a bit less efficient than setting the length when you
        know it.
        """
        ret_val = gxapi_cy.WrapVV._create(GXContext._get_tls_geo(), type, elements)
        return GXVV(ret_val)



    @classmethod
    def create_ext(cls, type, elements):
        """
        Create a `GXVV <geosoft.gxapi.GXVV>`, using one of the :ref:`GS_TYPES` special data types.
        
        :param type:      :ref:`GS_TYPES`
        :param elements:  Maximum number of elements in the `GXVV <geosoft.gxapi.GXVV>`, >= 0
        :type  type:      int
        :type  elements:  int

        :returns:         `GXVV <geosoft.gxapi.GXVV>` Object
        :rtype:           GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** See `create <geosoft.gxapi.GXVV.create>`

        Do not use data type flags: `GS_INT <geosoft.gxapi.GS_INT>` or `GS_REAL <geosoft.gxapi.GS_REAL>`,
        this will result in a respective data type of unsigned byte or
        short for the `GXVV <geosoft.gxapi.GXVV>`.
        """
        ret_val = gxapi_cy.WrapVV._create_ext(GXContext._get_tls_geo(), type, elements)
        return GXVV(ret_val)



    @classmethod
    def create_s(cls, bf):
        """
        Create a `GXVV <geosoft.gxapi.GXVV>`  from serialized source.
        
        :type  bf:  GXBF

        :returns:    `GXVV <geosoft.gxapi.GXVV>` Object
        :rtype:      GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapVV._create_s(GXContext._get_tls_geo(), bf)
        return GXVV(ret_val)






    def diff(self, n):
        """
        Calculate differences.
        
        :param n:   Number of differences
        :type  n:   int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Differences with dummies result in dummies.
        An even number of differences locates data accurately.
        An odd number of differences locates result 1/2 element lower
        in the `GXVV <geosoft.gxapi.GXVV>`.
        """
        self._diff(n)
        




    def divide(self, vv_y, vv_z):
        """
        Divide one `GXVV <geosoft.gxapi.GXVV>` by another: VV_A / VV_B = VV_C
        
        :param vv_y:  `GXVV <geosoft.gxapi.GXVV>` B
        :param vv_z:  `GXVV <geosoft.gxapi.GXVV>` C (returned), C = A / B
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._divide(vv_y, vv_z)
        




    def fid_norm(self, vv2):
        """
        Re-sample a pair of `GXVV <geosoft.gxapi.GXVV>`'s to match each other.
        
        :param vv2:  `GXVV <geosoft.gxapi.GXVV>` to resample
        :type  vv2:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Both `GXVV <geosoft.gxapi.GXVV>`'s will return with the same start
        fid and fid increment.  The smaller start fid
        and fid increment will be used.
        """
        self._fid_norm(vv2)
        




    def fill_int(self, int):
        """
        Fill a `GXVV <geosoft.gxapi.GXVV>` with an int value.
        
        :param int:  Value to fill with
        :type  int:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._fill_int(int)
        




    def fill_double(self, val):
        """
        Fill a `GXVV <geosoft.gxapi.GXVV>` with a real value.
        
        :param val:  Value to fill with
        :type  val:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._fill_double(val)
        




    def fill_string(self, str_val):
        """
        Fill a `GXVV <geosoft.gxapi.GXVV>` with a string value.
        
        :param str_val:  String
        :type  str_val:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._fill_string(str_val.encode())
        




    def count_dummies(self, start, elem):
        """
        Count the number of dummies in a `GXVV <geosoft.gxapi.GXVV>`
        
        :param start:  Starting point in `GXVV <geosoft.gxapi.GXVV>` (0 for all)
        :param elem:   Number of elements to process (-1 for all)
        :type  start:  int
        :type  elem:   int

        :returns:      The count
        :rtype:        int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._count_dummies(start, elem)
        return ret_val




    def find_dum(self, start, end, yn, order):
        """
        Finds the first dummy or non-dummy value in a `GXVV <geosoft.gxapi.GXVV>`
        
        :param start:  Lowest element in `GXVV <geosoft.gxapi.GXVV>` element to search
        :param end:    Highest element in `GXVV <geosoft.gxapi.GXVV>` to search
        :param yn:     0 = find first dummy / 1 = find first non-dummy
        :param order:  0 = use increasing order / 1 = use decreasing order
        :type  start:  int
        :type  end:    int
        :type  yn:     int
        :type  order:  int

        :returns:      The index of the first dummy or non-dummy value.
                       -1 if not found, 0 if the length of the `GXVV <geosoft.gxapi.GXVV>` is 0.
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If a decreasing order search is performed, it will start
        at the highest element specified. (Conversely, an increasing
        order starts at the lowest element specified.)
        """
        ret_val = self._find_dum(start, end, yn, order)
        return ret_val




    def get_fid_expansion(self):
        """
        Gets the Fiducial expansion from a `GXVV <geosoft.gxapi.GXVV>`
        

        :returns:    Number of expanions for this `GXVV <geosoft.gxapi.GXVV>` (see `re_fid_vv <geosoft.gxapi.GXVV.re_fid_vv>`)
        :rtype:      int

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_fid_expansion()
        return ret_val




    def get_int(self, element):
        """
        Get an integer element from a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param element:  Element wanted
        :type  element:  int

        :returns:        Element wanted, or `iDUMMY <geosoft.gxapi.iDUMMY>`
                         if the value is dummy or outside of the range of data.
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_int(element)
        return ret_val




    def get_string(self, element, str_val):
        """
        Get a string element from a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param element:  Element wanted
        :param str_val:  String in which to place element
        :type  element:  int
        :type  str_val:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Returns Element wanted, or blank string
        if the value is dummy or outside of the range of data.

        Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        str_val.value = self._get_string(element, str_val.value.encode())
        




    def index_max(self, max):
        """
        Get the index where the maximum value occurs.
        
        :param max:  Maximum value (`rDUMMY <geosoft.gxapi.rDUMMY>` if all dummies or no data)
        :type  max:  float_ref

        :returns:    Index of the maximum value, `iDUMMY <geosoft.gxapi.iDUMMY>` if no valid data.
        :rtype:      int

        .. versionadded:: 6.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If more than one value has the same maximum value, the index of the
        first is returned.
        """
        ret_val, max.value = self._index_max(max.value)
        return ret_val




    def length(self):
        """
        Returns current `GXVV <geosoft.gxapi.GXVV>` length.
        

        :returns:    # of elements in the `GXVV <geosoft.gxapi.GXVV>`.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._length()
        return ret_val




    def index_insert(self, vv_d, vv_i):
        """
        Insert items into a `GXVV <geosoft.gxapi.GXVV>` using an index `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vv_d:  Data items to insert (must be same type as output data `GXVV <geosoft.gxapi.GXVV>`)
        :param vv_i:  Index `GXVV <geosoft.gxapi.GXVV>` (must be type INT)
        :type  vv_d:  GXVV
        :type  vv_i:  GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The items in the input data `GXVV <geosoft.gxapi.GXVV>` are inserted into
        the output `GXVV <geosoft.gxapi.GXVV>` using the indices in the index `GXVV <geosoft.gxapi.GXVV>`.
        Values not referenced are not altered, so the output
        `GXVV <geosoft.gxapi.GXVV>` should be pre-initialized. The output `GXVV <geosoft.gxapi.GXVV>` length
        will NOT be changed, and index values referencing
        beyond the end of the output `GXVV <geosoft.gxapi.GXVV>` data will return an
        error.

        This function is useful when working with channel data that include
        dummies, but where the dummies must be removed before processing.
        Create and initialize an index (0, 1, 2...) `GXVV <geosoft.gxapi.GXVV>`, using the `init_index <geosoft.gxapi.GXVV.init_index>`
        function, and when you remove
        the dummies, remove the corresponding index values as well.
        After processing, init a `GXVV <geosoft.gxapi.GXVV>` to dummies, then use `index_insert <geosoft.gxapi.GXVV.index_insert>` to
        put the processed values at the correct locations in the data `GXVV <geosoft.gxapi.GXVV>`
        before you write it back to the channel.
        """
        self._index_insert(vv_d, vv_i)
        




    def index_order(self, vv_d):
        """
        Reorder a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vv_d:  `GXVV <geosoft.gxapi.GXVV>` to order
        :type  vv_d:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Given an index `GXVV <geosoft.gxapi.GXVV>` (of type INT), this method reorders a
        `GXVV <geosoft.gxapi.GXVV>`. Please make sure that the index holds valid information.
        """
        self._index_order(vv_d)
        




    def init_index(self, n):
        """
        Initialize an index `GXVV <geosoft.gxapi.GXVV>` to values 0, 1, 2, etc...
        
        :param n:   Final length of `GXVV <geosoft.gxapi.GXVV>` (-1 to use current length).
        :type  n:   int

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Populates a `GXVV <geosoft.gxapi.GXVV>` with the values 0, 1, 2, 3, 4 etc., to be
        used for various indexing functions, such as `index_insert <geosoft.gxapi.GXVV.index_insert>` or
        `index_order <geosoft.gxapi.GXVV.index_order>`.
        """
        self._init_index(n)
        




    def inv_log(self, log_base, log_mode, log_min):
        """
        Inverse of the `log <geosoft.gxapi.GXVV.log>` function.
        
        :param log_base:  :ref:`VV_LOG_BASE`
        :param log_mode:  :ref:`VV_LOGMODE`
        :param log_min:   Minimum value for :ref:`VV_LOG_NEGATIVE`
        :type  log_base:  int
        :type  log_mode:  int
        :type  log_min:   float

        .. versionadded:: 7.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is the inverse function for `log <geosoft.gxapi.GXVV.log>`, with the same inputs.
        """
        self._inv_log(log_base, log_mode, log_min)
        




    def order(self, rep):
        """
        Identifies the data size order of the elements.
        
        :param rep:  Returned: Do any values repeat (0: No, 1: Yes)?
        :type  rep:  int_ref

        :returns:    :ref:`VV_ORDER`
        :rtype:      int

        .. versionadded:: 6.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        ret_val, rep.value = self._order(rep.value)
        return ret_val




    def lines_to_xy(self, vv_x, vv_y):
        """
        Convert a 2D Line segment `GXVV <geosoft.gxapi.GXVV>` into X and Y VVs.
        
        :param vv_x:  Output `GXVV <geosoft.gxapi.GXVV>` with X locations (`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`)
        :param vv_y:  Output `GXVV <geosoft.gxapi.GXVV>` with Y locations (`GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`)
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV

        .. versionadded:: 8.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Some GX functions (such as `GXTIN.get_voronoi_edges <geosoft.gxapi.GXTIN.get_voronoi_edges>`) return
        a special `GXVV <geosoft.gxapi.GXVV>` where each element contains the start and end
        points of lines, (X_1, Y_1) and (X_2, Y_2).
        This GX dumps the individual X and Y values into individual
        X and Y VVs of type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` (REAL). N lines produces 2*N
        X and Y values.
        """
        self._lines_to_xy(vv_x, vv_y)
        




    def lookup_index(self, vvi, vvr):
        """
        Lookup a `GXVV <geosoft.gxapi.GXVV>` from another `GXVV <geosoft.gxapi.GXVV>` using an index `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vvi:  Index `GXVV <geosoft.gxapi.GXVV>` of REAL
        :param vvr:  Result `GXVV <geosoft.gxapi.GXVV>` (same type as Data `GXVV <geosoft.gxapi.GXVV>`)
        :type  vvi:  GXVV
        :type  vvr:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This method assigns index values of 0.0, 1.0, 2.0 etc. to the individual
        values in the input Data `GXVV <geosoft.gxapi.GXVV>`, and uses linear interpolation to calculate the values of
        Result `GXVV <geosoft.gxapi.GXVV>` at the input indices contained in the Index `GXVV <geosoft.gxapi.GXVV>`.

        If the input Data `GXVV <geosoft.gxapi.GXVV>` is string type, then only values at the integral index values
        are returned.

        See also `setup_index <geosoft.gxapi.GXVV.setup_index>` for an example of how this can be implemented.
        """
        self._lookup_index(vvi, vvr)
        




    def make_mem_based(self):
        """
        Make this `GXVV <geosoft.gxapi.GXVV>` use regular instead of virtual memory.
        

        .. versionadded:: 5.1.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function should be called immediately aftter
        `create <geosoft.gxapi.GXVV.create>`.

        Normal VVs are optimised to prevent thrashing, and to
        efficiently support many extremely large VVs, although
        there is a small performance penalty.
        This function is intended for `GXVV <geosoft.gxapi.GXVV>`'s that you know can be
        handled by the operating system virtual memory manager,
        and will be used heavily.  By using a memory based `GXVV <geosoft.gxapi.GXVV>`, you
        can achieve some performance improvements provided your
        application does not cause the memory manager to "thrash".

        External programs that use the GX API may prefer to use
        memory-based `GXVV <geosoft.gxapi.GXVV>`'s because you can get direct access to
        the `GXVV <geosoft.gxapi.GXVV>` through the `GXGEO.get_ptr_vv <geosoft.gxapi.GXGEO.get_ptr_vv>` function (see gx_extern.h).

        .. seealso::

            `GXGEO.get_ptr_vv <geosoft.gxapi.GXGEO.get_ptr_vv>` in gx_extern.h
        """
        self._make_mem_based()
        




    def mask_and(self, vv_y, vv_z):
        """
        Create mask from logical AND of two VVs.
        
        :param vv_y:  `GXVV <geosoft.gxapi.GXVV>` B
        :param vv_z:  `GXVV <geosoft.gxapi.GXVV>` C (returned)
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV

        .. versionadded:: 5.1.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If both values are non-dummies, then result is 1, else dummy.
        """
        self._mask_and(vv_y, vv_z)
        




    def mask_or(self, vv_y, vv_z):
        """
        Create mask from logical OR of two VVs.
        
        :param vv_y:  `GXVV <geosoft.gxapi.GXVV>` B
        :param vv_z:  `GXVV <geosoft.gxapi.GXVV>` C (returned)
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV

        .. versionadded:: 5.1.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If either values is non-dummy, then result is 1, else dummy.
        """
        self._mask_or(vv_y, vv_z)
        




    def mask_str(self, vv_m, str_val):
        """
        Mask one `GXVV <geosoft.gxapi.GXVV>` against another using a string.
        
        :param vv_m:     Mask `GXVV <geosoft.gxapi.GXVV>`
        :param str_val:  String to compare
        :type  vv_m:     GXVV
        :type  str_val:  str

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** All elements in the mask `GXVV <geosoft.gxapi.GXVV>` that are same as string will replace
        the original `GXVV <geosoft.gxapi.GXVV>` with a 1.

        The modified `GXVV <geosoft.gxapi.GXVV>` will always be expanded to the MaskVV size but
        not shortened after this call.  If the mask is longer than the target,
        the target will be lengthenned with dummies before applying the mask.
        """
        self._mask_str(vv_m, str_val.encode())
        




    def multiply(self, vv_y, vv_z):
        """
        Multiply two VVs: VV_A * VV_B = VV_C
        
        :param vv_y:  `GXVV <geosoft.gxapi.GXVV>` B
        :param vv_z:  `GXVV <geosoft.gxapi.GXVV>` C (returned), C = A * B
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._multiply(vv_y, vv_z)
        




    def amplitude_3d(self, v_vx, v_vy, v_vz):
        """
        Calculate the 3D length for XYZ component VVs
        
        :param v_vx:  X component `GXVV <geosoft.gxapi.GXVV>`
        :param v_vy:  Y component `GXVV <geosoft.gxapi.GXVV>`
        :param v_vz:  Z component `GXVV <geosoft.gxapi.GXVV>`
        :type  v_vx:  GXVV
        :type  v_vy:  GXVV
        :type  v_vz:  GXVV

        .. versionadded:: 8.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._amplitude_3d(v_vx, v_vy, v_vz)
        




    def polygon_mask(self, yvv, rvv, pply, dummy):
        """
        Mask a `GXVV <geosoft.gxapi.GXVV>` using XY data and a polygon
        
        :param yvv:    Y `GXVV <geosoft.gxapi.GXVV>`
        :param rvv:    `GXVV <geosoft.gxapi.GXVV>` to be masked
        :param pply:   Polygon Object
        :param dummy:  :ref:`VV_MASK`
        :type  yvv:    GXVV
        :type  rvv:    GXVV
        :type  pply:   GXPLY
        :type  dummy:  int

        .. versionadded:: 5.1.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The VVs has to be the same length
        """
        self._polygon_mask(yvv, rvv, pply, dummy)
        



    @classmethod
    def project(cls, pj, vv_x, vv_y):
        """
        This method projects an X and Y `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vv_x:  X
        :param vv_y:  Y
        :type  pj:    GXPJ
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This function is equivalent to `GXPJ.convert_vv <geosoft.gxapi.GXPJ.convert_vv>`.
        """
        gxapi_cy.WrapVV._project(GXContext._get_tls_geo(), pj, vv_x, vv_y)
        



    @classmethod
    def project_3d(cls, pj, vv_x, vv_y, vv_z):
        """
        This method projects an X,Y,Z `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vv_x:  X
        :param vv_y:  Y
        :param vv_z:  Z
        :type  pj:    GXPJ
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This function is equivalent to `GXPJ.convert_vv3 <geosoft.gxapi.GXPJ.convert_vv3>`.
        """
        gxapi_cy.WrapVV._project_3d(GXContext._get_tls_geo(), pj, vv_x, vv_y, vv_z)
        




    def range_double(self, min, max):
        """
        Get the min. and max. values of a `GXVV <geosoft.gxapi.GXVV>` while ignoring dummies.
        
        :param min:  Minimum value - returned
        :param max:  Maximum value - returned
        :type  min:  float_ref
        :type  max:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Minimum and maximum become `GS_R8DM <geosoft.gxapi.GS_R8DM>` if entire `GXVV <geosoft.gxapi.GXVV>` is dummy.
        """
        min.value, max.value = self._range_double(min.value, max.value)
        




    def re_fid(self, start, incr, length):
        """
        Re-sample a `GXVV <geosoft.gxapi.GXVV>` to a new fid start/icrement
        
        :param start:   New fid start
        :param incr:    New fid increment
        :param length:  New length
        :type  start:   float
        :type  incr:    float
        :type  length:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._re_fid(start, incr, length)
        




    def re_fid_vv(self, vv_m):
        """
        Re-sample a `GXVV <geosoft.gxapi.GXVV>` to match another `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vv_m:  `GXVV <geosoft.gxapi.GXVV>` model (fid increment and start)
        :type  vv_m:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This method will honor the `GXVV <geosoft.gxapi.GXVV>` FID Expansion and will expand/contract
        `GXVV <geosoft.gxapi.GXVV>`'s based on this flag if it is used.
        """
        self._re_fid_vv(vv_m)
        




    def re_sample(self, c_start, c_incr, n_start, n_incr, length, unused):
        """
        Resamples a `GXVV <geosoft.gxapi.GXVV>` from one fid/incr to another fid/incr.
        
        :param c_start:  Current start fid
        :param c_incr:   Current increment
        :param n_start:  New fid start
        :param n_incr:   New fid increment
        :param length:   New length
        :param unused:   This parameter is not used
        :type  c_start:  float
        :type  c_incr:   float
        :type  n_start:  float
        :type  n_incr:   float
        :type  length:   int
        :type  unused:   int

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._re_sample(c_start, c_incr, n_start, n_incr, length, unused)
        




    def get_fid_incr(self):
        """
        Gets the Fiducial increment from a `GXVV <geosoft.gxapi.GXVV>`
        

        :returns:    Fiducial increment of the `GXVV <geosoft.gxapi.GXVV>`.
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_fid_incr()
        return ret_val




    def get_fid_start(self):
        """
        Gets the Fiducial start from a `GXVV <geosoft.gxapi.GXVV>`
        

        :returns:    Fiducial start of the `GXVV <geosoft.gxapi.GXVV>`.
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = self._get_fid_start()
        return ret_val




    def get_double(self, element):
        """
        Get a real element from a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param element:  Element wanted
        :type  element:  int

        :returns:        Element wanted, or `rDUMMY <geosoft.gxapi.rDUMMY>`
                         if the value is dummy or outside of the range of data.
        :rtype:          float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Type conversions are performed if necessary.  Dummy values
        are converted to "*" string.
        """
        ret_val = self._get_double(element)
        return ret_val




    def sum(self):
        """
        Calculate the sum of the values in a `GXVV <geosoft.gxapi.GXVV>`.
        

        :returns:    The sum of the elements.
        :rtype:      float

        .. versionadded:: 7.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Dummy value is treated as Zero(0)
        """
        ret_val = self._sum()
        return ret_val




    def weighted_mean(self, vv_weights):
        """
        Calculate the weighted average of the values.
        
        :param vv_weights:   `GXVV <geosoft.gxapi.GXVV>` of weights
        :type  vv_weights:   GXVV

        :returns:            The weighted average of the values.
        :rtype:              float

        .. versionadded:: 7.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Dummy values are ignored.
        """
        ret_val = self._weighted_mean(vv_weights)
        return ret_val




    def set_fid_expansion(self, expand):
        """
        Sets the Fiducial expansion from a `GXVV <geosoft.gxapi.GXVV>`
        
        :param expand:  Expansion setting (1 or greater)
        :type  expand:  int

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_fid_expansion(expand)
        




    def set_fid_incr(self, incr):
        """
        Sets the Fiducial increment of a `GXVV <geosoft.gxapi.GXVV>`
        
        :param incr:  New increment
        :type  incr:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_fid_incr(incr)
        




    def set_fid_start(self, start):
        """
        Sets the Fiducial start of a `GXVV <geosoft.gxapi.GXVV>`
        
        :param start:  New start
        :type  start:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._set_fid_start(start)
        




    def set_int(self, element, value):
        """
        Set an integer element in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param element:  Element to set
        :param value:    Value to set
        :type  element:  int
        :type  value:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Element being set cannot be < 0.
        If the element is > current `GXVV <geosoft.gxapi.GXVV>` length, the `GXVV <geosoft.gxapi.GXVV>` length is
        increased.
        It is good practice to set the length ahead of time to the
        expected maximum value, as some `GXVV <geosoft.gxapi.GXVV>` processes rely on the
        current maximum length of the `GXVV <geosoft.gxapi.GXVV>` when you pass it in as an
        argument, and unexpected results may occur if the length is
        not what you expect it to be because of dynamic allocation at
        an earlier time.
        """
        self._set_int(element, value)
        




    def set_int_n(self, start, n, value):
        """
        Set N integer elements in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param start:  Start element (>= 0)
        :param n:      # elements to set (-1 sets all elements to end)
        :param value:  Value to set
        :type  start:  int
        :type  n:      int
        :type  value:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Element being set cannot be < 0.
        If the element is > current `GXVV <geosoft.gxapi.GXVV>` length, the `GXVV <geosoft.gxapi.GXVV>` length is
        increased.
        """
        self._set_int_n(start, n, value)
        




    def set_len(self, size):
        """
        Set the length of a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param size:  New length (number of elements)
        :type  size:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If increasing the `GXVV <geosoft.gxapi.GXVV>` size, new elements are set to dummies.

        It is good practice to set the length ahead of time to the
        expected maximum value, as some `GXVV <geosoft.gxapi.GXVV>` processes rely on the
        current maximum length of the `GXVV <geosoft.gxapi.GXVV>` when you pass it in as an
        argument, and unexpected results may occur if the length is
        not what you expect it to be because of dynamic allocation at
        an earlier time.
        """
        self._set_len(size)
        




    def set_double(self, element, value):
        """
        Set a real element in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param element:  Element to set
        :param value:    Value to set
        :type  element:  int
        :type  value:    float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Element being set cannot be < 0.
        If the element is > current `GXVV <geosoft.gxapi.GXVV>` length, the `GXVV <geosoft.gxapi.GXVV>` length is
        increased.
        It is good practice to set the length ahead of time to the
        expected maximum value, as some `GXVV <geosoft.gxapi.GXVV>` processes rely on the
        current maximum length of the `GXVV <geosoft.gxapi.GXVV>` when you pass it in as an
        argument, and unexpected results may occur if the length is
        not what you expect it to be because of dynamic allocation at
        an earlier time.
        """
        self._set_double(element, value)
        




    def set_double_n(self, start, n, value):
        """
        Set N real elements in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param start:  Start element (>= 0)
        :param n:      # elements to set (-1 sets all elements to end)
        :param value:  Value to set
        :type  start:  int
        :type  n:      int
        :type  value:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Element being set cannot be < 0.
        If the element is > current `GXVV <geosoft.gxapi.GXVV>` length, the `GXVV <geosoft.gxapi.GXVV>` length is
        increased.
        """
        self._set_double_n(start, n, value)
        




    def set_string(self, element, value):
        """
        Set a string element in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param element:  Element to set
        :param value:    String to set
        :type  element:  int
        :type  value:    str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Element being set cannot be < 0.
        If the element is > current `GXVV <geosoft.gxapi.GXVV>` length, the `GXVV <geosoft.gxapi.GXVV>` length is
        increased.
        It is good practice to set the length ahead of time to the
        expected maximum value, as some `GXVV <geosoft.gxapi.GXVV>` processes rely on the
        current maximum length of the `GXVV <geosoft.gxapi.GXVV>` when you pass it in as an
        argument, and unexpected results may occur if the length is
        not what you expect it to be because of dynamic allocation at
        an earlier time.
        """
        self._set_string(element, value.encode())
        




    def set_string_n(self, start, n, value):
        """
        Set N string elements in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param start:  Start element (>= 0)
        :param n:      # elements to set (-1 sets all elements to end)
        :param value:  String to set
        :type  start:  int
        :type  n:      int
        :type  value:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Element being set cannot be < 0.
        If the element is > current `GXVV <geosoft.gxapi.GXVV>` length, the `GXVV <geosoft.gxapi.GXVV>` length is
        increased.
        """
        self._set_string_n(start, n, value.encode())
        




    def setup_index(self, vvq, vvi, mode, space):
        """
        Setup an index `GXVV <geosoft.gxapi.GXVV>` from VV1 to VV2.
        
        :param vvq:    Query `GXVV <geosoft.gxapi.GXVV>` (same type as Data `GXVV <geosoft.gxapi.GXVV>`)
        :param vvi:    `GXVV <geosoft.gxapi.GXVV>` index `GXVV <geosoft.gxapi.GXVV>` of type REAL
        :param mode:   :ref:`VV_LOOKUP`
        :param space:  Spacing for some modes
        :type  vvq:    GXVV
        :type  vvi:    GXVV
        :type  mode:   int
        :type  space:  float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The input reference `GXVV <geosoft.gxapi.GXVV>` must be in ascending numerical order.
        If your reference data is NOT ordered, then use the `sort_index1 <geosoft.gxapi.GXVV.sort_index1>` 
        function to create an order index, then sort both the reference and data VVs 
        using this index `GXVV <geosoft.gxapi.GXVV>` before you call `setup_index <geosoft.gxapi.GXVV.setup_index>`.

        Example: You have a reference data set taken at specific times, ``hVVt``, ``hVVy``
        and you want to calculate/estimate/interpolate the values ``hVVy2`` at a second set
        of times ``hVVt2``

        Step 1: Create an index, ``hVVi``, type `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>`, and call `setup_index <geosoft.gxapi.GXVV.setup_index>`.

        with: ``hVVt2, hVVi, VV_LOOKUP_XXX, rSpacing``

        Internally, this assigns index values of 0.0, 1.0, 2.0 etc. to the individual
        values in ``hVVt``, then, depending on the lookup method chosen, assigns
        fractional index values to the input values in ``hVVt2``.

        Step 2: To determine what the lookup values ``hVVy2`` should be at times ``hVVt2``,
        call the `lookup_index <geosoft.gxapi.GXVV.lookup_index>` function for hVVy with ``hVVi, hVVy2``

        Internally, this assigns index values of 0.0, 1.0, 2.0 etc. to the individual
        values in ``hVVy``, and uses linear interpolation to calculate the values of
        ``hVVy2`` at the input indices contained in ``hVVi``.
        """
        self._setup_index(vvq, vvi, mode, space)
        




    def sort(self, order):
        """
        Sort a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param order:  :ref:`VV_SORT`
        :type  order:  int

        .. versionadded:: 5.1.5

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._sort(order)
        




    def sort_index(self, ivv):
        """
        Sort index `GXVV <geosoft.gxapi.GXVV>` based on a data `GXVV <geosoft.gxapi.GXVV>`.
        
        :param ivv:  Index `GXVV <geosoft.gxapi.GXVV>` of type INT
        :type  ivv:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Create an Index `GXVV <geosoft.gxapi.GXVV>` (of type `GS_LONG <geosoft.gxapi.GS_LONG>`) based on a data `GXVV <geosoft.gxapi.GXVV>`.
        This index vv can then be used by the IndexOrder method
        to order a group of `GXVV <geosoft.gxapi.GXVV>`'s.
        """
        self._sort_index(ivv)
        




    def sort_index1(self, ivv, ord1):
        """
        Sort index `GXVV <geosoft.gxapi.GXVV>` based on 1 data `GXVV <geosoft.gxapi.GXVV>` - set orders.
        
        :param ivv:   Index `GXVV <geosoft.gxapi.GXVV>` of type INT
        :param ord1:  :ref:`VV_SORT`
        :type  ivv:   GXVV
        :type  ord1:  int

        .. versionadded:: 5.0.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Create an Index `GXVV <geosoft.gxapi.GXVV>` (of type `GS_LONG <geosoft.gxapi.GS_LONG>`) based on a data `GXVV <geosoft.gxapi.GXVV>`.
        This index vv can then be used by the IndexOrder method
        to order a group of `GXVV <geosoft.gxapi.GXVV>`'s. The individual VVs may be ordered
        in ascending or descending order.
        If the primary `GXVV <geosoft.gxapi.GXVV>` values of two indices are the same, then
        the secondary `GXVV <geosoft.gxapi.GXVV>` values are compared. If the secondary values
        are the same, the ternary values are compared, etc.
        """
        self._sort_index1(ivv, ord1)
        




    def sort_index2(self, d2_vv, ivv, ord1, ord2):
        """
        Sort index `GXVV <geosoft.gxapi.GXVV>` based on 2 data VVs - set orders.
        
        :param d2_vv:  Secondary Data `GXVV <geosoft.gxapi.GXVV>`
        :param ivv:    Index `GXVV <geosoft.gxapi.GXVV>` of type INT
        :param ord1:   Primary Sort order :ref:`VV_SORT`
        :param ord2:   Secondary Sort order :ref:`VV_SORT`
        :type  d2_vv:  GXVV
        :type  ivv:    GXVV
        :type  ord1:   int
        :type  ord2:   int

        .. versionadded:: 5.0.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Create an Index `GXVV <geosoft.gxapi.GXVV>` (of type `GS_LONG <geosoft.gxapi.GS_LONG>`) based on a data `GXVV <geosoft.gxapi.GXVV>`.
        This index vv can then be used by the IndexOrder method
        to order a group of `GXVV <geosoft.gxapi.GXVV>`'s. The individual VVs may be ordered
        in ascending or descending order.
        If the primary `GXVV <geosoft.gxapi.GXVV>` values of two indices are the same, then
        the secondary `GXVV <geosoft.gxapi.GXVV>` values are compared. If the secondary values
        are the same, the ternary values are compared, etc
        """
        self._sort_index2(d2_vv, ivv, ord1, ord2)
        




    def sort_index3(self, d2_vv, d3_vv, ivv, ord1, ord2, ord3):
        """
        Sort index `GXVV <geosoft.gxapi.GXVV>` based on 3 data VVs - set orders.
        
        :param d2_vv:  Secondary Data `GXVV <geosoft.gxapi.GXVV>`
        :param d3_vv:  Ternary Data `GXVV <geosoft.gxapi.GXVV>`
        :param ivv:    Index `GXVV <geosoft.gxapi.GXVV>` of type INT
        :param ord1:   Primary Sort order :ref:`VV_SORT`
        :param ord2:   Secondary sort order :ref:`VV_SORT`
        :param ord3:   Third Sort order :ref:`VV_SORT`
        :type  d2_vv:  GXVV
        :type  d3_vv:  GXVV
        :type  ivv:    GXVV
        :type  ord1:   int
        :type  ord2:   int
        :type  ord3:   int

        .. versionadded:: 5.0.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Create an Index `GXVV <geosoft.gxapi.GXVV>` (of type `GS_LONG <geosoft.gxapi.GS_LONG>`) based on a data `GXVV <geosoft.gxapi.GXVV>`.
        This index vv can then be used by the IndexOrder method
        to order a group of `GXVV <geosoft.gxapi.GXVV>`'s. The individual VVs may be ordered
        in ascending or descending order.
        If the primary `GXVV <geosoft.gxapi.GXVV>` values of two indices are the same, then
        the secondary `GXVV <geosoft.gxapi.GXVV>` values are compared. If the secondary values
        are the same, the third values are compared, etc
        """
        self._sort_index3(d2_vv, d3_vv, ivv, ord1, ord2, ord3)
        




    def sort_index4(self, d2_vv, d3_vv, d4_vv, ivv, ord1, ord2, ord3, ord4):
        """
        Sort index `GXVV <geosoft.gxapi.GXVV>` based on 4 data VVs - set orders.
        
        :param d2_vv:  Secondary Data `GXVV <geosoft.gxapi.GXVV>`
        :param d3_vv:  Ternary Data `GXVV <geosoft.gxapi.GXVV>`
        :param d4_vv:  Quaternary Data `GXVV <geosoft.gxapi.GXVV>`
        :param ivv:    Index `GXVV <geosoft.gxapi.GXVV>` of type INT
        :param ord1:   Primary Ssort order :ref:`VV_SORT`
        :param ord2:   Secondary Sort order :ref:`VV_SORT`
        :param ord3:   Third Sort order :ref:`VV_SORT`
        :param ord4:   Fourth Sort order :ref:`VV_SORT`
        :type  d2_vv:  GXVV
        :type  d3_vv:  GXVV
        :type  d4_vv:  GXVV
        :type  ivv:    GXVV
        :type  ord1:   int
        :type  ord2:   int
        :type  ord3:   int
        :type  ord4:   int

        .. versionadded:: 5.0.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Create an Index `GXVV <geosoft.gxapi.GXVV>` (of type `GS_LONG <geosoft.gxapi.GS_LONG>`) based on a data `GXVV <geosoft.gxapi.GXVV>`.
        This index vv can then be used by the IndexOrder method
        to order a group of `GXVV <geosoft.gxapi.GXVV>`'s. The individual VVs may be ordered
        in ascending or descending order.
        If the primary `GXVV <geosoft.gxapi.GXVV>` values of two indices are the same, then
        the secondary `GXVV <geosoft.gxapi.GXVV>` values are compared. If the secondary values
        are the same, the third values are compared, etc
        """
        self._sort_index4(d2_vv, d3_vv, d4_vv, ivv, ord1, ord2, ord3, ord4)
        



    @classmethod
    def statistics(cls, st, vv):
        """
        Add a `GXVV <geosoft.gxapi.GXVV>` to a `GXST <geosoft.gxapi.GXST>`.
        
        :param st:  `GXST <geosoft.gxapi.GXST>` Handle
        :param vv:  `GXVV <geosoft.gxapi.GXVV>` to add to `GXST <geosoft.gxapi.GXST>`
        :type  st:  GXST
        :type  vv:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        gxapi_cy.WrapVV._statistics(GXContext._get_tls_geo(), st, vv)
        




    def subtract(self, vv_y, vv_z):
        """
        Subtract one `GXVV <geosoft.gxapi.GXVV>` from another: VV_A - VV_B = VV_C
        
        :param vv_y:  `GXVV <geosoft.gxapi.GXVV>` B
        :param vv_z:  `GXVV <geosoft.gxapi.GXVV>` C (returned), C = A - B
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._subtract(vv_y, vv_z)
        




    def swap(self):
        """
        Swaps the bytes of the SHORT, USHORT, LONG, FLOAT and DOUBLE vv's.
        Other vv's are not affected by this method. This is used
        primarily with changing the order of bytes for other machine
        created data.
        

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._swap()
        




    def window(self, min, max, mode):
        """
        Limit the elements of a vv to a range.
        
        :param min:   Min Val
        :param max:   Max Val
        :param mode:  :ref:`VV_WINDOW`
        :type  min:   float
        :type  max:   float
        :type  mode:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._window(min, max, mode)
        




    def write_xml(self, file, format, decimal):
        """
        Write the `GXVV <geosoft.gxapi.GXVV>` data as an XML object with bytes and formating.
        
        :param file:     XML file to create
        :param format:   Format
        :param decimal:  Significant digits/decimals
        :type  file:     str
        :type  format:   int
        :type  decimal:  int

        .. versionadded:: 8.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        self._write_xml(file.encode(), format, decimal)
        





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
        self._set_data(start, num_elements, np_array.data.tobytes(), gs_type)
    
    def get_data_array(self, start: int, num_elements: int, gs_type: int):
        return gxapi_cy_extend.GXMemMethods.get_data_array_vv(GXContext._internal_p(), self._internal_handle(), start, num_elements, gs_type)
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer