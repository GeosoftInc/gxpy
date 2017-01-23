#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXSTRINGS_wrap_launch_digitization_ui(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSTRINGS::launch_digitization_ui(arg1, arg2);
}

void gxPythonImportGXSTRINGS()
{

    class_<GXSTRINGS, boost::noncopyable> pyClass("GXSTRINGS",
            "\n.. parsed-literal::\n\n"
            "   The STRINGS class is used for displaying digitization tools for interpretations\n\n"
            , no_init);


    pyClass.def("launch_digitization_ui", &GXSTRINGS_wrap_launch_digitization_ui,
                "launch_digitization_ui((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch Digitization modeless window\n\n"

                ":param arg1: string file\n"
                ":type arg1: str\n"
                ":param arg2: definition guid\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.5.0\n\n"
               ).staticmethod("launch_digitization_ui");


}
