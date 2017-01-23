#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXEDOCPtr GXEDOC_wrap_create_new_gms_3d(const gx_string_type& arg1, int32_t arg2, int32_t arg3, int32_t arg4)
{
    GXEDOCPtr ret = GXEDOC::create_new_gms_3d(arg1, arg2, arg3, (GMS3D_MODELTYPE)arg4);
    return ret;
}
inline GXEDOCPtr GXEDOC_wrap_current(int32_t arg1)
{
    GXEDOCPtr ret = GXEDOC::current((EDOC_TYPE)arg1);
    return ret;
}
inline GXEDOCPtr GXEDOC_wrap_current_no_activate(int32_t arg1)
{
    GXEDOCPtr ret = GXEDOC::current_no_activate((EDOC_TYPE)arg1);
    return ret;
}
inline GXEDOCPtr GXEDOC_wrap_current_if_exists(int32_t arg1)
{
    GXEDOCPtr ret = GXEDOC::current_if_exists((EDOC_TYPE)arg1);
    return ret;
}
inline int32_t GXEDOC_wrap_get_documents_lst(GXLSTPtr arg1, int32_t arg2, int32_t arg3)
{
    int32_t ret = GXEDOC::get_documents_lst(arg1, (EDOC_PATH)arg2, (EDOC_TYPE)arg3);
    return ret;
}
inline void GXEDOC_wrap_get_name(GXEDOCPtr self, str_ref& arg1)
{
    self->get_name(arg1);
}
inline int32_t GXEDOC_wrap_get_window_state(GXEDOCPtr self)
{
    EDOC_WINDOW_STATE ret = self->get_window_state();
    return ret;
}
inline bool GXEDOC_wrap_have_current(int32_t arg1)
{
    bool ret = GXEDOC::have_current((EDOC_TYPE)arg1);
    return ret;
}
inline int32_t GXEDOC_wrap_loaded(const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = GXEDOC::loaded(arg1, (EDOC_TYPE)arg2);
    return ret;
}
inline void GXEDOC_wrap_get_window_position(GXEDOCPtr self, int_ref& arg1, int_ref& arg2, int_ref& arg3, int_ref& arg4, int_ref& arg5, int_ref& arg6)
{
    self->get_window_position(arg1, arg2, arg3, arg4, (EDOC_WINDOW_STATE&)arg5, (EDOC_WINDOW_POSITION&)arg6);
}
inline void GXEDOC_wrap_set_window_position(GXEDOCPtr self, int32_t arg1, int32_t arg2, int32_t arg3, int32_t arg4, int32_t arg5, int32_t arg6)
{
    self->set_window_position(arg1, arg2, arg3, arg4, (EDOC_WINDOW_STATE)arg5, (EDOC_WINDOW_POSITION)arg6);
}
inline bool GXEDOC_wrap_read_only(GXEDOCPtr self)
{
    bool ret = self->read_only();
    return ret;
}
inline GXEDOCPtr GXEDOC_wrap_load(const gx_string_type& arg1, int32_t arg2)
{
    GXEDOCPtr ret = GXEDOC::load(arg1, (EDOC_TYPE)arg2);
    return ret;
}
inline GXEDOCPtr GXEDOC_wrap_load_no_activate(const gx_string_type& arg1, int32_t arg2)
{
    GXEDOCPtr ret = GXEDOC::load_no_activate(arg1, (EDOC_TYPE)arg2);
    return ret;
}
inline void GXEDOC_wrap_make_current(GXEDOCPtr self)
{
    self->make_current();
}
inline void GXEDOC_wrap_set_window_state(GXEDOCPtr self, int32_t arg1)
{
    self->set_window_state((EDOC_WINDOW_STATE)arg1);
}
inline void GXEDOC_wrap_sync(const gx_string_type& arg1, int32_t arg2)
{
    GXEDOC::sync(arg1, (EDOC_TYPE)arg2);
}
inline void GXEDOC_wrap_sync_open(GXEDOCPtr self)
{
    self->sync_open();
}
inline void GXEDOC_wrap_un_load(const gx_string_type& arg1, int32_t arg2)
{
    GXEDOC::un_load(arg1, (EDOC_TYPE)arg2);
}
inline void GXEDOC_wrap_un_load_all(int32_t arg1)
{
    GXEDOC::un_load_all((EDOC_TYPE)arg1);
}
inline void GXEDOC_wrap_un_load_discard(const gx_string_type& arg1, int32_t arg2)
{
    GXEDOC::un_load_discard(arg1, (EDOC_TYPE)arg2);
}
inline void GXEDOC_wrap_un_load_verify(const gx_string_type& arg1, int32_t arg2, int32_t arg3)
{
    GXEDOC::un_load_verify(arg1, (EDOC_UNLOAD)arg2, (EDOC_TYPE)arg3);
}

