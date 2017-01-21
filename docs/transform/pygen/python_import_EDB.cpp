#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXEDB_wrap_apply_formula_internal(GXEDBPtr self, const gx_string_type& arg1)
{
    self->apply_formula_internal(arg1);
}
inline GXEDBPtr GXEDB_wrap_current()
{
    GXEDBPtr ret = GXEDB::current();
    return ret;
}
inline GXEDBPtr GXEDB_wrap_current_no_activate()
{
    GXEDBPtr ret = GXEDB::current_no_activate();
    return ret;
}
inline GXEDBPtr GXEDB_wrap_current_if_exists()
{
    GXEDBPtr ret = GXEDB::current_if_exists();
    return ret;
}
inline void GXEDB_wrap_del_line0(GXEDBPtr self)
{
    self->del_line0();
}
inline void GXEDB_wrap_destroy_view(GXEDBPtr self, int32_t arg1)
{
    self->destroy_view((EDB_REMOVE)arg1);
}
inline int32_t GXEDB_wrap_get_cur_chan_symb(GXEDBPtr self)
{
    int32_t ret = self->get_cur_chan_symb();
    return ret;
}
inline int32_t GXEDB_wrap_get_cur_line_symb(GXEDBPtr self)
{
    int32_t ret = self->get_cur_line_symb();
    return ret;
}
inline void GXEDB_wrap_get_displ_fid_range(GXEDBPtr self, int_ref& arg1, int_ref& arg2)
{
    self->get_displ_fid_range(arg1, arg2);
}
inline void GXEDB_wrap_get_fid_range(GXEDBPtr self, float_ref& arg1, float_ref& arg2, int_ref& arg3)
{
    self->get_fid_range(arg1, arg2, arg3);
}
inline int32_t GXEDB_wrap_get_next_line_symb(GXEDBPtr self)
{
    int32_t ret = self->get_next_line_symb();
    return ret;
}
inline int32_t GXEDB_wrap_get_prev_line_symb(GXEDBPtr self)
{
    int32_t ret = self->get_prev_line_symb();
    return ret;
}
inline void GXEDB_wrap_get_profile_range_x(GXEDBPtr self, float_ref& arg1, float_ref& arg2, int_ref& arg3)
{
    self->get_profile_range_x(arg1, arg2, arg3);
}
inline void GXEDB_wrap_get_profile_range_y(GXEDBPtr self, int32_t arg1, int32_t arg2, float_ref& arg3, float_ref& arg4, int_ref& arg5)
{
    self->get_profile_range_y(arg1, arg2, arg3, arg4, (EDB_PROFILE_SCALE&)arg5);
}
inline void GXEDB_wrap_get_profile_split(GXEDBPtr self, float_ref& arg1, float_ref& arg2)
{
    self->get_profile_split(arg1, arg2);
}
inline void GXEDB_wrap_get_profile_split5(GXEDBPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4)
{
    self->get_profile_split5(arg1, arg2, arg3, arg4);
}
inline void GXEDB_wrap_get_profile_split_vv(GXEDBPtr self, GXVVPtr arg1)
{
    self->get_profile_split_vv(arg1);
}
inline void GXEDB_wrap_get_profile_vertical_grid_lines(GXEDBPtr self, int_ref& arg1, float_ref& arg2)
{
    self->get_profile_vertical_grid_lines(arg1, arg2);
}
inline void GXEDB_wrap_get_profile_window(GXEDBPtr self, int32_t arg1, int_ref& arg2, int_ref& arg3)
{
    self->get_profile_window(arg1, arg2, arg3);
}
inline void GXEDB_wrap_goto_column(GXEDBPtr self, int32_t arg1)
{
    self->goto_column(arg1);
}
inline void GXEDB_wrap_goto_elem(GXEDBPtr self, int32_t arg1)
{
    self->goto_elem(arg1);
}
inline void GXEDB_wrap_goto_line(GXEDBPtr self, int32_t arg1)
{
    self->goto_line(arg1);
}
inline void GXEDB_wrap_histogram(GXEDBPtr self, GXSTPtr arg1, double arg2, double arg3, int32_t arg4)
{
    self->histogram(arg1, arg2, arg3, arg4);
}
inline int32_t GXEDB_wrap_all_chan_list(GXEDBPtr self, GXVVPtr arg1)
{
    int32_t ret = self->all_chan_list(arg1);
    return ret;
}
inline int32_t GXEDB_wrap_channels(GXEDBPtr self)
{
    int32_t ret = self->channels();
    return ret;
}
inline int32_t GXEDB_wrap_disp_chan_list(GXEDBPtr self, GXVVPtr arg1)
{
    int32_t ret = self->disp_chan_list(arg1);
    return ret;
}
inline int32_t GXEDB_wrap_disp_chan_lst(GXEDBPtr self, GXLSTPtr arg1)
{
    int32_t ret = self->disp_chan_lst(arg1);
    return ret;
}
inline int32_t GXEDB_wrap_disp_class_chan_lst(GXEDBPtr self, GXLSTPtr arg1, const gx_string_type& arg2)
{
    int32_t ret = self->disp_class_chan_lst(arg1, arg2);
    return ret;
}
inline int32_t GXEDB_wrap_find_channel_column(GXEDBPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->find_channel_column(arg1);
    return ret;
}
inline int32_t GXEDB_wrap_find_nearest(GXEDBPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, GXIPJPtr arg4)
{
    int32_t ret = self->find_nearest(arg1, arg2, arg3, arg4);
    return ret;
}
inline void GXEDB_wrap_get_cur_chan(GXEDBPtr self, str_ref& arg1)
{
    self->get_cur_chan(arg1);
}
inline void GXEDB_wrap_get_cur_fid_string(GXEDBPtr self, str_ref& arg1)
{
    self->get_cur_fid_string(arg1);
}
inline void GXEDB_wrap_get_cur_line(GXEDBPtr self, str_ref& arg1)
{
    self->get_cur_line(arg1);
}
inline int32_t GXEDB_wrap_get_cur_mark(GXEDBPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3)
{
    int32_t ret = self->get_cur_mark(arg1, arg2, arg3);
    return ret;
}
inline void GXEDB_wrap_get_current_selection(GXEDBPtr self, str_ref& arg1, str_ref& arg2, str_ref& arg3, str_ref& arg4)
{
    self->get_current_selection(arg1, arg2, arg3, arg4);
}
inline int32_t GXEDB_wrap_get_databases_lst(GXLSTPtr arg1, int32_t arg2)
{
    int32_t ret = GXEDB::get_databases_lst(arg1, (EDB_PATH)arg2);
    return ret;
}
inline int32_t GXEDB_wrap_get_mark_chan_vv(GXEDBPtr self, GXVVPtr arg1, int32_t arg2)
{
    int32_t ret = self->get_mark_chan_vv(arg1, arg2);
    return ret;
}
inline int32_t GXEDB_wrap_get_mark_chan_va(GXEDBPtr self, GXVAPtr arg1, int32_t arg2)
{
    int32_t ret = self->get_mark_chan_va(arg1, arg2);
    return ret;
}
inline void GXEDB_wrap_get_name(GXEDBPtr self, str_ref& arg1)
{
    self->get_name(arg1);
}
inline int32_t GXEDB_wrap_get_profile_parm_int(GXEDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    int32_t ret = self->get_profile_parm_int(arg1, arg2, (EDB_PROF)arg3);
    return ret;
}
inline int32_t GXEDB_wrap_get_window_state(GXEDBPtr self)
{
    EDB_WINDOW_STATE ret = self->get_window_state();
    return ret;
}
inline bool GXEDB_wrap_have_current()
{
    bool ret = GXEDB::have_current();
    return ret;
}
inline bool GXEDB_wrap_is_locked(GXEDBPtr self)
{
    bool ret = self->is_locked();
    return ret;
}
inline int32_t GXEDB_wrap_loaded(const gx_string_type& arg1)
{
    int32_t ret = GXEDB::loaded(arg1);
    return ret;
}
inline int32_t GXEDB_wrap_profile_open(GXEDBPtr self, int32_t arg1)
{
    int32_t ret = self->profile_open(arg1);
    return ret;
}
inline bool GXEDB_wrap_read_only(GXEDBPtr self)
{
    bool ret = self->read_only();
    return ret;
}
inline void GXEDB_wrap_get_window_position(GXEDBPtr self, int_ref& arg1, int_ref& arg2, int_ref& arg3, int_ref& arg4, int_ref& arg5, int_ref& arg6)
{
    self->get_window_position(arg1, arg2, arg3, arg4, (EDB_WINDOW_STATE&)arg5, (EDB_WINDOW_POSITION&)arg6);
}
inline void GXEDB_wrap_set_window_position(GXEDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    self->set_window_position(arg1, arg2, arg3, arg4, (EDB_WINDOW_STATE)arg5, (EDB_WINDOW_POSITION)arg6);
}
inline int32_t GXEDB_wrap_show_profile_name(GXEDBPtr self, int32_t arg1, const gx_string_type& arg2)
{
    int32_t ret = self->show_profile_name(arg1, arg2);
    return ret;
}
inline int32_t GXEDB_wrap_get_window_y_axis_direction(GXEDBPtr self, int32_t arg1)
{
    EDB_YAXIS_DIRECTION ret = self->get_window_y_axis_direction(arg1);
    return ret;
}
inline int32_t GXEDB_wrap_window_profiles(GXEDBPtr self, int32_t arg1)
{
    int32_t ret = self->window_profiles(arg1);
    return ret;
}
inline void GXEDB_wrap_launch_histogram(GXEDBPtr self, const gx_string_type& arg1)
{
    self->launch_histogram(arg1);
}
inline void GXEDB_wrap_launch_scatter(GXEDBPtr self)
{
    self->launch_scatter();
}
inline GXEDBPtr GXEDB_wrap_load(const gx_string_type& arg1)
{
    GXEDBPtr ret = GXEDB::load(arg1);
    return ret;
}
inline GXEDBPtr GXEDB_wrap_load_no_activate(const gx_string_type& arg1)
{
    GXEDBPtr ret = GXEDB::load_no_activate(arg1);
    return ret;
}
inline void GXEDB_wrap_load_all_chans(GXEDBPtr self)
{
    self->load_all_chans();
}
inline void GXEDB_wrap_load_chan(GXEDBPtr self, const gx_string_type& arg1)
{
    self->load_chan(arg1);
}
inline GXEDBPtr GXEDB_wrap_load_new(const gx_string_type& arg1)
{
    GXEDBPtr ret = GXEDB::load_new(arg1);
    return ret;
}
inline GXEDBPtr GXEDB_wrap_load_pass(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXEDBPtr ret = GXEDB::load_pass(arg1, arg2, arg3);
    return ret;
}
inline GXEDBPtr GXEDB_wrap_load_with_view(const gx_string_type& arg1, GXEDBPtr arg2)
{
    GXEDBPtr ret = GXEDB::load_with_view(arg1, arg2);
    return ret;
}
inline GXDBPtr GXEDB_wrap_lock(GXEDBPtr self)
{
    GXDBPtr ret = self->lock();
    return ret;
}
inline void GXEDB_wrap_make_current(GXEDBPtr self)
{
    self->make_current();
}
inline void GXEDB_wrap_remove_profile(GXEDBPtr self, int32_t arg1, int32_t arg2)
{
    self->remove_profile(arg1, arg2);
}
inline double GXEDB_wrap_get_cur_fid(GXEDBPtr self)
{
    double ret = self->get_cur_fid();
    return ret;
}
inline double GXEDB_wrap_get_profile_parm_double(GXEDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3)
{
    double ret = self->get_profile_parm_double(arg1, arg2, (EDB_PROF)arg3);
    return ret;
}
inline double GXEDB_wrap_get_split(GXEDBPtr self)
{
    double ret = self->get_split();
    return ret;
}
inline void GXEDB_wrap_run_channel_maker(GXEDBPtr self, const gx_string_type& arg1)
{
    self->run_channel_maker(arg1);
}
inline void GXEDB_wrap_run_channel_makers(GXEDBPtr self)
{
    self->run_channel_makers();
}
inline void GXEDB_wrap_set_cur_line(GXEDBPtr self, const gx_string_type& arg1)
{
    self->set_cur_line(arg1);
}
inline void GXEDB_wrap_set_cur_line_no_message(GXEDBPtr self, const gx_string_type& arg1)
{
    self->set_cur_line_no_message(arg1);
}
inline void GXEDB_wrap_set_cur_mark(GXEDBPtr self, double arg1, double arg2)
{
    self->set_cur_mark(arg1, arg2);
}
inline void GXEDB_wrap_set_profile_parm_i(GXEDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    self->set_profile_parm_i(arg1, arg2, (EDB_PROF)arg3, arg4);
}
inline void GXEDB_wrap_set_profile_parm_r(GXEDBPtr self, int32_t arg1, int32_t arg2, int32_t arg3, double arg4)
{
    self->set_profile_parm_r(arg1, arg2, (EDB_PROF)arg3, arg4);
}
inline void GXEDB_wrap_set_profile_range_x(GXEDBPtr self, double arg1, double arg2, int32_t arg3)
{
    self->set_profile_range_x(arg1, arg2, arg3);
}
inline void GXEDB_wrap_set_profile_range_y(GXEDBPtr self, int32_t arg1, int32_t arg2, double arg3, double arg4, int32_t arg5)
{
    self->set_profile_range_y(arg1, arg2, arg3, arg4, (EDB_PROFILE_SCALE)arg5);
}
inline void GXEDB_wrap_set_profile_split(GXEDBPtr self, double arg1, double arg2)
{
    self->set_profile_split(arg1, arg2);
}
inline void GXEDB_wrap_set_profile_split5(GXEDBPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->set_profile_split5(arg1, arg2, arg3, arg4);
}
inline void GXEDB_wrap_set_profile_split_vv(GXEDBPtr self, GXVVPtr arg1)
{
    self->set_profile_split_vv(arg1);
}
inline void GXEDB_wrap_set_split(GXEDBPtr self, double arg1)
{
    self->set_split(arg1);
}
inline void GXEDB_wrap_set_window_state(GXEDBPtr self, int32_t arg1)
{
    self->set_window_state((EDB_WINDOW_STATE)arg1);
}
inline void GXEDB_wrap_show_profile(GXEDBPtr self, int32_t arg1, int32_t arg2)
{
    self->show_profile(arg1, arg2);
}
inline void GXEDB_wrap_statistics(GXEDBPtr self, GXSTPtr arg1)
{
    self->statistics(arg1);
}
inline void GXEDB_wrap_un_load(const gx_string_type& arg1)
{
    GXEDB::un_load(arg1);
}
inline void GXEDB_wrap_un_load_all()
{
    GXEDB::un_load_all();
}
inline void GXEDB_wrap_un_load_all_chans(GXEDBPtr self)
{
    self->un_load_all_chans();
}
inline void GXEDB_wrap_un_load_chan(GXEDBPtr self, const gx_string_type& arg1)
{
    self->un_load_chan(arg1);
}
inline void GXEDB_wrap_un_load_discard(const gx_string_type& arg1)
{
    GXEDB::un_load_discard(arg1);
}
inline void GXEDB_wrap_un_load_verify(const gx_string_type& arg1, int32_t arg2)
{
    GXEDB::un_load_verify(arg1, (EDB_UNLOAD)arg2);
}
inline void GXEDB_wrap_un_lock(GXEDBPtr self)
{
    self->un_lock();
}

