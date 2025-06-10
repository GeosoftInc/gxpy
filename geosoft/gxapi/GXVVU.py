#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.

### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
import warnings
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXVVU(gxapi_cy.WrapVVU):
    """
    GXVVU class.

    These methods are not a class. Utility methods perform
    various operations on `GXVV <geosoft.gxapi.GXVV>` objects, including pruning,
    splining, clipping and filtering.
    """

    def __init__(self, handle=0):
        super(GXVVU, self).__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVVU <geosoft.gxapi.GXVVU>`
        
        :returns: A null `GXVVU <geosoft.gxapi.GXVVU>`
        :rtype:   GXVVU
        """
        return GXVVU()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def average_repeat(cls, ref_vv, dat_vv):
        """
        
        Average repeat values.
        
        :param ref_vv:  Reference `GXVV <geosoft.gxapi.GXVV>`
        :param dat_vv:  Data `GXVV <geosoft.gxapi.GXVV>` to average
        :type  ref_vv:  GXVV
        :type  dat_vv:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Repeated values in the reference `GXVV <geosoft.gxapi.GXVV>` will be averaged
        in the data `GXVV <geosoft.gxapi.GXVV>`.  The first value in the data `GXVV <geosoft.gxapi.GXVV>` will be set to the
        average and subsequent data `GXVV <geosoft.gxapi.GXVV>` values will be dummied out.
        Data is processed only to the minimum length of the
        input `GXVV <geosoft.gxapi.GXVV>` lengths.

        .. seealso::

            `remove_dummy <geosoft.gxapi.GXVVU.remove_dummy>`
        """
        
        gxapi_cy.WrapVVU._average_repeat(GXContext._get_tls_geo(), ref_vv, dat_vv)
        



    @classmethod
    def average_repeat_ex(cls, ref_vv, dat_vv, mode):
        """
        
        Average repeat values.
        
        :param ref_vv:  Reference `GXVV <geosoft.gxapi.GXVV>`
        :param dat_vv:  Data `GXVV <geosoft.gxapi.GXVV>` to average
        :param mode:    :ref:`VVU_MODE`
        :type  ref_vv:  GXVV
        :type  dat_vv:  GXVV
        :type  mode:    int

        .. versionadded:: 8.0.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Repeated values in the reference `GXVV <geosoft.gxapi.GXVV>` will be set to the mean, median, minimum or maximum value
        in the data `GXVV <geosoft.gxapi.GXVV>`.  For minimum and maximum, the index in the data `GXVV <geosoft.gxapi.GXVV>` containing the minimum or maximum value
        is retained, and the other repeated values are dummied out. For mean and median, the first value in the 
        data `GXVV <geosoft.gxapi.GXVV>` will be reset and subsequent data `GXVV <geosoft.gxapi.GXVV>` values will be dummied out.
        Data is processed only to the minimum length of the
        input `GXVV <geosoft.gxapi.GXVV>` lengths.

        .. seealso::

            `remove_dummy <geosoft.gxapi.GXVVU.remove_dummy>`
        """
        
        gxapi_cy.WrapVVU._average_repeat_ex(GXContext._get_tls_geo(), ref_vv, dat_vv, mode)
        



    @classmethod
    def average_repeat2(cls, ref_vv1, ref_vv2, dat_vv):
        """
        
        Average repeat values based on 2 reference channels.
        
        :param ref_vv1:  Reference `GXVV <geosoft.gxapi.GXVV>`
        :param ref_vv2:  Reference `GXVV <geosoft.gxapi.GXVV>`
        :param dat_vv:   Data `GXVV <geosoft.gxapi.GXVV>` to average
        :type  ref_vv1:  GXVV
        :type  ref_vv2:  GXVV
        :type  dat_vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Repeated values in the reference `GXVV <geosoft.gxapi.GXVV>` will be averaged
        in the data `GXVV <geosoft.gxapi.GXVV>`.  The first value in the data `GXVV <geosoft.gxapi.GXVV>` will be set to the
        average and subsequent data `GXVV <geosoft.gxapi.GXVV>` values will be dummied out.
        Data is processed only to the minimum length of the
        input `GXVV <geosoft.gxapi.GXVV>` lengths.
        Both the reference `GXVV <geosoft.gxapi.GXVV>` values must repeat for the averaging
        to occur. This version is useful for averaging on repeated
        (X,Y) locations.

        .. seealso::

            RemoveDummy_VV
        """
        
        gxapi_cy.WrapVVU._average_repeat2(GXContext._get_tls_geo(), ref_vv1, ref_vv2, dat_vv)
        



    @classmethod
    def average_repeat2_ex(cls, ref_vv1, ref_vv2, dat_vv, mode):
        """
        
        Average repeat values based on 2 reference channels.
        
        :param ref_vv1:  Reference `GXVV <geosoft.gxapi.GXVV>`
        :param ref_vv2:  Reference `GXVV <geosoft.gxapi.GXVV>`
        :param dat_vv:   Data `GXVV <geosoft.gxapi.GXVV>` to average
        :param mode:     :ref:`VVU_MODE`
        :type  ref_vv1:  GXVV
        :type  ref_vv2:  GXVV
        :type  dat_vv:   GXVV
        :type  mode:     int

        .. versionadded:: 8.0.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Repeated values in the reference `GXVV <geosoft.gxapi.GXVV>` will be set to the mean, median, minimum or maximum value
        in the data `GXVV <geosoft.gxapi.GXVV>`.  The first value in the data `GXVV <geosoft.gxapi.GXVV>` will be reset and subsequent data `GXVV <geosoft.gxapi.GXVV>` values will be dummied out.
        Data is processed only to the minimum length of the
        input `GXVV <geosoft.gxapi.GXVV>` lengths.
        Both the reference `GXVV <geosoft.gxapi.GXVV>` values must repeat for the averaging
        to occur. This version is useful for averaging on repeated
        (X,Y) locations.

        .. seealso::

            RemoveDummy_VV
        """
        
        gxapi_cy.WrapVVU._average_repeat2_ex(GXContext._get_tls_geo(), ref_vv1, ref_vv2, dat_vv, mode)
        



    @classmethod
    def binary_search(cls, vv, val, l_min, l_max):
        """
        
        Search  numeric value in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param val:    Value to search for.
        :param l_min:  Minimum Location
        :param l_max:  Maximum Location
        :type  vv:     GXVV
        :type  val:    float
        :type  l_min:  int_ref
        :type  l_max:  int_ref

        .. versionadded:: 7.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXVV <geosoft.gxapi.GXVV>` should be sorted.Search comparison is made on double
        comparison of the data.
        """
        
        l_min.value, l_max.value = gxapi_cy.WrapVVU._binary_search(GXContext._get_tls_geo(), vv, val, l_min.value, l_max.value)
        



    @classmethod
    def box_cox(cls, vv, lm):
        """
        
        Run Box-Cox (lambda) Transformation on `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vv:  [i/o] `GXVV <geosoft.gxapi.GXVV>`
        :param lm:  [i] Lambda Value
        :type  vv:  GXVV
        :type  lm:  float

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        gxapi_cy.WrapVVU._box_cox(GXContext._get_tls_geo(), vv, lm)
        



    @classmethod
    def bp_filt(cls, vv_i, vv_o, pr_sw, pr_lw, flen):
        """
        
        Band-pass filter to the specified.
        
        :param vv_i:   Input `GXVV <geosoft.gxapi.GXVV>`
        :param vv_o:   Filtered `GXVV <geosoft.gxapi.GXVV>`
        :param pr_sw:  Short wavelength cutoff, 0 for highpass
        :param pr_lw:  Long wavelength cutoff, 0 for lowpass
        :param flen:   Filter Length, 0 for default length
        :type  vv_i:   GXVV
        :type  vv_o:   GXVV
        :type  pr_sw:  float
        :type  pr_lw:  float
        :type  flen:   int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If the short and long wavelengths are <= 0, the input channel
        is simply copied to the output channel without filtering.

        The wavelengths are in fiducials.
        """
        
        gxapi_cy.WrapVVU._bp_filt(GXContext._get_tls_geo(), vv_i, vv_o, pr_sw, pr_lw, flen)
        



    @classmethod
    def clip(cls, vv, min, max, clip):
        """
        
        Clip a `GXVV <geosoft.gxapi.GXVV>` to a range.
        
        :param vv:    `GXVV <geosoft.gxapi.GXVV>` to clip
        :param min:   Minimum value, `rDUMMY <geosoft.gxapi.rDUMMY>` for no minimum clip
        :param max:   Maximum value, `rDUMMY <geosoft.gxapi.rDUMMY>` for no maximum clip
        :param clip:  :ref:`VVU_CLIP`
        :type  vv:    GXVV
        :type  min:   float
        :type  max:   float
        :type  clip:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        gxapi_cy.WrapVVU._clip(GXContext._get_tls_geo(), vv, min, max, clip)
        



    @classmethod
    def clip_to_detect_limit(cls, vv, det_limit, conv):
        """
        
        Apply detection limit clipping of data.
        
        :param vv:         Input data vv (altered).
        :param det_limit:  Detection limit
        :param conv:       Auto-convert negatives?
        :type  vv:         GXVV
        :type  det_limit:  float
        :type  conv:       int

        .. versionadded:: 5.1.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Flow:

        1. If auto-converting negatives, then all negative values
            are replaced by -0.5*value, and detection limit is ignored.

        2. If not auto-converting negatives, and the detection limit is not
           `rDUMMY <geosoft.gxapi.rDUMMY>`, then values less than the detection limit are converted to
           one-half the detection limit.

        This function is identical to `GXCHIMERA.clip_to_detect_limit <geosoft.gxapi.GXCHIMERA.clip_to_detect_limit>`.
        """
        
        gxapi_cy.WrapVVU._clip_to_detect_limit(GXContext._get_tls_geo(), vv, det_limit, conv)
        



    @classmethod
    def cond_depth_tem(cls, resp_vv, time_vv, cond_vv, depth_vv, current, flag, min_xvv, min_yvv, max_xvv, max_yvv, t_moment, r_moment, array):
        """
        
        .. deprecated:: None None 
        Calculate TEM apparent conductivity and depth
        
        :param resp_vv:   Response channel (microvolts)
        :param time_vv:   Time channel (milliseconds)
        :param cond_vv:   Conductivity channel (siemen/m)
        :param depth_vv:  Depth (m)
        :param current:   Transmitter current
        :param flag:      Flag  Transmitter defined by moment (0) or by 4 VVs (1) below
        :param min_xvv:   Minimum X to define transmitter loop layout (moment)
        :param min_yvv:   Minimum Y to define transmitter loop layout (moment)
        :param max_xvv:   Maximum X to define transmitter loop layout (moment)
        :param max_yvv:   Maximum Y to define transmitter loop layout (moment)
        :param t_moment:  Transmitter moment (square meters), dummy if the above flag is 1
        :param r_moment:  Receiver moment (square meters)
        :param array:     :ref:`TEM_ARRAY`
        :type  resp_vv:   GXVV
        :type  time_vv:   GXVV
        :type  cond_vv:   GXVV
        :type  depth_vv:  GXVV
        :type  current:   float
        :type  flag:      int
        :type  min_xvv:   GXVV
        :type  min_yvv:   GXVV
        :type  max_xvv:   GXVV
        :type  max_yvv:   GXVV
        :type  t_moment:  float
        :type  r_moment:  float
        :type  array:     int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        warnings.warn("""Deprecated since unknown, """, )
        gxapi_cy.WrapVVU._cond_depth_tem(GXContext._get_tls_geo(), resp_vv, time_vv, cond_vv, depth_vv, current, flag, min_xvv, min_yvv, max_xvv, max_yvv, t_moment, r_moment, array)
        



    @classmethod
    def decimate(cls, vv, decimate):
        """
        
        Decimate a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param decimate:  Decimation factor (must be > 0)
        :type  vv:        GXVV
        :type  decimate:  int

        .. versionadded:: 6.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** For a decimation factor N, will remove all values except
        those with indices equal to MN, where M is an integer.
        """
        
        gxapi_cy.WrapVVU._decimate(GXContext._get_tls_geo(), vv, decimate)
        



    @classmethod
    def deviation(cls, vv_x, vv_y, vv_d, x1, y1, x2, y2, line):
        """
        
        Calculate distance of point locations to a straight line
        
        :param vv_x:  X `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:  Y `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param vv_d:  Output deviation `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param x1:    X of 1st point to define straight line
        :param y1:    Y of 1st point to define straight line
        :param x2:    X of 2nd point or line azimuth in degrees (North is 0 degree)
        :param y2:    Y of 2nd point or `GS_R8DM <geosoft.gxapi.GS_R8DM>` if line azimuth is defined
        :param line:  :ref:`VVU_LINE`
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_d:  GXVV
        :type  x1:    float
        :type  y1:    float
        :type  x2:    float
        :type  y2:    float
        :type  line:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        gxapi_cy.WrapVVU._deviation(GXContext._get_tls_geo(), vv_x, vv_y, vv_d, x1, y1, x2, y2, line)
        



    @classmethod
    def distance(cls, vv_x, vv_y, vv_d, x_fid_start, x_fid_incr, y_fid_start, y_fid_incr):
        """
        
        Create a cumulative distance `GXVV <geosoft.gxapi.GXVV>`
        
        :param vv_x:         X `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:         Y `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param vv_d:         Output distance `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param x_fid_start:  X `GXVV <geosoft.gxapi.GXVV>` fid start
        :param x_fid_incr:   X `GXVV <geosoft.gxapi.GXVV>` fid incr
        :param y_fid_start:  Y `GXVV <geosoft.gxapi.GXVV>` fid start
        :param y_fid_incr:   Y `GXVV <geosoft.gxapi.GXVV>` fid incr
        :type  vv_x:         GXVV
        :type  vv_y:         GXVV
        :type  vv_d:         GXVV
        :type  x_fid_start:  float
        :type  x_fid_incr:   float
        :type  y_fid_start:  float
        :type  y_fid_incr:   float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        gxapi_cy.WrapVVU._distance(GXContext._get_tls_geo(), vv_x, vv_y, vv_d, x_fid_start, x_fid_incr, y_fid_start, y_fid_incr)
        



    @classmethod
    def distance_link_non_dummies(cls, vv_x, vv_y, vv_d, x_fid_start, x_fid_incr, y_fid_start, y_fid_incr):
        """
        
        Create distance linking non-dummies `GXVV <geosoft.gxapi.GXVV>`
        
        :param vv_x:         X `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:         Y `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param vv_d:         Output distance `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param x_fid_start:  X `GXVV <geosoft.gxapi.GXVV>` fid start
        :param x_fid_incr:   X `GXVV <geosoft.gxapi.GXVV>` fid incr
        :param y_fid_start:  Y `GXVV <geosoft.gxapi.GXVV>` fid start
        :param y_fid_incr:   Y `GXVV <geosoft.gxapi.GXVV>` fid incr
        :type  vv_x:         GXVV
        :type  vv_y:         GXVV
        :type  vv_d:         GXVV
        :type  x_fid_start:  float
        :type  x_fid_incr:   float
        :type  y_fid_start:  float
        :type  y_fid_incr:   float

        .. versionadded:: 2022.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        gxapi_cy.WrapVVU._distance_link_non_dummies(GXContext._get_tls_geo(), vv_x, vv_y, vv_d, x_fid_start, x_fid_incr, y_fid_start, y_fid_incr)
        



    @classmethod
    def distance_non_cumulative(cls, vv_x, vv_y, vv_d, x_fid_start, x_fid_incr, y_fid_start, y_fid_incr):
        """
        
        Create a non cumulative distance `GXVV <geosoft.gxapi.GXVV>` i.e each
        distance element is the distance of the corresponding
        (X,Y) element and the previous element.
        
        :param vv_x:         X `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:         Y `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param vv_d:         Output distance `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param x_fid_start:  X `GXVV <geosoft.gxapi.GXVV>` fid start
        :param x_fid_incr:   X `GXVV <geosoft.gxapi.GXVV>` fid incr
        :param y_fid_start:  Y `GXVV <geosoft.gxapi.GXVV>` fid start
        :param y_fid_incr:   Y `GXVV <geosoft.gxapi.GXVV>` fid incr
        :type  vv_x:         GXVV
        :type  vv_y:         GXVV
        :type  vv_d:         GXVV
        :type  x_fid_start:  float
        :type  x_fid_incr:   float
        :type  y_fid_start:  float
        :type  y_fid_incr:   float

        .. versionadded:: 7.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The fist distace element is `rDUMMY <geosoft.gxapi.rDUMMY>`.
        """
        
        gxapi_cy.WrapVVU._distance_non_cumulative(GXContext._get_tls_geo(), vv_x, vv_y, vv_d, x_fid_start, x_fid_incr, y_fid_start, y_fid_incr)
        



    @classmethod
    def distance_3d(cls, vv_x, vv_y, vv_z, start_distance, vv_d):
        """
        
        Create a cumulative distance `GXVV <geosoft.gxapi.GXVV>` from X, Y and Z VVs
        
        :param vv_x:            X `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:            Y `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param vv_z:            Z `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param start_distance:  Distance at first location
        :param vv_d:            Output distance `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :type  vv_x:            GXVV
        :type  vv_y:            GXVV
        :type  vv_z:            GXVV
        :type  start_distance:  float
        :type  vv_d:            GXVV

        .. versionadded:: 8.0.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The output `GXVV <geosoft.gxapi.GXVV>` is the length of the shortest X,Y or Z input `GXVV <geosoft.gxapi.GXVV>`.
        Any values with dummies are ignored - the distance at that
        point is equal to the distance at the previous valid point.
        The returned `GXVV <geosoft.gxapi.GXVV>` is the cumulative straight-line distance
        between the points. No re-sampling is performed.
        VVs of any type are supported.
        """
        
        gxapi_cy.WrapVVU._distance_3d(GXContext._get_tls_geo(), vv_x, vv_y, vv_z, start_distance, vv_d)
        



    @classmethod
    def find_gaps_3d(cls, vv_x, vv_y, vv_z, gap, vv_g):
        """
        
        Return indices of locations separated from previous locations by more than the input gap distance.
        
        :param vv_x:  X `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:  Y `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param vv_z:  Z `GXVV <geosoft.gxapi.GXVV>`,REAL `GXVV <geosoft.gxapi.GXVV>`
        :param gap:   Gap size (must be greater than zero)
        :param vv_g:  Returned indices of start of sections after gaps (INT `GXVV <geosoft.gxapi.GXVV>`)
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV
        :type  gap:   float
        :type  vv_g:  GXVV

        .. versionadded:: 8.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Locate the starting points of line segements determined by an input gap distance.
        The returned indices indicate where to break the line, given an input gap.
        The number of returned indices is one less than the number of line segments.
        (So if there are no gaps the returned `GXVV <geosoft.gxapi.GXVV>` has zero length).
        """
        
        gxapi_cy.WrapVVU._find_gaps_3d(GXContext._get_tls_geo(), vv_x, vv_y, vv_z, gap, vv_g)
        



    @classmethod
    def dummy_range(cls, vv, min, max, inside, incl):
        """
        
        Dummy values inside or outside a range in a `GXVV <geosoft.gxapi.GXVV>`
        
        :param vv:      `GXVV <geosoft.gxapi.GXVV>` handle
        :param min:     Minimum range value
        :param max:     Maximum range value
        :param inside:  If TRUE, dummy inside the range
        :param incl:    If TRUE, include Min, Max in the range.
        :type  vv:      GXVV
        :type  min:     float
        :type  max:     float
        :type  inside:  int
        :type  incl:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the Inside flag is TRUE, values within the specified
        range are set to dummy. If the inside flag is FALSE,
        values outside the range are set to dummy.  If the Inclusive
        flag is TRUE, then dMin and dMax are considered part of the
        range. If it is FALSE, then < or > are used, and dMin and
        dMax lie outside the range.
        """
        
        gxapi_cy.WrapVVU._dummy_range(GXContext._get_tls_geo(), vv, min, max, inside, incl)
        



    @classmethod
    def dummy_range_ex(cls, vv, min, max, inside, include_min, include_max):
        """
        
        Like DummyRangeVVU, with inclusion options for both ends.
        
        :param vv:           `GXVV <geosoft.gxapi.GXVV>` handle
        :param min:          Minimum range value
        :param max:          Maximum range value
        :param inside:       If TRUE, dummy inside the range
        :param include_min:  If TRUE, include Min in the range.
        :param include_max:  If TRUE, include Max in the range.
        :type  vv:           GXVV
        :type  min:          float
        :type  max:          float
        :type  inside:       int
        :type  include_min:  int
        :type  include_max:  int

        .. versionadded:: 5.0.7

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the Inside flag is TRUE, values within the specified
        range are set to dummy. If the inside flag is FALSE,
        values outside the range are set to dummy.  If the Inclusive
        flag is TRUE, then dMin and dMax are considered part of the
        range. If it is FALSE, then < or > are used, and dMin and
        dMax lie outside the range.
        """
        
        gxapi_cy.WrapVVU._dummy_range_ex(GXContext._get_tls_geo(), vv, min, max, inside, include_min, include_max)
        



    @classmethod
    def dummy_repeat(cls, vv, mode):
        """
        
        Dummy repeat values in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param mode:  :ref:`VVU_DUMMYREPEAT`
        :type  vv:    GXVV
        :type  mode:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Either the first, middle or last point will be left.
                          Use `interp <geosoft.gxapi.GXVVU.interp>` to interpolate after if desired.
        """
        
        gxapi_cy.WrapVVU._dummy_repeat(GXContext._get_tls_geo(), vv, mode)
        



    @classmethod
    def dup_stats(cls, data_vv, sample_vv, mean_vv, diff_vv):
        """
        
        Calculate means and differences for duplicate sample pairs
        
        :param data_vv:    Duplicate data `GXVV <geosoft.gxapi.GXVV>`
        :param sample_vv:  Sample Type `GXVV <geosoft.gxapi.GXVV>`
        :param mean_vv:    Mean values `GXVV <geosoft.gxapi.GXVV>` (returned)
        :param diff_vv:    Diff values `GXVV <geosoft.gxapi.GXVV>` (returned)
        :type  data_vv:    GXVV
        :type  sample_vv:  GXVV
        :type  mean_vv:    GXVV
        :type  diff_vv:    GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Created for duplicate sample handling in `GXCHIMERA <geosoft.gxapi.GXCHIMERA>`. On input,
        a numeric `GXVV <geosoft.gxapi.GXVV>` containing data values, and a sample type `GXVV <geosoft.gxapi.GXVV>`.
        Sample pairs have types "1" and "2". This routine searches for
        types in order "1 2 1 2", and writes the mean values of pairs
        to the mean value `GXVV <geosoft.gxapi.GXVV>`, and the differences with the mean (equal
        values, negative and positive) to the difference `GXVV <geosoft.gxapi.GXVV>`. Results
        for samples out of order, for unmatched values, or when the
        sample type does not equal "1" or "2" are set to dummy.
        """
        
        gxapi_cy.WrapVVU._dup_stats(GXContext._get_tls_geo(), data_vv, sample_vv, mean_vv, diff_vv)
        



    @classmethod
    def exp_dist(cls, vv, seed, mean, length):
        """
        
        Fill with exponentially distributed values.
        
        :param vv:      `GXVV <geosoft.gxapi.GXVV>` object
        :param seed:    Random number generator seed
        :param mean:    Mean value of distribution (> 0.0)
        :param length:  Number of values (-1 for all)
        :type  vv:      GXVV
        :type  seed:    int
        :type  mean:    float
        :type  length:  int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** `GXVV <geosoft.gxapi.GXVV>` is set to input length (except for -1)
        See RAND for a short discription of the
        random number generator used.
        """
        
        gxapi_cy.WrapVVU._exp_dist(GXContext._get_tls_geo(), vv, seed, mean, length)
        



    @classmethod
    def filter(cls, vv_i, vv_o, flt):
        """
        
        Apply a convolution filter to a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vv_i:  Input `GXVV <geosoft.gxapi.GXVV>`
        :param vv_o:  Filtered `GXVV <geosoft.gxapi.GXVV>`
        :param flt:   Filter handle (see `GXFLT <geosoft.gxapi.GXFLT>`)
        :type  vv_i:  GXVV
        :type  vv_o:  GXVV
        :type  flt:   int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        gxapi_cy.WrapVVU._filter(GXContext._get_tls_geo(), vv_i, vv_o, flt)
        



    @classmethod
    def find_string_items(cls, vv_source, vv_search, pis_source_sorted, pis_search_sorted, pis_case_tolerant, vv_i):
        """
        
        Searches a `GXVV <geosoft.gxapi.GXVV>` for items in a second `GXVV <geosoft.gxapi.GXVV>`, returns indices of those found.
        
        :param vv_source:          String `GXVV <geosoft.gxapi.GXVV>` in which to locate items
        :param vv_search:          String `GXVV <geosoft.gxapi.GXVV>` Items to search for
        :param pis_source_sorted:  Is the first `GXVV <geosoft.gxapi.GXVV>` already sorted?
        :param pis_search_sorted:  Is the second `GXVV <geosoft.gxapi.GXVV>` already sorted
        :param pis_case_tolerant:  Case tolerance for string comparisons
        :param vv_i:               `GS_LONG <geosoft.gxapi.GS_LONG>` `GXVV <geosoft.gxapi.GXVV>` of returned indices into the first `GXLST <geosoft.gxapi.GXLST>`.
        :type  vv_source:          GXVV
        :type  vv_search:          GXVV
        :type  pis_source_sorted:  int
        :type  pis_search_sorted:  int
        :type  pis_case_tolerant:  int
        :type  vv_i:               GXVV

        .. versionadded:: 7.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This is a much more efficient way of determining if items in
        one `GXVV <geosoft.gxapi.GXVV>` are found in a second, than by searching
        repeatedly in a loop.
        The returned `GS_LONG <geosoft.gxapi.GS_LONG>` `GXVV <geosoft.gxapi.GXVV>` contains the same number of items as
        the "search items" `GXVV <geosoft.gxapi.GXVV>`, and contains -1 for items where the
        value is not found, and the index of items that are found.
        Comparisons are case-tolerant.
        Non-string VVs are converted to string type VVs (element size 24) internally.

        The method requires that the `GXVV <geosoft.gxapi.GXVV>` items be sorted, and
        will do so internally. Since the input VVs may already be sorted,
        the method will run faster if this stage can be skipped.
        """
        
        gxapi_cy.WrapVVU._find_string_items(GXContext._get_tls_geo(), vv_source, vv_search, pis_source_sorted, pis_search_sorted, pis_case_tolerant, vv_i)
        



    @classmethod
    def fractal_filter(cls, vv_i, order, number, vv_o):
        """
        
        Fractal filter a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vv_i:    [i] `GXVV <geosoft.gxapi.GXVV>`
        :param order:   [i] filter order
        :param number:  [i] filter number
        :param vv_o:    [o] filtered `GXVV <geosoft.gxapi.GXVV>`
        :type  vv_i:    GXVV
        :type  order:   int
        :type  number:  int
        :type  vv_o:    GXVV

        .. versionadded:: 6.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        gxapi_cy.WrapVVU._fractal_filter(GXContext._get_tls_geo(), vv_i, order, number, vv_o)
        



    @classmethod
    def close_xy(cls, vv_x, vv_y, x, y):
        """
        
        Find the closest point to an input point (XY).
        
        :param vv_x:  X locations
        :param vv_y:  Y locations
        :param x:     Input X
        :param y:     Input Y
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  x:     float
        :type  y:     float

        :returns:     Index of closest point, -1 if no valid locations, or data is masked.
        :rtype:       int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Input X and Y location VVs, and a location.
        Returns the index of the point in the `GXVV <geosoft.gxapi.GXVV>` closest to the
        input point.
        """
        
        ret_val = gxapi_cy.WrapVVU._close_xy(GXContext._get_tls_geo(), vv_x, vv_y, x, y)
        return ret_val



    @classmethod
    def close_xym(cls, vv_x, vv_y, vv_m, x, y):
        """
        
        Find the closest point to an input point, with mask (XY).
        
        :param vv_x:  X locations
        :param vv_y:  Y locations
        :param vv_m:  Mask values
        :param x:     Input X
        :param y:     Input Y
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_m:  GXVV
        :type  x:     float
        :type  y:     float

        :returns:     Index of closest point, -1 if no valid locations, or data is masked.
        :rtype:       int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Input X and Y location VVs, and a location.
        Returns the index of the point in the `GXVV <geosoft.gxapi.GXVV>` closest to the
        input point.
        This skips points where the mask value is dummy.
        If no valid points are in the VVs, or all the mask `GXVV <geosoft.gxapi.GXVV>` values
        are dummy, the returned index is -1.
        """
        
        ret_val = gxapi_cy.WrapVVU._close_xym(GXContext._get_tls_geo(), vv_x, vv_y, vv_m, x, y)
        return ret_val



    @classmethod
    def close_xyz(cls, vv_x, vv_y, vv_z, x, y, z):
        """
        
        Find the closest point to an input point (XYZ).
        
        :param vv_x:  X locations
        :param vv_y:  Y locations
        :param vv_z:  Z locations
        :param x:     Input X
        :param y:     Input Y
        :param z:     Input Z
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV
        :type  x:     float
        :type  y:     float
        :type  z:     float

        :returns:     Index of closest point, -1 if no valid locations, or data is masked.
        :rtype:       int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Input X, Y and Z location VVs, and a location.
        Returns the index of the point in the `GXVV <geosoft.gxapi.GXVV>` closest to the
        input point.
        """
        
        ret_val = gxapi_cy.WrapVVU._close_xyz(GXContext._get_tls_geo(), vv_x, vv_y, vv_z, x, y, z)
        return ret_val



    @classmethod
    def close_xyzm(cls, vv_x, vv_y, vv_z, vv_m, x, y, z):
        """
        
        Find the closest point to an input point, with mask (XYZ).
        
        :param vv_x:  X locations
        :param vv_y:  Y locations
        :param vv_z:  Z locations
        :param vv_m:  Mask values
        :param x:     Input X
        :param y:     Input Y
        :param z:     Input Z
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_z:  GXVV
        :type  vv_m:  GXVV
        :type  x:     float
        :type  y:     float
        :type  z:     float

        :returns:     Index of closest point, -1 if no valid locations, or data is masked.
        :rtype:       int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Input X, Y and Z location VVs, and a location.
        Returns the index of the point in the `GXVV <geosoft.gxapi.GXVV>` closest to the
        input point.
        This skips points where the mask value is dummy.
        If no valid points are in the VVs, or all the mask `GXVV <geosoft.gxapi.GXVV>` values
        are dummy, the returned index is -1.
        """
        
        ret_val = gxapi_cy.WrapVVU._close_xyzm(GXContext._get_tls_geo(), vv_x, vv_y, vv_z, vv_m, x, y, z)
        return ret_val



    @classmethod
    def dummy_back_tracks(cls, vv):
        """
        
        Dummy all points that keep a `GXVV <geosoft.gxapi.GXVV>` from being monotonically increasing.
        
        :param vv:  `GXVV <geosoft.gxapi.GXVV>` handle
        :type  vv:  GXVV

        :returns:    The number of items dummied in order to render the `GXVV <geosoft.gxapi.GXVV>` montonically increasing.
        :rtype:      int

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The `GXVV <geosoft.gxapi.GXVV>` length remains the same. Any point that is less than or equal to
        the previous (valid) point in the `GXVV <geosoft.gxapi.GXVV>` is dummied.
        """
        
        ret_val = gxapi_cy.WrapVVU._dummy_back_tracks(GXContext._get_tls_geo(), vv)
        return ret_val



    @classmethod
    def find_dummy(cls, vv, dir, type, start, end):
        """
        
        Find the first dummy|non-dummy value in `GXVV <geosoft.gxapi.GXVV>`
        
        :param vv:     `GXVV <geosoft.gxapi.GXVV>` handle
        :param dir:    0 increasing order 1 decreasing order
        :param type:   0 to find the first dummy 1 find first non-dummy
        :param start:  Start search range at element
        :param end:    End search range at element (-1 for last)
        :type  vv:     GXVV
        :type  dir:    int
        :type  type:   int
        :type  start:  int
        :type  end:    int

        :returns:      The index of the first dummy|non-dummy value in `GXVV <geosoft.gxapi.GXVV>`
                       -1 if not found or if length of `GXVV <geosoft.gxapi.GXVV>` is 0
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Start and end of range are always defined lowest
        to largest even if decreasing search order.  To search
        entire `GXVV <geosoft.gxapi.GXVV>` range, specify 0,-1.
        """
        
        ret_val = gxapi_cy.WrapVVU._find_dummy(GXContext._get_tls_geo(), vv, dir, type, start, end)
        return ret_val



    @classmethod
    def interp(cls, vv, input, output):
        """
        
        Replace all dummies by interpolating from valid data.
        
        :param vv:      Input `GXVV <geosoft.gxapi.GXVV>`
        :param input:   :ref:`VVU_INTERP`
        :param output:  :ref:`VVU_INTERP_EDGE`
        :type  vv:      GXVV
        :type  input:   int
        :type  output:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Edge behaviour
             Dummies at the ends are treated as follows
             for various combinations of the inside and outside interpolation
             choices:

        ::

          if ((iOutside==VV_INTERP_EDGE_NEAREST) ||
              (iOutside==VV_INTERP_EDGE_SAME && iInside==VV_INTERP_NEAREST))

               // -- Set dummies to the same value as the last defined element

          else if ((iOutside==VV_INTERP_EDGE_LINEAR) ||
                   (iOutside==VV_INTERP_EDGE_SAME &&  iInside==VV_INTERP_LINEAR))

               // --- Set dummies using the slope of the last two defined elements

          endif

        In all other cases and combinations of the two interpolation
        choices, the dummies are left "as is".
        """
        
        gxapi_cy.WrapVVU._interp(GXContext._get_tls_geo(), vv, input, output)
        



    @classmethod
    def qc_fill_gaps(cls, vvx, vvy, vvf, vvd, dist):
        """
        
        Calculate fill in line segments
        
        :param vvx:   Input/output X `GXVV <geosoft.gxapi.GXVV>` on which to operate Required in `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` or `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`
        :param vvy:   Input/output Y `GXVV <geosoft.gxapi.GXVV>` on which to operate In `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` or `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`
        :param vvf:   Input Flag `GXVV <geosoft.gxapi.GXVV>` Required in `GS_BYTE <geosoft.gxapi.GS_BYTE>`
        :param vvd:   Input Gap `GXVV <geosoft.gxapi.GXVV>` to use for locating the fill inline segments In `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` or `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`
        :param dist:  Min segment length  (required)
        :type  vvx:   GXVV
        :type  vvy:   GXVV
        :type  vvf:   GXVV
        :type  vvd:   GXVV
        :type  dist:  float

        :returns:     1 if error, 0 if successful
        :rtype:       int

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The X & Y VVs are returned as the calculated fill in line segments.
        """
        
        ret_val = gxapi_cy.WrapVVU._qc_fill_gaps(GXContext._get_tls_geo(), vvx, vvy, vvf, vvd, dist)
        return ret_val



    @classmethod
    def search_text(cls, vv, text, case_sensitive, match, start, dir):
        """
        
        Search for a text value in a `GXVV <geosoft.gxapi.GXVV>`
        
        :param vv:              `GXVV <geosoft.gxapi.GXVV>` to search
        :param text:            Text to match
        :param case_sensitive:  :ref:`VVU_CASE`
        :param match:           :ref:`VVU_MATCH`
        :param start:           Index to begin search (-1 for full `GXVV <geosoft.gxapi.GXVV>`)
        :param dir:             1: forward search, -1: backward search
        :type  vv:              GXVV
        :type  text:            str
        :type  case_sensitive:  int
        :type  match:           int
        :type  start:           int
        :type  dir:             int

        :returns:               Index of first matching text, -1 if not found.
        :rtype:                 int

        .. versionadded:: 5.0.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Search comparison is made on string comparison
        of the data. Returns index of first item matching
        the input string.
        If start index is -1 or dummy, then full `GXVV <geosoft.gxapi.GXVV>` is searched.
        Use `VVU_MATCH_INPUT_LENGTH <geosoft.gxapi.VVU_MATCH_INPUT_LENGTH>` to match the first part of a string.
        This is also recommended for matching numerical values, since
        the displayed value in the database may not be the same as the
        stored value.

        .. seealso::

            sSearchReplace_VV
        """
        
        ret_val = gxapi_cy.WrapVVU._search_text(GXContext._get_tls_geo(), vv, text.encode(), case_sensitive, match, start, dir)
        return ret_val



    @classmethod
    def mask(cls, vv_d, vv_m):
        """
        
        Mask dummies in one `GXVV <geosoft.gxapi.GXVV>` onto another.
        
        :param vv_d:  `GXVV <geosoft.gxapi.GXVV>` to be masked
        :param vv_m:  Mask reference `GXVV <geosoft.gxapi.GXVV>`
        :type  vv_d:  GXVV
        :type  vv_m:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** `GXVV <geosoft.gxapi.GXVV>` to mask will be resampled to reference `GXVV <geosoft.gxapi.GXVV>` if required.
        The returned length of the `GXVV <geosoft.gxapi.GXVV>` to mask will be the shorter
        of the reference `GXVV <geosoft.gxapi.GXVV>` or the mask `GXVV <geosoft.gxapi.GXVV>`.
        """
        
        gxapi_cy.WrapVVU._mask(GXContext._get_tls_geo(), vv_d, vv_m)
        



    @classmethod
    def mask_and(cls, vv_a, vv_b, vv_c):
        """
        
        Create mask from logical AND of two VVs.
        
        :param vv_a:  `GXVV <geosoft.gxapi.GXVV>` A
        :param vv_b:  `GXVV <geosoft.gxapi.GXVV>` B
        :param vv_c:  `GXVV <geosoft.gxapi.GXVV>` C (returned)
        :type  vv_a:  GXVV
        :type  vv_b:  GXVV
        :type  vv_c:  GXVV

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If both values are non-dummies, then result is 1, else dummy.
        """
        
        gxapi_cy.WrapVVU._mask_and(GXContext._get_tls_geo(), vv_a, vv_b, vv_c)
        



    @classmethod
    def mask_or(cls, vv_a, vv_b, vv_c):
        """
        
        Create mask from logical OR of two VVs.
        
        :param vv_a:  `GXVV <geosoft.gxapi.GXVV>` A
        :param vv_b:  `GXVV <geosoft.gxapi.GXVV>` B
        :param vv_c:  `GXVV <geosoft.gxapi.GXVV>` C (returned)
        :type  vv_a:  GXVV
        :type  vv_b:  GXVV
        :type  vv_c:  GXVV

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If either values is non-dummy, then result is 1, else dummy.
        """
        
        gxapi_cy.WrapVVU._mask_or(GXContext._get_tls_geo(), vv_a, vv_b, vv_c)
        



    @classmethod
    def nl_filt(cls, vv_i, vv_o, fwid, pr_ftol):
        """
        
        Applies a non-linear filter.
        
        :param vv_i:     Input `GXVV <geosoft.gxapi.GXVV>`
        :param vv_o:     Filtered `GXVV <geosoft.gxapi.GXVV>`
        :param fwid:     Filter Width
        :param pr_ftol:  Filter Tolerance, 0 for 1% of Std. Dev.
        :type  vv_i:     GXVV
        :type  vv_o:     GXVV
        :type  fwid:     int
        :type  pr_ftol:  float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        gxapi_cy.WrapVVU._nl_filt(GXContext._get_tls_geo(), vv_i, vv_o, fwid, pr_ftol)
        



    @classmethod
    def noise_check(cls, vv_i, vv_f, all_tol, num):
        """
        
        Check on deviation of data from variable background in a `GXVV <geosoft.gxapi.GXVV>`
        
        :param vv_i:     Input `GXVV <geosoft.gxapi.GXVV>` on which to apply quality control Required in `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` or `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`
        :param vv_f:     Output flag `GXVV <geosoft.gxapi.GXVV>` with result 0 and 1. Required in `GS_BYTE <geosoft.gxapi.GS_BYTE>`
        :param all_tol:  Allowed deviation over a number of data points in input `GXVV <geosoft.gxapi.GXVV>` (next parameter). Must be >= 0.0
        :param num:      Number of data points. Must be > 0
        :type  vv_i:     GXVV
        :type  vv_f:     GXVV
        :type  all_tol:  float
        :type  num:      int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This function checks vertical deviation of data in input `GXVV <geosoft.gxapi.GXVV>`
        against a moving straight line. The straight line at any time is
        defined by two extreme points of a data segment.  Output `GXVV <geosoft.gxapi.GXVV>` will
        be 0 if data point in input `GXVV <geosoft.gxapi.GXVV>` falls within the deviation,
        otherwise, it will be 1.
        Output `GXVV <geosoft.gxapi.GXVV>` will be 0 if the straight line is vertical.
        """
        
        gxapi_cy.WrapVVU._noise_check(GXContext._get_tls_geo(), vv_i, vv_f, all_tol, num)
        



    @classmethod
    def noise_check2(cls, vv_i, vv_f, vv_d, all_tol, num):
        """
        
        Like `noise_check <geosoft.gxapi.GXVVU.noise_check>`, but returns maximum deviation at all points.
        
        :param vv_i:     Input `GXVV <geosoft.gxapi.GXVV>` on which to apply quality control Required in `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` or `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`
        :param vv_f:     Output flag `GXVV <geosoft.gxapi.GXVV>` with result 0 and 1. Required in `GS_BYTE <geosoft.gxapi.GS_BYTE>`
        :param vv_d:     Output maximum deviation `GXVV <geosoft.gxapi.GXVV>`.
        :param all_tol:  Allowed deviation over a number of data points in input `GXVV <geosoft.gxapi.GXVV>` (next parameter). Must be >= 0.0
        :param num:      Number of data points in the line segment. Must be > 0
        :type  vv_i:     GXVV
        :type  vv_f:     GXVV
        :type  vv_d:     GXVV
        :type  all_tol:  float
        :type  num:      int

        .. versionadded:: 6.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This function checks vertical deviation of data in an input `GXVV <geosoft.gxapi.GXVV>`
        against a moving straight line, where the X-axis value is
        taken to be the data index, and the Y-axis value is the
        input data `GXVV <geosoft.gxapi.GXVV>` value. The straight line is drawn between data points
        at the ends of the line segment, whose length is an input.

        The output flag `GXVV <geosoft.gxapi.GXVV>` is set to 0 if data point in input `GXVV <geosoft.gxapi.GXVV>` falls within the
        deviation for all the moving line segments of which it is a part, otherwise, it
        will be set to 1.

        The output maximum deviation `GXVV <geosoft.gxapi.GXVV>` contains the maximum deviation at each point
        for all the moving line segments that it is a part of.
        """
        
        gxapi_cy.WrapVVU._noise_check2(GXContext._get_tls_geo(), vv_i, vv_f, vv_d, all_tol, num)
        



    @classmethod
    def normal_dist(cls, vv, seed, mean, var, length):
        """
        
        Fill with normally (Gaussian) distributed values.
        
        :param vv:      `GXVV <geosoft.gxapi.GXVV>` object
        :param seed:    Random number generator seed
        :param mean:    Mean value of distribution
        :param var:     Variance of the distribution
        :param length:  Number of values (-1 for all)
        :type  vv:      GXVV
        :type  seed:    int
        :type  mean:    float
        :type  var:     float
        :type  length:  int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** `GXVV <geosoft.gxapi.GXVV>` is set to input length (except for -1)
        See RAND for a short discription of the
        random number generator used.
        """
        
        gxapi_cy.WrapVVU._normal_dist(GXContext._get_tls_geo(), vv, seed, mean, var, length)
        



    @classmethod
    def offset_circles(cls, vv_xi, vv_yi, offset, radius, vv_xo, vv_yo):
        """
        
        Get non-overlapping offset location for circular symbols.
        
        :param vv_xi:   Input X locations
        :param vv_yi:   Input Y locations
        :param offset:  Minimum offset distance
        :param radius:  Symbol radius
        :param vv_xo:   Output (offset) X locations
        :param vv_yo:   Output (offset) Y locations
        :type  vv_xi:   GXVV
        :type  vv_yi:   GXVV
        :type  offset:  float
        :type  radius:  float
        :type  vv_xo:   GXVV
        :type  vv_yo:   GXVV

        .. versionadded:: 5.0.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Often on maps plotted symbols and text overlap each other.
        This routine accepts of `GXVV <geosoft.gxapi.GXVV>` of locations and returns a new
        set of locations offset from the originals, and guaranteed
        not to overlap, given the size of the original symbols.
        The returned offset X, Y
        locations are offset from the original locations by
        the minimum of a) the input offset, b) the input symbol
        radius. This is to ensure that the original location is
        never covered by the offset symbol.

        Care should be taken when choosing the symbol size, because
        if the point density is too high, all the points will get
        pushed to the outside edge and your plot will look like a
        hedgehog (it also takes a lot longer!).
        """
        
        gxapi_cy.WrapVVU._offset_circles(GXContext._get_tls_geo(), vv_xi, vv_yi, offset, radius, vv_xo, vv_yo)
        



    @classmethod
    def offset_correct(cls, vv_xi, vv_yi, dist, heading, v_vxo, v_vyo):
        """
        
        Correct locations based on heading and fixed offset.
        
        :param vv_xi:    Input X
        :param vv_yi:    Input Y
        :param dist:     Offset distance
        :param heading:  :ref:`VVU_OFFSET`
        :param v_vxo:    Output X
        :param v_vyo:    Output Y
        :type  vv_xi:    GXVV
        :type  vv_yi:    GXVV
        :type  dist:     float
        :type  heading:  int
        :type  v_vxo:    GXVV
        :type  v_vyo:    GXVV

        .. versionadded:: 5.0.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** In many applications, measurements are taken with an instrument which
        is towed behind, or pushed ahead of where the locations are recorded.
        Use this function to estimate the actual location of the instrument.
        The method determines the heading along the line, using a "thinned"
        version of the line. The degree of thinning is based on the size of the
        offset; the larger the offset, the greater the distance between sample
        locations used to construct the thinned lined used for determining headings.
        The thinned line is splined at a frequency greater than the sample
        frequency, and the heading at any given point is determined from the
        vector formed by the closest two points on the splined line. The
        correction (behind, in front, left or right) is determined with respect
        to the heading, and added to the original location.

        IF this method fails, no dummies, no duplicated locations, no reversals
        are produced.

        The algorithm:

            1. Determine average distance between each point = D
            2. Smoothing interval = MAX(2*D, Offset distance) = I
            3. Thin input points to be at least the smoothing interval I apart from each other.
            4. Smoothly re-interpolate the thinned points at five times the
               original average distance D.
            5. For each input point, calculate the bearing using the nearest points
               on the smoothed curve
        """
        
        gxapi_cy.WrapVVU._offset_correct(GXContext._get_tls_geo(), vv_xi, vv_yi, dist, heading, v_vxo, v_vyo)
        



    @classmethod
    def offset_correct2(cls, vv_xi, vv_yi, dist, azimuth, vv_xo, vv_yo):
        """
        
        Same as `offset_correct <geosoft.gxapi.GXVVU.offset_correct>`, but for an arbitrary offset angle.
        
        :param vv_xi:    Input X
        :param vv_yi:    Input Y
        :param dist:     Offset distance
        :param azimuth:  Offset azimuth (degrees counter-clockwise from straight ahead)
        :param vv_xo:    Output X
        :param vv_yo:    Output Y
        :type  vv_xi:    GXVV
        :type  vv_yi:    GXVV
        :type  dist:     float
        :type  azimuth:  float
        :type  vv_xo:    GXVV
        :type  vv_yo:    GXVV

        .. versionadded:: 5.1.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        gxapi_cy.WrapVVU._offset_correct2(GXContext._get_tls_geo(), vv_xi, vv_yi, dist, azimuth, vv_xo, vv_yo)
        



    @classmethod
    def offset_correct3(cls, vv_xi, vv_yi, dist, azimuth, interval, vv_xo, vv_yo):
        """
        
        Same as `offset_correct2 <geosoft.gxapi.GXVVU.offset_correct2>`, but specify smoothing interval.
        
        :param vv_xi:     Input X
        :param vv_yi:     Input Y
        :param dist:      Offset distance
        :param azimuth:   Offset azimuth (degrees counter-clockwise from straight ahead)
        :param interval:  Averaging interval - `rDUMMY <geosoft.gxapi.rDUMMY>` for default
        :param vv_xo:     Output X
        :param vv_yo:     Output Y
        :type  vv_xi:     GXVV
        :type  vv_yi:     GXVV
        :type  dist:      float
        :type  azimuth:   float
        :type  interval:  float
        :type  vv_xo:     GXVV
        :type  vv_yo:     GXVV

        .. versionadded:: 5.1.4

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** See the algorithm note #2 above for the default smoothing interval.
        """
        
        gxapi_cy.WrapVVU._offset_correct3(GXContext._get_tls_geo(), vv_xi, vv_yi, dist, azimuth, interval, vv_xo, vv_yo)
        



    @classmethod
    def offset_correct_xyz(cls, vv_xi, vv_yi, vv_zi, x_off, y_off, z_off, interval, v_vxo, v_vyo, v_vzo):
        """
        
        Correct locations based on heading and fixed offset.
        
        :param vv_xi:     Input X
        :param vv_yi:     Input Y
        :param vv_zi:     Input Z
        :param x_off:     Offset along-track (+ve forward)
        :param y_off:     Offset across-track (+ve to the right)
        :param z_off:     Vertical Offset (+ve up)
        :param interval:  Sampling interval - `rDUMMY <geosoft.gxapi.rDUMMY>` for default
        :param v_vxo:     Output X
        :param v_vyo:     Output Y
        :param v_vzo:     Output Z
        :type  vv_xi:     GXVV
        :type  vv_yi:     GXVV
        :type  vv_zi:     GXVV
        :type  x_off:     float
        :type  y_off:     float
        :type  z_off:     float
        :type  interval:  float
        :type  v_vxo:     GXVV
        :type  v_vyo:     GXVV
        :type  v_vzo:     GXVV

        .. versionadded:: 9.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** In many applications, measurements are taken with an instrument which
        is towed behind, or pushed ahead of where the locations are recorded.
        Use this function to estimate the actual location of the instrument.
        The method determines the heading along the line, using a "thinned"
        version of the line. The default degree of thinning is based on the size of the
        offset; the larger the offset, the greater the distance between sample
        locations used to construct the thinned lined used for determining headings.
        The thinned line is splined at a frequency greater than the sample
        frequency, and the heading at any given point is determined from the
        vector formed by the closest two points on the splined line. The
        correction (behind, in front, left or right) is determined with respect
        to the heading, and added to the original location.

        IF this method fails, no dummies, no duplicated locations, no reversals
        are produced.

        The algorithm:

            1. Determine average distance between each point = D
            2. Default smoothing interval = MAX(2*D, Offset distance) = I
            3. Thin input points to be at least the smoothing interval I apart from each other.
            4. Smoothly re-interpolate the thinned points at five times the
               original average distance D.
            5. For each input point, calculate the bearing using the nearest points
               on the smoothed curve
        """
        
        gxapi_cy.WrapVVU._offset_correct_xyz(GXContext._get_tls_geo(), vv_xi, vv_yi, vv_zi, x_off, y_off, z_off, interval, v_vxo, v_vyo, v_vzo)
        



    @classmethod
    def offset_rectangles(cls, vv_xi, vv_yi, offset, size_x, size_y, vv_xo, vv_yo):
        """
        
        Get non-overlapping offset location for rectangular symbols.
        
        :param vv_xi:   Input X locations
        :param vv_yi:   Input Y locations
        :param offset:  Minimum offset distance
        :param size_x:  Symbol X size (width)
        :param size_y:  Symbol Y size (height)
        :param vv_xo:   Output (offset) X locations
        :param vv_yo:   Output (offset) Y locations
        :type  vv_xi:   GXVV
        :type  vv_yi:   GXVV
        :type  offset:  float
        :type  size_x:  float
        :type  size_y:  float
        :type  vv_xo:   GXVV
        :type  vv_yo:   GXVV

        .. versionadded:: 5.0.7

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Often on maps plotted symbols and text overlap each other.
        This routine accepts of `GXVV <geosoft.gxapi.GXVV>` of locations and returns a new
        set of locations offset from the originals, and guaranteed
        not to overlap, given the size of the original symbols.
        The returned offset X, Y
        locations are offset from the original locations by
        the minimum of a) the input offset, b) the input symbol
        X or Y size. This is to ensure that the original location is
        never covered by the offset symbol. In addition, the offset
        symbol is never place directly below the original location,
        to make it easier to draw a connecting line.

        Care should be taken when choosing the symbol size, because
        if the point density is too high, all the points will get
        pushed to the outside edge and your plot will look like a
        hedgehog (it also takes a lot longer!).
        """
        
        gxapi_cy.WrapVVU._offset_rectangles(GXContext._get_tls_geo(), vv_xi, vv_yi, offset, size_x, size_y, vv_xo, vv_yo)
        



    @classmethod
    def pick_peak(cls, vv_i, vv_o, pr_tol, width):
        """
        
        Find peaks in a `GXVV <geosoft.gxapi.GXVV>` - method one.
        
        :param vv_i:    Input `GXVV <geosoft.gxapi.GXVV>`
        :param vv_o:    Returned peak `GXVV <geosoft.gxapi.GXVV>`, all dummies except peak points.
        :param pr_tol:  Minimum value to accept (0.0 to find all)
        :param width:   Minimum width to accept (1 to find all)
        :type  vv_i:    GXVV
        :type  vv_o:    GXVV
        :type  pr_tol:  float
        :type  width:   int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Peaks are the maximum point within a sequence of
        positive values in the input `GXVV <geosoft.gxapi.GXVV>`.  The width is the
        number of points in the positive sequence.

        A `GXVV <geosoft.gxapi.GXVV>` may have to be pre-filtered before finding
        the peak values:

        Use `bp_filt <geosoft.gxapi.GXVVU.bp_filt>` to smooth the data as required.
        Use `filter <geosoft.gxapi.GXVVU.filter>` to apply a Laplace filter
        "-0.5,1.0,-0.5" to make curvature data.
        """
        
        gxapi_cy.WrapVVU._pick_peak(GXContext._get_tls_geo(), vv_i, vv_o, pr_tol, width)
        



    @classmethod
    def pick_peak2(cls, vv_i, vv_o, pr_base_lvl, pr_ampl):
        """
        
        Find peaks in a `GXVV <geosoft.gxapi.GXVV>` - method two.
        
        :param vv_i:         Input `GXVV <geosoft.gxapi.GXVV>`
        :param vv_o:         Returned peak `GXVV <geosoft.gxapi.GXVV>`, all dummies except peak points.
        :param pr_base_lvl:  Base level to accept (0.0 to find all)
        :param pr_ampl:      Minimum amplitude to accept
        :type  vv_i:         GXVV
        :type  vv_o:         GXVV
        :type  pr_base_lvl:  float
        :type  pr_ampl:      float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Peaks are the maximum point within a sequence of
        values in the input `GXVV <geosoft.gxapi.GXVV>`. Maximum points must be above
        the base level and have a local amplitude greater
        than the minimum amplitude specified.

        A `GXVV <geosoft.gxapi.GXVV>` may have to be pre-filtered before finding
        the peak values.
        """
        
        gxapi_cy.WrapVVU._pick_peak2(GXContext._get_tls_geo(), vv_i, vv_o, pr_base_lvl, pr_ampl)
        



    @classmethod
    def pick_peak3(cls, vv_i, vv_x, vv_y, pr_base_lvl, pr_ampl, v_vind, v_vamp, v_vwid, v_vhawid):
        """
        
        Find peaks in a `GXVV <geosoft.gxapi.GXVV>` - method two, returning width and half-amplitude widths.
        
        :param vv_i:         [i] data `GXVV <geosoft.gxapi.GXVV>`
        :param vv_x:         [i] X `GXVV <geosoft.gxapi.GXVV>` used to calculate distance
        :param vv_y:         [i] Y `GXVV <geosoft.gxapi.GXVV>` used to calculate distance
        :param pr_base_lvl:  [i] minimum value to accept (0.0 to find all)
        :param pr_ampl:      [i] amplitude
        :param v_vind:       [o] Indices with peak locations
        :param v_vamp:       [o] Amplitudes at the peaks
        :param v_vwid:       [o] Anomaly widths
        :param v_vhawid:     [o] Anomaly half-amplitude widths
        :type  vv_i:         GXVV
        :type  vv_x:         GXVV
        :type  vv_y:         GXVV
        :type  pr_base_lvl:  float
        :type  pr_ampl:      float
        :type  v_vind:       GXVV
        :type  v_vamp:       GXVV
        :type  v_vwid:       GXVV
        :type  v_vhawid:     GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Uses Method 2 above, but also returns the anomaly width (defined
        as the distance between the surrounding troughs), and the
        width at the half-amplitude. The half-amplitude width is
        calculated in two parts, individually for each side based on
        the distance from the maximum to the location where the
        amplitude is mid-way between the maximum and trough.

        The returned VVs are packed; no dummies. Instead the
        indicies of the peak locations are returned.
        """
        
        gxapi_cy.WrapVVU._pick_peak3(GXContext._get_tls_geo(), vv_i, vv_x, vv_y, pr_base_lvl, pr_ampl, v_vind, v_vamp, v_vwid, v_vhawid)
        



    @classmethod
    def poly_fill(cls, vv_d, order, vv_c):
        """
        
        Fill a `GXVV <geosoft.gxapi.GXVV>` with values from an n'th order polynomial, integral x.
        
        :param vv_d:   `GXVV <geosoft.gxapi.GXVV>` with output data. (Preset length)
        :param order:  Order of the polynomial 0-9
        :param vv_c:   `GXVV <geosoft.gxapi.GXVV>` with polynomial coefficients (input)
        :type  vv_d:   GXVV
        :type  order:  int
        :type  vv_c:   GXVV

        .. versionadded:: 5.0.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The output `GXVV <geosoft.gxapi.GXVV>` length must be set as desired before calling.

        The X scale is unitless (1 per element), i.e. 0,1,2,3,...

        .. seealso::

            `trend <geosoft.gxapi.GXVVU.trend>`, `trend2 <geosoft.gxapi.GXVVU.trend2>`, `poly_fill2 <geosoft.gxapi.GXVVU.poly_fill2>`
        """
        
        gxapi_cy.WrapVVU._poly_fill(GXContext._get_tls_geo(), vv_d, order, vv_c)
        



    @classmethod
    def poly_fill2(cls, vv_x, vv_d, order, vv_c):
        """
        
        Fill a `GXVV <geosoft.gxapi.GXVV>` with values from an n'th order polynomial, specified X
        
        :param vv_x:   `GXVV <geosoft.gxapi.GXVV>` with x spacing (input)
        :param vv_d:   `GXVV <geosoft.gxapi.GXVV>` with output data. (Preset length)
        :param order:  Order of the polynomial 0-9
        :param vv_c:   `GXVV <geosoft.gxapi.GXVV>` with polynomial coefficients (order+1 values)
        :type  vv_x:   GXVV
        :type  vv_d:   GXVV
        :type  order:  int
        :type  vv_c:   GXVV

        .. versionadded:: 5.0.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The output `GXVV <geosoft.gxapi.GXVV>` length must be set as desired before calling.
        The X scale is defined by a X `GXVV <geosoft.gxapi.GXVV>` (see Trend_VV for unitless X).

        .. seealso::

            `trend <geosoft.gxapi.GXVVU.trend>`, `trend2 <geosoft.gxapi.GXVVU.trend2>`, `poly_fill <geosoft.gxapi.GXVVU.poly_fill>`
        """
        
        gxapi_cy.WrapVVU._poly_fill2(GXContext._get_tls_geo(), vv_x, vv_d, order, vv_c)
        



    @classmethod
    def polygon_mask(cls, vv_x, vv_y, vv_m, pply, mask):
        """
        
        Mask a `GXVV <geosoft.gxapi.GXVV>` using XY data and a polygon.
        
        :param vv_x:  X `GXVV <geosoft.gxapi.GXVV>`
        :param vv_y:  Y `GXVV <geosoft.gxapi.GXVV>`
        :param vv_m:  `GXVV <geosoft.gxapi.GXVV>` to be masked
        :param pply:  `GXPLY <geosoft.gxapi.GXPLY>` object
        :param mask:  :ref:`VVU_MASK`
        :type  vv_x:  GXVV
        :type  vv_y:  GXVV
        :type  vv_m:  GXVV
        :type  pply:  GXPLY
        :type  mask:  int

        .. versionadded:: 6.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** The VVs have to be the same length
        """
        
        gxapi_cy.WrapVVU._polygon_mask(GXContext._get_tls_geo(), vv_x, vv_y, vv_m, pply, mask)
        



    @classmethod
    def prune(cls, vv_p, vv_r, o):
        """
        
        Prune values from a `GXVV <geosoft.gxapi.GXVV>` based on reference `GXVV <geosoft.gxapi.GXVV>`
        
        :param vv_p:  `GXVV <geosoft.gxapi.GXVV>` to prune
        :param vv_r:  Reference `GXVV <geosoft.gxapi.GXVV>`
        :param o:     :ref:`VVU_PRUNE`
        :type  vv_p:  GXVV
        :type  vv_r:  GXVV
        :type  o:     int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Pruning will shorten the `GXVV <geosoft.gxapi.GXVV>` by removing values
        that are either dummy or non-dummy in the reference
        `GXVV <geosoft.gxapi.GXVV>`
        """
        
        gxapi_cy.WrapVVU._prune(GXContext._get_tls_geo(), vv_p, vv_r, o)
        



    @classmethod
    def qc(cls, vv_i, vv_d, v_vf, nominal, max_tol, all_tol, dist, qc):
        """
        
        Quality control on deviation of data from norm in a `GXVV <geosoft.gxapi.GXVV>`
        
        :param vv_i:     Input `GXVV <geosoft.gxapi.GXVV>` on which to apply quality control Required in `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` or `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`
        :param vv_d:     Distance `GXVV <geosoft.gxapi.GXVV>` (NULL if criterion #2 does not apply). In `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` or `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`
        :param v_vf:     Output flag `GXVV <geosoft.gxapi.GXVV>` with result 0,1,2,3,-1,-2,-3. Required in `GS_BYTE <geosoft.gxapi.GS_BYTE>`
        :param nominal:  Nominal reading  (required, must not be `GS_R8DM <geosoft.gxapi.GS_R8DM>`)
        :param max_tol:  Maximum tolerance/deviation applied to a single reading (criterion #1). `GS_R8DM <geosoft.gxapi.GS_R8DM>` if criterion #1 does not apply. Otherwise, must be positive value including 0.0
        :param all_tol:  Allowed tolerance/deviation over a given distance (next parameter) (criterion #2). `GS_R8DM <geosoft.gxapi.GS_R8DM>` if criterion #2 does not apply. Otherwise, must be positive value including 0.0
        :param dist:     The specified distance. `GS_R8DM <geosoft.gxapi.GS_R8DM>` if criterion #2 does not apply. Otherwise, must be positive value excluding 0.0
        :param qc:       :ref:`QC_CRITERION`
        :type  vv_i:     GXVV
        :type  vv_d:     GXVV
        :type  v_vf:     GXVV
        :type  nominal:  float
        :type  max_tol:  float
        :type  all_tol:  float
        :type  dist:     float
        :type  qc:       int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This function tests data in input `GXVV <geosoft.gxapi.GXVV>` against
        two separate criteria. Each element of the output `GXVV <geosoft.gxapi.GXVV>`
        will have one of the following indicators:

        =========  ==============================================================
        Indicator  Meaning
        =========  ==============================================================
          0        Input data passed both tests
        ---------  --------------------------------------------------------------
          1        The input data and is greater than the nominal value
                   plus maximum tolerance/deviation (Criterion #1)
        ---------  --------------------------------------------------------------
          2        The input data over a specified distance is greater than the
                   nominal value plus allowed tolerance (Criterion #2)
        ---------  --------------------------------------------------------------
          3        The input data failed on above two tests
        ---------  --------------------------------------------------------------
         -1        The input data and is less than the nominal value
                   minus maximum tolerance (Criterion #1)
        ---------  --------------------------------------------------------------
         -2        The input data over a specified distance is less than the
                   nominal value minus allowed tolerance (Criterion #2)
        ---------  --------------------------------------------------------------
         -3        The input data failed on above two tests
        =========  ==============================================================
        """
        
        gxapi_cy.WrapVVU._qc(GXContext._get_tls_geo(), vv_i, vv_d, v_vf, nominal, max_tol, all_tol, dist, qc)
        



    @classmethod
    def qc2(cls, vv_i, vv_d, v_vf, vv_drape, max_tol, all_tol, dist, qc):
        """
        
        Quality control on deviation of data from norm in a `GXVV <geosoft.gxapi.GXVV>`
        
        :param vv_i:      Input `GXVV <geosoft.gxapi.GXVV>` on which to apply quality control Required in `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` or `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`
        :param vv_d:      Distance `GXVV <geosoft.gxapi.GXVV>` (NULL if criterion #2 does not apply). In `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` or `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`
        :param v_vf:      Output flag `GXVV <geosoft.gxapi.GXVV>` with result 0,1,2,3,-1,-2,-3. Required in `GS_BYTE <geosoft.gxapi.GS_BYTE>`
        :param vv_drape:  Drape elevation `GXVV <geosoft.gxapi.GXVV>` which is used instead of a constant nominal terrain clearance Required in `GS_DOUBLE <geosoft.gxapi.GS_DOUBLE>` or `GS_FLOAT <geosoft.gxapi.GS_FLOAT>`
        :param max_tol:   Maximum tolerance/deviation applied to a single reading (criterion #1). `GS_R8DM <geosoft.gxapi.GS_R8DM>` if criterion #1 does not apply. Otherwise, must be positive value including 0.0
        :param all_tol:   Allowed tolerance/deviation over a given distance (next parameter) (criterion #2). `GS_R8DM <geosoft.gxapi.GS_R8DM>` if criterion #2 does not apply. Otherwise, must be positive value including 0.0
        :param dist:      The specified distance. `GS_R8DM <geosoft.gxapi.GS_R8DM>` if criterion #2 does not apply. Otherwise, must be positive value excluding 0.0
        :param qc:        :ref:`QC_CRITERION`
        :type  vv_i:      GXVV
        :type  vv_d:      GXVV
        :type  v_vf:      GXVV
        :type  vv_drape:  GXVV
        :type  max_tol:   float
        :type  all_tol:   float
        :type  dist:      float
        :type  qc:        int

        .. versionadded:: 2022.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** This function tests data in input `GXVV <geosoft.gxapi.GXVV>` against
        two separate criteria. Each element of the output `GXVV <geosoft.gxapi.GXVV>`
        will have one of the following indicators:

        =========  ==============================================================
        Indicator  Meaning
        =========  ==============================================================
          0        Input data passed both tests
        ---------  --------------------------------------------------------------
          1        The input data and is greater than the nominal value
                   plus maximum tolerance/deviation (Criterion #1)
        ---------  --------------------------------------------------------------
          2        The input data over a specified distance is greater than the
                   nominal value plus allowed tolerance (Criterion #2)
        ---------  --------------------------------------------------------------
          3        The input data failed on above two tests
        ---------  --------------------------------------------------------------
         -1        The input data and is less than the nominal value
                   minus maximum tolerance (Criterion #1)
        ---------  --------------------------------------------------------------
         -2        The input data over a specified distance is less than the
                   nominal value minus allowed tolerance (Criterion #2)
        ---------  --------------------------------------------------------------
         -3        The input data failed on above two tests
        =========  ==============================================================
        """
        
        gxapi_cy.WrapVVU._qc2(GXContext._get_tls_geo(), vv_i, vv_d, v_vf, vv_drape, max_tol, all_tol, dist, qc)
        



    @classmethod
    def range_vector_mag(cls, vv1, vv2, min, max):
        """
        
        Find the range of hypotenuse values of two VVs.
        
        :param vv1:  First `GXVV <geosoft.gxapi.GXVV>` (X)
        :param vv2:  First `GXVV <geosoft.gxapi.GXVV>` (Y)
        :param min:  Min value (returned)
        :param max:  Max value (returned)
        :type  vv1:  GXVV
        :type  vv2:  GXVV
        :type  min:  float_ref
        :type  max:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** For each value in the VVs, finds sqrt(dV1*dV1 + dV2*dV2)
        and returns the min and max values.
        """
        
        min.value, max.value = gxapi_cy.WrapVVU._range_vector_mag(GXContext._get_tls_geo(), vv1, vv2, min.value, max.value)
        



    @classmethod
    def regress(cls, vv_x, vv_y, slp, intercept):
        """
        
        Calculate linear regression through data
        
        :param vv_x:       X data
        :param vv_y:       Y data
        :param slp:        Returns slope
        :param intercept:  Returns intercept
        :type  vv_x:       GXVV
        :type  vv_y:       GXVV
        :type  slp:        float_ref
        :type  intercept:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        slp.value, intercept.value = gxapi_cy.WrapVVU._regress(GXContext._get_tls_geo(), vv_x, vv_y, slp.value, intercept.value)
        



    @classmethod
    def rel_var_dup(cls, data_vv, sample_vv, rel_var, num_dup):
        """
        
        Estimate relative variance of duplicate sample pairs from a database.
        
        :param data_vv:    Data `GXVV <geosoft.gxapi.GXVV>`
        :param sample_vv:  Sample Type `GXVV <geosoft.gxapi.GXVV>`
        :param rel_var:    Returned relative variance
        :param num_dup:    Returned number of duplicates used.
        :type  data_vv:    GXVV
        :type  sample_vv:  GXVV
        :type  rel_var:    float_ref
        :type  num_dup:    int_ref

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Created for duplicate sample handling in `GXCHIMERA <geosoft.gxapi.GXCHIMERA>`. On input,
        a numeric or text `GXVV <geosoft.gxapi.GXVV>` containing data values, and a sample type `GXVV <geosoft.gxapi.GXVV>`.
        Sample pairs have types "1" and "2". This routine searches for
        types in order "1 2 1 2", and calulates the unnormalized relative variance,
        defined as the sum of the squared differences between duplicates
        divided by the sum of the squared mean values of the duplicates.
        (To get the true rel.var., divide by N-1, where N is the number of
        duplicate pairs used.)
        Samples out of order, unmatched pairs, or when the
        sample type does not equal "1" or "2" are ignored.
        """
        
        rel_var.value, num_dup.value = gxapi_cy.WrapVVU._rel_var_dup(GXContext._get_tls_geo(), data_vv, sample_vv, rel_var.value, num_dup.value)
        



    @classmethod
    def remove_dummy(cls, vv):
        """
        
        Remove dummy values from a `GXVV <geosoft.gxapi.GXVV>`
        
        :type  vv:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        
        gxapi_cy.WrapVVU._remove_dummy(GXContext._get_tls_geo(), vv)
        



    @classmethod
    def remove_dummy2(cls, vv1, vv2):
        """
        
        Remove dummy values from 2 VVs.
        
        :param vv1:  `GXVV <geosoft.gxapi.GXVV>` object
        :param vv2:  `GXVV <geosoft.gxapi.GXVV>` object
        :type  vv1:  GXVV
        :type  vv2:  GXVV

        .. versionadded:: 5.0.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Removes all indices where either `GXVV <geosoft.gxapi.GXVV>` has a dummy, or is
        not defined (due to length differences).
        """
        
        gxapi_cy.WrapVVU._remove_dummy2(GXContext._get_tls_geo(), vv1, vv2)
        



    @classmethod
    def remove_dummy3(cls, vv1, vv2, vv3):
        """
        
        Remove dummy values from 3 VVs.
        
        :param vv1:  `GXVV <geosoft.gxapi.GXVV>` object
        :param vv2:  `GXVV <geosoft.gxapi.GXVV>` object
        :param vv3:  `GXVV <geosoft.gxapi.GXVV>` object
        :type  vv1:  GXVV
        :type  vv2:  GXVV
        :type  vv3:  GXVV

        .. versionadded:: 5.0.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Removes all indices where any `GXVV <geosoft.gxapi.GXVV>` has a dummy, or is
        not defined (due to length differences).
        """
        
        gxapi_cy.WrapVVU._remove_dummy3(GXContext._get_tls_geo(), vv1, vv2, vv3)
        



    @classmethod
    def remove_dummy4(cls, vv1, vv2, vv3, vv4):
        """
        
        Remove dummy values from 4 VVs.
        
        :param vv1:  `GXVV <geosoft.gxapi.GXVV>` object
        :param vv2:  `GXVV <geosoft.gxapi.GXVV>` object
        :param vv3:  `GXVV <geosoft.gxapi.GXVV>` object
        :param vv4:  `GXVV <geosoft.gxapi.GXVV>` object
        :type  vv1:  GXVV
        :type  vv2:  GXVV
        :type  vv3:  GXVV
        :type  vv4:  GXVV

        .. versionadded:: 6.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Removes all indices where any `GXVV <geosoft.gxapi.GXVV>` has a dummy, or is
        not defined (due to length differences).
        """
        
        gxapi_cy.WrapVVU._remove_dummy4(GXContext._get_tls_geo(), vv1, vv2, vv3, vv4)
        



    @classmethod
    def remove_dup(cls, data_vv, sample_vv, output):
        """
        
        Remove/average duplicate sample pairs from a database.
        
        :param data_vv:    Data `GXVV <geosoft.gxapi.GXVV>`
        :param sample_vv:  Sample Type `GXVV <geosoft.gxapi.GXVV>`
        :param output:     :ref:`VV_DUP`
        :type  data_vv:    GXVV
        :type  sample_vv:  GXVV
        :type  output:     int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Created for duplicate sample handling in `GXCHIMERA <geosoft.gxapi.GXCHIMERA>`. On input,
        a numeric or text `GXVV <geosoft.gxapi.GXVV>` containing data values, and a sample type `GXVV <geosoft.gxapi.GXVV>`.
        Sample pairs have types "1" and "2". This routine searches for
        types in order "1 2 1 2", and replaces the pair of values in the
        data `GXVV <geosoft.gxapi.GXVV>` according to the :ref:`VV_DUP` value.
        Results for samples out of order, for unmatched pairs, or when the
        sample type does not equal "1" or "2" remain unchanged.
        """
        
        gxapi_cy.WrapVVU._remove_dup(GXContext._get_tls_geo(), data_vv, sample_vv, output)
        



    @classmethod
    def remove_xy_dup(cls, xvv, yvv, zvv, xy_dup):
        """
        
        Remove/average duplicate samples with the same (X, Y).
        
        :param xvv:     X `GXVV <geosoft.gxapi.GXVV>`
        :param yvv:     Y `GXVV <geosoft.gxapi.GXVV>`
        :param zvv:     (optional) Z `GXVV <geosoft.gxapi.GXVV>`
        :param xy_dup:  :ref:`VV_XYDUP`
        :type  xvv:     GXVV
        :type  yvv:     GXVV
        :type  zvv:     GXVV
        :type  xy_dup:  int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Searches for duplicated (X, Y) locations and removes the
        duplicates (can be more than just a pair). The "Z" values,
        if defined, are treated according to the value of :ref:`VV_XYDUP`.
        The returned VVs are shortened to the new length, without
        duplicates.
        The Z `GXVV <geosoft.gxapi.GXVV>` can be set to NULL on input, in which case it is ignored.
        """
        
        gxapi_cy.WrapVVU._remove_xy_dup(GXContext._get_tls_geo(), xvv, yvv, zvv, xy_dup)
        



    @classmethod
    def remove_xy_dup_index(cls, xvv, yvv, index_vv):
        """
        
        Remove duplicate samples with the same (X, Y) and update index.
        
        :param xvv:       X `GXVV <geosoft.gxapi.GXVV>`
        :param yvv:       Y `GXVV <geosoft.gxapi.GXVV>`
        :param index_vv:  Index `GXVV <geosoft.gxapi.GXVV>`
        :type  xvv:       GXVV
        :type  yvv:       GXVV
        :type  index_vv:  GXVV

        .. versionadded:: 7.2

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Searches for duplicated (X, Y) locations and removes the
        duplicates (can be more than just a pair). The Index `GXVV <geosoft.gxapi.GXVV>` is
        updated accordingly .i.e if  (X,Y) location of Index[0] == Index[1]
        Index[1] is removed.
        """
        
        gxapi_cy.WrapVVU._remove_xy_dup_index(GXContext._get_tls_geo(), xvv, yvv, index_vv)
        



    @classmethod
    def rolling_stats(cls, vv_i, vv_o, stat, window, shrink):
        """
        
        Calculate a statistic in a rolling window.
        
        :param vv_i:    Input `GXVV <geosoft.gxapi.GXVV>`
        :param vv_o:    Output `GXVV <geosoft.gxapi.GXVV>`
        :param stat:    :ref:`ST_INFO`
        :param window:  Window size (>0, increased to nearest odd value)
        :param shrink:  Shrink window at ends (1:Yes, 0:No)
        :type  vv_i:    GXVV
        :type  vv_o:    GXVV
        :type  stat:    int
        :type  window:  int
        :type  shrink:  int

        .. versionadded:: 5.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** If the input VVs are not REAL, copies are made to
        temporary REALs for processing.

        If the window size is even, it is increased by 1 so that the
        output value is put at the exact center index of the window.

        Statistics are calculated on the values in a window
        surrounding the individual data points.

        By shrinking the window at the ends, one-sided effects can be
        eliminated. For instance, if the data is linear to begin with,
        a rolling mean will not alter the original data.
        However, if the window size is kept constant, then values
        near the ends tend to be pulled up or down.

        With shrinking, the window is shrunk so that it always has the
        same width on both sides of the data point under analysis;
        at the end points the window width is 1, at the next point in
        it is 3, and so on, until the full width is reached.

        The median value is calculated by sorting the valid data in
        the window, then selecting the middle value. If the number
        of valid data points is even, then the average of the two
        central values is returned.

        The mode value is defined as the value which occurs most
        frequently in the data. This value may not even exist, or
        may not be unique. In this implementation, the following
        algorithm is used: The valid data in the window is sorted
        in ascending order. The number of occurrences of each data
        value is tracked, and if it occurs more times than any
        value, it becomes the modal value. If all
        values are different, this procedure returns the smallest
        value. If two or more values each have the same (maximum)
        number of occurrences, then the smallest of these values is
        returned.
        """
        
        gxapi_cy.WrapVVU._rolling_stats(GXContext._get_tls_geo(), vv_i, vv_o, stat, window, shrink)
        



    @classmethod
    def search_replace(cls, vv, val, rpl):
        """
        
        Search and replace numeric values in a `GXVV <geosoft.gxapi.GXVV>`.
        
        :param val:  Value to replace
        :param rpl:  Replacement
        :type  vv:   GXVV
        :type  val:  float
        :type  rpl:  float

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Search comparison is made on double comparison
        of the data.

        .. seealso::

            SearchReplaceText_VV
        """
        
        gxapi_cy.WrapVVU._search_replace(GXContext._get_tls_geo(), vv, val, rpl)
        



    @classmethod
    def search_replace_text(cls, vv, format, decimal, val, rpl, mode):
        """
        
        Search and replace text values in a `GXVV <geosoft.gxapi.GXVV>`
        
        :param format:   String format for numeric `GXVV <geosoft.gxapi.GXVV>`
        :param decimal:  Decimals for formating numeric `GXVV <geosoft.gxapi.GXVV>`
        :param val:      Formatted string to replace
        :param rpl:      Replacement
        :param mode:     :ref:`VVU_SRCHREPL_CASE`
        :type  vv:       GXVV
        :type  format:   int
        :type  decimal:  int
        :type  val:      str
        :type  rpl:      str
        :type  mode:     int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Search comparison is made on string comparison
        of the data.

        .. seealso::

            SearchReplace_VV
        """
        
        gxapi_cy.WrapVVU._search_replace_text(GXContext._get_tls_geo(), vv, format, decimal, val.encode(), rpl.encode(), mode)
        



    @classmethod
    def search_replace_text_ex(cls, vv, format, decimal, val, rpl, mode, items):
        """
        
        Search and replace text values in a `GXVV <geosoft.gxapi.GXVV>`, count items changed.
        
        :param format:   String format for numeric `GXVV <geosoft.gxapi.GXVV>`
        :param decimal:  Decimals for formating numeric `GXVV <geosoft.gxapi.GXVV>`
        :param val:      Formatted string to replace
        :param rpl:      Replacement
        :param mode:     :ref:`VVU_SRCHREPL_CASE`
        :param items:    Number of items replaced (returned)
        :type  vv:       GXVV
        :type  format:   int
        :type  decimal:  int
        :type  val:      str
        :type  rpl:      str
        :type  mode:     int
        :type  items:    int_ref

        .. versionadded:: 6.0.1

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Search comparison is made on a string comparison
        of the data.

        .. seealso::

            SearchReplaceText_VV
        """
        
        items.value = gxapi_cy.WrapVVU._search_replace_text_ex(GXContext._get_tls_geo(), vv, format, decimal, val.encode(), rpl.encode(), mode, items.value)
        



    @classmethod
    def spline(cls, vv_x, vv_y, vv_o, length, start, incr, gap, ext, type):
        """
        
        Spline a Y `GXVV <geosoft.gxapi.GXVV>` onto an X `GXVV <geosoft.gxapi.GXVV>`.
        
        :param vv_x:    X (no dummies)
        :param vv_y:    Y to be splined (no dummies)
        :param vv_o:    Y output
        :param length:  Output Length
        :param start:   Starting Location
        :param incr:    Separation Distance
        :param gap:     Maximum gap to interpolate across
        :param ext:     Number of elements to extend
        :param type:    :ref:`VVU_SPL`
        :type  vv_x:    GXVV
        :type  vv_y:    GXVV
        :type  vv_o:    GXVV
        :type  length:  int
        :type  start:   float
        :type  incr:    float
        :type  gap:     float
        :type  ext:     int
        :type  type:    int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        gxapi_cy.WrapVVU._spline(GXContext._get_tls_geo(), vv_x, vv_y, vv_o, length, start, incr, gap, ext, type)
        



    @classmethod
    def spline2(cls, vv_x, vv_y, vv_x2, vv_o, type):
        """
        
        Spline a Y `GXVV <geosoft.gxapi.GXVV>` onto an X `GXVV <geosoft.gxapi.GXVV>`. Uses specified values of X in X2
        
        :param vv_x:   X (no dummies)
        :param vv_y:   Y to be splined (no dummies)
        :param vv_x2:  X2 (no dummies)
        :param vv_o:   Y output
        :param type:   :ref:`VVU_SPL`
        :type  vv_x:   GXVV
        :type  vv_y:   GXVV
        :type  vv_x2:  GXVV
        :type  vv_o:   GXVV
        :type  type:   int

        .. versionadded:: 5.1.3

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_
        """
        
        gxapi_cy.WrapVVU._spline2(GXContext._get_tls_geo(), vv_x, vv_y, vv_x2, vv_o, type)
        



    @classmethod
    def tokenize_to_values(cls, vv, str_val):
        """
        
        Tokenize a string based on any characters.
        
        :param vv:       `GXVV <geosoft.gxapi.GXVV>` to place values in
        :param str_val:  Str - String to parse
        :type  vv:       GXVV
        :type  str_val:  str

        :returns:        Number of tokens (length of `GXVV <geosoft.gxapi.GXVV>`)
        :rtype:          int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Parses a series of space, tab or comma-delimited values to a `GXVV <geosoft.gxapi.GXVV>`.
        """
        
        ret_val = gxapi_cy.WrapVVU._tokenize_to_values(GXContext._get_tls_geo(), vv, str_val.encode())
        return ret_val



    @classmethod
    def translate(cls, vv, base, mult):
        """
        
        Translate values in a `GXVV <geosoft.gxapi.GXVV>`
        
        :param base:  Base
        :param mult:  Scale
        :type  vv:    GXVV
        :type  base:  float
        :type  mult:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** (new `GXVV <geosoft.gxapi.GXVV>`) = ((old `GXVV <geosoft.gxapi.GXVV>`) + base) * scale
        """
        
        gxapi_cy.WrapVVU._translate(GXContext._get_tls_geo(), vv, base, mult)
        



    @classmethod
    def trend(cls, vv_d, order, vv_c):
        """
        
        Calculate an n'th order best-fit polynomial, integral x.
        
        :param vv_d:   `GXVV <geosoft.gxapi.GXVV>` with input data
        :param order:  Order of the polynomial 0-9
        :param vv_c:   `GXVV <geosoft.gxapi.GXVV>` to hold polynomial coefficients (returned).
        :type  vv_d:   GXVV
        :type  order:  int
        :type  vv_c:   GXVV

        .. versionadded:: 5.0.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Returns coefficients c[0] .. c[n]

           Y(x) = c[0] + c[1]x + c[2](x**2) + ... + c[n](x**n)

        The X scale is unitless (1 per element), i.e. 0,1,2,3,...

        The polynomial `GXVV <geosoft.gxapi.GXVV>` length is set to the number of coefficients
        (order + 1)

        .. seealso::

            `poly_fill <geosoft.gxapi.GXVVU.poly_fill>`, `trend2 <geosoft.gxapi.GXVVU.trend2>`, `poly_fill2 <geosoft.gxapi.GXVVU.poly_fill2>`
        """
        
        gxapi_cy.WrapVVU._trend(GXContext._get_tls_geo(), vv_d, order, vv_c)
        



    @classmethod
    def trend2(cls, vv_x, vv_d, order, vv_c):
        """
        
        Calculate an n'th order best-fit polynomial, specified X
        
        :param vv_x:   `GXVV <geosoft.gxapi.GXVV>` with x spacing (input)
        :param vv_d:   `GXVV <geosoft.gxapi.GXVV>` with input data
        :param order:  Order of the polynomial 0-9
        :param vv_c:   `GXVV <geosoft.gxapi.GXVV>` to hold polynomial coefficients (returned)
        :type  vv_x:   GXVV
        :type  vv_d:   GXVV
        :type  order:  int
        :type  vv_c:   GXVV

        .. versionadded:: 5.0.6

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Returns coefficients c[0] .. c[n]

           Y(x) = c[0] + c[1]x + c[2](x**2) + ... + c[n](x**n)

        The X scale is defined by a X `GXVV <geosoft.gxapi.GXVV>` (see Trend_VV for unitless X).

        The polynomial `GXVV <geosoft.gxapi.GXVV>` length is set to the number of coefficients
        (order + 1)

        .. seealso::

            `poly_fill <geosoft.gxapi.GXVVU.poly_fill>`, `trend2 <geosoft.gxapi.GXVVU.trend2>`, `poly_fill2 <geosoft.gxapi.GXVVU.poly_fill2>`
        """
        
        gxapi_cy.WrapVVU._trend2(GXContext._get_tls_geo(), vv_x, vv_d, order, vv_c)
        



    @classmethod
    def uniform_dist(cls, vv, seed, min, max, length):
        """
        
        Fill with uniformly distributed values.
        
        :param vv:      `GXVV <geosoft.gxapi.GXVV>` object
        :param seed:    Random number generator seed
        :param min:     Minimum of range
        :param max:     Maximum of range
        :param length:  Number of values (-1 for all)
        :type  vv:      GXVV
        :type  seed:    int
        :type  min:     float
        :type  max:     float
        :type  length:  int

        .. versionadded:: 5.1.8

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** `GXVV <geosoft.gxapi.GXVV>` is set to input length (except for -1)
        See rand.gxh for a short discription of the
        random number generator used.
        """
        
        gxapi_cy.WrapVVU._uniform_dist(GXContext._get_tls_geo(), vv, seed, min, max, length)
        




# Deprecated


    @classmethod
    def offset_correct4(cls, vv_xi, vv_yi, vv_zi, zoffset, dist, azimuth, interval, vv_roll, vv_pitch, vv_yaw, vv_xo, vv_yo, vv_zo):
        """
        
        .. deprecated:: None None 
        Same as `offset_correct3 <geosoft.gxapi.GXVVU.offset_correct3>`, but specify roll, pitch, yaw and Z.
        
        :param vv_xi:     Input X
        :param vv_yi:     Input Y
        :param vv_zi:     Input Z
        :param zoffset:   ZOffset distance
        :param dist:      XYOffset distance
        :param azimuth:   XYOffset azimuth (degrees clockwise from straight ahead)
        :param interval:  Averaging interval - `rDUMMY <geosoft.gxapi.rDUMMY>` for default
        :param vv_roll:   Roll
        :param vv_pitch:  Pitch
        :param vv_yaw:    Yaw
        :param vv_xo:     Output X
        :param vv_yo:     Output Y
        :param vv_zo:     Output Z
        :type  vv_xi:     GXVV
        :type  vv_yi:     GXVV
        :type  vv_zi:     GXVV
        :type  zoffset:   float
        :type  dist:      float
        :type  azimuth:   float
        :type  interval:  float
        :type  vv_roll:   GXVV
        :type  vv_pitch:  GXVV
        :type  vv_yaw:    GXVV
        :type  vv_xo:     GXVV
        :type  vv_yo:     GXVV
        :type  vv_zo:     GXVV

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Add roll, pitch, yaw correction.
        """
        warnings.warn("""Deprecated since unknown, """, )
        gxapi_cy.WrapVVU._offset_correct4(GXContext._get_tls_geo(), vv_xi, vv_yi, vv_zi, zoffset, dist, azimuth, interval, vv_roll, vv_pitch, vv_yaw, vv_xo, vv_yo, vv_zo)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer