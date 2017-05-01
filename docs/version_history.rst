geosoft.gxpy module history
==========================================

  
Version 9.2
-----------------

New Classes
^^^^^^^^^^^

:class:`geosoft.gxpy.agg.Aggregate_image`

:class:`geosoft.gxpy.coordinate_system.Coordinate_system`

:class:`geosoft.gxpy.coordinate_system.GXpj`

:class:`geosoft.gxpy.dataframe.Data_frame`

:class:`geosoft.gxpy.geometry.Geometry`

:class:`geosoft.gxpy.geometry.PPoint`

:class:`geosoft.gxpy.geometry.Point2`

:class:`geosoft.gxpy.geometry.Point`

:class:`geosoft.gxpy.group.Agg_group`

:class:`geosoft.gxpy.group.Color_symbols_group_3d`

:class:`geosoft.gxpy.group.Color_symbols_group`

:class:`geosoft.gxpy.group.Color`

:class:`geosoft.gxpy.group.Draw_3d`

:class:`geosoft.gxpy.group.Group`

:class:`geosoft.gxpy.group.Text_def`

:class:`geosoft.gxpy.map.Map`

:class:`geosoft.gxpy.view.View_3d`

:class:`geosoft.gxpy.view.View`

:exc:`geosoft.gxpy.agg.AGGException`

:exc:`geosoft.gxpy.coordinate_system.CSException`

:exc:`geosoft.gxpy.dataframe.DfException`

:exc:`geosoft.gxpy.group.GroupException`

:exc:`geosoft.gxpy.map.MapException`

:exc:`geosoft.gxpy.view.ViewException`

