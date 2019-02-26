### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXST(gxapi_cy.WrapST):
    """
    GXST class.

    Mono-variate statistics. The `GXST <geosoft.gxapi.GXST>` class is used to accumulate statistical
    information about a set of data. This class is usually used in conjunction
    with others. For instance, `GXDU.stat <geosoft.gxapi.GXDU.stat>` (see `GXDU <geosoft.gxapi.GXDU>`) will add a channel's
    data to the `GXST <geosoft.gxapi.GXST>` object, and sComputeST_IMG (see `GXIMG <geosoft.gxapi.GXIMG>`) will compute
    statistics for a grid.

    **Note:**

    .. _histogram_ranges:

    *** Histogram ranges and color zone ranges ***

    Histogram bins are defined with inclusive minima and exclusive maxima;
    for instance if Min = 0 and Inc = 1, then the second bin would include
    all values z such that  0 >= z > 1 (the first bin has all values < 0).

    Color zones used in displaying grids (`GXITR <geosoft.gxapi.GXITR>`, ZON etc...) are the
    opposite, with exclusive minima and inclusive maxima.
    For instance, if a zone is defined from 0 to 1, then it would
    contain all values of z such that 0 > z >= 1.

    These definitions mean that it is impossible to perfectly assign
    `GXITR <geosoft.gxapi.GXITR>` colors to individual bars of a histogram. The best work-around
    when the data values are integers is to define the color zones using
    0.5 values between the integers. A general work-around is to make the
    number of histogram bins much larger than the number of color zones.

    See also  `GXST2 <geosoft.gxapi.GXST2>` (bi-variate statistics)
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXST <geosoft.gxapi.GXST>`
        
        :returns: A null `GXST <geosoft.gxapi.GXST>`
        :rtype:   GXST
        """
        return GXST()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous


    @classmethod
    def create(cls):
        """
        This method creates a statistics object which is used to
        accumulate statistics.
        

        :returns:    `GXST <geosoft.gxapi.GXST>` Object
        :rtype:      GXST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapST._create(GXContext._get_tls_geo())
        return GXST(ret_val)



    @classmethod
    def create_exact(cls):
        """
        This method creates a statistics object which stores
        all values.
        

        :returns:    `GXST <geosoft.gxapi.GXST>` Object
        :rtype:      GXST

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapST._create_exact(GXContext._get_tls_geo())
        return GXST(ret_val)




    def data(self, val):
        """
        Add this value to the statistics object.
        
        :param val:  Value to Add
        :type  val:  float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._data(val)
        




    def data_vv(self, vv):
        """
        Add all the values in this `GXVV <geosoft.gxapi.GXVV>` to the statistics object.
        
        :param vv:  `GXVV <geosoft.gxapi.GXVV>` object
        :type  vv:  GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._data_vv(vv)
        






    def get_histogram_bins(self, vv):
        """
        Retrieve number of items in each hostogram bin
        
        :param vv:  `GXVV <geosoft.gxapi.GXVV>` for numbers of items
        :type  vv:  GXVV

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The length of the returned `GXVV <geosoft.gxapi.GXVV>` is set to the total
        number of bins. If a histogram is not defined in
        the `GXST <geosoft.gxapi.GXST>`, then the returned length is zero.
        """
        self._get_histogram_bins(vv)
        




    def get_histogram_info(self, div, min, max):
        """
        Retrieve number of bins, min and max value in histogram
        
        :param div:  # of bins
        :param min:  Min (value at start of 2nd bin)
        :param max:  Max (value at end of 2nd last bin)
        :type  div:  int_ref
        :type  min:  float_ref
        :type  max:  float_ref

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The items correspond to those in `histogram2 <geosoft.gxapi.GXST.histogram2>`.
        If a histogram is not defined in
        the `GXST <geosoft.gxapi.GXST>`, then the returned number of bins is zero, and
        the min and max values will be dummies.
        """
        div.value, min.value, max.value = self._get_histogram_info(div.value, min.value, max.value)
        




    def histogram(self, bins):
        """
        This method prepares `GXST <geosoft.gxapi.GXST>` for recording histogram.
        
        :param bins:  # of bins
        :type  bins:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Number of bins includes the one before the minimum
        and the one after the maximum, so it must be a value >2.

        IMPORTANT: This function gets the histogram minimum and
        maximum from the current min and max values stored in the `GXST <geosoft.gxapi.GXST>`,
        so this is equivalent to calling `histogram2 <geosoft.gxapi.GXST.histogram2>` with

        ``#bins, Min, (Max-Min)/(# bins -2))``

        You should already have the data loaded in order to call this
        function.

        See histogram_ranges_
        """
        self._histogram(bins)
        




    def histogram2(self, bins, min, max):
        """
        This method prepares `GXST <geosoft.gxapi.GXST>` for recording histogram.
        
        :param bins:  # of bins
        :param min:   Min
        :param max:   Max
        :type  bins:  int
        :type  min:   float
        :type  max:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Number of bins includes the one before the minimum
        and the one after the maximum, so it must be a value >2.
        The width of the individual bins will be (Min-Max)/(# - 2)

        See histogram_ranges_
        """
        self._histogram2(bins, min, max)
        




    def equivalent_percentile(self, value):
        """
        Return corresponding Percentile for a Value.
        
        :param value:  Input value
        :type  value:  float

        :returns:      The percentile at the given value (0 - 100)
        :rtype:        float

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Statistics and histogram must have been calculated prior to
        calling this method
        """
        ret_val = self._equivalent_percentile(value)
        return ret_val




    def equivalent_value(self, percent):
        """
        Return corresponding Value for a Percentile
        
        :param percent:  Input percentile (0 - 100)
        :type  percent:  float

        :returns:        The value at the given percentile.
        :rtype:          float

        .. versionadded:: 5.0.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Statistics and histogram must have been calculated prior to
        calling this method
        """
        ret_val = self._equivalent_value(percent)
        return ret_val




    def reset(self):
        """
        Resets the Statistics.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        self._reset()
        




    def get_info(self, id):
        """
        This method allows you to retrieve (and compute) the
        information from the `GXST <geosoft.gxapi.GXST>` object.
        
        :param id:  :ref:`ST_INFO`
        :type  id:  int

        :returns:    Data you asked for
                    `GS_R8DM <geosoft.gxapi.GS_R8DM>` for none
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The following can only be determined if the `GXST <geosoft.gxapi.GXST>` has recorded
        a histogram: `ST_MEDIAN <geosoft.gxapi.ST_MEDIAN>`, `ST_MODE <geosoft.gxapi.ST_MODE>`

        `ST_MINPOS <geosoft.gxapi.ST_MINPOS>` can be used to retrieve the smallest value greater
        than zero, but not from `GXST <geosoft.gxapi.GXST>` objects recovered from serialized object.
        """
        ret_val = self._get_info(id)
        return ret_val



    @classmethod
    def get_norm_prob(cls, x):
        """
        Return percent value
        
        :param x:  Real
        :type  x:  float

        :returns:    real


                   Notes			this function is based on Normal Cumulative distribution function
                   mit to about 5 standard deviations
        :rtype:      float

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapST._get_norm_prob(GXContext._get_tls_geo(), x)
        return ret_val



    @classmethod
    def get_norm_prob_x(cls, percent):
        """
        Return number of sigmas from 50% a given percent is
        
        :param percent:  Real
        :type  percent:  float

        :returns:        real


                         Notes			this function is based on Normal Cumulative distribution function
                         mit to about 5 standard deviations
        :rtype:          float

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapST._get_norm_prob_x(GXContext._get_tls_geo(), percent)
        return ret_val




    def normal_test(self):
        """
        Test the "normality" of the histogram distribution
        

        :returns:    The normality statistic.
                    Terminates if no histogram in the `GXST <geosoft.gxapi.GXST>` object.
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function compares the histogram to a normal curve with the
        same mean and standard deviation. The individual counts are normalized
        by the total counts, the bin width and the standard deviation.
        For each bin, the rms difference between the expected probability and
        the normalized count is summed, and the final result is normalized by
        the total number of bins. In this way histograms with different means,
        standard deviations, number of bins and counts can be compared.
        If the histogram were perfectly normal, then a value of 0 would be returned.
        The more "non-normal", the higher the statistic.
        """
        ret_val = self._normal_test()
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer