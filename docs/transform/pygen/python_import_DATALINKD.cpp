#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXDATALINKDPtr GXDATALINKD_wrap_create_arc_lyr(const gx_string_type& arg1)
{
    GXDATALINKDPtr ret = GXDATALINKD::create_arc_lyr(arg1);
    return ret;
}
inline GXDATALINKDPtr GXDATALINKD_wrap_create_arc_lyr_ex(const gx_string_type& arg1, int32_t arg2)
{
    GXDATALINKDPtr ret = GXDATALINKD::create_arc_lyr_ex(arg1, arg2);
    return ret;
}
inline GXDATALINKDPtr GXDATALINKD_wrap_create_arc_lyr_from_tmp(const gx_string_type& arg1)
{
    GXDATALINKDPtr ret = GXDATALINKD::create_arc_lyr_from_tmp(arg1);
    return ret;
}
inline GXDATALINKDPtr GXDATALINKD_wrap_create_arc_lyr_from_tmp_ex(const gx_string_type& arg1, int32_t arg2)
{
    GXDATALINKDPtr ret = GXDATALINKD::create_arc_lyr_from_tmp_ex(arg1, arg2);
    return ret;
}
inline GXDATALINKDPtr GXDATALINKD_wrap_create_bing(int32_t arg1)
{
    GXDATALINKDPtr ret = GXDATALINKD::create_bing(arg1);
    return ret;
}
inline void GXDATALINKD_wrap_get_extents(GXDATALINKDPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4)
{
    self->get_extents(arg1, arg2, arg3, arg4);
}
inline void GXDATALINKD_wrap_get_ipj(GXDATALINKDPtr self, GXIPJPtr arg1)
{
    self->get_ipj(arg1);
}

void gxPythonImportGXDATALINKD()
{

    class_<GXDATALINKD, GXDATALINKDPtr> pyClass("GXDATALINKD",
            "\n.. parsed-literal::\n\n"
            "   DATALINK Display object.\n\n"
            , no_init);

    pyClass.def("null", &GXDATALINKD::null, "null() -> GXDATALINKD\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXDATALINKD`\n\n:returns: A null :class:`geosoft.gxapi.GXDATALINKD`\n:rtype: :class:`geosoft.gxapi.GXDATALINKD`\n").staticmethod("null");
    pyClass.def("is_null", &GXDATALINKD::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXDATALINKD is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXDATALINKD`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXDATALINKD::_internal_handle);
    pyClass.def("create_arc_lyr", &GXDATALINKD_wrap_create_arc_lyr,
                "create_arc_lyr((str)arg1) -> GXDATALINKD:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an DATALINKD object from a ArcGIS LYR file\n\n"

                ":param arg1: Arc LYR file name\n"
                ":type arg1: str\n"
                ":returns: DATALINKD handle, terminates if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXDATALINKD`\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Needs ArcEngine licence.\n\n"
               ).staticmethod("create_arc_lyr");
    pyClass.def("create_arc_lyr_ex", &GXDATALINKD_wrap_create_arc_lyr_ex,
                "create_arc_lyr_ex((str)arg1, (int)arg2) -> GXDATALINKD:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an DATALINKD object from a ArcGIS LYR file\n\n"

                ":param arg1: Arc LYR file name\n"
                ":type arg1: str\n"
                ":param arg2: Display as 3D Group? (as opposed to bitmap on plane)\n"
                ":type arg2: int\n"
                ":returns: DATALINKD handle, terminates if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXDATALINKD`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Needs ArcEngine licence.\n\n"
               ).staticmethod("create_arc_lyr_ex");
    pyClass.def("create_arc_lyr_from_tmp", &GXDATALINKD_wrap_create_arc_lyr_from_tmp,
                "create_arc_lyr_from_tmp((str)arg1) -> GXDATALINKD:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an DATALINKD object from a temporary ArcGIS LYR file\n\n"

                ":param arg1: Arc LYR file name\n"
                ":type arg1: str\n"
                ":returns: DATALINKD handle, terminates if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXDATALINKD`\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Needs ArcEngine licence.\n\n"
               ).staticmethod("create_arc_lyr_from_tmp");
    pyClass.def("create_arc_lyr_from_tmp_ex", &GXDATALINKD_wrap_create_arc_lyr_from_tmp_ex,
                "create_arc_lyr_from_tmp_ex((str)arg1, (int)arg2) -> GXDATALINKD:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an DATALINKD object from a temporary ArcGIS LYR file\n\n"

                ":param arg1: Arc LYR file name\n"
                ":type arg1: str\n"
                ":param arg2: Display as 3D Group? (as opposed to bitmap on plane)\n"
                ":type arg2: int\n"
                ":returns: DATALINKD handle, terminates if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXDATALINKD`\n"
                "\n"

                "\n.. versionadded:: 9.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Needs ArcEngine licence.\n\n"
               ).staticmethod("create_arc_lyr_from_tmp_ex");
    pyClass.def("create_bing", &GXDATALINKD_wrap_create_bing,
                "create_bing((int)arg1) -> GXDATALINKD:\n"

                "\n.. parsed-literal::\n\n"
                "   Create an DATALINKD object for a BING dataset\n\n"

                ":param arg1: 0 = Aerial, 1 = Road\n"
                ":type arg1: int\n"
                ":returns: DATALINKD handle, terminates if creation fails\n"
                ":rtype: :class:`geosoft.gxapi.GXDATALINKD`\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("create_bing");
    pyClass.def("get_extents", &GXDATALINKD_wrap_get_extents,
                "get_extents((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the data extents of the DATALINK Display object.\n\n"

                ":param arg1: Min X\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Max X\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Min Y\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Max Y\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               );
    pyClass.def("get_ipj", &GXDATALINKD_wrap_get_ipj,
                "get_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the projection of the DATALINK Display object.\n\n"

                ":param arg1: IPJ object to set the projection to\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               );


}