:exc:`geosoft.gxpy.viewer.ViewerException`


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxpy.agg.Aggregate_image.add_layer`

:func:`geosoft.gxpy.agg.Aggregate_image.layer_file_names`

:func:`geosoft.gxpy.coordinate_system.Coordinate_system.coordinate_dict`

:func:`geosoft.gxpy.coordinate_system.Coordinate_system.cs_name`

:func:`geosoft.gxpy.coordinate_system.Coordinate_system.oriented_from_xyz`

:func:`geosoft.gxpy.coordinate_system.Coordinate_system.xyz_from_oriented`

:func:`geosoft.gxpy.coordinate_system.GXpj.convert`

:func:`geosoft.gxpy.coordinate_system.name_from_hcs_orient_vcs`

:func:`geosoft.gxpy.coordinate_system.name_list`

:func:`geosoft.gxpy.coordinate_system.parameters`

:func:`geosoft.gxpy.dataframe.table_column`

:func:`geosoft.gxpy.dataframe.table_record`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.read_channel_va`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.read_channel_vv`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.read_line_vv`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.write_channel_va`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.write_channel_vv`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.write_line_vv`

:func:`geosoft.gxpy.geometry.PPoint.make_xyz_vv`

:func:`geosoft.gxpy.grid.Grid.copy`

:func:`geosoft.gxpy.grid.Grid.extent_2d`

:func:`geosoft.gxpy.grid.Grid.extent_3d`

:func:`geosoft.gxpy.grid.Grid.index_window`

:func:`geosoft.gxpy.grid.delete_files`

:func:`geosoft.gxpy.group.Agg_group.extent_map_cm`

:func:`geosoft.gxpy.group.Agg_group.locate`

:func:`geosoft.gxpy.group.Color.adjust_brightness`

:func:`geosoft.gxpy.group.Color_map.color_of_value`

:func:`geosoft.gxpy.group.Color_map.set_linear`

:func:`geosoft.gxpy.group.Color_map.set_logarithmic`

:func:`geosoft.gxpy.group.Color_map.set_normal`

:func:`geosoft.gxpy.group.Color_map.set_sequential`

:func:`geosoft.gxpy.group.Color_symbols_group.extent_map_cm`

:func:`geosoft.gxpy.group.Color_symbols_group.locate`

:func:`geosoft.gxpy.group.Color_symbols_group_3d.extent_map_cm`

:func:`geosoft.gxpy.group.Color_symbols_group_3d.locate`

:func:`geosoft.gxpy.group.Color_symbols_group_3d.new`

:func:`geosoft.gxpy.group.Draw.extent_map_cm`

:func:`geosoft.gxpy.group.Draw.graticule`

:func:`geosoft.gxpy.group.Draw.line`

:func:`geosoft.gxpy.group.Draw.locate`

:func:`geosoft.gxpy.group.Draw.new_pen`

:func:`geosoft.gxpy.group.Draw.polygon`

:func:`geosoft.gxpy.group.Draw.polyline`

:func:`geosoft.gxpy.group.Draw.rectangle`

:func:`geosoft.gxpy.group.Draw.text`

:func:`geosoft.gxpy.group.Draw_3d.box_3d`

:func:`geosoft.gxpy.group.Draw_3d.cone_3d`

:func:`geosoft.gxpy.group.Draw_3d.cylinder_3d`

:func:`geosoft.gxpy.group.Draw_3d.extent_map_cm`

:func:`geosoft.gxpy.group.Draw_3d.graticule`

:func:`geosoft.gxpy.group.Draw_3d.line`

:func:`geosoft.gxpy.group.Draw_3d.locate`

:func:`geosoft.gxpy.group.Draw_3d.new_pen`

:func:`geosoft.gxpy.group.Draw_3d.polygon`

:func:`geosoft.gxpy.group.Draw_3d.polyline_3d`

:func:`geosoft.gxpy.group.Draw_3d.polyline`

:func:`geosoft.gxpy.group.Draw_3d.polypoint_3d`

:func:`geosoft.gxpy.group.Draw_3d.rectangle`

:func:`geosoft.gxpy.group.Draw_3d.sphere`

:func:`geosoft.gxpy.group.Draw_3d.text`

:func:`geosoft.gxpy.group.Group.extent_map_cm`

:func:`geosoft.gxpy.group.Group.locate`

:func:`geosoft.gxpy.group.Pen.from_mapplot_string`

:func:`geosoft.gxpy.group.edge_reference`

:func:`geosoft.gxpy.group.font_weight_from_line_thickness`

:func:`geosoft.gxpy.group.legend_color_bar`

:func:`geosoft.gxpy.group.thickness_from_font_weight`

:func:`geosoft.gxpy.gx.GXpy.elapsed_seconds`

:func:`geosoft.gxpy.gx.GXpy.keep_temp_folder`

:func:`geosoft.gxpy.gx.GXpy.log`

:func:`geosoft.gxpy.gx.GXpy.temp_file`

:func:`geosoft.gxpy.gx.GXpy.temp_folder`

:func:`geosoft.gxpy.map.Map.annotate_data_ll`

:func:`geosoft.gxpy.map.Map.annotate_data_xy`

:func:`geosoft.gxpy.map.Map.create_linked_3d_view`

:func:`geosoft.gxpy.map.Map.delete_view`

:func:`geosoft.gxpy.map.Map.extent_data_views`

:func:`geosoft.gxpy.map.Map.get_class_name`

:func:`geosoft.gxpy.map.Map.map_reference_location`

:func:`geosoft.gxpy.map.Map.new`

:func:`geosoft.gxpy.map.Map.north_arrow`

:func:`geosoft.gxpy.map.Map.open`

:func:`geosoft.gxpy.map.Map.scale_bar`

:func:`geosoft.gxpy.map.Map.set_class_name`

:func:`geosoft.gxpy.map.Map.surround`

:func:`geosoft.gxpy.map._Mapplot.start_group`

:func:`geosoft.gxpy.map.crc_map`

:func:`geosoft.gxpy.map.delete_files`

:func:`geosoft.gxpy.map.map_file_name`

:func:`geosoft.gxpy.map.save_as_image`

:func:`geosoft.gxpy.map.unique_temporary_file_name`

:func:`geosoft.gxpy.project.dummy_none`

:func:`geosoft.gxpy.project.pause`

:func:`geosoft.gxpy.project.user_message`

:func:`geosoft.gxpy.utility.crc32_file`

:func:`geosoft.gxpy.utility.crc32_str`

:func:`geosoft.gxpy.utility.crc32`

:func:`geosoft.gxpy.utility.datetime_from_year`

:func:`geosoft.gxpy.utility.dummy_mask`

:func:`geosoft.gxpy.utility.dummy_none`

:func:`geosoft.gxpy.utility.gx_dummy`

:func:`geosoft.gxpy.utility.normalize_file_name`

:func:`geosoft.gxpy.utility.uuid`

:func:`geosoft.gxpy.utility.year_from_datetime`

:func:`geosoft.gxpy.view.View.close`

:func:`geosoft.gxpy.view.View.delete_group`

:func:`geosoft.gxpy.view.View.extent_map_cm`

:func:`geosoft.gxpy.view.View.get_class_name`

:func:`geosoft.gxpy.view.View.locate`

:func:`geosoft.gxpy.view.View.map_cm_to_view`

:func:`geosoft.gxpy.view.View.set_class_name`

:func:`geosoft.gxpy.view.View.view_to_map_cm`

:func:`geosoft.gxpy.view.View_3d.delete_group`

:func:`geosoft.gxpy.view.View_3d.extent_map_cm`

:func:`geosoft.gxpy.view.View_3d.get_class_name`

:func:`geosoft.gxpy.view.View_3d.locate`

:func:`geosoft.gxpy.view.View_3d.map_cm_to_view`

:func:`geosoft.gxpy.view.View_3d.new`

:func:`geosoft.gxpy.view.View_3d.open`

:func:`geosoft.gxpy.view.View_3d.set_class_name`

:func:`geosoft.gxpy.view.View_3d.view_to_map_cm`

:func:`geosoft.gxpy.viewer.view_document`


  
Version 9.1
-----------------

New Classes
^^^^^^^^^^^

:class:`geosoft.gxpy.gdb.Geosoft_gdb`

:class:`geosoft.gxpy.grid.Grid`

:class:`geosoft.gxpy.gx.GXpy`

:class:`geosoft.gxpy.va.GXva`

:class:`geosoft.gxpy.vv.GXvv`

:exc:`geosoft.gxpy.gdb.GDBException`

:exc:`geosoft.gxpy.grid.GridException`

:exc:`geosoft.gxpy.gx.GXException`

:exc:`geosoft.gxpy.project.ProjectException`

:exc:`geosoft.gxpy.system.GXSysException`

:exc:`geosoft.gxpy.utility.UtilityException`

:exc:`geosoft.gxpy.va.VAException`

:exc:`geosoft.gxpy.vv.VVException`


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxpy.coordinate_system.hcs_orient_vcs_from_name`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.channel_details`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.channel_dtype`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.channel_name_symb`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.channel_width`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.commit`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.delete_channel`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.delete_line`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.discard`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.file_name`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.line_details`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.line_name_symb`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.list_channels`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.list_lines`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.list_values`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.new_channel`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.new_line`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.new`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.open`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.read_channel`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.read_line`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.select_lines`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.set_channel_details`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.write_channel`

:func:`geosoft.gxpy.gdb.Geosoft_gdb.write_line`

:func:`geosoft.gxpy.grid.Grid.delete_files`

:func:`geosoft.gxpy.grid.Grid.from_data_array`

:func:`geosoft.gxpy.grid.Grid.new`

:func:`geosoft.gxpy.grid.Grid.open`

:func:`geosoft.gxpy.grid.Grid.properties`

:func:`geosoft.gxpy.grid.Grid.read_column`

:func:`geosoft.gxpy.grid.Grid.read_row`

:func:`geosoft.gxpy.grid.Grid.set_properties`

:func:`geosoft.gxpy.grid.Grid.write_rows`

:func:`geosoft.gxpy.grid.array_locations`

:func:`geosoft.gxpy.grid.decorate_name`

:func:`geosoft.gxpy.grid.grid_bool`

:func:`geosoft.gxpy.grid.grid_mosaic`

:func:`geosoft.gxpy.grid.name_parts`

:func:`geosoft.gxpy.gx.GXpy.active_wind_id`

:func:`geosoft.gxpy.gx.GXpy.disable_app`

:func:`geosoft.gxpy.gx.GXpy.enable_app`

:func:`geosoft.gxpy.gx.GXpy.entitlements`

:func:`geosoft.gxpy.gx.GXpy.license_class`

:func:`geosoft.gxpy.gx.GXpy.main_wind_id`

:func:`geosoft.gxpy.project.dict_from_lst`

:func:`geosoft.gxpy.project.get_user_input`

:func:`geosoft.gxpy.project.running_script`

:func:`geosoft.gxpy.system.app_name`

:func:`geosoft.gxpy.system.func_name`

:func:`geosoft.gxpy.system.parallel_map`

:func:`geosoft.gxpy.system.remove_dir`

:func:`geosoft.gxpy.system.unzip`

:func:`geosoft.gxpy.system.wait_on_file`

:func:`geosoft.gxpy.utility.check_version`

:func:`geosoft.gxpy.utility.decode`

:func:`geosoft.gxpy.utility.dict_from_lst`

:func:`geosoft.gxpy.utility.dict_from_reg`

:func:`geosoft.gxpy.utility.display_message`

:func:`geosoft.gxpy.utility.dtype_gx`

:func:`geosoft.gxpy.utility.folder_temp`

:func:`geosoft.gxpy.utility.folder_user`

:func:`geosoft.gxpy.utility.folder_workspace`

:func:`geosoft.gxpy.utility.get_parameters`

:func:`geosoft.gxpy.utility.get_shared_dict`

:func:`geosoft.gxpy.utility.gx_dtype`

:func:`geosoft.gxpy.utility.rdecode_err`

:func:`geosoft.gxpy.utility.rdecode`

:func:`geosoft.gxpy.utility.run_external_python`

:func:`geosoft.gxpy.utility.save_parameters`

:func:`geosoft.gxpy.utility.set_shared_dict`

:func:`geosoft.gxpy.utility.yearFromJulianDay2`

:func:`geosoft.gxpy.va.GXva.get_data`

:func:`geosoft.gxpy.va.GXva.refid`

:func:`geosoft.gxpy.va.GXva.set_data`

:func:`geosoft.gxpy.vv.GXvv.get_data`

:func:`geosoft.gxpy.vv.GXvv.refid`

:func:`geosoft.gxpy.vv.GXvv.set_data`


geosoft.gxapi module history
==========================================

  
Version 9.2.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GX3DV.from_map`

