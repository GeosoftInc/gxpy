#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXLPTPtr GXLPT_wrap_create()
{
    GXLPTPtr ret = GXLPT::create();
    return ret;
}
inline void GXLPT_wrap_get_lst(GXLPTPtr self, GXLSTPtr arg1)
{
    self->get_lst(arg1);
}
inline void GXLPT_wrap_get_standard_lst(GXLPTPtr self, GXLSTPtr arg1)
{
    self->get_standard_lst(arg1);
}

void gxPythonImportGXLPT()
{

    class_<GXLPT, GXLPTPtr> pyClass("GXLPT",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		This class allows access to the current default line patterns.\n"
                                    "   		It does not allow the definition of individual patterns. It is\n"
                                    "   		is used primarily with MAP class functions.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXLPT::null, "null() -> GXLPT\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXLPT`\n\n:returns: A null :class:`geosoft.gxapi.GXLPT`\n:rtype: :class:`geosoft.gxapi.GXLPT`\n").staticmethod("null");
    pyClass.def("is_null", &GXLPT::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXLPT is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXLPT`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXLPT::_internal_handle);
    pyClass.def("create", &GXLPT_wrap_create,
                "create() -> GXLPT:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a line pattern object with current default patterns.\n\n"

                ":returns: LPT Object\n"
                ":rtype: :class:`geosoft.gxapi.GXLPT`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("get_lst", &GXLPT_wrap_get_lst,
                "get_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copies all pattern names into a LST object.\n\n"

                ":param arg1: LST Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_standard_lst", &GXLPT_wrap_get_standard_lst,
                "get_standard_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copies the six standard line types into a LST object.\n\n"

                ":param arg1: LST Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The six standard line types are \"solid\", \"long dash\", \"dotted\", \"short dash\", \"long, short dash\" and \"dash dot\".\n\n"
               );


}
