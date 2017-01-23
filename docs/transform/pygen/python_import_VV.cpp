#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes




np::ndarray GXVV_wrap_get_data_np(GXVVPtr self, int32_t start, int32_t elements, object dtype)
{
    return self->get_data_np(start, elements, dtype);
}




void GXVV_wrap_set_data_np(GXVVPtr self, int32_t start, np::ndarray np_array)
{
    return self->set_data_np(start, np_array);
}


inline void GXVV_wrap_copy(GXVVPtr self, GXVVPtr arg1)
{
    self->copy(arg1);
}
inline void GXVV_wrap_copy2(GXVVPtr self, int32_t arg1, GXVVPtr arg2, int32_t arg3, int32_t arg4)
{
    self->copy2(arg1, arg2, arg3, arg4);
}
inline void GXVV_wrap_log(GXVVPtr self, int32_t arg1, int32_t arg2, double arg3)
{
    self->log((VV_LOG_BASE)arg1, (VV_LOG_NEGATIVE)arg2, arg3);
}
inline void GXVV_wrap_log_linear(GXVVPtr self, double arg1)
{
    self->log_linear(arg1);
}
inline void GXVV_wrap_mask(GXVVPtr self, GXVVPtr arg1)
{
    self->mask(arg1);
}
inline void GXVV_wrap_reverse(GXVVPtr self)
{
    self->reverse();
}
inline void GXVV_wrap_serial(GXVVPtr self, GXBFPtr arg1)
{
    self->serial(arg1);
}
inline void GXVV_wrap_trans(GXVVPtr self, double arg1, double arg2)
{
    self->trans(arg1, arg2);
}
inline void GXVV_wrap_abs(GXVVPtr self)
{
    self->abs();
}
inline void GXVV_wrap_add(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->add(arg1, arg2);
}
inline void GXVV_wrap_add2(GXVVPtr self, double arg1, GXVVPtr arg2, double arg3, GXVVPtr arg4)
{
    self->add2(arg1, arg2, arg3, arg4);
}
inline void GXVV_wrap_append(GXVVPtr self, GXVVPtr arg1)
{
    self->append(arg1);
}
inline int32_t GXVV_wrap_crc(GXVVPtr self, int32_t arg1)
{
    int32_t ret = self->crc(arg1);
    return ret;
}
inline int32_t GXVV_wrap_crc_inexact(GXVVPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    int32_t ret = self->crc_inexact(arg1, (VV_FLOAT_CRC_BITS)arg2, (VV_DOUBLE_CRC_BITS)arg3);
    return ret;
}
inline GXVVPtr GXVV_wrap_create(int32_t arg1, int32_t arg2)
{
    GXVVPtr ret = GXVV::create((GEO_VAR)arg1, arg2);
    return ret;
}
inline GXVVPtr GXVV_wrap_create_ext(int32_t arg1, int32_t arg2)
{
    GXVVPtr ret = GXVV::create_ext((GS_TYPES)arg1, arg2);
    return ret;
}
inline GXVVPtr GXVV_wrap_create_s(GXBFPtr arg1)
{
    GXVVPtr ret = GXVV::create_s(arg1);
    return ret;
}
inline void GXVV_wrap_diff(GXVVPtr self, int32_t arg1)
{
    self->diff(arg1);
}
inline void GXVV_wrap_divide(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->divide(arg1, arg2);
}
inline void GXVV_wrap_fid_norm(GXVVPtr self, GXVVPtr arg1)
{
    self->fid_norm(arg1);
}
inline void GXVV_wrap_fill_int(GXVVPtr self, int32_t arg1)
{
    self->fill_int(arg1);
}
inline void GXVV_wrap_fill_double(GXVVPtr self, double arg1)
{
    self->fill_double(arg1);
}
inline void GXVV_wrap_fill_string(GXVVPtr self, const gx_string_type& arg1)
{
    self->fill_string(arg1);
}
inline int32_t GXVV_wrap_count_dummies(GXVVPtr self, int32_t arg1, int32_t arg2)
{
    int32_t ret = self->count_dummies(arg1, arg2);
    return ret;
}
inline int32_t GXVV_wrap_find_dum(GXVVPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    int32_t ret = self->find_dum(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXVV_wrap_get_fid_expansion(GXVVPtr self)
{
    int32_t ret = self->get_fid_expansion();
    return ret;
}
inline int32_t GXVV_wrap_get_int(GXVVPtr self, int32_t arg1)
{
    int32_t ret = self->get_int(arg1);
    return ret;
}
inline void GXVV_wrap_get_string(GXVVPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_string(arg1, arg2);
}
inline int32_t GXVV_wrap_index_max(GXVVPtr self, float_ref& arg1)
{
    int32_t ret = self->index_max(arg1);
    return ret;
}
inline int32_t GXVV_wrap_length(GXVVPtr self)
{
    int32_t ret = self->length();
    return ret;
}
inline void GXVV_wrap_index_insert(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->index_insert(arg1, arg2);
}
inline void GXVV_wrap_index_order(GXVVPtr self, GXVVPtr arg1)
{
    self->index_order(arg1);
}
inline void GXVV_wrap_init_index(GXVVPtr self, int32_t arg1)
{
    self->init_index(arg1);
}
inline void GXVV_wrap_inv_log(GXVVPtr self, int32_t arg1, int32_t arg2, double arg3)
{
    self->inv_log((VV_LOG_BASE)arg1, (VV_LOG_NEGATIVE)arg2, arg3);
}
inline int32_t GXVV_wrap_order(GXVVPtr self, int_ref& arg1)
{
    VV_ORDER ret = self->order(arg1);
    return ret;
}
inline void GXVV_wrap_lines_to_xy(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->lines_to_xy(arg1, arg2);
}
inline void GXVV_wrap_lookup_index(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->lookup_index(arg1, arg2);
}
inline void GXVV_wrap_make_mem_based(GXVVPtr self)
{
    self->make_mem_based();
}
inline void GXVV_wrap_mask_and(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->mask_and(arg1, arg2);
}
inline void GXVV_wrap_mask_or(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->mask_or(arg1, arg2);
}
inline void GXVV_wrap_mask_str(GXVVPtr self, GXVVPtr arg1, const gx_string_type& arg2)
{
    self->mask_str(arg1, arg2);
}
inline void GXVV_wrap_multiply(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->multiply(arg1, arg2);
}
inline void GXVV_wrap_amplitude_3d(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    self->amplitude_3d(arg1, arg2, arg3);
}
inline void GXVV_wrap_polygon_mask(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2, GXPLYPtr arg3, int32_t arg4)
{
    self->polygon_mask(arg1, arg2, arg3, (VV_MASK)arg4);
}
inline void GXVV_wrap_project(GXPJPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    GXVV::project(arg1, arg2, arg3);
}
inline void GXVV_wrap_project_3d(GXPJPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4)
{
    GXVV::project_3d(arg1, arg2, arg3, arg4);
}
inline void GXVV_wrap_range_double(GXVVPtr self, float_ref& arg1, float_ref& arg2)
{
    self->range_double(arg1, arg2);
}
inline void GXVV_wrap_re_fid(GXVVPtr self, double arg1, double arg2, int32_t arg3)
{
    self->re_fid(arg1, arg2, arg3);
}
inline void GXVV_wrap_re_fid_vv(GXVVPtr self, GXVVPtr arg1)
{
    self->re_fid_vv(arg1);
}
inline void GXVV_wrap_re_sample(GXVVPtr self, double arg1, double arg2, double arg3, double arg4, int32_t arg5, int32_t arg6)
{
    self->re_sample(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline double GXVV_wrap_get_fid_incr(GXVVPtr self)
{
    double ret = self->get_fid_incr();
    return ret;
}
inline double GXVV_wrap_get_fid_start(GXVVPtr self)
{
    double ret = self->get_fid_start();
    return ret;
}
inline double GXVV_wrap_get_double(GXVVPtr self, int32_t arg1)
{
    double ret = self->get_double(arg1);
    return ret;
}
inline double GXVV_wrap_sum(GXVVPtr self)
{
    double ret = self->sum();
    return ret;
}
inline double GXVV_wrap_weighted_mean(GXVVPtr self, GXVVPtr arg1)
{
    double ret = self->weighted_mean(arg1);
    return ret;
}
inline void GXVV_wrap_set_fid_expansion(GXVVPtr self, int32_t arg1)
{
    self->set_fid_expansion(arg1);
}
inline void GXVV_wrap_set_fid_incr(GXVVPtr self, double arg1)
{
    self->set_fid_incr(arg1);
}
inline void GXVV_wrap_set_fid_start(GXVVPtr self, double arg1)
{
    self->set_fid_start(arg1);
}
inline void GXVV_wrap_set_int(GXVVPtr self, int32_t arg1, int32_t arg2)
{
    self->set_int(arg1, arg2);
}
inline void GXVV_wrap_set_int_n(GXVVPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    self->set_int_n(arg1, arg2, arg3);
}
inline void GXVV_wrap_set_len(GXVVPtr self, int32_t arg1)
{
    self->set_len(arg1);
}
inline void GXVV_wrap_set_double(GXVVPtr self, int32_t arg1, double arg2)
{
    self->set_double(arg1, arg2);
}
inline void GXVV_wrap_set_double_n(GXVVPtr self, int32_t arg1, int32_t arg2, double arg3)
{
    self->set_double_n(arg1, arg2, arg3);
}
inline void GXVV_wrap_set_string(GXVVPtr self, int32_t arg1, const gx_string_type& arg2)
{
    self->set_string(arg1, arg2);
}
inline void GXVV_wrap_set_string_n(GXVVPtr self, int32_t arg1, int32_t arg2, const gx_string_type& arg3)
{
    self->set_string_n(arg1, arg2, arg3);
}
inline void GXVV_wrap_setup_index(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2, int32_t arg3, double arg4)
{
    self->setup_index(arg1, arg2, (VV_LOOKUP)arg3, arg4);
}
inline void GXVV_wrap_sort(GXVVPtr self, int32_t arg1)
{
    self->sort((VV_SORT)arg1);
}
inline void GXVV_wrap_sort_index(GXVVPtr self, GXVVPtr arg1)
{
    self->sort_index(arg1);
}
inline void GXVV_wrap_sort_index1(GXVVPtr self, GXVVPtr arg1, int32_t arg2)
{
    self->sort_index1(arg1, (VV_SORT)arg2);
}
inline void GXVV_wrap_sort_index2(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2, int32_t arg3, int32_t arg4)
{
    self->sort_index2(arg1, arg2, (VV_SORT)arg3, (VV_SORT)arg4);
}
inline void GXVV_wrap_sort_index3(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    self->sort_index3(arg1, arg2, arg3, (VV_SORT)arg4, (VV_SORT)arg5, (VV_SORT)arg6);
}
inline void GXVV_wrap_sort_index4(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, int32_t arg5, int32_t arg6, int32_t arg7, int32_t arg8)
{
    self->sort_index4(arg1, arg2, arg3, arg4, (VV_SORT)arg5, (VV_SORT)arg6, (VV_SORT)arg7, (VV_SORT)arg8);
}
inline void GXVV_wrap_statistics(GXSTPtr arg1, GXVVPtr arg2)
{
    GXVV::statistics(arg1, arg2);
}
inline void GXVV_wrap_subtract(GXVVPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->subtract(arg1, arg2);
}
inline void GXVV_wrap_swap(GXVVPtr self)
{
    self->swap();
}
inline void GXVV_wrap_window(GXVVPtr self, double arg1, double arg2, int32_t arg3)
{
    self->window(arg1, arg2, (VV_WINDOW)arg3);
}
inline void GXVV_wrap_write_xml(GXVVPtr self, const gx_string_type& arg1, int32_t arg2, int32_t arg3)
{
    self->write_xml(arg1, arg2, arg3);
}

void gxPythonImportGXVV()
{

    class_<GXVV, GXVVPtr> pyClass("GXVV",
                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		The VV class stores very long vector (array) data (such\n"
                                  "   		as channel data from an OASIS database) in memory and\n"
                                  "   		performs specific actions on the data. This set of\n"
                                  "   		functions is similar to the VM functions except that\n"
                                  "   		you cannot access data directly and therefore you cannot\n"
                                  "   		use a VV to pass data to an external (non-Geosoft)\n"
                                  "   		Dynamic Link Library (DLL) object function.\n"
                                  "   \n"
                                  "   		If you want to pass data to a DLL, you must move a subset\n"
                                  "   		of the data stored in memory to a small vector object and\n"
                                  "   		then use the \\ :func:`geosoft.gxapi.GXGEO.get_ptr_vm`\\  function to pass a pointer to the\n"
                                  "   		data on to the external function.\n"
                                  "   \n"
                                  "   		See VVU for more utility methods.\n"
                                  "   	\n\n"
                                  , no_init);

    pyClass.def("null", &GXVV::null, "null() -> GXVV\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXVV`\n\n:returns: A null :class:`geosoft.gxapi.GXVV`\n:rtype: :class:`geosoft.gxapi.GXVV`\n").staticmethod("null");
    pyClass.def("is_null", &GXVV::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXVV is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXVV`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXVV::_internal_handle);


    pyClass.def("get_data_np", &GXVV_wrap_get_data_np, "get_data_np((int)start, (int)num_elements, (object)dtype) -> ndarray:\n"
                "\n"
                "Gets a `numpy ndarray <http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html>`_ from data in a VV.\n"
                "\n"
                ":param start: starting element\n"
                ":type start: int\n"
                ":param num_elements: number of elements to get\n"
                ":type num_elements: int\n"
                ":param dtype: object that describes the required `numpy datatype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ (e.g. np.float64)\n"
                ":type dtype: object\n"
                ":rtype: ndarray\n"
                "");




    pyClass.def("set_data_np", &GXVV_wrap_set_data_np, "set_data_np((int)start, (ndarray)array) -> None:\n"
                "\n"
                "Transfers data from `numpy ndarray <http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html>`_ into a VV.\n"
                "\n"
                ":param start: starting element\n"
                ":type start: int\n"
                ":param array: array of values to set into the VV\n"
                ":type array: ndarray\n"
                ":rtype: None\n"
                "");


    pyClass.def("copy", &GXVV_wrap_copy,
                "copy((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy one VV to another.\n\n"

                ":param arg1: source\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("copy2", &GXVV_wrap_copy2,
                "copy2((int)arg1, (GXVV)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy part of a vector into part of another vector.\n\n"

                ":param arg1: Destination start element\n"
                ":type arg1: int\n"
                ":param arg2: Source VV (can be the same as Destination)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Source start element\n"
                ":type arg3: int\n"
                ":param arg4: Number of points\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1. Unlike Copy_VV destination VV is not reallocated, nor is\n"
                "   					the length changed. The caller must make any desired changes.\n"
                "   \n"
                "   					2. All VV types are supported and will be converted using\n"
                "   					Convert_GS if necessary.\n"
                "   				\n\n"
               );
    pyClass.def("log", &GXVV_wrap_log,
                "log((int)arg1, (int)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply log to the vv.\n\n"

                ":param arg1: \\ :ref:`VV_LOG_BASE`\\ \n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`VV_LOG_NEGATIVE`\\ \n"
                ":type arg2: int\n"
                ":param arg3: minimum value for \\ :ref:`VV_LOG_NEGATIVE`\\ \n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Minimum value will be defaulted to 1.0 if it is 0.0 or\n"
                "   					less than 0.0\n"
                "   				\n\n"
               );
    pyClass.def("log_linear", &GXVV_wrap_log_linear,
                "log_linear((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Take the log10 or original value of a VV.\n\n"

                ":param arg1: minimum value\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the data is in the range +/- minimum value,\n"
                "   					it is left alone. Otherwise, the result is calculated as\n"
                "   \n"
                "   					d = dMin \\ `*`\\  (log10(fabs(d)/dMin)+1.0)\n"
                "   \n"
                "   					Sign is reapplied to d.\n"
                "   \n"
                "   					Minimum value will be defaulted to 1.0 if it is negative\n"
                "   					or 0.\n"
                "   				\n\n"
               );
    pyClass.def("mask", &GXVV_wrap_mask,
                "mask((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Mask one VV against another.\n\n"

                ":param arg1: Mask VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					All elements in the mask VV that are dummies will replace\n"
                "   					the value in the original VV with a dummy.\n"
                "   \n"
                "   					The modified VV will always be the same length as the mask\n"
                "   					VV after this call.  If the mask is longer than the target,\n"
                "   					the target will be lengthenned with dummies.\n"
                "   				\n\n"
               );
    pyClass.def("reverse", &GXVV_wrap_reverse,
                "reverse() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reverses the order of the data in a VV.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );
    pyClass.def("serial", &GXVV_wrap_serial,
                "serial((GXBF)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Serialize\n\n"

                ":param arg1: BF\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("trans", &GXVV_wrap_trans,
                "trans((float)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Translate (VV + base ) \\ `*`\\  mult\n\n"

                ":param arg1: base value\n"
                ":type arg1: float\n"
                ":param arg2: mult value\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   All VV types now supported.\n\n"
               );
    pyClass.def("abs", &GXVV_wrap_abs,
                "abs() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Take the absolute value of values in a VV.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               );
    pyClass.def("add", &GXVV_wrap_add,
                "add((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add two VVs: VV_A + VV_B = VV_C\n\n"

                ":param arg1: VV B\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV C (returned), C = A + B\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"
               );
    pyClass.def("add2", &GXVV_wrap_add2,
                "add2((float)arg1, (GXVV)arg2, (float)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add two VVs with linear factors: VV_A\\ `*`\\ f1 + VV_B\\ `*`\\ f2 = VV_C\n\n"

                ":param arg1: multiplier f1 for A\n"
                ":type arg1: float\n"
                ":param arg2: VV B\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: multiplier f2 for B\n"
                ":type arg3: float\n"
                ":param arg4: VV C (returned), C = A\\ `*`\\ f1 + B\\ `*`\\ f2\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The multipliers must be defined and within the GS_R8MN GS_R8MX range.\n\n"
               );
    pyClass.def("append", &GXVV_wrap_append,
                "append((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Appends VV's\n\n"

                ":param arg1: VV to append\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("crc", &GXVV_wrap_crc,
                "crc((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute the CRC value of a VV.\n\n"

                ":param arg1: previous CRC \\ :ref:`CRC_INIT_VALUE`\\ \n"
                ":type arg1: int\n"
                ":returns: CRC Value\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("crc_inexact", &GXVV_wrap_crc_inexact,
                "crc_inexact((int)arg1, (int)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Compute the CRC value of a VV and allows you to specify\n"
                "   					number of bits of floats/doubles to drop so that the CRC\n"
                "   					will be same even of this are changed.\n"
                "   				\n\n"

                ":param arg1: previous CRC \\ :ref:`CRC_INIT_VALUE`\\ \n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`VV_FLOAT_CRC_BITS`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`VV_DOUBLE_CRC_BITS`\\ \n"
                ":type arg3: int\n"
                ":returns: CRC Value\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Very usefull for testing where the last bits of accuracy\n"
                "   					are not as important.\n"
                "   				\n\n"
               );
    pyClass.def("create", &GXVV_wrap_create,
                "create((int)arg1, (int)arg2) -> GXVV:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a VV.\n\n"

                ":param arg1: \\ :ref:`GEO_VAR`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Maximum number of elements in the VV, >= 0\n"
                ":type arg2: int\n"
                ":returns: VV Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVV`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					To set the fiducial start and increment for the data in the VV\n"
                "   					you need to call \\ :func:`geosoft.gxapi.GXVV.set_fid_start`\\  and \\ :func:`geosoft.gxapi.GXVV.set_fid_incr`\\ .\n"
                "   \n"
                "   					If you are basing the VV data on fiducial information from a\n"
                "   					different VV, call GetFidStart_VV and GetFidIncr_VV to obtain\n"
                "   					that VV's fiducial information. Do this prior to setting the\n"
                "   					new VV's fiducial start and increment.\n"
                "   \n"
                "   					If you do not know the required length for a VV, use 0\n"
                "   					and the VV length will be adjusted as needed.  This is\n"
                "   					a bit less efficient than setting the length when you\n"
                "   					know it.\n"
                "   				\n\n"
               ).staticmethod("create");
    pyClass.def("create_ext", &GXVV_wrap_create_ext,
                "create_ext((int)arg1, (int)arg2) -> GXVV:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a VV, using one of the \\ :ref:`GS_TYPES`\\  special data types.\n\n"

                ":param arg1: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Maximum number of elements in the VV, >= 0\n"
                ":type arg2: int\n"
                ":returns: VV Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVV`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					See \\ :func:`geosoft.gxapi.GXVV.create`\\ \n"
                "   \n"
                "   					Do not use data type flags: GS_INT or GS_REAL on CreateExt(),\n"
                "   					this will result in a respective data type of unsigned byte or\n"
                "   					short for the VV.\n"
                "   				\n\n"
               ).staticmethod("create_ext");
    pyClass.def("create_s", &GXVV_wrap_create_s,
                "create_s((GXBF)arg1) -> GXVV:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a VV  from serialized source.\n\n"

                ":param arg1: BF\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: VV Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVV`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_s");
    pyClass.def("diff", &GXVV_wrap_diff,
                "diff((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate differences.\n\n"

                ":param arg1: Number of differences\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Differences with dummies result in dummies.\n"
                "   					An even number of differences locates data accurately.\n"
                "   					An odd number of differences locates result 1/2 element lower\n"
                "   					in the VV.\n"
                "   				\n\n"
               );
    pyClass.def("divide", &GXVV_wrap_divide,
                "divide((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Divide one VV by another: VV_A / VV_B = VV_C\n\n"

                ":param arg1: VV B\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV C (returned), C = A / B\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"
               );
    pyClass.def("fid_norm", &GXVV_wrap_fid_norm,
                "fid_norm((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Re-sample a pair of VV's to match each other.\n\n"

                ":param arg1: VV to resample\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Both VV's will return with the same start\n"
                "   					fid and fid increment.  The smaller start fid\n"
                "   					and fid increment will be used.\n"
                "   				\n\n"
               );
    pyClass.def("fill_int", &GXVV_wrap_fill_int,
                "fill_int((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill a VV with an int value.\n\n"

                ":param arg1: Value to fill with\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("fill_double", &GXVV_wrap_fill_double,
                "fill_double((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill a VV with a real value.\n\n"

                ":param arg1: Value to fill with\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("fill_string", &GXVV_wrap_fill_string,
                "fill_string((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill a VV with a string value.\n\n"

                ":param arg1: string\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("count_dummies", &GXVV_wrap_count_dummies,
                "count_dummies((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Count the number of dummies in a VV\n\n"

                ":param arg1: Starting point in VV (0 for all)\n"
                ":type arg1: int\n"
                ":param arg2: Number of elements to process (-1 for all)\n"
                ":type arg2: int\n"
                ":returns: The count\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("find_dum", &GXVV_wrap_find_dum,
                "find_dum((int)arg1, (int)arg2, (int)arg3, (int)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Finds the first dummy or non-dummy value in a VV\n\n"

                ":param arg1: Lowest element in VV element to search\n"
                ":type arg1: int\n"
                ":param arg2: Highest element in VV to search\n"
                ":type arg2: int\n"
                ":param arg3: 0 = find first dummy / 1 = find first non-dummy\n"
                ":type arg3: int\n"
                ":param arg4: 0 = use increasing order / 1 = use decreasing order\n"
                ":type arg4: int\n"
                ":returns: The index of the first dummy or non-dummy value.\n"
                "          						-1 if not found, 0 if the length of the VV is 0.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If a decreasing order search is performed, it will start\n"
                "   					at the highest element specified. (Conversely, an increasing\n"
                "   					order starts at the lowest element specified.)\n"
                "   				\n\n"
               );
    pyClass.def("get_fid_expansion", &GXVV_wrap_get_fid_expansion,
                "get_fid_expansion() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the Fiducial expansion from a VV\n\n"

                ":returns: Number of expanions for this VV (see ReFidVV_VV)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               );
    pyClass.def("get_int", &GXVV_wrap_get_int,
                "get_int((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an integer element from a VV.\n\n"

                ":param arg1: element wanted\n"
                ":type arg1: int\n"
                ":returns: Element wanted, or iDUMMY\n"
                "          						if the value is dummy or outside of the range of data.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_string", &GXVV_wrap_get_string,
                "get_string((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a string element from a VV.\n\n"

                ":param arg1: element wanted\n"
                ":type arg1: int\n"
                ":param arg2: string in which to place element\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns Element wanted, or blank string\n"
                "   					if the value is dummy or outside of the range of data.\n"
                "   \n"
                "   					Type conversions are performed if necessary.  Dummy values\n"
                "   					are converted to \"\\ `*`\\ \" string.\n"
                "   				\n\n"
               );
    pyClass.def("index_max", &GXVV_wrap_index_max,
                "index_max((float_ref)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the index where the maximum value occurs.\n\n"

                ":param arg1: Maximum value (rDUMMY if all dummies or no data)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Index of the maximum value, iDUMMY if no valid data.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If more than one value has the same maximum value, the index of the\n"
                "   					first is returned.\n"
                "   				\n\n"
               );
    pyClass.def("length", &GXVV_wrap_length,
                "length() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns current VV length.\n\n"

                ":returns: # of elements in the VV.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("index_insert", &GXVV_wrap_index_insert,
                "index_insert((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Insert items into a VV using an index VV.\n\n"

                ":param arg1: Data items to insert (must be same type as output data VV)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Index VV (must be type INT)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The items in the input data VV are inserted into\n"
                "   					the output VV using the indices in the index VV.\n"
                "   					Values not referenced are not altered, so the output\n"
                "   					VV should be pre-initialized. The output VV length\n"
                "   					will NOT be changed, and index values referencing\n"
                "   					beyond the end of the output VV data will return an\n"
                "   					error.\n"
                "   \n"
                "   					This function is useful when working with channel data that include\n"
                "   					dummies, but where the dummies must be removed before processing.\n"
                "   					Create and initialize an index (0, 1, 2...) VV, using the \\ :func:`geosoft.gxapi.GXVV.init_index`\\ \n"
                "   					function, and when you remove\n"
                "   					the dummies, remove the corresponding index values as well.\n"
                "   					After processing, init a VV to dummies, then use \\ :func:`geosoft.gxapi.GXVV.index_insert`\\  to\n"
                "   					put the processed values at the correct locations in the data VV\n"
                "   					before you write it back to the channel.\n"
                "   				\n\n"
               );
    pyClass.def("index_order", &GXVV_wrap_index_order,
                "index_order((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reorder a VV.\n\n"

                ":param arg1: VV to order\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Given an index VV (of type INT), this method reorders a\n"
                "   					VV. Please make sure that the index holds valid information.\n"
                "   				\n\n"
               );
    pyClass.def("init_index", &GXVV_wrap_init_index,
                "init_index((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Initialize an index VV to values 0, 1, 2, etc...\n\n"

                ":param arg1: Final length of VV (-1 to use current length).\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Populates a VV with the values 0, 1, 2, 3, 4 etc., to be\n"
                "   					used for various indexing functions, such as \\ :func:`geosoft.gxapi.GXVV.index_insert`\\  or\n"
                "   					\\ :func:`geosoft.gxapi.GXVV.index_order`\\ .\n"
                "   				\n\n"
               );
    pyClass.def("inv_log", &GXVV_wrap_inv_log,
                "inv_log((int)arg1, (int)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Inverse of the Log_VV function.\n\n"

                ":param arg1: \\ :ref:`VV_LOG_BASE`\\ \n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`VV_LOG_NEGATIVE`\\ \n"
                ":type arg2: int\n"
                ":param arg3: minimum value for \\ :ref:`VV_LOG_NEGATIVE`\\ \n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is the inverse function for Log_VV, with the same inputs.\n"
                "   \n"
                "   					NEGATIVE_NO    - will not return values smaller than the input minimum\n"
                "   					NEGATIVE_YES   - if the data is in the range +/- minimum,\n"
                "   					it is left alone.  Otherwise, the sign is removed,\n"
                "   					the minimum is subtracted, the log of the minimum is added,\n"
                "   					and the exponential (base e or base 10) is taken of the\n"
                "   					sum. The sign is then reapplied.\n"
                "   					Minimum value will be defaulted to 1.0 if it is 0.0 or\n"
                "   					less than 0.0\n"
                "   				\n\n"
               );
    pyClass.def("order", &GXVV_wrap_order,
                "order((int_ref)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Identifies the data size order of the elements.\n\n"

                ":param arg1: returned: Do any values repeat (0: No, 1: Yes)?\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: \\ :ref:`VV_ORDER`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               );
    pyClass.def("lines_to_xy", &GXVV_wrap_lines_to_xy,
                "lines_to_xy((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a 2D Line segment VV into X and Y VVs.\n\n"

                ":param arg1: output VV with X locations (GS_DOUBLE)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: output VV with Y locations (GS_DOUBLE)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Some GX functions (such as \\ :func:`geosoft.gxapi.GXTIN.get_voronoi_edges`\\ ) return\n"
                "   					a special VV where each element contains the start and end\n"
                "   					points of lines, (X_1, Y_1) and (X_2, Y_2).\n"
                "   					This GX dumps the individual X and Y values into individual\n"
                "   					X and Y VVs of type GS_DOUBLE (REAL). N lines produces 2\\ `*`\\ N\n"
                "   					X and Y values.\n"
                "   				\n\n"
               );
    pyClass.def("lookup_index", &GXVV_wrap_lookup_index,
                "lookup_index((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Lookup a VV from another VV using an index VV.\n\n"

                ":param arg1: Index VV of REAL\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Result VV (same type as Data VV)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method assigns index values of 0.0, 1.0, 2.0 etc. to the individual\n"
                "   					values in the input Data VV, and uses linear interpolation to calculate the values of\n"
                "   					Result VV at the input indices contained in the Index VV.\n"
                "   \n"
                "   					If the input Data VV is string type, then only values at the integral index values\n"
                "   					are returned.\n"
                "   \n"
                "   					See also \\ :func:`geosoft.gxapi.GXVV.setup_index`\\  for an example of how this can be implemented.\n"
                "   				\n\n"
               );
    pyClass.def("make_mem_based", &GXVV_wrap_make_mem_based,
                "make_mem_based() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Make this VV use regular instead of virtual memory.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function should be called immediately aftter\n"
                "   					\\ :func:`geosoft.gxapi.GXVV.create`\\ .\n"
                "   \n"
                "   					Normal VVs are optimised to prevent thrashing, and to\n"
                "   					efficiently support many extremely large VVs, although\n"
                "   					there is a small performance penalty.\n"
                "   					This function is intended for VV's that you know can be\n"
                "   					handled by the operating system virtual memory manager,\n"
                "   					and will be used heavily.  By using a memory based VV, you\n"
                "   					can achieve some performance improvements provided your\n"
                "   					application does not cause the memory manager to \"thrash\".\n"
                "   \n"
                "   					External programs that use the GX API may prefer to use\n"
                "   					memory-based VV's because you can get direct access to\n"
                "   					the VV through the \\ :func:`geosoft.gxapi.GXGEO.get_ptr_vv`\\  function (see gx_extern.h).\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXGEO.get_ptr_vv`\\  in gx_extern.h\n\n"
               );
    pyClass.def("mask_and", &GXVV_wrap_mask_and,
                "mask_and((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create mask from logical AND of two VVs.\n\n"

                ":param arg1: VV B\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV C (returned)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If both values are non-dummies, then result is 1, else dummy.\n\n"
               );
    pyClass.def("mask_or", &GXVV_wrap_mask_or,
                "mask_or((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create mask from logical OR of two VVs.\n\n"

                ":param arg1: VV B\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV C (returned)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If either values is non-dummy, then result is 1, else dummy.\n\n"
               );
    pyClass.def("mask_str", &GXVV_wrap_mask_str,
                "mask_str((GXVV)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Mask one VV against another using a string.\n\n"

                ":param arg1: Mask VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: String to compare\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					All elements in the mask VV that are same as string will replace\n"
                "   					the original VV with a 1.\n"
                "   \n"
                "   					The modified VV will always be expanded to the MaskVV size but\n"
                "   					not shortened after this call.  If the mask is longer than the target,\n"
                "   					the target will be lengthenned with dummies before applying the mask.\n"
                "   				\n\n"
               );
    pyClass.def("multiply", &GXVV_wrap_multiply,
                "multiply((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Multiply two VVs: VV_A \\ `*`\\  VV_B = VV_C\n\n"

                ":param arg1: VV B\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV C (returned), C = A \\ `*`\\  B\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"
               );
    pyClass.def("amplitude_3d", &GXVV_wrap_amplitude_3d,
                "amplitude_3d((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the 3D length for XYZ component VVs\n\n"

                ":param arg1: X component VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y component VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z component VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"
               );
    pyClass.def("polygon_mask", &GXVV_wrap_polygon_mask,
                "polygon_mask((GXVV)arg1, (GXVV)arg2, (GXPLY)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Mask a VV using XY data and a polygon\n\n"

                ":param arg1: Y VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV to be masked\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Polygon Object\n"
                ":type arg3: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg4: \\ :ref:`VV_MASK`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The VVs has to be the same length\n\n"
               );
    pyClass.def("project", &GXVV_wrap_project,
                "project((GXPJ)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method projects an X and Y VV.\n\n"

                ":param arg1: PJ\n"
                ":type arg1: :class:`geosoft.gxapi.GXPJ`\n"
                ":param arg2: X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function is equivalent to \\ :func:`geosoft.gxapi.GXPJ.convert_vv`\\ .\n\n"
               ).staticmethod("project");
    pyClass.def("project_3d", &GXVV_wrap_project_3d,
                "project_3d((GXPJ)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method projects an X,Y,Z VV.\n\n"

                ":param arg1: PJ\n"
                ":type arg1: :class:`geosoft.gxapi.GXPJ`\n"
                ":param arg2: X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Z\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function is equivalent to \\ :func:`geosoft.gxapi.GXPJ.convert_vv3`\\ .\n\n"
               ).staticmethod("project_3d");
    pyClass.def("range_double", &GXVV_wrap_range_double,
                "range_double((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the min. and max. values of a VV while ignoring dummies.\n\n"

                ":param arg1: minimum value - returned\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: maximum value - returned\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Minimum and maximum become GS_R8DM if entire VV is dummy.\n\n"
               );
    pyClass.def("re_fid", &GXVV_wrap_re_fid,
                "re_fid((float)arg1, (float)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Re-sample a VV to a new fid start/icrement\n\n"

                ":param arg1: New fid start\n"
                ":type arg1: float\n"
                ":param arg2: New fid increment\n"
                ":type arg2: float\n"
                ":param arg3: New length\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("re_fid_vv", &GXVV_wrap_re_fid_vv,
                "re_fid_vv((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Re-sample a VV to match another VV.\n\n"

                ":param arg1: VV model (fid increment and start)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method will honor the VV FID Expansion and will expand/contract\n"
                "   					VV's based on this flag if it is used.\n"
                "   				\n\n"
               );
    pyClass.def("re_sample", &GXVV_wrap_re_sample,
                "re_sample((float)arg1, (float)arg2, (float)arg3, (float)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Resamples a VV from one fid/incr to another fid/incr.\n\n"

                ":param arg1: Current start fid\n"
                ":type arg1: float\n"
                ":param arg2: Current increment\n"
                ":type arg2: float\n"
                ":param arg3: New fid start\n"
                ":type arg3: float\n"
                ":param arg4: New fid increment\n"
                ":type arg4: float\n"
                ":param arg5: New length\n"
                ":type arg5: int\n"
                ":param arg6: Extrapolate Endpoints (0 - No, 1 - Yes)\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.1\n\n"
               );
    pyClass.def("get_fid_incr", &GXVV_wrap_get_fid_incr,
                "get_fid_incr() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the Fiducial increment from a VV\n\n"

                ":returns: Fiducial increment of the VV.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_fid_start", &GXVV_wrap_get_fid_start,
                "get_fid_start() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the Fiducial start from a VV\n\n"

                ":returns: Fiducial start of the VV.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_double", &GXVV_wrap_get_double,
                "get_double((int)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a real element from a VV.\n\n"

                ":param arg1: element wanted\n"
                ":type arg1: int\n"
                ":returns: Element wanted, or rDUMMY\n"
                "          						if the value is dummy or outside of the range of data.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Type conversions are performed if necessary.  Dummy values\n"
                "   					are converted to \"\\ `*`\\ \" string.\n"
                "   				\n\n"
               );
    pyClass.def("sum", &GXVV_wrap_sum,
                "sum() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the sum of the values in a VV.\n\n"

                ":returns: The sum of the elements.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy value is treated as Zero(0)\n\n"
               );
    pyClass.def("weighted_mean", &GXVV_wrap_weighted_mean,
                "weighted_mean((GXVV)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the weighted average of the values.\n\n"

                ":param arg1: VV of weights\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: The weighted average of the values.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Dummy values are ignored.\n\n"
               );
    pyClass.def("set_fid_expansion", &GXVV_wrap_set_fid_expansion,
                "set_fid_expansion((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the Fiducial expansion from a VV\n\n"

                ":param arg1: Expansion setting (1 or greater)\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               );
    pyClass.def("set_fid_incr", &GXVV_wrap_set_fid_incr,
                "set_fid_incr((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the Fiducial increment of a VV\n\n"

                ":param arg1: New increment\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_fid_start", &GXVV_wrap_set_fid_start,
                "set_fid_start((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the Fiducial start of a VV\n\n"

                ":param arg1: New start\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_int", &GXVV_wrap_set_int,
                "set_int((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set an integer element in a VV.\n\n"

                ":param arg1: element to set\n"
                ":type arg1: int\n"
                ":param arg2: value to set\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Element being set cannot be < 0.\n"
                "   					If the element is > current VV length, the VV length is\n"
                "   					increased.\n"
                "   					It is good practice to set the length ahead of time to the\n"
                "   					expected maximum value, as some VV processes rely on the\n"
                "   					current maximum length of the VV when you pass it in as an\n"
                "   					argument, and unexpected results may occur if the length is\n"
                "   					not what you expect it to be because of dynamic allocation at\n"
                "   					an earlier time.\n"
                "   				\n\n"
               );
    pyClass.def("set_int_n", &GXVV_wrap_set_int_n,
                "set_int_n((int)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set N integer elements in a VV.\n\n"

                ":param arg1: start element (>= 0)\n"
                ":type arg1: int\n"
                ":param arg2: # elements to set (-1 sets all elements to end)\n"
                ":type arg2: int\n"
                ":param arg3: value to set\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Element being set cannot be < 0.\n"
                "   					If the element is > current VV length, the VV length is\n"
                "   					increased.\n"
                "   				\n\n"
               );
    pyClass.def("set_len", &GXVV_wrap_set_len,
                "set_len((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the length of a VV.\n\n"

                ":param arg1: New length (number of elements)\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If increasing the VV size, new elements are set to dummies.\n"
                "   \n"
                "   					It is good practice to set the length ahead of time to the\n"
                "   					expected maximum value, as some VV processes rely on the\n"
                "   					current maximum length of the VV when you pass it in as an\n"
                "   					argument, and unexpected results may occur if the length is\n"
                "   					not what you expect it to be because of dynamic allocation at\n"
                "   					an earlier time.\n"
                "   				\n\n"
               );
    pyClass.def("set_double", &GXVV_wrap_set_double,
                "set_double((int)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a real element in a VV.\n\n"

                ":param arg1: element to set\n"
                ":type arg1: int\n"
                ":param arg2: value to set\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Element being set cannot be < 0.\n"
                "   					If the element is > current VV length, the VV length is\n"
                "   					increased.\n"
                "   					It is good practice to set the length ahead of time to the\n"
                "   					expected maximum value, as some VV processes rely on the\n"
                "   					current maximum length of the VV when you pass it in as an\n"
                "   					argument, and unexpected results may occur if the length is\n"
                "   					not what you expect it to be because of dynamic allocation at\n"
                "   					an earlier time.\n"
                "   				\n\n"
               );
    pyClass.def("set_double_n", &GXVV_wrap_set_double_n,
                "set_double_n((int)arg1, (int)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set N real elements in a VV.\n\n"

                ":param arg1: start element (>= 0)\n"
                ":type arg1: int\n"
                ":param arg2: # elements to set (-1 sets all elements to end)\n"
                ":type arg2: int\n"
                ":param arg3: value to set\n"
                ":type arg3: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Element being set cannot be < 0.\n"
                "   					If the element is > current VV length, the VV length is\n"
                "   					increased.\n"
                "   				\n\n"
               );
    pyClass.def("set_string", &GXVV_wrap_set_string,
                "set_string((int)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a string element in a VV.\n\n"

                ":param arg1: element to set\n"
                ":type arg1: int\n"
                ":param arg2: string to set\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Element being set cannot be < 0.\n"
                "   					If the element is > current VV length, the VV length is\n"
                "   					increased.\n"
                "   					It is good practice to set the length ahead of time to the\n"
                "   					expected maximum value, as some VV processes rely on the\n"
                "   					current maximum length of the VV when you pass it in as an\n"
                "   					argument, and unexpected results may occur if the length is\n"
                "   					not what you expect it to be because of dynamic allocation at\n"
                "   					an earlier time.\n"
                "   				\n\n"
               );
    pyClass.def("set_string_n", &GXVV_wrap_set_string_n,
                "set_string_n((int)arg1, (int)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set N string elements in a VV.\n\n"

                ":param arg1: start element (>= 0)\n"
                ":type arg1: int\n"
                ":param arg2: # elements to set (-1 sets all elements to end)\n"
                ":type arg2: int\n"
                ":param arg3: string to set\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Element being set cannot be < 0.\n"
                "   					If the element is > current VV length, the VV length is\n"
                "   					increased.\n"
                "   				\n\n"
               );
    pyClass.def("setup_index", &GXVV_wrap_setup_index,
                "setup_index((GXVV)arg1, (GXVV)arg2, (int)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Setup an index VV from VV1 to VV2.\n\n"

                ":param arg1: Query VV (same type as Data VV)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV index VV of type REAL\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: \\ :ref:`VV_LOOKUP`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Spacing for some modes\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The input reference VV must be in ascending numerical order.\n"
                "   					If your reference data is NOT ordered, then use the the\n"
                "   					\\ :func:`geosoft.gxapi.GXVV.sort_index1`\\  function to create an order index, then sort\n"
                "   					both the reference and data VVs using this index VV before\n"
                "   					you call \\ :func:`geosoft.gxapi.GXVV.setup_index`\\ .\n"
                "   \n"
                "   					Example: You have a reference data set taken at specific times, hVVt, hVVy\n"
                "   					and you want to calculate/estimate/interpolate the values hVVy2 at a second set\n"
                "   					of times hVVt2\n"
                "   \n"
                "   					Step 1: Create an index, hVVi, type GS_DOUBLE, and call \\ :func:`geosoft.gxapi.GXVV.setup_index`\\ .\n"
                "   \n"
                "   					e.g. : \\ :func:`geosoft.gxapi.GXVV.setup_index`\\ (hVVt, hVVt2, hVVi, VV_LOOKUP_XXX, rSpacing);\n"
                "   \n"
                "   					Internally, this assigns index values of 0.0, 1.0, 2.0 etc. to the individual\n"
                "   					values in hVVt, then, depending on the lookup method chosen, assigns\n"
                "   					fractional index values to the input values in hVVt2.\n"
                "   \n"
                "   					Step 2: To determine what the lookup values hVVy2 should be at times hVVt2,\n"
                "   					call the sLookupIndex_VV function:\n"
                "   \n"
                "   					e.g. : \\ :func:`geosoft.gxapi.GXVV.lookup_index`\\ (hVVy, hVVi, hVVy2);\n"
                "   \n"
                "   					Internally, this assigns index values of 0.0, 1.0, 2.0 etc. to the individual\n"
                "   					values in hVVy, and uses linear interpolation to calculate the values of\n"
                "   					hVVy2 at the input indices contained in hVVi.\n"
                "   				\n\n"
               );
    pyClass.def("sort", &GXVV_wrap_sort,
                "sort((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sort a VV.\n\n"

                ":param arg1: \\ :ref:`VV_SORT`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"
               );
    pyClass.def("sort_index", &GXVV_wrap_sort_index,
                "sort_index((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sort index VV based on a data VV.\n\n"

                ":param arg1: Index VV of type INT\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Create an Index VV (of type GS_LONG) based on a data VV.\n"
                "   					This index vv can then be used by the IndexOrder method\n"
                "   					to order a group of VV's.\n"
                "   				\n\n"
               );
    pyClass.def("sort_index1", &GXVV_wrap_sort_index1,
                "sort_index1((GXVV)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sort index VV based on 1 data VV - set orders.\n\n"

                ":param arg1: Index VV of type INT\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: \\ :ref:`VV_SORT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Create an Index VV (of type GS_LONG) based on a data VV.\n"
                "   					This index vv can then be used by the IndexOrder method\n"
                "   					to order a group of VV's. The individual VVs may be ordered\n"
                "   					in ascending or descending order.\n"
                "   					If the primary VV values of two indices are the same, then\n"
                "   					the secondary VV values are compared. If the secondary values\n"
                "   					are the same, the ternary values are compared, etc.\n"
                "   				\n\n"
               );
    pyClass.def("sort_index2", &GXVV_wrap_sort_index2,
                "sort_index2((GXVV)arg1, (GXVV)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sort index VV based on 2 data VVs - set orders.\n\n"

                ":param arg1: Secondary Data VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Index VV of type INT\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Primary Sort order \\ :ref:`VV_SORT`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Secondary Sort order \\ :ref:`VV_SORT`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Create an Index VV (of type GS_LONG) based on a data VV.\n"
                "   					This index vv can then be used by the IndexOrder method\n"
                "   					to order a group of VV's. The individual VVs may be ordered\n"
                "   					in ascending or descending order.\n"
                "   					If the primary VV values of two indices are the same, then\n"
                "   					the secondary VV values are compared. If the secondary values\n"
                "   					are the same, the ternary values are compared, etc\n"
                "   				\n\n"
               );
    pyClass.def("sort_index3", &GXVV_wrap_sort_index3,
                "sort_index3((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sort index VV based on 3 data VVs - set orders.\n\n"

                ":param arg1: Secondary Data VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Ternary Data VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Index VV of type INT\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Primary Sort order \\ :ref:`VV_SORT`\\ \n"
                ":type arg4: int\n"
                ":param arg5: Secondary sort order \\ :ref:`VV_SORT`\\ \n"
                ":type arg5: int\n"
                ":param arg6: Third Sort order \\ :ref:`VV_SORT`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Create an Index VV (of type GS_LONG) based on a data VV.\n"
                "   					This index vv can then be used by the IndexOrder method\n"
                "   					to order a group of VV's. The individual VVs may be ordered\n"
                "   					in ascending or descending order.\n"
                "   					If the primary VV values of two indices are the same, then\n"
                "   					the secondary VV values are compared. If the secondary values\n"
                "   					are the same, the third values are compared, etc\n"
                "   				\n\n"
               );
    pyClass.def("sort_index4", &GXVV_wrap_sort_index4,
                "sort_index4((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (int)arg5, (int)arg6, (int)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sort index VV based on 4 data VVs - set orders.\n\n"

                ":param arg1: Secondary Data VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Ternary Data VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Quaternary Data VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Index VV of type INT\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Primary Ssort order \\ :ref:`VV_SORT`\\ \n"
                ":type arg5: int\n"
                ":param arg6: Secondary Sort order \\ :ref:`VV_SORT`\\ \n"
                ":type arg6: int\n"
                ":param arg7: Third Sort order \\ :ref:`VV_SORT`\\ \n"
                ":type arg7: int\n"
                ":param arg8: Fourth Sort order \\ :ref:`VV_SORT`\\ \n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Create an Index VV (of type GS_LONG) based on a data VV.\n"
                "   					This index vv can then be used by the IndexOrder method\n"
                "   					to order a group of VV's. The individual VVs may be ordered\n"
                "   					in ascending or descending order.\n"
                "   					If the primary VV values of two indices are the same, then\n"
                "   					the secondary VV values are compared. If the secondary values\n"
                "   					are the same, the third values are compared, etc\n"
                "   				\n\n"
               );
    pyClass.def("statistics", &GXVV_wrap_statistics,
                "statistics((GXST)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a VV to a ST.\n\n"

                ":param arg1: ST Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXST`\n"
                ":param arg2: VV to add to ST\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("statistics");
    pyClass.def("subtract", &GXVV_wrap_subtract,
                "subtract((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Subtract one VV from another: VV_A - VV_B = VV_C\n\n"

                ":param arg1: VV B\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VV C (returned), C = A - B\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"
               );
    pyClass.def("swap", &GXVV_wrap_swap,
                "swap() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Swaps the bytes of the SHORT, USHORT, LONG, FLOAT and DOUBLE vv's.\n"
                "   					Other vv's are not affected by this method. This is used\n"
                "   					primarily with changing the order of bytes for other machine\n"
                "   					created data.\n"
                "   				\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("window", &GXVV_wrap_window,
                "window((float)arg1, (float)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Limit the elements of a vv to a range.\n\n"

                ":param arg1: Min Val\n"
                ":type arg1: float\n"
                ":param arg2: Max Val\n"
                ":type arg2: float\n"
                ":param arg3: \\ :ref:`VV_WINDOW`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("write_xml", &GXVV_wrap_write_xml,
                "write_xml((str)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write the VV data as an XML object with bytes and formating.\n\n"

                ":param arg1: XML file to create\n"
                ":type arg1: str\n"
                ":param arg2: format\n"
                ":type arg2: int\n"
                ":param arg3: Significant digits/decimals\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               );

    scope().attr("VV_DOUBLE_CRC_BITS_EXACT") = (int32_t)0;
    scope().attr("VV_DOUBLE_CRC_BITS_DEFAULT") = (int32_t)10;
    scope().attr("VV_DOUBLE_CRC_BITS_MAX") = (int32_t)51;
    scope().attr("VV_FLOAT_CRC_BITS_EXACT") = (int32_t)0;
    scope().attr("VV_FLOAT_CRC_BITS_DEFAULT") = (int32_t)7;
    scope().attr("VV_FLOAT_CRC_BITS_MAX") = (int32_t)22;
    scope().attr("VV_LOG_BASE_10") = (int32_t)0;
    scope().attr("VV_LOG_BASE_E") = (int32_t)1;
    scope().attr("VV_LOG_NEGATIVE_NO") = (int32_t)0;
    scope().attr("VV_LOG_NEGATIVE_YES") = (int32_t)1;
    scope().attr("VV_LOOKUP_EXACT") = (int32_t)0;
    scope().attr("VV_LOOKUP_NEAREST") = (int32_t)1;
    scope().attr("VV_LOOKUP_INTERPOLATE") = (int32_t)2;
    scope().attr("VV_LOOKUP_NEARESTCLOSE") = (int32_t)3;
    scope().attr("VV_LOOKUP_INTERPCLOSE") = (int32_t)4;
    scope().attr("VV_MASK_INSIDE") = (int32_t)0;
    scope().attr("VV_MASK_OUTSIDE") = (int32_t)1;
    scope().attr("VV_ORDER_NONE") = (int32_t)0;
    scope().attr("VV_ORDER_INCREASING") = (int32_t)1;
    scope().attr("VV_ORDER_DECREASING") = (int32_t)2;
    scope().attr("VV_SORT_ASCENDING") = (int32_t)0;
    scope().attr("VV_SORT_DESCENDING") = (int32_t)1;
    scope().attr("VV_WINDOW_DUMMY") = (int32_t)0;
    scope().attr("VV_WINDOW_LIMIT") = (int32_t)1;

}