:func:`geosoft.gxapi.GXEDB.get_cur_point`

:func:`geosoft.gxapi.GXEMAP.packed_files`

:func:`geosoft.gxapi.GXIP.export_data_to_ubc_3d`

:func:`geosoft.gxapi.GXIP.get_electrode_locations_and_mask_values2`

:func:`geosoft.gxapi.GXIP.get_qc_channel`

:func:`geosoft.gxapi.GXIP.set_electrode_mask_values_single_qc_channel`

:func:`geosoft.gxapi.GXIPJ.set_vcs`

:func:`geosoft.gxapi.GXMAP.create_linked_3d_view`

:func:`geosoft.gxapi.GXMVIEW.get_3d_point_of_view`

:func:`geosoft.gxapi.GXMVIEW.get_aggregate`

:func:`geosoft.gxapi.GXMVIEW.get_col_symbol`

:func:`geosoft.gxapi.GXMVIEW.get_datalinkd`

:func:`geosoft.gxapi.GXMVIEW.set_3d_point_of_view`

:func:`geosoft.gxapi.GXPROJ.current_document_of_type`

:func:`geosoft.gxapi.GXPROJ.current_document`

:func:`geosoft.gxapi.GXPROJ.list_loaded_documents`

:func:`geosoft.gxapi.GXSYS.log_script_run`

:func:`geosoft.gxapi.GXTEST.core_class`


  
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


