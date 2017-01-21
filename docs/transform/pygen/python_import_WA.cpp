#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXWA_wrap_puts(GXWAPtr self, const gx_string_type& arg1)
{
    self->puts(arg1);
}
inline GXWAPtr GXWA_wrap_create(const gx_string_type& arg1, int32_t arg2)
{
    GXWAPtr ret = GXWA::create(arg1, (WA_OPEN)arg2);
    return ret;
}
inline GXWAPtr GXWA_wrap_create_ex(const gx_string_type& arg1, int32_t arg2, int32_t arg3)
{
    GXWAPtr ret = GXWA::create_ex(arg1, (WA_OPEN)arg2, (WA_ENCODE)arg3);
    return ret;
}
inline GXWAPtr GXWA_wrap_create_sbf(GXSBFPtr arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXWAPtr ret = GXWA::create_sbf(arg1, arg2, (WA_OPEN)arg3);
    return ret;
}
inline GXWAPtr GXWA_wrap_create_sbf_ex(GXSBFPtr arg1, const gx_string_type& arg2, int32_t arg3, int32_t arg4)
{
    GXWAPtr ret = GXWA::create_sbf_ex(arg1, arg2, (WA_OPEN)arg3, (WA_ENCODE)arg4);
    return ret;
}
inline void GXWA_wrap_new_line(GXWAPtr self)
{
    self->new_line();
}

void gxPythonImportGXWA()
{

    class_<GXWA, GXWAPtr> pyClass("GXWA",
                                  "\n.. parsed-literal::\n\n"
                                  "   The WA class enables you to access and write data to ASCII files.\n\n"
                                  , no_init);

    pyClass.def("null", &GXWA::null, "null() -> GXWA\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXWA`\n\n:returns: A null :class:`geosoft.gxapi.GXWA`\n:rtype: :class:`geosoft.gxapi.GXWA`\n").staticmethod("null");
    pyClass.def("is_null", &GXWA::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXWA is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXWA`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXWA::_internal_handle);
    pyClass.def("puts", &GXWA_wrap_puts,
                "puts((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Writes a string to the file.\n\n"

                ":param arg1: String to write\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("create", &GXWA_wrap_create,
                "create((str)arg1, (int)arg2) -> GXWA:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates an ASCII file to write to.\n\n"

                ":param arg1: Name of the File\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`WA_OPEN`\\ \n"
                ":type arg2: int\n"
                ":returns: WA Handle\n"
                ":rtype: :class:`geosoft.gxapi.GXWA`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   ANSI Encoding is assumed, See \\ :func:`geosoft.gxapi.GXWA.create_ex`\\  to override this.\n\n"
               ).staticmethod("create");
    pyClass.def("create_ex", &GXWA_wrap_create_ex,
                "create_ex((str)arg1, (int)arg2, (int)arg3) -> GXWA:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates an ASCII file to write to.\n\n"

                ":param arg1: Name of the File\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`WA_OPEN`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`WA_ENCODE`\\ \n"
                ":type arg3: int\n"
                ":returns: WA Handle\n"
                ":rtype: :class:`geosoft.gxapi.GXWA`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Before version 6.2. text in on the GX API level were handled as characters in the current ANSI code page\n"
                "   					defining how characters above ASCII 127 would be displayed. 6.2. introduced Unicode in the core\n"
                "   					montaj engine that greatly increased the number of symbols that can be used. The WA_ENCODE constants\n"
                "   					were introduce that controls how text are written to files on disk with the WA class.\n"
                "   				\n\n"
               ).staticmethod("create_ex");
    pyClass.def("create_sbf", &GXWA_wrap_create_sbf,
                "create_sbf((GXSBF)arg1, (str)arg2, (int)arg3) -> GXWA:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates an ASCII file to write to in an SBF.\n\n"

                ":param arg1: Storage\n"
                ":type arg1: :class:`geosoft.gxapi.GXSBF`\n"
                ":param arg2: Name of the File\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`WA_OPEN`\\ \n"
                ":type arg3: int\n"
                ":returns: WA Handle\n"
                ":rtype: :class:`geosoft.gxapi.GXWA`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   See sbf.gxh. ANSI Encoding is assumed, See \\ :func:`geosoft.gxapi.GXWA.create_sbf_ex`\\  to override this.\n\n"
               ).staticmethod("create_sbf");
    pyClass.def("create_sbf_ex", &GXWA_wrap_create_sbf_ex,
                "create_sbf_ex((GXSBF)arg1, (str)arg2, (int)arg3, (int)arg4) -> GXWA:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates an ASCII file to write to in an SBF.\n\n"

                ":param arg1: Storage\n"
                ":type arg1: :class:`geosoft.gxapi.GXSBF`\n"
                ":param arg2: Name of the File\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`WA_OPEN`\\ \n"
                ":type arg3: int\n"
                ":param arg4: \\ :ref:`WA_ENCODE`\\ \n"
                ":type arg4: int\n"
                ":returns: WA Handle\n"
                ":rtype: :class:`geosoft.gxapi.GXWA`\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Also see sbf.gxh\n"
                "   					Before version 6.2. text in on the GX API level were handled as characters in the current ANSI code page\n"
                "   					defining how characters above ASCII 127 would be displayed. 6.2. introduced Unicode in the core\n"
                "   					montaj engine that greatly increased the number of symbols that can be used. The WA_ENCODE constants\n"
                "   					were introduce that controls how text are written to files on disk with the WA class.\n"
                "   				\n\n"
               ).staticmethod("create_sbf_ex");
    pyClass.def("new_line", &GXWA_wrap_new_line,
                "new_line() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Forces a new line in the WA object.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );

    scope().attr("WA_ENCODE_ANSI") = (int32_t)0;
    scope().attr("WA_ENCODE_RAW") = (int32_t)1;
    scope().attr("WA_ENCODE_UTF8") = (int32_t)2;
    scope().attr("WA_ENCODE_UTF8_NOHEADER") = (int32_t)3;
    scope().attr("WA_ENCODE_UTF16_NOHEADER") = (int32_t)4;
    scope().attr("WA_NEW") = (int32_t)0;
    scope().attr("WA_APPEND") = (int32_t)1;

}
