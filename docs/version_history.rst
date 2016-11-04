geosoft.gxapi module history
==============================

  
Version 9.1
-----------------

New Classes
^^^^^^^^^^^

:exc:`geosoft.gxapi.GXAPIError`

:exc:`geosoft.gxapi.GXCancel`

:exc:`geosoft.gxapi.GXError`

:exc:`geosoft.gxapi.GXExit`


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXContext.clear_ui_console`

:func:`geosoft.gxapi.GXContext.create`

:func:`geosoft.gxapi.GXContext.current`

:func:`geosoft.gxapi.GXContext.enable_application_windows`

:func:`geosoft.gxapi.GXContext.get_active_wnd_id`

:func:`geosoft.gxapi.GXContext.get_main_wnd_id`

:func:`geosoft.gxapi.GXContext.has_ui_console`

:func:`geosoft.gxapi.GXContext.show_ui_console`

:func:`geosoft.gxapi.GXDB.valid_symb`

:func:`geosoft.gxapi.GXDH.plot_symbols_3d`

:func:`geosoft.gxapi.GXDU.get_xyz_num_fields`

:func:`geosoft.gxapi.GXDU.import_bin4`

:func:`geosoft.gxapi.GXDU.table_selected_lines_fid`

:func:`geosoft.gxapi.GXEMAP.draw_rect_3d`

:func:`geosoft.gxapi.GXEMAP.get_point_3d`

:func:`geosoft.gxapi.GXEMAP.get_view_ipj`

:func:`geosoft.gxapi.GXIPGUI.launch_offset_ipqc_tool`

:func:`geosoft.gxapi.GXMVIEW.get_3d_group_flags`

:func:`geosoft.gxapi.GXMVIEW.set_3d_group_flags`

:func:`geosoft.gxapi.GXSYS.filter_parm_group`


  
Version 9.0.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDATALINKD.create_arc_lyr_ex`

:func:`geosoft.gxapi.GXDATALINKD.create_arc_lyr_from_tmp_ex`

:func:`geosoft.gxapi.GXDB.get_line_selection`

:func:`geosoft.gxapi.GXDB.set_line_selection`

:func:`geosoft.gxapi.GXDBWRITE.add_block`

:func:`geosoft.gxapi.GXDBWRITE.add_channel`

:func:`geosoft.gxapi.GXDBWRITE.commit`

:func:`geosoft.gxapi.GXDBWRITE.create_xy`

:func:`geosoft.gxapi.GXDBWRITE.create_xyz`

:func:`geosoft.gxapi.GXDBWRITE.create`

:func:`geosoft.gxapi.GXDBWRITE.get_chan_array_size`

:func:`geosoft.gxapi.GXDBWRITE.get_db`

:func:`geosoft.gxapi.GXDBWRITE.get_v_vx`

:func:`geosoft.gxapi.GXDBWRITE.get_v_vy`

:func:`geosoft.gxapi.GXDBWRITE.get_v_vz`

:func:`geosoft.gxapi.GXDBWRITE.get_va`

:func:`geosoft.gxapi.GXDBWRITE.get_vv`

:func:`geosoft.gxapi.GXDBWRITE.test_func`

:func:`geosoft.gxapi.GXDU.split_line_by_direction2`

:func:`geosoft.gxapi.GXDU.split_line_xy3`

:func:`geosoft.gxapi.GXEDB.current_no_activate`

:func:`geosoft.gxapi.GXEDB.get_window_position`

:func:`geosoft.gxapi.GXEDB.set_window_position`

:func:`geosoft.gxapi.GXEDOC.current_no_activate`

:func:`geosoft.gxapi.GXEDOC.get_window_position`

:func:`geosoft.gxapi.GXEDOC.load_no_activate`

:func:`geosoft.gxapi.GXEDOC.set_window_position`

:func:`geosoft.gxapi.GXEMAP.current_no_activate`

:func:`geosoft.gxapi.GXEMAP.digitize_peaks`

:func:`geosoft.gxapi.GXEMAP.get_window_position`

:func:`geosoft.gxapi.GXEMAP.reload_grid`

:func:`geosoft.gxapi.GXEMAP.set_window_position`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.current_no_activate`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.get_window_position`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.set_window_position`

:func:`geosoft.gxapi.GXEUL3.ex_euler_calc`

:func:`geosoft.gxapi.GXEUL3.ex_euler_derive`

:func:`geosoft.gxapi.GXGUI.coord_sys_wizard_grid`

:func:`geosoft.gxapi.GXGUI.get_client_window_area`

:func:`geosoft.gxapi.GXGUI.get_window_position`

:func:`geosoft.gxapi.GXGUI.get_window_state`

:func:`geosoft.gxapi.GXGUI.launch_geo_dotnetx_tool_ex`

:func:`geosoft.gxapi.GXGUI.launch_geo_x_tool_ex`

:func:`geosoft.gxapi.GXGUI.launch_single_geo_dotnetx_tool_ex`

:func:`geosoft.gxapi.GXGUI.set_window_position`

:func:`geosoft.gxapi.GXGUI.set_window_state`

:func:`geosoft.gxapi.GXIMU.get_z_peaks_vv`

:func:`geosoft.gxapi.GXIP.get_electrode_locations_and_mask_values`

:func:`geosoft.gxapi.GXIP.set_electrode_mask_values`

:func:`geosoft.gxapi.GXIPJ.reproject_section_grid`

:func:`geosoft.gxapi.GXIPJ.set_3d_view_from_axes`

:func:`geosoft.gxapi.GXLPT.get_standard_lst`

:func:`geosoft.gxapi.GXMVIEW.is_projection_empty`

:func:`geosoft.gxapi.GXMXD.convert_to_map`

:func:`geosoft.gxapi.GXSYS.check_arc_license_ex`

:func:`geosoft.gxapi.GXSYS.decrypt_string`

:func:`geosoft.gxapi.GXSYS.encrypt_string`

:func:`geosoft.gxapi.GXSYS.get_entitlement_rights`

:func:`geosoft.gxapi.GXSYS.get_loaded_menus`

:func:`geosoft.gxapi.GXSYS.is_encrypted_string`

:func:`geosoft.gxapi.GXSYS.set_loaded_menus`

:func:`geosoft.gxapi.GXVVU.offset_correct_xyz`

:func:`geosoft.gxapi.GXVVU.tokenize_to_values`


  
Version 8.5.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDBREAD.add_channel`

:func:`geosoft.gxapi.GXDBREAD.create_xy`

:func:`geosoft.gxapi.GXDBREAD.create_xyz`

:func:`geosoft.gxapi.GXDBREAD.create`

:func:`geosoft.gxapi.GXDBREAD.get_chan_array_size`

:func:`geosoft.gxapi.GXDBREAD.get_next_block`

:func:`geosoft.gxapi.GXDBREAD.get_number_of_blocks_to_process`

:func:`geosoft.gxapi.GXDBREAD.get_v_vx`

:func:`geosoft.gxapi.GXDBREAD.get_v_vy`

:func:`geosoft.gxapi.GXDBREAD.get_v_vz`

:func:`geosoft.gxapi.GXDBREAD.get_va`

:func:`geosoft.gxapi.GXDBREAD.get_vv`

:func:`geosoft.gxapi.GXDU.import_io_gas`

:func:`geosoft.gxapi.GXDU.range_xy`

:func:`geosoft.gxapi.GXDU.range_xyz`

:func:`geosoft.gxapi.GXDU.split_line_by_direction`

:func:`geosoft.gxapi.GXFFT.rc_filter`

:func:`geosoft.gxapi.GXGU.gravity_still_reading_correction`

:func:`geosoft.gxapi.GXIPJ.get_3d_matrix_orientation`

:func:`geosoft.gxapi.GXIPJ.set_3d_matrix_orientation`

:func:`geosoft.gxapi.GXMVIEW.hide_shadow2_d_interpretations`

:func:`geosoft.gxapi.GXMVU.generate_surface_from_voxel`

:func:`geosoft.gxapi.GXPDF3D.export2_d`

:func:`geosoft.gxapi.GXPROJ.add_document_without_opening`

:func:`geosoft.gxapi.GXSURFACE.get_extents`

:func:`geosoft.gxapi.GXSURFACEITEM.compute_extended_info`

:func:`geosoft.gxapi.GXSURFACEITEM.get_extents`

:func:`geosoft.gxapi.GXSURFACEITEM.get_geometry_info`

:func:`geosoft.gxapi.GXSURFACEITEM.get_info`

:func:`geosoft.gxapi.GXSURFACEITEM.get_properties_ex`

:func:`geosoft.gxapi.GXSURFACEITEM.set_properties_ex`

:func:`geosoft.gxapi.GXVOX.add_generate_by_subset_pg`

:func:`geosoft.gxapi.GXVOX.end_generate_by_subset_pg`

:func:`geosoft.gxapi.GXVOX.export_seg_y`

:func:`geosoft.gxapi.GXVOX.generate_vector_voxel_from_db`

:func:`geosoft.gxapi.GXVOX.init_generate_by_subset_pg`

:func:`geosoft.gxapi.GXVOX.tin_grid_db`


  
Version 8.4.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDU.break_line2`

:func:`geosoft.gxapi.GXDU.break_line_to_groups2`

:func:`geosoft.gxapi.GXDU.calculate_draped_survey_altitude2`

:func:`geosoft.gxapi.GXDU.direct_grid_data_to_voxel`

:func:`geosoft.gxapi.GXDU.direct_grid_item_counts_to_voxel`

:func:`geosoft.gxapi.GXDU.interp_gap`

:func:`geosoft.gxapi.GXDU.split_line2`

:func:`geosoft.gxapi.GXDU.split_line_xy2`

:func:`geosoft.gxapi.GXDU.xyz_line3`

:func:`geosoft.gxapi.GXGEOSTRING.get_all_shapes`

:func:`geosoft.gxapi.GXGEOSTRING.get_feature_properties`

:func:`geosoft.gxapi.GXGEOSTRING.get_features`

:func:`geosoft.gxapi.GXGEOSTRING.get_ipj`

:func:`geosoft.gxapi.GXGEOSTRING.get_section_properties`

:func:`geosoft.gxapi.GXGEOSTRING.get_sections`

:func:`geosoft.gxapi.GXGEOSTRING.get_shape_properties`

:func:`geosoft.gxapi.GXGEOSTRING.get_shapes_for_feature_and_section`

:func:`geosoft.gxapi.GXGEOSTRING.get_shapes_for_feature`

:func:`geosoft.gxapi.GXGEOSTRING.get_shapes_for_section`

:func:`geosoft.gxapi.GXGEOSTRING.open`

:func:`geosoft.gxapi.GXPROJ.get_name`

:func:`geosoft.gxapi.GXSURFACE.add_surface_item`

:func:`geosoft.gxapi.GXSURFACE.append_vulcan_triangulation`

:func:`geosoft.gxapi.GXSURFACE.create_from_vulcan_triangulation`

:func:`geosoft.gxapi.GXSURFACE.create`

:func:`geosoft.gxapi.GXSURFACE.get_ipj`

:func:`geosoft.gxapi.GXSURFACE.get_surface_item`

:func:`geosoft.gxapi.GXSURFACE.get_surface_items`

:func:`geosoft.gxapi.GXSURFACE.open`

:func:`geosoft.gxapi.GXSURFACE.set_ipj`

:func:`geosoft.gxapi.GXSURFACEITEM.add_mesh`

:func:`geosoft.gxapi.GXSURFACEITEM.create`

:func:`geosoft.gxapi.GXSURFACEITEM.get_default_render_properties`

:func:`geosoft.gxapi.GXSURFACEITEM.get_guid`

:func:`geosoft.gxapi.GXSURFACEITEM.get_mesh_info`

:func:`geosoft.gxapi.GXSURFACEITEM.get_mesh`

:func:`geosoft.gxapi.GXSURFACEITEM.get_properties`

:func:`geosoft.gxapi.GXSURFACEITEM.num_components`

:func:`geosoft.gxapi.GXSURFACEITEM.set_default_render_properties`

:func:`geosoft.gxapi.GXSURFACEITEM.set_properties`

:func:`geosoft.gxapi.GXSYS.generate_guid`

:func:`geosoft.gxapi.GXTIN.get_triangles`

:func:`geosoft.gxapi.GXVOX.convert_density_to_velocity`

:func:`geosoft.gxapi.GXVOX.convert_numeric_to_thematic`

:func:`geosoft.gxapi.GXVOX.convert_thematic_to_numeric`

:func:`geosoft.gxapi.GXVOX.convert_velocity_in_range_to_density`

:func:`geosoft.gxapi.GXVOX.convert_velocity_to_density`

:func:`geosoft.gxapi.GXVOX.dw_grid_db`

:func:`geosoft.gxapi.GXVOX.export_ji_gs_xml`

:func:`geosoft.gxapi.GXVOX.generate_constant_value_vv`

:func:`geosoft.gxapi.GXVOX.generate_constant_value`

:func:`geosoft.gxapi.GXVOX.invert_z`

:func:`geosoft.gxapi.GXVOX.slice_multi_layer_ipj`

:func:`geosoft.gxapi.GXVULCAN.block_model_to_voxel`

:func:`geosoft.gxapi.GXVULCAN.get_block_model_string_variable_values`

:func:`geosoft.gxapi.GXVULCAN.get_block_model_variable_info`

:func:`geosoft.gxapi.GXVULCAN.is_valid_block_model_file`

:func:`geosoft.gxapi.GXVULCAN.is_valid_triangulation_file`

:func:`geosoft.gxapi.GXVULCAN.triangulation_to_view`


  
Version 8.3.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXCHIMERA.duplicate_chem_view`

:func:`geosoft.gxapi.GXCHIMERA.standard_view`

:func:`geosoft.gxapi.GXDH.modify_hole_traces_gui2`

:func:`geosoft.gxapi.GXDH.plot_holes_on_section`

:func:`geosoft.gxapi.GXDH.surface_intersections`

:func:`geosoft.gxapi.GXDU.calculate_draped_survey_altitude`

:func:`geosoft.gxapi.GXDU.sample_img_line_lst`

:func:`geosoft.gxapi.GXDU.split_line_xy`

:func:`geosoft.gxapi.GXEDB.get_window_y_axis_direction`

:func:`geosoft.gxapi.GXGUI.import_drill_database_odbc_maxwell`

:func:`geosoft.gxapi.GXIPJ.has_section_orientation`

:func:`geosoft.gxapi.GXMAP.get_data_proj`

:func:`geosoft.gxapi.GXMSTK.set_y_axis_direction`

:func:`geosoft.gxapi.GXMVU.mapset2_test`

:func:`geosoft.gxapi.GXMVU.mapset2`

:func:`geosoft.gxapi.GXPG.get`


  
Version 8.2
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXAGG.layer_img_ex`

:func:`geosoft.gxapi.GXARCDH.s_prompt_for_esri_symbol`

:func:`geosoft.gxapi.GXDB.array_size_lst`

:func:`geosoft.gxapi.GXDB.get_va_base_coordinate_info`

:func:`geosoft.gxapi.GXDB.normal_chan_lst`

:func:`geosoft.gxapi.GXDB.set_va_base_coordinate_info`

:func:`geosoft.gxapi.GXDH.get_databases_sorted_vv`

:func:`geosoft.gxapi.GXDU.create_drillhole_parameter_weight_constraint_database`

:func:`geosoft.gxapi.GXEDB.get_mark_chan_va`

:func:`geosoft.gxapi.GXHTTP.silent_download`

:func:`geosoft.gxapi.GXIMG.get_double_parameter`

:func:`geosoft.gxapi.GXIMG.set_double_parameter`

:func:`geosoft.gxapi.GXIMU.slope_standard_deviation`

:func:`geosoft.gxapi.GXITR.save_file`

:func:`geosoft.gxapi.GXLTB.get_english_string`

:func:`geosoft.gxapi.GXMVIEW.get_voxd`

:func:`geosoft.gxapi.GXMVIEW.is_section`

:func:`geosoft.gxapi.GXMVU.color_bar_reg`

:func:`geosoft.gxapi.GXSURFACE.create_from_dxf`

:func:`geosoft.gxapi.GXUSERMETA.save_file_lineage`

:func:`geosoft.gxapi.GXVA.check_for_repeating2`

:func:`geosoft.gxapi.GXVA.check_for_repeating`

:func:`geosoft.gxapi.GXVOX.is_vector_voxel`

:func:`geosoft.gxapi.GXVOX.krig`

:func:`geosoft.gxapi.GXVOX.sample_cdi_to_topography`

:func:`geosoft.gxapi.GXVOX.sample_vv`

:func:`geosoft.gxapi.GXVOXD.get_name`


  
Version 8.1.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDB.get_channel_length`

:func:`geosoft.gxapi.GXDU.distance_3d`

:func:`geosoft.gxapi.GXDU.range_xyz_data`

:func:`geosoft.gxapi.GXGUI.line_pattern_form`

:func:`geosoft.gxapi.GXGUI.render_line_pattern`

:func:`geosoft.gxapi.GXIP.a_spacing`

:func:`geosoft.gxapi.GXIP.export_ubc_res3`

:func:`geosoft.gxapi.GXIP.export_ubc_res_control_v5`

:func:`geosoft.gxapi.GXIP.export_ubcip3`

:func:`geosoft.gxapi.GXIP.export_ubcip_control_v5`

:func:`geosoft.gxapi.GXIP.get_channel_info`

:func:`geosoft.gxapi.GXIP.is_valid_line`

:func:`geosoft.gxapi.GXIP.line_array_type`

:func:`geosoft.gxapi.GXIP.pldp_convention`

:func:`geosoft.gxapi.GXIP.set_channel_info`

:func:`geosoft.gxapi.GXIPGUI.ipqc_tool_exists`

:func:`geosoft.gxapi.GXIPGUI.launch_ipqc_tool`

:func:`geosoft.gxapi.GXTR.copy`

:func:`geosoft.gxapi.GXVVU.find_gaps_3d`


  
Version 8.0.1
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXARCDH.geostrings_extension_available`

:func:`geosoft.gxapi.GXARCDH.get_current_string_file_gdb`

:func:`geosoft.gxapi.GXARCDH.has_string_file_gdb_edits`

:func:`geosoft.gxapi.GXARCDH.is_valid_feature_class_name`

:func:`geosoft.gxapi.GXARCDH.is_valid_fgdb_file_name`

:func:`geosoft.gxapi.GXARCDH.stop_editing_string_file_gdb`

:func:`geosoft.gxapi.GXARCMAP.get_ipj_for_predefined_esri_gcs`

:func:`geosoft.gxapi.GXARCMAP.get_ipj_for_predefined_esri_pcs`

:func:`geosoft.gxapi.GXCHIMERA.fixed_symbol_scatter_plot`

:func:`geosoft.gxapi.GXCHIMERA.fixed_symbol_tri_plot`

:func:`geosoft.gxapi.GXCHIMERA.plot_string_classified_symbols_legend_from_class_file`

:func:`geosoft.gxapi.GXCHIMERA.string_classified_scatter_plot`

:func:`geosoft.gxapi.GXCHIMERA.string_classified_tri_plot`

:func:`geosoft.gxapi.GXCHIMERA.zone_coloured_scatter_plot`

:func:`geosoft.gxapi.GXCHIMERA.zone_coloured_tri_plot`

:func:`geosoft.gxapi.GXDH.get_map`

:func:`geosoft.gxapi.GXDH.get_num_maps`

:func:`geosoft.gxapi.GXGU.gr_curv_cor_ex`

:func:`geosoft.gxapi.GXIMG.is_valid_img_file_ex`

:func:`geosoft.gxapi.GXMVIEW.draw_vectors_3d`

:func:`geosoft.gxapi.GXVV.amplitude_3d`

:func:`geosoft.gxapi.GXVVU.average_repeat2_ex`

:func:`geosoft.gxapi.GXVVU.average_repeat_ex`

:func:`geosoft.gxapi.GXVVU.distance_3d`


  
Version 8.0.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GX3DV.copy_to_map`

:func:`geosoft.gxapi.GX3DV.crc_3dv`

:func:`geosoft.gxapi.GX3DV.create_new`

:func:`geosoft.gxapi.GX3DV.open_mview`

:func:`geosoft.gxapi.GX3DV.open`

:func:`geosoft.gxapi.GXARCDB.create_dat_3d`

:func:`geosoft.gxapi.GXARCDB.create_dat`

:func:`geosoft.gxapi.GXARCDB.current`

:func:`geosoft.gxapi.GXARCDB.exist_field`

:func:`geosoft.gxapi.GXARCDB.export_to_db`

:func:`geosoft.gxapi.GXARCDB.field_lst`

:func:`geosoft.gxapi.GXARCDB.from_i_unknown`

:func:`geosoft.gxapi.GXARCDB.get_i_unknown`

:func:`geosoft.gxapi.GXARCDB.get_ipj`

:func:`geosoft.gxapi.GXARCDB.import_chem_database_wizard`

:func:`geosoft.gxapi.GXARCDB.sel_tbl_ex_gui`

:func:`geosoft.gxapi.GXARCDB.sel_tbl_gui`

:func:`geosoft.gxapi.GXARCDH.close_project`

:func:`geosoft.gxapi.GXARCDH.set_project`

:func:`geosoft.gxapi.GXARCDH.set_string_file_gdb`

:func:`geosoft.gxapi.GXARCMAP.change_size`

:func:`geosoft.gxapi.GXARCMAP.display_in_3d_view`

:func:`geosoft.gxapi.GXARCMAP.export_feature_layer_by_name_to_3d_file`

:func:`geosoft.gxapi.GXARCMAP.export_selected_feature_layer_to_3d_file`

:func:`geosoft.gxapi.GXARCMAP.get_current_document_info`

:func:`geosoft.gxapi.GXARCMAP.get_load_map`

:func:`geosoft.gxapi.GXARCMAP.get_load_shape`

:func:`geosoft.gxapi.GXARCMAP.get_number_of_selected_layers`

:func:`geosoft.gxapi.GXARCMAP.get_selected_layer_info`

:func:`geosoft.gxapi.GXARCMAP.load_lyr`

:func:`geosoft.gxapi.GXARCMAP.load_map_ex`

:func:`geosoft.gxapi.GXARCMAP.load_map_view`

:func:`geosoft.gxapi.GXARCMAP.load_map`

:func:`geosoft.gxapi.GXARCMAP.load_raster`

:func:`geosoft.gxapi.GXARCMAP.load_shape`

:func:`geosoft.gxapi.GXARCMAP.load_spf`

:func:`geosoft.gxapi.GXARCMAP.map_view_to_shape`

:func:`geosoft.gxapi.GXARCMAP.query_size`

:func:`geosoft.gxapi.GXARCMAP.show_layer_by_name_in_3d`

:func:`geosoft.gxapi.GXARCMAP.show_selected_layers_in_3d`

:func:`geosoft.gxapi.GXARCSYS.get_browse_loc`

:func:`geosoft.gxapi.GXARCSYS.get_current_doc`

:func:`geosoft.gxapi.GXARCSYS.set_browse_loc`

:func:`geosoft.gxapi.GXDATALINKD.create_bing`

:func:`geosoft.gxapi.GXDH.get_selected_holes_vv`

:func:`geosoft.gxapi.GXDH.set_selected_holes_vv`

:func:`geosoft.gxapi.GXDSEL.set_extract_as_document`

:func:`geosoft.gxapi.GXDU.export_geodatabase`

:func:`geosoft.gxapi.GXDU.get_existing_feature_classes_in_geodatabase`

:func:`geosoft.gxapi.GXIMG.is_valid_img_file`

:func:`geosoft.gxapi.GXIP.import_instrumentation_gdd`

:func:`geosoft.gxapi.GXIP.recalculate_ex`

:func:`geosoft.gxapi.GXPG.copy_subset_3d`

:func:`geosoft.gxapi.GXPGU.direct_gridding_dat_3d`

:func:`geosoft.gxapi.GXPGU.direct_gridding_db_3d`

:func:`geosoft.gxapi.GXPGU.dw_gridding_dat_3d`

:func:`geosoft.gxapi.GXPGU.dw_gridding_db_3d`

:func:`geosoft.gxapi.GXSURFACE.crc`

:func:`geosoft.gxapi.GXSURFACE.get_closed_surface_names`

:func:`geosoft.gxapi.GXSURFACE.get_surface_names`

:func:`geosoft.gxapi.GXSURFACE.sync`

:func:`geosoft.gxapi.GXSYS.get_top_error_ap`

:func:`geosoft.gxapi.GXVOX.can_append_to`

:func:`geosoft.gxapi.GXVOX.generate_pgvv`

:func:`geosoft.gxapi.GXVOX.resample_pg`

:func:`geosoft.gxapi.GXVV.lines_to_xy`

