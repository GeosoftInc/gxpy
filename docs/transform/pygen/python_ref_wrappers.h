#pragma once

typedef std::vector<double> float_list;
typedef std::vector<int32_t> int_list;

template<typename T>
struct by_ref_value
{
public:
    inline by_ref_value();
    inline by_ref_value(const T& value) : value_(value) { }
    inline by_ref_value(const by_ref_value<T> & other)
    {
        value_ = other.value_;
    }

    operator const T&() const
    {
        return value_;
    }
    operator T&()
    {
        return value_;
    }

    T get_value()
    {
        return value_;
    }
    void set_value(const T& value)
    {
        value_ = value;
    }

private:
    T value_;
};

typedef by_ref_value<double> float_ref;
typedef by_ref_value<int32_t> int_ref;
typedef by_ref_value<bool> bool_ref;
typedef by_ref_value<std::wstring> str_ref;

typedef by_ref_value<DATE_FORMAT> DATE_FORMAT_ref;
typedef by_ref_value<GEO_STRING_SIZE> GEO_STRING_SIZE_ref;
typedef by_ref_value<GEO_VAR> GEO_VAR_ref;
typedef by_ref_value<GS_FORMATS> GS_FORMATS_ref;
typedef by_ref_value<GS_TYPES> GS_TYPES_ref;
typedef by_ref_value<TIME_FORMAT> TIME_FORMAT_ref;




typedef by_ref_value<GEO3DV_OPEN> GEO3DV_OPEN_ref;


typedef by_ref_value<ACQUIRE_SEL> ACQUIRE_SEL_ref;


typedef by_ref_value<ARC_SELTBL_TYPE> ARC_SELTBL_TYPE_ref;




typedef by_ref_value<ARCMAP_LOAD_FLAGS> ARCMAP_LOAD_FLAGS_ref;






typedef by_ref_value<CHIMERA_PLOT> CHIMERA_PLOT_ref;


typedef by_ref_value<COM_BAUD> COM_BAUD_ref;
typedef by_ref_value<COM_DATASIZE> COM_DATASIZE_ref;
typedef by_ref_value<COM_FLOWCONTROL> COM_FLOWCONTROL_ref;
typedef by_ref_value<COM_PARITY> COM_PARITY_ref;
typedef by_ref_value<COM_STOPBITS> COM_STOPBITS_ref;


typedef by_ref_value<CSYMB_COLOR> CSYMB_COLOR_ref;


typedef by_ref_value<DGW_OBJECT> DGW_OBJECT_ref;


typedef by_ref_value<DH_COMP_CHOICE> DH_COMP_CHOICE_ref;
typedef by_ref_value<DH_COMPSTDB_HOLSEL> DH_COMPSTDB_HOLSEL_ref;
typedef by_ref_value<DH_COMPSTDB_INTSEL> DH_COMPSTDB_INTSEL_ref;
typedef by_ref_value<DH_DATA> DH_DATA_ref;
typedef by_ref_value<DH_EXP> DH_EXP_ref;
typedef by_ref_value<DH_HOLES> DH_HOLES_ref;
typedef by_ref_value<DH_MASK> DH_MASK_ref;
typedef by_ref_value<DH_PLOT> DH_PLOT_ref;
typedef by_ref_value<DH_SECT_PAGE> DH_SECT_PAGE_ref;
typedef by_ref_value<DH_SURFACE> DH_SURFACE_ref;
typedef by_ref_value<DIP_CONVENTION> DIP_CONVENTION_ref;




typedef by_ref_value<DOCU_OPEN> DOCU_OPEN_ref;


