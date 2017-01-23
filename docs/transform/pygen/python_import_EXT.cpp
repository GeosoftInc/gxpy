#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXEXT_wrap_get_info(const gx_string_type& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, GXIPJPtr arg6)
{
    GXEXT::get_info(arg1, arg2, arg3, arg4, arg5, arg6);
}

void gxPythonImportGXEXT()
{

    class_<GXEXT, boost::noncopyable> pyClass("GXEXT",
            "\n.. parsed-literal::\n\n"
            "   External (plug-in) image methods.\n\n"
            , no_init);


    pyClass.def("get_info", &GXEXT_wrap_get_info,
                "get_info((str)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (GXIPJ)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieves information about an external image format.\n\n"

                ":param arg1: Image Name\n"
                ":type arg1: str\n"
                ":param arg2: X Min\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y Min\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: X Max\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Y Max\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Projection Information\n"
                ":type arg6: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_info");


}
