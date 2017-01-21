#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXMAPLPtr GXMAPL_wrap_create(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXMAPLPtr ret = GXMAPL::create(arg1, arg2, arg3);
    return ret;
}
inline GXMAPLPtr GXMAPL_wrap_create_reg(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3, GXREGPtr arg4)
{
    GXMAPLPtr ret = GXMAPL::create_reg(arg1, arg2, arg3, arg4);
    return ret;
}
inline void GXMAPL_wrap_process(GXMAPLPtr self, GXMAPPtr arg1)
{
    self->process(arg1);
}
inline void GXMAPL_wrap_replace_string(GXMAPLPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->replace_string(arg1, arg2);
}

void gxPythonImportGXMAPL()
{

    class_<GXMAPL, GXMAPLPtr> pyClass("GXMAPL",
                                      "\n.. parsed-literal::\n\n"
                                      "   \n"
                                      "   		The MAPL class is the interface with the MAPPLOT program,\n"
                                      "   		which reads a MAPPLOT control file and plots graphical\n"
                                      "   		entities to a map. The MAPL object is created for a given\n"
                                      "   		control file, then passed to the MAPPLOT program, along\n"
                                      "   		with the target MAP object on which to do the drawing\n"
                                      "   	\n\n"
                                      , no_init);

    pyClass.def("null", &GXMAPL::null, "null() -> GXMAPL\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXMAPL`\n\n:returns: A null :class:`geosoft.gxapi.GXMAPL`\n:rtype: :class:`geosoft.gxapi.GXMAPL`\n").staticmethod("null");
    pyClass.def("is_null", &GXMAPL::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXMAPL is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXMAPL`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXMAPL::_internal_handle);
    pyClass.def("create", &GXMAPL_wrap_create,
                "create((str)arg1, (str)arg2, (int)arg3) -> GXMAPL:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a MAPL.\n\n"

                ":param arg1: MAPL file name\n"
                ":type arg1: str\n"
                ":param arg2: map base reference name\n"
                ":type arg2: str\n"
                ":param arg3: start line number in file (0 is first)\n"
                ":type arg3: int\n"
                ":returns: MAPL, aborts if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXMAPL`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The default map groups will use the reference name with\n"
                "   					\"_Data\" and \"_Base\" added.  If no reference name is specified,\n"
                "   					the name \"MAPL\" is used\n"
                "   				\n\n"
               ).staticmethod("create");
    pyClass.def("create_reg", &GXMAPL_wrap_create_reg,
                "create_reg((str)arg1, (str)arg2, (int)arg3, (GXREG)arg4) -> GXMAPL:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a MAPL with REG.\n\n"

                ":param arg1: MAPL file name\n"
                ":type arg1: str\n"
                ":param arg2: map base reference name\n"
                ":type arg2: str\n"
                ":param arg3: start line number in file (0 is first)\n"
                ":type arg3: int\n"
                ":param arg4: REG\n"
                ":type arg4: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: MAPL, aborts if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXMAPL`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The default map groups will use the reference name with\n"
                "   					\"_Data\" and \"_Base\" added.  If no reference name is specified,\n"
                "   					the name \"MAPL\" is used\n"
                "   				\n\n"
               ).staticmethod("create_reg");
    pyClass.def("process", &GXMAPL_wrap_process,
                "process((GXMAP)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Process a MAPL\n\n"

                ":param arg1: MAP\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("replace_string", &GXMAPL_wrap_replace_string,
                "replace_string((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Adds a replacement string to a mapplot control file.\n\n"

                ":param arg1: Variable\n"
                ":type arg1: str\n"
                ":param arg2: Replacement\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );


}