typedef by_ref_value<DB_DUP> DB_DUP_ref;
typedef by_ref_value<DB_DUPEDIT> DB_DUPEDIT_ref;
typedef by_ref_value<DU_CHANNELS> DU_CHANNELS_ref;
typedef by_ref_value<DU_EXPORT> DU_EXPORT_ref;
typedef by_ref_value<DU_FILL> DU_FILL_ref;
typedef by_ref_value<DU_IMPORT> DU_IMPORT_ref;
typedef by_ref_value<DU_INTERP> DU_INTERP_ref;
typedef by_ref_value<DU_INTERP_EDGE> DU_INTERP_EDGE_ref;
typedef by_ref_value<DU_LAB_TYPE> DU_LAB_TYPE_ref;
typedef by_ref_value<DU_LEVEL> DU_LEVEL_ref;
typedef by_ref_value<DU_LINEOUT> DU_LINEOUT_ref;
typedef by_ref_value<DU_FEATURE_TYPE_OUTPUT> DU_FEATURE_TYPE_OUTPUT_ref;
typedef by_ref_value<DU_GEODATABASE_EXPORT_TYPE> DU_GEODATABASE_EXPORT_TYPE_ref;
typedef by_ref_value<DU_LINES> DU_LINES_ref;
typedef by_ref_value<DU_LOADLTB> DU_LOADLTB_ref;
typedef by_ref_value<DU_LOOKUP> DU_LOOKUP_ref;
typedef by_ref_value<DU_MASK> DU_MASK_ref;
typedef by_ref_value<DU_MERGE> DU_MERGE_ref;
typedef by_ref_value<DU_MODFID> DU_MODFID_ref;
typedef by_ref_value<DU_MOVE> DU_MOVE_ref;
typedef by_ref_value<DU_REFID> DU_REFID_ref;
typedef by_ref_value<DU_SORT> DU_SORT_ref;
typedef by_ref_value<DU_SPLITLINE> DU_SPLITLINE_ref;
typedef by_ref_value<DU_STORAGE> DU_STORAGE_ref;
typedef by_ref_value<QC_PLAN_TYPE> QC_PLAN_TYPE_ref;
typedef by_ref_value<DU_DISTANCE_CHANNEL_TYPE> DU_DISTANCE_CHANNEL_TYPE_ref;
typedef by_ref_value<DU_DIRECTGRID_METHOD> DU_DIRECTGRID_METHOD_ref;




typedef by_ref_value<EDB_PATH> EDB_PATH_ref;
typedef by_ref_value<EDB_PROF> EDB_PROF_ref;
typedef by_ref_value<EDB_PROFILE_SCALE> EDB_PROFILE_SCALE_ref;
typedef by_ref_value<EDB_REMOVE> EDB_REMOVE_ref;
typedef by_ref_value<EDB_UNLOAD> EDB_UNLOAD_ref;
typedef by_ref_value<EDB_WINDOW_POSITION> EDB_WINDOW_POSITION_ref;
typedef by_ref_value<EDB_WINDOW_STATE> EDB_WINDOW_STATE_ref;
typedef by_ref_value<EDB_YAXIS_DIRECTION> EDB_YAXIS_DIRECTION_ref;


typedef by_ref_value<EDOC_PATH> EDOC_PATH_ref;
typedef by_ref_value<EDOC_TYPE> EDOC_TYPE_ref;
typedef by_ref_value<EDOC_UNLOAD> EDOC_UNLOAD_ref;
typedef by_ref_value<EDOC_WINDOW_POSITION> EDOC_WINDOW_POSITION_ref;
typedef by_ref_value<EDOC_WINDOW_STATE> EDOC_WINDOW_STATE_ref;
typedef by_ref_value<GMS3D_MODELTYPE> GMS3D_MODELTYPE_ref;
typedef by_ref_value<GMS2D_MODELTYPE> GMS2D_MODELTYPE_ref;


typedef by_ref_value<EMAP_FONT> EMAP_FONT_ref;
typedef by_ref_value<EMAP_PATH> EMAP_PATH_ref;
typedef by_ref_value<EMAP_REDRAW> EMAP_REDRAW_ref;
typedef by_ref_value<EMAP_REMOVE> EMAP_REMOVE_ref;
typedef by_ref_value<EMAP_TRACK> EMAP_TRACK_ref;
typedef by_ref_value<EMAP_VIEWPORT> EMAP_VIEWPORT_ref;
typedef by_ref_value<EMAP_WINDOW_POSITION> EMAP_WINDOW_POSITION_ref;
typedef by_ref_value<EMAP_WINDOW_STATE> EMAP_WINDOW_STATE_ref;
typedef by_ref_value<LAYOUT_VIEW_UNITS> LAYOUT_VIEW_UNITS_ref;


typedef by_ref_value<EMAPTEMPLATE_PATH> EMAPTEMPLATE_PATH_ref;
typedef by_ref_value<EMAPTEMPLATE_TRACK> EMAPTEMPLATE_TRACK_ref;
typedef by_ref_value<EMAPTEMPLATE_WINDOW_POSITION> EMAPTEMPLATE_WINDOW_POSITION_ref;
typedef by_ref_value<EMAPTEMPLATE_WINDOW_STATE> EMAPTEMPLATE_WINDOW_STATE_ref;


typedef by_ref_value<EUL3_RESULT> EUL3_RESULT_ref;




typedef by_ref_value<FFT_DETREND> FFT_DETREND_ref;


typedef by_ref_value<FFT2_PG> FFT2_PG_ref;




typedef by_ref_value<GD_STATUS> GD_STATUS_ref;






typedef by_ref_value<EM_ERR> EM_ERR_ref;
typedef by_ref_value<EM_INV> EM_INV_ref;
typedef by_ref_value<EMPLATE_DOMAIN> EMPLATE_DOMAIN_ref;
typedef by_ref_value<EMPLATE_TX> EMPLATE_TX_ref;
typedef by_ref_value<GU_DAARC500_DATATYPE> GU_DAARC500_DATATYPE_ref;
typedef by_ref_value<PEAKEULER_XY> PEAKEULER_XY_ref;


typedef by_ref_value<AOI_RETURN_STATE> AOI_RETURN_STATE_ref;
typedef by_ref_value<COORDSYS_MODE> COORDSYS_MODE_ref;
typedef by_ref_value<DAT_TYPE> DAT_TYPE_ref;
typedef by_ref_value<FILE_FILTER> FILE_FILTER_ref;
typedef by_ref_value<FILE_FORM> FILE_FORM_ref;
typedef by_ref_value<GS_DIRECTORY> GS_DIRECTORY_ref;
typedef by_ref_value<IMPCH_TYPE> IMPCH_TYPE_ref;
typedef by_ref_value<WINDOW_STATE> WINDOW_STATE_ref;
typedef by_ref_value<XTOOL_ALIGN> XTOOL_ALIGN_ref;
typedef by_ref_value<XTOOL_DOCK> XTOOL_DOCK_ref;










typedef by_ref_value<IP_ARRAY> IP_ARRAY_ref;
typedef by_ref_value<IP_CHANNELS> IP_CHANNELS_ref;
typedef by_ref_value<IP_DOMAIN> IP_DOMAIN_ref;
typedef by_ref_value<IP_DUPLICATE> IP_DUPLICATE_ref;
typedef by_ref_value<IP_FILTER> IP_FILTER_ref;
typedef by_ref_value<IP_I2XIMPMODE> IP_I2XIMPMODE_ref;
typedef by_ref_value<IP_I2XINV> IP_I2XINV_ref;
typedef by_ref_value<IP_LINES> IP_LINES_ref;
typedef by_ref_value<IP_PLOT> IP_PLOT_ref;
typedef by_ref_value<IP_STACK_TYPE> IP_STACK_TYPE_ref;
typedef by_ref_value<IP_STNSCALE> IP_STNSCALE_ref;
typedef by_ref_value<IP_SYS> IP_SYS_ref;
typedef by_ref_value<IP_UBC_CONTROL> IP_UBC_CONTROL_ref;
typedef by_ref_value<IP_PLDP_CONV> IP_PLDP_CONV_ref;












typedef by_ref_value<MVG_DRAW> MVG_DRAW_ref;
typedef by_ref_value<MVG_GRID> MVG_GRID_ref;
typedef by_ref_value<MVG_LABEL_BOUND> MVG_LABEL_BOUND_ref;
typedef by_ref_value<MVG_LABEL_JUST> MVG_LABEL_JUST_ref;
typedef by_ref_value<MVG_LABEL_ORIENT> MVG_LABEL_ORIENT_ref;
typedef by_ref_value<MVG_SCALE> MVG_SCALE_ref;
typedef by_ref_value<MVG_WRAP> MVG_WRAP_ref;






typedef by_ref_value<BLAKEY_TEST> BLAKEY_TEST_ref;
typedef by_ref_value<PGU_CORR> PGU_CORR_ref;
typedef by_ref_value<PGU_DIRECTGRID> PGU_DIRECTGRID_ref;
typedef by_ref_value<PGU_DIRECTION> PGU_DIRECTION_ref;
typedef by_ref_value<PGU_TRANS> PGU_TRANS_ref;
typedef by_ref_value<PGU_INTERP_ORDER> PGU_INTERP_ORDER_ref;




