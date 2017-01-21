#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline GXGISPtr GXGIS_wrap_create(const gx_string_type& arg1, const gx_string_type& arg2, int32_t arg3)
{
    GXGISPtr ret = GXGIS::create(arg1, arg2, (GIS_TYPE)arg3);
    return ret;
}
inline void GXGIS_wrap_create_map2_d(GXGISPtr self, const gx_string_type& arg1, double arg2, GXIPJPtr arg3, int32_t arg4)
{
    self->create_map2_d(arg1, arg2, arg3, (GIS_MAP2D)arg4);
}
inline void GXGIS_wrap_get_bpr_models_lst(GXGISPtr self, const gx_string_type& arg1, GXLSTPtr arg2)
{
    self->get_bpr_models_lst(arg1, arg2);
}
inline GXIPJPtr GXGIS_wrap_get_ipj(GXGISPtr self)
{
    GXIPJPtr ret = self->get_ipj();
    return ret;
}
inline void GXGIS_wrap_get_meta(GXGISPtr self, GXMETAPtr arg1)
{
    self->get_meta(arg1);
}
inline void GXGIS_wrap_get_range(GXGISPtr self, float_ref& arg1, float_ref& arg2, float_ref& arg3, float_ref& arg4, float_ref& arg5, float_ref& arg6)
{
    self->get_range(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline int32_t GXGIS_wrap_datamine_type(const gx_string_type& arg1)
{
    int32_t ret = GXGIS::datamine_type(arg1);
    return ret;
}
inline void GXGIS_wrap_get_file_name(GXGISPtr self, str_ref& arg1)
{
    self->get_file_name(arg1);
}
inline int32_t GXGIS_wrap_is_mi_map_file(const gx_string_type& arg1)
{
    int32_t ret = GXGIS::is_mi_map_file(arg1);
    return ret;
}
inline int32_t GXGIS_wrap_is_mi_raster_tab_file(const gx_string_type& arg1)
{
    int32_t ret = GXGIS::is_mi_raster_tab_file(arg1);
    return ret;
}
inline int32_t GXGIS_wrap_is_mi_rotated_raster_tab_file(const gx_string_type& arg1)
{
    int32_t ret = GXGIS::is_mi_rotated_raster_tab_file(arg1);
    return ret;
}
inline int32_t GXGIS_wrap_is_shp_file_3d(GXGISPtr self)
{
    int32_t ret = self->is_shp_file_3d();
    return ret;
}
inline int32_t GXGIS_wrap_is_shp_file_point(GXGISPtr self)
{
    int32_t ret = self->is_shp_file_point();
    return ret;
}
inline int32_t GXGIS_wrap_num_attribs(GXGISPtr self)
{
    int32_t ret = self->num_attribs();
    return ret;
}
inline int32_t GXGIS_wrap_num_shapes(GXGISPtr self)
{
    int32_t ret = self->num_shapes();
    return ret;
}
inline void GXGIS_wrap_scan_mi_raster_tab_file(const gx_string_type& arg1, str_ref& arg2, GXIPJPtr arg3)
{
    GXGIS::scan_mi_raster_tab_file(arg1, arg2, arg3);
}
inline void GXGIS_wrap_load_ascii(GXGISPtr self, GXWAPtr arg1)
{
    self->load_ascii(arg1);
}
inline void GXGIS_wrap_load_gdb(GXGISPtr self, GXDBPtr arg1)
{
    self->load_gdb(arg1);
}
inline void GXGIS_wrap_load_map(GXGISPtr self, GXMVIEWPtr arg1)
{
    self->load_map(arg1);
}
inline void GXGIS_wrap_load_map_ex(GXGISPtr self, GXMAPPtr arg1, const gx_string_type& arg2)
{
    self->load_map_ex(arg1, arg2);
}
inline void GXGIS_wrap_load_meta_groups_map(GXGISPtr self, GXMVIEWPtr arg1, GXMETAPtr arg2, int32_t arg3, const gx_string_type& arg4, const gx_string_type& arg5)
{
    self->load_meta_groups_map(arg1, arg2, arg3, arg4, arg5);
}
inline void GXGIS_wrap_load_ply(GXGISPtr self, GXPLYPtr arg1)
{
    self->load_ply(arg1);
}
inline void GXGIS_wrap_load_shapes_gdb(GXGISPtr self, GXDBPtr arg1)
{
    self->load_shapes_gdb(arg1);
}
inline void GXGIS_wrap_set_dm_wireframe_pt_file(GXGISPtr self, const gx_string_type& arg1)
{
    self->set_dm_wireframe_pt_file(arg1);
}
inline void GXGIS_wrap_set_ipj(GXGISPtr self, GXIPJPtr arg1)
{
    self->set_ipj(arg1);
}
inline void GXGIS_wrap_set_lst(GXGISPtr self, GXLSTPtr arg1)
{
    self->set_lst(arg1);
}
inline void GXGIS_wrap_set_meta(GXGISPtr self, GXMETAPtr arg1)
{
    self->set_meta(arg1);
}
inline void GXGIS_wrap_set_triangulation_object_index(GXGISPtr self, int32_t arg1)
{
    self->set_triangulation_object_index(arg1);
}

void gxPythonImportGXGIS()
{

    class_<GXGIS, GXGISPtr> pyClass("GXGIS",
                                    "\n.. parsed-literal::\n\n"
                                    "   \n"
                                    "   		The GIS class is used for the import, export,\n"
                                    "   		and interrogation of GIS Data stored in external formats,\n"
                                    "   		such as MapInfo® TAB files.\n"
                                    "   	\n\n"
                                    , no_init);

    pyClass.def("null", &GXGIS::null, "null() -> GXGIS\n\nA null (undefined) instance of :class:`geosoft.gxapi.GXGIS`\n\n:returns: A null :class:`geosoft.gxapi.GXGIS`\n:rtype: :class:`geosoft.gxapi.GXGIS`\n").staticmethod("null");
    pyClass.def("is_null", &GXGIS::is_null, "is_null() -> bool\n\nCheck if the instance of :class:`geosoft.gxapi.GXGIS is null (undefined)`\n\n:returns: True if this is a null instance of :class:`geosoft.gxapi.GXGIS`, False otherwise.\n:rtype: bool`\n");
    pyClass.def("_internal_handle", &GXGIS::_internal_handle);
    pyClass.def("create", &GXGIS_wrap_create,
                "create((str)arg1, (str)arg2, (int)arg3) -> GXGIS:\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a GIS Object\n\n"

                ":param arg1: data source (file)\n"
                ":type arg1: str\n"
                ":param arg2: data qualifying information if required.\n"
                ":type arg2: str\n"
                ":param arg3: \\ :ref:`GIS_TYPE`\\ \n"
                ":type arg3: int\n"
                ":returns: GIS Object\n"
                ":rtype: :class:`geosoft.gxapi.GXGIS`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("create");
    pyClass.def("create_map2_d", &GXGIS_wrap_create_map2_d,
                "create_map2_d((str)arg1, (float)arg2, (GXIPJ)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   \\ :func:`geosoft.gxapi.GXGIS.create_map2_d`\\    Create a new 2D map for GIS imports.\n\n"

                ":param arg1: Map name\n"
                ":type arg1: str\n"
                ":param arg2: Map scale (can be rDUMMY)\n"
                ":type arg2: float\n"
                ":param arg3: Projection (no orientation)\n"
                ":type arg3: :class:`geosoft.gxapi.GXIPJ`\n"
                ":param arg4: \\ :ref:`GIS_MAP2D`\\ \n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This function was created to minimize duplication in\n"
                "   					creation of new maps with 2D views.\n"
                "   				\n\n"
               );
    pyClass.def("get_bpr_models_lst", &GXGIS_wrap_get_bpr_models_lst,
                "get_bpr_models_lst((str)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get a LST of block models contained in a Gemcom BPR or BRP2 file\n\n"

                ":param arg1: BPR or BPR2 file\n"
                ":type arg1: str\n"
                ":param arg2: Returned LST of block models\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The Returned LST has items in the following format:\n"
                "   \n"
                "   					Name:  If there is only one sub-directory with models, then only\n"
                "   					the block model name \"Rock Type_5\" is required to ensure uniqueness.\n"
                "   					If there is more than one sub-directory, then the name is set\n"
                "   					to (.e.g.) \"[Standard]Rock Type_5\"\n"
                "   					Value: Sub-directory file path  \"Standard\\Rock Type_5.BLK\", (includes the extension).\n"
                "   \n"
                "   					The Gemcom BPR and BPR2 files keep their block models in one\n"
                "   					or more sub-directories, identified in the \\ `*`\\ .CAT file located\n"
                "   					beside the input BPR or BPR2.\n"
                "   				\n\n"
               );
    pyClass.def("get_ipj", &GXGIS_wrap_get_ipj,
                "get_ipj() -> GXIPJ:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the GIS IPJ\n\n"

                ":returns: IPJ handle\n"
                "          						NULL if error\n"
                ":rtype: :class:`geosoft.gxapi.GXIPJ`\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					This is your copy, you must destroy it.\n"
                "   					If the GIS does not have an IPJ, an IPJ with\n"
                "   					no warp and UNKNOWN projection is returned.\n"
                "   				\n\n"
               );
    pyClass.def("get_meta", &GXGIS_wrap_get_meta,
                "get_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the GIS META\n\n"

                ":param arg1: Meta object to store GIS meta information\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("get_range", &GXGIS_wrap_get_range,
                "get_range((float_ref)arg1, (float_ref)arg2, (float_ref)arg3, (float_ref)arg4, (float_ref)arg5, (float_ref)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the range of data in the GIS\n\n"

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

                "\n.. versionadded:: 5.0.0\n\n"
               );
    pyClass.def("datamine_type", &GXGIS_wrap_datamine_type,
                "datamine_type((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns the type of a Datamine file.\n\n"

                ":param arg1: Name of input datamine file\n"
                ":type arg1: str\n"
                ":returns: Datamine file types - bitwise AND of types.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Terminates if file is not a Datamine file.\n"
                "   					A datamine file can contain fields from a multitude\n"
                "   					of types, so use \\ :func:`geosoft.gxapi.GXMATH.and`\\  or \\ :func:`geosoft.gxapi.GXMATH.or`\\  to determine if\n"
                "   					the file contains the required data.\n"
                "   				\n\n"
               ).staticmethod("datamine_type");
    pyClass.def("get_file_name", &GXGIS_wrap_get_file_name,
                "get_file_name((str_ref)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the file name\n\n"

                ":param arg1: returned file name\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               );
    pyClass.def("is_mi_map_file", &GXGIS_wrap_is_mi_map_file,
                "is_mi_map_file((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns TRUE if file is a MapInfo MAP file.\n\n"

                ":param arg1: Name of input map file\n"
                ":type arg1: str\n"
                ":returns: 0 if not a MapInfo MAP file\n"
                "          						1 if it is.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					It is important not to overwrite a MapInfo MAP file\n"
                "   					with a GEOSOFT one. Use this function to test the MAP\n"
                "   					file (looks at the first few bytes).\n"
                "   				\n\n"
               ).staticmethod("is_mi_map_file");
    pyClass.def("is_mi_raster_tab_file", &GXGIS_wrap_is_mi_raster_tab_file,
                "is_mi_raster_tab_file((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns TRUE if file is a MapInfo Raster TAB file.\n\n"

                ":param arg1: Name of input tab file\n"
                ":type arg1: str\n"
                ":returns: 0 if not a MapInfo Raster TAB file\n"
                "          						1 if it is.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"
               ).staticmethod("is_mi_raster_tab_file");
    pyClass.def("is_mi_rotated_raster_tab_file", &GXGIS_wrap_is_mi_rotated_raster_tab_file,
                "is_mi_rotated_raster_tab_file((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns TRUE if file is a rotated MapInfo Raster TAB file.\n\n"

                ":param arg1: Name of input tab file\n"
                ":type arg1: str\n"
                ":returns: 0 if not a rotated MapInfo Raster TAB file\n"
                "          						1 if it is (see conditions below).\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.4.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Returns 1 if:\n"
                "   \n"
                "   					a) This is a MapInfo RASTER file\n"
                "   					b) A three-point warp is defined.\n"
                "   					c) The warp requires a rotation in order to exactly map\n"
                "   					the input and output warp points. The rotation must\n"
                "   					be at least 1.e-6 radians.\n"
                "   \n"
                "   					This function will register an error (and return 0)\n"
                "   					if problems are encountered opening or reading the TAB file.\n"
                "   				\n\n"
               ).staticmethod("is_mi_rotated_raster_tab_file");
    pyClass.def("is_shp_file_3d", &GXGIS_wrap_is_shp_file_3d,
                "is_shp_file_3d() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns TRUE if an ArcView SHP file is type POINTZ, ARCZ, POLYGONZ or MULTIPOINTZ\n\n"

                ":returns: 0 if the SHP file is 2D\n"
                "          						1 if the SHP file is of type POINTZ, ARCZ, POLYGONZ or MULTIPOINTZ\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					SHP files come in 2D and 3D forms.\n"
                "   					Fails if not GIS_TYPE_ARCVIEW.\n"
                "   				\n\n"
               );
    pyClass.def("is_shp_file_point", &GXGIS_wrap_is_shp_file_point,
                "is_shp_file_point() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Returns TRUE if an ArcView SHP file is type POINT or POINTZ\n\n"

                ":returns: 0 if the SHP file is not points\n"
                "          						if the SHP file is of type POINT or POINTZ\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Fails if not GIS_TYPE_ARCVIEW.\n\n"
               );
    pyClass.def("num_attribs", &GXGIS_wrap_num_attribs,
                "num_attribs() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   The number of attribute fields in the GIS dataset\n\n"

                ":returns: The number of attribute fields\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               );
    pyClass.def("num_shapes", &GXGIS_wrap_num_shapes,
                "num_shapes() -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   The number of shape entities in the GIS dataset\n\n"

                ":returns: The number of shape entities\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               );
    pyClass.def("scan_mi_raster_tab_file", &GXGIS_wrap_scan_mi_raster_tab_file,
                "scan_mi_raster_tab_file((str)arg1, (str_ref)arg2, (GXIPJ)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Scan and set up a MapInf RASTER.\n\n"

                ":param arg1: Name of input file\n"
                ":type arg1: str\n"
                ":param arg2: Name of Raster file (an IMG DAT)\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg3: Projection\n"
                ":type arg3: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This will create a GI file for the raster image.\n\n"
               ).staticmethod("scan_mi_raster_tab_file");
    pyClass.def("load_ascii", &GXGIS_wrap_load_ascii,
                "load_ascii((GXWA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save GIS attribute table information (string fields) into a WA.\n\n"

                ":param arg1: WA object\n"
                ":type arg1: :class:`geosoft.gxapi.GXWA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					All string fields (excluding X/Y and numerical fields) will be saved into the WA columns.\n"
                "   \n"
                "   					e field names are saved in the first line, followed by a blank line.\n"
                "   					e field columns are seperated by a tab (delimited character).\n"
                "   				\n\n"
               );
    pyClass.def("load_gdb", &GXGIS_wrap_load_gdb,
                "load_gdb((GXDB)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load GIS table information into a GDB.\n\n"

                ":param arg1: database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					All fields of the database will be loaded into the group.\n"
                "   \n"
                "   					Channels will use the same name (or a allowable alias) as\n"
                "   					the GIS field name.\n"
                "   \n"
                "   					If a channel does not exist, it will be created based on the\n"
                "   					characteristics of the GIS field.\n"
                "   \n"
                "   					If a channel exists, it will be used as-is.\n"
                "   				\n\n"
               );
    pyClass.def("load_map", &GXGIS_wrap_load_map,
                "load_map((GXMVIEW)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load GIS table drawing into a MAP.\n\n"

                ":param arg1: view in which to place GIS drawing.\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.0.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The GIS drawing will be drawin in the current group.\n\n"
               );
    pyClass.def("load_map_ex", &GXGIS_wrap_load_map_ex,
                "load_map_ex((GXMAP)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load GIS table drawing into a MAP.\n\n"

                ":param arg1: Map handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: Name of existing data view\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The GIS drawing will be drawin in the current group.\n\n"
               );
    pyClass.def("load_meta_groups_map", &GXGIS_wrap_load_meta_groups_map,
                "load_meta_groups_map((GXMVIEW)arg1, (GXMETA)arg2, (int)arg3, (str)arg4, (str)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load GIS table drawing into a MAP.\n\n"

                ":param arg1: view in which to place GIS drawing.\n"
                ":type arg1: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg2: META\n"
                ":type arg2: :class:`geosoft.gxapi.GXMETA`\n"
                ":param arg3: Class\n"
                ":type arg3: int\n"
                ":param arg4: Group Name prefix\n"
                ":type arg4: str\n"
                ":param arg5: Name field (Empty to use ID of entity)\n"
                ":type arg5: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.8\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					The GIS drawing will be drawn in the current group.\n"
                "   					A group will be created for every entity and data items\n"
                "   					containing an entity's field will be added to the Meta\n"
                "   					information of every group into the class specified.\n"
                "   					Note that the map may grow very large for big datasets.\n"
                "   				\n\n"
               );
    pyClass.def("load_ply", &GXGIS_wrap_load_ply,
                "load_ply((GXPLY)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load GIS table drawing into a Multi-Polygon object.\n\n"

                ":param arg1: Polygon object in which to place GIS shapes.\n"
                ":type arg1: :class:`geosoft.gxapi.GXPLY`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 5.1.6\n\n"
               );
    pyClass.def("load_shapes_gdb", &GXGIS_wrap_load_shapes_gdb,
                "load_shapes_gdb((GXDB)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Load GIS shapes table information into separate lines in a GDB.\n\n"

                ":param arg1: database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					All fields of the database will be loaded into the group.\n"
                "   \n"
                "   					Channels will use the same name (or a allowable alias) as\n"
                "   					the GIS field name.\n"
                "   \n"
                "   					If a channel does not exist, it will be created based on the\n"
                "   					characteristics of the GIS field.\n"
                "   \n"
                "   					If a channel exists, it will be used as-is.\n"
                "   \n"
                "   					The shape ID will be used as the line numbers.\n"
                "   				\n\n"
               );
    pyClass.def("set_dm_wireframe_pt_file", &GXGIS_wrap_set_dm_wireframe_pt_file,
                "set_dm_wireframe_pt_file((str)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Specify the wireframe point file corresponding to the input file.\n\n"

                ":param arg1: Name of the wireframe point file\n"
                ":type arg1: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					Datamine wireframe models are specified by pairs of files,\n"
                "   					the first is the triangle node file, and the second gives\n"
                "   					the XYZ locations of the node points. This\n"
                "   					function allows you to specify the latter when reading the\n"
                "   					first, so that the full model can be decoded.\n"
                "   				\n\n"
               );
    pyClass.def("set_ipj", &GXGIS_wrap_set_ipj,
                "set_ipj((GXIPJ)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save the IPJ back to GIS file\n\n"

                ":param arg1: IPJ to save\n"
                ":type arg1: :class:`geosoft.gxapi.GXIPJ`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("set_lst", &GXGIS_wrap_set_lst,
                "set_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save a LST of items inside the GIS object for special use.\n\n"

                ":param arg1: LST object to save to GIS LST.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \n"
                "   					If the GIS LST object already exists, it is destroyed and\n"
                "   					recreated to match the size of the input LST, before the\n"
                "   					input LST is copied to it.\n"
                "   				\n\n"
               );
    pyClass.def("set_meta", &GXGIS_wrap_set_meta,
                "set_meta((GXMETA)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Save the META back to GIS\n\n"

                ":param arg1: META object to save to GIS meta\n"
                ":type arg1: :class:`geosoft.gxapi.GXMETA`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.0.0\n\n"
               );
    pyClass.def("set_triangulation_object_index", &GXGIS_wrap_set_triangulation_object_index,
                "set_triangulation_object_index((int)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the triangulation object index (Micromine)\n\n"

                ":param arg1: Triangulation object index\n"
                ":type arg1: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               );

    scope().attr("GIS_MAP2D_PLAN") = (int32_t)0;
    scope().attr("GIS_MAP2D_EWSECTION") = (int32_t)1;
    scope().attr("GIS_MAP2D_NSSECTION") = (int32_t)2;
    scope().attr("GIS_TYPE_MAPINFO") = (int32_t)1;
    scope().attr("GIS_TYPE_ARCVIEW") = (int32_t)2;
    scope().attr("GIS_TYPE_DGN") = (int32_t)3;
    scope().attr("GIS_TYPE_SURPAC") = (int32_t)4;
    scope().attr("GIS_TYPE_DATAMINE") = (int32_t)5;
    scope().attr("GIS_TYPE_GEMCOM") = (int32_t)6;
    scope().attr("GIS_TYPE_MICROMINE") = (int32_t)7;
    scope().attr("GIS_TYPE_MINESIGHT") = (int32_t)8;

}
