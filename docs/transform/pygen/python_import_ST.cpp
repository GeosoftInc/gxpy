#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXSTPtr GXST_wrap_create()
{
    GXSTPtr ret = GXST::create();
    return ret;
}
inline GXSTPtr GXST_wrap_create_exact()
{
    GXSTPtr ret = GXST::create_exact();
    return ret;
}
inline void GXST_wrap_data(GXSTPtr self, double arg1)
{
    self->data(arg1);
}
inline void GXST_wrap_data_vv(GXSTPtr self, GXVVPtr arg1)
{
    self->data_vv(arg1);
}
inline void GXST_wrap_get_histogram_bins(GXSTPtr self, GXVVPtr arg1)
{
    self->get_histogram_bins(arg1);
}
inline void GXST_wrap_get_histogram_info(GXSTPtr self, int_ref& arg1, float_ref& arg2, float_ref& arg3)
{
    self->get_histogram_info(arg1, arg2, arg3);
}
inline void GXST_wrap_histogram(GXSTPtr self, int32_t arg1)
{
    self->histogram(arg1);
}
inline void GXST_wrap_histogram2(GXSTPtr self, int32_t arg1, double arg2, double arg3)
{
    self->histogram2(arg1, arg2, arg3);
}
inline double GXST_wrap_equivalent_percentile(GXSTPtr self, double arg1)
{
    double ret = self->equivalent_percentile(arg1);
    return ret;
}
inline double GXST_wrap_equivalent_value(GXSTPtr self, double arg1)
{
    double ret = self->equivalent_value(arg1);
    return ret;
}
inline void GXST_wrap_reset(GXSTPtr self)
{
    self->reset();
}
inline double GXST_wrap_get_info(GXSTPtr self, int32_t arg1)
{
    double ret = self->get_info((ST_INFO)arg1);
    return ret;
}
inline double GXST_wrap_get_norm_prob(double arg1)
{
    double ret = GXST::get_norm_prob(arg1);
    return ret;
}
inline double GXST_wrap_get_norm_prob_x(double arg1)
{
    double ret = GXST::get_norm_prob_x(arg1);
    return ret;
}
inline double GXST_wrap_normal_test(GXSTPtr self)
{
    double ret = self->normal_test();
    return ret;
}

