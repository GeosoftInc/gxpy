geosoft.gxpy module history
==========================================

  
Version 9.2
-----------------

New Classes
^^^^^^^^^^^

:class:`geosoft.gxpy.coordinate_system.GXcs`

:class:`geosoft.gxpy.coordinate_system.GXpj`

:class:`geosoft.gxpy.geometry.Geometry`

:class:`geosoft.gxpy.geometry.PPoint`

:class:`geosoft.gxpy.geometry.Point2`

:class:`geosoft.gxpy.geometry.Point`

:class:`geosoft.gxpy.map.GXmap`

:class:`geosoft.gxpy.view.GXview`

:exc:`geosoft.gxpy.coordinate_system.CSException`

:exc:`geosoft.gxpy.map.MapException`

:exc:`geosoft.gxpy.view.ViewException`


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxpy.coordinate_system.GXcs.gxf`

:func:`geosoft.gxpy.coordinate_system.GXcs.name`

:func:`geosoft.gxpy.coordinate_system.GXcs.units`

:func:`geosoft.gxpy.coordinate_system.GXpj.convert`

:func:`geosoft.gxpy.coordinate_system.name_from_hcs_orient_vcs`

:func:`geosoft.gxpy.coordinate_system.name_list`

:func:`geosoft.gxpy.coordinate_system.parameters`

:func:`geosoft.gxpy.gdb.GXdb.read_channel_va`

:func:`geosoft.gxpy.gdb.GXdb.read_channel_vv`

:func:`geosoft.gxpy.gdb.GXdb.read_line_vv`

:func:`geosoft.gxpy.gdb.GXdb.write_channel_va`

:func:`geosoft.gxpy.gdb.GXdb.write_channel_vv`

:func:`geosoft.gxpy.gdb.GXdb.write_line_vv`

:func:`geosoft.gxpy.grd.delete_files`

:func:`geosoft.gxpy.gx.GXpy.elapsed_seconds`

:func:`geosoft.gxpy.gx.GXpy.keep_temp_folder`

:func:`geosoft.gxpy.gx.GXpy.log`

:func:`geosoft.gxpy.gx.GXpy.temp_file`

:func:`geosoft.gxpy.gx.GXpy.temp_folder`

:func:`geosoft.gxpy.ipj.GXipj.from_any`

:func:`geosoft.gxpy.map.GXmap.new_standard_geosoft`

:func:`geosoft.gxpy.map.GXmap.new`

:func:`geosoft.gxpy.map.GXmap.open`

:func:`geosoft.gxpy.map.crc_map`

:func:`geosoft.gxpy.map.delete_files`

:func:`geosoft.gxpy.map.map_file_name`

:func:`geosoft.gxpy.map.save_as_image`

:func:`geosoft.gxpy.utility.crc32_file`

:func:`geosoft.gxpy.utility.crc32_str`

:func:`geosoft.gxpy.utility.crc32`

:func:`geosoft.gxpy.utility.datetime_from_year`

:func:`geosoft.gxpy.utility.uuid`

:func:`geosoft.gxpy.utility.year_from_datetime`

:func:`geosoft.gxpy.view.GXview.box_3d`

:func:`geosoft.gxpy.view.GXview.locate`

:func:`geosoft.gxpy.view.GXview.start_group`

:func:`geosoft.gxpy.view.GXview.xy_line`

:func:`geosoft.gxpy.view.GXview.xy_poly_line`

:func:`geosoft.gxpy.view.GXview.xy_rectangle`

:func:`geosoft.gxpy.view.GXview3d.box_3d`

:func:`geosoft.gxpy.view.GXview3d.locate`

:func:`geosoft.gxpy.view.GXview3d.start_group`

:func:`geosoft.gxpy.view.GXview3d.xy_line`

:func:`geosoft.gxpy.view.GXview3d.xy_poly_line`

:func:`geosoft.gxpy.view.GXview3d.xy_rectangle`


  
Version 9.1
-----------------

New Classes
^^^^^^^^^^^

:class:`geosoft.gxpy.gdb.GXdb`

:class:`geosoft.gxpy.grd.GXgrd`

:class:`geosoft.gxpy.gx.GXpy`

:class:`geosoft.gxpy.ipj.GXipj`

:class:`geosoft.gxpy.ipj.GXpj`

:class:`geosoft.gxpy.vv.GXvv`

:exc:`geosoft.gxpy.gdb.GDBException`

:exc:`geosoft.gxpy.grd.GRDException`

:exc:`geosoft.gxpy.gx.GXException`

:exc:`geosoft.gxpy.ipj.IPJException`

:exc:`geosoft.gxpy.om.OMException`

:exc:`geosoft.gxpy.system.GXSysException`

:exc:`geosoft.gxpy.utility.UtilityException`

:exc:`geosoft.gxpy.vv.VVException`


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxpy.coordinate_system.hcs_orient_vcs_from_name`

:func:`geosoft.gxpy.gdb.GXdb.channel_details`

:func:`geosoft.gxpy.gdb.GXdb.channel_dtype`

:func:`geosoft.gxpy.gdb.GXdb.channel_name_symb`

:func:`geosoft.gxpy.gdb.GXdb.channel_width`

:func:`geosoft.gxpy.gdb.GXdb.commit`

:func:`geosoft.gxpy.gdb.GXdb.delete_channel`

:func:`geosoft.gxpy.gdb.GXdb.delete_line`

:func:`geosoft.gxpy.gdb.GXdb.discard`

:func:`geosoft.gxpy.gdb.GXdb.file_name`

:func:`geosoft.gxpy.gdb.GXdb.line_details`

:func:`geosoft.gxpy.gdb.GXdb.line_name_symb`

:func:`geosoft.gxpy.gdb.GXdb.list_channels`

:func:`geosoft.gxpy.gdb.GXdb.list_lines`

:func:`geosoft.gxpy.gdb.GXdb.list_values`

:func:`geosoft.gxpy.gdb.GXdb.new_channel`

:func:`geosoft.gxpy.gdb.GXdb.new_line`

:func:`geosoft.gxpy.gdb.GXdb.new`

:func:`geosoft.gxpy.gdb.GXdb.open`

:func:`geosoft.gxpy.gdb.GXdb.read_channel`

:func:`geosoft.gxpy.gdb.GXdb.read_line`

:func:`geosoft.gxpy.gdb.GXdb.select_lines`

:func:`geosoft.gxpy.gdb.GXdb.set_channel_details`

:func:`geosoft.gxpy.gdb.GXdb.write_channel`

:func:`geosoft.gxpy.gdb.GXdb.write_line`

:func:`geosoft.gxpy.grd.GXgrd.delete_files`

:func:`geosoft.gxpy.grd.GXgrd.dtype`

:func:`geosoft.gxpy.grd.GXgrd.from_data_array`

:func:`geosoft.gxpy.grd.GXgrd.indexWindow`

:func:`geosoft.gxpy.grd.GXgrd.new`

:func:`geosoft.gxpy.grd.GXgrd.open`

:func:`geosoft.gxpy.grd.GXgrd.properties`

:func:`geosoft.gxpy.grd.GXgrd.read_rows`

:func:`geosoft.gxpy.grd.GXgrd.save_as`

:func:`geosoft.gxpy.grd.GXgrd.set_properties`

:func:`geosoft.gxpy.grd.GXgrd.write_rows`

:func:`geosoft.gxpy.grd.array_locations`

:func:`geosoft.gxpy.grd.decorate_name`

:func:`geosoft.gxpy.grd.gridBool`

:func:`geosoft.gxpy.grd.gridMosaic`

:func:`geosoft.gxpy.grd.name_parts`

:func:`geosoft.gxpy.gx.GXpy.active_wind_id`

:func:`geosoft.gxpy.gx.GXpy.disable_app`

:func:`geosoft.gxpy.gx.GXpy.enable_app`

:func:`geosoft.gxpy.gx.GXpy.entitlements`

:func:`geosoft.gxpy.gx.GXpy.environment`

:func:`geosoft.gxpy.gx.GXpy.license_class`

:func:`geosoft.gxpy.gx.GXpy.main_wind_id`

:func:`geosoft.gxpy.ipj.GXipj.compare`

:func:`geosoft.gxpy.ipj.GXipj.dict`

:func:`geosoft.gxpy.ipj.GXipj.from_dict`

:func:`geosoft.gxpy.ipj.GXipj.from_esri`

:func:`geosoft.gxpy.ipj.GXipj.from_gxf`

:func:`geosoft.gxpy.ipj.GXipj.from_json`

:func:`geosoft.gxpy.ipj.GXipj.from_name`

:func:`geosoft.gxpy.ipj.GXipj.name`

:func:`geosoft.gxpy.ipj.GXipj.names`

:func:`geosoft.gxpy.ipj.GXipj.to_gxf`

:func:`geosoft.gxpy.ipj.GXipj.to_json`

:func:`geosoft.gxpy.ipj.GXipj.units`

:func:`geosoft.gxpy.ipj.GXpj.convert`

:func:`geosoft.gxpy.om.dict_from_lst`

:func:`geosoft.gxpy.om.get_user_input`

:func:`geosoft.gxpy.om.menus`

:func:`geosoft.gxpy.om.pause`

:func:`geosoft.gxpy.om.running_script`

:func:`geosoft.gxpy.om.state`

:func:`geosoft.gxpy.om.user_message`

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

:func:`geosoft.gxpy.utility.dummy_mask`

:func:`geosoft.gxpy.utility.folder_temp`

:func:`geosoft.gxpy.utility.folder_user`

:func:`geosoft.gxpy.utility.folder_workspace`

:func:`geosoft.gxpy.utility.get_parameters`

:func:`geosoft.gxpy.utility.get_shared_dict`

:func:`geosoft.gxpy.utility.gx_dtype`

:func:`geosoft.gxpy.utility.gx_dummy`

:func:`geosoft.gxpy.utility.rdecode_err`

:func:`geosoft.gxpy.utility.rdecode`

:func:`geosoft.gxpy.utility.run_external_python`

:func:`geosoft.gxpy.utility.save_parameters`

:func:`geosoft.gxpy.utility.set_shared_dict`

:func:`geosoft.gxpy.utility.yearFromJulianDay2`

:func:`geosoft.gxpy.vv.GXvv.dtype`

:func:`geosoft.gxpy.vv.GXvv.fid`

:func:`geosoft.gxpy.vv.GXvv.gxtype`

:func:`geosoft.gxpy.vv.GXvv.length`

:func:`geosoft.gxpy.vv.GXvv.np`

:func:`geosoft.gxpy.vv.GXvv.reFid`

:func:`geosoft.gxpy.vv.GXvv.setFid`

:func:`geosoft.gxpy.vv.GXvv.vv_np`

:func:`geosoft.gxpy.vv.GXvv.vv`


geosoft.gxapi module history
==========================================

  
Version 9.2.0
-----------------

New Classes
^^^^^^^^^^^


New Functions
^^^^^^^^^^^^^

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