void gxPythonImportGXEDOC()
{

    class_<GXEDOC, GXEDOCPtr> pyClass("GXEDOC",
                                      "\n.. parsed-literal::\n\n"
                                      "   The EDOC class provides access to a generic documents views as loaded within\n"
                                      "   Oasis montaj.\n\n"
                                      , no_init);

    pyClass.def("null", &GXEDOC::null, "null() -> GXEDOC\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXEDOC`\n\n:returns: A null :class:`geosoft.gxapi.GXEDOC`\n:rtype: :class:`geosoft.gxapi.GXEDOC`\n").staticmethod("null");
    pyClass.def("is_null", &GXEDOC::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXEDOC is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXEDOC`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXEDOC::_internal_handle);
    pyClass.def("create_new_gms_3d", &GXEDOC_wrap_create_new_gms_3d,
                "create_new_gms_3d((str)arg1, (int)arg2, (int)arg3, (int)arg4) -> GXEDOC:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a new GMSYS 3D Model into the workspace, flags as new.\n\n"

                ":param arg1: Document to load.\n"
                ":type arg1: str\n"
                ":param arg2: X Size\n"
                ":type arg2: int\n"
                ":param arg3: Y Size\n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`GMS3D_MODELTYPE`\\ \n"
                ":type arg4: int\n"
                ":returns: Handle to the newly created edited model.\n"
                ":rtype: :class:`geosoft.gxapi.GXEDOC`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See \\ :func:`geosoft.gxapi.GXEDOC.load`\\ . This is used for brand new documents, it also sets\n"
                "   an internal flag such that if on closing the user chooses\n"
                "   not to save changes, the document is deleted thus keeping the\n"
                "   project folders clean.\n\n"
               ).staticmethod("create_new_gms_3d");
    pyClass.def("current", &GXEDOC_wrap_current,
                "current((int)arg1) -> GXEDOC:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the Current Edited Document.\n\n"

                ":param arg1: \\ :ref:`EDOC_TYPE`\\ \n"
                ":type arg1: int\n"
                ":returns: EDOC Object\n"
                ":rtype: :class:`geosoft.gxapi.GXEDOC`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("current");
    pyClass.def("current_no_activate", &GXEDOC_wrap_current_no_activate,
                "current_no_activate((int)arg1) -> GXEDOC:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the Current Edited Document.\n\n"

                ":param arg1: \\ :ref:`EDOC_TYPE`\\ \n"
                ":type arg1: int\n"
                ":returns: EDOC Object\n"
                ":rtype: :class:`geosoft.gxapi.GXEDOC`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function acts just like \\ :func:`geosoft.gxapi.GXEDOC.current`\\  except that the document is not activated (brought to foreground) and no\n"
                "   				guarantee is given about which document is currently active.\n\n"
               ).staticmethod("current_no_activate");
    pyClass.def("current_if_exists", &GXEDOC_wrap_current_if_exists,
                "current_if_exists((int)arg1) -> GXEDOC:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the Current Edited Document.\n\n"

                ":param arg1: \\ :ref:`EDOC_TYPE`\\ \n"
                ":type arg1: int\n"
                ":returns: EDOC Object to current edited document. If there is no current document,\n"
                "          the user is not prompted for a document, and 0 is returned.\n"
                ":rtype: :class:`geosoft.gxapi.GXEDOC`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("current_if_exists");
    pyClass.def("get_documents_lst", &GXEDOC_wrap_get_documents_lst,
                "get_documents_lst((GXLST)arg1, (int)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Load the file names of open documents into a LST.\n\n"

                ":param arg1: LST to load\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`EDOC_PATH`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`EDOC_TYPE`\\ \n"
                ":type arg3: int\n"
                ":returns: The number of documents loaded into the LST.\n"
                "          The LST is cleared first.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_documents_lst");
    pyClass.def("get_name", &GXEDOC_wrap_get_name,
                "get_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the name of the document object of this EDOC.\n\n"

                ":param arg1: Name returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_window_state", &GXEDOC_wrap_get_window_state,
                "get_window_state() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve the current state of the document window\n\n"

                ":returns: \\ :ref:`EDOC_WINDOW_STATE`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("have_current", &GXEDOC_wrap_have_current,
                "have_current((int)arg1) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns true if a document is loaded\n\n"

                ":param arg1: \\ :ref:`EDOC_TYPE`\\ \n"
                ":type arg1: int\n"
                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("have_current");
    pyClass.def("loaded", &GXEDOC_wrap_loaded,
                "loaded((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns 1 if a document is loaded .\n\n"

                ":param arg1: document name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`EDOC_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: 1 if document is loaded, 0 otherwise.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("loaded");
    pyClass.def("get_window_position", &GXEDOC_wrap_get_window_position,
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
                ":param arg5: Window state \\ :ref:`EDOC_WINDOW_STATE`\\ \n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: Docked or floating \\ :ref:`EDOC_WINDOW_POSITION`\\ \n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               );
    pyClass.def("set_window_position", &GXEDOC_wrap_set_window_position,
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
                ":param arg5: Window state \\ :ref:`EDOC_WINDOW_STATE`\\ \n"
                ":type arg5: int\n"
                ":param arg6: Docked or floating \\ :ref:`EDOC_WINDOW_POSITION`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               );
    pyClass.def("read_only", &GXEDOC_wrap_read_only,
                "read_only() -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Checks if a document is currently opened in a read-only mode.\n\n"

                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("load", &GXEDOC_wrap_load,
                "load((str)arg1, (int)arg2) -> GXEDOC:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads a list of documents into the workspace\n\n"

                ":param arg1: list of documents (';' or '\\ `|`\\ ' delimited) to load.\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`EDOC_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: Handle to current edited document, which will be the last\n"
                "          document in the list.\n"
                ":rtype: :class:`geosoft.gxapi.GXEDOC`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The last listed document will become the current document.\n"
                "   \n"
                "   Only the first file in the list may have a directory path.\n"
                "   All other files in the list are assumed to be in the same\n"
                "   directory as the first file.\n\n"
               ).staticmethod("load");
    pyClass.def("load_no_activate", &GXEDOC_wrap_load_no_activate,
                "load_no_activate((str)arg1, (int)arg2) -> GXEDOC:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads a list of documents into the workspace\n\n"

                ":param arg1: list of documents (';' or '\\ `|`\\ ' delimited) to load.\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`EDOC_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: Handle to current edited document, which will be the last\n"
                "          document in the list.\n"
                ":rtype: :class:`geosoft.gxapi.GXEDOC`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function acts just like \\ :func:`geosoft.gxapi.GXEDOC.load`\\  except that the document(s) is not activated (brought to foreground) and no\n"
                "   					guarantee is given about which document is currently active.\n\n"
               ).staticmethod("load_no_activate");
    pyClass.def("make_current", &GXEDOC_wrap_make_current,
                "make_current() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Makes this EDOC object the current active object to the user.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_window_state", &GXEDOC_wrap_set_window_state,
                "set_window_state((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Changes the state of the document window\n\n"

                ":param arg1: \\ :ref:`EDOC_WINDOW_STATE`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("sync", &GXEDOC_wrap_sync,
                "sync((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Syncronize the Metadata of a document that is not currently open\n\n"

                ":param arg1: Document file name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`EDOC_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("sync");
    pyClass.def("sync_open", &GXEDOC_wrap_sync_open,
                "sync_open() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Syncronize the Metadata of a document\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("un_load", &GXEDOC_wrap_un_load,
                "un_load((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unloads an edited document.\n\n"

                ":param arg1: Name of document to unload\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`EDOC_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the document is not loaded, nothing happens.\n"
                "   Same as \\ :func:`geosoft.gxapi.GXEDOC.un_load_verify`\\  with FALSE to prompt save.\n\n"
               ).staticmethod("un_load");
    pyClass.def("un_load_all", &GXEDOC_wrap_un_load_all,
                "un_load_all((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unloads all opened documents\n\n"

                ":param arg1: \\ :ref:`EDOC_TYPE`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("un_load_all");
    pyClass.def("un_load_discard", &GXEDOC_wrap_un_load_discard,
                "un_load_discard((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unloads a document in the workspace, discards changes.\n\n"

                ":param arg1: Name of document to unload\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`EDOC_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the document is not loaded, nothing happens.\n\n"
               ).staticmethod("un_load_discard");
    pyClass.def("un_load_verify", &GXEDOC_wrap_un_load_verify,
                "un_load_verify((str)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Unloads an edited document, optional prompt to save.\n\n"

                ":param arg1: Name of document to unload\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`EDOC_UNLOAD`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`EDOC_TYPE`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the document is not loaded, nothing happens.\n"
                "   The user can be prompted to save before unloading.\n"
                "   If EDOC_UNLOAD_NO_PROMPT, data is always saved.\n\n"
               ).staticmethod("un_load_verify");

    scope().attr("EDOC_PATH_FULL") = (int32_t)0;
    scope().attr("EDOC_PATH_DIR") = (int32_t)1;
    scope().attr("EDOC_PATH_NAME_EXT") = (int32_t)2;
    scope().attr("EDOC_PATH_NAME") = (int32_t)3;
    scope().attr("EDOC_TYPE_GMS3D") = (int32_t)0;
    scope().attr("EDOC_TYPE_VOXEL") = (int32_t)1;
    scope().attr("EDOC_TYPE_VOXEL_INVERSION") = (int32_t)2;
    scope().attr("EDOC_TYPE_GMS2D") = (int32_t)3;
    scope().attr("EDOC_UNLOAD_NO_PROMPT") = (int32_t)0;
    scope().attr("EDOC_UNLOAD_PROMPT") = (int32_t)1;
    scope().attr("EDOC_WINDOW_POSITION_DOCKED") = (int32_t)0;
    scope().attr("EDOC_WINDOW_POSITION_FLOATING") = (int32_t)1;
    scope().attr("EDOC_WINDOW_RESTORE") = (int32_t)0;
    scope().attr("EDOC_WINDOW_MINIMIZE") = (int32_t)1;
    scope().attr("EDOC_WINDOW_MAXIMIZE") = (int32_t)2;
    scope().attr("GMS3D_MODELTYPE_DEPTH") = (int32_t)0;
    scope().attr("GMS3D_MODELTYPE_TIME") = (int32_t)1;
    scope().attr("GMS2D_MODELTYPE_DEPTH") = (int32_t)0;
    scope().attr("GMS2D_MODELTYPE_TIME") = (int32_t)1;

}