:func:`geosoft.gxapi.GXVV.write_xml`


  
Version 7.6.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXMVIEW.draw_vector_voxel_vectors`


  
Version 7.5.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXSTRINGS.launch_digitization_ui`


  
Version 7.3.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDAT.range_xyz`

:func:`geosoft.gxapi.GXDH.compute_hole_xyz`

:func:`geosoft.gxapi.GXDH.get_chan_code_info`

:func:`geosoft.gxapi.GXDH.get_table_default_chan_lst`

:func:`geosoft.gxapi.GXDH.get_template_info_ex`

:func:`geosoft.gxapi.GXDH.get_unique_channel_items_from_collar`

:func:`geosoft.gxapi.GXDH.grid_intersection`

:func:`geosoft.gxapi.GXGIS.load_ascii`

:func:`geosoft.gxapi.GXIMG.user_preference_to_plot_as_colour_shaded_grid`

:func:`geosoft.gxapi.GXIMU.grid_reproject_and_window`

:func:`geosoft.gxapi.GXIMU.grid_resample`

:func:`geosoft.gxapi.GXIP.average_duplicates_qc`

:func:`geosoft.gxapi.GXIP.qc_chan_lst`

:func:`geosoft.gxapi.GXIPJ.get_north_azimuth`

:func:`geosoft.gxapi.GXMAP.un_pack_files_to_folder`

:func:`geosoft.gxapi.GXMISC.convert_cg3to_raw`

:func:`geosoft.gxapi.GXMISC.convert_cg5to_raw`

:func:`geosoft.gxapi.GXMVU.plot_voxel_surface2`

:func:`geosoft.gxapi.GXPGU.direct_gridding_dat`

:func:`geosoft.gxapi.GXPGU.direct_gridding_db`

:func:`geosoft.gxapi.GXPGU.direct_gridding_vv`

:func:`geosoft.gxapi.GXPGU.dw_gridding_dat`

:func:`geosoft.gxapi.GXPGU.dw_gridding_db`

:func:`geosoft.gxapi.GXPGU.dw_gridding_vv`

:func:`geosoft.gxapi.GXPGU.numeric_to_thematic`

:func:`geosoft.gxapi.GXPGU.thematic_to_numeric`

:func:`geosoft.gxapi.GXPJ.convert_xy_from_xyz`

:func:`geosoft.gxapi.GXSTR.printf`

:func:`geosoft.gxapi.GXTPAT.setup_translation_vv`

:func:`geosoft.gxapi.GXVOX.export_to_grids`

:func:`geosoft.gxapi.GXVOX.filter`

:func:`geosoft.gxapi.GXVOX.merge`

:func:`geosoft.gxapi.GXVOX.re_grid`

:func:`geosoft.gxapi.GXVOX.rescale_cell_sizes`

:func:`geosoft.gxapi.GXVOX.subset_to_double_extents`

:func:`geosoft.gxapi.GXVOX.window_ply`

:func:`geosoft.gxapi.GXVOX.window_xyz`

:func:`geosoft.gxapi.GXVV.inv_log`

:func:`geosoft.gxapi.GXVVU.find_string_items`


  
Version 7.2.1
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXVA.create_vv`


  
Version 7.2.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXCHIMERA.is_acquire_chan`

:func:`geosoft.gxapi.GXDB.is_chan_name`

:func:`geosoft.gxapi.GXDH.modify_crooked_section_holes_gui`

:func:`geosoft.gxapi.GXDH.numeric_chan_lst`

:func:`geosoft.gxapi.GXDH.numeric_from_to_data_lst`

:func:`geosoft.gxapi.GXDH.set_crooked_section_ipj`

:func:`geosoft.gxapi.GXDH.set_current_view_name`

:func:`geosoft.gxapi.GXDH.significant_intersections_db`

:func:`geosoft.gxapi.GXDH.slice_selection_tool_gui`

:func:`geosoft.gxapi.GXDH.string_chan_lst`

:func:`geosoft.gxapi.GXDH.string_from_to_data_lst`

:func:`geosoft.gxapi.GXDU.import_daarc500_serial_gps`

:func:`geosoft.gxapi.GXDU.import_daarc500_serial`

:func:`geosoft.gxapi.GXFFT2.rad_spc1`

:func:`geosoft.gxapi.GXFFT2.rad_spc2`

:func:`geosoft.gxapi.GXGU.import_daarc500_ethernet`

:func:`geosoft.gxapi.GXGU.import_daarc500_serial`

:func:`geosoft.gxapi.GXGU.lag_daarc500_gps`

:func:`geosoft.gxapi.GXGU.scan_daarc500_ethernet`

:func:`geosoft.gxapi.GXGU.scan_daarc500_serial`

:func:`geosoft.gxapi.GXHTTP.set_proxy_credentials`

:func:`geosoft.gxapi.GXIMU.export_grid_without_data_section_xml`

:func:`geosoft.gxapi.GXIMU.grid_exp_fill`

:func:`geosoft.gxapi.GXIMU.grid_in_fill`

:func:`geosoft.gxapi.GXIPJ.clear_coordinate_system`

:func:`geosoft.gxapi.GXIPJ.coordinate_systems_are_the_same_within_a_small_tolerance`

:func:`geosoft.gxapi.GXIPJ.coordinate_systems_are_the_same`

:func:`geosoft.gxapi.GXIPJ.get_crooked_section_view_v_vs`

:func:`geosoft.gxapi.GXIPJ.has_projection`

:func:`geosoft.gxapi.GXIPJ.orientations_are_the_same_within_a_small_tolerance`

:func:`geosoft.gxapi.GXIPJ.orientations_are_the_same`

:func:`geosoft.gxapi.GXIPJ.projection_type_is_fully_supported`

:func:`geosoft.gxapi.GXIPJ.set_crooked_section_view`

:func:`geosoft.gxapi.GXIPJ.warps_are_the_same_within_a_small_tolerance`

:func:`geosoft.gxapi.GXIPJ.warps_are_the_same`

:func:`geosoft.gxapi.GXMVIEW.create_crooked_section_data_profile`

:func:`geosoft.gxapi.GXMVIEW.create_crooked_section`

:func:`geosoft.gxapi.GXMVIEW.find_group`

:func:`geosoft.gxapi.GXMVIEW.get_group_freeze_scale`

:func:`geosoft.gxapi.GXMVIEW.get_map`

:func:`geosoft.gxapi.GXMVIEW.group_name`

:func:`geosoft.gxapi.GXMVIEW.set_freeze_scale`

:func:`geosoft.gxapi.GXMVIEW.set_group_freeze_scale`

:func:`geosoft.gxapi.GXMVU.cdi_pixel_plot_3d`

:func:`geosoft.gxapi.GXMVU.cdi_pixel_plot`

:func:`geosoft.gxapi.GXSHP.append_item`

:func:`geosoft.gxapi.GXSHP.max_id_num`

:func:`geosoft.gxapi.GXSHP.num_fields`

:func:`geosoft.gxapi.GXSHP.num_records`

:func:`geosoft.gxapi.GXSHP.open`

:func:`geosoft.gxapi.GXSHP.type`

:func:`geosoft.gxapi.GXSYS.exist_double`

:func:`geosoft.gxapi.GXSYS.exist_int`

:func:`geosoft.gxapi.GXSYS.exist_string`

:func:`geosoft.gxapi.GXSYS.prog_state`

:func:`geosoft.gxapi.GXUSERMETA.update_file_type`

:func:`geosoft.gxapi.GXVA.add_elevations_vv_to_depths`

:func:`geosoft.gxapi.GXVA.trans`

:func:`geosoft.gxapi.GXVOX.log_grid_points_z_ex`

:func:`geosoft.gxapi.GXVOX.sample_cdi`

:func:`geosoft.gxapi.GXVV.sum`

:func:`geosoft.gxapi.GXVV.weighted_mean`

:func:`geosoft.gxapi.GXVVU.distance_non_cumulative`

:func:`geosoft.gxapi.GXVVU.remove_xy_dup_index`


  
Version 7.1.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDH.export_geodatabase_lst`

:func:`geosoft.gxapi.GXDH.modify_plan_holes_gui`

:func:`geosoft.gxapi.GXDH.modify_section_holes_gui`

:func:`geosoft.gxapi.GXDH.open`

:func:`geosoft.gxapi.GXDH.replot_holes`

:func:`geosoft.gxapi.GXDH.set_map`

:func:`geosoft.gxapi.GXDH.update_survey_from_collar`

:func:`geosoft.gxapi.GXDU.gen_lev_db`

:func:`geosoft.gxapi.GXDU.import_esri`

:func:`geosoft.gxapi.GXDU.intersect_gd_bto_tbl`

:func:`geosoft.gxapi.GXDU.intersect_tb_lto_gdb`

:func:`geosoft.gxapi.GXDU.update_intersect_db`

:func:`geosoft.gxapi.GXGIS.create_map2_d`

:func:`geosoft.gxapi.GXGIS.get_bpr_models_lst`

:func:`geosoft.gxapi.GXGIS.get_file_name`

:func:`geosoft.gxapi.GXGIS.is_shp_file_point`

:func:`geosoft.gxapi.GXGIS.load_map_ex`

:func:`geosoft.gxapi.GXGIS.load_shapes_gdb`

:func:`geosoft.gxapi.GXGIS.num_attribs`

:func:`geosoft.gxapi.GXGIS.num_shapes`

:func:`geosoft.gxapi.GXGIS.set_lst`

:func:`geosoft.gxapi.GXGIS.set_triangulation_object_index`

:func:`geosoft.gxapi.GXGUI.gcs_datum_warning_shp_ex`

:func:`geosoft.gxapi.GXGUI.gcs_datum_warning_shp`

:func:`geosoft.gxapi.GXGUI.gcs_datum_warning_shpdb_ex`

:func:`geosoft.gxapi.GXIP.convert_ubcip2_d_to_grid`

:func:`geosoft.gxapi.GXIP.import_ubc2_d_topo`

:func:`geosoft.gxapi.GXIP.import_ubc2_dmod`

:func:`geosoft.gxapi.GXIP.import_ubc2_dmsh`

:func:`geosoft.gxapi.GXIP.trim_ubc2_d_model`

:func:`geosoft.gxapi.GXMAP.export_all_in_view`

:func:`geosoft.gxapi.GXMAP.export_all_raster`

:func:`geosoft.gxapi.GXMAP.export_area_in_view`

:func:`geosoft.gxapi.GXMAP.export_area_raster`

:func:`geosoft.gxapi.GXMVIEW.clear_esrild_ts`

:func:`geosoft.gxapi.GXMVU.exportable_dxf_3d_groups_lst`

:func:`geosoft.gxapi.GXPDF3D.render_to_page`

:func:`geosoft.gxapi.GXPGEXP.add_pager`

:func:`geosoft.gxapi.GXPGEXP.create`

:func:`geosoft.gxapi.GXPGEXP.do_formula`

:func:`geosoft.gxapi.GXPGU.add_scalar`

:func:`geosoft.gxapi.GXPGU.maximum_terrain_steepness`

:func:`geosoft.gxapi.GXPGU.multiply_scalar`

:func:`geosoft.gxapi.GXSEMPLOT.export_view2`

:func:`geosoft.gxapi.GXST.get_norm_prob_x`

:func:`geosoft.gxapi.GXST.get_norm_prob`

:func:`geosoft.gxapi.GXSYS.check_arc_license`

:func:`geosoft.gxapi.GXVV.abs`

:func:`geosoft.gxapi.GXVVU.binary_search`


  
Version 7.0.1
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDH.qa_collar_lst`

:func:`geosoft.gxapi.GXRGRD.create_img`

:func:`geosoft.gxapi.GXSTR.remove_qualifiers`

:func:`geosoft.gxapi.GXSTR.replace_match_string`

:func:`geosoft.gxapi.GXSTR.replacei_match_string`

:func:`geosoft.gxapi.GXSYS.remove_lineage_output`

:func:`geosoft.gxapi.GXUSERMETA.update_extents2_d`


  
Version 7.0.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDATALINKD.create_arc_lyr_from_tmp`

:func:`geosoft.gxapi.GXDB.del_line0`

:func:`geosoft.gxapi.GXDB.get_info`

:func:`geosoft.gxapi.GXDB.set_all_chan_protect`

:func:`geosoft.gxapi.GXDB.sync`

:func:`geosoft.gxapi.GXDH.chan_type`

:func:`geosoft.gxapi.GXDH.find_hole_intersection`

:func:`geosoft.gxapi.GXDH.get_geology_contacts`

:func:`geosoft.gxapi.GXDH.get_unique_channel_items`

:func:`geosoft.gxapi.GXDH.hole_select_from_list_gui`

:func:`geosoft.gxapi.GXDH.import2`

:func:`geosoft.gxapi.GXDH.litho_grid_3d`

:func:`geosoft.gxapi.GXDH.modify_fence_gui`

:func:`geosoft.gxapi.GXDH.punch_grid_holes`

:func:`geosoft.gxapi.GXDH.qa_dip_az_curvature_lst`

:func:`geosoft.gxapi.GXDH.qa_dip_az_survey_lst`

:func:`geosoft.gxapi.GXDH.qa_east_north_curvature_lst`

:func:`geosoft.gxapi.GXDH.qa_east_north_survey_lst`

:func:`geosoft.gxapi.GXDSEL.select_size`

:func:`geosoft.gxapi.GXGUI.file_filter_index`

:func:`geosoft.gxapi.GXGUI.get_dat_defaults`

:func:`geosoft.gxapi.GXGUI.get_file_filter`

:func:`geosoft.gxapi.GXGUI.get_gs_directory`

:func:`geosoft.gxapi.GXIMG.refresh_gi`

:func:`geosoft.gxapi.GXIMG.set_grid_unchanged`

:func:`geosoft.gxapi.GXIMG.sync`

:func:`geosoft.gxapi.GXIMU.export_raw_xml`

:func:`geosoft.gxapi.GXIPJ.add_log_warp`

:func:`geosoft.gxapi.GXIPJ.add_matrix_warp`

:func:`geosoft.gxapi.GXIPJ.copy_projection`

:func:`geosoft.gxapi.GXIPJ.create_xml`

:func:`geosoft.gxapi.GXIPJ.get_3d_view_ex`

:func:`geosoft.gxapi.GXIPJ.get_mi_coord_sys`

:func:`geosoft.gxapi.GXIPJ.get_xml`

:func:`geosoft.gxapi.GXIPJ.serial_fgdcxml`

:func:`geosoft.gxapi.GXIPJ.serial_isoxml`

:func:`geosoft.gxapi.GXIPJ.serial_xml`

:func:`geosoft.gxapi.GXIPJ.set_3d_view_ex`

:func:`geosoft.gxapi.GXIPJ.set_depth_section_view`

:func:`geosoft.gxapi.GXIPJ.set_gxf_safe`

:func:`geosoft.gxapi.GXIPJ.set_normal_section_view`

:func:`geosoft.gxapi.GXIPJ.set_xml`

:func:`geosoft.gxapi.GXIPJ.warp_type`

:func:`geosoft.gxapi.GXMAP.save_as_mxd`

:func:`geosoft.gxapi.GXMAP.sync`

:func:`geosoft.gxapi.GXMAPTEMPLATE.refresh`

:func:`geosoft.gxapi.GXMVIEW.draw_surface_3d_ex`

:func:`geosoft.gxapi.GXMVIEW.draw_surface_3d_from_file`

:func:`geosoft.gxapi.GXMXD.create_metadata`

:func:`geosoft.gxapi.GXMXD.sync`

:func:`geosoft.gxapi.GXSYS.add_lineage_parameter`

:func:`geosoft.gxapi.GXSYS.add_lineage_source`

:func:`geosoft.gxapi.GXSYS.backup_geo_file`

:func:`geosoft.gxapi.GXSYS.clear_lineage_parameters`

:func:`geosoft.gxapi.GXSYS.clear_lineage_sources`

:func:`geosoft.gxapi.GXSYS.copy_geo_file`

:func:`geosoft.gxapi.GXSYS.delete_grid_file`

:func:`geosoft.gxapi.GXSYS.remove_lineage_parameter`

:func:`geosoft.gxapi.GXSYS.remove_lineage_source`

:func:`geosoft.gxapi.GXSYS.restore_geo_file`

:func:`geosoft.gxapi.GXSYS.set_lineage_description`

:func:`geosoft.gxapi.GXSYS.set_lineage_display_name`

:func:`geosoft.gxapi.GXSYS.set_lineage_name`

:func:`geosoft.gxapi.GXSYS.utc_date`

:func:`geosoft.gxapi.GXSYS.utc_file_date`

:func:`geosoft.gxapi.GXSYS.utc_file_time`

:func:`geosoft.gxapi.GXSYS.utc_time`

:func:`geosoft.gxapi.GXTPAT.add_color`

:func:`geosoft.gxapi.GXTPAT.code`

:func:`geosoft.gxapi.GXTPAT.create`

:func:`geosoft.gxapi.GXTPAT.get_solid_pattern`

:func:`geosoft.gxapi.GXTPAT.load_csv`

:func:`geosoft.gxapi.GXTPAT.size`

:func:`geosoft.gxapi.GXUSERMETA.compare`

:func:`geosoft.gxapi.GXUSERMETA.create_s`

:func:`geosoft.gxapi.GXUSERMETA.create`

:func:`geosoft.gxapi.GXUSERMETA.get_data_creation_date`

:func:`geosoft.gxapi.GXUSERMETA.get_data_creator`

:func:`geosoft.gxapi.GXUSERMETA.get_extents2d`

:func:`geosoft.gxapi.GXUSERMETA.get_extents3d`

:func:`geosoft.gxapi.GXUSERMETA.get_format`

:func:`geosoft.gxapi.GXUSERMETA.get_ipj`

:func:`geosoft.gxapi.GXUSERMETA.get_meta_creation_date`

:func:`geosoft.gxapi.GXUSERMETA.get_meta_creator`

:func:`geosoft.gxapi.GXUSERMETA.get_project`

:func:`geosoft.gxapi.GXUSERMETA.get_title`

:func:`geosoft.gxapi.GXUSERMETA.get_xml_format`

:func:`geosoft.gxapi.GXUSERMETA.serial`

:func:`geosoft.gxapi.GXUSERMETA.set_data_creation_date`

:func:`geosoft.gxapi.GXUSERMETA.set_data_creator`

:func:`geosoft.gxapi.GXUSERMETA.set_extents2d`

:func:`geosoft.gxapi.GXUSERMETA.set_extents3d`

:func:`geosoft.gxapi.GXUSERMETA.set_format`

:func:`geosoft.gxapi.GXUSERMETA.set_ipj`

:func:`geosoft.gxapi.GXUSERMETA.set_meta_creation_date`

:func:`geosoft.gxapi.GXUSERMETA.set_meta_creator`

:func:`geosoft.gxapi.GXUSERMETA.set_project`

:func:`geosoft.gxapi.GXUSERMETA.set_title`

:func:`geosoft.gxapi.GXVOX.get_gocad_location`

:func:`geosoft.gxapi.GXVOX.get_tpat`

:func:`geosoft.gxapi.GXVOX.is_thematic`

:func:`geosoft.gxapi.GXVOX.nearest_neighbour_grid`

:func:`geosoft.gxapi.GXVOX.set_tpat`

:func:`geosoft.gxapi.GXVOX.sync`

:func:`geosoft.gxapi.GXVOXD.create_thematic`

:func:`geosoft.gxapi.GXVVU.dummy_back_tracks`


  
Version 6.4.2
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXCHIMERA.atomic_weight`

:func:`geosoft.gxapi.GXDB.can_open_read_only`

:func:`geosoft.gxapi.GXDB.open_read_only`

:func:`geosoft.gxapi.GXDH.qa_dip_az_curvature2`

:func:`geosoft.gxapi.GXDH.qa_east_north_curvature2`

:func:`geosoft.gxapi.GXIMG.report_csv`

:func:`geosoft.gxapi.GXIP.get_topo_line`

:func:`geosoft.gxapi.GXIP.write_distant_electrodes_lst`

:func:`geosoft.gxapi.GXPDF3D.render`

:func:`geosoft.gxapi.GXSEMPLOT.view_type`

:func:`geosoft.gxapi.GXTEST.enable_disable_arc_engine_license`

:func:`geosoft.gxapi.GXTEST.test_mode`

:func:`geosoft.gxapi.GXVA.lookup_index`

:func:`geosoft.gxapi.GXVM.create_ext`


  
Version 6.4.1
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXIPJ.get_plane_equation2`


  
Version 6.4.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXCHIMERA.get_expression_data_vv`

:func:`geosoft.gxapi.GXDATALINKD.create_arc_lyr`

:func:`geosoft.gxapi.GXDATALINKD.get_extents`

:func:`geosoft.gxapi.GXDATALINKD.get_ipj`

:func:`geosoft.gxapi.GXDB.gen_valid_line_symb`

:func:`geosoft.gxapi.GXDB.get_chan_vv_expanded`

:func:`geosoft.gxapi.GXDH.depth_data_lst`

:func:`geosoft.gxapi.GXDH.from_to_data_lst`

:func:`geosoft.gxapi.GXDH.get_oriented_core_dip_dir`

:func:`geosoft.gxapi.GXDU.voxel_section`

:func:`geosoft.gxapi.GXGIS.is_mi_rotated_raster_tab_file`

:func:`geosoft.gxapi.GXIP.export_ipdata_dir`

:func:`geosoft.gxapi.GXIP.export_ipred_dir`

:func:`geosoft.gxapi.GXIP.export_ubc_res_control`

:func:`geosoft.gxapi.GXIP.export_ubcip_control`

:func:`geosoft.gxapi.GXIP.ps_stack2_dir`

:func:`geosoft.gxapi.GXIP.pseudo_plot2_dir`

:func:`geosoft.gxapi.GXIPJ.convert_orientation_warp_vv`

:func:`geosoft.gxapi.GXITR.get_zone_model_type`

:func:`geosoft.gxapi.GXKGRD.run3`

:func:`geosoft.gxapi.GXMAP.packed_files`

:func:`geosoft.gxapi.GXMAP.un_pack_files_ex`

:func:`geosoft.gxapi.GXMAPTEMPLATE.render_preview_map_production`

:func:`geosoft.gxapi.GXMVIEW.datalinkd`

:func:`geosoft.gxapi.GXMVIEW.emf_object`

:func:`geosoft.gxapi.GXMVIEW.is_movable`

:func:`geosoft.gxapi.GXMVIEW.render`

:func:`geosoft.gxapi.GXMVIEW.set_movability`

:func:`geosoft.gxapi.GXMVU.get_range_gocad_surface`

:func:`geosoft.gxapi.GXMVU.import_gocad_surface`

:func:`geosoft.gxapi.GXMVU.plot_voxel_surface`

:func:`geosoft.gxapi.GXPRAGA3.launch`

:func:`geosoft.gxapi.GXSYS.crc_file_offset`

:func:`geosoft.gxapi.GXSYS.emf_object_size`

:func:`geosoft.gxapi.GXSYS.get_pattern`

:func:`geosoft.gxapi.GXSYS.set_pattern`

:func:`geosoft.gxapi.GXTEST.arc_engine_license`

:func:`geosoft.gxapi.GXVOX.compute_cell_size`

:func:`geosoft.gxapi.GXVOX.get_grid_section_cell_sizes`

:func:`geosoft.gxapi.GXVOX.get_limits_xyz`

:func:`geosoft.gxapi.GXVOX.get_limits`

:func:`geosoft.gxapi.GXVOX.grid_points_z_ex`

:func:`geosoft.gxapi.GXVOX.grid_points_z`

:func:`geosoft.gxapi.GXVV.get_fid_expansion`

:func:`geosoft.gxapi.GXVV.order`

:func:`geosoft.gxapi.GXVV.set_fid_expansion`


  
Version 6.3.1
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXIMG.create_projected3`

:func:`geosoft.gxapi.GXIPJ.is_3d_inverted_angles`

:func:`geosoft.gxapi.GXIPJ.is_3d_inverted`

:func:`geosoft.gxapi.GXIPJ.set_3d_inverted_angles`

:func:`geosoft.gxapi.GXIPJ.set_3d_inverted`

:func:`geosoft.gxapi.GXPG.statistics`

:func:`geosoft.gxapi.GXVOX.get_cell_size_strings`

:func:`geosoft.gxapi.GXVOX.set_cell_size_strings`