typedef by_ref_value<COMMAND_ENV> COMMAND_ENV_ref;
typedef by_ref_value<TOOL_TYPE> TOOL_TYPE_ref;
typedef by_ref_value<PROJ_DISPLAY> PROJ_DISPLAY_ref;




typedef by_ref_value<SEMPLOT_EXPORT> SEMPLOT_EXPORT_ref;
typedef by_ref_value<SEMPLOT_EXT> SEMPLOT_EXT_ref;
typedef by_ref_value<SEMPLOT_PLOT> SEMPLOT_PLOT_ref;


typedef by_ref_value<SHP_GEOM_TYPE> SHP_GEOM_TYPE_ref;


typedef by_ref_value<MFCSQL_DRIVER> MFCSQL_DRIVER_ref;


typedef by_ref_value<STK_AXIS> STK_AXIS_ref;
typedef by_ref_value<STK_FLAG> STK_FLAG_ref;
typedef by_ref_value<STK_GRID> STK_GRID_ref;




typedef by_ref_value<TC_OPT> TC_OPT_ref;
typedef by_ref_value<TC_SURVEYTYPE> TC_SURVEYTYPE_ref;
typedef by_ref_value<GG_ELEMENT> GG_ELEMENT_ref;






typedef by_ref_value<TRND_NODE> TRND_NODE_ref;


typedef by_ref_value<UTF8> UTF8_ref;


typedef by_ref_value<VAU_PRUNE> VAU_PRUNE_ref;




typedef by_ref_value<QC_CRITERION> QC_CRITERION_ref;
typedef by_ref_value<TEM_ARRAY> TEM_ARRAY_ref;
typedef by_ref_value<VV_DUP> VV_DUP_ref;
typedef by_ref_value<VV_XYDUP> VV_XYDUP_ref;
typedef by_ref_value<VVU_CASE> VVU_CASE_ref;
typedef by_ref_value<VVU_CLIP> VVU_CLIP_ref;
typedef by_ref_value<VVU_DUMMYREPEAT> VVU_DUMMYREPEAT_ref;
typedef by_ref_value<VVU_INTERP> VVU_INTERP_ref;
typedef by_ref_value<VVU_INTERP_EDGE> VVU_INTERP_EDGE_ref;
typedef by_ref_value<VVU_LINE> VVU_LINE_ref;
typedef by_ref_value<VVU_MASK> VVU_MASK_ref;
typedef by_ref_value<VVU_MATCH> VVU_MATCH_ref;
typedef by_ref_value<VVU_MODE> VVU_MODE_ref;
typedef by_ref_value<VVU_OFFSET> VVU_OFFSET_ref;
typedef by_ref_value<VVU_PRUNE> VVU_PRUNE_ref;
typedef by_ref_value<VVU_SPL> VVU_SPL_ref;
typedef by_ref_value<VVU_SRCHREPL_CASE> VVU_SRCHREPL_CASE_ref;


typedef by_ref_value<AGG_LAYER_ZONE> AGG_LAYER_ZONE_ref;
typedef by_ref_value<AGG_MODEL> AGG_MODEL_ref;
typedef by_ref_value<AGG_RENDER> AGG_RENDER_ref;


typedef by_ref_value<BF_BYTEORDER> BF_BYTEORDER_ref;
typedef by_ref_value<BF_CLOSE> BF_CLOSE_ref;
typedef by_ref_value<BF_ENCODE> BF_ENCODE_ref;
typedef by_ref_value<BF_OPEN_MODE> BF_OPEN_MODE_ref;
typedef by_ref_value<BF_SEEK> BF_SEEK_ref;


typedef by_ref_value<DAT_FILE> DAT_FILE_ref;
typedef by_ref_value<DAT_FILE_FORM> DAT_FILE_FORM_ref;
typedef by_ref_value<DAT_XGD> DAT_XGD_ref;




typedef by_ref_value<GIS_DMTYPE> GIS_DMTYPE_ref;


