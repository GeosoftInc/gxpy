#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline int32_t GXIPGUI_wrap_modify_job(GXIPPtr arg1, GXDBPtr arg2, const gx_string_type& arg3, int32_t arg4, int_ref& arg5)
{
    int32_t ret = GXIPGUI::modify_job(arg1, arg2, arg3, (IP_PLOT)arg4, arg5);
    return ret;
}
inline void GXIPGUI_wrap_launch_ipqc_tool(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXIPGUI::launch_ipqc_tool(arg1, arg2, arg3);
}
inline void GXIPGUI_wrap_launch_offset_ipqc_tool(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXIPGUI::launch_offset_ipqc_tool(arg1, arg2, arg3);
}
inline int32_t GXIPGUI_wrap_ipqc_tool_exists()
{
    int32_t ret = GXIPGUI::ipqc_tool_exists();
    return ret;
}

void gxPythonImportGXIPGUI()
{

    class_<GXIPGUI, boost::noncopyable> pyClass("GXIPGUI",
            "\n.. parsed-literal::\n\n"
            "   This class is used in the IP System for GUI functions\n"
            "   such as defining parameters for pseudo-section plots.\n\n"

            "\n\n**Note:**\n\n"

            "\n.. parsed-literal::\n\n"
            "   None\n\n"
            , no_init);


    pyClass.def("modify_job", &GXIPGUI_wrap_modify_job,
                "modify_job((GXIP)arg1, (GXDB)arg2, (str)arg3, (int)arg4, (int_ref)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Modify parameters for an IP plot.\n\n"

                ":param arg1: DH Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXIP`\n"
                ":param arg2: DB Handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg3: Job Name (\\ `*`\\ .inp)\n"
                ":type arg3: str\n"
                ":param arg4: Job type \\ :ref:`IP_PLOT`\\ \n"
                ":type arg4: int\n"
                ":param arg5: Page to open GUI on\n"
                ":type arg5: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: 0 - Ok\n"
                "          -1 - User Cancelled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               ).staticmethod("modify_job");
    pyClass.def("launch_ipqc_tool", &GXIPGUI_wrap_launch_ipqc_tool,
                "launch_ipqc_tool((str)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch the In-Line IP QC tool on a database.\n\n"

                ":param arg1: Database name\n"
                ":type arg1: str\n"
                ":param arg2: Current Line (can be blank)\n"
                ":type arg2: str\n"
                ":param arg3: Channel to open with (can be blank)\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 The database should be a currently open database.\n"
                "   			 \n\n"
               ).staticmethod("launch_ipqc_tool");
    pyClass.def("launch_offset_ipqc_tool", &GXIPGUI_wrap_launch_offset_ipqc_tool,
                "launch_offset_ipqc_tool((str)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch the Offset IP QC tool on a database.\n\n"

                ":param arg1: Database name\n"
                ":type arg1: str\n"
                ":param arg2: Current Line (can be blank)\n"
                ":type arg2: str\n"
                ":param arg3: Channel to open with (can be blank)\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "             The database should be a currently open database.\n"
                "           \n\n"
               ).staticmethod("launch_offset_ipqc_tool");
    pyClass.def("ipqc_tool_exists", &GXIPGUI_wrap_ipqc_tool_exists,
                "ipqc_tool_exists() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   See if there is an IPQC Tool (Offset or Inline) already open.\n\n"

                ":returns: 0 if not open, 1 if open\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   				 See if there is an IPQC Tool already open.\n"
                "   			 \n\n"
               ).staticmethod("ipqc_tool_exists");


}
