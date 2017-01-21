#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXVVU_wrap_average_repeat(GXVVPtr arg1, GXVVPtr arg2)
{
    GXVVU::average_repeat(arg1, arg2);
}
inline void GXVVU_wrap_average_repeat_ex(GXVVPtr arg1, GXVVPtr arg2, int32_t arg3)
{
    GXVVU::average_repeat_ex(arg1, arg2, (VVU_MODE)arg3);
}
inline void GXVVU_wrap_average_repeat2(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    GXVVU::average_repeat2(arg1, arg2, arg3);
}
inline void GXVVU_wrap_average_repeat2_ex(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, int32_t arg4)
{
    GXVVU::average_repeat2_ex(arg1, arg2, arg3, (VVU_MODE)arg4);
}
inline void GXVVU_wrap_binary_search(GXVVPtr arg1, double arg2, int_ref& arg3, int_ref& arg4)
{
    GXVVU::binary_search(arg1, arg2, arg3, arg4);
}
inline void GXVVU_wrap_box_cox(GXVVPtr arg1, double arg2)
{
    GXVVU::box_cox(arg1, arg2);
}
inline void GXVVU_wrap_bp_filt(GXVVPtr arg1, GXVVPtr arg2, double arg3, double arg4, int32_t arg5)
{
    GXVVU::bp_filt(arg1, arg2, arg3, arg4, arg5);
}
inline void GXVVU_wrap_clip(GXVVPtr arg1, double arg2, double arg3, int32_t arg4)
{
    GXVVU::clip(arg1, arg2, arg3, (VVU_CLIP)arg4);
}
inline void GXVVU_wrap_clip_to_detect_limit(GXVVPtr arg1, double arg2, int32_t arg3)
{
    GXVVU::clip_to_detect_limit(arg1, arg2, arg3);
}
inline void GXVVU_wrap_decimate(GXVVPtr arg1, int32_t arg2)
{
    GXVVU::decimate(arg1, arg2);
}
inline void GXVVU_wrap_deviation(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, double arg4, double arg5, double arg6, double arg7, int32_t arg8)
{
    GXVVU::deviation(arg1, arg2, arg3, arg4, arg5, arg6, arg7, (VVU_LINE)arg8);
}
inline void GXVVU_wrap_distance(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, double arg4, double arg5, double arg6, double arg7)
{
    GXVVU::distance(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXVVU_wrap_distance_non_cumulative(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, double arg4, double arg5, double arg6, double arg7)
{
    GXVVU::distance_non_cumulative(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXVVU_wrap_distance_3d(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, double arg4, GXVVPtr arg5)
{
    GXVVU::distance_3d(arg1, arg2, arg3, arg4, arg5);
}
inline void GXVVU_wrap_find_gaps_3d(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, double arg4, GXVVPtr arg5)
{
    GXVVU::find_gaps_3d(arg1, arg2, arg3, arg4, arg5);
}
inline void GXVVU_wrap_dummy_range(GXVVPtr arg1, double arg2, double arg3, int32_t arg4, int32_t arg5)
{
    GXVVU::dummy_range(arg1, arg2, arg3, arg4, arg5);
}
inline void GXVVU_wrap_dummy_range_ex(GXVVPtr arg1, double arg2, double arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    GXVVU::dummy_range_ex(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXVVU_wrap_dummy_repeat(GXVVPtr arg1, int32_t arg2)
{
    GXVVU::dummy_repeat(arg1, (VVU_DUMMYREPEAT)arg2);
}
inline void GXVVU_wrap_dup_stats(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4)
{
    GXVVU::dup_stats(arg1, arg2, arg3, arg4);
}
inline void GXVVU_wrap_exp_dist(GXVVPtr arg1, int32_t arg2, double arg3, int32_t arg4)
{
    GXVVU::exp_dist(arg1, arg2, arg3, arg4);
}
inline void GXVVU_wrap_filter(GXVVPtr arg1, GXVVPtr arg2, GXFLTPtr arg3)
{
    GXVVU::filter(arg1, arg2, arg3);
}
inline void GXVVU_wrap_find_string_items(GXVVPtr arg1, GXVVPtr arg2, int32_t arg3, int32_t arg4, int32_t arg5, GXVVPtr arg6)
{
    GXVVU::find_string_items(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXVVU_wrap_fractal_filter(GXVVPtr arg1, int32_t arg2, int32_t arg3, GXVVPtr arg4)
{
    GXVVU::fractal_filter(arg1, arg2, arg3, arg4);
}
inline int32_t GXVVU_wrap_close_xy(GXVVPtr arg1, GXVVPtr arg2, double arg3, double arg4)
{
    int32_t ret = GXVVU::close_xy(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXVVU_wrap_close_xym(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, double arg4, double arg5)
{
    int32_t ret = GXVVU::close_xym(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline int32_t GXVVU_wrap_close_xyz(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, double arg4, double arg5, double arg6)
{
    int32_t ret = GXVVU::close_xyz(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline int32_t GXVVU_wrap_close_xyzm(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, double arg5, double arg6, double arg7)
{
    int32_t ret = GXVVU::close_xyzm(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
    return ret;
}
inline int32_t GXVVU_wrap_dummy_back_tracks(GXVVPtr arg1)
{
    int32_t ret = GXVVU::dummy_back_tracks(arg1);
    return ret;
}
inline int32_t GXVVU_wrap_find_dummy(GXVVPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    int32_t ret = GXVVU::find_dummy(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline void GXVVU_wrap_interp(GXVVPtr arg1, int32_t arg2, int32_t arg3)
{
    GXVVU::interp(arg1, (VVU_INTERP)arg2, (VVU_INTERP_EDGE)arg3);
}
inline int32_t GXVVU_wrap_qc_fill_gaps(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, double arg5)
{
    int32_t ret = GXVVU::qc_fill_gaps(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline int32_t GXVVU_wrap_search_text(GXVVPtr arg1, const gx_string_type& arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    int32_t ret = GXVVU::search_text(arg1, arg2, (VVU_CASE)arg3, (VVU_MATCH)arg4, arg5, arg6);
    return ret;
}
inline void GXVVU_wrap_mask(GXVVPtr arg1, GXVVPtr arg2)
{
    GXVVU::mask(arg1, arg2);
}
inline void GXVVU_wrap_mask_and(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    GXVVU::mask_and(arg1, arg2, arg3);
}
inline void GXVVU_wrap_mask_or(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    GXVVU::mask_or(arg1, arg2, arg3);
}
inline void GXVVU_wrap_nl_filt(GXVVPtr arg1, GXVVPtr arg2, int32_t arg3, double arg4)
{
    GXVVU::nl_filt(arg1, arg2, arg3, arg4);
}
inline void GXVVU_wrap_noise_check(GXVVPtr arg1, GXVVPtr arg2, double arg3, int32_t arg4)
{
    GXVVU::noise_check(arg1, arg2, arg3, arg4);
}
inline void GXVVU_wrap_noise_check2(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, double arg4, int32_t arg5)
{
    GXVVU::noise_check2(arg1, arg2, arg3, arg4, arg5);
}
inline void GXVVU_wrap_normal_dist(GXVVPtr arg1, int32_t arg2, double arg3, double arg4, int32_t arg5)
{
    GXVVU::normal_dist(arg1, arg2, arg3, arg4, arg5);
}
inline void GXVVU_wrap_offset_circles(GXVVPtr arg1, GXVVPtr arg2, double arg3, double arg4, GXVVPtr arg5, GXVVPtr arg6)
{
    GXVVU::offset_circles(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXVVU_wrap_offset_correct(GXVVPtr arg1, GXVVPtr arg2, double arg3, int32_t arg4, GXVVPtr arg5, GXVVPtr arg6)
{
    GXVVU::offset_correct(arg1, arg2, arg3, (VVU_OFFSET)arg4, arg5, arg6);
}
inline void GXVVU_wrap_offset_correct2(GXVVPtr arg1, GXVVPtr arg2, double arg3, double arg4, GXVVPtr arg5, GXVVPtr arg6)
{
    GXVVU::offset_correct2(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXVVU_wrap_offset_correct3(GXVVPtr arg1, GXVVPtr arg2, double arg3, double arg4, double arg5, GXVVPtr arg6, GXVVPtr arg7)
{
    GXVVU::offset_correct3(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXVVU_wrap_offset_correct_xyz(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, double arg4, double arg5, double arg6, double arg7, GXVVPtr arg8, GXVVPtr arg9, GXVVPtr arg10)
{
    GXVVU::offset_correct_xyz(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline void GXVVU_wrap_offset_rectangles(GXVVPtr arg1, GXVVPtr arg2, double arg3, double arg4, double arg5, GXVVPtr arg6, GXVVPtr arg7)
{
    GXVVU::offset_rectangles(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXVVU_wrap_pick_peak(GXVVPtr arg1, GXVVPtr arg2, double arg3, int32_t arg4)
{
    GXVVU::pick_peak(arg1, arg2, arg3, arg4);
}
inline void GXVVU_wrap_pick_peak2(GXVVPtr arg1, GXVVPtr arg2, double arg3, double arg4)
{
    GXVVU::pick_peak2(arg1, arg2, arg3, arg4);
}
inline void GXVVU_wrap_pick_peak3(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, double arg4, double arg5, GXVVPtr arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9)
{
    GXVVU::pick_peak3(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXVVU_wrap_poly_fill(GXVVPtr arg1, int32_t arg2, GXVVPtr arg3)
{
    GXVVU::poly_fill(arg1, arg2, arg3);
}
inline void GXVVU_wrap_poly_fill2(GXVVPtr arg1, GXVVPtr arg2, int32_t arg3, GXVVPtr arg4)
{
    GXVVU::poly_fill2(arg1, arg2, arg3, arg4);
}
inline void GXVVU_wrap_polygon_mask(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXPLYPtr arg4, int32_t arg5)
{
    GXVVU::polygon_mask(arg1, arg2, arg3, arg4, (VVU_MASK)arg5);
}
inline void GXVVU_wrap_prune(GXVVPtr arg1, GXVVPtr arg2, int32_t arg3)
{
    GXVVU::prune(arg1, arg2, (VVU_PRUNE)arg3);
}
inline void GXVVU_wrap_qc(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, double arg4, double arg5, double arg6, double arg7, int32_t arg8)
{
    GXVVU::qc(arg1, arg2, arg3, arg4, arg5, arg6, arg7, (QC_CRITERION)arg8);
}
inline void GXVVU_wrap_range_vector_mag(GXVVPtr arg1, GXVVPtr arg2, float_ref& arg3, float_ref& arg4)
{
    GXVVU::range_vector_mag(arg1, arg2, arg3, arg4);
}
inline void GXVVU_wrap_regress(GXVVPtr arg1, GXVVPtr arg2, float_ref& arg3, float_ref& arg4)
{
    GXVVU::regress(arg1, arg2, arg3, arg4);
}
inline void GXVVU_wrap_rel_var_dup(GXVVPtr arg1, GXVVPtr arg2, float_ref& arg3, int_ref& arg4)
{
    GXVVU::rel_var_dup(arg1, arg2, arg3, arg4);
}
inline void GXVVU_wrap_remove_dummy(GXVVPtr arg1)
{
    GXVVU::remove_dummy(arg1);
}
inline void GXVVU_wrap_remove_dummy2(GXVVPtr arg1, GXVVPtr arg2)
{
    GXVVU::remove_dummy2(arg1, arg2);
}
inline void GXVVU_wrap_remove_dummy3(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    GXVVU::remove_dummy3(arg1, arg2, arg3);
}
inline void GXVVU_wrap_remove_dummy4(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4)
{
    GXVVU::remove_dummy4(arg1, arg2, arg3, arg4);
}
inline void GXVVU_wrap_remove_dup(GXVVPtr arg1, GXVVPtr arg2, int32_t arg3)
{
    GXVVU::remove_dup(arg1, arg2, (VV_DUP)arg3);
}
inline void GXVVU_wrap_remove_xy_dup(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, int32_t arg4)
{
    GXVVU::remove_xy_dup(arg1, arg2, arg3, (VV_XYDUP)arg4);
}
inline void GXVVU_wrap_remove_xy_dup_index(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    GXVVU::remove_xy_dup_index(arg1, arg2, arg3);
}
inline void GXVVU_wrap_rolling_stats(GXVVPtr arg1, GXVVPtr arg2, int32_t arg3, int32_t arg4, int32_t arg5)
{
    GXVVU::rolling_stats(arg1, arg2, (ST_INFO)arg3, arg4, arg5);
}
inline void GXVVU_wrap_search_replace(GXVVPtr arg1, double arg2, double arg3)
{
    GXVVU::search_replace(arg1, arg2, arg3);
}
inline void GXVVU_wrap_search_replace_text(GXVVPtr arg1, int32_t arg2, int32_t arg3, const gx_string_type& arg4, const gx_string_type& arg5, int32_t arg6)
{
    GXVVU::search_replace_text(arg1, arg2, arg3, arg4, arg5, (VVU_SRCHREPL_CASE)arg6);
}
inline void GXVVU_wrap_search_replace_text_ex(GXVVPtr arg1, int32_t arg2, int32_t arg3, const gx_string_type& arg4, const gx_string_type& arg5, int32_t arg6, int_ref& arg7)
{
    GXVVU::search_replace_text_ex(arg1, arg2, arg3, arg4, arg5, (VVU_SRCHREPL_CASE)arg6, arg7);
}
inline void GXVVU_wrap_spline(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, int32_t arg4, double arg5, double arg6, double arg7, int32_t arg8, int32_t arg9)
{
    GXVVU::spline(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, (VVU_SPL)arg9);
}
inline void GXVVU_wrap_spline2(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, int32_t arg5)
{
    GXVVU::spline2(arg1, arg2, arg3, arg4, (VVU_SPL)arg5);
}
inline int32_t GXVVU_wrap_tokenize_to_values(GXVVPtr arg1, const gx_string_type& arg2)
{
    int32_t ret = GXVVU::tokenize_to_values(arg1, arg2);
    return ret;
}
inline void GXVVU_wrap_translate(GXVVPtr arg1, double arg2, double arg3)
{
    GXVVU::translate(arg1, arg2, arg3);
}
inline void GXVVU_wrap_trend(GXVVPtr arg1, int32_t arg2, GXVVPtr arg3)
{
    GXVVU::trend(arg1, arg2, arg3);
}
inline void GXVVU_wrap_trend2(GXVVPtr arg1, GXVVPtr arg2, int32_t arg3, GXVVPtr arg4)
{
    GXVVU::trend2(arg1, arg2, arg3, arg4);
}
inline void GXVVU_wrap_uniform_dist(GXVVPtr arg1, int32_t arg2, double arg3, double arg4, int32_t arg5)
{
    GXVVU::uniform_dist(arg1, arg2, arg3, arg4, arg5);
}

void gxPythonImportGXVVU()
{

    class_<GXVVU, boost::noncopyable> pyClass("GXVVU",
            "\n.. parsed-literal::\n\n"
            "   These methods are not a class. Utility methods perform\n"
            "   various operations on VV objects, including pruning,\n"
            "   splining, clipping and filtering.\n\n"
            , no_init);


    pyClass.def("average_repeat", &GXVVU_wrap_average_repeat,
                "average_repeat((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Average repeat values.\n\n"

                ":param arg1: reference VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: data VV to average\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Repeated values in the reference VV will be averaged\n"
                "   in the data VV.  The first value in the data VV will be set to the\n"
                "   average and subsequent data VV values will be dummied out.\n"
                "   Data is processed only to the minimum length of the\n"
                "   input VV lengths.\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXVVU.remove_dummy`\\ \n\n"
               ).staticmethod("average_repeat");
    pyClass.def("average_repeat_ex", &GXVVU_wrap_average_repeat_ex,
                "average_repeat_ex((GXVV)arg1, (GXVV)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Average repeat values.\n\n"

                ":param arg1: reference VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: data VV to average\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: \\ :ref:`VVU_MODE`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Repeated values in the reference VV will be set to the mean, median, minimum or maximum value\n"
                "   				 in the data VV.  For minimum and maximum, the index in the data VV containing the minimum or maximum value\n"
                "   				 is retained, and the other repeated values are dummied out. For mean and median, the first value in the \n"
                "   				 data VV will be reset and subsequent data VV values will be dummied out.\n"
                "   				 Data is processed only to the minimum length of the\n"
                "   				 input VV lengths.\n"
                "   			 \n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXVVU.remove_dummy`\\ \n\n"
               ).staticmethod("average_repeat_ex");
    pyClass.def("average_repeat2", &GXVVU_wrap_average_repeat2,
                "average_repeat2((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Average repeat values based on 2 reference channels.\n\n"

                ":param arg1: reference VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: reference VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: data VV to average\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Repeated values in the reference VV will be averaged\n"
                "   in the data VV.  The first value in the data VV will be set to the\n"
                "   average and subsequent data VV values will be dummied out.\n"
                "   Data is processed only to the minimum length of the\n"
                "   input VV lengths.\n"
                "   Both the reference VV values must repeat for the averageing\n"
                "   to occur. This version is useful for averaging on repeated\n"
                "   (X,Y) locations.\n\n"

                "\n.. seealso::\n\n"
                "   RemoveDummy_VV\n\n"
               ).staticmethod("average_repeat2");
    pyClass.def("average_repeat2_ex", &GXVVU_wrap_average_repeat2_ex,
                "average_repeat2_ex((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Average repeat values based on 2 reference channels.\n\n"

                ":param arg1: reference VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: reference VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: data VV to average\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: \\ :ref:`VVU_MODE`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Repeated values in the reference VV will be set to the mean, median, minimum or maximum value\n"
                "   				 in the data VV.  The first value in the data VV will be reset and subsequent data VV values will be dummied out.\n"
                "   				 Data is processed only to the minimum length of the\n"
                "   				 input VV lengths.\n"
                "   				 Both the reference VV values must repeat for the averageing\n"
                "   				 to occur. This version is useful for averaging on repeated\n"
                "   				 (X,Y) locations.\n"
                "   			 \n\n"

                "\n.. seealso::\n\n"
                "   RemoveDummy_VV\n\n"
               ).staticmethod("average_repeat2_ex");
    pyClass.def("binary_search", &GXVVU_wrap_binary_search,
                "binary_search((GXVV)arg1, (float)arg2, (int_ref)arg3, (int_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Search  numeric value in a VV.\n\n"

                ":param arg1: VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: value to search for.\n"
                ":type arg2: float\n"
                ":param arg3: Minmum Location\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Maximum Location\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The VV should be sorted.Search comparison is made on double\n"
                "   comparison of the data.\n\n"
               ).staticmethod("binary_search");
    pyClass.def("box_cox", &GXVVU_wrap_box_cox,
                "box_cox((GXVV)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Run Box-Cox (lambda) Transformation on VV.\n\n"

                ":param arg1: [i/o] VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: [i] Lambda Value\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               ).staticmethod("box_cox");
    pyClass.def("bp_filt", &GXVVU_wrap_bp_filt,
                "bp_filt((GXVV)arg1, (GXVV)arg2, (float)arg3, (float)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Band-pass filter to the specified.\n\n"

                ":param arg1: input VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: filtered VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Short wavelength cutoff, 0 for highpass\n"
                ":type arg3: float\n"
                ":param arg4: Long wavelength cutoff, 0 for lowpass\n"
                ":type arg4: float\n"
                ":param arg5: Filter Length, 0 for default length\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the short and long wavelengths are <= 0, the input channel\n"
                "   is simply copied to the output channel without filtering.\n"
                "   \n"
                "   The wavelengths are in fiducials.\n\n"
               ).staticmethod("bp_filt");
    pyClass.def("clip", &GXVVU_wrap_clip,
                "clip((GXVV)arg1, (float)arg2, (float)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clip a VV to a range.\n\n"

                ":param arg1: VV to clip\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: minimum value, rDUMMY for no minimum clip\n"
                ":type arg2: float\n"
                ":param arg3: maximum value, rDUMMY for no maximum clip\n"
                ":type arg3: float\n"
                ":param arg4: \\ :ref:`VVU_CLIP`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("clip");
    pyClass.def("clip_to_detect_limit", &GXVVU_wrap_clip_to_detect_limit,
                "clip_to_detect_limit((GXVV)arg1, (float)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply detection limit clipping of data.\n\n"

                ":param arg1: Input data vv (altered).\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Detection limit\n"
                ":type arg2: float\n"
                ":param arg3: Auto-convert negatives?\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Flow:\n"
                "   \n"
                "   1. If auto-converting negatives, then all negative values\n"
                "       are replaced by -0.5\\ `*`\\ value, and detection limit is ignored.\n"
                "   \n"
                "   2. If not auto-converting negatives, and the detection limit is not\n"
                "      rDUMMY, then values less than the detection limit are converted to\n"
                "      one-half the detection limit.\n"
                "   \n"
                "   This function is identical to \\ :func:`geosoft.gxapi.GXCHIMERA.clip_to_detect_limit`\\ .\n\n"
               ).staticmethod("clip_to_detect_limit");
    pyClass.def("decimate", &GXVVU_wrap_decimate,
                "decimate((GXVV)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Decimate a VV.\n\n"

                ":param arg1: VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: decimation factor (must be > 0)\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   For a decimation factor N, will remove all values except\n"
                "   those with indices equal to MN, where M is an integer.\n\n"
               ).staticmethod("decimate");
    pyClass.def("deviation", &GXVVU_wrap_deviation,
                "deviation((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate distance of point locations to a straight line\n\n"

                ":param arg1: X VV,REAL VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV,REAL VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Output deviation VV,REAL VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: X of 1st point to define straight line\n"
                ":type arg4: float\n"
                ":param arg5: Y of 1st point to define straight line\n"
                ":type arg5: float\n"
                ":param arg6: X of 2nd point or line azimuth in degrees (North is 0 degree)\n"
                ":type arg6: float\n"
                ":param arg7: Y of 2nd point or GS_R8DM if line azimuth is defined\n"
                ":type arg7: float\n"
                ":param arg8: \\ :ref:`VVU_LINE`\\ \n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("deviation");
    pyClass.def("distance", &GXVVU_wrap_distance,
                "distance((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a cumulative distance VV\n\n"

                ":param arg1: X VV,REAL VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV,REAL VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Output distance VV,REAL VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: X VV fid start\n"
                ":type arg4: float\n"
                ":param arg5: X VV fid incr\n"
                ":type arg5: float\n"
                ":param arg6: Y VV fid start\n"
                ":type arg6: float\n"
                ":param arg7: Y VV fid incr\n"
                ":type arg7: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("distance");
    pyClass.def("distance_non_cumulative", &GXVVU_wrap_distance_non_cumulative,
                "distance_non_cumulative((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a non cumulative distance VV i.e each\n"
                "   distance element is the distance of the corresponding\n"
                "   (X,Y) element and the previous element.\n\n"

                ":param arg1: X VV,REAL VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV,REAL VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Output distance VV,REAL VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: X VV fid start\n"
                ":type arg4: float\n"
                ":param arg5: X VV fid incr\n"
                ":type arg5: float\n"
                ":param arg6: Y VV fid start\n"
                ":type arg6: float\n"
                ":param arg7: Y VV fid incr\n"
                ":type arg7: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The fist distace element is rDUMMY.\n\n"
               ).staticmethod("distance_non_cumulative");
    pyClass.def("distance_3d", &GXVVU_wrap_distance_3d,
                "distance_3d((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (float)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a cumulative distance VV from X, Y and Z VVs\n\n"

                ":param arg1: X VV,REAL VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV,REAL VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z VV,REAL VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Distance at first location\n"
                ":type arg4: float\n"
                ":param arg5: Output distance VV,REAL VV\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The output VV is the length of the shortest X,Y or Z input VV.\n"
                "   Any values with dummies are ignored - the distance at that\n"
                "   point is equal to the distance at the previous valid point.\n"
                "   The returned VV is the cumulative straight-line distance\n"
                "   between the points. No re-sampling is performed.\n"
                "   VVs of any type are supported.\n"
                "   			 \n\n"
               ).staticmethod("distance_3d");
    pyClass.def("find_gaps_3d", &GXVVU_wrap_find_gaps_3d,
                "find_gaps_3d((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (float)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return indices of locations separated from previous locations by more than the input gap distance.\n\n"

                ":param arg1: X VV,REAL VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV,REAL VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z VV,REAL VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Gap size (must be greater than zero)\n"
                ":type arg4: float\n"
                ":param arg5: Returned indices of start of sections after gaps (INT VV)\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Locate the starting points of line segements determined by an input gap distance.\n"
                "   				 The returned indices indicate where to break the line, given an input gap.\n"
                "   				 The number of returned indices is one less than the number of line segments.\n"
                "   				 (So if there are no gaps the returned VV has zero length).\n"
                "   			 \n\n"
               ).staticmethod("find_gaps_3d");
    pyClass.def("dummy_range", &GXVVU_wrap_dummy_range,
                "dummy_range((GXVV)arg1, (float)arg2, (float)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values inside or outside a range in a VV\n\n"

                ":param arg1: VV handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Minimum range value\n"
                ":type arg2: float\n"
                ":param arg3: Maximum range value\n"
                ":type arg3: float\n"
                ":param arg4: If TRUE, dummy inside the range\n"
                ":type arg4: int\n"
                ":param arg5: If TRUE, include Min, Max in the range.\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the Inside flag is TRUE, values within the specified\n"
                "   range are set to dummy. If the inside flag is FALSE,\n"
                "   values outside the range are set to dummy.  If the Inclusive\n"
                "   flag is TRUE, then dMin and dMax are considered part of the\n"
                "   range. If it is FALSE, then < or > are used, and dMin and\n"
                "   dMax lie outside the range.\n\n"
               ).staticmethod("dummy_range");
    pyClass.def("dummy_range_ex", &GXVVU_wrap_dummy_range_ex,
                "dummy_range_ex((GXVV)arg1, (float)arg2, (float)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Like DummyRangeVVU, with inclusion options for both ends.\n\n"

                ":param arg1: VV handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Minimum range value\n"
                ":type arg2: float\n"
                ":param arg3: Maximum range value\n"
                ":type arg3: float\n"
                ":param arg4: If TRUE, dummy inside the range\n"
                ":type arg4: int\n"
                ":param arg5: If TRUE, include Min in the range.\n"
                ":type arg5: int\n"
                ":param arg6: If TRUE, include Max in the range.\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the Inside flag is TRUE, values within the specified\n"
                "   range are set to dummy. If the inside flag is FALSE,\n"
                "   values outside the range are set to dummy.  If the Inclusive\n"
                "   flag is TRUE, then dMin and dMax are considered part of the\n"
                "   range. If it is FALSE, then < or > are used, and dMin and\n"
                "   dMax lie outside the range.\n\n"
               ).staticmethod("dummy_range_ex");
    pyClass.def("dummy_repeat", &GXVVU_wrap_dummy_repeat,
                "dummy_repeat((GXVV)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   dummy repeat values in a VV.\n\n"

                ":param arg1: VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: \\ :ref:`VVU_DUMMYREPEAT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Either the first, middle or last point will be left.\n"
                "                     Use \\ :func:`geosoft.gxapi.GXVVU.interp`\\  to interpolate after if desired.\n\n"
               ).staticmethod("dummy_repeat");
    pyClass.def("dup_stats", &GXVVU_wrap_dup_stats,
                "dup_stats((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate means and differences for duplicate sample pairs\n\n"

                ":param arg1: Duplicate data VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Sample Type VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Mean values VV (returned)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Diff values VV (returned)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Created for duplicate sample handling in CHIMERA. On input,\n"
                "   a numeric VV containing data values, and a sample type VV.\n"
                "   Sample pairs have types \"1\" and \"2\". This routine searches for\n"
                "   types in order \"1 2 1 2\", and writes the mean values of pairs\n"
                "   to the mean value VV, and the differences with the mean (equal\n"
                "   values, negative and positive) to the difference VV. Results\n"
                "   for samples out of order, for unmatched values, or when the\n"
                "   sample type does not equal \"1\" or \"2\" are set to dummy.\n\n"
               ).staticmethod("dup_stats");
    pyClass.def("exp_dist", &GXVVU_wrap_exp_dist,
                "exp_dist((GXVV)arg1, (int)arg2, (float)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill with exponentially distributed values.\n\n"

                ":param arg1: VV object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Random number generator seed\n"
                ":type arg2: int\n"
                ":param arg3: Mean value of distribution (> 0.0)\n"
                ":type arg3: float\n"
                ":param arg4: Number of values (-1 for all)\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   VV is set to input length (except for -1)\n"
                "   See RAND for a short discription of the\n"
                "   random number generator used.\n\n"
               ).staticmethod("exp_dist");
    pyClass.def("filter", &GXVVU_wrap_filter,
                "filter((GXVV)arg1, (GXVV)arg2, (GXFLT)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply a convolution filter to a VV.\n\n"

                ":param arg1: input VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: filtered VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Filter handle (see FLT)\n"
                ":type arg3: :class:`geosoft.gxapi.GXFLT`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("filter");
    pyClass.def("find_string_items", &GXVVU_wrap_find_string_items,
                "find_string_items((GXVV)arg1, (GXVV)arg2, (int)arg3, (int)arg4, (int)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Searches a VV for items in a second VV, returns indices of those found.\n\n"

                ":param arg1: String VV in which to locate items\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: String VV Items to search for\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Is the first VV already sorted?\n"
                ":type arg3: int\n"
                ":param arg4: Is the second VV already sorted\n"
                ":type arg4: int\n"
                ":param arg5: Case tolerance for string comparisons\n"
                ":type arg5: int\n"
                ":param arg6: GS_LONG VV of returned indices into the first LST.\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This is a much more efficient way of determining if items in\n"
                "   one VV are found in a second, than by searching\n"
                "   repeatedly in a loop.\n"
                "   The returned GS_LONG VV contains the same number of items as\n"
                "   the \"search items\" VV, and contains -1 for items where the\n"
                "   value is not found, and the index of items that are found.\n"
                "   Comparisons are case-tolerant.\n"
                "   Non-string VVs are converted to string type VVs (element size 24) internally.\n"
                "   \n"
                "   The method requires that the VV items be sorted, and\n"
                "   will do so internally. Since the input VVs may already be sorted,\n"
                "   the method will run faster if this stage can be skipped.\n\n"
               ).staticmethod("find_string_items");
    pyClass.def("fractal_filter", &GXVVU_wrap_fractal_filter,
                "fractal_filter((GXVV)arg1, (int)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fractal filter a VV.\n\n"

                ":param arg1: [i] VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: [i] filter order\n"
                ":type arg2: int\n"
                ":param arg3: [i] filter number\n"
                ":type arg3: int\n"
                ":param arg4: [o] filtered VV\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               ).staticmethod("fractal_filter");
    pyClass.def("close_xy", &GXVVU_wrap_close_xy,
                "close_xy((GXVV)arg1, (GXVV)arg2, (float)arg3, (float)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the closest point to an input point (XY).\n\n"

                ":param arg1: X locations\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: input X\n"
                ":type arg3: float\n"
                ":param arg4: input Y\n"
                ":type arg4: float\n"
                ":returns: Index of closest point, -1 if no valid locations, or data is masked.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Input X and Y location VVs, and a location.\n"
                "   Returns the index of the point in the VV closest to the\n"
                "   input point.\n\n"
               ).staticmethod("close_xy");
    pyClass.def("close_xym", &GXVVU_wrap_close_xym,
                "close_xym((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (float)arg4, (float)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the closest point to an input point, with mask (XY).\n\n"

                ":param arg1: X locations\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Mask values\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: input X\n"
                ":type arg4: float\n"
                ":param arg5: input Y\n"
                ":type arg5: float\n"
                ":returns: Index of closest point, -1 if no valid locations, or data is masked.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Input X and Y location VVs, and a location.\n"
                "   Returns the index of the point in the VV closest to the\n"
                "   input point.\n"
                "   This skips points where the mask value is dummy.\n"
                "   If no valid points are in the VVs, or all the mask VV values\n"
                "   are dummy, the returned index is -1.\n\n"
               ).staticmethod("close_xym");
    pyClass.def("close_xyz", &GXVVU_wrap_close_xyz,
                "close_xyz((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (float)arg4, (float)arg5, (float)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the closest point to an input point (XYZ).\n\n"

                ":param arg1: X locations\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z locations\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: input X\n"
                ":type arg4: float\n"
                ":param arg5: input Y\n"
                ":type arg5: float\n"
                ":param arg6: input Z\n"
                ":type arg6: float\n"
                ":returns: Index of closest point, -1 if no valid locations, or data is masked.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Input X, Y and Z location VVs, and a location.\n"
                "   Returns the index of the point in the VV closest to the\n"
                "   input point.\n\n"
               ).staticmethod("close_xyz");
    pyClass.def("close_xyzm", &GXVVU_wrap_close_xyzm,
                "close_xyzm((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (float)arg5, (float)arg6, (float)arg7) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the closest point to an input point, with mask (XYZ).\n\n"

                ":param arg1: X locations\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z locations\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Mask values\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: input X\n"
                ":type arg5: float\n"
                ":param arg6: input Y\n"
                ":type arg6: float\n"
                ":param arg7: input Z\n"
                ":type arg7: float\n"
                ":returns: Index of closest point, -1 if no valid locations, or data is masked.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Input X, Y and Z location VVs, and a location.\n"
                "   Returns the index of the point in the VV closest to the\n"
                "   input point.\n"
                "   This skips points where the mask value is dummy.\n"
                "   If no valid points are in the VVs, or all the mask VV values\n"
                "   are dummy, the returned index is -1.\n\n"
               ).staticmethod("close_xyzm");
    pyClass.def("dummy_back_tracks", &GXVVU_wrap_dummy_back_tracks,
                "dummy_back_tracks((GXVV)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy all points that keep a VV from being monotonically increasing.\n\n"

                ":param arg1: VV handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: The number of items dummied in order to render the VV montonically increasing.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The VV length remains the same. Any point that is less than or equal to\n"
                "   the previous (valid) point in the VV is dummied.\n\n"
               ).staticmethod("dummy_back_tracks");
    pyClass.def("find_dummy", &GXVVU_wrap_find_dummy,
                "find_dummy((GXVV)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the first dummy\\ `|`\\ non-dummy value in VV\n\n"

                ":param arg1: VV handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: 0 increasing order 1 decreasing order\n"
                ":type arg2: int\n"
                ":param arg3: 0 to find the first dummy 1 find first non-dummy\n"
                ":type arg3: int\n"
                ":param arg4: start search range at element\n"
                ":type arg4: int\n"
                ":param arg5: end search range at element (-1 for last)\n"
                ":type arg5: int\n"
                ":returns: The index of the first dummy\\ `|`\\ non-dummy value in VV\n"
                "          -1 if not found or if length of VV is 0\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Start and end of range are always defined lowest\n"
                "   to largest even if decreasing search order.  To search\n"
                "   entire VV range, specify 0,-1.\n\n"
               ).staticmethod("find_dummy");
    pyClass.def("interp", &GXVVU_wrap_interp,
                "interp((GXVV)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replace all dummies by interpolating from valid data.\n\n"

                ":param arg1: input VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: \\ :ref:`VVU_INTERP`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`VVU_INTERP_EDGE`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Edge behaviour: Dummies at the ends are treated as follows\n"
                "   for various combinations of the inside and outside interpolation\n"
                "    choices:\n"
                "   \n"
                "     if ((iOutside==VV_INTERP_EDGE_NEAREST) \\ `|`\\ \\ `|`\\ \n"
                "         (iOutside==VV_INTERP_EDGE_SAME && iInside==VV_INTERP_NEAREST))\n"
                "   \n"
                "        // -- Set dummies to the same value as the last defined element\n"
                "   \n"
                "     else if ((iOutside==VV_INTERP_EDGE_LINEAR) \\ `|`\\ \\ `|`\\ \n"
                "              (iOutside==VV_INTERP_EDGE_SAME &&  iInside==VV_INTERP_LINEAR))\n"
                "   \n"
                "        // --- Set dummies using the slope of the last two defined elements\n"
                "   \n"
                "     endif\n"
                "   \n"
                "   In all other cases and combinations of the two interpolation\n"
                "   choices, the dummies are left \"as is\".\n\n"
               ).staticmethod("interp");
    pyClass.def("qc_fill_gaps", &GXVVU_wrap_qc_fill_gaps,
                "qc_fill_gaps((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (float)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate fill in line segments\n\n"

                ":param arg1: input/output X VV on which to operate Required in GS_DOUBLE or GS_FLOAT\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: input/output Y VV on which to operate In GS_DOUBLE or GS_FLOAT\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: input Flag VV Required in GS_BYTE\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: input Gap VV to use for locating the fill inline segments In GS_DOUBLE or GS_FLOAT\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Min segment length  (required)\n"
                ":type arg5: float\n"
                ":returns: 1 if error, 0 if successful\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The X & Y VVs are returned as the calculated fill in line segments.\n\n"
               ).staticmethod("qc_fill_gaps");
    pyClass.def("search_text", &GXVVU_wrap_search_text,
                "search_text((GXVV)arg1, (str)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Search for a text value in a VV\n\n"

                ":param arg1: VV to search\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Text to match\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`VVU_CASE`\\ \n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`VVU_MATCH`\\ \n"
                ":type arg4: int\n"
                ":param arg5: index to begin search (-1 for full VV)\n"
                ":type arg5: int\n"
                ":param arg6: 1: forward search, -1: backward search\n"
                ":type arg6: int\n"
                ":returns: Index of first matching text, -1 if not found.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Search comparison is made on string comparison\n"
                "   of the data. Returns index of first item matching\n"
                "   the input string.\n"
                "   If start index is -1 or dummy, then full VV is searched.\n"
                "   Use VVU_MATCH_INPUT_LENGTH to match the first part of a string.\n"
                "   This is also recommended for matching numerical values, since\n"
                "   the displayed value in the database may not be the same as the\n"
                "   stored value.\n\n"

                "\n.. seealso::\n\n"
                "   sSearchReplace_VV\n\n"
               ).staticmethod("search_text");
    pyClass.def("mask", &GXVVU_wrap_mask,
                "mask((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Mask dummies in one VV onto another.\n\n"

                ":param arg1: VV to be masked\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: mask reference VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   VV to mask will be resampled to reference VV if required.\n"
                "   The returned length of the VV to mask will be the shorter\n"
                "   of the reference VV or the mask VV.\n\n"
               ).staticmethod("mask");
    pyClass.def("mask_and", &GXVVU_wrap_mask_and,
                "mask_and((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create mask from logical AND of two VVs.\n\n"

                ":param arg1: VV A\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV B\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: VV C (returned)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If both values are non-dummies, then result is 1, else dummy.\n\n"
               ).staticmethod("mask_and");
    pyClass.def("mask_or", &GXVVU_wrap_mask_or,
                "mask_or((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create mask from logical OR of two VVs.\n\n"

                ":param arg1: VV A\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV B\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: VV C (returned)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If either values is non-dummy, then result is 1, else dummy.\n\n"
               ).staticmethod("mask_or");
    pyClass.def("nl_filt", &GXVVU_wrap_nl_filt,
                "nl_filt((GXVV)arg1, (GXVV)arg2, (int)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Applies a non-linear filter.\n\n"

                ":param arg1: input VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: filtered VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Filter Width\n"
                ":type arg3: int\n"
                ":param arg4: Filter Tolerance, 0 for 1% of Std. Dev.\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("nl_filt");
    pyClass.def("noise_check", &GXVVU_wrap_noise_check,
                "noise_check((GXVV)arg1, (GXVV)arg2, (float)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Check on deviation of data from variable background in a VV\n\n"

                ":param arg1: input VV on which to apply quality control Required in GS_DOUBLE or GS_FLOAT\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: output flag VV with result 0 and 1. Required in GS_BYTE\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: allowed deviation over a number of data points in input VV (next parameter). Must be >= 0.0\n"
                ":type arg3: float\n"
                ":param arg4: number of data points. Must be > 0\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function checks vertical deviation of data in input VV\n"
                "   against a moving straight line. The straight line at any time is\n"
                "   defined by two extreme points of a data segment.  Output VV will\n"
                "   be 0 if data point in input VV falls within the deviation,\n"
                "   otherwise, it will be 1.\n"
                "   Output VV will be 0 if the straight line is vertical.\n\n"
               ).staticmethod("noise_check");
    pyClass.def("noise_check2", &GXVVU_wrap_noise_check2,
                "noise_check2((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (float)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Like \\ :func:`geosoft.gxapi.GXVVU.noise_check`\\ , but returns maximum deviation at all points.\n\n"

                ":param arg1: input VV on which to apply quality control Required in GS_DOUBLE or GS_FLOAT\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: output flag VV with result 0 and 1. Required in GS_BYTE\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Output maximum deviation VV.\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: allowed deviation over a number of data points in input VV (next parameter). Must be >= 0.0\n"
                ":type arg4: float\n"
                ":param arg5: number of data points in the line segment. Must be > 0\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function checks vertical deviation of data in an input VV\n"
                "   against a moving straight line, where the X-axis value is\n"
                "   taken to be the data index, and the Y-axis value is the\n"
                "   input data VV value. The straight line is drawn between data points\n"
                "   at the ends of the line segment, whose length is an input.\n"
                "   \n"
                "   The output flag VV is set to 0 if data point in input VV falls within the\n"
                "   deviation for all the moving line segments of which it is a part, otherwise, it\n"
                "   will be set to 1.\n"
                "   \n"
                "   The output maximum deviation VV contains the maximum deviation at each point\n"
                "   for all the moving line segments that it is a part of.\n\n"
               ).staticmethod("noise_check2");
    pyClass.def("normal_dist", &GXVVU_wrap_normal_dist,
                "normal_dist((GXVV)arg1, (int)arg2, (float)arg3, (float)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill with normally (Gaussian) distributed values.\n\n"

                ":param arg1: VV object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Random number generator seed\n"
                ":type arg2: int\n"
                ":param arg3: Mean value of distribution\n"
                ":type arg3: float\n"
                ":param arg4: Variance of the distribution\n"
                ":type arg4: float\n"
                ":param arg5: Number of values (-1 for all)\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   VV is set to input length (except for -1)\n"
                "   See RAND for a short discription of the\n"
                "   random number generator used.\n\n"
               ).staticmethod("normal_dist");
    pyClass.def("offset_circles", &GXVVU_wrap_offset_circles,
                "offset_circles((GXVV)arg1, (GXVV)arg2, (float)arg3, (float)arg4, (GXVV)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get non-overlapping offset location for circular symbols.\n\n"

                ":param arg1: Input X locations\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Input Y locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: minimum offset distance\n"
                ":type arg3: float\n"
                ":param arg4: symbol radius\n"
                ":type arg4: float\n"
                ":param arg5: Output (offset) X locations\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Output (offset) Y locations\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Often on maps plotted symbols and text overlap each other.\n"
                "   This routine accepts of VV of locations and returns a new\n"
                "   set of locations offset from the originals, and guaranteed\n"
                "   not to overlap, given the size of the original symbols.\n"
                "   The returned offset X, Y\n"
                "   locations are offset from the original locations by\n"
                "   the minimum of a) the input offset, b) the input symbol\n"
                "   radius. This is to ensure that the original location is\n"
                "   never covered by the offset symbol.\n"
                "   \n"
                "   Care should be taken when choosing the symbol size, because\n"
                "   if the point density is too high, all the points will get\n"
                "   pushed to the outside edge and your plot will look like a\n"
                "   hedgehog (it also takes a lot longer!).\n\n"
               ).staticmethod("offset_circles");
    pyClass.def("offset_correct", &GXVVU_wrap_offset_correct,
                "offset_correct((GXVV)arg1, (GXVV)arg2, (float)arg3, (int)arg4, (GXVV)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Correct locations based on heading and fixed offset.\n\n"

                ":param arg1: Input X\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Input Y\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Offset distance\n"
                ":type arg3: float\n"
                ":param arg4: \\ :ref:`VVU_OFFSET`\\ \n"
                ":type arg4: int\n"
                ":param arg5: Output X\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Output Y\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   In many applications, measurements are taken with an instrument which\n"
                "   is towed behind, or pushed ahead of where the locations are recorded.\n"
                "   Use this function to estimate the actual location of the instrument.\n"
                "   The method determines the heading along the line, using a \"thinned\"\n"
                "   version of the line. The degree of thinning is based on the size of the\n"
                "   offset; the larger the offset, the greater the distance between sample\n"
                "   locations used to construct the thinned lined used for determining headings.\n"
                "   The thinned line is splined at a frequency greater than the sample\n"
                "   frequency, and the heading at any given point is determined from the\n"
                "   vector formed by the closest two points on the splined line. The\n"
                "   correction (behind, in front, left or right) is determined with respect\n"
                "   to the heading, and added to the original location.\n"
                "   \n"
                "   IF this method fails, no dummies, no duplicated locations, no reversals\n"
                "   are produced.\n"
                "   \n"
                "   The algorithm:\n"
                "   \n"
                "   1. Determine average distance between each point = D\n"
                "   2. Smoothing interval = MAX(2\\ `*`\\ D, Offset distance) = I\n"
                "   3. Thin input points to be at least the smoothing interval I apart from each other.\n"
                "   4. Smoothly re-interpolate the thinned points at five times the\n"
                "      original average distance D.\n"
                "   5. For each input point, calculate the bearing using the nearest points\n"
                "      on the smoothed curve\n\n"
               ).staticmethod("offset_correct");
    pyClass.def("offset_correct2", &GXVVU_wrap_offset_correct2,
                "offset_correct2((GXVV)arg1, (GXVV)arg2, (float)arg3, (float)arg4, (GXVV)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXVVU.offset_correct`\\ , but for an arbitrary offset angle.\n\n"

                ":param arg1: Input X\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Input Y\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Offset distance\n"
                ":type arg3: float\n"
                ":param arg4: Offset azimuth (degrees counter-clockwise from straight ahead)\n"
                ":type arg4: float\n"
                ":param arg5: Output X\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Output Y\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               ).staticmethod("offset_correct2");
    pyClass.def("offset_correct3", &GXVVU_wrap_offset_correct3,
                "offset_correct3((GXVV)arg1, (GXVV)arg2, (float)arg3, (float)arg4, (float)arg5, (GXVV)arg6, (GXVV)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXVVU.offset_correct2`\\ , but specify smoothing interval.\n\n"

                ":param arg1: Input X\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Input Y\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Offset distance\n"
                ":type arg3: float\n"
                ":param arg4: Offset azimuth (degrees counter-clockwise from straight ahead)\n"
                ":type arg4: float\n"
                ":param arg5: Averaging interval - rDUMMY for default\n"
                ":type arg5: float\n"
                ":param arg6: Output X\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Output Y\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See the algorithm note #2 above for the default smoothing interval.\n\n"
               ).staticmethod("offset_correct3");
    pyClass.def("offset_correct_xyz", &GXVVU_wrap_offset_correct_xyz,
                "offset_correct_xyz((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (GXVV)arg8, (GXVV)arg9, (GXVV)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Correct locations based on heading and fixed offset.\n\n"

                ":param arg1: Input X\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Input Y\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Input Z\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Offset along-track (+ve forward)\n"
                ":type arg4: float\n"
                ":param arg5: Offset across-track (+ve to the right)\n"
                ":type arg5: float\n"
                ":param arg6: Vertical Offset (+ve up)\n"
                ":type arg6: float\n"
                ":param arg7: Sampling interval - rDUMMY for default\n"
                ":type arg7: float\n"
                ":param arg8: Output X\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Output Y\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Output Z\n"
                ":type arg10: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 In many applications, measurements are taken with an instrument which\n"
                "   				 is towed behind, or pushed ahead of where the locations are recorded.\n"
                "   				 Use this function to estimate the actual location of the instrument.\n"
                "   				 The method determines the heading along the line, using a \"thinned\"\n"
                "   				 version of the line. The default degree of thinning is based on the size of the\n"
                "   				 offset; the larger the offset, the greater the distance between sample\n"
                "   				 locations used to construct the thinned lined used for determining headings.\n"
                "   				 The thinned line is splined at a frequency greater than the sample\n"
                "   				 frequency, and the heading at any given point is determined from the\n"
                "   				 vector formed by the closest two points on the splined line. The\n"
                "   				 correction (behind, in front, left or right) is determined with respect\n"
                "   				 to the heading, and added to the original location.\n"
                "   \n"
                "   				 IF this method fails, no dummies, no duplicated locations, no reversals\n"
                "   				 are produced.\n"
                "   \n"
                "   				 The algorithm:\n"
                "   \n"
                "   				 1. Determine average distance between each point = D\n"
                "   				 2. Default smoothing interval = MAX(2\\ `*`\\ D, Offset distance) = I\n"
                "   				 3. Thin input points to be at least the smoothing interval I apart from each other.\n"
                "   				 4. Smoothly re-interpolate the thinned points at five times the\n"
                "   				 original average distance D.\n"
                "   				 5. For each input point, calculate the bearing using the nearest points\n"
                "   				 on the smoothed curve\n"
                "   			 \n\n"
               ).staticmethod("offset_correct_xyz");
    pyClass.def("offset_rectangles", &GXVVU_wrap_offset_rectangles,
                "offset_rectangles((GXVV)arg1, (GXVV)arg2, (float)arg3, (float)arg4, (float)arg5, (GXVV)arg6, (GXVV)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get non-overlapping offset location for rectangular symbols.\n\n"

                ":param arg1: Input X locations\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Input Y locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: minimum offset distance\n"
                ":type arg3: float\n"
                ":param arg4: symbol X size (width)\n"
                ":type arg4: float\n"
                ":param arg5: symbol Y size (height)\n"
                ":type arg5: float\n"
                ":param arg6: Output (offset) X locations\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Output (offset) Y locations\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Often on maps plotted symbols and text overlap each other.\n"
                "   This routine accepts of VV of locations and returns a new\n"
                "   set of locations offset from the originals, and guaranteed\n"
                "   not to overlap, given the size of the original symbols.\n"
                "   The returned offset X, Y\n"
                "   locations are offset from the original locations by\n"
                "   the minimum of a) the input offset, b) the input symbol\n"
                "   X or Y size. This is to ensure that the original location is\n"
                "   never covered by the offset symbol. In addition, the offset\n"
                "   symbol is never place directly below the original location,\n"
                "   to make it easier to draw a connecting line.\n"
                "   \n"
                "   Care should be taken when choosing the symbol size, because\n"
                "   if the point density is too high, all the points will get\n"
                "   pushed to the outside edge and your plot will look like a\n"
                "   hedgehog (it also takes a lot longer!).\n\n"
               ).staticmethod("offset_rectangles");
    pyClass.def("pick_peak", &GXVVU_wrap_pick_peak,
                "pick_peak((GXVV)arg1, (GXVV)arg2, (float)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Find peaks in a VV - method one.\n\n"

                ":param arg1: input VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: returned peak VV, all dummies except peak points.\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: minimum value to accept (0.0 to find all)\n"
                ":type arg3: float\n"
                ":param arg4: minimum width to accept (1 to find all)\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Peaks are the maximum point within a sequence of\n"
                "   positive values in the input VV.  The width is the\n"
                "   number of points in the positive sequence.\n"
                "   \n"
                "   A VV may have to be pre-filtered before finding\n"
                "   the peak values:\n"
                "   \n"
                "   Use \\ :func:`geosoft.gxapi.GXVVU.bp_filt`\\  to smooth the data as required.\n"
                "   Use \\ :func:`geosoft.gxapi.GXVVU.filter`\\  to apply a Laplace filter\n"
                "   \"-0.5,1.0,-0.5\" to make curvature data.\n\n"
               ).staticmethod("pick_peak");
    pyClass.def("pick_peak2", &GXVVU_wrap_pick_peak2,
                "pick_peak2((GXVV)arg1, (GXVV)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Find peaks in a VV - method two.\n\n"

                ":param arg1: input VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: returned peak VV, all dummies except peak points.\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: base level to accept (0.0 to find all)\n"
                ":type arg3: float\n"
                ":param arg4: minimum amplitude to accept\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Peaks are the maximum point within a sequence of\n"
                "   values in the input VV. Maximum points must be above\n"
                "   the base level and have a local amplitude greater\n"
                "   than the minimum amplitude specified.\n"
                "   \n"
                "   A VV may have to be pre-filtered before finding\n"
                "   the peak values.\n\n"
               ).staticmethod("pick_peak2");
    pyClass.def("pick_peak3", &GXVVU_wrap_pick_peak3,
                "pick_peak3((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (float)arg4, (float)arg5, (GXVV)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Find peaks in a VV - method two, returning width and half-amplitude widths.\n\n"

                ":param arg1: [i] data VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: [i] X VV used to calculate distance\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: [i] Y VV used to calculate distance\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: [i] minimum value to accept (0.0 to find all)\n"
                ":type arg4: float\n"
                ":param arg5: [i] amplitude\n"
                ":type arg5: float\n"
                ":param arg6: [o] Indices with peak locations\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: [o] Amplitudes at the peaks\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: [o] Anomaly widths\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: [o] Anomaly half-amplitude widths\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Uses Method 2 above, but also returns the anomaly width (defined\n"
                "   as the distance between the surrounding troughs), and the\n"
                "   width at the half-amplitude. The half-amplitude width is\n"
                "   calculated in two parts, individually for each side based on\n"
                "   the distance from the maximum to the location where the\n"
                "   amplitude is mid-way between the maximum and trough.\n"
                "   \n"
                "   The returned VVs are packed; no dummies. Instead the\n"
                "   indicies of the peak locations are returned.\n\n"
               ).staticmethod("pick_peak3");
    pyClass.def("poly_fill", &GXVVU_wrap_poly_fill,
                "poly_fill((GXVV)arg1, (int)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill a VV with values from an n'th order polynomial, integral x.\n\n"

                ":param arg1: VV with output data. (Preset length)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: order of the polynomial 0-9\n"
                ":type arg2: int\n"
                ":param arg3: VV with polynomial coefficients (input)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The output VV length must be set as desired before calling.\n"
                "   \n"
                "   The X scale is unitless (1 per element), i.e. 0,1,2,3,...\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXVVU.trend`\\ , \\ :func:`geosoft.gxapi.GXVVU.trend2`\\ , \\ :func:`geosoft.gxapi.GXVVU.poly_fill2`\\ \n\n"
               ).staticmethod("poly_fill");
    pyClass.def("poly_fill2", &GXVVU_wrap_poly_fill2,
                "poly_fill2((GXVV)arg1, (GXVV)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill a VV with values from an n'th order polynomial, specified X\n\n"

                ":param arg1: VV with x spacing (input)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV with output data. (Preset length)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: order of the polynomial 0-9\n"
                ":type arg3: int\n"
                ":param arg4: VV with polynomial coefficients (order+1 values)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The output VV length must be set as desired before calling.\n"
                "   The X scale is defined by a X VV (see Trend_VV for unitless X).\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXVVU.trend`\\ , \\ :func:`geosoft.gxapi.GXVVU.trend2`\\ , \\ :func:`geosoft.gxapi.GXVVU.poly_fill`\\ \n\n"
               ).staticmethod("poly_fill2");
    pyClass.def("polygon_mask", &GXVVU_wrap_polygon_mask,
                "polygon_mask((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXPLY)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Mask a VV using XY data and a polygon.\n\n"

                ":param arg1: X VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: VV to be masked\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: PLY object\n"
                ":type arg4: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg5: \\ :ref:`VVU_MASK`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The VVs have to be the same length\n\n"
               ).staticmethod("polygon_mask");
    pyClass.def("prune", &GXVVU_wrap_prune,
                "prune((GXVV)arg1, (GXVV)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Prune values from a VV based on reference VV\n\n"

                ":param arg1: VV to prune\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Reference VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: \\ :ref:`VVU_PRUNE`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Pruning will shorten the VV by removing values\n"
                "   that are either dummy or non-dummy in the reference\n"
                "   VV\n\n"
               ).staticmethod("prune");
    pyClass.def("qc", &GXVVU_wrap_qc,
                "qc((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Qualit control on deviation of data from norm in a VV\n\n"

                ":param arg1: input VV on which to apply quality control Required in GS_DOUBLE or GS_FLOAT\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: distance VV (NULL if criterion #2 does not apply). In GS_DOUBLE or GS_FLOAT\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: output flag VV with result 0,1,2,3,-1,-2,-3. Required in GS_BYTE\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: nominal reading  (required, must not be GS_R8DM)\n"
                ":type arg4: float\n"
                ":param arg5: maximum tolerance/deviation applied to a single reading (criterion #1). GS_R8DM if criterion #1 does not apply. Otherwise, must be positive value including 0.0\n"
                ":type arg5: float\n"
                ":param arg6: allowed tolerance/deviation over a given distance (next parameter) (criterion #2). GS_R8DM if criterion #2 does not apply. Otherwise, must be positive value including 0.0\n"
                ":type arg6: float\n"
                ":param arg7: the specified distance. GS_R8DM if criterion #2 does not apply. Otherwise, must be positive value excluding 0.0\n"
                ":type arg7: float\n"
                ":param arg8: \\ :ref:`QC_CRITERION`\\ \n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function tests data in input VV against\n"
                "   two separate criteria. Each element of the output VV\n"
                "   will have one of the following indicators:\n"
                "   \n"
                "   Indicator  Meaning\n"
                "   ---------  --------\n"
                "     0        Input data passed both tests\n"
                "     1        The input data and is greater than the nominal value\n"
                "              plus maximum tolerance/deviation (Criterion #1)\n"
                "     2        The input data over a specified distance is greater than the\n"
                "                      nominal value plus allowed tolerance (Criterion #2)\n"
                "     3        The input data failed on above two tests\n"
                "    -1        The input data and is less than the nominal value\n"
                "              minus maximum tolerance (Criterion #1)\n"
                "    -2        The input data over a specified distance is less than the\n"
                "                      nominal value minus allowed tolerance (Criterion #2)\n"
                "    -3        The input data failed on above two tests\n\n"
               ).staticmethod("qc");
    pyClass.def("range_vector_mag", &GXVVU_wrap_range_vector_mag,
                "range_vector_mag((GXVV)arg1, (GXVV)arg2, (float_ref)arg3, (float_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the range of hypotenuse values of two VVs.\n\n"

                ":param arg1: First VV (X)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: First VV (Y)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Min value (returned)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Max value (returned)\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   For each value in the VVs, finds sqrt(dV1\\ `*`\\ dV1 + dV2\\ `*`\\ dV2)\n"
                "   and returns the min and max values.\n\n"
               ).staticmethod("range_vector_mag");
    pyClass.def("regress", &GXVVU_wrap_regress,
                "regress((GXVV)arg1, (GXVV)arg2, (float_ref)arg3, (float_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate linear regression through data\n\n"

                ":param arg1: X data\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y data\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: returns slope\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: returns intercept\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("regress");
    pyClass.def("rel_var_dup", &GXVVU_wrap_rel_var_dup,
                "rel_var_dup((GXVV)arg1, (GXVV)arg2, (float_ref)arg3, (int_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Estimate relative variance of duplicate sample pairs from a database.\n\n"

                ":param arg1: Data VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Sample Type VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Returned relative variance\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Returned number of duplicates used.\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Created for duplicate sample handling in CHIMERA. On input,\n"
                "   a numeric or text VV containing data values, and a sample type VV.\n"
                "   Sample pairs have types \"1\" and \"2\". This routine searches for\n"
                "   types in order \"1 2 1 2\", and calulates the unnormalized relative variance,\n"
                "   defined as the sum of the squared differences between duplicates\n"
                "   divided by the sum of the squared mean values of the duplicates.\n"
                "   (To get the true rel.var., divide by N-1, where N is the number of\n"
                "   duplicate pairs used.)\n"
                "   Samples out of order, unmatched pairs, or when the\n"
                "   sample type does not equal \"1\" or \"2\" are ignored.\n\n"
               ).staticmethod("rel_var_dup");
    pyClass.def("remove_dummy", &GXVVU_wrap_remove_dummy,
                "remove_dummy((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove dummy values from a VV\n\n"

                ":param arg1: VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("remove_dummy");
    pyClass.def("remove_dummy2", &GXVVU_wrap_remove_dummy2,
                "remove_dummy2((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove dummy values from 2 VVs.\n\n"

                ":param arg1: VV object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV object\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Removes all indices where either VV has a dummy, or is\n"
                "   not defined (due to length differences).\n\n"
               ).staticmethod("remove_dummy2");
    pyClass.def("remove_dummy3", &GXVVU_wrap_remove_dummy3,
                "remove_dummy3((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove dummy values from 3 VVs.\n\n"

                ":param arg1: VV object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV object\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: VV object\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Removes all indices where any VV has a dummy, or is\n"
                "   not defined (due to length differences).\n\n"
               ).staticmethod("remove_dummy3");
    pyClass.def("remove_dummy4", &GXVVU_wrap_remove_dummy4,
                "remove_dummy4((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove dummy values from 4 VVs.\n\n"

                ":param arg1: VV object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV object\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: VV object\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: VV object\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Removes all indices where any VV has a dummy, or is\n"
                "   not defined (due to length differences).\n\n"
               ).staticmethod("remove_dummy4");
    pyClass.def("remove_dup", &GXVVU_wrap_remove_dup,
                "remove_dup((GXVV)arg1, (GXVV)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove/average duplicate sample pairs from a database.\n\n"

                ":param arg1: Data VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Sample Type VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: \\ :ref:`VV_DUP`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Created for duplicate sample handling in CHIMERA. On input,\n"
                "   a numeric or text VV containing data values, and a sample type VV.\n"
                "   Sample pairs have types \"1\" and \"2\". This routine searches for\n"
                "   types in order \"1 2 1 2\", and replaces the pair of values in the\n"
                "   data VV according to the \\ :ref:`VV_DUP`\\  value.\n"
                "   Results for samples out of order, for unmatched pairs, or when the\n"
                "   sample type does not equal \"1\" or \"2\" remain unchanged.\n\n"
               ).staticmethod("remove_dup");
    pyClass.def("remove_xy_dup", &GXVVU_wrap_remove_xy_dup,
                "remove_xy_dup((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove/average duplicate samples with the same (X, Y).\n\n"

                ":param arg1: X VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: (optional) Z VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: \\ :ref:`VV_XYDUP`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Searches for duplicated (X, Y) locations and removes the\n"
                "   duplicates (can be more than just a pair). The \"Z\" values,\n"
                "   if defined, are treated according to the value of VV_XYDUP.\n"
                "   The returned VVs are shortened to the new length, without\n"
                "   duplicates.\n"
                "   The Z VV can be set to NULL on input, in which case it is ignored.\n\n"
               ).staticmethod("remove_xy_dup");
    pyClass.def("remove_xy_dup_index", &GXVVU_wrap_remove_xy_dup_index,
                "remove_xy_dup_index((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove duplicate samples with the same (X, Y) and update index.\n\n"

                ":param arg1: X VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Index VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Searches for duplicated (X, Y) locations and removes the\n"
                "   duplicates (can be more than just a pair). The Index VV is\n"
                "   updated accordingly .i.e if  (X,Y) location of Index[0] == Index[1]\n"
                "   Index[1] is removed.\n\n"
               ).staticmethod("remove_xy_dup_index");
    pyClass.def("rolling_stats", &GXVVU_wrap_rolling_stats,
                "rolling_stats((GXVV)arg1, (GXVV)arg2, (int)arg3, (int)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate a statistic in a rolling window.\n\n"

                ":param arg1: Input VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Output VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: \\ :ref:`ST_INFO`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Window size (>0, increased to nearest odd value)\n"
                ":type arg4: int\n"
                ":param arg5: Shrink window at ends (1:Yes, 0:No)\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the input VVs are not REAL, copies are made to\n"
                "   temporary REALs for processing.\n"
                "   \n"
                "   If the window size is even, it is increased by 1 so that the\n"
                "   output value is put at the exact center index of the window.\n"
                "   \n"
                "   Statistics are calculated on the values in a window\n"
                "   surrounding the individual data points.\n"
                "   \n"
                "   By shrinking the window at the ends, one-sided effects can be\n"
                "   eliminated. For instance, if the data is linear to begin with,\n"
                "   a rolling mean will not alter the original data.\n"
                "   However, if the window size is kept constant, then values\n"
                "   near the ends tend to be pulled up or down.\n"
                "   \n"
                "   With shrinking, the window is shrunk so that it always has the\n"
                "   same width on both sides of the data point under analysis;\n"
                "   at the end points the window width is 1, at the next point in\n"
                "   it is 3, and so on, until the full width is reached.\n"
                "   \n"
                "   The median value is calculated by sorting the valid data in\n"
                "   the window, then selecting the middle value. If the number\n"
                "   of valid data points is even, then the average of the two\n"
                "   central values is returned.\n"
                "   \n"
                "   The mode value is defined as the value which occurs most\n"
                "   frequently in the data. This value may not even exist, or\n"
                "   may not be unique. In this implementation, the following\n"
                "   algorithm is used: The valid data in the window is sorted\n"
                "   in ascending order. The number of occurrences of each data\n"
                "   value is tracked, and if it occurs more times than any\n"
                "   value, it becomes the modal value. If all\n"
                "   values are different, this procedure returns the smallest\n"
                "   value. If two or more values each have the same (maximum)\n"
                "   number of occurrences, then the smallest of these values is\n"
                "   returned.\n\n"
               ).staticmethod("rolling_stats");
    pyClass.def("search_replace", &GXVVU_wrap_search_replace,
                "search_replace((GXVV)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Search and replace numeric values in a VV.\n\n"

                ":param arg1: VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: value to replace\n"
                ":type arg2: float\n"
                ":param arg3: replacement\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Search comparison is made on double comparison\n"
                "   of the data.\n\n"

                "\n.. seealso::\n\n"
                "   SearchReplaceText_VV\n\n"
               ).staticmethod("search_replace");
    pyClass.def("search_replace_text", &GXVVU_wrap_search_replace_text,
                "search_replace_text((GXVV)arg1, (int)arg2, (int)arg3, (str)arg4, (str)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Search and replace text values in a VV\n\n"

                ":param arg1: VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: string format for numeric VV\n"
                ":type arg2: int\n"
                ":param arg3: decimals for formating numeric VV\n"
                ":type arg3: int\n"
                ":param arg4: formatted string to replace\n"
                ":type arg4: str\n"
                ":param arg5: replacement\n"
                ":type arg5: str\n"
                ":param arg6: \\ :ref:`VVU_SRCHREPL_CASE`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Search comparison is made on string comparison\n"
                "   of the data.\n\n"

                "\n.. seealso::\n\n"
                "   SearchReplace_VV\n\n"
               ).staticmethod("search_replace_text");
    pyClass.def("search_replace_text_ex", &GXVVU_wrap_search_replace_text_ex,
                "search_replace_text_ex((GXVV)arg1, (int)arg2, (int)arg3, (str)arg4, (str)arg5, (int)arg6, (int_ref)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Search and replace text values in a VV, count items changed.\n\n"

                ":param arg1: VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: string format for numeric VV\n"
                ":type arg2: int\n"
                ":param arg3: decimals for formating numeric VV\n"
                ":type arg3: int\n"
                ":param arg4: formatted string to replace\n"
                ":type arg4: str\n"
                ":param arg5: replacement\n"
                ":type arg5: str\n"
                ":param arg6: \\ :ref:`VVU_SRCHREPL_CASE`\\ \n"
                ":type arg6: int\n"
                ":param arg7: number of items replaced (returned)\n"
                ":type arg7: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Search comparison is made on a string comparison\n"
                "   of the data.\n\n"

                "\n.. seealso::\n\n"
                "   SearchReplaceText_VV\n\n"
               ).staticmethod("search_replace_text_ex");
    pyClass.def("spline", &GXVVU_wrap_spline,
                "spline((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (int)arg4, (float)arg5, (float)arg6, (float)arg7, (int)arg8, (int)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Spline a Y VV onto an X VV.\n\n"

                ":param arg1: X (no dummies)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y to be splined (no dummies)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y output\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: output Length\n"
                ":type arg4: int\n"
                ":param arg5: Starting Location\n"
                ":type arg5: float\n"
                ":param arg6: Separation Distance\n"
                ":type arg6: float\n"
                ":param arg7: Maximum gap to interpolate across\n"
                ":type arg7: float\n"
                ":param arg8: Number of elements to extend\n"
                ":type arg8: int\n"
                ":param arg9: \\ :ref:`VVU_SPL`\\ \n"
                ":type arg9: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("spline");
    pyClass.def("spline2", &GXVVU_wrap_spline2,
                "spline2((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Spline a Y VV onto an X VV. Uses specified values of X in X2\n\n"

                ":param arg1: X (no dummies)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y to be splined (no dummies)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: X2 (no dummies)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Y output\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: \\ :ref:`VVU_SPL`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               ).staticmethod("spline2");
    pyClass.def("tokenize_to_values", &GXVVU_wrap_tokenize_to_values,
                "tokenize_to_values((GXVV)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Tokenize a string based on any characters.\n\n"

                ":param arg1: VV to place values in\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: str - String to parse\n"
                ":type arg2: str\n"
                ":returns: number of tokens (length of VV)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				Parses a series of space, tab or comma-delimited values to a VV.\n"
                "   			 \n\n"
               ).staticmethod("tokenize_to_values");
    pyClass.def("translate", &GXVVU_wrap_translate,
                "translate((GXVV)arg1, (float)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Translate values in a VV\n\n"

                ":param arg1: VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: base\n"
                ":type arg2: float\n"
                ":param arg3: scale\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   (new VV) = ((old VV) + base) \\ `*`\\  scale\n\n"
               ).staticmethod("translate");
    pyClass.def("trend", &GXVVU_wrap_trend,
                "trend((GXVV)arg1, (int)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate an n'th order best-fit polynomial, integral x.\n\n"

                ":param arg1: VV with input data\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: order of the polynomial 0-9\n"
                ":type arg2: int\n"
                ":param arg3: VV to hold polynomial coefficients (returned).\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Returns coefficients c[0] .. c[n]\n"
                "   \n"
                "      Y(x) = c[0] + c[1]x + c[2](x\\ `*`\\ \\ `*`\\ 2) + ... + c[n](x\\ `*`\\ \\ `*`\\ n)\n"
                "   \n"
                "   The X scale is unitless (1 per element), i.e. 0,1,2,3,...\n"
                "   \n"
                "   The polynomial VV length is set to the number of coefficients\n"
                "   (order + 1)\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXVVU.poly_fill`\\ , \\ :func:`geosoft.gxapi.GXVVU.trend2`\\ , \\ :func:`geosoft.gxapi.GXVVU.poly_fill2`\\ \n\n"
               ).staticmethod("trend");
    pyClass.def("trend2", &GXVVU_wrap_trend2,
                "trend2((GXVV)arg1, (GXVV)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate an n'th order best-fit polynomial, specified X\n\n"

                ":param arg1: VV with x spacing (input)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV with input data\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: order of the polynomial 0-9\n"
                ":type arg3: int\n"
                ":param arg4: VV to hold polynomial coefficients (returned)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Returns coefficients c[0] .. c[n]\n"
                "   \n"
                "      Y(x) = c[0] + c[1]x + c[2](x\\ `*`\\ \\ `*`\\ 2) + ... + c[n](x\\ `*`\\ \\ `*`\\ n)\n"
                "   \n"
                "   The X scale is defined by a X VV (see Trend_VV for unitless X).\n"
                "   \n"
                "   The polynomial VV length is set to the number of coefficients\n"
                "   (order + 1)\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXVVU.poly_fill`\\ , \\ :func:`geosoft.gxapi.GXVVU.trend2`\\ , \\ :func:`geosoft.gxapi.GXVVU.poly_fill2`\\ \n\n"
               ).staticmethod("trend2");
    pyClass.def("uniform_dist", &GXVVU_wrap_uniform_dist,
                "uniform_dist((GXVV)arg1, (int)arg2, (float)arg3, (float)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill with uniformly distributed values.\n\n"

                ":param arg1: VV object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Random number generator seed\n"
                ":type arg2: int\n"
                ":param arg3: Minimum of range\n"
                ":type arg3: float\n"
                ":param arg4: Maximum of range\n"
                ":type arg4: float\n"
                ":param arg5: Number of values (-1 for all)\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   VV is set to input length (except for -1)\n"
                "   See rand.gxh for a short discription of the\n"
                "   random number generator used.\n\n"
               ).staticmethod("uniform_dist");

    scope().attr("QC_CRITERION_1") = (int32_t)0;
    scope().attr("QC_CRITERION_2") = (int32_t)1;
    scope().attr("QC_CRITERION_12") = (int32_t)2;
    scope().attr("TEM_ARRAY_VERTICALSOUNDING") = (int32_t)0;
    scope().attr("TEM_ARRAY_PROFILING") = (int32_t)1;
    scope().attr("TEM_ARRAY_BOREHOLE") = (int32_t)2;
    scope().attr("VV_DUP_AVERAGE") = (int32_t)0;
    scope().attr("VV_DUP_1") = (int32_t)1;
    scope().attr("VV_DUP_2") = (int32_t)2;
    scope().attr("VV_DUP_DUMMY") = (int32_t)3;
    scope().attr("VV_DUP_SAMPLE") = (int32_t)4;
    scope().attr("VV_XYDUP_AVERAGE") = (int32_t)0;
    scope().attr("VV_XYDUP_SUM") = (int32_t)1;
    scope().attr("VVU_CASE_TOLERANT") = (int32_t)0;
    scope().attr("VVU_CASE_SENSITIVE") = (int32_t)1;
    scope().attr("VVU_CLIP_DUMMY") = (int32_t)0;
    scope().attr("VVU_CLIP_LIMIT") = (int32_t)1;
    scope().attr("VVU_DUMMYREPEAT_FIRST") = (int32_t)0;
    scope().attr("VVU_DUMMYREPEAT_LAST") = (int32_t)1;
    scope().attr("VVU_DUMMYREPEAT_MIDDLE") = (int32_t)2;
    scope().attr("VVU_INTERP_NEAREST") = (int32_t)1;
    scope().attr("VVU_INTERP_LINEAR") = (int32_t)2;
    scope().attr("VVU_INTERP_CUBIC") = (int32_t)3;
    scope().attr("VVU_INTERP_AKIMA") = (int32_t)4;
    scope().attr("VVU_INTERP_PREDICT") = (int32_t)5;
    scope().attr("VVU_INTERP_EDGE_NONE") = (int32_t)0;
    scope().attr("VVU_INTERP_EDGE_SAME") = (int32_t)1;
    scope().attr("VVU_INTERP_EDGE_NEAREST") = (int32_t)2;
    scope().attr("VVU_INTERP_EDGE_LINEAR") = (int32_t)3;
    scope().attr("LINE_2_POINTS") = (int32_t)0;
    scope().attr("LINE_POINT_AZIMUTH") = (int32_t)1;
    scope().attr("VVU_MASK_INSIDE") = (int32_t)0;
    scope().attr("VVU_MASK_OUTSIDE") = (int32_t)1;
    scope().attr("VVU_MATCH_FULL_STRINGS") = (int32_t)0;
    scope().attr("VVU_MATCH_INPUT_LENGTH") = (int32_t)1;
    scope().attr("VVU_MODE_MEAN") = (int32_t)0;
    scope().attr("VVU_MODE_MEDIAN") = (int32_t)1;
    scope().attr("VVU_MODE_MAXIMUM") = (int32_t)2;
    scope().attr("VVU_MODE_MINIMUM") = (int32_t)3;
    scope().attr("VVU_OFFSET_FORWARD") = (int32_t)0;
    scope().attr("VVU_OFFSET_BACKWARD") = (int32_t)1;
    scope().attr("VVU_OFFSET_RIGHT") = (int32_t)2;
    scope().attr("VVU_OFFSET_LEFT") = (int32_t)3;
    scope().attr("VVU_PRUNE_DUMMY") = (int32_t)0;
    scope().attr("VVU_PRUNE_VALID") = (int32_t)1;
    scope().attr("VVU_SPL_LINEAR") = (int32_t)0;
    scope().attr("VVU_SPL_CUBIC") = (int32_t)1;
    scope().attr("VVU_SPL_AKIMA") = (int32_t)2;
    scope().attr("VVU_SPL_NEAREST") = (int32_t)3;
    scope().attr("VVU_SRCHREPL_CASE_TOLERANT") = (int32_t)0;
    scope().attr("VVU_SRCHREPL_CASE_SENSITIVE") = (int32_t)1;

}