typedef by_ref_value<DB_CATEGORY_BLOB> DB_CATEGORY_BLOB_ref;
typedef by_ref_value<DB_CATEGORY_CHAN> DB_CATEGORY_CHAN_ref;
typedef by_ref_value<DB_CATEGORY_LINE> DB_CATEGORY_LINE_ref;
typedef by_ref_value<DB_CATEGORY_USER> DB_CATEGORY_USER_ref;
typedef by_ref_value<DB_CHAN_FORMAT> DB_CHAN_FORMAT_ref;
typedef by_ref_value<DB_CHAN_PROTECTION> DB_CHAN_PROTECTION_ref;
typedef by_ref_value<DB_CHAN_SYMBOL> DB_CHAN_SYMBOL_ref;
typedef by_ref_value<DB_COMP> DB_COMP_ref;
typedef by_ref_value<DB_COORDPAIR> DB_COORDPAIR_ref;
typedef by_ref_value<DB_INFO> DB_INFO_ref;
typedef by_ref_value<DB_LINE_LABEL_FORMAT> DB_LINE_LABEL_FORMAT_ref;
typedef by_ref_value<DB_LINE_SELECT> DB_LINE_SELECT_ref;
typedef by_ref_value<DB_LINE_TYPE> DB_LINE_TYPE_ref;
typedef by_ref_value<DB_LOCK> DB_LOCK_ref;
typedef by_ref_value<DB_NAME> DB_NAME_ref;
typedef by_ref_value<DB_OWN> DB_OWN_ref;
typedef by_ref_value<DB_SYMB_TYPE> DB_SYMB_TYPE_ref;
typedef by_ref_value<DB_WAIT> DB_WAIT_ref;
typedef by_ref_value<DB_ARRAY_BASETYPE> DB_ARRAY_BASETYPE_ref;






typedef by_ref_value<DSEL_PICTURE_QUALITY> DSEL_PICTURE_QUALITY_ref;






typedef by_ref_value<GEOSTRING_OPEN> GEOSTRING_OPEN_ref;
typedef by_ref_value<SECTION_ORIENTATION> SECTION_ORIENTATION_ref;


typedef by_ref_value<GIS_MAP2D> GIS_MAP2D_ref;
typedef by_ref_value<GIS_TYPE> GIS_TYPE_ref;






typedef by_ref_value<IMG_FILE> IMG_FILE_ref;
typedef by_ref_value<IMG_QUERY> IMG_QUERY_ref;
typedef by_ref_value<IMG_RELOCATE> IMG_RELOCATE_ref;


typedef by_ref_value<IMU_BOOL_OLAP> IMU_BOOL_OLAP_ref;
typedef by_ref_value<IMU_BOOL_OPT> IMU_BOOL_OPT_ref;
typedef by_ref_value<IMU_BOOL_SIZING> IMU_BOOL_SIZING_ref;
typedef by_ref_value<IMU_DOUBLE_CRC_BITS> IMU_DOUBLE_CRC_BITS_ref;
typedef by_ref_value<IMU_EXPAND_SHAPE> IMU_EXPAND_SHAPE_ref;
typedef by_ref_value<IMU_FILL_ROLLOPT> IMU_FILL_ROLLOPT_ref;
typedef by_ref_value<IMU_FILT_DUMMY> IMU_FILT_DUMMY_ref;
typedef by_ref_value<IMU_FILT_FILE> IMU_FILT_FILE_ref;
typedef by_ref_value<IMU_FILT_HZDRV> IMU_FILT_HZDRV_ref;
typedef by_ref_value<IMU_FLOAT_CRC_BITS> IMU_FLOAT_CRC_BITS_ref;
typedef by_ref_value<IMU_MASK> IMU_MASK_ref;
typedef by_ref_value<IMU_STAT_FORCED> IMU_STAT_FORCED_ref;
typedef by_ref_value<IMU_TRANS> IMU_TRANS_ref;
typedef by_ref_value<IMU_TREND> IMU_TREND_ref;
typedef by_ref_value<IMU_WIND_COORD> IMU_WIND_COORD_ref;
typedef by_ref_value<IMU_WIND_DUMMIES> IMU_WIND_DUMMIES_ref;
typedef by_ref_value<IMU_XYZ_INDEX> IMU_XYZ_INDEX_ref;
typedef by_ref_value<IMU_XYZ_LABEL> IMU_XYZ_LABEL_ref;


