#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXVAU_wrap_prune(GXVAPtr arg1, GXVVPtr arg2, int32_t arg3)
{
    GXVAU::prune(arg1, arg2, (VAU_PRUNE)arg3);
}
inline void GXVAU_wrap_total_vector(GXVAPtr arg1, GXVAPtr arg2, GXVAPtr arg3, GXVAPtr arg4)
{
    GXVAU::total_vector(arg1, arg2, arg3, arg4);
}

void gxPythonImportGXVAU()
{

    class_<GXVAU, boost::noncopyable> pyClass("GXVAU",
            "\n.. parsed-literal::\n\n"
            "   This is not a class. These are methods that work on\n"
            "   data stored in VA objects\n\n"
            , no_init);


    pyClass.def("prune", &GXVAU_wrap_prune,
                "prune((GXVA)arg1, (GXVV)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Prune values from a VA based on reference VA\n\n"

                ":param arg1: VA to prune\n"
                ":type arg1: :class:`geosoft.gxapi.GXVA`\n"
                ":param arg2: Reference VV\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: \\ :ref:`VAU_PRUNE`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Pruning will shorten the VA by removing values\n"
                "   that are either dummy or non-dummy in the reference\n"
                "   VA\n\n"
               ).staticmethod("prune");
    pyClass.def("total_vector", &GXVAU_wrap_total_vector,
                "total_vector((GXVA)arg1, (GXVA)arg2, (GXVA)arg3, (GXVA)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate total vector for X,Y and Z components\n\n"

                ":param arg1: X Component object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVA`\n"
                ":param arg2: Y Component object\n"
                ":type arg2: :class:`geosoft.gxapi.GXVA`\n"
                ":param arg3: Z Component object\n"
                ":type arg3: :class:`geosoft.gxapi.GXVA`\n"
                ":param arg4: Returned total vector VA object\n"
                ":type arg4: :class:`geosoft.gxapi.GXVA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("total_vector");

    scope().attr("VAU_PRUNE_DUMMY") = (int32_t)0;
    scope().attr("VAU_PRUNE_VALID") = (int32_t)1;

}
