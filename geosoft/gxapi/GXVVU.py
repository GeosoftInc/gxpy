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
class GXVVU:
    """
    GXVVU class.

    These methods are not a class. Utility methods perform
    various operations on `GXVV` objects, including pruning,
    splining, clipping and filtering.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVVU(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVVU`
        
        :returns: A null `GXVVU`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXVVU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXVVU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def average_repeat(cls, ref_vv, dat_vv):
        """
        Average repeat values.

        **Note:**

        Repeated values in the reference `GXVV` will be averaged
        in the data `GXVV`.  The first value in the data `GXVV` will be set to the
        average and subsequent data `GXVV` values will be dummied out.
        Data is processed only to the minimum length of the
        input `GXVV` lengths.

        .. seealso::

            `remove_dummy`
        """
        gxapi_cy.WrapVVU.average_repeat(GXContext._get_tls_geo(), ref_vv._wrapper, dat_vv._wrapper)
        



    @classmethod
    def average_repeat_ex(cls, ref_vv, dat_vv, mode):
        """
        Average repeat values.

        **Note:**

        Repeated values in the reference `GXVV` will be set to the mean, median, minimum or maximum value
        in the data `GXVV`.  For minimum and maximum, the index in the data `GXVV` containing the minimum or maximum value
        is retained, and the other repeated values are dummied out. For mean and median, the first value in the 
        data `GXVV` will be reset and subsequent data `GXVV` values will be dummied out.
        Data is processed only to the minimum length of the
        input `GXVV` lengths.

        .. seealso::

            `remove_dummy`
        """
        gxapi_cy.WrapVVU.average_repeat_ex(GXContext._get_tls_geo(), ref_vv._wrapper, dat_vv._wrapper, mode)
        



    @classmethod
    def average_repeat2(cls, ref_vv1, ref_vv2, dat_vv):
        """
        Average repeat values based on 2 reference channels.

        **Note:**

        Repeated values in the reference `GXVV` will be averaged
        in the data `GXVV`.  The first value in the data `GXVV` will be set to the
        average and subsequent data `GXVV` values will be dummied out.
        Data is processed only to the minimum length of the
        input `GXVV` lengths.
        Both the reference `GXVV` values must repeat for the averaging
        to occur. This version is useful for averaging on repeated
        (X,Y) locations.

        .. seealso::

            RemoveDummy_VV
        """
        gxapi_cy.WrapVVU.average_repeat2(GXContext._get_tls_geo(), ref_vv1._wrapper, ref_vv2._wrapper, dat_vv._wrapper)
        



    @classmethod
    def average_repeat2_ex(cls, ref_vv1, ref_vv2, dat_vv, mode):
        """
        Average repeat values based on 2 reference channels.

        **Note:**

        Repeated values in the reference `GXVV` will be set to the mean, median, minimum or maximum value
        in the data `GXVV`.  The first value in the data `GXVV` will be reset and subsequent data `GXVV` values will be dummied out.
        Data is processed only to the minimum length of the
        input `GXVV` lengths.
        Both the reference `GXVV` values must repeat for the averaging
        to occur. This version is useful for averaging on repeated
        (X,Y) locations.

        .. seealso::

            RemoveDummy_VV
        """
        gxapi_cy.WrapVVU.average_repeat2_ex(GXContext._get_tls_geo(), ref_vv1._wrapper, ref_vv2._wrapper, dat_vv._wrapper, mode)
        



    @classmethod
    def binary_search(cls, vv, val, l_min, l_max):
        """
        Search  numeric value in a `GXVV`.

        **Note:**

        The `GXVV` should be sorted.Search comparison is made on double
        comparison of the data.
        """
        l_min.value, l_max.value = gxapi_cy.WrapVVU.binary_search(GXContext._get_tls_geo(), vv._wrapper, val, l_min.value, l_max.value)
        



    @classmethod
    def box_cox(cls, vv, lm):
        """
        Run Box-Cox (lambda) Transformation on `GXVV`.
        """
        gxapi_cy.WrapVVU.box_cox(GXContext._get_tls_geo(), vv._wrapper, lm)
        



    @classmethod
    def bp_filt(cls, vv_i, vv_o, pr_sw, pr_lw, flen):
        """
        Band-pass filter to the specified.

        **Note:**

        If the short and long wavelengths are <= 0, the input channel
        is simply copied to the output channel without filtering.
        
        The wavelengths are in fiducials.
        """
        gxapi_cy.WrapVVU.bp_filt(GXContext._get_tls_geo(), vv_i._wrapper, vv_o._wrapper, pr_sw, pr_lw, flen)
        



    @classmethod
    def clip(cls, vv, min, max, clip):
        """
        Clip a `GXVV` to a range.
        """
        gxapi_cy.WrapVVU.clip(GXContext._get_tls_geo(), vv._wrapper, min, max, clip)
        



    @classmethod
    def clip_to_detect_limit(cls, vv, det_limit, conv):
        """
        Apply detection limit clipping of data.

        **Note:**

        Flow:
        
        1. If auto-converting negatives, then all negative values
            are replaced by -0.5*value, and detection limit is ignored.
        
        2. If not auto-converting negatives, and the detection limit is not
           `rDUMMY`, then values less than the detection limit are converted to
           one-half the detection limit.
        
        This function is identical to `GXCHIMERA.clip_to_detect_limit`.
        """
        gxapi_cy.WrapVVU.clip_to_detect_limit(GXContext._get_tls_geo(), vv._wrapper, det_limit, conv)
        



    @classmethod
    def decimate(cls, vv, decimate):
        """
        Decimate a `GXVV`.

        **Note:**

        For a decimation factor N, will remove all values except
        those with indices equal to MN, where M is an integer.
        """
        gxapi_cy.WrapVVU.decimate(GXContext._get_tls_geo(), vv._wrapper, decimate)
        



    @classmethod
    def deviation(cls, vv_x, vv_y, vv_d, x1, y1, x2, y2, line):
        """
        Calculate distance of point locations to a straight line
        """
        gxapi_cy.WrapVVU.deviation(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, vv_d._wrapper, x1, y1, x2, y2, line)
        



    @classmethod
    def distance(cls, vv_x, vv_y, vv_d, x_fid_start, x_fid_incr, y_fid_start, y_fid_incr):
        """
        Create a cumulative distance `GXVV`
        """
        gxapi_cy.WrapVVU.distance(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, vv_d._wrapper, x_fid_start, x_fid_incr, y_fid_start, y_fid_incr)
        



    @classmethod
    def distance_non_cumulative(cls, vv_x, vv_y, vv_d, x_fid_start, x_fid_incr, y_fid_start, y_fid_incr):
        """
        Create a non cumulative distance `GXVV` i.e each
        distance element is the distance of the corresponding
        (X,Y) element and the previous element.

        **Note:**

        The fist distace element is `rDUMMY`.
        """
        gxapi_cy.WrapVVU.distance_non_cumulative(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, vv_d._wrapper, x_fid_start, x_fid_incr, y_fid_start, y_fid_incr)
        



    @classmethod
    def distance_3d(cls, vv_x, vv_y, vv_z, start_distance, vv_d):
        """
        Create a cumulative distance `GXVV` from X, Y and Z VVs

        **Note:**

        The output `GXVV` is the length of the shortest X,Y or Z input `GXVV`.
        Any values with dummies are ignored - the distance at that
        point is equal to the distance at the previous valid point.
        The returned `GXVV` is the cumulative straight-line distance
        between the points. No re-sampling is performed.
        VVs of any type are supported.
        """
        gxapi_cy.WrapVVU.distance_3d(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, start_distance, vv_d._wrapper)
        



    @classmethod
    def find_gaps_3d(cls, vv_x, vv_y, vv_z, gap, vv_g):
        """
        Return indices of locations separated from previous locations by more than the input gap distance.

        **Note:**

        Locate the starting points of line segements determined by an input gap distance.
        The returned indices indicate where to break the line, given an input gap.
        The number of returned indices is one less than the number of line segments.
        (So if there are no gaps the returned `GXVV` has zero length).
        """
        gxapi_cy.WrapVVU.find_gaps_3d(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, gap, vv_g._wrapper)
        



    @classmethod
    def dummy_range(cls, vv, min, max, inside, incl):
        """
        Dummy values inside or outside a range in a `GXVV`

        **Note:**

        If the Inside flag is TRUE, values within the specified
        range are set to dummy. If the inside flag is FALSE,
        values outside the range are set to dummy.  If the Inclusive
        flag is TRUE, then dMin and dMax are considered part of the
        range. If it is FALSE, then < or > are used, and dMin and
        dMax lie outside the range.
        """
        gxapi_cy.WrapVVU.dummy_range(GXContext._get_tls_geo(), vv._wrapper, min, max, inside, incl)
        



    @classmethod
    def dummy_range_ex(cls, vv, min, max, inside, include_min, include_max):
        """
        Like DummyRangeVVU, with inclusion options for both ends.

        **Note:**

        If the Inside flag is TRUE, values within the specified
        range are set to dummy. If the inside flag is FALSE,
        values outside the range are set to dummy.  If the Inclusive
        flag is TRUE, then dMin and dMax are considered part of the
        range. If it is FALSE, then < or > are used, and dMin and
        dMax lie outside the range.
        """
        gxapi_cy.WrapVVU.dummy_range_ex(GXContext._get_tls_geo(), vv._wrapper, min, max, inside, include_min, include_max)
        



    @classmethod
    def dummy_repeat(cls, vv, mode):
        """
        Dummy repeat values in a `GXVV`.

        **Note:**

        Either the first, middle or last point will be left.
                          Use `interp` to interpolate after if desired.
        """
        gxapi_cy.WrapVVU.dummy_repeat(GXContext._get_tls_geo(), vv._wrapper, mode)
        



    @classmethod
    def dup_stats(cls, data_vv, sample_vv, mean_vv, diff_vv):
        """
        Calculate means and differences for duplicate sample pairs

        **Note:**

        Created for duplicate sample handling in `GXCHIMERA`. On input,
        a numeric `GXVV` containing data values, and a sample type `GXVV`.
        Sample pairs have types "1" and "2". This routine searches for
        types in order "1 2 1 2", and writes the mean values of pairs
        to the mean value `GXVV`, and the differences with the mean (equal
        values, negative and positive) to the difference `GXVV`. Results
        for samples out of order, for unmatched values, or when the
        sample type does not equal "1" or "2" are set to dummy.
        """
        gxapi_cy.WrapVVU.dup_stats(GXContext._get_tls_geo(), data_vv._wrapper, sample_vv._wrapper, mean_vv._wrapper, diff_vv._wrapper)
        



    @classmethod
    def exp_dist(cls, vv, seed, mean, length):
        """
        Fill with exponentially distributed values.

        **Note:**

        `GXVV` is set to input length (except for -1)
        See RAND for a short discription of the
        random number generator used.
        """
        gxapi_cy.WrapVVU.exp_dist(GXContext._get_tls_geo(), vv._wrapper, seed, mean, length)
        



    @classmethod
    def filter(cls, vv_i, vv_o, flt):
        """
        Apply a convolution filter to a `GXVV`.
        """
        gxapi_cy.WrapVVU.filter(GXContext._get_tls_geo(), vv_i._wrapper, vv_o._wrapper, flt)
        



    @classmethod
    def find_string_items(cls, vv_source, vv_search, pis_source_sorted, pis_search_sorted, pis_case_tolerant, vv_i):
        """
        Searches a `GXVV` for items in a second `GXVV`, returns indices of those found.

        **Note:**

        This is a much more efficient way of determining if items in
        one `GXVV` are found in a second, than by searching
        repeatedly in a loop.
        The returned `GS_LONG` `GXVV` contains the same number of items as
        the "search items" `GXVV`, and contains -1 for items where the
        value is not found, and the index of items that are found.
        Comparisons are case-tolerant.
        Non-string VVs are converted to string type VVs (element size 24) internally.
        
        The method requires that the `GXVV` items be sorted, and
        will do so internally. Since the input VVs may already be sorted,
        the method will run faster if this stage can be skipped.
        """
        gxapi_cy.WrapVVU.find_string_items(GXContext._get_tls_geo(), vv_source._wrapper, vv_search._wrapper, pis_source_sorted, pis_search_sorted, pis_case_tolerant, vv_i._wrapper)
        



    @classmethod
    def fractal_filter(cls, vv_i, order, number, vv_o):
        """
        Fractal filter a `GXVV`.
        """
        gxapi_cy.WrapVVU.fractal_filter(GXContext._get_tls_geo(), vv_i._wrapper, order, number, vv_o._wrapper)
        



    @classmethod
    def close_xy(cls, vv_x, vv_y, x, y):
        """
        Find the closest point to an input point (XY).

        **Note:**

        Input X and Y location VVs, and a location.
        Returns the index of the point in the `GXVV` closest to the
        input point.
        """
        ret_val = gxapi_cy.WrapVVU.close_xy(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, x, y)
        return ret_val



    @classmethod
    def close_xym(cls, vv_x, vv_y, vv_m, x, y):
        """
        Find the closest point to an input point, with mask (XY).

        **Note:**

        Input X and Y location VVs, and a location.
        Returns the index of the point in the `GXVV` closest to the
        input point.
        This skips points where the mask value is dummy.
        If no valid points are in the VVs, or all the mask `GXVV` values
        are dummy, the returned index is -1.
        """
        ret_val = gxapi_cy.WrapVVU.close_xym(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, vv_m._wrapper, x, y)
        return ret_val



    @classmethod
    def close_xyz(cls, vv_x, vv_y, vv_z, x, y, z):
        """
        Find the closest point to an input point (XYZ).

        **Note:**

        Input X, Y and Z location VVs, and a location.
        Returns the index of the point in the `GXVV` closest to the
        input point.
        """
        ret_val = gxapi_cy.WrapVVU.close_xyz(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, x, y, z)
        return ret_val



    @classmethod
    def close_xyzm(cls, vv_x, vv_y, vv_z, vv_m, x, y, z):
        """
        Find the closest point to an input point, with mask (XYZ).

        **Note:**

        Input X, Y and Z location VVs, and a location.
        Returns the index of the point in the `GXVV` closest to the
        input point.
        This skips points where the mask value is dummy.
        If no valid points are in the VVs, or all the mask `GXVV` values
        are dummy, the returned index is -1.
        """
        ret_val = gxapi_cy.WrapVVU.close_xyzm(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, vv_z._wrapper, vv_m._wrapper, x, y, z)
        return ret_val



    @classmethod
    def dummy_back_tracks(cls, vv):
        """
        Dummy all points that keep a `GXVV` from being monotonically increasing.

        **Note:**

        The `GXVV` length remains the same. Any point that is less than or equal to
        the previous (valid) point in the `GXVV` is dummied.
        """
        ret_val = gxapi_cy.WrapVVU.dummy_back_tracks(GXContext._get_tls_geo(), vv._wrapper)
        return ret_val



    @classmethod
    def find_dummy(cls, vv, dir, type, start, end):
        """
        Find the first dummy|non-dummy value in `GXVV`

        **Note:**

        Start and end of range are always defined lowest
        to largest even if decreasing search order.  To search
        entire `GXVV` range, specify 0,-1.
        """
        ret_val = gxapi_cy.WrapVVU.find_dummy(GXContext._get_tls_geo(), vv._wrapper, dir, type, start, end)
        return ret_val



    @classmethod
    def interp(cls, vv, input, output):
        """
        Replace all dummies by interpolating from valid data.

        **Note:**

        Edge behaviour
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
        gxapi_cy.WrapVVU.interp(GXContext._get_tls_geo(), vv._wrapper, input, output)
        



    @classmethod
    def qc_fill_gaps(cls, vvx, vvy, vvf, vvd, dist):
        """
        Calculate fill in line segments

        **Note:**

        The X & Y VVs are returned as the calculated fill in line segments.
        """
        ret_val = gxapi_cy.WrapVVU.qc_fill_gaps(GXContext._get_tls_geo(), vvx._wrapper, vvy._wrapper, vvf._wrapper, vvd._wrapper, dist)
        return ret_val



    @classmethod
    def search_text(cls, vv, text, case, match, start, dir):
        """
        Search for a text value in a `GXVV`

        **Note:**

        Search comparison is made on string comparison
        of the data. Returns index of first item matching
        the input string.
        If start index is -1 or dummy, then full `GXVV` is searched.
        Use `VVU_MATCH_INPUT_LENGTH` to match the first part of a string.
        This is also recommended for matching numerical values, since
        the displayed value in the database may not be the same as the
        stored value.

        .. seealso::

            sSearchReplace_VV
        """
        ret_val = gxapi_cy.WrapVVU.search_text(GXContext._get_tls_geo(), vv._wrapper, text.encode(), case, match, start, dir)
        return ret_val



    @classmethod
    def mask(cls, vv_d, vv_m):
        """
        Mask dummies in one `GXVV` onto another.

        **Note:**

        `GXVV` to mask will be resampled to reference `GXVV` if required.
        The returned length of the `GXVV` to mask will be the shorter
        of the reference `GXVV` or the mask `GXVV`.
        """
        gxapi_cy.WrapVVU.mask(GXContext._get_tls_geo(), vv_d._wrapper, vv_m._wrapper)
        



    @classmethod
    def mask_and(cls, vv_a, vv_b, vv_c):
        """
        Create mask from logical AND of two VVs.

        **Note:**

        If both values are non-dummies, then result is 1, else dummy.
        """
        gxapi_cy.WrapVVU.mask_and(GXContext._get_tls_geo(), vv_a._wrapper, vv_b._wrapper, vv_c._wrapper)
        



    @classmethod
    def mask_or(cls, vv_a, vv_b, vv_c):
        """
        Create mask from logical OR of two VVs.

        **Note:**

        If either values is non-dummy, then result is 1, else dummy.
        """
        gxapi_cy.WrapVVU.mask_or(GXContext._get_tls_geo(), vv_a._wrapper, vv_b._wrapper, vv_c._wrapper)
        



    @classmethod
    def nl_filt(cls, vv_i, vv_o, fwid, pr_ftol):
        """
        Applies a non-linear filter.
        """
        gxapi_cy.WrapVVU.nl_filt(GXContext._get_tls_geo(), vv_i._wrapper, vv_o._wrapper, fwid, pr_ftol)
        



    @classmethod
    def noise_check(cls, vv_i, vv_f, all_tol, num):
        """
        Check on deviation of data from variable background in a `GXVV`

        **Note:**

        This function checks vertical deviation of data in input `GXVV`
        against a moving straight line. The straight line at any time is
        defined by two extreme points of a data segment.  Output `GXVV` will
        be 0 if data point in input `GXVV` falls within the deviation,
        otherwise, it will be 1.
        Output `GXVV` will be 0 if the straight line is vertical.
        """
        gxapi_cy.WrapVVU.noise_check(GXContext._get_tls_geo(), vv_i._wrapper, vv_f._wrapper, all_tol, num)
        



    @classmethod
    def noise_check2(cls, vv_i, vv_f, vv_d, all_tol, num):
        """
        Like `noise_check`, but returns maximum deviation at all points.

        **Note:**

        This function checks vertical deviation of data in an input `GXVV`
        against a moving straight line, where the X-axis value is
        taken to be the data index, and the Y-axis value is the
        input data `GXVV` value. The straight line is drawn between data points
        at the ends of the line segment, whose length is an input.
        
        The output flag `GXVV` is set to 0 if data point in input `GXVV` falls within the
        deviation for all the moving line segments of which it is a part, otherwise, it
        will be set to 1.
        
        The output maximum deviation `GXVV` contains the maximum deviation at each point
        for all the moving line segments that it is a part of.
        """
        gxapi_cy.WrapVVU.noise_check2(GXContext._get_tls_geo(), vv_i._wrapper, vv_f._wrapper, vv_d._wrapper, all_tol, num)
        



    @classmethod
    def normal_dist(cls, vv, seed, mean, var, length):
        """
        Fill with normally (Gaussian) distributed values.

        **Note:**

        `GXVV` is set to input length (except for -1)
        See RAND for a short discription of the
        random number generator used.
        """
        gxapi_cy.WrapVVU.normal_dist(GXContext._get_tls_geo(), vv._wrapper, seed, mean, var, length)
        



    @classmethod
    def offset_circles(cls, vv_xi, vv_yi, offset, radius, vv_xo, vv_yo):
        """
        Get non-overlapping offset location for circular symbols.

        **Note:**

        Often on maps plotted symbols and text overlap each other.
        This routine accepts of `GXVV` of locations and returns a new
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
        gxapi_cy.WrapVVU.offset_circles(GXContext._get_tls_geo(), vv_xi._wrapper, vv_yi._wrapper, offset, radius, vv_xo._wrapper, vv_yo._wrapper)
        



    @classmethod
    def offset_correct(cls, vv_xi, vv_yi, dist, heading, v_vxo, v_vyo):
        """
        Correct locations based on heading and fixed offset.

        **Note:**

        In many applications, measurements are taken with an instrument which
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
        gxapi_cy.WrapVVU.offset_correct(GXContext._get_tls_geo(), vv_xi._wrapper, vv_yi._wrapper, dist, heading, v_vxo._wrapper, v_vyo._wrapper)
        



    @classmethod
    def offset_correct2(cls, vv_xi, vv_yi, dist, azimuth, vv_xo, vv_yo):
        """
        Same as `offset_correct`, but for an arbitrary offset angle.
        """
        gxapi_cy.WrapVVU.offset_correct2(GXContext._get_tls_geo(), vv_xi._wrapper, vv_yi._wrapper, dist, azimuth, vv_xo._wrapper, vv_yo._wrapper)
        



    @classmethod
    def offset_correct3(cls, vv_xi, vv_yi, dist, azimuth, interval, vv_xo, vv_yo):
        """
        Same as `offset_correct2`, but specify smoothing interval.

        **Note:**

        See the algorithm note #2 above for the default smoothing interval.
        """
        gxapi_cy.WrapVVU.offset_correct3(GXContext._get_tls_geo(), vv_xi._wrapper, vv_yi._wrapper, dist, azimuth, interval, vv_xo._wrapper, vv_yo._wrapper)
        



    @classmethod
    def offset_correct_xyz(cls, vv_xi, vv_yi, vv_zi, x_off, y_off, z_off, interval, v_vxo, v_vyo, v_vzo):
        """
        Correct locations based on heading and fixed offset.

        **Note:**

        In many applications, measurements are taken with an instrument which
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
        gxapi_cy.WrapVVU.offset_correct_xyz(GXContext._get_tls_geo(), vv_xi._wrapper, vv_yi._wrapper, vv_zi._wrapper, x_off, y_off, z_off, interval, v_vxo._wrapper, v_vyo._wrapper, v_vzo._wrapper)
        



    @classmethod
    def offset_rectangles(cls, vv_xi, vv_yi, offset, size_x, size_y, vv_xo, vv_yo):
        """
        Get non-overlapping offset location for rectangular symbols.

        **Note:**

        Often on maps plotted symbols and text overlap each other.
        This routine accepts of `GXVV` of locations and returns a new
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
        gxapi_cy.WrapVVU.offset_rectangles(GXContext._get_tls_geo(), vv_xi._wrapper, vv_yi._wrapper, offset, size_x, size_y, vv_xo._wrapper, vv_yo._wrapper)
        



    @classmethod
    def pick_peak(cls, vv_i, vv_o, pr_tol, width):
        """
        Find peaks in a `GXVV` - method one.

        **Note:**

        Peaks are the maximum point within a sequence of
        positive values in the input `GXVV`.  The width is the
        number of points in the positive sequence.
        
        A `GXVV` may have to be pre-filtered before finding
        the peak values:
        
        Use `bp_filt` to smooth the data as required.
        Use `filter` to apply a Laplace filter
        "-0.5,1.0,-0.5" to make curvature data.
        """
        gxapi_cy.WrapVVU.pick_peak(GXContext._get_tls_geo(), vv_i._wrapper, vv_o._wrapper, pr_tol, width)
        



    @classmethod
    def pick_peak2(cls, vv_i, vv_o, pr_base_lvl, pr_ampl):
        """
        Find peaks in a `GXVV` - method two.

        **Note:**

        Peaks are the maximum point within a sequence of
        values in the input `GXVV`. Maximum points must be above
        the base level and have a local amplitude greater
        than the minimum amplitude specified.
        
        A `GXVV` may have to be pre-filtered before finding
        the peak values.
        """
        gxapi_cy.WrapVVU.pick_peak2(GXContext._get_tls_geo(), vv_i._wrapper, vv_o._wrapper, pr_base_lvl, pr_ampl)
        



    @classmethod
    def pick_peak3(cls, vv_i, vv_x, vv_y, pr_base_lvl, pr_ampl, v_vind, v_vamp, v_vwid, v_vhawid):
        """
        Find peaks in a `GXVV` - method two, returning width and half-amplitude widths.

        **Note:**

        Uses Method 2 above, but also returns the anomaly width (defined
        as the distance between the surrounding troughs), and the
        width at the half-amplitude. The half-amplitude width is
        calculated in two parts, individually for each side based on
        the distance from the maximum to the location where the
        amplitude is mid-way between the maximum and trough.
        
        The returned VVs are packed; no dummies. Instead the
        indicies of the peak locations are returned.
        """
        gxapi_cy.WrapVVU.pick_peak3(GXContext._get_tls_geo(), vv_i._wrapper, vv_x._wrapper, vv_y._wrapper, pr_base_lvl, pr_ampl, v_vind._wrapper, v_vamp._wrapper, v_vwid._wrapper, v_vhawid._wrapper)
        



    @classmethod
    def poly_fill(cls, vv_d, order, vv_c):
        """
        Fill a `GXVV` with values from an n'th order polynomial, integral x.

        **Note:**

        The output `GXVV` length must be set as desired before calling.
        
        The X scale is unitless (1 per element), i.e. 0,1,2,3,...

        .. seealso::

            `trend`, `trend2`, `poly_fill2`
        """
        gxapi_cy.WrapVVU.poly_fill(GXContext._get_tls_geo(), vv_d._wrapper, order, vv_c._wrapper)
        



    @classmethod
    def poly_fill2(cls, vv_x, vv_d, order, vv_c):
        """
        Fill a `GXVV` with values from an n'th order polynomial, specified X

        **Note:**

        The output `GXVV` length must be set as desired before calling.
        The X scale is defined by a X `GXVV` (see Trend_VV for unitless X).

        .. seealso::

            `trend`, `trend2`, `poly_fill`
        """
        gxapi_cy.WrapVVU.poly_fill2(GXContext._get_tls_geo(), vv_x._wrapper, vv_d._wrapper, order, vv_c._wrapper)
        



    @classmethod
    def polygon_mask(cls, vv_x, vv_y, vv_m, pply, mask):
        """
        Mask a `GXVV` using XY data and a polygon.

        **Note:**

        The VVs have to be the same length
        """
        gxapi_cy.WrapVVU.polygon_mask(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, vv_m._wrapper, pply._wrapper, mask)
        



    @classmethod
    def prune(cls, vv_p, vv_r, o):
        """
        Prune values from a `GXVV` based on reference `GXVV`

        **Note:**

        Pruning will shorten the `GXVV` by removing values
        that are either dummy or non-dummy in the reference
        `GXVV`
        """
        gxapi_cy.WrapVVU.prune(GXContext._get_tls_geo(), vv_p._wrapper, vv_r._wrapper, o)
        



    @classmethod
    def qc(cls, vv_i, vv_d, v_vf, nominal, max_tol, all_tol, dist, qc):
        """
        Quality control on deviation of data from norm in a `GXVV`

        **Note:**

        This function tests data in input `GXVV` against
        two separate criteria. Each element of the output `GXVV`
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
        gxapi_cy.WrapVVU.qc(GXContext._get_tls_geo(), vv_i._wrapper, vv_d._wrapper, v_vf._wrapper, nominal, max_tol, all_tol, dist, qc)
        



    @classmethod
    def range_vector_mag(cls, vv1, vv2, min, max):
        """
        Find the range of hypotenuse values of two VVs.

        **Note:**

        For each value in the VVs, finds sqrt(dV1*dV1 + dV2*dV2)
        and returns the min and max values.
        """
        min.value, max.value = gxapi_cy.WrapVVU.range_vector_mag(GXContext._get_tls_geo(), vv1._wrapper, vv2._wrapper, min.value, max.value)
        



    @classmethod
    def regress(cls, vv_x, vv_y, slp, int):
        """
        Calculate linear regression through data
        """
        slp.value, int.value = gxapi_cy.WrapVVU.regress(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, slp.value, int.value)
        



    @classmethod
    def rel_var_dup(cls, data_vv, sample_vv, rel_var, num_dup):
        """
        Estimate relative variance of duplicate sample pairs from a database.

        **Note:**

        Created for duplicate sample handling in `GXCHIMERA`. On input,
        a numeric or text `GXVV` containing data values, and a sample type `GXVV`.
        Sample pairs have types "1" and "2". This routine searches for
        types in order "1 2 1 2", and calulates the unnormalized relative variance,
        defined as the sum of the squared differences between duplicates
        divided by the sum of the squared mean values of the duplicates.
        (To get the true rel.var., divide by N-1, where N is the number of
        duplicate pairs used.)
        Samples out of order, unmatched pairs, or when the
        sample type does not equal "1" or "2" are ignored.
        """
        rel_var.value, num_dup.value = gxapi_cy.WrapVVU.rel_var_dup(GXContext._get_tls_geo(), data_vv._wrapper, sample_vv._wrapper, rel_var.value, num_dup.value)
        



    @classmethod
    def remove_dummy(cls, vv):
        """
        Remove dummy values from a `GXVV`
        """
        gxapi_cy.WrapVVU.remove_dummy(GXContext._get_tls_geo(), vv._wrapper)
        



    @classmethod
    def remove_dummy2(cls, vv1, vv2):
        """
        Remove dummy values from 2 VVs.

        **Note:**

        Removes all indices where either `GXVV` has a dummy, or is
        not defined (due to length differences).
        """
        gxapi_cy.WrapVVU.remove_dummy2(GXContext._get_tls_geo(), vv1._wrapper, vv2._wrapper)
        



    @classmethod
    def remove_dummy3(cls, vv1, vv2, vv3):
        """
        Remove dummy values from 3 VVs.

        **Note:**

        Removes all indices where any `GXVV` has a dummy, or is
        not defined (due to length differences).
        """
        gxapi_cy.WrapVVU.remove_dummy3(GXContext._get_tls_geo(), vv1._wrapper, vv2._wrapper, vv3._wrapper)
        



    @classmethod
    def remove_dummy4(cls, vv1, vv2, vv3, vv4):
        """
        Remove dummy values from 4 VVs.

        **Note:**

        Removes all indices where any `GXVV` has a dummy, or is
        not defined (due to length differences).
        """
        gxapi_cy.WrapVVU.remove_dummy4(GXContext._get_tls_geo(), vv1._wrapper, vv2._wrapper, vv3._wrapper, vv4._wrapper)
        



    @classmethod
    def remove_dup(cls, data_vv, sample_vv, output):
        """
        Remove/average duplicate sample pairs from a database.

        **Note:**

        Created for duplicate sample handling in `GXCHIMERA`. On input,
        a numeric or text `GXVV` containing data values, and a sample type `GXVV`.
        Sample pairs have types "1" and "2". This routine searches for
        types in order "1 2 1 2", and replaces the pair of values in the
        data `GXVV` according to the `VV_DUP` value.
        Results for samples out of order, for unmatched pairs, or when the
        sample type does not equal "1" or "2" remain unchanged.
        """
        gxapi_cy.WrapVVU.remove_dup(GXContext._get_tls_geo(), data_vv._wrapper, sample_vv._wrapper, output)
        



    @classmethod
    def remove_xy_dup(cls, xvv, yvv, zvv, xy_dup):
        """
        Remove/average duplicate samples with the same (X, Y).

        **Note:**

        Searches for duplicated (X, Y) locations and removes the
        duplicates (can be more than just a pair). The "Z" values,
        if defined, are treated according to the value of `VV_XYDUP`.
        The returned VVs are shortened to the new length, without
        duplicates.
        The Z `GXVV` can be set to NULL on input, in which case it is ignored.
        """
        gxapi_cy.WrapVVU.remove_xy_dup(GXContext._get_tls_geo(), xvv._wrapper, yvv._wrapper, zvv._wrapper, xy_dup)
        



    @classmethod
    def remove_xy_dup_index(cls, xvv, yvv, index_vv):
        """
        Remove duplicate samples with the same (X, Y) and update index.

        **Note:**

        Searches for duplicated (X, Y) locations and removes the
        duplicates (can be more than just a pair). The Index `GXVV` is
        updated accordingly .i.e if  (X,Y) location of Index[0] == Index[1]
        Index[1] is removed.
        """
        gxapi_cy.WrapVVU.remove_xy_dup_index(GXContext._get_tls_geo(), xvv._wrapper, yvv._wrapper, index_vv._wrapper)
        



    @classmethod
    def rolling_stats(cls, vv_i, vv_o, stat, window, shrink):
        """
        Calculate a statistic in a rolling window.

        **Note:**

        If the input VVs are not REAL, copies are made to
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
        gxapi_cy.WrapVVU.rolling_stats(GXContext._get_tls_geo(), vv_i._wrapper, vv_o._wrapper, stat, window, shrink)
        



    @classmethod
    def search_replace(cls, vv, val, rpl):
        """
        Search and replace numeric values in a `GXVV`.

        **Note:**

        Search comparison is made on double comparison
        of the data.

        .. seealso::

            SearchReplaceText_VV
        """
        gxapi_cy.WrapVVU.search_replace(GXContext._get_tls_geo(), vv._wrapper, val, rpl)
        



    @classmethod
    def search_replace_text(cls, vv, format, decimal, val, rpl, mode):
        """
        Search and replace text values in a `GXVV`

        **Note:**

        Search comparison is made on string comparison
        of the data.

        .. seealso::

            SearchReplace_VV
        """
        gxapi_cy.WrapVVU.search_replace_text(GXContext._get_tls_geo(), vv._wrapper, format, decimal, val.encode(), rpl.encode(), mode)
        



    @classmethod
    def search_replace_text_ex(cls, vv, format, decimal, val, rpl, mode, items):
        """
        Search and replace text values in a `GXVV`, count items changed.

        **Note:**

        Search comparison is made on a string comparison
        of the data.

        .. seealso::

            SearchReplaceText_VV
        """
        items.value = gxapi_cy.WrapVVU.search_replace_text_ex(GXContext._get_tls_geo(), vv._wrapper, format, decimal, val.encode(), rpl.encode(), mode, items.value)
        



    @classmethod
    def spline(cls, vv_x, vv_y, vv_o, length, start, incr, gap, ext, type):
        """
        Spline a Y `GXVV` onto an X `GXVV`.
        """
        gxapi_cy.WrapVVU.spline(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, vv_o._wrapper, length, start, incr, gap, ext, type)
        



    @classmethod
    def spline2(cls, vv_x, vv_y, vv_x2, vv_o, type):
        """
        Spline a Y `GXVV` onto an X `GXVV`. Uses specified values of X in X2
        """
        gxapi_cy.WrapVVU.spline2(GXContext._get_tls_geo(), vv_x._wrapper, vv_y._wrapper, vv_x2._wrapper, vv_o._wrapper, type)
        



    @classmethod
    def tokenize_to_values(cls, vv, str_val):
        """
        Tokenize a string based on any characters.

        **Note:**

        Parses a series of space, tab or comma-delimited values to a `GXVV`.
        """
        ret_val = gxapi_cy.WrapVVU.tokenize_to_values(GXContext._get_tls_geo(), vv._wrapper, str_val.encode())
        return ret_val



    @classmethod
    def translate(cls, vv, base, mult):
        """
        Translate values in a `GXVV`

        **Note:**

        (new `GXVV`) = ((old `GXVV`) + base) * scale
        """
        gxapi_cy.WrapVVU.translate(GXContext._get_tls_geo(), vv._wrapper, base, mult)
        



    @classmethod
    def trend(cls, vv_d, order, vv_c):
        """
        Calculate an n'th order best-fit polynomial, integral x.

        **Note:**

        Returns coefficients c[0] .. c[n]
        
           Y(x) = c[0] + c[1]x + c[2](x**2) + ... + c[n](x**n)
        
        The X scale is unitless (1 per element), i.e. 0,1,2,3,...
        
        The polynomial `GXVV` length is set to the number of coefficients
        (order + 1)

        .. seealso::

            `poly_fill`, `trend2`, `poly_fill2`
        """
        gxapi_cy.WrapVVU.trend(GXContext._get_tls_geo(), vv_d._wrapper, order, vv_c._wrapper)
        



    @classmethod
    def trend2(cls, vv_x, vv_d, order, vv_c):
        """
        Calculate an n'th order best-fit polynomial, specified X

        **Note:**

        Returns coefficients c[0] .. c[n]
        
           Y(x) = c[0] + c[1]x + c[2](x**2) + ... + c[n](x**n)
        
        The X scale is defined by a X `GXVV` (see Trend_VV for unitless X).
        
        The polynomial `GXVV` length is set to the number of coefficients
        (order + 1)

        .. seealso::

            `poly_fill`, `trend2`, `poly_fill2`
        """
        gxapi_cy.WrapVVU.trend2(GXContext._get_tls_geo(), vv_x._wrapper, vv_d._wrapper, order, vv_c._wrapper)
        



    @classmethod
    def uniform_dist(cls, vv, seed, min, max, length):
        """
        Fill with uniformly distributed values.

        **Note:**

        `GXVV` is set to input length (except for -1)
        See rand.gxh for a short discription of the
        random number generator used.
        """
        gxapi_cy.WrapVVU.uniform_dist(GXContext._get_tls_geo(), vv._wrapper, seed, min, max, length)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer