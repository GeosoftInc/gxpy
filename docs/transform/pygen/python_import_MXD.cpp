#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXMXD_wrap_create_metadata(const gx_string_type& arg1)
{
    GXMXD::create_metadata(arg1);
}
inline void GXMXD_wrap_convert_to_map(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXMXD::convert_to_map(arg1, arg2);
}
inline void GXMXD_wrap_sync(const gx_string_type& arg1)
{
    GXMXD::sync(arg1);
}

void gxPythonImportGXMXD()
{

    class_<GXMXD, GXMXDPtr> pyClass("GXMXD",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		A MXD wraps and provides manipulation and usage for\n"
                                    "   		the content of an ArcGIS MXD file.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXMXD::null, "null() -> GXMXD\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXMXD`\n\n:returns: A null :class:`geosoft.gxapi.GXMXD`\n:rtype: :class:`geosoft.gxapi.GXMXD`\n").staticmethod("null");
    pyClass.def("is_null", &GXMXD::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXMXD is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXMXD`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXMXD::_internal_handle);
    pyClass.def("create_metadata", &GXMXD_wrap_create_metadata,
                "create_metadata((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create metadata for this brand new MXD (we are the creator)\n\n"

                ":param arg1: MXD file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("create_metadata");
    pyClass.def("convert_to_map", &GXMXD_wrap_convert_to_map,
                "convert_to_map((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create Geosoft map from ArcGIS MXD\n\n"

                ":param arg1: ArcGIS MXD file name\n"
                ":type arg1: str\n"
                ":param arg2: Geosoft map file name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"
               ).staticmethod("convert_to_map");
    pyClass.def("sync", &GXMXD_wrap_sync,
                "sync((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Syncronize any Metadata for this MXD\n\n"

                ":param arg1: MXD file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("sync");


}
