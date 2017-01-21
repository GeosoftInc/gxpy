#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXDXFIPtr GXDXFI_wrap_create(const gx_string_type& arg1)
{
    GXDXFIPtr ret = GXDXFI::create(arg1);
    return ret;
}
inline void GXDXFI_wrap_dxf2_ply(GXPLYPtr arg1, GXDXFIPtr arg2)
{
    GXDXFI::dxf2_ply(arg1, arg2);
}
inline void GXDXFI_wrap_dxf2_view_ex(GXDXFIPtr self, GXMVIEWPtr arg1, int32_t arg2, int32_t arg3, const gx_string_type& arg4, int32_t arg5, int32_t arg6)
{
    self->dxf2_view_ex(arg1, arg2, arg3, arg4, arg5, (MVIEW_COLOR)arg6);
}
inline void GXDXFI_wrap_get_range(GXDXFIPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    self->get_range(arg1, arg2, arg3, arg4, arg5, arg6);
}

void gxPythonImportGXDXFI()
{

    class_<GXDXFI, GXDXFIPtr> pyClass("GXDXFI",
                                      "\n.. parsed-literal::\n\n"
                                      "   The DXFI class is used for importing AutoCAD® dxf files into Geosoft maps.\n\n"
                                      , no_init);

    pyClass.def("null", &GXDXFI::null, "null() -> GXDXFI\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXDXFI`\n\n:returns: A null :class:`geosoft.gxapi.GXDXFI`\n:rtype: :class:`geosoft.gxapi.GXDXFI`\n").staticmethod("null");
    pyClass.def("is_null", &GXDXFI::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXDXFI is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXDXFI`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXDXFI::_internal_handle);
    pyClass.def("create", &GXDXFI_wrap_create,
                "create((str)arg1) -> GXDXFI:\n"

                "\n.. parsed-literal::\n\n"
                "   Create DXFI.\n\n"

                ":param arg1: DXF file name\n"
                ":type arg1: str\n"
                ":returns: DXFI Object\n"
                ":rtype: :class:`geosoft.gxapi.GXDXFI`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("dxf2_ply", &GXDXFI_wrap_dxf2_ply,
                "dxf2_ply((GXPLY)arg1, (GXDXFI)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert a DXF file to a PLY object\n\n"

                ":param arg1: PLY handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg2: DXFI handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXDXFI`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               ).staticmethod("dxf2_ply");
    pyClass.def("dxf2_view_ex", &GXDXFI_wrap_dxf2_view_ex,
                "dxf2_view_ex((GXMVIEW)arg1, (int)arg2, (int)arg3, (str)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Draw entities in a DXF file to a view in a map\n\n"

                ":param arg1: MVIEW\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: User defined number of pens to use (can be iDUMMY)\n"
                ":type arg2: int\n"
                ":param arg3: TRUE to place entire DXF in one group\n"
                ":type arg3: int\n"
                ":param arg4: group name for one group (can be \"\" if above is FALSE)\n"
                ":type arg4: str\n"
                ":param arg5: TRUE to force one colour\n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`MVIEW_COLOR`\\  (ignored if above is FALSE)\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );
    pyClass.def("get_range", &GXDXFI_wrap_get_range,
                "get_range((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get DXF data range\n\n"

                ":param arg1: X min\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: X max\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Y min\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Y max\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Z min\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Z max\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               );


}
