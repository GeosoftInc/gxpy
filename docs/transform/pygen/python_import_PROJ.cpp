#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXPROJ_wrap_drop_map_clip_data(int32_t arg1)
{
    GXPROJ::drop_map_clip_data(arg1);
}
inline int32_t GXPROJ_wrap_add_document(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    int32_t ret = GXPROJ::add_document(arg1, arg2, (PROJ_DISPLAY)arg3);
    return ret;
}
inline int32_t GXPROJ_wrap_add_document_without_opening(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXPROJ::add_document_without_opening(arg1, arg2);
    return ret;
}
inline int32_t GXPROJ_wrap_get_command_environment()
{
    COMMAND_ENV ret = GXPROJ::get_command_environment();
    return ret;
}
inline int32_t GXPROJ_wrap_list_documents(GXVVPtr arg1, const gx_string_type& arg2)
{
    int32_t ret = GXPROJ::list_documents(arg1, arg2);
    return ret;
}
inline int32_t GXPROJ_wrap_list_tools(GXLSTPtr arg1, int32_t arg2)
{
    int32_t ret = GXPROJ::list_tools(arg1, (TOOL_TYPE)arg2);
    return ret;
}
inline int32_t GXPROJ_wrap_remove_document(const gx_string_type& arg1)
{
    int32_t ret = GXPROJ::remove_document(arg1);
    return ret;
}
inline int32_t GXPROJ_wrap_remove_tool(const gx_string_type& arg1)
{
    int32_t ret = GXPROJ::remove_tool(arg1);
    return ret;
}
inline int32_t GXPROJ_wrap_save_close_documents(const gx_string_type& arg1)
{
    int32_t ret = GXPROJ::save_close_documents(arg1);
    return ret;
}
inline void GXPROJ_wrap_get_name(str_ref& arg1)
{
    GXPROJ::get_name(arg1);
}

