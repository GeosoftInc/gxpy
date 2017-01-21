#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXFLTPtr GXFLT_wrap_create(const gx_string_type& arg1)
{
    GXFLTPtr ret = GXFLT::create(arg1);
    return ret;
}
inline GXFLTPtr GXFLT_wrap_load(const gx_string_type& arg1)
{
    GXFLTPtr ret = GXFLT::load(arg1);
    return ret;
}

void gxPythonImportGXFLT()
{

    class_<GXFLT, GXFLTPtr> pyClass("GXFLT",
                                    "\n.. parsed-literal::\n\n"
                                    "   The FLT class allows the application of user-defined convolution filters to data in an OASIS database\n\n"
                                    , no_init);

    pyClass.def("null", &GXFLT::null, "null() -> GXFLT\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXFLT`\n\n:returns: A null :class:`geosoft.gxapi.GXFLT`\n:rtype: :class:`geosoft.gxapi.GXFLT`\n").staticmethod("null");
    pyClass.def("is_null", &GXFLT::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXFLT is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXFLT`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXFLT::_internal_handle);
    pyClass.def("create", &GXFLT_wrap_create,
                "create((str)arg1) -> GXFLT:\n"

                "\n.. parsed-literal::\n\n"
                "   create a filter from a comma/space delimited string.\n\n"

                ":param arg1: Filter string\n"
                ":type arg1: str\n"
                ":returns: FLT Object\n"
                ":rtype: :class:`geosoft.gxapi.GXFLT`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Terminates process if filter not found.\n"
                "   Sample Fraser Filter string:\n"
                "   \n"
                "         \"-1,-1,1,1\"\n\n"
               ).staticmethod("create");
    pyClass.def("load", &GXFLT_wrap_load,
                "load((str)arg1) -> GXFLT:\n"

                "\n.. parsed-literal::\n\n"
                "   Load and return handle to a convolution filter.\n\n"

                ":param arg1: Name of the filter File\n"
                ":type arg1: str\n"
                ":returns: FLT Object\n"
                ":rtype: :class:`geosoft.gxapi.GXFLT`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Terminates process if filter not found.\n"
                "   A filter file is an ASCII file that contains filter\n"
                "   coefficients, which are simply mumbers.  There can be\n"
                "   one coefficient to a line.  Blank lines and comment lines\n"
                "   are skipped.  Comment lines beginn with a forward slash\n"
                "   character in column 1.  Following is an example Fraser\n"
                "   Filter file:\n"
                "   \n"
                "      /----------------------\n"
                "      / Fraser Filter\n"
                "      /----------------------\n"
                "      -1\n"
                "      -1\n"
                "      1\n"
                "      1\n\n"
               ).staticmethod("load");


}