typedef by_ref_value<IPJ_3D_FLAG> IPJ_3D_FLAG_ref;
typedef by_ref_value<IPJ_3D_ROTATE> IPJ_3D_ROTATE_ref;
typedef by_ref_value<IPJ_CSP> IPJ_CSP_ref;
typedef by_ref_value<IPJ_NAME> IPJ_NAME_ref;
typedef by_ref_value<IPJ_ORIENT> IPJ_ORIENT_ref;
typedef by_ref_value<IPJ_PARM_LST> IPJ_PARM_LST_ref;
typedef by_ref_value<IPJ_TYPE> IPJ_TYPE_ref;
typedef by_ref_value<IPJ_UNIT> IPJ_UNIT_ref;
typedef by_ref_value<IPJ_WARP> IPJ_WARP_ref;


typedef by_ref_value<ITR_COLOR_MODEL> ITR_COLOR_MODEL_ref;
typedef by_ref_value<ITR_POWER> ITR_POWER_ref;
typedef by_ref_value<ITR_ZONE> ITR_ZONE_ref;
typedef by_ref_value<ITR_ZONE_MODEL> ITR_ZONE_MODEL_ref;


typedef by_ref_value<LAYOUT_CONSTR> LAYOUT_CONSTR_ref;






typedef by_ref_value<LST_ITEM> LST_ITEM_ref;


typedef by_ref_value<LTB_CASE> LTB_CASE_ref;
typedef by_ref_value<LTB_CONLST> LTB_CONLST_ref;
typedef by_ref_value<LTB_DELIM> LTB_DELIM_ref;
typedef by_ref_value<LTB_TYPE> LTB_TYPE_ref;


typedef by_ref_value<DUPMAP> DUPMAP_ref;
typedef by_ref_value<MAP_EXPORT_BITS> MAP_EXPORT_BITS_ref;
typedef by_ref_value<MAP_EXPORT_METHOD> MAP_EXPORT_METHOD_ref;
typedef by_ref_value<MAP_LIST_MODE> MAP_LIST_MODE_ref;
typedef by_ref_value<MAP_OPEN> MAP_OPEN_ref;




typedef by_ref_value<MAPTEMPLATE_OPEN> MAPTEMPLATE_OPEN_ref;




typedef by_ref_value<META_CORE_ATTRIB> META_CORE_ATTRIB_ref;
typedef by_ref_value<META_CORE_CLASS> META_CORE_CLASS_ref;
typedef by_ref_value<META_CORE_TYPE> META_CORE_TYPE_ref;


typedef by_ref_value<MAKER> MAKER_ref;
typedef by_ref_value<MVIEW_CLIP> MVIEW_CLIP_ref;
typedef by_ref_value<MVIEW_COLOR> MVIEW_COLOR_ref;
typedef by_ref_value<MVIEW_CYLINDER3D> MVIEW_CYLINDER3D_ref;
typedef by_ref_value<MVIEW_DRAW> MVIEW_DRAW_ref;
typedef by_ref_value<MVIEW_DRAWOBJ3D_ENTITY> MVIEW_DRAWOBJ3D_ENTITY_ref;
typedef by_ref_value<MVIEW_DRAWOBJ3D_MODE> MVIEW_DRAWOBJ3D_MODE_ref;
typedef by_ref_value<MVIEW_EXTENT> MVIEW_EXTENT_ref;
typedef by_ref_value<MVIEW_FIT> MVIEW_FIT_ref;
typedef by_ref_value<MVIEW_FONT_WEIGHT> MVIEW_FONT_WEIGHT_ref;
typedef by_ref_value<MVIEW_GRID> MVIEW_GRID_ref;
typedef by_ref_value<MVIEW_GROUP> MVIEW_GROUP_ref;
typedef by_ref_value<MVIEW_GROUP_LIST> MVIEW_GROUP_LIST_ref;
typedef by_ref_value<MVIEW_HIDE> MVIEW_HIDE_ref;
typedef by_ref_value<MVIEW_IS> MVIEW_IS_ref;
typedef by_ref_value<MVIEW_LABEL_BOUND> MVIEW_LABEL_BOUND_ref;
typedef by_ref_value<MVIEW_LABEL_JUST> MVIEW_LABEL_JUST_ref;
typedef by_ref_value<MVIEW_LABEL_ORIENT> MVIEW_LABEL_ORIENT_ref;
typedef by_ref_value<MVIEW_OPEN> MVIEW_OPEN_ref;
typedef by_ref_value<MVIEW_PJ> MVIEW_PJ_ref;
typedef by_ref_value<MVIEW_RELOCATE> MVIEW_RELOCATE_ref;
typedef by_ref_value<MVIEW_SMOOTH> MVIEW_SMOOTH_ref;
typedef by_ref_value<MVIEW_TILE> MVIEW_TILE_ref;
typedef by_ref_value<MVIEW_UNIT> MVIEW_UNIT_ref;
typedef by_ref_value<MVIEW_EXTENT_UNIT> MVIEW_EXTENT_UNIT_ref;
typedef by_ref_value<TEXT_REF> TEXT_REF_ref;
typedef by_ref_value<MVIEW_3D_RENDER> MVIEW_3D_RENDER_ref;


