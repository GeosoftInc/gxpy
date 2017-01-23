#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXTRND_wrap_get_max_min(GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, double arg7, int32_t arg8)
{
    GXTRND::get_max_min(arg1, arg2, arg3, arg4, arg5, arg6, arg7, (TRND_NODE)arg8);
}
inline void GXTRND_wrap_get_mesh(GXDBPtr arg1, const gx_string_type& arg2, double arg3, double arg4, GXVVPtr arg5, int32_t arg6)
{
    GXTRND::get_mesh(arg1, arg2, arg3, arg4, arg5, (TRND_NODE)arg6);
}
inline void GXTRND_wrap_trnd_db(GXDBPtr arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10)
{
    GXTRND::trnd_db(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10);
}

void gxPythonImportGXTRND()
{

    class_<GXTRND, boost::noncopyable> pyClass("GXTRND",
            "\n.. parsed-literal::\n\n"
            "   The TRND methods are used to determine trend directions in database data by locating\n"
            "   maxima and minima along lines and joining them in a specified direction.\n"
            "   The resulting trend lines are appended to the database and used by gridding methods\n"
            "   such as Bigrid and Rangrid to enforce features in the specified direction.\n\n"
            , no_init);


    pyClass.def("get_max_min", &GXTRND_wrap_get_max_min,
                "get_max_min((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (float)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Find the max/min nodes in a line.\n\n"

                ":param arg1: X Channel\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y Channel\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Data Channel\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: X MaxMin (returned)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Y MaxMin (returned)\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Data MaxMin (returned)\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: MaxMin Window\n"
                ":type arg7: float\n"
                ":param arg8: \\ :ref:`TRND_NODE`\\ \n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Trend lines positions consist of X and Y VVs\n\n"
               ).staticmethod("get_max_min");
    pyClass.def("get_mesh", &GXTRND_wrap_get_mesh,
                "get_mesh((GXDB)arg1, (str)arg2, (float)arg3, (float)arg4, (GXVV)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the lines in a trend mesh.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Selected channel\n"
                ":type arg2: str\n"
                ":param arg3: MaxMin Window\n"
                ":type arg3: float\n"
                ":param arg4: Maximum join length\n"
                ":type arg4: float\n"
                ":param arg5: VV of type GS_D2POINT (returned)\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: \\ :ref:`TRND_NODE`\\ \n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("get_mesh");
    pyClass.def("trnd_db", &GXTRND_wrap_trnd_db,
                "trnd_db((GXDB)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Uses a selected channel to find data trends in a database.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Selected channel\n"
                ":type arg2: str\n"
                ":param arg3: MaxMin Window\n"
                ":type arg3: float\n"
                ":param arg4: Preferred angle, degrees CCW from X\n"
                ":type arg4: float\n"
                ":param arg5: Allowed deviation\n"
                ":type arg5: float\n"
                ":param arg6: Longest join\n"
                ":type arg6: float\n"
                ":param arg7: Maximum deflection in join (can be rDUMMY)\n"
                ":type arg7: float\n"
                ":param arg8: Minimum length for trend lines (can be rDUMMY)\n"
                ":type arg8: float\n"
                ":param arg9: Resampling distance (can be rDUMMY)\n"
                ":type arg9: float\n"
                ":param arg10: Breaking angle, degrees CCW from X (can be rDUMMY)\n"
                ":type arg10: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("trnd_db");

    scope().attr("TRND_MIN") = (int32_t)0;
    scope().attr("TRND_MAX") = (int32_t)1;

}
