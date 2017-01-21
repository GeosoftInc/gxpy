#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXMAP_wrap_export_all_in_view(GXMAPPtr self, const gx_string_type& arg1, const gx_string_type& arg2, double arg3, double arg4, int32_t arg5, int32_t arg6, const gx_string_type& arg7, const gx_string_type& arg8)
{
    self->export_all_in_view(arg1, arg2, arg3, arg4, (MAP_EXPORT_BITS)arg5, (MAP_EXPORT_METHOD)arg6, arg7, arg8);
}
inline void GXMAP_wrap_export_all_raster(GXMAPPtr self, const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3, int32_t arg4, double arg5, int32_t arg6, int32_t arg7, const gx_string_type& arg8, const gx_string_type& arg9)
{
    self->export_all_raster(arg1, arg2, arg3, arg4, arg5, (MAP_EXPORT_BITS)arg6, (MAP_EXPORT_METHOD)arg7, arg8, arg9);
}
inline void GXMAP_wrap_export_area_in_view(GXMAPPtr self, const gx_string_type& arg1, const gx_string_type& arg2, double arg3, double arg4, int32_t arg5, int32_t arg6, double arg7, double arg8, double arg9, double arg10, const gx_string_type& arg11, const gx_string_type& arg12)
{
    self->export_area_in_view(arg1, arg2, arg3, arg4, (MAP_EXPORT_BITS)arg5, (MAP_EXPORT_METHOD)arg6, arg7, arg8, arg9, arg10, arg11, arg12);
}
inline void GXMAP_wrap_export_area_raster(GXMAPPtr self, const gx_string_type& arg1, const gx_string_type& arg2, double arg3, double arg4, double arg5, double arg6, int32_t arg7, int32_t arg8, double arg9, int32_t arg10, int32_t arg11, const gx_string_type& arg12, const gx_string_type& arg13)
{
    self->export_area_raster(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, (MAP_EXPORT_BITS)arg10, (MAP_EXPORT_METHOD)arg11, arg12, arg13);
}
inline void GXMAP_wrap_render_bitmap(GXMAPPtr self, const gx_string_type& arg1, double arg2, double arg3, double arg4, double arg5, const gx_string_type& arg6, int32_t arg7)
{
    self->render_bitmap(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXMAP_wrap_agg_list(GXMAPPtr self, GXLSTPtr arg1, int32_t arg2)
{
    self->agg_list(arg1, arg2);
}
inline void GXMAP_wrap_agg_list_ex(GXMAPPtr self, GXLSTPtr arg1, int32_t arg2, int32_t arg3)
{
    self->agg_list_ex(arg1, arg2, (MAP_LIST_MODE)arg3);
}
inline void GXMAP_wrap_clean(GXMAPPtr self)
{
    self->clean();
}
inline void GXMAP_wrap_commit(GXMAPPtr self)
{
    self->commit();
}
inline void GXMAP_wrap_copy_map_to_view(GXMAPPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->copy_map_to_view(arg1, arg2);
}
inline void GXMAP_wrap_crc_map(GXMAPPtr self, int_ref& arg1, const gx_string_type& arg2)
{
    self->crc_map(arg1, arg2);
}
inline GXMAPPtr GXMAP_wrap_create(const gx_string_type& arg1, int32_t arg2)
{
    GXMAPPtr ret = GXMAP::create(arg1, (MAP_OPEN)arg2);
    return ret;
}
inline GXMAPPtr GXMAP_wrap_current()
{
    GXMAPPtr ret = GXMAP::current();
    return ret;
}
inline void GXMAP_wrap_delete_view(GXMAPPtr self, const gx_string_type& arg1)
{
    self->delete_view(arg1);
}
inline void GXMAP_wrap_discard(GXMAPPtr self)
{
    self->discard();
}
inline void GXMAP_wrap_dup_map(GXMAPPtr self, GXMAPPtr arg1, int32_t arg2)
{
    self->dup_map(arg1, (DUPMAP)arg2);
}
inline GXLPTPtr GXMAP_wrap_get_lpt(GXMAPPtr self)
{
    GXLPTPtr ret = self->get_lpt();
    return ret;
}
inline void GXMAP_wrap_get_map_size(GXMAPPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4)
{
    self->get_map_size(arg1, arg2, arg3, arg4);
}
inline GXMETAPtr GXMAP_wrap_get_meta(GXMAPPtr self)
{
    GXMETAPtr ret = self->get_meta();
    return ret;
}
inline GXREGPtr GXMAP_wrap_get_reg(GXMAPPtr self)
{
    GXREGPtr ret = self->get_reg();
    return ret;
}
inline void GXMAP_wrap_group_list(GXMAPPtr self, GXLSTPtr arg1)
{
    self->group_list(arg1);
}
inline void GXMAP_wrap_group_list_ex(GXMAPPtr self, GXLSTPtr arg1, int32_t arg2)
{
    self->group_list_ex(arg1, (MAP_LIST_MODE)arg2);
}
inline void GXMAP_wrap_duplicate_view(GXMAPPtr self, const gx_string_type& arg1, str_ref& arg2, bool arg3)
{
    self->duplicate_view(arg1, arg2, arg3);
}
inline int32_t GXMAP_wrap_exist_view(GXMAPPtr self, const gx_string_type& arg1)
{
    int32_t ret = self->exist_view(arg1);
    return ret;
}
inline void GXMAP_wrap_get_class_name(GXMAPPtr self, const gx_string_type& arg1, str_ref& arg2)
{
    self->get_class_name(arg1, arg2);
}
inline void GXMAP_wrap_get_file_name(GXMAPPtr self, str_ref& arg1)
{
    self->get_file_name(arg1);
}
inline void GXMAP_wrap_get_map_name(GXMAPPtr self, str_ref& arg1)
{
    self->get_map_name(arg1);
}
inline int32_t GXMAP_wrap_packed_files(GXMAPPtr self)
{
    int32_t ret = self->packed_files();
    return ret;
}
inline void GXMAP_wrap_un_pack_files_ex(GXMAPPtr self, int32_t arg1, str_ref& arg2)
{
    self->un_pack_files_ex(arg1, arg2);
}
inline void GXMAP_wrap_un_pack_files_to_folder(GXMAPPtr self, int32_t arg1, const gx_string_type& arg2, str_ref& arg3)
{
    self->un_pack_files_to_folder(arg1, arg2, arg3);
}
inline void GXMAP_wrap_pack_files(GXMAPPtr self)
{
    self->pack_files();
}
inline void GXMAP_wrap_render(GXMAPPtr self, const gx_string_type& arg1)
{
    self->render(arg1);
}
inline void GXMAP_wrap_resize_all(GXMAPPtr self)
{
    self->resize_all();
}
inline void GXMAP_wrap_resize_all_ex(GXMAPPtr self, int32_t arg1)
{
    self->resize_all_ex((MVIEW_EXTENT)arg1);
}
inline double GXMAP_wrap_get_map_scale(GXMAPPtr self)
{
    double ret = self->get_map_scale();
    return ret;
}
inline void GXMAP_wrap_save_as_mxd(GXMAPPtr self, const gx_string_type& arg1)
{
    self->save_as_mxd(arg1);
}
inline void GXMAP_wrap_set_class_name(GXMAPPtr self, const gx_string_type& arg1, const gx_string_type& arg2)
{
    self->set_class_name(arg1, arg2);
}
inline void GXMAP_wrap_set_current(GXMAPPtr self)
{
    self->set_current();
}
inline void GXMAP_wrap_set_map_name(GXMAPPtr self, const gx_string_type& arg1)
{
    self->set_map_name(arg1);
}
inline void GXMAP_wrap_set_map_scale(GXMAPPtr self, double arg1)
{
    self->set_map_scale(arg1);
}
inline void GXMAP_wrap_set_map_size(GXMAPPtr self, double arg1, double arg2, double arg3, double arg4)
{
    self->set_map_size(arg1, arg2, arg3, arg4);
}
inline void GXMAP_wrap_set_meta(GXMAPPtr self, GXMETAPtr arg1)
{
    self->set_meta(arg1);
}
inline void GXMAP_wrap_set_reg(GXMAPPtr self, GXREGPtr arg1)
{
    self->set_reg(arg1);
}
inline void GXMAP_wrap_sync(const gx_string_type& arg1)
{
    GXMAP::sync(arg1);
}
inline void GXMAP_wrap_un_pack_files(GXMAPPtr self)
{
    self->un_pack_files();
}
inline void GXMAP_wrap_view_list(GXMAPPtr self, GXLSTPtr arg1)
{
    self->view_list(arg1);
}
inline void GXMAP_wrap_view_list_ex(GXMAPPtr self, GXLSTPtr arg1, int32_t arg2)
{
    self->view_list_ex(arg1, (MAP_LIST_MODE)arg2);
}
inline int32_t GXMAP_wrap_get_data_proj(GXMAPPtr self)
{
    int32_t ret = self->get_data_proj();
    return ret;
}

void gxPythonImportGXMAP()
{

    class_<GXMAP, GXMAPPtr> pyClass("GXMAP",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		MAPs are containers for MVIEW objects. A view is a 3-D translation\n"
                                    "   		and a clip window on a map. Graphic entities can be drawn in an MVIEW.\n"
                                    "   		It is recommended that the MAP class be instantiated by first creating\n"
                                    "   		an EMAP object and calling the \\ :func:`geosoft.gxapi.GXEMAP.lock`\\ () function.\n"
                                    "   		(See the explanation on the distinction between the MAP and EMAP classes).\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXMAP::null, "null() -> GXMAP\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXMAP`\n\n:returns: A null :class:`geosoft.gxapi.GXMAP`\n:rtype: :class:`geosoft.gxapi.GXMAP`\n").staticmethod("null");
    pyClass.def("is_null", &GXMAP::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXMAP is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXMAP`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXMAP::_internal_handle);
    pyClass.def("export_all_in_view", &GXMAP_wrap_export_all_in_view,
                "export_all_in_view((str)arg1, (str)arg2, (float)arg3, (float)arg4, (int)arg5, (int)arg6, (str)arg7, (str)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export the entire map in view units to an external format.\n\n"

                ":param arg1: File Name To Export\n"
                ":type arg1: str\n"
                ":param arg2: View to export coordinates in\n"
                ":type arg2: str\n"
                ":param arg3: Resolution in view units of one pixel (or dummy, will be used if DPI is dummy)\n"
                ":type arg3: float\n"
                ":param arg4: Resolution in DPI (will override view resolution if not dummy, map page size will be used to determine pixel size of output)\n"
                ":type arg4: float\n"
                ":param arg5: \\ :ref:`MAP_EXPORT_BITS`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`MAP_EXPORT_METHOD`\\ \n"
                ":type arg6: int\n"
                ":param arg7: \\ :ref:`MAP_EXPORT_FORMAT`\\ \n"
                ":type arg7: str\n"
                ":param arg8: Extended Options String (format specific)\n"
                ":type arg8: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               );
    pyClass.def("export_all_raster", &GXMAP_wrap_export_all_raster,
                "export_all_raster((str)arg1, (str)arg2, (int)arg3, (int)arg4, (float)arg5, (int)arg6, (int)arg7, (str)arg8, (str)arg9) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export the entire map to map to a non-geo raster format\n\n"

                ":param arg1: File Name To Export\n"
                ":type arg1: str\n"
                ":param arg2: View to export coordinates in\n"
                ":type arg2: str\n"
                ":param arg3: Number of Pixels in X (X or Y should be specified the other should be 0 and computed by export, or both can be 0 and DPI defined)\n"
                ":type arg3: int\n"
                ":param arg4: Number of Pixels in Y (X or Y should be specified the other should be 0 and computed by export, or both can be 0 and DPI defined)\n"
                ":type arg4: int\n"
                ":param arg5: Resolution in DPI (will override X and Y if not dummy, map page size will be used to determine pixel size of output)\n"
                ":type arg5: float\n"
                ":param arg6: \\ :ref:`MAP_EXPORT_BITS`\\ \n"
                ":type arg6: int\n"
                ":param arg7: \\ :ref:`MAP_EXPORT_METHOD`\\ \n"
                ":type arg7: int\n"
                ":param arg8: \\ :ref:`MAP_EXPORT_RASTER_FORMAT`\\ \n"
                ":type arg8: str\n"
                ":param arg9: Extended Options String (format specific)\n"
                ":type arg9: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               );
    pyClass.def("export_area_in_view", &GXMAP_wrap_export_area_in_view,
                "export_area_in_view((str)arg1, (str)arg2, (float)arg3, (float)arg4, (int)arg5, (int)arg6, (float)arg7, (float)arg8, (float)arg9, (float)arg10, (str)arg11, (str)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export an area of a map in view units to an external format\n\n"

                ":param arg1: File Name To Export\n"
                ":type arg1: str\n"
                ":param arg2: View to export coordinates in\n"
                ":type arg2: str\n"
                ":param arg3: Resolution in view units of one pixel (or dummy, will be used if DPI is dummy)\n"
                ":type arg3: float\n"
                ":param arg4: Resolution in DPI (will override view resolution if not dummy, map page size will be used to determine pixel size of output)\n"
                ":type arg4: float\n"
                ":param arg5: \\ :ref:`MAP_EXPORT_BITS`\\ \n"
                ":type arg5: int\n"
                ":param arg6: \\ :ref:`MAP_EXPORT_METHOD`\\ \n"
                ":type arg6: int\n"
                ":param arg7: Area To Export Min X location in view units\n"
                ":type arg7: float\n"
                ":param arg8: Area To Export Min Y location in view units\n"
                ":type arg8: float\n"
                ":param arg9: Area To Export Max X location in view units\n"
                ":type arg9: float\n"
                ":param arg10: Area To Export Max Y location in view units\n"
                ":type arg10: float\n"
                ":param arg11: \\ :ref:`MAP_EXPORT_FORMAT`\\ \n"
                ":type arg11: str\n"
                ":param arg12: Extended Options String (format specific)\n"
                ":type arg12: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               );
    pyClass.def("export_area_raster", &GXMAP_wrap_export_area_raster,
                "export_area_raster((str)arg1, (str)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6, (int)arg7, (int)arg8, (float)arg9, (int)arg10, (int)arg11, (str)arg12, (str)arg13) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Export an area of a map to a non-geo raster format\n\n"

                ":param arg1: File Name To Export\n"
                ":type arg1: str\n"
                ":param arg2: View to export coordinates in\n"
                ":type arg2: str\n"
                ":param arg3: Area To Export Min X location in view units\n"
                ":type arg3: float\n"
                ":param arg4: Area To Export Min Y location in view units\n"
                ":type arg4: float\n"
                ":param arg5: Area To Export Max X location in view units\n"
                ":type arg5: float\n"
                ":param arg6: Area To Export Max Y location in view units\n"
                ":type arg6: float\n"
                ":param arg7: Number of Pixels in X (X or Y should be specified the other should be 0 and computed by export, or both can be 0 and DPI defined)\n"
                ":type arg7: int\n"
                ":param arg8: Number of Pixels in Y (X or Y should be specified the other should be 0 and computed by export, or both can be 0 and DPI defined)\n"
                ":type arg8: int\n"
                ":param arg9: Resolution in DPI (will override X and Y if not dummy, map page size will be used to determine pixel size of output)\n"
                ":type arg9: float\n"
                ":param arg10: \\ :ref:`MAP_EXPORT_BITS`\\ \n"
                ":type arg10: int\n"
                ":param arg11: \\ :ref:`MAP_EXPORT_METHOD`\\ \n"
                ":type arg11: int\n"
                ":param arg12: \\ :ref:`MAP_EXPORT_RASTER_FORMAT`\\ \n"
                ":type arg12: str\n"
                ":param arg13: Extended Options String (format specific)\n"
                ":type arg13: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               );
    pyClass.def("render_bitmap", &GXMAP_wrap_render_bitmap,
                "render_bitmap((str)arg1, (float)arg2, (float)arg3, (float)arg4, (float)arg5, (str)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Render a map to a bitmap.\n\n"

                ":param arg1: View we exporting units in\n"
                ":type arg1: str\n"
                ":param arg2: MinX\n"
                ":type arg2: float\n"
                ":param arg3: MinY\n"
                ":type arg3: float\n"
                ":param arg4: MaxX\n"
                ":type arg4: float\n"
                ":param arg5: MaxY\n"
                ":type arg5: float\n"
                ":param arg6: File to generate (ext forced to BMP)\n"
                ":type arg6: str\n"
                ":param arg7: Maximum resolution in either direction, -1 for none (will change the pixel density of image if exceeded)\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("agg_list", &GXMAP_wrap_agg_list,
                "agg_list((GXLST)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of all aggregates in this map.\n\n"

                ":param arg1: list to hold the views (allow up to 96 characters)\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: 0 - view/agg only 1 - view/agg/layer\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					List items are returned as view/agg/layer.\n"
                "   					The layer name is optional\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXLST`\\  class.\n\n"
               );
    pyClass.def("agg_list_ex", &GXMAP_wrap_agg_list_ex,
                "agg_list_ex((GXLST)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of aggregates in this map based on a mode\n\n"

                ":param arg1: list to hold the views (allow up to 96 characters)\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: 0 - view/agg only 1 - view/agg/layer\n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`MAP_LIST_MODE`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					List items are returned as view/agg/layer.\n"
                "   					The layer name is optional\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXLST`\\  class.\n\n"
               );
    pyClass.def("clean", &GXMAP_wrap_clean,
                "clean() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Clean up empty groups in all views in map.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("commit", &GXMAP_wrap_commit,
                "commit() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Commit any changes to a map.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("copy_map_to_view", &GXMAP_wrap_copy_map_to_view,
                "copy_map_to_view((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Copy entire map into one view in output map.\n\n"

                ":param arg1: Destination MAP name\n"
                ":type arg1: str\n"
                ":param arg2: Name of View\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               );
    pyClass.def("crc_map", &GXMAP_wrap_crc_map,
                "crc_map((int_ref)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate an XML CRC of a MAP\n\n"

                ":param arg1: CRC returned\n"
                ":type arg1: :class:`geosoft.gxapi.int_ref`\n"
                ":param arg2: Name of xml to generate (.zip added)\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("create", &GXMAP_wrap_create,
                "create((str)arg1, (int)arg2) -> GXMAP:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a MAP.\n\n"

                ":param arg1: MAP file name\n"
                ":type arg1: str\n"
                ":param arg2: \\ :ref:`MAP_OPEN`\\ \n"
                ":type arg2: int\n"
                ":returns: MAP Object\n"
                ":rtype: :class:`geosoft.gxapi.GXMAP`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("current", &GXMAP_wrap_current,
                "current() -> GXMAP:\n"

                "\n.. parsed-literal::\n\n"
                "   This method returns the Current map opened.\n\n"

                ":returns: MAP Object\n"
                ":rtype: :class:`geosoft.gxapi.GXMAP`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If there is no current map, and running interactively,\n"
                "   					the user is prompted to open a map.\n"
                "   				\n\n"
               ).staticmethod("current");
    pyClass.def("delete_view", &GXMAP_wrap_delete_view,
                "delete_view((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Deletes a view in this map.\n\n"

                ":param arg1: View Name to delete\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the view does not exist, nothing happens.\n\n"
               );
    pyClass.def("discard", &GXMAP_wrap_discard,
                "discard() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Discard all changes made to the map.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("dup_map", &GXMAP_wrap_dup_map,
                "dup_map((GXMAP)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Duplicate copy of current map.\n\n"

                ":param arg1: Destination MAP object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: \\ :ref:`DUPMAP`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Before version 6.2. text in maps were displayed with a character set\n"
                "   					defining how characters above ASCII 127 would be displayed. 6.2. introduced\n"
                "   					Unicode in the core montaj engine that eliminated the need for such a setting and\n"
                "   					greatly increased the number of symbols that can be used. The only caveat\n"
                "   					of the new system is that text may appear corrupted (especially with GFN fonts) in\n"
                "   					versions prior to 6.2. for maps that was created with a version after the port.\n"
                "   					The constant DUPMAP_COPY_PRE62 provides a way to create maps that can be\n"
                "   					distributed to versions prior to 6.2.\n"
                "   				\n\n"
               );
    pyClass.def("get_lpt", &GXMAP_wrap_get_lpt,
                "get_lpt() -> GXLPT:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the LPT Object of a MAP.\n\n"

                ":returns: LPT Object\n"
                ":rtype: :class:`geosoft.gxapi.GXLPT`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_map_size", &GXMAP_wrap_get_map_size,
                "get_map_size((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the size of the Map.\n\n"

                ":param arg1: X minimum in mm\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y minimun in mm\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg3: X maximum in mm\n"
                ":type arg3: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg4: Y maximum in mm\n"
                ":type arg4: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_meta", &GXMAP_wrap_get_meta,
                "get_meta() -> GXMETA:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the map's META\n\n"

                ":returns: META Object\n"
                ":rtype: :class:`geosoft.gxapi.GXMETA`\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the map has no META, an empty META will be created.\n\n"
               );
    pyClass.def("get_reg", &GXMAP_wrap_get_reg,
                "get_reg() -> GXREG:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the map's REG\n\n"

                ":returns: REG Object\n"
                ":rtype: :class:`geosoft.gxapi.GXREG`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the map has no REG, an empty REG will be created.\n\n"
               );
    pyClass.def("group_list", &GXMAP_wrap_group_list,
                "group_list((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of all views/groups in this map.\n\n"

                ":param arg1: list to hold the view/groups.  Names may be up to 2080 characters in length.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns all groups in the form \"ViewName\\GroupName\"\n"
                "   					To get a LST of groups in a specific map view, use\n"
                "   					the \\ :func:`geosoft.gxapi.GXMVIEW.list_groups`\\  function.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   \n"
                "   					\\ :class:`geosoft.gxapi.GXLST`\\  class.\n"
                "   					\\ :func:`geosoft.gxapi.GXMVIEW.list_groups`\\ \n"
                "   				\n\n"
               );
    pyClass.def("group_list_ex", &GXMAP_wrap_group_list_ex,
                "group_list_ex((GXLST)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of views/groups in this map for this mode\n\n"

                ":param arg1: list to hold the views.  View names may be up to 2080 characters in length.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`MAP_LIST_MODE`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXLST`\\  class.\n\n"
               );
    pyClass.def("duplicate_view", &GXMAP_wrap_duplicate_view,
                "duplicate_view((str)arg1, (str_ref)arg2, (bool)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Duplicate an entire view\n\n"

                ":param arg1: Name of view to duplicate\n"
                ":type arg1: str\n"
                ":param arg2: Name of new view created (pass in \"\" and the new name is returned)\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Copy all groups bool\n"
                ":type arg3: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("exist_view", &GXMAP_wrap_exist_view,
                "exist_view((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Checks to see if a view exists.\n\n"

                ":param arg1: View name\n"
                ":type arg1: str\n"
                ":returns: 0 view does not exist.\n"
                "          						1 view exists.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_class_name", &GXMAP_wrap_get_class_name,
                "get_class_name((str)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a class name.\n\n"

                ":param arg1: class\n"
                ":type arg1: str\n"
                ":param arg2: name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Map class names are intended to be used to record the\n"
                "   					names of certain view classes in the map, such as the\n"
                "   					\"Data\", \"Base\" and \"Section\" views.\n"
                "   \n"
                "   					There can only be one name for each class, but it can\n"
                "   					be changed.  This lets the \"Data\" class name change,\n"
                "   					for example, so plotting can select which class to plot\n"
                "   					to.\n"
                "   \n"
                "   					If a name is not set, the class name is set and\n"
                "   					returned.\n"
                "   				\n\n"
               );
    pyClass.def("get_file_name", &GXMAP_wrap_get_file_name,
                "get_file_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the name of the map.\n\n"

                ":param arg1: returned map file name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("get_map_name", &GXMAP_wrap_get_map_name,
                "get_map_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the Map Name of the Map.\n\n"

                ":param arg1: returned map name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("packed_files", &GXMAP_wrap_packed_files,
                "packed_files() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   The number of packed files in the current map.\n\n"

                ":returns: The number of packed files in map.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"
               );
    pyClass.def("un_pack_files_ex", &GXMAP_wrap_un_pack_files_ex,
                "un_pack_files_ex((int)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   UnPack all files from map to workspace.\n\n"

                ":param arg1: (0 - Produce errors, 1 - Force overwrites)\n"
                ":type arg1: int\n"
                ":param arg2: List of files that are problematic returned\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The option to force will simply overwrite the files.\n"
                "   					When the non-force option is in effect the method will\n"
                "   					stop if any files are going to be overwritting. These\n"
                "   					file names will end up in the Errors string.\n"
                "   				\n\n"
               );
    pyClass.def("un_pack_files_to_folder", &GXMAP_wrap_un_pack_files_to_folder,
                "un_pack_files_to_folder((int)arg1, (str)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   UnPack all files from map to workspace.\n\n"

                ":param arg1: (0 - Produce errors, 1 - Force overwrites)\n"
                ":type arg1: int\n"
                ":param arg2: Directory to place unpacked files in.\n"
                ":type arg2: str\n"
                ":param arg3: List of files that are problematic returned\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"
               );
    pyClass.def("pack_files", &GXMAP_wrap_pack_files,
                "pack_files() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Pack all files in the map so that it can be mailed.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("render", &GXMAP_wrap_render,
                "render((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Render a map to file/device.\n\n"

                ":param arg1: Plot file/device\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("resize_all", &GXMAP_wrap_resize_all,
                "resize_all() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Resize a map to the extents of all views.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is the same as \\ :func:`geosoft.gxapi.GXMAP.resize_all_ex`\\  with\n"
                "   					MVIEW_EXTENT_CLIP.\n"
                "   				\n\n"
               );
    pyClass.def("resize_all_ex", &GXMAP_wrap_resize_all_ex,
                "resize_all_ex((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \\ :func:`geosoft.gxapi.GXMAP.resize_all`\\  with selection of view extent type selection.\n\n"

                ":param arg1: \\ :ref:`MVIEW_EXTENT`\\ \n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					MVIEW_EXTENT_VISIBLE gives a more \"reasonable\" map size, and won't\n"
                "   					clip off labels outside a graph window.\n"
                "   				\n\n"
               );
    pyClass.def("get_map_scale", &GXMAP_wrap_get_map_scale,
                "get_map_scale() -> float:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the current map scale\n\n"

                ":returns: The current map scale\n"
                ":rtype: float\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If there is a \"Data\" view, the scale is derived from\n"
                "   					this view.\n"
                "   \n"
                "   					If their is no data view, the scale is derived\n"
                "   					from the first view that is not scaled in mm.\n"
                "   					otherwise, the scale is 1000 (mm).\n"
                "   \n"
                "   					All views must be closed, or open read-only.\n"
                "   				\n\n"
               );
    pyClass.def("save_as_mxd", &GXMAP_wrap_save_as_mxd,
                "save_as_mxd((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save as ArcGIS MXD\n\n"

                ":param arg1: Geosoft map file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               );
    pyClass.def("set_class_name", &GXMAP_wrap_set_class_name,
                "set_class_name((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set a class name.\n\n"

                ":param arg1: class\n"
                ":type arg1: str\n"
                ":param arg2: name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Map class names are intended to be used to record the\n"
                "   					names of certain view classes in the map, such as the\n"
                "   					\"Data\", \"Base\" and \"Section\" views.\n"
                "   \n"
                "   					There can only be one name for each class, but it can\n"
                "   					be changed.  This lets the \"Data\" class name change,\n"
                "   					for example, so plotting can select which class to plot\n"
                "   					to.\n"
                "   \n"
                "   					If a name is not set, the class name is set and\n"
                "   					returned.\n"
                "   				\n\n"
               );
    pyClass.def("set_current", &GXMAP_wrap_set_current,
                "set_current() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets the current map to this map.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_map_name", &GXMAP_wrap_set_map_name,
                "set_map_name((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the Map Name of the Map.\n\n"

                ":param arg1: Map Name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("set_map_scale", &GXMAP_wrap_set_map_scale,
                "set_map_scale((float)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the current map scale\n\n"

                ":param arg1: new map scale (must be > 0).\n"
                ":type arg1: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					All views in the map will be resized for the new\n"
                "   					map scale.\n"
                "   				\n\n"
               );
    pyClass.def("set_map_size", &GXMAP_wrap_set_map_size,
                "set_map_size((float)arg1, (float)arg2, (float)arg3, (float)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the size of the Map.\n\n"

                ":param arg1: X minimum in mm\n"
                ":type arg1: float\n"
                ":param arg2: Y minimun in mm\n"
                ":type arg2: float\n"
                ":param arg3: X maximum in mm\n"
                ":type arg3: float\n"
                ":param arg4: Y maximum in mm\n"
                ":type arg4: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The map size is area on the MAP that contains graphics\n"
                "   					to be plotted.  The area can be bigger or smaller that\n"
                "   					the current views.  In the absense of any other information\n"
                "   					only the area defined by the map size is plotted.\n"
                "   				\n\n"

                "\n.. seealso::\n\n"
                "   SetSizeViews_MAP\n\n"
               );
    pyClass.def("set_meta", &GXMAP_wrap_set_meta,
                "set_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write a META to a map.\n\n"

                ":param arg1: META to write to map\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"
               );
    pyClass.def("set_reg", &GXMAP_wrap_set_reg,
                "set_reg((GXREG)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Write a REG to a map.\n\n"

                ":param arg1: REG to write to map\n"
                ":type arg1: :class:`geosoft.gxapi.GXREG`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("sync", &GXMAP_wrap_sync,
                "sync((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Syncronize the Metadata\n\n"

                ":param arg1: Geosoft map file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.0.0\n\n"
               ).staticmethod("sync");
    pyClass.def("un_pack_files", &GXMAP_wrap_un_pack_files,
                "un_pack_files() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   UnPack all files from map to workspace.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("view_list", &GXMAP_wrap_view_list,
                "view_list((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of all views in this map.\n\n"

                ":param arg1: list to hold the views.  View names may be up to 2080 characters in length.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n.. seealso::\n\n"
                "   \\ :class:`geosoft.gxapi.GXLST`\\  class.\n\n"
               );
    pyClass.def("view_list_ex", &GXMAP_wrap_view_list_ex,
                "view_list_ex((GXLST)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a list of views of certain types in this map\n\n"

                ":param arg1: list to hold the views.  View names may be up to 2080 characters in length.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`MAP_LIST_MODE`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.2\n\n"
               );
    pyClass.def("get_data_proj", &GXMAP_wrap_get_data_proj,
                "get_data_proj() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the projection type of the Data view of a map.\n\n"

                ":returns: Project type as an integer\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.3.0\n\n"
               );

    scope().attr("DUPMAP_BLANK") = (int32_t)0;
    scope().attr("DUPMAP_COPY") = (int32_t)1;
    scope().attr("DUPMAP_COPY_PRE62") = (int32_t)2;
    scope().attr("MAP_EXPORT_BITS_24") = (int32_t)24;
    scope().attr("MAP_EXPORT_BITS_GREY8") = (int32_t)9;
    scope().attr("MAP_EXPORT_BITS_8") = (int32_t)8;
    scope().attr("MAP_EXPORT_BITS_GREY4") = (int32_t)5;
    scope().attr("MAP_EXPORT_BITS_4") = (int32_t)4;
    scope().attr("MAP_EXPORT_BITS_GREY1") = (int32_t)1;
    scope().attr("MAP_EXPORT_BITS_DEFAULT") = (int32_t)0;
    scope().attr("MAP_EXPORT_FORMAT_PLT") = "PLT";
    scope().attr("MAP_EXPORT_FORMAT_SHP") = "SHP";
    scope().attr("MAP_EXPORT_FORMAT_DXF12") = "DXF12";
    scope().attr("MAP_EXPORT_FORMAT_DXF13") = "DXF13";
    scope().attr("MAP_EXPORT_FORMAT_GTIFF") = "GTIFF";
    scope().attr("MAP_EXPORT_FORMAT_MTIFF") = "MTIFF";
    scope().attr("MAP_EXPORT_FORMAT_ATIFF") = "ATIFF";
    scope().attr("MAP_EXPORT_FORMAT_GEO") = "GEO";
    scope().attr("MAP_EXPORT_FORMAT_ERM") = "ERM";
    scope().attr("MAP_EXPORT_FORMAT_KMZ") = "KMZ";
    scope().attr("MAP_EXPORT_METHOD_STANDARD") = (int32_t)0;
    scope().attr("MAP_EXPORT_METHOD_DIFFUSE") = (int32_t)1;
    scope().attr("MAP_EXPORT_METHOD_NONE") = (int32_t)2;
    scope().attr("MAP_EXPORT_RASTER_FORMAT_EMF") = "EMF";
    scope().attr("MAP_EXPORT_RASTER_FORMAT_BMP") = "BMP";
    scope().attr("MAP_EXPORT_RASTER_FORMAT_JPEGL") = "JPEGL";
    scope().attr("MAP_EXPORT_RASTER_FORMAT_JPEG") = "JPEG";
    scope().attr("MAP_EXPORT_RASTER_FORMAT_JPEGH") = "JPEGH";
    scope().attr("MAP_EXPORT_RASTER_FORMAT_GIF") = "GIF";
    scope().attr("MAP_EXPORT_RASTER_FORMAT_PCX") = "PCX";
    scope().attr("MAP_EXPORT_RASTER_FORMAT_PNG") = "PNG";
    scope().attr("MAP_EXPORT_RASTER_FORMAT_EPS") = "EPS";
    scope().attr("MAP_EXPORT_RASTER_FORMAT_TIFF") = "TIFF";
    scope().attr("MAP_LIST_MODE_ALL") = (int32_t)0;
    scope().attr("MAP_LIST_MODE_3D") = (int32_t)1;
    scope().attr("MAP_LIST_MODE_NOT3D") = (int32_t)2;
    scope().attr("MAP_WRITENEW") = (int32_t)1;
    scope().attr("MAP_WRITEOLD") = (int32_t)2;

}
