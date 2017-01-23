#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXTRPtr GXTR_wrap_create(int32_t arg1)
{
    GXTRPtr ret = GXTR::create(arg1);
    return ret;
}
inline void GXTR_wrap_copy(GXTRPtr self, GXTRPtr arg1)
{
    self->copy(arg1);
}

void gxPythonImportGXTR()
{

    class_<GXTR, GXTRPtr> pyClass("GXTR",
                                  "\n.. parsed-literal::\n\n"
                                  "   \n"
                                  "   		The TR object contains trend information about a grid or\n"
                                  "   		grid pager. Currently, it is used only in conjunction with\n"
                                  "   		the \\ :func:`geosoft.gxapi.GXIMG.get_tr`\\ , \\ :func:`geosoft.gxapi.GXIMG.set_tr`\\ , and \\ :func:`geosoft.gxapi.GXPGU.trend`\\  functions.\n"
                                  "   	\n\n"
                                  , no_init);

    pyClass.def("null", &GXTR::null, "null() -> GXTR\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXTR`\n\n:returns: A null :class:`geosoft.gxapi.GXTR`\n:rtype: :class:`geosoft.gxapi.GXTR`\n").staticmethod("null");
    pyClass.def("is_null", &GXTR::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXTR is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXTR`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXTR::_internal_handle);
    pyClass.def("create", &GXTR_wrap_create,
                "create((int)arg1) -> GXTR:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a Trend object\n\n"

                ":param arg1: Trend order (must >=0 and <=3)\n"
                ":type arg1: int\n"
                ":returns: TR Object\n"
                ":rtype: :class:`geosoft.gxapi.GXTR`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("copy", &GXTR_wrap_copy,
                "copy((GXTR)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method copies a table resource to another trend table resource.\n\n"

                ":param arg1: Source Trend Object to Copy\n"
                ":type arg1: :class:`geosoft.gxapi.GXTR`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.1.0\n\n"
               );


}
