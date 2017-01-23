#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline int32_t GXINTERNET_wrap_download_http(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    int32_t ret = GXINTERNET::download_http(arg1, arg2, arg3);
    return ret;
}
inline void GXINTERNET_wrap_send_mail(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8)
{
    GXINTERNET::send_mail(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8);
}

void gxPythonImportGXINTERNET()
{

    class_<GXINTERNET, boost::noncopyable> pyClass("GXINTERNET",
            "\n.. parsed-literal::\n\n"
            "   This library provides functions for accessing the internet\n"
            "   and MAPI-compliant e-mail services.\n"
            "   Supported by Oasis montaj ONLY.\n\n"
            , no_init);


    pyClass.def("download_http", &GXINTERNET_wrap_download_http,
                "download_http((str)arg1, (str)arg2, (int)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Download HTTP file from the internet to file.\n\n"

                ":param arg1: HTTP URL\n"
                ":type arg1: str\n"
                ":param arg2: File Name to save to\n"
                ":type arg2: str\n"
                ":param arg3: No longer used, just pass 0\n"
                ":type arg3: int\n"
                ":returns: 0 - Ok\n"
                "          1 - Error\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The file must be stored on a server that supports\n"
                "   the HTTP protocol and not require a password.\n\n"

                "\n.. seealso::\n\n"
                "   iserver.gxh internet class.\n\n"
               ).staticmethod("download_http");
    pyClass.def("send_mail", &GXINTERNET_wrap_send_mail,
                "send_mail((str)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (str)arg6, (str)arg7, (str)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Prepaire an email for the user.\n\n"

                ":param arg1: Recipient Name        (\"\" for none)\n"
                ":type arg1: str\n"
                ":param arg2: Recipient Address     (\"\" for none)\n"
                ":type arg2: str\n"
                ":param arg3: szSubject             (\"\" for none)\n"
                ":type arg3: str\n"
                ":param arg4: Message Text          (\"\" for none)\n"
                ":type arg4: str\n"
                ":param arg5: Attachment1 File Name (\"\" for none)\n"
                ":type arg5: str\n"
                ":param arg6: Attachment1 User Name (\"\" for none)\n"
                ":type arg6: str\n"
                ":param arg7: Attachment2 File Name (\"\" for none)\n"
                ":type arg7: str\n"
                ":param arg8: Attachment2 User Name (\"\" for none)\n"
                ":type arg8: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Requires a MAPI complient mail system to be installed\n"
                "   on the client machine.\n\n"
               ).staticmethod("send_mail");


}
