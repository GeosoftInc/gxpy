#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXPGU_wrap_bool_mask(GXPGPtr arg1, const gx_string_type& arg2)
{
    GXPGU::bool_mask(arg1, arg2);
}
inline void GXPGU_wrap_direct_gridding_dat(GXPGPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6, GXDATPtr arg7, int32_t arg8)
{
    GXPGU::direct_gridding_dat(arg1, arg2, arg3, arg4, arg5, arg6, arg7, (PGU_DIRECTGRID)arg8);
}
inline void GXPGU_wrap_direct_gridding_dat_3d(GXPGPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, GXDATPtr arg9, int32_t arg10)
{
    GXPGU::direct_gridding_dat_3d(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (PGU_DIRECTGRID)arg10);
}
inline void GXPGU_wrap_direct_gridding_db(GXPGPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6, GXDBPtr arg7, int32_t arg8, int32_t arg9, int32_t arg10, int32_t arg11)
{
    GXPGU::direct_gridding_db(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, (PGU_DIRECTGRID)arg11);
}
inline void GXPGU_wrap_direct_gridding_db_3d(GXPGPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, GXDBPtr arg9, int32_t arg10, int32_t arg11, int32_t arg12, int32_t arg13, int32_t arg14)
{
    GXPGU::direct_gridding_db_3d(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, (PGU_DIRECTGRID)arg14);
}
inline void GXPGU_wrap_direct_gridding_vv(GXPGPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, int32_t arg10)
{
    GXPGU::direct_gridding_vv(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (PGU_DIRECTGRID)arg10);
}
inline void GXPGU_wrap_expand(GXPGPtr arg1, GXPGPtr arg2, double arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    GXPGU::expand(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXPGU_wrap_fill(GXPGPtr arg1, int32_t arg2, double arg3, int32_t arg4, int32_t arg5, int32_t arg6, double arg7, double arg8, int32_t arg9, int32_t arg10, const gx_string_type& arg11)
{
    GXPGU::fill(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXPGU_wrap_fill_value(GXPGPtr arg1, double arg2)
{
    GXPGU::fill_value(arg1, arg2);
}
inline void GXPGU_wrap_filt_sym(GXPGPtr arg1, int32_t arg2, int32_t arg3, const gx_string_type& arg4, int32_t arg5, GXVVPtr arg6)
{
    GXPGU::filt_sym(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXPGU_wrap_filt_sym5(GXPGPtr arg1, int32_t arg2, int32_t arg3, const gx_string_type& arg4, GXVVPtr arg5)
{
    GXPGU::filt_sym5(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPGU_wrap_grid_peak(const gx_string_type& arg1, int32_t arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5)
{
    GXPGU::grid_peak(arg1, (BLAKEY_TEST)arg2, arg3, arg4, arg5);
}
inline void GXPGU_wrap_dw_gridding_dat(GXPGPtr arg1, GXDATPtr arg2, GXREGPtr arg3)
{
    GXPGU::dw_gridding_dat(arg1, arg2, arg3);
}
inline void GXPGU_wrap_dw_gridding_dat_3d(GXPGPtr arg1, GXDATPtr arg2, GXREGPtr arg3)
{
    GXPGU::dw_gridding_dat_3d(arg1, arg2, arg3);
}
inline void GXPGU_wrap_dw_gridding_db(GXPGPtr arg1, GXDBPtr arg2, int32_t arg3, int32_t arg4, int32_t arg5, GXREGPtr arg6)
{
    GXPGU::dw_gridding_db(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXPGU_wrap_dw_gridding_db_3d(GXPGPtr arg1, GXDBPtr arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, GXREGPtr arg7)
{
    GXPGU::dw_gridding_db_3d(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXPGU_wrap_dw_gridding_vv(GXPGPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXREGPtr arg5)
{
    GXPGU::dw_gridding_vv(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPGU_wrap_numeric_to_thematic(GXPGPtr arg1, GXVVPtr arg2, GXPGPtr arg3)
{
    GXPGU::numeric_to_thematic(arg1, arg2, arg3);
}
inline void GXPGU_wrap_peakedness(const gx_string_type& arg1, int32_t arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5)
{
    GXPGU::peakedness(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPGU_wrap_peakedness_grid(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3, double arg4)
{
    GXPGU::peakedness_grid(arg1, arg2, arg3, arg4);
}
inline void GXPGU_wrap_ref_file(GXPGPtr arg1, const gx_string_type& arg2)
{
    GXPGU::ref_file(arg1, arg2);
}
inline void GXPGU_wrap_save_file(GXPGPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6, GXTRPtr arg7, GXIPJPtr arg8, const gx_string_type& arg9)
{
    GXPGU::save_file(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXPGU_wrap_thematic_to_numeric(GXPGPtr arg1, GXVVPtr arg2, GXPGPtr arg3)
{
    GXPGU::thematic_to_numeric(arg1, arg2, arg3);
}
inline void GXPGU_wrap_trend(GXPGPtr arg1, GXPGPtr arg2, GXTRPtr arg3, int32_t arg4, int32_t arg5, double arg6, double arg7, double arg8, double arg9)
{
    GXPGU::trend(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXPGU_wrap_add_scalar(GXPGPtr arg1, double arg2)
{
    GXPGU::add_scalar(arg1, arg2);
}
inline void GXPGU_wrap_multiply_scalar(GXPGPtr arg1, double arg2)
{
    GXPGU::multiply_scalar(arg1, arg2);
}
inline void GXPGU_wrap_correlation_matrix(GXPGPtr arg1, GXPGPtr arg2)
{
    GXPGU::correlation_matrix(arg1, arg2);
}
inline void GXPGU_wrap_correlation_matrix2(GXPGPtr arg1, int32_t arg2, GXPGPtr arg3)
{
    GXPGU::correlation_matrix2(arg1, (PGU_CORR)arg2, arg3);
}
inline void GXPGU_wrap_invert_matrix(GXPGPtr arg1, GXPGPtr arg2)
{
    GXPGU::invert_matrix(arg1, arg2);
}
inline void GXPGU_wrap_jacobi(GXPGPtr arg1, GXVVPtr arg2, GXPGPtr arg3)
{
    GXPGU::jacobi(arg1, arg2, arg3);
}
inline void GXPGU_wrap_lu_back_sub(GXPGPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4)
{
    GXPGU::lu_back_sub(arg1, arg2, arg3, arg4);
}
inline void GXPGU_wrap_lu_decomp(GXPGPtr arg1, GXPGPtr arg2, GXVVPtr arg3)
{
    GXPGU::lu_decomp(arg1, arg2, arg3);
}
inline void GXPGU_wrap_matrix_mult(GXPGPtr arg1, int32_t arg2, GXPGPtr arg3, int32_t arg4, GXPGPtr arg5)
{
    GXPGU::matrix_mult(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPGU_wrap_matrix_vector_mult(GXPGPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    GXPGU::matrix_vector_mult(arg1, arg2, arg3);
}
inline void GXPGU_wrap_sv_decompose(GXPGPtr arg1, GXPGPtr arg2, GXVVPtr arg3, GXPGPtr arg4)
{
    GXPGU::sv_decompose(arg1, arg2, arg3, arg4);
}
inline void GXPGU_wrap_sv_recompose(GXPGPtr arg1, GXVVPtr arg2, GXPGPtr arg3, double arg4, GXPGPtr arg5)
{
    GXPGU::sv_recompose(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPGU_wrap_pc_communality(GXPGPtr arg1, GXVVPtr arg2)
{
    GXPGU::pc_communality(arg1, arg2);
}
inline void GXPGU_wrap_pc_loadings(GXPGPtr arg1, GXPGPtr arg2)
{
    GXPGU::pc_loadings(arg1, arg2);
}
inline void GXPGU_wrap_pc_loadings2(GXPGPtr arg1, GXPGPtr arg2)
{
    GXPGU::pc_loadings2(arg1, arg2);
}
inline void GXPGU_wrap_pc_scores(GXPGPtr arg1, GXPGPtr arg2, GXPGPtr arg3)
{
    GXPGU::pc_scores(arg1, arg2, arg3);
}
inline void GXPGU_wrap_pc_standardize(GXPGPtr arg1, GXVVPtr arg2, GXVVPtr arg3, int32_t arg4)
{
    GXPGU::pc_standardize(arg1, arg2, arg3, (PGU_DIRECTION)arg4);
}
inline void GXPGU_wrap_pc_standardize2(GXPGPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, int32_t arg5)
{
    GXPGU::pc_standardize2(arg1, arg2, arg3, arg4, arg5);
}
inline void GXPGU_wrap_pc_transform(GXPGPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, int32_t arg5)
{
    GXPGU::pc_transform(arg1, arg2, arg3, arg4, (PGU_DIRECTION)arg5);
}
inline void GXPGU_wrap_pc_varimax(GXPGPtr arg1, GXPGPtr arg2)
{
    GXPGU::pc_varimax(arg1, arg2);
}
inline double GXPGU_wrap_maximum_terrain_steepness(GXPGPtr arg1, int32_t arg2)
{
    double ret = GXPGU::maximum_terrain_steepness(arg1, arg2);
    return ret;
}

void gxPythonImportGXPGU()
{

    class_<GXPGU, boost::noncopyable> pyClass("GXPGU",
            "\n.. parsed-literal::\n\n"
            "   A collection of methods applied to PG objects, including\n"
            "   fills, trending and 2-D FFT operations.\n\n"
            , no_init);


    pyClass.def("bool_mask", &GXPGU_wrap_bool_mask,
                "bool_mask((GXPG)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply reference file boolean mask to pager\n\n"

                ":param arg1: pager obj\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: sRefFil - reference file for boolean mask flag.\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("bool_mask");
    pyClass.def("direct_gridding_dat", &GXPGU_wrap_direct_gridding_dat,
                "direct_gridding_dat((GXPG)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (GXDAT)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Direct-gridding method, DAT version.\n\n"

                ":param arg1: input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: X origin of grid\n"
                ":type arg2: float\n"
                ":param arg3: Y origin of grid\n"
                ":type arg3: float\n"
                ":param arg4: X cell size\n"
                ":type arg4: float\n"
                ":param arg5: Y cell size\n"
                ":type arg5: float\n"
                ":param arg6: rotation angle (degrees CCW).\n"
                ":type arg6: float\n"
                ":param arg7: DAT source\n"
                ":type arg7: :class:`geosoft.gxapi.GXDAT`\n"
                ":param arg8: \\ :ref:`PGU_DIRECTGRID`\\ \n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Grid cells take on the specified statistic of the values inside the\n"
                "   cell area. Grid cells containing no data values are set to dummy.\n\n"
               ).staticmethod("direct_gridding_dat");
    pyClass.def("direct_gridding_dat_3d", &GXPGU_wrap_direct_gridding_dat_3d,
                "direct_gridding_dat_3d((GXPG)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (GXDAT)arg9, (int)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Direct-gridding method, DAT version, 3D.\n\n"

                ":param arg1: input 3D PG\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: X origin of 3D grid\n"
                ":type arg2: float\n"
                ":param arg3: Y origin of 3D grid\n"
                ":type arg3: float\n"
                ":param arg4: Z origin of 3D grid\n"
                ":type arg4: float\n"
                ":param arg5: X cell size\n"
                ":type arg5: float\n"
                ":param arg6: Y cell size\n"
                ":type arg6: float\n"
                ":param arg7: Z cell size\n"
                ":type arg7: float\n"
                ":param arg8: rotation angle (degrees CCW, vertical axis only).\n"
                ":type arg8: float\n"
                ":param arg9: 3D DAT source\n"
                ":type arg9: :class:`geosoft.gxapi.GXDAT`\n"
                ":param arg10: \\ :ref:`PGU_DIRECTGRID`\\ \n"
                ":type arg10: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   3D grid cells take on the specified statistic of the values inside the\n"
                "   cell area. Grid cells containing no data values are set to dummy.\n\n"
               ).staticmethod("direct_gridding_dat_3d");
    pyClass.def("direct_gridding_db", &GXPGU_wrap_direct_gridding_db,
                "direct_gridding_db((GXPG)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (GXDB)arg7, (int)arg8, (int)arg9, (int)arg10, (int)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Direct-gridding method, DB version.\n\n"

                ":param arg1: input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: X origin of grid\n"
                ":type arg2: float\n"
                ":param arg3: Y origin of grid\n"
                ":type arg3: float\n"
                ":param arg4: X cell size\n"
                ":type arg4: float\n"
                ":param arg5: Y cell size\n"
                ":type arg5: float\n"
                ":param arg6: rotation angle (degrees CCW).\n"
                ":type arg6: float\n"
                ":param arg7: Database\n"
                ":type arg7: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg8: X Channel [READONLY]\n"
                ":type arg8: int\n"
                ":param arg9: Y Channel [READONLY]\n"
                ":type arg9: int\n"
                ":param arg10: Data Channel [READONLY]\n"
                ":type arg10: int\n"
                ":param arg11: \\ :ref:`PGU_DIRECTGRID`\\ \n"
                ":type arg11: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Grid cells take on the specified statistic of the values inside the\n"
                "   cell area. Grid cells containing no data values are set to dummy.\n\n"
               ).staticmethod("direct_gridding_db");
    pyClass.def("direct_gridding_db_3d", &GXPGU_wrap_direct_gridding_db_3d,
                "direct_gridding_db_3d((GXPG)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (GXDB)arg9, (int)arg10, (int)arg11, (int)arg12, (int)arg13, (int)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Direct-gridding method, DB version, 3D.\n\n"

                ":param arg1: input 3D PG\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: X origin of 3D grid\n"
                ":type arg2: float\n"
                ":param arg3: Y origin of 3D grid\n"
                ":type arg3: float\n"
                ":param arg4: Z origin of 3D grid\n"
                ":type arg4: float\n"
                ":param arg5: X cell size\n"
                ":type arg5: float\n"
                ":param arg6: Y cell size\n"
                ":type arg6: float\n"
                ":param arg7: Z cell size\n"
                ":type arg7: float\n"
                ":param arg8: rotation angle (degrees CCW, vertical axis only).\n"
                ":type arg8: float\n"
                ":param arg9: Database\n"
                ":type arg9: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg10: X Channel [READONLY]\n"
                ":type arg10: int\n"
                ":param arg11: Y Channel [READONLY]\n"
                ":type arg11: int\n"
                ":param arg12: Z Channel [READONLY]\n"
                ":type arg12: int\n"
                ":param arg13: Data Channel [READONLY]\n"
                ":type arg13: int\n"
                ":param arg14: \\ :ref:`PGU_DIRECTGRID`\\ \n"
                ":type arg14: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   3D grid cells take on the specified statistic of the values inside the\n"
                "   cell area. Grid cells containing no data values are set to dummy.\n\n"
               ).staticmethod("direct_gridding_db_3d");
    pyClass.def("direct_gridding_vv", &GXPGU_wrap_direct_gridding_vv,
                "direct_gridding_vv((GXPG)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (int)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Direct-gridding method, VV version.\n\n"

                ":param arg1: input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: X origin of grid\n"
                ":type arg2: float\n"
                ":param arg3: Y origin of grid\n"
                ":type arg3: float\n"
                ":param arg4: X cell size\n"
                ":type arg4: float\n"
                ":param arg5: Y cell size\n"
                ":type arg5: float\n"
                ":param arg6: rotation angle (degrees CCW).\n"
                ":type arg6: float\n"
                ":param arg7: X locations of values\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Y locations of values\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Z values to grid\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: \\ :ref:`PGU_DIRECTGRID`\\ \n"
                ":type arg10: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Grid cells take on the specified statistic of the values inside the\n"
                "   cell area. Grid cells containing no data values are set to dummy.\n\n"
               ).staticmethod("direct_gridding_vv");
    pyClass.def("expand", &GXPGU_wrap_expand,
                "expand((GXPG)arg1, (GXPG)arg2, (float)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Expand a pager by filling the dummies for expanded edges\n\n"

                ":param arg1: original pager obj\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: expanded pager obj\n"
                ":type arg2: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg3: % expansion\n"
                ":type arg3: float\n"
                ":param arg4: option  0 - rectangular, 1 - square\n"
                ":type arg4: int\n"
                ":param arg5: X dimension to expand to (0 for expansion to FFT2D legal dimension)\n"
                ":type arg5: int\n"
                ":param arg6: Y dimension to expand to (0 for expansion to FFT2D legal dimension)\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   3D pagers are expanded in X,Y direction the number of slices(Z) is unchanged .\n\n"
               ).staticmethod("expand");
    pyClass.def("fill", &GXPGU_wrap_fill,
                "fill((GXPG)arg1, (int)arg2, (float)arg3, (int)arg4, (int)arg5, (int)arg6, (float)arg7, (float)arg8, (int)arg9, (int)arg10, (str)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replace all dummies in a pager by predict values.\n\n"

                ":param arg1: pager obj\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Roll off weighting option: 1 - linear, 2 - square\n"
                ":type arg2: int\n"
                ":param arg3: dRollBase - the value to roll off to, GS_R8DM for roll off to mean value line by line.\n"
                ":type arg3: float\n"
                ":param arg4: lRollDist - (at unit of cell dist.) for roll-off. 0 for no roll of, -1 for the default: 2 times of min. dummy edge dim.\n"
                ":type arg4: int\n"
                ":param arg5: lMxf - max. filter length.  -1 for no max. entropy. 0 for the default of MIN(minimum dummy edge dim, 32).\n"
                ":type arg5: int\n"
                ":param arg6: lMxp - max. pred. sample 0 for the default of 2\\ `*`\\ lMxf.\n"
                ":type arg6: int\n"
                ":param arg7: dAmpLmt - limit (abs. value) amplitudes to this level. Amplitudes are limited starting at half this value. <=0.0 for no amp limit.\n"
                ":type arg7: float\n"
                ":param arg8: dEdgeLmt - limit edge (abs. value) amplitudes to this level. <0.0 for no edge limit.\n"
                ":type arg8: float\n"
                ":param arg9: lEdgeWidth - within this dist. (at unit of cell size) for amp. limited. -1 for no edge limit. 0 for the default of minimum dummy edge dim.\n"
                ":type arg9: int\n"
                ":param arg10: iNPass - number of time to pass smooth filter\n"
                ":type arg10: int\n"
                ":param arg11: sRefFil - reference file for smooth filter flag.\n"
                ":type arg11: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("fill");
    pyClass.def("fill_value", &GXPGU_wrap_fill_value,
                "fill_value((GXPG)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set all values in a pager to a single value.\n\n"

                ":param arg1: pager obj\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Value to set in pager\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"
               ).staticmethod("fill_value");
    pyClass.def("filt_sym", &GXPGU_wrap_filt_sym,
                "filt_sym((GXPG)arg1, (int)arg2, (int)arg3, (str)arg4, (int)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply 5x5, 7x7 or 9X9 symmetric convolution filter to a PG.\n\n"

                ":param arg1: pager obj\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: number of time to pass smooth filter\n"
                ":type arg2: int\n"
                ":param arg3: flag to use filter file\n"
                ":type arg3: int\n"
                ":param arg4: file for filter values\n"
                ":type arg4: str\n"
                ":param arg5: size of filter window, 5/7/9\n"
                ":type arg5: int\n"
                ":param arg6: array of 6/10/15 filter coefficients\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"
               ).staticmethod("filt_sym");
    pyClass.def("filt_sym5", &GXPGU_wrap_filt_sym5,
                "filt_sym5((GXPG)arg1, (int)arg2, (int)arg3, (str)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply 5x5 symmetric convolution filter to a PG.\n\n"

                ":param arg1: pager obj\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: number of time to pass smooth filter\n"
                ":type arg2: int\n"
                ":param arg3: flag to use filter file\n"
                ":type arg3: int\n"
                ":param arg4: file for filter values\n"
                ":type arg4: str\n"
                ":param arg5: array of 6 filter coefficients at position 00, 10, 11, 20, 21, 22. Symmetric filters look like : 22 21 20 21 22 21 11 10 11 21 20 10 00 10 20 21 11 10 11 21 22 21 20 21 22\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("filt_sym5");
    pyClass.def("grid_peak", &GXPGU_wrap_grid_peak,
                "grid_peak((str)arg1, (int)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Pick grid peaks.\n\n"

                ":param arg1: Grid file name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`BLAKEY_TEST`\\ \n"
                ":type arg2: int\n"
                ":param arg3: X of found peaks\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Y of found peaks\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Z values of found peaks\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Blakey test limit defines how grid peaks are to be found.\n"
                "   For example, with the BLAKEY_TEST_ONESIDE, a grid\n"
                "   point will be picked if its grid value is greater than\n"
                "   the value of one or more of its four neighouring points.\n\n"
               ).staticmethod("grid_peak");
    pyClass.def("dw_gridding_dat", &GXPGU_wrap_dw_gridding_dat,
                "dw_gridding_dat((GXPG)arg1, (GXDAT)arg2, (GXREG)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \\ :func:`geosoft.gxapi.GXPGU.dw_gridding_dat`\\      Inverse-distance weighting gridding method, DAT version.\n\n"

                ":param arg1: input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: DAT source\n"
                ":type arg2: :class:`geosoft.gxapi.GXDAT`\n"
                ":param arg3: Parameters (see above)\n"
                ":type arg3: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See the notes for \\ :func:`geosoft.gxapi.GXPGU.dw_gridding_db`\\ .\n\n"
               ).staticmethod("dw_gridding_dat");
    pyClass.def("dw_gridding_dat_3d", &GXPGU_wrap_dw_gridding_dat_3d,
                "dw_gridding_dat_3d((GXPG)arg1, (GXDAT)arg2, (GXREG)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \\ :func:`geosoft.gxapi.GXPGU.dw_gridding_dat_3d`\\      Inverse-distance weighting gridding method, DAT version, 3D.\n\n"

                ":param arg1: input 3D PG\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: DAT source\n"
                ":type arg2: :class:`geosoft.gxapi.GXDAT`\n"
                ":param arg3: Parameters (see above)\n"
                ":type arg3: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See the notes for \\ :func:`geosoft.gxapi.GXPGU.dw_gridding_db_3d`\\ .\n\n"
               ).staticmethod("dw_gridding_dat_3d");
    pyClass.def("dw_gridding_db", &GXPGU_wrap_dw_gridding_db,
                "dw_gridding_db((GXPG)arg1, (GXDB)arg2, (int)arg3, (int)arg4, (int)arg5, (GXREG)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \\ :func:`geosoft.gxapi.GXPGU.dw_gridding_db`\\      Inverse-distance weighting gridding method, DB version.\n\n"

                ":param arg1: input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Database\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg3: X Channel [READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Channel [READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Data Channel [READONLY]\n"
                ":type arg5: int\n"
                ":param arg6: Parameters (see above)\n"
                ":type arg6: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Grid cells take on the averaged values within a search radius, weighted inversely by distance.\n"
                "   \n"
                "   Weighting can be controlled using the power and slope properties;\n"
                "   \n"
                "   weighting = 1 / (distance^wtpower + 1/slope) where distance is in\n"
                "   units of grid cells (X dimenstion). Default is 0.0,\n"
                "   \n"
                "   If the blanking distance is set, all cells whose center point is not within the blanking distance of\n"
                "   at least one data point are set to dummy.\n"
                "   \n"
                "   REG Parameters:\n"
                "   \n"
                "   X0, Y0, DX, DY: Grid origin, and cell sizes (required)\n"
                "   WT_POWER (default=2), WT_SLOPE (default=1) Weighting function parameters\n"
                "   SEARCH_RADIUS: Distance weighting limit (default = 4 \\ `*`\\  SQRT(DX\\ `*`\\ DY))\n"
                "   BLANKING_DISTANCE: Dummy values farther from data than this distance. (default = 4 \\ `*`\\  SQRT(DX\\ `*`\\ DY))\n"
                "   LOG: Apply log transform to input data before gridding (0:No (default), 1:Yes)?\n"
                "   LOG_BASE: One of VV_LOG_BASE_10 (default) or VV_LOG_BASE_E\n"
                "   LOG_NEGATIVE: One of VV_LOG_NEGATIVE_NO (default) or VV_LOG_NEGATIVE_YES\n\n"
               ).staticmethod("dw_gridding_db");
    pyClass.def("dw_gridding_db_3d", &GXPGU_wrap_dw_gridding_db_3d,
                "dw_gridding_db_3d((GXPG)arg1, (GXDB)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (GXREG)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \\ :func:`geosoft.gxapi.GXPGU.dw_gridding_db_3d`\\      Inverse-distance weighting gridding method, DB version, 3D.\n\n"

                ":param arg1: input 3D PG\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Database\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg3: X Channel [READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Y Channel [READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Z Channel [READONLY]\n"
                ":type arg5: int\n"
                ":param arg6: Data Channel [READONLY]\n"
                ":type arg6: int\n"
                ":param arg7: Parameters (see above)\n"
                ":type arg7: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   3D cells take on the averaged values within a search radius, weighted inversely by distance.\n"
                "   \n"
                "   Weighting can be controlled using the power and slope properties;\n"
                "   \n"
                "   weighting = 1 / (distance^wtpower + 1/slope) where distance is in\n"
                "   units of grid cells (X dimenstion). Default is 0.0,\n"
                "   \n"
                "   If the blanking distance is set, all cells whose center point is not within the blanking distance of\n"
                "   at least one data point are set to dummy.\n"
                "   \n"
                "   REG Parameters:\n"
                "   \n"
                "   X0, Y0, Z0, DX, DY, DZ: Grid origin, and cell sizes (required)\n"
                "   WT_POWER (default=2), WT_SLOPE (default=1) Weighting function parameters\n"
                "   SEARCH_RADIUS: Distance weighting limit (default = 4 \\ `*`\\  CUBE_ROOT(DX\\ `*`\\ DY\\ `*`\\ DZ))\n"
                "   BLANKING_DISTANCE: Dummy values farther from data than this distance. (default = 4 \\ `*`\\  CUBE_ROOT(DX\\ `*`\\ DY\\ `*`\\ DZ))\n"
                "   LOG: Apply log transform to input data before gridding (0:No (default), 1:Yes)?\n"
                "   LOG_BASE: One of VV_LOG_BASE_10 (default) or VV_LOG_BASE_E\n"
                "   LOG_NEGATIVE: One of VV_LOG_NEGATIVE_NO (default) or VV_LOG_NEGATIVE_YES\n\n"
               ).staticmethod("dw_gridding_db_3d");
    pyClass.def("dw_gridding_vv", &GXPGU_wrap_dw_gridding_vv,
                "dw_gridding_vv((GXPG)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXREG)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \\ :func:`geosoft.gxapi.GXPGU.dw_gridding_vv`\\      Inverse-distance weighting gridding method, VV version.\n\n"

                ":param arg1: input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: X locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y locations\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Data values to grid\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Parameters (see above)\n"
                ":type arg5: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See the notes for \\ :func:`geosoft.gxapi.GXPGU.dw_gridding_db`\\ .\n\n"
               ).staticmethod("dw_gridding_vv");
    pyClass.def("numeric_to_thematic", &GXPGU_wrap_numeric_to_thematic,
                "numeric_to_thematic((GXPG)arg1, (GXVV)arg2, (GXPG)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \\ :func:`geosoft.gxapi.GXPGU.numeric_to_thematic`\\     Set index values in a pager based on a numeric pager with translation VV.\n"
                "   \n"
                "   Returns			  Nothing\n\n"

                ":param arg1: Input numeric PG\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Translation VV (see notes above)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Output thematic PG\n"
                ":type arg3: :class:`geosoft.gxapi.GXPG`\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The values in the input data VV represent the center-of-range\n"
                "   values of unique properties with indices 0 to N-1, where N\n"
                "   is the number of items in the input VV.\n"
                "   \n"
                "   This VV is sorted from smallest to largest, and each value in\n"
                "   in the input numeric PG is tested to see into which range it goes.\n"
                "   The closest range value for each item is used, so the half-way point\n"
                "   is the dividing point. The top and bottom-most range widths are determined\n"
                "   by the \"inside half-width\" to the nearest range.\n"
                "   \n"
                "   The INDEX of the closest range is then inserted into the output PG, so\n"
                "   it can be used in a thematic voxel (for instance).\n\n"
               ).staticmethod("numeric_to_thematic");
    pyClass.def("peakedness", &GXPGU_wrap_peakedness,
                "peakedness((str)arg1, (int)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Find all peaks in peakedneess grid pager\n\n"

                ":param arg1: Grid file name\n"
                ":type arg1: str\n"
                ":param arg2: Cutoff limit for finding peaks\n"
                ":type arg2: int\n"
                ":param arg3: X of found peaks\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Y of found peaks\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Z values of found peaks\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"
               ).staticmethod("peakedness");
    pyClass.def("peakedness_grid", &GXPGU_wrap_peakedness_grid,
                "peakedness_grid((str)arg1, (str)arg2, (int)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create peakedneess grid from input grid.\n\n"

                ":param arg1: Input grid file name\n"
                ":type arg1: str\n"
                ":param arg2: Output grid (peakedness) file name\n"
                ":type arg2: str\n"
                ":param arg3: Radius\n"
                ":type arg3: int\n"
                ":param arg4: PercentLess\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function creates a peakedneess grid from input grid.\n"
                "   Radius, is the maximum radius at which the value of the parent pixel is compared to\n"
                "   the value of surrounding pixels.\n"
                "   PercentLesser, is used to indicate the percentage of pixels at each radii smaller than\n"
                "   or equal to Radius that must have value lower than the parent pixel in order to call\n"
                "   that radius true or equal to 1.\n"
                "   Description:  For each pixel in the grid a series of radii are evaluated from 1 to Radius.\n"
                "   If the percentage of pixels for a given radius is less than PercentLesser the parent pixel\n"
                "   receives an additional 1.\n"
                "   For examples if the Radius is set to 5 and the PercentLesser is set to 70%.\n"
                "   And radius 1 = 90%, radius 2 = 85%, radius 3 = 75%, radius 4 = 70% and radius 5 = 65%\n"
                "   then the parent pixel would receive 1+1+1+1+0 = 4.\n"
                "   Use:  This function is useful in isolating the anomaly peaks in data that has a large\n"
                "   value range for anomalies. For example the 1 mV anomaly could quite possibly have\n"
                "   the same representation as the 100 mV anomaly using this function.\n\n"
               ).staticmethod("peakedness_grid");
    pyClass.def("ref_file", &GXPGU_wrap_ref_file,
                "ref_file((GXPG)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a reference file (boolean mask flag) from pager.\n\n"

                ":param arg1: PG object\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Reference file name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   A reference file is a binary file with the following format:\n"
                "   \n"
                "   The first 8 bytes are the pager dimensions NX and NY as longs.\n"
                "   The remaining bits, one bit per pager cell - (NX \\ `*`\\  NY)/8 bytes\n"
                "   are zero where the pager is dummy, and 1 where the pager is defined.\n"
                "   \n"
                "   The reference file is used in various operations where it is\n"
                "   necessary to mask some output to the original defined cells.\n\n"
               ).staticmethod("ref_file");
    pyClass.def("save_file", &GXPGU_wrap_save_file,
                "save_file((GXPG)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (GXTR)arg7, (GXIPJ)arg8, (str)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Writes a PG to an image file.\n\n"

                ":param arg1: input PG object\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: X origin\n"
                ":type arg2: float\n"
                ":param arg3: Y origin\n"
                ":type arg3: float\n"
                ":param arg4: DX\n"
                ":type arg4: float\n"
                ":param arg5: DY\n"
                ":type arg5: float\n"
                ":param arg6: rotation angle\n"
                ":type arg6: float\n"
                ":param arg7: Trend information or NULL\n"
                ":type arg7: :class:`geosoft.gxapi.GXTR`\n"
                ":param arg8: Projection or NULL\n"
                ":type arg8: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg9: Output file name\n"
                ":type arg9: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The trend object and projection are optional.\n\n"
               ).staticmethod("save_file");
    pyClass.def("thematic_to_numeric", &GXPGU_wrap_thematic_to_numeric,
                "thematic_to_numeric((GXPG)arg1, (GXVV)arg2, (GXPG)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set numeric values in a pager based on an index pager with translation VV.\n"
                "   \n"
                "   Returns			  Nothing\n\n"

                ":param arg1: Input Index PG\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Translation VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Output Data PG\n"
                ":type arg3: :class:`geosoft.gxapi.GXPG`\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The items in the input data VV are inserted into\n"
                "   the output PG using the indices in the index PG.\n"
                "   \n"
                "   This function is useful when converting a thematic voxel, which is\n"
                "   type GS_LONG and contains indices into its own internal TPAT\n"
                "   object, and you provide a numeric mapping VV, calculated using\n"
                "   SetupTranslateToNumericVV_TPAT.\n\n"
               ).staticmethod("thematic_to_numeric");
    pyClass.def("trend", &GXPGU_wrap_trend,
                "trend((GXPG)arg1, (GXPG)arg2, (GXTR)arg3, (int)arg4, (int)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Trend remove or replace back in pager\n\n"

                ":param arg1: original pager obj\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: trended pager obj\n"
                ":type arg2: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg3: trend obj\n"
                ":type arg3: :class:`geosoft.gxapi.GXTR`\n"
                ":param arg4: option  0 - calculate, 1 - given in TR, 2 - replace back from TR\n"
                ":type arg4: int\n"
                ":param arg5: trend base on: 0 - all points, 1 - edge points\n"
                ":type arg5: int\n"
                ":param arg6: trend orogin  rXo,\n"
                ":type arg6: float\n"
                ":param arg7: trend orogin  rYo,\n"
                ":type arg7: float\n"
                ":param arg8: inclrement in X directon  rDx,\n"
                ":type arg8: float\n"
                ":param arg9: inclrement in Y directon  rDy\n"
                ":type arg9: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("trend");
    pyClass.def("add_scalar", &GXPGU_wrap_add_scalar,
                "add_scalar((GXPG)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a scalar value to a pager\n\n"

                ":param arg1: Pager\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Scalar Value\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Only available for FLOAT or DOUBLE pagers\n\n"
               ).staticmethod("add_scalar");
    pyClass.def("multiply_scalar", &GXPGU_wrap_multiply_scalar,
                "multiply_scalar((GXPG)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Multiply a scalar value and a pager\n\n"

                ":param arg1: Pager\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Scalar Value\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Only available for FLOAT or DOUBLE pagers\n\n"
               ).staticmethod("multiply_scalar");
    pyClass.def("correlation_matrix", &GXPGU_wrap_correlation_matrix,
                "correlation_matrix((GXPG)arg1, (GXPG)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the correlations between columns in a matrix\n\n"

                ":param arg1: input matrix\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: returned correlation matrix\n"
                ":type arg2: :class:`geosoft.gxapi.GXPG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The input matrix is M rows by N columns. The returned matrix\n"
                "   is a symmetric N by N matrix whose elements are the normalized\n"
                "   dot products of the columns of the input matrix with themselves.\n"
                "   The elements take on values from 0 (orthogonal) to 1 (parallel).\n\n"
               ).staticmethod("correlation_matrix");
    pyClass.def("correlation_matrix2", &GXPGU_wrap_correlation_matrix2,
                "correlation_matrix2((GXPG)arg1, (int)arg2, (GXPG)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXPGU.correlation_matrix`\\ , but select correlation type.\n\n"

                ":param arg1: input matrix\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: \\ :ref:`PGU_CORR`\\ \n"
                ":type arg2: int\n"
                ":param arg3: returned correlation matrix\n"
                ":type arg3: :class:`geosoft.gxapi.GXPG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               ).staticmethod("correlation_matrix2");
    pyClass.def("invert_matrix", &GXPGU_wrap_invert_matrix,
                "invert_matrix((GXPG)arg1, (GXPG)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Inverts a square matrix using LU decomp. and back-substitution\n\n"

                ":param arg1: Input matrix\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Output inverted matrix (can be same as input).\n"
                ":type arg2: :class:`geosoft.gxapi.GXPG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This is an \"in-place\" operation, and set up so that the input and\n"
                "   output pagers may be the same handle. (If they are different, the\n"
                "   input pager remains unchanged).\n"
                "   Pagers and VVs must be type REAL.\n\n"
               ).staticmethod("invert_matrix");
    pyClass.def("jacobi", &GXPGU_wrap_jacobi,
                "jacobi((GXPG)arg1, (GXVV)arg2, (GXPG)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Find eigenvalues, eigenvectors of a real symmetric matrix.\n\n"

                ":param arg1: Input Pager\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Eigenvalues (returned)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Eigenvectors (returned)\n"
                ":type arg3: :class:`geosoft.gxapi.GXPG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The number of rows must equal the number of columns.\n"
                "   Eienvalues, vectors are sorted in descending order.\n\n"
               ).staticmethod("jacobi");
    pyClass.def("lu_back_sub", &GXPGU_wrap_lu_back_sub,
                "lu_back_sub((GXPG)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Solve a linear system using LU decomposition and back-substitution.\n\n"

                ":param arg1: LU decomposition of A\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: permutation vector (type INT)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: right hand side vector B (input)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: solution vector (output)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Solves the system Ax = b for a given b, using the LU decomposition\n"
                "   of the matrix a\n"
                "   The LU decomposition and the permutation vector are obtained\n"
                "   from \\ :func:`geosoft.gxapi.GXPGU.lu_back_sub`\\ .\n"
                "   Pagers and VVs must be type REAL except for the permutation vector,\n"
                "   which should be INT\n\n"
               ).staticmethod("lu_back_sub");
    pyClass.def("lu_decomp", &GXPGU_wrap_lu_decomp,
                "lu_decomp((GXPG)arg1, (GXPG)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Perform an LU decomposition on a square pager.\n\n"

                ":param arg1: input\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: LU decomposition (may be same pager as input)\n"
                ":type arg2: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg3: permutation vector (type INT)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The L and U matrix are both contained in the returned pager; The\n"
                "   \"L\" matrix is composed of the sub-diagonal elements of the output\n"
                "   pager, as well as \"1\" values on the diagonal. The \"U\" matrix is\n"
                "   composed of the diagonal elements (sub-diagonal elements set to 0).\n"
                "   This is an \"in-place\" operation, and set up so that the input and\n"
                "   output pagers may be the same handle. (If they are different, the\n"
                "   input pager remains unchanged).\n"
                "   The LU decomposition, and the permutation vector are used for\n"
                "   \\ :func:`geosoft.gxapi.GXPGU.lu_back_sub`\\ .\n"
                "   Pagers must be type REAL and the permutation vector type INT\n\n"
               ).staticmethod("lu_decomp");
    pyClass.def("matrix_mult", &GXPGU_wrap_matrix_mult,
                "matrix_mult((GXPG)arg1, (int)arg2, (GXPG)arg3, (int)arg4, (GXPG)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Multiply two pagers as if they were matrices.\n\n"

                ":param arg1: matrix U\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: TRUE (1) if U should be transposed before multiplication\n"
                ":type arg2: int\n"
                ":param arg3: matrix V\n"
                ":type arg3: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg4: TRUE (1) if V should be transposed before multiplication\n"
                ":type arg4: int\n"
                ":param arg5: returned matrix U\\ `*`\\ V\n"
                ":type arg5: :class:`geosoft.gxapi.GXPG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The matrices must be correctly dimensioned, taking into\n"
                "   account whether transposition should occur before\n"
                "   multiplication. The input matrices are not altered on output (even\n"
                "   if transposition is requested).\n"
                "   Assertions if: Matrices are not expected sizes\n"
                "   Dummies are treated as 0 values.\n\n"
               ).staticmethod("matrix_mult");
    pyClass.def("matrix_vector_mult", &GXPGU_wrap_matrix_vector_mult,
                "matrix_vector_mult((GXPG)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Multiply a VV by a pager like a matrix\\ `*`\\ vector multiply.\n\n"

                ":param arg1: matrix U\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: vector x\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: returned vector U\\ `*`\\ x\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The matrix is input as an M rows (data) by N columns (variables) PG.\n"
                "   The vector must be of length N. The output VV is set to length M.\n"
                "   The PG and VVs must be type GS_DOUBLE.\n"
                "   Terminates if: Matrices, VV are not expected sizes (taken from U)\n"
                "                  PGs are not REAL.\n"
                "   Dummies are treated as 0 values.\n\n"
               ).staticmethod("matrix_vector_mult");
    pyClass.def("sv_decompose", &GXPGU_wrap_sv_decompose,
                "sv_decompose((GXPG)arg1, (GXPG)arg2, (GXVV)arg3, (GXPG)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Do a singular value decomposition on a matrix stored as a PG\n\n"

                ":param arg1: Input A matrix, M data (rows), N variables (columns)\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: The returned U Matrix\n"
                ":type arg2: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg3: Returned weights (W)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Returned V matrix\n"
                ":type arg4: :class:`geosoft.gxapi.GXPG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The matrix is input as an N rows (data) by M columns (variables) PG.\n"
                "   On return, the matrix is decomposed to A = U \\ `*`\\  W \\ `*`\\  Vt.\n"
                "   If M<N, then an error will be registered. In this case, augment the\n"
                "   \"A\" PG with rows of zero values.\n"
                "   The input matrices must be A[M,N], U[M.N] and V[N,N]. The length of the W VV\n"
                "   is set by sSVD_PGU to N.\n"
                "   The Pagers must be type REAL.\n"
                "   Terminates if: U is not M by N. (Taken from size of A)\n"
                "                  V is not N by N. (Taken from #columns in A).\n"
                "                  PGs, VV are not REAL\n\n"
               ).staticmethod("sv_decompose");
    pyClass.def("sv_recompose", &GXPGU_wrap_sv_recompose,
                "sv_recompose((GXPG)arg1, (GXVV)arg2, (GXPG)arg3, (float)arg4, (GXPG)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reconstitute the original matrix from an SVD.\n\n"

                ":param arg1: U matrix\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Weights (W)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: V matrix\n"
                ":type arg3: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg4: Minimum weight to use (Dummy for all)\n"
                ":type arg4: float\n"
                ":param arg5: A matrix (returned)\n"
                ":type arg5: :class:`geosoft.gxapi.GXPG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The matrix is input as an N rows (data) by M columns (variables) PG.\n"
                "   On return, the matrix is decomposed to A = U \\ `*`\\  W \\ `*`\\  Vt.\n"
                "   If M<N, then an error will be registered. In this case, augment the\n"
                "   \"A\" PG with rows of zero values.\n"
                "   The input matrices must be A[M,N], U[M.N] and V[N,N]. The length of the W VV\n"
                "   is set by sSVDecompose_PGU to N.\n"
                "   The Pagers must be type GS_DOUBLE.\n"
                "   Terminates if: U is not M by N. (Taken from size of A)\n"
                "                  V is not N by N. (Taken from #columns in A).\n"
                "                  PGs, VV are not REAL.\n"
                "   Dummies are treated as 0 values.\n\n"
               ).staticmethod("sv_recompose");
    pyClass.def("pc_communality", &GXPGU_wrap_pc_communality,
                "pc_communality((GXPG)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Determines principal component communalities.\n\n"

                ":param arg1: Input pager of the principal components\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: returned communality values\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate communalities (sums of the squares of the column\n"
                "   values in each row)\n"
                "   Pagers and VVs must be type GS_DOUBLE.\n\n"
               ).staticmethod("pc_communality");
    pyClass.def("pc_loadings", &GXPGU_wrap_pc_loadings,
                "pc_loadings((GXPG)arg1, (GXPG)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute the principal component loadings from the standardized data.\n\n"

                ":param arg1: standardized data matrix (M by N)\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: principal component loadings (N by N)\n"
                ":type arg2: :class:`geosoft.gxapi.GXPG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works on columns of the PG.\n"
                "   Calculates the correlation matrix from the columns of the\n"
                "   standardized data, then computes the eigen values and eigenvectors\n"
                "   of the correlation matrix. The loadings are the eigenvectors, ordered\n"
                "   by descending eigenvalues, scaled by the square root of the\n"
                "   eigenvalues. The returned pager must be sized the same as the\n"
                "   input pager.\n"
                "   Correlations are performed using \"PGU_CORR_SIMPLE\", so if you want\n"
                "   Pearson correlations, or wish to use a modified correlation matrix,\n"
                "   use \\ :func:`geosoft.gxapi.GXPGU.pc_loadings2`\\  and input the correlation matrix directly.\n\n"
               ).staticmethod("pc_loadings");
    pyClass.def("pc_loadings2", &GXPGU_wrap_pc_loadings2,
                "pc_loadings2((GXPG)arg1, (GXPG)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as PCLoading_PGU, but input correlation matrix.\n\n"

                ":param arg1: correllation matrix (N by N)\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: principal component loadings (N by N)\n"
                ":type arg2: :class:`geosoft.gxapi.GXPG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See \\ :func:`geosoft.gxapi.GXPGU.pc_loadings`\\ .\n\n"
               ).staticmethod("pc_loadings2");
    pyClass.def("pc_scores", &GXPGU_wrap_pc_scores,
                "pc_scores((GXPG)arg1, (GXPG)arg2, (GXPG)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute the principal component scores from the standardized data.\n\n"

                ":param arg1: standardized data matrix  (M by N)\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: principal component loadings (input) (N by L, L<=N)\n"
                ":type arg2: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg3: principal component scores (returned) (M by L, L<=N)\n"
                ":type arg3: :class:`geosoft.gxapi.GXPG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   t  -1\n"
                "   Forms the product X Ap (Ap Ap),  where X is the\n"
                "   standardized data matrix, and Ap is the matrix of\n"
                "   principal component loadings (see \\ :func:`geosoft.gxapi.GXPGU.pc_loadings`\\ ).\n"
                "   The loadings must be input, and can be calculated by calling\n"
                "   \\ :func:`geosoft.gxapi.GXPGU.pc_loadings`\\ .\n"
                "   Pagers and VVs must be type GS_DOUBLE.\n\n"
               ).staticmethod("pc_scores");
    pyClass.def("pc_standardize", &GXPGU_wrap_pc_standardize,
                "pc_standardize((GXPG)arg1, (GXVV)arg2, (GXVV)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove/Replace mean and standard deviation\n\n"

                ":param arg1: matrix to standardize\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: means\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: standard deviations\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: \\ :ref:`PGU_DIRECTION`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works on columns of the PG.\n\n"
               ).staticmethod("pc_standardize");
    pyClass.def("pc_standardize2", &GXPGU_wrap_pc_standardize2,
                "pc_standardize2((GXPG)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove/Replace mean and standard deviation, subset values.\n\n"

                ":param arg1: matrix to standardize\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: mask VV for data selection (forward only)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: means\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: standard deviations\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: forward or reverse\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Like \\ :func:`geosoft.gxapi.GXPGU.pc_standardize`\\ , except that not all the values are\n"
                "   included in the calculation of the means and standard\n"
                "   deviations. The inclusion is controlled by a mask VV,\n"
                "   The rows where the mask is dummy are not included\n"
                "   in the calculation, but ALL the values are standardized.\n\n"
               ).staticmethod("pc_standardize2");
    pyClass.def("pc_transform", &GXPGU_wrap_pc_transform,
                "pc_transform((GXPG)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Transform/De-transform data.\n\n"

                ":param arg1: matrix to transform\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: detection limits for the columns\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: maximum values for the columns\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: \\ :ref:`PGU_TRANS`\\ \n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: \\ :ref:`PGU_DIRECTION`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works on columns of the PG.\n"
                "   Forward direction: Applies the selected transform to the data.\n"
                "   Backward direction: Applies the inverse transform to the data.\n"
                "   The detection limits are input with a VV. In the forward\n"
                "   transform, data values less than the detection limit are set\n"
                "   to the limit.\n"
                "   The factor limits are input with a VV. In the forward\n"
                "   transform, data values greater than the maximum values are set\n"
                "   to the maximum.\n\n"
               ).staticmethod("pc_transform");
    pyClass.def("pc_varimax", &GXPGU_wrap_pc_varimax,
                "pc_varimax((GXPG)arg1, (GXPG)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Perform the Kaiser Varimax transformation on pr. comp. loadings\n\n"

                ":param arg1: principal component loadings (input) (N by M, M<=N)\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: rotated principal component loadings (returned) (N by L, L<=M)\n"
                ":type arg2: :class:`geosoft.gxapi.GXPG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Rotates the principal components using the Kaiser's varimax\n"
                "   scheme to move move each factor axis to positions so that\n"
                "   projections from each variable on the factor axes are either\n"
                "   near the extremities or near the origin.\n"
                "   Pagers must be type GS_DOUBLE.\n\n"
               ).staticmethod("pc_varimax");
    pyClass.def("maximum_terrain_steepness", &GXPGU_wrap_maximum_terrain_steepness,
                "maximum_terrain_steepness((GXPG)arg1, (int)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute the Maximum Steepness of a topography Pager\n\n"

                ":param arg1: Topography Pager\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Annular Size\n"
                ":type arg2: int\n"
                ":returns: Maximum Terrain Steepness Computation.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Calculates forward-looking slopes SX and SY in the X and Y directions\n"
                "   using pager locations (ix, iy), (ix+size, iy), (ix, iy+isize)\n"
                "   and returns SX\\ `*`\\ SX + SY\\ `*`\\ SY.\n"
                "   The values in the last \"size\" rows and columns are not\n"
                "   processed.\n"
                "   The wrapper was created for testing and development purposes.\n\n"
               ).staticmethod("maximum_terrain_steepness");

    scope().attr("BLAKEY_TEST_ONESIDE") = (int32_t)1;
    scope().attr("BLAKEY_TEST_TWOSIDE") = (int32_t)2;
    scope().attr("BLAKEY_TEST_THREESIDE") = (int32_t)3;
    scope().attr("BLAKEY_TEST_FOURSIDE") = (int32_t)4;
    scope().attr("PGU_CORR_SIMPLE") = (int32_t)0;
    scope().attr("PGU_CORR_PEARSON") = (int32_t)1;
    scope().attr("PGU_DIRECTGRID_MINIMUM") = (int32_t)0;
    scope().attr("PGU_DIRECTGRID_MAXIMUM") = (int32_t)1;
    scope().attr("PGU_DIRECTGRID_MEAN") = (int32_t)2;
    scope().attr("PGU_DIRECTGRID_ITEMS") = (int32_t)3;
    scope().attr("PGU_FORWARD") = (int32_t)0;
    scope().attr("PGU_BACKWARD") = (int32_t)1;
    scope().attr("PGU_TRANS_NONE") = (int32_t)0;
    scope().attr("PGU_TRANS_LOG") = (int32_t)1;
    scope().attr("PGU_INTERP_ORDER_XYZ") = (int32_t)0;
    scope().attr("PGU_INTERP_ORDER_XZY") = (int32_t)1;
    scope().attr("PGU_INTERP_ORDER_YXZ") = (int32_t)2;
    scope().attr("PGU_INTERP_ORDER_YZX") = (int32_t)3;
    scope().attr("PGU_INTERP_ORDER_ZXY") = (int32_t)4;
    scope().attr("PGU_INTERP_ORDER_ZYX") = (int32_t)5;

}
