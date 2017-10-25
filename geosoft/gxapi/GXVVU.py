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
    various operations on :class:`geosoft.gxapi.GXVV` objects, including pruning,
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
        A null (undefined) instance of :class:`geosoft.gxapi.GXVVU`
        
        :returns: A null :class:`geosoft.gxapi.GXVVU`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXVVU` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXVVU`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def average_repeat(cls, p1, p2):
        """
        Average repeat values.

        **Note:**

        Repeated values in the reference :class:`geosoft.gxapi.GXVV` will be averaged
        in the data :class:`geosoft.gxapi.GXVV`.  The first value in the data :class:`geosoft.gxapi.GXVV` will be set to the
        average and subsequent data :class:`geosoft.gxapi.GXVV` values will be dummied out.
        Data is processed only to the minimum length of the
        input :class:`geosoft.gxapi.GXVV` lengths.
        """
        gxapi_cy.WrapVVU.average_repeat(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def average_repeat_ex(cls, p1, p2, p3):
        """
        Average repeat values.

        **Note:**

        Repeated values in the reference :class:`geosoft.gxapi.GXVV` will be set to the mean, median, minimum or maximum value
        in the data :class:`geosoft.gxapi.GXVV`.  For minimum and maximum, the index in the data :class:`geosoft.gxapi.GXVV` containing the minimum or maximum value
        is retained, and the other repeated values are dummied out. For mean and median, the first value in the 
        data :class:`geosoft.gxapi.GXVV` will be reset and subsequent data :class:`geosoft.gxapi.GXVV` values will be dummied out.
        Data is processed only to the minimum length of the
        input :class:`geosoft.gxapi.GXVV` lengths.
        """
        gxapi_cy.WrapVVU.average_repeat_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3)
        



    @classmethod
    def average_repeat2(cls, p1, p2, p3):
        """
        Average repeat values based on 2 reference channels.

        **Note:**

        Repeated values in the reference :class:`geosoft.gxapi.GXVV` will be averaged
        in the data :class:`geosoft.gxapi.GXVV`.  The first value in the data :class:`geosoft.gxapi.GXVV` will be set to the
        average and subsequent data :class:`geosoft.gxapi.GXVV` values will be dummied out.
        Data is processed only to the minimum length of the
        input :class:`geosoft.gxapi.GXVV` lengths.
        Both the reference :class:`geosoft.gxapi.GXVV` values must repeat for the averageing
        to occur. This version is useful for averaging on repeated
        (X,Y) locations.
        """
        gxapi_cy.WrapVVU.average_repeat2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def average_repeat2_ex(cls, p1, p2, p3, p4):
        """
        Average repeat values based on 2 reference channels.

        **Note:**

        Repeated values in the reference :class:`geosoft.gxapi.GXVV` will be set to the mean, median, minimum or maximum value
        in the data :class:`geosoft.gxapi.GXVV`.  The first value in the data :class:`geosoft.gxapi.GXVV` will be reset and subsequent data :class:`geosoft.gxapi.GXVV` values will be dummied out.
        Data is processed only to the minimum length of the
        input :class:`geosoft.gxapi.GXVV` lengths.
        Both the reference :class:`geosoft.gxapi.GXVV` values must repeat for the averageing
        to occur. This version is useful for averaging on repeated
        (X,Y) locations.
        """
        gxapi_cy.WrapVVU.average_repeat2_ex(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4)
        



    @classmethod
    def binary_search(cls, p1, p2, p3, p4):
        """
        Search  numeric value in a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        The :class:`geosoft.gxapi.GXVV` should be sorted.Search comparison is made on double
        comparison of the data.
        """
        p3.value, p4.value = gxapi_cy.WrapVVU.binary_search(GXContext._get_tls_geo(), p1._wrapper, p2, p3.value, p4.value)
        



    @classmethod
    def box_cox(cls, p1, p2):
        """
        Run Box-Cox (lambda) Transformation on :class:`geosoft.gxapi.GXVV`.
        """
        gxapi_cy.WrapVVU.box_cox(GXContext._get_tls_geo(), p1._wrapper, p2)
        



    @classmethod
    def bp_filt(cls, p1, p2, p3, p4, p5):
        """
        Band-pass filter to the specified.

        **Note:**

        If the short and long wavelengths are <= 0, the input channel
        is simply copied to the output channel without filtering.
        
        The wavelengths are in fiducials.
        """
        gxapi_cy.WrapVVU.bp_filt(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5)
        



    @classmethod
    def clip(cls, p1, p2, p3, p4):
        """
        Clip a :class:`geosoft.gxapi.GXVV` to a range.
        """
        gxapi_cy.WrapVVU.clip(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        



    @classmethod
    def clip_to_detect_limit(cls, p1, p2, p3):
        """
        Apply detection limit clipping of data.

        **Note:**

        Flow:
        
        1. If auto-converting negatives, then all negative values
            are replaced by -0.5*value, and detection limit is ignored.
        
        2. If not auto-converting negatives, and the detection limit is not
           :attr:`geosoft.gxapi.rDUMMY`, then values less than the detection limit are converted to
           one-half the detection limit.
        
        This function is identical to ClipToDetectLimit_CHIMERA.
        """
        gxapi_cy.WrapVVU.clip_to_detect_limit(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def decimate(cls, p1, p2):
        """
        Decimate a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        For a decimation factor N, will remove all values except
        those with indices equal to MN, where M is an integer.
        """
        gxapi_cy.WrapVVU.decimate(GXContext._get_tls_geo(), p1._wrapper, p2)
        



    @classmethod
    def deviation(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Calculate distance of point locations to a straight line
        """
        gxapi_cy.WrapVVU.deviation(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8)
        



    @classmethod
    def distance(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Create a cumulative distance :class:`geosoft.gxapi.GXVV`
        """
        gxapi_cy.WrapVVU.distance(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7)
        



    @classmethod
    def distance_non_cumulative(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Create a non cumulative distance :class:`geosoft.gxapi.GXVV` i.e each
        distance element is the distance of the corresponding
        (X,Y) element and the previous element.

        **Note:**

        The fist distace element is :attr:`geosoft.gxapi.rDUMMY`.
        """
        gxapi_cy.WrapVVU.distance_non_cumulative(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7)
        



    @classmethod
    def distance_3d(cls, p1, p2, p3, p4, p5):
        """
        Create a cumulative distance :class:`geosoft.gxapi.GXVV` from X, Y and Z VVs

        **Note:**

        The output :class:`geosoft.gxapi.GXVV` is the length of the shortest X,Y or Z input :class:`geosoft.gxapi.GXVV`.
        Any values with dummies are ignored - the distance at that
        point is equal to the distance at the previous valid point.
        The returned :class:`geosoft.gxapi.GXVV` is the cumulative straight-line distance
        between the points. No re-sampling is performed.
        VVs of any type are supported.
        """
        gxapi_cy.WrapVVU.distance_3d(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5._wrapper)
        



    @classmethod
    def find_gaps_3d(cls, p1, p2, p3, p4, p5):
        """
        Return indices of locations separated from previous locations by more than the input gap distance.

        **Note:**

        Locate the starting points of line segements determined by an input gap distance.
        The returned indices indicate where to break the line, given an input gap.
        The number of returned indices is one less than the number of line segments.
        (So if there are no gaps the returned :class:`geosoft.gxapi.GXVV` has zero length).
        """
        gxapi_cy.WrapVVU.find_gaps_3d(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5._wrapper)
        



    @classmethod
    def dummy_range(cls, p1, p2, p3, p4, p5):
        """
        Dummy values inside or outside a range in a :class:`geosoft.gxapi.GXVV`

        **Note:**

        If the Inside flag is TRUE, values within the specified
        range are set to dummy. If the inside flag is FALSE,
        values outside the range are set to dummy.  If the Inclusive
        flag is TRUE, then dMin and dMax are considered part of the
        range. If it is FALSE, then < or > are used, and dMin and
        dMax lie outside the range.
        """
        gxapi_cy.WrapVVU.dummy_range(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        



    @classmethod
    def dummy_range_ex(cls, p1, p2, p3, p4, p5, p6):
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
        gxapi_cy.WrapVVU.dummy_range_ex(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5, p6)
        



    @classmethod
    def dummy_repeat(cls, p1, p2):
        """
        Dummy repeat values in a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        Either the first, middle or last point will be left.
                          Use Interp_VVU to interpolate after if desired.
        """
        gxapi_cy.WrapVVU.dummy_repeat(GXContext._get_tls_geo(), p1._wrapper, p2)
        



    @classmethod
    def dup_stats(cls, p1, p2, p3, p4):
        """
        Calculate means and differences for duplicate sample pairs

        **Note:**

        Created for duplicate sample handling in :class:`geosoft.gxapi.GXCHIMERA`. On input,
        a numeric :class:`geosoft.gxapi.GXVV` containing data values, and a sample type :class:`geosoft.gxapi.GXVV`.
        Sample pairs have types "1" and "2". This routine searches for
        types in order "1 2 1 2", and writes the mean values of pairs
        to the mean value :class:`geosoft.gxapi.GXVV`, and the differences with the mean (equal
        values, negative and positive) to the difference :class:`geosoft.gxapi.GXVV`. Results
        for samples out of order, for unmatched values, or when the
        sample type does not equal "1" or "2" are set to dummy.
        """
        gxapi_cy.WrapVVU.dup_stats(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def exp_dist(cls, p1, p2, p3, p4):
        """
        Fill with exponentially distributed values.

        **Note:**

        :class:`geosoft.gxapi.GXVV` is set to input length (except for -1)
        See RAND for a short discription of the
        random number generator used.
        """
        gxapi_cy.WrapVVU.exp_dist(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4)
        



    @classmethod
    def filter(cls, p1, p2, p3):
        """
        Apply a convolution filter to a :class:`geosoft.gxapi.GXVV`.
        """
        gxapi_cy.WrapVVU.filter(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3)
        



    @classmethod
    def find_string_items(cls, p1, p2, p3, p4, p5, p6):
        """
        Searches a :class:`geosoft.gxapi.GXVV` for items in a second :class:`geosoft.gxapi.GXVV`, returns indices of those found.

        **Note:**

        This is a much more efficient way of determining if items in
        one :class:`geosoft.gxapi.GXVV` are found in a second, than by searching
        repeatedly in a loop.
        The returned :attr:`geosoft.gxapi.GS_LONG` :class:`geosoft.gxapi.GXVV` contains the same number of items as
        the "search items" :class:`geosoft.gxapi.GXVV`, and contains -1 for items where the
        value is not found, and the index of items that are found.
        Comparisons are case-tolerant.
        Non-string VVs are converted to string type VVs (element size 24) internally.
        
        The method requires that the :class:`geosoft.gxapi.GXVV` items be sorted, and
        will do so internally. Since the input VVs may already be sorted,
        the method will run faster if this stage can be skipped.
        """
        gxapi_cy.WrapVVU.find_string_items(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6._wrapper)
        



    @classmethod
    def fractal_filter(cls, p1, p2, p3, p4):
        """
        Fractal filter a :class:`geosoft.gxapi.GXVV`.
        """
        gxapi_cy.WrapVVU.fractal_filter(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4._wrapper)
        



    @classmethod
    def close_xy(cls, p1, p2, p3, p4):
        """
        Find the closest point to an input point (XY).

        **Note:**

        Input X and Y location VVs, and a location.
        Returns the index of the point in the :class:`geosoft.gxapi.GXVV` closest to the
        input point.
        """
        ret_val = gxapi_cy.WrapVVU.close_xy(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4)
        return ret_val



    @classmethod
    def close_xym(cls, p1, p2, p3, p4, p5):
        """
        Find the closest point to an input point, with mask (XY).

        **Note:**

        Input X and Y location VVs, and a location.
        Returns the index of the point in the :class:`geosoft.gxapi.GXVV` closest to the
        input point.
        This skips points where the mask value is dummy.
        If no valid points are in the VVs, or all the mask :class:`geosoft.gxapi.GXVV` values
        are dummy, the returned index is -1.
        """
        ret_val = gxapi_cy.WrapVVU.close_xym(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5)
        return ret_val



    @classmethod
    def close_xyz(cls, p1, p2, p3, p4, p5, p6):
        """
        Find the closest point to an input point (XYZ).

        **Note:**

        Input X, Y and Z location VVs, and a location.
        Returns the index of the point in the :class:`geosoft.gxapi.GXVV` closest to the
        input point.
        """
        ret_val = gxapi_cy.WrapVVU.close_xyz(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6)
        return ret_val



    @classmethod
    def close_xyzm(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Find the closest point to an input point, with mask (XYZ).

        **Note:**

        Input X, Y and Z location VVs, and a location.
        Returns the index of the point in the :class:`geosoft.gxapi.GXVV` closest to the
        input point.
        This skips points where the mask value is dummy.
        If no valid points are in the VVs, or all the mask :class:`geosoft.gxapi.GXVV` values
        are dummy, the returned index is -1.
        """
        ret_val = gxapi_cy.WrapVVU.close_xyzm(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5, p6, p7)
        return ret_val



    @classmethod
    def dummy_back_tracks(cls, p1):
        """
        Dummy all points that keep a :class:`geosoft.gxapi.GXVV` from being monotonically increasing.

        **Note:**

        The :class:`geosoft.gxapi.GXVV` length remains the same. Any point that is less than or equal to
        the previous (valid) point in the :class:`geosoft.gxapi.GXVV` is dummied.
        """
        ret_val = gxapi_cy.WrapVVU.dummy_back_tracks(GXContext._get_tls_geo(), p1._wrapper)
        return ret_val



    @classmethod
    def find_dummy(cls, p1, p2, p3, p4, p5):
        """
        Find the first dummy|non-dummy value in :class:`geosoft.gxapi.GXVV`

        **Note:**

        Start and end of range are always defined lowest
        to largest even if decreasing search order.  To search
        entire :class:`geosoft.gxapi.GXVV` range, specify 0,-1.
        """
        ret_val = gxapi_cy.WrapVVU.find_dummy(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        return ret_val



    @classmethod
    def interp(cls, p1, p2, p3):
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
        gxapi_cy.WrapVVU.interp(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def qc_fill_gaps(cls, p1, p2, p3, p4, p5):
        """
        Calculate fill in line segments

        **Note:**

        The X & Y VVs are returned as the calculated fill in line segments.
        """
        ret_val = gxapi_cy.WrapVVU.qc_fill_gaps(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5)
        return ret_val



    @classmethod
    def search_text(cls, p1, p2, p3, p4, p5, p6):
        """
        Search for a text value in a :class:`geosoft.gxapi.GXVV`

        **Note:**

        Search comparison is made on string comparison
        of the data. Returns index of first item matching
        the input string.
        If start index is -1 or dummy, then full :class:`geosoft.gxapi.GXVV` is searched.
        Use :attr:`geosoft.gxapi.VVU_MATCH_INPUT_LENGTH` to match the first part of a string.
        This is also recommended for matching numerical values, since
        the displayed value in the database may not be the same as the
        stored value.
        """
        ret_val = gxapi_cy.WrapVVU.search_text(GXContext._get_tls_geo(), p1._wrapper, p2.encode(), p3, p4, p5, p6)
        return ret_val



    @classmethod
    def mask(cls, p1, p2):
        """
        Mask dummies in one :class:`geosoft.gxapi.GXVV` onto another.

        **Note:**

        :class:`geosoft.gxapi.GXVV` to mask will be resampled to reference :class:`geosoft.gxapi.GXVV` if required.
        The returned length of the :class:`geosoft.gxapi.GXVV` to mask will be the shorter
        of the reference :class:`geosoft.gxapi.GXVV` or the mask :class:`geosoft.gxapi.GXVV`.
        """
        gxapi_cy.WrapVVU.mask(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def mask_and(cls, p1, p2, p3):
        """
        Create mask from logical AND of two VVs.

        **Note:**

        If both values are non-dummies, then result is 1, else dummy.
        """
        gxapi_cy.WrapVVU.mask_and(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def mask_or(cls, p1, p2, p3):
        """
        Create mask from logical OR of two VVs.

        **Note:**

        If either values is non-dummy, then result is 1, else dummy.
        """
        gxapi_cy.WrapVVU.mask_or(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def nl_filt(cls, p1, p2, p3, p4):
        """
        Applies a non-linear filter.
        """
        gxapi_cy.WrapVVU.nl_filt(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4)
        



    @classmethod
    def noise_check(cls, p1, p2, p3, p4):
        """
        Check on deviation of data from variable background in a :class:`geosoft.gxapi.GXVV`

        **Note:**

        This function checks vertical deviation of data in input :class:`geosoft.gxapi.GXVV`
        against a moving straight line. The straight line at any time is
        defined by two extreme points of a data segment.  Output :class:`geosoft.gxapi.GXVV` will
        be 0 if data point in input :class:`geosoft.gxapi.GXVV` falls within the deviation,
        otherwise, it will be 1.
        Output :class:`geosoft.gxapi.GXVV` will be 0 if the straight line is vertical.
        """
        gxapi_cy.WrapVVU.noise_check(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4)
        



    @classmethod
    def noise_check2(cls, p1, p2, p3, p4, p5):
        """
        Like NoiseCheck_VVU, but returns maximum deviation at all points.

        **Note:**

        This function checks vertical deviation of data in an input :class:`geosoft.gxapi.GXVV`
        against a moving straight line, where the X-axis value is
        taken to be the data index, and the Y-axis value is the
        input data :class:`geosoft.gxapi.GXVV` value. The straight line is drawn between data points
        at the ends of the line segment, whose length is an input.
        
        The output flag :class:`geosoft.gxapi.GXVV` is set to 0 if data point in input :class:`geosoft.gxapi.GXVV` falls within the
        deviation for all the moving line segments of which it is a part, otherwise, it
        will be set to 1.
        
        The output maximum deviation :class:`geosoft.gxapi.GXVV` contains the maximum deviation at each point
        for all the moving line segments that it is a part of.
        """
        gxapi_cy.WrapVVU.noise_check2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5)
        



    @classmethod
    def normal_dist(cls, p1, p2, p3, p4, p5):
        """
        Fill with normally (Gaussian) distributed values.

        **Note:**

        :class:`geosoft.gxapi.GXVV` is set to input length (except for -1)
        See RAND for a short discription of the
        random number generator used.
        """
        gxapi_cy.WrapVVU.normal_dist(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        



    @classmethod
    def offset_circles(cls, p1, p2, p3, p4, p5, p6):
        """
        Get non-overlapping offset location for circular symbols.

        **Note:**

        Often on maps plotted symbols and text overlap each other.
        This routine accepts of :class:`geosoft.gxapi.GXVV` of locations and returns a new
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
        gxapi_cy.WrapVVU.offset_circles(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5._wrapper, p6._wrapper)
        



    @classmethod
    def offset_correct(cls, p1, p2, p3, p4, p5, p6):
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
        gxapi_cy.WrapVVU.offset_correct(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5._wrapper, p6._wrapper)
        



    @classmethod
    def offset_correct2(cls, p1, p2, p3, p4, p5, p6):
        """
        Same as OffsetCorrect_VVU, but for an arbitrary offset angle.
        """
        gxapi_cy.WrapVVU.offset_correct2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5._wrapper, p6._wrapper)
        



    @classmethod
    def offset_correct3(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Same as OffsetCorrect2_VVU, but specify smoothing interval.

        **Note:**

        See the algorithm note #2 above for the default smoothing interval.
        """
        gxapi_cy.WrapVVU.offset_correct3(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6._wrapper, p7._wrapper)
        



    @classmethod
    def offset_correct_xyz(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
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
        gxapi_cy.WrapVVU.offset_correct_xyz(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8._wrapper, p9._wrapper, p10._wrapper)
        



    @classmethod
    def offset_rectangles(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Get non-overlapping offset location for rectangular symbols.

        **Note:**

        Often on maps plotted symbols and text overlap each other.
        This routine accepts of :class:`geosoft.gxapi.GXVV` of locations and returns a new
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
        gxapi_cy.WrapVVU.offset_rectangles(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5, p6._wrapper, p7._wrapper)
        



    @classmethod
    def pick_peak(cls, p1, p2, p3, p4):
        """
        Find peaks in a :class:`geosoft.gxapi.GXVV` - method one.

        **Note:**

        Peaks are the maximum point within a sequence of
        positive values in the input :class:`geosoft.gxapi.GXVV`.  The width is the
        number of points in the positive sequence.
        
        A :class:`geosoft.gxapi.GXVV` may have to be pre-filtered before finding
        the peak values:
        
        Use BPFilt_VVU to smooth the data as required.
        Use Filter_VVU to apply a Laplace filter
        "-0.5,1.0,-0.5" to make curvature data.
        """
        gxapi_cy.WrapVVU.pick_peak(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4)
        



    @classmethod
    def pick_peak2(cls, p1, p2, p3, p4):
        """
        Find peaks in a :class:`geosoft.gxapi.GXVV` - method two.

        **Note:**

        Peaks are the maximum point within a sequence of
        values in the input :class:`geosoft.gxapi.GXVV`. Maximum points must be above
        the base level and have a local amplitude greater
        than the minimum amplitude specified.
        
        A :class:`geosoft.gxapi.GXVV` may have to be pre-filtered before finding
        the peak values.
        """
        gxapi_cy.WrapVVU.pick_peak2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4)
        



    @classmethod
    def pick_peak3(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Find peaks in a :class:`geosoft.gxapi.GXVV` - method two, returning width and half-amplitude widths.

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
        gxapi_cy.WrapVVU.pick_peak3(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6._wrapper, p7._wrapper, p8._wrapper, p9._wrapper)
        



    @classmethod
    def poly_fill(cls, p1, p2, p3):
        """
        Fill a :class:`geosoft.gxapi.GXVV` with values from an n'th order polynomial, integral x.

        **Note:**

        The output :class:`geosoft.gxapi.GXVV` length must be set as desired before calling.
        
        The X scale is unitless (1 per element), i.e. 0,1,2,3,...
        """
        gxapi_cy.WrapVVU.poly_fill(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper)
        



    @classmethod
    def poly_fill2(cls, p1, p2, p3, p4):
        """
        Fill a :class:`geosoft.gxapi.GXVV` with values from an n'th order polynomial, specified X

        **Note:**

        The output :class:`geosoft.gxapi.GXVV` length must be set as desired before calling.
        The X scale is defined by a X :class:`geosoft.gxapi.GXVV` (see Trend_VV for unitless X).
        """
        gxapi_cy.WrapVVU.poly_fill2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4._wrapper)
        



    @classmethod
    def polygon_mask(cls, p1, p2, p3, p4, p5):
        """
        Mask a :class:`geosoft.gxapi.GXVV` using XY data and a polygon.

        **Note:**

        The VVs have to be the same length
        """
        gxapi_cy.WrapVVU.polygon_mask(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5)
        



    @classmethod
    def prune(cls, p1, p2, p3):
        """
        Prune values from a :class:`geosoft.gxapi.GXVV` based on reference :class:`geosoft.gxapi.GXVV`

        **Note:**

        Pruning will shorten the :class:`geosoft.gxapi.GXVV` by removing values
        that are either dummy or non-dummy in the reference
        :class:`geosoft.gxapi.GXVV`
        """
        gxapi_cy.WrapVVU.prune(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3)
        



    @classmethod
    def qc(cls, p1, p2, p3, p4, p5, p6, p7, p8):
        """
        Quality control on deviation of data from norm in a :class:`geosoft.gxapi.GXVV`

        **Note:**

        This function tests data in input :class:`geosoft.gxapi.GXVV` against
        two separate criteria. Each element of the output :class:`geosoft.gxapi.GXVV`
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
        gxapi_cy.WrapVVU.qc(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8)
        



    @classmethod
    def range_vector_mag(cls, p1, p2, p3, p4):
        """
        Find the range of hypotenuse values of two VVs.

        **Note:**

        For each value in the VVs, finds sqrt(dV1*dV1 + dV2*dV2)
        and returns the min and max values.
        """
        p3.value, p4.value = gxapi_cy.WrapVVU.range_vector_mag(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.value, p4.value)
        



    @classmethod
    def regress(cls, p1, p2, p3, p4):
        """
        Calculate linear regression through data
        """
        p3.value, p4.value = gxapi_cy.WrapVVU.regress(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.value, p4.value)
        



    @classmethod
    def rel_var_dup(cls, p1, p2, p3, p4):
        """
        Estimate relative variance of duplicate sample pairs from a database.

        **Note:**

        Created for duplicate sample handling in :class:`geosoft.gxapi.GXCHIMERA`. On input,
        a numeric or text :class:`geosoft.gxapi.GXVV` containing data values, and a sample type :class:`geosoft.gxapi.GXVV`.
        Sample pairs have types "1" and "2". This routine searches for
        types in order "1 2 1 2", and calulates the unnormalized relative variance,
        defined as the sum of the squared differences between duplicates
        divided by the sum of the squared mean values of the duplicates.
        (To get the true rel.var., divide by N-1, where N is the number of
        duplicate pairs used.)
        Samples out of order, unmatched pairs, or when the
        sample type does not equal "1" or "2" are ignored.
        """
        p3.value, p4.value = gxapi_cy.WrapVVU.rel_var_dup(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3.value, p4.value)
        



    @classmethod
    def remove_dummy(cls, p1):
        """
        Remove dummy values from a :class:`geosoft.gxapi.GXVV`
        """
        gxapi_cy.WrapVVU.remove_dummy(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def remove_dummy2(cls, p1, p2):
        """
        Remove dummy values from 2 VVs.

        **Note:**

        Removes all indices where either :class:`geosoft.gxapi.GXVV` has a dummy, or is
        not defined (due to length differences).
        """
        gxapi_cy.WrapVVU.remove_dummy2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper)
        



    @classmethod
    def remove_dummy3(cls, p1, p2, p3):
        """
        Remove dummy values from 3 VVs.

        **Note:**

        Removes all indices where any :class:`geosoft.gxapi.GXVV` has a dummy, or is
        not defined (due to length differences).
        """
        gxapi_cy.WrapVVU.remove_dummy3(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def remove_dummy4(cls, p1, p2, p3, p4):
        """
        Remove dummy values from 4 VVs.

        **Note:**

        Removes all indices where any :class:`geosoft.gxapi.GXVV` has a dummy, or is
        not defined (due to length differences).
        """
        gxapi_cy.WrapVVU.remove_dummy4(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper)
        



    @classmethod
    def remove_dup(cls, p1, p2, p3):
        """
        Remove/average duplicate sample pairs from a database.

        **Note:**

        Created for duplicate sample handling in :class:`geosoft.gxapi.GXCHIMERA`. On input,
        a numeric or text :class:`geosoft.gxapi.GXVV` containing data values, and a sample type :class:`geosoft.gxapi.GXVV`.
        Sample pairs have types "1" and "2". This routine searches for
        types in order "1 2 1 2", and replaces the pair of values in the
        data :class:`geosoft.gxapi.GXVV` according to the `VV_DUP` value.
        Results for samples out of order, for unmatched pairs, or when the
        sample type does not equal "1" or "2" remain unchanged.
        """
        gxapi_cy.WrapVVU.remove_dup(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3)
        



    @classmethod
    def remove_xy_dup(cls, p1, p2, p3, p4):
        """
        Remove/average duplicate samples with the same (X, Y).

        **Note:**

        Searches for duplicated (X, Y) locations and removes the
        duplicates (can be more than just a pair). The "Z" values,
        if defined, are treated according to the value of `VV_XYDUP`.
        The returned VVs are shortened to the new length, without
        duplicates.
        The Z :class:`geosoft.gxapi.GXVV` can be set to NULL on input, in which case it is ignored.
        """
        gxapi_cy.WrapVVU.remove_xy_dup(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4)
        



    @classmethod
    def remove_xy_dup_index(cls, p1, p2, p3):
        """
        Remove duplicate samples with the same (X, Y) and update index.

        **Note:**

        Searches for duplicated (X, Y) locations and removes the
        duplicates (can be more than just a pair). The Index :class:`geosoft.gxapi.GXVV` is
        updated accordingly .i.e if  (X,Y) location of Index[0] == Index[1]
        Index[1] is removed.
        """
        gxapi_cy.WrapVVU.remove_xy_dup_index(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def rolling_stats(cls, p1, p2, p3, p4, p5):
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
        gxapi_cy.WrapVVU.rolling_stats(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4, p5)
        



    @classmethod
    def search_replace(cls, p1, p2, p3):
        """
        Search and replace numeric values in a :class:`geosoft.gxapi.GXVV`.

        **Note:**

        Search comparison is made on double comparison
        of the data.
        """
        gxapi_cy.WrapVVU.search_replace(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def search_replace_text(cls, p1, p2, p3, p4, p5, p6):
        """
        Search and replace text values in a :class:`geosoft.gxapi.GXVV`

        **Note:**

        Search comparison is made on string comparison
        of the data.
        """
        gxapi_cy.WrapVVU.search_replace_text(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4.encode(), p5.encode(), p6)
        



    @classmethod
    def search_replace_text_ex(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Search and replace text values in a :class:`geosoft.gxapi.GXVV`, count items changed.

        **Note:**

        Search comparison is made on a string comparison
        of the data.
        """
        p7.value = gxapi_cy.WrapVVU.search_replace_text_ex(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4.encode(), p5.encode(), p6, p7.value)
        



    @classmethod
    def spline(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9):
        """
        Spline a Y :class:`geosoft.gxapi.GXVV` onto an X :class:`geosoft.gxapi.GXVV`.
        """
        gxapi_cy.WrapVVU.spline(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4, p5, p6, p7, p8, p9)
        



    @classmethod
    def spline2(cls, p1, p2, p3, p4, p5):
        """
        Spline a Y :class:`geosoft.gxapi.GXVV` onto an X :class:`geosoft.gxapi.GXVV`. Uses specified values of X in X2
        """
        gxapi_cy.WrapVVU.spline2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper, p4._wrapper, p5)
        



    @classmethod
    def tokenize_to_values(cls, p1, p2):
        """
        Tokenize a string based on any characters.

        **Note:**

        Parses a series of space, tab or comma-delimited values to a :class:`geosoft.gxapi.GXVV`.
        """
        ret_val = gxapi_cy.WrapVVU.tokenize_to_values(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        return ret_val



    @classmethod
    def translate(cls, p1, p2, p3):
        """
        Translate values in a :class:`geosoft.gxapi.GXVV`

        **Note:**

        (new :class:`geosoft.gxapi.GXVV`) = ((old :class:`geosoft.gxapi.GXVV`) + base) * scale
        """
        gxapi_cy.WrapVVU.translate(GXContext._get_tls_geo(), p1._wrapper, p2, p3)
        



    @classmethod
    def trend(cls, p1, p2, p3):
        """
        Calculate an n'th order best-fit polynomial, integral x.

        **Note:**

        Returns coefficients c[0] .. c[n]
        
           Y(x) = c[0] + c[1]x + c[2](x**2) + ... + c[n](x**n)
        
        The X scale is unitless (1 per element), i.e. 0,1,2,3,...
        
        The polynomial :class:`geosoft.gxapi.GXVV` length is set to the number of coefficients
        (order + 1)
        """
        gxapi_cy.WrapVVU.trend(GXContext._get_tls_geo(), p1._wrapper, p2, p3._wrapper)
        



    @classmethod
    def trend2(cls, p1, p2, p3, p4):
        """
        Calculate an n'th order best-fit polynomial, specified X

        **Note:**

        Returns coefficients c[0] .. c[n]
        
           Y(x) = c[0] + c[1]x + c[2](x**2) + ... + c[n](x**n)
        
        The X scale is defined by a X :class:`geosoft.gxapi.GXVV` (see Trend_VV for unitless X).
        
        The polynomial :class:`geosoft.gxapi.GXVV` length is set to the number of coefficients
        (order + 1)
        """
        gxapi_cy.WrapVVU.trend2(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3, p4._wrapper)
        



    @classmethod
    def uniform_dist(cls, p1, p2, p3, p4, p5):
        """
        Fill with uniformly distributed values.

        **Note:**

        :class:`geosoft.gxapi.GXVV` is set to input length (except for -1)
        See rand.gxh for a short discription of the
        random number generator used.
        """
        gxapi_cy.WrapVVU.uniform_dist(GXContext._get_tls_geo(), p1._wrapper, p2, p3, p4, p5)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer