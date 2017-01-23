#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXVVEXP_wrap_add_vv(GXVVEXPPtr self, GXVVPtr arg1, const gx_string_type& arg2)
{
    self->add_vv(arg1, arg2);
}
inline GXVVEXPPtr GXVVEXP_wrap_create()
{
    GXVVEXPPtr ret = GXVVEXP::create();
    return ret;
}
inline void GXVVEXP_wrap_do_formula(GXVVEXPPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->do_formula(arg1, arg2);
}

void gxPythonImportGXVVEXP()
{

    class_<GXVVEXP, GXVVEXPPtr> pyClass("GXVVEXP",
                                        "\n.. parsed-literal::\n\n"
                                        "   The VVEXP class is similar to the IEXP class, but is used\n"
                                        "   to apply math expressions to VV objects.\n\n"
                                        , no_init);

    pyClass.def("null", &GXVVEXP::null, "null() -> GXVVEXP\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXVVEXP`\n\n:returns: A null :class:`geosoft.gxapi.GXVVEXP`\n:rtype: :class:`geosoft.gxapi.GXVVEXP`\n").staticmethod("null");
    pyClass.def("is_null", &GXVVEXP::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXVVEXP is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXVVEXP`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXVVEXP::_internal_handle);
    pyClass.def("add_vv", &GXVVEXP_wrap_add_vv,
                "add_vv((GXVV)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method adds a VV to the VVEXP object with a\n"
                "   variable name.\n\n"

                ":param arg1: VV to add\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Variable name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("create", &GXVVEXP_wrap_create,
                "create() -> GXVVEXP:\n"

                "\n.. parsed-literal::\n\n"
                "   This method creates an VVEXP object.\n\n"

                ":returns: VVEXP Object\n"
                ":rtype: :class:`geosoft.gxapi.GXVVEXP`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("create");
    pyClass.def("do_formula", &GXVVEXP_wrap_do_formula,
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

                "\n.. versionadded:: 6.2.0\n\n"
               );


}
