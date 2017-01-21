#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes




np::ndarray GXVA_wrap_get_array_np(GXVAPtr self, int32_t start_row, int32_t start_column, int32_t num_rows, int32_t num_columns, object dtype)
{
    return self->get_array_np(start_row, start_column, num_rows, num_columns, dtype);
}




void GXVA_wrap_set_array_np(GXVAPtr self, int32_t start_row, int32_t start_column, np::ndarray np_array)
{
    return self->set_array_np(start_row, start_column, np_array);
}


inline void GXVA_wrap_add_elevations_vv_to_depths(GXVAPtr self, GXVVPtr arg1, int32_t arg2)
{
    self->add_elevations_vv_to_depths(arg1, arg2);
}
inline void GXVA_wrap_append(GXVAPtr self, GXVAPtr arg1)
{
    self->append(arg1);
}
inline void GXVA_wrap_average(GXVAPtr self, GXVVPtr arg1, int32_t arg2)
{
    self->average(arg1, (VA_AVERAGE)arg2);
}
inline void GXVA_wrap_copy(GXVAPtr self, GXVAPtr arg1)
{
    self->copy(arg1);
}
inline void GXVA_wrap_copy2(GXVAPtr self, int32_t arg1, int32_t arg2, GXVAPtr arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    self->copy2(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline GXVAPtr GXVA_wrap_create(int32_t arg1, int32_t arg2, int32_t arg3)
{
    GXVAPtr ret = GXVA::create((GEO_VAR)arg1, arg2, arg3);
    return ret;
}
inline GXVAPtr GXVA_wrap_create_ext(int32_t arg1, int32_t arg2, int32_t arg3)
{
    GXVAPtr ret = GXVA::create_ext((GS_TYPES)arg1, arg2, arg3);
    return ret;
}
inline GXVAPtr GXVA_wrap_create_vv(GXVVPtr arg1, int32_t arg2, int32_t arg3)
{
    GXVAPtr ret = GXVA::create_vv(arg1, arg2, arg3);
    return ret;
}
inline GXVVPtr GXVA_wrap_get_full_vv(GXVAPtr self)
{
    GXVVPtr ret = self->get_full_vv();
    return ret;
}
inline void GXVA_wrap_get_vv(GXVAPtr self, int32_t arg1, int32_t arg2, GXVVPtr arg3)
{
    self->get_vv(arg1, (VA_OBJECT)arg2, arg3);
}
inline int32_t GXVA_wrap_col(GXVAPtr self)
{
    int32_t ret = self->col();
    return ret;
}
inline int32_t GXVA_wrap_get_int(GXVAPtr self, int32_t arg1, int32_t arg2)
{
    int32_t ret = self->get_int(arg1, arg2);
    return ret;
}
inline void GXVA_wrap_get_string(GXVAPtr self, int32_t arg1, int32_t arg2, str_ref& arg3)
{
    self->get_string(arg1, arg2, arg3);
}
inline int32_t GXVA_wrap_len(GXVAPtr self)
{
    int32_t ret = self->len();
    return ret;
}
inline void GXVA_wrap_index_order(GXVVPtr arg1, GXVAPtr arg2)
{
    GXVA::index_order(arg1, arg2);
}
inline void GXVA_wrap_lookup_index(GXVAPtr self, GXVVPtr arg1, GXVAPtr arg2)
{
    self->lookup_index(arg1, arg2);
}
inline void GXVA_wrap_range_double(GXVAPtr self, float_ref& arg1, float_ref& arg2)
{
    self->range_double(arg1, arg2);
}
inline void GXVA_wrap_re_fid(GXVAPtr self, double arg1, double arg2, int32_t arg3)
{
    self->re_fid(arg1, arg2, arg3);
}
inline void GXVA_wrap_reverse(GXVAPtr self)
{
    self->reverse();
}
inline double GXVA_wrap_get_fid_incr(GXVAPtr self)
{
    double ret = self->get_fid_incr();
    return ret;
}
inline double GXVA_wrap_get_fid_start(GXVAPtr self)
{
    double ret = self->get_fid_start();
    return ret;
}
inline double GXVA_wrap_get_double(GXVAPtr self, int32_t arg1, int32_t arg2)
{
    double ret = self->get_double(arg1, arg2);
    return ret;
}
inline void GXVA_wrap_set_fid_incr(GXVAPtr self, double arg1)
{
    self->set_fid_incr(arg1);
}
inline void GXVA_wrap_set_fid_start(GXVAPtr self, double arg1)
{
    self->set_fid_start(arg1);
}
inline void GXVA_wrap_set_int(GXVAPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    self->set_int(arg1, arg2, arg3);
}
inline void GXVA_wrap_set_ln(GXVAPtr self, int32_t arg1)
{
    self->set_ln(arg1);
}
inline void GXVA_wrap_set_double(GXVAPtr self, int32_t arg1, int32_t arg2, double arg3)
{
    self->set_double(arg1, arg2, arg3);
}
inline void GXVA_wrap_set_string(GXVAPtr self, int32_t arg1, int32_t arg2, const gx_string_type& arg3)
{
    self->set_string(arg1, arg2, arg3);
}
inline void GXVA_wrap_set_vv(GXVAPtr self, int32_t arg1, int32_t arg2, GXVVPtr arg3)
{
    self->set_vv(arg1, (VA_OBJECT)arg2, arg3);
}
inline void GXVA_wrap_trans(GXVAPtr self, double arg1, double arg2)
{
    self->trans(arg1, arg2);
}
inline void GXVA_wrap_window(GXVAPtr self, int32_t arg1, int32_t arg2, GXVVPtr arg3)
{
    self->window(arg1, arg2, arg3);
}
inline void GXVA_wrap_window2(GXVAPtr self, double arg1, double arg2, GXVVPtr arg3)
{
    self->window2(arg1, arg2, arg3);
}
inline int32_t GXVA_wrap_check_for_repeating(GXVAPtr self, GXVVPtr arg1, int32_t arg2, GXVVPtr arg3, double arg4)
{
    int32_t ret = self->check_for_repeating(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXVA_wrap_check_for_repeating2(GXVAPtr self, GXVVPtr arg1, int32_t arg2, GXVVPtr arg3, double arg4, int_ref& arg5, int_ref& arg6)
{
    int32_t ret = self->check_for_repeating2(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}

void gxPythonImportGXVA()
{

    class_<GXVA, GXVAPtr> pyClass("GXVA",
                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		The VA class is the 2-Dimensional analogue to the VV class.\n"
                                  "   		When displayed in a database, VA objects are displayed graphically\n"
                                  "   		as profiles, one to a cell, and can also be displayed one column of\n"
                                  "   		data at a time by specifying an index; e.g. CH[0]. A VA object is\n"
                                  "   		declared with a fixed number of columns, which cannot be altered.\n"
                                  "   		The number of rows, however can be changed, in the same way that\n"
                                  "   		the length of a VV can be changed. Data can be added or extracted\n"
                                  "   		using VVs, either by row or column.\n"
                                  "   \n"
                                  "   		A VA is used to store an array of data in which each element may have\n"
                                  "   		multiple elements.  For example, 256-channel radiometric data can\n"
                                  "   		be stored in a VA that is 256 elements wide.\n"
                                  "   	\n\n"
                                  , no_init);

    pyClass.def("null", &GXVA::null, "null() -> GXVA\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXVA`\n\n:returns: A null :class:`geosoft.gxapi.GXVA`\n:rtype: :class:`geosoft.gxapi.GXVA`\n").staticmethod("null");
    pyClass.def("is_null", &GXVA::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXVA is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXVA`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXVA::_internal_handle);


    pyClass.def("get_array_np", &GXVA_wrap_get_array_np, "get_array_np((int)start_row, (int)start_column, (int)num_rows, (int)num_columns, (object)dtype) -> ndarray:\n"
                "\n"
                "Gets a `numpy ndarray <http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html>`_ from data in a VA.\n"
                "\n"
                ":param start_row: starting row\n"
                ":type start_row: int\n"
                ":param start_column: starting column\n"
                ":type start_column: int\n"
                ":param num_rows: number of rows\n"
                ":type num_rows: int\n"
                ":param num_columns: number of columns\n"
                ":type num_columns: int\n"
                ":param dtype: object that describes the required `numpy datatype <http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html>`_ (e.g. np.float64)\n"
                ":type dtype: object\n"
                ":rtype: ndarray\n"
                "");




    pyClass.def("set_array_np", &GXVA_wrap_set_array_np, "set_array_np((int)start_row, (int)start_column, (ndarray)array) -> None:\n"
                "\n"
                "Transfers data from `numpy ndarray <http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html>`_ into a VA.\n"
                "\n"
                ":param start_row: starting row\n"
                ":type start_row: int\n"
                ":param start_column: starting column\n"
                ":type start_column: int\n"
                ":param array: array of values to set into the VA (has to be 2D)\n"
                ":type array: ndarray\n"
                ":rtype: None\n"
                "");


    pyClass.def("add_elevations_vv_to_depths", &GXVA_wrap_add_elevations_vv_to_depths,
                "add_elevations_vv_to_depths((GXVV)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add one VV value to each row of the VA, output true elevation.\n\n"

                ":param arg1: Elevations to add\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Use negative VA depths (0:No, 1:Yes)?\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Adds each value in an input elevation VV to all the values at\n"
                "   					the same fid in a depths VA. Includes an option for negative depths down\n"
                "   					(e.g. a relative level).\n"
                "   				\n\n"
               );
    pyClass.def("append", &GXVA_wrap_append,
                "append((GXVA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Appends VAs\n\n"

                ":param arg1: VA to append\n"
                ":type arg1: :class:`geosoft.gxapi.GXVA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the VAs have different numbers of columns, the smaller number\n"
                "   					is used in the copy operation.\n"
                "   				\n\n"
               );
    pyClass.def("average", &GXVA_wrap_average,
                "average((GXVV)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Average elements in a VA by row or column\n\n"

                ":param arg1: VV in which to place average results\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: \\ :ref:`VA_AVERAGE`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The output VV will be dimensioned by the number of\n"
                "   					rows or columns in the input VV depending on the\n"
                "   					\\ :ref:`VA_AVERAGE`\\  setting.\n"
                "   \n"
                "   					Dummies are not included in the average.\n"
                "   				\n\n"
               );
    pyClass.def("copy", &GXVA_wrap_copy,
                "copy((GXVA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy one VA to another.\n\n"

                ":param arg1: source\n"
                ":type arg1: :class:`geosoft.gxapi.GXVA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("copy2", &GXVA_wrap_copy2,
                "copy2((int)arg1, (int)arg2, (GXVA)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy part of a vector into part of another vector.\n\n"

                ":param arg1: Destination start row\n"
                ":type arg1: int\n"
                ":param arg2: Destination start column\n"
                ":type arg2: int\n"
                ":param arg3: Source VA (can be the same as Destination)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVA`\n"
                ":param arg4: Source start row\n"
                ":type arg4: int\n"
                ":param arg5: Source start column\n"
                ":type arg5: int\n"
                ":param arg6: Number of rows\n"
                ":type arg6: int\n"
                ":param arg7: Number of columns\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					1. Unlike \\ :func:`geosoft.gxapi.GXVA.copy`\\  destination VA is not reallocated, nor are\n"
                "   					the dimensions changed. The caller must make any desired changes.\n"
                "   \n"
                "   					2. All VA types are supported and will be converted using\n"
                "   					Convert_GS if necessary.\n"
                "   				\n\n"
               );
    pyClass.def("create", &GXVA_wrap_create,
                "create((int)arg1, (int)arg2, (int)arg3) -> GXVA:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a VA.\n\n"

                ":param arg1: \\ :ref:`GEO_VAR`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Maximum number of rows in the VA, >= 0\n"
                ":type arg2: int\n"
                ":param arg3: Number of columns in the VA, > 0\n"
                ":type arg3: int\n"
                ":returns: VA Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVA`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_ext", &GXVA_wrap_create_ext,
                "create_ext((int)arg1, (int)arg2, (int)arg3) -> GXVA:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a VA, using one of the \\ :ref:`GS_TYPES`\\  special data types.\n\n"

                ":param arg1: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Maximum number of rows in the VA, >= 0\n"
                ":type arg2: int\n"
                ":param arg3: Number of columns in the VA, > 0\n"
                ":type arg3: int\n"
                ":returns: VA, aborts if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXVA`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See \\ :func:`geosoft.gxapi.GXVV.create`\\ \n\n"
               ).staticmethod("create_ext");
    pyClass.def("create_vv", &GXVA_wrap_create_vv,
                "create_vv((GXVV)arg1, (int)arg2, (int)arg3) -> GXVA:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a VA using the data in a VV.\n\n"

                ":param arg1: VV with the data\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: # of rows\n"
                ":type arg2: int\n"
                ":param arg3: # of columns\n"
                ":type arg3: int\n"
                ":returns: VA, aborts if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXVA`\n"
                "\n"

                "\n.. versionadded:: 7.2.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See \\ :func:`geosoft.gxapi.GXVV.create`\\ \n\n"
               ).staticmethod("create_vv");
    pyClass.def("get_full_vv", &GXVA_wrap_get_full_vv,
                "get_full_vv() -> GXVV:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the full VV from the VA.\n\n"

                ":returns: VV Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVV`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					No data is copied, this is the handle to the data VV in the VA.\n"
                "   					The fid start/increment of the VA is passed to the VV at the time\n"
                "   					of the call.  If a new VA is read, you must call GetFull_VV_VA\n"
                "   					to get the new fid in the VV.\n"
                "   				\n\n"
               );
    pyClass.def("get_vv", &GXVA_wrap_get_vv,
                "get_vv((int)arg1, (int)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a row or column of data as a VV from an array.\n\n"

                ":param arg1: Row or Column # (0 is first)\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`VA_OBJECT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: VV in which to place data\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("col", &GXVA_wrap_col,
                "col() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return number of columns in VA\n\n"

                ":returns: Columns in VA\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \\ :func:`geosoft.gxapi.GXVA.len`\\  returns the number of rows.\n\n"
               );
    pyClass.def("get_int", &GXVA_wrap_get_int,
                "get_int((int)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an integer element from a VA.\n\n"

                ":param arg1: Row\n"
                ":type arg1: int\n"
                ":param arg2: Column\n"
                ":type arg2: int\n"
                ":returns: Element wanted, rDUMMY, iDUMMY or blank string\n"
                "          						if the value is dummy or outside of the range of data.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Type conversions are performed if necessary.  Dummy values\n"
                "   					are converted to \"\\ `*`\\ \" string.\n"
                "   				\n\n"
               );
    pyClass.def("get_string", &GXVA_wrap_get_string,
                "get_string((int)arg1, (int)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a string element from a VA.\n\n"

                ":param arg1: Row\n"
                ":type arg1: int\n"
                ":param arg2: Column\n"
                ":type arg2: int\n"
                ":param arg3: string in which to place element\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns element wanted, rDUMMY, iDUMMY or blank string\n"
                "   					if the value is dummy or outside of the range of data.\n"
                "   \n"
                "   					Type conversions are performed if necessary.  Dummy values\n"
                "   					are converted to \"\\ `*`\\ \" string.\n"
                "   				\n\n"
               );
    pyClass.def("len", &GXVA_wrap_len,
                "len() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return length (number of rows) in a VA.\n\n"

                ":returns: Length of VA\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \\ :func:`geosoft.gxapi.GXVA.col`\\  returns the number of columns.\n\n"
               );
    pyClass.def("index_order", &GXVA_wrap_index_order,
                "index_order((GXVV)arg1, (GXVA)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reorder a VA based on an index VV\n\n"

                ":param arg1: Index VV of type INT\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VA to order\n"
                ":type arg2: :class:`geosoft.gxapi.GXVA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Given a row index VV (of type INT), this method reorders a\n"
                "   					VA. Please make sure that the index holds valid information.\n"
                "   				\n\n"
               ).staticmethod("index_order");
    pyClass.def("lookup_index", &GXVA_wrap_lookup_index,
                "lookup_index((GXVV)arg1, (GXVA)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Lookup a VA from another VA using an index VV.\n\n"

                ":param arg1: Index VV of REAL\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VA to output results (same type as Data VA)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Fractional values in the VV will interpolate between the value\n"
                "   					at the whole integer value and the next whole integer, dummy\n"
                "   					if outside the VA.\n"
                "   				\n\n"
               );
    pyClass.def("range_double", &GXVA_wrap_range_double,
                "range_double((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Computes the minimum and maximum range of the data, in doubles,\n"
                "   					in a vector while ignoring dummies.\n"
                "   				\n\n"

                ":param arg1: Minimum value - returned\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Maximum value - returned\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("re_fid", &GXVA_wrap_re_fid,
                "re_fid((float)arg1, (float)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Re-sample a VA to a new fid start/icrement\n\n"

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
    pyClass.def("reverse", &GXVA_wrap_reverse,
                "reverse() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reverses the order of the rows in a VA.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"
               );
    pyClass.def("get_fid_incr", &GXVA_wrap_get_fid_incr,
                "get_fid_incr() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the Fiducial increment from a VA\n\n"

                ":returns: Fiducial increment of the VA.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_fid_start", &GXVA_wrap_get_fid_start,
                "get_fid_start() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the Fiducial start from a VA\n\n"

                ":returns: Fiducial start of the VA.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_double", &GXVA_wrap_get_double,
                "get_double((int)arg1, (int)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a real element from a VA.\n\n"

                ":param arg1: Row\n"
                ":type arg1: int\n"
                ":param arg2: Column\n"
                ":type arg2: int\n"
                ":returns: Element wanted, rDUMMY, iDUMMY or blank string\n"
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
    pyClass.def("set_fid_incr", &GXVA_wrap_set_fid_incr,
                "set_fid_incr((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the Fiducial increment of a VA\n\n"

                ":param arg1: New increment\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_fid_start", &GXVA_wrap_set_fid_start,
                "set_fid_start((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the Fiducial start of a VA\n\n"

                ":param arg1: New start\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_int", &GXVA_wrap_set_int,
                "set_int((int)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set an integer element in a VA.\n\n"

                ":param arg1: Row\n"
                ":type arg1: int\n"
                ":param arg2: Column\n"
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
                "   					If the element is > current VA length, the VA length is\n"
                "   					increased.\n"
                "   				\n\n"
               );
    pyClass.def("set_ln", &GXVA_wrap_set_ln,
                "set_ln((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the length (number of rows) of the VA\n\n"

                ":param arg1: length\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The number of columns in a VA is fixed, and cannot be\n"
                "   					altered once the VA is created.\n"
                "   				\n\n"
               );
    pyClass.def("set_double", &GXVA_wrap_set_double,
                "set_double((int)arg1, (int)arg2, (float)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a real element in a VA.\n\n"

                ":param arg1: Row\n"
                ":type arg1: int\n"
                ":param arg2: Column\n"
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
                "   					If the element is > current VA length, the VA length is\n"
                "   					increased.\n"
                "   				\n\n"
               );
    pyClass.def("set_string", &GXVA_wrap_set_string,
                "set_string((int)arg1, (int)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a string element in a VA.\n\n"

                ":param arg1: Row\n"
                ":type arg1: int\n"
                ":param arg2: Column\n"
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
                "   					If the element is > current VA length, the VA length is\n"
                "   					increased.\n"
                "   				\n\n"
               );
    pyClass.def("set_vv", &GXVA_wrap_set_vv,
                "set_vv((int)arg1, (int)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a row or column of data in an array from a VV.\n\n"

                ":param arg1: Row or Column # (0 is first)\n"
                ":type arg1: int\n"
                ":param arg2: \\ :ref:`VA_OBJECT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: VV from which to get data\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("trans", &GXVA_wrap_trans,
                "trans((float)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Translate (VA + base ) \\ `*`\\  mult\n\n"

                ":param arg1: base value\n"
                ":type arg1: float\n"
                ":param arg2: mult value\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Supports all VA types using an internal double VV.\n\n"
               );
    pyClass.def("window", &GXVA_wrap_window,
                "window((int)arg1, (int)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Window a VA to a VV based in intergral frame\n\n"

                ":param arg1: first element in the window\n"
                ":type arg1: int\n"
                ":param arg2: number of elements in the window\n"
                ":type arg2: int\n"
                ":param arg3: VV in which to place results\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The defined window must be within the VA element dimensions.\n"
                "   					The windowed result will be the simple sum of all\n"
                "   					values in the window.\n"
                "   					If any values are dummy, the result will be dummy.\n"
                "   				\n\n"
               );
    pyClass.def("window2", &GXVA_wrap_window2,
                "window2((float)arg1, (float)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Window a VA to a VV based on fractional frame\n\n"

                ":param arg1: start point (from 0.0)\n"
                ":type arg1: float\n"
                ":param arg2: end point (< VA elements - 1.0)\n"
                ":type arg2: float\n"
                ":param arg3: VV in which to place results\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The defined window must be within the VA element dimensions.\n"
                "   					The windowed result will be the simple sum of all\n"
                "   					values in the window.\n"
                "   					If any values are dummy, the result will be dummy.\n"
                "   				\n\n"
               );
    pyClass.def("check_for_repeating", &GXVA_wrap_check_for_repeating,
                "check_for_repeating((GXVV)arg1, (int)arg2, (GXVV)arg3, (float)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Window a VA to a VV based on fractional frame\n\n"

                ":param arg1: Items to test for repeats (length equal to the number of columns in the VA)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: If set to 1, subtract single values in the following VV from every array row item before testing (e.g. an elevation value)\n"
                ":type arg2: int\n"
                ":param arg3: values to subtract from each row before doing the comparison test (length equal to the length of the VA). Can be VV_NULL (-1) if above subtraction parameter is zero\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: comparison tolerance - set to zero or dummy for exact match\n"
                ":type arg4: float\n"
                ":returns: 1 if rows repeat, 0 if not.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns 1 if all rows contain values which match the input values.\n"
                "   					Optionally, row values can be offset by amounts specified with a secondary VV.\n"
                "   					This function was designed to detect \"depth\" array channels, including those which might\n"
                "   					have been offset with topography on each row.\n"
                "   					An absolute tolerance can be specified to ignore numerical noise.\n"
                "   				\n\n"
               );
    pyClass.def("check_for_repeating2", &GXVA_wrap_check_for_repeating2,
                "check_for_repeating2((GXVV)arg1, (int)arg2, (GXVV)arg3, (float)arg4, (int_ref)arg5, (int_ref)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Window a VA to a VV based on fractional frame\n\n"

                ":param arg1: Items to test for repeats (length equal to the number of columns in the VA)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: If set to 1, subtract single values in the following VV from every array row item before testing (e.g. an elevation value)\n"
                ":type arg2: int\n"
                ":param arg3: values to subtract from each row before doing the comparison test (length equal to the length of the VA). Can be VV_NULL (-1) if above subtraction parameter is zero\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: comparison tolerance - set to zero or dummy for exact match\n"
                ":type arg4: float\n"
                ":param arg5: row index of first mismatch\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: column index of first mismatch\n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 1 if rows repeat, 0 if not.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns 1 if all rows contain values which match the input values.\n"
                "   					Optionally, row values can be offset by amounts specified with a secondary VV.\n"
                "   					This function was designed to detect \"depth\" array channels, including those which might\n"
                "   					have been offset with topography on each row.\n"
                "   					An absolute tolerance can be specified to ignore numerical noise.\n"
                "   					This version returns the row and column index of first mismatch.\n"
                "   				\n\n"
               );

    scope().attr("VA_AVERAGE_ROWS") = (int32_t)0;
    scope().attr("VA_AVERAGE_COLUMNS") = (int32_t)1;
    scope().attr("VA_ROW") = (int32_t)0;
    scope().attr("VA_COL") = (int32_t)1;

}
