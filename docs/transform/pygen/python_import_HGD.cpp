#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXHGDPtr GXHGD_wrap_create(const gx_string_type& arg1)
{
    GXHGDPtr ret = GXHGD::create(arg1);
    return ret;
}
inline void GXHGD_wrap_export_img(GXHGDPtr self, const gx_string_type& arg1)
{
    self->export_img(arg1);
}
inline void GXHGD_wrap_get_meta(GXHGDPtr self, GXMETAPtr arg1)
{
    self->get_meta(arg1);
}
inline GXHGDPtr GXHGD_wrap_h_create_img(GXIMGPtr arg1, const gx_string_type& arg2)
{
    GXHGDPtr ret = GXHGD::h_create_img(arg1, arg2);
    return ret;
}
inline void GXHGD_wrap_set_meta(GXHGDPtr self, GXMETAPtr arg1)
{
    self->set_meta(arg1);
}

void gxPythonImportGXHGD()
{

    class_<GXHGD, GXHGDPtr> pyClass("GXHGD",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		High Performance Grid. Designed to place grid data\n"
                                    "   		on a DAP server. It produces a multi-resolution\n"
                                    "   		compressed object that supports multi-threading and\n"
                                    "   		allows for high-speed extraction of data at any\n"
                                    "   		resolution.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXHGD::null, "null() -> GXHGD\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXHGD`\n\n:returns: A null :class:`geosoft.gxapi.GXHGD`\n:rtype: :class:`geosoft.gxapi.GXHGD`\n").staticmethod("null");
    pyClass.def("is_null", &GXHGD::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXHGD is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXHGD`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXHGD::_internal_handle);
    pyClass.def("create", &GXHGD_wrap_create,
                "create((str)arg1) -> GXHGD:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a handle to an HGD object\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":returns: HGD handle, terminates if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXHGD`\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               ).staticmethod("create");
    pyClass.def("export_img", &GXHGD_wrap_export_img,
                "export_img((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export all layers of this HGD into grid files.\n\n"

                ":param arg1: Name of grids (each layers adds _Number to the name)\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.1.0\n\n"
               );
    pyClass.def("get_meta", &GXHGD_wrap_get_meta,
                "get_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the metadata of a grid.\n\n"

                ":param arg1: META object to save HGD's meta to\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );
    pyClass.def("h_create_img", &GXHGD_wrap_h_create_img,
                "h_create_img((GXIMG)arg1, (str)arg2) -> GXHGD:\n"

                "\n.. parsed-literal::\n\n"
                "   Make an HGD from an IMG\n\n"

                ":param arg1: Image Handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXIMG`\n"
                ":param arg2: Name of HGD object\n"
                ":type arg2: str\n"
                ":returns: HGD Object\n"
                ":rtype: :class:`geosoft.gxapi.GXHGD`\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               ).staticmethod("h_create_img");
    pyClass.def("set_meta", &GXHGD_wrap_set_meta,
                "set_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the metadata of a grid.\n\n"

                ":param arg1: META object to add to HGD's meta\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.0\n\n"
               );


}
