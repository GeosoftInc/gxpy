#include "stdafx.h"

using namespace boost::python;
using boost::python::init;


// Dummy classes


inline void GXSEMPLOT_wrap_apply_filter_to_mask(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, int32_t arg6)
{
    GXSEMPLOT::apply_filter_to_mask(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXSEMPLOT_wrap_convert_dummies(GXDBPtr arg1, int32_t arg2)
{
    GXSEMPLOT::convert_dummies(arg1, arg2);
}
inline void GXSEMPLOT_wrap_create_groups(GXDBPtr arg1, const gx_string_type& arg2)
{
    GXSEMPLOT::create_groups(arg1, arg2);
}
inline void GXSEMPLOT_wrap_default_groups(GXDBPtr arg1)
{
    GXSEMPLOT::default_groups(arg1);
}
inline void GXSEMPLOT_wrap_edit_map_plot_parameters(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXMAPPtr arg4, const gx_string_type& arg5)
{
    GXSEMPLOT::edit_map_plot_parameters(arg1, arg2, arg3, arg4, arg5);
}
inline void GXSEMPLOT_wrap_edit_plot_components(GXDBPtr arg1, const gx_string_type& arg2)
{
    GXSEMPLOT::edit_plot_components(arg1, arg2);
}
inline void GXSEMPLOT_wrap_edit_plot_parameters(GXDBPtr arg1, const gx_string_type& arg2)
{
    GXSEMPLOT::edit_plot_parameters(arg1, arg2);
}
inline void GXSEMPLOT_wrap_export_overlay(const gx_string_type& arg1, const gx_string_type& arg2, GXMVIEWPtr arg3, const gx_string_type& arg4, int32_t arg5, const gx_string_type& arg6, const gx_string_type& arg7, const gx_string_type& arg8, const gx_string_type& arg9, const gx_string_type& arg10, const gx_string_type& arg11, int32_t arg12)
{
    GXSEMPLOT::export_overlay(arg1, arg2, arg3, arg4, (SEMPLOT_PLOT)arg5, arg6, arg7, arg8, arg9, arg10, arg11, (SEMPLOT_EXT)arg12);
}
inline void GXSEMPLOT_wrap_export_view(GXDBPtr arg1, GXLSTPtr arg2, GXDBPtr arg3, int32_t arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7)
{
    GXSEMPLOT::export_view(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXSEMPLOT_wrap_export_view2(GXDBPtr arg1, GXLSTPtr arg2, GXDBPtr arg3, int32_t arg4, const gx_string_type& arg5, const gx_string_type& arg6, const gx_string_type& arg7, int32_t arg8)
{
    GXSEMPLOT::export_view2(arg1, arg2, arg3, arg4, arg5, arg6, arg7, (SEMPLOT_EXPORT)arg8);
}
inline void GXSEMPLOT_wrap_filter_lst(GXLSTPtr arg1)
{
    GXSEMPLOT::filter_lst(arg1);
}
inline void GXSEMPLOT_wrap_filter_mineral_pos_data(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, int32_t arg5)
{
    GXSEMPLOT::filter_mineral_pos_data(arg1, arg2, arg3, arg4, arg5);
}
inline void GXSEMPLOT_wrap_get_associated_lst(GXDBPtr arg1, int32_t arg2, GXLSTPtr arg3)
{
    GXSEMPLOT::get_associated_lst(arg1, arg2, arg3);
}
inline void GXSEMPLOT_wrap_get_current_mineral_lst(GXDBPtr arg1, const gx_string_type& arg2, GXLSTPtr arg3)
{
    GXSEMPLOT::get_current_mineral_lst(arg1, arg2, arg3);
}
inline void GXSEMPLOT_wrap_get_current_position_lst(GXDBPtr arg1, GXLSTPtr arg2)
{
    GXSEMPLOT::get_current_position_lst(arg1, arg2);
}
inline void GXSEMPLOT_wrap_get_full_mineral_lst(GXLSTPtr arg1)
{
    GXSEMPLOT::get_full_mineral_lst(arg1);
}
inline void GXSEMPLOT_wrap_get_full_position_lst(GXLSTPtr arg1)
{
    GXSEMPLOT::get_full_position_lst(arg1);
}
inline void GXSEMPLOT_wrap_get_grouping_lst(GXDBPtr arg1, GXLSTPtr arg2)
{
    GXSEMPLOT::get_grouping_lst(arg1, arg2);
}
inline int32_t GXSEMPLOT_wrap_create_ascii_template(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSEMPLOT::create_ascii_template(arg1, arg2);
    return ret;
}
inline int32_t GXSEMPLOT_wrap_create_database_template(const gx_string_type& arg1, const gx_string_type& arg2)
{
    int32_t ret = GXSEMPLOT::create_database_template(arg1, arg2);
    return ret;
}
inline int32_t GXSEMPLOT_wrap_edit_filter(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5)
{
    int32_t ret = GXSEMPLOT::edit_filter(arg1, arg2, arg3, arg4, arg5);
    return ret;
}
inline void GXSEMPLOT_wrap_get_mineral_channel_name(GXDBPtr arg1, str_ref& arg2)
{
    GXSEMPLOT::get_mineral_channel_name(arg1, arg2);
}
inline void GXSEMPLOT_wrap_import_ascii_wizard(const gx_string_type& arg1, const gx_string_type& arg2, str_ref& arg3)
{
    GXSEMPLOT::import_ascii_wizard(arg1, arg2, arg3);
}
inline void GXSEMPLOT_wrap_import_database_odbc(str_ref& arg1, str_ref& arg2)
{
    GXSEMPLOT::import_database_odbc(arg1, arg2);
}
inline void GXSEMPLOT_wrap_import_bin(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, int32_t arg5, double arg6)
{
    GXSEMPLOT::import_bin(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXSEMPLOT_wrap_import_database_ado(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSEMPLOT::import_database_ado(arg1, arg2);
}
inline void GXSEMPLOT_wrap_init_group_symbols_used(GXDBPtr arg1)
{
    GXSEMPLOT::init_group_symbols_used(arg1);
}
inline int32_t GXSEMPLOT_wrap_template_type(const gx_string_type& arg1)
{
    int32_t ret = GXSEMPLOT::template_type(arg1);
    return ret;
}
inline int32_t GXSEMPLOT_wrap_view_type(GXMAPPtr arg1, const gx_string_type& arg2)
{
    SEMPLOT_PLOT ret = GXSEMPLOT::view_type(arg1, arg2);
    return ret;
}
inline void GXSEMPLOT_wrap_mineral_id(GXDBPtr arg1, double arg2, int32_t arg3, int32_t arg4)
{
    GXSEMPLOT::mineral_id(arg1, arg2, arg3, arg4);
}
inline void GXSEMPLOT_wrap_new_filter(const gx_string_type& arg1, const gx_string_type& arg2)
{
    GXSEMPLOT::new_filter(arg1, arg2);
}
inline void GXSEMPLOT_wrap_new_template(const gx_string_type& arg1, int32_t arg2, const gx_string_type& arg3)
{
    GXSEMPLOT::new_template(arg1, arg2, arg3);
}
inline void GXSEMPLOT_wrap_overlay_lst(GXLSTPtr arg1, int32_t arg2, int32_t arg3)
{
    GXSEMPLOT::overlay_lst(arg1, (SEMPLOT_EXT)arg2, (SEMPLOT_PLOT)arg3);
}
inline void GXSEMPLOT_wrap_plot(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, int32_t arg6, int32_t arg7)
{
    GXSEMPLOT::plot(arg1, arg2, arg3, arg4, arg5, arg6, arg7);
}
inline void GXSEMPLOT_wrap_plot_symbol_legend(GXDBPtr arg1, GXMVIEWPtr arg2, double arg3, double arg4, double arg5, double arg6)
{
    GXSEMPLOT::plot_symbol_legend(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXSEMPLOT_wrap_prop_symb(GXDBPtr arg1, GXMAPPtr arg2, const gx_string_type& arg3, const gx_string_type& arg4, const gx_string_type& arg5, const gx_string_type& arg6, int32_t arg7, int32_t arg8, double arg9, double arg10, int32_t arg11, int32_t arg12, int32_t arg13, int32_t arg14, int32_t arg15)
{
    GXSEMPLOT::prop_symb(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15);
}
inline void GXSEMPLOT_wrap_replot(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, GXMAPPtr arg4, const gx_string_type& arg5)
{
    GXSEMPLOT::replot(arg1, arg2, arg3, arg4, arg5);
}
inline void GXSEMPLOT_wrap_re_plot_symbol_legend(GXDBPtr arg1, GXMVIEWPtr arg2)
{
    GXSEMPLOT::re_plot_symbol_legend(arg1, arg2);
}
inline void GXSEMPLOT_wrap_reset_groups(GXDBPtr arg1, const gx_string_type& arg2)
{
    GXSEMPLOT::reset_groups(arg1, arg2);
}
inline void GXSEMPLOT_wrap_reset_used_channel(GXDBPtr arg1)
{
    GXSEMPLOT::reset_used_channel(arg1);
}
inline void GXSEMPLOT_wrap_select_poly(GXDBPtr arg1, GXMVIEWPtr arg2, const gx_string_type& arg3, const gx_string_type& arg4, GXPLYPtr arg5, int32_t arg6)
{
    GXSEMPLOT::select_poly(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXSEMPLOT_wrap_set_channel_order(GXDBPtr arg1, GXLSTPtr arg2)
{
    GXSEMPLOT::set_channel_order(arg1, arg2);
}
inline void GXSEMPLOT_wrap_set_channel_units(GXDBPtr arg1)
{
    GXSEMPLOT::set_channel_units(arg1);
}
inline void GXSEMPLOT_wrap_set_itr(GXDBPtr arg1, int32_t arg2, GXITRPtr arg3)
{
    GXSEMPLOT::set_itr(arg1, arg2, arg3);
}
inline void GXSEMPLOT_wrap_set_mask(GXDBPtr arg1, const gx_string_type& arg2, const gx_string_type& arg3, const gx_string_type& arg4, int32_t arg5, int32_t arg6)
{
    GXSEMPLOT::set_mask(arg1, arg2, arg3, arg4, arg5, arg6);
}
inline void GXSEMPLOT_wrap_sort_data(GXDBPtr arg1, int32_t arg2, int32_t arg3)
{
    GXSEMPLOT::sort_data(arg1, arg2, arg3);
}
inline void GXSEMPLOT_wrap_template_lst(GXLSTPtr arg1, int32_t arg2)
{
    GXSEMPLOT::template_lst(arg1, (SEMPLOT_PLOT)arg2);
}
inline void GXSEMPLOT_wrap_tile_windows()
{
    GXSEMPLOT::tile_windows();
}
inline void GXSEMPLOT_wrap_total_oxides(GXDBPtr arg1, const gx_string_type& arg2)
{
    GXSEMPLOT::total_oxides(arg1, arg2);
}

void gxPythonImportGXSEMPLOT()
{

    class_<GXSEMPLOT, boost::noncopyable> pyClass("GXSEMPLOT",
            "\n.. parsed-literal::\n\n"
            "   Oasis montaj implementation of RTE SEMPLOT\n\n"
            , no_init);


    pyClass.def("apply_filter_to_mask", &GXSEMPLOT_wrap_apply_filter_to_mask,
                "apply_filter_to_mask((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Apply the filter to the mask channel\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Filter name\n"
                ":type arg2: str\n"
                ":param arg3: Mask channel name\n"
                ":type arg3: str\n"
                ":param arg4: Mineral channel name\n"
                ":type arg4: str\n"
                ":param arg5: Mineral to use (\"All\" or \"\" for all)\n"
                ":type arg5: str\n"
                ":param arg6: Mask mode (0: Append, 1: New)\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The mask channel is updated for the current data to reflect\n"
                "   the actions of the filter. Those values passing get 1, those\n"
                "   failing get 0.\n\n"
               ).staticmethod("apply_filter_to_mask");
    pyClass.def("convert_dummies", &GXSEMPLOT_wrap_convert_dummies,
                "convert_dummies((GXDB)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Convert dummies to zero values for assay channels.\n\n"

                ":param arg1: database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Input line to convert\n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The is operation is controlled by the Preferences\n"
                "   \"Use dummies to indicate no data?\" By default, this option is \"yes\"\n"
                "   so this function will return with no changes. However, if\n"
                "   \"no\", then all ASSAY class channels will have dummy values\n"
                "   converted to 0.0.\n\n"
               ).staticmethod("convert_dummies");
    pyClass.def("create_groups", &GXSEMPLOT_wrap_create_groups,
                "create_groups((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Group data by anomaly or string channel - Interactive.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Mask channel\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("create_groups");
    pyClass.def("default_groups", &GXSEMPLOT_wrap_default_groups,
                "default_groups((GXDB)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Group data by selected anomalies.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("default_groups");
    pyClass.def("edit_map_plot_parameters", &GXSEMPLOT_wrap_edit_map_plot_parameters,
                "edit_map_plot_parameters((GXDB)arg1, (str)arg2, (str)arg3, (GXMAP)arg4, (str)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Alter parameters in an XYplot Triplot map.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Mask channel (can be \"\")\n"
                ":type arg2: str\n"
                ":param arg3: Mineral channel (can be \"\" for raw data)\n"
                ":type arg3: str\n"
                ":param arg4: Map handle\n"
                ":type arg4: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg5: Map View\n"
                ":type arg5: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Parameters GUI is loaded based on settings stored in\n"
                "   the map. The map is then re-plotted, overwriting the old one,\n"
                "   based on the new settings. Note that the selection of data\n"
                "   in the current DB is used to replot the map.\n\n"
               ).staticmethod("edit_map_plot_parameters");
    pyClass.def("edit_plot_components", &GXSEMPLOT_wrap_edit_plot_components,
                "edit_plot_components((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set group names and channels to plot in a template.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Template name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The \"Components\" group in the INI file is edited.\n"
                "   \n"
                "   Looks first in user\\etc, then in \\etc.\n"
                "   Looks first for file prefix \"semtemplate\" then \"xyt\" or \"tri\"\n"
                "   The altered template will be output to the user\\etc directory with\n"
                "   the file extension \"semtemplate\".\n\n"
               ).staticmethod("edit_plot_components");
    pyClass.def("edit_plot_parameters", &GXSEMPLOT_wrap_edit_plot_parameters,
                "edit_plot_parameters((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set TriPlot parameters in a template.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Template name\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The \"Parameters\" group in the INI file is edited.\n"
                "   \n"
                "   Looks first in user\\etc, then in \\etc.\n"
                "   Looks first for file prefix \"semtemplate\" then \"xyt\" or \"tri\"\n"
                "   The altered template will be output to the user\\etc directory with\n"
                "   the file extension \"semtemplate\".\n\n"
               ).staticmethod("edit_plot_parameters");
    pyClass.def("export_overlay", &GXSEMPLOT_wrap_export_overlay,
                "export_overlay((str)arg1, (str)arg2, (GXMVIEW)arg3, (str)arg4, (int)arg5, (str)arg6, (str)arg7, (str)arg8, (str)arg9, (str)arg10, (str)arg11, (int)arg12) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create overlay map and file from a group.\n\n"

                ":param arg1: overlay file name\n"
                ":type arg1: str\n"
                ":param arg2: associated map\n"
                ":type arg2: str\n"
                ":param arg3: View with group\n"
                ":type arg3: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg4: group name\n"
                ":type arg4: str\n"
                ":param arg5: \\ :ref:`SEMPLOT_PLOT`\\ \n"
                ":type arg5: int\n"
                ":param arg6: XStage\n"
                ":type arg6: str\n"
                ":param arg7: XOxide\n"
                ":type arg7: str\n"
                ":param arg8: YStage\n"
                ":type arg8: str\n"
                ":param arg9: YOxide\n"
                ":type arg9: str\n"
                ":param arg10: ZStage\n"
                ":type arg10: str\n"
                ":param arg11: ZOxide\n"
                ":type arg11: str\n"
                ":param arg12: \\ :ref:`SEMPLOT_EXT`\\ \n"
                ":type arg12: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The group is written to a new map, and an overlay file\n"
                "   is created which points to this map.\n\n"
               ).staticmethod("export_overlay");
    pyClass.def("export_view", &GXSEMPLOT_wrap_export_view,
                "export_view((GXDB)arg1, (GXLST)arg2, (GXDB)arg3, (int)arg4, (str)arg5, (str)arg6, (str)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a \"View\" database\n\n"

                ":param arg1: Original raw data database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: List of lines (anomlies) to export\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: Destination database\n"
                ":type arg3: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg4: View to export - One of SEMPLOT_XXX_STAGE\n"
                ":type arg4: int\n"
                ":param arg5: Mask channel (\"\" for None)\n"
                ":type arg5: str\n"
                ":param arg6: Mineral channel\n"
                ":type arg6: str\n"
                ":param arg7: Mineral to export (\"\" for all)\n"
                ":type arg7: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("export_view");
    pyClass.def("export_view2", &GXSEMPLOT_wrap_export_view2,
                "export_view2((GXDB)arg1, (GXLST)arg2, (GXDB)arg3, (int)arg4, (str)arg5, (str)arg6, (str)arg7, (int)arg8) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a \"View\" database, with channel selection\n\n"

                ":param arg1: Original raw data database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: List of lines (anomlies) to export\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg3: Destination database\n"
                ":type arg3: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg4: View to export - One of SEMPLOT_XXX_STAGE\n"
                ":type arg4: int\n"
                ":param arg5: Mask channel (\"\" for None)\n"
                ":type arg5: str\n"
                ":param arg6: Mineral channel\n"
                ":type arg6: str\n"
                ":param arg7: Mineral to export (\"\" for all)\n"
                ":type arg7: str\n"
                ":param arg8: \\ :ref:`SEMPLOT_EXPORT`\\  Channel selection\n"
                ":type arg8: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 7.1.0\n\n"
               ).staticmethod("export_view2");
    pyClass.def("filter_lst", &GXSEMPLOT_wrap_filter_lst,
                "filter_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill a LST with existing SEMPLOT filters\n\n"

                ":param arg1: LST to fill.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   \"Supplied\" filters are stored in \\etc, while user-edited and new filters\n"
                "   are stored in user\\etc. This function finds all files with the extension\n"
                "   \".semfilter\", first in user\\etc, then in \\etc, and adds the file names\n"
                "   (without the extension) to the LST. The name with the extension is stored\n"
                "   as the value.\n"
                "   The LST is cleared first.\n\n"
               ).staticmethod("filter_lst");
    pyClass.def("filter_mineral_pos_data", &GXSEMPLOT_wrap_filter_mineral_pos_data,
                "filter_mineral_pos_data((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (int)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Filter raw data by position and mineral values\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Mask channel\n"
                ":type arg2: str\n"
                ":param arg3: Mineral channel\n"
                ":type arg3: str\n"
                ":param arg4: mineral (string) - \"C\", \"I\" etc.\n"
                ":type arg4: str\n"
                ":param arg5: Grain position\n"
                ":type arg5: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The Mask channel will be updated so that those data values\n"
                "   which \"pass\" get \"1\" and those that \"fail\" get dummy \"\\ `*`\\ \"\n"
                "   NO DATA IS REMOVED.\n"
                "   Works on all selected lines of data.\n\n"
               ).staticmethod("filter_mineral_pos_data");
    pyClass.def("get_associated_lst", &GXSEMPLOT_wrap_get_associated_lst,
                "get_associated_lst((GXDB)arg1, (int)arg2, (GXLST)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get the associated channels for this group in a LST\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Data Group handle\n"
                ":type arg2: int\n"
                ":param arg3: LST to copy channels into\n"
                ":type arg3: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("get_associated_lst");
    pyClass.def("get_current_mineral_lst", &GXSEMPLOT_wrap_get_current_mineral_lst,
                "get_current_mineral_lst((GXDB)arg1, (str)arg2, (GXLST)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve LST of minerals in selected lines.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Mineral channel name\n"
                ":type arg2: str\n"
                ":param arg3: LST object\n"
                ":type arg3: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the mineral channel name is not specified, it returns\n"
                "   just the \"X\" (Unknown) item.\n\n"
               ).staticmethod("get_current_mineral_lst");
    pyClass.def("get_current_position_lst", &GXSEMPLOT_wrap_get_current_position_lst,
                "get_current_position_lst((GXDB)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve LST of positions in selected lines.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: LST object\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("get_current_position_lst");
    pyClass.def("get_full_mineral_lst", &GXSEMPLOT_wrap_get_full_mineral_lst,
                "get_full_mineral_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve LST of all minerals in Semplot_Minerals.csv\n\n"

                ":param arg1: LST object\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("get_full_mineral_lst");
    pyClass.def("get_full_position_lst", &GXSEMPLOT_wrap_get_full_position_lst,
                "get_full_position_lst((GXLST)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve LST of all possible mineral positions.\n\n"

                ":param arg1: LST object\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("get_full_position_lst");
    pyClass.def("get_grouping_lst", &GXSEMPLOT_wrap_get_grouping_lst,
                "get_grouping_lst((GXDB)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Get list of items to group symbols by.\n\n"

                ":param arg1: database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: list to hold items\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The first item is \"Anomaly\", which gives the line names, The second\n"
                "   item (if the channel exists in the database) is the Sample Number.\n"
                "   After this are included all string channels which are NOT oxides or\n"
                "   elements. (The list can include the mineral).\n"
                "   Channel symbol is the LST value (except for the first item - \"Anomaly\")\n\n"
               ).staticmethod("get_grouping_lst");
    pyClass.def("create_ascii_template", &GXSEMPLOT_wrap_create_ascii_template,
                "create_ascii_template((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   : Generate ASCII import template automatically\n\n"

                ":param arg1: data file name\n"
                ":type arg1: str\n"
                ":param arg2: template to make\n"
                ":type arg2: str\n"
                ":returns: 1 if it succeeds in creating a Template.\n"
                "          0 if it fails.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("create_ascii_template");
    pyClass.def("create_database_template", &GXSEMPLOT_wrap_create_database_template,
                "create_database_template((str)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate database import template automatically\n\n"

                ":param arg1: data file name\n"
                ":type arg1: str\n"
                ":param arg2: template to make\n"
                ":type arg2: str\n"
                ":returns: 1 if it succeeds in creating a Template.\n"
                "          0 if it fails.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("create_database_template");
    pyClass.def("edit_filter", &GXSEMPLOT_wrap_edit_filter,
                "edit_filter((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Edit and create filter on channel values\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Name of filter\n"
                ":type arg2: str\n"
                ":param arg3: Mask channel name\n"
                ":type arg3: str\n"
                ":param arg4: Mineral channel name\n"
                ":type arg4: str\n"
                ":param arg5: Mineral to restrict filter to.\n"
                ":type arg5: str\n"
                ":returns: -1 - Cancel - Edits to filter discarded.\n"
                "          \n"
                "           0 - Normal Return. Edits saved to filter file.\n"
                "          \n"
                "           1 - Apply filter to current data only\n"
                "          \n"
                "           2 - Remove filter - If removing filtered data, just\n"
                "               restore the data to the Min/Pos data\n"
                "               otherwise set the mask channel to 1.\n"
                "          \n"
                "          Re-entry code. If not iDUMMY, what to do inside the filter after\n"
                "          going back in. Returned on exit, used on next input.\n"
                "          \n"
                "           0 - Nothing. Don't need to go back into this function again.\n"
                "           1 - Edit the filter.\n"
                "          \n"
                "          Notes            New and edited filters are stored in user\\etc in files with\n"
                "           the file extension \".semfilter\"\n"
                "           If a file for the specified filter does not exist, then a\n"
                "           new filter by that name will be created.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("edit_filter");
    pyClass.def("get_mineral_channel_name", &GXSEMPLOT_wrap_get_mineral_channel_name,
                "get_mineral_channel_name((GXDB)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Retrieve the mineral channel name.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Mineral channel name\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   First looks at the SEMPLOT.MINERAL_CHANNEL value.\n"
                "   If not found, returns the first MINERAL class\n"
                "   channel found. If still not found, returns a\n"
                "   blank string.\n\n"
               ).staticmethod("get_mineral_channel_name");
    pyClass.def("import_ascii_wizard", &GXSEMPLOT_wrap_import_ascii_wizard,
                "import_ascii_wizard((str)arg1, (str)arg2, (str_ref)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a SEMPLOT ASCII import template.\n\n"

                ":param arg1: data file name\n"
                ":type arg1: str\n"
                ":param arg2: template to make\n"
                ":type arg2: str\n"
                ":param arg3: anomaly name (can be \"\")\n"
                ":type arg3: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the anomaly name is not included, then\n"
                "   the input data must have an \"Anom_Name\" field.\n\n"
               ).staticmethod("import_ascii_wizard");
    pyClass.def("import_database_odbc", &GXSEMPLOT_wrap_import_database_odbc,
                "import_database_odbc((str_ref)arg1, (str_ref)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a template file for importing ODBC databases.\n\n"

                ":param arg1: connection string (input and returned)\n"
                ":type arg1: :class:`geosoft.gxapi.str_ref`\n"
                ":param arg2: template file (returned)\n"
                ":type arg2: :class:`geosoft.gxapi.str_ref`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("import_database_odbc");
    pyClass.def("import_bin", &GXSEMPLOT_wrap_import_bin,
                "import_bin((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (int)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Import blocked binary or archive ASCII data\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: import data file name\n"
                ":type arg2: str\n"
                ":param arg3: import template name\n"
                ":type arg3: str\n"
                ":param arg4: Optional Line name (see note 3.)\n"
                ":type arg4: str\n"
                ":param arg5: Optional Flight number\n"
                ":type arg5: int\n"
                ":param arg6: Optional date\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This wrapper is for SEMPLOT, and does not require the import licence.\n"
                "   \n"
                "      1. Binary import templates have extension .I2 by convention.  See\n"
                "         BINARY.I2 for a description of the template format.\n"
                "         Archive import templates have extension .I3 by convention. See\n"
                "         ARCHIVE.I3 for a description of the template format.\n"
                "   \n"
                "      2. Both the import template and data file must exist.\n"
                "   \n"
                "      3. If a line already exists in the database, a new version is created\n"
                "         unless a line name is passed in.  In this case, the specified name\n"
                "         is used and the imported channels on the previous line will be\n"
                "         destroyed.\n\n"

                "\n.. seealso::\n\n"
                "   \\ :func:`geosoft.gxapi.GXDU.lab_template`\\  in du.gxh\n\n"
               ).staticmethod("import_bin");
    pyClass.def("import_database_ado", &GXSEMPLOT_wrap_import_database_ado,
                "import_database_ado((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Generate a template file for importing semplot databases.\n\n"

                ":param arg1: data file name\n"
                ":type arg1: str\n"
                ":param arg2: template to make\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("import_database_ado");
    pyClass.def("init_group_symbols_used", &GXSEMPLOT_wrap_init_group_symbols_used,
                "init_group_symbols_used((GXDB)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Initializes memory of symbols used in plotting.\n\n"

                ":param arg1: database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Maintains a list of the symbols used in plotting. Call before\n"
                "   Plotting one or more legends - symbols are accumulated.\n"
                "   \\ :func:`geosoft.gxapi.GXSEMPLOT.plot_symbol_legend`\\  uses this information to create a legend.\n\n"
               ).staticmethod("init_group_symbols_used");
    pyClass.def("template_type", &GXSEMPLOT_wrap_template_type,
                "template_type((str)arg1) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new XYPlot or TriPlot template.\n\n"

                ":param arg1: Template name\n"
                ":type arg1: str\n"
                ":returns: SEMPLOT_PLOT_XYPLOT or\n"
                "          SEMPLOT_PLOT_TRIPLOT\n"
                "          Terminates if error.\n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("template_type");
    pyClass.def("view_type", &GXSEMPLOT_wrap_view_type,
                "view_type((GXMAP)arg1, (str)arg2) -> int:\n"

                "\n.. parsed-literal::\n\n"
                "   Test to see if a view is an XYPlot or Triplot view.\n\n"

                ":param arg1: Input map object\n"
                ":type arg1: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg2: Input view name\n"
                ":type arg2: str\n"
                ":returns: \\ :ref:`SEMPLOT_PLOT`\\ \n"
                ":rtype: int\n"
                "\n"

                "\n.. versionadded:: 6.4.2\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   First checks the view name to see if it starts with\n"
                "   \"XYplt_\" or \"Triplt_\". Failing that it looks in the\n"
                "   view REG for a value for \"Components.Type\", which will\n"
                "   be either \"XYPlot\" or \"TriPlot\".\n"
                "   If the view does not appear to be an XYPlot or a TriPlot view,\n"
                "   the function returns SEMPLOT_PLOT_UNKNOWN.\n\n"
               ).staticmethod("view_type");
    pyClass.def("mineral_id", &GXSEMPLOT_wrap_mineral_id,
                "mineral_id((GXDB)arg1, (float)arg2, (int)arg3, (int)arg4) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Identify minerals from the oxide channels.\n\n"

                ":param arg1: Database\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Maximum residual value (in % of the total oxide)\n"
                ":type arg2: float\n"
                ":param arg3: Mineral channel (Locked RW)\n"
                ":type arg3: int\n"
                ":param arg4: Residual channel (Locked RW)\n"
                ":type arg4: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.3.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Finds the best mineral matching the composition for each\n"
                "   row of oxide values. Works using linear programming and\n"
                "   the simplex method to maximize the oxides used to create\n"
                "   each of the possible output minerals. The mineral leaving the\n"
                "   least leftover is selected, as long as the residual (measured\n"
                "   as a percent of the total) is less than or equal to the\n"
                "   input value.\n\n"
               ).staticmethod("mineral_id");
    pyClass.def("new_filter", &GXSEMPLOT_wrap_new_filter,
                "new_filter((str)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new selection filter.\n\n"

                ":param arg1: New filter name\n"
                ":type arg1: str\n"
                ":param arg2: Filter to use as a model (can be \"\")\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Creates a new, empty filter file in the user\\etc directory\n\n"
               ).staticmethod("new_filter");
    pyClass.def("new_template", &GXSEMPLOT_wrap_new_template,
                "new_template((str)arg1, (int)arg2, (str)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Create a new XYPlot or TriPlot template.\n\n"

                ":param arg1: New template name\n"
                ":type arg1: str\n"
                ":param arg2: Unknown\n"
                ":type arg2: int\n"
                ":param arg3: Template to use as a model (can be \"\")\n"
                ":type arg3: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The new template is written to the user\\etc directory, with\n"
                "   the file extension \"semfilter\". The template contains a parameter\n"
                "   identifying it as an XY or Triplot.\n"
                "   \n"
                "   Model Template: Looks first in user\\etc, then in \\etc.\n"
                "   Looks first for file prefix \"semtemplate\" then \"xyt\" or \"tri\"\n"
                "   \n"
                "   Because there are so many shared parameters, it is possible to use\n"
                "   an XYPlot template as a model for a TriPlot, and vica-verca, with\n"
                "   few complications.  (e.g. needing to define a \"Z\" component)\n\n"
               ).staticmethod("new_template");
    pyClass.def("overlay_lst", &GXSEMPLOT_wrap_overlay_lst,
                "overlay_lst((GXLST)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill a list with the available plot overlay names\n\n"

                ":param arg1: Input LST.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`SEMPLOT_EXT`\\ \n"
                ":type arg2: int\n"
                ":param arg3: \\ :ref:`SEMPLOT_PLOT`\\ \n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Looks first in user\\etc, then in \\etc.\n"
                "   See SEMPLOT_EXT definitions above for which files to look for.\n\n"
               ).staticmethod("overlay_lst");
    pyClass.def("plot", &GXSEMPLOT_wrap_plot,
                "plot((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (str)arg5, (int)arg6, (int)arg7) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot an XYPlot or TriPlot based on the template.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Template file name\n"
                ":type arg2: str\n"
                ":param arg3: Mask channel (can be \"\")\n"
                ":type arg3: str\n"
                ":param arg4: Mineral channel (can be \"\" for raw data)\n"
                ":type arg4: str\n"
                ":param arg5: Map name\n"
                ":type arg5: str\n"
                ":param arg6: Map open mode; one of MAP_WRITEXXX (see map.gxh)\n"
                ":type arg6: int\n"
                ":param arg7: Plot symbols (O: No, 1:Yes) ?\n"
                ":type arg7: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The \"Components\" and \"Parameters\" groups in the INI file\n"
                "   are used.\n"
                "   Only values with mask values of 1 are plotted, if the mask\n"
                "   channel is specified.\n"
                "   \n"
                "   Call \"\\ :func:`geosoft.gxapi.GXSEMPLOT.reset_used_channel`\\ \" prior to this function\n"
                "   in order to track the values actually plotted.\n"
                "   \n"
                "   Call \\ :func:`geosoft.gxapi.GXSEMPLOT.init_group_symbols_used`\\  prior to this function\n"
                "   to reset recording of the symbols used in plotting (for legends etc).\n\n"
               ).staticmethod("plot");
    pyClass.def("plot_symbol_legend", &GXSEMPLOT_wrap_plot_symbol_legend,
                "plot_symbol_legend((GXDB)arg1, (GXMVIEW)arg2, (float)arg3, (float)arg4, (float)arg5, (float)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot a symbol legend in a view.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: View to plot into\n"
                ":type arg2: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg3: X Minimum\n"
                ":type arg3: float\n"
                ":param arg4: Y Minimum\n"
                ":type arg4: float\n"
                ":param arg5: Y Maximum\n"
                ":type arg5: float\n"
                ":param arg6: Symbol size\n"
                ":type arg6: float\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function depends on \\ :func:`geosoft.gxapi.GXSEMPLOT.init_group_symbols_used`\\ \n"
                "   before the plot for which this legend is created is made.\n"
                "   The symbols and groups to use in the legend are stored to\n"
                "   a database blob after the plot is made. These values are\n"
                "   recovered by this function to make the legend at the\n"
                "   specified location.\n\n"
               ).staticmethod("plot_symbol_legend");
    pyClass.def("prop_symb", &GXSEMPLOT_wrap_prop_symb,
                "prop_symb((GXDB)arg1, (GXMAP)arg2, (str)arg3, (str)arg4, (str)arg5, (str)arg6, (int)arg7, (int)arg8, (float)arg9, (float)arg10, (int)arg11, (int)arg12, (int)arg13, (int)arg14, (int)arg15) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Plot a proportional symbol plot.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Map to plot to\n"
                ":type arg2: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg3: View to replot\n"
                ":type arg3: str\n"
                ":param arg4: channel name\n"
                ":type arg4: str\n"
                ":param arg5: mask channel (can be \"\")\n"
                ":type arg5: str\n"
                ":param arg6: mineral channel (\n"
                ":type arg6: str\n"
                ":param arg7: linear (0) or logarithmic (1) scaling\n"
                ":type arg7: int\n"
                ":param arg8: scale by diameter (0) or area (1)\n"
                ":type arg8: int\n"
                ":param arg9: scale base (log) data units\n"
                ":type arg9: float\n"
                ":param arg10: scale factor (log) data units/mm\n"
                ":type arg10: float\n"
                ":param arg11: symbol number\n"
                ":type arg11: int\n"
                ":param arg12: symbol weight\n"
                ":type arg12: int\n"
                ":param arg13: symbol line color\n"
                ":type arg13: int\n"
                ":param arg14: symbol fill color\n"
                ":type arg14: int\n"
                ":param arg15: plot legend?\n"
                ":type arg15: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Replots map using proportional symbols\n\n"
               ).staticmethod("prop_symb");
    pyClass.def("replot", &GXSEMPLOT_wrap_replot,
                "replot((GXDB)arg1, (str)arg2, (str)arg3, (GXMAP)arg4, (str)arg5) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replot an existing SEMPLOT plot based on current data.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Mask channel (can be \"\")\n"
                ":type arg2: str\n"
                ":param arg3: Mineral channel (can be \"\" for raw data)\n"
                ":type arg3: str\n"
                ":param arg4: Map handle\n"
                ":type arg4: :class:`geosoft.gxapi.GXMAP`\n"
                ":param arg5: Map View containing the plot\n"
                ":type arg5: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Note that the selection of data\n"
                "   in the current DB is used to replot the map.\n"
                "   \n"
                "   Call \"\\ :func:`geosoft.gxapi.GXSEMPLOT.reset_used_channel`\\ \" prior to this function\n"
                "   in order to track the values actually plotted.\n"
                "   \n"
                "   Call \\ :func:`geosoft.gxapi.GXSEMPLOT.init_group_symbols_used`\\  prior to this function\n"
                "   to reset recording of the symbols used in plotting (for legends etc).\n\n"
               ).staticmethod("replot");
    pyClass.def("re_plot_symbol_legend", &GXSEMPLOT_wrap_re_plot_symbol_legend,
                "re_plot_symbol_legend((GXDB)arg1, (GXMVIEW)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Replot a symbol legend in a view.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: View to plot into\n"
                ":type arg2: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Searches the VIEW REG for information on a previously\n"
                "   created legend, and if it finds that info, replots the Legend,\n"
                "   using the current data, group key etc.\n\n"
               ).staticmethod("re_plot_symbol_legend");
    pyClass.def("reset_groups", &GXSEMPLOT_wrap_reset_groups,
                "reset_groups((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Re-group data using current settings.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Mask channel\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("reset_groups");
    pyClass.def("reset_used_channel", &GXSEMPLOT_wrap_reset_used_channel,
                "reset_used_channel((GXDB)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the \"Plotted\" channel to dummies\n\n"

                ":param arg1: database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   This function is called before one or a series of plots to initialize\n"
                "   the \"Plotted\" channel in all the selected lines to dummy values.\n"
                "   As the plots are created, those points used in the plot are set to 1,\n"
                "   so that at the end the database records which values have been plotted.\n"
                "   This information can then be used to make a symbol legend.\n"
                "   If the \"Plotted\" channel does not exist, it is created, associated,\n"
                "   loaded, and filled with dummies.\n\n"
               ).staticmethod("reset_used_channel");
    pyClass.def("select_poly", &GXSEMPLOT_wrap_select_poly,
                "select_poly((GXDB)arg1, (GXMVIEW)arg2, (str)arg3, (str)arg4, (GXPLY)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Select data from a polygonal area on a map.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: View Handle\n"
                ":type arg2: :class:`geosoft.gxapi.GXMVIEW`\n"
                ":param arg3: Mask channel to update\n"
                ":type arg3: str\n"
                ":param arg4: Mineral channel\n"
                ":type arg4: str\n"
                ":param arg5: Polygon to select from, in the view coordinates.\n"
                ":type arg5: :class:`geosoft.gxapi.GXPLY`\n"
                ":param arg6: Mask mode (0: Append, 1: New)\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("select_poly");
    pyClass.def("set_channel_order", &GXSEMPLOT_wrap_set_channel_order,
                "set_channel_order((GXDB)arg1, (GXLST)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sets preset channel order.\n\n"

                ":param arg1: database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: channel names, handles\n"
                ":type arg2: :class:`geosoft.gxapi.GXLST`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Sets channel order as follows:\n"
                "   \n"
                "   Sample_No\n"
                "   X and Y Locations\n"
                "   Mineral\n"
                "   Grain_No\n"
                "   Position (e.g. center, edge etc.)\n"
                "   Grain Morph\n"
                "   Oxides (in the order they appear in Semplot_Oxides.csv)\n"
                "   Trace Elements (Ordered as in the periodic table)\n"
                "   Total\n"
                "   Mask\n"
                "   IsPlotted (flag set when a value is plotted)\n"
                "   Other channels\n"
                "   \n"
                "   Channel order is set for all \"RawData\" groups.\n\n"
               ).staticmethod("set_channel_order");
    pyClass.def("set_channel_units", &GXSEMPLOT_wrap_set_channel_units,
                "set_channel_units((GXDB)arg1) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set units for oxides (%) and elements (ppm)\n\n"

                ":param arg1: database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   If the channel units are already set, then they are not changed.\n"
                "   Oxide channels are identified from the Semplot_Oxides.csv file.\n"
                "   Trace elements are identified from the periodic table of the\n"
                "   elements, except for \"Y\", if it is the current Y channel.\n\n"
               ).staticmethod("set_channel_units");
    pyClass.def("set_itr", &GXSEMPLOT_wrap_set_itr,
                "set_itr((GXDB)arg1, (int)arg2, (GXITR)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Put ITR into a channel.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Data channel handle\n"
                ":type arg2: int\n"
                ":param arg3: ITR\n"
                ":type arg3: :class:`geosoft.gxapi.GXITR`\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("set_itr");
    pyClass.def("set_mask", &GXSEMPLOT_wrap_set_mask,
                "set_mask((GXDB)arg1, (str)arg2, (str)arg3, (str)arg4, (int)arg5, (int)arg6) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Set the mask channel ON or OFF.\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Mask channel\n"
                ":type arg2: str\n"
                ":param arg3: Mineral channel\n"
                ":type arg3: str\n"
                ":param arg4: Mineral to use (\"All\" or \"\" for all)\n"
                ":type arg4: str\n"
                ":param arg5: 0 for all lines, 1 for selected lines\n"
                ":type arg5: int\n"
                ":param arg6: 0 for off, 1 for on.\n"
                ":type arg6: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("set_mask");
    pyClass.def("sort_data", &GXSEMPLOT_wrap_sort_data,
                "sort_data((GXDB)arg1, (int)arg2, (int)arg3) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Sort data by Sample No, Grain and Position\n\n"

                ":param arg1: Database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Data Group handle\n"
                ":type arg2: int\n"
                ":param arg3: Use Anomaly channel as primary sort?\n"
                ":type arg3: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("sort_data");
    pyClass.def("template_lst", &GXSEMPLOT_wrap_template_lst,
                "template_lst((GXLST)arg1, (int)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Fill a list with the available plot template names\n\n"

                ":param arg1: Input LST.\n"
                ":type arg1: :class:`geosoft.gxapi.GXLST`\n"
                ":param arg2: \\ :ref:`SEMPLOT_PLOT`\\ \n"
                ":type arg2: int\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   Looks first in user\\etc, then in \\etc.\n"
                "   Looks first for file prefix \"semtemplate\" then \"xyt\" or \"tri\"\n"
                "   (New-style templates with the \"semtemplate\" extentsion have the\n"
                "   plot type \"triplot\" or \"xyplot\" inside them.)\n\n"
               ).staticmethod("template_lst");
    pyClass.def("tile_windows", &GXSEMPLOT_wrap_tile_windows,
                "tile_windows() -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Tile currently maximimized windows.\n\n"

                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"
               ).staticmethod("tile_windows");
    pyClass.def("total_oxides", &GXSEMPLOT_wrap_total_oxides,
                "total_oxides((GXDB)arg1, (str)arg2) -> None:\n"

                "\n.. parsed-literal::\n\n"
                "   Calculate the total oxides channel.\n\n"

                ":param arg1: database handle\n"
                ":type arg1: :class:`geosoft.gxapi.GXDB`\n"
                ":param arg2: Mineral channel\n"
                ":type arg2: str\n"
                ":returns: Nothing\n"
                ":rtype: None\n"
                "\n"

                "\n.. versionadded:: 6.2.0\n\n"

                "\n\n**Note:**\n\n"

                "\n.. parsed-literal::\n\n"
                "   The mineral channel is needed in order to adjust the total\n"
                "   with the Fe Corrected Ferric and Ferrous values, and these\n"
                "   require a mineral for their identification. If none is provided,\n"
                "   mineral \"X\" (unknown) is assumed.\n\n"
               ).staticmethod("total_oxides");

    scope().attr("SEMPLOT_GROUP_CLASS") = "Semplot";
    scope().attr("SEMPLOT_EXPORT_NORMAL") = (int32_t)0;
    scope().attr("SEMPLOT_EXPORT_NOEXTRA") = (int32_t)1;
    scope().attr("SEMPLOT_EXT_ALL") = (int32_t)0;
    scope().attr("SEMPLOT_EXT_SEMPLOT") = (int32_t)1;
    scope().attr("SEMPLOT_EXT_CHIMERA") = (int32_t)2;
    scope().attr("SEMPLOT_PLOT_ALL") = (int32_t)0;
    scope().attr("SEMPLOT_PLOT_XYPLOT") = (int32_t)1;
    scope().attr("SEMPLOT_PLOT_TRIPLOT") = (int32_t)2;
    scope().attr("SEMPLOT_PLOT_UNKNOWN") = (int32_t)3;

}