typedef by_ref_value<EMLAY_GEOMETRY> EMLAY_GEOMETRY_ref;
typedef by_ref_value<ARROW_ALIGNMENT> ARROW_ALIGNMENT_ref;
typedef by_ref_value<BARCHART_LABEL> BARCHART_LABEL_ref;
typedef by_ref_value<COLORBAR_LABEL> COLORBAR_LABEL_ref;
typedef by_ref_value<COLORBAR_STYLE> COLORBAR_STYLE_ref;
typedef by_ref_value<MVU_ORIENTATION> MVU_ORIENTATION_ref;
typedef by_ref_value<MVU_DIVISION_STYLE> MVU_DIVISION_STYLE_ref;
typedef by_ref_value<MVU_ARROW> MVU_ARROW_ref;
typedef by_ref_value<MVU_FLIGHT_COMPASS> MVU_FLIGHT_COMPASS_ref;
typedef by_ref_value<MVU_FLIGHT_DUMMIES> MVU_FLIGHT_DUMMIES_ref;
typedef by_ref_value<MVU_FLIGHT_LOCATE> MVU_FLIGHT_LOCATE_ref;
typedef by_ref_value<MVU_VOX_SURFACE_METHOD> MVU_VOX_SURFACE_METHOD_ref;
typedef by_ref_value<MVU_VOX_SURFACE_OPTION> MVU_VOX_SURFACE_OPTION_ref;
typedef by_ref_value<MVU_TEXTBOX> MVU_TEXTBOX_ref;
typedef by_ref_value<MVU_VPOINT> MVU_VPOINT_ref;
typedef by_ref_value<MVU_VPOS> MVU_VPOS_ref;
typedef by_ref_value<MVU_VSIZE> MVU_VSIZE_ref;
typedef by_ref_value<MVU_VSTYLE> MVU_VSTYLE_ref;






typedef by_ref_value<PG_3D_DIR> PG_3D_DIR_ref;
typedef by_ref_value<PG_BF_CONV> PG_BF_CONV_ref;


typedef by_ref_value<PJ_ELEVATION> PJ_ELEVATION_ref;
typedef by_ref_value<PJ_RECT> PJ_RECT_ref;


typedef by_ref_value<PLY_CLIP> PLY_CLIP_ref;
typedef by_ref_value<PLY_LINE_CLIP> PLY_LINE_CLIP_ref;




typedef by_ref_value<REG_MERGE> REG_MERGE_ref;


typedef by_ref_value<SBF_OPEN> SBF_OPEN_ref;
typedef by_ref_value<SBF_TYPE> SBF_TYPE_ref;


typedef by_ref_value<ST_INFO> ST_INFO_ref;


typedef by_ref_value<ST2_CORRELATION> ST2_CORRELATION_ref;


typedef by_ref_value<FILE_EXT> FILE_EXT_ref;
typedef by_ref_value<STR_CASE> STR_CASE_ref;
typedef by_ref_value<STR_ESCAPE> STR_ESCAPE_ref;
typedef by_ref_value<STR_FILE_PART> STR_FILE_PART_ref;
typedef by_ref_value<STR_JUSTIFY> STR_JUSTIFY_ref;
typedef by_ref_value<STR_TRIM> STR_TRIM_ref;


