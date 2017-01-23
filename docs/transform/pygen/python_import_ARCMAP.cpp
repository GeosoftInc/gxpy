#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXARCMAP_wrap_change_size(double arg1, double arg2)
{
    GXARCMAP::change_size(arg1, arg2);
}
inline void GXARCMAP_wrap_display_in_3d_view(const gx_string_type& arg1)
{
    GXARCMAP::display_in_3d_view(arg1);
}
inline void GXARCMAP_wrap_export_feature_layer_by_name_to_3d_file(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4)
{
    GXARCMAP::export_feature_layer_by_name_to_3d_file(arg1, arg2, arg3, arg4);
}
inline void GXARCMAP_wrap_export_selected_feature_layer_to_3d_file(const gx_string_type& arg1)
{
    GXARCMAP::export_selected_feature_layer_to_3d_file(arg1);
}
inline void GXARCMAP_wrap_get_current_document_info(str_ref& arg1, str_ref& arg2, str_ref& arg3)
{
    GXARCMAP::get_current_document_info(arg1, arg2, arg3);
}
inline void GXARCMAP_wrap_get_selected_layer_info(int32_t arg1, str_ref& arg2, str_ref& arg3)
{
    GXARCMAP::get_selected_layer_info(arg1, arg2, arg3);
}
inline int32_t GXARCMAP_wrap_get_number_of_selected_layers()
{
    int32_t ret = GXARCMAP::get_number_of_selected_layers();
    return ret;
}
inline int32_t GXARCMAP_wrap_get_load_map(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4)
{
    int32_t ret = GXARCMAP::get_load_map(arg1, arg2, arg3, (ARCMAP_LOAD_FLAGS)arg4);
    return ret;
}
inline int32_t GXARCMAP_wrap_load_map_ex(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, int32_t arg5)
{
    int32_t ret = GXARCMAP::load_map_ex(arg1, arg2, arg3, arg4, (ARCMAP_LOAD_FLAGS)arg5);
    return ret;
}
inline int32_t GXARCMAP_wrap_get_load_shape(const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = GXARCMAP::get_load_shape(arg1, arg2);
    return ret;
}
inline int32_t GXARCMAP_wrap_load_spf(const gx_string_type& arg1, int32_t arg2)
{
    int32_t ret = GXARCMAP::load_spf(arg1, arg2);
    return ret;
}
inline void GXARCMAP_wrap_load_lyr(const gx_string_type& arg1)
{
    GXARCMAP::load_lyr(arg1);
}
inline void GXARCMAP_wrap_load_map(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, bool arg5, bool arg6, bool arg7)
{
    GXARCMAP::load_map(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXARCMAP_wrap_load_map_view(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, int32_t arg4)
{
    GXARCMAP::load_map_view(arg1, arg2, arg3, arg4);
}
inline void GXARCMAP_wrap_load_raster(const gx_string_type& arg1)
{
    GXARCMAP::load_raster(arg1);
}
inline void GXARCMAP_wrap_load_shape(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXARCMAP::load_shape(arg1, arg2, arg3);
}
inline void GXARCMAP_wrap_map_view_to_shape(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXLSTPtr arg4)
{
    GXARCMAP::map_view_to_shape(arg1, arg2, arg3, arg4);
}
inline void GXARCMAP_wrap_query_size(float_ref& arg1, float_ref& arg2)
{
    GXARCMAP::query_size(arg1, arg2);
}
inline void GXARCMAP_wrap_show_layer_by_name_in_3d(const gx_string_type& arg1, const gx_string_type& arg2, const gx_string_type& arg3)
{
    GXARCMAP::show_layer_by_name_in_3d(arg1, arg2, arg3);
}
inline void GXARCMAP_wrap_show_selected_layers_in_3d()
{
    GXARCMAP::show_selected_layers_in_3d();
}
inline void GXARCMAP_wrap_get_ipj_for_predefined_esri_gcs(GXIPJPtr arg1, int32_t arg2)
{
    GXARCMAP::get_ipj_for_predefined_esri_gcs(arg1, arg2);
}
inline void GXARCMAP_wrap_get_ipj_for_predefined_esri_pcs(GXIPJPtr arg1, int32_t arg2)
{
    GXARCMAP::get_ipj_for_predefined_esri_pcs(arg1, arg2);
}

void gxPythonImportGXARCMAP()
{

    class_<GXARCMAP, boost::noncopyable> pyClass("GXARCMAP",
            "\n.. parsed-literal::\n\n"
            "   This library is not a class. It contains various utilities\n"
            "   used in maps and layers by the Geosoft extensions for ArcGIS.\n\n"
            , no_init);


    pyClass.def("change_size", &GXARCMAP_wrap_change_size,
                "change_size((float)arg1, (float)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Changes the custom page size of the ArcGIS Map document.\n\n"

                ":param arg1: X Size (mm)\n"
                ":type arg1: float\n"
                ":param arg2: Y Size (mm)\n"
                ":type arg2: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("change_size");
    pyClass.def("display_in_3d_view", &GXARCMAP_wrap_display_in_3d_view,
                "display_in_3d_view((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Display a file in 3D view\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("display_in_3d_view");
    pyClass.def("export_feature_layer_by_name_to_3d_file", &GXARCMAP_wrap_export_feature_layer_by_name_to_3d_file,
                "export_feature_layer_by_name_to_3d_file((str)arg1, (str)arg2, (str)arg3, (str)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Exports the shapes from a feature layer of the ArcMap document to a 3D File.\n\n"

                ":param arg1: MXD filename\n"
                ":type arg1: str\n"
                ":param arg2: Dataframe name\n"
                ":type arg2: str\n"
                ":param arg3: Layer name\n"
                ":type arg3: str\n"
                ":param arg4: output file name\n"
                ":type arg4: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("export_feature_layer_by_name_to_3d_file");
    pyClass.def("export_selected_feature_layer_to_3d_file", &GXARCMAP_wrap_export_selected_feature_layer_to_3d_file,
                "export_selected_feature_layer_to_3d_file((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Exports the shapes from the currently selected feature layer (if any) in ArcMap to a 3D file (only on oriented frames i.e. sections).\n\n"

                ":param arg1: output file name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("export_selected_feature_layer_to_3d_file");
    pyClass.def("get_current_document_info", &GXARCMAP_wrap_get_current_document_info,
                "get_current_document_info((str_ref)arg1, (str_ref)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get some info on the current MXD in ArcMap and selected layer (if any)\n\n"

                ":param arg1: MXD filename\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: Selected Layer name (If a layer is selected)\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Dataframe name containing selected layer (If a layer is selected)\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("get_current_document_info");
    pyClass.def("get_selected_layer_info", &GXARCMAP_wrap_get_selected_layer_info,
                "get_selected_layer_info((int)arg1, (str_ref)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the name info on the specified selected layer\n\n"

                ":param arg1: Selected layer number\n"
                ":type arg1: int\n"
                ":param arg2: Selected Layer name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Dataframe name containing selected layer\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("get_selected_layer_info");
    pyClass.def("get_number_of_selected_layers", &GXARCMAP_wrap_get_number_of_selected_layers,
                "get_number_of_selected_layers() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the number of selected layers in the TOC\n"
                "   \n"
                "   Returns									 The number of layers selected.\n\n"

                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("get_number_of_selected_layers");
    pyClass.def("get_load_map", &GXARCMAP_wrap_get_load_map,
                "get_load_map((str)arg1, (str)arg2, (str)arg3, (int)arg4) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads a Geosoft map into the ArcMap document.\n\n"

                ":param arg1: Map File Name\n"
                ":type arg1: str\n"
                ":param arg2: Optional Extra Datasets CSV Filename (Rasters and shape files to display with layers)\n"
                ":type arg2: str\n"
                ":param arg3: Optional frame/layer tag (suffix)\n"
                ":type arg3: str\n"
                ":param arg4: Combination of \\ :ref:`ARCMAP_LOAD_FLAGS`\\ \n"
                ":type arg4: int\n"
                ":returns: 0 - OK\n"
                "          1 - Error\n"
                "          -1 - Canceled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The extra datasets CSV should contain the the following fields:\n"
                "   \n"
                "    ID          -  Unique identifier\n"
                "    DATASOURCE  -  Filename\n"
                "    TYPE        -  RASTER and SHAPE supported\n"
                "    MAPMATCH    -  Map to associate with (used for grouping logic)\n"
                "    VIEWMATCH   -  View to match with in associated map (used for grouping logic)\n"
                "    ZONEFILE    -  Used for type RASTER\n\n"
               ).staticmethod("get_load_map");
    pyClass.def("load_map_ex", &GXARCMAP_wrap_load_map_ex,
                "load_map_ex((str)arg1, (str)arg2, (str)arg3, (str)arg4, (int)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads a Geosoft map into the ArcMap document, specifying which View to use as Data view.\n\n"

                ":param arg1: Map File Name\n"
                ":type arg1: str\n"
                ":param arg2: View Name\n"
                ":type arg2: str\n"
                ":param arg3: Optional Extra Datasets CSV Filename (Rasters and shape files to display with layers)\n"
                ":type arg3: str\n"
                ":param arg4: Optional frame/layer tag (suffix)\n"
                ":type arg4: str\n"
                ":param arg5: Combination of \\ :ref:`ARCMAP_LOAD_FLAGS`\\ \n"
                ":type arg5: int\n"
                ":returns: 0 - OK\n"
                "          1 - Error\n"
                "          -1 - Canceled\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The extra datasets CSV should contain the the following fields:\n"
                "   \n"
                "    ID          -  Unique identifier\n"
                "    DATASOURCE  -  Filename\n"
                "    TYPE        -  RASTER and SHAPE supported\n"
                "    MAPMATCH    -  Map to associate with (used for grouping logic)\n"
                "    VIEWMATCH   -  View to match with in associated map (used for grouping logic)\n"
                "    ZONEFILE    -  Used for type RASTER\n\n"
               ).staticmethod("load_map_ex");
    pyClass.def("get_load_shape", &GXARCMAP_wrap_get_load_shape,
                "get_load_shape((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a shape file into ArcMap.\n\n"

                ":param arg1: shape file to load\n"
                ":type arg1: str\n"
                ":param arg2: delete existing layers?\n"
                ":type arg2: int\n"
                ":returns: 0- OK, 1 - Error, -1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("get_load_shape");
    pyClass.def("load_spf", &GXARCMAP_wrap_load_spf,
                "load_spf((str)arg1, (int)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Load all the shape files generated by importing a SPF into ArcMap.\n\n"

                ":param arg1: list of shape files to load\n"
                ":type arg1: str\n"
                ":param arg2: number of shape files\n"
                ":type arg2: int\n"
                ":returns: 0- OK, 1 - Error, -1 - Cancel\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("load_spf");
    pyClass.def("load_lyr", &GXARCMAP_wrap_load_lyr,
                "load_lyr((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a LYR file to the current data frame\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("load_lyr");
    pyClass.def("load_map", &GXARCMAP_wrap_load_map,
                "load_map((str)arg1, (str)arg2, (str)arg3, (str)arg4, (bool)arg5, (bool)arg6, (bool)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Loads a Geosoft map into the current ArcMap document\n\n"

                ":param arg1: Map File Name\n"
                ":type arg1: str\n"
                ":param arg2: View Name\n"
                ":type arg2: str\n"
                ":param arg3: Optional Extra Datasets CSV Filename (Rasters and shape files to display with layers)\n"
                ":type arg3: str\n"
                ":param arg4: Optional frame/layer tag (suffix)\n"
                ":type arg4: str\n"
                ":param arg5: Fit to map size; one of bool\n"
                ":type arg5: bool\n"
                ":param arg6: Activate view (3D); one of bool\n"
                ":type arg6: bool\n"
                ":param arg7: Layer name tag is prefix; one of bool\n"
                ":type arg7: bool\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The extra datasets CSV should contain the the following fields:\n"
                "   \n"
                "       ID          -  Unique identifier\n"
                "       DATASOURCE  -  Filename\n"
                "       TYPE        -  RASTER and SHAPE supported\n"
                "       MAPMATCH    -  Map to associate with (used for grouping logic)\n"
                "       VIEWMATCH   -  View to match with in associated map (used for grouping logic)\n"
                "       ZONEFILE    -  Used for type RASTER\n\n"
               ).staticmethod("load_map");
    pyClass.def("load_map_view", &GXARCMAP_wrap_load_map_view,
                "load_map_view((str)arg1, (str)arg2, (str)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a Geosoft Map as a layer into the current data frame\n\n"

                ":param arg1: Map File Name\n"
                ":type arg1: str\n"
                ":param arg2: View Name\n"
                ":type arg2: str\n"
                ":param arg3: Layer Name\n"
                ":type arg3: str\n"
                ":param arg4: Pass TRUE to also render other views in map (Use second parameter view for location)\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("load_map_view");
    pyClass.def("load_raster", &GXARCMAP_wrap_load_raster,
                "load_raster((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a raster file to the current data frame\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Loads any file type recognized as \"raster\" formats by ARC GIS.\n"
                "   This includes geosoft GRD files.\n\n"
               ).staticmethod("load_raster");
    pyClass.def("load_shape", &GXARCMAP_wrap_load_shape,
                "load_shape((str)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load a SHP file to the current data frame\n\n"

                ":param arg1: File Name\n"
                ":type arg1: str\n"
                ":param arg2: Layer Name Prefix: An underscore is added automatically\n"
                ":type arg2: str\n"
                ":param arg3: Layer Name Suffix  An underscore is added automatically\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The input layer name is created using the (optional) prefix and suffix as follows:\n"
                "   \n"
                "   Prefix_NAME_Suffix\n\n"
               ).staticmethod("load_shape");
    pyClass.def("map_view_to_shape", &GXARCMAP_wrap_map_view_to_shape,
                "map_view_to_shape((str)arg1, (str)arg2, (str)arg3, (GXLST)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create SHP file(s) from a Geosoft Map view.\n\n"

                ":param arg1: Map File Name\n"
                ":type arg1: str\n"
                ":param arg2: View Name\n"
                ":type arg2: str\n"
                ":param arg3: SHP File Name\n"
                ":type arg3: str\n"
                ":param arg4: List to fill with shape files created\n"
                ":type arg4: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The output SHP file name(s) are made up as follows\n"
                "   (where NAME is the input SHP file name):\n"
                "   \n"
                "         NAME_pt.shp    (point objects)\n"
                "         NAME_ln.shp    (line or arc objects)\n"
                "         NAME_pg.shp    (polygon objects)\n\n"
               ).staticmethod("map_view_to_shape");
    pyClass.def("query_size", &GXARCMAP_wrap_query_size,
                "query_size((float_ref)arg1, (float_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Querie the page size in mm of the entire map page.\n\n"

                ":param arg1: X Size (mm)\n"
                ":type arg1: :class:`geosoft.gxapi.float_ref`\n"
                ":param arg2: Y Size (mm)\n"
                ":type arg2: :class:`geosoft.gxapi.float_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("query_size");
    pyClass.def("show_layer_by_name_in_3d", &GXARCMAP_wrap_show_layer_by_name_in_3d,
                "show_layer_by_name_in_3d((str)arg1, (str)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Shows a layer in ArcMap in a 3D view in an MXD\n\n"

                ":param arg1: MXD filename\n"
                ":type arg1: str\n"
                ":param arg2: Dataframe name\n"
                ":type arg2: str\n"
                ":param arg3: Layer name\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("show_layer_by_name_in_3d");
    pyClass.def("show_selected_layers_in_3d", &GXARCMAP_wrap_show_selected_layers_in_3d,
                "show_selected_layers_in_3d() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Shows the selected layers in ArcMap in a 3D view\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.0\n\n"
               ).staticmethod("show_selected_layers_in_3d");
    pyClass.def("get_ipj_for_predefined_esri_gcs", &GXARCMAP_wrap_get_ipj_for_predefined_esri_gcs,
                "get_ipj_for_predefined_esri_gcs((GXIPJ)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fills an IPJ with a predefined ESRI GCS\n\n"

                ":param arg1: IPJ to fill\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: Predefined ESRI GCS Code\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"
               ).staticmethod("get_ipj_for_predefined_esri_gcs");
    pyClass.def("get_ipj_for_predefined_esri_pcs", &GXARCMAP_wrap_get_ipj_for_predefined_esri_pcs,
                "get_ipj_for_predefined_esri_pcs((GXIPJ)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fills an IPJ with a predefined ESRI PCS\n\n"

                ":param arg1: IPJ to fill\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg2: Predefined ESRI PCS Code\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 8.0.1\n\n"
               ).staticmethod("get_ipj_for_predefined_esri_pcs");

    scope().attr("ARCMAP_LOAD_DELFRAME") = (int32_t)1;
    scope().attr("ARCMAP_LOAD_DELLAYER") = (int32_t)2;
    scope().attr("ARCMAP_LOAD_EXISTFRAME") = (int32_t)4;
    scope().attr("ARCMAP_LOAD_COPYLAYER") = (int32_t)8;
    scope().attr("ARCMAP_LOAD_HIDESIBLINGS") = (int32_t)16;
    scope().attr("ARCMAP_LOAD_PREFIXMAPFRAME") = (int32_t)32;
    scope().attr("ARCMAP_LOAD_PREFIXMAPLAYER") = (int32_t)64;
    scope().attr("ARCMAP_LOAD_MERGETOSINGLEVIEW") = (int32_t)128;
    scope().attr("ARCMAP_LOAD_INTOCURRENTFRAME") = (int32_t)256;
    scope().attr("ARCMAP_LOAD_NOMAPLAYERS") = (int32_t)512;
    scope().attr("ARCMAP_LOAD_ACTIVATE") = (int32_t)1024;
    scope().attr("ARCMAP_LOAD_NEW") = (int32_t)2048;
    scope().attr("ARCMAP_LOAD_NAMETAGISPREFIX") = (int32_t)4096;

}