:func:`geosoft.gxapi.GXVOX.set_origin`


  
Version 6.3.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GX3DN.get_axis_color`

:func:`geosoft.gxapi.GX3DN.get_axis_font`

:func:`geosoft.gxapi.GX3DN.get_background_color`

:func:`geosoft.gxapi.GX3DN.get_point_of_view`

:func:`geosoft.gxapi.GX3DN.get_render_controls`

:func:`geosoft.gxapi.GX3DN.get_scale`

:func:`geosoft.gxapi.GX3DN.get_shading`

:func:`geosoft.gxapi.GX3DN.set_shading`

:func:`geosoft.gxapi.GXBF.read_binary_string`

:func:`geosoft.gxapi.GXBF.write_binary_string`

:func:`geosoft.gxapi.GXBIGRID.run2`

:func:`geosoft.gxapi.GXDATAMINE.create_voxel`

:func:`geosoft.gxapi.GXDATAMINE.numeric_field_lst`

:func:`geosoft.gxapi.GXDB.chan_lst`

:func:`geosoft.gxapi.GXDB.get_symb_lock`

:func:`geosoft.gxapi.GXDB.line_lst`

:func:`geosoft.gxapi.GXDH.assay_hole_lst`

:func:`geosoft.gxapi.GXDH.convert_old_line_names`

:func:`geosoft.gxapi.GXDH.datamine_to_csv`

:func:`geosoft.gxapi.GXDH.select_holes`

:func:`geosoft.gxapi.GXDH.un_selected_hole_lst`

:func:`geosoft.gxapi.GXDU.proj_points`

:func:`geosoft.gxapi.GXGIS.datamine_type`

:func:`geosoft.gxapi.GXGIS.is_shp_file_3d`

:func:`geosoft.gxapi.GXGIS.set_dm_wireframe_pt_file`

:func:`geosoft.gxapi.GXGU.gen_ux_detect_symbols_group_name`

:func:`geosoft.gxapi.GXGU.import_p190`

:func:`geosoft.gxapi.GXIP.set_import_mode`

:func:`geosoft.gxapi.GXIP.write_distant_electrodes`

:func:`geosoft.gxapi.GXIPJ.convert_warp_vv`

:func:`geosoft.gxapi.GXIPJ.convert_warp`

:func:`geosoft.gxapi.GXIPJ.get_3d_view`

:func:`geosoft.gxapi.GXIPJ.get_display_name`

:func:`geosoft.gxapi.GXIPJ.get_orientation_name`

:func:`geosoft.gxapi.GXIPJ.is_geographic`

:func:`geosoft.gxapi.GXIPJ.set_3d_view`

:func:`geosoft.gxapi.GXITR.set_data_limits`

:func:`geosoft.gxapi.GXLAYOUT.add_constraint`

:func:`geosoft.gxapi.GXLAYOUT.add_rectangle`

:func:`geosoft.gxapi.GXLAYOUT.calculate_rects`

:func:`geosoft.gxapi.GXLAYOUT.clear_all`

:func:`geosoft.gxapi.GXLAYOUT.clear_constraints`

:func:`geosoft.gxapi.GXLAYOUT.create`

:func:`geosoft.gxapi.GXLAYOUT.get_rect_name`

:func:`geosoft.gxapi.GXLAYOUT.get_rectangle`

:func:`geosoft.gxapi.GXLAYOUT.num_rectangles`

:func:`geosoft.gxapi.GXLAYOUT.set_rectangle_name`

:func:`geosoft.gxapi.GXLAYOUT.set_rectangle`

:func:`geosoft.gxapi.GXLST.find_items`

:func:`geosoft.gxapi.GXLST.gt_symb_item`

:func:`geosoft.gxapi.GXMAP.resize_all_ex`

:func:`geosoft.gxapi.GXMAPTEMPLATE.commit`

:func:`geosoft.gxapi.GXMAPTEMPLATE.create_map`

:func:`geosoft.gxapi.GXMAPTEMPLATE.create`

:func:`geosoft.gxapi.GXMAPTEMPLATE.discard`

:func:`geosoft.gxapi.GXMAPTEMPLATE.get_file_name`

:func:`geosoft.gxapi.GXMAPTEMPLATE.get_tmp_copy`

:func:`geosoft.gxapi.GXMAPTEMPLATE.render_preview`

:func:`geosoft.gxapi.GXMAPTEMPLATE.update_from_tmp_copy`

:func:`geosoft.gxapi.GXMATH.and`

:func:`geosoft.gxapi.GXMATH.or`

:func:`geosoft.gxapi.GXMATH.rand`

:func:`geosoft.gxapi.GXMATH.s_rand`

:func:`geosoft.gxapi.GXMATH.xor`

:func:`geosoft.gxapi.GXMETA.set_empty_attrib`

:func:`geosoft.gxapi.GXMVIEW.color2_rgb`

:func:`geosoft.gxapi.GXMVIEW.is_group_empty`

:func:`geosoft.gxapi.GXMVIEW.is_visible`

:func:`geosoft.gxapi.GXMVIEW.line_smooth`

:func:`geosoft.gxapi.GXMVIEW.mark_empty_groups`

:func:`geosoft.gxapi.GXMVIEW.render_order`

:func:`geosoft.gxapi.GXMVIEW.set_render_order`

:func:`geosoft.gxapi.GXMVIEW.set_visibility`

:func:`geosoft.gxapi.GXMVU.export_datamine_string`

:func:`geosoft.gxapi.GXMVU.mapset_test`

:func:`geosoft.gxapi.GXMVU.tick_ex`

:func:`geosoft.gxapi.GXPG.read_trace_3d`

:func:`geosoft.gxapi.GXPG.write_trace_3d`

:func:`geosoft.gxapi.GXPJ.convert_xyz`

:func:`geosoft.gxapi.GXPLY.clip_line_int`

:func:`geosoft.gxapi.GXRGRD.run_vv`

:func:`geosoft.gxapi.GXSEMPLOT.get_mineral_channel_name`

:func:`geosoft.gxapi.GXSEMPLOT.import_ascii_wizard`

:func:`geosoft.gxapi.GXSEMPLOT.mineral_id`

:func:`geosoft.gxapi.GXSHP.add_double_field`

:func:`geosoft.gxapi.GXSHP.add_int_field`

:func:`geosoft.gxapi.GXSHP.add_string_field`

:func:`geosoft.gxapi.GXSHP.create`

:func:`geosoft.gxapi.GXSHP.find_field`

:func:`geosoft.gxapi.GXSHP.set_arc_z`

:func:`geosoft.gxapi.GXSHP.set_arc`

:func:`geosoft.gxapi.GXSHP.set_double`

:func:`geosoft.gxapi.GXSHP.set_int`

:func:`geosoft.gxapi.GXSHP.set_ipj`

:func:`geosoft.gxapi.GXSHP.set_point_z`

:func:`geosoft.gxapi.GXSHP.set_point`

:func:`geosoft.gxapi.GXSHP.set_polygon_z`

:func:`geosoft.gxapi.GXSHP.set_polygon`

:func:`geosoft.gxapi.GXSHP.set_string`

:func:`geosoft.gxapi.GXSHP.write_item`

:func:`geosoft.gxapi.GXSTR.replace_char2`

:func:`geosoft.gxapi.GXSYS.dateto_long`

:func:`geosoft.gxapi.GXSYS.get_geodist`

:func:`geosoft.gxapi.GXSYS.longto_date`

:func:`geosoft.gxapi.GXSYS.longto_time`

:func:`geosoft.gxapi.GXSYS.make_file_readonly`

:func:`geosoft.gxapi.GXSYS.make_file_writable`

:func:`geosoft.gxapi.GXSYS.script_record`

:func:`geosoft.gxapi.GXSYS.secondsto_time`

:func:`geosoft.gxapi.GXSYS.send_general_message`

:func:`geosoft.gxapi.GXSYS.timeto_long`

:func:`geosoft.gxapi.GXSYS.timeto_seconds`

:func:`geosoft.gxapi.GXSYS.write_debug_log`

:func:`geosoft.gxapi.GXVOX.export_db`

:func:`geosoft.gxapi.GXVOX.export_xyz`

:func:`geosoft.gxapi.GXVOX.generate_db`

:func:`geosoft.gxapi.GXVOX.generate_oriented_gocad`

:func:`geosoft.gxapi.GXVOX.generate_xyz`

:func:`geosoft.gxapi.GXVOX.get_double_location`

:func:`geosoft.gxapi.GXVOX.get_location_points`

:func:`geosoft.gxapi.GXVOX.math`

:func:`geosoft.gxapi.GXVOX.slice_ipj`

:func:`geosoft.gxapi.GXVOXE.create`

:func:`geosoft.gxapi.GXVOXE.profile`

:func:`geosoft.gxapi.GXVOXE.value`

:func:`geosoft.gxapi.GXVOXE.vector`

:func:`geosoft.gxapi.GXVV.count_dummies`

:func:`geosoft.gxapi.GXVVU.noise_check2`

:func:`geosoft.gxapi.GXVVU.qc_fill_gaps`


  
Version 6.2.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXCHIMERA.categorize_by_value_det_limit`

:func:`geosoft.gxapi.GXCHIMERA.get_lithogeochem_data`

:func:`geosoft.gxapi.GXCHIMERA.get_transform`

:func:`geosoft.gxapi.GXCHIMERA.set_lithogeochem_data`

:func:`geosoft.gxapi.GXDB.csv_chan_lst`

:func:`geosoft.gxapi.GXDB.get_reg_symb_setting_double`

:func:`geosoft.gxapi.GXDB.get_reg_symb_setting_int`

:func:`geosoft.gxapi.GXDB.string_chan_lst`

:func:`geosoft.gxapi.GXDH.re_survey_straight_seg`

:func:`geosoft.gxapi.GXDU.closest_point`

:func:`geosoft.gxapi.GXDXFI.dxf2_view_ex`

:func:`geosoft.gxapi.GXDXFI.get_range`

:func:`geosoft.gxapi.GXGU.gr_demvv`

:func:`geosoft.gxapi.GXIMU.update_ply`

:func:`geosoft.gxapi.GXIPJ.compare_datums`

:func:`geosoft.gxapi.GXLST.add_symb_item`

:func:`geosoft.gxapi.GXLST.append`

:func:`geosoft.gxapi.GXLST.load_file`

:func:`geosoft.gxapi.GXLTB.create_crypt`

:func:`geosoft.gxapi.GXLTB.save_crypt`

:func:`geosoft.gxapi.GXMVIEW.draw_object_3d`

:func:`geosoft.gxapi.GXMVIEW.voxd`

:func:`geosoft.gxapi.GXMVU.export_dxf_3d`

:func:`geosoft.gxapi.GXMVU.export_surpac_str`

:func:`geosoft.gxapi.GXPG.create_3d`

:func:`geosoft.gxapi.GXPG.n_slices`

:func:`geosoft.gxapi.GXPG.re_allocate_3d`

:func:`geosoft.gxapi.GXPG.read_bf`

:func:`geosoft.gxapi.GXPG.read_col_3d`

:func:`geosoft.gxapi.GXPG.read_ra`

:func:`geosoft.gxapi.GXPG.read_row_3d`

:func:`geosoft.gxapi.GXPG.write_bf`

:func:`geosoft.gxapi.GXPG.write_col_3d`

:func:`geosoft.gxapi.GXPG.write_row_3d`

:func:`geosoft.gxapi.GXPG.write_wa`

:func:`geosoft.gxapi.GXPJ.setup_ldt`

:func:`geosoft.gxapi.GXSEMPLOT.apply_filter_to_mask`

:func:`geosoft.gxapi.GXSEMPLOT.convert_dummies`

:func:`geosoft.gxapi.GXSEMPLOT.create_ascii_template`

:func:`geosoft.gxapi.GXSEMPLOT.create_database_template`

:func:`geosoft.gxapi.GXSEMPLOT.create_groups`

:func:`geosoft.gxapi.GXSEMPLOT.default_groups`

:func:`geosoft.gxapi.GXSEMPLOT.edit_filter`

:func:`geosoft.gxapi.GXSEMPLOT.edit_map_plot_parameters`

:func:`geosoft.gxapi.GXSEMPLOT.edit_plot_components`

:func:`geosoft.gxapi.GXSEMPLOT.edit_plot_parameters`

:func:`geosoft.gxapi.GXSEMPLOT.export_overlay`

:func:`geosoft.gxapi.GXSEMPLOT.export_view`

:func:`geosoft.gxapi.GXSEMPLOT.filter_lst`

:func:`geosoft.gxapi.GXSEMPLOT.filter_mineral_pos_data`

:func:`geosoft.gxapi.GXSEMPLOT.get_associated_lst`

:func:`geosoft.gxapi.GXSEMPLOT.get_current_mineral_lst`

:func:`geosoft.gxapi.GXSEMPLOT.get_current_position_lst`

:func:`geosoft.gxapi.GXSEMPLOT.get_full_mineral_lst`

:func:`geosoft.gxapi.GXSEMPLOT.get_full_position_lst`

:func:`geosoft.gxapi.GXSEMPLOT.get_grouping_lst`

:func:`geosoft.gxapi.GXSEMPLOT.import_bin`

:func:`geosoft.gxapi.GXSEMPLOT.import_database_ado`

:func:`geosoft.gxapi.GXSEMPLOT.import_database_odbc`

:func:`geosoft.gxapi.GXSEMPLOT.init_group_symbols_used`

:func:`geosoft.gxapi.GXSEMPLOT.new_filter`

:func:`geosoft.gxapi.GXSEMPLOT.new_template`

:func:`geosoft.gxapi.GXSEMPLOT.overlay_lst`

:func:`geosoft.gxapi.GXSEMPLOT.plot_symbol_legend`

:func:`geosoft.gxapi.GXSEMPLOT.plot`

:func:`geosoft.gxapi.GXSEMPLOT.prop_symb`

:func:`geosoft.gxapi.GXSEMPLOT.re_plot_symbol_legend`

:func:`geosoft.gxapi.GXSEMPLOT.replot`

:func:`geosoft.gxapi.GXSEMPLOT.reset_groups`

:func:`geosoft.gxapi.GXSEMPLOT.reset_used_channel`

:func:`geosoft.gxapi.GXSEMPLOT.select_poly`

:func:`geosoft.gxapi.GXSEMPLOT.set_channel_order`

:func:`geosoft.gxapi.GXSEMPLOT.set_channel_units`

:func:`geosoft.gxapi.GXSEMPLOT.set_itr`

:func:`geosoft.gxapi.GXSEMPLOT.set_mask`

:func:`geosoft.gxapi.GXSEMPLOT.sort_data`

:func:`geosoft.gxapi.GXSEMPLOT.template_lst`

:func:`geosoft.gxapi.GXSEMPLOT.template_type`

:func:`geosoft.gxapi.GXSEMPLOT.tile_windows`

:func:`geosoft.gxapi.GXSEMPLOT.total_oxides`

:func:`geosoft.gxapi.GXSTR.substr`

:func:`geosoft.gxapi.GXSYS.file_writable`

:func:`geosoft.gxapi.GXSYS.set_server_messages_ap`

:func:`geosoft.gxapi.GXTC.create_ex`

:func:`geosoft.gxapi.GXUNC.is_valid_utf16_char`

:func:`geosoft.gxapi.GXUNC.utf16_val_to_str`

:func:`geosoft.gxapi.GXUNC.valid_symbol`

:func:`geosoft.gxapi.GXUNC.validate_symbols`

:func:`geosoft.gxapi.GXVOX.calc_stats`

:func:`geosoft.gxapi.GXVOX.create_pg`

:func:`geosoft.gxapi.GXVOX.create_type_pg`

:func:`geosoft.gxapi.GXVOX.create`

:func:`geosoft.gxapi.GXVOX.dump`

:func:`geosoft.gxapi.GXVOX.export_img`

:func:`geosoft.gxapi.GXVOX.export_xml`

:func:`geosoft.gxapi.GXVOX.generate_gocad`

:func:`geosoft.gxapi.GXVOX.generate_pg`

:func:`geosoft.gxapi.GXVOX.generate_ubc`

:func:`geosoft.gxapi.GXVOX.get_area`

:func:`geosoft.gxapi.GXVOX.get_info`

:func:`geosoft.gxapi.GXVOX.get_ipj`

:func:`geosoft.gxapi.GXVOX.get_location`

:func:`geosoft.gxapi.GXVOX.get_meta`

:func:`geosoft.gxapi.GXVOX.get_simple_location`

:func:`geosoft.gxapi.GXVOX.get_stats`

:func:`geosoft.gxapi.GXVOX.grid_points`

:func:`geosoft.gxapi.GXVOX.list_gocad_properties`

:func:`geosoft.gxapi.GXVOX.set_ipj`

:func:`geosoft.gxapi.GXVOX.set_location`

:func:`geosoft.gxapi.GXVOX.set_meta`

:func:`geosoft.gxapi.GXVOX.set_simple_location`

:func:`geosoft.gxapi.GXVOX.write_xml`

:func:`geosoft.gxapi.GXVOXD.create_itr`

:func:`geosoft.gxapi.GXVOXD.create`

:func:`geosoft.gxapi.GXVOXD.get_draw_controls`

:func:`geosoft.gxapi.GXVOXD.get_itr`

:func:`geosoft.gxapi.GXVOXD.get_shell_controls`

:func:`geosoft.gxapi.GXVOXD.set_draw_controls`

:func:`geosoft.gxapi.GXVOXD.set_itr`

:func:`geosoft.gxapi.GXVOXD.set_shell_controls`

:func:`geosoft.gxapi.GXVV.index_insert`

:func:`geosoft.gxapi.GXVV.index_max`

:func:`geosoft.gxapi.GXVV.init_index`

:func:`geosoft.gxapi.GXVVEXP.add_vv`

:func:`geosoft.gxapi.GXVVEXP.create`

:func:`geosoft.gxapi.GXVVEXP.do_formula`

:func:`geosoft.gxapi.GXVVU.pick_peak3`

:func:`geosoft.gxapi.GXVVU.polygon_mask`

:func:`geosoft.gxapi.GXVVU.remove_dummy4`

:func:`geosoft.gxapi.GXWA.create_ex`

:func:`geosoft.gxapi.GXWA.create_sbf_ex`


  
Version 6.1.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GX3DN.set_scale`

:func:`geosoft.gxapi.GXCHIMERA.categorize_by_value`

:func:`geosoft.gxapi.GXDB.can_open`

:func:`geosoft.gxapi.GXDB.get_symb_name`

:func:`geosoft.gxapi.GXDB.is_empty`

:func:`geosoft.gxapi.GXDB.is_line_empty`

:func:`geosoft.gxapi.GXDH.current`

:func:`geosoft.gxapi.GXDH.get_section_id`

:func:`geosoft.gxapi.GXDH.have_current2`

:func:`geosoft.gxapi.GXDH.have_current`

:func:`geosoft.gxapi.GXDH.modify_hole_traces_3dgui`

:func:`geosoft.gxapi.GXDH.modify_rock_codes_gui2`

:func:`geosoft.gxapi.GXDH.modify_structure_codes_gui2`

:func:`geosoft.gxapi.GXDH.modify_structure_codes_gui`

:func:`geosoft.gxapi.GXDH.plot_hole_traces_3d`

:func:`geosoft.gxapi.GXDH.qa_write_unregistered_holes`

:func:`geosoft.gxapi.GXDH.select_ply2`

:func:`geosoft.gxapi.GXDU.export_shp`

:func:`geosoft.gxapi.GXDU.get_chan_data_lst`

:func:`geosoft.gxapi.GXDU.get_chan_data_vv`

:func:`geosoft.gxapi.GXDU.import_bin3`

:func:`geosoft.gxapi.GXGU.maxwell_plate_corners`

:func:`geosoft.gxapi.GXHGD.export_img`

:func:`geosoft.gxapi.GXIGRF.date_range`

:func:`geosoft.gxapi.GXIP.create_default_job`

:func:`geosoft.gxapi.GXIP.get_n_value_lst`

:func:`geosoft.gxapi.GXIP.import_i2_x_ex`

:func:`geosoft.gxapi.GXIP.open_job`

:func:`geosoft.gxapi.GXIP.save_job`

:func:`geosoft.gxapi.GXIPGUI.modify_job`

:func:`geosoft.gxapi.GXLTB.create_ex`

:func:`geosoft.gxapi.GXMETA.create_attrib`

:func:`geosoft.gxapi.GXMETA.create_class`

:func:`geosoft.gxapi.GXMETA.create_type`

:func:`geosoft.gxapi.GXST.get_histogram_bins`

:func:`geosoft.gxapi.GXST.get_histogram_info`

:func:`geosoft.gxapi.GXSYS.get_license_class`

:func:`geosoft.gxapi.GXTEST.wrapper_test`

:func:`geosoft.gxapi.GXVVU.decimate`


  
Version 6.0.1
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXACQUIRE.import_hole`

:func:`geosoft.gxapi.GXACQUIRE.import_point`

:func:`geosoft.gxapi.GXACQUIRE.selection_tool`

:func:`geosoft.gxapi.GXCOM.read_chars_no_terminate`

:func:`geosoft.gxapi.GXCOM.read_line_no_terminate`

:func:`geosoft.gxapi.GXCOM.write_chars_no_terminate`

:func:`geosoft.gxapi.GXDB.check`

:func:`geosoft.gxapi.GXDB.get_chan_array_size`

:func:`geosoft.gxapi.GXDB.get_chan_decimal`

:func:`geosoft.gxapi.GXDB.get_chan_format`

:func:`geosoft.gxapi.GXDB.get_chan_protect`

:func:`geosoft.gxapi.GXDB.get_chan_type`

:func:`geosoft.gxapi.GXDB.get_chan_width`

:func:`geosoft.gxapi.GXDH.import_las`

:func:`geosoft.gxapi.GXDH.test_import_las`

:func:`geosoft.gxapi.GXIMG.is_colour`

:func:`geosoft.gxapi.GXKGRD.load_parms`

:func:`geosoft.gxapi.GXKGRD.run2`

:func:`geosoft.gxapi.GXKGRD.run`

:func:`geosoft.gxapi.GXKGRD.save_parms`

:func:`geosoft.gxapi.GXMATH.abs_double`

:func:`geosoft.gxapi.GXMATH.abs_int`

:func:`geosoft.gxapi.GXMATH.arc_cos`

:func:`geosoft.gxapi.GXMATH.arc_sin`

:func:`geosoft.gxapi.GXMATH.arc_tan2`

:func:`geosoft.gxapi.GXMATH.arc_tan`

:func:`geosoft.gxapi.GXMATH.ceil`

:func:`geosoft.gxapi.GXMATH.cos`

:func:`geosoft.gxapi.GXMATH.exp`

:func:`geosoft.gxapi.GXMATH.floor`

:func:`geosoft.gxapi.GXMATH.hypot`

:func:`geosoft.gxapi.GXMATH.lambda_trans_rev`

:func:`geosoft.gxapi.GXMATH.lambda_trans`

:func:`geosoft.gxapi.GXMATH.log10`

:func:`geosoft.gxapi.GXMATH.log_z`

:func:`geosoft.gxapi.GXMATH.log`

:func:`geosoft.gxapi.GXMATH.mod_double`

:func:`geosoft.gxapi.GXMATH.mod_int`

:func:`geosoft.gxapi.GXMATH.nicer_log_scale`

:func:`geosoft.gxapi.GXMATH.nicer_scale`

:func:`geosoft.gxapi.GXMATH.pow`

:func:`geosoft.gxapi.GXMATH.round_double`

:func:`geosoft.gxapi.GXMATH.round_int`

:func:`geosoft.gxapi.GXMATH.sign`

:func:`geosoft.gxapi.GXMATH.sin`

:func:`geosoft.gxapi.GXMATH.sqrt`

:func:`geosoft.gxapi.GXMATH.tan`

:func:`geosoft.gxapi.GXMATH.un_log_z`

:func:`geosoft.gxapi.GXMETA.has_value`

:func:`geosoft.gxapi.GXPJ.project_bounding_rectangle2`

:func:`geosoft.gxapi.GXPJ.project_bounding_rectangle_res2`

:func:`geosoft.gxapi.GXRGRD.default`

:func:`geosoft.gxapi.GXRGRD.load_parms`

:func:`geosoft.gxapi.GXRGRD.run2`

:func:`geosoft.gxapi.GXRGRD.run`

:func:`geosoft.gxapi.GXRGRD.save_parms`

:func:`geosoft.gxapi.GXSTK.get_flag`

:func:`geosoft.gxapi.GXSTK.set_va_index_start`

:func:`geosoft.gxapi.GXSTR.scan_date`

:func:`geosoft.gxapi.GXSTR.scan_form`

:func:`geosoft.gxapi.GXSTR.scan_i`

:func:`geosoft.gxapi.GXSTR.scan_r`

:func:`geosoft.gxapi.GXSTR.scan_time`

:func:`geosoft.gxapi.GXSYS.crc_file`

:func:`geosoft.gxapi.GXSYS.find_path_ex`

:func:`geosoft.gxapi.GXSYS.find_path`

:func:`geosoft.gxapi.GXSYS.get_dot_net_gx_entries`

:func:`geosoft.gxapi.GXSYS.get_double`

:func:`geosoft.gxapi.GXSYS.get_int`

:func:`geosoft.gxapi.GXSYS.global`

:func:`geosoft.gxapi.GXSYS.registry_get_val`

:func:`geosoft.gxapi.GXSYS.relative_file_name`

:func:`geosoft.gxapi.GXSYS.script`

:func:`geosoft.gxapi.GXTIN.export_xml`

