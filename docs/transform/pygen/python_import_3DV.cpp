#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXMVIEWPtr GX3DV_wrap_open_mview(GX3DVPtr self, int32_t arg1)
{
    GXMVIEWPtr ret = self->open_mview((GEO3DV_OPEN)arg1);
    return ret;
}
inline void GX3DV_wrap_copy_to_map(GX3DVPtr self, GXMAPPtr arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, double arg6, int32_t arg7, str_ref& arg8, str_ref& arg9)
{
    self->copy_to_map(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
inline GX3DVPtr GX3DV_wrap_create_new(const gx_string_type& arg1, GXMVIEWPtr arg2)
{
    GX3DVPtr ret = GX3DV::create_new(arg1, arg2);
    return ret;
}
inline GX3DVPtr GX3DV_wrap_open(const gx_string_type& arg1)
{
    GX3DVPtr ret = GX3DV::open(arg1);
    return ret;
}
inline GX3DVPtr GX3DV_wrap_from_map(GXMAPPtr arg1)
{
    GX3DVPtr ret = GX3DV::from_map(arg1);
    return ret;
}
inline void GX3DV_wrap_crc_3dv(GX3DVPtr self, int_ref& arg1, const gx_string_type& arg2)
{
    self->crc_3dv(arg1, arg2);
}

void gxPythonImportGX3DV()
{

    class_<GX3DV, GX3DVPtr> pyClass("GX3DV",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		TODO...\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GX3DV::null, "null() -> GX3DV\n\nA null (undefined) instance of :class:`geosoft.gxapi.GX3DV`\n\n:returns: A null :class:`geosoft.gxapi.GX3DV`\n:rtype: :class:`geosoft.gxapi.GX3DV`\n").staticmethod("null");
    pyClass.def("is_null", &GX3DV::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GX3DV is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GX3DV`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GX3DV::_internal_handle);
    pyClass.def("open_mview", &GX3DV_wrap_open_mview,
                "open_mview((int)arg1) -> GXMVIEW:\n"

                "\n.. parsed-literal::\n\n"
                "   Open 3DV's 3D MVIEW\n\n"

                ":param arg1: \\ :ref:`GEO3DV_OPEN`\\ \n"
                ":type arg1: int\n"
                ":returns: MVIEW, aborts on failure\n"
                ":rtype: :class:`geosoft.gxapi.GXMVIEW`\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               );
    pyClass.def("copy_to_map", &GX3DV_wrap_copy_to_map,
                "copy_to_map((GXMAP)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (int)arg7, (str_ref)arg8, (str_ref)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy the 3DV's 3D MVIEW into a map.\n\n"

                ":param arg1: MAP Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: Desired new view name\n"
                ":type arg2: str\n"
                ":param arg3: X minimum in mm\n"
                ":type arg3: float\n"
                ":param arg4: Y minimun in mm\n"
                ":type arg4: float\n"
                ":param arg5: X maximum in mm\n"
                ":type arg5: float\n"
                ":param arg6: Y maximum in mm\n"
                ":type arg6: float\n"
                ":param arg7: (0 - Produce errors for conflicting unpacked files, 1 - Force overwrites of conflicting unpacked files)\n"
                ":type arg7: int\n"
                ":param arg8: New view name created\n"
                ":type arg8: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg9: List of files that are problematic returned\n"
                ":type arg9: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					A 3DV packs all source files. This functions creates an unpacked map and\n"
                "   					unpacks the packed files in the same way that UnPackFilesEx in the MAP class does.\n"
                "   				\n\n"
               );
    pyClass.def("create_new", &GX3DV_wrap_create_new,
                "create_new((str)arg1, (GXMVIEW)arg2) -> GX3DV:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new 3DV.\n\n"

                ":param arg1: 3DV file name\n"
                ":type arg1: str\n"
                ":param arg2: 3D MVIEW to create new 3DV from\n"
                ":type arg2: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":returns: 3DV Object\n"
                ":rtype: :class:`geosoft.gxapi.GX3DV`\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("create_new");
    pyClass.def("open", &GX3DV_wrap_open,
                "open((str)arg1) -> GX3DV:\n"

                "\n.. parsed-literal::\n\n"
                "   Open an existing 3DV.\n\n"

                ":param arg1: 3DV file name\n"
                ":type arg1: str\n"
                ":returns: 3DV Object\n"
                ":rtype: :class:`geosoft.gxapi.GX3DV`\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("open");
    pyClass.def("from_map", &GX3DV_wrap_from_map,
                "from_map((GXMAP)arg1) -> GX3DV:\n"

                "\n.. parsed-literal::\n\n"
                "   Get an 3DV from MAP handle (e.g. from \\ :func:`geosoft.gxapi.GXEMAP.lock`\\  on open geosoft_3dv document in project)\n\n"

                ":param arg1: MAP Object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":returns: 3DV Object\n"
                ":rtype: :class:`geosoft.gxapi.GX3DV`\n"
                "\n"

                "\n.. versionadded:: 9.2.0\n\n"
               ).staticmethod("from_map");
    pyClass.def("crc_3dv", &GX3DV_wrap_crc_3dv,
                "crc_3dv((int_ref)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate an XML CRC of a 3DV\n\n"

                ":param arg1: CRC returned\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Name of xml to generate (.zip added)\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               );

    scope().attr("GEO3DV_MVIEW_READ") = (int32_t)0;
    scope().attr("GEO3DV_MVIEW_WRITEOLD") = (int32_t)2;

}