void gxPythonImportGXEDB()
{

    class_<GXEDB, GXEDBPtr> pyClass("GXEDB",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		The EDB class provides access to a database as displayed within\n"
                                    "   		Oasis montaj, but does not change data within the database itself.\n"
                                    "   		It performs functions such as setting the current line.\n"
                                    "   	\n\n"

                                    "\n\n**Note:**\n\n"

                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		To obtain access to the database itself, it is recommended practice\n"
                                    "   		to begin with an EDB object, and use the \\ :func:`geosoft.gxapi.GXEDB.lock`\\  function to\n"
                                    "   		lock the underlying map to prevent external changes. The returned\n"
                                    "   		DB object (see DB.GXH) may then be safely used to make changes to the map itself.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXEDB::null, "null() -> GXEDB\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXEDB`\n\n:returns: A null :class:`geosoft.gxapi.GXEDB`\n:rtype: :class:`geosoft.gxapi.GXEDB`\n").staticmethod("null");
    pyClass.def("is_null", &GXEDB::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXEDB is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXEDB`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXEDB::_internal_handle);
    pyClass.def("apply_formula_internal", &GXEDB_wrap_apply_formula_internal,
                "apply_formula_internal((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Apply a formula to selected cells of the\n"
                "   					current line. (Do not use this wrapper if you\n"
                "   					want to apply a formula across multiple lines)\n"
                "   \n"
                "   					Notes:\n"
                "   \n"
                "   					The current selection must be on cell(s) of\n"
                "   					a channel or on the a channel header.\n"
                "   \n"
                "   					If the selection is on cell(s) of a channel,\n"
                "   					the formula is applied to only these cells.\n"
                "   \n"
                "   					If the selection is on a channel header, the\n"
                "   					formula is applied to every cell in the channel.\n"
                "   \n"
                "   					The given formula string must be of the form:\n"
                "   					\"<NameOfCurrentChannel>=<SomeExpression>;\"\n"
                "   					e.g. \"x=y+1;\"\n"
                "   				\n\n"

                ":param arg1: Formula (\"<NameOfCurrentChannel>=<SomeExpression>;\")\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("current", &GXEDB_wrap_current,
                "current() -> GXEDB:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the Current Edited Database.\n\n"

                ":returns: EDB Object\n"
                ":rtype: :class:`geosoft.gxapi.GXEDB`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("current");
    pyClass.def("current_no_activate", &GXEDB_wrap_current_no_activate,
                "current_no_activate() -> GXEDB:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the Current Edited Database.\n\n"

                ":returns: EDB Object\n"
                ":rtype: :class:`geosoft.gxapi.GXEDB`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function acts just like \\ :func:`geosoft.gxapi.GXEDB.current`\\  except that the document is not activated (brought to foreground) and no\n"
                "   					guarantee is given about which document is currently active.\n"
                "   				\n\n"
               ).staticmethod("current_no_activate");
    pyClass.def("current_if_exists", &GXEDB_wrap_current_if_exists,
                "current_if_exists() -> GXEDB:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the Current Edited Database.\n\n"

                ":returns: EDB Object to current edited database. If there is no current database,\n"
                "          						the user is not prompted for a database, and 0 is returned.\n"
                ":rtype: :class:`geosoft.gxapi.GXEDB`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("current_if_exists");
    pyClass.def("del_line0", &GXEDB_wrap_del_line0,
                "del_line0() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Delete Line 0.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Deletes an empty line 0 from the database.\n\n"
               );
    pyClass.def("destroy_view", &GXEDB_wrap_destroy_view,
                "destroy_view((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Removes the view from the workspace.\n\n"

                ":param arg1: \\ :ref:`EDB_REMOVE`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Can only be run in interactive mode. After this call the\n"
                "   					EDB object will become invalid. If this is the last view on\n"
                "   					the document and the document has been modified the map will be\n"
                "   					unloaded and optionally saved depending on the \\ :ref:`EDB_REMOVE`\\ \n"
                "   					parameter.\n"
                "   				\n\n"
               );
    pyClass.def("get_cur_chan_symb", &GXEDB_wrap_get_cur_chan_symb,
                "get_cur_chan_symb() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the currently marked channel symbol.\n\n"

                ":returns: Currently channel symbol.\n"
                "          						\\ :ref:`NULLSYMB`\\  if the mark is not in a channel.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_cur_line_symb", &GXEDB_wrap_get_cur_line_symb,
                "get_cur_line_symb() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get current line symbol.\n\n"

                ":returns: Currently displayed line symbol.\n"
                "          						\\ :ref:`NULLSYMB`\\  if no line displayed.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_displ_fid_range", &GXEDB_wrap_get_displ_fid_range,
                "get_displ_fid_range((int_ref)arg1, (int_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Return the displayed fiducial start index & number of cells\n\n"

                ":param arg1: fiducial start\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: number of fiducials\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_fid_range", &GXEDB_wrap_get_fid_range,
                "get_fid_range((float_ref)arg1, (float_ref)arg2, (int_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns currently displayed fid range\n\n"

                ":param arg1: fiducial start\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: fiducial increment\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: number of fiducials\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_next_line_symb", &GXEDB_wrap_get_next_line_symb,
                "get_next_line_symb() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the next line symbol.\n\n"

                ":returns: The next line symbol of currently displayed line.\n"
                "          						\\ :ref:`NULLSYMB`\\  if no line displayed.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_prev_line_symb", &GXEDB_wrap_get_prev_line_symb,
                "get_prev_line_symb() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the previous line symbol.\n\n"

                ":returns: The previous line symbol of currently displayed line.\n"
                "          						\\ :ref:`NULLSYMB`\\  if no line displayed.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_profile_range_x", &GXEDB_wrap_get_profile_range_x,
                "get_profile_range_x((float_ref)arg1, (float_ref)arg2, (int_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get profile X range and X channel\n\n"

                ":param arg1: minimum x\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: maximum x\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: X axis channel, \\ :ref:`NULLSYMB`\\  if none\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_profile_range_y", &GXEDB_wrap_get_profile_range_y,
                "get_profile_range_y((int)arg1, (int)arg2, (float_ref)arg3, (float_ref)arg4, (int_ref)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get profile Y range and display option\n\n"

                ":param arg1: profile window number (0 to MAX_PROF_WND-1, see iProfileOpen_EDB)\n"
                ":type arg1: int\n"
                ":param arg2: profile number in window (see iWindowProfiles_EDB which returns number of profiles in a window)\n"
                ":type arg2: int\n"
                ":param arg3: minimum y\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: maximum y\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: \\ :ref:`EDB_PROFILE_SCALE`\\ \n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_profile_split", &GXEDB_wrap_get_profile_split,
                "get_profile_split((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get profile split for 3 windows.\n\n"

                ":param arg1: split d1 (profile window 0 height / entire profile window height)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: split d2 (profile window 1 height / entire profile window height)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_profile_split5", &GXEDB_wrap_get_profile_split5,
                "get_profile_split5((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get profile split for 5 windows.\n\n"

                ":param arg1: split d1 (profile window 0 height / entire profile window height)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: split d2 (profile window 1 height / entire profile window height)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: split d3 (profile window 2 height / entire profile window height)\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: split d4 (profile window 3 height / entire profile window height)\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_profile_split_vv", &GXEDB_wrap_get_profile_split_vv,
                "get_profile_split_vv((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get profile window splits.\n\n"

                ":param arg1: split VV (REAL) (profile window heights / entire profile window height)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The returned VV is sized to the maximum number of profiles\n"
                "   					that can be displayed. If a profile is not currently displayed,\n"
                "   					its height fraction is 0.  The sum of all the fractions returned\n"
                "   					is equal to 1.\n"
                "   \n"
                "   					The profile splits refers to the relative sizes of the individual\n"
                "   					profile windows. To get/set the fraction of the total database window\n"
                "   					devoted to the profiles, use the \\ :func:`geosoft.gxapi.GXEDB.set_split`\\  and \\ :func:`geosoft.gxapi.GXEDB.get_split`\\  functions.\n"
                "   				\n\n"
               );
    pyClass.def("get_profile_vertical_grid_lines", &GXEDB_wrap_get_profile_vertical_grid_lines,
                "get_profile_vertical_grid_lines((int_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get profile grid vertical line info.\n\n"

                ":param arg1: vertical grid lines?\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: vertical grid interval\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_profile_window", &GXEDB_wrap_get_profile_window,
                "get_profile_window((int)arg1, (int_ref)arg2, (int_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get profile window size\n\n"

                ":param arg1: profile window number (0 to MAX_PROF_WND-1, see iProfileOpen_EDB)\n"
                ":type arg1: int\n"
                ":param arg2: window x size in pixels\n"
                ":type arg2: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg3: window y size in pixels\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("goto_column", &GXEDB_wrap_goto_column,
                "goto_column((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Move the channel marker to a specific column.\n\n"

                ":param arg1: channel column number, 0 is first -1 for first column without data\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("goto_elem", &GXEDB_wrap_goto_elem,
                "goto_elem((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Goto an element in the current line.\n\n"

                ":param arg1: Element number\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("goto_line", &GXEDB_wrap_goto_line,
                "goto_line((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Goto to a line symbol in the editor.\n\n"

                ":param arg1: Line symbol to goto to\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("histogram", &GXEDB_wrap_histogram,
                "histogram((GXST)arg1, (float)arg2, (float)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create histogram stats.\n\n"

                ":param arg1: ST handle to update\n"
                ":type arg1: :class:`geosoft.gxapi.GXST`\n"
                ":param arg2: histogram minimum\n"
                ":type arg2: float\n"
                ":param arg3: histogram increment\n"
                ":type arg3: float\n"
                ":param arg4: number of increments\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("all_chan_list", &GXEDB_wrap_all_chan_list,
                "all_chan_list((GXVV)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of the all channels but in the way they are displayed.\n\n"

                ":param arg1: VV (INT) in which to place the list.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Number of symbols in the list.\n"
                "          						Terminates GX if there was an error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The VV elements must be INT.\n"
                "   \n"
                "   					Displayed channel lists are filled in the order the channels\n"
                "   					appear on the display, left to right.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXEDB.disp_chan_list`\\ \n\n"
               );
    pyClass.def("channels", &GXEDB_wrap_channels,
                "channels() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns number of displayed channels\n\n"

                ":returns: x - number of displayed channels\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("disp_chan_list", &GXEDB_wrap_disp_chan_list,
                "disp_chan_list((GXVV)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of the displayed channel symbols.\n\n"

                ":param arg1: VV (INT) in which to place the list.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Number of symbols in the list.\n"
                "          						Terminates GX if there was an error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The VV elements must be INT.\n"
                "   \n"
                "   					Displayed channel lists are filled in the order the channels\n"
                "   					appear on the display, left to right.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXEDB.disp_chan_lst`\\ \n\n"
               );
    pyClass.def("disp_chan_lst", &GXEDB_wrap_disp_chan_lst,
                "disp_chan_lst((GXLST)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of the displayed channel names.\n\n"

                ":param arg1: LST object\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Number of channels in the list.\n"
                "          						Terminates GX if there was an error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Displayed channel lists are filled in the order the channels\n"
                "   					appear on the display, left to right.\n"
                "   \n"
                "   					The channel names will be placed in the \"Name\" part of\n"
                "   					the list and the values are set to the symbol handle.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXEDB.disp_chan_list`\\ \n\n"
               );
    pyClass.def("disp_class_chan_lst", &GXEDB_wrap_disp_class_chan_lst,
                "disp_class_chan_lst((GXLST)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of the displayed channels in a given channel class.\n\n"

                ":param arg1: LST object\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: class name (\"\" for all)\n"
                ":type arg2: str\n"
                ":returns: Number of channels in the list.\n"
                "          						Terminates GX if there was an error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Displayed channel lists are filled in the order the channels\n"
                "   					appear on the display, left to right.\n"
                "   \n"
                "   					The channel names will be placed in the \"Name\" part of\n"
                "   					the list and the values are set to the symbol handle.\n"
                "   \n"
                "   					Examples of channel classes in current use are \"MASK\" and\n"
                "   					\"ASSAY\". (Searches are case tolerant).\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXEDB.disp_chan_list`\\ \n\n"
               );
    pyClass.def("find_channel_column", &GXEDB_wrap_find_channel_column,
                "find_channel_column((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the column that contains a channel\n\n"

                ":param arg1: channel\n"
                ":type arg1: str\n"
                ":returns: Column number that contains a specific channel\n"
                "          						iDUMMY of channel not loaded\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("find_nearest", &GXEDB_wrap_find_nearest,
                "find_nearest((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (GXIPJ)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Find the nearest point on the current line based\n"
                "   					on X,Y and Z and their projection.\n"
                "   				\n\n"

                ":param arg1: X - Modified with true point\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y - Modified with true point\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Z - Modified with true point\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Projection of X,Y,Z\n"
                ":type arg4: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: x - Nearest point\n"
                "          						-1 - Not available\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_cur_chan", &GXEDB_wrap_get_cur_chan,
                "get_cur_chan((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get current channel name.\n\n"

                ":param arg1: Where to put the name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   returns \"\" if mark not currently in a channel.\n\n"
               );
    pyClass.def("get_cur_fid_string", &GXEDB_wrap_get_cur_fid_string,
                "get_cur_fid_string((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method returns the currently selected value\n"
                "   					at the current fid (if available).\n"
                "   				\n\n"

                ":param arg1: String returned here\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_cur_line", &GXEDB_wrap_get_cur_line,
                "get_cur_line((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get current line name.\n\n"

                ":param arg1: Where to put the name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_cur_mark", &GXEDB_wrap_get_cur_mark,
                "get_cur_mark((float_ref)arg1, (float_ref)arg2, (float_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the current data mark info.\n\n"

                ":param arg1: start fiducial\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: end fiducial\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: fiducial increment\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 - if data is marked.\n"
                "          						1 - if data is not currently marked.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_current_selection", &GXEDB_wrap_get_current_selection,
                "get_current_selection((str_ref)arg1, (str_ref)arg2, (str_ref)arg3, (str_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get current selection information.\n\n"

                ":param arg1: Database name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: Name of Selected channel\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Selected lines buffer\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg4: Fiducial range\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Channel Name    Empty if no channel\n"
                "   					Line Name       \"[All]\" if all lines are selected\n"
                "   					Fid Range       \"[All]\" if all values in all lines are selected\n"
                "   					\"[None]\"  if no values are selected\n"
                "   					\"10 to 20\"  giving the range of values.\n"
                "   				\n\n"
               );
    pyClass.def("get_databases_lst", &GXEDB_wrap_get_databases_lst,
                "get_databases_lst((GXLST)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Load the file names of open databases into a LST.\n\n"

                ":param arg1: LST to load\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`EDB_PATH`\\ \n"
                ":type arg2: int\n"
                ":returns: The number of documents loaded into the LST.\n"
                "          						The LST is cleared first.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_databases_lst");
    pyClass.def("get_mark_chan_vv", &GXEDB_wrap_get_mark_chan_vv,
                "get_mark_chan_vv((GXVV)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get channel data for the current mark.\n\n"

                ":param arg1: VV in which to place the data.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Channel symbol to retrieve.\n"
                ":type arg2: int\n"
                ":returns: 0 if successful.\n"
                "          						1 if failed, or if entire database is marked.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The current \"mark\" in this case is the start and\n"
                "   					end fiducials and not the selected channel. You\n"
                "   					can use this method to retrieve the selected range\n"
                "   					from any channel, loaded or not.\n"
                "   \n"
                "   					The VV will be resized to the length of the data\n"
                "   				\n\n"
               );
    pyClass.def("get_mark_chan_va", &GXEDB_wrap_get_mark_chan_va,
                "get_mark_chan_va((GXVA)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get channel data for the current mark.\n\n"

                ":param arg1: VA in which to place the data.\n"
                ":type arg1: :class:`geosoft.gxapi.GXVA`\n"
                ":param arg2: Channel symbol to retrieve.\n"
                ":type arg2: int\n"
                ":returns: 0 if successful.\n"
                "                      1 if failed, or if entire database is marked.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "             The current \"mark\" in this case is the start and\n"
                "             end fiducials and not the selected channel. You\n"
                "             can use this method to retrieve the selected range\n"
                "             from any channel, loaded or not.\n"
                "   \n"
                "             The VA will be resized to the length of the data\n"
                "           \n\n"
               );
    pyClass.def("get_name", &GXEDB_wrap_get_name,
                "get_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the name of the database object of this EDB.\n\n"

                ":param arg1: Name returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_profile_parm_int", &GXEDB_wrap_get_profile_parm_int,
                "get_profile_parm_int((int)arg1, (int)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get integer profile parameter\n\n"

                ":param arg1: profile window number (0 to MAX_PROF_WND-1, see iProfileOpen_EDB)\n"
                ":type arg1: int\n"
                ":param arg2: profile number in window (see GetProfileRangeY_EDB)\n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`EDB_PROF`\\ \n"
                ":type arg3: int\n"
                ":returns: Data Value (See notes)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_window_state", &GXEDB_wrap_get_window_state,
                "get_window_state() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve the current state of the database window\n\n"

                ":returns: \\ :ref:`EDB_WINDOW_STATE`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("have_current", &GXEDB_wrap_have_current,
                "have_current() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns true if a database is loaded\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("have_current");
    pyClass.def("is_locked", &GXEDB_wrap_is_locked,
                "is_locked() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this Database locked\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("loaded", &GXEDB_wrap_loaded,
                "loaded((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns 1 if a database is loaded .\n\n"

                ":param arg1: database name\n"
                ":type arg1: str\n"
                ":returns: 1 if database is loaded, 0 otherwise.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("loaded");
    pyClass.def("profile_open", &GXEDB_wrap_profile_open,
                "profile_open((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Return TRUE or FALSE if profile window is open\n\n"

                ":param arg1: profile window number: 0 is the top window 1 is the middle window 2 is the bottom window\n"
                ":type arg1: int\n"
                ":returns: TRUE if window is open\n"
                "          						FALSE if window is closed\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This functions will return FALSE if requested window\n"
                "   					is not supported in current version of Oasis montaj.\n"
                "   				\n\n"
               );
    pyClass.def("read_only", &GXEDB_wrap_read_only,
                "read_only() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Checks if a database is currently opened in a read-only mode.\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_window_position", &GXEDB_wrap_get_window_position,
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
                ":param arg5: Window state \\ :ref:`EDB_WINDOW_STATE`\\ \n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Docked or floating \\ :ref:`EDB_WINDOW_POSITION`\\ \n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               );
    pyClass.def("set_window_position", &GXEDB_wrap_set_window_position,
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
                ":param arg5: Window state \\ :ref:`EDB_WINDOW_STATE`\\ \n"
                ":type arg5: int\n"
                ":param arg6: Docked or floating \\ :ref:`EDB_WINDOW_POSITION`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               );
    pyClass.def("show_profile_name", &GXEDB_wrap_show_profile_name,
                "show_profile_name((int)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Show a profile in the profile window\n\n"

                ":param arg1: profile window number (0 to MAX_PROF_WND-1, see iProfileOpen_EDB)\n"
                ":type arg1: int\n"
                ":param arg2: Name of the channel\n"
                ":type arg2: str\n"
                ":returns: Profile ID if loaded, -1 for error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the symbol is not loaded, it will be loaded.\n\n"
               );
    pyClass.def("get_window_y_axis_direction", &GXEDB_wrap_get_window_y_axis_direction,
                "get_window_y_axis_direction((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the y-axis direction for a window\n\n"

                ":param arg1: profile window number (0 to MAX_PROF_WND-1, see iProfileOpen_EDB)\n"
                ":type arg1: int\n"
                ":returns: \\ :ref:`EDB_YAXIS_DIRECTION`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"
               );
    pyClass.def("window_profiles", &GXEDB_wrap_window_profiles,
                "window_profiles((int)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get number of profiles in a window\n\n"

                ":param arg1: profile window number (0 to MAX_PROF_WND-1, see iProfileOpen_EDB)\n"
                ":type arg1: int\n"
                ":returns: Number of profiles in a window\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("launch_histogram", &GXEDB_wrap_launch_histogram,
                "launch_histogram((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch histogram tool on a database.\n\n"

                ":param arg1: First chan name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.6\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXCHIMERA.launch_histogram`\\  in chimera.gxh\n\n"
               );
    pyClass.def("launch_scatter", &GXEDB_wrap_launch_scatter,
                "launch_scatter() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch scatter tool on a database.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.6\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The scatter tool uses the following INI parameters\n"
                "   \n"
                "   					SCATTER.STM       name of the scatter template,\"none\" for none\n"
                "   					SCATTER.STM_NAME  name of last template section, \"\" for none.\n"
                "   					SCATTER.X         name of channel to display in X\n"
                "   					SCATTER.Y         name of channel to display in Y\n"
                "   					SCATTER.MASK      name of channel to use for mask\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXCHIMERA.launch_scatter`\\  in chimera.gxh\n\n"
               );
    pyClass.def("load", &GXEDB_wrap_load,
                "load((str)arg1) -> GXEDB:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads a list of databases into the workspace\n\n"

                ":param arg1: list of databases (';' or '\\ `|`\\ ' delimited) to load.\n"
                ":type arg1: str\n"
                ":returns: Handle to current edited database, which will be the last\n"
                "          						database in the list.\n"
                ":rtype: :class:`geosoft.gxapi.GXEDB`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The last listed database will become the current database.\n"
                "   \n"
                "   					Databases may already be loaded.\n"
                "   \n"
                "   					Only the first file in the list may have a directory path.\n"
                "   					All other files in the list are assumed to be in the same\n"
                "   					directory as the first file.\n"
                "   				\n\n"
               ).staticmethod("load");
    pyClass.def("load_no_activate", &GXEDB_wrap_load_no_activate,
                "load_no_activate((str)arg1) -> GXEDB:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads documents into the workspace\n\n"

                ":param arg1: list of documents (';' or '\\ `|`\\ ' delimited) to load.\n"
                ":type arg1: str\n"
                ":returns: Handle to current edited document, which will be the last\n"
                "          						database in the list if multiple files were provided.\n"
                ":rtype: :class:`geosoft.gxapi.GXEDB`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function acts just like \\ :func:`geosoft.gxapi.GXEDB.load`\\  except that the document(s) is not activated (brought to foreground) and no\n"
                "   					guarantee is given about which document is currently active.\n"
                "   				\n\n"
               ).staticmethod("load_no_activate");
    pyClass.def("load_all_chans", &GXEDB_wrap_load_all_chans,
                "load_all_chans() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load all channels into current database\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("load_chan", &GXEDB_wrap_load_chan,
                "load_chan((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a channel into current database\n\n"

                ":param arg1: channel name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the channel does not exist, or if channel is already\n"
                "   					loaded nothing happens.\n"
                "   				\n\n"
               );
    pyClass.def("load_new", &GXEDB_wrap_load_new,
                "load_new((str)arg1) -> GXEDB:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads a database into the workspace, flags as new.\n\n"

                ":param arg1: Database to load.\n"
                ":type arg1: str\n"
                ":returns: Handle to the current edited database.\n"
                ":rtype: :class:`geosoft.gxapi.GXEDB`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					See \\ :func:`geosoft.gxapi.GXEDB.load`\\ . This is used for brand new databases, to set\n"
                "   					an internal flag such that if on closing the user chooses\n"
                "   					not to save changes, the database is deleted.\n"
                "   				\n\n"
               ).staticmethod("load_new");
    pyClass.def("load_pass", &GXEDB_wrap_load_pass,
                "load_pass((str)arg1, (str)arg2, (str)arg3) -> GXEDB:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads a database into the editor with login and password.\n\n"

                ":param arg1: Name of database to load\n"
                ":type arg1: str\n"
                ":param arg2: Login Name\n"
                ":type arg2: str\n"
                ":param arg3: Password\n"
                ":type arg3: str\n"
                ":returns: Handle to current edited database.\n"
                ":rtype: :class:`geosoft.gxapi.GXEDB`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The loaded database will become the current database.\n"
                "   \n"
                "   					If the database is already loaded, it simply becomes\n"
                "   					the current database.\n"
                "   				\n\n"
               ).staticmethod("load_pass");
    pyClass.def("load_with_view", &GXEDB_wrap_load_with_view,
                "load_with_view((str)arg1, (GXEDB)arg2) -> GXEDB:\n"

                "\n.. parsed-literal::\n\n"
                "   Load an EDB with the view from a current EDB.\n\n"

                ":param arg1: Source DB name\n"
                ":type arg1: str\n"
                ":param arg2: EDB to use as the source view\n"
                ":type arg2: :class:`geosoft.gxapi.GXEDB`\n"
                ":returns: New EDB handle.\n"
                ":rtype: :class:`geosoft.gxapi.GXEDB`\n"
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
    pyClass.def("lock", &GXEDB_wrap_lock,
                "lock() -> GXDB:\n"

                "\n.. parsed-literal::\n\n"
                "   This method locks the Edited Database.\n\n"

                ":returns: Handle to database associated with edited database.\n"
                ":rtype: :class:`geosoft.gxapi.GXDB`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("make_current", &GXEDB_wrap_make_current,
                "make_current() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Makes this EDB object the current active object to the user.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("remove_profile", &GXEDB_wrap_remove_profile,
                "remove_profile((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Remove a profile from the profile window\n\n"

                ":param arg1: profile window number (0 to MAX_PROF_WND-1, see iProfileOpen_EDB)\n"
                ":type arg1: int\n"
                ":param arg2: profile number in window (see GetProfileRangeY_EDB)\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_cur_fid", &GXEDB_wrap_get_cur_fid,
                "get_cur_fid() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This method returns the currently selected fiducial if\n"
                "   					the user is selecting a fiducial. If not, it returns\n"
                "   					a dummy.\n"
                "   				\n\n"

                ":returns: x     - Fiducial\n"
                "          						DUMMY - No Selected Fiducial\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_profile_parm_double", &GXEDB_wrap_get_profile_parm_double,
                "get_profile_parm_double((int)arg1, (int)arg2, (int)arg3) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get real profile parameter\n\n"

                ":param arg1: profile window number (0 to MAX_PROF_WND-1, see iProfileOpen_EDB)\n"
                ":type arg1: int\n"
                ":param arg2: profile number in window (see GetProfileRangeY_EDB)\n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`EDB_PROF`\\ \n"
                ":type arg3: int\n"
                ":returns: Real profile parameter\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_split", &GXEDB_wrap_get_split,
                "get_split() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get split ratio between spreadsheet and profile sections.\n\n"

                ":returns: d = (spreadsheet window height/\n"
                "          						(spreadsheet window height + entire profile window height))\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("run_channel_maker", &GXEDB_wrap_run_channel_maker,
                "run_channel_maker((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Run the maker for a single channel.\n\n"

                ":param arg1: channel name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Skips channels without makers; will not return an\n"
                "   					error if the channel does not exist.\n"
                "   				\n\n"
               );
    pyClass.def("run_channel_makers", &GXEDB_wrap_run_channel_makers,
                "run_channel_makers() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Recreate channels with makers.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Skips channels without makers.\n\n"
               );
    pyClass.def("set_cur_line", &GXEDB_wrap_set_cur_line,
                "set_cur_line((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the current line name.\n\n"

                ":param arg1: line name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_cur_line_no_message", &GXEDB_wrap_set_cur_line_no_message,
                "set_cur_line_no_message((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set Line but do not send a message.\n\n"

                ":param arg1: line name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_cur_mark", &GXEDB_wrap_set_cur_mark,
                "set_cur_mark((float)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the current mark.\n\n"

                ":param arg1: start fiducial\n"
                ":type arg1: float\n"
                ":param arg2: end fiducial\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_profile_parm_i", &GXEDB_wrap_set_profile_parm_i,
                "set_profile_parm_i((int)arg1, (int)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set integer profile parameter\n\n"

                ":param arg1: profile window number (0 to MAX_PROF_WND-1, see iProfileOpen_EDB)\n"
                ":type arg1: int\n"
                ":param arg2: profile number in window (see GetProfileRangeY_EDB)\n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`EDB_PROF`\\ \n"
                ":type arg3: int\n"
                ":param arg4: setting\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_profile_parm_r", &GXEDB_wrap_set_profile_parm_r,
                "set_profile_parm_r((int)arg1, (int)arg2, (int)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set real profile parameter\n\n"

                ":param arg1: profile window number (0 to MAX_PROF_WND-1, see iProfileOpen_EDB)\n"
                ":type arg1: int\n"
                ":param arg2: profile number in window (see GetProfileRangeY_EDB)\n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`EDB_PROF`\\ \n"
                ":type arg3: int\n"
                ":param arg4: setting\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_profile_range_x", &GXEDB_wrap_set_profile_range_x,
                "set_profile_range_x((float)arg1, (float)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set profile X range and X channel\n\n"

                ":param arg1: minimum x, rDUMMY for data minimum\n"
                ":type arg1: float\n"
                ":param arg2: maximum x, rDUMMY for data maximum\n"
                ":type arg2: float\n"
                ":param arg3: X axis channel, \\ :ref:`NULLSYMB`\\  to use fids\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_profile_range_y", &GXEDB_wrap_set_profile_range_y,
                "set_profile_range_y((int)arg1, (int)arg2, (float)arg3, (float)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set profile Y range and display option\n\n"

                ":param arg1: profile window number (0 to MAX_PROF_WND-1, see iProfileOpen_EDB)\n"
                ":type arg1: int\n"
                ":param arg2: profile number in window (see GetProfileRangeY_EDB)\n"
                ":type arg2: int\n"
                ":param arg3: minimum y\n"
                ":type arg3: float\n"
                ":param arg4: maximum y\n"
                ":type arg4: float\n"
                ":param arg5: \\ :ref:`EDB_PROFILE_SCALE`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If channel is not loaded or displayed, it will\n"
                "   					loaded and/or displayed.\n"
                "   				\n\n"
               );
    pyClass.def("set_profile_split", &GXEDB_wrap_set_profile_split,
                "set_profile_split((float)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set profile split for 3 windows.\n\n"

                ":param arg1: split d1 (profile window 0 height / entire profile window height)\n"
                ":type arg1: float\n"
                ":param arg2: split d2 (profile window 1 height / entire profile window height)\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_profile_split5", &GXEDB_wrap_set_profile_split5,
                "set_profile_split5((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set profile split for 5 windows.\n\n"

                ":param arg1: split d1 (profile window 0 height / entire profile window height)\n"
                ":type arg1: float\n"
                ":param arg2: split d2 (profile window 1 height / entire profile window height)\n"
                ":type arg2: float\n"
                ":param arg3: split d3 (profile window 2 height / entire profile window height)\n"
                ":type arg3: float\n"
                ":param arg4: split d4 (profile window 3 height / entire profile window height)\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_profile_split_vv", &GXEDB_wrap_set_profile_split_vv,
                "set_profile_split_vv((GXVV)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set profile splits\n\n"

                ":param arg1: split VV (REAL) (relative sizes of each profile window)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The input VV values are the fractional heights for each\n"
                "   					profile window. Values are summed, and normalized (so you can\n"
                "   					enter \"1,1,1\", with a VV of length 3, if you want 3 equal profile windows).\n"
                "   \n"
                "   					VV values beyond the maximum number of displayable\n"
                "   					profiles (MAX_PROF_WND) are ignored.\n"
                "   				\n\n"
               );
    pyClass.def("set_split", &GXEDB_wrap_set_split,
                "set_split((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set split ratio between spreadsheet and profile sections.\n\n"

                ":param arg1: split d (0.0 <= d <= 1.0).\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					d = (spreadsheet window height/\n"
                "   					(spreadsheet window height + entire profile window height))\n"
                "   				\n\n"
               );
    pyClass.def("set_window_state", &GXEDB_wrap_set_window_state,
                "set_window_state((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Changes the state of the database window\n\n"

                ":param arg1: \\ :ref:`EDB_WINDOW_STATE`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("show_profile", &GXEDB_wrap_show_profile,
                "show_profile((int)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Show a profile in the profile window\n\n"

                ":param arg1: profile window number (0 to MAX_PROF_WND-1, see iProfileOpen_EDB)\n"
                ":type arg1: int\n"
                ":param arg2: channel symbol\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the symbol is not loaded, it will be loaded.\n\n"
               );
    pyClass.def("statistics", &GXEDB_wrap_statistics,
                "statistics((GXST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add all currently selected data to the ST.\n\n"

                ":param arg1: ST handle to update\n"
                ":type arg1: :class:`geosoft.gxapi.GXST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Use \\ :func:`geosoft.gxapi.GXEDB.histogram`\\  to get median or histogram.\n\n"
               );
    pyClass.def("un_load", &GXEDB_wrap_un_load,
                "un_load((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unloads an edited database.\n\n"

                ":param arg1: Name of database to unload\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the database is not loaded, nothing happens.\n"
                "   					Same as \\ :func:`geosoft.gxapi.GXEDB.un_load_verify`\\  with FALSE to prompt save.\n"
                "   				\n\n"
               ).staticmethod("un_load");
    pyClass.def("un_load_all", &GXEDB_wrap_un_load_all,
                "un_load_all() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unloads all opened databases\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("un_load_all");
    pyClass.def("un_load_all_chans", &GXEDB_wrap_un_load_all_chans,
                "un_load_all_chans() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unload all channels into current database\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("un_load_chan", &GXEDB_wrap_un_load_chan,
                "un_load_chan((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unload a channel into current database\n\n"

                ":param arg1: channel name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the channel does not exist, or if channel is already\n"
                "   					loaded nothing happens.\n"
                "   				\n\n"
               );
    pyClass.def("un_load_discard", &GXEDB_wrap_un_load_discard,
                "un_load_discard((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unloads a database in the workspace, discards changes.\n\n"

                ":param arg1: Name of database to unload\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the database is not loaded, nothing happens.\n\n"
               ).staticmethod("un_load_discard");
    pyClass.def("un_load_verify", &GXEDB_wrap_un_load_verify,
                "un_load_verify((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unloads an edited database, optional prompt to save.\n\n"

                ":param arg1: Name of database to unload\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`EDB_UNLOAD`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the database is not loaded, nothing happens.\n"
                "   					The user can be prompted to save before unloading.\n"
                "   					If EDB_UNLOAD_NO_PROMPT, data is always saved.\n"
                "   					EDB_UNLOAD_MULTIPROMPT is now obsolete and\n"
                "   					is equivalent to EDB_UNLOAD_SINGLE_PROMPT.\n"
                "   				\n\n"
               ).staticmethod("un_load_verify");
    pyClass.def("un_lock", &GXEDB_wrap_un_lock,
                "un_lock() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method unlocks the Edited Database.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );

    scope().attr("MAX_PROF_WND") = (int32_t)5;
    scope().attr("EDB_PATH_FULL") = (int32_t)0;
    scope().attr("EDB_PATH_DIR") = (int32_t)1;
    scope().attr("EDB_PATH_NAME_EXT") = (int32_t)2;
    scope().attr("EDB_PATH_NAME") = (int32_t)3;
    scope().attr("EDB_PROF_I_CHANNEL") = (int32_t)0;
    scope().attr("EDB_PROF_I_LINE_STYLE") = (int32_t)1;
    scope().attr("EDB_PROF_I_LINE_WEIGHT") = (int32_t)2;
    scope().attr("EDB_PROF_I_SYMBOL") = (int32_t)3;
    scope().attr("EDB_PROF_I_SYMBOL_WEIGHT") = (int32_t)4;
    scope().attr("EDB_PROF_I_COLOR") = (int32_t)5;
    scope().attr("EDB_PROF_I_WRAP") = (int32_t)6;
    scope().attr("EDB_PROF_I_BREAK_ON_DUMMY") = (int32_t)7;
    scope().attr("EDB_PROF_I_GRID_LINE") = (int32_t)8;
    scope().attr("EDB_PROF_R_GRID_LINE_INTERVAL") = (int32_t)9;
    scope().attr("EDB_PROF_I_LOG") = (int32_t)10;
    scope().attr("EDB_PROF_R_LOG_MINIMUM") = (int32_t)11;
    scope().attr("EDB_PROF_I_SAMESCALE") = (int32_t)12;
    scope().attr("EDB_PROF_I_SOURCELINE") = (int32_t)13;
    scope().attr("EDB_PROF_I_SCALEOPTION") = (int32_t)14;
    scope().attr("EDB_PROF_I_SAMERANGE") = (int32_t)15;
    scope().attr("EDB_PROFILE_SCALE_LINEAR") = (int32_t)0;
    scope().attr("EDB_PROFILE_SCALE_LOG") = (int32_t)1;
    scope().attr("EDB_PROFILE_SCALE_LOGLINEAR") = (int32_t)2;
    scope().attr("EDB_REMOVE_SAVE") = (int32_t)0;
    scope().attr("EDB_REMOVE_PROMPT") = (int32_t)1;
    scope().attr("EDB_REMOVE_DISCARD") = (int32_t)2;
    scope().attr("EDB_UNLOAD_NO_PROMPT") = (int32_t)0;
    scope().attr("EDB_UNLOAD_SINGLE_PROMPT") = (int32_t)1;
    scope().attr("EDB_UNLOAD_MULTI_PROMPT") = (int32_t)2;
    scope().attr("EDB_WINDOW_POSITION_DOCKED") = (int32_t)0;
    scope().attr("EDB_WINDOW_POSITION_FLOATING") = (int32_t)1;
    scope().attr("EDB_WINDOW_RESTORE") = (int32_t)0;
    scope().attr("EDB_WINDOW_MINIMIZE") = (int32_t)1;
    scope().attr("EDB_WINDOW_MAXIMIZE") = (int32_t)2;
    scope().attr("EDB_YAXIS_NORMAL") = (int32_t)0;
    scope().attr("EDB_YAXIS_INVERTED") = (int32_t)1;

}