:func:`geosoft.gxapi.GXVVU.search_replace_text_ex`


  
Version 6.0.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXACQUIRE.create`

:func:`geosoft.gxapi.GXACQUIRE.delete_empty_chan`

:func:`geosoft.gxapi.GXBF.set_destroy_status`

:func:`geosoft.gxapi.GXCOM.create_no_terminate`

:func:`geosoft.gxapi.GXDH.get_template_blob`

:func:`geosoft.gxapi.GXDH.get_template_info`

:func:`geosoft.gxapi.GXDH.load_data_parameters_ini`

:func:`geosoft.gxapi.GXDH.load_plot_parameters`

:func:`geosoft.gxapi.GXDH.save_data_parameters_ini`

:func:`geosoft.gxapi.GXDH.section_window_size_mm`

:func:`geosoft.gxapi.GXDH.set_template_blob`

:func:`geosoft.gxapi.GXDMPPLY.clear`

:func:`geosoft.gxapi.GXDMPPLY.copy`

:func:`geosoft.gxapi.GXDMPPLY.create`

:func:`geosoft.gxapi.GXDMPPLY.get_azimuth`

:func:`geosoft.gxapi.GXDMPPLY.get_extents`

:func:`geosoft.gxapi.GXDMPPLY.get_joins`

:func:`geosoft.gxapi.GXDMPPLY.get_normal_vectors`

:func:`geosoft.gxapi.GXDMPPLY.get_poly`

:func:`geosoft.gxapi.GXDMPPLY.get_swing`

:func:`geosoft.gxapi.GXDMPPLY.get_vertex`

:func:`geosoft.gxapi.GXDMPPLY.load`

:func:`geosoft.gxapi.GXDMPPLY.move_vertex`

:func:`geosoft.gxapi.GXDMPPLY.num_joins`

:func:`geosoft.gxapi.GXDMPPLY.num_polys`

:func:`geosoft.gxapi.GXDMPPLY.num_vertices`

:func:`geosoft.gxapi.GXDMPPLY.project_poly`

:func:`geosoft.gxapi.GXDMPPLY.re_project_poly`

:func:`geosoft.gxapi.GXDMPPLY.save`

:func:`geosoft.gxapi.GXDMPPLY.set_poly`

:func:`geosoft.gxapi.GXDU.export_chan_crc`

:func:`geosoft.gxapi.GXDU.export_database_crc`

:func:`geosoft.gxapi.GXDU.import_ubc_mod_msh`

:func:`geosoft.gxapi.GXGIS.get_meta`

:func:`geosoft.gxapi.GXGIS.set_ipj`

:func:`geosoft.gxapi.GXGIS.set_meta`

:func:`geosoft.gxapi.GXIMU.export_grid_xml`

:func:`geosoft.gxapi.GXIMU.export_xml`

:func:`geosoft.gxapi.GXIPJ.get_list`

:func:`geosoft.gxapi.GXIPJ.support_datum_transform`

:func:`geosoft.gxapi.GXITR.get_data_limits`

:func:`geosoft.gxapi.GXMAP.crc_map`

:func:`geosoft.gxapi.GXMAP.render_bitmap`

:func:`geosoft.gxapi.GXMATH.cross_product`

:func:`geosoft.gxapi.GXMATH.dot_product_3d`

:func:`geosoft.gxapi.GXMATH.normalise_3d`

:func:`geosoft.gxapi.GXMATH.rotate_vector`

:func:`geosoft.gxapi.GXMVIEW.crc_view_group`

:func:`geosoft.gxapi.GXMVIEW.crc_view`

:func:`geosoft.gxapi.GXMVIEW.delete_ext_clip_ply`

:func:`geosoft.gxapi.GXMVIEW.ext_clip_ply_list`

:func:`geosoft.gxapi.GXMVIEW.get_ext_clip_ply`

:func:`geosoft.gxapi.GXMVIEW.get_group_ext_clip_ply`

:func:`geosoft.gxapi.GXMVIEW.get_group_transparency`

:func:`geosoft.gxapi.GXMVIEW.get_name_ext_clip_ply`

:func:`geosoft.gxapi.GXMVIEW.get_plane_clip_ply`

:func:`geosoft.gxapi.GXMVIEW.get_ply`

:func:`geosoft.gxapi.GXMVIEW.measure_text`

:func:`geosoft.gxapi.GXMVIEW.num_ext_clip_ply`

:func:`geosoft.gxapi.GXMVIEW.set_ext_clip_ply`

:func:`geosoft.gxapi.GXMVIEW.set_group_ext_clip_ply`

:func:`geosoft.gxapi.GXMVIEW.set_group_transparency`

:func:`geosoft.gxapi.GXMVIEW.transparency`

:func:`geosoft.gxapi.GXMVIEW.z_value`

:func:`geosoft.gxapi.GXPJ.project_limited_bounding_rectangle`

:func:`geosoft.gxapi.GXSTR.replace_non_ascii`

:func:`geosoft.gxapi.GXSYS.check_intrinsic`

:func:`geosoft.gxapi.GXSYS.default_double`

:func:`geosoft.gxapi.GXSYS.default_int`

:func:`geosoft.gxapi.GXSYS.default_string`

:func:`geosoft.gxapi.GXSYS.delay`

:func:`geosoft.gxapi.GXSYS.get_error_message_ap`

:func:`geosoft.gxapi.GXSYS.get_licensed_user`

:func:`geosoft.gxapi.GXSYS.get_settings_meta`

:func:`geosoft.gxapi.GXSYS.get_timer`

:func:`geosoft.gxapi.GXSYS.num_errors_ap`

:func:`geosoft.gxapi.GXSYS.set_settings_meta`

:func:`geosoft.gxapi.GXTC.g_gterain`

:func:`geosoft.gxapi.GXTC.grterain2`

:func:`geosoft.gxapi.GXTIN.nearest_vv`

:func:`geosoft.gxapi.GXVVU.fractal_filter`


  
Version 5.1.8
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXCHIMERA.launch_probability`

:func:`geosoft.gxapi.GXCHIMERA.ordered_channel_lst`

:func:`geosoft.gxapi.GXCHIMERA.stacked_bar_plot`

:func:`geosoft.gxapi.GXCOM.purge_comm`

:func:`geosoft.gxapi.GXDAT.get_lst`

:func:`geosoft.gxapi.GXDB.get_chan_class`

:func:`geosoft.gxapi.GXDB.set_chan_class`

:func:`geosoft.gxapi.GXDH.add_survey_table`

:func:`geosoft.gxapi.GXDH.assay_lst`

:func:`geosoft.gxapi.GXDH.composite_db`

:func:`geosoft.gxapi.GXDH.creat_chan_lst`

:func:`geosoft.gxapi.GXDH.create_collar_table_dir`

:func:`geosoft.gxapi.GXDH.export_las`

:func:`geosoft.gxapi.GXDH.export_lst`

:func:`geosoft.gxapi.GXDH.get_ipj`

:func:`geosoft.gxapi.GXDH.get_map_names_vv`

:func:`geosoft.gxapi.GXDH.hole_selection_tool_gui`

:func:`geosoft.gxapi.GXDH.is_esri`

:func:`geosoft.gxapi.GXDH.modify_stacked_section_gui`

:func:`geosoft.gxapi.GXDH.set_ipj`

:func:`geosoft.gxapi.GXDH.set_new_ipj`

:func:`geosoft.gxapi.GXDOCU.get_file_meta`

:func:`geosoft.gxapi.GXDOCU.set_file_meta`

:func:`geosoft.gxapi.GXDU.base_data_ex`

:func:`geosoft.gxapi.GXDU.break_line_to_groups`

:func:`geosoft.gxapi.GXFFT.create_ex`

:func:`geosoft.gxapi.GXFFT.create_ref_ex`

:func:`geosoft.gxapi.GXGIS.load_meta_groups_map`

:func:`geosoft.gxapi.GXIMG.inherit_img`

:func:`geosoft.gxapi.GXIMU.grid_edge_ply`

:func:`geosoft.gxapi.GXIMU.mosaic`

:func:`geosoft.gxapi.GXIMU.range_grids`

:func:`geosoft.gxapi.GXIP.export_line_ipdata`

:func:`geosoft.gxapi.GXIP.get_chan_domain`

:func:`geosoft.gxapi.GXIP.import_merge_ipred`

:func:`geosoft.gxapi.GXIP.pseudo_plot2`

:func:`geosoft.gxapi.GXIPJ.get_esri`

:func:`geosoft.gxapi.GXIPJ.make_wgs84`

:func:`geosoft.gxapi.GXIPJ.set_esri`

:func:`geosoft.gxapi.GXLST.convert_from_csv_string`

:func:`geosoft.gxapi.GXLST.convert_to_csv_string`

:func:`geosoft.gxapi.GXLST.select_csv_string_items`

:func:`geosoft.gxapi.GXMAP.copy_map_to_view`

:func:`geosoft.gxapi.GXMAP.get_meta`

:func:`geosoft.gxapi.GXMAP.set_meta`

:func:`geosoft.gxapi.GXMETA.copy`

:func:`geosoft.gxapi.GXMETA.create_s`

:func:`geosoft.gxapi.GXMETA.move_datas_across`

:func:`geosoft.gxapi.GXMETA.serial`

:func:`geosoft.gxapi.GXMVIEW.best_fit_window`

:func:`geosoft.gxapi.GXMVIEW.delete_group`

:func:`geosoft.gxapi.GXMVU.probability`

:func:`geosoft.gxapi.GXPGU.correlation_matrix2`

:func:`geosoft.gxapi.GXPGU.pc_loadings2`

:func:`geosoft.gxapi.GXPGU.pc_standardize2`

:func:`geosoft.gxapi.GXPJ.project_bounding_rectangle_res`

:func:`geosoft.gxapi.GXPLY.clear`

:func:`geosoft.gxapi.GXSQLSRV.attach_mdf`

:func:`geosoft.gxapi.GXSQLSRV.detach_db`

:func:`geosoft.gxapi.GXSQLSRV.get_database_languages_lst`

:func:`geosoft.gxapi.GXSQLSRV.get_databases_lst`

:func:`geosoft.gxapi.GXSQLSRV.get_login_gui`

:func:`geosoft.gxapi.GXSQLSRV.get_servers_lst`

:func:`geosoft.gxapi.GXST.create_exact`

:func:`geosoft.gxapi.GXSTR.make_alpha`

:func:`geosoft.gxapi.GXSTR.strins`

:func:`geosoft.gxapi.GXSYS.copy_file`

:func:`geosoft.gxapi.GXSYS.reset_settings`

:func:`geosoft.gxapi.GXSYS.temp_file_ext`

:func:`geosoft.gxapi.GXSYS.transfer_path`

:func:`geosoft.gxapi.GXVVU.box_cox`

:func:`geosoft.gxapi.GXVVU.close_xy`

:func:`geosoft.gxapi.GXVVU.close_xym`

:func:`geosoft.gxapi.GXVVU.close_xyz`

:func:`geosoft.gxapi.GXVVU.close_xyzm`

:func:`geosoft.gxapi.GXVVU.exp_dist`

:func:`geosoft.gxapi.GXVVU.mask_and`

:func:`geosoft.gxapi.GXVVU.mask_or`

:func:`geosoft.gxapi.GXVVU.normal_dist`

:func:`geosoft.gxapi.GXVVU.uniform_dist`


  
Version 5.1.6
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GX3DN.set_axis_color`

:func:`geosoft.gxapi.GX3DN.set_axis_font`

:func:`geosoft.gxapi.GX3DN.set_background_color`

:func:`geosoft.gxapi.GXCHIMERA.tri_plot2`

:func:`geosoft.gxapi.GXDB.get_va_prof_sect_option`

:func:`geosoft.gxapi.GXDB.get_va_sect_color_file`

:func:`geosoft.gxapi.GXDB.set_va_prof_sect_option`

:func:`geosoft.gxapi.GXDB.set_va_sect_color_file`

:func:`geosoft.gxapi.GXDH.create_collar_table`

:func:`geosoft.gxapi.GXDH.create_external`

:func:`geosoft.gxapi.GXDH.modify3d_gui`

:func:`geosoft.gxapi.GXDOCU.is_reference`

:func:`geosoft.gxapi.GXDU.export2`

:func:`geosoft.gxapi.GXDU.import_bin2`

:func:`geosoft.gxapi.GXDU.import_xyz2`

:func:`geosoft.gxapi.GXDXFI.dxf2_ply`

:func:`geosoft.gxapi.GXGIS.load_ply`

:func:`geosoft.gxapi.GXGU.dipole_mag`

:func:`geosoft.gxapi.GXIMU.agg_to_geo_color`

:func:`geosoft.gxapi.GXIMU.grid_ply_ex`

:func:`geosoft.gxapi.GXIMU.make_mi_tab_file`

:func:`geosoft.gxapi.GXIPJ.clear_orientation`

:func:`geosoft.gxapi.GXIPJ.get_orientation_info`

:func:`geosoft.gxapi.GXIPJ.get_plane_equation`

:func:`geosoft.gxapi.GXIPJ.set_plan_view`

:func:`geosoft.gxapi.GXIPJ.set_section_view`

:func:`geosoft.gxapi.GXITR.color_vv`

:func:`geosoft.gxapi.GXITR.load_a`

:func:`geosoft.gxapi.GXLST.assay_channel`

:func:`geosoft.gxapi.GXLST.find_item_mask`

:func:`geosoft.gxapi.GXLST.insert_item`

:func:`geosoft.gxapi.GXMETA.delete_attrib`

:func:`geosoft.gxapi.GXMETA.delete_class`

:func:`geosoft.gxapi.GXMETA.delete_data`

:func:`geosoft.gxapi.GXMETA.delete_item`

:func:`geosoft.gxapi.GXMETA.delete_type`

:func:`geosoft.gxapi.GXMETA.find_data`

:func:`geosoft.gxapi.GXMETA.get_attrib_bool`

:func:`geosoft.gxapi.GXMETA.get_attrib_enum`

:func:`geosoft.gxapi.GXMETA.h_copy_across_attribute`

:func:`geosoft.gxapi.GXMETA.h_copy_across_class`

:func:`geosoft.gxapi.GXMETA.h_copy_across_data`

:func:`geosoft.gxapi.GXMETA.h_copy_across_item`

:func:`geosoft.gxapi.GXMETA.h_copy_across_type`

:func:`geosoft.gxapi.GXMETA.h_creat_item`

:func:`geosoft.gxapi.GXMETA.set_attrib_bool`

:func:`geosoft.gxapi.GXMETA.set_attrib_enum`

:func:`geosoft.gxapi.GXMETA.set_attribute_editable`

:func:`geosoft.gxapi.GXMETA.set_attribute_visible`

:func:`geosoft.gxapi.GXMETA.write_text`

:func:`geosoft.gxapi.GXMVIEW.box_3d`

:func:`geosoft.gxapi.GXMVIEW.cylinder_3d`

:func:`geosoft.gxapi.GXMVIEW.define_plane_3d`

:func:`geosoft.gxapi.GXMVIEW.define_viewer_axis_3d`

:func:`geosoft.gxapi.GXMVIEW.define_viewer_plane_3d`

:func:`geosoft.gxapi.GXMVIEW.get_meta`

:func:`geosoft.gxapi.GXMVIEW.point_3d`

:func:`geosoft.gxapi.GXMVIEW.poly_line_3d`

:func:`geosoft.gxapi.GXMVIEW.set_meta`

:func:`geosoft.gxapi.GXMVIEW.sphere_3d`

:func:`geosoft.gxapi.GXMVIEW.update_met_afrom_group`

:func:`geosoft.gxapi.GXMVU.contour_ply`

:func:`geosoft.gxapi.GXSTR.str_str`

:func:`geosoft.gxapi.GXSYS.get_thread_id`

:func:`geosoft.gxapi.GXSYS.run_multi_user_script`

:func:`geosoft.gxapi.GXTB.find_col_by_index`

:func:`geosoft.gxapi.GXVVU.clip_to_detect_limit`


  
Version 5.1.5
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXCHIMERA.pie_plot2`

:func:`geosoft.gxapi.GXCHIMERA.rose_plot2`

:func:`geosoft.gxapi.GXDB.get_meta`

:func:`geosoft.gxapi.GXDB.get_va_prof_color_file`

:func:`geosoft.gxapi.GXDB.get_va_scaling`

:func:`geosoft.gxapi.GXDB.get_va_windows`

:func:`geosoft.gxapi.GXDB.mask_chan_lst`

:func:`geosoft.gxapi.GXDB.set_meta`

:func:`geosoft.gxapi.GXDB.set_va_prof_color_file`

:func:`geosoft.gxapi.GXDB.set_va_scaling`

:func:`geosoft.gxapi.GXDB.set_va_windows`

:func:`geosoft.gxapi.GXHXYZ.h_create_db`

:func:`geosoft.gxapi.GXIMU.make_mi_tabfrom_grid`

:func:`geosoft.gxapi.GXIMU.make_mi_tabfrom_map`

:func:`geosoft.gxapi.GXIPJ.make_geographic`

:func:`geosoft.gxapi.GXIPJ.make_projected`

:func:`geosoft.gxapi.GXIPJ.new_box_resolution`

:func:`geosoft.gxapi.GXIPJ.set_wms_coord_sys`

:func:`geosoft.gxapi.GXLST.set_item`

:func:`geosoft.gxapi.GXMETA.delete_all_items`

:func:`geosoft.gxapi.GXMETA.export_table_csv`

:func:`geosoft.gxapi.GXMETA.import_table_csv`

:func:`geosoft.gxapi.GXMVIEW.get_agg_file_names`

:func:`geosoft.gxapi.GXPGU.filt_sym`

:func:`geosoft.gxapi.GXSTK.get_axis_format`

:func:`geosoft.gxapi.GXSTK.set_axis_format`

:func:`geosoft.gxapi.GXSTR.replace_multi_char`

:func:`geosoft.gxapi.GXVA.reverse`

:func:`geosoft.gxapi.GXVV.sort`


  
Version 5.1.4
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDSEL.picture_quality`

:func:`geosoft.gxapi.GXDU.intersect_old`

:func:`geosoft.gxapi.GXFFT.h_int`

:func:`geosoft.gxapi.GXGU.gr_test`

:func:`geosoft.gxapi.GXIMU.grid_stitch_ctl`

:func:`geosoft.gxapi.GXIMU.peak_size2`

:func:`geosoft.gxapi.GXIPJ.get_orientation`

:func:`geosoft.gxapi.GXIPJ.set_mi_coord_sys`

:func:`geosoft.gxapi.GXMVIEW.set_plane_clip_ply`

:func:`geosoft.gxapi.GXPJ.project_bounding_rectangle`

:func:`geosoft.gxapi.GXSTR.gen_group_name`

:func:`geosoft.gxapi.GXSTR.set_char_n`

:func:`geosoft.gxapi.GXSTR.set_char`

:func:`geosoft.gxapi.GXTIN.linear_interp_vv`

:func:`geosoft.gxapi.GXVVU.offset_correct3`


  
Version 5.1.3
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDB.exist_chan`

:func:`geosoft.gxapi.GXDB.find_chan`

:func:`geosoft.gxapi.GXDB.get_xyz_chan_symb`

:func:`geosoft.gxapi.GXDB.get_xyz_chan`

:func:`geosoft.gxapi.GXDB.is_associated`

:func:`geosoft.gxapi.GXDB.set_xyz_chan`

:func:`geosoft.gxapi.GXDH.compositing_tool_gui`

:func:`geosoft.gxapi.GXDH.get_data_type`

:func:`geosoft.gxapi.GXDH.h_assay_db`

:func:`geosoft.gxapi.GXDH.h_assay_symb`

:func:`geosoft.gxapi.GXDH.h_collar_db`

:func:`geosoft.gxapi.GXDH.h_collar_symb`

:func:`geosoft.gxapi.GXDH.h_dip_az_survey_db`

:func:`geosoft.gxapi.GXDH.h_dip_az_survey_symb`

:func:`geosoft.gxapi.GXDH.h_en_survey_db`

:func:`geosoft.gxapi.GXDH.h_en_survey_symb`

:func:`geosoft.gxapi.GXDH.mask_ply`

:func:`geosoft.gxapi.GXDH.modify_strip_log_gui`

:func:`geosoft.gxapi.GXDH.num_assays`

:func:`geosoft.gxapi.GXDH.qa_collar`

:func:`geosoft.gxapi.GXDH.qa_dip_az_curvature`

:func:`geosoft.gxapi.GXDH.qa_dip_az_survey`

:func:`geosoft.gxapi.GXDH.qa_east_north_curvature`

:func:`geosoft.gxapi.GXDH.qa_east_north_survey`

:func:`geosoft.gxapi.GXDH.qa_from_to_data`

:func:`geosoft.gxapi.GXDH.qa_point_data`

:func:`geosoft.gxapi.GXDH.re_survey_east_north`

:func:`geosoft.gxapi.GXDSEL.meta_query`

:func:`geosoft.gxapi.GXDSEL.request_all_info`

:func:`geosoft.gxapi.GXDSEL.select_area`

:func:`geosoft.gxapi.GXHXYZ.create`

:func:`geosoft.gxapi.GXHXYZ.get_meta`

:func:`geosoft.gxapi.GXHXYZ.h_create_sql`

:func:`geosoft.gxapi.GXHXYZ.set_meta`

:func:`geosoft.gxapi.GXIP.winnow_chan_list2`

:func:`geosoft.gxapi.GXMETA.get_obj_name`

:func:`geosoft.gxapi.GXMETA.h_get_next_item`

:func:`geosoft.gxapi.GXMVIEW.meta`

:func:`geosoft.gxapi.GXPLY.area`

:func:`geosoft.gxapi.GXPLY.clip_area`

:func:`geosoft.gxapi.GXPLY.clip_ply`

:func:`geosoft.gxapi.GXPLY.thin`

:func:`geosoft.gxapi.GXVA.append`

:func:`geosoft.gxapi.GXVV.polygon_mask`

:func:`geosoft.gxapi.GXVV.reverse`

:func:`geosoft.gxapi.GXVVU.offset_correct2`

:func:`geosoft.gxapi.GXVVU.spline2`


  
Version 5.1.2
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GX3DN.copy`

:func:`geosoft.gxapi.GX3DN.create`

:func:`geosoft.gxapi.GX3DN.set_point_of_view`

:func:`geosoft.gxapi.GX3DN.set_render_controls`

:func:`geosoft.gxapi.GXDB.selected_line_lst`

:func:`geosoft.gxapi.GXDH.clean_will_delete_db`

:func:`geosoft.gxapi.GXDH.clean`

:func:`geosoft.gxapi.GXDH.compute_xyz`

:func:`geosoft.gxapi.GXDH.create_default_job`

:func:`geosoft.gxapi.GXDH.delete_holes`

:func:`geosoft.gxapi.GXDH.delete_will_delete_db`

:func:`geosoft.gxapi.GXDH.get_collar_table_db`

:func:`geosoft.gxapi.GXDH.get_databases_vv`

:func:`geosoft.gxapi.GXDH.get_project_name`

:func:`geosoft.gxapi.GXDH.hole_lst2`

:func:`geosoft.gxapi.GXDH.modify_hole_traces_gui`

:func:`geosoft.gxapi.GXDH.modify_plan_gui`

:func:`geosoft.gxapi.GXDH.modify_rock_codes_gui`

:func:`geosoft.gxapi.GXDH.modify_section_gui`

:func:`geosoft.gxapi.GXDH.plot_hole_traces`

:func:`geosoft.gxapi.GXDH.re_survey_pol_fit`

:func:`geosoft.gxapi.GXDH.re_survey_rad_curve`

:func:`geosoft.gxapi.GXDH.re_survey_straight`

:func:`geosoft.gxapi.GXDH.wholeplot`

:func:`geosoft.gxapi.GXIMU.grid_st`

:func:`geosoft.gxapi.GXITR.equal_area`

:func:`geosoft.gxapi.GXITR.normal`

:func:`geosoft.gxapi.GXITR.save_a`

:func:`geosoft.gxapi.GXLST.get_double`

:func:`geosoft.gxapi.GXLST.get_int`

:func:`geosoft.gxapi.GXMAP.agg_list_ex`

:func:`geosoft.gxapi.GXMAP.duplicate_view`

:func:`geosoft.gxapi.GXMAP.group_list_ex`

:func:`geosoft.gxapi.GXMAP.view_list_ex`

:func:`geosoft.gxapi.GXMVIEW.copy_raw_marked_groups`

:func:`geosoft.gxapi.GXMVIEW.create_plane`

:func:`geosoft.gxapi.GXMVIEW.delete_plane`

:func:`geosoft.gxapi.GXMVIEW.find_plane`

:func:`geosoft.gxapi.GXMVIEW.fit_map_window_3d`

:func:`geosoft.gxapi.GXMVIEW.get_class_name`

:func:`geosoft.gxapi.GXMVIEW.get_def_plane`

:func:`geosoft.gxapi.GXMVIEW.get_plane_equation`

:func:`geosoft.gxapi.GXMVIEW.get_view_plane_equation`

:func:`geosoft.gxapi.GXMVIEW.is_view_3d`

:func:`geosoft.gxapi.GXMVIEW.list_plane_groups`

:func:`geosoft.gxapi.GXMVIEW.list_planes`

:func:`geosoft.gxapi.GXMVIEW.set_all_groups_to_plane`

:func:`geosoft.gxapi.GXMVIEW.set_all_new_groups_to_plane`

:func:`geosoft.gxapi.GXMVIEW.set_class_name`

:func:`geosoft.gxapi.GXMVIEW.set_def_plane`

:func:`geosoft.gxapi.GXMVIEW.set_group_to_plane`

:func:`geosoft.gxapi.GXMVIEW.set_h_3dn`

:func:`geosoft.gxapi.GXMVIEW.set_plane_equation`

:func:`geosoft.gxapi.GXMVIEW.set_plane_surf_info`

:func:`geosoft.gxapi.GXMVIEW.set_plane_surface`

:func:`geosoft.gxapi.GXVV.make_mem_based`

:func:`geosoft.gxapi.GXVV.mask_and`

:func:`geosoft.gxapi.GXVV.mask_or`


  
Version 5.1.1
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXAGG.set_render_method`

:func:`geosoft.gxapi.GXBF.query_write`

:func:`geosoft.gxapi.GXDB.associate_class`

:func:`geosoft.gxapi.GXDB.blobs_max`

:func:`geosoft.gxapi.GXDB.chans_max`

:func:`geosoft.gxapi.GXDB.compact`

:func:`geosoft.gxapi.GXDB.get_line_map_fid`

:func:`geosoft.gxapi.GXDB.get_va_chan_vv`

:func:`geosoft.gxapi.GXDB.grow`

:func:`geosoft.gxapi.GXDB.is_chan_valid`

:func:`geosoft.gxapi.GXDB.line_bearing`

