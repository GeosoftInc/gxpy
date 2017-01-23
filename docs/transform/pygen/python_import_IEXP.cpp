#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXIEXP_wrap_add_grid(GXIEXPPtr self, GXIMGPtr arg1, const gx_string_type& arg2)
{
    self->add_grid(arg1, arg2);
}
inline GXIEXPPtr GXIEXP_wrap_create()
{
    GXIEXPPtr ret = GXIEXP::create();
    return ret;
}
inline void GXIEXP_wrap_do_formula(GXIEXPPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->do_formula(arg1, arg2);
}

void gxPythonImportGXIEXP()
{

    class_<GXIEXP, GXIEXPPtr> pyClass("GXIEXP",
                                      "\n.. parsed-literal::\n\n"
                                      "   The IEXP class is similar to the EXP class, but is used\n"
                                      "   to apply math expressions to grids (IMG objects).\n\n"
                                      , no_init);

    pyClass.def("null", &GXIEXP::null, "null() -> GXIEXP\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXIEXP`\n\n:returns: A null :class:`geosoft.gxapi.GXIEXP`\n:rtype: :class:`geosoft.gxapi.GXIEXP`\n").staticmethod("null");
    pyClass.def("is_null", &GXIEXP::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXIEXP is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXIEXP`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXIEXP::_internal_handle);
    pyClass.def("add_grid", &GXIEXP_wrap_add_grid,
                "add_grid((GXIMG)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method adds an image to the IEXP object with a\n"
                "   variable name.\n\n"

                ":param arg1: Image to add\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Variable name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create", &GXIEXP_wrap_create,
                "create() -> GXIEXP:\n"

                "\n.. parsed-literal::\n\n"
                "   This method creates an IEXP object.\n\n"

                ":returns: IEXP Object\n"
                ":rtype: :class:`geosoft.gxapi.GXIEXP`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("do_formula", &GXIEXP_wrap_do_formula,
                "do_formula((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method runs a formula on the grids.\n\n"

                ":param arg1: Formula\n"
                ":type arg1: str\n"
                ":param arg2: Max. Buff size\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );


}
