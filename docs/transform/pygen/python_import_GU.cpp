#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXGU_wrap_dipole_mag(const gx_string_type& arg1, double arg2, double arg3, int32_t arg4, int32_t arg5, double arg6, double arg7)
{
    GXGU::dipole_mag(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXGU_wrap_em_half_space_inv(double arg1, double arg2, int32_t arg3, double arg4, double arg5, GXVVPtr arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, int32_t arg10, int32_t arg11, double arg12)
{
    GXGU::em_half_space_inv(arg1, arg2, (EMLAY_GEOMETRY)arg3, arg4, arg5, arg6, arg7, arg8, arg9, (EM_INV)arg10, (EM_ERR)arg11, arg12);
}
inline void GXGU_wrap_em_half_space_vv(double arg1, double arg2, int32_t arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7)
{
    GXGU::em_half_space_vv(arg1, arg2, (EMLAY_GEOMETRY)arg3, arg4, arg5, arg6, arg7);
}
inline void GXGU_wrap_geometrics2_db(GXDBPtr arg1, GXRAPtr arg2, GXWAPtr arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7, double arg8, double arg9, double arg10, double arg11)
{
    GXGU::geometrics2_db(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXGU_wrap_geometrics2_tbl(GXRAPtr arg1, GXWAPtr arg2, GXWAPtr arg3)
{
    GXGU::geometrics2_tbl(arg1, arg2, arg3);
}
inline void GXGU_wrap_geometrics_qc(GXWAPtr arg1, const gx_string_type& arg2, GXVVPtr arg3, double arg4, double arg5, double arg6, GXVVPtr arg7, GXVVPtr arg8)
{
    GXGU::geometrics_qc(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXGU_wrap_geonics3138_dump2_db(GXDBPtr arg1, GXRAPtr arg2, GXRAPtr arg3, GXWAPtr arg4, double arg5, double arg6)
{
    GXGU::geonics3138_dump2_db(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXGU_wrap_geonics61_dump2_db(GXDBPtr arg1, GXRAPtr arg2, GXWAPtr arg3, double arg4, double arg5)
{
    GXGU::geonics61_dump2_db(arg1, arg2, arg3, arg4, arg5);
}
inline void GXGU_wrap_geonics_dat2_db(GXDBPtr arg1, GXRAPtr arg2, GXWAPtr arg3, double arg4, double arg5)
{
    GXGU::geonics_dat2_db(arg1, arg2, arg3, arg4, arg5);
}
inline void GXGU_wrap_gr_curv_cor(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    GXGU::gr_curv_cor(arg1, arg2, arg3);
}
inline void GXGU_wrap_gr_curv_cor_ex(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, double arg4)
{
    GXGU::gr_curv_cor_ex(arg1, arg2, arg3, arg4);
}
inline void GXGU_wrap_gr_demvv(GXIMGPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4)
{
    GXGU::gr_demvv(arg1, arg2, arg3, arg4);
}
inline void GXGU_wrap_gr_test(double arg1, double arg2, double arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9)
{
    GXGU::gr_test(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXGU_wrap_gravity_still_reading_correction(GXDBPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4, const gx_string_type& arg5, int32_t arg6)
{
    GXGU::gravity_still_reading_correction(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline int32_t GXGU_wrap_em_layer(double arg1, double arg2, double arg3, int32_t arg4, int32_t arg5, GXVVPtr arg6, GXVVPtr arg7, float_ref& arg8, float_ref& arg9)
{
    int32_t ret = GXGU::em_layer(arg1, arg2, arg3, (EMLAY_GEOMETRY)arg4, arg5, arg6, arg7, arg8, arg9);
    return ret;
}
inline int32_t GXGU_wrap_em_plate(double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, int32_t arg10, GXVVPtr arg11, int32_t arg12, double arg13, double arg14, double arg15, GXVVPtr arg16, GXVVPtr arg17, GXVVPtr arg18, GXVVPtr arg19, GXVVPtr arg20, GXVVPtr arg21)
{
    int32_t ret = GXGU::em_plate(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (EMPLATE_DOMAIN)arg10, arg11, (EMPLATE_TX)arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21);
    return ret;
}
inline void GXGU_wrap_gen_ux_detect_symbols_group_name(const gx_string_type& arg1, const gx_string_type& arg2, str_ref& arg3)
{
    GXGU::gen_ux_detect_symbols_group_name(arg1, arg2, arg3);
}
inline void GXGU_wrap_import_daarc500_ethernet(const gx_string_type& arg1, const gx_string_type& arg2, int_ref& arg3)
{
    GXGU::import_daarc500_ethernet(arg1, arg2, arg3);
}
inline void GXGU_wrap_import_daarc500_serial(const gx_string_type& arg1, int32_t arg2, const gx_string_type& arg3, int_ref& arg4)
{
    GXGU::import_daarc500_serial(arg1, arg2, arg3, arg4);
}
inline void GXGU_wrap_import_p190(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXWAPtr arg4)
{
    GXGU::import_p190(arg1, arg2, arg3, arg4);
}
inline void GXGU_wrap_lag_daarc500_gps(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    GXGU::lag_daarc500_gps(arg1, arg2, arg3);
}
inline void GXGU_wrap_maxwell_plate_corners(double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, float_ref& arg9, float_ref& arg10, float_ref& arg11, float_ref& arg12, float_ref& arg13, float_ref& arg14, float_ref& arg15, float_ref& arg16, float_ref& arg17, float_ref& arg18, float_ref& arg19, float_ref& arg20)
{
    GXGU::maxwell_plate_corners(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20);
}
inline void GXGU_wrap_scan_daarc500_ethernet(const gx_string_type& arg1, int_ref& arg2, int_ref& arg3)
{
    GXGU::scan_daarc500_ethernet(arg1, arg2, arg3);
}
inline void GXGU_wrap_scan_daarc500_serial(const gx_string_type& arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    GXGU::scan_daarc500_serial(arg1, arg2, arg3);
}
inline void GXGU_wrap_vv_euler(GXVVPtr arg1, GXVVPtr arg2, GXIMGPtr arg3, GXIMGPtr arg4, GXIMGPtr arg5, GXIMGPtr arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, GXVVPtr arg10, GXVVPtr arg11, GXVVPtr arg12, int32_t arg13, double arg14, double arg15, int32_t arg16)
{
    GXGU::vv_euler(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, (PEAKEULER_XY)arg16);
}
inline void GXGU_wrap_vv_euler2(GXVVPtr arg1, GXVVPtr arg2, GXIMGPtr arg3, GXIMGPtr arg4, GXIMGPtr arg5, GXIMGPtr arg6, GXVVPtr arg7, GXVVPtr arg8, GXVVPtr arg9, GXVVPtr arg10, GXVVPtr arg11, GXVVPtr arg12, GXVVPtr arg13, double arg14, double arg15, int32_t arg16)
{
    GXGU::vv_euler2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, (PEAKEULER_XY)arg16);
}

void gxPythonImportGXGU()
{

    class_<GXGU, boost::noncopyable> pyClass("GXGU",
            "\n.. parsed-literal::\n\n"
            "   Not a class. A catch-all group of functions performing\n"
            "   various geophysical processes, including the calculation\n"
            "   of simple EM model responses, certain instrument dump\n"
            "   file imports, and 2D Euler deconvolution.\n\n"
            , no_init);


    pyClass.def("dipole_mag", &GXGU_wrap_dipole_mag,
                "dipole_mag((str)arg1, (float)arg2, (float)arg3, (int)arg4, (int)arg5, (float)arg6, (float)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate a dipole magnetic field into XYZ file\n\n"

                ":param arg1: sXYZ\n"
                ":type arg1: str\n"
                ":param arg2: rDepth\n"
                ":type arg2: float\n"
                ":param arg3: rInc\n"
                ":type arg3: float\n"
                ":param arg4: iNX\n"
                ":type arg4: int\n"
                ":param arg5: iNY\n"
                ":type arg5: int\n"
                ":param arg6: rDX\n"
                ":type arg6: float\n"
                ":param arg7: rDY\n"
                ":type arg7: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               ).staticmethod("dipole_mag");
    pyClass.def("em_half_space_inv", &GXGU_wrap_em_half_space_inv,
                "em_half_space_inv((float)arg1, (float)arg2, (int)arg3, (float)arg4, (float)arg5, (GXVV)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (int)arg10, (int)arg11, (float)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Inverts EM responses to the best halfspace model.\n\n"

                ":param arg1: coil spacing: error if == 0\n"
                ":type arg1: float\n"
                ":param arg2: frequency\n"
                ":type arg2: float\n"
                ":param arg3: \\ :ref:`EMLAY_GEOMETRY`\\ \n"
                ":type arg3: int\n"
                ":param arg4: fractional error in best fit resistivity\n"
                ":type arg4: float\n"
                ":param arg5: don't invert values below this\n"
                ":type arg5: float\n"
                ":param arg6: Height above ground\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: In-phase part (ppm)\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Quadrature part (ppm)\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: On return - inverted halfspace resistivities\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: \\ :ref:`EM_INV`\\ \n"
                ":type arg10: int\n"
                ":param arg11: \\ :ref:`EM_ERR`\\ \n"
                ":type arg11: int\n"
                ":param arg12: Starting value for inversion (can be rDUMMY)\n"
                ":type arg12: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("em_half_space_inv");
    pyClass.def("em_half_space_vv", &GXGU_wrap_em_half_space_vv,
                "em_half_space_vv((float)arg1, (float)arg2, (int)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   EM Halfspace forward model response.\n\n"

                ":param arg1: Coil separation\n"
                ":type arg1: float\n"
                ":param arg2: frequency\n"
                ":type arg2: float\n"
                ":param arg3: \\ :ref:`EMLAY_GEOMETRY`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Input resistivity values\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Input height values\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Output In-phase\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Output Quadrature-phase\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("em_half_space_vv");
    pyClass.def("geometrics2_db", &GXGU_wrap_geometrics2_db,
                "geometrics2_db((GXDB)arg1, (GXRA)arg2, (GXWA)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7, (float)arg8, (float)arg9, (float)arg10, (float)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a Geometrics STN file to a database.\n\n"

                ":param arg1: DB handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: RA handle, STN file\n"
                ":type arg2: :class:`geosoft.gxapi.GXRA`\n"
                ":param arg3: Log file WA handle\n"
                ":type arg3: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg4: Simple mode (1) or Mapped mode (2)\n"
                ":type arg4: int\n"
                ":param arg5: Survey line orientation:  North-south - 0 East-west   - 1\n"
                ":type arg5: int\n"
                ":param arg6: Starting survey position: SW - 0, NW - 1, SE - 2, NE - 3,\n"
                ":type arg6: int\n"
                ":param arg7: Bidirectional (0) or Unidirectional (1)\n"
                ":type arg7: int\n"
                ":param arg8: Starting position X\n"
                ":type arg8: float\n"
                ":param arg9: Starting position Y\n"
                ":type arg9: float\n"
                ":param arg10: Mark spacing\n"
                ":type arg10: float\n"
                ":param arg11: Line spacing\n"
                ":type arg11: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Assumes that the database is new and empty. If not, existing channels\n"
                "   with names X, Y, Mag1, Mag2, Time, Date,\n"
                "   and Mark will deleted and then created.  Existing lines will\n"
                "   be erased and then created if they are the same as the new ones.\n\n"
               ).staticmethod("geometrics2_db");
    pyClass.def("geometrics2_tbl", &GXGU_wrap_geometrics2_tbl,
                "geometrics2_tbl((GXRA)arg1, (GXWA)arg2, (GXWA)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a Geometrics station file (STN) to a table file (TBL)\n\n"

                ":param arg1: RA handle, input station file\n"
                ":type arg1: :class:`geosoft.gxapi.GXRA`\n"
                ":param arg2: Output TBL file\n"
                ":type arg2: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg3: Log file WA handle\n"
                ":type arg3: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("geometrics2_tbl");
    pyClass.def("geometrics_qc", &GXGU_wrap_geometrics_qc,
                "geometrics_qc((GXWA)arg1, (str)arg2, (GXVV)arg3, (float)arg4, (float)arg5, (float)arg6, (GXVV)arg7, (GXVV)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Correct reading positions in a database.\n\n"

                ":param arg1: Output error log file\n"
                ":type arg1: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg2: Database line number. For output to log file only\n"
                ":type arg2: str\n"
                ":param arg3: Input VV, GS_DOUBLE\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Tolerance defined as percentage, say 50.0 means 50%. Must be >=0.0 Lower bound = (Normal Density) - (Normal Density)\\ `*`\\ Tolerance Upper bound = (Normal Density) + (Normal Density)\\ `*`\\ Tolerance\n"
                ":type arg4: float\n"
                ":param arg5: Minimum coordinate (X or Y)\n"
                ":type arg5: float\n"
                ":param arg6: Maximum coordinate (X or Y)\n"
                ":type arg6: float\n"
                ":param arg7: Output VV, GS_DOUBLE\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Output Flag VV, GS_LONG\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   There are six cases to consider:\n"
                "   \n"
                "   Case        Flag  Solutions      Symptons\n"
                "   -------     ----  -------------  -----------------------------\n"
                "   \n"
                "   CASE 1A:    0     No correction  Recorded and actual Line lengths same\n"
                "                                    Reading densities vary slightly (passed\n"
                "                                    the tolerance test)\n"
                "   \n"
                "   CASE 1B:    -1    No correction  Line lengths same\n"
                "                                    Reading densities vary and cannot\n"
                "                                    pass the tolerance test\n"
                "   \n"
                "   CASE 2A:    1     Corrected by   Recorded line length too short\n"
                "                     extension      Possilble high readings in segment(s)\n"
                "                                    Corrected (by extending) and actual\n"
                "                                    lengths become the same\n"
                "   \n"
                "   CASE 2B:    2     Corrected by   Recorded line length too short\n"
                "                     interpolation  Possilble high readings in segment(s)\n"
                "                                    Corrected (by extending) and actual\n"
                "                                    lengths are not same. Interpolation is\n"
                "                                    then applied\n"
                "   \n"
                "   CASE 3A:    1     Corrected by   Recorded line length too long\n"
                "                     shifting or    Possible low readings in segment(s)\n"
                "                     (shrank)       Corrected (by shifting) and actual\n"
                "                                    lengths are same\n"
                "   \n"
                "   CASE 3B:    2     Corrected by   Recorded line length too long\n"
                "                     interpolation  Possible low readings in segment(s)\n"
                "                                    Corrected (by shifting) and actual\n"
                "                                    lengths are not same. Interpolation\n"
                "                                    is then applied\n"
                "   \n"
                "   \n"
                "   TERMINOLOGY:\n"
                "   \n"
                "   Segments:         A segment refers to the distance and its contents between\n"
                "                     two adjacent fiducial markers\n"
                "   \n"
                "   Normal Density:   The density (number of readings) shared by the segments in\n"
                "                     in a survey line.\n"
                "                     The number of segments with the density is greater than the\n"
                "                     number of segments having a different density in a line.\n"
                "   \n"
                "   Tolerance and Bound:\n"
                "                     Tolerance is defined as a percentage, say 50% (=0.5).\n"
                "                     Based on the tolerance, a lower bound and upper bound\n"
                "   \n"
                "                     can be defined:\n"
                "   \n"
                "                     Lower bound = (Normal Density) - (Normal Density)\\ `*`\\ Tolerance\n"
                "                     Upper bound = (Normal Density) - (Normal Density)\\ `*`\\ Tolerance\n"
                "   \n"
                "                     Segments will pass the tolerance test if the number of readings\n"
                "                     falls within the Lower and Upper Bounds.\n\n"
               ).staticmethod("geometrics_qc");
    pyClass.def("geonics3138_dump2_db", &GXGU_wrap_geonics3138_dump2_db,
                "geonics3138_dump2_db((GXDB)arg1, (GXRA)arg2, (GXRA)arg3, (GXWA)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a Geonics EM31/EM38 file in dump format to a database.\n\n"

                ":param arg1: DB handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: RA handle, Header file\n"
                ":type arg2: :class:`geosoft.gxapi.GXRA`\n"
                ":param arg3: RA handle, Dump file\n"
                ":type arg3: :class:`geosoft.gxapi.GXRA`\n"
                ":param arg4: Log file WA handle\n"
                ":type arg4: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg5: Line multiplier\n"
                ":type arg5: float\n"
                ":param arg6: Station multiplier\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Assumes that the database is new and empty. If not, existing channels\n"
                "   with names X, Y, Station, Conductivity, Inphase, Quadrature,\n"
                "   and Time will deleted and then created.  Existing lines will\n"
                "   be erased and then created if they are the same as the new ones.\n\n"
               ).staticmethod("geonics3138_dump2_db");
    pyClass.def("geonics61_dump2_db", &GXGU_wrap_geonics61_dump2_db,
                "geonics61_dump2_db((GXDB)arg1, (GXRA)arg2, (GXWA)arg3, (float)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a Geonics EM61 file in dump format to a database.\n\n"

                ":param arg1: DB handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: RA handle, dump file\n"
                ":type arg2: :class:`geosoft.gxapi.GXRA`\n"
                ":param arg3: Log file WA handle\n"
                ":type arg3: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg4: Line multiplier\n"
                ":type arg4: float\n"
                ":param arg5: Station multiplier - Not used in the calculation\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Assumes that the database is new and empty. If not, existing channels\n"
                "   with names X, Y, Station, Conductivity, Inphase, Quadrature,\n"
                "   and Time will deleted and then created.  Existing lines will\n"
                "   be erased and then created if they are the same as the new ones.\n\n"
               ).staticmethod("geonics61_dump2_db");
    pyClass.def("geonics_dat2_db", &GXGU_wrap_geonics_dat2_db,
                "geonics_dat2_db((GXDB)arg1, (GXRA)arg2, (GXWA)arg3, (float)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a Geonics EM31/EM38/EM61 file in DAT format to a database.\n\n"

                ":param arg1: DB handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: RA handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXRA`\n"
                ":param arg3: Log file WA handle\n"
                ":type arg3: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg4: Line multiplier\n"
                ":type arg4: float\n"
                ":param arg5: Station multiplier - Not used in the calculation\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Assumes that the database is new and empty. If not, existing channels\n"
                "   with names X, Y, Station, Conductivity, Inphase, Quadrature,\n"
                "   and Time will deleted and then created.  Existing lines will\n"
                "   be erased and then created if they are the same as the new ones.\n\n"
               ).staticmethod("geonics_dat2_db");
    pyClass.def("gr_curv_cor", &GXGU_wrap_gr_curv_cor,
                "gr_curv_cor((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gravity Curvature (Bullard B) Correction to Bouguer anomaly\n\n"

                ":param arg1: Input Elevation VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Input Latitude VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Bouguer VV for Curvature Correction\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("gr_curv_cor");
    pyClass.def("gr_curv_cor_ex", &GXGU_wrap_gr_curv_cor_ex,
                "gr_curv_cor_ex((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gravity Curvature (Bullard B) Correction to Bouguer anomaly, with user input cap density.\n\n"

                ":param arg1: Input Elevation VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Input Latitude VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Bouguer VV for Curvature Correction\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Cap Density (g/cm^3\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"
               ).staticmethod("gr_curv_cor_ex");
    pyClass.def("gr_demvv", &GXGU_wrap_gr_demvv,
                "gr_demvv((GXIMG)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get gravity DEM grid VV for Bouguer anomaly\n\n"

                ":param arg1: DEM grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Input X VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Input Y VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Output DEM VV for Bouguer Correction\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("gr_demvv");
    pyClass.def("gr_test", &GXGU_wrap_gr_test,
                "gr_test((float)arg1, (float)arg2, (float)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Test triangular prism gravity calculation\n\n"

                ":param arg1: dXm  - model dimension x\n"
                ":type arg1: float\n"
                ":param arg2: dYm  - model dimension y\n"
                ":type arg2: float\n"
                ":param arg3: dZm  - model depth\n"
                ":type arg3: float\n"
                ":param arg4: VVx  - stations x\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: VVy  - stations y\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: VVg3 - 2 triangular prism gravity results\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: VVg4 - regtangular prism gravity results\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: VVg1 - lower triangular prism gravity results\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: VVg2 - upper triangular prism gravity results\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"
               ).staticmethod("gr_test");
    pyClass.def("gravity_still_reading_correction", &GXGU_wrap_gravity_still_reading_correction,
                "gravity_still_reading_correction((GXDB)arg1, (int)arg2, (int)arg3, (int)arg4, (str)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gravity Still Reading Correction on selected lines.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Input gravity channel handle [DB_LOCK_READONLY]\n"
                ":type arg2: int\n"
                ":param arg3: Input date channel handle [DB_LOCK_READONLY]\n"
                ":type arg3: int\n"
                ":param arg4: Input time channel handle [DB_LOCK_READONLY]\n"
                ":type arg4: int\n"
                ":param arg5: Still readings file\n"
                ":type arg5: str\n"
                ":param arg6: Output gravity channel handle [DB_LOCK_READWRITE]\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               ).staticmethod("gravity_still_reading_correction");
    pyClass.def("em_layer", &GXGU_wrap_em_layer,
                "em_layer((float)arg1, (float)arg2, (float)arg3, (int)arg4, (int)arg5, (GXVV)arg6, (GXVV)arg7, (float_ref)arg8, (float_ref)arg9) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the EM response of a layered earth model.\n\n"

                ":param arg1: coil spacing, error if == 0\n"
                ":type arg1: float\n"
                ":param arg2: coil frequency\n"
                ":type arg2: float\n"
                ":param arg3: coil height above layer [0]\n"
                ":type arg3: float\n"
                ":param arg4: \\ :ref:`EMLAY_GEOMETRY`\\ \n"
                ":type arg4: int\n"
                ":param arg5: Number of layers (including lower halfspace)\n"
                ":type arg5: int\n"
                ":param arg6: sNLayer-1 thicknesses  [0] to [sNLayer-2]\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: sNLayer conductivities [0] to [sNLayer-1]\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: On return - in-phase part (ppm)\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: On return - quadrature part (ppm)\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 of OK\n"
                "          1 if some error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("em_layer");
    pyClass.def("em_plate", &GXGU_wrap_em_plate,
                "em_plate((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (int)arg10, (GXVV)arg11, (int)arg12, (float)arg13, (float)arg14, (float)arg15, (GXVV)arg16, (GXVV)arg17, (GXVV)arg18, (GXVV)arg19, (GXVV)arg20, (GXVV)arg21) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the conductance of a thin plate model.\n\n"

                ":param arg1: plate strike length (m)\n"
                ":type arg1: float\n"
                ":param arg2: Plate dip length (m)\n"
                ":type arg2: float\n"
                ":param arg3: Plate strike (degrees) from X axis\n"
                ":type arg3: float\n"
                ":param arg4: Plate dip (degrees) from horizontal\n"
                ":type arg4: float\n"
                ":param arg5: plate plunge (degrees) from horizontal\n"
                ":type arg5: float\n"
                ":param arg6: Rx offset in X from Tx\n"
                ":type arg6: float\n"
                ":param arg7: Rx offset in Y from Tx\n"
                ":type arg7: float\n"
                ":param arg8: Rx offset in Z from Tx (+'ve down)\n"
                ":type arg8: float\n"
                ":param arg9: Depth below Tx\n"
                ":type arg9: float\n"
                ":param arg10: \\ :ref:`EMPLATE_DOMAIN`\\ \n"
                ":type arg10: int\n"
                ":param arg11: The plate conductances (VV length <= 100)\n"
                ":type arg11: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg12: \\ :ref:`EMPLATE_TX`\\ \n"
                ":type arg12: int\n"
                ":param arg13: Tx frequency (for EMPLATE_TIME)\n"
                ":type arg13: float\n"
                ":param arg14: Tx time window spacing (for EMPLATE_TIME)\n"
                ":type arg14: float\n"
                ":param arg15: The frequency/time parameters (SI units: f[Hz] or t[s])\n"
                ":type arg15: float\n"
                ":param arg16: On return - X in-phase part (ppm)\n"
                ":type arg16: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg17: On return - Y in-phase part (ppm)\n"
                ":type arg17: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg18: On return - Z in-phase part (ppm)\n"
                ":type arg18: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg19: On return - X quadrature part (ppm)\n"
                ":type arg19: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg20: On return - Y quadrature part (ppm)\n"
                ":type arg20: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg21: On return - Z quadrature part (ppm)\n"
                ":type arg21: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: 0 of OK\n"
                "          1 if some error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("em_plate");
    pyClass.def("gen_ux_detect_symbols_group_name", &GXGU_wrap_gen_ux_detect_symbols_group_name,
                "gen_ux_detect_symbols_group_name((str)arg1, (str)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a group name string for UX-Detect symbols\n\n"

                ":param arg1: input Targets database name\n"
                ":type arg1: str\n"
                ":param arg2: input Targets group (line) name\n"
                ":type arg2: str\n"
                ":param arg3: output group name string\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Start a new group for the symbols in the UX-Detect system.\n"
                "   The Target GDB is often in the form \"GDB_Targets\", where\n"
                "   \"GDB\" is the original data. Cut off the part including the\n"
                "   underscore when creating the map, so you don't get map group\n"
                "   Names like \"SYMBOLS_UxData_Targets_Targets\".\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXSTR.gen_group_name`\\ \n\n"
               ).staticmethod("gen_ux_detect_symbols_group_name");
    pyClass.def("import_daarc500_ethernet", &GXGU_wrap_import_daarc500_ethernet,
                "import_daarc500_ethernet((str)arg1, (str)arg2, (int_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import Ethernet data from the RMS Instruments DAARC500.\n\n"

                ":param arg1: File to import\n"
                ":type arg1: str\n"
                ":param arg2: Output binary file\n"
                ":type arg2: str\n"
                ":param arg3: Returned number of bytes per block\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Imports Ethernet data recorded\n"
                "   by the RMS Instruments DAARC500 instrument, and outputs the data\n"
                "   to a new binary file, returning the number of bytes per\n"
                "   block, to make it easier to import the data using the regular binary import.\n\n"
               ).staticmethod("import_daarc500_ethernet");
    pyClass.def("import_daarc500_serial", &GXGU_wrap_import_daarc500_serial,
                "import_daarc500_serial((str)arg1, (int)arg2, (str)arg3, (int_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import Serial data from the RMS Instruments DAARC500.\n\n"

                ":param arg1: File to import\n"
                ":type arg1: str\n"
                ":param arg2: Channel to import, 1-8\n"
                ":type arg2: int\n"
                ":param arg3: Output binary file\n"
                ":type arg3: str\n"
                ":param arg4: Returned number of bytes per block\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Imports a single channel of the up to 8 serial data channels recorded\n"
                "   by the RMS Instruments DAARC500 instrument, and outputs the data for\n"
                "   that channel to a new binary file, returning the number of bytes per\n"
                "   block, to make it easier to import the data using the regular binary import.\n\n"
               ).staticmethod("import_daarc500_serial");
    pyClass.def("import_p190", &GXGU_wrap_import_p190,
                "import_p190((GXDB)arg1, (str)arg2, (str)arg3, (GXWA)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import navigation data in the P190 format.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: P190 file name\n"
                ":type arg2: str\n"
                ":param arg3: Single letter code, e.g. \"C\", \"E\", \"S\", \"T\" or \"V\", or blank for all records.\n"
                ":type arg3: str\n"
                ":param arg4: Log file\n"
                ":type arg4: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Imports the data, and, if projection information is included\n"
                "   set the \"X\" and \"Y\" channel projection info. (Note: the last file\n"
                "   imported always takes precedence).\n"
                "   Different record types are imported to separate lines, but in the\n"
                "   same order as in the file. Data in existing lines is overwritten.\n"
                "   If the record type is specified, only records beginning with that\n"
                "   letter are imported, otherwise all records (except for the header \"H\"\n"
                "   records) are imported.\n\n"
               ).staticmethod("import_p190");
    pyClass.def("lag_daarc500_gps", &GXGU_wrap_lag_daarc500_gps,
                "lag_daarc500_gps((GXVV)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Lag the GPS fid values for the DAARC500 import.\n\n"

                ":param arg1: Mag fid values   (GS_DOUBLE)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Mag event values (GS_LONG)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: GPS fid values (GS_DOUBLE, altered on return)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The fiducial times recorded for the GPS in the RMS Instrument DAARC500\n"
                "   are delayed, and associated with the \"wrong\" fid value. They should actually\n"
                "   be moved to the previous fid value in the mag data where the event flag is non-zero.\n\n"
               ).staticmethod("lag_daarc500_gps");
    pyClass.def("maxwell_plate_corners", &GXGU_wrap_maxwell_plate_corners,
                "maxwell_plate_corners((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float_ref)arg9, (float_ref)arg10, (float_ref)arg11, (float_ref)arg12, (float_ref)arg13, (float_ref)arg14, (float_ref)arg15, (float_ref)arg16, (float_ref)arg17, (float_ref)arg18, (float_ref)arg19, (float_ref)arg20) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the corner point locations for a Maxwell Plate.\n\n"

                ":param arg1: Top-center point, X\n"
                ":type arg1: float\n"
                ":param arg2: Top-center point, Y\n"
                ":type arg2: float\n"
                ":param arg3: Top-center point, Z\n"
                ":type arg3: float\n"
                ":param arg4: dip\n"
                ":type arg4: float\n"
                ":param arg5: dip-direction\n"
                ":type arg5: float\n"
                ":param arg6: plunge\n"
                ":type arg6: float\n"
                ":param arg7: length\n"
                ":type arg7: float\n"
                ":param arg8: width (height)\n"
                ":type arg8: float\n"
                ":param arg9: [returned] Corner 1 X\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: [returned] Corner 1 Y\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: [returned] Corner 1 Z\n"
                ":type arg11: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg12: [returned] Corner 2 X\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg13: [returned] Corner 2 Y\n"
                ":type arg13: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg14: [returned] Corner 2 Z\n"
                ":type arg14: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg15: [returned] Corner 3 X\n"
                ":type arg15: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg16: [returned] Corner 3 Y\n"
                ":type arg16: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg17: [returned] Corner 3 Z\n"
                ":type arg17: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg18: [returned] Corner 4 X\n"
                ":type arg18: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg19: [returned] Corner 4 Y\n"
                ":type arg19: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg20: [returned] Corner 4 Z\n"
                ":type arg20: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This routine calculates the corner locations of plates defined in the Maxwell Plate\n"
                "   program, given the top-center location and plate geometry parameters.\n\n"
               ).staticmethod("maxwell_plate_corners");
    pyClass.def("scan_daarc500_ethernet", &GXGU_wrap_scan_daarc500_ethernet,
                "scan_daarc500_ethernet((str)arg1, (int_ref)arg2, (int_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Scan Ethernet data from the RMS Instruments DAARC500.\n\n"

                ":param arg1: File to import\n"
                ":type arg1: str\n"
                ":param arg2: Recognized type\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Number of items\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Scans the file to see what data type is in the Ethernet file.\n"
                "   Currently only detects GR820 types.\n\n"
               ).staticmethod("scan_daarc500_ethernet");
    pyClass.def("scan_daarc500_serial", &GXGU_wrap_scan_daarc500_serial,
                "scan_daarc500_serial((str)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Scan Serial data from the RMS Instruments DAARC500.\n\n"

                ":param arg1: File to import\n"
                ":type arg1: str\n"
                ":param arg2: 8 Recognized types - GS_LONG\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: 8 Numbers of items - GS_LONG\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Scans the file to see which of the 8 serial channels were used to store data.\n\n"
               ).staticmethod("scan_daarc500_serial");
    pyClass.def("vv_euler", &GXGU_wrap_vv_euler,
                "vv_euler((GXVV)arg1, (GXVV)arg2, (GXIMG)arg3, (GXIMG)arg4, (GXIMG)arg5, (GXIMG)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (GXVV)arg10, (GXVV)arg11, (GXVV)arg12, (int)arg13, (float)arg14, (float)arg15, (int)arg16) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get Euler solutions of depth from VVs and grids.\n\n"

                ":param arg1: Input X VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Input Y VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Field grid\n"
                ":type arg3: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg4: dF/dX grid\n"
                ":type arg4: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg5: dF/dY grid\n"
                ":type arg5: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg6: dF/dZ grid\n"
                ":type arg6: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg7: Output X VV\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Output Y VV\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Output depth VV\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Output background field VV\n"
                ":type arg10: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg11: Output depth uncertainty VV\n"
                ":type arg11: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg12: Output XY uncertainty VV\n"
                ":type arg12: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg13: Window size\n"
                ":type arg13: int\n"
                ":param arg14: Structure index\n"
                ":type arg14: float\n"
                ":param arg15: Weighting factor\n"
                ":type arg15: float\n"
                ":param arg16: \\ :ref:`PEAKEULER_XY`\\ \n"
                ":type arg16: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   All VVs must be REAL\n"
                "   \n"
                "   The output X and Y values are the same as the inputs,\n"
                "   except if PEAKEULER_XY_FIT is selected. All other\n"
                "   output values are set to dummy if:\n"
                "        a) The input X or Y is a dummy\n"
                "        b) The derived window size is a dummy.\n"
                "        c) The derived solution is outside the range\n"
                "        d) The solution is invalid (singular matrix)\n\n"
               ).staticmethod("vv_euler");
    pyClass.def("vv_euler2", &GXGU_wrap_vv_euler2,
                "vv_euler2((GXVV)arg1, (GXVV)arg2, (GXIMG)arg3, (GXIMG)arg4, (GXIMG)arg5, (GXIMG)arg6, (GXVV)arg7, (GXVV)arg8, (GXVV)arg9, (GXVV)arg10, (GXVV)arg11, (GXVV)arg12, (GXVV)arg13, (float)arg14, (float)arg15, (int)arg16) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get Euler solutions of depth from VVs and grids (method 2).\n\n"

                ":param arg1: Input X VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Input Y VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Field grid\n"
                ":type arg3: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg4: dF/dX grid\n"
                ":type arg4: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg5: dF/dY grid\n"
                ":type arg5: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg6: dF/dZ grid\n"
                ":type arg6: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg7: Output X VV\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: Output Y VV\n"
                ":type arg8: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg9: Output depth VV\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg10: Output background field VV\n"
                ":type arg10: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg11: Output depth uncertainty VV\n"
                ":type arg11: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg12: Output XY uncertainty VV\n"
                ":type arg12: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg13: Window size (diameters of targets)\n"
                ":type arg13: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg14: Structure index\n"
                ":type arg14: float\n"
                ":param arg15: Weighting factor\n"
                ":type arg15: float\n"
                ":param arg16: \\ :ref:`PEAKEULER_XY`\\ \n"
                ":type arg16: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   All VVs must be REAL\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXGU.vv_euler`\\ \n\n"
               ).staticmethod("vv_euler2");

    scope().attr("EM_ERR_UNSCALED") = (int32_t)0;
    scope().attr("EM_ERR_LOGSCALING") = (int32_t)1;
    scope().attr("EM_INV_INPHASE") = (int32_t)0;
    scope().attr("EM_INV_QUADRATURE") = (int32_t)1;
    scope().attr("EM_INV_BOTH") = (int32_t)2;
    scope().attr("EMPLATE_FREQUENCY") = (int32_t)1;
    scope().attr("EMPLATE_TIME") = (int32_t)9;
    scope().attr("EMPLATE_TX_X") = (int32_t)1;
    scope().attr("EMPLATE_TX_Y") = (int32_t)2;
    scope().attr("EMPLATE_TX_Z") = (int32_t)3;
    scope().attr("GU_DAARC500_UNKNOWN") = (int32_t)0;
    scope().attr("GU_DAARC500_GENERIC_ASCII") = (int32_t)1;
    scope().attr("GU_DAARC500_GPS") = (int32_t)2;
    scope().attr("GU_DAARC500_GR820_256D") = (int32_t)3;
    scope().attr("GU_DAARC500_GR820_256DU") = (int32_t)4;
    scope().attr("GU_DAARC500_GR820_512DU") = (int32_t)5;
    scope().attr("GU_DAARC500_NAV") = (int32_t)6;
    scope().attr("PEAKEULER_XY_NOFIT") = (int32_t)0;
    scope().attr("PEAKEULER_XY_FIT") = (int32_t)1;

}
