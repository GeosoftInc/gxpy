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
class GXST:
    """
    GXST class.

    Mono-variate statistics. The :class:`geosoft.gxapi.GXST` class is used to accumulate statistical
    information about a set of data. This class is usually used in conjunction
    with others. For instance, Stat_DU (see :class:`geosoft.gxapi.GXDU`) will add a channel's
    data to the :class:`geosoft.gxapi.GXST` object, and sComputeST_IMG (see :class:`geosoft.gxapi.GXIMG`) will compute
    statistics for a grid.

    **Note:**

    *** Histogram ranges and color zone ranges ***
    
    Histogram bins are defined with inclusive minima and exclusive maxima;
    for instance if Min = 0 and Inc = 1, then the second bin would include
    all values z such that  0 >= z > 1 (the first bin has all values < 0).
    
    Color zones used in displaying grids (:class:`geosoft.gxapi.GXITR`, ZON etc...) are the
    opposite, with exclusive minima and inclusive maxima.
    For instance, if a zone is defined from 0 to 1, then it would
    contain all values of z such that 0 > z >= 1.
    
    These definitions mean that it is impossible to perfectly assign
    :class:`geosoft.gxapi.GXITR` colors to individual bars of a histogram. The best work-around
    when the data values are integers is to define the color zones using
    0.5 values between the integers. A general work-around is to make the
    number of histogram bins much larger than the number of color zones.
    
    See also  :class:`geosoft.gxapi.GXST2` (bi-variate statistics)
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapST(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of :class:`geosoft.gxapi.GXST`
        
        :returns: A null :class:`geosoft.gxapi.GXST`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of :class:`geosoft.gxapi.GXST` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of :class:`geosoft.gxapi.GXST`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls):
        """
        This method creates a statistics object which is used to
        accumulate statistics.
        """
        ret_val = gxapi_cy.WrapST.create(GXContext._get_tls_geo())
        return GXST(ret_val)



    @classmethod
    def create_exact(cls):
        """
        This method creates a statistics object which stores
        all values.
        """
        ret_val = gxapi_cy.WrapST.create_exact(GXContext._get_tls_geo())
        return GXST(ret_val)




    def data(self, p2):
        """
        Add this value to the statistics object.
        """
        self._wrapper.data(p2)
        




    def data_vv(self, p2):
        """
        Add all the values in this :class:`geosoft.gxapi.GXVV` to the statistics object.
        """
        self._wrapper.data_vv(p2._wrapper)
        






    def get_histogram_bins(self, p2):
        """
        Retrieve number of items in each hostogram bin

        **Note:**

        The length of the returned :class:`geosoft.gxapi.GXVV` is set to the total
        number of bins. If a histogram is not defined in
        the :class:`geosoft.gxapi.GXST`, then the returned length is zero.
        """
        self._wrapper.get_histogram_bins(p2._wrapper)
        




    def get_histogram_info(self, p2, p3, p4):
        """
        Retrieve number of bins, min and max value in histogram

        **Note:**

        The items correspond to those in Histogram2_ST.
        If a histogram is not defined in
        the :class:`geosoft.gxapi.GXST`, then the returned number of bins is zero, and
        the min and max values will be dummies.
        """
        p2.value, p3.value, p4.value = self._wrapper.get_histogram_info(p2.value, p3.value, p4.value)
        




    def histogram(self, p2):
        """
        This method prepares :class:`geosoft.gxapi.GXST` for recording histogram.

        **Note:**

        The Number of bins includes the one before the minimum
        and the one after the maximum, so it must be a value >2.
        
        IMPORTANT: This function gets the histogram minimum and
        maximum from the current min and max values stored in the :class:`geosoft.gxapi.GXST`,
        so this is equivalent to calling
        
        Histogram2_ST( #bins, Min, (Max-Min)/(# bins -2));
        
        You should already have the data loaded in order to call this
        function.
        
        See the note above "Histogram ranges and color zone ranges"
        """
        self._wrapper.histogram(p2)
        




    def histogram2(self, p2, p3, p4):
        """
        This method prepares :class:`geosoft.gxapi.GXST` for recording histogram.

        **Note:**

        The Number of bins includes the one before the minimum
        and the one after the maximum, so it must be a value >2.
        The width of the individual bins will be (Min-Max)/(# - 2)
        
        See the note above "Histogram ranges and color zone ranges"
        """
        self._wrapper.histogram2(p2, p3, p4)
        




    def equivalent_percentile(self, p2):
        """
        Return corresponding Percentile for a Value.

        **Note:**

        Statistics and histogram must have been calculated prior to
        calling this method
        """
        ret_val = self._wrapper.equivalent_percentile(p2)
        return ret_val




    def equivalent_value(self, p2):
        """
        Return corresponding Value for a Percentile

        **Note:**

        Statistics and histogram must have been calculated prior to
        calling this method
        """
        ret_val = self._wrapper.equivalent_value(p2)
        return ret_val




    def reset(self):
        """
        Resets the Statistics.
        """
        self._wrapper.reset()
        




    def get_info(self, p2):
        """
        This method allows you to retrieve (and compute) the
        information from the :class:`geosoft.gxapi.GXST` object.

        **Note:**

        The following can only be determined if the :class:`geosoft.gxapi.GXST` has recorded
        a histogram: :attr:`geosoft.gxapi.ST_MEDIAN`, :attr:`geosoft.gxapi.ST_MODE`
        
        :attr:`geosoft.gxapi.ST_MINPOS` can be used to retrieve the smallest value greater
        than zero, but not from :class:`geosoft.gxapi.GXST` objects recovered from serialized object.
        """
        ret_val = self._wrapper.get_info(p2)
        return ret_val



    @classmethod
    def get_norm_prob(cls, p1):
        """
        Return percent value
        """
        ret_val = gxapi_cy.WrapST.get_norm_prob(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def get_norm_prob_x(cls, p1):
        """
        Return number of sigmas from 50% a given percent is
        """
        ret_val = gxapi_cy.WrapST.get_norm_prob_x(GXContext._get_tls_geo(), p1)
        return ret_val




    def normal_test(self):
        """
        Test the "normality" of the histogram distribution

        **Note:**

        This function compares the histogram to a normal curve with the
        same mean and standard deviation. The individual counts are normalized
        by the total counts, the bin width and the standard deviation.
        For each bin, the rms difference between the expected probability and
        the normalized count is summed, and the final result is normalized by
        the total number of bins. In this way histograms with different means,
        standard deviations, number of bins and counts can be compared.
        If the histogram were perfectly normal, then a value of 0 would be returned.
        The more "non-normal", the higher the statistic.
        """
        ret_val = self._wrapper.normal_test()
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer