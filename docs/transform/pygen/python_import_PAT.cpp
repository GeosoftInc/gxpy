#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXPATPtr GXPAT_wrap_create()
{
    GXPATPtr ret = GXPAT::create();
    return ret;
}
inline void GXPAT_wrap_get_lst(GXPATPtr self, const gx_string_type& arg1, GXLSTPtr arg2)
{
    self->get_lst(arg1, arg2);
}

void gxPythonImportGXPAT()
{

    class_<GXPAT, GXPATPtr> pyClass("GXPAT",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		A PAT object is created from a Geosoft-format pattern file.\n"
                                    "   		It contains all the individual patterns listed in the file.\n"
                                    "   \n"
                                    "   		Notes		You may create your own fill patterns should be added to the \"user.pat\"\n"
                                    "   		le in the <geosoft>\\user\\etc directory.\n"
                                    "   \n"
                                    "   		you wish to add your own fill patterns, create a file named user.pat in\n"
                                    "   		e <geosoft>/User/ directory and add your own fill patterns in the number\n"
                                    "   		nge 20000 to 29999.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXPAT::null, "null() -> GXPAT\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXPAT`\n\n:returns: A null :class:`geosoft.gxapi.GXPAT`\n:rtype: :class:`geosoft.gxapi.GXPAT`\n").staticmethod("null");
    pyClass.def("is_null", &GXPAT::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXPAT is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXPAT`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXPAT::_internal_handle);
    pyClass.def("create", &GXPAT_wrap_create,
                "create() -> GXPAT:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a pattern object with current default patterns.\n\n"

                ":returns: PAT object\n"
                ":rtype: :class:`geosoft.gxapi.GXPAT`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("get_lst", &GXPAT_wrap_get_lst,
                "get_lst((str)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copies all pattern names into a LST object.\n\n"

                ":param arg1: Class name (\"\" for all classes)\n"
                ":type arg1: str\n"
                ":param arg2: LST Handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns a list of the available patterns.\n"
                "   					There will always be at least two items,\n"
                "   					\"None\" and \"Solid Fill\"\n"
                "   				\n\n"
               );


}
