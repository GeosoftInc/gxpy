#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline bool GXEMAPTEMPLATE_wrap_drag_drop_enabled(GXEMAPTEMPLATEPtr self)
{
    bool ret = self->drag_drop_enabled();
    return ret;
}
inline void GXEMAPTEMPLATE_wrap_set_drag_drop_enabled(GXEMAPTEMPLATEPtr self, bool arg1)
{
    self->set_drag_drop_enabled(arg1);
}
inline GXEMAPTEMPLATEPtr GXEMAPTEMPLATE_wrap_current()
{
    GXEMAPTEMPLATEPtr ret = GXEMAPTEMPLATE::current();
    return ret;
}
inline GXEMAPTEMPLATEPtr GXEMAPTEMPLATE_wrap_current_no_activate()
{
    GXEMAPTEMPLATEPtr ret = GXEMAPTEMPLATE::current_no_activate();
    return ret;
}
inline GXEMAPTEMPLATEPtr GXEMAPTEMPLATE_wrap_current_if_exists()
{
    GXEMAPTEMPLATEPtr ret = GXEMAPTEMPLATE::current_if_exists();
    return ret;
}
inline int32_t GXEMAPTEMPLATE_wrap_get_map_templates_lst(GXLSTPtr arg1, int32_t arg2)
{
    int32_t ret = GXEMAPTEMPLATE::get_map_templates_lst(arg1, (EMAPTEMPLATE_PATH)arg2);
    return ret;
}
inline void GXEMAPTEMPLATE_wrap_get_name(GXEMAPTEMPLATEPtr self, str_ref& arg1)
{
    self->get_name(arg1);
}
inline int32_t GXEMAPTEMPLATE_wrap_have_current()
{
    int32_t ret = GXEMAPTEMPLATE::have_current();
    return ret;
}
inline int32_t GXEMAPTEMPLATE_wrap_i_get_specified_map_name(const gx_string_type& arg1, const gx_string_type& arg2, str_ref& arg3)
{
    int32_t ret = GXEMAPTEMPLATE::i_get_specified_map_name(arg1, arg2, arg3);
    return ret;
}
inline bool GXEMAPTEMPLATE_wrap_is_locked(GXEMAPTEMPLATEPtr self)
{
    bool ret = self->is_locked();
    return ret;
}
inline int32_t GXEMAPTEMPLATE_wrap_loaded(const gx_string_type& arg1)
{
    int32_t ret = GXEMAPTEMPLATE::loaded(arg1);
    return ret;
}
inline void GXEMAPTEMPLATE_wrap_get_window_position(GXEMAPTEMPLATEPtr self, int_ref& arg1, int_ref& arg2, int_ref& arg3, int_ref& arg4, int_ref& arg5, int_ref& arg6)
{
    self->get_window_position(arg1, arg2, arg3, arg4, (EMAPTEMPLATE_WINDOW_STATE&)arg5, (EMAPTEMPLATE_WINDOW_POSITION&)arg6);
}
inline void GXEMAPTEMPLATE_wrap_set_window_position(GXEMAPTEMPLATEPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    self->set_window_position(arg1, arg2, arg3, arg4, (EMAPTEMPLATE_WINDOW_STATE)arg5, (EMAPTEMPLATE_WINDOW_POSITION)arg6);
}
inline bool GXEMAPTEMPLATE_wrap_read_only(GXEMAPTEMPLATEPtr self)
{
    bool ret = self->read_only();
    return ret;
}
inline GXEMAPTEMPLATEPtr GXEMAPTEMPLATE_wrap_load(const gx_string_type& arg1)
{
    GXEMAPTEMPLATEPtr ret = GXEMAPTEMPLATE::load(arg1);
    return ret;
}
inline GXEMAPTEMPLATEPtr GXEMAPTEMPLATE_wrap_load_no_activate(const gx_string_type& arg1)
{
    GXEMAPTEMPLATEPtr ret = GXEMAPTEMPLATE::load_no_activate(arg1);
    return ret;
}
inline GXMAPTEMPLATEPtr GXEMAPTEMPLATE_wrap_lock(GXEMAPTEMPLATEPtr self)
{
    GXMAPTEMPLATEPtr ret = self->lock();
    return ret;
}
inline void GXEMAPTEMPLATE_wrap_make_current(GXEMAPTEMPLATEPtr self)
{
    self->make_current();
}
inline void GXEMAPTEMPLATE_wrap_un_load(const gx_string_type& arg1)
{
    GXEMAPTEMPLATE::un_load(arg1);
}
inline void GXEMAPTEMPLATE_wrap_un_load_all()
{
    GXEMAPTEMPLATE::un_load_all();
}
inline void GXEMAPTEMPLATE_wrap_un_load_verify(const gx_string_type& arg1, bool arg2)
{
    GXEMAPTEMPLATE::un_load_verify(arg1, arg2);
}
inline void GXEMAPTEMPLATE_wrap_un_lock(GXEMAPTEMPLATEPtr self)
{
    self->un_lock();
}
inline int32_t GXEMAPTEMPLATE_wrap_get_box(GXEMAPTEMPLATEPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    int32_t ret = self->get_box(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline int32_t GXEMAPTEMPLATE_wrap_get_line(GXEMAPTEMPLATEPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    int32_t ret = self->get_line(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline int32_t GXEMAPTEMPLATE_wrap_get_point(GXEMAPTEMPLATEPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3)
{
    int32_t ret = self->get_point(arg1, arg2, arg3);
    return ret;
}
inline int32_t GXEMAPTEMPLATE_wrap_get_rect(GXEMAPTEMPLATEPtr self, const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5)
{
    int32_t ret = self->get_rect(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline int32_t GXEMAPTEMPLATE_wrap_track_point(GXEMAPTEMPLATEPtr self, int32_t arg1, float_ref& arg2, float_ref& arg3)
{
    int32_t ret = self->track_point((EMAPTEMPLATE_TRACK)arg1, arg2, arg3);
    return ret;
}
inline bool GXEMAPTEMPLATE_wrap_get_item_selection(GXEMAPTEMPLATEPtr self, str_ref& arg1)
{
    bool ret = self->get_item_selection(arg1);
    return ret;
}
inline void GXEMAPTEMPLATE_wrap_set_item_selection(GXEMAPTEMPLATEPtr self, const gx_string_type& arg1)
{
    self->set_item_selection(arg1);
}
inline void GXEMAPTEMPLATE_wrap_get_display_area(GXEMAPTEMPLATEPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4)
{
    self->get_display_area(arg1, arg2, arg3, arg4);
}
inline void GXEMAPTEMPLATE_wrap_get_template_layout_props(GXEMAPTEMPLATEPtr self, bool_ref& arg1, float_ref& arg2, int_ref& arg3, int_ref& arg4, int_ref& arg5, int_ref& arg6, int_ref& arg7, int_ref& arg8)
{
    self->get_template_layout_props(arg1, arg2, arg3, arg4, (LAYOUT_VIEW_UNITS&)arg5, arg6, arg7, arg8);
}
inline int32_t GXEMAPTEMPLATE_wrap_get_window_state(GXEMAPTEMPLATEPtr self)
{
    EMAPTEMPLATE_WINDOW_STATE ret = self->get_window_state();
    return ret;
}
inline void GXEMAPTEMPLATE_wrap_set_display_area(GXEMAPTEMPLATEPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->set_display_area(arg1, arg2, arg3, arg4);
}
inline void GXEMAPTEMPLATE_wrap_set_template_layout_props(GXEMAPTEMPLATEPtr self, bool arg1, double arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6, int32_t arg7, int32_t arg8)
{
    self->set_template_layout_props(arg1, arg2, arg3, arg4, (LAYOUT_VIEW_UNITS)arg5, arg6, arg7, arg8);
}
inline void GXEMAPTEMPLATE_wrap_set_window_state(GXEMAPTEMPLATEPtr self, int32_t arg1)
{
    self->set_window_state((EMAPTEMPLATE_WINDOW_STATE)arg1);
}
inline GXEMAPTEMPLATEPtr GXEMAPTEMPLATE_wrap_create_virtual(const gx_string_type& arg1)
{
    GXEMAPTEMPLATEPtr ret = GXEMAPTEMPLATE::create_virtual(arg1);
    return ret;
}

void gxPythonImportGXEMAPTEMPLATE()
{

    class_<GXEMAPTEMPLATE, GXEMAPTEMPLATEPtr> pyClass("GXEMAPTEMPLATE",
            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		The EMAPTEMPLATE class provides access to a map template as displayed within\n"
            "   Oasis montaj, but does not change data within the template itself.\n"
            "   It performs functions such as setting the currently displayed area,\n"
            "   or drawing \"tracking\" lines or boxes on the template (which are not\n"
            "   part of the template itself).\n"
            "   	\n\n"

            "\n\n**Note:**\n\n"

            "\n.. parsed-literal::\n\n"
            "   \n"
            "   		To obtain access to the map template itself, it is recommended practice\n"
            "   to begin with an EMAPTEMPLATE object, and use the Lock function to\n"
            "   lock the underlying template to prevent external changes. The returned\n"
            "   MAPTEMPLATE object may then be safely used to make changes to the template itself.\n"
            "   \n"
            "   VIRTUAL EMAPTEMPLATE SUPPORT\n"
            "   \n"
            "   These methods are only available when running in an external application.\n"
            "   They allow the GX to open a map template and then create a Virtual EMAPTEMPLATE from that\n"
            "   map template. The GX can then call MakeCurrent and set the current EMAPTEMPLATE so\n"
            "   that code that follows sees this map template as the current MAPTEMPLATE.\n"
            "   \n"
            "   Supported methods on Virtual EMAPTEMPLATEs are:\n"
            "   \n"
            "     \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.current`\\ \n"
            "     \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.current_no_activate`\\ \n"
            "     \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.make_current`\\ \n"
            "     \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.have_current`\\ \n"
            "     \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.current_if_exists`\\ \n"
            "   \n"
            "     \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.lock`\\ \n"
            "     \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.un_lock`\\ \n"
            "   \n"
            "     \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.get_name`\\ \n"
            "   \n"
            "     \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.loaded`\\ \n"
            "     \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.load`\\ \n"
            "     \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.load_no_activate`\\ \n"
            "     \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.un_load_verify`\\ \n"
            "     \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.un_load`\\ \n"
            "   \n"
            "     \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.create_virtual`\\ \n"
            "   	\n\n"
            , no_init);

    pyClass.def("null", &GXEMAPTEMPLATE::null, "null() -> GXEMAPTEMPLATE\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXEMAPTEMPLATE`\n\n:returns: A null :class:`geosoft.gxapi.GXEMAPTEMPLATE`\n:rtype: :class:`geosoft.gxapi.GXEMAPTEMPLATE`\n").staticmethod("null");
    pyClass.def("is_null", &GXEMAPTEMPLATE::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXEMAPTEMPLATE is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXEMAPTEMPLATE`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXEMAPTEMPLATE::_internal_handle);
    pyClass.def("drag_drop_enabled", &GXEMAPTEMPLATE_wrap_drag_drop_enabled,
                "drag_drop_enabled() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Is drag-and-drop enabled for the map?\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_drag_drop_enabled", &GXEMAPTEMPLATE_wrap_set_drag_drop_enabled,
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
    pyClass.def("current", &GXEMAPTEMPLATE_wrap_current,
                "current() -> GXEMAPTEMPLATE:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the Current Edited map template.\n\n"

                ":returns: EMAPTEMPLATE Object\n"
                ":rtype: :class:`geosoft.gxapi.GXEMAPTEMPLATE`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("current");
    pyClass.def("current_no_activate", &GXEMAPTEMPLATE_wrap_current_no_activate,
                "current_no_activate() -> GXEMAPTEMPLATE:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the Current Edited map template.\n\n"

                ":returns: EMAPTEMPLATE Object\n"
                ":rtype: :class:`geosoft.gxapi.GXEMAPTEMPLATE`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function acts just like \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.current`\\  except that the document is not activated (brought to foreground) and no\n"
                "   					guarantee is given about which document is currently active.\n"
                "   				\n\n"
               ).staticmethod("current_no_activate");
    pyClass.def("current_if_exists", &GXEMAPTEMPLATE_wrap_current_if_exists,
                "current_if_exists() -> GXEMAPTEMPLATE:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the Current Edited map.\n\n"

                ":returns: EMAPTEMPLATE Object to current edited map. If there is no current map,\n"
                "          the user is not prompted for a map, and 0 is returned.\n"
                ":rtype: :class:`geosoft.gxapi.GXEMAPTEMPLATE`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("current_if_exists");
    pyClass.def("get_map_templates_lst", &GXEMAPTEMPLATE_wrap_get_map_templates_lst,
                "get_map_templates_lst((GXLST)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Load the file names of open maps into a LST.\n\n"

                ":param arg1: LST to load\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`EMAPTEMPLATE_PATH`\\ \n"
                ":type arg2: int\n"
                ":returns: The number of documents loaded into the LST.\n"
                "          The LST is cleared first.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_map_templates_lst");
    pyClass.def("get_name", &GXEMAPTEMPLATE_wrap_get_name,
                "get_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the name of the map object of this EMAPTEMPLATE.\n\n"

                ":param arg1: Name returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("have_current", &GXEMAPTEMPLATE_wrap_have_current,
                "have_current() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns whether a current map is loaded\n\n"

                ":returns: 0 - no current map.\n"
                "          1 - current map\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("have_current");
    pyClass.def("i_get_specified_map_name", &GXEMAPTEMPLATE_wrap_i_get_specified_map_name,
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
                "          1 - No Map Found\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("i_get_specified_map_name");
    pyClass.def("is_locked", &GXEMAPTEMPLATE_wrap_is_locked,
                "is_locked() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this MapTemplate locked\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("loaded", &GXEMAPTEMPLATE_wrap_loaded,
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
    pyClass.def("get_window_position", &GXEMAPTEMPLATE_wrap_get_window_position,
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
                ":param arg5: Window state \\ :ref:`EMAPTEMPLATE_WINDOW_STATE`\\ \n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Docked or floating \\ :ref:`EMAPTEMPLATE_WINDOW_POSITION`\\ \n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               );
    pyClass.def("set_window_position", &GXEMAPTEMPLATE_wrap_set_window_position,
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
                ":param arg5: Window state \\ :ref:`EMAPTEMPLATE_WINDOW_STATE`\\ \n"
                ":type arg5: int\n"
                ":param arg6: Docked or floating \\ :ref:`EMAPTEMPLATE_WINDOW_POSITION`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               );
    pyClass.def("read_only", &GXEMAPTEMPLATE_wrap_read_only,
                "read_only() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Checks if a map is currently opened in a read-only mode.\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("load", &GXEMAPTEMPLATE_wrap_load,
                "load((str)arg1) -> GXEMAPTEMPLATE:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads maps into the editor.\n\n"

                ":param arg1: list of maps (';' or '\\ `|`\\ ' delimited) to load.\n"
                ":type arg1: str\n"
                ":returns: EMAPTEMPLATE Object to edited map.\n"
                ":rtype: :class:`geosoft.gxapi.GXEMAPTEMPLATE`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The last map in the list will be the current map.\n"
                "   \n"
                "   Maps may already be loaded.\n"
                "   \n"
                "   Only the first file in the list may have a directory path.\n"
                "   All other files in the list are assumed to be in the same\n"
                "   directory as the first file.\n"
                "   				\n\n"
               ).staticmethod("load");
    pyClass.def("load_no_activate", &GXEMAPTEMPLATE_wrap_load_no_activate,
                "load_no_activate((str)arg1) -> GXEMAPTEMPLATE:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads documents into the workspace\n\n"

                ":param arg1: list of documents (';' or '\\ `|`\\ ' delimited) to load.\n"
                ":type arg1: str\n"
                ":returns: Handle to current edited document, which will be the last\n"
                "          						database in the list if multiple files were provided.\n"
                ":rtype: :class:`geosoft.gxapi.GXEMAPTEMPLATE`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function acts just like \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.load`\\  except that the document(s) is not activated (brought to foreground) and no\n"
                "   					guarantee is given about which document is currently active.\n"
                "   				\n\n"
               ).staticmethod("load_no_activate");
    pyClass.def("lock", &GXEMAPTEMPLATE_wrap_lock,
                "lock() -> GXMAPTEMPLATE:\n"

                "\n.. parsed-literal::\n\n"
                "   This method locks the Edited map.\n\n"

                ":returns: MAPTEMPLATE Object to map associated with edited map.\n"
                ":rtype: :class:`geosoft.gxapi.GXMAPTEMPLATE`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("make_current", &GXEMAPTEMPLATE_wrap_make_current,
                "make_current() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Makes this EMAPTEMPLATE object the current active object to the user.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("un_load", &GXEMAPTEMPLATE_wrap_un_load,
                "un_load((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unloads a map template.\n\n"

                ":param arg1: Name of the map to unload\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the map template is not loaded, nothing happens.\n"
                "   Same as \\ :func:`geosoft.gxapi.GXEMAPTEMPLATE.un_load_verify`\\  with FALSE to prompt save.\n"
                "   				\n\n"
               ).staticmethod("un_load");
    pyClass.def("un_load_all", &GXEMAPTEMPLATE_wrap_un_load_all,
                "un_load_all() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unloads all opened maps\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("un_load_all");
    pyClass.def("un_load_verify", &GXEMAPTEMPLATE_wrap_un_load_verify,
                "un_load_verify((str)arg1, (bool)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unloads an edited map, optional prompt to save.\n\n"

                ":param arg1: Name of map to unload\n"
                ":type arg1: str\n"
                ":param arg2: prompt bool\n"
                ":type arg2: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the map is not loaded, nothing happens.\n"
                "   If \"FALSE\", map is saved without a prompt.\n"
                "   				\n\n"
               ).staticmethod("un_load_verify");
    pyClass.def("un_lock", &GXEMAPTEMPLATE_wrap_un_lock,
                "un_lock() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method unlocks the Edited map.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_box", &GXEMAPTEMPLATE_wrap_get_box,
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
                "          1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The coordinates are returned in the current template units\n"
                "   (See GetUnits and SetUnits in MAPTEMPLATE)\n"
                "   				\n\n"
               );
    pyClass.def("get_line", &GXEMAPTEMPLATE_wrap_get_line,
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
                "          1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The coordinates are returned in the current template units\n"
                "   (See GetUnits and SetUnits in MAPTEMPLATE)\n"
                "   				\n\n"
               );
    pyClass.def("get_point", &GXEMAPTEMPLATE_wrap_get_point,
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
                "          1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The coordinates are returned in the current template units\n"
                "   (See GetUnits and SetUnits in MAPTEMPLATE)\n"
                "   				\n\n"
               );
    pyClass.def("get_rect", &GXEMAPTEMPLATE_wrap_get_rect,
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
                "          1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The coordinates are returned in the current template units\n"
                "   (See GetUnits and SetUnits in MAPTEMPLATE)\n"
                "   				\n\n"
               );
    pyClass.def("track_point", &GXEMAPTEMPLATE_wrap_track_point,
                "track_point((int)arg1, (float_ref)arg2, (float_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get point without prompt or cursor change with tracking\n\n"

                ":param arg1: \\ :ref:`EMAPTEMPLATE_TRACK`\\ \n"
                ":type arg1: int\n"
                ":param arg2: X coordinate in current view user units.\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: 0 if point returned.\n"
                "          1 if user cancelled.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_item_selection", &GXEMAPTEMPLATE_wrap_get_item_selection,
                "get_item_selection((str_ref)arg1) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets info about the current selected item\n\n"

                ":param arg1: returned item name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: bool Is item a view?\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If nothing is selected the string will be empty and the function will return ``False``;\n\n"
               );
    pyClass.def("set_item_selection", &GXEMAPTEMPLATE_wrap_set_item_selection,
                "set_item_selection((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the current selected item\n\n"

                ":param arg1: item name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   An empty string will unselect everything.\n\n"
               );
    pyClass.def("get_display_area", &GXEMAPTEMPLATE_wrap_get_display_area,
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
                "   					The coordinates are based on the current template units\n"
                "   (See GetUnits and SetUnits in MAPTEMPLATE)\n"
                "   				\n\n"
               );
    pyClass.def("get_template_layout_props", &GXEMAPTEMPLATE_wrap_get_template_layout_props,
                "get_template_layout_props((bool_ref)arg1, (float_ref)arg2, (int_ref)arg3, (int_ref)arg4, (int_ref)arg5, (int_ref)arg6, (int_ref)arg7, (int_ref)arg8) -> None:\n"

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
                "   view of a map.\n"
                "   				\n\n"
               );
    pyClass.def("get_window_state", &GXEMAPTEMPLATE_wrap_get_window_state,
                "get_window_state() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve the current state of the map window\n\n"

                ":returns: \\ :ref:`EMAPTEMPLATE_WINDOW_STATE`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_display_area", &GXEMAPTEMPLATE_wrap_set_display_area,
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
                "   					The coordinates are based on the current template units\n"
                "   (See GetUnits and SetUnits in MAPTEMPLATE)\n"
                "   				\n\n"
               );
    pyClass.def("set_template_layout_props", &GXEMAPTEMPLATE_wrap_set_template_layout_props,
                "set_template_layout_props((bool)arg1, (float)arg2, (int)arg3, (int)arg4, (int)arg5, (int)arg6, (int)arg7, (int)arg8) -> None:\n"

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
                "   view of a map.\n"
                "   				\n\n"
               );
    pyClass.def("set_window_state", &GXEMAPTEMPLATE_wrap_set_window_state,
                "set_window_state((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Changes the state of the map window\n\n"

                ":param arg1: \\ :ref:`EMAPTEMPLATE_WINDOW_STATE`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create_virtual", &GXEMAPTEMPLATE_wrap_create_virtual,
                "create_virtual((str)arg1) -> GXEMAPTEMPLATE:\n"

                "\n.. parsed-literal::\n\n"
                "   Makes this EMAPTEMPLATE object the current active object to the user.\n\n"

                ":param arg1: Name of map to create a virtual EMAMTEMPLATE from\n"
                ":type arg1: str\n"
                ":returns: EMAPTEMPLATE Object\n"
                ":rtype: :class:`geosoft.gxapi.GXEMAPTEMPLATE`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_virtual");

    scope().attr("EMAPTEMPLATE_PATH_FULL") = (int32_t)0;
    scope().attr("EMAPTEMPLATE_PATH_DIR") = (int32_t)1;
    scope().attr("EMAPTEMPLATE_PATH_NAME_EXT") = (int32_t)2;
    scope().attr("EMAPTEMPLATE_PATH_NAME") = (int32_t)3;
    scope().attr("EMAPTEMPLATE_TRACK_ERASE") = (int32_t)1;
    scope().attr("EMAPTEMPLATE_TRACK_RMENU") = (int32_t)2;
    scope().attr("EMAPTEMPLATE_TRACK_CYCLE") = (int32_t)4;
    scope().attr("EMAPTEMPLATE_WINDOW_POSITION_DOCKED") = (int32_t)0;
    scope().attr("EMAPTEMPLATE_WINDOW_POSITION_FLOATING") = (int32_t)1;
    scope().attr("EMAPTEMPLATE_WINDOW_RESTORE") = (int32_t)0;
    scope().attr("EMAPTEMPLATE_WINDOW_MINIMIZE") = (int32_t)1;
    scope().attr("EMAPTEMPLATE_WINDOW_MAXIMIZE") = (int32_t)2;

}
