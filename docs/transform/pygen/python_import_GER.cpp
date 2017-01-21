#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXGERPtr GXGER_wrap_create(const gx_string_type& arg1)
{
    GXGERPtr ret = GXGER::create(arg1);
    return ret;
}
inline int32_t GXGER_wrap_get(GXGERPtr self, int32_t arg1, str_ref& arg2)
{
    int32_t ret = self->get(arg1, arg2);
    return ret;
}
inline void GXGER_wrap_set_int(GXGERPtr self, const gx_string_type& arg1, int32_t arg2)
{
    self->set_int(arg1, arg2);
}
inline void GXGER_wrap_set_double(GXGERPtr self, const gx_string_type& arg1, double arg2)
{
    self->set_double(arg1, arg2);
}
inline void GXGER_wrap_set_string(GXGERPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->set_string(arg1, arg2);
}

void gxPythonImportGXGER()
{

    class_<GXGER, GXGERPtr> pyClass("GXGER",
                                    "\n.. parsed-literal::\n\n"
                                    "   Allows access to a Geosoft format error message file. This class\n"
                                    "   does not in itself produce an error message, but retrieves a\n"
                                    "   selected message from the file, and allows the\n"
                                    "   setting of replacement parameters within the message. It\n"
                                    "   is up to the user to display or use the message.\n\n"

                                    "\n\n**Note:**\n\n"

                                    "\n.. parsed-literal::\n\n"
                                    "   GER message files contain numbered messages that can be used within GXs.\n"
                                    "   Following is an example from the file GEOSOFT.GER:\n"
                                    "   \n"
                                    "   \n"
                                    "         #20008\n"
                                    "         ! Invalid password. The product installation has failed.\n"
                                    "   \n"
                                    "         #20009\n"
                                    "         ! Unable to find INI file: %1\n"
                                    "         ! See the documentation for details\n"
                                    "   \n"
                                    "   \n"
                                    "   A '#' character in column 1 indicates a message number.  The message\n"
                                    "   follows on lines that begin with a '!' character.  Strings in the message\n"
                                    "   may be replaced at run time with values using the \\ :func:`geosoft.gxapi.GXGER.set_string`\\ ,\n"
                                    "   \\ :func:`geosoft.gxapi.GXGER.set_int`\\  and \\ :func:`geosoft.gxapi.GXGER.set_double`\\  methods. The iGet_GER will return the message\n"
                                    "   with strings replaced by their settings.  By convention, we recommend\n"
                                    "   that you use \"%1\", \"%2\", etc. as replacement strings.\n\n"
                                    , no_init);

    pyClass.def("null", &GXGER::null, "null() -> GXGER\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXGER`\n\n:returns: A null :class:`geosoft.gxapi.GXGER`\n:rtype: :class:`geosoft.gxapi.GXGER`\n").staticmethod("null");
    pyClass.def("is_null", &GXGER::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXGER is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXGER`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXGER::_internal_handle);
    pyClass.def("create", &GXGER_wrap_create,
                "create((str)arg1) -> GXGER:\n"

                "\n.. parsed-literal::\n\n"
                "   Opens an ASCII error file to read from.\n\n"

                ":param arg1: GER file name.\n"
                ":type arg1: str\n"
                ":returns: GER Object\n"
                ":rtype: :class:`geosoft.gxapi.GXGER`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The GER file may be in the local directory or the GEOSOFT\n"
                "   directory.\n\n"
               ).staticmethod("create");
    pyClass.def("get", &GXGER_wrap_get,
                "get((int)arg1, (str_ref)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a message string.\n\n"

                ":param arg1: message number\n"
                ":type arg1: int\n"
                ":param arg2: message string returned, replacements filtered\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: 0 if message found\n"
                "          1 if no message, passed message remains unchanged\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_int", &GXGER_wrap_set_int,
                "set_int((str)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a replacement string value to an int.\n\n"

                ":param arg1: replacement string (ie. \"%1\")\n"
                ":type arg1: str\n"
                ":param arg2: setting\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_double", &GXGER_wrap_set_double,
                "set_double((str)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a replacement string value to a real.\n\n"

                ":param arg1: replacement string (ie. \"%1\")\n"
                ":type arg1: str\n"
                ":param arg2: setting\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_string", &GXGER_wrap_set_string,
                "set_string((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a replacement string value.\n\n"

                ":param arg1: replacement string (ie. \"%1\")\n"
                ":type arg1: str\n"
                ":param arg2: setting\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );


}
