#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXPG_wrap_copy(GXPGPtr self, GXPGPtr arg1)
{
    self->copy(arg1);
}
inline void GXPG_wrap_copy_subset(GXPGPtr self, GXPGPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7)
{
    self->copy_subset(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline GXPGPtr GXPG_wrap_create(int32_t arg1, int32_t arg2, int32_t arg3)
{
    GXPGPtr ret = GXPG::create(arg1, arg2, (GS_TYPES)arg3);
    return ret;
}
inline GXPGPtr GXPG_wrap_create_s(GXBFPtr arg1)
{
    GXPGPtr ret = GXPG::create_s(arg1);
    return ret;
}
inline void GXPG_wrap_dummy(GXPGPtr self)
{
    self->dummy();
}
inline int32_t GXPG_wrap_e_type(GXPGPtr self)
{
    GS_TYPES ret = self->e_type();
    return ret;
}
inline int32_t GXPG_wrap_n_cols(GXPGPtr self)
{
    int32_t ret = self->n_cols();
    return ret;
}
inline int32_t GXPG_wrap_n_rows(GXPGPtr self)
{
    int32_t ret = self->n_rows();
    return ret;
}
inline int32_t GXPG_wrap_n_slices(GXPGPtr self)
{
    int32_t ret = self->n_slices();
    return ret;
}
inline void GXPG_wrap_range(GXPGPtr self, float_ref& arg1, float_ref& arg2)
{
    self->range(arg1, arg2);
}
inline double GXPG_wrap_get(GXPGPtr self, int32_t arg1, int32_t arg2)
{
    double ret = self->get(arg1, arg2);
    return ret;
}
inline void GXPG_wrap_read_col(GXPGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, GXVVPtr arg4)
{
    self->read_col(arg1, arg2, arg3, arg4);
}
inline void GXPG_wrap_read_row(GXPGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, GXVVPtr arg4)
{
    self->read_row(arg1, arg2, arg3, arg4);
}
inline void GXPG_wrap_re_allocate(GXPGPtr self, int32_t arg1, int32_t arg2)
{
    self->re_allocate(arg1, arg2);
}
inline void GXPG_wrap_serial(GXPGPtr self, GXBFPtr arg1)
{
    self->serial(arg1);
}
inline void GXPG_wrap_statistics(GXPGPtr self, GXSTPtr arg1)
{
    self->statistics(arg1);
}
inline void GXPG_wrap_write_col(GXPGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, GXVVPtr arg4)
{
    self->write_col(arg1, arg2, arg3, arg4);
}
inline void GXPG_wrap_write_row(GXPGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, GXVVPtr arg4)
{
    self->write_row(arg1, arg2, arg3, arg4);
}
inline void GXPG_wrap_copy_subset_3d(GXPGPtr self, GXPGPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7, int32_t arg8, int32_t arg9, int32_t arg10)
{
    self->copy_subset_3d(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}
inline GXPGPtr GXPG_wrap_create_3d(int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    GXPGPtr ret = GXPG::create_3d(arg1, arg2, arg3, (GS_TYPES)arg4);
    return ret;
}
inline void GXPG_wrap_read_col_3d(GXPGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXVVPtr arg5)
{
    self->read_col_3d(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPG_wrap_read_row_3d(GXPGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXVVPtr arg5)
{
    self->read_row_3d(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPG_wrap_read_trace_3d(GXPGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXVVPtr arg5)
{
    self->read_trace_3d(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPG_wrap_re_allocate_3d(GXPGPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    self->re_allocate_3d(arg1, arg2, arg3);
}
inline void GXPG_wrap_write_col_3d(GXPGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXVVPtr arg5)
{
    self->write_col_3d(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPG_wrap_write_row_3d(GXPGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXVVPtr arg5)
{
    self->write_row_3d(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPG_wrap_write_trace_3d(GXPGPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, GXVVPtr arg5)
{
    self->write_trace_3d(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPG_wrap_read_bf(GXPGPtr self, GXBFPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    self->read_bf(arg1, (PG_3D_DIR)arg2, (PG_BF_CONV)arg3, arg4, arg5, arg6);
}
inline void GXPG_wrap_read_ra(GXPGPtr self, GXRAPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, const gx_string_type& arg6)
{
    self->read_ra(arg1, (PG_3D_DIR)arg2, arg3, arg4, arg5, arg6);
}
inline void GXPG_wrap_write_bf(GXPGPtr self, GXBFPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    self->write_bf(arg1, (PG_3D_DIR)arg2, (PG_BF_CONV)arg3, arg4, arg5, arg6);
}
inline void GXPG_wrap_write_wa(GXPGPtr self, GXWAPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, const gx_string_type& arg6)
{
    self->write_wa(arg1, (PG_3D_DIR)arg2, arg3, arg4, arg5, arg6);
}

void gxPythonImportGXPG()
{

    class_<GXPG, GXPGPtr> pyClass("GXPG",
                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		Pager methods for large 2-D arrays\n"
                                  "   		This class handles very-large 2-D arrays in which efficient\n"
                                  "   		access is required along both rows and columns.\n"
                                  "   	\n\n"

                                  "\n\n**Note:**\n\n"

                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		Typically a grid is accessed using the IMG class, and a PG\n"
                                  "   		is obtained from the IMG using the \\ :func:`geosoft.gxapi.GXIMG.get_pg`\\  function.\n"
                                  "   		Following operations on the PG, it can be written back to\n"
                                  "   		the IMG using \\ :func:`geosoft.gxapi.GXIMG.set_pg`\\ .\n"
                                  "   	\n\n"
                                  , no_init);

    pyClass.def("null", &GXPG::null, "null() -> GXPG\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXPG`\n\n:returns: A null :class:`geosoft.gxapi.GXPG`\n:rtype: :class:`geosoft.gxapi.GXPG`\n").staticmethod("null");
    pyClass.def("is_null", &GXPG::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXPG is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXPG`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXPG::_internal_handle);
    pyClass.def("copy", &GXPG_wrap_copy,
                "copy((GXPG)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy the data from one pager to another.\n\n"

                ":param arg1: Source PG object\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("copy_subset", &GXPG_wrap_copy_subset,
                "copy_subset((GXPG)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a subset of data from one pager to another.\n\n"

                ":param arg1: Source PG object\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Y (row) Origin on destination\n"
                ":type arg2: int\n"
                ":param arg3: X (col) Origin on destination\n"
                ":type arg3: int\n"
                ":param arg4: Y (row) Origin on source\n"
                ":type arg4: int\n"
                ":param arg5: X (col) Origin on source\n"
                ":type arg5: int\n"
                ":param arg6: Number of Y (rows) to copy\n"
                ":type arg6: int\n"
                ":param arg7: Number of X (columns) to copy\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   2D Only\n\n"
               );
    pyClass.def("create", &GXPG_wrap_create,
                "create((int)arg1, (int)arg2, (int)arg3) -> GXPG:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a Pager object\n\n"

                ":param arg1: # elements in y (# of row)\n"
                ":type arg1: int\n"
                ":param arg2: # elements in x (# of column)\n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg3: int\n"
                ":returns: PG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXPG`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_s", &GXPG_wrap_create_s,
                "create_s((GXBF)arg1) -> GXPG:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a 2D PG from serialized source.\n\n"

                ":param arg1: BF\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: PG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXPG`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   For 3D pagers, use CreateBF_PG.\n\n"
               ).staticmethod("create_s");
    pyClass.def("dummy", &GXPG_wrap_dummy,
                "dummy() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the Entire pager to dummy.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("e_type", &GXPG_wrap_e_type,
                "e_type() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the type of pager.\n\n"

                ":returns: \\ :ref:`GS_TYPES`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("n_cols", &GXPG_wrap_n_cols,
                "n_cols() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the # of columns in pager.\n\n"

                ":returns: # of columns.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("n_rows", &GXPG_wrap_n_rows,
                "n_rows() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the # of rows in pager.\n\n"

                ":returns: # of rows.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("n_slices", &GXPG_wrap_n_slices,
                "n_slices() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the # of slices (z) in pager.\n\n"

                ":returns: # of rows.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("range", &GXPG_wrap_range,
                "range((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Computes the range of the entire pager.\n\n"

                ":param arg1: Minimum Data (Dummy if no range)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Maximum Data (Dummy if no range)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get", &GXPG_wrap_get,
                "get((int)arg1, (int)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Read a single value from a 2D PG\n\n"

                ":param arg1: iBx - element # in x (column #)\n"
                ":type arg1: int\n"
                ":param arg2: iBy - element # in y (row #)\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is a low-performance method.\n"
                "   				\n\n"
               );
    pyClass.def("read_col", &GXPG_wrap_read_col,
                "read_col((int)arg1, (int)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Read a set of elements in X (column) from pager into vv\n\n"

                ":param arg1: iBx - element # in x (column #)\n"
                ":type arg1: int\n"
                ":param arg2: iBy - begining element # in y to read (0 is the first)\n"
                ":type arg2: int\n"
                ":param arg3: iNy - # elements to read (0 for whole vector)\n"
                ":type arg3: int\n"
                ":param arg4: hVV - VV handle\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("read_row", &GXPG_wrap_read_row,
                "read_row((int)arg1, (int)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Read a set of elements in Y (row) from pager into vv\n\n"

                ":param arg1: iBy - element # in y (row #)\n"
                ":type arg1: int\n"
                ":param arg2: iBx - begining element # in x to read (0 is the first)\n"
                ":type arg2: int\n"
                ":param arg3: iNx - # elements to read (0 for whole vector)\n"
                ":type arg3: int\n"
                ":param arg4: hVV - VV handle\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("re_allocate", &GXPG_wrap_re_allocate,
                "re_allocate((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Changes the size of Pager\n\n"

                ":param arg1: Number of Y (rows) to reallocate\n"
                ":type arg1: int\n"
                ":param arg2: Number of X (columns) to reallocate\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("serial", &GXPG_wrap_serial,
                "serial((GXBF)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Serialize a 2D PG to a BF.\n\n"

                ":param arg1: BF\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   For 3D pagers, use \\ :func:`geosoft.gxapi.GXPG.write_bf`\\ .\n\n"
               );
    pyClass.def("statistics", &GXPG_wrap_statistics,
                "statistics((GXST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute the statistics of a pager object.\n\n"

                ":param arg1: hST - statistics object\n"
                ":type arg1: :class:`geosoft.gxapi.GXST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.1\n\n"
               );
    pyClass.def("write_col", &GXPG_wrap_write_col,
                "write_col((int)arg1, (int)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write a set of elements in X (column) from vv into pager\n\n"

                ":param arg1: iBx - element # in x (column #)\n"
                ":type arg1: int\n"
                ":param arg2: iBy - begining element # in y to write (0 is the first)\n"
                ":type arg2: int\n"
                ":param arg3: iNy - # elements to write (0 for whole vector)\n"
                ":type arg3: int\n"
                ":param arg4: hVV - VV handle\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("write_row", &GXPG_wrap_write_row,
                "write_row((int)arg1, (int)arg2, (int)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write a set of elements in Y (row) from vv into pager\n\n"

                ":param arg1: iBy - element # in y (row #)\n"
                ":type arg1: int\n"
                ":param arg2: iBx - begining element # in x to write (0 is the first)\n"
                ":type arg2: int\n"
                ":param arg3: iNx - # elements to write (0 for whole vector)\n"
                ":type arg3: int\n"
                ":param arg4: hVV - VV handle\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("copy_subset_3d", &GXPG_wrap_copy_subset_3d,
                "copy_subset_3d((GXPG)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7, (int)arg8, (int)arg9, (int)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy a subset of data from one pager to another.\n\n"

                ":param arg1: Source PG object\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Z (slice) Origin on destination\n"
                ":type arg2: int\n"
                ":param arg3: Y (row) Origin on destination\n"
                ":type arg3: int\n"
                ":param arg4: X (col) Origin on destination\n"
                ":type arg4: int\n"
                ":param arg5: Z (slice) Origin on source\n"
                ":type arg5: int\n"
                ":param arg6: Y (row) Origin on source\n"
                ":type arg6: int\n"
                ":param arg7: X (col) Origin on source\n"
                ":type arg7: int\n"
                ":param arg8: Number of Z (slice) to copy\n"
                ":type arg8: int\n"
                ":param arg9: Number of Y (rows) to copy\n"
                ":type arg9: int\n"
                ":param arg10: Number of X (columns) to copy\n"
                ":type arg10: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   2D Only\n\n"
               );
    pyClass.def("create_3d", &GXPG_wrap_create_3d,
                "create_3d((int)arg1, (int)arg2, (int)arg3, (int)arg4) -> GXPG:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a Pager object\n\n"

                ":param arg1: # elements in z (# of slices)\n"
                ":type arg1: int\n"
                ":param arg2: # elements in y (# of row)\n"
                ":type arg2: int\n"
                ":param arg3: # elements in x (# of column)\n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`GS_TYPES`\\ \n"
                ":type arg4: int\n"
                ":returns: PG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXPG`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("create_3d");
    pyClass.def("read_col_3d", &GXPG_wrap_read_col_3d,
                "read_col_3d((int)arg1, (int)arg2, (int)arg3, (int)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Read a set of elements in X (column) from pager into vv\n\n"

                ":param arg1: iBz - element # in z (slice #)\n"
                ":type arg1: int\n"
                ":param arg2: iBx - element # in x (column #)\n"
                ":type arg2: int\n"
                ":param arg3: iBy - begining element # in y to read (0 is the first)\n"
                ":type arg3: int\n"
                ":param arg4: iNy - # elements to read (0 for whole vector)\n"
                ":type arg4: int\n"
                ":param arg5: hVV - VV handle\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("read_row_3d", &GXPG_wrap_read_row_3d,
                "read_row_3d((int)arg1, (int)arg2, (int)arg3, (int)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Read a set of elements in Y (row) from pager into vv\n\n"

                ":param arg1: iBz - element # in z (slice #)\n"
                ":type arg1: int\n"
                ":param arg2: iBy - element # in y (row #)\n"
                ":type arg2: int\n"
                ":param arg3: iBx - begining element # in x to read (0 is the first)\n"
                ":type arg3: int\n"
                ":param arg4: iNx - # elements to read (0 for whole vector)\n"
                ":type arg4: int\n"
                ":param arg5: hVV - VV handle\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("read_trace_3d", &GXPG_wrap_read_trace_3d,
                "read_trace_3d((int)arg1, (int)arg2, (int)arg3, (int)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Read a set of elements in Z (trace) from pager into vv\n\n"

                ":param arg1: iBx - element # in x (column #)\n"
                ":type arg1: int\n"
                ":param arg2: iBy - element # in y (row #)\n"
                ":type arg2: int\n"
                ":param arg3: iBy - begining element # in z to read (0 is the first)\n"
                ":type arg3: int\n"
                ":param arg4: iNy - # elements to read (0 for whole vector)\n"
                ":type arg4: int\n"
                ":param arg5: hVV - VV handle\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("re_allocate_3d", &GXPG_wrap_re_allocate_3d,
                "re_allocate_3d((int)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Changes the size of 3D Pager\n\n"

                ":param arg1: Number of Z (slices) to reallocate\n"
                ":type arg1: int\n"
                ":param arg2: Number of Y (rows) to reallocate\n"
                ":type arg2: int\n"
                ":param arg3: Number of X (columns) to reallocate\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("write_col_3d", &GXPG_wrap_write_col_3d,
                "write_col_3d((int)arg1, (int)arg2, (int)arg3, (int)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write a set of elements in X (column) from vv into pager\n\n"

                ":param arg1: iBz - element # in z (slice #)\n"
                ":type arg1: int\n"
                ":param arg2: iBx - element # in x (column #)\n"
                ":type arg2: int\n"
                ":param arg3: iBy - begining element # in y to write (0 is the first)\n"
                ":type arg3: int\n"
                ":param arg4: iNy - # elements to write (0 for whole vector)\n"
                ":type arg4: int\n"
                ":param arg5: hVV - VV handle\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("write_row_3d", &GXPG_wrap_write_row_3d,
                "write_row_3d((int)arg1, (int)arg2, (int)arg3, (int)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write a set of elements in Y (row) from vv into pager\n\n"

                ":param arg1: iBz - element # in z (slice #)\n"
                ":type arg1: int\n"
                ":param arg2: iBy - element # in y (row #)\n"
                ":type arg2: int\n"
                ":param arg3: iBx - begining element # in x to write (0 is the first)\n"
                ":type arg3: int\n"
                ":param arg4: iNx - # elements to write (0 for whole vector)\n"
                ":type arg4: int\n"
                ":param arg5: hVV - VV handle\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("write_trace_3d", &GXPG_wrap_write_trace_3d,
                "write_trace_3d((int)arg1, (int)arg2, (int)arg3, (int)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write a set of elements in Z (trace) from pager into vv\n\n"

                ":param arg1: iBx - element # in x (column #)\n"
                ":type arg1: int\n"
                ":param arg2: iBy - element # in y (row #)\n"
                ":type arg2: int\n"
                ":param arg3: iBy - begining element # in z to read (0 is the first)\n"
                ":type arg3: int\n"
                ":param arg4: iNy - # elements to read (0 for whole vector)\n"
                ":type arg4: int\n"
                ":param arg5: hVV - VV handle\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("read_bf", &GXPG_wrap_read_bf,
                "read_bf((GXBF)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Read the contents of a 2D or 3D pager to from a BF.\n\n"

                ":param arg1: BF to read from\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":param arg2: \\ :ref:`PG_3D_DIR`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`PG_BF_CONV`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Reverse X\n"
                ":type arg4: int\n"
                ":param arg5: Reverse Y\n"
                ":type arg5: int\n"
                ":param arg6: Reverse Z\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("read_ra", &GXPG_wrap_read_ra,
                "read_ra((GXRA)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Read the contents of a 2D or 3D pager to from an RA.\n\n"

                ":param arg1: RA to read from\n"
                ":type arg1: :class:`geosoft.gxapi.GXRA`\n"
                ":param arg2: \\ :ref:`PG_3D_DIR`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Reverse X\n"
                ":type arg3: int\n"
                ":param arg4: Reverse Y\n"
                ":type arg4: int\n"
                ":param arg5: Reverse Z\n"
                ":type arg5: int\n"
                ":param arg6: Dummy\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Each line must hold only 1 value\n\n"
               );
    pyClass.def("write_bf", &GXPG_wrap_write_bf,
                "write_bf((GXBF)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write the contents of a 2D or 3D pager to a BF.\n\n"

                ":param arg1: BF to write to\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":param arg2: \\ :ref:`PG_3D_DIR`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`PG_BF_CONV`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Reverse X\n"
                ":type arg4: int\n"
                ":param arg5: Reverse Y\n"
                ":type arg5: int\n"
                ":param arg6: Reverse Z\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("write_wa", &GXPG_wrap_write_wa,
                "write_wa((GXWA)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write the contents of a 2D or 3D pager to a WA\n\n"

                ":param arg1: WA to write to\n"
                ":type arg1: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg2: \\ :ref:`PG_3D_DIR`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Reverse X\n"
                ":type arg3: int\n"
                ":param arg4: Reverse Y\n"
                ":type arg4: int\n"
                ":param arg5: Reverse Z\n"
                ":type arg5: int\n"
                ":param arg6: Dummy\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Each line will hold only 1 value\n\n"
               );

    scope().attr("PG_3D_DIR_XYZ") = (int32_t)0;
    scope().attr("PG_3D_DIR_YXZ") = (int32_t)1;
    scope().attr("PG_3D_DIR_XZY") = (int32_t)2;
    scope().attr("PG_3D_DIR_YZX") = (int32_t)3;
    scope().attr("PG_3D_DIR_ZXY") = (int32_t)4;
    scope().attr("PG_3D_DIR_ZYX") = (int32_t)5;
    scope().attr("PG_BF_CONV_NONE") = (int32_t)0;
    scope().attr("PG_BF_CONV_SWAP") = (int32_t)1;

}
