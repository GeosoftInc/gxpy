#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXIPJ_wrap_clear_warp(GXIPJPtr self)
{
    self->clear_warp();
}
inline void GXIPJ_wrap_make_geographic(GXIPJPtr self)
{
    self->make_geographic();
}
inline void GXIPJ_wrap_make_wgs84(GXIPJPtr self)
{
    self->make_wgs84();
}
inline void GXIPJ_wrap_set_units(GXIPJPtr self, double arg1, const gx_string_type& arg2)
{
    self->set_units(arg1, arg2);
}
inline void GXIPJ_wrap_add_exagg_warp(GXIPJPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6)
{
    self->add_exagg_warp(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXIPJ_wrap_add_log_warp(GXIPJPtr self, int32_t arg1, int32_t arg2)
{
    self->add_log_warp(arg1, arg2);
}
inline void GXIPJ_wrap_add_matrix_warp(GXIPJPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10, double arg11, double arg12, double arg13, double arg14, double arg15, double arg16)
{
    self->add_matrix_warp(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16);
}
inline void GXIPJ_wrap_add_warp(GXIPJPtr self, int32_t arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5)
{
    self->add_warp((IPJ_TYPE)arg1, arg2, arg3, arg4, arg5);
}
inline void GXIPJ_wrap_clear_coordinate_system(GXIPJPtr self)
{
    self->clear_coordinate_system();
}
inline void GXIPJ_wrap_clear_orientation(GXIPJPtr self)
{
    self->clear_orientation();
}
inline void GXIPJ_wrap_convert_orientation_warp_vv(GXIPJPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, int32_t arg4)
{
    self->convert_orientation_warp_vv(arg1, arg2, arg3, arg4);
}
inline void GXIPJ_wrap_copy(GXIPJPtr self, GXIPJPtr arg1)
{
    self->copy(arg1);
}
inline void GXIPJ_wrap_copy_projection(GXIPJPtr self, GXIPJPtr arg1)
{
    self->copy_projection(arg1);
}
inline GXIPJPtr GXIPJ_wrap_create()
{
    GXIPJPtr ret = GXIPJ::create();
    return ret;
}
inline GXIPJPtr GXIPJ_wrap_create_s(GXBFPtr arg1)
{
    GXIPJPtr ret = GXIPJ::create_s(arg1);
    return ret;
}
inline GXIPJPtr GXIPJ_wrap_create_xml(const gx_string_type& arg1)
{
    GXIPJPtr ret = GXIPJ::create_xml(arg1);
    return ret;
}
inline void GXIPJ_wrap_get_3d_view(GXIPJPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9)
{
    self->get_3d_view(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXIPJ_wrap_get_3d_view_ex(GXIPJPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9, int_ref& arg10, int_ref& arg11)
{
    self->get_3d_view_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (IPJ_3D_ROTATE&)arg10, (IPJ_3D_FLAG&)arg11);
}
inline void GXIPJ_wrap_get_crooked_section_view_v_vs(GXIPJPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, int_ref& arg4)
{
    self->get_crooked_section_view_v_vs(arg1, arg2, arg3, arg4);
}
inline void GXIPJ_wrap_get_list(int32_t arg1, const gx_string_type& arg2, GXLSTPtr arg3)
{
    GXIPJ::get_list((IPJ_PARM_LST)arg1, arg2, arg3);
}
inline void GXIPJ_wrap_get_orientation_info(GXIPJPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    self->get_orientation_info(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIPJ_wrap_get_plane_equation(GXIPJPtr self, double arg1, double arg2, double arg3, double arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9, float_ref& arg10, float_ref& arg11, float_ref& arg12, float_ref& arg13)
{
    self->get_plane_equation(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13);
}
inline void GXIPJ_wrap_get_plane_equation2(GXIPJPtr self, GXIPJPtr arg1, double arg2, double arg3, double arg4, double arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9, float_ref& arg10, float_ref& arg11, float_ref& arg12, float_ref& arg13, float_ref& arg14)
{
    self->get_plane_equation2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14);
}
inline int32_t GXIPJ_wrap_compare_datums(GXIPJPtr self, GXIPJPtr arg1)
{
    int32_t ret = self->compare_datums(arg1);
    return ret;
}
inline int32_t GXIPJ_wrap_convert_warp(GXIPJPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, int32_t arg4)
{
    int32_t ret = self->convert_warp(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXIPJ_wrap_convert_warp_vv(GXIPJPtr self, GXVVPtr arg1, GXVVPtr arg2, int32_t arg3)
{
    int32_t ret = self->convert_warp_vv(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXIPJ_wrap_coordinate_systems_are_the_same(GXIPJPtr self, GXIPJPtr arg1)
{
    int32_t ret = self->coordinate_systems_are_the_same(arg1);
    return ret;
}
inline int32_t GXIPJ_wrap_coordinate_systems_are_the_same_within_a_small_tolerance(GXIPJPtr self, GXIPJPtr arg1)
{
    int32_t ret = self->coordinate_systems_are_the_same_within_a_small_tolerance(arg1);
    return ret;
}
inline void GXIPJ_wrap_get_display_name(GXIPJPtr self, str_ref& arg1)
{
    self->get_display_name(arg1);
}
inline void GXIPJ_wrap_get_esri(GXIPJPtr self, str_ref& arg1)
{
    self->get_esri(arg1);
}
inline void GXIPJ_wrap_get_gxf(GXIPJPtr self, str_ref& arg1, str_ref& arg2, str_ref& arg3, str_ref& arg4, str_ref& arg5)
{
    self->get_gxf(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIPJ_wrap_get_mi_coord_sys(GXIPJPtr self, str_ref& arg1, str_ref& arg2)
{
    self->get_mi_coord_sys(arg1, arg2);
}
inline void GXIPJ_wrap_get_name(GXIPJPtr self, int32_t arg1, str_ref& arg2)
{
    self->get_name((IPJ_NAME)arg1, arg2);
}
inline int32_t GXIPJ_wrap_get_orientation(GXIPJPtr self)
{
    IPJ_ORIENT ret = self->get_orientation();
    return ret;
}
inline void GXIPJ_wrap_get_orientation_name(GXIPJPtr self, str_ref& arg1)
{
    self->get_orientation_name(arg1);
}
inline void GXIPJ_wrap_get_units(GXIPJPtr self, float_ref& arg1, str_ref& arg2)
{
    self->get_units(arg1, arg2);
}
inline void GXIPJ_wrap_get_xml(GXIPJPtr self, str_ref& arg1)
{
    self->get_xml(arg1);
}
inline int32_t GXIPJ_wrap_has_projection(GXIPJPtr self)
{
    int32_t ret = self->has_projection();
    return ret;
}
inline int32_t GXIPJ_wrap_is_3d_inverted(GXIPJPtr self)
{
    int32_t ret = self->is_3d_inverted();
    return ret;
}
inline int32_t GXIPJ_wrap_is_3d_inverted_angles(GXIPJPtr self)
{
    int32_t ret = self->is_3d_inverted_angles();
    return ret;
}
inline int32_t GXIPJ_wrap_is_geographic(GXIPJPtr self)
{
    int32_t ret = self->is_geographic();
    return ret;
}
inline int32_t GXIPJ_wrap_orientations_are_the_same(GXIPJPtr self, GXIPJPtr arg1)
{
    int32_t ret = self->orientations_are_the_same(arg1);
    return ret;
}
inline int32_t GXIPJ_wrap_orientations_are_the_same_within_a_small_tolerance(GXIPJPtr self, GXIPJPtr arg1)
{
    int32_t ret = self->orientations_are_the_same_within_a_small_tolerance(arg1);
    return ret;
}
inline int32_t GXIPJ_wrap_has_section_orientation(GXIPJPtr self)
{
    int32_t ret = self->has_section_orientation();
    return ret;
}
inline int32_t GXIPJ_wrap_projection_type_is_fully_supported(GXIPJPtr self)
{
    int32_t ret = self->projection_type_is_fully_supported();
    return ret;
}
inline int32_t GXIPJ_wrap_set_gxf_safe(GXIPJPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5)
{
    int32_t ret = self->set_gxf_safe(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline int32_t GXIPJ_wrap_source_type(GXIPJPtr self)
{
    IPJ_TYPE ret = self->source_type();
    return ret;
}
inline int32_t GXIPJ_wrap_support_datum_transform(GXIPJPtr self, GXIPJPtr arg1)
{
    int32_t ret = self->support_datum_transform(arg1);
    return ret;
}
inline void GXIPJ_wrap_unit_name(double arg1, int32_t arg2, str_ref& arg3)
{
    GXIPJ::unit_name(arg1, (IPJ_UNIT)arg2, arg3);
}
inline bool GXIPJ_wrap_warped(GXIPJPtr self)
{
    bool ret = self->warped();
    return ret;
}
inline int32_t GXIPJ_wrap_warps_are_the_same(GXIPJPtr self, GXIPJPtr arg1)
{
    int32_t ret = self->warps_are_the_same(arg1);
    return ret;
}
inline int32_t GXIPJ_wrap_warps_are_the_same_within_a_small_tolerance(GXIPJPtr self, GXIPJPtr arg1)
{
    int32_t ret = self->warps_are_the_same_within_a_small_tolerance(arg1);
    return ret;
}
inline int32_t GXIPJ_wrap_warp_type(GXIPJPtr self)
{
    IPJ_WARP ret = self->warp_type();
    return ret;
}
inline void GXIPJ_wrap_make_projected(GXIPJPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->make_projected(arg1, arg2, arg3, arg4);
}
inline void GXIPJ_wrap_new_box_resolution(GXIPJPtr self, GXIPJPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9)
{
    self->new_box_resolution(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXIPJ_wrap_read(GXIPJPtr self, int32_t arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    self->read((IPJ_TYPE)arg1, arg2, arg3, arg4);
}
inline double GXIPJ_wrap_get_method_parm(GXIPJPtr self, int32_t arg1)
{
    double ret = self->get_method_parm((IPJ_CSP)arg1);
    return ret;
}
inline double GXIPJ_wrap_get_north_azimuth(GXIPJPtr self, double arg1, double arg2)
{
    double ret = self->get_north_azimuth(arg1, arg2);
    return ret;
}
inline double GXIPJ_wrap_unit_scale(const gx_string_type& arg1, double arg2)
{
    double ret = GXIPJ::unit_scale(arg1, arg2);
    return ret;
}
inline void GXIPJ_wrap_serial(GXIPJPtr self, GXBFPtr arg1)
{
    self->serial(arg1);
}
inline void GXIPJ_wrap_serial_fgdcxml(GXIPJPtr self, const gx_string_type& arg1)
{
    self->serial_fgdcxml(arg1);
}
inline void GXIPJ_wrap_serial_isoxml(GXIPJPtr self, const gx_string_type& arg1)
{
    self->serial_isoxml(arg1);
}
inline void GXIPJ_wrap_serial_xml(GXIPJPtr self, const gx_string_type& arg1)
{
    self->serial_xml(arg1);
}
inline void GXIPJ_wrap_set_3d_inverted(GXIPJPtr self, int32_t arg1)
{
    self->set_3d_inverted(arg1);
}
inline void GXIPJ_wrap_set_3d_inverted_angles(GXIPJPtr self, int32_t arg1)
{
    self->set_3d_inverted_angles(arg1);
}
inline void GXIPJ_wrap_set_3d_view(GXIPJPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9)
{
    self->set_3d_view(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline void GXIPJ_wrap_set_3d_view_ex(GXIPJPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, int32_t arg10, int32_t arg11)
{
    self->set_3d_view_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (IPJ_3D_ROTATE)arg10, (IPJ_3D_FLAG)arg11);
}
inline void GXIPJ_wrap_set_3d_view_from_axes(GXIPJPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10, double arg11, double arg12)
{
    self->set_3d_view_from_axes(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12);
}
inline void GXIPJ_wrap_set_crooked_section_view(GXIPJPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, int32_t arg4)
{
    self->set_crooked_section_view(arg1, arg2, arg3, arg4);
}
inline void GXIPJ_wrap_set_depth_section_view(GXIPJPtr self, double arg1)
{
    self->set_depth_section_view(arg1);
}
inline void GXIPJ_wrap_set_esri(GXIPJPtr self, const gx_string_type& arg1)
{
    self->set_esri(arg1);
}
inline void GXIPJ_wrap_set_gxf(GXIPJPtr self, const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5)
{
    self->set_gxf(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIPJ_wrap_set_method_parm(GXIPJPtr self, int32_t arg1, double arg2)
{
    self->set_method_parm((IPJ_CSP)arg1, arg2);
}
inline void GXIPJ_wrap_set_mi_coord_sys(GXIPJPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->set_mi_coord_sys(arg1, arg2);
}
inline void GXIPJ_wrap_set_normal_section_view(GXIPJPtr self, double arg1, double arg2, double arg3, double arg4, double arg5)
{
    self->set_normal_section_view(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIPJ_wrap_set_plan_view(GXIPJPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->set_plan_view(arg1, arg2, arg3, arg4);
}
inline void GXIPJ_wrap_set_section_view(GXIPJPtr self, double arg1, double arg2, double arg3, double arg4, double arg5)
{
    self->set_section_view(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIPJ_wrap_set_wms_coord_sys(GXIPJPtr self, const gx_string_type& arg1, double arg2, double arg3, double arg4, double arg5)
{
    self->set_wms_coord_sys(arg1, arg2, arg3, arg4, arg5);
}
inline void GXIPJ_wrap_set_xml(GXIPJPtr self, const gx_string_type& arg1)
{
    self->set_xml(arg1);
}
inline void GXIPJ_wrap_get_3d_matrix_orientation(GXIPJPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9, float_ref& arg10, float_ref& arg11, float_ref& arg12, float_ref& arg13, float_ref& arg14, float_ref& arg15, float_ref& arg16)
{
    self->get_3d_matrix_orientation(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16);
}
inline void GXIPJ_wrap_set_3d_matrix_orientation(GXIPJPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10, double arg11, double arg12, double arg13, double arg14, double arg15, double arg16)
{
    self->set_3d_matrix_orientation(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16);
}
inline void GXIPJ_wrap_reproject_section_grid(GXIPJPtr self, GXIPJPtr arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    self->reproject_section_grid(arg1, arg2, arg3, arg4, arg5, arg6);
}

void gxPythonImportGXIPJ()
{

    class_<GXIPJ, GXIPJPtr> pyClass("GXIPJ",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		The IPJ class describes a single spatial reference in the world,\n"
                                    "   		defined under a coordinate system, an orientation,\n"
                                    "   		and a warp (which can be used to distort the projected object\n"
                                    "   		to a particular shape or boundary).\n"
                                    "   	\n\n"

                                    "\n\n**Note:**\n\n"

                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		IPJ objects may be attached to channels or views. Two IPJs taken\n"
                                    "   		together are used to create a PJ object, which allows for the\n"
                                    "   		conversion of positions from one projection to the other.\n"
                                    "   		See also the LL2 class, which creates Datum correction lookups.\n"
                                    "   \n"
                                    "   		See also          PJ    Converts coordinates between projections\n"
                                    "   		LL2   Creates Datum correction lookups.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXIPJ::null, "null() -> GXIPJ\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXIPJ`\n\n:returns: A null :class:`geosoft.gxapi.GXIPJ`\n:rtype: :class:`geosoft.gxapi.GXIPJ`\n").staticmethod("null");
    pyClass.def("is_null", &GXIPJ::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXIPJ is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXIPJ`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXIPJ::_internal_handle);
    pyClass.def("clear_warp", &GXIPJ_wrap_clear_warp,
                "clear_warp() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clear warp parameters (if any) from an IPJ.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("make_geographic", &GXIPJ_wrap_make_geographic,
                "make_geographic() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove a projected coordinate system from an IPJ\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function does nothing if the IPJ is not a projected coordinate system.\n\n"
               );
    pyClass.def("make_wgs84", &GXIPJ_wrap_make_wgs84,
                "make_wgs84() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Make a WGS 84 geographic projection\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               );
    pyClass.def("set_units", &GXIPJ_wrap_set_units,
                "set_units((float)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set unit parameters\n\n"

                ":param arg1: factor to meters, must be >= 0.0\n"
                ":type arg1: float\n"
                ":param arg2: abbreviation, can be \"\"\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("add_exagg_warp", &GXIPJ_wrap_add_exagg_warp,
                "add_exagg_warp((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a warp to IPJ to exaggerate X, Y and Z.\n\n"

                ":param arg1: X exaggeration, must be > 0.0\n"
                ":type arg1: float\n"
                ":param arg2: Y exaggeration, must be > 0.0\n"
                ":type arg2: float\n"
                ":param arg3: Z exaggeration, must be > 0.0\n"
                ":type arg3: float\n"
                ":param arg4: X reference origin\n"
                ":type arg4: float\n"
                ":param arg5: Y reference origin\n"
                ":type arg5: float\n"
                ":param arg6: Z reference origin\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("add_log_warp", &GXIPJ_wrap_add_log_warp,
                "add_log_warp((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a warp to IPJ to log one or both coordinantes\n\n"

                ":param arg1: Log in X?\n"
                ":type arg1: int\n"
                ":param arg2: Log in Y?\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("add_matrix_warp", &GXIPJ_wrap_add_matrix_warp,
                "add_matrix_warp((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14, (float)arg15, (float)arg16) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a warp to IPJ using a matrix\n\n"

                ":param arg1: Row 0 Element 0\n"
                ":type arg1: float\n"
                ":param arg2: Row 0 Element 1\n"
                ":type arg2: float\n"
                ":param arg3: Row 0 Element 2\n"
                ":type arg3: float\n"
                ":param arg4: Row 0 Element 3\n"
                ":type arg4: float\n"
                ":param arg5: Row 1 Element 0\n"
                ":type arg5: float\n"
                ":param arg6: Row 1 Element 1\n"
                ":type arg6: float\n"
                ":param arg7: Row 1 Element 2\n"
                ":type arg7: float\n"
                ":param arg8: Row 1 Element 3\n"
                ":type arg8: float\n"
                ":param arg9: Row 2 Element 0\n"
                ":type arg9: float\n"
                ":param arg10: Row 2 Element 1\n"
                ":type arg10: float\n"
                ":param arg11: Row 2 Element 2\n"
                ":type arg11: float\n"
                ":param arg12: Row 2 Element 3\n"
                ":type arg12: float\n"
                ":param arg13: Row 3 Element 0\n"
                ":type arg13: float\n"
                ":param arg14: Row 3 Element 1\n"
                ":type arg14: float\n"
                ":param arg15: Row 3 Element 2\n"
                ":type arg15: float\n"
                ":param arg16: Row 3 Element 3\n"
                ":type arg16: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("add_warp", &GXIPJ_wrap_add_warp,
                "add_warp((int)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a warp to IPJ.\n\n"

                ":param arg1: \\ :ref:`IPJ_TYPE`\\ \n"
                ":type arg1: int\n"
                ":param arg2: Old X VV (real)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Old Y VV (real)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: New X VV (real)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: New Y VV (real)\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					There must be at least \"warp type\" points in the\n"
                "   					warp point VV's.\n"
                "   					All point VV's must have the same number of points.\n"
                "   					If there are more points than required by the warp,\n"
                "   					the warp will be determined by least-square fitting\n"
                "   					to the warp surface for all but the 4-point warp.\n"
                "   					The 4-point ward requires exactly 4 points.\n"
                "   \n"
                "   					Cannot be used with WARP_MATRIX or WARP_LOG\n"
                "   				\n\n"
               );
    pyClass.def("clear_coordinate_system", &GXIPJ_wrap_clear_coordinate_system,
                "clear_coordinate_system() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clear coordinate sytsem, except for units\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Clears the Datum, Local Datum and Projection info.\n"
                "   					Leaves units, any warp or orientation warp unchanged.\n"
                "   				\n\n"
               );
    pyClass.def("clear_orientation", &GXIPJ_wrap_clear_orientation,
                "clear_orientation() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clear an orientation warp from an IPJ.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("convert_orientation_warp_vv", &GXIPJ_wrap_convert_orientation_warp_vv,
                "convert_orientation_warp_vv((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert X,Y and Z VVs using the orientation warp from an IPJ.\n\n"

                ":param arg1: X VV coordinates converted on output\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV coordinates converted on output\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z VV coordinates converted on output\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: 1 -  Forward (raw -> coordinate) , 0 - (coordinate -> raw)\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               );
    pyClass.def("copy", &GXIPJ_wrap_copy,
                "copy((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy IPJs\n\n"

                ":param arg1: destination IPJ\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("copy_projection", &GXIPJ_wrap_copy_projection,
                "copy_projection((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy the projection from one IPJ to another\n\n"

                ":param arg1: source\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Copies the projection parameters, while leaving the rest\n"
                "   					(e.g. Datum, Local Datum Transform) unchanged.\n"
                "   				\n\n"
               );
    pyClass.def("create", &GXIPJ_wrap_create,
                "create() -> GXIPJ:\n"

                "\n.. parsed-literal::\n\n"
                "   This method creates a projection object.\n\n"

                ":returns: IPJ Object\n"
                ":rtype: :class:`geosoft.gxapi.GXIPJ`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_s", &GXIPJ_wrap_create_s,
                "create_s((GXBF)arg1) -> GXIPJ:\n"

                "\n.. parsed-literal::\n\n"
                "   Create IPJ from serialized source.\n\n"

                ":param arg1: BF\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: IPJ Object\n"
                ":rtype: :class:`geosoft.gxapi.GXIPJ`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_s");
    pyClass.def("create_xml", &GXIPJ_wrap_create_xml,
                "create_xml((str)arg1) -> GXIPJ:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an IPJ from serialized Geosoft MetaData XML file\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":returns: IPJ Object\n"
                ":rtype: :class:`geosoft.gxapi.GXIPJ`\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("create_xml");
    pyClass.def("get_3d_view", &GXIPJ_wrap_get_3d_view,
                "get_3d_view((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get 3D orientation parameters\n\n"

                ":param arg1: X location of view origin\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y location of view origin\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Z location of view origin\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Rotation in X\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Rotation in Y\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Rotation in Z\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Scaling in X\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Scaling in Y\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Scaling in Z\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The view must have a 3D orientation\n\n"
               );
    pyClass.def("get_3d_view_ex", &GXIPJ_wrap_get_3d_view_ex,
                "get_3d_view_ex((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9, (int_ref)arg10, (int_ref)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get 3D orientation parameters with new flags\n\n"

                ":param arg1: X location of view origin\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y location of view origin\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Z location of view origin\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Rotation in X\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Rotation in Y\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Rotation in Z\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Scaling in X\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Scaling in Y\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Scaling in Z\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: \\ :ref:`IPJ_3D_ROTATE`\\ \n"
                ":type arg10: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg11: \\ :ref:`IPJ_3D_FLAG`\\ \n"
                ":type arg11: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The view must have a 3D orientation\n\n"
               );
    pyClass.def("get_crooked_section_view_v_vs", &GXIPJ_wrap_get_crooked_section_view_v_vs,
                "get_crooked_section_view_v_vs((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (int_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the crooked section path.\n\n"

                ":param arg1: Section X locations (e.g. distance along the curve)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: True X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: True Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Use logarithmic Y-axis (usually for data profiles) 0:No, 1:Yes\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the orignal VVs used to set up the crooked section path.\n\n"
               );
    pyClass.def("get_list", &GXIPJ_wrap_get_list,
                "get_list((int)arg1, (str)arg2, (GXLST)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of parameters.\n\n"

                ":param arg1: \\ :ref:`IPJ_PARM_LST`\\ \n"
                ":type arg1: int\n"
                ":param arg2: datum filter, \"\" for no filter\n"
                ":type arg2: str\n"
                ":param arg3: list returned\n"
                ":type arg3: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The datum filter string, if specified, will limit the requested\n"
                "   					list to those valid for the spacified datum.\n"
                "   				\n\n"
               ).staticmethod("get_list");
    pyClass.def("get_orientation_info", &GXIPJ_wrap_get_orientation_info,
                "get_orientation_info((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get IPJ orientation parameters.\n\n"

                ":param arg1: Plane Origin X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Plane Origin Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Plane Origin Z\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Plane Azimuth (section) or Rotation (plan)\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Plane Swing   (section)\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					IPJ_ORIENT_TYPE:\n"
                "   					IPJ_ORIENT_DEFAULT - no special orientation - plan view.\n"
                "   					This is equivalent to IPJ_ORIENT_PLAN with\n"
                "   					dXo = dYo = dZo = dRotation = 0.0.\n"
                "   \n"
                "   					IPJ_ORIENT_PLAN      Azimuth = Rotation CCW degrees\n"
                "   					The plan differs from the default view in that\n"
                "   					a reference level is set, and the axes can be\n"
                "   					rotated and offset from the local X,Y.\n"
                "   \n"
                "   					IPJ_ORIENT_SECTION   Azimuth - CW degrees from North\n"
                "   					-360 <= azimuth <= 360\n"
                "   					Swing - degrees bottom towards viewer\n"
                "   					-90 < swing < 90\n"
                "   					The section view projects all plotted objects\n"
                "   					HORIZONTALLY onto the viewing plan in order to\n"
                "   					preserve elevations, even if the section has a swing.\n"
                "   				\n\n"
               );
    pyClass.def("get_plane_equation", &GXIPJ_wrap_get_plane_equation,
                "get_plane_equation((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9, (float_ref)arg10, (float_ref)arg11, (float_ref)arg12, (float_ref)arg13) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the equation of a plane\n\n"

                ":param arg1: Min X of surface\n"
                ":type arg1: float\n"
                ":param arg2: Min Y of surface\n"
                ":type arg2: float\n"
                ":param arg3: Max X of surface\n"
                ":type arg3: float\n"
                ":param arg4: Max Y of surface\n"
                ":type arg4: float\n"
                ":param arg5: Pitch angle (between -360 and 360)\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Yaw angle (between -360 and 360)\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Roll angles (between -360 and 360)\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: X offset of plane\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Y offset of plane\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: Z offset of plane\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: X scale\n"
                ":type arg11: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg12: Y scale\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg13: Z scale\n"
                ":type arg13: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Two opposite corners of the plane are required.\n"
                "   					Because the origin of the plane does not necessarily\n"
                "   					have a stable back-projection into true 3d coordinates.\n"
                "   					In practice, use the current view extents, or the corners\n"
                "   					of a grid.\n"
                "   				\n\n"
               );
    pyClass.def("get_plane_equation2", &GXIPJ_wrap_get_plane_equation2,
                "get_plane_equation2((GXIPJ)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9, (float_ref)arg10, (float_ref)arg11, (float_ref)arg12, (float_ref)arg13, (float_ref)arg14) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the equation of a plane with reprojection.\n\n"

                ":param arg1: IPJ object for the output values\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: Min X of surface (in grid coords)\n"
                ":type arg2: float\n"
                ":param arg3: Min Y of surface\n"
                ":type arg3: float\n"
                ":param arg4: Max X of surface\n"
                ":type arg4: float\n"
                ":param arg5: Max Y of surface\n"
                ":type arg5: float\n"
                ":param arg6: Pitch angle (between -360 and 360) (in view coords)\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Yaw angle (between -360 and 360)\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Roll angles (between -360 and 360)\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: X offset of plane (in view coords)\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: Y offset of plane\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: Z offset of plane\n"
                ":type arg11: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg12: X scale (in view coords)\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg13: Y scale\n"
                ":type arg13: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg14: Z scale\n"
                ":type arg14: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.1\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is the same as \\ :func:`geosoft.gxapi.GXIPJ.get_plane_equation`\\ , but the\n"
                "   					input projected coordinate system (PCS) may\n"
                "   					be different from that of the IPJ you want the\n"
                "   					plane equation values described in. This may be\n"
                "   					required, for instance, when a 3D view has been created\n"
                "   					in one PCS, and an oriented grid from a different PCS is\n"
                "   					to be displayed in that view.\n"
                "   \n"
                "   					If the two input IPJs share the same PCS (determined\n"
                "   					using the \\ :func:`geosoft.gxapi.GXIPJ.same`\\  function), then the \\ :func:`geosoft.gxapi.GXIPJ.get_plane_equation`\\ \n"
                "   					function is called directly, using the input IPJ.\n"
                "   				\n\n"
               );
    pyClass.def("compare_datums", &GXIPJ_wrap_compare_datums,
                "compare_datums((GXIPJ)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Compare the datums of two coordinate systems?\n\n"

                ":param arg1: IPJ 2\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: 0 - Datums are different\n"
                "          						1 - Datums are the same, but different LDT\n"
                "          						2 - Datums and LTD are the same\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					To transform between different datums requires the use of a local\n"
                "   					datum transform.  The local datum transform can be defined when\n"
                "   					a coordinate system is created, but the definition is optional.\n"
                "   					This function will test that the local datum transforms are defined.\n"
                "   					Note that a coordinate transformation between datums without a\n"
                "   					local datum transform is still possible, but only the effect of\n"
                "   					ellipsoid shape will be modelled in the transform.\n"
                "   				\n\n"
               );
    pyClass.def("convert_warp", &GXIPJ_wrap_convert_warp,
                "convert_warp((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (int)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Converts a point X, Y, Z to the new IPJ plane.\n\n"

                ":param arg1: X coordinates converted on output\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y coordinates converted on output\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Z coordinates converted on output\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: 1 -  Forward (raw -> coordinate) , 0 - (coordinate -> raw)\n"
                ":type arg4: int\n"
                ":returns: 0 if ok - 1 otherwise\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("convert_warp_vv", &GXIPJ_wrap_convert_warp_vv,
                "convert_warp_vv((GXVV)arg1, (GXVV)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Converts a set of X & Y VVs to the new IPJ plane. The Z is assumed to be 0\n\n"

                ":param arg1: X VV coordinates converted on output\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV coordinates converted on output\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: 1 -  Forward (raw -> coordinate) , 0 - (coordinate -> raw)\n"
                ":type arg3: int\n"
                ":returns: 0 if ok - 1 otherwise\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("coordinate_systems_are_the_same", &GXIPJ_wrap_coordinate_systems_are_the_same,
                "coordinate_systems_are_the_same((GXIPJ)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Are these two coordinate systems the same?\n\n"

                ":param arg1: IPJ 2\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: 0 - No\n"
                "          						1 - Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This does not compare LDT information (use \\ :func:`geosoft.gxapi.GXIPJ.compare_datums`\\  for that).\n\n"
               );
    pyClass.def("coordinate_systems_are_the_same_within_a_small_tolerance", &GXIPJ_wrap_coordinate_systems_are_the_same_within_a_small_tolerance,
                "coordinate_systems_are_the_same_within_a_small_tolerance((GXIPJ)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXIPJ.coordinate_systems_are_the_same`\\ , but allows for small numerical differences\n\n"

                ":param arg1: IPJ 2\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: 0 - No\n"
                "          						1 - Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("get_display_name", &GXIPJ_wrap_get_display_name,
                "get_display_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a name for display purposes from IPJ\n\n"

                ":param arg1: name returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("get_esri", &GXIPJ_wrap_get_esri,
                "get_esri((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Store coordinate system in an ESRI prj coordinate string\n\n"

                ":param arg1: ESRI projection string returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the projection is not supported in ESRI, the projection\n"
                "   					string will be empty.\n"
                "   				\n\n"
               );
    pyClass.def("get_gxf", &GXIPJ_wrap_get_gxf,
                "get_gxf((str_ref)arg1, (str_ref)arg2, (str_ref)arg3, (str_ref)arg4, (str_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Store coordinate system in GXF style strings.\n\n"

                ":param arg1: projection name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: datum name, major axis, elipticity\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: method name, parameters\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: unit name, factor\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: local transform name,dX,dY,dZ,rX,rY,rZ,Scale\n"
                ":type arg5: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					See GXF revision 3 for string descriptions\n"
                "   					All strings must be the same length, 160 (STR_GXF) recommended.\n"
                "   					Strings too short will be truncated.\n"
                "   				\n\n"
               );
    pyClass.def("get_mi_coord_sys", &GXIPJ_wrap_get_mi_coord_sys,
                "get_mi_coord_sys((str_ref)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Store coordinate system in MapInfo coordsys pair\n\n"

                ":param arg1: MapInfo coordsys string returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: MapInfo unit string returned\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("get_name", &GXIPJ_wrap_get_name,
                "get_name((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an IPJ name\n\n"

                ":param arg1: \\ :ref:`IPJ_NAME`\\ \n"
                ":type arg1: int\n"
                ":param arg2: name returned\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_orientation", &GXIPJ_wrap_get_orientation,
                "get_orientation() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get IPJ orientation in space.\n\n"

                ":returns: \\ :ref:`IPJ_ORIENT`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Projections can be created oriented horizontally (e.g. in plan maps)\n"
                "   					or vertically (in section maps - Wholeplot and IP).\n"
                "   				\n\n"
               );
    pyClass.def("get_orientation_name", &GXIPJ_wrap_get_orientation_name,
                "get_orientation_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a name for display purposes from IPJ\n\n"

                ":param arg1: name returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("get_units", &GXIPJ_wrap_get_units,
                "get_units((float_ref)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get unit parameters\n\n"

                ":param arg1: factor to meters\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: abbreviation\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_xml", &GXIPJ_wrap_get_xml,
                "get_xml((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an Geosoft Metadata XML string from an IPJ\n\n"

                ":param arg1: XML string returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("has_projection", &GXIPJ_wrap_has_projection,
                "has_projection() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Does the IPJ object contain a projection?\n\n"

                ":returns: 0 - No\n"
                "          						1 - Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("is_3d_inverted", &GXIPJ_wrap_is_3d_inverted,
                "is_3d_inverted() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this 3D View inverted ?\n\n"

                ":returns: 0 - No\n"
                "          						1 - Yes (inverted)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.1\n\n"
               );
    pyClass.def("is_3d_inverted_angles", &GXIPJ_wrap_is_3d_inverted_angles,
                "is_3d_inverted_angles() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Are the angles in this 3D View inverted ?\n\n"

                ":returns: 0 - No\n"
                "          						1 - Yes (inverted)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.1\n\n"
               );
    pyClass.def("is_geographic", &GXIPJ_wrap_is_geographic,
                "is_geographic() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   See if this projection is geographic\n\n"

                ":returns: 0 - No\n"
                "          						1 - Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("orientations_are_the_same", &GXIPJ_wrap_orientations_are_the_same,
                "orientations_are_the_same((GXIPJ)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Are these two orientations the same?\n\n"

                ":param arg1: IPJ 2\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: 0 - No\n"
                "          						1 - Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("orientations_are_the_same_within_a_small_tolerance", &GXIPJ_wrap_orientations_are_the_same_within_a_small_tolerance,
                "orientations_are_the_same_within_a_small_tolerance((GXIPJ)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXIPJ.orientations_are_the_same`\\ , but allows for small numerical differences\n\n"

                ":param arg1: IPJ 2\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: 0 - No\n"
                "          						1 - Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("has_section_orientation", &GXIPJ_wrap_has_section_orientation,
                "has_section_orientation() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Does this projection contain an orientation used by section plots?\n\n"

                ":returns: 0 - No\n"
                "          						1 - Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns     1 if there is a section orientation\n"
                "   \n"
                "   					The following orientations can be used to orient sections or section views:\n"
                "   \n"
                "   					IPJ_ORIENT_SECTION - Target-type sections with Z projection horizontally\n"
                "   					IPJ_ORIENT_SECTION_NORMAL - Like IPJ_ORIENT_SECTION, but Z projects\n"
                "   					perpendicular to the secton plane.\n"
                "   					IPJ_ORIENT_SECTION_CROOKED - Crooked sections\n"
                "   					IPJ_ORIENT_3D - Some Sections extracted from a voxel - e.g. VoxelToGrids,\n"
                "   					as the voxel can have any orientation in 3D.\n"
                "   \n"
                "   					It is sometimes important to ignore the section orientation, for instance\n"
                "   					when rendering a grid in 3D where it has been located on a plane.\n"
                "   				\n\n"
               );
    pyClass.def("projection_type_is_fully_supported", &GXIPJ_wrap_projection_type_is_fully_supported,
                "projection_type_is_fully_supported() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is the projection type fully supported?\n\n"

                ":returns: 0 - No\n"
                "          						1 - Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function checks only the projected coordinated system\n"
                "   					in the IPJ object, so should only be used with projections\n"
                "   					of type IPJ_TYPE_PCS.\n"
                "   					This function does not test the validity of datums or local\n"
                "   					datum transforms.\n"
                "   				\n\n"
               );
    pyClass.def("set_gxf_safe", &GXIPJ_wrap_set_gxf_safe,
                "set_gxf_safe((str)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXIPJ.set_gxf`\\ , but fails gracefully.\n\n"

                ":param arg1: \"projection name\" or PCS_NAME from ipj_pcs.csv (datum / projection) or EPSG coordinate system code number or \"<file.prj>\" projection file name or \"<file.wrp>\" warp file name\n"
                ":type arg1: str\n"
                ":param arg2: \"datum name\"[, major axis, elipticity, prime meridian] or DATUM from datum.csv or EPSG datum code number\n"
                ":type arg2: str\n"
                ":param arg3: \"method name\", parameters (P1 through P8) or \"projection name\"[,\"method name\",\"Units\",P1,P2...] or TRANSFORM from transform.csv or EPSG transform method code number\n"
                ":type arg3: str\n"
                ":param arg4: \"unit name\", convertion to metres or UNIT_LENGTH from units.csv\n"
                ":type arg4: str\n"
                ":param arg5: \"local transform name\"[,dX,dY,dZ,rX,rY,rZ,Scale] or DATUM_TRF from datumtrf.csv or AREA_OF_USE from ldatum.csv or EPSG local datum transform code number\n"
                ":type arg5: str\n"
                ":returns: 0 - error in setting IPJ, input IPJ unchanged.\n"
                "          						1 - success: IPJ set using input values.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXIPJ.set_gxf`\\  will fail and terminate the GX if anything goes wrong (e.g. having a wrong\n"
                "   					parameter). If this function fails, it simply returns 0 and leaves the\n"
                "   					IPJ unchanged.\n"
                "   				\n\n"
               );
    pyClass.def("source_type", &GXIPJ_wrap_source_type,
                "source_type() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get IPJ source type\n\n"

                ":returns: \\ :ref:`IPJ_TYPE`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("support_datum_transform", &GXIPJ_wrap_support_datum_transform,
                "support_datum_transform((GXIPJ)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Can we transform between these two datums?\n\n"

                ":param arg1: IPJ 2\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: 0 - No\n"
                "          						1 - Yes, either because both CS are on the same datum,\n"
                "          						or because a local datum transform is defined\n"
                "          						for each coordinate system.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					To transform between different datums requires the use of a local\n"
                "   					datum transform.  The local datum transform can be defined when\n"
                "   					a coordinate system is created, but the definition is optional.\n"
                "   					This function will test that the local datum transforms are defined.\n"
                "   					Note that a coordinate transformation between datums without a\n"
                "   					local datum transform is still possible, but only the effect of\n"
                "   					ellipsoid shape will be modelled in the transform.\n"
                "   				\n\n"
               );
    pyClass.def("unit_name", &GXIPJ_wrap_unit_name,
                "unit_name((float)arg1, (int)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a unit name given a scale factor\n\n"

                ":param arg1: factor to meters\n"
                ":type arg1: float\n"
                ":param arg2: \\ :ref:`IPJ_UNIT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: name returned, \"\" if cannot find unit\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("unit_name");
    pyClass.def("warped", &GXIPJ_wrap_warped,
                "warped() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Does IPJ contain a warp?\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("warps_are_the_same", &GXIPJ_wrap_warps_are_the_same,
                "warps_are_the_same((GXIPJ)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Are these two warps the same?\n\n"

                ":param arg1: IPJ 2\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: 0 - No\n"
                "          						1 - Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("warps_are_the_same_within_a_small_tolerance", &GXIPJ_wrap_warps_are_the_same_within_a_small_tolerance,
                "warps_are_the_same_within_a_small_tolerance((GXIPJ)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as \\ :func:`geosoft.gxapi.GXIPJ.warps_are_the_same`\\ , but allows for small numerical differences\n\n"

                ":param arg1: IPJ 2\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: 0 - No\n"
                "          						1 - Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );
    pyClass.def("warp_type", &GXIPJ_wrap_warp_type,
                "warp_type() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Obtain the warp type of an IPJ.\n\n"

                ":returns: \\ :ref:`IPJ_WARP`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("make_projected", &GXIPJ_wrap_make_projected,
                "make_projected((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a default projected coordinate system from lat-long ranges.\n\n"

                ":param arg1: minimum longitude\n"
                ":type arg1: float\n"
                ":param arg2: minimum latitude\n"
                ":type arg2: float\n"
                ":param arg3: maximum longitude\n"
                ":type arg3: float\n"
                ":param arg4: maximum latitude\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Terminates with invalid or unsupported ranges.\n"
                "   					If the map crosses the equator, or if map is within 20 degrees of the\n"
                "   					equator, uses an equatorial mercator projection centered at the central\n"
                "   					longitude. Otherwise, uses a Lambert Conic Conformal (1SP) projection\n"
                "   					for the map. Global maps outside of +/- 70 degrees latitude are not\n"
                "   					supported.\n"
                "   				\n\n"
               );
    pyClass.def("new_box_resolution", &GXIPJ_wrap_new_box_resolution,
                "new_box_resolution((GXIPJ)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Determine a data resolution in a new coordinate system\n\n"

                ":param arg1: new IPJ\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: data resolution in original IPJ\n"
                ":type arg2: float\n"
                ":param arg3: X minimum of bounding box in new IPJ\n"
                ":type arg3: float\n"
                ":param arg4: Y minimum\n"
                ":type arg4: float\n"
                ":param arg5: X maximum\n"
                ":type arg5: float\n"
                ":param arg6: Y maximum\n"
                ":type arg6: float\n"
                ":param arg7: minimum data resolution in new IPJ,\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: maximum data resolution in new IPJ\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: diagonal data resolution in new IPJ\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					if there are any problems reprojecting, new resolutions will\n"
                "   					dummy.  The conversion to new resolution is based on measurements\n"
                "   					along the four edges and two diagonals.\n"
                "   				\n\n"
               );
    pyClass.def("read", &GXIPJ_wrap_read,
                "read((int)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Read and define an IPJ from a standard file.\n\n"

                ":param arg1: \\ :ref:`IPJ_TYPE`\\ \n"
                ":type arg1: int\n"
                ":param arg2: string 1\n"
                ":type arg2: str\n"
                ":param arg3: string 2\n"
                ":type arg3: str\n"
                ":param arg4: string 3\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_method_parm", &GXIPJ_wrap_get_method_parm,
                "get_method_parm((int)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get projection method parameter\n\n"

                ":param arg1: \\ :ref:`IPJ_CSP`\\ \n"
                ":type arg1: int\n"
                ":returns: Parameter setting, rDUMMY if dot used\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_north_azimuth", &GXIPJ_wrap_get_north_azimuth,
                "get_north_azimuth((float)arg1, (float)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the azimuth of geographic North at a point.\n\n"

                ":param arg1: input X location\n"
                ":type arg1: float\n"
                ":param arg2: input Y location\n"
                ":type arg2: float\n"
                ":returns: Azimuth (degrees CW) of geographic north from grid north at a location.\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the IPJ is not a projected coordinate system\n"
                "   					then the returned azimuth is GS_R8DM;\n"
                "   				\n\n"
               );
    pyClass.def("unit_scale", &GXIPJ_wrap_unit_scale,
                "unit_scale((str)arg1, (float)arg2) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a unit scale (m/unit) given a name\n\n"

                ":param arg1: unit name, abbreviation or full name\n"
                ":type arg1: str\n"
                ":param arg2: default to return if name not found\n"
                ":type arg2: float\n"
                ":returns: Scale factor m/unit\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If name cannot be found, returns default.\n\n"
               ).staticmethod("unit_scale");
    pyClass.def("serial", &GXIPJ_wrap_serial,
                "serial((GXBF)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Serialize IPJ to a BF.\n\n"

                ":param arg1: BF\n"
                ":type arg1: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("serial_fgdcxml", &GXIPJ_wrap_serial_fgdcxml,
                "serial_fgdcxml((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write the IPJ as a FDGC MetaData XML object\n\n"

                ":param arg1: Name of file to export to\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("serial_isoxml", &GXIPJ_wrap_serial_isoxml,
                "serial_isoxml((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write the IPJ as a ISO MetaData XML object\n\n"

                ":param arg1: Name of file to export to\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("serial_xml", &GXIPJ_wrap_serial_xml,
                "serial_xml((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write the IPJ as a Geosoft MetaData XML object\n\n"

                ":param arg1: Name of file to export to\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_3d_inverted", &GXIPJ_wrap_set_3d_inverted,
                "set_3d_inverted((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set whether a view is inverted (must be 3D already)\n\n"

                ":param arg1: Inverted (0 or 1)\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.1\n\n"
               );
    pyClass.def("set_3d_inverted_angles", &GXIPJ_wrap_set_3d_inverted_angles,
                "set_3d_inverted_angles((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set whether the angles in this view are inverted (must be 3D already)\n\n"

                ":param arg1: Inverted (0 or 1)\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.1\n\n"
               );
    pyClass.def("set_3d_view", &GXIPJ_wrap_set_3d_view,
                "set_3d_view((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set 3D orientation parameters\n\n"

                ":param arg1: X location of view origin\n"
                ":type arg1: float\n"
                ":param arg2: Y location of view origin\n"
                ":type arg2: float\n"
                ":param arg3: Z location of view origin\n"
                ":type arg3: float\n"
                ":param arg4: Rotation in X\n"
                ":type arg4: float\n"
                ":param arg5: Rotation in Y\n"
                ":type arg5: float\n"
                ":param arg6: Rotation in Z\n"
                ":type arg6: float\n"
                ":param arg7: Scaling in X\n"
                ":type arg7: float\n"
                ":param arg8: Scaling in Y\n"
                ":type arg8: float\n"
                ":param arg9: Scaling in Z\n"
                ":type arg9: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Sets up translation, scaling and rotation in all three directions\n"
                "   					for 3D objects.\n"
                "   				\n\n"
               );
    pyClass.def("set_3d_view_ex", &GXIPJ_wrap_set_3d_view_ex,
                "set_3d_view_ex((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (int)arg10, (int)arg11) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set 3D orientation parameters with new flags\n\n"

                ":param arg1: X location of view origin\n"
                ":type arg1: float\n"
                ":param arg2: Y location of view origin\n"
                ":type arg2: float\n"
                ":param arg3: Z location of view origin\n"
                ":type arg3: float\n"
                ":param arg4: Rotation in X\n"
                ":type arg4: float\n"
                ":param arg5: Rotation in Y\n"
                ":type arg5: float\n"
                ":param arg6: Rotation in Z\n"
                ":type arg6: float\n"
                ":param arg7: Scaling in X\n"
                ":type arg7: float\n"
                ":param arg8: Scaling in Y\n"
                ":type arg8: float\n"
                ":param arg9: Scaling in Z\n"
                ":type arg9: float\n"
                ":param arg10: \\ :ref:`IPJ_3D_ROTATE`\\ \n"
                ":type arg10: int\n"
                ":param arg11: \\ :ref:`IPJ_3D_FLAG`\\ \n"
                ":type arg11: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Sets up translation, scaling and rotation in all three directions\n"
                "   					for 3D objects.\n"
                "   				\n\n"
               );
    pyClass.def("set_3d_view_from_axes", &GXIPJ_wrap_set_3d_view_from_axes,
                "set_3d_view_from_axes((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (float)arg11, (float)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set 3D orientation parameters\n\n"

                ":param arg1: X location of view origin\n"
                ":type arg1: float\n"
                ":param arg2: Y location of view origin\n"
                ":type arg2: float\n"
                ":param arg3: Z location of view origin\n"
                ":type arg3: float\n"
                ":param arg4: X axis X component\n"
                ":type arg4: float\n"
                ":param arg5: X axis Y component\n"
                ":type arg5: float\n"
                ":param arg6: X axis Z component\n"
                ":type arg6: float\n"
                ":param arg7: Y axis X component\n"
                ":type arg7: float\n"
                ":param arg8: Y axis Y component\n"
                ":type arg8: float\n"
                ":param arg9: Y axis Z component\n"
                ":type arg9: float\n"
                ":param arg10: Scaling in X\n"
                ":type arg10: float\n"
                ":param arg11: Scaling in Y\n"
                ":type arg11: float\n"
                ":param arg12: Scaling in Z\n"
                ":type arg12: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Sets up translation, scaling and rotation in all three directions\n"
                "   					for 3D objects, based on input origin and X and Y axis vectors.\n"
                "   				\n\n"
               );
    pyClass.def("set_crooked_section_view", &GXIPJ_wrap_set_crooked_section_view,
                "set_crooked_section_view((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set up the crooked section view.\n\n"

                ":param arg1: Section X locations (e.g. distance along the curve)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: True X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: True Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Use logarithmic Y-axis (usually for data profiles) 0:No, 1:Yes\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A non-plane section. It is a vertical section which curves along a path in\n"
                "   					(X, Y).\n"
                "   				\n\n"
               );
    pyClass.def("set_depth_section_view", &GXIPJ_wrap_set_depth_section_view,
                "set_depth_section_view((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set depth section orientation parameters\n\n"

                ":param arg1: View Y value for Depth = 0.0.\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_esri", &GXIPJ_wrap_set_esri,
                "set_esri((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set coordinate system from an ESRI prj coordinate string\n\n"

                ":param arg1: ESRI prj format projection string\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the projection is not supported in Geosoft, the\n"
                "   					IPJ will be unknown.\n"
                "   				\n\n"
               );
    pyClass.def("set_gxf", &GXIPJ_wrap_set_gxf,
                "set_gxf((str)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set coordinate system from GXF style strings.\n\n"

                ":param arg1: \"projection name\" or PCS_NAME from ipj_pcs.csv (datum / projection) or EPSG coordinate system code number or \"<file.prj>\" projection file name or \"<file.wrp>\" warp file name\n"
                ":type arg1: str\n"
                ":param arg2: \"datum name\"[, major axis, elipticity, prime meridian] or DATUM from datum.csv or EPSG datum code number\n"
                ":type arg2: str\n"
                ":param arg3: \"method name\", parameters (P1 through P8) or \"projection name\"[,\"method name\",\"Units\",P1,P2...] or TRANSFORM from transform.csv or EPSG transform method code number\n"
                ":type arg3: str\n"
                ":param arg4: \"unit name\", convertion to metres or UNIT_LENGTH from units.csv\n"
                ":type arg4: str\n"
                ":param arg5: \"local transform name\"[,dX,dY,dZ,rX,rY,rZ,Scale] or DATUM_TRF from datumtrf.csv or AREA_OF_USE from ldatum.csv or EPSG local datum transform code number\n"
                ":type arg5: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Simplest Usage:\n"
                "   \n"
                "   					The coordinate system can be resolved from the \"coordinate system name\"\n"
                "   					if the name is specified using an EPSG number or naming convention such as:\n"
                "   \n"
                "   					\"datum / projection\"  (example: \"Arc 1960 / UTM zone 37S\")\n"
                "   \n"
                "   					Where:\n"
                "   					\"datum\" is the EPSG datum name (eg. NAD83).  All supported datums are\n"
                "   					listed in ...usercsvdatum.csv.\n"
                "   					\"projection\" is the EPSG coordinate system map projection.\n"
                "   					datum name (eg. \"UTM zone 10N\").  All supported coordinate\n"
                "   					system projections are listed in ...user/csv/transform.csv.\n"
                "   					All EPSG known combined coordinate systems of the earth are\n"
                "   					listed in ...user/csv/ipj_pcs.csv.\n"
                "   \n"
                "   					To define a geographic (longitude, latitude) oordinate system, specify\n"
                "   					the datum name alone (ie \"Arc 1960\").  EPSG numbers can also be used, so in\n"
                "   					the example above the name can be \"21037\".\n"
                "   \n"
                "   					The coordinate system may also be oriented arbitrarily in 3D relative to\n"
                "   					the base coordinate system by specifying the orientation as a set of\n"
                "   					6 comma-separated values between angled brackets after the coordinate system name:\n"
                "   \n"
                "   					\"datum / projection\"<oX,oY,oZ,rX,rY,rZ>\n"
                "   					21037<oX,oY,oZ,rX,rY,rZ>\n"
                "   \n"
                "   					where:\n"
                "   					oX,oY,oZ    is the location of the local origin on the CS\n"
                "   					rX,rY,rZ    are rotations in degrees azimuth (clockwise) of\n"
                "   					the local axis frame around the X, Y and Z axis\n"
                "   					respectively.  A simple plane rotation will only have\n"
                "   					a rotation around Z.  For example:\n"
                "   					\"Arc 1960 / UTM zone 37S\"<525000,2500000,0,0,0,15>\n"
                "   					defines a local system with origin at (525000,2500000)\n"
                "   					with a rotation of 15 degrees azimuth.\n"
                "   \n"
                "   					Orientation parameters not defined will default to align with the\n"
                "   					base CS,  Note that although allowed, it does not make sense to have\n"
                "   					an orientation on a geographic coordinate system (long,lat).\n"
                "   \n"
                "   					Complete usage:\n"
                "   \n"
                "   					A coordinate system can also be fully described by providing an additional\n"
                "   					four strings that define the datum, map projection, length units and\n"
                "   					prefered local datum transform.  Refer to GXF revision 3 for further detail:\n"
                "   					http://www.geosoft.com/resources/goto/GXF-Grid-eXchange-File\n"
                "   \n"
                "   					Note that coordinate system reference tables sre maintained in csv files\n"
                "   					located in the .../user/csv folder found with the Geosoft installation files,\n"
                "   					which will usually be located here:\n"
                "   					C:\\Program Files (x86)\\Geosoft\\Oasis montaj\\user\\csv\n"
                "   \n"
                "   					The \"datum\" string can use a datum name defined in the \"datum.csv\" file,\n"
                "   					or the local datum name from datumtrf.csv, or the local datum description\n"
                "   					from ldatum.csv.\n"
                "   					For a non-EPSG datum, you can define your own datum parameters in the\n"
                "   					Datum stringfield as follows:\n"
                "   \n"
                "   					\"\\ `*`\\ YourDatumName\",major_axis,flattening(or eccentricity)[,prime_meridian]\n"
                "   \n"
                "   					where\n"
                "   					The \\ `*`\\  before \"YourDatumName\" indicates this is a non-EPSG name.\n"
                "   					major_axis is in metres.\n"
                "   					flattening less than 0 is interpreted as eccentricity (0 indicates a sphere).\n"
                "   					prime_meridian is optional, specified in degrees of longitude relative to\n"
                "   					Greenwich.\n"
                "   \n"
                "   					The \"Projection\" can contain a projection system defined in the\n"
                "   					\"transform.csv\" file, or the name of a projection type followed by projection\n"
                "   					parameters.  Geographic coordinates systems (long/lat only) must leave\n"
                "   					\"projection\" blank.\n"
                "   \n"
                "   					Projection names not defined in \"transform.csv\" can be defined in the\n"
                "   					\"projection\" string as follows:\n"
                "   \n"
                "   					method,length_units,P1,P2,...\n"
                "   \n"
                "   					where:\n"
                "   \n"
                "   					\"method\" is a method from the table \"transform_parameters.csv\".\n"
                "   					\"length_units\" is a \"Unit_length\" from units.csv.\n"
                "   					P1 through P8 (or fewer) are the projection parameters for the method\n"
                "   					as defined in \"transform_parameters.csv\", and in the order defined.\n"
                "   					Parameters that are blank in \"transform_parameters.csv\" are omitted\n"
                "   					from the list so that each method will have a minimum list of\n"
                "   					parameters.\n"
                "   \n"
                "   					Angular parameters must always be degrees, and may be defined a\n"
                "   					decimal degree fromat, or \"DEG.MM.SS.ssss\".\n"
                "   					Distance parameters (False Northing and False Easting) must be\n"
                "   					defined in the \"length_units\" (string 4).\n"
                "   \n"
                "   					Examples:\n"
                "   \n"
                "   					Geographic long,lat on datum \"Arc 1960\":\n"
                "   					\"4210\",\"\",\"\",\"\",\"\"\n"
                "   					\"Arc 1960\",\"\",\"\",\"\",\"\"\n"
                "   					\"\",\"Arc 1960\",\"\",\"\",\"\"\n"
                "   \n"
                "   					Projected Coordinate System, UTM zone 37S\n"
                "   					\"21037\",\"\",\"\",\"\",\"\"\n"
                "   					\"\",\"4210\",\"16137\",\"\",\"\"\n"
                "   					\"\"Arc 1960 / UTM zone 37S\"\",\"\",\"\",\"\",\"\"\n"
                "   					\"\",\"\"Arc 1960\"\",\"UTM zone 37S\",\"\",\"\"\n"
                "   					\"\",\"\"Arc 1960\"\",\"UTM zone 37S\",\"m\",\"\"\n"
                "   					\"\",\"\"Arc 1960\"\",\"UTM zone 37S\",\"m,1.0\",\"\"\n"
                "   					\"\",\"\"Arc 1960\"\",\"UTM zone 37S\",\"m,1.0\",\"\");\n"
                "   					\"\",\"\"Arc 1960\"\",\"UTM zone 37S\",\"m\",\"Arc 1960 to WGS 84 (1)\"\n"
                "   \n"
                "   					Locally oriented coordinate system (origin at 525000,2500000, rotated 15 deg):\n"
                "   					\"21037<525000,2500000,0,0,0,15>\",\"\",\"\",\"\",\"\"\n"
                "   					\"<525000,2500000,0,0,0,15>\",\"4210\",\"16137\",\"\",\"\"\n"
                "   					\"\"Arc 1960 / UTM zone 37S\"<525000,2500000,0,0,0,15>\",\"\",\"\",\"\",\"\"\n"
                "   				\n\n"
               );
    pyClass.def("set_method_parm", &GXIPJ_wrap_set_method_parm,
                "set_method_parm((int)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set projection method parameter\n\n"

                ":param arg1: \\ :ref:`IPJ_CSP`\\ \n"
                ":type arg1: int\n"
                ":param arg2: parameter value\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If parameter is not valid, nothing happens.\n\n"
               );
    pyClass.def("set_mi_coord_sys", &GXIPJ_wrap_set_mi_coord_sys,
                "set_mi_coord_sys((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set coordinate system from a MapInfo coordsys command\n\n"

                ":param arg1: MapInfo Coordinate System\n"
                ":type arg1: str\n"
                ":param arg2: MapInfo Units\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.4\n\n"
               );
    pyClass.def("set_normal_section_view", &GXIPJ_wrap_set_normal_section_view,
                "set_normal_section_view((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set normal section orientation parameters\n\n"

                ":param arg1: X location of view origin\n"
                ":type arg1: float\n"
                ":param arg2: Y location of view origin\n"
                ":type arg2: float\n"
                ":param arg3: Z location of view origin\n"
                ":type arg3: float\n"
                ":param arg4: Section azimuth - degrees CCW from north\n"
                ":type arg4: float\n"
                ":param arg5: Section swing -90 < swing < 90.\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This section is the type where values are projected\n"
                "   					normal to the section, and the \"Y\" values in a grid\n"
                "   					do not necessarily correspond to the elvations for a swung section.\n"
                "   				\n\n"
               );
    pyClass.def("set_plan_view", &GXIPJ_wrap_set_plan_view,
                "set_plan_view((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set plan orientation parameters.\n\n"

                ":param arg1: X location of view origin\n"
                ":type arg1: float\n"
                ":param arg2: Y location of view origin\n"
                ":type arg2: float\n"
                ":param arg3: Z location of view origin\n"
                ":type arg3: float\n"
                ":param arg4: rotation CCW from normal XY coords\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This sets up the orientation of an IPJ for plan view plots,\n"
                "   					for instance in Wholeplot. These differ from regular plan\n"
                "   					map views in that the elevation of the view plane is set, and\n"
                "   					the view may be rotated. In addition, when viewed in a map,\n"
                "   					a view with this IPJ will give a status bar location (X, Y, Z)\n"
                "   					of the actual location in space, as opposed to just the X, Y of\n"
                "   					the view plane itself.\n"
                "   				\n\n"
               );
    pyClass.def("set_section_view", &GXIPJ_wrap_set_section_view,
                "set_section_view((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set section orientation parameters\n\n"

                ":param arg1: X location of view origin\n"
                ":type arg1: float\n"
                ":param arg2: Y location of view origin\n"
                ":type arg2: float\n"
                ":param arg3: Z location of view origin\n"
                ":type arg3: float\n"
                ":param arg4: Section azimuth - degrees CCW from north\n"
                ":type arg4: float\n"
                ":param arg5: Section swing -90 < swing < 90.\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This sets up the orientation of an IPJ for section view plots,\n"
                "   					for instance in Wholeplot. In addition, when viewed in a map,\n"
                "   					a view with this IPJ will give a status bar location (X, Y, Z)\n"
                "   					of the actual location in space, as opposed to just the X, Y of\n"
                "   					the view plane itself.\n"
                "   					Swung sections are tricky because they are set up for section\n"
                "   					plots in such a way that the vertical axis remains \"true\"; points\n"
                "   					are projected horizontally to the viewing plane, independent of the\n"
                "   					swing angle. In other words, all locations in 3D space viewed using this\n"
                "   					projection will plot on the same horizontal line in the map view.\n"
                "   					This function is NOT suitable for simply creating\n"
                "   					an orientation for a dipping grid or view.\n"
                "   				\n\n"
               );
    pyClass.def("set_wms_coord_sys", &GXIPJ_wrap_set_wms_coord_sys,
                "set_wms_coord_sys((str)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set coordinate system from a WMS coordsys string.\n\n"

                ":param arg1: WMS style coordinate string\n"
                ":type arg1: str\n"
                ":param arg2: minimum X bounding box\n"
                ":type arg2: float\n"
                ":param arg3: minimum Y\n"
                ":type arg3: float\n"
                ":param arg4: maximum X\n"
                ":type arg4: float\n"
                ":param arg5: maximum Y\n"
                ":type arg5: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					WMS coordinate strings supported:\n"
                "   \n"
                "   \n"
                "   					EPSG:code\n"
                "   \n"
                "   					where \"code\" is the EPSG code number\n"
                "   					\"EPSG:4326\"  is geographic \"WGS 84\" (see datum.csv)\n"
                "   					\"EPSG:25834\" is projected \"ETRS89 / UTM zone 34N\"\n"
                "   					(see ipj_pcs.csv)\n"
                "   \n"
                "   					The bounding box for EPSG systems must be defined in the\n"
                "   					EPSG coordinate system.  If a bounding box is provided,\n"
                "   					it will not be changed.\n"
                "   \n"
                "   \n"
                "   					AUTO:wm_id,epsg_units,lon,lat (see OGC documentation)\n"
                "   \n"
                "   					for \"AUTO\" coordinates, the \"epsg_units\" is the units\n"
                "   					of the bounding box.  This procedure will transform\n"
                "   					the supplied bounding box from these units to the\n"
                "   					units of the projection.  Normally, this is from\n"
                "   					long/lat (9102) to metres (9001).\n"
                "   				\n\n"
               );
    pyClass.def("set_xml", &GXIPJ_wrap_set_xml,
                "set_xml((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set an IPJ from a Geosoft Metadata XML string\n\n"

                ":param arg1: XML string to set\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("get_3d_matrix_orientation", &GXIPJ_wrap_get_3d_matrix_orientation,
                "get_3d_matrix_orientation((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9, (float_ref)arg10, (float_ref)arg11, (float_ref)arg12, (float_ref)arg13, (float_ref)arg14, (float_ref)arg15, (float_ref)arg16) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the coefficients of a 3D matrix orientation.\n\n"

                ":param arg1: Row 0 Element 0\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Row 0 Element 1\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Row 0 Element 2\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Row 0 Element 3\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Row 1 Element 0\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Row 1 Element 1\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Row 1 Element 2\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Row 1 Element 3\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Row 2 Element 0\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg10: Row 2 Element 1\n"
                ":type arg10: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg11: Row 2 Element 2\n"
                ":type arg11: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg12: Row 2 Element 3\n"
                ":type arg12: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg13: Row 3 Element 0\n"
                ":type arg13: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg14: Row 3 Element 1\n"
                ":type arg14: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg15: Row 3 Element 2\n"
                ":type arg15: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg16: Row 3 Element 3\n"
                ":type arg16: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               );
    pyClass.def("set_3d_matrix_orientation", &GXIPJ_wrap_set_3d_matrix_orientation,
                "set_3d_matrix_orientation((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (float)arg11, (float)arg12, (float)arg13, (float)arg14, (float)arg15, (float)arg16) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply a 3D orientation directly using matrix coefficients.\n\n"

                ":param arg1: Row 0 Element 0\n"
                ":type arg1: float\n"
                ":param arg2: Row 0 Element 1\n"
                ":type arg2: float\n"
                ":param arg3: Row 0 Element 2\n"
                ":type arg3: float\n"
                ":param arg4: Row 0 Element 3\n"
                ":type arg4: float\n"
                ":param arg5: Row 1 Element 0\n"
                ":type arg5: float\n"
                ":param arg6: Row 1 Element 1\n"
                ":type arg6: float\n"
                ":param arg7: Row 1 Element 2\n"
                ":type arg7: float\n"
                ":param arg8: Row 1 Element 3\n"
                ":type arg8: float\n"
                ":param arg9: Row 2 Element 0\n"
                ":type arg9: float\n"
                ":param arg10: Row 2 Element 1\n"
                ":type arg10: float\n"
                ":param arg11: Row 2 Element 2\n"
                ":type arg11: float\n"
                ":param arg12: Row 2 Element 3\n"
                ":type arg12: float\n"
                ":param arg13: Row 3 Element 0\n"
                ":type arg13: float\n"
                ":param arg14: Row 3 Element 1\n"
                ":type arg14: float\n"
                ":param arg15: Row 3 Element 2\n"
                ":type arg15: float\n"
                ":param arg16: Row 3 Element 3\n"
                ":type arg16: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               );
    pyClass.def("reproject_section_grid", &GXIPJ_wrap_reproject_section_grid,
                "reproject_section_grid((GXIPJ)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reproject a section grid\n\n"

                ":param arg1: Reprojected IPJ on input (need not include an orientation). On output contains the same\n"
                "             						type of orientation as the initial IPJ, adjusted to be in the same location.\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: X origin of grid (input initial value, output new value)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y origin of grid (input initial value, output new value)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: X cell size of grid (input initial value, output new value)\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Y cell size of grid (input initial value, output new value)\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Grid rotation (degrees CCW) (input initial value, output new value)\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Reproject a section grid to a new IPJ, adjusting its orientation and registration so that\n"
                "   					it remains in the same location.\n"
                "   				\n\n"
               );

    scope().attr("IPJ_3D_FLAG_NONE") = (int32_t)0;
    scope().attr("IPJ_3D_FLAG_INVERTANGLES") = (int32_t)1;
    scope().attr("IPJ_3D_FLAG_INVERTZ") = (int32_t)2;
    scope().attr("IPJ_3D_FLAG_ORDER_ROTATION") = (int32_t)4;
    scope().attr("IPJ_3D_ROTATE_DEFAULT") = (int32_t)0;
    scope().attr("IPJ_3D_ROTATE_XYZ") = (int32_t)1;
    scope().attr("IPJ_3D_ROTATE_XZY") = (int32_t)2;
    scope().attr("IPJ_3D_ROTATE_YXZ") = (int32_t)3;
    scope().attr("IPJ_3D_ROTATE_YZX") = (int32_t)4;
    scope().attr("IPJ_3D_ROTATE_ZXY") = (int32_t)5;
    scope().attr("IPJ_3D_ROTATE_ZYX") = (int32_t)6;
    scope().attr("IPJ_CSP_SCALE") = (int32_t)0;
    scope().attr("IPJ_CSP_FALSEEAST") = (int32_t)1;
    scope().attr("IPJ_CSP_FALSENORTH") = (int32_t)2;
    scope().attr("IPJ_CSP_LATORIGIN") = (int32_t)3;
    scope().attr("IPJ_CSP_LONORIGIN") = (int32_t)4;
    scope().attr("IPJ_CSP_PARALLEL_1") = (int32_t)5;
    scope().attr("IPJ_CSP_PARALLEL_2") = (int32_t)6;
    scope().attr("IPJ_CSP_AZIMUTH") = (int32_t)7;
    scope().attr("IPJ_CSP_ANGLE") = (int32_t)8;
    scope().attr("IPJ_CSP_POINTLAT_1") = (int32_t)9;
    scope().attr("IPJ_CSP_POINTLON_1") = (int32_t)10;
    scope().attr("IPJ_CSP_POINTLAT_2") = (int32_t)11;
    scope().attr("IPJ_CSP_POINTLON_2") = (int32_t)12;
    scope().attr("IPJ_NAME_PCS") = (int32_t)0;
    scope().attr("IPJ_NAME_PROJECTION") = (int32_t)1;
    scope().attr("IPJ_NAME_METHOD") = (int32_t)2;
    scope().attr("IPJ_NAME_DATUM") = (int32_t)3;
    scope().attr("IPJ_NAME_ELLIPSOID") = (int32_t)4;
    scope().attr("IPJ_NAME_LDATUM") = (int32_t)5;
    scope().attr("IPJ_NAME_UNIT_ABBR") = (int32_t)6;
    scope().attr("IPJ_NAME_UNIT_FULL") = (int32_t)7;
    scope().attr("IPJ_NAME_TYPE") = (int32_t)8;
    scope().attr("IPJ_NAME_LLDATUM") = (int32_t)9;
    scope().attr("IPJ_NAME_METHOD_PARMS") = (int32_t)10;
    scope().attr("IPJ_NAME_METHOD_LABEL") = (int32_t)11;
    scope().attr("IPJ_NAME_DATUM_PARMS") = (int32_t)12;
    scope().attr("IPJ_NAME_LDATUM_PARMS") = (int32_t)13;
    scope().attr("IPJ_NAME_GEOID") = (int32_t)14;
    scope().attr("IPJ_NAME_LDATUMDESCRIPTION") = (int32_t)15;
    scope().attr("IPJ_NAME_METHOD_PARMS_NATIVE") = (int32_t)16;
    scope().attr("IPJ_NAME_ORIENTATION_PARMS") = (int32_t)17;
    scope().attr("IPJ_ORIENT_DEFAULT") = (int32_t)0;
    scope().attr("IPJ_ORIENT_PLAN") = (int32_t)1;
    scope().attr("IPJ_ORIENT_SECTION") = (int32_t)2;
    scope().attr("IPJ_ORIENT_SECTION_NORMAL") = (int32_t)5;
    scope().attr("IPJ_ORIENT_DEPTH_SECTION") = (int32_t)3;
    scope().attr("IPJ_ORIENT_3D") = (int32_t)4;
    scope().attr("IPJ_ORIENT_3D_MATRIX") = (int32_t)7;
    scope().attr("IPJ_ORIENT_SECTION_CROOKED") = (int32_t)6;
    scope().attr("IPJ_PARM_LST_COORDINATESYSTEM") = (int32_t)0;
    scope().attr("IPJ_PARM_LST_DATUM") = (int32_t)1;
    scope().attr("IPJ_PARM_LST_PROJECTION") = (int32_t)2;
    scope().attr("IPJ_PARM_LST_UNITS") = (int32_t)3;
    scope().attr("IPJ_PARM_LST_LOCALDATUMDESCRIPTION") = (int32_t)4;
    scope().attr("IPJ_PARM_LST_LOCALDATUMNAME") = (int32_t)5;
    scope().attr("IPJ_PARM_LST_UNITSDESCRIPTION") = (int32_t)6;
    scope().attr("IPJ_TYPE_PRJ") = (int32_t)0;
    scope().attr("IPJ_TYPE_PCS") = (int32_t)1;
    scope().attr("IPJ_TYPE_GCS") = (int32_t)2;
    scope().attr("IPJ_TYPE_ANY") = (int32_t)3;
    scope().attr("IPJ_TYPE_NONE") = (int32_t)4;
    scope().attr("IPJ_TYPE_WRP") = (int32_t)5;
    scope().attr("IPJ_TYPE_TEST") = (int32_t)6;
    scope().attr("IPJ_UNIT_ABBREVIATION") = (int32_t)0;
    scope().attr("IPJ_UNIT_FULLNAME") = (int32_t)1;
    scope().attr("IPJ_WARP_MATRIX") = (int32_t)-1;
    scope().attr("IPJ_WARP_NONE") = (int32_t)0;
    scope().attr("IPJ_WARP_TRANS1") = (int32_t)1;
    scope().attr("IPJ_WARP_TRANS2") = (int32_t)2;
    scope().attr("IPJ_WARP_TRANS3") = (int32_t)3;
    scope().attr("IPJ_WARP_QUAD") = (int32_t)4;
    scope().attr("IPJ_WARP_MULTIPOINT") = (int32_t)5;
    scope().attr("IPJ_WARP_LOG") = (int32_t)6;
    scope().attr("IPJ_WARP_MULTIPOINT_Y") = (int32_t)7;

}
