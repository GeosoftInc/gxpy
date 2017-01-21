#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXHXYZPtr GXHXYZ_wrap_create(const gx_string_type& arg1)
{
    GXHXYZPtr ret = GXHXYZ::create(arg1);
    return ret;
}
inline void GXHXYZ_wrap_get_meta(GXHXYZPtr self, GXMETAPtr arg1)
{
    self->get_meta(arg1);
}
inline GXHXYZPtr GXHXYZ_wrap_h_create_db(GXDBPtr arg1, GXVVPtr arg2, const gx_string_type& arg3)
{
    GXHXYZPtr ret = GXHXYZ::h_create_db(arg1, arg2, arg3);
    return ret;
}
inline GXHXYZPtr GXHXYZ_wrap_h_create_sql(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, GXIPJPtr arg5, const gx_string_type& arg6)
{
    GXHXYZPtr ret = GXHXYZ::h_create_sql(arg1, arg2, arg3, arg4, arg5, arg6);
    return ret;
}
inline void GXHXYZ_wrap_set_meta(GXHXYZPtr self, GXMETAPtr arg1)
{
    self->set_meta(arg1);
}

void gxPythonImportGXHXYZ()
{

    class_<GXHXYZ, GXHXYZPtr> pyClass("GXHXYZ",
                                      "\n.. parsed-literal::\n\n"
                                      "   \n"
                                      "   		High Performance Data Point Storage. This is used\n"
                                      "   		to put Point data on a DAP server. It is compressed\n"
                                      "   		and uses a Quad-Tree design to allow very high speed\n"
                                      "   		data extraction. It is also multi-threaded.\n"
                                      "   	\n\n"
                                      , no_init);

    pyClass.def("null", &GXHXYZ::null, "null() -> GXHXYZ\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXHXYZ`\n\n:returns: A null :class:`geosoft.gxapi.GXHXYZ`\n:rtype: :class:`geosoft.gxapi.GXHXYZ`\n").staticmethod("null");
    pyClass.def("is_null", &GXHXYZ::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXHXYZ is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXHXYZ`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXHXYZ::_internal_handle);
    pyClass.def("create", &GXHXYZ_wrap_create,
                "create((str)arg1) -> GXHXYZ:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a handle to an HXYZ object\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":returns: HXYZ Object\n"
                ":rtype: :class:`geosoft.gxapi.GXHXYZ`\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               ).staticmethod("create");
    pyClass.def("get_meta", &GXHXYZ_wrap_get_meta,
                "get_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the metadata of a grid.\n\n"

                ":param arg1: META object to save HXYZ's meta to\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );
    pyClass.def("h_create_db", &GXHXYZ_wrap_h_create_db,
                "h_create_db((GXDB)arg1, (GXVV)arg2, (str)arg3) -> GXHXYZ:\n"

                "\n.. parsed-literal::\n\n"
                "   Make an HXYZ from GDB\n\n"

                ":param arg1: DB handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: VV of channels to export\n"
                ":type arg2: :class:`geosoft.gxapi.GXVV`\n"
                ":param arg3: Name of HXYZ object\n"
                ":type arg3: str\n"
                ":returns: HXYZ object\n"
                ":rtype: :class:`geosoft.gxapi.GXHXYZ`\n"
                "\n"

                "\n.. versionadded:: 5.1.5\n\n"
               ).staticmethod("h_create_db");
    pyClass.def("h_create_sql", &GXHXYZ_wrap_h_create_sql,
                "h_create_sql((str)arg1, (str)arg2, (str)arg3, (str)arg4, (GXIPJ)arg5, (str)arg6) -> GXHXYZ:\n"

                "\n.. parsed-literal::\n\n"
                "   Make an HXYZ from SQL Query\n\n"

                ":param arg1: Template File Name\n"
                ":type arg1: str\n"
                ":param arg2: X field name\n"
                ":type arg2: str\n"
                ":param arg3: Y field name\n"
                ":type arg3: str\n"
                ":param arg4: Z field name\n"
                ":type arg4: str\n"
                ":param arg5: Projection of data values\n"
                ":type arg5: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg6: Name of HXYZ object\n"
                ":type arg6: str\n"
                ":returns: HXYZ object\n"
                ":rtype: :class:`geosoft.gxapi.GXHXYZ`\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               ).staticmethod("h_create_sql");
    pyClass.def("set_meta", &GXHXYZ_wrap_set_meta,
                "set_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the metadata of a grid.\n\n"

                ":param arg1: META object to add to HXYZ's meta\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.3\n\n"
               );


}