:func:`geosoft.gxapi.GXDB.lines_max`

:func:`geosoft.gxapi.GXDB.put_va_chan_vv`

:func:`geosoft.gxapi.GXDB.repair`

:func:`geosoft.gxapi.GXDB.set_line_bearing`

:func:`geosoft.gxapi.GXDB.un_lock_all_symb`

:func:`geosoft.gxapi.GXDB.users_max`

:func:`geosoft.gxapi.GXDOCU.copy`

:func:`geosoft.gxapi.GXDOCU.create_s`

:func:`geosoft.gxapi.GXDOCU.create`

:func:`geosoft.gxapi.GXDOCU.doc_name`

:func:`geosoft.gxapi.GXDOCU.file_name`

:func:`geosoft.gxapi.GXDOCU.get_file`

:func:`geosoft.gxapi.GXDOCU.get_meta`

:func:`geosoft.gxapi.GXDOCU.have_meta`

:func:`geosoft.gxapi.GXDOCU.open`

:func:`geosoft.gxapi.GXDOCU.serial`

:func:`geosoft.gxapi.GXDOCU.set_file`

:func:`geosoft.gxapi.GXDOCU.set_meta`

:func:`geosoft.gxapi.GXIP.recalculate_z`

:func:`geosoft.gxapi.GXMVIEW.move_group_backward`

:func:`geosoft.gxapi.GXMVIEW.move_group_forward`

:func:`geosoft.gxapi.GXMVIEW.move_group_to_back`

:func:`geosoft.gxapi.GXMVIEW.move_group_to_front`

:func:`geosoft.gxapi.GXMVIEW.rename_group`

:func:`geosoft.gxapi.GXREG.entries`

:func:`geosoft.gxapi.GXREG.get_one`

:func:`geosoft.gxapi.GXSYS.break_date`

:func:`geosoft.gxapi.GXSYS.clear_err_ap`

:func:`geosoft.gxapi.GXSYS.clear_group_parm`

:func:`geosoft.gxapi.GXSYS.make_date`

:func:`geosoft.gxapi.GXVV.re_sample`


  
Version 5.1.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXHGD.create`

:func:`geosoft.gxapi.GXHGD.get_meta`

:func:`geosoft.gxapi.GXHGD.h_create_img`

:func:`geosoft.gxapi.GXHGD.set_meta`

:func:`geosoft.gxapi.GXIMU.grid_ply`

:func:`geosoft.gxapi.GXIP.import_ipdata2`

:func:`geosoft.gxapi.GXIP.import_ipred`

:func:`geosoft.gxapi.GXIP.ps_stack2`

:func:`geosoft.gxapi.GXITR.color_value`

:func:`geosoft.gxapi.GXITR.create_img`

:func:`geosoft.gxapi.GXLTB.contract`

:func:`geosoft.gxapi.GXMETA.get_attrib_double`

:func:`geosoft.gxapi.GXMETA.get_attrib_int`

:func:`geosoft.gxapi.GXMETA.get_attrib_obj`

:func:`geosoft.gxapi.GXMETA.get_attrib_string`

:func:`geosoft.gxapi.GXMETA.resolve_umn`

:func:`geosoft.gxapi.GXMETA.set_attrib_double`

:func:`geosoft.gxapi.GXMETA.set_attrib_int`

:func:`geosoft.gxapi.GXMETA.set_attrib_obj`

:func:`geosoft.gxapi.GXMETA.set_attrib_string`

:func:`geosoft.gxapi.GXMVIEW.font_weight_lst`

:func:`geosoft.gxapi.GXMVIEW.polygon_ply`

:func:`geosoft.gxapi.GXMVU.color_bar_hor2_style`

:func:`geosoft.gxapi.GXMVU.color_bar_hor2`

:func:`geosoft.gxapi.GXMVU.color_bar_hor_style`

:func:`geosoft.gxapi.GXPJ.elevation`

:func:`geosoft.gxapi.GXPLY.create_s`

:func:`geosoft.gxapi.GXPLY.get_description`

:func:`geosoft.gxapi.GXPLY.serial`

:func:`geosoft.gxapi.GXPLY.set_description`

:func:`geosoft.gxapi.GXVA.index_order`

:func:`geosoft.gxapi.GXVVU.rolling_stats`


  
Version 5.0.8
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXCHIMERA.clip_to_detect_limit`

:func:`geosoft.gxapi.GXDB.add_comment`

:func:`geosoft.gxapi.GXDB.add_double_comment`

:func:`geosoft.gxapi.GXDB.add_int_comment`

:func:`geosoft.gxapi.GXDB.add_time_comment`

:func:`geosoft.gxapi.GXDB.class_group_lst`

:func:`geosoft.gxapi.GXDB.get_chan_order_lst`

:func:`geosoft.gxapi.GXDB.get_group_class`

:func:`geosoft.gxapi.GXDB.set_chan_order_lst`

:func:`geosoft.gxapi.GXDB.set_group_class`

:func:`geosoft.gxapi.GXDSEL.data_significant_figures`

:func:`geosoft.gxapi.GXDSEL.set_ipj`

:func:`geosoft.gxapi.GXDSEL.spatial_accuracy`

:func:`geosoft.gxapi.GXDU.ado_table_names`

:func:`geosoft.gxapi.GXDU.copy_line_masked`

:func:`geosoft.gxapi.GXDU.import_ado`

:func:`geosoft.gxapi.GXDU.import_all_ado`

:func:`geosoft.gxapi.GXDU.scan_ado`

:func:`geosoft.gxapi.GXIMG.get_meta`

:func:`geosoft.gxapi.GXIMG.geth_pg`

:func:`geosoft.gxapi.GXIMG.set_meta`

:func:`geosoft.gxapi.GXIMU.get_zvv`

:func:`geosoft.gxapi.GXIMU.pigeon_hole`

:func:`geosoft.gxapi.GXMETA.create`

:func:`geosoft.gxapi.GXMVIEW.gen_new_group_name`

:func:`geosoft.gxapi.GXMVU.path_plot_ex2`

:func:`geosoft.gxapi.GXMVU.prop_symb_legend`

:func:`geosoft.gxapi.GXPGU.fill_value`

:func:`geosoft.gxapi.GXPGU.peakedness_grid`

:func:`geosoft.gxapi.GXPGU.peakedness`

:func:`geosoft.gxapi.GXST.equivalent_percentile`

:func:`geosoft.gxapi.GXST.equivalent_value`

:func:`geosoft.gxapi.GXVV.add2`

:func:`geosoft.gxapi.GXVV.add`

:func:`geosoft.gxapi.GXVV.divide`

:func:`geosoft.gxapi.GXVV.multiply`

:func:`geosoft.gxapi.GXVV.subtract`

:func:`geosoft.gxapi.GXVVU.offset_correct`

:func:`geosoft.gxapi.GXVVU.remove_dummy2`

:func:`geosoft.gxapi.GXVVU.remove_dummy3`

:func:`geosoft.gxapi.GXVVU.search_text`


  
Version 5.0.7
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXCHIMERA.bar_plot`

:func:`geosoft.gxapi.GXCHIMERA.draw_circle_offset_markers`

:func:`geosoft.gxapi.GXCHIMERA.draw_rectangle_offset_markers`

:func:`geosoft.gxapi.GXCHIMERA.duplicate_chem`

:func:`geosoft.gxapi.GXCHIMERA.is_element`

:func:`geosoft.gxapi.GXCHIMERA.launch_triplot`

:func:`geosoft.gxapi.GXCHIMERA.mask_chan_lst`

:func:`geosoft.gxapi.GXCHIMERA.pie_plot`

:func:`geosoft.gxapi.GXCHIMERA.rose_plot`

:func:`geosoft.gxapi.GXCHIMERA.scatter2`

:func:`geosoft.gxapi.GXCHIMERA.standard`

:func:`geosoft.gxapi.GXLMSG.goto_point`

:func:`geosoft.gxapi.GXLMSG.view_area`

:func:`geosoft.gxapi.GXMVIEW.segment`

:func:`geosoft.gxapi.GXSBF.create_obj_list`

:func:`geosoft.gxapi.GXVVU.dummy_range_ex`

:func:`geosoft.gxapi.GXVVU.offset_circles`

:func:`geosoft.gxapi.GXVVU.offset_rectangles`


  
Version 5.0.6
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXAGG.list_img`

:func:`geosoft.gxapi.GXCHIMERA.launch_histogram`

:func:`geosoft.gxapi.GXCHIMERA.launch_scatter`

:func:`geosoft.gxapi.GXEDB.launch_histogram`

:func:`geosoft.gxapi.GXEDB.launch_scatter`

:func:`geosoft.gxapi.GXIMG.create_mem`

:func:`geosoft.gxapi.GXIMG.load_img`

:func:`geosoft.gxapi.GXMVIEW.polygon_dm`

:func:`geosoft.gxapi.GXSTR.escape`

:func:`geosoft.gxapi.GXVVU.poly_fill2`

:func:`geosoft.gxapi.GXVVU.poly_fill`

:func:`geosoft.gxapi.GXVVU.trend2`

:func:`geosoft.gxapi.GXVVU.trend`


  
Version 5.0.5
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXAGG.create_map`

:func:`geosoft.gxapi.GXDB.class_chan_list`

:func:`geosoft.gxapi.GXIMG.element_type`

:func:`geosoft.gxapi.GXIMG.query_double`

:func:`geosoft.gxapi.GXIMG.query_int`

:func:`geosoft.gxapi.GXIMU.stat_window`

:func:`geosoft.gxapi.GXMVIEW.get_reg`

:func:`geosoft.gxapi.GXMVIEW.is_group`

:func:`geosoft.gxapi.GXMVIEW.set_group_moveable`

:func:`geosoft.gxapi.GXMVIEW.set_mark_moveable`

:func:`geosoft.gxapi.GXPLY.change_ipj`

:func:`geosoft.gxapi.GXPLY.get_ipj`

:func:`geosoft.gxapi.GXPLY.rectangle`

:func:`geosoft.gxapi.GXPLY.set_ipj`

:func:`geosoft.gxapi.GXSTR.strncmp`


  
Version 5.0.3
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDB.class_chan_lst`

:func:`geosoft.gxapi.GXDSEL.create`

:func:`geosoft.gxapi.GXDSEL.select_rect`

:func:`geosoft.gxapi.GXDSEL.select_resolution`

:func:`geosoft.gxapi.GXIMG.create`

:func:`geosoft.gxapi.GXSTK.get_profile_ex`

:func:`geosoft.gxapi.GXSTK.set_profile_ex`

:func:`geosoft.gxapi.GXTIN.get_ipj`

:func:`geosoft.gxapi.GXTIN.set_ipj`


  
Version 5.0.2
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXIMG.get_def_itr`

:func:`geosoft.gxapi.GXIMG.set_def_itr`

:func:`geosoft.gxapi.GXITR.set_color_model`

:func:`geosoft.gxapi.GXVV.sort_index1`

:func:`geosoft.gxapi.GXVV.sort_index2`

:func:`geosoft.gxapi.GXVV.sort_index3`

:func:`geosoft.gxapi.GXVV.sort_index4`


  
Version 5.0.1
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDB.window_va_ch2`

:func:`geosoft.gxapi.GXDU.export_aseg_proj`

:func:`geosoft.gxapi.GXDU.import_aseg_proj`

:func:`geosoft.gxapi.GXFFT2.td_xd_y`

:func:`geosoft.gxapi.GXGMSYS.launch`

:func:`geosoft.gxapi.GXSTK.set_array_colors`

:func:`geosoft.gxapi.GXSTR.parse_list`

:func:`geosoft.gxapi.GXTB.data_type`