typedef by_ref_value<SURFACE_OPEN> SURFACE_OPEN_ref;


typedef by_ref_value<SURFACERENDER_MODE> SURFACERENDER_MODE_ref;


typedef by_ref_value<ARC_LICENSE> ARC_LICENSE_ref;
typedef by_ref_value<GEO_DIRECTORY> GEO_DIRECTORY_ref;
typedef by_ref_value<REG_DOMAIN> REG_DOMAIN_ref;
typedef by_ref_value<SHELL_EXECUTE> SHELL_EXECUTE_ref;
typedef by_ref_value<SYS_DIR> SYS_DIR_ref;
typedef by_ref_value<SYS_FONT> SYS_FONT_ref;
typedef by_ref_value<SYS_INFO> SYS_INFO_ref;
typedef by_ref_value<SYS_LINEAGE_SOURCE> SYS_LINEAGE_SOURCE_ref;
typedef by_ref_value<SYS_MENU_CLEAR> SYS_MENU_CLEAR_ref;
typedef by_ref_value<SYS_PATH> SYS_PATH_ref;
typedef by_ref_value<SYS_RUN_DISPLAY> SYS_RUN_DISPLAY_ref;
typedef by_ref_value<SYS_RUN_HOLD> SYS_RUN_HOLD_ref;
typedef by_ref_value<SYS_RUN_TYPE> SYS_RUN_TYPE_ref;
typedef by_ref_value<SYS_RUN_WIN> SYS_RUN_WIN_ref;
typedef by_ref_value<SYS_SEARCH_PATH> SYS_SEARCH_PATH_ref;
typedef by_ref_value<SYS_ENCRYPTION_KEY> SYS_ENCRYPTION_KEY_ref;


typedef by_ref_value<TB_SEARCH> TB_SEARCH_ref;


typedef by_ref_value<TPAT_STRING_SIZE> TPAT_STRING_SIZE_ref;




typedef by_ref_value<USERMETA_FORMAT> USERMETA_FORMAT_ref;


typedef by_ref_value<VA_AVERAGE> VA_AVERAGE_ref;
typedef by_ref_value<VA_OBJECT> VA_OBJECT_ref;




typedef by_ref_value<VOX_DIR> VOX_DIR_ref;
typedef by_ref_value<VOX_DIRECTION> VOX_DIRECTION_ref;
typedef by_ref_value<VOX_FILTER3D> VOX_FILTER3D_ref;
typedef by_ref_value<VOX_GOCAD_ORIENTATION> VOX_GOCAD_ORIENTATION_ref;
typedef by_ref_value<VOX_GRID_LOGOPT> VOX_GRID_LOGOPT_ref;
typedef by_ref_value<VOX_ORIGIN> VOX_ORIGIN_ref;
typedef by_ref_value<VOX_SLICE_MODE> VOX_SLICE_MODE_ref;
typedef by_ref_value<VOX_VECTORVOX_IMPORT> VOX_VECTORVOX_IMPORT_ref;




typedef by_ref_value<VOXE_EVAL> VOXE_EVAL_ref;


typedef by_ref_value<BLOCK_MODEL_VARIABLE_TYPE> BLOCK_MODEL_VARIABLE_TYPE_ref;


typedef by_ref_value<VV_DOUBLE_CRC_BITS> VV_DOUBLE_CRC_BITS_ref;
typedef by_ref_value<VV_FLOAT_CRC_BITS> VV_FLOAT_CRC_BITS_ref;
typedef by_ref_value<VV_LOG_BASE> VV_LOG_BASE_ref;
typedef by_ref_value<VV_LOG_NEGATIVE> VV_LOG_NEGATIVE_ref;
typedef by_ref_value<VV_LOOKUP> VV_LOOKUP_ref;
typedef by_ref_value<VV_MASK> VV_MASK_ref;
typedef by_ref_value<VV_ORDER> VV_ORDER_ref;
typedef by_ref_value<VV_SORT> VV_SORT_ref;
typedef by_ref_value<VV_WINDOW> VV_WINDOW_ref;


typedef by_ref_value<WA_ENCODE> WA_ENCODE_ref;
typedef by_ref_value<WA_OPEN> WA_OPEN_ref;

