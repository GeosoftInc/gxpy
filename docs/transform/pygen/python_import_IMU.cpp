#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXIMU_wrap_agg_to_geo_color(GXAGGPtr arg1, const gx_string_type& arg2, GXIPJPtr arg3, double arg4)
{
    GXIMU::agg_to_geo_color(arg1, arg2, arg3, arg4);
}
inline int32_t GXIMU_wrap_crc(GXIMGPtr arg1, int32_t arg2)
{
    int32_t ret = GXIMU::crc(arg1, arg2);
    return ret;
}
inline int32_t GXIMU_wrap_crc_grid(const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = GXIMU::crc_grid(arg1, arg2);
    return ret;
}
inline int32_t GXIMU_wrap_crc_grid_inexact(const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    int32_t ret = GXIMU::crc_grid_inexact(arg1, arg2, (IMU_FLOAT_CRC_BITS)arg3, (IMU_DOUBLE_CRC_BITS)arg4);
    return ret;
}
inline int32_t GXIMU_wrap_crc_inexact(GXIMGPtr arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    int32_t ret = GXIMU::crc_inexact(arg1, arg2, (IMU_FLOAT_CRC_BITS)arg3, (IMU_DOUBLE_CRC_BITS)arg4);
    return ret;
}
inline void GXIMU_wrap_export_grid_without_data_section_xml(const gx_string_type& arg1, int_ref& arg2, const gx_string_type& arg3)
{
    GXIMU::export_grid_without_data_section_xml(arg1, arg2, arg3);
}
inline void GXIMU_wrap_export_grid_xml(const gx_string_type& arg1, int_ref& arg2, const gx_string_type& arg3)
{
    GXIMU::export_grid_xml(arg1, arg2, arg3);
}
inline void GXIMU_wrap_export_raw_xml(GXIMGPtr arg1, int_ref& arg2, const gx_string_type& arg3)
{
    GXIMU::export_raw_xml(arg1, arg2, arg3);
}
inline void GXIMU_wrap_export_xml(GXIMGPtr arg1, int_ref& arg2, const gx_string_type& arg3)
{
    GXIMU::export_xml(arg1, arg2, arg3);
}
inline void GXIMU_wrap_get_zvv(GXIMGPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4)
{
    GXIMU::get_zvv(arg1, arg2, arg3, arg4);
}
inline void GXIMU_wrap_get_z_peaks_vv(GXIMGPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4)
{
    GXIMU::get_z_peaks_vv(arg1, arg2, arg3, arg4);
}
inline void GXIMU_wrap_grid_add(GXIMGPtr arg1, double arg2, GXIMGPtr arg3, double arg4, GXIMGPtr arg5)
{
    GXIMU::grid_add(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIMU_wrap_grid_agc(GXIMGPtr arg1, GXIMGPtr arg2, int32_t arg3, double arg4, int32_t arg5)
{
    GXIMU::grid_agc(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIMU_wrap_grid_bool(GXIMGPtr arg1, GXIMGPtr arg2, const gx_string_type& arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    GXIMU::grid_bool(arg1, arg2, arg3, (IMU_BOOL_OPT)arg4, (IMU_BOOL_SIZING)arg5, (IMU_BOOL_OLAP)arg6);
}
inline void GXIMU_wrap_grid_edge(const gx_string_type& arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    GXIMU::grid_edge(arg1, arg2, arg3);
}
inline void GXIMU_wrap_grid_edge_ply(GXIMGPtr arg1, GXPLYPtr arg2, int32_t arg3)
{
    GXIMU::grid_edge_ply(arg1, arg2, arg3);
}
inline void GXIMU_wrap_grid_expand(GXIMGPtr arg1, const gx_string_type& arg2, double arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    GXIMU::grid_expand(arg1, arg2, arg3, (IMU_EXPAND_SHAPE)arg4, arg5, arg6);
}
inline void GXIMU_wrap_grid_exp_fill(const gx_string_type& arg1, const gx_string_type& arg2, double arg3, int32_t arg4)
{
    GXIMU::grid_exp_fill(arg1, arg2, arg3, arg4);
}
inline void GXIMU_wrap_grid_fill(GXIMGPtr arg1, GXIMGPtr arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, double arg7, double arg8, double arg9, int32_t arg10, int32_t arg11)
{
    GXIMU::grid_fill(arg1, arg2, (IMU_FILL_ROLLOPT)arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
}
inline void GXIMU_wrap_grid_filt(GXIMGPtr arg1, GXIMGPtr arg2, int32_t arg3, double arg4, int32_t arg5, int32_t arg6, int32_t arg7, const gx_string_type& arg8, GXVVPtr arg9)
{
    GXIMU::grid_filt(arg1, arg2, arg3, arg4, (IMU_FILT_DUMMY)arg5, (IMU_FILT_HZDRV)arg6, (IMU_FILT_FILE)arg7, arg8, arg9);
}
inline void GXIMU_wrap_grid_head(const gx_string_type& arg1, double arg2, double arg3, double arg4, double arg5, double arg6)
{
    GXIMU::grid_head(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXIMU_wrap_grid_in_fill(GXIMGPtr arg1, const gx_string_type& arg2, int32_t arg3, int32_t arg4)
{
    GXIMU::grid_in_fill(arg1, arg2, arg3, arg4);
}
inline void GXIMU_wrap_grid_mask(const gx_string_type& arg1, const gx_string_type& arg2, GXPLYPtr arg3, int32_t arg4)
{
    GXIMU::grid_mask(arg1, arg2, arg3, (IMU_MASK)arg4);
}
inline void GXIMU_wrap_grid_peak(const gx_string_type& arg1, int32_t arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5)
{
    GXIMU::grid_peak(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIMU_wrap_grid_ply(GXIMGPtr arg1, GXPLYPtr arg2, int32_t arg3)
{
    GXIMU::grid_ply(arg1, arg2, arg3);
}
inline void GXIMU_wrap_grid_ply_ex(GXIMGPtr arg1, GXPLYPtr arg2, int32_t arg3, int32_t arg4)
{
    GXIMU::grid_ply_ex(arg1, arg2, arg3, arg4);
}
inline void GXIMU_wrap_grid_reproject_and_window(const gx_string_type& arg1, const gx_string_type& arg2, GXIPJPtr arg3, double arg4, double arg5, double arg6, double arg7)
{
    GXIMU::grid_reproject_and_window(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXIMU_wrap_grid_resample(const gx_string_type& arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, double arg6, int32_t arg7, int32_t arg8)
{
    GXIMU::grid_resample(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXIMU_wrap_grid_resize(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXIMU::grid_resize(arg1, arg2);
}
inline void GXIMU_wrap_grid_shad(const gx_string_type& arg1, const gx_string_type& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    GXIMU::grid_shad(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIMU_wrap_grid_st(const gx_string_type& arg1, GXSTPtr arg2)
{
    GXIMU::grid_st(arg1, arg2);
}
inline void GXIMU_wrap_grid_stat(const gx_string_type& arg1, int_ref& arg2, int_ref& arg3, int_ref& arg4, float_ref& arg5, float_ref& arg6, int_ref& arg7, float_ref& arg8, float_ref& arg9, float_ref& arg10, float_ref& arg11, float_ref& arg12)
{
    GXIMU::grid_stat(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12);
}
inline void GXIMU_wrap_grid_stat_comp(const gx_string_type& arg1, int_ref& arg2, int_ref& arg3, int_ref& arg4, float_ref& arg5, float_ref& arg6, int_ref& arg7, float_ref& arg8, float_ref& arg9, float_ref& arg10, float_ref& arg11, float_ref& arg12, float_ref& arg13)
{
    GXIMU::grid_stat_comp(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13);
}
inline void GXIMU_wrap_grid_stat_ext(const gx_string_type& arg1, int32_t arg2, int_ref& arg3, int_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8)
{
    GXIMU::grid_stat_ext(arg1, (IMU_STAT_FORCED)arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXIMU_wrap_grid_stat_trend(const gx_string_type& arg1, int_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    GXIMU::grid_stat_trend(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIMU_wrap_grid_stat_trend_ext(const gx_string_type& arg1, int_ref& arg2, int_ref& arg3, float_ref& arg4, float_ref& arg5, GXVMPtr arg6)
{
    GXIMU::grid_stat_trend_ext(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline double GXIMU_wrap_slope_standard_deviation(GXIMGPtr arg1)
{
    double ret = GXIMU::slope_standard_deviation(arg1);
    return ret;
}
inline void GXIMU_wrap_grid_stitch(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7, double arg8, int32_t arg9, int32_t arg10, GXPLYPtr arg11, double arg12, int32_t arg13)
{
    GXIMU::grid_stitch(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13);
}
inline void GXIMU_wrap_grid_stitch_ctl(const gx_string_type& arg1)
{
    GXIMU::grid_stitch_ctl(arg1);
}
inline void GXIMU_wrap_grid_tiff(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4, int32_t arg5, int32_t arg6, double arg7, int32_t arg8, double arg9)
{
    GXIMU::grid_tiff(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXIMU_wrap_grid_trnd(GXIMGPtr arg1, GXIMGPtr arg2, int32_t arg3, int32_t arg4, int32_t arg5, GXVMPtr arg6, int32_t arg7)
{
    GXIMU::grid_trnd(arg1, arg2, arg3, (IMU_TREND)arg4, arg5, arg6, arg7);
}
inline void GXIMU_wrap_grid_trns(const gx_string_type& arg1, int32_t arg2)
{
    GXIMU::grid_trns(arg1, (IMU_TRANS)arg2);
}
inline void GXIMU_wrap_grid_vd(GXIMGPtr arg1, GXIMGPtr arg2)
{
    GXIMU::grid_vd(arg1, arg2);
}
inline void GXIMU_wrap_grid_vol(GXIMGPtr arg1, double arg2, double arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    GXIMU::grid_vol(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXIMU_wrap_grid_wind(GXIMGPtr arg1, const gx_string_type& arg2, int32_t arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10, int32_t arg11, int32_t arg12, const gx_string_type& arg13)
{
    GXIMU::grid_wind(arg1, arg2, (IMU_WIND_COORD)arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, (IMU_WIND_DUMMIES)arg11, arg12, arg13);
}
inline void GXIMU_wrap_grid_wind2(GXIMGPtr arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, int32_t arg9)
{
    GXIMU::grid_wind2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, (IMU_WIND_DUMMIES)arg9);
}
inline void GXIMU_wrap_grid_xyz(GXIMGPtr arg1, const gx_string_type& arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    GXIMU::grid_xyz(arg1, arg2, (IMU_XYZ_INDEX)arg3, arg4, arg5, (IMU_XYZ_LABEL)arg6);
}
inline int32_t GXIMU_wrap_grid_type(const gx_string_type& arg1)
{
    GS_TYPES ret = GXIMU::grid_type(arg1);
    return ret;
}
inline void GXIMU_wrap_make_mi_tab_file(const gx_string_type& arg1)
{
    GXIMU::make_mi_tab_file(arg1);
}
inline void GXIMU_wrap_make_mi_tabfrom_grid(const gx_string_type& arg1)
{
    GXIMU::make_mi_tabfrom_grid(arg1);
}
inline void GXIMU_wrap_make_mi_tabfrom_map(const gx_string_type& arg1)
{
    GXIMU::make_mi_tabfrom_map(arg1);
}
inline GXIMGPtr GXIMU_wrap_mosaic(const gx_string_type& arg1, const gx_string_type& arg2, GXIPJPtr arg3, double arg4)
{
    GXIMGPtr ret = GXIMU::mosaic(arg1, arg2, arg3, arg4);
    return ret;
}
inline void GXIMU_wrap_peak_size(const gx_string_type& arg1, GXVVPtr arg2, GXVVPtr arg3, int32_t arg4, double arg5, GXVVPtr arg6)
{
    GXIMU::peak_size(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXIMU_wrap_peak_size2(const gx_string_type& arg1, GXVVPtr arg2, GXVVPtr arg3, int32_t arg4, GXVVPtr arg5)
{
    GXIMU::peak_size2(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIMU_wrap_pigeon_hole(GXIMGPtr arg1, GXVVPtr arg2, GXVVPtr arg3, int_ref& arg4)
{
    GXIMU::pigeon_hole(arg1, arg2, arg3, arg4);
}
inline void GXIMU_wrap_profile(GXIMGPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6, GXVVPtr arg7)
{
    GXIMU::profile(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXIMU_wrap_profile_vv(GXIMGPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4)
{
    GXIMU::profile_vv(arg1, arg2, arg3, arg4);
}
inline void GXIMU_wrap_range_grids(const gx_string_type& arg1, GXIPJPtr arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    GXIMU::range_grids(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXIMU_wrap_range_ll(GXIMGPtr arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    GXIMU::range_ll(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIMU_wrap_stat_window(GXIMGPtr arg1, double arg2, double arg3, double arg4, double arg5, int32_t arg6, GXSTPtr arg7)
{
    GXIMU::stat_window(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXIMU_wrap_update_ply(GXIMGPtr arg1, GXPLYPtr arg2)
{
    GXIMU::update_ply(arg1, arg2);
}

void gxPythonImportGXIMU()
{

    class_<GXIMU, boost::noncopyable> pyClass("GXIMU",
            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		Not a class. This is a catch-all group of functions working\n"
            "   		on IMG objects (see IMG). Grid operations include masking,\n"
            "   		trending, windowing, expanding and grid stitching.\n"
            "   	\n\n"
            , no_init);


    pyClass.def("agg_to_geo_color", &GXIMU_wrap_agg_to_geo_color,
                "agg_to_geo_color((GXAGG)arg1, (str)arg2, (GXIPJ)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a geosoft color grid from an aggregate.\n\n"

                ":param arg1: Input Aggregate\n"
                ":type arg1: :class:`geosoft.gxapi.GXAGG`\n"
                ":param arg2: Output image name\n"
                ":type arg2: str\n"
                ":param arg3: Projection to use\n"
                ":type arg3: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg4: Resolution (Cell Size) size to use\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This consumes a very small amount of memory\n\n"
               ).staticmethod("agg_to_geo_color");
    pyClass.def("crc", &GXIMU_wrap_crc,
                "crc((GXIMG)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Computes a CRC Checksum on an image.\n\n"

                ":param arg1: input image\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: starting CRC (use \\ :ref:`CRC_INIT_VALUE`\\  if none)\n"
                ":type arg2: int\n"
                ":returns: CRC value\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("crc");
    pyClass.def("crc_grid", &GXIMU_wrap_crc_grid,
                "crc_grid((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Computes a CRC Checksum on a grid.\n\n"

                ":param arg1: grid\n"
                ":type arg1: str\n"
                ":param arg2: starting CRC (use \\ :ref:`CRC_INIT_VALUE`\\  if none)\n"
                ":type arg2: int\n"
                ":returns: CRC value\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("crc_grid");
    pyClass.def("crc_grid_inexact", &GXIMU_wrap_crc_grid_inexact,
                "crc_grid_inexact((str)arg1, (int)arg2, (int)arg3, (int)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Computes a CRC Checksum on a grid and allows you to specify\n"
                "   					number of bits of floats/doubles to drop so that the CRC\n"
                "   					will be same even of this are changed.\n"
                "   				\n\n"

                ":param arg1: grid\n"
                ":type arg1: str\n"
                ":param arg2: starting CRC (use \\ :ref:`CRC_INIT_VALUE`\\  if none)\n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`IMU_FLOAT_CRC_BITS`\\ \n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`IMU_DOUBLE_CRC_BITS`\\ \n"
                ":type arg4: int\n"
                ":returns: CRC value\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Very usefull for testing where the last bits of accuracy\n"
                "   					are not as important.\n"
                "   				\n\n"
               ).staticmethod("crc_grid_inexact");
    pyClass.def("crc_inexact", &GXIMU_wrap_crc_inexact,
                "crc_inexact((GXIMG)arg1, (int)arg2, (int)arg3, (int)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Computes a CRC Checksum on an image and allows you to specify\n"
                "   					number of bits of floats/doubles to drop so that the CRC\n"
                "   					will be same even of this are changed.\n"
                "   				\n\n"

                ":param arg1: input image\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: starting CRC (use \\ :ref:`CRC_INIT_VALUE`\\  if none)\n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`IMU_FLOAT_CRC_BITS`\\ \n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`IMU_DOUBLE_CRC_BITS`\\ \n"
                ":type arg4: int\n"
                ":returns: CRC value\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Very usefull for testing where the last bits of accuracy\n"
                "   					are not as important.\n"
                "   				\n\n"
               ).staticmethod("crc_inexact");
    pyClass.def("export_grid_without_data_section_xml", &GXIMU_wrap_export_grid_without_data_section_xml,
                "export_grid_without_data_section_xml((str)arg1, (int_ref)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a Grid minus the data section as an XML file.\n\n"

                ":param arg1: Grid\n"
                ":type arg1: str\n"
                ":param arg2: CRC returned\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Output XML file\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               ).staticmethod("export_grid_without_data_section_xml");
    pyClass.def("export_grid_xml", &GXIMU_wrap_export_grid_xml,
                "export_grid_xml((str)arg1, (int_ref)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a Grid as an XML file.\n\n"

                ":param arg1: Grid\n"
                ":type arg1: str\n"
                ":param arg2: CRC returned\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Output XML file\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               ).staticmethod("export_grid_xml");
    pyClass.def("export_raw_xml", &GXIMU_wrap_export_raw_xml,
                "export_raw_xml((GXIMG)arg1, (int_ref)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a Grid as an XML file using a fast raw output.\n\n"

                ":param arg1: Image\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: CRC returned\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Output XML file\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("export_raw_xml");
    pyClass.def("export_xml", &GXIMU_wrap_export_xml,
                "export_xml((GXIMG)arg1, (int_ref)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a Grid as an XML file.\n\n"

                ":param arg1: Image\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: CRC returned\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Output XML file\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               ).staticmethod("export_xml");
    pyClass.def("get_zvv", &GXIMU_wrap_get_zvv,
                "get_zvv((GXIMG)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Extract an interpolated image value for given XY VV locations\n\n"

                ":param arg1: input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: X VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Z VV filled with values (set to be same size as X, Y)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"
               ).staticmethod("get_zvv");
    pyClass.def("get_z_peaks_vv", &GXIMU_wrap_get_z_peaks_vv,
                "get_z_peaks_vv((GXIMG)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXIMU.get_zvv`\\ , but find the closest peak value to the input locations, and return\n"
                "   				             the peak value and peak value location.\n\n"

                ":param arg1: input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: X VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Z VV filled with values (set to be same size as X, Y)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The returned locations will always be a grid point location; no interpolation is performed when locating the peaks. A simple search is\n"
                "   				done of all neighbouring points from the starting point, and once no neighbours can be located with a higher value, the search stops.\n\n"
               ).staticmethod("get_z_peaks_vv");
    pyClass.def("grid_add", &GXIMU_wrap_grid_add,
                "grid_add((GXIMG)arg1, (float)arg2, (GXIMG)arg3, (float)arg4, (GXIMG)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Adds two Grid images together point-by-point.\n\n"

                ":param arg1: Image of first grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Multiplier to operate on first grid image\n"
                ":type arg2: float\n"
                ":param arg3: Image of second grid\n"
                ":type arg3: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg4: Multiplier to operate on second grid image\n"
                ":type arg4: float\n"
                ":param arg5: Output grid image\n"
                ":type arg5: :class:`geosoft.gxapi.GXIMG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The IMG parameters MUST be of type GS_DOUBLE!\n"
                "   					If not, the method will terminate.\n"
                "   				\n\n"
               ).staticmethod("grid_add");
    pyClass.def("grid_agc", &GXIMU_wrap_grid_agc,
                "grid_agc((GXIMG)arg1, (GXIMG)arg2, (int)arg3, (float)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Automatic Gain Compensation of a grid.\n\n"

                ":param arg1: Image of input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Image of output grid\n"
                ":type arg2: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg3: Width of filter to separate signal from background.\n"
                ":type arg3: int\n"
                ":param arg4: Maximum gain applied to the signal.\n"
                ":type arg4: float\n"
                ":param arg5: Remove background before applying gain?\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The IMG parameters MUST be of type GS_FLOAT!\n"
                "   					If not, the method will terminate.\n"
                "   				\n\n"
               ).staticmethod("grid_agc");
    pyClass.def("grid_bool", &GXIMU_wrap_grid_bool,
                "grid_bool((GXIMG)arg1, (GXIMG)arg2, (str)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Mask one grid against another using boolean logic\n"
                "   					operations.\n"
                "   				\n\n"

                ":param arg1: Image of first input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Image of second input grid\n"
                ":type arg2: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg3: File name of output grid\n"
                ":type arg3: str\n"
                ":param arg4: \\ :ref:`IMU_BOOL_OPT`\\ \n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`IMU_BOOL_SIZING`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`IMU_BOOL_OLAP`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The IMG parameters must be of type GS_DOUBLE!\n"
                "   					If not, the method will terminate.\n"
                "   				\n\n"
               ).staticmethod("grid_bool");
    pyClass.def("grid_edge", &GXIMU_wrap_grid_edge,
                "grid_edge((str)arg1, (GXVV)arg2, (GXVV)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get grid edge points\n\n"

                ":param arg1: Grid file name\n"
                ":type arg1: str\n"
                ":param arg2: X coordinates of edge points\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y coordinates of edge points\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("grid_edge");
    pyClass.def("grid_edge_ply", &GXIMU_wrap_grid_edge_ply,
                "grid_edge_ply((GXIMG)arg1, (GXPLY)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get grid edge points\n\n"

                ":param arg1: The Grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: PLY containing the edges.\n"
                ":type arg2: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg3: Minimum number of points in polygons (0 for all)\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Unlike \\ :func:`geosoft.gxapi.GXIMU.grid_ply`\\  and GridPlyEx_IMU, the image is not\n"
                "   					altered. It just gives the PLY.\n"
                "   				\n\n"
               ).staticmethod("grid_edge_ply");
    pyClass.def("grid_expand", &GXIMU_wrap_grid_expand,
                "grid_expand((GXIMG)arg1, (str)arg2, (float)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Expand a grid and place dummies in the area\n"
                "   					beyond the original edges.\n"
                "   				\n\n"

                ":param arg1: Image of input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: File name of output grid\n"
                ":type arg2: str\n"
                ":param arg3: Minimum percentage to expand the grid by\n"
                ":type arg3: float\n"
                ":param arg4: \\ :ref:`IMU_EXPAND_SHAPE`\\ \n"
                ":type arg4: int\n"
                ":param arg5: X Dimension the output grid is expanded to\n"
                ":type arg5: int\n"
                ":param arg6: Y Dimension the output grid is expanded to\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The IMG parameter MUST be of type GS_FLOAT!\n"
                "   					If not, the method will terminate.\n"
                "   				\n\n"
               ).staticmethod("grid_expand");
    pyClass.def("grid_exp_fill", &GXIMU_wrap_grid_exp_fill,
                "grid_exp_fill((str)arg1, (str)arg2, (float)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Extends and fills a grid for FFT2.\n\n"

                ":param arg1: Name of the input grid\n"
                ":type arg1: str\n"
                ":param arg2: Name of the output grid\n"
                ":type arg2: str\n"
                ":param arg3: % expansion\n"
                ":type arg3: float\n"
                ":param arg4: Shape of expansion: 0 - rectangle, 1 - square\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               ).staticmethod("grid_exp_fill");
    pyClass.def("grid_fill", &GXIMU_wrap_grid_fill,
                "grid_fill((GXIMG)arg1, (GXIMG)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (float)arg7, (float)arg8, (float)arg9, (int)arg10, (int)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Interpolates to fill dummies, generates an output grid.\n\n"

                ":param arg1: Image of input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Image of output grid\n"
                ":type arg2: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg3: \\ :ref:`IMU_FILL_ROLLOPT`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Distance at which to roll off to 0\n"
                ":type arg4: int\n"
                ":param arg5: Maximum prediction filter length\n"
                ":type arg5: int\n"
                ":param arg6: Maximum prediction filter area\n"
                ":type arg6: int\n"
                ":param arg7: Base value to roll off to\n"
                ":type arg7: float\n"
                ":param arg8: Maximum amplitude allowed in grid\n"
                ":type arg8: float\n"
                ":param arg9: Maximum edge amplitude allowed in grid\n"
                ":type arg9: float\n"
                ":param arg10: Width from edge to start limiting from\n"
                ":type arg10: int\n"
                ":param arg11: Number of convolution passes to apply\n"
                ":type arg11: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The IMG parameters MUST be of type GS_FLOAT!\n"
                "   					If not, the method will terminate.\n"
                "   				\n\n"
               ).staticmethod("grid_fill");
    pyClass.def("grid_filt", &GXIMU_wrap_grid_filt,
                "grid_filt((GXIMG)arg1, (GXIMG)arg2, (int)arg3, (float)arg4, (int)arg5, (int)arg6, (int)arg7, (str)arg8, (GXVV)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Applies a filter to a grid any number\n"
                "   					of passes.\n"
                "   				\n\n"

                ":param arg1: Image of first grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Image of second grid\n"
                ":type arg2: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg3: Number of passes to apply filter (>0)\n"
                ":type arg3: int\n"
                ":param arg4: Multiplier to apply to grid values\n"
                ":type arg4: float\n"
                ":param arg5: \\ :ref:`IMU_FILT_DUMMY`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`IMU_FILT_HZDRV`\\ \n"
                ":type arg6: int\n"
                ":param arg7: \\ :ref:`IMU_FILT_FILE`\\ \n"
                ":type arg7: int\n"
                ":param arg8: Name of file containing filter values\n"
                ":type arg8: str\n"
                ":param arg9: VV containing filter values (if not using a file for the values) MUST BE OF TYPE 'real'\n"
                ":type arg9: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The IMG parameters MUST be of type GS_FLOAT!\n"
                "   					If not, the method will terminate.\n"
                "   				\n\n"
               ).staticmethod("grid_filt");
    pyClass.def("grid_head", &GXIMU_wrap_grid_head,
                "grid_head((str)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Modifies Statistics contained in a grid header.\n\n"

                ":param arg1: Name of the grid whose header is to be modified.\n"
                ":type arg1: str\n"
                ":param arg2: Element separation\n"
                ":type arg2: float\n"
                ":param arg3: Vector separation\n"
                ":type arg3: float\n"
                ":param arg4: Grid X Origin on ground\n"
                ":type arg4: float\n"
                ":param arg5: Grid Y Origin on ground\n"
                ":type arg5: float\n"
                ":param arg6: Grid Rotation\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("grid_head");
    pyClass.def("grid_in_fill", &GXIMU_wrap_grid_in_fill,
                "grid_in_fill((GXIMG)arg1, (str)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill in a ribbon along the edge and inside hollow areas of the grid\n\n"

                ":param arg1: Image of input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Name of the output grid\n"
                ":type arg2: str\n"
                ":param arg3: Number of cells to extend ribbon along the edge\n"
                ":type arg3: int\n"
                ":param arg4: Number of iterations to fill inside hollow areas\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               ).staticmethod("grid_in_fill");
    pyClass.def("grid_mask", &GXIMU_wrap_grid_mask,
                "grid_mask((str)arg1, (str)arg2, (GXPLY)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Create a mask grid using a set of polygon\n"
                "   					coordinates defined in a separate file, then\n"
                "   					masking the polygon over an input grid.\n"
                "   				\n\n"

                ":param arg1: Name of input grid\n"
                ":type arg1: str\n"
                ":param arg2: Name of output mask grid file\n"
                ":type arg2: str\n"
                ":param arg3: Polygon containing mask coordinates\n"
                ":type arg3: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg4: \\ :ref:`IMU_MASK`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The IMG parameters MUST be of type GS_DOUBLE!\n"
                "   					If not, the method will terminate.\n"
                "   \n"
                "   					The PLY will contain more than one polygon\n"
                "   					if it was loaded from a file containing\n"
                "   					coordinates of more than one polygon.\n"
                "   				\n\n"
               ).staticmethod("grid_mask");
    pyClass.def("grid_peak", &GXIMU_wrap_grid_peak,
                "grid_peak((str)arg1, (int)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Pick grid peaks.\n\n"

                ":param arg1: Grid file name\n"
                ":type arg1: str\n"
                ":param arg2: peak test directions (1 to 4)\n"
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
                "   \n"
                "   					Peak test directions defines how grid peaks are to be found.\n"
                "   					For example, with the 1, a grid point will be picked if its\n"
                "   					value is greater than it's two neighbors in at least one\n"
                "   					direction.  Up to 4 directions can be tested.\n"
                "   				\n\n"
               ).staticmethod("grid_peak");
    pyClass.def("grid_ply", &GXIMU_wrap_grid_ply,
                "grid_ply((GXIMG)arg1, (GXPLY)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the grid edge in a PLY\n\n"

                ":param arg1: the IMG\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: PLY to which the bounding polygons will be added.\n"
                ":type arg2: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg3: TRUE to force the boundary to be refreshed.\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This will optionally refresh the grid boundary PLY and return\n"
                "   					the PLY.\n"
                "   \n"
                "   					If the boundary is not refreshed and has never been calculated,\n"
                "   					the boundary will be the bounding rectangle of the grid.\n"
                "   \n"
                "   					The grid PLY will be added to existing ploygons in the passed PLY.\n"
                "   				\n\n"
               ).staticmethod("grid_ply");
    pyClass.def("grid_ply_ex", &GXIMU_wrap_grid_ply_ex,
                "grid_ply_ex((GXIMG)arg1, (GXPLY)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the grid edge in a PLY (with min points)\n\n"

                ":param arg1: the IMG\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: PLY to which the bounding polygons will be added.\n"
                ":type arg2: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg3: TRUE to force the boundary to be refreshed.\n"
                ":type arg3: int\n"
                ":param arg4: Minimum number of points in polygons refreshed (0 for all)\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This will optionally refresh the grid boundary PLY and return\n"
                "   					the PLY.\n"
                "   \n"
                "   					If the boundary is not refreshed and has never been calculated,\n"
                "   					the boundary will be the bounding rectangle of the grid.\n"
                "   \n"
                "   					The grid PLY will be added to existing ploygons in the passed PLY.\n"
                "   				\n\n"
               ).staticmethod("grid_ply_ex");
    pyClass.def("grid_reproject_and_window", &GXIMU_wrap_grid_reproject_and_window,
                "grid_reproject_and_window((str)arg1, (str)arg2, (GXIPJ)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new grid by reprojecting an existing grid and windowing its contents\n\n"

                ":param arg1: Input grid filename\n"
                ":type arg1: str\n"
                ":param arg2: Output grid filename\n"
                ":type arg2: str\n"
                ":param arg3: Output grid projection\n"
                ":type arg3: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg4: Window minX (in output projection)\n"
                ":type arg4: float\n"
                ":param arg5: Window maxX (in output projection)\n"
                ":type arg5: float\n"
                ":param arg6: Window minY (in output projection)\n"
                ":type arg6: float\n"
                ":param arg7: Window maxY (in output projection)\n"
                ":type arg7: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"
               ).staticmethod("grid_reproject_and_window");
    pyClass.def("grid_resample", &GXIMU_wrap_grid_resample,
                "grid_resample((str)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (int)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "    Create a new grid by resampling an existing grid \n\n"

                ":param arg1: Input grid filename\n"
                ":type arg1: str\n"
                ":param arg2: Output grid filename\n"
                ":type arg2: str\n"
                ":param arg3: Origin X\n"
                ":type arg3: float\n"
                ":param arg4: Origin Y\n"
                ":type arg4: float\n"
                ":param arg5: cell spacing X\n"
                ":type arg5: float\n"
                ":param arg6: cell spacing Y\n"
                ":type arg6: float\n"
                ":param arg7: elements in X\n"
                ":type arg7: int\n"
                ":param arg8: elements in Y\n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Works only for un rotated grids.\n"
                "   				\n\n"
               ).staticmethod("grid_resample");
    pyClass.def("grid_resize", &GXIMU_wrap_grid_resize,
                "grid_resize((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Resize a grid to reduce the size not cover the outside dummies.\n\n"

                ":param arg1: File name of input grid\n"
                ":type arg1: str\n"
                ":param arg2: File name of output grid\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("grid_resize");
    pyClass.def("grid_shad", &GXIMU_wrap_grid_shad,
                "grid_shad((str)arg1, (str)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a shadded relief image.\n\n"

                ":param arg1: input image name\n"
                ":type arg1: str\n"
                ":param arg2: output new shaded image\n"
                ":type arg2: str\n"
                ":param arg3: inclination 0-90 degrees (def. 45)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: declination 0-360 degrees azimuth (def. 45)\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: vertical scale factor (distance/z unit)\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Pass GS_R8DM as parameters to obtain default values.\n"
                "   					The default values are returned.\n"
                "   				\n\n"
               ).staticmethod("grid_shad");
    pyClass.def("grid_st", &GXIMU_wrap_grid_st,
                "grid_st((str)arg1, (GXST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Update an ST object using a grid.\n\n"

                ":param arg1: grid name\n"
                ":type arg1: str\n"
                ":param arg2: ST (statistics) object to fill/update\n"
                ":type arg2: :class:`geosoft.gxapi.GXST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The input ST object is not initialized by \\ :func:`geosoft.gxapi.GXIMU.grid_st`\\ ,\n"
                "   					so this function can be used to accumulate statistical\n"
                "   					info on more than a single grid.\n"
                "   					See ST.GXH.\n"
                "   				\n\n"
               ).staticmethod("grid_st");
    pyClass.def("grid_stat", &GXIMU_wrap_grid_stat,
                "grid_stat((str)arg1, (int_ref)arg2, (int_ref)arg3, (int_ref)arg4, (float_ref)arg5, (float_ref)arg6, (int_ref)arg7, (float_ref)arg8, (float_ref)arg9, (float_ref)arg10, (float_ref)arg11, (float_ref)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reports statistics contained in a grid header.\n\n"

                ":param arg1: Name of the grid to get stats from\n"
                ":type arg1: str\n"
                ":param arg2: Element type in bytes\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Elements in X direction\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Elements in Y direction\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: X element separation\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Y element separation\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: KX (storage orientation)\n"
                ":type arg7: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg8: X origin\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Y origin\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: Grid Rotation\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: Base removed\n"
                ":type arg11: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg12: Grid multiplier\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Statistics are returned in the parameter set\n\n"
               ).staticmethod("grid_stat");
    pyClass.def("grid_stat_comp", &GXIMU_wrap_grid_stat_comp,
                "grid_stat_comp((str)arg1, (int_ref)arg2, (int_ref)arg3, (int_ref)arg4, (float_ref)arg5, (float_ref)arg6, (int_ref)arg7, (float_ref)arg8, (float_ref)arg9, (float_ref)arg10, (float_ref)arg11, (float_ref)arg12, (float_ref)arg13) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reports statistics contained in a grid header.\n\n"

                ":param arg1: Name of the grid to get stats from\n"
                ":type arg1: str\n"
                ":param arg2: Element type: 0 - byte 1 - USHORT 2 - SHORT 3 - LONG 4 - FLOAT 5 - DOUBLE 6 - 32 byte Colour (RGBx)\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Elements in X direction\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Elements in Y direction\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: X element separation\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Y element separation\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: KX (storage orientation)\n"
                ":type arg7: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg8: X origin\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Y origin\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: Grid Rotation\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: Base removed\n"
                ":type arg11: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg12: Grid multiplier\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg13: Compression Ratio\n"
                ":type arg13: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Statistics are returned in the parameter set\n\n"
               ).staticmethod("grid_stat_comp");
    pyClass.def("grid_stat_ext", &GXIMU_wrap_grid_stat_ext,
                "grid_stat_ext((str)arg1, (int)arg2, (int_ref)arg3, (int_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reports statistics of a grid's elements.\n\n"

                ":param arg1: Name of the grid to get stats from\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`IMU_STAT_FORCED`\\ \n"
                ":type arg2: int\n"
                ":param arg3: Number of valid elements in grid\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Number of dummies in grid\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: Minimum grid value\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Maximum grid value\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Grid mean\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Grid standard deviation\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the \\ :ref:`IMU_STAT_FORCED`\\  value is set, the\n"
                "   					statistics will be recalculated.\n"
                "   					Statistics are returned in the parameter set.\n"
                "   				\n\n"
               ).staticmethod("grid_stat_ext");
    pyClass.def("grid_stat_trend", &GXIMU_wrap_grid_stat_trend,
                "grid_stat_trend((str)arg1, (int_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reports Trend Info of a grid (for first order coef only).\n\n"

                ":param arg1: Name of the grid to get stats from\n"
                ":type arg1: str\n"
                ":param arg2: Trend Valid Flag\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Trend Coeff rCo\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Trend Coeff rCx\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Trend Coeff rCy\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Trend Info are returned in the parameter set\n\n"
               ).staticmethod("grid_stat_trend");
    pyClass.def("grid_stat_trend_ext", &GXIMU_wrap_grid_stat_trend_ext,
                "grid_stat_trend_ext((str)arg1, (int_ref)arg2, (int_ref)arg3, (float_ref)arg4, (float_ref)arg5, (GXVM)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reports Extended Trend Info of a grid (for upto third order coef).\n\n"

                ":param arg1: grid name\n"
                ":type arg1: str\n"
                ":param arg2: trend order\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Number of coefficients\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: trend origin Xo\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: trend origin Yo\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: VM hold coefficient values MUST BE OF TYPE 'real'\n"
                ":type arg6: :class:`geosoft.gxapi.GXVM`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Trend Info are returned in the parameter set\n\n"
               ).staticmethod("grid_stat_trend_ext");
    pyClass.def("slope_standard_deviation", &GXIMU_wrap_slope_standard_deviation,
                "slope_standard_deviation((GXIMG)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Return the standard deviation of the slopes.\n"
                "   				\n\n"

                ":param arg1: Grid object\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":returns: Standard devation of grid slopes\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method calculates the standard dev. of the horizontal\n"
                "   					differences in the X and Y directions for the supplied\n"
                "   					image.  This is useful for shading routines.  A good\n"
                "   					default scaling factor is 2.5 / standard deviation.\n"
                "   \n"
                "   					The image will be sub-sampled to a statistically meaningful number.\n"
                "   \n"
                "   					The cell sizes are used to determine the slopes.\n"
                "   				\n\n"
               ).staticmethod("slope_standard_deviation");
    pyClass.def("grid_stitch", &GXIMU_wrap_grid_stitch,
                "grid_stitch((str)arg1, (str)arg2, (str)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7, (float)arg8, (int)arg9, (int)arg10, (GXPLY)arg11, (float)arg12, (int)arg13) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Stitches together too grids\n\n"

                ":param arg1: Input Grid1 Name\n"
                ":type arg1: str\n"
                ":param arg2: Input Grid2 Name\n"
                ":type arg2: str\n"
                ":param arg3: Output Grid Name\n"
                ":type arg3: str\n"
                ":param arg4: Stitching Method\n"
                ":type arg4: int\n"
                ":param arg5: Grid 1 trend removal order\n"
                ":type arg5: int\n"
                ":param arg6: Grid 2 trend removal order\n"
                ":type arg6: int\n"
                ":param arg7: Trend removal type of points to use\n"
                ":type arg7: int\n"
                ":param arg8: Gap for interpolation\n"
                ":type arg8: float\n"
                ":param arg9: Interpolation spline method\n"
                ":type arg9: int\n"
                ":param arg10: Path selection\n"
                ":type arg10: int\n"
                ":param arg11: PLY object for user path\n"
                ":type arg11: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg12: Correction weighting\n"
                ":type arg12: float\n"
                ":param arg13: width of corrections, in grid cells (8 to 256)\n"
                ":type arg13: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("grid_stitch");
    pyClass.def("grid_stitch_ctl", &GXIMU_wrap_grid_stitch_ctl,
                "grid_stitch_ctl((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Stitches together two grids - control file for options.\n\n"

                ":param arg1: Control file containing all \"GRIDSTCH\" parameters\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Data validation is done internally, not in the GX.\n"
                "   					This is simply a way of avoiding writing a new GX wrapper\n"
                "   					every time an option is added.\n"
                "   				\n\n"
               ).staticmethod("grid_stitch_ctl");
    pyClass.def("grid_tiff", &GXIMU_wrap_grid_tiff,
                "grid_tiff((str)arg1, (str)arg2, (str)arg3, (int)arg4, (int)arg5, (int)arg6, (float)arg7, (int)arg8, (float)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a Tiff (Tagged-Image file format) file with up to 16 grids.\n\n"

                ":param arg1: Comma-delimited string containing names of all grids to use in Tiff generation Up to 16 grids allowed.\n"
                ":type arg1: str\n"
                ":param arg2: Name of Tiff file to create\n"
                ":type arg2: str\n"
                ":param arg3: Background colour option. One of W (White)  K (Black) C (Cyan) M (Magenta) Y (Yellow) R (Red)  G (Green) B (Blue)\n"
                ":type arg3: str\n"
                ":param arg4: Background Red value (0-255)\n"
                ":type arg4: int\n"
                ":param arg5: Background Green (0-255)\n"
                ":type arg5: int\n"
                ":param arg6: Background Blue  (0-255)\n"
                ":type arg6: int\n"
                ":param arg7: New cell size\n"
                ":type arg7: float\n"
                ":param arg8: Pixel size of registration marks\n"
                ":type arg8: int\n"
                ":param arg9: Map Scale\n"
                ":type arg9: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The background colour can be either selected\n"
                "   					from one of 8 settings, or can be specified\n"
                "   					as a combination of Reg,Green, and Blue values.\n"
                "   				\n\n"
               ).staticmethod("grid_tiff");
    pyClass.def("grid_trnd", &GXIMU_wrap_grid_trnd,
                "grid_trnd((GXIMG)arg1, (GXIMG)arg2, (int)arg3, (int)arg4, (int)arg5, (GXVM)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove a trend surface from a grid.\n\n"

                ":param arg1: Handle to input image\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Handle to output image\n"
                ":type arg2: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg3: 0-calculate, 1-given, 2-replace\n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`IMU_TREND`\\ \n"
                ":type arg4: int\n"
                ":param arg5: Trend order\n"
                ":type arg5: int\n"
                ":param arg6: VM holds coefficients\n"
                ":type arg6: :class:`geosoft.gxapi.GXVM`\n"
                ":param arg7: Number of coefficients\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Both Images must be of type GS_DOUBLE.\n"
                "   					The VM parameter must be of type REAL,\n"
                "   					and be of size 10 at most.\n"
                "   \n"
                "   					The number of coefficients must be\n"
                "   					compatible with the order of the\n"
                "   					trend removed. Following is the\n"
                "   					number of coefficients which should\n"
                "   					be present for a given order\n"
                "   \n"
                "   					Order            Number of Coefficients\n"
                "   					-----            ----------------------\n"
                "   					0                 1\n"
                "   					1                 3\n"
                "   					2                 6\n"
                "   					3                 10\n"
                "   				\n\n"
               ).staticmethod("grid_trnd");
    pyClass.def("grid_trns", &GXIMU_wrap_grid_trns,
                "grid_trns((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Transpose a grid by swapping the grid rows with\n"
                "   					the grid columns.\n"
                "   				\n\n"

                ":param arg1: Name of the grid to transpose\n"
                ":type arg1: str\n"
                ":param arg2: Transpose condition value \\ :ref:`IMU_TRANS`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the grid has a line orientation that does NOT\n"
                "   					match the \\ :ref:`IMU_TRANS`\\  value, this method will\n"
                "   					not succeed.\n"
                "   				\n\n"
               ).staticmethod("grid_trns");
    pyClass.def("grid_vd", &GXIMU_wrap_grid_vd,
                "grid_vd((GXIMG)arg1, (GXIMG)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply vertical derivertive convolution filter to a grid.\n\n"

                ":param arg1: input image\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: output image\n"
                ":type arg2: :class:`geosoft.gxapi.GXIMG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("grid_vd");
    pyClass.def("grid_vol", &GXIMU_wrap_grid_vol,
                "grid_vol((GXIMG)arg1, (float)arg2, (float)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Calculates the grid volumes above and below a\n"
                "   					reference base.\n"
                "   				\n\n"

                ":param arg1: Image of the grid to calculate volume for\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Reference base\n"
                ":type arg2: float\n"
                ":param arg3: Multiplier to final volume\n"
                ":type arg3: float\n"
                ":param arg4: Grid Volume above reference base\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Grid Volume below reference base\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Differences between volumes\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Volumes are calculated above and below a\n"
                "   					reference base level, and reported as positive\n"
                "   					integers. A multiplier is applied to the final\n"
                "   					volume (to correct for units).\n"
                "   \n"
                "   					The IMG parameters MUST be of type GS_FLOAT!\n"
                "   					If not, the method will terminate.\n"
                "   				\n\n"
               ).staticmethod("grid_vol");
    pyClass.def("grid_wind", &GXIMU_wrap_grid_wind,
                "grid_wind((GXIMG)arg1, (str)arg2, (int)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (int)arg11, (int)arg12, (str)arg13) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Create a grid using a defined area window\n"
                "   					within a larger grid.\n"
                "   				\n\n"

                ":param arg1: Image of input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Name of output grid file\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`IMU_WIND_COORD`\\ \n"
                ":type arg3: int\n"
                ":param arg4: Min. limit of window in X direction (can be rDUMMY)\n"
                ":type arg4: float\n"
                ":param arg5: Max. limit of window in X direction (can be rDUMMY)\n"
                ":type arg5: float\n"
                ":param arg6: Min. limit of window in Y direction (can be rDUMMY)\n"
                ":type arg6: float\n"
                ":param arg7: Max. limit of window in Y direction (can be rDUMMY)\n"
                ":type arg7: float\n"
                ":param arg8: Minimum Z data value in output grid (can be rDUMMY)\n"
                ":type arg8: float\n"
                ":param arg9: Maximum Z data value in output grid (can be rDUMMY)\n"
                ":type arg9: float\n"
                ":param arg10: New grid cell size\n"
                ":type arg10: float\n"
                ":param arg11: \\ :ref:`IMU_WIND_DUMMIES`\\ \n"
                ":type arg11: int\n"
                ":param arg12: Decimation factor\n"
                ":type arg12: int\n"
                ":param arg13: Name of .MDF file for data clipping\n"
                ":type arg13: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("grid_wind");
    pyClass.def("grid_wind2", &GXIMU_wrap_grid_wind2,
                "grid_wind2((GXIMG)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (int)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Window a grid.\n\n"

                ":param arg1: Image of input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Name of output grid file\n"
                ":type arg2: str\n"
                ":param arg3: Minimum X, ground units (can be rDUMMY)\n"
                ":type arg3: float\n"
                ":param arg4: Maximum X (can be rDUMMY)\n"
                ":type arg4: float\n"
                ":param arg5: Minimum Y (can be rDUMMY)\n"
                ":type arg5: float\n"
                ":param arg6: Maximum Y (can be rDUMMY)\n"
                ":type arg6: float\n"
                ":param arg7: Minimum Z (can be rDUMMY)\n"
                ":type arg7: float\n"
                ":param arg8: Maximum Z (can be rDUMMY)\n"
                ":type arg8: float\n"
                ":param arg9: \\ :ref:`IMU_WIND_DUMMIES`\\ \n"
                ":type arg9: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					To change the cell size or work in a different projection,\n"
                "   					first inherit the IMG by calling\n"
                "   \n"
                "   					The windowed grid will be adjusted/expanded to include the\n"
                "   					defined area and line up on an even grid cell.\n"
                "   				\n\n"
               ).staticmethod("grid_wind2");
    pyClass.def("grid_xyz", &GXIMU_wrap_grid_xyz,
                "grid_xyz((GXIMG)arg1, (str)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export a Grid image to an XYZ file.\n\n"

                ":param arg1: Image of the grid to export\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Name of new XYZ file\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`IMU_XYZ_INDEX`\\ \n"
                ":type arg3: int\n"
                ":param arg4: X direction decimation factor\n"
                ":type arg4: int\n"
                ":param arg5: Y direction decimation factor\n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`IMU_XYZ_LABEL`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The IMG (image) of the grid to export must\n"
                "   					be of type GS_FLOAT. If not, this method will\n"
                "   					terminate with an error.\n"
                "   				\n\n"
               ).staticmethod("grid_xyz");
    pyClass.def("grid_type", &GXIMU_wrap_grid_type,
                "grid_type((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Reports the true data the of a grid (geosoft types)\n\n"

                ":param arg1: Name of the Grid\n"
                ":type arg1: str\n"
                ":returns: \\ :ref:`GS_TYPES`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("grid_type");
    pyClass.def("make_mi_tab_file", &GXIMU_wrap_make_mi_tab_file,
                "make_mi_tab_file((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Make a MapInfo tab file for this grid\n\n"

                ":param arg1: Grid file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               ).staticmethod("make_mi_tab_file");
    pyClass.def("make_mi_tabfrom_grid", &GXIMU_wrap_make_mi_tabfrom_grid,
                "make_mi_tabfrom_grid((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Make a MapInfo tab file for this grid as rendered in a map\n\n"

                ":param arg1: Grid file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"
               ).staticmethod("make_mi_tabfrom_grid");
    pyClass.def("make_mi_tabfrom_map", &GXIMU_wrap_make_mi_tabfrom_map,
                "make_mi_tabfrom_map((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Make a MapInfo tab file from this map\n\n"

                ":param arg1: Map file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"
               ).staticmethod("make_mi_tabfrom_map");
    pyClass.def("mosaic", &GXIMU_wrap_mosaic,
                "mosaic((str)arg1, (str)arg2, (GXIPJ)arg3, (float)arg4) -> GXIMG:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a mosaic image of an image list.\n\n"

                ":param arg1: Image names ('\\ `|`\\ ' separated)\n"
                ":type arg1: str\n"
                ":param arg2: Output image name (\"\" for a memory only image)\n"
                ":type arg2: str\n"
                ":param arg3: Projection to use (0 to use the first grid's projection)\n"
                ":type arg3: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg4: Cell size to use (rDummy to use first grid)\n"
                ":type arg4: float\n"
                ":returns: IMG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXIMG`\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The images are simply placed on the output image, starting with\n"
                "   					the first image. Note that this function may require very large\n"
                "   					amounts of virtual memory.\n"
                "   				\n\n"
               ).staticmethod("mosaic");
    pyClass.def("peak_size", &GXIMU_wrap_peak_size,
                "peak_size((str)arg1, (GXVV)arg2, (GXVV)arg3, (int)arg4, (float)arg5, (GXVV)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Define the sizes of all the peaks in an image.\n\n"

                ":param arg1: Grid file name\n"
                ":type arg1: str\n"
                ":param arg2: Peaks' X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Peaks' Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Maximum target diameter (window) in # of cells\n"
                ":type arg4: int\n"
                ":param arg5: Precision factor (see note above)\n"
                ":type arg5: float\n"
                ":param arg6: Returned peak (anomaly) sizes in data units\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Extending from the peak location of an anomaly to the inflection\n"
                "   					points of the grid values along each of the 8 directions results in\n"
                "   					8 radii. Anomaly size is defined as the 2\\ `*`\\ mediam of the 8 radii.\n"
                "   \n"
                "   					Precision factor is used to control definition of an inflection point.\n"
                "   					For points A,B, and C, B is an inflection point if (A+C)/2.0 > B. With\n"
                "   					the precision factor, B is an inflection point only when\n"
                "   					(A+C)/2.0 > B\\ `*`\\ (1.0+Precision factor).\n"
                "   					This factor must be within (-1.0,1.0).\n"
                "   \n"
                "   					Note: \\ :func:`geosoft.gxapi.GXIMU.peak_size2`\\  is probably a better routine...\n"
                "   				\n\n"
               ).staticmethod("peak_size");
    pyClass.def("peak_size2", &GXIMU_wrap_peak_size2,
                "peak_size2((str)arg1, (GXVV)arg2, (GXVV)arg3, (int)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Define the sizes of all the peaks in an image - new algorithm\n\n"

                ":param arg1: Grid file name\n"
                ":type arg1: str\n"
                ":param arg2: Peaks' X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Peaks' Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Maximum target diameter (window) in # of cells\n"
                ":type arg4: int\n"
                ":param arg5: Returned peak (anomaly) sizes in data units\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Extending from the peak location of an anomaly to the inflection\n"
                "   					points of the grid values along each of the 8 directions results in\n"
                "   					8 radii. Anomaly size is defined as the 2\\ `*`\\ mediam of the 8 radii.\n"
                "   \n"
                "   					This algorithm uses 4 successive points d1, d2, d3 and d4 in any\n"
                "   					direction. Given slopes m1 = d2-d1, m2 = d3-d2 and m3 = d4-d3,\n"
                "   					an inflection point occurs between d2 and d3 if m1>m2 and m2<m3.\n"
                "   					The location index is given as i3 - s2/(s2-s1), where i3 is the index\n"
                "   					of d3, and s1=m2-m1 and s2=m3-m2.\n"
                "   \n"
                "   					This algorithm tends to give much smaller (and more reasonable)\n"
                "   					results than \\ :func:`geosoft.gxapi.GXIMU.peak_size`\\ .\n"
                "   				\n\n"
               ).staticmethod("peak_size2");
    pyClass.def("pigeon_hole", &GXIMU_wrap_pigeon_hole,
                "pigeon_hole((GXIMG)arg1, (GXVV)arg2, (GXVV)arg3, (int_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Pigeon-hole and count points by location into a grid.\n\n"

                ":param arg1: input grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: X locations\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y locations\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Number of points located in the grid.\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					X and Y location VVs are input. If a point (X, Y) is located within\n"
                "   					one-half cell width from a location in the grid, then the value of\n"
                "   					the grid at that location is incremented by 1.\n"
                "   					The cells are inclusive at the minima, and exclusive at the maxima:\n"
                "   					e.g. if dDx = dDy = 1, and dXo = dYo = 0, then the corner cell would\n"
                "   					accept values  -0.5 <= X < 0.5 and -0.5 <= Y < 0.5.\n"
                "   					The grid values should be set to 0 before calling this function.\n"
                "   \n"
                "   					The number of points \"pigeon-holed\" is returned to the user.\n"
                "   					This function is useful, for instance, in determining the density of\n"
                "   					sample locations in a survey area.\n"
                "   				\n\n"
               ).staticmethod("pigeon_hole");
    pyClass.def("profile", &GXIMU_wrap_profile,
                "profile((GXIMG)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (GXVV)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Extract a profile from a grid.\n\n"

                ":param arg1: input image\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: X1\n"
                ":type arg2: float\n"
                ":param arg3: Y1\n"
                ":type arg3: float\n"
                ":param arg4: X2\n"
                ":type arg4: float\n"
                ":param arg5: Y2\n"
                ":type arg5: float\n"
                ":param arg6: sample separation, if 0.0, use grid cell size\n"
                ":type arg6: float\n"
                ":param arg7: VV in which to place result\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returned VV will start at X1,Y1 and will sample\n"
                "   					up to X2,Y2 at the specified separation.\n"
                "   				\n\n"
               ).staticmethod("profile");
    pyClass.def("profile_vv", &GXIMU_wrap_profile_vv,
                "profile_vv((GXIMG)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Extract a VV profile from a grid.\n\n"

                ":param arg1: input image\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: X VV coordinates\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y VV coordinates\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: VV in which to place result\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   iGetPolyLine_DBE\n\n"
               ).staticmethod("profile_vv");
    pyClass.def("range_grids", &GXIMU_wrap_range_grids,
                "range_grids((str)arg1, (GXIPJ)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Determine bounding rectangle for a set of grids\n\n"

                ":param arg1: list of grid files, \"\\ `|`\\ \" delimited\n"
                ":type arg1: str\n"
                ":param arg2: projection for the range - see notes\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg3: Min X - returned range in the projection\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Min Y\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Max X\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Max Y\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If an IPJ is IPJ_CS_UNKNOWN, the\n"
                "   					IPJ of the first grid in the list will be used and\n"
                "   					the IPJ will be returned in this setting.\n"
                "   					Otherwise, the range in the requested IPJ will be\n"
                "   					determined.\n"
                "   				\n\n"
               ).staticmethod("range_grids");
    pyClass.def("range_ll", &GXIMU_wrap_range_ll,
                "range_ll((GXIMG)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Determine the range in lat. and long. of a projected grid\n\n"

                ":param arg1: input image\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Min latitude\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Min longitude\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Max latitude\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Max longitude\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This routine determines the latitude and longitudes along the\n"
                "   					edge of a grid and returns the minimal and maximal values.\n"
                "   					It scans each row and and column and finds the first non-dummy\n"
                "   					position at the start and end, and then determines the coordinates\n"
                "   					at those points.\n"
                "   					If the grid has no data, no IPJ object, or if the Source Type of\n"
                "   					the IPJ is not IPJ_TYPE_PCS (projected coordinate system), then the\n"
                "   					returned values are dummies (GS_R8DM).\n"
                "   				\n\n"
               ).staticmethod("range_ll");
    pyClass.def("stat_window", &GXIMU_wrap_stat_window,
                "stat_window((GXIMG)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (int)arg6, (GXST)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate grid statistics in a window\n\n"

                ":param arg1: Name of the grid to get stats from\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: min X window\n"
                ":type arg2: float\n"
                ":param arg3: min Y window\n"
                ":type arg3: float\n"
                ":param arg4: max X window\n"
                ":type arg4: float\n"
                ":param arg5: max Y window\n"
                ":type arg5: float\n"
                ":param arg6: maximum values needed, 0 for all\n"
                ":type arg6: int\n"
                ":param arg7: ST object, stats are accumulated\n"
                ":type arg7: :class:`geosoft.gxapi.GXST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The maximum values needed will beused to\n"
                "   					decimate the sampling of the grid in order to\n"
                "   					improve performance.  100000 is often a good\n"
                "   					number when absolute precision is not\n"
                "   					required.\n"
                "   				\n\n"
               ).staticmethod("stat_window");
    pyClass.def("update_ply", &GXIMU_wrap_update_ply,
                "update_ply((GXIMG)arg1, (GXPLY)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Update the grid boundary in the grid metadata\n\n"

                ":param arg1: The Grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: PLY containing the edges.\n"
                ":type arg2: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					You can call the GridEdgePLY function to get an edge,\n"
                "   					perhaps alter the edge, such as thin it to a reasonable\n"
                "   					resolution, then put set it as the grid boundary by\n"
                "   					calling this funtion.  This is similar to the\n"
                "   					GridPLYEx function except that you get to alter the\n"
                "   					PLY before it is placed back in the IMG.\n"
                "   				\n\n"
               ).staticmethod("update_ply");

    scope().attr("IMU_BOOL_OLAP_AVE") = (int32_t)0;
    scope().attr("IMU_BOOL_OLAP_1") = (int32_t)1;
    scope().attr("IMU_BOOL_OLAP_2") = (int32_t)2;
    scope().attr("IMU_BOOL_OPT_AND") = (int32_t)0;
    scope().attr("IMU_BOOL_OPT_OR") = (int32_t)1;
    scope().attr("IMU_BOOL_OPT_XOR") = (int32_t)2;
    scope().attr("IMU_BOOL_SIZING_MIN") = (int32_t)0;
    scope().attr("IMU_BOOL_SIZING_0") = (int32_t)1;
    scope().attr("IMU_BOOL_SIZING_1") = (int32_t)2;
    scope().attr("IMU_BOOL_SIZING_MAX") = (int32_t)3;
    scope().attr("IMU_DOUBLE_CRC_BITS_EXACT") = (int32_t)0;
    scope().attr("IMU_DOUBLE_CRC_BITS_DEFAULT") = (int32_t)10;
    scope().attr("IMU_DOUBLE_CRC_BITS_MAX") = (int32_t)51;
    scope().attr("IMU_EXPAND_SHAPE_RECTANGLE") = (int32_t)0;
    scope().attr("IMU_EXPAND_SHAPE_SQUARE") = (int32_t)1;
    scope().attr("IMU_FILL_ROLLOPT_LINEAR") = (int32_t)1;
    scope().attr("IMU_FILL_ROLLOPT_SQUARE") = (int32_t)2;
    scope().attr("IMU_FILT_DUMMY_NO") = (int32_t)0;
    scope().attr("IMU_FILT_DUMMY_YES") = (int32_t)1;
    scope().attr("IMU_FILT_FILE_NO") = (int32_t)0;
    scope().attr("IMU_FILT_FILE_YES") = (int32_t)1;
    scope().attr("IMU_FILT_HZDRV_NO") = (int32_t)0;
    scope().attr("IMU_FILT_HZDRV_X") = (int32_t)1;
    scope().attr("IMU_FILT_HZDRV_Y") = (int32_t)2;
    scope().attr("IMU_FLOAT_CRC_BITS_EXACT") = (int32_t)0;
    scope().attr("IMU_FLOAT_CRC_BITS_DEFAULT") = (int32_t)7;
    scope().attr("IMU_FLOAT_CRC_BITS_MAX") = (int32_t)22;
    scope().attr("IMU_MASK_INSIDE") = (int32_t)0;
    scope().attr("IMU_MASK_OUTSIDE") = (int32_t)1;
    scope().attr("IMU_STAT_FORCED_NO") = (int32_t)0;
    scope().attr("IMU_STAT_FORCED_YES") = (int32_t)1;
    scope().attr("IMU_TRANS_DEFAULT") = (int32_t)0;
    scope().attr("IMU_TRANS_Y") = (int32_t)1;
    scope().attr("IMU_TRANS_X") = (int32_t)-1;
    scope().attr("IMU_TREND_ALL") = (int32_t)0;
    scope().attr("IMU_TREND_EDGE") = (int32_t)1;
    scope().attr("IMU_WIND_GRID") = (int32_t)0;
    scope().attr("IMU_WIND_GROUND") = (int32_t)1;
    scope().attr("IMU_WIND_DUMMY") = (int32_t)0;
    scope().attr("IMU_WIND_CLIP") = (int32_t)1;
    scope().attr("IMU_XYZ_INDEX_NO") = (int32_t)0;
    scope().attr("IMU_XYZ_INDEX_YES") = (int32_t)1;
    scope().attr("IMU_XYZ_LABEL_NO") = (int32_t)1;
    scope().attr("IMU_XYZ_LABEL_YES") = (int32_t)0;

}
