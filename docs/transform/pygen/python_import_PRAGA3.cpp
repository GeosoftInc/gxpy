#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline int32_t GXPRAGA3_wrap_launch()
{
    int32_t ret = GXPRAGA3::launch();
    return ret;
}

void gxPythonImportGXPRAGA3()
{

    class_<GXPRAGA3, boost::noncopyable> pyClass("GXPRAGA3",
            "\n.. parsed-literal::\n\n"
            "   PRAGA3 application methods\n\n"

            "\n\n**Note:**\n\n"

            "\n.. parsed-literal::\n\n"
            "   No notes\n\n"
            , no_init);


    pyClass.def("launch", &GXPRAGA3_wrap_launch,
                "launch() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   This method launches the application.\n\n"

                ":returns: 1 - OK, 2 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               ).staticmethod("launch");


}