:func:`geosoft.gxapi.GXTB.format`


  
Version 5.0.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXAGG.change_brightness`

:func:`geosoft.gxapi.GXAGG.create`

:func:`geosoft.gxapi.GXAGG.get_brightness`

:func:`geosoft.gxapi.GXAGG.get_layer_itr`

:func:`geosoft.gxapi.GXAGG.layer_img`

:func:`geosoft.gxapi.GXAGG.layer_shade_img`

:func:`geosoft.gxapi.GXAGG.num_layers`

:func:`geosoft.gxapi.GXAGG.set_layer_itr`

:func:`geosoft.gxapi.GXAGG.set_model`

:func:`geosoft.gxapi.GXBF.ch_size`

:func:`geosoft.gxapi.GXBF.copy`

:func:`geosoft.gxapi.GXBF.crc`

:func:`geosoft.gxapi.GXBF.create_sbf`

:func:`geosoft.gxapi.GXBF.create`

:func:`geosoft.gxapi.GXBF.eof`

:func:`geosoft.gxapi.GXBF.read_double`

:func:`geosoft.gxapi.GXBF.read_int`

:func:`geosoft.gxapi.GXBF.read_vv`

:func:`geosoft.gxapi.GXBF.seek`

:func:`geosoft.gxapi.GXBF.size`

:func:`geosoft.gxapi.GXBF.tell`

:func:`geosoft.gxapi.GXBF.write_data_null`

:func:`geosoft.gxapi.GXBF.write_double`

:func:`geosoft.gxapi.GXBF.write_int`

:func:`geosoft.gxapi.GXBF.write_vv`

:func:`geosoft.gxapi.GXBIGRID.clear`

:func:`geosoft.gxapi.GXBIGRID.create`

:func:`geosoft.gxapi.GXBIGRID.load_parms`

:func:`geosoft.gxapi.GXBIGRID.load_warp`

:func:`geosoft.gxapi.GXBIGRID.run`

:func:`geosoft.gxapi.GXBIGRID.save_parms`

:func:`geosoft.gxapi.GXCOM.create`

:func:`geosoft.gxapi.GXCOM.read_chars`

:func:`geosoft.gxapi.GXCOM.read_em61_lines_wa`

:func:`geosoft.gxapi.GXCOM.read_file2_wa`

:func:`geosoft.gxapi.GXCOM.read_line`

:func:`geosoft.gxapi.GXCOM.read_lines_wa`

:func:`geosoft.gxapi.GXCOM.set_time_out`

:func:`geosoft.gxapi.GXCOM.write_chars`

:func:`geosoft.gxapi.GXCOM.write_line`

:func:`geosoft.gxapi.GXCSYMB.add_data`

:func:`geosoft.gxapi.GXCSYMB.create`

:func:`geosoft.gxapi.GXCSYMB.set_angle`

:func:`geosoft.gxapi.GXCSYMB.set_base`

:func:`geosoft.gxapi.GXCSYMB.set_dynamic_col`

:func:`geosoft.gxapi.GXCSYMB.set_fixed`

:func:`geosoft.gxapi.GXCSYMB.set_font`

:func:`geosoft.gxapi.GXCSYMB.set_number`

:func:`geosoft.gxapi.GXCSYMB.set_scale`

:func:`geosoft.gxapi.GXCSYMB.set_static_col`

:func:`geosoft.gxapi.GXDAT.create_db`

:func:`geosoft.gxapi.GXDAT.create_xgd`

:func:`geosoft.gxapi.GXDB.add_associated_load`

:func:`geosoft.gxapi.GXDB.array_lst`

:func:`geosoft.gxapi.GXDB.associate_all`

:func:`geosoft.gxapi.GXDB.associate`

:func:`geosoft.gxapi.GXDB.commit`

:func:`geosoft.gxapi.GXDB.coord_pair`

:func:`geosoft.gxapi.GXDB.copy_data`

:func:`geosoft.gxapi.GXDB.count_sel_lines`

:func:`geosoft.gxapi.GXDB.create_comp`

:func:`geosoft.gxapi.GXDB.create_dup_comp`

:func:`geosoft.gxapi.GXDB.create_dup`

:func:`geosoft.gxapi.GXDB.create_ex`

:func:`geosoft.gxapi.GXDB.create_symb_ex`

:func:`geosoft.gxapi.GXDB.create_symb`

:func:`geosoft.gxapi.GXDB.create`

:func:`geosoft.gxapi.GXDB.delete_symb`

:func:`geosoft.gxapi.GXDB.discard`

:func:`geosoft.gxapi.GXDB.dup_line_symb`

:func:`geosoft.gxapi.GXDB.dup_symb_across`

:func:`geosoft.gxapi.GXDB.dup_symb_no_lock`

:func:`geosoft.gxapi.GXDB.dup_symb`

:func:`geosoft.gxapi.GXDB.easy_maker_symb`

:func:`geosoft.gxapi.GXDB.exist_symb`

:func:`geosoft.gxapi.GXDB.find_symb`

:func:`geosoft.gxapi.GXDB.first_sel_line`

:func:`geosoft.gxapi.GXDB.format_chan`

:func:`geosoft.gxapi.GXDB.gen_valid_chan_symb`

:func:`geosoft.gxapi.GXDB.get_chan_double`

:func:`geosoft.gxapi.GXDB.get_chan_int`

:func:`geosoft.gxapi.GXDB.get_chan_label`

:func:`geosoft.gxapi.GXDB.get_chan_name`

:func:`geosoft.gxapi.GXDB.get_chan_str`

:func:`geosoft.gxapi.GXDB.get_chan_unit`

:func:`geosoft.gxapi.GXDB.get_chan_va`

:func:`geosoft.gxapi.GXDB.get_chan_vv`

:func:`geosoft.gxapi.GXDB.get_col_va`

:func:`geosoft.gxapi.GXDB.get_fid_incr`

:func:`geosoft.gxapi.GXDB.get_fid_start`

:func:`geosoft.gxapi.GXDB.get_ipj`

:func:`geosoft.gxapi.GXDB.get_itr`

:func:`geosoft.gxapi.GXDB.get_name`

:func:`geosoft.gxapi.GXDB.get_reg_symb_setting`

:func:`geosoft.gxapi.GXDB.get_reg_symb`

:func:`geosoft.gxapi.GXDB.get_select`

:func:`geosoft.gxapi.GXDB.have_itr`

:func:`geosoft.gxapi.GXDB.is_line_name`

:func:`geosoft.gxapi.GXDB.is_line_valid`

:func:`geosoft.gxapi.GXDB.is_wholeplot`

:func:`geosoft.gxapi.GXDB.line_category`

:func:`geosoft.gxapi.GXDB.line_date`

:func:`geosoft.gxapi.GXDB.line_flight`

:func:`geosoft.gxapi.GXDB.line_label`

:func:`geosoft.gxapi.GXDB.line_number2`

:func:`geosoft.gxapi.GXDB.line_number`

:func:`geosoft.gxapi.GXDB.line_type`

:func:`geosoft.gxapi.GXDB.line_version`

:func:`geosoft.gxapi.GXDB.load_select`

:func:`geosoft.gxapi.GXDB.lock_symb`

:func:`geosoft.gxapi.GXDB.maker_symb`

:func:`geosoft.gxapi.GXDB.next_sel_line`

:func:`geosoft.gxapi.GXDB.open`

:func:`geosoft.gxapi.GXDB.put_chan_va`

:func:`geosoft.gxapi.GXDB.put_chan_vv`

:func:`geosoft.gxapi.GXDB.read_blob_bf`

:func:`geosoft.gxapi.GXDB.save_select`

:func:`geosoft.gxapi.GXDB.select`

:func:`geosoft.gxapi.GXDB.set_chan_decimal`

:func:`geosoft.gxapi.GXDB.set_chan_double`

:func:`geosoft.gxapi.GXDB.set_chan_format`

:func:`geosoft.gxapi.GXDB.set_chan_int`

:func:`geosoft.gxapi.GXDB.set_chan_label`

:func:`geosoft.gxapi.GXDB.set_chan_name`

:func:`geosoft.gxapi.GXDB.set_chan_protect`

:func:`geosoft.gxapi.GXDB.set_chan_str`

:func:`geosoft.gxapi.GXDB.set_chan_unit`

:func:`geosoft.gxapi.GXDB.set_chan_width`

:func:`geosoft.gxapi.GXDB.set_fid`

:func:`geosoft.gxapi.GXDB.set_ipj`

:func:`geosoft.gxapi.GXDB.set_itr`

:func:`geosoft.gxapi.GXDB.set_line_date`

:func:`geosoft.gxapi.GXDB.set_line_flight`

:func:`geosoft.gxapi.GXDB.set_line_map_fid`

:func:`geosoft.gxapi.GXDB.set_line_name2`

:func:`geosoft.gxapi.GXDB.set_line_name`

:func:`geosoft.gxapi.GXDB.set_line_num`

:func:`geosoft.gxapi.GXDB.set_line_type`

:func:`geosoft.gxapi.GXDB.set_line_ver`

:func:`geosoft.gxapi.GXDB.set_reg_symb_setting`

:func:`geosoft.gxapi.GXDB.set_reg_symb`

:func:`geosoft.gxapi.GXDB.set_select`

:func:`geosoft.gxapi.GXDB.symb_list`

:func:`geosoft.gxapi.GXDB.symb_lst`

:func:`geosoft.gxapi.GXDB.un_lock_symb`

:func:`geosoft.gxapi.GXDB.window_va_ch`

:func:`geosoft.gxapi.GXDB.write_blob_bf`

:func:`geosoft.gxapi.GXDGW.create`

:func:`geosoft.gxapi.GXDGW.get_info_meta`

:func:`geosoft.gxapi.GXDGW.get_info_sys`

:func:`geosoft.gxapi.GXDGW.get_list`

:func:`geosoft.gxapi.GXDGW.gt_info`

:func:`geosoft.gxapi.GXDGW.run_dialogue`

:func:`geosoft.gxapi.GXDGW.set_info_meta`

:func:`geosoft.gxapi.GXDGW.set_info_sys`

:func:`geosoft.gxapi.GXDGW.set_info`

:func:`geosoft.gxapi.GXDGW.set_title`

:func:`geosoft.gxapi.GXDH.add_hole`

:func:`geosoft.gxapi.GXDH.auto_select_holes`

:func:`geosoft.gxapi.GXDH.compute_sel_extent`

:func:`geosoft.gxapi.GXDH.create`

:func:`geosoft.gxapi.GXDH.export_file`

:func:`geosoft.gxapi.GXDH.find_hole`

:func:`geosoft.gxapi.GXDH.flush_select`

:func:`geosoft.gxapi.GXDH.get_default_section`

:func:`geosoft.gxapi.GXDH.get_hole_group`

:func:`geosoft.gxapi.GXDH.get_hole_survey`

:func:`geosoft.gxapi.GXDH.get_info`

:func:`geosoft.gxapi.GXDH.get_reg`

:func:`geosoft.gxapi.GXDH.get_units`

:func:`geosoft.gxapi.GXDH.hole_lst`

:func:`geosoft.gxapi.GXDH.holes`

:func:`geosoft.gxapi.GXDH.load_select`

:func:`geosoft.gxapi.GXDH.num_selected_holes`

:func:`geosoft.gxapi.GXDH.open_job`

:func:`geosoft.gxapi.GXDH.save_job`

:func:`geosoft.gxapi.GXDH.save_select`

:func:`geosoft.gxapi.GXDH.select_all_holes`

:func:`geosoft.gxapi.GXDH.select_name`

:func:`geosoft.gxapi.GXDH.select_ply`

:func:`geosoft.gxapi.GXDH.set_info`

:func:`geosoft.gxapi.GXDH.un_select_all_holes`

:func:`geosoft.gxapi.GXDH.update_collar_table`

:func:`geosoft.gxapi.GXDH.update_hole_extent`

:func:`geosoft.gxapi.GXDU.an_sig`

:func:`geosoft.gxapi.GXDU.append`

:func:`geosoft.gxapi.GXDU.avg_azimuth`

:func:`geosoft.gxapi.GXDU.b_spline`

:func:`geosoft.gxapi.GXDU.base_data`

:func:`geosoft.gxapi.GXDU.bound_line`

:func:`geosoft.gxapi.GXDU.bp_filt`

:func:`geosoft.gxapi.GXDU.break_line`

:func:`geosoft.gxapi.GXDU.copy_line_across`

:func:`geosoft.gxapi.GXDU.copy_line_chan_across`

:func:`geosoft.gxapi.GXDU.copy_line`

:func:`geosoft.gxapi.GXDU.dao_table_names`

:func:`geosoft.gxapi.GXDU.decimate`

:func:`geosoft.gxapi.GXDU.diff`

:func:`geosoft.gxapi.GXDU.direction`

:func:`geosoft.gxapi.GXDU.distance`

:func:`geosoft.gxapi.GXDU.distline`

:func:`geosoft.gxapi.GXDU.dup_chan_locks`

:func:`geosoft.gxapi.GXDU.dup_chans`

:func:`geosoft.gxapi.GXDU.edit_duplicates`

:func:`geosoft.gxapi.GXDU.export1`

:func:`geosoft.gxapi.GXDU.export_amira`

:func:`geosoft.gxapi.GXDU.export_aseg`

:func:`geosoft.gxapi.GXDU.export_csv`

:func:`geosoft.gxapi.GXDU.export_gbn`

:func:`geosoft.gxapi.GXDU.export_mdb`

:func:`geosoft.gxapi.GXDU.export_xyz2`

:func:`geosoft.gxapi.GXDU.export_xyz`

:func:`geosoft.gxapi.GXDU.fft`

:func:`geosoft.gxapi.GXDU.filter`

:func:`geosoft.gxapi.GXDU.gen_lev`

:func:`geosoft.gxapi.GXDU.gen_xyz_temp`

:func:`geosoft.gxapi.GXDU.gradient`

:func:`geosoft.gxapi.GXDU.grav_drift`

:func:`geosoft.gxapi.GXDU.grav_tide`

:func:`geosoft.gxapi.GXDU.grid_load_xyz`

:func:`geosoft.gxapi.GXDU.grid_load`

:func:`geosoft.gxapi.GXDU.head`

:func:`geosoft.gxapi.GXDU.imp_cb_ply`

:func:`geosoft.gxapi.GXDU.import_all_dao`

:func:`geosoft.gxapi.GXDU.import_amira`

:func:`geosoft.gxapi.GXDU.import_aseg`

:func:`geosoft.gxapi.GXDU.import_bin`

:func:`geosoft.gxapi.GXDU.import_dao`

:func:`geosoft.gxapi.GXDU.import_gbn`

:func:`geosoft.gxapi.GXDU.import_oddf`

:func:`geosoft.gxapi.GXDU.import_pico`

:func:`geosoft.gxapi.GXDU.import_usgs_post`

:func:`geosoft.gxapi.GXDU.import_xyz`

:func:`geosoft.gxapi.GXDU.index_order`

:func:`geosoft.gxapi.GXDU.interp`

:func:`geosoft.gxapi.GXDU.intersect_all`

:func:`geosoft.gxapi.GXDU.intersect`

:func:`geosoft.gxapi.GXDU.lab_template`

:func:`geosoft.gxapi.GXDU.load_gravity`

:func:`geosoft.gxapi.GXDU.load_ltb`

:func:`geosoft.gxapi.GXDU.make_fid`

:func:`geosoft.gxapi.GXDU.mask`

:func:`geosoft.gxapi.GXDU.math`

:func:`geosoft.gxapi.GXDU.merge_line`

:func:`geosoft.gxapi.GXDU.mod_fid_range`

:func:`geosoft.gxapi.GXDU.move`

:func:`geosoft.gxapi.GXDU.nl_filt`

:func:`geosoft.gxapi.GXDU.normal`

:func:`geosoft.gxapi.GXDU.poly_fill`

:func:`geosoft.gxapi.GXDU.poly_mask`

:func:`geosoft.gxapi.GXDU.project_data`

:func:`geosoft.gxapi.GXDU.project_xyz`

:func:`geosoft.gxapi.GXDU.qc_init_separation`

:func:`geosoft.gxapi.GXDU.qc_survey_plan`

:func:`geosoft.gxapi.GXDU.re_fid_all_ch`

:func:`geosoft.gxapi.GXDU.re_fid_ch`

:func:`geosoft.gxapi.GXDU.re_fid`

:func:`geosoft.gxapi.GXDU.rotate`

:func:`geosoft.gxapi.GXDU.sample_gd`

:func:`geosoft.gxapi.GXDU.sample_img`

:func:`geosoft.gxapi.GXDU.scan_aseg`

:func:`geosoft.gxapi.GXDU.scan_dao`

:func:`geosoft.gxapi.GXDU.scan_pico`

:func:`geosoft.gxapi.GXDU.sort_index2`

:func:`geosoft.gxapi.GXDU.sort_index`

:func:`geosoft.gxapi.GXDU.sort`

:func:`geosoft.gxapi.GXDU.split_line`

:func:`geosoft.gxapi.GXDU.stat`

:func:`geosoft.gxapi.GXDU.table_line_fid`

:func:`geosoft.gxapi.GXDU.table_look1`

:func:`geosoft.gxapi.GXDU.table_look2`

:func:`geosoft.gxapi.GXDU.table_look_i2`

:func:`geosoft.gxapi.GXDU.table_look_r2`

:func:`geosoft.gxapi.GXDU.time_constant`

:func:`geosoft.gxapi.GXDU.trend`

:func:`geosoft.gxapi.GXDU.write_wa`

:func:`geosoft.gxapi.GXDU.xyz_line2`

:func:`geosoft.gxapi.GXDU.xyz_line`

:func:`geosoft.gxapi.GXDU.z_mask`

:func:`geosoft.gxapi.GXDXFI.create`

:func:`geosoft.gxapi.GXEDB.all_chan_list`

:func:`geosoft.gxapi.GXEDB.apply_formula_internal`

:func:`geosoft.gxapi.GXEDB.channels`

:func:`geosoft.gxapi.GXEDB.current_if_exists`

:func:`geosoft.gxapi.GXEDB.current`

:func:`geosoft.gxapi.GXEDB.del_line0`

:func:`geosoft.gxapi.GXEDB.destroy_view`

:func:`geosoft.gxapi.GXEDB.disp_chan_list`

:func:`geosoft.gxapi.GXEDB.disp_chan_lst`

:func:`geosoft.gxapi.GXEDB.disp_class_chan_lst`

:func:`geosoft.gxapi.GXEDB.find_channel_column`

:func:`geosoft.gxapi.GXEDB.find_nearest`

:func:`geosoft.gxapi.GXEDB.get_cur_chan_symb`

:func:`geosoft.gxapi.GXEDB.get_cur_chan`

:func:`geosoft.gxapi.GXEDB.get_cur_fid_string`

:func:`geosoft.gxapi.GXEDB.get_cur_fid`

:func:`geosoft.gxapi.GXEDB.get_cur_line_symb`

:func:`geosoft.gxapi.GXEDB.get_cur_line`

:func:`geosoft.gxapi.GXEDB.get_cur_mark`

:func:`geosoft.gxapi.GXEDB.get_current_selection`

:func:`geosoft.gxapi.GXEDB.get_databases_lst`

:func:`geosoft.gxapi.GXEDB.get_displ_fid_range`

:func:`geosoft.gxapi.GXEDB.get_fid_range`

:func:`geosoft.gxapi.GXEDB.get_mark_chan_vv`

:func:`geosoft.gxapi.GXEDB.get_name`

:func:`geosoft.gxapi.GXEDB.get_next_line_symb`

:func:`geosoft.gxapi.GXEDB.get_prev_line_symb`

:func:`geosoft.gxapi.GXEDB.get_profile_parm_double`

:func:`geosoft.gxapi.GXEDB.get_profile_parm_int`

:func:`geosoft.gxapi.GXEDB.get_profile_range_x`

:func:`geosoft.gxapi.GXEDB.get_profile_range_y`

:func:`geosoft.gxapi.GXEDB.get_profile_split5`

:func:`geosoft.gxapi.GXEDB.get_profile_split_vv`

:func:`geosoft.gxapi.GXEDB.get_profile_split`

:func:`geosoft.gxapi.GXEDB.get_profile_vertical_grid_lines`

:func:`geosoft.gxapi.GXEDB.get_profile_window`

:func:`geosoft.gxapi.GXEDB.get_split`

:func:`geosoft.gxapi.GXEDB.get_window_state`

:func:`geosoft.gxapi.GXEDB.goto_column`

:func:`geosoft.gxapi.GXEDB.goto_elem`

:func:`geosoft.gxapi.GXEDB.goto_line`

:func:`geosoft.gxapi.GXEDB.have_current`

:func:`geosoft.gxapi.GXEDB.histogram`

:func:`geosoft.gxapi.GXEDB.is_locked`

:func:`geosoft.gxapi.GXEDB.load_all_chans`

:func:`geosoft.gxapi.GXEDB.load_chan`

:func:`geosoft.gxapi.GXEDB.load_new`

:func:`geosoft.gxapi.GXEDB.load_no_activate`

:func:`geosoft.gxapi.GXEDB.load_pass`

:func:`geosoft.gxapi.GXEDB.load_with_view`

:func:`geosoft.gxapi.GXEDB.load`

:func:`geosoft.gxapi.GXEDB.loaded`

:func:`geosoft.gxapi.GXEDB.lock`

:func:`geosoft.gxapi.GXEDB.make_current`

:func:`geosoft.gxapi.GXEDB.profile_open`

:func:`geosoft.gxapi.GXEDB.read_only`

:func:`geosoft.gxapi.GXEDB.remove_profile`

:func:`geosoft.gxapi.GXEDB.run_channel_maker`

:func:`geosoft.gxapi.GXEDB.run_channel_makers`

:func:`geosoft.gxapi.GXEDB.set_cur_line_no_message`

:func:`geosoft.gxapi.GXEDB.set_cur_line`

:func:`geosoft.gxapi.GXEDB.set_cur_mark`

:func:`geosoft.gxapi.GXEDB.set_profile_parm_i`

:func:`geosoft.gxapi.GXEDB.set_profile_parm_r`

:func:`geosoft.gxapi.GXEDB.set_profile_range_x`

:func:`geosoft.gxapi.GXEDB.set_profile_range_y`

:func:`geosoft.gxapi.GXEDB.set_profile_split5`

:func:`geosoft.gxapi.GXEDB.set_profile_split_vv`

:func:`geosoft.gxapi.GXEDB.set_profile_split`

:func:`geosoft.gxapi.GXEDB.set_split`

:func:`geosoft.gxapi.GXEDB.set_window_state`

:func:`geosoft.gxapi.GXEDB.show_profile_name`

:func:`geosoft.gxapi.GXEDB.show_profile`

:func:`geosoft.gxapi.GXEDB.statistics`

:func:`geosoft.gxapi.GXEDB.un_load_all_chans`

:func:`geosoft.gxapi.GXEDB.un_load_all`

:func:`geosoft.gxapi.GXEDB.un_load_chan`

:func:`geosoft.gxapi.GXEDB.un_load_discard`

:func:`geosoft.gxapi.GXEDB.un_load_verify`

:func:`geosoft.gxapi.GXEDB.un_load`

:func:`geosoft.gxapi.GXEDB.un_lock`

:func:`geosoft.gxapi.GXEDB.window_profiles`

:func:`geosoft.gxapi.GXEDOC.create_new_gms_3d`

:func:`geosoft.gxapi.GXEDOC.current_if_exists`

:func:`geosoft.gxapi.GXEDOC.current`

:func:`geosoft.gxapi.GXEDOC.get_documents_lst`

:func:`geosoft.gxapi.GXEDOC.get_name`

:func:`geosoft.gxapi.GXEDOC.get_window_state`

:func:`geosoft.gxapi.GXEDOC.have_current`

:func:`geosoft.gxapi.GXEDOC.load`

:func:`geosoft.gxapi.GXEDOC.loaded`

:func:`geosoft.gxapi.GXEDOC.make_current`

:func:`geosoft.gxapi.GXEDOC.read_only`

:func:`geosoft.gxapi.GXEDOC.set_window_state`

:func:`geosoft.gxapi.GXEDOC.sync_open`

:func:`geosoft.gxapi.GXEDOC.sync`

:func:`geosoft.gxapi.GXEDOC.un_load_all`

:func:`geosoft.gxapi.GXEDOC.un_load_discard`

:func:`geosoft.gxapi.GXEDOC.un_load_verify`

:func:`geosoft.gxapi.GXEDOC.un_load`

:func:`geosoft.gxapi.GXEMAP.activate_group`

:func:`geosoft.gxapi.GXEMAP.activate_view`

:func:`geosoft.gxapi.GXEMAP.change_current_view`

:func:`geosoft.gxapi.GXEMAP.copy_to_clip`

:func:`geosoft.gxapi.GXEMAP.create_group_snapshot`

:func:`geosoft.gxapi.GXEMAP.create_virtual`

:func:`geosoft.gxapi.GXEMAP.current_if_exists`

:func:`geosoft.gxapi.GXEMAP.current`

:func:`geosoft.gxapi.GXEMAP.destroy_view`

:func:`geosoft.gxapi.GXEMAP.digitize2`

:func:`geosoft.gxapi.GXEMAP.digitize_polygon`

:func:`geosoft.gxapi.GXEMAP.digitize`

:func:`geosoft.gxapi.GXEMAP.doubleize_group_snapshot`

:func:`geosoft.gxapi.GXEMAP.drag_drop_enabled`

:func:`geosoft.gxapi.GXEMAP.draw_line`

:func:`geosoft.gxapi.GXEMAP.draw_rect`

:func:`geosoft.gxapi.GXEMAP.drop_map_clip_data`

:func:`geosoft.gxapi.GXEMAP.font_lst`

:func:`geosoft.gxapi.GXEMAP.get_3d_view_name`

:func:`geosoft.gxapi.GXEMAP.get_aoi_area`

:func:`geosoft.gxapi.GXEMAP.get_box2`

:func:`geosoft.gxapi.GXEMAP.get_box`

:func:`geosoft.gxapi.GXEMAP.get_cur_point_mm`

:func:`geosoft.gxapi.GXEMAP.get_cur_point`

:func:`geosoft.gxapi.GXEMAP.get_current_group`

:func:`geosoft.gxapi.GXEMAP.get_current_view`

:func:`geosoft.gxapi.GXEMAP.get_cursor_mm`

:func:`geosoft.gxapi.GXEMAP.get_cursor`

:func:`geosoft.gxapi.GXEMAP.get_display_area_raw`

:func:`geosoft.gxapi.GXEMAP.get_display_area`

:func:`geosoft.gxapi.GXEMAP.get_grid`

:func:`geosoft.gxapi.GXEMAP.get_line_ex`

:func:`geosoft.gxapi.GXEMAP.get_line_xyz`

:func:`geosoft.gxapi.GXEMAP.get_line`

:func:`geosoft.gxapi.GXEMAP.get_map_layout_props`

:func:`geosoft.gxapi.GXEMAP.get_map_snap`

:func:`geosoft.gxapi.GXEMAP.get_maps_lst`

:func:`geosoft.gxapi.GXEMAP.get_name`

:func:`geosoft.gxapi.GXEMAP.get_point_ex`

:func:`geosoft.gxapi.GXEMAP.get_point`

:func:`geosoft.gxapi.GXEMAP.get_poly_line_xyz`

:func:`geosoft.gxapi.GXEMAP.get_poly_line`

:func:`geosoft.gxapi.GXEMAP.get_rect`

:func:`geosoft.gxapi.GXEMAP.get_selected_vertices`

:func:`geosoft.gxapi.GXEMAP.get_window_state`

:func:`geosoft.gxapi.GXEMAP.have_current`

:func:`geosoft.gxapi.GXEMAP.i_get_specified_map_name`

:func:`geosoft.gxapi.GXEMAP.is_3d_view`

:func:`geosoft.gxapi.GXEMAP.is_grid`

:func:`geosoft.gxapi.GXEMAP.is_locked`

:func:`geosoft.gxapi.GXEMAP.load_no_activate`

:func:`geosoft.gxapi.GXEMAP.load_with_view`

:func:`geosoft.gxapi.GXEMAP.load`

:func:`geosoft.gxapi.GXEMAP.loaded`

:func:`geosoft.gxapi.GXEMAP.lock`

:func:`geosoft.gxapi.GXEMAP.make_current`

:func:`geosoft.gxapi.GXEMAP.print`

:func:`geosoft.gxapi.GXEMAP.read_only`

:func:`geosoft.gxapi.GXEMAP.redraw`

:func:`geosoft.gxapi.GXEMAP.select_group`

:func:`geosoft.gxapi.GXEMAP.set_aoi_area`

:func:`geosoft.gxapi.GXEMAP.set_current_view`

:func:`geosoft.gxapi.GXEMAP.set_display_area`

:func:`geosoft.gxapi.GXEMAP.set_drag_drop_enabled`

:func:`geosoft.gxapi.GXEMAP.set_map_layout_props`

:func:`geosoft.gxapi.GXEMAP.set_map_snap`

:func:`geosoft.gxapi.GXEMAP.set_redraw_flag`

:func:`geosoft.gxapi.GXEMAP.set_viewport_mode`

:func:`geosoft.gxapi.GXEMAP.set_window_state`

:func:`geosoft.gxapi.GXEMAP.track_point`

:func:`geosoft.gxapi.GXEMAP.un_load_all`

:func:`geosoft.gxapi.GXEMAP.un_load_verify`

:func:`geosoft.gxapi.GXEMAP.un_load`

:func:`geosoft.gxapi.GXEMAP.un_lock`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.create_virtual`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.current_if_exists`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.current`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.drag_drop_enabled`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.get_box`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.get_display_area`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.get_item_selection`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.get_line`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.get_map_templates_lst`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.get_name`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.get_point`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.get_rect`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.get_template_layout_props`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.get_window_state`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.have_current`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.i_get_specified_map_name`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.is_locked`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.load_no_activate`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.load`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.loaded`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.lock`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.make_current`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.read_only`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.set_display_area`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.set_drag_drop_enabled`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.set_item_selection`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.set_template_layout_props`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.set_window_state`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.track_point`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.un_load_all`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.un_load_verify`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.un_load`

:func:`geosoft.gxapi.GXEMAPTEMPLATE.un_lock`

:func:`geosoft.gxapi.GXEUL3.creat`

:func:`geosoft.gxapi.GXEUL3.destr`

:func:`geosoft.gxapi.GXEUL3.get_result`

:func:`geosoft.gxapi.GXEUL3.write`

:func:`geosoft.gxapi.GXEXP.create_file`

:func:`geosoft.gxapi.GXEXP.create`

:func:`geosoft.gxapi.GXEXT.get_info`

:func:`geosoft.gxapi.GXFFT.app_dens`

:func:`geosoft.gxapi.GXFFT.app_susc`

:func:`geosoft.gxapi.GXFFT.b_worth`

:func:`geosoft.gxapi.GXFFT.band_pass`

:func:`geosoft.gxapi.GXFFT.contin`

:func:`geosoft.gxapi.GXFFT.cos_roll`

:func:`geosoft.gxapi.GXFFT.create_ref`

:func:`geosoft.gxapi.GXFFT.create`

:func:`geosoft.gxapi.GXFFT.gaus`

:func:`geosoft.gxapi.GXFFT.get_vv`

:func:`geosoft.gxapi.GXFFT.h_drv`

:func:`geosoft.gxapi.GXFFT.high_pass`

:func:`geosoft.gxapi.GXFFT.inverse`

:func:`geosoft.gxapi.GXFFT.low_pass`

:func:`geosoft.gxapi.GXFFT.nyquist`

:func:`geosoft.gxapi.GXFFT.red_pol`

:func:`geosoft.gxapi.GXFFT.samp_incr`

:func:`geosoft.gxapi.GXFFT.set_vv`

:func:`geosoft.gxapi.GXFFT.spectrum`

:func:`geosoft.gxapi.GXFFT.v_drv`

:func:`geosoft.gxapi.GXFFT.v_int`

:func:`geosoft.gxapi.GXFFT.wave_incr`

:func:`geosoft.gxapi.GXFFT.write_spectrum`

:func:`geosoft.gxapi.GXFFT2.fft2_in`

:func:`geosoft.gxapi.GXFFT2.filter_pg`

:func:`geosoft.gxapi.GXFFT2.flt_inv`

:func:`geosoft.gxapi.GXFFT2.flt`

:func:`geosoft.gxapi.GXFFT2.pow_spc`

:func:`geosoft.gxapi.GXFFT2.rad_spc`

:func:`geosoft.gxapi.GXFFT2.trans_pg`

:func:`geosoft.gxapi.GXFLT.create`

:func:`geosoft.gxapi.GXFLT.load`

:func:`geosoft.gxapi.GXGD.create`

:func:`geosoft.gxapi.GXGER.create`

:func:`geosoft.gxapi.GXGER.get`

:func:`geosoft.gxapi.GXGER.set_double`

:func:`geosoft.gxapi.GXGER.set_int`

:func:`geosoft.gxapi.GXGER.set_string`

:func:`geosoft.gxapi.GXGIS.create`

:func:`geosoft.gxapi.GXGIS.get_ipj`

:func:`geosoft.gxapi.GXGIS.get_range`

:func:`geosoft.gxapi.GXGIS.is_mi_map_file`

:func:`geosoft.gxapi.GXGIS.is_mi_raster_tab_file`

:func:`geosoft.gxapi.GXGIS.load_gdb`

:func:`geosoft.gxapi.GXGIS.load_map`

:func:`geosoft.gxapi.GXGIS.scan_mi_raster_tab_file`

:func:`geosoft.gxapi.GXGU.em_half_space_inv`

:func:`geosoft.gxapi.GXGU.em_half_space_vv`

:func:`geosoft.gxapi.GXGU.em_layer`

:func:`geosoft.gxapi.GXGU.em_plate`

:func:`geosoft.gxapi.GXGU.geometrics2_db`

:func:`geosoft.gxapi.GXGU.geometrics2_tbl`

:func:`geosoft.gxapi.GXGU.geometrics_qc`

:func:`geosoft.gxapi.GXGU.geonics3138_dump2_db`

:func:`geosoft.gxapi.GXGU.geonics61_dump2_db`

:func:`geosoft.gxapi.GXGU.geonics_dat2_db`

:func:`geosoft.gxapi.GXGU.gr_curv_cor`

:func:`geosoft.gxapi.GXGU.vv_euler2`

:func:`geosoft.gxapi.GXGU.vv_euler`

:func:`geosoft.gxapi.GXGUI.browse_dir`

:func:`geosoft.gxapi.GXGUI.color_form`

:func:`geosoft.gxapi.GXGUI.color_transform_ex`

:func:`geosoft.gxapi.GXGUI.color_transform`

:func:`geosoft.gxapi.GXGUI.coord_sys_wizard_licensed`

:func:`geosoft.gxapi.GXGUI.coord_sys_wizard`

:func:`geosoft.gxapi.GXGUI.create_wnd_from_hwnd`

:func:`geosoft.gxapi.GXGUI.cumulative_percent`

:func:`geosoft.gxapi.GXGUI.dat_file_form`

:func:`geosoft.gxapi.GXGUI.database_type`

:func:`geosoft.gxapi.GXGUI.datamine_type`

:func:`geosoft.gxapi.GXGUI.export_xyz_template_editor_ex`

:func:`geosoft.gxapi.GXGUI.export_xyz_template_editor`

:func:`geosoft.gxapi.GXGUI.fft2_spec_filter`

:func:`geosoft.gxapi.GXGUI.gen_file_form`

:func:`geosoft.gxapi.GXGUI.get_area_of_interest_3d`

:func:`geosoft.gxapi.GXGUI.get_area_of_interest`

:func:`geosoft.gxapi.GXGUI.get_parent_wnd`

:func:`geosoft.gxapi.GXGUI.get_printer_lst`

:func:`geosoft.gxapi.GXGUI.grid_stat_hist`

:func:`geosoft.gxapi.GXGUI.import_ascii_wizard`

:func:`geosoft.gxapi.GXGUI.import_chem_database_ado`

:func:`geosoft.gxapi.GXGUI.import_chem_database`

:func:`geosoft.gxapi.GXGUI.import_chem_wizard`

:func:`geosoft.gxapi.GXGUI.import_database_ado`

:func:`geosoft.gxapi.GXGUI.import_database_sql`

:func:`geosoft.gxapi.GXGUI.import_database_sqlado`

:func:`geosoft.gxapi.GXGUI.import_database`

:func:`geosoft.gxapi.GXGUI.import_drill_database_ado2`

:func:`geosoft.gxapi.GXGUI.import_drill_database_ado`

:func:`geosoft.gxapi.GXGUI.import_drill_database_esri`

:func:`geosoft.gxapi.GXGUI.import_drill_database_odbc`

:func:`geosoft.gxapi.GXGUI.import_drill_wizard`

:func:`geosoft.gxapi.GXGUI.import_template_sql`

:func:`geosoft.gxapi.GXGUI.import_template_sqlado`

:func:`geosoft.gxapi.GXGUI.import_xyz_template_editor`

:func:`geosoft.gxapi.GXGUI.internet_trust`

:func:`geosoft.gxapi.GXGUI.launch_geo_dotnetx_tool`

:func:`geosoft.gxapi.GXGUI.launch_geo_x_tool`

:func:`geosoft.gxapi.GXGUI.launch_single_geo_dotnetx_tool`

:func:`geosoft.gxapi.GXGUI.meta_data_tool`

:func:`geosoft.gxapi.GXGUI.meta_data_viewer`

:func:`geosoft.gxapi.GXGUI.odbc_file_connect`

:func:`geosoft.gxapi.GXGUI.pattern_form`

:func:`geosoft.gxapi.GXGUI.print_file`

:func:`geosoft.gxapi.GXGUI.render_pattern`

:func:`geosoft.gxapi.GXGUI.set_parent_wnd`

:func:`geosoft.gxapi.GXGUI.set_printer`

:func:`geosoft.gxapi.GXGUI.set_prog_always_on`

:func:`geosoft.gxapi.GXGUI.show_direct_hist`

:func:`geosoft.gxapi.GXGUI.show_hist`

:func:`geosoft.gxapi.GXGUI.simple_map_dialog`

:func:`geosoft.gxapi.GXGUI.symbol_form`

:func:`geosoft.gxapi.GXGUI.thematic_voxel_info`

:func:`geosoft.gxapi.GXGUI.two_panel_selection2`

:func:`geosoft.gxapi.GXGUI.two_panel_selection_ex2`

:func:`geosoft.gxapi.GXGUI.two_panel_selection_ex`

:func:`geosoft.gxapi.GXGUI.two_panel_selection`

:func:`geosoft.gxapi.GXGUI.voxel_stat_hist`

:func:`geosoft.gxapi.GXHTTP.create`

:func:`geosoft.gxapi.GXHTTP.download`

:func:`geosoft.gxapi.GXHTTP.get`

:func:`geosoft.gxapi.GXHTTP.post`

:func:`geosoft.gxapi.GXIEXP.add_grid`

:func:`geosoft.gxapi.GXIEXP.create`

:func:`geosoft.gxapi.GXIEXP.do_formula`

:func:`geosoft.gxapi.GXIGRF.calc_vv`

:func:`geosoft.gxapi.GXIGRF.calc`

:func:`geosoft.gxapi.GXIGRF.create`

:func:`geosoft.gxapi.GXIMG.average2`

:func:`geosoft.gxapi.GXIMG.copy`

:func:`geosoft.gxapi.GXIMG.create_file`

:func:`geosoft.gxapi.GXIMG.create_new_file`

:func:`geosoft.gxapi.GXIMG.create_out_file`

:func:`geosoft.gxapi.GXIMG.create_projected2`

:func:`geosoft.gxapi.GXIMG.create_projected`

:func:`geosoft.gxapi.GXIMG.e_type`

:func:`geosoft.gxapi.GXIMG.get_info`

:func:`geosoft.gxapi.GXIMG.get_ipj`

:func:`geosoft.gxapi.GXIMG.get_pg`

:func:`geosoft.gxapi.GXIMG.get_projected_cell_size`

:func:`geosoft.gxapi.GXIMG.get_tr`

:func:`geosoft.gxapi.GXIMG.get_z`

:func:`geosoft.gxapi.GXIMG.inherit`

:func:`geosoft.gxapi.GXIMG.load_into_pager`

:func:`geosoft.gxapi.GXIMG.ne`

:func:`geosoft.gxapi.GXIMG.nv`

:func:`geosoft.gxapi.GXIMG.nx`

:func:`geosoft.gxapi.GXIMG.ny`

:func:`geosoft.gxapi.GXIMG.opt_kx`

:func:`geosoft.gxapi.GXIMG.query_kx`

:func:`geosoft.gxapi.GXIMG.read_v`

:func:`geosoft.gxapi.GXIMG.read_x`

:func:`geosoft.gxapi.GXIMG.read_y`

:func:`geosoft.gxapi.GXIMG.relocate`

:func:`geosoft.gxapi.GXIMG.report`

:func:`geosoft.gxapi.GXIMG.set_info`

:func:`geosoft.gxapi.GXIMG.set_ipj`

:func:`geosoft.gxapi.GXIMG.set_pg`

:func:`geosoft.gxapi.GXIMG.set_tr`

:func:`geosoft.gxapi.GXIMG.write_v`

:func:`geosoft.gxapi.GXIMG.write_x`

:func:`geosoft.gxapi.GXIMG.write_y`

:func:`geosoft.gxapi.GXIMU.crc_grid_inexact`

:func:`geosoft.gxapi.GXIMU.crc_grid`

:func:`geosoft.gxapi.GXIMU.crc_inexact`

:func:`geosoft.gxapi.GXIMU.crc`

:func:`geosoft.gxapi.GXIMU.grid_add`

:func:`geosoft.gxapi.GXIMU.grid_agc`

:func:`geosoft.gxapi.GXIMU.grid_bool`

:func:`geosoft.gxapi.GXIMU.grid_edge`

:func:`geosoft.gxapi.GXIMU.grid_expand`

:func:`geosoft.gxapi.GXIMU.grid_fill`

:func:`geosoft.gxapi.GXIMU.grid_filt`

:func:`geosoft.gxapi.GXIMU.grid_head`

:func:`geosoft.gxapi.GXIMU.grid_mask`

:func:`geosoft.gxapi.GXIMU.grid_peak`

:func:`geosoft.gxapi.GXIMU.grid_resize`

:func:`geosoft.gxapi.GXIMU.grid_shad`

:func:`geosoft.gxapi.GXIMU.grid_stat_comp`

:func:`geosoft.gxapi.GXIMU.grid_stat_ext`

:func:`geosoft.gxapi.GXIMU.grid_stat_trend_ext`

:func:`geosoft.gxapi.GXIMU.grid_stat_trend`

:func:`geosoft.gxapi.GXIMU.grid_stat`

:func:`geosoft.gxapi.GXIMU.grid_stitch`

:func:`geosoft.gxapi.GXIMU.grid_tiff`

:func:`geosoft.gxapi.GXIMU.grid_trnd`

:func:`geosoft.gxapi.GXIMU.grid_trns`

:func:`geosoft.gxapi.GXIMU.grid_type`

:func:`geosoft.gxapi.GXIMU.grid_vd`

:func:`geosoft.gxapi.GXIMU.grid_vol`

:func:`geosoft.gxapi.GXIMU.grid_wind2`

:func:`geosoft.gxapi.GXIMU.grid_wind`

:func:`geosoft.gxapi.GXIMU.grid_xyz`

:func:`geosoft.gxapi.GXIMU.peak_size`

:func:`geosoft.gxapi.GXIMU.profile_vv`

:func:`geosoft.gxapi.GXIMU.profile`

:func:`geosoft.gxapi.GXIMU.range_ll`

:func:`geosoft.gxapi.GXINTERNET.download_http`

:func:`geosoft.gxapi.GXINTERNET.send_mail`

:func:`geosoft.gxapi.GXIP.create`

:func:`geosoft.gxapi.GXIP.export_i2_x`

:func:`geosoft.gxapi.GXIP.export_ipdata`

:func:`geosoft.gxapi.GXIP.export_ipred`

:func:`geosoft.gxapi.GXIP.export_sgdf`

:func:`geosoft.gxapi.GXIP.get_chan_label`

:func:`geosoft.gxapi.GXIP.import_dump`

:func:`geosoft.gxapi.GXIP.import_grid`

:func:`geosoft.gxapi.GXIP.import_i2_x`

:func:`geosoft.gxapi.GXIP.import_ipdata`

:func:`geosoft.gxapi.GXIP.import_sgdf`

:func:`geosoft.gxapi.GXIP.import_topo_csv`

:func:`geosoft.gxapi.GXIP.import_topo_grid`

:func:`geosoft.gxapi.GXIP.import_zonge_avg`

:func:`geosoft.gxapi.GXIP.import_zonge_fld`

:func:`geosoft.gxapi.GXIP.new_xy_database`

:func:`geosoft.gxapi.GXIP.ps_stack`

:func:`geosoft.gxapi.GXIP.pseudo_plot`

:func:`geosoft.gxapi.GXIP.recalculate`

:func:`geosoft.gxapi.GXIP.window`

:func:`geosoft.gxapi.GXIP.winnow_chan_list`

:func:`geosoft.gxapi.GXIPJ.add_exagg_warp`

:func:`geosoft.gxapi.GXIPJ.add_warp`

:func:`geosoft.gxapi.GXIPJ.clear_warp`

:func:`geosoft.gxapi.GXIPJ.copy`

:func:`geosoft.gxapi.GXIPJ.create_s`

:func:`geosoft.gxapi.GXIPJ.create`

:func:`geosoft.gxapi.GXIPJ.get_gxf`

:func:`geosoft.gxapi.GXIPJ.get_method_parm`

:func:`geosoft.gxapi.GXIPJ.get_name`

:func:`geosoft.gxapi.GXIPJ.get_units`

:func:`geosoft.gxapi.GXIPJ.read`

:func:`geosoft.gxapi.GXIPJ.serial`

:func:`geosoft.gxapi.GXIPJ.set_gxf`

:func:`geosoft.gxapi.GXIPJ.set_method_parm`

:func:`geosoft.gxapi.GXIPJ.set_units`

:func:`geosoft.gxapi.GXIPJ.source_type`

:func:`geosoft.gxapi.GXIPJ.unit_name`

:func:`geosoft.gxapi.GXIPJ.unit_scale`

:func:`geosoft.gxapi.GXIPJ.warped`

:func:`geosoft.gxapi.GXITR.change_brightness`

:func:`geosoft.gxapi.GXITR.copy`

:func:`geosoft.gxapi.GXITR.create_file`

:func:`geosoft.gxapi.GXITR.create_map`

:func:`geosoft.gxapi.GXITR.create_s`

:func:`geosoft.gxapi.GXITR.create`

:func:`geosoft.gxapi.GXITR.get_brightness`

:func:`geosoft.gxapi.GXITR.get_reg`

:func:`geosoft.gxapi.GXITR.get_size`

:func:`geosoft.gxapi.GXITR.get_zone_color`

:func:`geosoft.gxapi.GXITR.get_zone_value`

:func:`geosoft.gxapi.GXITR.linear`

:func:`geosoft.gxapi.GXITR.log_linear`

:func:`geosoft.gxapi.GXITR.power_zone`

:func:`geosoft.gxapi.GXITR.serial`

:func:`geosoft.gxapi.GXITR.set_agg_map`

:func:`geosoft.gxapi.GXITR.set_bright_contrast`

:func:`geosoft.gxapi.GXITR.set_size`

:func:`geosoft.gxapi.GXITR.set_zone_color`

:func:`geosoft.gxapi.GXITR.set_zone_value`

:func:`geosoft.gxapi.GXKGRD.clear`

:func:`geosoft.gxapi.GXKGRD.create`

:func:`geosoft.gxapi.GXLL2.create`

:func:`geosoft.gxapi.GXLL2.save`

:func:`geosoft.gxapi.GXLL2.set_row`

:func:`geosoft.gxapi.GXLPT.create`

:func:`geosoft.gxapi.GXLPT.get_lst`

:func:`geosoft.gxapi.GXLST.add_item`

:func:`geosoft.gxapi.GXLST.add_unique_item`

:func:`geosoft.gxapi.GXLST.clear`

:func:`geosoft.gxapi.GXLST.copy`

:func:`geosoft.gxapi.GXLST.create_s`

:func:`geosoft.gxapi.GXLST.create`

:func:`geosoft.gxapi.GXLST.del_item`

:func:`geosoft.gxapi.GXLST.find_item`

:func:`geosoft.gxapi.GXLST.gt_item`

:func:`geosoft.gxapi.GXLST.load_csv`

:func:`geosoft.gxapi.GXLST.resource`

:func:`geosoft.gxapi.GXLST.save_file`

:func:`geosoft.gxapi.GXLST.serial`

:func:`geosoft.gxapi.GXLST.size`

:func:`geosoft.gxapi.GXLST.sort`

:func:`geosoft.gxapi.GXLTB.add_record`

:func:`geosoft.gxapi.GXLTB.create`

:func:`geosoft.gxapi.GXLTB.delete_record`

:func:`geosoft.gxapi.GXLTB.fields`

:func:`geosoft.gxapi.GXLTB.find_field`

:func:`geosoft.gxapi.GXLTB.find_key`

:func:`geosoft.gxapi.GXLTB.get_con_lst`

:func:`geosoft.gxapi.GXLTB.get_double`

:func:`geosoft.gxapi.GXLTB.get_field`

:func:`geosoft.gxapi.GXLTB.get_int`

:func:`geosoft.gxapi.GXLTB.get_lst2`

:func:`geosoft.gxapi.GXLTB.get_lst`

:func:`geosoft.gxapi.GXLTB.get_string`

:func:`geosoft.gxapi.GXLTB.merge`

:func:`geosoft.gxapi.GXLTB.records`

:func:`geosoft.gxapi.GXLTB.save`

:func:`geosoft.gxapi.GXLTB.search`

:func:`geosoft.gxapi.GXLTB.set_double`

:func:`geosoft.gxapi.GXLTB.set_int`

:func:`geosoft.gxapi.GXLTB.set_string`

:func:`geosoft.gxapi.GXMAP.agg_list`

:func:`geosoft.gxapi.GXMAP.clean`

:func:`geosoft.gxapi.GXMAP.commit`

:func:`geosoft.gxapi.GXMAP.create`

:func:`geosoft.gxapi.GXMAP.current`

:func:`geosoft.gxapi.GXMAP.delete_view`

:func:`geosoft.gxapi.GXMAP.discard`

:func:`geosoft.gxapi.GXMAP.dup_map`

:func:`geosoft.gxapi.GXMAP.exist_view`

:func:`geosoft.gxapi.GXMAP.get_class_name`

:func:`geosoft.gxapi.GXMAP.get_file_name`

:func:`geosoft.gxapi.GXMAP.get_lpt`

:func:`geosoft.gxapi.GXMAP.get_map_name`

:func:`geosoft.gxapi.GXMAP.get_map_scale`

:func:`geosoft.gxapi.GXMAP.get_map_size`

:func:`geosoft.gxapi.GXMAP.get_reg`

:func:`geosoft.gxapi.GXMAP.group_list`

:func:`geosoft.gxapi.GXMAP.pack_files`

:func:`geosoft.gxapi.GXMAP.render`

:func:`geosoft.gxapi.GXMAP.resize_all`

:func:`geosoft.gxapi.GXMAP.set_class_name`

:func:`geosoft.gxapi.GXMAP.set_current`

:func:`geosoft.gxapi.GXMAP.set_map_name`

:func:`geosoft.gxapi.GXMAP.set_map_scale`

:func:`geosoft.gxapi.GXMAP.set_map_size`

:func:`geosoft.gxapi.GXMAP.set_reg`

:func:`geosoft.gxapi.GXMAP.un_pack_files`

:func:`geosoft.gxapi.GXMAP.view_list`

:func:`geosoft.gxapi.GXMAPL.create_reg`

:func:`geosoft.gxapi.GXMAPL.create`

:func:`geosoft.gxapi.GXMAPL.process`

:func:`geosoft.gxapi.GXMAPL.replace_string`

:func:`geosoft.gxapi.GXMISC.ukoa2_tbl`

:func:`geosoft.gxapi.GXMSTK.add_stk`

:func:`geosoft.gxapi.GXMSTK.chan_list_vv`

:func:`geosoft.gxapi.GXMSTK.create`

:func:`geosoft.gxapi.GXMSTK.delete_stk`

:func:`geosoft.gxapi.GXMSTK.draw_profile`

:func:`geosoft.gxapi.GXMSTK.find_stk2`

:func:`geosoft.gxapi.GXMSTK.find_stk`

:func:`geosoft.gxapi.GXMSTK.get_num_stk`

:func:`geosoft.gxapi.GXMSTK.get_stk`

:func:`geosoft.gxapi.GXMSTK.read_ini`

:func:`geosoft.gxapi.GXMSTK.save_profile`

:func:`geosoft.gxapi.GXMVG.axis_x`

:func:`geosoft.gxapi.GXMVG.axis_y`

:func:`geosoft.gxapi.GXMVG.create`

:func:`geosoft.gxapi.GXMVG.get_mview`

:func:`geosoft.gxapi.GXMVG.grid`

:func:`geosoft.gxapi.GXMVG.label_x`

:func:`geosoft.gxapi.GXMVG.label_y`

:func:`geosoft.gxapi.GXMVG.poly_line_va`

:func:`geosoft.gxapi.GXMVG.poly_line_vv`

:func:`geosoft.gxapi.GXMVG.rescale_x_range`

:func:`geosoft.gxapi.GXMVG.rescale_y_range`

:func:`geosoft.gxapi.GXMVIEW.aggregate`

:func:`geosoft.gxapi.GXMVIEW.arc`

:func:`geosoft.gxapi.GXMVIEW.axis_x`

:func:`geosoft.gxapi.GXMVIEW.axis_y`

:func:`geosoft.gxapi.GXMVIEW.change_line_message`

:func:`geosoft.gxapi.GXMVIEW.chord`

:func:`geosoft.gxapi.GXMVIEW.classified_symbols`

:func:`geosoft.gxapi.GXMVIEW.clip_clear`

:func:`geosoft.gxapi.GXMVIEW.clip_groups`

:func:`geosoft.gxapi.GXMVIEW.clip_marked_groups`

:func:`geosoft.gxapi.GXMVIEW.clip_mode`

:func:`geosoft.gxapi.GXMVIEW.clip_poly_ex`

:func:`geosoft.gxapi.GXMVIEW.clip_poly`

:func:`geosoft.gxapi.GXMVIEW.clip_rect_ex`

:func:`geosoft.gxapi.GXMVIEW.clip_rect`

:func:`geosoft.gxapi.GXMVIEW.col_symbol`

:func:`geosoft.gxapi.GXMVIEW.color_cmy`

:func:`geosoft.gxapi.GXMVIEW.color_descr`

:func:`geosoft.gxapi.GXMVIEW.color_hsv`

:func:`geosoft.gxapi.GXMVIEW.color_rgb`

:func:`geosoft.gxapi.GXMVIEW.color`

:func:`geosoft.gxapi.GXMVIEW.complex_polygon`

:func:`geosoft.gxapi.GXMVIEW.copy_marked_groups`

:func:`geosoft.gxapi.GXMVIEW.crc_group`

:func:`geosoft.gxapi.GXMVIEW.create`

:func:`geosoft.gxapi.GXMVIEW.del_marked_groups`

:func:`geosoft.gxapi.GXMVIEW.easy_maker`

:func:`geosoft.gxapi.GXMVIEW.ellipse`

:func:`geosoft.gxapi.GXMVIEW.exist_group`

:func:`geosoft.gxapi.GXMVIEW.extent`

:func:`geosoft.gxapi.GXMVIEW.external_string_object`

:func:`geosoft.gxapi.GXMVIEW.fill_color`

:func:`geosoft.gxapi.GXMVIEW.fit_window`

:func:`geosoft.gxapi.GXMVIEW.get_clip_ply`

:func:`geosoft.gxapi.GXMVIEW.get_group_extent`

:func:`geosoft.gxapi.GXMVIEW.get_ipj`

:func:`geosoft.gxapi.GXMVIEW.get_map_scale`

:func:`geosoft.gxapi.GXMVIEW.get_name`

:func:`geosoft.gxapi.GXMVIEW.get_user_ipj`

:func:`geosoft.gxapi.GXMVIEW.grid`

:func:`geosoft.gxapi.GXMVIEW.group_clip_mode`

:func:`geosoft.gxapi.GXMVIEW.group_to_ply`

:func:`geosoft.gxapi.GXMVIEW.hide_marked_groups`

:func:`geosoft.gxapi.GXMVIEW.label_fid`

:func:`geosoft.gxapi.GXMVIEW.label_x`

:func:`geosoft.gxapi.GXMVIEW.label_y`

:func:`geosoft.gxapi.GXMVIEW.line_color`

:func:`geosoft.gxapi.GXMVIEW.line_style`

:func:`geosoft.gxapi.GXMVIEW.line_thick`

:func:`geosoft.gxapi.GXMVIEW.line_vv`

:func:`geosoft.gxapi.GXMVIEW.line`

:func:`geosoft.gxapi.GXMVIEW.link`

:func:`geosoft.gxapi.GXMVIEW.list_groups`

:func:`geosoft.gxapi.GXMVIEW.maker`

:func:`geosoft.gxapi.GXMVIEW.map_origin`

:func:`geosoft.gxapi.GXMVIEW.mark_all_groups`

:func:`geosoft.gxapi.GXMVIEW.mark_group`

:func:`geosoft.gxapi.GXMVIEW.mode_pj`

:func:`geosoft.gxapi.GXMVIEW.north`

:func:`geosoft.gxapi.GXMVIEW.optimum_tick`

:func:`geosoft.gxapi.GXMVIEW.pat_angle`

:func:`geosoft.gxapi.GXMVIEW.pat_density`

:func:`geosoft.gxapi.GXMVIEW.pat_number`

:func:`geosoft.gxapi.GXMVIEW.pat_size`

:func:`geosoft.gxapi.GXMVIEW.pat_style`

:func:`geosoft.gxapi.GXMVIEW.pat_thick`

:func:`geosoft.gxapi.GXMVIEW.plot_to_view`

:func:`geosoft.gxapi.GXMVIEW.poly_line_dm`

:func:`geosoft.gxapi.GXMVIEW.poly_line`

:func:`geosoft.gxapi.GXMVIEW.poly_wrap`

:func:`geosoft.gxapi.GXMVIEW.re_scale`

:func:`geosoft.gxapi.GXMVIEW.rectangle`

:func:`geosoft.gxapi.GXMVIEW.relocate_group`

:func:`geosoft.gxapi.GXMVIEW.scale_all_group`

:func:`geosoft.gxapi.GXMVIEW.scale_mm`

:func:`geosoft.gxapi.GXMVIEW.scale_pj_mm`

:func:`geosoft.gxapi.GXMVIEW.scale_window`

:func:`geosoft.gxapi.GXMVIEW.scale_ymm`

:func:`geosoft.gxapi.GXMVIEW.set_clip_ply`

:func:`geosoft.gxapi.GXMVIEW.set_ipj`

:func:`geosoft.gxapi.GXMVIEW.set_thin_res`

:func:`geosoft.gxapi.GXMVIEW.set_u_fac`

:func:`geosoft.gxapi.GXMVIEW.set_user_ipj`

:func:`geosoft.gxapi.GXMVIEW.set_window`

:func:`geosoft.gxapi.GXMVIEW.set_working_ipj`

:func:`geosoft.gxapi.GXMVIEW.size_symbols`

:func:`geosoft.gxapi.GXMVIEW.start_group`

:func:`geosoft.gxapi.GXMVIEW.symb_angle`

:func:`geosoft.gxapi.GXMVIEW.symb_color`

:func:`geosoft.gxapi.GXMVIEW.symb_fill_color`

:func:`geosoft.gxapi.GXMVIEW.symb_font`

:func:`geosoft.gxapi.GXMVIEW.symb_number`

:func:`geosoft.gxapi.GXMVIEW.symb_size`

:func:`geosoft.gxapi.GXMVIEW.symbol`

:func:`geosoft.gxapi.GXMVIEW.symbols_itr`

:func:`geosoft.gxapi.GXMVIEW.symbols`

:func:`geosoft.gxapi.GXMVIEW.text_angle`

:func:`geosoft.gxapi.GXMVIEW.text_color`

:func:`geosoft.gxapi.GXMVIEW.text_font`

:func:`geosoft.gxapi.GXMVIEW.text_ref`

:func:`geosoft.gxapi.GXMVIEW.text_size`

:func:`geosoft.gxapi.GXMVIEW.text`

:func:`geosoft.gxapi.GXMVIEW.tran_scale`

:func:`geosoft.gxapi.GXMVIEW.user_to_view`

:func:`geosoft.gxapi.GXMVIEW.view_to_plot`

:func:`geosoft.gxapi.GXMVIEW.view_to_user`

:func:`geosoft.gxapi.GXMVU.arrow_vector_vv`

:func:`geosoft.gxapi.GXMVU.arrow`

:func:`geosoft.gxapi.GXMVU.bar_chart`

:func:`geosoft.gxapi.GXMVU.c_symb_legend`

:func:`geosoft.gxapi.GXMVU.color_bar2_style`

:func:`geosoft.gxapi.GXMVU.color_bar2`

:func:`geosoft.gxapi.GXMVU.color_bar_hor`

:func:`geosoft.gxapi.GXMVU.color_bar_style`

:func:`geosoft.gxapi.GXMVU.color_bar`

:func:`geosoft.gxapi.GXMVU.contour`

:func:`geosoft.gxapi.GXMVU.decay_curve`

:func:`geosoft.gxapi.GXMVU.direction_plot`

:func:`geosoft.gxapi.GXMVU.em_forward`

:func:`geosoft.gxapi.GXMVU.flight_plot`

:func:`geosoft.gxapi.GXMVU.gen_areas`

:func:`geosoft.gxapi.GXMVU.histogram2`

:func:`geosoft.gxapi.GXMVU.histogram3`

:func:`geosoft.gxapi.GXMVU.histogram4`

:func:`geosoft.gxapi.GXMVU.histogram5`

:func:`geosoft.gxapi.GXMVU.histogram`

:func:`geosoft.gxapi.GXMVU.load_plot`

:func:`geosoft.gxapi.GXMVU.map_from_plt`

:func:`geosoft.gxapi.GXMVU.map_mdf`

:func:`geosoft.gxapi.GXMVU.mapset`

:func:`geosoft.gxapi.GXMVU.mdf`

:func:`geosoft.gxapi.GXMVU.path_plot_ex`

:func:`geosoft.gxapi.GXMVU.path_plot`

:func:`geosoft.gxapi.GXMVU.post_ex`

:func:`geosoft.gxapi.GXMVU.post`

:func:`geosoft.gxapi.GXMVU.profile_plot_ex`

:func:`geosoft.gxapi.GXMVU.profile_plot`

:func:`geosoft.gxapi.GXMVU.re_gen_areas`

:func:`geosoft.gxapi.GXMVU.symb_off`

:func:`geosoft.gxapi.GXMVU.text_box`

:func:`geosoft.gxapi.GXMVU.tick`

:func:`geosoft.gxapi.GXMVU.trnd_path`

:func:`geosoft.gxapi.GXPAT.create`

:func:`geosoft.gxapi.GXPAT.get_lst`

:func:`geosoft.gxapi.GXPG.copy_subset`

:func:`geosoft.gxapi.GXPG.copy`

:func:`geosoft.gxapi.GXPG.create_s`

:func:`geosoft.gxapi.GXPG.create`

:func:`geosoft.gxapi.GXPG.dummy`

:func:`geosoft.gxapi.GXPG.e_type`

:func:`geosoft.gxapi.GXPG.n_cols`

:func:`geosoft.gxapi.GXPG.n_rows`

:func:`geosoft.gxapi.GXPG.range`

:func:`geosoft.gxapi.GXPG.re_allocate`

:func:`geosoft.gxapi.GXPG.read_col`

:func:`geosoft.gxapi.GXPG.read_row`

:func:`geosoft.gxapi.GXPG.serial`

:func:`geosoft.gxapi.GXPG.write_col`

:func:`geosoft.gxapi.GXPG.write_row`

:func:`geosoft.gxapi.GXPGU.bool_mask`

:func:`geosoft.gxapi.GXPGU.correlation_matrix`

:func:`geosoft.gxapi.GXPGU.expand`

:func:`geosoft.gxapi.GXPGU.fill`

:func:`geosoft.gxapi.GXPGU.filt_sym5`

:func:`geosoft.gxapi.GXPGU.grid_peak`

:func:`geosoft.gxapi.GXPGU.invert_matrix`

:func:`geosoft.gxapi.GXPGU.jacobi`

:func:`geosoft.gxapi.GXPGU.lu_back_sub`

:func:`geosoft.gxapi.GXPGU.lu_decomp`

:func:`geosoft.gxapi.GXPGU.matrix_mult`

:func:`geosoft.gxapi.GXPGU.matrix_vector_mult`

:func:`geosoft.gxapi.GXPGU.pc_communality`

:func:`geosoft.gxapi.GXPGU.pc_loadings`

:func:`geosoft.gxapi.GXPGU.pc_scores`

:func:`geosoft.gxapi.GXPGU.pc_standardize`

:func:`geosoft.gxapi.GXPGU.pc_transform`

:func:`geosoft.gxapi.GXPGU.pc_varimax`

:func:`geosoft.gxapi.GXPGU.ref_file`

:func:`geosoft.gxapi.GXPGU.save_file`

:func:`geosoft.gxapi.GXPGU.sv_decompose`

:func:`geosoft.gxapi.GXPGU.sv_recompose`

:func:`geosoft.gxapi.GXPGU.trend`

:func:`geosoft.gxapi.GXPJ.clip_ply`

:func:`geosoft.gxapi.GXPJ.convert_vv3`

:func:`geosoft.gxapi.GXPJ.convert_vv`

:func:`geosoft.gxapi.GXPJ.convert_xy`

:func:`geosoft.gxapi.GXPJ.create_ipj`

:func:`geosoft.gxapi.GXPJ.create_rectified`

:func:`geosoft.gxapi.GXPJ.create`

:func:`geosoft.gxapi.GXPJ.is_input_ll`

:func:`geosoft.gxapi.GXPJ.is_output_ll`

:func:`geosoft.gxapi.GXPLY.add_polygon_ex`

:func:`geosoft.gxapi.GXPLY.add_polygon`

:func:`geosoft.gxapi.GXPLY.copy`

:func:`geosoft.gxapi.GXPLY.create`

:func:`geosoft.gxapi.GXPLY.extent`

:func:`geosoft.gxapi.GXPLY.get_polygon_ex`

:func:`geosoft.gxapi.GXPLY.get_polygon`

:func:`geosoft.gxapi.GXPLY.load_table`

:func:`geosoft.gxapi.GXPLY.num_poly`

:func:`geosoft.gxapi.GXPLY.rotate`

:func:`geosoft.gxapi.GXPLY.save_table`

:func:`geosoft.gxapi.GXPROJ.add_document`

:func:`geosoft.gxapi.GXPROJ.drop_map_clip_data`

:func:`geosoft.gxapi.GXPROJ.get_command_environment`

:func:`geosoft.gxapi.GXPROJ.list_documents`

:func:`geosoft.gxapi.GXPROJ.list_tools`

:func:`geosoft.gxapi.GXPROJ.remove_document`

:func:`geosoft.gxapi.GXPROJ.remove_tool`

:func:`geosoft.gxapi.GXPROJ.save_close_documents`

:func:`geosoft.gxapi.GXRA.create_sbf`

:func:`geosoft.gxapi.GXRA.create`

:func:`geosoft.gxapi.GXRA.gets`

:func:`geosoft.gxapi.GXRA.len`

:func:`geosoft.gxapi.GXRA.line`

:func:`geosoft.gxapi.GXRA.seek`

:func:`geosoft.gxapi.GXREG.clear`

:func:`geosoft.gxapi.GXREG.copy`

:func:`geosoft.gxapi.GXREG.create_s`

:func:`geosoft.gxapi.GXREG.create`

:func:`geosoft.gxapi.GXREG.get_double`

:func:`geosoft.gxapi.GXREG.get_int`

:func:`geosoft.gxapi.GXREG.get`

:func:`geosoft.gxapi.GXREG.load_ini`

:func:`geosoft.gxapi.GXREG.match_string`

:func:`geosoft.gxapi.GXREG.merge`

:func:`geosoft.gxapi.GXREG.save_ini`

:func:`geosoft.gxapi.GXREG.serial`

:func:`geosoft.gxapi.GXREG.set_double`

:func:`geosoft.gxapi.GXREG.set_int`

:func:`geosoft.gxapi.GXREG.set`

:func:`geosoft.gxapi.GXRGRD.clear`

:func:`geosoft.gxapi.GXRGRD.create`

:func:`geosoft.gxapi.GXSBF.create`

:func:`geosoft.gxapi.GXSBF.del_dir`

:func:`geosoft.gxapi.GXSBF.del_file`

:func:`geosoft.gxapi.GXSBF.exist_dir`

:func:`geosoft.gxapi.GXSBF.exist_file`

:func:`geosoft.gxapi.GXSBF.h_get_db`

:func:`geosoft.gxapi.GXSBF.h_get_map`

:func:`geosoft.gxapi.GXSBF.h_get_sys`

:func:`geosoft.gxapi.GXSBF.save_log`

:func:`geosoft.gxapi.GXST.create`

:func:`geosoft.gxapi.GXST.data_vv`

:func:`geosoft.gxapi.GXST.data`

:func:`geosoft.gxapi.GXST.get_info`

:func:`geosoft.gxapi.GXST.histogram2`

:func:`geosoft.gxapi.GXST.histogram`

:func:`geosoft.gxapi.GXST.normal_test`

:func:`geosoft.gxapi.GXST.reset`

:func:`geosoft.gxapi.GXST2.create`

:func:`geosoft.gxapi.GXST2.data_vv`

:func:`geosoft.gxapi.GXST2.get`

:func:`geosoft.gxapi.GXST2.items`

:func:`geosoft.gxapi.GXST2.reset`

:func:`geosoft.gxapi.GXSTK.get_axis_parms`

:func:`geosoft.gxapi.GXSTK.get_fid_parms`

:func:`geosoft.gxapi.GXSTK.get_gen_parms`

:func:`geosoft.gxapi.GXSTK.get_grid_parms`

:func:`geosoft.gxapi.GXSTK.get_label_parms`

:func:`geosoft.gxapi.GXSTK.get_profile`

:func:`geosoft.gxapi.GXSTK.get_symb_parms`

:func:`geosoft.gxapi.GXSTK.get_title_parms`

:func:`geosoft.gxapi.GXSTK.get_trans_parms`

:func:`geosoft.gxapi.GXSTK.set_axis_parms`

:func:`geosoft.gxapi.GXSTK.set_fid_parms`

:func:`geosoft.gxapi.GXSTK.set_flag`

:func:`geosoft.gxapi.GXSTK.set_gen_parms`

:func:`geosoft.gxapi.GXSTK.set_grid_parms`

:func:`geosoft.gxapi.GXSTK.set_label_parms`

:func:`geosoft.gxapi.GXSTK.set_line_parm`

:func:`geosoft.gxapi.GXSTK.set_profile`

:func:`geosoft.gxapi.GXSTK.set_symb_parms`

:func:`geosoft.gxapi.GXSTK.set_title_parms`

:func:`geosoft.gxapi.GXSTK.set_trans_parms`

:func:`geosoft.gxapi.GXSTR.char_n`

:func:`geosoft.gxapi.GXSTR.count_tokens`

:func:`geosoft.gxapi.GXSTR.file_combine_parts`

:func:`geosoft.gxapi.GXSTR.file_ext`

:func:`geosoft.gxapi.GXSTR.file_name_part`

:func:`geosoft.gxapi.GXSTR.format_crc`

:func:`geosoft.gxapi.GXSTR.format_date`

:func:`geosoft.gxapi.GXSTR.format_double`

:func:`geosoft.gxapi.GXSTR.format_i`

:func:`geosoft.gxapi.GXSTR.format_r2`

:func:`geosoft.gxapi.GXSTR.format_r`

:func:`geosoft.gxapi.GXSTR.format_time`

:func:`geosoft.gxapi.GXSTR.get_char`

:func:`geosoft.gxapi.GXSTR.get_m_file`

:func:`geosoft.gxapi.GXSTR.get_token`

:func:`geosoft.gxapi.GXSTR.justify`

:func:`geosoft.gxapi.GXSTR.replace_char`

:func:`geosoft.gxapi.GXSTR.split_string`

:func:`geosoft.gxapi.GXSTR.str_mask`

:func:`geosoft.gxapi.GXSTR.str_min2`

:func:`geosoft.gxapi.GXSTR.str_min`

:func:`geosoft.gxapi.GXSTR.strcat`

:func:`geosoft.gxapi.GXSTR.strcmp`

:func:`geosoft.gxapi.GXSTR.strcpy`

:func:`geosoft.gxapi.GXSTR.stri_mask`

:func:`geosoft.gxapi.GXSTR.strlen`

:func:`geosoft.gxapi.GXSTR.to_lower`

:func:`geosoft.gxapi.GXSTR.to_upper`

:func:`geosoft.gxapi.GXSTR.tokenize`

:func:`geosoft.gxapi.GXSTR.tokens2`

:func:`geosoft.gxapi.GXSTR.tokens`

:func:`geosoft.gxapi.GXSTR.trim_quotes`

:func:`geosoft.gxapi.GXSTR.trim_space`

:func:`geosoft.gxapi.GXSTR.un_quote`

:func:`geosoft.gxapi.GXSTR.xyz_line`

:func:`geosoft.gxapi.GXSYS.abort`

:func:`geosoft.gxapi.GXSYS.absolute_file_name`

:func:`geosoft.gxapi.GXSYS.assert_gx`

:func:`geosoft.gxapi.GXSYS.assert`

:func:`geosoft.gxapi.GXSYS.cancel`

:func:`geosoft.gxapi.GXSYS.check_stop`

:func:`geosoft.gxapi.GXSYS.clear_group`

:func:`geosoft.gxapi.GXSYS.clear_menus`

:func:`geosoft.gxapi.GXSYS.clear_parm`

:func:`geosoft.gxapi.GXSYS.clipboard_to_file`

:func:`geosoft.gxapi.GXSYS.create_clipboard_ra`

:func:`geosoft.gxapi.GXSYS.create_clipboard_wa`

:func:`geosoft.gxapi.GXSYS.date`

:func:`geosoft.gxapi.GXSYS.delete_file`

:func:`geosoft.gxapi.GXSYS.delete_gi_file`

:func:`geosoft.gxapi.GXSYS.destroy_ptmp`

:func:`geosoft.gxapi.GXSYS.dir_exist`

:func:`geosoft.gxapi.GXSYS.disable_gx_debugger`

:func:`geosoft.gxapi.GXSYS.display_double`

:func:`geosoft.gxapi.GXSYS.display_help_topic`

:func:`geosoft.gxapi.GXSYS.display_help`

:func:`geosoft.gxapi.GXSYS.display_int`

:func:`geosoft.gxapi.GXSYS.display_message`

:func:`geosoft.gxapi.GXSYS.display_question_with_cancel`

:func:`geosoft.gxapi.GXSYS.display_question`

:func:`geosoft.gxapi.GXSYS.do_command`

:func:`geosoft.gxapi.GXSYS.enable_gx_debugger`

:func:`geosoft.gxapi.GXSYS.error_tag`

:func:`geosoft.gxapi.GXSYS.error`

:func:`geosoft.gxapi.GXSYS.exist_env`

:func:`geosoft.gxapi.GXSYS.exit`

:func:`geosoft.gxapi.GXSYS.file_date`

:func:`geosoft.gxapi.GXSYS.file_exist`

:func:`geosoft.gxapi.GXSYS.file_ren`

:func:`geosoft.gxapi.GXSYS.file_size`

:func:`geosoft.gxapi.GXSYS.file_time`

:func:`geosoft.gxapi.GXSYS.file_to_clipboard`

:func:`geosoft.gxapi.GXSYS.find_files_vv`

:func:`geosoft.gxapi.GXSYS.font_lst`

:func:`geosoft.gxapi.GXSYS.get_directory`

:func:`geosoft.gxapi.GXSYS.get_env`

:func:`geosoft.gxapi.GXSYS.get_path`

:func:`geosoft.gxapi.GXSYS.get_ptmp`

:func:`geosoft.gxapi.GXSYS.get_reg`

:func:`geosoft.gxapi.GXSYS.get_sys_info`

:func:`geosoft.gxapi.GXSYS.get_windows_dir`

:func:`geosoft.gxapi.GXSYS.get_workspace_reg`

:func:`geosoft.gxapi.GXSYS.get_yes_no`

:func:`geosoft.gxapi.GXSYS.global_reset`

:func:`geosoft.gxapi.GXSYS.global_set`

:func:`geosoft.gxapi.GXSYS.global_write`

:func:`geosoft.gxapi.GXSYS.gt_string`

:func:`geosoft.gxapi.GXSYS.interactive`

:func:`geosoft.gxapi.GXSYS.load_parm`

:func:`geosoft.gxapi.GXSYS.make_dir`

:func:`geosoft.gxapi.GXSYS.ole_automation`

:func:`geosoft.gxapi.GXSYS.prog_name`

:func:`geosoft.gxapi.GXSYS.prog_update_l`

:func:`geosoft.gxapi.GXSYS.prog_update`

:func:`geosoft.gxapi.GXSYS.progress`

:func:`geosoft.gxapi.GXSYS.prompt`

:func:`geosoft.gxapi.GXSYS.registry_delete_key`

:func:`geosoft.gxapi.GXSYS.registry_delete_val`

:func:`geosoft.gxapi.GXSYS.registry_set_val`

:func:`geosoft.gxapi.GXSYS.replace_string`

:func:`geosoft.gxapi.GXSYS.run_gs`

:func:`geosoft.gxapi.GXSYS.run_gx_ex`

:func:`geosoft.gxapi.GXSYS.run_gx`

:func:`geosoft.gxapi.GXSYS.run_pdf`

:func:`geosoft.gxapi.GXSYS.run`

:func:`geosoft.gxapi.GXSYS.save_log`

:func:`geosoft.gxapi.GXSYS.save_parm`

:func:`geosoft.gxapi.GXSYS.save_ptmp`

:func:`geosoft.gxapi.GXSYS.set_cursor`

:func:`geosoft.gxapi.GXSYS.set_double`

:func:`geosoft.gxapi.GXSYS.set_env`

:func:`geosoft.gxapi.GXSYS.set_info_line`

:func:`geosoft.gxapi.GXSYS.set_int`

:func:`geosoft.gxapi.GXSYS.set_interactive`

:func:`geosoft.gxapi.GXSYS.set_reg`

:func:`geosoft.gxapi.GXSYS.set_return`

:func:`geosoft.gxapi.GXSYS.set_string`

:func:`geosoft.gxapi.GXSYS.set_workspace_reg`

:func:`geosoft.gxapi.GXSYS.shell_execute`

:func:`geosoft.gxapi.GXSYS.short_path_file_name`

:func:`geosoft.gxapi.GXSYS.show_error`

:func:`geosoft.gxapi.GXSYS.temp_file_name`

:func:`geosoft.gxapi.GXSYS.terminate`

:func:`geosoft.gxapi.GXSYS.time`

:func:`geosoft.gxapi.GXSYS.valid_file_name`

:func:`geosoft.gxapi.GXSYS.write_in_dir`

:func:`geosoft.gxapi.GXTB.create_db`

:func:`geosoft.gxapi.GXTB.create_ltb`

:func:`geosoft.gxapi.GXTB.create`

:func:`geosoft.gxapi.GXTB.field`

:func:`geosoft.gxapi.GXTB.find_col_by_name`

:func:`geosoft.gxapi.GXTB.get_double`

:func:`geosoft.gxapi.GXTB.get_int`

:func:`geosoft.gxapi.GXTB.get_string`

:func:`geosoft.gxapi.GXTB.load_db`

:func:`geosoft.gxapi.GXTB.num_columns`

:func:`geosoft.gxapi.GXTB.num_rows`

:func:`geosoft.gxapi.GXTB.save_db`

:func:`geosoft.gxapi.GXTB.save_to_ascii`

:func:`geosoft.gxapi.GXTB.save`

:func:`geosoft.gxapi.GXTB.set_double`

:func:`geosoft.gxapi.GXTB.set_int`

:func:`geosoft.gxapi.GXTB.set_search_mode`

:func:`geosoft.gxapi.GXTB.set_string`

:func:`geosoft.gxapi.GXTB.sort`

:func:`geosoft.gxapi.GXTC.create`

:func:`geosoft.gxapi.GXTC.grregter`

:func:`geosoft.gxapi.GXTC.grterain`

:func:`geosoft.gxapi.GXTIN.copy`

:func:`geosoft.gxapi.GXTIN.create_s`

:func:`geosoft.gxapi.GXTIN.create`

:func:`geosoft.gxapi.GXTIN.get_convex_hull`

:func:`geosoft.gxapi.GXTIN.get_joins`

:func:`geosoft.gxapi.GXTIN.get_mesh`

:func:`geosoft.gxapi.GXTIN.get_nodes`

:func:`geosoft.gxapi.GXTIN.get_triangle`

:func:`geosoft.gxapi.GXTIN.get_voronoi_edges`

:func:`geosoft.gxapi.GXTIN.interp_vv`

:func:`geosoft.gxapi.GXTIN.is_z_valued`

:func:`geosoft.gxapi.GXTIN.locate_triangle`

:func:`geosoft.gxapi.GXTIN.nodes`

:func:`geosoft.gxapi.GXTIN.range_xy`

:func:`geosoft.gxapi.GXTIN.serial`

:func:`geosoft.gxapi.GXTIN.triangles`

:func:`geosoft.gxapi.GXTR.create`

:func:`geosoft.gxapi.GXTRND.get_max_min`

:func:`geosoft.gxapi.GXTRND.get_mesh`

:func:`geosoft.gxapi.GXTRND.trnd_db`

:func:`geosoft.gxapi.GXVA.average`

:func:`geosoft.gxapi.GXVA.col`

:func:`geosoft.gxapi.GXVA.copy2`

:func:`geosoft.gxapi.GXVA.copy`

:func:`geosoft.gxapi.GXVA.create_ext`

:func:`geosoft.gxapi.GXVA.create`

:func:`geosoft.gxapi.GXVA.get_double`

:func:`geosoft.gxapi.GXVA.get_fid_incr`

:func:`geosoft.gxapi.GXVA.get_fid_start`

:func:`geosoft.gxapi.GXVA.get_full_vv`

:func:`geosoft.gxapi.GXVA.get_int`

:func:`geosoft.gxapi.GXVA.get_string`

:func:`geosoft.gxapi.GXVA.get_vv`

:func:`geosoft.gxapi.GXVA.len`

:func:`geosoft.gxapi.GXVA.range_double`

:func:`geosoft.gxapi.GXVA.re_fid`

:func:`geosoft.gxapi.GXVA.set_double`

:func:`geosoft.gxapi.GXVA.set_fid_incr`

:func:`geosoft.gxapi.GXVA.set_fid_start`

:func:`geosoft.gxapi.GXVA.set_int`

:func:`geosoft.gxapi.GXVA.set_ln`

:func:`geosoft.gxapi.GXVA.set_string`

:func:`geosoft.gxapi.GXVA.set_vv`

:func:`geosoft.gxapi.GXVA.window2`

:func:`geosoft.gxapi.GXVA.window`

:func:`geosoft.gxapi.GXVAU.cond_depth_tem`

:func:`geosoft.gxapi.GXVAU.prune`

:func:`geosoft.gxapi.GXVAU.section_cond_tem`

:func:`geosoft.gxapi.GXVAU.total_vector`

:func:`geosoft.gxapi.GXVM.create`

:func:`geosoft.gxapi.GXVM.get_double`

:func:`geosoft.gxapi.GXVM.get_int`

:func:`geosoft.gxapi.GXVM.get_string`

:func:`geosoft.gxapi.GXVM.length`

:func:`geosoft.gxapi.GXVM.re_size`

:func:`geosoft.gxapi.GXVM.set_double`

:func:`geosoft.gxapi.GXVM.set_int`

:func:`geosoft.gxapi.GXVM.set_string`

:func:`geosoft.gxapi.GXVV.append`

:func:`geosoft.gxapi.GXVV.copy2`

:func:`geosoft.gxapi.GXVV.copy`

:func:`geosoft.gxapi.GXVV.crc_inexact`

:func:`geosoft.gxapi.GXVV.crc`

:func:`geosoft.gxapi.GXVV.create_ext`

:func:`geosoft.gxapi.GXVV.create_s`

:func:`geosoft.gxapi.GXVV.create`

:func:`geosoft.gxapi.GXVV.diff`

:func:`geosoft.gxapi.GXVV.fid_norm`

:func:`geosoft.gxapi.GXVV.fill_double`

:func:`geosoft.gxapi.GXVV.fill_int`

:func:`geosoft.gxapi.GXVV.fill_string`

:func:`geosoft.gxapi.GXVV.find_dum`

:func:`geosoft.gxapi.GXVV.get_double`

:func:`geosoft.gxapi.GXVV.get_fid_incr`

:func:`geosoft.gxapi.GXVV.get_fid_start`

:func:`geosoft.gxapi.GXVV.get_int`

:func:`geosoft.gxapi.GXVV.get_string`

:func:`geosoft.gxapi.GXVV.index_order`

:func:`geosoft.gxapi.GXVV.length`

:func:`geosoft.gxapi.GXVV.log_linear`

:func:`geosoft.gxapi.GXVV.log`

:func:`geosoft.gxapi.GXVV.lookup_index`

:func:`geosoft.gxapi.GXVV.mask_str`

:func:`geosoft.gxapi.GXVV.mask`

:func:`geosoft.gxapi.GXVV.project_3d`

:func:`geosoft.gxapi.GXVV.project`

:func:`geosoft.gxapi.GXVV.range_double`

:func:`geosoft.gxapi.GXVV.re_fid_vv`

:func:`geosoft.gxapi.GXVV.re_fid`

:func:`geosoft.gxapi.GXVV.serial`

:func:`geosoft.gxapi.GXVV.set_double_n`

:func:`geosoft.gxapi.GXVV.set_double`

:func:`geosoft.gxapi.GXVV.set_fid_incr`

:func:`geosoft.gxapi.GXVV.set_fid_start`

:func:`geosoft.gxapi.GXVV.set_int_n`

:func:`geosoft.gxapi.GXVV.set_int`

:func:`geosoft.gxapi.GXVV.set_len`

:func:`geosoft.gxapi.GXVV.set_string_n`

:func:`geosoft.gxapi.GXVV.set_string`

:func:`geosoft.gxapi.GXVV.setup_index`

:func:`geosoft.gxapi.GXVV.sort_index`

:func:`geosoft.gxapi.GXVV.statistics`

:func:`geosoft.gxapi.GXVV.swap`

:func:`geosoft.gxapi.GXVV.trans`

:func:`geosoft.gxapi.GXVV.window`

:func:`geosoft.gxapi.GXVVU.average_repeat2`

:func:`geosoft.gxapi.GXVVU.average_repeat`

:func:`geosoft.gxapi.GXVVU.bp_filt`

:func:`geosoft.gxapi.GXVVU.clip`

:func:`geosoft.gxapi.GXVVU.cond_depth_tem`

:func:`geosoft.gxapi.GXVVU.deviation`

:func:`geosoft.gxapi.GXVVU.distance`

:func:`geosoft.gxapi.GXVVU.dummy_range`

:func:`geosoft.gxapi.GXVVU.dummy_repeat`

:func:`geosoft.gxapi.GXVVU.dup_stats`

:func:`geosoft.gxapi.GXVVU.filter`

:func:`geosoft.gxapi.GXVVU.find_dummy`

:func:`geosoft.gxapi.GXVVU.interp`

:func:`geosoft.gxapi.GXVVU.mask`

:func:`geosoft.gxapi.GXVVU.nl_filt`

:func:`geosoft.gxapi.GXVVU.noise_check`

:func:`geosoft.gxapi.GXVVU.pick_peak2`

:func:`geosoft.gxapi.GXVVU.pick_peak`

:func:`geosoft.gxapi.GXVVU.prune`

:func:`geosoft.gxapi.GXVVU.qc`

:func:`geosoft.gxapi.GXVVU.range_vector_mag`

:func:`geosoft.gxapi.GXVVU.regress`

:func:`geosoft.gxapi.GXVVU.rel_var_dup`

:func:`geosoft.gxapi.GXVVU.remove_dummy`

:func:`geosoft.gxapi.GXVVU.remove_dup`

:func:`geosoft.gxapi.GXVVU.remove_xy_dup`

:func:`geosoft.gxapi.GXVVU.search_replace_text`

:func:`geosoft.gxapi.GXVVU.search_replace`

:func:`geosoft.gxapi.GXVVU.spline`

:func:`geosoft.gxapi.GXVVU.translate`

:func:`geosoft.gxapi.GXWA.create_sbf`

:func:`geosoft.gxapi.GXWA.create`

:func:`geosoft.gxapi.GXWA.new_line`

:func:`geosoft.gxapi.GXWA.puts`


geosoft.gxpy module history
==============================

