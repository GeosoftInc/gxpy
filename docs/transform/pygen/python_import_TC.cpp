#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXTCPtr GXTC_wrap_create(GXIMGPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, int32_t arg8, double arg9, int32_t arg10)
{
    GXTCPtr ret = GXTC::create(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (TC_OPT)arg10);
    return ret;
}
inline GXTCPtr GXTC_wrap_create_ex(GXIMGPtr arg1, double arg2, double arg3, double arg4, double arg5, double arg6, double arg7, int32_t arg8, double arg9, int32_t arg10, int32_t arg11)
{
    GXTCPtr ret = GXTC::create_ex(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (TC_OPT)arg10, (TC_SURVEYTYPE)arg11);
    return ret;
}
inline void GXTC_wrap_grregter(GXTCPtr self, GXIMGPtr arg1, GXIMGPtr arg2)
{
    self->grregter(arg1, arg2);
}
inline void GXTC_wrap_grterain(GXTCPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, GXIMGPtr arg6, double arg7)
{
    self->grterain(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXTC_wrap_grterain2(GXTCPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, GXVVPtr arg5, GXVVPtr arg6, GXIMGPtr arg7, double arg8)
{
    self->grterain2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}
inline void GXTC_wrap_g_gterain(GXTCPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, double arg5, double arg6, int32_t arg7)
{
    self->g_gterain(arg1, arg2, arg3, arg4, arg5, arg6, (GG_ELEMENT)arg7);
}

void gxPythonImportGXTC()
{

    class_<GXTC, GXTCPtr> pyClass("GXTC",
                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		The TC object is used in gravitational modelling to create\n"
                                  "   		a terrain correction grid from a topography grid. This is\n"
                                  "   		accomplished with a call first to \\ :func:`geosoft.gxapi.GXTC.grregter`\\ , which determines\n"
                                  "   		the terrain correction from an input topography grid, then\n"
                                  "   		to \\ :func:`geosoft.gxapi.GXTC.grterain`\\ , which calculates the actual corrections at\n"
                                  "   		the input positions.\n"
                                  "   	\n\n"
                                  , no_init);

    pyClass.def("null", &GXTC::null, "null() -> GXTC\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXTC`\n\n:returns: A null :class:`geosoft.gxapi.GXTC`\n:rtype: :class:`geosoft.gxapi.GXTC`\n").staticmethod("null");
    pyClass.def("is_null", &GXTC::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXTC is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXTC`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXTC::_internal_handle);
    pyClass.def("create", &GXTC_wrap_create,
                "create((GXIMG)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (int)arg8, (float)arg9, (int)arg10) -> GXTC:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a Terrain Correction object\n\n"

                ":param arg1: topo (DEM) grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: elevation unit in 1 metre (i.e. 0.3048 for feet)\n"
                ":type arg2: float\n"
                ":param arg3: inner distance (in topo grid projection units, default in metres)\n"
                ":type arg3: float\n"
                ":param arg4: outer distance (in topo grid projection units, default in metres)\n"
                ":type arg4: float\n"
                ":param arg5: terrain density in g/cc\n"
                ":type arg5: float\n"
                ":param arg6: water density in g/cc\n"
                ":type arg6: float\n"
                ":param arg7: water reference elevation (in elevation unit)\n"
                ":type arg7: float\n"
                ":param arg8: ``True`` to calculate an edge correction (compensation)\n"
                ":type arg8: int\n"
                ":param arg9: average elevation beyond max distance (in elevation unit)\n"
                ":type arg9: float\n"
                ":param arg10: \\ :ref:`TC_OPT`\\ \n"
                ":type arg10: int\n"
                ":returns: TC Object\n"
                ":rtype: :class:`geosoft.gxapi.GXTC`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_ex", &GXTC_wrap_create_ex,
                "create_ex((GXIMG)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (float)arg7, (int)arg8, (float)arg9, (int)arg10, (int)arg11) -> GXTC:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a Terrain Correction object	with surveytype\n\n"

                ":param arg1: topo (DEM) grid\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: elevation unit in 1 metre (i.e. 0.3048 for feet)\n"
                ":type arg2: float\n"
                ":param arg3: inner distance (in topo grid projection units, default in metres)\n"
                ":type arg3: float\n"
                ":param arg4: outer distance (in topo grid projection units, default in metres)\n"
                ":type arg4: float\n"
                ":param arg5: terrain density in g/cc\n"
                ":type arg5: float\n"
                ":param arg6: water density in g/cc\n"
                ":type arg6: float\n"
                ":param arg7: water reference elevation (in elevation unit)\n"
                ":type arg7: float\n"
                ":param arg8: ``True`` to calculate an edge correction (compensation)\n"
                ":type arg8: int\n"
                ":param arg9: average elevation beyond max distance (in elevation unit)\n"
                ":type arg9: float\n"
                ":param arg10: \\ :ref:`TC_OPT`\\ \n"
                ":type arg10: int\n"
                ":param arg11: \\ :ref:`TC_SURVEYTYPE`\\ \n"
                ":type arg11: int\n"
                ":returns: TC Object\n"
                ":rtype: :class:`geosoft.gxapi.GXTC`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("create_ex");
    pyClass.def("grregter", &GXTC_wrap_grregter,
                "grregter((GXIMG)arg1, (GXIMG)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a terrain correction grid for a topo grid.\n\n"

                ":param arg1: Input IMG (local DEM topo grid used for station elevation)\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Image of output grid\n"
                ":type arg2: :class:`geosoft.gxapi.GXIMG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("grterain", &GXTC_wrap_grterain,
                "grterain((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (GXIMG)arg6, (float)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate terrain corrections.\n\n"

                ":param arg1: input X channel data (in topo grid projection units, default in metres)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: input Y channel data (in topo grid projection units, default in metres)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: input Elevation channel data (in elevation unit)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: input slope channel data\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: output Terrain Corrected channel data\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: Image of input correction grid\n"
                ":type arg6: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg7: Terrain density (default 2.67)\n"
                ":type arg7: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("grterain2", &GXTC_wrap_grterain2,
                "grterain2((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (GXVV)arg5, (GXVV)arg6, (GXIMG)arg7, (float)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate terrain corrections (work for marine gravity too).\n\n"

                ":param arg1: input X channel data (in topo grid projection units, default in metres)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: input Y channel data (in topo grid projection units, default in metres)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: input Elevation channel data (in elevation unit)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: input slope channel data\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: input Water depth channel data (in metres)\n"
                ":type arg5: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg6: output Terrain Corrected channel data\n"
                ":type arg6: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg7: Image of input correction grid\n"
                ":type arg7: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg8: Terrain density (default 2.67)\n"
                ":type arg8: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("g_gterain", &GXTC_wrap_g_gterain,
                "g_gterain((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (float)arg5, (float)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate GG terrain corrections\n\n"

                ":param arg1: input X channel data (in topo grid projection units, default in metres)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: input Y channel data (in topo grid projection units, default in metres)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: input Elevation channel data (in elevation unit)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: output Terrain Corrected channel data\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: Terrain density (default 2.67)\n"
                ":type arg5: float\n"
                ":param arg6: Terrain reference level (default 0.0)\n"
                ":type arg6: float\n"
                ":param arg7: \\ :ref:`GG_ELEMENT`\\ \n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );

    scope().attr("TC_OPT_NONE") = (int32_t)0;
    scope().attr("TC_OPT_MAX") = (int32_t)1;
    scope().attr("TC_SURVEYTYPE_GROUND") = (int32_t)0;
    scope().attr("TC_SURVEYTYPE_SHIPBORNE") = (int32_t)1;
    scope().attr("TC_SURVEYTYPE_AIRBORNE") = (int32_t)2;
    scope().attr("GG_ELEMENT_XX") = (int32_t)0;
    scope().attr("GG_ELEMENT_YY") = (int32_t)1;
    scope().attr("GG_ELEMENT_XY") = (int32_t)2;
    scope().attr("GG_ELEMENT_XZ") = (int32_t)3;
    scope().attr("GG_ELEMENT_YZ") = (int32_t)4;

}
