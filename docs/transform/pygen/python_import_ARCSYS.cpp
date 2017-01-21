#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXARCSYS_wrap_get_browse_loc(str_ref& arg1)
{
    GXARCSYS::get_browse_loc(arg1);
}
inline void GXARCSYS_wrap_get_current_doc(str_ref& arg1)
{
    GXARCSYS::get_current_doc(arg1);
}
inline void GXARCSYS_wrap_set_browse_loc(const gx_string_type& arg1)
{
    GXARCSYS::set_browse_loc(arg1);
}

void gxPythonImportGXARCSYS()
{

    class_<GXARCSYS, boost::noncopyable> pyClass("GXARCSYS",
            "\n.. parsed-literal::\n\n"
            "   This library is not a class. It contains various general\n"
            "   system utilities used by the Geosoft extensions for ArcGIS.\n\n"
            , no_init);


    pyClass.def("get_browse_loc", &GXARCSYS_wrap_get_browse_loc,
                "get_browse_loc((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the current catalog browser location in ArcGIS\n\n"

                ":param arg1: Path String\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Gets the \"local\" directory (current catalog browser location in ArcGIS if map has not been saved,\n"
                "   otherwise MxD path). We cannot mess with the CWD in ArcGIS because there MxD settings for\n"
                "   relative/absolute paths depends on it.\n\n"
               ).staticmethod("get_browse_loc");
    pyClass.def("get_current_doc", &GXARCSYS_wrap_get_current_doc,
                "get_current_doc((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the current Mx Document file name\n\n"

                ":param arg1: Path String\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the current document is not yet saved, this will return an empty string.\n\n"
               ).staticmethod("get_current_doc");
    pyClass.def("set_browse_loc", &GXARCSYS_wrap_set_browse_loc,
                "set_browse_loc((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the current catalog browser location in ArcGIS\n\n"

                ":param arg1: Path String\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Will also set the current working directory (CWD) if the MxD has not been saved.\n"
                "   We cannot mess with the CWD in ArcGIS because their MxD settings for relative/absolute paths depends on it.\n\n"
               ).staticmethod("set_browse_loc");


}
