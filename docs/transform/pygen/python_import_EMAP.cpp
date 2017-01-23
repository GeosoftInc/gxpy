#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXEMAP_wrap_drop_map_clip_data(GXEMAPPtr self, int32_t arg1)
{
    self->drop_map_clip_data(arg1);
}
inline bool GXEMAP_wrap_drag_drop_enabled(GXEMAPPtr self)
{
    bool ret = self->drag_drop_enabled();
    return ret;
}
inline void GXEMAP_wrap_set_drag_drop_enabled(GXEMAPPtr self, bool arg1)
{
    self->set_drag_drop_enabled(arg1);
}
inline void GXEMAP_wrap_copy_to_clip(GXEMAPPtr self)
{
    self->copy_to_clip();
}
inline void GXEMAP_wrap_draw_line(GXEMAPPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->draw_line(arg1, arg2, arg3, arg4);
}
inline void GXEMAP_wrap_draw_rect(GXEMAPPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->draw_rect(arg1, arg2, arg3, arg4);
}
inline void GXEMAP_wrap_draw_rect_3d(GXEMAPPtr self, double arg1, double arg2, double arg3, int32_t arg4)
{
    self->draw_rect_3d(arg1, arg2, arg3, arg4);
}
inline void GXEMAP_wrap_get_display_area(GXEMAPPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4)
{
    self->get_display_area(arg1, arg2, arg3, arg4);
}
inline void GXEMAP_wrap_get_display_area_raw(GXEMAPPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4)
{
    self->get_display_area_raw(arg1, arg2, arg3, arg4);
}
inline void GXEMAP_wrap_get_map_layout_props(GXEMAPPtr self, bool_ref& arg1, float_ref& arg2, int_ref& arg3, int_ref& arg4, int_ref& arg5, int_ref& arg6, int_ref& arg7, int_ref& arg8)
{
    self->get_map_layout_props(arg1, arg2, arg3, arg4, (LAYOUT_VIEW_UNITS&)arg5, arg6, arg7, arg8);
}
inline void GXEMAP_wrap_get_map_snap(GXEMAPPtr self, float_ref& arg1)
{
    self->get_map_snap(arg1);
}
inline int32_t GXEMAP_wrap_get_window_state(GXEMAPPtr self)
{
    EMAP_WINDOW_STATE ret = self->get_window_state();
    return ret;
}
inline void GXEMAP_wrap_set_display_area(GXEMAPPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->set_display_area(arg1, arg2, arg3, arg4);
}
inline void GXEMAP_wrap_set_map_layout_props(GXEMAPPtr self, bool arg1, double arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7, int32_t arg8)
{
    self->set_map_layout_props(arg1, arg2, arg3, arg4, (LAYOUT_VIEW_UNITS)arg5, arg6, arg7, arg8);
}
inline void GXEMAP_wrap_set_map_snap(GXEMAPPtr self, double arg1)
{
    self->set_map_snap(arg1);
}
inline void GXEMAP_wrap_set_window_state(GXEMAPPtr self, int32_t arg1)
{
    self->set_window_state((EMAP_WINDOW_STATE)arg1);
}
inline void GXEMAP_wrap_activate_group(GXEMAPPtr self, const gx_string_type& arg1)
{
    self->activate_group(arg1);
}
inline void GXEMAP_wrap_activate_view(GXEMAPPtr self, const gx_string_type& arg1)
{
    self->activate_view(arg1);
}
inline GXEMAPPtr GXEMAP_wrap_current()
{
    GXEMAPPtr ret = GXEMAP::current();
    return ret;
}
inline GXEMAPPtr GXEMAP_wrap_current_no_activate()
{
    GXEMAPPtr ret = GXEMAP::current_no_activate();
    return ret;
}
inline GXEMAPPtr GXEMAP_wrap_current_if_exists()
{
    GXEMAPPtr ret = GXEMAP::current_if_exists();
    return ret;
}
inline void GXEMAP_wrap_destroy_view(GXEMAPPtr self, int32_t arg1)
{
    self->destroy_view((EMAP_REMOVE)arg1);
}
inline void GXEMAP_wrap_font_lst(GXEMAPPtr self, GXLSTPtr arg1, int32_t arg2)
{
    self->font_lst(arg1, (EMAP_FONT)arg2);
}
inline int32_t GXEMAP_wrap_change_current_view(GXEMAPPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->change_current_view(arg1);
    return ret;
}
inline int32_t GXEMAP_wrap_create_group_snapshot(GXEMAPPtr self, GXLSTPtr arg1)
{
    int32_t ret = self->create_group_snapshot(arg1);
    return ret;
}
inline void GXEMAP_wrap_get_3d_view_name(GXEMAPPtr self, str_ref& arg1)
{
    self->get_3d_view_name(arg1);
}
inline void GXEMAP_wrap_get_current_group(GXEMAPPtr self, str_ref& arg1)
{
    self->get_current_group(arg1);
}
inline void GXEMAP_wrap_get_current_view(GXEMAPPtr self, str_ref& arg1)
{
    self->get_current_view(arg1);
}
inline int32_t GXEMAP_wrap_get_maps_lst(GXLSTPtr arg1, int32_t arg2)
{
    int32_t ret = GXEMAP::get_maps_lst(arg1, (EMAP_PATH)arg2);
    return ret;
}
inline void GXEMAP_wrap_get_name(GXEMAPPtr self, str_ref& arg1)
{
    self->get_name(arg1);
}
inline int32_t GXEMAP_wrap_have_current()
{
    int32_t ret = GXEMAP::have_current();
    return ret;
}
inline int32_t GXEMAP_wrap_i_get_specified_map_name(const gx_string_type& arg1, const gx_string_type& arg2, str_ref& arg3)
{
    int32_t ret = GXEMAP::i_get_specified_map_name(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXEMAP_wrap_is_grid(GXEMAPPtr self)
{
    int32_t ret = self->is_grid();
    return ret;
}
inline void GXEMAP_wrap_reload_grid(const gx_string_type& arg1)
{
    GXEMAP::reload_grid(arg1);
}
inline int32_t GXEMAP_wrap_is_3d_view(GXEMAPPtr self)
{
    int32_t ret = self->is_3d_view();
    return ret;
}
inline bool GXEMAP_wrap_is_locked(GXEMAPPtr self)
{
    bool ret = self->is_locked();
    return ret;
}
inline int32_t GXEMAP_wrap_loaded(const gx_string_type& arg1)
{
    int32_t ret = GXEMAP::loaded(arg1);
    return ret;
}
inline bool GXEMAP_wrap_read_only(GXEMAPPtr self)
{
    bool ret = self->read_only();
    return ret;
}
inline void GXEMAP_wrap_get_window_position(GXEMAPPtr self, int_ref& arg1, int_ref& arg2, int_ref& arg3, int_ref& arg4, int_ref& arg5, int_ref& arg6)
{
    self->get_window_position(arg1, arg2, arg3, arg4, (EMAP_WINDOW_STATE&)arg5, (EMAP_WINDOW_POSITION&)arg6);
}
inline void GXEMAP_wrap_set_window_position(GXEMAPPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    self->set_window_position(arg1, arg2, arg3, arg4, (EMAP_WINDOW_STATE)arg5, (EMAP_WINDOW_POSITION)arg6);
}
inline int32_t GXEMAP_wrap_doubleize_group_snapshot(GXEMAPPtr self, GXLSTPtr arg1)
{
    int32_t ret = self->doubleize_group_snapshot(arg1);
    return ret;
}
inline int32_t GXEMAP_wrap_set_current_view(GXEMAPPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->set_current_view(arg1);
    return ret;
}
inline void GXEMAP_wrap_get_view_ipj(GXEMAPPtr self, const gx_string_type& arg1, GXIPJPtr arg2)
{
    self->get_view_ipj(arg1, arg2);
}
inline GXEMAPPtr GXEMAP_wrap_load(const gx_string_type& arg1)
{
    GXEMAPPtr ret = GXEMAP::load(arg1);
    return ret;
}
inline GXEMAPPtr GXEMAP_wrap_load_no_activate(const gx_string_type& arg1)
{
    GXEMAPPtr ret = GXEMAP::load_no_activate(arg1);
    return ret;
}
inline GXEMAPPtr GXEMAP_wrap_load_with_view(const gx_string_type& arg1, GXEMAPPtr arg2)
{
    GXEMAPPtr ret = GXEMAP::load_with_view(arg1, arg2);
    return ret;
}
inline GXMAPPtr GXEMAP_wrap_lock(GXEMAPPtr self)
{
    GXMAPPtr ret = self->lock();
    return ret;
}
inline void GXEMAP_wrap_make_current(GXEMAPPtr self)
{
    self->make_current();
}
inline void GXEMAP_wrap_print(GXEMAPPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7, int32_t arg8, double arg9, int32_t arg10, int32_t arg11, int32_t arg12, const gx_string_type& arg13)
{
    self->print(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13);
}
inline void GXEMAP_wrap_redraw(GXEMAPPtr self)
{
    self->redraw();
}
inline void GXEMAP_wrap_select_group(GXEMAPPtr self, const gx_string_type& arg1)
{
    self->select_group(arg1);
}
inline void GXEMAP_wrap_set_redraw_flag(GXEMAPPtr self, int32_t arg1)
{
    self->set_redraw_flag((EMAP_REDRAW)arg1);
}
inline void GXEMAP_wrap_un_load(const gx_string_type& arg1)
{
    GXEMAP::un_load(arg1);
}
inline void GXEMAP_wrap_un_load_all()
{
    GXEMAP::un_load_all();
}
inline void GXEMAP_wrap_un_load_verify(const gx_string_type& arg1, bool arg2)
{
    GXEMAP::un_load_verify(arg1, arg2);
}
inline void GXEMAP_wrap_un_lock(GXEMAPPtr self)
{
    self->un_lock();
}
inline void GXEMAP_wrap_get_cur_point(GXEMAPPtr self, float_ref& arg1, float_ref& arg2)
{
    self->get_cur_point(arg1, arg2);
}
inline void GXEMAP_wrap_get_cur_point_mm(GXEMAPPtr self, float_ref& arg1, float_ref& arg2)
{
    self->get_cur_point_mm(arg1, arg2);
}
inline void GXEMAP_wrap_get_cursor(GXEMAPPtr self, float_ref& arg1, float_ref& arg2)
{
    self->get_cursor(arg1, arg2);
}
inline void GXEMAP_wrap_get_cursor_mm(GXEMAPPtr self, float_ref& arg1, float_ref& arg2)
{
    self->get_cursor_mm(arg1, arg2);
}
inline int32_t GXEMAP_wrap_digitize(GXEMAPPtr self, GXWAPtr arg1, GXIMGPtr arg2, int32_t arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6, int32_t arg7)
{
    int32_t ret = self->digitize(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
    return ret;
}
inline int32_t GXEMAP_wrap_digitize2(GXEMAPPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXIMGPtr arg4, const gx_string_type& arg5, int32_t arg6)
{
    int32_t ret = self->digitize2(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline int32_t GXEMAP_wrap_digitize_peaks(GXEMAPPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXIMGPtr arg4, const gx_string_type& arg5, int32_t arg6)
{
    int32_t ret = self->digitize_peaks(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline int32_t GXEMAP_wrap_digitize_polygon(GXEMAPPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXIMGPtr arg4, const gx_string_type& arg5, int32_t arg6, int32_t arg7)
{
    int32_t ret = self->digitize_polygon(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
    return ret;
}
inline int32_t GXEMAP_wrap_get_box(GXEMAPPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    int32_t ret = self->get_box(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline int32_t GXEMAP_wrap_get_box2(GXEMAPPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8, float_ref& arg9)
{
    int32_t ret = self->get_box2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
    return ret;
}
inline int32_t GXEMAP_wrap_get_grid(GXEMAPPtr self, const gx_string_type& arg1, int32_t arg2, int32_t arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7, float_ref& arg8)
{
    int32_t ret = self->get_grid(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
    return ret;
}
inline int32_t GXEMAP_wrap_get_line(GXEMAPPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    int32_t ret = self->get_line(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline int32_t GXEMAP_wrap_get_line_ex(GXEMAPPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    int32_t ret = self->get_line_ex(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline int32_t GXEMAP_wrap_get_line_xyz(GXEMAPPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6, float_ref& arg7)
{
    int32_t ret = self->get_line_xyz(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
    return ret;
}
inline int32_t GXEMAP_wrap_get_point(GXEMAPPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3)
{
    int32_t ret = self->get_point(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXEMAP_wrap_get_point_ex(GXEMAPPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3)
{
    int32_t ret = self->get_point_ex(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXEMAP_wrap_get_point_3d(GXEMAPPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4)
{
    int32_t ret = self->get_point_3d(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXEMAP_wrap_get_poly_line(GXEMAPPtr self, const gx_string_type& arg1, GXVVPtr arg2, GXVVPtr arg3)
{
    int32_t ret = self->get_poly_line(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXEMAP_wrap_get_poly_line_xyz(GXEMAPPtr self, const gx_string_type& arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4)
{
    int32_t ret = self->get_poly_line_xyz(arg1, arg2, arg3, arg4);
    return ret;
}
inline int32_t GXEMAP_wrap_get_rect(GXEMAPPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    int32_t ret = self->get_rect(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline int32_t GXEMAP_wrap_track_point(GXEMAPPtr self, int32_t arg1, float_ref& arg2, float_ref& arg3)
{
    int32_t ret = self->track_point((EMAP_TRACK)arg1, arg2, arg3);
    return ret;
}
inline void GXEMAP_wrap_get_aoi_area(GXEMAPPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4)
{
    self->get_aoi_area(arg1, arg2, arg3, arg4);
}
inline void GXEMAP_wrap_set_aoi_area(GXEMAPPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->set_aoi_area(arg1, arg2, arg3, arg4);
}
inline void GXEMAP_wrap_set_viewport_mode(GXEMAPPtr self, int32_t arg1)
{
    self->set_viewport_mode((EMAP_VIEWPORT)arg1);
}
inline void GXEMAP_wrap_get_selected_vertices(GXEMAPPtr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->get_selected_vertices(arg1, arg2);
}
inline GXEMAPPtr GXEMAP_wrap_create_virtual(const gx_string_type& arg1)
{
    GXEMAPPtr ret = GXEMAP::create_virtual(arg1);
    return ret;
}

void gxPythonImportGXEMAP()
{

    class_<GXEMAP, GXEMAPPtr> pyClass("GXEMAP",
                                      "\n.. parsed-literal::\n\n"
                                      "   \n"
                                      "   		The EMAP class provides access to a map as displayed within\n"
                                      "   		Oasis montaj, but (usually) does not change data within the map itself.\n"
                                      "   		It performs functions such as setting the currently displayed area,\n"
                                      "   		or drawing \"tracking\" lines or boxes on the map (which are not\n"
                                      "   		part of the map itself).\n"
                                      "   	\n\n"

                                      "\n\n**Note:**\n\n"

                                      "\n.. parsed-literal::\n\n"
                                      "   \n"
                                      "   		To obtain access to the map itself, it is recommended practice\n"
                                      "   		to begin with an EMAP object, and use the \\ :func:`geosoft.gxapi.GXEMAP.lock`\\  function to\n"
                                      "   		lock the underlying map to prevent external changes. The returned\n"
                                      "   		MAP object (see MAP.GXH) may then be safely used to make changes to the map itself.\n"
                                      "   \n"
                                      "   		MAP Redraw Rules:\n"
                                      "   \n"
                                      "   		1. Redraws only occur at the end of the proccess (GX or SCRIPT) not during.\n"
                                      "   		You can safely call other GX's and the map will not redraw. If you need the\n"
                                      "   		map to redraw immediately use \\ :func:`geosoft.gxapi.GXEMAP.redraw`\\  instead.\n"
                                      "   \n"
                                      "   		2. If the final GX calls \\ :func:`geosoft.gxapi.GXSYS.cancel`\\ , the map redraw is not done. If you\n"
                                      "   		need to force a redraw when the user hits cancel use the \\ :func:`geosoft.gxapi.GXEMAP.redraw`\\  function.\n"
                                      "   \n"
                                      "   		3. You can set the redraw flag to EMAP_REDRAW_YES or EMAP_REDRAW_NO at any\n"
                                      "   		time using \\ :func:`geosoft.gxapi.GXEMAP.set_redraw_flag`\\ . This flag will only be looked at, when\n"
                                      "   		the last call to \\ :func:`geosoft.gxapi.GXEMAP.un_lock`\\  occurs and is ignored on a \\ :func:`geosoft.gxapi.GXSYS.cancel`\\ .\n"
                                      "   \n"
                                      "   		4. \\ :func:`geosoft.gxapi.GXEMAP.redraw`\\  only works if the current map is not locked. It will do nothing\n"
                                      "   		if the map is locked.  Issue an \\ :func:`geosoft.gxapi.GXEMAP.un_lock`\\  before using this function.\n"
                                      "   \n"
                                      "   \n"
                                      "   		VIRTUAL EMAP SUPPORT\n"
                                      "   \n"
                                      "   		These methods are only available when running in an external application.\n"
                                      "   		They allow the GX to open a MAP and then create a Virtual EMAP from that\n"
                                      "   		map. The GX can then call \\ :func:`geosoft.gxapi.GXEMAP.make_current`\\  and set the current EMAP so\n"
                                      "   		that code that follows sees this map as the current MAP.\n"
                                      "   \n"
                                      "   		Supported methods on Virtual EMAPS are:\n"
                                      "   \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.current`\\ \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.current_no_activate`\\ \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.make_current`\\ \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.have_current`\\ \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.current_if_exists`\\ \n"
                                      "   		\\ :func:`geosoft.gxapi.GXMAP.current`\\ \n"
                                      "   \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.lock`\\ \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.un_lock`\\ \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.is_locked`\\ \n"
                                      "   \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.get_name`\\ \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.set_redraw_flag`\\ \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.redraw`\\ \n"
                                      "   \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.loaded`\\ \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.load`\\ \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.load_no_activate`\\ \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.un_load_verify`\\ \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.un_load`\\ \n"
                                      "   \n"
                                      "   		\\ :func:`geosoft.gxapi.GXEMAP.create_virtual`\\ \n"
                                      "   	\n\n"
                                      , no_init);

    pyClass.def("null", &GXEMAP::null, "null() -> GXEMAP\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXEMAP`\n\n:returns: A null :class:`geosoft.gxapi.GXEMAP`\n:rtype: :class:`geosoft.gxapi.GXEMAP`\n").staticmethod("null");
    pyClass.def("is_null", &GXEMAP::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXEMAP is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXEMAP`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXEMAP::_internal_handle);
    pyClass.def("drop_map_clip_data", &GXEMAP_wrap_drop_map_clip_data,
                "drop_map_clip_data((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Drop Map clipboard data on this EMAP\n\n"

                ":param arg1: Handle to Global Clipboard data\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("drag_drop_enabled", &GXEMAP_wrap_drag_drop_enabled,
                "drag_drop_enabled() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Is drag-and-drop enabled for the map?\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_drag_drop_enabled", &GXEMAP_wrap_set_drag_drop_enabled,
                "set_drag_drop_enabled((bool)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set whether drag-and-drop is enabled for the map.\n\n"

                ":param arg1: Enables/disables drag-and-drop bool\n"
                ":type arg1: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("copy_to_clip", &GXEMAP_wrap_copy_to_clip,
                "copy_to_clip() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy entire map to clipboard.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Four objects are placed on the clipboard:\n"
                "   \n"
                "   					1. Georefernce Text\n"
                "   					2. Bitmap of current window screen resolution\n"
                "   					3. EMF of current window screen resolution\n"
                "   					4. Entire map as a Geosoft View (go to view mode\n"
                "   					and hit paste). The coordinates are placed\n"
                "   					in the current view coordinates.\n"
                "   				\n\n"
               );
    pyClass.def("draw_line", &GXEMAP_wrap_draw_line,
                "draw_line((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draws a line on the current map.\n\n"

                ":param arg1: X1\n"
                ":type arg1: float\n"
                ":param arg2: Y1\n"
                ":type arg2: float\n"
                ":param arg3: X2\n"
                ":type arg3: float\n"
                ":param arg4: Y2\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Locations are in the current view user units.\n"
                "   \n"
                "   					The line is temporary and will disappear on the next\n"
                "   					screen refresh.  This function is for you to provide\n"
                "   					interactive screen feedback to your user.\n"
                "   				\n\n"
               );
    pyClass.def("draw_rect", &GXEMAP_wrap_draw_rect,
                "draw_rect((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draws a rect on the current map.\n\n"

                ":param arg1: X1\n"
                ":type arg1: float\n"
                ":param arg2: Y1\n"
                ":type arg2: float\n"
                ":param arg3: X2\n"
                ":type arg3: float\n"
                ":param arg4: Y2\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Locations are in the current view user units.\n"
                "   \n"
                "   					The line is temporary and will disappear on the next\n"
                "   					screen refresh.  This function is for you to provide\n"
                "   					interactive screen feedback to your user.\n"
                "   				\n\n"
               );
    pyClass.def("draw_rect_3d", &GXEMAP_wrap_draw_rect_3d,
                "draw_rect_3d((float)arg1, (float)arg2, (float)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot a square symbol on a section view.\n\n"

                ":param arg1: X - True X location\n"
                ":type arg1: float\n"
                ":param arg2: Y - True Y location\n"
                ":type arg2: float\n"
                ":param arg3: Z - True Z location\n"
                ":type arg3: float\n"
                ":param arg4: Size in pixels (\"radius\")\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Plot a square symbol on a section view, but input 3D user coordinates\n"
                "   \n"
                "   					The line is temporary and will disappear on the next\n"
                "   					screen refresh.  This function is for you to provide\n"
                "   					interactive screen feedback to your user.					\n"
                "   				\n\n"
               );
    pyClass.def("get_display_area", &GXEMAP_wrap_get_display_area,
                "get_display_area((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the area you are currently looking at.\n\n"

                ":param arg1: X Min returned\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y Min returned\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: X Max returned\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Y Max returned\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Coordinates are based on the current view units.\n"
                "   					For 3D views this will return the full map extents.\n"
                "   				\n\n"
               );
    pyClass.def("get_display_area_raw", &GXEMAP_wrap_get_display_area_raw,
                "get_display_area_raw((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the area you are currently looking at in raw map units\n\n"

                ":param arg1: X Min returned\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y Min returned\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: X Max returned\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Y Max returned\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Coordinates are in millimeters.\n"
                "   					For 3D views this will return the full map extents.\n"
                "   				\n\n"
               );
    pyClass.def("get_map_layout_props", &GXEMAP_wrap_get_map_layout_props,
                "get_map_layout_props((bool_ref)arg1, (float_ref)arg2, (int_ref)arg3, (int_ref)arg4, (int_ref)arg5, (int_ref)arg6, (int_ref)arg7, (int_ref)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the base layout view properties.\n\n"

                ":param arg1: bool Snap to grid\n"
                ":type arg1: :class:`geosoft.gxapi.bool_ref`\n"
                ":param arg2: Snapping distance (always in mm)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: View Grid\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: View Rulers\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: \\ :ref:`LAYOUT_VIEW_UNITS`\\  View Units\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Grid Red Component (0-255)\n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg7: Grid Green Component (0-255)\n"
                ":type arg7: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg8: Grid Blue Component (0-255)\n"
                ":type arg8: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This affects the display units and other related properties for the base\n"
                "   					view of a map.\n"
                "   				\n\n"
               );
    pyClass.def("get_map_snap", &GXEMAP_wrap_get_map_snap,
                "get_map_snap((float_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get current snapping distance in MM\n\n"

                ":param arg1: Snap value in MM (returned)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_window_state", &GXEMAP_wrap_get_window_state,
                "get_window_state() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve the current state of the map window\n\n"

                ":returns: \\ :ref:`EMAP_WINDOW_STATE`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_display_area", &GXEMAP_wrap_set_display_area,
                "set_display_area((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the area you wish to see.\n\n"

                ":param arg1: X Min\n"
                ":type arg1: float\n"
                ":param arg2: Y Min\n"
                ":type arg2: float\n"
                ":param arg3: X Max\n"
                ":type arg3: float\n"
                ":param arg4: Y Max\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Coordinates are based on the current view user units.\n"
                "   					The map is immediatly redrawn.\n"
                "   				\n\n"
               );
    pyClass.def("set_map_layout_props", &GXEMAP_wrap_set_map_layout_props,
                "set_map_layout_props((bool)arg1, (float)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the base layout view properties.\n\n"

                ":param arg1: bool Snap to grid\n"
                ":type arg1: bool\n"
                ":param arg2: Snapping distance (always in mm)\n"
                ":type arg2: float\n"
                ":param arg3: View Grid\n"
                ":type arg3: int\n"
                ":param arg4: View Rulers\n"
                ":type arg4: int\n"
                ":param arg5: \\ :ref:`LAYOUT_VIEW_UNITS`\\  View Units\n"
                ":type arg5: int\n"
                ":param arg6: Grid Red Component (0-255)\n"
                ":type arg6: int\n"
                ":param arg7: Grid Green Component (0-255)\n"
                ":type arg7: int\n"
                ":param arg8: Grid Blue Component (0-255)\n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This affects the display units and other related properties for the base\n"
                "   					view of a map.\n"
                "   				\n\n"
               );
    pyClass.def("set_map_snap", &GXEMAP_wrap_set_map_snap,
                "set_map_snap((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set current snapping distance in MM\n\n"

                ":param arg1: Snap value in MM\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_window_state", &GXEMAP_wrap_set_window_state,
                "set_window_state((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Changes the state of the map window\n\n"

                ":param arg1: \\ :ref:`EMAP_WINDOW_STATE`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("activate_group", &GXEMAP_wrap_activate_group,
                "activate_group((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Activates a group and associated tools.\n\n"

                ":param arg1: \"View/Group\"\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Activating a group basically enters the edit mode associated\n"
                "   					with the type of group. E.g. a vector group will enable the\n"
                "   					edit toolbar for that gorup and an AGG will bring up the\n"
                "   					image colour tool. Be sure to pass a combined name containing\n"
                "   					both the view name and the group separated by a \"/\" or \"\\\".\n"
                "   				\n\n"
               );
    pyClass.def("activate_view", &GXEMAP_wrap_activate_view,
                "activate_view((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Activates a view and associated tools.\n\n"

                ":param arg1: \"View\"\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("current", &GXEMAP_wrap_current,
                "current() -> GXEMAP:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the Current Edited map.\n\n"

                ":returns: EMAP Object\n"
                ":rtype: :class:`geosoft.gxapi.GXEMAP`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("current");
    pyClass.def("current_no_activate", &GXEMAP_wrap_current_no_activate,
                "current_no_activate() -> GXEMAP:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the Current Edited map.\n\n"

                ":returns: EMAP Object\n"
                ":rtype: :class:`geosoft.gxapi.GXEMAP`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function acts just like \\ :func:`geosoft.gxapi.GXEMAP.current`\\  except that the document is not activated (brought to foreground) and no\n"
                "   					guarantee is given about which document is currently active.\n"
                "   				\n\n"
               ).staticmethod("current_no_activate");
    pyClass.def("current_if_exists", &GXEMAP_wrap_current_if_exists,
                "current_if_exists() -> GXEMAP:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the Current Edited map.\n\n"

                ":returns: EMAP Object to current edited map. If there is no current map,\n"
                "          						the user is not prompted for a map, and 0 is returned.\n"
                ":rtype: :class:`geosoft.gxapi.GXEMAP`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("current_if_exists");
    pyClass.def("destroy_view", &GXEMAP_wrap_destroy_view,
                "destroy_view((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Removes the view from the workspace.\n\n"

                ":param arg1: \\ :ref:`EMAP_REMOVE`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Can only be run in interactive mode. After this call the\n"
                "   					EMAP object will become invalid. If this is the last view on\n"
                "   					the document and the document has been modified the map will be\n"
                "   					unloaded and optionally saved depending on the \\ :ref:`EMAP_REMOVE`\\ \n"
                "   					parameter.\n"
                "   				\n\n"
               );
    pyClass.def("font_lst", &GXEMAP_wrap_font_lst,
                "font_lst((GXLST)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   List all Windows and geosoft fonts.\n\n"

                ":param arg1: List Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`EMAP_FONT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					To get TT and GFN fonts, call twice with the same list\n"
                "   					and EMAP_FONT_TT, then EMAP_FONT_GFN, or vice-versa to\n"
                "   					change order of listing.\n"
                "   				\n\n"
               );
    pyClass.def("change_current_view", &GXEMAP_wrap_change_current_view,
                "change_current_view((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Change the current working view.\n\n"

                ":param arg1: view name\n"
                ":type arg1: str\n"
                ":returns: 0 if view set, 1 if view does not exist.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function operates on the current map.\n"
                "   					Unlike \\ :func:`geosoft.gxapi.GXEMAP.set_current_view`\\  this function's action\n"
                "   					survive the GX finishing.\n"
                "   				\n\n"
               );
    pyClass.def("create_group_snapshot", &GXEMAP_wrap_create_group_snapshot,
                "create_group_snapshot((GXLST)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Loads an LST with the current view/group names\n"
                "   					existing in a map. Typically used to track group\n"
                "   					changes that are about to occur.\n"
                "   				\n\n"

                ":param arg1: LST object to fill\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: 0 if LST filled properly\n"
                "          						1 if not\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_3d_view_name", &GXEMAP_wrap_get_3d_view_name,
                "get_3d_view_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the name of a 3D view if the current view is 3D.\n\n"

                ":param arg1: Name returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_current_group", &GXEMAP_wrap_get_current_group,
                "get_current_group((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the current group name.\n\n"

                ":param arg1: returned group name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function operates on the current map.\n\n"
               );
    pyClass.def("get_current_view", &GXEMAP_wrap_get_current_view,
                "get_current_view((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the current view name.\n\n"

                ":param arg1: returned view name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function operates on the current map.\n\n"
               );
    pyClass.def("get_maps_lst", &GXEMAP_wrap_get_maps_lst,
                "get_maps_lst((GXLST)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Load the file names of open maps into a LST.\n\n"

                ":param arg1: LST to load\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`EMAP_PATH`\\ \n"
                ":type arg2: int\n"
                ":returns: The number of documents loaded into the LST.\n"
                "          						The LST is cleared first.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_maps_lst");
    pyClass.def("get_name", &GXEMAP_wrap_get_name,
                "get_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the name of the map object of this EMAP.\n\n"

                ":param arg1: Name returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("have_current", &GXEMAP_wrap_have_current,
                "have_current() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns whether a current map is loaded\n\n"

                ":returns: 0 - no current map.\n"
                "          						1 - current map\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("have_current");
    pyClass.def("i_get_specified_map_name", &GXEMAP_wrap_i_get_specified_map_name,
                "i_get_specified_map_name((str)arg1, (str)arg2, (str_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Find a loaded map that has a setting in its reg.\n\n"

                ":param arg1: REG field name\n"
                ":type arg1: str\n"
                ":param arg2: REG field value to find\n"
                ":type arg2: str\n"
                ":param arg3: buffer for map name\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 - Ok\n"
                "          						1 - No Map Found\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("i_get_specified_map_name");
    pyClass.def("is_grid", &GXEMAP_wrap_is_grid,
                "is_grid() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is the map a grid map?\n\n"

                ":returns: 1 - Yes, 0 - No\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("reload_grid", &GXEMAP_wrap_reload_grid,
                "reload_grid((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Reloads a grid document.\n\n"

                ":param arg1: Source file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Use this method to reload (if loaded) a grid document if the file on disk changed.\n"
                "   				\n\n"
               ).staticmethod("reload_grid");
    pyClass.def("is_3d_view", &GXEMAP_wrap_is_3d_view,
                "is_3d_view() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is the current view a 3D view.\n\n"

                ":returns: 1 - Yes, 0 - No\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("is_locked", &GXEMAP_wrap_is_locked,
                "is_locked() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this Map locked\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("loaded", &GXEMAP_wrap_loaded,
                "loaded((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns 1 if a map is loaded .\n\n"

                ":param arg1: map name\n"
                ":type arg1: str\n"
                ":returns: 1 if map is loaded, 0 otherwise.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("loaded");
    pyClass.def("read_only", &GXEMAP_wrap_read_only,
                "read_only() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Checks if a map is currently opened in a read-only mode.\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_window_position", &GXEMAP_wrap_get_window_position,
                "get_window_position((int_ref)arg1, (int_ref)arg2, (int_ref)arg3, (int_ref)arg4, (int_ref)arg5, (int_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the map window's position and dock state\n\n"

                ":param arg1: Window left position\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Window top position\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: Window right position\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg4: Window bottom position\n"
                ":type arg4: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg5: Window state \\ :ref:`EMAP_WINDOW_STATE`\\ \n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Docked or floating \\ :ref:`EMAP_WINDOW_POSITION`\\ \n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               );
    pyClass.def("set_window_position", &GXEMAP_wrap_set_window_position,
                "set_window_position((int)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the map window's position and dock state\n\n"

                ":param arg1: Window left position\n"
                ":type arg1: int\n"
                ":param arg2: Window top position\n"
                ":type arg2: int\n"
                ":param arg3: Window right position\n"
                ":type arg3: int\n"
                ":param arg4: Window bottom position\n"
                ":type arg4: int\n"
                ":param arg5: Window state \\ :ref:`EMAP_WINDOW_STATE`\\ \n"
                ":type arg5: int\n"
                ":param arg6: Docked or floating \\ :ref:`EMAP_WINDOW_POSITION`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               );
    pyClass.def("doubleize_group_snapshot", &GXEMAP_wrap_doubleize_group_snapshot,
                "doubleize_group_snapshot((GXLST)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The LST passed in must contain View\\Group strings in\n"
                "   					the Name field only. The function will compare with\n"
                "   					a more current LST and zoom the map to the new entry.\n"
                "   				\n\n"

                ":param arg1: LST object used for comparison\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: 0 if zoom proceeded ok\n"
                "          						1 if error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Typically this function is used in conjunction with\n"
                "   					CreateSnapshot_EMAP.\n"
                "   				\n\n"
               );
    pyClass.def("set_current_view", &GXEMAP_wrap_set_current_view,
                "set_current_view((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the current working view.\n\n"

                ":param arg1: view name\n"
                ":type arg1: str\n"
                ":returns: 0 if view set, 1 if view does not exist.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function operates on the current map.\n"
                "   					It changes the view only during the execution of the\n"
                "   					GX. As soon as the GX terminates the view will revert\n"
                "   					to the original one.\n"
                "   				\n\n"
               );
    pyClass.def("get_view_ipj", &GXEMAP_wrap_get_view_ipj,
                "get_view_ipj((str)arg1, (GXIPJ)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a view's IPJ.\n\n"

                ":param arg1: view name\n"
                ":type arg1: str\n"
                ":param arg2: IPJ in which to place the view IPJ\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function can be used to obtain a views coordinate system \n"
                "   					without having to call \\ :func:`geosoft.gxapi.GXEMAP.lock`\\ . This could be an expensive operation\n"
                "   					that cause undesirable UX.\n"
                "   				\n\n"
               );
    pyClass.def("load", &GXEMAP_wrap_load,
                "load((str)arg1) -> GXEMAP:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads maps into the editor.\n\n"

                ":param arg1: list of maps (';' or '\\ `|`\\ ' delimited) to load.\n"
                ":type arg1: str\n"
                ":returns: EMAP Object to edited map.\n"
                ":rtype: :class:`geosoft.gxapi.GXEMAP`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The last map in the list will be the current map.\n"
                "   \n"
                "   					Maps may already be loaded.\n"
                "   \n"
                "   					Only the first file in the list may have a directory path.\n"
                "   					All other files in the list are assumed to be in the same\n"
                "   					directory as the first file.\n"
                "   				\n\n"
               ).staticmethod("load");
    pyClass.def("load_no_activate", &GXEMAP_wrap_load_no_activate,
                "load_no_activate((str)arg1) -> GXEMAP:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads documents into the workspace\n\n"

                ":param arg1: list of documents (';' or '\\ `|`\\ ' delimited) to load.\n"
                ":type arg1: str\n"
                ":returns: Handle to current edited document, which will be the last\n"
                "          						database in the list if multiple files were provided.\n"
                ":rtype: :class:`geosoft.gxapi.GXEMAP`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function acts just like \\ :func:`geosoft.gxapi.GXEMAP.load`\\  except that the document(s) is not activated (brought to foreground) and no\n"
                "   					guarantee is given about which document is currently active.\n"
                "   				\n\n"
               ).staticmethod("load_no_activate");
    pyClass.def("load_with_view", &GXEMAP_wrap_load_with_view,
                "load_with_view((str)arg1, (GXEMAP)arg2) -> GXEMAP:\n"

                "\n.. parsed-literal::\n\n"
                "   Load an EMAP with the view from a current EMAP.\n\n"

                ":param arg1: Source Map name\n"
                ":type arg1: str\n"
                ":param arg2: EMAP to use as the source view\n"
                ":type arg2: :class:`geosoft.gxapi.GXEMAP`\n"
                ":returns: New EMAP handle.\n"
                ":rtype: :class:`geosoft.gxapi.GXEMAP`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Can only be run in interactive mode. Is used by\n"
                "   					dbsubset to create a new database with the same\n"
                "   					view as previously.\n"
                "   				\n\n"
               ).staticmethod("load_with_view");
    pyClass.def("lock", &GXEMAP_wrap_lock,
                "lock() -> GXMAP:\n"

                "\n.. parsed-literal::\n\n"
                "   This method locks the Edited map.\n\n"

                ":returns: EMAP Object to map associated with edited map.\n"
                ":rtype: :class:`geosoft.gxapi.GXMAP`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Redraw flag is set to EMAP_REDRAW_YES when this functions is called.\n\n"
               );
    pyClass.def("make_current", &GXEMAP_wrap_make_current,
                "make_current() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Makes this EMAP object the current active object to the user.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("print", &GXEMAP_wrap_print,
                "print((int)arg1, (int)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7, (int)arg8, (float)arg9, (int)arg10, (int)arg11, (int)arg12, (str)arg13) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Print the current map to current printer.\n\n"

                ":param arg1: lEntireMap  (0 or 1)\n"
                ":type arg1: int\n"
                ":param arg2: lScaleToFit 0 - use scale factor 1 - fit to media 2 - fit to roll media\n"
                ":type arg2: int\n"
                ":param arg3: lPrintToFile(0 or 1)\n"
                ":type arg3: int\n"
                ":param arg4: lAllPages   (0 or 1)\n"
                ":type arg4: int\n"
                ":param arg5: lCentre     (0 or 1)\n"
                ":type arg5: int\n"
                ":param arg6: lCopies\n"
                ":type arg6: int\n"
                ":param arg7: lFirstPage\n"
                ":type arg7: int\n"
                ":param arg8: lLastPage\n"
                ":type arg8: int\n"
                ":param arg9: dScaleFactor (2.0 doubles plot size)\n"
                ":type arg9: float\n"
                ":param arg10: lOverlapSize (mm)\n"
                ":type arg10: int\n"
                ":param arg11: lOffsetX     (mm)\n"
                ":type arg11: int\n"
                ":param arg12: lOffsetY     (mm)\n"
                ":type arg12: int\n"
                ":param arg13: szFile       (if lPrintToFile==1)\n"
                ":type arg13: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("redraw", &GXEMAP_wrap_redraw,
                "redraw() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Redraw the map immediately.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Redraws the map immediately. Map must not be locked.\n\n"
               );
    pyClass.def("select_group", &GXEMAP_wrap_select_group,
                "select_group((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Select a group.\n\n"

                ":param arg1: \"View/Group\"\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_redraw_flag", &GXEMAP_wrap_set_redraw_flag,
                "set_redraw_flag((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the redraw flag.\n\n"

                ":param arg1: \\ :ref:`EMAP_REDRAW`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function is generally used to prevent redrawing of\n"
                "   					the map, which normally occurs after the last \\ :func:`geosoft.gxapi.GXEMAP.un_lock`\\ \n"
                "   					call, in cases where it is known that no changes are being\n"
                "   					made to the map.\n"
                "   \n"
                "   					Typical usage:\n"
                "   \n"
                "   					ap = \\ :func:`geosoft.gxapi.GXEMAP.lock`\\ (EMap);\n"
                "   					etRedrawFlag_EMAP(EMap,EMAP_REDRAW_NO);\n"
                "   \n"
                "   					Stuff....\n"
                "   \n"
                "   					\\ :func:`geosoft.gxapi.GXEMAP.un_lock`\\ (Map);\n"
                "   				\n\n"
               );
    pyClass.def("un_load", &GXEMAP_wrap_un_load,
                "un_load((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unloads a MAP.\n\n"

                ":param arg1: Name of the map to unload\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the MAP is not loaded, nothing happens.\n"
                "   					Same as \\ :func:`geosoft.gxapi.GXEMAP.un_load_verify`\\  with FALSE to prompt save.\n"
                "   				\n\n"
               ).staticmethod("un_load");
    pyClass.def("un_load_all", &GXEMAP_wrap_un_load_all,
                "un_load_all() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unloads all opened maps\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("un_load_all");
    pyClass.def("un_load_verify", &GXEMAP_wrap_un_load_verify,
                "un_load_verify((str)arg1, (bool)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unloads an edited map, optional prompt to save.\n\n"

                ":param arg1: Name of map to unload\n"
                ":type arg1: str\n"
                ":param arg2: Prompt? bool\n"
                ":type arg2: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the map is not loaded, nothing happens.\n"
                "   					If \"FALSE\", map is saved without a prompt.\n"
                "   				\n\n"
               ).staticmethod("un_load_verify");
    pyClass.def("un_lock", &GXEMAP_wrap_un_lock,
                "un_lock() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method unlocks the Edited map.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_cur_point", &GXEMAP_wrap_get_cur_point,
                "get_cur_point((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the coordinates of the currently selected point in view coordinates\n\n"

                ":param arg1: X coordinate in current user units.\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_cur_point_mm", &GXEMAP_wrap_get_cur_point_mm,
                "get_cur_point_mm((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the coordinates of the currently selected point in mm on map\n\n"

                ":param arg1: X coordinate in map mm\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_cursor", &GXEMAP_wrap_get_cursor,
                "get_cursor((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the coordinates of the last known cursor location\n\n"

                ":param arg1: X coordinate in current view user units\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_cursor_mm", &GXEMAP_wrap_get_cursor_mm,
                "get_cursor_mm((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the coordinates of the last known cursor location in mm on map.\n\n"

                ":param arg1: X coordinate in map mm\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("digitize", &GXEMAP_wrap_digitize,
                "digitize((GXWA)arg1, (GXIMG)arg2, (int)arg3, (str)arg4, (str)arg5, (str)arg6, (int)arg7) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Digitise points from the current map and place in a WA.\n\n"

                ":param arg1: WA in which to write digitized points\n"
                ":type arg1: :class:`geosoft.gxapi.GXWA`\n"
                ":param arg2: IMG for Z value, or IMG_NULL for no Z.\n"
                ":type arg2: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg3: number of significant digits to use, 0 for all.\n"
                ":type arg3: int\n"
                ":param arg4: Command line prompt string\n"
                ":type arg4: str\n"
                ":param arg5: New line prefix string\n"
                ":type arg5: str\n"
                ":param arg6: Delimiter\n"
                ":type arg6: str\n"
                ":param arg7: 0 for no newline 1 for automatic newline at each point\n"
                ":type arg7: int\n"
                ":returns: 0 if user digitized some points.\n"
                "          						1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The command line will start to recieve digitized points\n"
                "   					from the mouse.  Whenever the left mouse button is\n"
                "   					pressed, the current view X,Y are placed on the workspace\n"
                "   					command line.  If a valid IMG is passed, the Z value is\n"
                "   					also placed on the command line.  If auto-newline is\n"
                "   					specified, the line is immediately placed into WA,\n"
                "   					otherwise the user has the oportunity to enter data\n"
                "   					before pressing Enter.\n"
                "   \n"
                "   					Locations are in the current view user units\n"
                "   				\n\n"
               );
    pyClass.def("digitize2", &GXEMAP_wrap_digitize2,
                "digitize2((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXIMG)arg4, (str)arg5, (int)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Digitise points from the current map and place in VVs.\n\n"

                ":param arg1: real X VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: real Y VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: real Z VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: IMG for Z value, or IMG_NULL for no Z.\n"
                ":type arg4: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg5: Command line prompt string\n"
                ":type arg5: str\n"
                ":param arg6: 0 for no newline 1 for automatic newline at each point\n"
                ":type arg6: int\n"
                ":returns: 0 if user digitized some points.\n"
                "          						1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The command line will start to recieve digitized points\n"
                "   					from the mouse.  Whenever the left mouse button is\n"
                "   					pressed, the current view X,Y are placed on the workspace\n"
                "   					command line.  If a valid IMG is passed, the Z value is\n"
                "   					also placed on the command line.  If auto-newline is\n"
                "   					specified, the line is immediately placed into the VVs,\n"
                "   					otherwise the user has the oportunity to enter data\n"
                "   					before pressing Enter.\n"
                "   \n"
                "   					Locations are in the current view user units\n"
                "   				\n\n"
               );
    pyClass.def("digitize_peaks", &GXEMAP_wrap_digitize_peaks,
                "digitize_peaks((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXIMG)arg4, (str)arg5, (int)arg6) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Digitise points from the current map and place in VVs.\n\n"

                ":param arg1: real X VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: real Y VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: real Z VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: IMG for Z value, or IMG_NULL for no Z.\n"
                ":type arg4: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg5: Command line prompt string\n"
                ":type arg5: str\n"
                ":param arg6: 0 for no newline 1 for automatic newline at each point\n"
                ":type arg6: int\n"
                ":returns: 0 if user digitized some points.\n"
                "          						1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Same as \\ :func:`geosoft.gxapi.GXEMAP.digitize2`\\ , but the closest peaks to the selected locations are\n"
                "   					returned instead of the selected location. The method chooses the highest value\n"
                "   					of the 8 surrounding points, the repeats this process until no higher value can\n"
                "   					be found in any of the 8 surrounding points. If there are two or more points with\n"
                "   					a higher value, it will just take the first one and continue, and this method will\n"
                "   					stall on flat areas as well (since no surrounding point is larger).\n"
                "   				\n\n"
               );
    pyClass.def("digitize_polygon", &GXEMAP_wrap_digitize_polygon,
                "digitize_polygon((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXIMG)arg4, (str)arg5, (int)arg6, (int)arg7) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Same as iDigitze2_EMAP, but automatically close polygons.\n\n"

                ":param arg1: real X VV\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: real Y VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: real Z VV\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: IMG for Z value, or IMG_NULL for no Z.\n"
                ":type arg4: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg5: Command line prompt string\n"
                ":type arg5: str\n"
                ":param arg6: 0 for no newline 1 for automatic newline at each point\n"
                ":type arg6: int\n"
                ":param arg7: close the polygon if the selected location is within this radius in screen pixels.\n"
                ":type arg7: int\n"
                ":returns: 0 if user digitized some points.\n"
                "          						1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is the same as \\ :func:`geosoft.gxapi.GXEMAP.digitize2`\\ , except that it automatically\n"
                "   					detects, (except for the 2nd and 3rd points) when a selected location\n"
                "   					is within the entered number of pixels from the starting point. If yes,\n"
                "   					the polygon is assumed to be closed, and the operation is the same as\n"
                "   					the RMB \"done\" command, and the process returns 0.\n"
                "   				\n\n"
               );
    pyClass.def("get_box", &GXEMAP_wrap_get_box,
                "get_box((str)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the coordinates of a user selected box.\n\n"

                ":param arg1: user prompt string\n"
                ":type arg1: str\n"
                ":param arg2: X minimum in current view user units.\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: X maximum\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Y\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 if point returned.\n"
                "          						1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_box2", &GXEMAP_wrap_get_box2,
                "get_box2((str)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8, (float_ref)arg9) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the coordinates of a user selected box in a warped view.\n\n"

                ":param arg1: user prompt string\n"
                ":type arg1: str\n"
                ":param arg2: X1 bottom left corner\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y1\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: X2 bottom right corner\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Y2\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: X3 top right corner\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Y3\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: X4 top left corner\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg9: Y4\n"
                ":type arg9: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 if point returned.\n"
                "          						1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the data view has a rotational (or other) warp, then the\n"
                "   					\\ :func:`geosoft.gxapi.GXEMAP.get_box`\\  function returns only opposite diagonal points in the\n"
                "   					box, not enough info to determine the other two corners. This\n"
                "   					function returns the exact coordinates of all four corners, calculated\n"
                "   					from the pixel locations.\n"
                "   				\n\n"
               );
    pyClass.def("get_grid", &GXEMAP_wrap_get_grid,
                "get_grid((str)arg1, (int)arg2, (int)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7, (float_ref)arg8) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Position and size a grid on a map.\n\n"

                ":param arg1: user prompt string\n"
                ":type arg1: str\n"
                ":param arg2: Number of elements along primary axis to draw.\n"
                ":type arg2: int\n"
                ":param arg3: Number of elements along secondary axis to draw.\n"
                ":type arg3: int\n"
                ":param arg4: Angle of primary axis in degrees\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Grid origin X\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Grid origin Y\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Primary axis length\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg8: Secondary axis length\n"
                ":type arg8: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 if line returned.\n"
                "          						1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the input angle is rDUMMY, an extra step is inserted\n"
                "   					for the user to define the angle by drawing a line\n"
                "   					with the mouse.\n"
                "   					The output primary axis angle will always be in the\n"
                "   					range -90 < angle <= 90. The grid origin is shifted to\n"
                "   					whichever corner necessary to make this possible, while keeping\n"
                "   					the secondary axis at 90 degrees greater than the primary (\n"
                "   					going counter-clockwise).\n"
                "   					The coordinates are returned in the current User projection\n"
                "   					(See \\ :func:`geosoft.gxapi.GXMVIEW.get_user_ipj`\\  and \\ :func:`geosoft.gxapi.GXMVIEW.set_user_ipj`\\ .)\n"
                "   				\n\n"
               );
    pyClass.def("get_line", &GXEMAP_wrap_get_line,
                "get_line((str)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the end points of a line.\n\n"

                ":param arg1: user prompt string\n"
                ":type arg1: str\n"
                ":param arg2: X1 in view user units\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y1\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: X2\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Y2\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 if line returned.\n"
                "          						1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The coordinates are returned in the current User projection\n"
                "   					(See \\ :func:`geosoft.gxapi.GXMVIEW.get_user_ipj`\\  and \\ :func:`geosoft.gxapi.GXMVIEW.set_user_ipj`\\ .)\n"
                "   				\n\n"
               );
    pyClass.def("get_line_ex", &GXEMAP_wrap_get_line_ex,
                "get_line_ex((str)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the end points of a line.\n\n"

                ":param arg1: user prompt string\n"
                ":type arg1: str\n"
                ":param arg2: X1 in view user units\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y1\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: X2\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Y2\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 if line returned.\n"
                "          						1 - Right Mouse\n"
                "          						2 - Escape/Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The coordinates are returned in the current User projection\n"
                "   					(See \\ :func:`geosoft.gxapi.GXMVIEW.get_user_ipj`\\  and \\ :func:`geosoft.gxapi.GXMVIEW.set_user_ipj`\\ .)\n"
                "   				\n\n"
               );
    pyClass.def("get_line_xyz", &GXEMAP_wrap_get_line_xyz,
                "get_line_xyz((str)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6, (float_ref)arg7) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the end points of a line in X,Y and Z\n\n"

                ":param arg1: user prompt string\n"
                ":type arg1: str\n"
                ":param arg2: X1 in view user units\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y1\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Z1\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: X2\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Y2\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg7: Z2\n"
                ":type arg7: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 if line returned.\n"
                "          						1 - Right Mouse\n"
                "          						2 - Escape/Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The coordinates are returned in the current User projection\n"
                "   					(See \\ :func:`geosoft.gxapi.GXMVIEW.get_user_ipj`\\  and \\ :func:`geosoft.gxapi.GXMVIEW.set_user_ipj`\\ .)\n"
                "   					This is useful for digitizing a line in an oriented view and getting\n"
                "   					the true coordinates in (X, Y, Z) at the selected point on the view plane.\n"
                "   				\n\n"
               );
    pyClass.def("get_point", &GXEMAP_wrap_get_point,
                "get_point((str)arg1, (float_ref)arg2, (float_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the coordinates of a user selected point.\n\n"

                ":param arg1: user prompt string\n"
                ":type arg1: str\n"
                ":param arg2: X coordinate in current view user units.\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 if point returned.\n"
                "          						1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This will wait for user to select a point.\n\n"

                "\n.. seealso::\n\n"
                "   iTrackPoint, GetCurPoint, GetCursor\n\n"
               );
    pyClass.def("get_point_ex", &GXEMAP_wrap_get_point_ex,
                "get_point_ex((str)arg1, (float_ref)arg2, (float_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the coordinates of a user selected point.\n\n"

                ":param arg1: user prompt string\n"
                ":type arg1: str\n"
                ":param arg2: X coordinate in current view user units.\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 if point returned.\n"
                "          						1 if user used right mouse and then Done.\n"
                "          						2 if user cancelled.\n"
                "          						3 if capture is lost.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This will wait for user to select a point.\n\n"

                "\n.. seealso::\n\n"
                "   iTrackPoint, GetCurPoint, GetCursor\n\n"
               );
    pyClass.def("get_point_3d", &GXEMAP_wrap_get_point_3d,
                "get_point_3d((str)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the coordinates of a user selected point.\n\n"

                ":param arg1: user prompt string\n"
                ":type arg1: str\n"
                ":param arg2: X coordinate in current view user units.\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Z\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 if point returned.\n"
                "          						1 if user used right mouse and then Done.\n"
                "          						2 if user cancelled.\n"
                "          						3 if capture is lost.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This will wait for user to select a point.\n\n"

                "\n.. seealso::\n\n"
                "   iTrackPoint, GetCurPoint, GetCursor\n\n"
               );
    pyClass.def("get_poly_line", &GXEMAP_wrap_get_poly_line,
                "get_poly_line((str)arg1, (GXVV)arg2, (GXVV)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns a polyline.\n\n"

                ":param arg1: user prompt string\n"
                ":type arg1: str\n"
                ":param arg2: X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: 0 if line returned.\n"
                "          						1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The coordinates are returned in the current User projection\n"
                "   					(See \\ :func:`geosoft.gxapi.GXMVIEW.get_user_ipj`\\  and \\ :func:`geosoft.gxapi.GXMVIEW.set_user_ipj`\\ .)\n"
                "   				\n\n"
               );
    pyClass.def("get_poly_line_xyz", &GXEMAP_wrap_get_poly_line_xyz,
                "get_poly_line_xyz((str)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns a polyline.\n\n"

                ":param arg1: user prompt string\n"
                ":type arg1: str\n"
                ":param arg2: X\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: Z\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: 0 if line returned.\n"
                "          						1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The coordinates are returned in the current User projection\n"
                "   					(See \\ :func:`geosoft.gxapi.GXMVIEW.get_user_ipj`\\  and \\ :func:`geosoft.gxapi.GXMVIEW.set_user_ipj`\\ .) In this version\n"
                "   					of the method X, Y and Z (depth) are returned. Initially created\n"
                "   					to deal with crooked sections.\n"
                "   				\n\n"
               );
    pyClass.def("get_rect", &GXEMAP_wrap_get_rect,
                "get_rect((str)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the coordinates of a user selected box starting at a corner.\n\n"

                ":param arg1: user prompt string\n"
                ":type arg1: str\n"
                ":param arg2: X minimum in current view user units.   (defines corner)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: X maximum\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Y\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 if point returned.\n"
                "          						1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The coordinates are returned in the current User projection\n"
                "   					(See \\ :func:`geosoft.gxapi.GXMVIEW.get_user_ipj`\\  and \\ :func:`geosoft.gxapi.GXMVIEW.set_user_ipj`\\ .)\n"
                "   					If the user IPJ distorts the coordinates from being rectilinear\n"
                "   					(e.g. for a TriPlot graph), then care should be taken since the\n"
                "   					(Xmin, Ymin) and (Xmax, Ymax) values returned do not necessarily\n"
                "   					correspond to the lower-left and upper-right corners. In fact, the\n"
                "   					returned values are calculated by taking the starting (fixed) corner\n"
                "   					and the tracked (opposite) corner, and finding the min and max for\n"
                "   					X and Y among these two points. With a warped User projection, those\n"
                "   					two corner locations could easily be (Xmin, Ymax) and (Xmax, Ymin).\n"
                "   					This becomes quite important if you want to use the rectangle for a\n"
                "   					masking operation, because the \"other\" two corner's coordinates may\n"
                "   					need to be constructed based on a knowledge of the User projection,\n"
                "   					and may not be directly obtained from the returned X and Y min and\n"
                "   					max values. What appears to be a rectangle as seen on the map is not\n"
                "   					necessarily a rectangle in the User coordinates.\n"
                "   				\n\n"
               );
    pyClass.def("track_point", &GXEMAP_wrap_track_point,
                "track_point((int)arg1, (float_ref)arg2, (float_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get point without prompt or cursor change with tracking\n\n"

                ":param arg1: \\ :ref:`EMAP_TRACK`\\ \n"
                ":type arg1: int\n"
                ":param arg2: X coordinate in current view user units.\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 if point returned.\n"
                "          						1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_aoi_area", &GXEMAP_wrap_get_aoi_area,
                "get_aoi_area((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the area of interest.\n\n"

                ":param arg1: X Min returned\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y Min returned\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: X Max returned\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Y Max returned\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Coordinates are based on the current view units.\n\n"
               );
    pyClass.def("set_aoi_area", &GXEMAP_wrap_set_aoi_area,
                "set_aoi_area((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the area of interest.\n\n"

                ":param arg1: X Min\n"
                ":type arg1: float\n"
                ":param arg2: Y Min\n"
                ":type arg2: float\n"
                ":param arg3: X Max\n"
                ":type arg3: float\n"
                ":param arg4: Y Max\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Coordinates are based on the current view user units.\n"
                "   					The map is immediatly redrawn.\n"
                "   				\n\n"
               );
    pyClass.def("set_viewport_mode", &GXEMAP_wrap_set_viewport_mode,
                "set_viewport_mode((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the viewport mode.\n\n"

                ":param arg1: \\ :ref:`EMAP_VIEWPORT`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is handy for using a map to define an area of interest. Use in conjunction\n"
                "   					with Get/Set AOIArea. If this is used inside montaj it is important to set or provide\n"
                "   					for a method to set the map mode back to normal as this is not exposed in the interface.\n"
                "   				\n\n"
               );
    pyClass.def("get_selected_vertices", &GXEMAP_wrap_get_selected_vertices,
                "get_selected_vertices((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the verticies of selected object\n\n"

                ":param arg1: X VV Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV Handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Works only in Vertex Edit Mode\n\n"
               );
    pyClass.def("create_virtual", &GXEMAP_wrap_create_virtual,
                "create_virtual((str)arg1) -> GXEMAP:\n"

                "\n.. parsed-literal::\n\n"
                "   Makes this EMAP object the current active object to the user.\n\n"

                ":param arg1: Name of map to create a virtual EMAP from\n"
                ":type arg1: str\n"
                ":returns: EMAP Object\n"
                ":rtype: :class:`geosoft.gxapi.GXEMAP`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_virtual");

    scope().attr("EMAP_FONT_TT") = (int32_t)0;
    scope().attr("EMAP_FONT_GFN") = (int32_t)1;
    scope().attr("EMAP_PATH_FULL") = (int32_t)0;
    scope().attr("EMAP_PATH_DIR") = (int32_t)1;
    scope().attr("EMAP_PATH_NAME_EXT") = (int32_t)2;
    scope().attr("EMAP_PATH_NAME") = (int32_t)3;
    scope().attr("EMAP_REDRAW_NO") = (int32_t)0;
    scope().attr("EMAP_REDRAW_YES") = (int32_t)1;
    scope().attr("EMAP_REMOVE_SAVE") = (int32_t)0;
    scope().attr("EMAP_REMOVE_PROMPT") = (int32_t)1;
    scope().attr("EMAP_REMOVE_DISCARD") = (int32_t)2;
    scope().attr("EMAP_TRACK_ERASE") = (int32_t)1;
    scope().attr("EMAP_TRACK_RMENU") = (int32_t)2;
    scope().attr("EMAP_TRACK_CYCLE") = (int32_t)4;
    scope().attr("EMAP_VIEWPORT_NORMAL") = (int32_t)0;
    scope().attr("EMAP_VIEWPORT_BROWSEZOOM") = (int32_t)1;
    scope().attr("EMAP_VIEWPORT_BROWSEAOI") = (int32_t)2;
    scope().attr("EMAP_WINDOW_POSITION_DOCKED") = (int32_t)0;
    scope().attr("EMAP_WINDOW_POSITION_FLOATING") = (int32_t)1;
    scope().attr("EMAP_WINDOW_RESTORE") = (int32_t)0;
    scope().attr("EMAP_WINDOW_MINIMIZE") = (int32_t)1;
    scope().attr("EMAP_WINDOW_MAXIMIZE") = (int32_t)2;
    scope().attr("LAYOUT_VIEW_MM") = (int32_t)0;
    scope().attr("LAYOUT_VIEW_CM") = (int32_t)1;
    scope().attr("LAYOUT_VIEW_IN") = (int32_t)2;

}
