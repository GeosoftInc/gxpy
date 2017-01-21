#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline int32_t GXVULCAN_wrap_is_valid_triangulation_file(const gx_string_type& arg1)
{
    int32_t ret = GXVULCAN::is_valid_triangulation_file(arg1);
    return ret;
}
inline int32_t GXVULCAN_wrap_is_valid_block_model_file(const gx_string_type& arg1)
{
    int32_t ret = GXVULCAN::is_valid_block_model_file(arg1);
    return ret;
}
inline void GXVULCAN_wrap_triangulation_to_view(const gx_string_type& arg1, GXIPJPtr arg2, GXMVIEWPtr arg3, const gx_string_type& arg4)
{
    GXVULCAN::triangulation_to_view(arg1, arg2, arg3, arg4);
}
inline void GXVULCAN_wrap_get_block_model_variable_info(const gx_string_type& arg1, int32_t arg2, GXLSTPtr arg3)
{
    GXVULCAN::get_block_model_variable_info(arg1, (BLOCK_MODEL_VARIABLE_TYPE)arg2, arg3);
}
inline void GXVULCAN_wrap_get_block_model_string_variable_values(const gx_string_type& arg1, const gx_string_type& arg2, GXLSTPtr arg3)
{
    GXVULCAN::get_block_model_string_variable_values(arg1, arg2, arg3);
}
inline void GXVULCAN_wrap_block_model_to_voxel(const gx_string_type& arg1, GXIPJPtr arg2, const gx_string_type& arg3, const gx_string_type& arg4, bool arg5, const gx_string_type& arg6)
{
    GXVULCAN::block_model_to_voxel(arg1, arg2, arg3, arg4, arg5, arg6);
}

void gxPythonImportGXVULCAN()
{

    class_<GXVULCAN, boost::noncopyable> pyClass("GXVULCAN",
            "\n.. parsed-literal::\n\n"
            "   The VULCAN class is used for importing Maptek® Vulcan block and triangulation files.\n\n"
            , no_init);


    pyClass.def("is_valid_triangulation_file", &GXVULCAN_wrap_is_valid_triangulation_file,
                "is_valid_triangulation_file((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check if the given file can be opened as a Vulcan triangulation file.\n\n"

                ":param arg1: Triangulation file\n"
                ":type arg1: str\n"
                ":returns: 0 - No\n"
                "          						1 - Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("is_valid_triangulation_file");
    pyClass.def("is_valid_block_model_file", &GXVULCAN_wrap_is_valid_block_model_file,
                "is_valid_block_model_file((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Check if the given file can be opened as a Vulcan block model file.\n\n"

                ":param arg1: Block model file\n"
                ":type arg1: str\n"
                ":returns: 0 - No\n"
                "          						1 - Yes\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("is_valid_block_model_file");
    pyClass.def("triangulation_to_view", &GXVULCAN_wrap_triangulation_to_view,
                "triangulation_to_view((str)arg1, (GXIPJ)arg2, (GXMVIEW)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw triangle edges in a Vulcan triangulation file to a 3D view in a map.\n\n"

                ":param arg1: Triangulation file\n"
                ":type arg1: str\n"
                ":param arg2: Triangulation projection\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg3: Destination MVIEW\n"
                ":type arg3: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg4: New group name\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("triangulation_to_view");
    pyClass.def("get_block_model_variable_info", &GXVULCAN_wrap_get_block_model_variable_info,
                "get_block_model_variable_info((str)arg1, (int)arg2, (GXLST)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Query a block model for the variable names and descriptions.\n\n"

                ":param arg1: Block model file\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`BLOCK_MODEL_VARIABLE_TYPE`\\  Which variables to return.\n"
                ":type arg2: int\n"
                ":param arg3: List used to return variable names/descriptions.\n"
                ":type arg3: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("get_block_model_variable_info");
    pyClass.def("get_block_model_string_variable_values", &GXVULCAN_wrap_get_block_model_string_variable_values,
                "get_block_model_string_variable_values((str)arg1, (str)arg2, (GXLST)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Query a block model for the values a string variable can assume.\n\n"

                ":param arg1: Block model file\n"
                ":type arg1: str\n"
                ":param arg2: Variable name\n"
                ":type arg2: str\n"
                ":param arg3: List used to return variable names\n"
                ":type arg3: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("get_block_model_string_variable_values");
    pyClass.def("block_model_to_voxel", &GXVULCAN_wrap_block_model_to_voxel,
                "block_model_to_voxel((str)arg1, (GXIPJ)arg2, (str)arg3, (str)arg4, (bool)arg5, (str)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a Geosoft voxel file from a Vulcan block model file.\n\n"

                ":param arg1: Block model file\n"
                ":type arg1: str\n"
                ":param arg2: Block model projection\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg3: Variable to import\n"
                ":type arg3: str\n"
                ":param arg4: Ouput voxel filename\n"
                ":type arg4: str\n"
                ":param arg5: Remove default values from input? bool\n"
                ":type arg5: bool\n"
                ":param arg6: Rock code file for string variable imports. Optional, unused for numeric variable imports.\n"
                ":type arg6: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("block_model_to_voxel");

    scope().attr("BLOCK_MODEL_NUMERIC_VARIABLE") = (int32_t)1;
    scope().attr("BLOCK_MODEL_STRING_VARIABLE") = (int32_t)2;

}