void gxPythonImportGXST()
{

    class_<GXST, GXSTPtr> pyClass("GXST",
                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		Mono-variate statistics. The ST class is used to accumulate statistical\n"
                                  "   		information about a set of data. This class is usually used in conjunction\n"
                                  "   		with others. For instance, \\ :func:`geosoft.gxapi.GXDU.stat`\\  (see DU) will add a channel's\n"
                                  "   		data to the ST object, and sComputeST_IMG (see IMG) will compute\n"
                                  "   		statistics for a grid.\n"
                                  "   	\n\n"

                                  "\n\n**Note:**\n\n"

                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		\\ `*`\\ \\ `*`\\ \\ `*`\\  Histogram ranges and colour zone ranges \\ `*`\\ \\ `*`\\ \\ `*`\\ \n"
                                  "   \n"
                                  "   		Histogram bins are defined with inclusive minima and exclusive maxima;\n"
                                  "   		for instance if Min = 0 and Inc = 1, then the second bin would include\n"
                                  "   		all values z such that  0 >= z > 1 (the first bin has all values < 0).\n"
                                  "   \n"
                                  "   		Colour zones used in displaying grids (ITR, ZON etc...) are the\n"
                                  "   		opposite, with exclusive minima and inclusive maxima.\n"
                                  "   		For instance, if a zone is defined from 0 to 1, then it would\n"
                                  "   		contain all values of z such that 0 > z >= 1.\n"
                                  "   \n"
                                  "   		These definitions mean that it is impossible to perfectly assign\n"
                                  "   		ITR colours to individual bars of a histogram. The best work-around\n"
                                  "   		when the data values are integers is to define the colour zones using\n"
                                  "   		0.5 values between the integers. A general work-around is to make the\n"
                                  "   		number of histogram bins much larger than the number of colour zones.\n"
                                  "   \n"
                                  "   		See also  ST2 (bi-variate statistics)\n"
                                  "   	\n\n"
                                  , no_init);

    pyClass.def("null", &GXST::null, "null() -> GXST\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXST`\n\n:returns: A null :class:`geosoft.gxapi.GXST`\n:rtype: :class:`geosoft.gxapi.GXST`\n").staticmethod("null");
    pyClass.def("is_null", &GXST::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXST is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXST`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXST::_internal_handle);
    pyClass.def("create", &GXST_wrap_create,
                "create() -> GXST:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method creates a statistics object which is used to\n"
                "   					accumulate statistics.\n"
                "   				\n\n"

                ":returns: ST Object\n"
                ":rtype: :class:`geosoft.gxapi.GXST`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_exact", &GXST_wrap_create_exact,
                "create_exact() -> GXST:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method creates a statistics object which stores\n"
                "   					all values.\n"
                "   				\n\n"

                ":returns: ST Object\n"
                ":rtype: :class:`geosoft.gxapi.GXST`\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               ).staticmethod("create_exact");
    pyClass.def("data", &GXST_wrap_data,
                "data((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add this value to the statistics object.\n\n"

                ":param arg1: Value to Add\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("data_vv", &GXST_wrap_data_vv,
                "data_vv((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add all the values in this VV to the statistics object.\n\n"

                ":param arg1: VV object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_histogram_bins", &GXST_wrap_get_histogram_bins,
                "get_histogram_bins((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve number of items in each hostogram bin\n\n"

                ":param arg1: VV for numbers of items\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The length of the returned VV is set to the total\n"
                "   					number of bins. If a histogram is not defined in\n"
                "   					the ST, then the returned length is zero.\n"
                "   				\n\n"
               );
    pyClass.def("get_histogram_info", &GXST_wrap_get_histogram_info,
                "get_histogram_info((int_ref)arg1, (float_ref)arg2, (float_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve number of bins, min and max value in histogram\n\n"

                ":param arg1: # of bins\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Min (value at start of 2nd bin)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Max (value at end of 2nd last bin)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The items correspond to those in \\ :func:`geosoft.gxapi.GXST.histogram2`\\ .\n"
                "   					If a histogram is not defined in\n"
                "   					the ST, then the returned number of bins is zero, and\n"
                "   					the min and max values will be dummies.\n"
                "   				\n\n"
               );
    pyClass.def("histogram", &GXST_wrap_histogram,
                "histogram((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method prepares ST for recording histogram.\n\n"

                ":param arg1: # of bins\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The Number of bins includes the one before the minimum\n"
                "   					and the one after the maximum, so it must be a value >2.\n"
                "   \n"
                "   					IMPORTANT: This function gets the histogram minimum and\n"
                "   					maximum from the current min and max values stored in the ST,\n"
                "   					so this is equivalent to calling\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXST.histogram2`\\ ( #bins, Min, (Max-Min)/(# bins -2));\n"
                "   \n"
                "   					You should already have the data loaded in order to call this\n"
                "   					function.\n"
                "   \n"
                "   					See the note above \"Histogram ranges and colour zone ranges\"\n"
                "   				\n\n"
               );
    pyClass.def("histogram2", &GXST_wrap_histogram2,
                "histogram2((int)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method prepares ST for recording histogram.\n\n"

                ":param arg1: # of bins\n"
                ":type arg1: int\n"
                ":param arg2: Min\n"
                ":type arg2: float\n"
                ":param arg3: Max\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The Number of bins includes the one before the minimum\n"
                "   					and the one after the maximum, so it must be a value >2.\n"
                "   					The width of the individual bins will be (Min-Max)/(# - 2)\n"
                "   \n"
                "   					See the note above \"Histogram ranges and colour zone ranges\"\n"
                "   				\n\n"
               );
    pyClass.def("equivalent_percentile", &GXST_wrap_equivalent_percentile,
                "equivalent_percentile((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Return corresponding Percentile for a Value.\n\n"

                ":param arg1: input value\n"
                ":type arg1: float\n"
                ":returns: The percentile at the given value (0 - 100)\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Statistics and histogram must have been calculated prior to\n"
                "   					calling this method\n"
                "   				\n\n"
               );
    pyClass.def("equivalent_value", &GXST_wrap_equivalent_value,
                "equivalent_value((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Return corresponding Value for a Percentile\n\n"

                ":param arg1: input percentile (0 - 100)\n"
                ":type arg1: float\n"
                ":returns: The value at the given percentile.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Statistics and histogram must have been calculated prior to\n"
                "   					calling this method\n"
                "   				\n\n"
               );
    pyClass.def("reset", &GXST_wrap_reset,
                "reset() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Resets the Statistics.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_info", &GXST_wrap_get_info,
                "get_info((int)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method allows you to retrieve (and compute) the\n"
                "   					information from the ST object.\n"
                "   				\n\n"

                ":param arg1: \\ :ref:`ST_INFO`\\ \n"
                ":type arg1: int\n"
                ":returns: Data you asked for\n"
                "          						GS_R8DM for none\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The following can only be determined if the ST has recorded\n"
                "   					a histogram: ST_MEDIAN, ST_MODE\n"
                "   \n"
                "   					ST_MINPOS can be used to retrieve the smallest value greater\n"
                "   					than zero, but not from ST objects recovered from serialized object.\n"
                "   				\n\n"
               );
    pyClass.def("get_norm_prob", &GXST_wrap_get_norm_prob,
                "get_norm_prob((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   return percent value\n\n"

                ":param arg1: real\n"
                ":type arg1: float\n"
                ":returns: real\n"
                "          \n"
                "          \n"
                "          						Notes			this function is based on Normal Cumulative distribution function\n"
                "          						mit to about 5 standard deviations\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               ).staticmethod("get_norm_prob");
    pyClass.def("get_norm_prob_x", &GXST_wrap_get_norm_prob_x,
                "get_norm_prob_x((float)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Return number of sigmas from 50% a given percent is\n\n"

                ":param arg1: real\n"
                ":type arg1: float\n"
                ":returns: real\n"
                "          \n"
                "          \n"
                "          						Notes			this function is based on Normal Cumulative distribution function\n"
                "          						mit to about 5 standard deviations\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               ).staticmethod("get_norm_prob_x");
    pyClass.def("normal_test", &GXST_wrap_normal_test,
                "normal_test() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Test the \"normality\" of the histogram distribution\n\n"

                ":returns: The normality statistic.\n"
                "          						Terminates if no histogram in the ST object.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function compares the histogram to a normal curve with the\n"
                "   					same mean and standard deviation. The individual counts are normalized\n"
                "   					by the total counts, the bin width and the standard deviation.\n"
                "   					For each bin, the rms difference between the expected probability and\n"
                "   					the normalized count is summed, and the final result is normalized by\n"
                "   					the total number of bins. In this way histograms with different means,\n"
                "   					standard deviations, number of bins and counts can be compared.\n"
                "   					If the histogram were perfectly normal, then a value of 0 would be returned.\n"
                "   					The more \"non-normal\", the higher the statistic.\n"
                "   				\n\n"
               );

    scope().attr("ST_ITEMS") = (int32_t)0;
    scope().attr("ST_NPOS") = (int32_t)1;
    scope().attr("ST_NZERO") = (int32_t)22;
    scope().attr("ST_DUMMIES") = (int32_t)2;
    scope().attr("ST_MIN") = (int32_t)3;
    scope().attr("ST_MAX") = (int32_t)4;
    scope().attr("ST_RANGE") = (int32_t)5;
    scope().attr("ST_MEAN") = (int32_t)6;
    scope().attr("ST_MEDIAN") = (int32_t)7;
    scope().attr("ST_MODE") = (int32_t)8;
    scope().attr("ST_GEOMEAN") = (int32_t)9;
    scope().attr("ST_VARIANCE") = (int32_t)10;
    scope().attr("ST_STDDEV") = (int32_t)11;
    scope().attr("ST_STDERR") = (int32_t)12;
    scope().attr("ST_SKEW") = (int32_t)13;
    scope().attr("ST_KURTOSIS") = (int32_t)14;
    scope().attr("ST_BASE") = (int32_t)15;
    scope().attr("ST_SUM") = (int32_t)16;
    scope().attr("ST_SUM2") = (int32_t)17;
    scope().attr("ST_SUM3") = (int32_t)18;
    scope().attr("ST_SUM4") = (int32_t)19;
    scope().attr("ST_MINPOS") = (int32_t)21;
    scope().attr("ST_HIST_MAXCOUNT") = (int32_t)100;

}
