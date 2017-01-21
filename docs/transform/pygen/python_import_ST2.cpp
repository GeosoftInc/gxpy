#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXST2Ptr GXST2_wrap_create()
{
    GXST2Ptr ret = GXST2::create();
    return ret;
}
inline void GXST2_wrap_data_vv(GXST2Ptr self, GXVVPtr arg1, GXVVPtr arg2)
{
    self->data_vv(arg1, arg2);
}
inline int32_t GXST2_wrap_items(GXST2Ptr self)
{
    int32_t ret = self->items();
    return ret;
}
inline void GXST2_wrap_reset(GXST2Ptr self)
{
    self->reset();
}
inline double GXST2_wrap_get(GXST2Ptr self, int32_t arg1)
{
    double ret = self->get((ST2_CORRELATION)arg1);
    return ret;
}

void gxPythonImportGXST2()
{

    class_<GXST2, GXST2Ptr> pyClass("GXST2",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		Bi-variate statistics. The ST2 class accumulates statistics\n"
                                    "   		on two data vectors simultaneously in order to compute correlation\n"
                                    "   		information. Statistics are accumulated using the \\ :func:`geosoft.gxapi.GXST2.data_vv`\\  function.\n"
                                    "   		See also ST (mono-variate statistics).\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXST2::null, "null() -> GXST2\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXST2`\n\n:returns: A null :class:`geosoft.gxapi.GXST2`\n:rtype: :class:`geosoft.gxapi.GXST2`\n").staticmethod("null");
    pyClass.def("is_null", &GXST2::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXST2 is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXST2`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXST2::_internal_handle);
    pyClass.def("create", &GXST2_wrap_create,
                "create() -> GXST2:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a statistics object which is used to accumulate statistics.\n\n"

                ":returns: ST2 Object\n"
                ":rtype: :class:`geosoft.gxapi.GXST2`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("data_vv", &GXST2_wrap_data_vv,
                "data_vv((GXVV)arg1, (GXVV)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add all the values in VVx and VVy to ST2 object.\n\n"

                ":param arg1: VVx handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: VVy handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("items", &GXST2_wrap_items,
                "items() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets Number of items\n\n"

                ":returns: Number of items in ST2\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("reset", &GXST2_wrap_reset,
                "reset() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Resets the Statistics.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get", &GXST2_wrap_get,
                "get((int)arg1) -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Gets correlation coeff. from the ST2 object.\n\n"

                ":param arg1: \\ :ref:`ST2_CORRELATION`\\ \n"
                ":type arg1: int\n"
                ":returns: Data you asked for\n"
                "          						GS_R8DM for none\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );

    scope().attr("ST2_CORR") = (int32_t)0;
    scope().attr("ST2_PCORR") = (int32_t)1;

}