void gxPythonImportGXPROJ()
{

    class_<GXPROJ, boost::noncopyable> pyClass("GXPROJ",
            "\n.. parsed-literal::\n\n"
            "   Project functions\n\n"
            , no_init);


    pyClass.def("drop_map_clip_data", &GXPROJ_wrap_drop_map_clip_data,
                "drop_map_clip_data((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Drop Map clipboard data in the current project (workspace background)\n\n"

                ":param arg1: Handle to Global Clipboard data\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("drop_map_clip_data");
    pyClass.def("add_document", &GXPROJ_wrap_add_document,
                "add_document((str)arg1, (str)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Adds (and opens) a document file in the current project.\n\n"

                ":param arg1: Document name\n"
                ":type arg1: str\n"
                ":param arg2: Type of document to add\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`PROJ_DISPLAY`\\ \n"
                ":type arg3: int\n"
                ":returns: 0 - Ok\n"
                "          1 - Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The passed file name must be a valid\n"
                "   file name complete with an extension and\n"
                "   qualifiers (if applicable).\n"
                "   \n"
                "   The type string can be one of the following:\n"
                "   Database    Save and close only databases.\n"
                "   Map         Save and close only maps.\n"
                "   Grid        Save and close only grids.\n"
                "   \n\n"
               ).staticmethod("add_document");
    pyClass.def("add_document_without_opening", &GXPROJ_wrap_add_document_without_opening,
                "add_document_without_opening((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Adds (and opens) a document file in the current project.\n\n"

                ":param arg1: Document name\n"
                ":type arg1: str\n"
                ":param arg2: Type of document to add\n"
                ":type arg2: str\n"
                ":returns: 0 - Ok\n"
                "          1 - Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The passed file name must be a valid\n"
                "   file name complete with an extension and\n"
                "   qualifiers (if applicable).\n"
                "   \n"
                "   The type string can be one of the following:\n"
                "   Database    Save and close only databases.\n"
                "   Map         Save and close only maps.\n"
                "   Grid        Save and close only grids.\n"
                "   Voxel		Voxel file.\n"
                "   \n\n"
               ).staticmethod("add_document_without_opening");
    pyClass.def("get_command_environment", &GXPROJ_wrap_get_command_environment,
                "get_command_environment() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   The current command environment\n\n"

                ":returns: \\ :ref:`COMMAND_ENV`\\ \n"
                "          \n"
                "          Notes									We are moving towards embedded tools and menus and this setting can be set\n"
                "          queried from the project to determine how specific commands should react.\n"
                "          ly 3D viewer is currently making use of this.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_command_environment");
    pyClass.def("list_documents", &GXPROJ_wrap_list_documents,
                "list_documents((GXVV)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Fills a VV with documents of a certain type.\n\n"

                ":param arg1: VV of type -STR_FILE\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Type of document to obtain\n"
                ":type arg2: str\n"
                ":returns: The number of documents listed in the VV.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   GX will terminate if error.\n"
                "   \n"
                "   The type string can be one of the following:\n"
                "   Database         List Databases.\n"
                "   Grid             List Grids.\n"
                "   Map              List Maps.\n"
                "   Voxel            List Voxels.\n"
                "   VoxelInversion   List VOXI Documents.\n"
                "   MXD              List ArcGIS MXDs.\n"
                "   GMS3D            List GM-SYS 3D Models.\n"
                "   GMS2D            List GM-SYS 2D Models.\n"
                "   All              Lists all files.\n\n"
               ).staticmethod("list_documents");
    pyClass.def("list_tools", &GXPROJ_wrap_list_tools,
                "list_tools((GXLST)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Fills an LST object with tools of a certain type and\n"
                "   notes the current visibility setting.\n\n"

                ":param arg1: LST object to hold list\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`TOOL_TYPE`\\ \n"
                ":type arg2: int\n"
                ":returns: The number of tools found.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   GX will terminate if there is an error.\n"
                "   \n"
                "   LST object will hold the tool name in the name column and\n"
                "   include whether the tool is currently visible in the value\n"
                "   column (1=visible, 0-hidden).\n\n"
               ).staticmethod("list_tools");
    pyClass.def("remove_document", &GXPROJ_wrap_remove_document,
                "remove_document((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Removes (and closes if visible) a document from the current project.\n\n"

                ":param arg1: Document name\n"
                ":type arg1: str\n"
                ":returns: 0 - Ok\n"
                "          1 - Document not found in project\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The passed file name must be a valid\n"
                "   file name complete with an extension and\n"
                "   qualifiers (if applicable).\n\n"
               ).staticmethod("remove_document");
    pyClass.def("remove_tool", &GXPROJ_wrap_remove_tool,
                "remove_tool((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Removes (and closes if visible) a auxiliary tool from the current project.\n\n"

                ":param arg1: Tool name\n"
                ":type arg1: str\n"
                ":returns: 0 - Ok\n"
                "          1 - Tool not found in project\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Nothing\n\n"
               ).staticmethod("remove_tool");
    pyClass.def("save_close_documents", &GXPROJ_wrap_save_close_documents,
                "save_close_documents((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Saves and closes (if visible) documents contained in the current project.\n\n"

                ":param arg1: Type of document to save / close\n"
                ":type arg1: str\n"
                ":returns: 0  - Ok\n"
                "          -1 - User hit cancel in save dialog\n"
                "          1  - Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This wrapper brings up the save dialog tool to allow\n"
                "   the user to save the modified documents for this project.\n"
                "   Only documents that have actually changed will be listed.\n"
                "   \n"
                "   The type string can be one of the following:\n"
                "   Database    Save and close only databases.\n"
                "   Map         Save and close only maps.\n"
                "   Grid        Save and close only grids.\n"
                "   All         Saves and closes all files.\n\n"
               ).staticmethod("save_close_documents");
    pyClass.def("get_name", &GXPROJ_wrap_get_name,
                "get_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Return the name of the project file.\n"
                "   			 \n\n"

                ":param arg1: name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing.\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 Return the name of the project file.\n"
                "   			 \n\n"
               ).staticmethod("get_name");

    scope().attr("COMMAND_ENV_NORMAL") = (int32_t)0;
    scope().attr("COMMAND_ENV_IN3DVIEWER") = (int32_t)1;
    scope().attr("TOOL_TYPE_DEFAULT") = (int32_t)0;
    scope().attr("TOOL_TYPE_AUXILIARY") = (int32_t)1;
    scope().attr("TOOL_TYPE_ALL") = (int32_t)2;
    scope().attr("PROJ_DISPLAY_NO") = (int32_t)0;
    scope().attr("PROJ_DISPLAY_YES") = (int32_t)1;
    scope().attr("PROJ_DISPLAY_ALWAYS") = (int32_t)2;

}
