#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXVOXEPtr GXVOXE_wrap_create(GXVOXPtr arg1)
{
    GXVOXEPtr ret = GXVOXE::create(arg1);
    return ret;
}
inline void GXVOXE_wrap_profile(GXVOXEPtr self, GXVVPtr arg1, GXVVPtr arg2, GXVVPtr arg3, GXVVPtr arg4, int32_t arg5)
{
    self->profile(arg1, arg2, arg3, arg4, (VOXE_EVAL)arg5);
}
inline double GXVOXE_wrap_value(GXVOXEPtr self, double arg1, double arg2, double arg3, int32_t arg4)
{
    double ret = self->value(arg1, arg2, arg3, (VOXE_EVAL)arg4);
    return ret;
}
inline void GXVOXE_wrap_vector(GXVOXEPtr self, double arg1, double arg2, double arg3, double arg4, double arg5, double arg6, GXVVPtr arg7, int32_t arg8)
{
    self->vector(arg1, arg2, arg3, arg4, arg5, arg6, arg7, (VOXE_EVAL)arg8);
}

void gxPythonImportGXVOXE()
{

    class_<GXVOXE, GXVOXEPtr> pyClass("GXVOXE",
                                      "\n.. parsed-literal::\n\n"
                                      "   \n"
                                      "   		VOX evaluator class. Used to sample values from\n"
                                      "   		the voxel.\n"
                                      "   	\n\n"
                                      , no_init);

    pyClass.def("null", &GXVOXE::null, "null() -> GXVOXE\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXVOXE`\n\n:returns: A null :class:`geosoft.gxapi.GXVOXE`\n:rtype: :class:`geosoft.gxapi.GXVOXE`\n").staticmethod("null");
    pyClass.def("is_null", &GXVOXE::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXVOXE is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXVOXE`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXVOXE::_internal_handle);
    pyClass.def("create", &GXVOXE_wrap_create,
                "create((GXVOX)arg1) -> GXVOXE:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a handle to an VOXE object\n\n"

                ":param arg1: VOX Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXVOX`\n"
                ":returns: VOXE handle, terminates if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXVOXE`\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               ).staticmethod("create");
    pyClass.def("profile", &GXVOXE_wrap_profile,
                "profile((GXVV)arg1, (GXVV)arg2, (GXVV)arg3, (GXVV)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Extract a profile of data along points provided.\n\n"

                ":param arg1: X VV (must be double)\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Y VV (must be double)\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Z VV (must be double)\n"
                ":type arg3: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg4: D VV (must be double)\n"
                ":type arg4: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg5: \\ :ref:`VOXE_EVAL`\\ \n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("value", &GXVOXE_wrap_value,
                "value((float)arg1, (float)arg2, (float)arg3, (int)arg4) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a value at a specific point\n\n"

                ":param arg1: X Location\n"
                ":type arg1: float\n"
                ":param arg2: Y Location\n"
                ":type arg2: float\n"
                ":param arg3: Z Location\n"
                ":type arg3: float\n"
                ":param arg4: \\ :ref:`VOXE_EVAL`\\ \n"
                ":type arg4: int\n"
                ":returns: Value at the point or DUMMY if not valid\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );
    pyClass.def("vector", &GXVOXE_wrap_vector,
                "vector((float)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (GXVV)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Extract a profile of data along a vector\n\n"

                ":param arg1: X Origin\n"
                ":type arg1: float\n"
                ":param arg2: Y Origin\n"
                ":type arg2: float\n"
                ":param arg3: Z Origin\n"
                ":type arg3: float\n"
                ":param arg4: X Delta\n"
                ":type arg4: float\n"
                ":param arg5: Y Delta\n"
                ":type arg5: float\n"
                ":param arg6: Z Delta\n"
                ":type arg6: float\n"
                ":param arg7: Data VV (must be double)\n"
                ":type arg7: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg8: \\ :ref:`VOXE_EVAL`\\ \n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"
               );

    scope().attr("VOXE_EVAL_NEAR") = (int32_t)0;
    scope().attr("VOXE_EVAL_INTERP") = (int32_t)1;
    scope().attr("VOXE_EVAL_BEST") = (int32_t)2;

}
