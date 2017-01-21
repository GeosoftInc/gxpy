#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline bool GXUNC_wrap_is_valid_utf16_char(int32_t arg1)
{
    bool ret = GXUNC::is_valid_utf16_char(arg1);
    return ret;
}
inline bool GXUNC_wrap_valid_symbol(const gx_string_type& arg1, bool arg2, int32_t arg3)
{
    bool ret = GXUNC::valid_symbol(arg1, arg2, arg3);
    return ret;
}
inline void GXUNC_wrap_utf16_val_to_str(int32_t arg1, str_ref& arg2)
{
    GXUNC::utf16_val_to_str(arg1, arg2);
}
inline void GXUNC_wrap_validate_symbols(GXVVPtr arg1, const gx_string_type& arg2, bool arg3)
{
    GXUNC::validate_symbols(arg1, arg2, arg3);
}

void gxPythonImportGXUNC()
{

    class_<GXUNC, boost::noncopyable> pyClass("GXUNC",
            "\n.. parsed-literal::\n\n"
            "   This library is not a class. Use the UNC library functions\n"
            "   to work with Unicode characters and strings. Since version 6.2\n"
            "   all strings are represented internally in the the GX engine\n"
            "   as UTF-8. The character set concept was discarded as a way to\n"
            "   work with characters that does not fall within the normal\n"
            "   ASCII range 0x01-0x7F. The utilities here aids with any new\n"
            "   functionality that is now possible (e.g. an expanded symbol range\n"
            "   with TrueType fonts).\n\n"
            , no_init);


    pyClass.def("is_valid_utf16_char", &GXUNC_wrap_is_valid_utf16_char,
                "is_valid_utf16_char((int)arg1) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   Check if the UTF-16 value is a valid Unicode character code point.\n\n"

                ":param arg1: UTF-16 value (32-bit int, lower 16 bits used, upper bits reserved for future use)\n"
                ":type arg1: int\n"
                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("is_valid_utf16_char");
    pyClass.def("valid_symbol", &GXUNC_wrap_valid_symbol,
                "valid_symbol((str)arg1, (bool)arg2, (int)arg3) -> bool:\n"

                "\n.. parsed-literal::\n\n"
                "   See if a Symbol number is valid in a particular font.\n\n"

                ":param arg1: Face name (undecorated)\n"
                ":type arg1: str\n"
                ":param arg2: Geosoft font? bool\n"
                ":type arg2: bool\n"
                ":param arg3: symbol number\n"
                ":type arg3: int\n"
                ":returns: bool\n"
                ":rtype: bool\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("valid_symbol");
    pyClass.def("utf16_val_to_str", &GXUNC_wrap_utf16_val_to_str,
                "utf16_val_to_str((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a UTF-16 value to a UTF-8 encoded string.\n\n"

                ":param arg1: UTF-16 value (32-bit int, lower 16 bits used, upper bits reserved for future use)\n"
                ":type arg1: int\n"
                ":param arg2: Converted string\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   An empty string will be returned for invalid symbols\n\n"
               ).staticmethod("utf16_val_to_str");
    pyClass.def("validate_symbols", &GXUNC_wrap_validate_symbols,
                "validate_symbols((GXVV)arg1, (str)arg2, (bool)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   High performance method to see if a set of symbols\n"
                "   are valid in a particular font.\n\n"

                ":param arg1: VV of symbols\n"
                ":type arg1: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg2: Face name (undecorated)\n"
                ":type arg2: str\n"
                ":param arg3: Geosoft font? bool\n"
                ":type arg3: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Invalid symbols in the VV will be set to -1 by this call. VV has to be of type GS_LONG.\n\n"
               ).staticmethod("validate_symbols");

    scope().attr("UTF8_MAX_CHAR") = (int32_t)5;

}
