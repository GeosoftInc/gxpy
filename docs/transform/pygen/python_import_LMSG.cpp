#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXLMSG_wrap_goto_point(double arg1, double arg2, double arg3, GXIPJPtr arg4)
{
    GXLMSG::goto_point(arg1, arg2, arg3, arg4);
}
inline void GXLMSG_wrap_view_area(double arg1, double arg2, double arg3, double arg4, GXIPJPtr arg5)
{
    GXLMSG::view_area(arg1, arg2, arg3, arg4, arg5);
}

void gxPythonImportGXLMSG()
{

    class_<GXLMSG, boost::noncopyable> pyClass("GXLMSG",
            "\n.. parsed-literal::\n\n"
            "   Message class methods.\n\n"
            , no_init);


    pyClass.def("goto_point", &GXLMSG_wrap_goto_point,
                "goto_point((float)arg1, (float)arg2, (float)arg3, (GXIPJ)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sends a move cursor message\n\n"

                ":param arg1: X location\n"
                ":type arg1: float\n"
                ":param arg2: Y location\n"
                ":type arg2: float\n"
                ":param arg3: Z location\n"
                ":type arg3: float\n"
                ":param arg4: IPJ (if (IPJ)0, default coordinate system)\n"
                ":type arg4: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"
               ).staticmethod("goto_point");
    pyClass.def("view_area", &GXLMSG_wrap_view_area,
                "view_area((float)arg1, (float)arg2, (float)arg3, (float)arg4, (GXIPJ)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sends a view area message\n\n"

                ":param arg1: X0 location\n"
                ":type arg1: float\n"
                ":param arg2: Y0 location\n"
                ":type arg2: float\n"
                ":param arg3: X1 location\n"
                ":type arg3: float\n"
                ":param arg4: Y1 location\n"
                ":type arg4: float\n"
                ":param arg5: IPJ (if (IPJ)0, default coordinate system)\n"
                ":type arg5: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.7\n\n"
               ).staticmethod("view_area");


}
