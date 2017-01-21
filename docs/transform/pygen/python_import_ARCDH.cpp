#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXARCDH_wrap_close_project()
{
    GXARCDH::close_project();
}
inline void GXARCDH_wrap_set_project(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXARCDH::set_project(arg1, arg2);
}
inline void GXARCDH_wrap_set_string_file_gdb(const gx_string_type& arg1)
{
    GXARCDH::set_string_file_gdb(arg1);
}
inline void GXARCDH_wrap_stop_editing_string_file_gdb()
{
    GXARCDH::stop_editing_string_file_gdb();
}
inline int32_t GXARCDH_wrap_has_string_file_gdb_edits()
{
    int32_t ret = GXARCDH::has_string_file_gdb_edits();
    return ret;
}
inline int32_t GXARCDH_wrap_geostrings_extension_available()
{
    int32_t ret = GXARCDH::geostrings_extension_available();
    return ret;
}
inline void GXARCDH_wrap_get_current_string_file_gdb(str_ref& arg1)
{
    GXARCDH::get_current_string_file_gdb(arg1);
}
inline int32_t GXARCDH_wrap_is_valid_fgdb_file_name(const gx_string_type& arg1)
{
    int32_t ret = GXARCDH::is_valid_fgdb_file_name(arg1);
    return ret;
}
inline int32_t GXARCDH_wrap_is_valid_feature_class_name(const gx_string_type& arg1)
{
    int32_t ret = GXARCDH::is_valid_feature_class_name(arg1);
    return ret;
}
inline void GXARCDH_wrap_s_prompt_for_esri_symbol(HWND arg1, const gx_string_type& arg2, int32_t arg3, str_ref& arg4, int_ref& arg5, int_ref& arg6)
{
    GXARCDH::s_prompt_for_esri_symbol(arg1, arg2, arg3, arg4, arg5, arg6);
}

void gxPythonImportGXARCDH()
{

    class_<GXARCDH, boost::noncopyable> pyClass("GXARCDH",
            "\n.. parsed-literal::\n\n"
            "   This library is not a class. It contains various utilities\n"
            "   used in the Target extension for ArcGIS.\n\n"
            , no_init);


    pyClass.def("close_project", &GXARCDH_wrap_close_project,
                "close_project() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Closes the current DH project in the Target extension\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("close_project");
    pyClass.def("set_project", &GXARCDH_wrap_set_project,
                "set_project((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the current DH project in the Target extension\n\n"

                ":param arg1: Path String\n"
                ":type arg1: str\n"
                ":param arg2: Project Name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("set_project");
    pyClass.def("set_string_file_gdb", &GXARCDH_wrap_set_string_file_gdb,
                "set_string_file_gdb((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the current Geostring File Geodatabase in the Target extension\n\n"

                ":param arg1: File Geodatabase\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("set_string_file_gdb");
    pyClass.def("stop_editing_string_file_gdb", &GXARCDH_wrap_stop_editing_string_file_gdb,
                "stop_editing_string_file_gdb() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Stops editing session for current string fGDB\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"
               ).staticmethod("stop_editing_string_file_gdb");
    pyClass.def("has_string_file_gdb_edits", &GXARCDH_wrap_has_string_file_gdb_edits,
                "has_string_file_gdb_edits() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is a Geostring File Geodatabase loaded and contain edits?\n\n"

                ":returns: Nothing\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"
               ).staticmethod("has_string_file_gdb_edits");
    pyClass.def("geostrings_extension_available", &GXARCDH_wrap_geostrings_extension_available,
                "geostrings_extension_available() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Verifies if the geostrings extension in TfA is available. Return 1 if true, 0 otherwise\n\n"

                ":returns: Nothing\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"
               ).staticmethod("geostrings_extension_available");
    pyClass.def("get_current_string_file_gdb", &GXARCDH_wrap_get_current_string_file_gdb,
                "get_current_string_file_gdb((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the current Geostring File Geodatabase.\n\n"

                ":param arg1: name returned\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"
               ).staticmethod("get_current_string_file_gdb");
    pyClass.def("is_valid_fgdb_file_name", &GXARCDH_wrap_is_valid_fgdb_file_name,
                "is_valid_fgdb_file_name((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this a valid FGDB filename?\n\n"

                ":param arg1: FGDB filename\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"
               ).staticmethod("is_valid_fgdb_file_name");
    pyClass.def("is_valid_feature_class_name", &GXARCDH_wrap_is_valid_feature_class_name,
                "is_valid_feature_class_name((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Is this a valid featureclass name?\n\n"

                ":param arg1: featureclass name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"
               ).staticmethod("is_valid_feature_class_name");
    pyClass.def("s_prompt_for_esri_symbol", &GXARCDH_wrap_s_prompt_for_esri_symbol,
                "s_prompt_for_esri_symbol((HWND)arg1, (str)arg2, (int)arg3, (str_ref)arg4, (int_ref)arg5, (int_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Prompt the user to select an ESRI symbol and return it as an XML string. The output string will be empty if the user cancels the dialog.\n\n"

                ":param arg1: Window handle\n"
                ":type arg1: :class:`geosoft.gxapi.HWND`\n"
                ":param arg2: Initial symbol that you want displayed when the dialog is launched (use \"\" if none)\n"
                ":type arg2: str\n"
                ":param arg3: (This parameter is ignored if an initial symbol was specified) Initial symbol type that you want displayed when the dialog is launched (0 for Fill, 1 for Line)\n"
                ":type arg3: int\n"
                ":param arg4: Returned XML string representing the symbol that was chosen by the user\n"
                ":type arg4: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg5: RGBA representation of fill color to be set\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg6: RGBA representation of edge color to be set\n"
                ":type arg6: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"
               ).staticmethod("s_prompt_for_esri_symbol");


}
