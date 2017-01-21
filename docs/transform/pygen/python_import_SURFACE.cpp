#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXSURFACEPtr GXSURFACE_wrap_create(const gx_string_type& arg1, GXIPJPtr arg2)
{
    GXSURFACEPtr ret = GXSURFACE::create(arg1, arg2);
    return ret;
}
inline GXSURFACEPtr GXSURFACE_wrap_open(const gx_string_type& arg1, int32_t arg2)
{
    GXSURFACEPtr ret = GXSURFACE::open(arg1, (SURFACE_OPEN)arg2);
    return ret;
}
inline void GXSURFACE_wrap_get_ipj(GXSURFACEPtr self, GXIPJPtr arg1)
{
    self->get_ipj(arg1);
}
inline void GXSURFACE_wrap_set_ipj(GXSURFACEPtr self, GXIPJPtr arg1)
{
    self->set_ipj(arg1);
}
inline void GXSURFACE_wrap_get_surface_items(GXSURFACEPtr self, GXLSTPtr arg1)
{
    self->get_surface_items(arg1);
}
inline GXSURFACEITEMPtr GXSURFACE_wrap_get_surface_item(GXSURFACEPtr self, const gx_string_type& arg1)
{
    GXSURFACEITEMPtr ret = self->get_surface_item(arg1);
    return ret;
}
inline void GXSURFACE_wrap_add_surface_item(GXSURFACEPtr self, GXSURFACEITEMPtr arg1)
{
    self->add_surface_item(arg1);
}
inline void GXSURFACE_wrap_get_surface_names(const gx_string_type& arg1, GXLSTPtr arg2)
{
    GXSURFACE::get_surface_names(arg1, arg2);
}
inline void GXSURFACE_wrap_get_closed_surface_names(const gx_string_type& arg1, GXLSTPtr arg2)
{
    GXSURFACE::get_closed_surface_names(arg1, arg2);
}
inline void GXSURFACE_wrap_get_extents(GXSURFACEPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    self->get_extents(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline int32_t GXSURFACE_wrap_crc(const gx_string_type& arg1, const gx_string_type& arg2, int_ref& arg3)
{
    int32_t ret = GXSURFACE::crc(arg1, arg2, arg3);
    return ret;
}
inline void GXSURFACE_wrap_sync(const gx_string_type& arg1)
{
    GXSURFACE::sync(arg1);
}
inline void GXSURFACE_wrap_create_from_dxf(GXIPJPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXSURFACE::create_from_dxf(arg1, arg2, arg3);
}
inline void GXSURFACE_wrap_create_from_vulcan_triangulation(const gx_string_type& arg1, GXIPJPtr arg2, const gx_string_type& arg3)
{
    GXSURFACE::create_from_vulcan_triangulation(arg1, arg2, arg3);
}
inline void GXSURFACE_wrap_append_vulcan_triangulation(const gx_string_type& arg1, GXIPJPtr arg2, const gx_string_type& arg3)
{
    GXSURFACE::append_vulcan_triangulation(arg1, arg2, arg3);
}

void gxPythonImportGXSURFACE()
{

    class_<GXSURFACE, GXSURFACEPtr> pyClass("GXSURFACE",
                                            "\n.. parsed-literal::\n\n"
                                            "   \n"
                                            "   		The SURFACE class allows you to create, read and alter Geosurface files (\\ `*`\\ .geosoft_surface).\n"
                                            "   		A Geosurface file can contain one or more surface items (see SURFACEITEM class). In turn each item can\n"
                                            "   		contains one or more triangular polyhedral meshes.\n"
                                            "   	\n\n"
                                            , no_init);

    pyClass.def("null", &GXSURFACE::null, "null() -> GXSURFACE\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXSURFACE`\n\n:returns: A null :class:`geosoft.gxapi.GXSURFACE`\n:rtype: :class:`geosoft.gxapi.GXSURFACE`\n").staticmethod("null");
    pyClass.def("is_null", &GXSURFACE::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXSURFACE is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXSURFACE`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXSURFACE::_internal_handle);
    pyClass.def("create", &GXSURFACE_wrap_create,
                "create((str)arg1, (GXIPJ)arg2) -> GXSURFACE:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new Geosurface file\n\n"

                ":param arg1: Geosurface file name\n"
                ":type arg1: str\n"
                ":param arg2: IPJ containing coordinate system of the Geosurface\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: SURFACE Object\n"
                ":rtype: :class:`geosoft.gxapi.GXSURFACE`\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("create");
    pyClass.def("open", &GXSURFACE_wrap_open,
                "open((str)arg1, (int)arg2) -> GXSURFACE:\n"

                "\n.. parsed-literal::\n\n"
                "   Open a Geosurface file\n\n"

                ":param arg1: Geosurface file name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`SURFACE_OPEN`\\ \n"
                ":type arg2: int\n"
                ":returns: SURFACE Object\n"
                ":rtype: :class:`geosoft.gxapi.GXSURFACE`\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("open");
    pyClass.def("get_ipj", &GXSURFACE_wrap_get_ipj,
                "get_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the coordinate system of the SURFACE.\n\n"

                ":param arg1: IPJ in which to place the Geosurface coordinate system\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("set_ipj", &GXSURFACE_wrap_set_ipj,
                "set_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Change the coordinate system of the SURFACE.\n\n"

                ":param arg1: IPJ containing the new coordinate system of the Geosurface\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_surface_items", &GXSURFACE_wrap_get_surface_items,
                "get_surface_items((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the surfaces items in a Geosurface file\n\n"

                ":param arg1: LST to fill\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_surface_item", &GXSURFACE_wrap_get_surface_item,
                "get_surface_item((str)arg1) -> GXSURFACEITEM:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the an existing surface item from the SURFACE\n\n"

                ":param arg1: Item GUID\n"
                ":type arg1: str\n"
                ":returns: SURFACEITEM Object\n"
                ":rtype: :class:`geosoft.gxapi.GXSURFACEITEM`\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("add_surface_item", &GXSURFACE_wrap_add_surface_item,
                "add_surface_item((GXSURFACEITEM)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Add a new surface item to the SURFACE\n\n"

                ":param arg1: SURFACEITEM to add\n"
                ":type arg1: :class:`geosoft.gxapi.GXSURFACEITEM`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               );
    pyClass.def("get_surface_names", &GXSURFACE_wrap_get_surface_names,
                "get_surface_names((str)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the surface item names in a Geosurface file\n\n"

                ":param arg1: Geosurface file\n"
                ":type arg1: str\n"
                ":param arg2: LST to fill\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("get_surface_names");
    pyClass.def("get_closed_surface_names", &GXSURFACE_wrap_get_closed_surface_names,
                "get_closed_surface_names((str)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the names of closed surface items in a Geosurface file (may return an empty list)\n\n"

                ":param arg1: Geosurface file\n"
                ":type arg1: str\n"
                ":param arg2: LST to fill (may return an empty LST if none of the surfaces are closed)\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("get_closed_surface_names");
    pyClass.def("get_extents", &GXSURFACE_wrap_get_extents,
                "get_extents((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the spatial range of all surface items.\n\n"

                ":param arg1: Minimum valid data in X.\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Minimum valid data in Y.\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: Minimum valid data in Z.\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Maximum valid data in X.\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg5: Maximum valid data in Y.\n"
                ":type arg5: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg6: Maximum valid data in Z.\n"
                ":type arg6: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.5.0\n\n"
               );
    pyClass.def("crc", &GXSURFACE_wrap_crc,
                "crc((str)arg1, (str)arg2, (int_ref)arg3) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Compute an XML CRC of a Geosurface file.\n\n"

                ":param arg1: Geosurface file\n"
                ":type arg1: str\n"
                ":param arg2: output file\n"
                ":type arg2: str\n"
                ":param arg3: CRC (unused, always set to 0)\n"
                ":type arg3: :class:`geosoft.gxapi.int_ref`\n"
                ":returns: CRC Value (always 0)\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("crc");
    pyClass.def("sync", &GXSURFACE_wrap_sync,
                "sync((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Syncronize the Metadata for this Geosurface\n\n"

                ":param arg1: Geosurface file\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("sync");
    pyClass.def("create_from_dxf", &GXSURFACE_wrap_create_from_dxf,
                "create_from_dxf((GXIPJ)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create Geosurface file from DXF file.\n\n"

                ":param arg1: IPJ\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: Geosurface file\n"
                ":type arg2: str\n"
                ":param arg3: dxf file\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.2.0\n\n"
               ).staticmethod("create_from_dxf");
    pyClass.def("create_from_vulcan_triangulation", &GXSURFACE_wrap_create_from_vulcan_triangulation,
                "create_from_vulcan_triangulation((str)arg1, (GXIPJ)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create Geosurface file from a Maptek Vulcan triangulation file.\n\n"

                ":param arg1: 00t file\n"
                ":type arg1: str\n"
                ":param arg2: IPJ\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg3: Geosurface file\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("create_from_vulcan_triangulation");
    pyClass.def("append_vulcan_triangulation", &GXSURFACE_wrap_append_vulcan_triangulation,
                "append_vulcan_triangulation((str)arg1, (GXIPJ)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create new surface from a Maptek Vulcan triangulation file and add to an existing geosurface.\n\n"

                ":param arg1: 00t file\n"
                ":type arg1: str\n"
                ":param arg2: IPJ\n"
                ":type arg2: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg3: Geosurface file\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.4.0\n\n"
               ).staticmethod("append_vulcan_triangulation");

    scope().attr("SURFACE_OPEN_READ") = (int32_t)0;
    scope().attr("SURFACE_OPEN_READWRITE") = (int32_t)1;

}
