#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXEUL3_wrap_destr(GXEUL3Ptr self)
{
    self->destr();
}
inline GXEUL3Ptr GXEUL3_wrap_creat(GXIMGPtr arg1, GXIMGPtr arg2, GXIMGPtr arg3, GXIMGPtr arg4, int32_t arg5, double arg6, double arg7, double arg8, int32_t arg9, double arg10, double arg11)
{
    GXEUL3Ptr ret = GXEUL3::creat(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11);
    return ret;
}
inline void GXEUL3_wrap_get_result(GXEUL3Ptr self, GXVVPtr arg1, int32_t arg2)
{
    self->get_result(arg1, (EUL3_RESULT)arg2);
}
inline void GXEUL3_wrap_write(GXEUL3Ptr self, const gx_string_type& arg1)
{
    self->write(arg1);
}
inline int32_t GXEUL3_wrap_ex_euler_derive(GXVVPtr arg1, double arg2, GXVVPtr arg3, int32_t arg4, GXVVPtr arg5, GXVVPtr arg6, int32_t arg7)
{
    int32_t ret = GXEUL3::ex_euler_derive(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
    return ret;
}
inline int32_t GXEUL3_wrap_ex_euler_calc(int32_t arg1, double arg2, int32_t arg3, double arg4, double arg5, double arg6, double arg7, double arg8, double arg9, double arg10, int32_t arg11, GXVVPtr arg12, GXVVPtr arg13, GXVVPtr arg14, GXVVPtr arg15, int32_t arg16, GXVVPtr arg17, GXVVPtr arg18, GXVVPtr arg19, GXVVPtr arg20)
{
    int32_t ret = GXEUL3::ex_euler_calc(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20);
    return ret;
}

void gxPythonImportGXEUL3()
{

    class_<GXEUL3, GXEUL3Ptr> pyClass("GXEUL3",
                                      "\n.. parsed-literal::\n\n"
                                      "   This is a specialized class which performs 3D Euler deconvolution\n"
                                      "   for potential field interpretation.\n\n"
                                      , no_init);

    pyClass.def("null", &GXEUL3::null, "null() -> GXEUL3\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXEUL3`\n\n:returns: A null :class:`geosoft.gxapi.GXEUL3`\n:rtype: :class:`geosoft.gxapi.GXEUL3`\n").staticmethod("null");
    pyClass.def("is_null", &GXEUL3::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXEUL3 is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXEUL3`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXEUL3::_internal_handle);
    pyClass.def("destr", &GXEUL3_wrap_destr,
                "destr() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Destroys a EUL3 object.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("creat", &GXEUL3_wrap_creat,
                "creat((GXIMG)arg1, (GXIMG)arg2, (GXIMG)arg3, (GXIMG)arg4, (int)arg5, (float)arg6, (float)arg7, (float)arg8, (int)arg9, (float)arg10, (float)arg11) -> GXEUL3:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates an EUL3 object.\n\n"

                ":param arg1: Image of grid T\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Image of grid Tx\n"
                ":type arg2: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg3: Image of grid Ty\n"
                ":type arg3: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg4: Image of grid Tz\n"
                ":type arg4: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg5: Window size (maximum 20)\n"
                ":type arg5: int\n"
                ":param arg6: Geometric index, from 0.0 to 3.0\n"
                ":type arg6: float\n"
                ":param arg7: Max tolerance to allow (percentage)\n"
                ":type arg7: float\n"
                ":param arg8: Max dist. acceptable (0 for infinite)\n"
                ":type arg8: float\n"
                ":param arg9: ObsFlg  Height (0) or Elevation (1)\n"
                ":type arg9: int\n"
                ":param arg10: Height of observation plane\n"
                ":type arg10: float\n"
                ":param arg11: Elevation of observation plane\n"
                ":type arg11: float\n"
                ":returns: EUL3 Object\n"
                ":rtype: :class:`geosoft.gxapi.GXEUL3`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("creat");
    pyClass.def("get_result", &GXEUL3_wrap_get_result,
                "get_result((GXVV)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a result field VV from EUL3 object\n\n"

                ":param arg1: VV to store the result\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: \\ :ref:`EUL3_RESULT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("write", &GXEUL3_wrap_write,
                "write((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write the results of EUL3 object to output file.\n\n"

                ":param arg1: Output File Name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("ex_euler_derive", &GXEUL3_wrap_ex_euler_derive,
                "ex_euler_derive((GXVV)arg1, (float)arg2, (GXVV)arg3, (int)arg4, (GXVV)arg5, (GXVV)arg6, (int)arg7) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculates gradients\n\n"

                ":param arg1: Input distance\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Sample Interval\n"
                ":type arg2: float\n"
                ":param arg3: Input mag\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: SampleCount\n"
                ":type arg4: int\n"
                ":param arg5: Horizontal Gradient out\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Vertical Gradient out\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Output array size limit\n"
                ":type arg7: int\n"
                ":returns: 0 for OK, -1 for Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("ex_euler_derive");
    pyClass.def("ex_euler_calc", &GXEUL3_wrap_ex_euler_calc,
                "ex_euler_calc((int)arg1, (float)arg2, (int)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (int)arg11, (GXVV)arg12, (GXVV)arg13, (GXVV)arg14, (GXVV)arg15, (int)arg16, (GXVV)arg17, (GXVV)arg18, (GXVV)arg19, (GXVV)arg20) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Does the exeuler depth calculations\n\n"

                ":param arg1: Solution type flag (0 for contacts, 1 for dykes)\n"
                ":type arg1: int\n"
                ":param arg2: Structural index value (used only when generating dykes)\n"
                ":type arg2: float\n"
                ":param arg3: Window length\n"
                ":type arg3: int\n"
                ":param arg4: Field strength in nT\n"
                ":type arg4: float\n"
                ":param arg5: Inclination\n"
                ":type arg5: float\n"
                ":param arg6: Declination\n"
                ":type arg6: float\n"
                ":param arg7: Profile azimuth wrt north\n"
                ":type arg7: float\n"
                ":param arg8: Minimum depth for returned solutions\n"
                ":type arg8: float\n"
                ":param arg9: Maximum depth for returned solutions\n"
                ":type arg9: float\n"
                ":param arg10: Percentage error allowed before rejection\n"
                ":type arg10: float\n"
                ":param arg11: Number of points in profile\n"
                ":type arg11: int\n"
                ":param arg12: Array of point distances along profile\n"
                ":type arg12: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg13: Array of observed values\n"
                ":type arg13: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg14: Array of horizontal derivative values. Can be NULL for calculated\n"
                ":type arg14: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg15: Array of vertical derivative values. Can be NULL for calculated\n"
                ":type arg15: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg16: Length of solutions arrays passed in\n"
                ":type arg16: int\n"
                ":param arg17: The profile distance for each solution\n"
                ":type arg17: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg18: The depth for each solution\n"
                ":type arg18: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg19: The dip for each solution\n"
                ":type arg19: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg20: The susceptibility for each solution\n"
                ":type arg20: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: >0 for OK, -1 for Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("ex_euler_calc");

    scope().attr("EUL3_RESULT_X") = (int32_t)1;
    scope().attr("EUL3_RESULT_Y") = (int32_t)2;
    scope().attr("EUL3_RESULT_DEPTH") = (int32_t)3;
    scope().attr("EUL3_RESULT_BACKGROUND") = (int32_t)4;
    scope().attr("EUL3_RESULT_DEPTHERROR") = (int32_t)5;
    scope().attr("EUL3_RESULT_LOCATIONERROR") = (int32_t)6;
    scope().attr("EUL3_RESULT_WINDOWX") = (int32_t)7;
    scope().attr("EUL3_RESULT_WINDOWY") = (int32_t)8;

}
