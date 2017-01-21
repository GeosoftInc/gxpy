#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXEXPPtr GXEXP_wrap_create(GXDBPtr arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXEXPPtr ret = GXEXP::create(arg1, arg2, arg3);
    return ret;
}
inline GXEXPPtr GXEXP_wrap_create_file(GXDBPtr arg1, const gx_string_type& arg2)
{
    GXEXPPtr ret = GXEXP::create_file(arg1, arg2);
    return ret;
}

void gxPythonImportGXEXP()
{

    class_<GXEXP, GXEXPPtr> pyClass("GXEXP",
                                    "\n.. parsed-literal::\n\n"
                                    "   EXP objects are created from text strings that contain\n"
                                    "   C-like math to be applied to channels in a database.\n"
                                    "   It is used with the \\ :func:`geosoft.gxapi.GXDU.math`\\  function (see DU). See also\n"
                                    "   IEXP for applying math expressions to images (grids).\n"
                                    "   See also \\ :func:`geosoft.gxapi.GXDU.math`\\  applies expressions to the database\n\n"
                                    , no_init);

    pyClass.def("null", &GXEXP::null, "null() -> GXEXP\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXEXP`\n\n:returns: A null :class:`geosoft.gxapi.GXEXP`\n:rtype: :class:`geosoft.gxapi.GXEXP`\n").staticmethod("null");
    pyClass.def("is_null", &GXEXP::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXEXP is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXEXP`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXEXP::_internal_handle);
    pyClass.def("create", &GXEXP_wrap_create,
                "create((GXDB)arg1, (str)arg2, (int)arg3) -> GXEXP:\n"

                "\n.. parsed-literal::\n\n"
                "   This method creates an EXP object.\n\n"

                ":param arg1: Database Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Expression using channel names\n"
                ":type arg2: str\n"
                ":param arg3: Maximum size of expression after expanding all local variables (those with $ prefix).\n"
                ":type arg3: int\n"
                ":returns: EXP Object\n"
                ":rtype: :class:`geosoft.gxapi.GXEXP`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Expressions are strings that contain C-like math to be\n"
                "   applied to channels in a database.  For example, following\n"
                "   an expression:\n"
                "   \n"
                "      \"@a = mag-64000; @b = gravity\\ `*`\\ 100;\n"
                "       $sRatio = @a/@b;\n"
                "       MULT = @a \\ `*`\\ @b;\"\n"
                "   \n"
                "   Rules:\n"
                "   \n"
                "      ;  - terminates a sub-expression\n"
                "      @  - prefix to a temporary name, which is a double precision\n"
                "           floating point number to be used later in the same\n"
                "           expression.\n"
                "      $  - prefix to a local GX variable name.  Such names will be\n"
                "           evaluated to the variable value at the time \\ :func:`geosoft.gxapi.GXEXP.create`\\ \n"
                "           is called.\n"
                "   \n"
                "      All other tokens are assumed to be channel names.\n\n"
               ).staticmethod("create");
    pyClass.def("create_file", &GXEXP_wrap_create_file,
                "create_file((GXDB)arg1, (str)arg2) -> GXEXP:\n"

                "\n.. parsed-literal::\n\n"
                "   This method creates an EXP object from a file\n\n"

                ":param arg1: Database Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: File name\n"
                ":type arg2: str\n"
                ":returns: EXP Object\n"
                ":rtype: :class:`geosoft.gxapi.GXEXP`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create_file");


}
