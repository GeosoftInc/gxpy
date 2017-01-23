#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXGMSYS_wrap_launch(const gx_string_type& arg1)
{
    GXGMSYS::launch(arg1);
}

void gxPythonImportGXGMSYS()
{

    class_<GXGMSYS, boost::noncopyable> pyClass("GXGMSYS",
            "\n.. parsed-literal::\n\n"
            "   The GMSYS Methods\n\n"
            , no_init);


    pyClass.def("launch", &GXGMSYS_wrap_launch,
                "launch((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Launch GMSYS with extension\n\n"

                ":param arg1: Model name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.1\n\n"
               ).staticmethod("launch");


}
