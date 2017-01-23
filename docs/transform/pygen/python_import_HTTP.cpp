#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXHTTPPtr GXHTTP_wrap_create(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    GXHTTPPtr ret = GXHTTP::create(arg1, arg2, arg3, arg4);
    return ret;
}
inline void GXHTTP_wrap_download(GXHTTPPtr self, const gx_string_type& arg1, GXBFPtr arg2, int32_t arg3)
{
    self->download(arg1, arg2, arg3);
}
inline void GXHTTP_wrap_silent_download(GXHTTPPtr self, const gx_string_type& arg1, GXBFPtr arg2, int32_t arg3)
{
    self->silent_download(arg1, arg2, arg3);
}
inline void GXHTTP_wrap_get(GXHTTPPtr self, const gx_string_type& arg1, const gx_string_type& arg2, GXBFPtr arg3, GXBFPtr arg4)
{
    self->get(arg1, arg2, arg3, arg4);
}
inline void GXHTTP_wrap_post(GXHTTPPtr self, const gx_string_type& arg1, const gx_string_type& arg2, GXBFPtr arg3)
{
    self->post(arg1, arg2, arg3);
}
inline void GXHTTP_wrap_set_proxy_credentials(GXHTTPPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->set_proxy_credentials(arg1, arg2);
}

void gxPythonImportGXHTTP()
{

    class_<GXHTTP, GXHTTPPtr> pyClass("GXHTTP",
                                      "\n.. parsed-literal::\n\n"
                                      "   Connect to an Internet Server using HTTP.\n\n"

                                      "\n\n**Note:**\n\n"

                                      "\n.. parsed-literal::\n\n"
                                      "   \n"
                                      "   		References:\n"
                                      "   \n"
                                      "   		1. http://www.w3.org/Protocols/HTTP/HTTP2.html\n"
                                      "   \n"
                                      "   		2. http://www.w3.org/Addressing/URL/5_BNF.html\n"
                                      "   \n"
                                      "   		Note that path and search must conform be xalpha string (ref 2.).\n"
                                      "   		Special characters can be specified with a %xx, where xx is the\n"
                                      "   		hex ASCII number.  For example, a search string \"This one\" should\n"
                                      "   		be  specified as \"This%20one\"\n"
                                      "   	\n\n"
                                      , no_init);

    pyClass.def("null", &GXHTTP::null, "null() -> GXHTTP\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXHTTP`\n\n:returns: A null :class:`geosoft.gxapi.GXHTTP`\n:rtype: :class:`geosoft.gxapi.GXHTTP`\n").staticmethod("null");
    pyClass.def("is_null", &GXHTTP::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXHTTP is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXHTTP`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXHTTP::_internal_handle);
    pyClass.def("create", &GXHTTP_wrap_create,
                "create((str)arg1, (str)arg2, (str)arg3, (str)arg4) -> GXHTTP:\n"

                "\n.. parsed-literal::\n\n"
                "   This method creates a connection to an HTTP server\n\n"

                ":param arg1: URL of the server\n"
                ":type arg1: str\n"
                ":param arg2: user name, \"\" for none\n"
                ":type arg2: str\n"
                ":param arg3: password,  \"\" for none\n"
                ":type arg3: str\n"
                ":param arg4: Purpose of communication (for user verification)\n"
                ":type arg4: str\n"
                ":returns: HTTP Object\n"
                ":rtype: :class:`geosoft.gxapi.GXHTTP`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					An OM user has the ability to control access and verification of access\n"
                "   					to servers over the Internet.  A GX Developer has no way to change the\n"
                "   					users choice of access.  This is to prevent the creation of GX's that\n"
                "   					may be dangerous or may be used to collect information without the\n"
                "   					knowledgede of the user.\n"
                "   \n"
                "   					If the specified URL is restricted from access by the user, the create\n"
                "   					function will fail.\n"
                "   \n"
                "   					If the specified URL has not been accessed by this user before, or if\n"
                "   					the user has this site on \"Verify\", the user will be presented with a\n"
                "   					dialog requiring verification before communication can begin.  The user\n"
                "   					may choose to change the server site to a full \"Trust\" relationship, in\n"
                "   					which case the verification message will not reappear unless the site\n"
                "   					is explicitly changed back to verify or is restricted.\n"
                "   \n"
                "   					If you intend your GX to communicate with a server without\n"
                "   					verification, you must instruct your user to change their trust\n"
                "   					relationship with your server to \"Trusted\".  Your user will have the\n"
                "   					opportunity to do so the first time a script is run.\n"
                "   				\n\n"
               ).staticmethod("create");
    pyClass.def("download", &GXHTTP_wrap_download,
                "download((str)arg1, (GXBF)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Download file from the internet to a BF.\n\n"

                ":param arg1: File Name on the HTTP site\n"
                ":type arg1: str\n"
                ":param arg2: BF in which to place the file\n"
                ":type arg2: :class:`geosoft.gxapi.GXBF`\n"
                ":param arg3: Dynamic content (0 - no, 1 - yes)\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The file will be written starting at the current location\n"
                "   					in the BF\n"
                "   				\n\n"
               );
    pyClass.def("silent_download", &GXHTTP_wrap_silent_download,
                "silent_download((str)arg1, (GXBF)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Download file from the internet to a BF with no prompt for proxy authentication.\n\n"

                ":param arg1: File Name on the HTTP site\n"
                ":type arg1: str\n"
                ":param arg2: BF in which to place the file\n"
                ":type arg2: :class:`geosoft.gxapi.GXBF`\n"
                ":param arg3: Dynamic content (0 - no, 1 - yes)\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The file will be written starting at the current location\n"
                "   					in the BF. No prompt for proxy authentication\n"
                "   				\n\n"
               );
    pyClass.def("get", &GXHTTP_wrap_get,
                "get((str)arg1, (str)arg2, (GXBF)arg3, (GXBF)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get data from a server.\n\n"

                ":param arg1: http path (file or an ISAPI DLL), no spaces\n"
                ":type arg1: str\n"
                ":param arg2: http search string, no spaces\n"
                ":type arg2: str\n"
                ":param arg3: data to send\n"
                ":type arg3: :class:`geosoft.gxapi.GXBF`\n"
                ":param arg4: data returned\n"
                ":type arg4: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Full contents of the BF are sent in an HTTP GET message.\n"
                "   					BF pointer is returned to location before the call.\n"
                "   \n"
                "   					request URL will be:\n"
                "   					http://server/path?search\n"
                "   				\n\n"
               );
    pyClass.def("post", &GXHTTP_wrap_post,
                "post((str)arg1, (str)arg2, (GXBF)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Post data to the server.\n\n"

                ":param arg1: http path (file or an ISAPI DLL)\n"
                ":type arg1: str\n"
                ":param arg2: http search string, no spaces\n"
                ":type arg2: str\n"
                ":param arg3: data to post\n"
                ":type arg3: :class:`geosoft.gxapi.GXBF`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Full contents of the BF are sent as an HTTP POST message.\n"
                "   \n"
                "   					request URL will be:\n"
                "   					http://server/path?search\n"
                "   				\n\n"
               );
    pyClass.def("set_proxy_credentials", &GXHTTP_wrap_set_proxy_credentials,
                "set_proxy_credentials((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Assigns the proxy username and password so that\n"
                "   					user is not prompted when the first download fails\n"
                "   				\n\n"

                ":param arg1: username\n"
                ":type arg1: str\n"
                ":param arg2: password\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.2.0\n\n"
               );


}
