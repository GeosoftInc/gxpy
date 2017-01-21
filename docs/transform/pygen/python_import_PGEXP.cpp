#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXPGEXP_wrap_add_pager(GXPGEXPPtr self, GXPGPtr arg1, const gx_string_type& arg2)
{
    self->add_pager(arg1, arg2);
}
inline GXPGEXPPtr GXPGEXP_wrap_create()
{
    GXPGEXPPtr ret = GXPGEXP::create();
    return ret;
}
inline void GXPGEXP_wrap_do_formula(GXPGEXPPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->do_formula(arg1, arg2);
}

void gxPythonImportGXPGEXP()
{

    class_<GXPGEXP, GXPGEXPPtr> pyClass("GXPGEXP",
                                        "\n.. parsed-literal::\n\n"
                                        "   The PGEXP class is similar to the EXP class, but is used\n"
                                        "   to apply math expressions to pagers (PG objects).\n"
                                        "   \n"
                                        "   It works only on PGs of the same dimensions.\n\n"
                                        , no_init);

    pyClass.def("null", &GXPGEXP::null, "null() -> GXPGEXP\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXPGEXP`\n\n:returns: A null :class:`geosoft.gxapi.GXPGEXP`\n:rtype: :class:`geosoft.gxapi.GXPGEXP`\n").staticmethod("null");
    pyClass.def("is_null", &GXPGEXP::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXPGEXP is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXPGEXP`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXPGEXP::_internal_handle);
    pyClass.def("add_pager", &GXPGEXP_wrap_add_pager,
                "add_pager((GXPG)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method adds an pager to the PGEXP object with a\n"
                "   variable name.\n\n"

                ":param arg1: pager to add\n"
                ":type arg1: :class:`geosoft.gxapi.GXPG`\n"
                ":param arg2: Variable name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               );
    pyClass.def("create", &GXPGEXP_wrap_create,
                "create() -> GXPGEXP:\n"

                "\n.. parsed-literal::\n\n"
                "   This method creates an PGEXP object.\n\n"

                ":returns: PGEXP Object\n"
                ":rtype: :class:`geosoft.gxapi.GXPGEXP`\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               ).staticmethod("create");
    pyClass.def("do_formula", &GXPGEXP_wrap_do_formula,
                "do_formula((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   This method runs a formula on the pagers.\n\n"

                ":param arg1: Formula\n"
                ":type arg1: str\n"
                ":param arg2: Max. Buff size\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               );


}
