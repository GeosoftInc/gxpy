geosoft.gxpy module history
==========================================

  
Version 9.9
-----------------

New Classes
^^^^^^^^^^^

:class:`geosoft.gxpy.view.PlaneReliefSurfaceInfo` Information about a relief surface assigned to a plane. The following properties are represented:


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxpy.map.Map.from_gxapi` Instantiate Map from gxapi instance.

:func:`geosoft.gxpy.view.View.from_gxapi` Instantiate View from gxapi instance.

:func:`geosoft.gxpy.view.View_3d.from_gxapi` Instantiate View_3d from gxapi instance.


  
Version 9.6
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxpy.gdb.Geosoft_gdb.delete_line_data` Delete all data in line(s) by name or symbol but keep the line.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.sorted_chan_list` Get a list of sorted channels from Gdb, placing x, y and z channels (if defined) at front of list.

:func:`geosoft.gxpy.gdb.Line.delete_data` Delete all data in a line but keep the line

:func:`geosoft.gxpy.gx.GXpyContext.run_gx` Runs a GX.


  
Version 9.5
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxpy.gdb.Geosoft_gdb.read_line_dataframe` Read a line of data into a Pandas DataFrame


  
Version 9.4
-----------------

New Classes
^^^^^^^^^^^

:class:`geosoft.gxpy.dap_client.DapClient` DapClient class to communicate with a Geosoft DAP server.

:class:`geosoft.gxpy.dap_client.DataCard` Single dataset information instance.

:class:`geosoft.gxpy.dap_client.DataExtract` Data extraction instance.

:class:`geosoft.gxpy.dap_client.ResultFilter` Results filter instance.

:class:`geosoft.gxpy.dap_client.SearchFilter` Search filter instance.

:class:`geosoft.gxpy.dap_client.SearchParameters` Search parameter instance, defined by a `SearchFilter` and a `ResultFilter`

:class:`geosoft.gxpy.grid_fft.GridFFT` Descrete Fourier Transform of a grid.

:class:`geosoft.gxpy.view.CrookedPath` Description of a crooked (x, y) path that defines a crooked-section view, or a crooked-section grid.

:exc:`geosoft.gxpy.geometry_utility.GeometryUtilityException` Exceptions from `geosoft.gxpy.geometry_utility`.

:exc:`geosoft.gxpy.grid_utility.GridUtilityException` Exceptions from `geosoft.gxpy.grid_utility`.


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxpy.dap_client.DapClient.catalog` Return a filtered catalog list.

:func:`geosoft.gxpy.dap_client.DapClient.datacard_from_id` Return the `DataCard` instance based on the dataset ID #

:func:`geosoft.gxpy.dap_client.DapClient.fetch_data` Fetch data from the server.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.close` Close the database and free resources

:func:`geosoft.gxpy.gdb.Geosoft_gdb.scan_line_fid` Scan channels in a line and return the smallest common fid, line length, data width, list of channels

:func:`geosoft.gxpy.geometry.PPoint.merge` Create a `PPoint` from a list of `Point`, 'Point2` or `PPoint` instances or point arrays.

:func:`geosoft.gxpy.geometry_utility.resample` Return points resampled at a constant separation along the trace of points.

:func:`geosoft.gxpy.grid.Grid.extent_point_2d` Return the 2D extent of the grid point (cell centers) on the grid plane.

:func:`geosoft.gxpy.grid.Grid.generate_color_map` Generate color map for grid based on statistics and method

:func:`geosoft.gxpy.grid.Grid.get_default_color_map` Get default color map for grid

:func:`geosoft.gxpy.grid.Grid.mask` Mask against blank areas in `mask` grid.  Both grids must be same dimension.

:func:`geosoft.gxpy.grid.Grid.minimum_curvature` Create a minimum-curvature surface grid from (x, y, value) located data.

:func:`geosoft.gxpy.grid.Grid.statistics` Calculate and return current grid data statistics as a dictionary.

:func:`geosoft.gxpy.grid.Grid.write_column` :param data:    data to write, `geosoft.gxpy.vv.GXvv` instance or an array

:func:`geosoft.gxpy.grid.Grid.write_row` :param data:    data to write, `geosoft.gxpy.vv.GXvv` instance or an array

:func:`geosoft.gxpy.grid.Grid.xy_from_index` Return the rotated location of grid index ix, iy

:func:`geosoft.gxpy.grid.reopen` Reopen a grid to access the grid as an existing grid.

:func:`geosoft.gxpy.grid_fft.GridFFT.filter` Apply a pre-defined filter.

:func:`geosoft.gxpy.grid_fft.GridFFT.log_average_spectral_density` Log of the average spectral density of the transform.

:func:`geosoft.gxpy.grid_fft.GridFFT.radially_averaged_spectrum` Radially averaged spectrum as a Numpy array shaped (n_wavenumbers, 5).

:func:`geosoft.gxpy.grid_fft.GridFFT.read_uv_row` Read a row (constant wavenumber v) from (u, v) transform.

:func:`geosoft.gxpy.grid_fft.GridFFT.result_grid` Produce a filter result grid.

:func:`geosoft.gxpy.grid_fft.GridFFT.spectrum_grid` Return the 2D log(power) amplitude as a grid in wavenumber domain (u, v).

:func:`geosoft.gxpy.grid_fft.GridFFT.tr_row_from_uv` Returns transform row index from (u, v) space row index.

:func:`geosoft.gxpy.grid_fft.GridFFT.uv_row_from_tr` Returns (u, v) space row index of a transform row.

:func:`geosoft.gxpy.grid_fft.GridFFT.write_uv_row` Write a row (constant wavenumber v) to the (u, v) transform.

:func:`geosoft.gxpy.grid_utility.calculate_slope_standard_deviation` Return the standard deviation of the slopes.

:func:`geosoft.gxpy.grid_utility.contour_points` Return a set of point segments that represent the spatial locations of contours threaded through the grid.

:func:`geosoft.gxpy.grid_utility.feather` Feather the edge of a grid to a constant value at the edge.

:func:`geosoft.gxpy.grid_utility.flood` Flood blank areas in a grid based on a minimum-curvature surface.

:func:`geosoft.gxpy.grid_utility.grid_bool` Combine two grids into a single grid, with boolean logic to determine the result.

:func:`geosoft.gxpy.grid_utility.grid_mosaic` Combine a set of grids into a single grid.  Raises an error if the resulting grid is too large.

:func:`geosoft.gxpy.grid_utility.tilt_depth` Return estimate of the depth sources of potential filed anomalies.

:func:`geosoft.gxpy.group.Draw.text_extent` Return the extent of a text string in view units relative to the current

:func:`geosoft.gxpy.utility.delete_files_by_root` Delete all files that have the same file_root (without extension). This can be safely applied to remove

:func:`geosoft.gxpy.utility.dict_from_http_response_text` Decode http response text to a dictionary. Response may be json or xml.

:func:`geosoft.gxpy.utility.geosoft_xml_from_dict` Return a unicode XML string of a dictionary with geosoft namespace defined.

:func:`geosoft.gxpy.view.CrookedPath.set_in_geosoft_ipj` Set the crooked-path in the `geosoft.gxapi.GXIPJ` instance of the coordinate system.


  
Version 9.3.2
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxpy.gx.GXpyContext.remove_stale_temporary_files` Removes stale temporary files from the current instance temporary file folder.


  
Version 9.3.1
-----------------

New Classes
^^^^^^^^^^^

:class:`geosoft.gxpy.geometry.Mesh` Mesh - set of triangular faces, which are indexes into verticies.

:class:`geosoft.gxpy.group.VoxDisplayGroup` Vox display group in a view.  Use class methods `new()` and `open()`

:class:`geosoft.gxpy.spatialdata.SpatialData` Base class for spatial datasets.

:class:`geosoft.gxpy.surface.SurfaceDataset` Surface dataset, which contains one or more `Surface` instances.

:class:`geosoft.gxpy.surface.Surface` A single surface, which contains one or more `geosoft.gxpy.geometry.Mesh` instances.

:class:`geosoft.gxpy.vox.Vox` Vox (voxset) class.

:class:`geosoft.gxpy.vox_display.VoxDisplay` Creation and handling of vox displays. Vox displays can be placed into a 3D view for display.


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxpy.agg.Aggregate_image.image_file` Save the aggregate as a georeferenced image file.

:func:`geosoft.gxpy.coordinate_system.Coordinate_system.local` Create an ad-hoc local coordinate system.

:func:`geosoft.gxpy.coordinate_system.Coordinate_translate.convert_vv` Project vv locations in-place.

:func:`geosoft.gxpy.coordinate_system.is_known` Return True if this is a known coordinate system

:func:`geosoft.gxpy.gdb.Geosoft_gdb.clear_extent` Clear the extent cache.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.update_gxmeta` Update the database Geosoft metadata as a Geosoft `geosoft.gxpy.metadata.Metadata` instance.

:func:`geosoft.gxpy.geometry.Mesh.point_array` Return numpy array of face corner locations.

:func:`geosoft.gxpy.geometry.extent_union` Return the spatial union of two spatial objects.

:func:`geosoft.gxpy.geometry.first_coordinate_system` Return the first found known coordinate system in the list

:func:`geosoft.gxpy.grid.Grid.image_file` Save as a georeferenced image file.

:func:`geosoft.gxpy.grid.Grid.np` Return a numpy array of grid values in the working dtype.

:func:`geosoft.gxpy.grid.image_file` Save a grid file grid as a georeferenced image file.

:func:`geosoft.gxpy.group.VoxDisplayGroup.new` Add a VoxDisplay as a new group in the view

:func:`geosoft.gxpy.group.face_normals_np` Return normals of the verticies based on tringular faces, assuming right-hand

:func:`geosoft.gxpy.group.surface_group_from_file` Create a 3D surface group from a surface dataset file.

:func:`geosoft.gxpy.group.vertex_normals_np` Return normals of the verticies based on tringular faces, assuming right-hand

:func:`geosoft.gxpy.group.vertex_normals_vv` Return normals of the verticies based on tringular faces, assuming right-hand

:func:`geosoft.gxpy.metadata.Metadata.update_dict` Update the metadata from the content of a dictionary.

:func:`geosoft.gxpy.metadata.get_node_from_meta_dict` Get the node content from a metadata dictionary.

:func:`geosoft.gxpy.metadata.set_node_in_meta_dict` Set a node in a metadata dictionary. Tree nodes are added if absent.

:func:`geosoft.gxpy.spatialdata.delete_files` Delete file and xml file

:func:`geosoft.gxpy.spatialdata.extent_from_metadata_file` Return spatial dataset extent from file metadata .xml file

:func:`geosoft.gxpy.spatialdata.extent_from_metadata` Return spatial dataset extent from geosoft metadata.

:func:`geosoft.gxpy.spatialdata.find_meta_branch` Return the lowest branch in the meta dictionary that contains the item.

:func:`geosoft.gxpy.surface.Surface.computed_properties` Surface properties, see: `geosoft.gxapi.GXSURFACEITEM.compute_extended_info`.

:func:`geosoft.gxpy.surface.Surface.mesh` Returns a component mesh as `geosoft.gxpy.geometry.Mesh` instance

:func:`geosoft.gxpy.surface.Surface.properties` Surface properties from `geosoft.gxapi.GXSURFACEITEM.get_properties_ex`.

:func:`geosoft.gxpy.surface.SurfaceDataset.add_surface_dataset` Add the surfaces from an existing surface dataset.

:func:`geosoft.gxpy.surface.SurfaceDataset.add_surface` Add a surface to the surface dataset.  One can only add surfaces to new datasets.

:func:`geosoft.gxpy.surface.SurfaceDataset.new` Create a new surface dataset.

:func:`geosoft.gxpy.surface.SurfaceDataset.open` Open an existing surface dataset.

:func:`geosoft.gxpy.surface.SurfaceDataset.surface_guid` Return the guid of a surface based on the name.

:func:`geosoft.gxpy.surface.SurfaceDataset.vox_surface` Add voxel isosurfaces to a surface dataset.

:func:`geosoft.gxpy.surface.delete_files` Delete all files associated with this surface dataset.

:func:`geosoft.gxpy.surface.render` Render a surface, surface dataset or surface dataset file in a 3D view.

:func:`geosoft.gxpy.utility.delete_file` Delete a file, does nothing if file does not exist.

:func:`geosoft.gxpy.utility.delete_folder` Delete a folder if all files and sub-folders are accessible and deletable.

:func:`geosoft.gxpy.utility.dtype_gx_dimension` :returns:   numpy dtype and dimension of the type, 1, 2 or 3. The dimension indicates 1D, 2D or 3D data.

:func:`geosoft.gxpy.utility.file_age` Returns the age of a file in seconds from now. -1 if the file does not exist.

:func:`geosoft.gxpy.utility.gx_dtype_dimension` :returns:   GX type for a numpy dtype, with dimensions 2 and 3

:func:`geosoft.gxpy.utility.is_file_locked` Returns True if the file exists and is currently locked by another process or is younger than age.

:func:`geosoft.gxpy.utility.is_path_locked` Returns True if any files in this folder or sub-folders are locked or younger than age.

:func:`geosoft.gxpy.utility.jupyter_markdown_toc` Create a markdoown table-of-content string from a jupyter notebook based on markdown "#".

:func:`geosoft.gxpy.utility.unique_name` Build a unique name or file name.

:func:`geosoft.gxpy.utility.vector_normalize` Normalise (Euclidean) the last axis of a numpy array

:func:`geosoft.gxpy.view.View_3d.add_extent` Expand current extent to include this extent.

:func:`geosoft.gxpy.view.View_3d.delete_plane` Delete a plane, and all content

:func:`geosoft.gxpy.view.delete_files` Delete a v3d file with associated files. Just calls `geosoft.gxpy.map.delete_files`.

:func:`geosoft.gxpy.vox.Vox.copy_vox` Create a new vox dataset to match a source vox, with optional new data.

:func:`geosoft.gxpy.vox.Vox.new` Create a new vox dataset

:func:`geosoft.gxpy.vox.Vox.np` Return vox subset in a 3D numpy array.

:func:`geosoft.gxpy.vox.Vox.open` Open an existing vox.

:func:`geosoft.gxpy.vox.Vox.value_at_location` Vox  at a location.

:func:`geosoft.gxpy.vox.delete_files` Delete all files associated with this vox name.

:func:`geosoft.gxpy.vox.elevation_from_depth` Return elevation origin and elevation cells sizes from a depth origin and depth cell-sizes

:func:`geosoft.gxpy.vox.locations_from_cells` Return the cell center locations from an array of cell sizes.

:func:`geosoft.gxpy.vox_display.VoxDisplay.solid` Create a solid colored vox_display from a `geosoft.gxpy.vox.Vox` instance.

:func:`geosoft.gxpy.vox_display.VoxDisplay.vector` Create a vector symbol vox_display from a `geosoft.gxpy.vox.Vox` instance.

:func:`geosoft.gxpy.vv.GXvv.fill` Fill a vv with a constant value.

:func:`geosoft.gxpy.vv.GXvv.min_max` Return the minimum and maximum values as doubles.  Strings are converted if possible.

:func:`geosoft.gxpy.vv.np_from_vvset` Return a 2d numpy array from a set of `GXvv` instances.

:func:`geosoft.gxpy.vv.vvset_from_np` Return a set of `GXvv` instances from a 2d numpy array.


  
Version 9.3
-----------------

New Classes
^^^^^^^^^^^

:class:`geosoft.gxpy.gdb.Channel` Class to work with database channels.  Use constructor `Channel.new` to create a new channel.

:class:`geosoft.gxpy.gdb.Line` Class to work with database lines.  Use constructor `Line.new` to create a new line.

:class:`geosoft.gxpy.metadata.Metadata` Simple interface to work with Geosoft metadata objects `geosoft.gxapi.GXMETA`.

:exc:`geosoft.gxpy.metadata.MetadataException` Exceptions from :mod:`geosoft.gxpy.metadata`.


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxpy.agg.Aggregate_image.figure_map` Create a figure map file from an aggregate.

:func:`geosoft.gxpy.agg.Aggregate_image.layer_unit_of_measure` Return the unit of measurement for the specified layer

:func:`geosoft.gxpy.gdb.Channel.delete` Delete the channel and all associated data.  After calling this method this

:func:`geosoft.gxpy.gdb.Geosoft_gdb.figure_map` Create a figure map file from selected lines in the database.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.get_gx_metadata` Return the database Geosoft metadata as a Geosoft `geosoft.gxpy.metadata.Metadata` instance.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.unlock_all` Unlock all locked symbols.

:func:`geosoft.gxpy.gdb.Line.bearing` Return bearing of a line based on location of the first and last point in the line.

:func:`geosoft.gxpy.gdb.Line.delete` Delete the line and all data associated with the line.  After calling this method this

:func:`geosoft.gxpy.gdb.Line.new` Create a new line.

:func:`geosoft.gxpy.gdb.create_line_name` Returns a valid database line name constructed from the component parts.

:func:`geosoft.gxpy.gdb.delete_files` Delete all files associates with this database name.

:func:`geosoft.gxpy.gdb.is_valid_line_name` Return True if this is a valid line name.

:func:`geosoft.gxpy.grid.figure_map` Create a map figure from a grid file.

:func:`geosoft.gxpy.group.Color_symbols_group.color_map` Return the :class:`geosoft.gxpy.group.Color_map` of a color symbol group.

:func:`geosoft.gxpy.group.Draw.point` Draw a point.

:func:`geosoft.gxpy.group.Draw.polypoint` Draw many points.

:func:`geosoft.gxpy.group.color_from_string` Return a Geosoft color number from a color string.

:func:`geosoft.gxpy.group.contour` Create a contour group from a grid file.  A default contour interval is determined from the grid.

:func:`geosoft.gxpy.gx.GXpyContext.has_entitlement` Returns True if the user has this entitlement.

:func:`geosoft.gxpy.map.Map.crc_image` Return the CRC of a map based on the output bitmap image.

:func:`geosoft.gxpy.map.Map.export_geotiff` Export map as a GeoTIFF image

:func:`geosoft.gxpy.map.Map.figure` Create a figure-style map.

:func:`geosoft.gxpy.map.Map.image_file` Save a map to an image file

:func:`geosoft.gxpy.metadata.Metadata.get_attribute` Retrieve an attribute setting.

:func:`geosoft.gxpy.metadata.Metadata.has_attribute` Returns `True` if this attribute exists in the metadata.

:func:`geosoft.gxpy.metadata.Metadata.has_node` Returns `True` if this node exists in the metadata.

:func:`geosoft.gxpy.metadata.Metadata.meta_dict` Metadata content as a nested dictionary.

:func:`geosoft.gxpy.metadata.Metadata.meta_type` Return if the content of this node is a node (`META_TYPE_NODE`) or an attribute (`META_TYPE_ATTRIBUTE`).

:func:`geosoft.gxpy.metadata.Metadata.node_attribute_token` returns the node and attribute number of an attribute.

:func:`geosoft.gxpy.metadata.Metadata.set_attribute` Set an attribute to a value.  The attribute is created if it does not exist.

:func:`geosoft.gxpy.project.add_document` Add a document to the project.  The document file can be any supported geosoft

:func:`geosoft.gxpy.project.remove_document` Remove a document from the project.  The document is identified by the document name, which

:func:`geosoft.gxpy.surface.Surface.add_mesh` Add a vv mesh to a new surface.

:func:`geosoft.gxpy.surface.SurfaceDataset.figure_map` Create a figure view file from an SurfaceDataset.

:func:`geosoft.gxpy.surface.SurfaceDataset.view_3d` Create a 3d view (`geosoft.gxpy.view.View_3d`) that contains this `SurfaceDataset`.

:func:`geosoft.gxpy.utility.url_retrieve` Retrieve a URL resource as a file.

:func:`geosoft.gxpy.view.View_3d.set_plane_relief_surface` Establish a relief surface for the current plane based on a grid.

:func:`geosoft.gxpy.vox.Vox.xyz` Return the spatial location of a the center of a cell in the vox.

:func:`geosoft.gxpy.vox_display.VoxDisplay.figure_map` Create a figure view file from the instance.

:func:`geosoft.gxpy.vox_display.VoxDisplay.view_3d` Create a 3d view (`geosoft.gxpy.view.View_3d`) from the instance.


  
Version 9.2.1
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxpy.grid.Grid.xyz` Returns the (x, y, z) location of an indexed point in the grid.


  
Version 9.2
-----------------

New Classes
^^^^^^^^^^^

:class:`geosoft.gxpy.agg.Aggregate_image` The AGG class supports the creation of aggregate images from one or more grid data sets. Aggregates

:class:`geosoft.gxpy.coordinate_system.Coordinate_system` Coordinate system class. A coordinate system defines a horizontal and vertical reference

:class:`geosoft.gxpy.coordinate_system.Coordinate_translate` Class to reproject coordinates between different coordinate systems.

:class:`geosoft.gxpy.coordinate_system.Wkt` Helper class to parse WKT-formatted spatial reference strings.

:class:`geosoft.gxpy.geometry.Geometry` Geometry base class for all geometries and spatial objects in Geosoft.

:class:`geosoft.gxpy.geometry.PPoint` Poly-Point class. Basic instance arithmetic and equality testing is supported.

:class:`geosoft.gxpy.geometry.Point2` Two points, for a line, or a rectangle, or a cube.  Basic instance arithmetic and equality testing is supported.

:class:`geosoft.gxpy.geometry.Point` Spatial location (x,y,z).  Basic instance arithmetic and equality testing is supported.

:class:`geosoft.gxpy.group.Aggregate_group` Aggregate group in a view

:class:`geosoft.gxpy.group.Color_map` Color map for establishing data color mapping for things like aggregates and color symbols.

:class:`geosoft.gxpy.group.Color` Colours, which are stored as a 32-bit color integer.

:class:`geosoft.gxpy.group.Draw_3d` Create a 3D drawing group within a 3D view.

:class:`geosoft.gxpy.group.Group` Geosoft group class.

:class:`geosoft.gxpy.group.Text_def` Text definition:

:class:`geosoft.gxpy.map.Map` Geosoft map files.

:class:`geosoft.gxpy.view.View_3d` Geosoft 3D views, which contain 3D drawing groups.

:class:`geosoft.gxpy.view.View` Geosoft view class.

:exc:`geosoft.gxpy.agg.AggregateException` Exceptions from :mod:`geosoft.gxpy.agg`.

:exc:`geosoft.gxpy.coordinate_system.CSException` Exceptions from :mod:`geosoft.gxpy.coordinate_system`.

:exc:`geosoft.gxpy.dataframe.DfException` Exceptions from :mod:`geosoft.gxpy.dataframe`.

:exc:`geosoft.gxpy.group.GroupException` Exceptions from :mod:`geosoft.gxpy.group`.

:exc:`geosoft.gxpy.map.MapException` Exceptions from :mod:`geosoft.gxpy.map`.

:exc:`geosoft.gxpy.view.ViewException` Exceptions from :mod:`geosoft.gxpy.view`.

:exc:`geosoft.gxpy.viewer.ViewerException` Exceptions from :mod:`geosoft.gxpy.viewer`.

:exc:`geosoft.gxpy.vox_display.VoxDisplayException` Exceptions from :mod:`geosoft.gxpy.vox_display`.


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxpy.agg.Aggregate_image.add_layer` Add an image layer to an aggregate

:func:`geosoft.gxpy.agg.Aggregate_image.layer_color_map` Return the :class:`geosoft.gxpy.group.Color_map` of a layer.

:func:`geosoft.gxpy.agg.Aggregate_image.new` Create a new aggregate from a grid.

:func:`geosoft.gxpy.agg.Aggregate_image.open` Create an :class:`Aggregate_image` from a :class:`geosoft.gxapi.GXAGG` instance.

:func:`geosoft.gxpy.coordinate_system.Coordinate_system.coordinate_dict` Returns "Geosoft" dictionary of coordinate system attributes.

:func:`geosoft.gxpy.coordinate_system.Coordinate_system.cs_name` Return requested name.

:func:`geosoft.gxpy.coordinate_system.Coordinate_system.oriented_from_xyz` Return oriented (x, y, z) coordinates from true base (x, y, z) coordinates.

:func:`geosoft.gxpy.coordinate_system.Coordinate_system.same_as` Return True if both coordinate systems (HCS and VCS) are the same.

:func:`geosoft.gxpy.coordinate_system.Coordinate_system.same_hcs` Return True if the HCS are the same.

:func:`geosoft.gxpy.coordinate_system.Coordinate_system.same_vcs` Return True if the VCS are the same.

:func:`geosoft.gxpy.coordinate_system.Coordinate_system.xyz_from_oriented` Return true base (x, y, z) coordinates from oriented (x, y, z) coordinates.

:func:`geosoft.gxpy.coordinate_system.Coordinate_translate.convert` Project data in array in which first columns are x,y or x,y,z.

:func:`geosoft.gxpy.coordinate_system.Wkt.find_key` Return the name and list of items for a key

:func:`geosoft.gxpy.coordinate_system.find_key` Find a key in the wkt, return it's name and items.

:func:`geosoft.gxpy.coordinate_system.hcs_orient_vcs_from_name` Split a full coordinate system name into its components. A name has the form "hcs <orient> [vcs]"

:func:`geosoft.gxpy.coordinate_system.list_from_wktsrs` Return a list from a wkt spatial reference string.

:func:`geosoft.gxpy.coordinate_system.name_from_hcs_orient_vcs` Construct a coordinate system name from an hcs, orientation and vcs.  If orient or vcs are None or

:func:`geosoft.gxpy.coordinate_system.name_list` Get a list of coordinate system names

:func:`geosoft.gxpy.coordinate_system.parameter_exists` Test if a parameter set exists in a coordinate system table.

:func:`geosoft.gxpy.coordinate_system.parameters` Get a dictionary of parameters for a coordinate system item.  Parameters are maintained in

:func:`geosoft.gxpy.coordinate_system.wkt_vcs` Compose a wkt VERTCS block from a Geosoft vcs string.

:func:`geosoft.gxpy.dataframe.Data_frame` Pandas DataFrame from a Geosoft table.

:func:`geosoft.gxpy.dataframe.table_column` Return a dictionary of a column from a table

:func:`geosoft.gxpy.dataframe.table_record` Return a dictionary of a single record from a table

:func:`geosoft.gxpy.gdb.Geosoft_gdb.read_channel_va` Read VA data from a single channel, return in a va.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.read_channel_vv` Read data from a single channel, return in a vv.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.read_line_vv` Read a line of data into VVs stored in a dictionary by channel.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.write_channel_va` Write VA data to a single channel.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.write_channel_vv` Write data to a single channel.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.write_line_vv` Write data to multiple channels in a line.  If no channel list is provided it assumes that the

:func:`geosoft.gxpy.geometry.PPoint.make_xyz_vv` Return x, y and z as a set of :class:`geosoft.gxpy.vv.GXvv`.

:func:`geosoft.gxpy.grid.Grid.copy` Create a new Grid instance as a copy of an existing grid.

:func:`geosoft.gxpy.grid.Grid.extent_2d` Return the 2D extent of the grid on the grid plane.

:func:`geosoft.gxpy.grid.Grid.extent_3d` Return the 3D extent of the grid in the base coordinate system.

:func:`geosoft.gxpy.grid.Grid.index_window` Create a windowed instance of a grid.

:func:`geosoft.gxpy.grid.Grid.xyzv` Return a numpy float array of (x, y, z, v) grid points.

:func:`geosoft.gxpy.grid.delete_files` Delete all files associates with this grid name.

:func:`geosoft.gxpy.group.Aggregate_group.new` Create a new aggregate group in a view.

:func:`geosoft.gxpy.group.Aggregate_group.open` Open an existing aggregate group in a view.

:func:`geosoft.gxpy.group.Color.adjust_brightness` Return a :class:`Color` instance adjusted for brightness.

:func:`geosoft.gxpy.group.Color_map.color_of_value` Return the gxg.Color of a value.  The mapping is determined with exclusive minima, inclusive maxima

:func:`geosoft.gxpy.group.Color_map.save_file` Save to a Geosoft file, `.tbl`, `.itr` or `.zon`.  If the file_name does not have an

:func:`geosoft.gxpy.group.Color_map.set_linear` Set the map boundaries based on a linear distribution between minimum and maximum.

:func:`geosoft.gxpy.group.Color_map.set_logarithmic` Set the color boundaries based on a logarithmic distribution between minimum and maximum.

:func:`geosoft.gxpy.group.Color_map.set_normal` Set the color boundaries using a normal distribution around a mean.

:func:`geosoft.gxpy.group.Color_map.set_sequential` Set color map zones based on a start and increment between each color zone.

:func:`geosoft.gxpy.group.Color_symbols_group.new` Create a new color symbols group with color mapping. If the group exists a new unique name is

:func:`geosoft.gxpy.group.Color_symbols_group.open` Open an existing color symbols group.

:func:`geosoft.gxpy.group.Draw.contour` Draw contours for a grid file.

:func:`geosoft.gxpy.group.Draw.graticule` Draw a graticule reference on a view.

:func:`geosoft.gxpy.group.Draw.line` Draw a line on the current plane

:func:`geosoft.gxpy.group.Draw.new_pen` Returns a pen that inherits default from the current view pen.  Arguments are the same

:func:`geosoft.gxpy.group.Draw.polygon` Draw a polygon on the current plane.

:func:`geosoft.gxpy.group.Draw.polyline` Draw a polyline the current plane

:func:`geosoft.gxpy.group.Draw.rectangle` Draw a 2D rectangle on the current plane

:func:`geosoft.gxpy.group.Draw.text` Draw text in the view.

:func:`geosoft.gxpy.group.Draw_3d.box_3d` Draw a 3D box

:func:`geosoft.gxpy.group.Draw_3d.cone_3d` Draw a cone.

:func:`geosoft.gxpy.group.Draw_3d.cylinder_3d` Draw a cylinder.

:func:`geosoft.gxpy.group.Draw_3d.polydata_3d` Create 3D objects rendered using data attributes.

:func:`geosoft.gxpy.group.Draw_3d.polyline_3d` Draw a polyline.

:func:`geosoft.gxpy.group.Draw_3d.polypoint_3d` Draw multiple points.

:func:`geosoft.gxpy.group.Draw_3d.sphere` Draw a sphere.

:func:`geosoft.gxpy.group.Group.extent_map_cm` Return an extent in map cm.

:func:`geosoft.gxpy.group.Group.locate` Locate the group relative to a point.

:func:`geosoft.gxpy.group.Pen.from_mapplot_string` Create a :class:`Pen` instance from a mapplot-style string descriptor using either a

:func:`geosoft.gxpy.group.edge_reference` Location of a reference point of an area.

:func:`geosoft.gxpy.group.font_weight_from_line_thickness` Returns font weight for a text height and line thickness.

:func:`geosoft.gxpy.group.legend_color_bar` Draw a color bar legend from :class:Color_map coloring definitions.

:func:`geosoft.gxpy.group.thickness_from_font_weight` Returns the line thickness appropriate for a text weight.

:func:`geosoft.gxpy.gx.GXpyContext.elapsed_seconds` Return the elapsed seconds since this GX instance started.

:func:`geosoft.gxpy.gx.GXpyContext.keep_temp_folder` Keep temporary file folder setting.

:func:`geosoft.gxpy.gx.GXpyContext.log` Log a string to the log file or log call-back as defined when creating :class:`GXpy` instance.

:func:`geosoft.gxpy.gx.GXpyContext.temp_file` Return a unique temporary file name as a full path.  The temporary file is created in

:func:`geosoft.gxpy.gx.GXpyContext.temp_folder` Return the GX temporary folder path.

:func:`geosoft.gxpy.gx.pop_resource` Pop a tracked resource off the resource stack.

:func:`geosoft.gxpy.gx.track_resource` Track a resource.  Resource tracking is useful for debugging resource leaks.  If you create a class

:func:`geosoft.gxpy.map.Map.aggregate_list` List of all aggregates in the map as 'view_name/group_name' (mode=0) or

:func:`geosoft.gxpy.map.Map.annotate_data_ll` Annotate the data view axis

:func:`geosoft.gxpy.map.Map.annotate_data_xy` Annotate a data view axis

:func:`geosoft.gxpy.map.Map.copy_view` Copy an existing view into a new view.

:func:`geosoft.gxpy.map.Map.create_linked_3d_view` Create a linked 3D view inside a 2D map to a `geosoft.gxpy.view.View_3d` in a 3DV

:func:`geosoft.gxpy.map.Map.delete_view` Delete a view from a map. You cannot delete the last view in a map.

:func:`geosoft.gxpy.map.Map.extent_data_views` Returns the extent of all data views on the map in map cm.

:func:`geosoft.gxpy.map.Map.get_class_name` Get the view name associated with a class.

:func:`geosoft.gxpy.map.Map.new` Create and open a new Geosoft map.

:func:`geosoft.gxpy.map.Map.north_arrow` Add a North arrow to the base view of the map.

:func:`geosoft.gxpy.map.Map.open` Open an existing map file.

:func:`geosoft.gxpy.map.Map.scale_bar` Draw a scale bar.

:func:`geosoft.gxpy.map.Map.set_class_name` Set the view name associated with a class.

:func:`geosoft.gxpy.map.Map.surround` Draw a map surround.  This will draw a single or a double neat-line around the base view of the

:func:`geosoft.gxpy.map.crc_map` Return the CRC of a map based on the output bitmap image.

:func:`geosoft.gxpy.map.delete_files` Delete all files associated with this map name.

:func:`geosoft.gxpy.map.map_file_name` Return a fully resolved map file path using the file name, with .map extension

:func:`geosoft.gxpy.map.save_as_image` Save a map file to an image file

:func:`geosoft.gxpy.project.Geosoft_project.current_db_state` Return the state of the current database.

:func:`geosoft.gxpy.project.Geosoft_project.current_map_state` Return the state of the current map.

:func:`geosoft.gxpy.project.pause` Display a pause dialog, wait for user to press continue or cancel

:func:`geosoft.gxpy.project.user_message` Display a message to the user

:func:`geosoft.gxpy.system.call_location` Returns function call location including file and line number as a string

:func:`geosoft.gxpy.utility.crc32_file` Return 32-bit CRC of a file.

:func:`geosoft.gxpy.utility.crc32_str` Return 32-bit CRC of a string.

:func:`geosoft.gxpy.utility.crc32` Return 32-bit CRC of a byte buffer.

:func:`geosoft.gxpy.utility.datetime_from_year` Return the Python datetime from a decimal Gregorian year.

:func:`geosoft.gxpy.utility.dict_from_xml` Return a dictionary of an xml string.

:func:`geosoft.gxpy.utility.dummy_mask` Return a 1-D dummy mask that is True for all rows  in a 2D numpy array that

:func:`geosoft.gxpy.utility.dummy_none` Returns None if dummy, otherwise the value.

:func:`geosoft.gxpy.utility.dummy_to_nan` Replaces dummies in float data to numpy.nan.  All other data types are returned unchanged.

:func:`geosoft.gxpy.utility.geosoft_metadata` Get the metadata dictionary for a geosoft data file.

:func:`geosoft.gxpy.utility.gx_dummy` Return the dummy for this value, or this type.

:func:`geosoft.gxpy.utility.merge_dict` Update a dictionary by adding key-values from second dictionary.  Unlike Python's

:func:`geosoft.gxpy.utility.normalize_file_name` Normalize a file name string by replacing '' with '/'.  This is useful for writing

:func:`geosoft.gxpy.utility.uuid` :returns: a uuid as a string

:func:`geosoft.gxpy.utility.xml_from_dict` Return a unicode XML string of a dictionary.

:func:`geosoft.gxpy.utility.year_from_datetime` Return a decimal Gregorian calendar year from a Python datetime.

:func:`geosoft.gxpy.view.View.close` Close a view.  Use to close a view when working outside of a `with ... as:` construct.

:func:`geosoft.gxpy.view.View.delete_group` Delete a group from a map. Nothing happens if the view does not contain this group.

:func:`geosoft.gxpy.view.View.extent_map_cm` Return an extent in map cm.

:func:`geosoft.gxpy.view.View.get_class_name` Get the name associated with a view class.

:func:`geosoft.gxpy.view.View.locate` Locate and scale the view on the map.

:func:`geosoft.gxpy.view.View.map_cm_to_view` Returns the location of this point on the map (in cm) to the view location in view units.

:func:`geosoft.gxpy.view.View.new` Create a new view on a map.

:func:`geosoft.gxpy.view.View.open` Open an en existing view on a map.

:func:`geosoft.gxpy.view.View.set_class_name` Set the name associated with a class.

:func:`geosoft.gxpy.view.View.view_to_map_cm` Returns the location of this point on the map in the view.

:func:`geosoft.gxpy.view.View_3d.groups_on_plane_list` List of groups on a plane.

:func:`geosoft.gxpy.view.View_3d.has_plane` True if the view contains plane

:func:`geosoft.gxpy.view.View_3d.new` Create a new 3D view.

:func:`geosoft.gxpy.view.View_3d.open` Open an existing geosoft_3dv file.

:func:`geosoft.gxpy.viewer.view_document` Open Geosoft Desktop application for viewing a supported Geosoft document type.  These include:

:func:`geosoft.gxpy.vv.GXvv.list` Return the content of the VV as a list.


  
Version 9.1
-----------------

New Classes
^^^^^^^^^^^

:class:`geosoft.gxpy.gdb.Geosoft_gdb` Class to work with Geosoft databases. This class wraps many of the functions found in

:class:`geosoft.gxpy.grid.Grid` Grid and image class.

:class:`geosoft.gxpy.gx.GXpyContext` Geosoft GX context.  There should be only one instance of this created per thread. To simplify usage, use the

:class:`geosoft.gxpy.va.GXva` VA class wrapper.

:class:`geosoft.gxpy.vv.GXvv` VV class wrapper.

:exc:`geosoft.gxpy.gdb.GdbException` Exceptions from `geosoft.gxpy.gdb`.

:exc:`geosoft.gxpy.grid.GridException` Exceptions from :mod:`geosoft.gxpy.grid`.

:exc:`geosoft.gxpy.gx.GXException` Exceptions from :mod:`geosoft.gxpy.gx`.

:exc:`geosoft.gxpy.project.ProjectException` Exceptions from :mod:`geosoft.gxpy.project`.

:exc:`geosoft.gxpy.system.GXSysException` Exceptions from :mod:`geosoft.gxpy.system`.

:exc:`geosoft.gxpy.utility.UtilityException` Exceptions from :mod:`geosoft.gxpy.utility`.

:exc:`geosoft.gxpy.va.VAException` Exceptions from :mod:`geosoft.gxpy.va`.

:exc:`geosoft.gxpy.vv.VVException` Exceptions from :mod:`geosoft.gxpy.vv`.


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxpy.gdb.Geosoft_gdb.channel_details` Return dictionary of channel details

:func:`geosoft.gxpy.gdb.Geosoft_gdb.channel_dtype` Returns channel numpy dtype

:func:`geosoft.gxpy.gdb.Geosoft_gdb.channel_name_symb` Return channel name, symbol

:func:`geosoft.gxpy.gdb.Geosoft_gdb.channel_width` Channel array width, 1 for normal channels, >1 for VA channels.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.commit` Commit database changes.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.delete_channel` Delete channel(s) by name or symbol.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.delete_line` Delete line(s) by name or symbol.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.discard` Discard database changes.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.exist_symb_` Check if a symbol exists of the required type.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.is_channel` Returns `True` if the channel name exists in the database.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.is_line` Returns `True` if the named line exists in the database.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.line_details` Return dictionary of line details

:func:`geosoft.gxpy.gdb.Geosoft_gdb.line_name_symb` Return line name, symbol

:func:`geosoft.gxpy.gdb.Geosoft_gdb.list_channels` Return a dict of channels in the database.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.list_lines` List of lines in the database, returned as a {name: symbol} dictionary

:func:`geosoft.gxpy.gdb.Geosoft_gdb.list_values` Build a list of unique values in a channel.  Uniqueness depends on the current display format for

:func:`geosoft.gxpy.gdb.Geosoft_gdb.new_channel` Return a channel symbol, create if it does not exist.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.new_line` Create a new line symbol.  If line exists an error is raised.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.new` Create a new database.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.open` Open an existing database.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.read_channel` Read data from a single channel.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.read_line` Read a line of data into a numpy array.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.select_lines` Change selected state of a line, or group of lines

:func:`geosoft.gxpy.gdb.Geosoft_gdb.set_channel_details` Set/change channel details from dictionary

:func:`geosoft.gxpy.gdb.Geosoft_gdb.write_channel` Write data to a single channel.

:func:`geosoft.gxpy.gdb.Geosoft_gdb.write_line` Write data to a multiple channels in a line.  If no channel list is provided it assumes that the

:func:`geosoft.gxpy.grid.Grid.delete_files` Delete the files associated with this grid when deleting the grid object.

:func:`geosoft.gxpy.grid.Grid.from_data_array` Create grid from a 2D data array or `geosoft.gxapi.GXPG`.

:func:`geosoft.gxpy.grid.Grid.gxpg` Get a copy of the `geosoft.gxapi.GXPG` instance for the grid.

:func:`geosoft.gxpy.grid.Grid.new` Create a new grid file.

:func:`geosoft.gxpy.grid.Grid.open` Open an existing grid file.

:func:`geosoft.gxpy.grid.Grid.properties` Get the grid properties dictionary

:func:`geosoft.gxpy.grid.Grid.read_column` :param column:  column to read, if not specified the next column is read starting from column 0

:func:`geosoft.gxpy.grid.Grid.read_row` :param row:     row to read, if not specified the next row is read starting from row 0

:func:`geosoft.gxpy.grid.Grid.set_properties` Set grid properties from a properties dict.  Settable property keys are:

:func:`geosoft.gxpy.grid.Grid.write_rows` Write data to a grid by rows.

:func:`geosoft.gxpy.grid.array_locations` Create an array of (x,y,z) points for a grid defined by properties

:func:`geosoft.gxpy.grid.decorate_name` Properly decorate a grid name.

:func:`geosoft.gxpy.grid.name_parts` Return folder, undecorated file name + ext, file root, ext, decorations.

:func:`geosoft.gxpy.grid_utility.sample` Return grid values sampled at the point locations.

:func:`geosoft.gxpy.gx.GXpyContext.disable_app` Disables application windows to allow modal Python UI.

:func:`geosoft.gxpy.gx.GXpyContext.enable_app` Enables application windows to allow modal Python UI.

:func:`geosoft.gxpy.gx.GXpyContext.entitlements` :returns: The current user entitlements as a dictionary.

:func:`geosoft.gxpy.project.dict_from_lst` Return a dictionary from a Geosoft `geosoft.gxapi.GXLST` instance.

:func:`geosoft.gxpy.project.get_user_input` Display a dialog prompt on the Geosoft Desktop and wait for user input.

:func:`geosoft.gxpy.project.running_script` :returns: 1 if running from a script, 0 if running interactively.

:func:`geosoft.gxpy.system.app_name` Returns application script name.

:func:`geosoft.gxpy.system.func_name` Returns function name.

:func:`geosoft.gxpy.system.parallel_map` A parallel equivalent of the map() built-in Python function (it supports only one iterable argument though).

:func:`geosoft.gxpy.system.remove_dir` Robust directory removal, with timed retries to allow for OS timing lags.  If you need to use this

:func:`geosoft.gxpy.system.unzip` Decompress and write the content of a zip file to a folder.

:func:`geosoft.gxpy.system.wait_on_file` Working with large files on systems that cache the file can cause a situation

:func:`geosoft.gxpy.utility.check_version` Check the minimum API version.

:func:`geosoft.gxpy.utility.decode` Decode a string (s) to a numpy format defined by string (f).

:func:`geosoft.gxpy.utility.dict_from_lst` Return a dictionary from a Geosoft `geosoft.gxapi.GXLST` instance.

:func:`geosoft.gxpy.utility.dict_from_reg` dictionary from a `geosoft.gxapi.GXREG` instance

:func:`geosoft.gxpy.utility.display_message` Display a message to the user.

:func:`geosoft.gxpy.utility.dtype_gx` :returns:   numpy dtype from a GX type

:func:`geosoft.gxpy.utility.folder_temp` Return the Geosoft temporary folder name.

:func:`geosoft.gxpy.utility.folder_user` Return the Geosoft user configurations folder name.

:func:`geosoft.gxpy.utility.folder_workspace` Return the Geosoft project folder name.

:func:`geosoft.gxpy.utility.get_parameters` Get parameters from the Project Parameter Block.

:func:`geosoft.gxpy.utility.get_shared_dict` Get a dictionary shared by an external application.

:func:`geosoft.gxpy.utility.gx_dtype` :returns:   GX type for a numpy dtype

:func:`geosoft.gxpy.utility.rdecode_err` Geosoft string conversion to a number, raising ValueError on failure

:func:`geosoft.gxpy.utility.rdecode` Geosoft string (number, date, time, geographic) conversion to a number, always works.

:func:`geosoft.gxpy.utility.reg_from_dict` `geosoft.gxapi.GXREG` instance from a dictionary

:func:`geosoft.gxpy.utility.run_external_python` Run a python script as an external program, returning results as a dictionary.

:func:`geosoft.gxpy.utility.save_parameters` Save parameters to the Project Parameter Block.  Parameter group names and member names

:func:`geosoft.gxpy.utility.set_shared_dict` Save a dictionary to be shared by an separate application.

:func:`geosoft.gxpy.utility.yearFromJulianDay2` Julian year

:func:`geosoft.gxpy.va.GXva.get_data` Return a numpy array of data from a va.

:func:`geosoft.gxpy.va.GXva.refid` Resample VA to a new fiducial and length

:func:`geosoft.gxpy.va.GXva.set_data` Copy numpy data into a VA.

:func:`geosoft.gxpy.vv.GXvv.get_data` Return vv data in a numpy array

:func:`geosoft.gxpy.vv.GXvv.refid` Resample VV to a new fiducial and length

:func:`geosoft.gxpy.vv.GXvv.set_data` Set vv data from an iterable, which can be another `GXvv` instance.  If the data is float type numpy.nan


geosoft.gxapi module history
==========================================

  
Version 2023.1
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXBIGRID.get_default_cell_size` Get default cell size value.

:func:`geosoft.gxapi.GXDU.avg_azimuth2` Returns average azimuth of selected lines.

:func:`geosoft.gxapi.GXDU.get_angled_bounding_rectangle` Return the angled bounding rectangle for data to be gridded on an angle.

:func:`geosoft.gxapi.GXDU.get_gridding_azimuth_to_minimize_padding` Return the gridding azimuth (degrees CW from north) that minimizes padding.

:func:`geosoft.gxapi.GXEDB.load_channel_after` Loads the channel after specified channel

:func:`geosoft.gxapi.GXPGU.direct_gridding_db2` Direct-gridding method, `GXDB <geosoft.gxapi.GXDB>` version.


  
Version 2023.0
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDB.get_modification_count` Gets the modification count from the database.

:func:`geosoft.gxapi.GXIMU.decimate_crooked_section_grid` Decimate a crooked section grid.


  
Version 2022.2
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GX3DC.create` Create a 3D view container which can be used to instantiate a full 3D View.

:func:`geosoft.gxapi.GX3DC.destroy_internal` Destroys a 3D container object and cleans up any unmanaged resources.

:func:`geosoft.gxapi.GX3DC.get_geo_view` Retrieves the GeoView associated with the 3D container.

:func:`geosoft.gxapi.GXDU.interp_gap_and_fill` Replace all dummies by interpolating from valid data.

:func:`geosoft.gxapi.GXDU.load_gravity_cg6_ex` Load a CG-6 gravity survey file. Specify the name of the output line

:func:`geosoft.gxapi.GXITR.equal_area_or_linear` Calculate an equal area transform.

:func:`geosoft.gxapi.GXKGRD.run_vv` Executes the Krigrid program directly on input data VVs.

:func:`geosoft.gxapi.GXLMSG.goto_line` Sends a 'go to line' message

:func:`geosoft.gxapi.GXMVIEW.render_ex` Render a specified area of view onto a Windows DC handle, setting the type of it and returning the new data extents

:func:`geosoft.gxapi.GXMVU.plot_voxel_slice` Extract a vertical slice from a voxel along a path and plot it to a 2D view.

:func:`geosoft.gxapi.GXSTK.set_error_plot_params` Set error bar plot parameters for the current profile.

:func:`geosoft.gxapi.GXVVU.distance_link_non_dummies` Create distance linking non-dummies `GXVV <geosoft.gxapi.GXVV>`

:func:`geosoft.gxapi.GXVVU.qc2` Quality control on deviation of data from norm in a `GXVV <geosoft.gxapi.GXVV>`


  
Version 2022.1
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDCOL.update_zone_transform_parameters` Recalculate the layer's ITR, based on the current type of the `GXDCOL <geosoft.gxapi.GXDCOL>`. Launches anappropriate zone transform type parameter GUI based on the current selection.

:func:`geosoft.gxapi.GXDU.average_spacing` Returns the average spacing along a line.

:func:`geosoft.gxapi.GXEDOC.copy` Copies a managed document to another document.

:func:`geosoft.gxapi.GXEDOC.save` Save the managed document.

:func:`geosoft.gxapi.GXMAP.dataset_file_path_list` Get a list of all dataset file paths in this map.

:func:`geosoft.gxapi.GXMAP.delete_empty_groups` Remove empty groups in the map, do not delete empty views.

:func:`geosoft.gxapi.GXMVIEW.add_folder_2d` Add a Map folder to the `GXMVIEW <geosoft.gxapi.GXMVIEW>`.

:func:`geosoft.gxapi.GXMVIEW.delete_folder_2d` Delete a 3DView folder.

:func:`geosoft.gxapi.GXMVIEW.move_group_to_folder_2d` Add group to a Map folder in `GXMVIEW <geosoft.gxapi.GXMVIEW>`.

:func:`geosoft.gxapi.GXPROJ.add_document_include_meta` Adds (and opens) a document file in the current project.

:func:`geosoft.gxapi.GXPROJ.get_default_project_path` Get default project folder.

:func:`geosoft.gxapi.GXPROJ.has_pending_central_publish_event` Checks if there is a pending publish event.

:func:`geosoft.gxapi.GXPROJ.save_document_view` Save document view to a file.

:func:`geosoft.gxapi.GXPROJ.set_default_project_path` Set default project folder.

:func:`geosoft.gxapi.GXTRANSFORMLAYER.apply_constant_transform` Apply constant transform to the transform layer

:func:`geosoft.gxapi.GXTRANSFORMLAYER.can_redo` Can perform redo on the transform layer

:func:`geosoft.gxapi.GXTRANSFORMLAYER.can_undo` Can perform undo on the transform layer

:func:`geosoft.gxapi.GXTRANSFORMLAYER.cancel_` Cancel changes done in the transform layer

:func:`geosoft.gxapi.GXTRANSFORMLAYER.clear_node_selection` Clear the section status of every node

:func:`geosoft.gxapi.GXTRANSFORMLAYER.end` End interactive editing for selected grid layer in gmsys.

:func:`geosoft.gxapi.GXTRANSFORMLAYER.redo` Redo one step of editing in the transform layer

:func:`geosoft.gxapi.GXTRANSFORMLAYER.save_to_new_layer_grid` Save changes to a new grid

:func:`geosoft.gxapi.GXTRANSFORMLAYER.select_node` Select or deselect a node by its index

:func:`geosoft.gxapi.GXTRANSFORMLAYER.undo` Undo one step of editing in the transform layer


  
Version 2021.2
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXAGG.get_layer_st` Get a `GXST <geosoft.gxapi.GXST>` filled with layer statistics

:func:`geosoft.gxapi.GXBIGRID.get_defaults` Get default values for max line separation, max point separation and trend angle.

:func:`geosoft.gxapi.GXCSYMB.get_stat` Get the `GXST <geosoft.gxapi.GXST>` of the `GXCSYMB <geosoft.gxapi.GXCSYMB>`

:func:`geosoft.gxapi.GXDCOL.end` TODO

:func:`geosoft.gxapi.GXDCOL.get_brightness_type` Is brightness set separately by layer and by object or just by object?

:func:`geosoft.gxapi.GXDCOL.get_brightness` Get the brightness of a single layer, or all the layers

:func:`geosoft.gxapi.GXDCOL.get_layer_histogram` Get a `GXVV <geosoft.gxapi.GXVV>` filled with histogram bin counts for each zone of the ITR

:func:`geosoft.gxapi.GXDCOL.get_layer_info` Get a layer's information

:func:`geosoft.gxapi.GXDCOL.get_layer_itr` Get a layer's ITR

:func:`geosoft.gxapi.GXDCOL.get_layer_statistics` Get a `GXST <geosoft.gxapi.GXST>` filled with layer statistics

:func:`geosoft.gxapi.GXDCOL.get_transparency` Get the transparency. This is returned for the entire map group.

:func:`geosoft.gxapi.GXDCOL.get_type` Get a layer's type

:func:`geosoft.gxapi.GXDCOL.number_of_layers` Get the number of layers.

:func:`geosoft.gxapi.GXDCOL.reset` Reset the AGG back to its initial state. Same as cancelling out of the colour tool and restarting; all layers are reset.

:func:`geosoft.gxapi.GXDCOL.save_layer_itr` Save the layer's ITR to a file. A dialog prompts for the file name.

:func:`geosoft.gxapi.GXDCOL.set_brightness` Set the brightness of a single layer, or all the layers

:func:`geosoft.gxapi.GXDCOL.set_itr_transform_from_layer` Set the input ITR transform to the provided type, based on the statistics of the chosen layer.

:func:`geosoft.gxapi.GXDCOL.set_layer_itr` Set a layer's ITR

:func:`geosoft.gxapi.GXDCOL.set_transparency` Set the transparency. This is set for the entire map group.

:func:`geosoft.gxapi.GXDCOL.update_zone_transform_type` Recalculate the layer's ITR to the provided type, based on the statistics of the chosen layer.

:func:`geosoft.gxapi.GXGUI.grid_stat_hist5` Display Histogram of up to 5 different grids

:func:`geosoft.gxapi.GXIMG.get_display_property` Gets display information about this image.

:func:`geosoft.gxapi.GXIMG.get_shadow_grid_path` Gets the name of a view.

:func:`geosoft.gxapi.GXIMG.set_display_property` Sets display information about this image.

:func:`geosoft.gxapi.GXIMG.set_shadow_grid_path` Sets display information about this image.

:func:`geosoft.gxapi.GXITR.get_contour` Get the contour value associated with the current transform model of the `GXITR <geosoft.gxapi.GXITR>`

:func:`geosoft.gxapi.GXITR.get_contrast` Get the contrast setting of the `GXITR <geosoft.gxapi.GXITR>`

:func:`geosoft.gxapi.GXITR.get_name` Get the name of the `GXITR <geosoft.gxapi.GXITR>`.

:func:`geosoft.gxapi.GXITR.get_zone_active` Get whether a zone of the `GXITR <geosoft.gxapi.GXITR>` is active (1) or rendered trasparent (0)

:func:`geosoft.gxapi.GXITR.get_zone_base_color` Get the base color in a zone of the `GXITR <geosoft.gxapi.GXITR>`

:func:`geosoft.gxapi.GXITR.get_zone_model` Get the `GXITR <geosoft.gxapi.GXITR>` zone model (e.g. Linear, LogLin, Equal Area) and the accompanying values (if defined)

:func:`geosoft.gxapi.GXITR.set_name` Set the name of the `GXITR <geosoft.gxapi.GXITR>`.

:func:`geosoft.gxapi.GXITR.set_zone_active` Set whether a zone of the `GXITR <geosoft.gxapi.GXITR>` is active (1) or rendered trasparent (0)

:func:`geosoft.gxapi.GXITR.set_zone_base_color` Set the color in a zone of the `GXITR <geosoft.gxapi.GXITR>`

:func:`geosoft.gxapi.GXITR.set_zone_model` Set the `GXITR <geosoft.gxapi.GXITR>` zone model (e.g. Linear, LogLin, Equal Area) and the accompanying values (if defined)

:func:`geosoft.gxapi.GXKGRD.get_defaults` Get default blanking distance and low-pass desampling factor.

:func:`geosoft.gxapi.GXMESHUTIL.apply_transformation` Applies a transformation to a surface, see :ref:`SURFACE_TRANSFORMATION_METHOD`for available operations. The existing mesh will be preserved, and a new mesh will be created with the target name in the target file. Reprojection willbe handled automatically in the case that the coordinate systems differ.

:func:`geosoft.gxapi.GXMESHUTIL.copy_mesh_to_geo_surface_file` Copy a mesh from one geosurface file to another

:func:`geosoft.gxapi.GXMESHUTIL.project_geosurface_onto_grid` Repoject surface with the coordinate system of the `GXIPJ <geosoft.gxapi.GXIPJ>`.

:func:`geosoft.gxapi.GXMESHUTIL.reproject_geosurface_file` Repoject surface with the coordinate system of the `GXIPJ <geosoft.gxapi.GXIPJ>`.

:func:`geosoft.gxapi.GXPROJ.get_central_project_information` Get Central project information.

:func:`geosoft.gxapi.GXPROJ.get_server_and_project_guid` Return the unique identifier of the project and server.

:func:`geosoft.gxapi.GXPROJ.set_central_project_information` Set Central project information.

:func:`geosoft.gxapi.GXSHD.end_shading` This ends interactive shading and must be called if any interactive changes should be applied. Passing false to apply changes is equivalent to simply disposing handle.

:func:`geosoft.gxapi.GXSHD.refresh` Refresh the SHD with new shading parameters.

:func:`geosoft.gxapi.GXSHD.track_interactive` Track a line on map and get shading parameters based on its length and direction.

:func:`geosoft.gxapi.GXSYS.get_publish_path_for_central` Get cache path to publish datasets to Central

:func:`geosoft.gxapi.GXSYS.publish_datasets_to_central` Publish datasets to Central


  
Version 2021.1
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.database_contains_voxel_geometry` Returns 1 if the original voxel geometry is stored inside the database

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.import_from_gdb_ignore_stored_voxel_geometry` Imports from a Geosoft Database, but ignores any stored internal geometry


  
Version 9.10
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDH.update_template_blob` Update the import template and store to the database if necessary.

:func:`geosoft.gxapi.GXDU.sort_index_n` Create an ordered index from any number of channels.  The order of rows where compared items are the same is preserved.

:func:`geosoft.gxapi.GXIMG.add_fault` Add a fault trace

:func:`geosoft.gxapi.GXIMG.delete_fault` Delete a fault trace

:func:`geosoft.gxapi.GXIMG.get_fault` Retrieve a fault trace

:func:`geosoft.gxapi.GXIMG.number_of_faults` Returns the number of individual fault traces stored in the IMG

:func:`geosoft.gxapi.GXIP.get_line_data` Get electrodes, data and mask values for a single line.

:func:`geosoft.gxapi.GXIP.recalculate_derived_data` Recalculate derived channel values.

:func:`geosoft.gxapi.GXIPJ.add_as_favourite_coordinate_system` Add as favourite coordinate system to Settings.

:func:`geosoft.gxapi.GXIPJ.compare_datums_to_specified_tolerance_with_feedback` Compare the datums of two coordinate systems, but allows for a specified accuracy and returns the reason if they are different

:func:`geosoft.gxapi.GXIPJ.coordinate_systems_are_the_same_to_specified_tolerance_with_feedback` Same as `coordinate_systems_are_the_same <geosoft.gxapi.GXIPJ.coordinate_systems_are_the_same>`, but allows for a specified accuracy and returns the reason if they are different

:func:`geosoft.gxapi.GXIPJ.copy_orientation` Copy any orientation and/or warp from one `GXIPJ <geosoft.gxapi.GXIPJ>` to another.

:func:`geosoft.gxapi.GXIPJ.get_authority_id` Get Authority ID (e.g. EPSG, ESRI) for coordinate system or `iDUMMY <geosoft.gxapi.iDUMMY>` if unknown.

:func:`geosoft.gxapi.GXIPJ.get_epsgid_for_datum` Get EPSG ID for datum of coordinate system or `iDUMMY <geosoft.gxapi.iDUMMY>` if unknown.

:func:`geosoft.gxapi.GXIPJ.get_favourite_coordinate_system` Get a favourite coordinate system from Settings.

:func:`geosoft.gxapi.GXIPJ.get_number_of_favourite_coordinate_systems` Get number of favourite coordinate systems in Settings.

:func:`geosoft.gxapi.GXIPJ.orientations_are_the_same_to_specified_tolerance_with_feedback` Same as `orientations_are_the_same <geosoft.gxapi.GXIPJ.orientations_are_the_same>`, but allows for small numerical differences

:func:`geosoft.gxapi.GXIPJ.remove_favourite_coordinate_system` Remove favourite coordinate system from Settings.

:func:`geosoft.gxapi.GXIPJ.warps_are_the_same_to_specified_tolerance_with_feedback` Same as `warps_are_the_same <geosoft.gxapi.GXIPJ.warps_are_the_same>`, but allows for a specified accuracy and returns the reason if they are different

:func:`geosoft.gxapi.GXKML.import_3d_line_path` Imports a KML 3D LinePath into a provided view.

:func:`geosoft.gxapi.GXKML.import_3d_polygon` Imports a KML 3D polygon into a provided view.

:func:`geosoft.gxapi.GXMVIEW.add_folder_3d` Add a 3DView folder to the `GXMVIEW <geosoft.gxapi.GXMVIEW>`.

:func:`geosoft.gxapi.GXMVIEW.delete_folder_3d` Delete a Map folder.

:func:`geosoft.gxapi.GXMVIEW.get_folder_items_2d` Get the list of key-value pairs representing the name(key) and the type(value) of all children in the specified parent folders in the `GXMVIEW <geosoft.gxapi.GXMVIEW>`.

:func:`geosoft.gxapi.GXMVIEW.get_folder_items_3d` Get the list of folders in the `GXMVIEW <geosoft.gxapi.GXMVIEW>`.

:func:`geosoft.gxapi.GXMVIEW.move_group_to_folder_3d` Add group to a 3DView folder in `GXMVIEW <geosoft.gxapi.GXMVIEW>`.

:func:`geosoft.gxapi.GXMVU.color_bar_reg_ex` Create a Color Bar in view

:func:`geosoft.gxapi.GXPG.set` Write a single value to a 2D `GXPG <geosoft.gxapi.GXPG>`

:func:`geosoft.gxapi.GXSEGYREADER.get_trace_data` Get the SEG Y trace file header data for a particular starting trace

:func:`geosoft.gxapi.GXSEGYREADER.get_trace_header_as_json` Return the contents of a trace header as JSON.


  
Version 9.9.1
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXGUI.configure_connection` Configures connection string from ODBC database data.


  
Version 9.9
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDB.non_string_and_non_array_chan_lst` Load a `GXLST <geosoft.gxapi.GXLST>` with non-string and non-array database channels.

:func:`geosoft.gxapi.GXDB.rename_line` Change the name for a line.

:func:`geosoft.gxapi.GXFFT.add_white_noise` Add white noise to the power spectrum of an FFT object.

:func:`geosoft.gxapi.GXFFT2.filter_response` Calculates response for filter(s) defined in control file. Not specific to 2D.

:func:`geosoft.gxapi.GXGU.magnetic_tilt_depth` Calculate the depth of magnetic sources based on the tilt depth method by Ahmed Salem et al.

:func:`geosoft.gxapi.GXGUI.dat_file_form_ex` Grid and Image file Open/Save Form for Multiple/Single file selections and optional filter list sorting.

:func:`geosoft.gxapi.GXIMU.grid_vc` Apply vertical continuation convolution filter to a grid.

:func:`geosoft.gxapi.GXMAP.rename_view` Renames a view in this map.

:func:`geosoft.gxapi.GXMVIEW.capture_3d_snapshot` Capture current 3D view state to a snapshot.

:func:`geosoft.gxapi.GXMVIEW.get_3d_snapshots` Get the list of 3D snapshots in a 3D view.

:func:`geosoft.gxapi.GXMVIEW.get_plane_surf_info` Get the surface information

:func:`geosoft.gxapi.GXMVIEW.get_plane_surface` Get the surface image of a plane

:func:`geosoft.gxapi.GXMVIEW.restore_3d_snapshot` Restore 3D view to specific snapshot state.

:func:`geosoft.gxapi.GXSYS.run_python` Run a Python GX script with initialization information.

:func:`geosoft.gxapi.GXTC.create_ex2` Creates a Terrain Correction object with surveytype and topo surface elevation grid


  
Version 9.8
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDB.create_symb_lst` Create  a `GXLST <geosoft.gxapi.GXLST>` object large enough to contain channel names and symbols numbers.

:func:`geosoft.gxapi.GXSYS.connect_with_current_central_instance` Query information necessary to communicate with current Central Instance


  
Version 9.7.1
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDH.get_template_blob_no_source_resolve` Retrieve the import template from the database.

:func:`geosoft.gxapi.GXDXFI.dxf2_view_no_surfaces` Draw entities in a DXF file to a view in a map, but for 3D views skips all surfaces

:func:`geosoft.gxapi.GXSURFACEITEM.compute_poly_line_intersections` Compute intersections of a 3D PolyLine with a `GXSURFACEITEM <geosoft.gxapi.GXSURFACEITEM>` Object

:func:`geosoft.gxapi.GXSURFACEITEM.intersects_bounding_box` Checks intersections of a bounding box with a `GXSURFACEITEM <geosoft.gxapi.GXSURFACEITEM>` Object


  
Version 9.7
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXContext.get_key_based_product_dirs` Gets key product folders based on geosoft.key file and registry

:func:`geosoft.gxapi.GXDH.convert_oriented_core_dip_dir_for_hole_survey` Converted alpha/beta values in oriented cores to dip/dip direction.

:func:`geosoft.gxapi.GXDH.desurvey_from_to` Calculate survey locations and depth from a hole survey using from/to values

:func:`geosoft.gxapi.GXDH.desurvey` Calculate survey locations and depth from a hole survey.

:func:`geosoft.gxapi.GXDU.load_gravity_cg6_to_line` Load a CG-6 gravity survey file. Specify the name of the output line

:func:`geosoft.gxapi.GXEDB.profile_shown` Return index of first profile window in which a profile is shown

:func:`geosoft.gxapi.GXGU.gravity_still_reading_database_correction` Gravity Still Reading Correction on selected lines, using a still readings database

:func:`geosoft.gxapi.GXIMG.extent` Get the img extents

:func:`geosoft.gxapi.GXIP.get_grids_vv` Get a VV populated with grids created making pseudosections by this IP object

:func:`geosoft.gxapi.GXIP.locate_contributing_electrodes_3d` Locate on a 3D view electrodes selected in a database row.

:func:`geosoft.gxapi.GXMULTIGRID3D.export_to_binary_ex` Export contents of `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to a Binary File, with dummy replacement.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.export_to_binary_ex` Export contents of `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to a Binary File, with dummy replacement.

:func:`geosoft.gxapi.GXMVIEW.get_maker_name` Used to retrieve the maker for a particular view group.

:func:`geosoft.gxapi.GXMVIEW.get_surface_filename` Get the surface filename.

:func:`geosoft.gxapi.GXMVIEW.is_group_exportable` Query whether the group is an exportable type.

:func:`geosoft.gxapi.GXMVIEW.is_plane_visible` Is the plane visible?

:func:`geosoft.gxapi.GXMVIEW.is_surface_item_visible` Is the surface item visible?

:func:`geosoft.gxapi.GXMVIEW.is_surface_plane` Is a surface plane?

:func:`geosoft.gxapi.GXMVIEW.view_group_json` Generate a JSON representation of a Group.

:func:`geosoft.gxapi.GXPROJ.add_grid_document` Adds (and opens) a grid document file in the current project with a particular colour distribution and colour file.

:func:`geosoft.gxapi.GXSEGYREADER.add_trace_filter` Add a filter based on trace header fields.

:func:`geosoft.gxapi.GXSEGYREADER.clear_trace_dummy_value` Disables the trace dummy value.

:func:`geosoft.gxapi.GXSEGYREADER.clear_trace_filters` Remove all active trace filters.

:func:`geosoft.gxapi.GXSEGYREADER.clear_user_range` Clears inline and crossline ranges to clamp to.

:func:`geosoft.gxapi.GXSEGYREADER.clear_user_z_range` Clears Z-range to clamp to, disbling z-clamping.

:func:`geosoft.gxapi.GXSEGYREADER.count_traces_that_pass_filters` Count the number of traces that pass the currently-configured trace filters.

:func:`geosoft.gxapi.GXSEGYREADER.export_files` Exports contents of SEG Y file to voxel and/or database.

:func:`geosoft.gxapi.GXSEGYREADER.get_clip_xy_extents` Gets the X,Y extents to clip the voxel.

:func:`geosoft.gxapi.GXSEGYREADER.get_is_3d` Returns true if the file is 3D false if it is 2D.

:func:`geosoft.gxapi.GXSEGYREADER.get_slice_filenames` Returns a list of the filenames of the XY slices that will be exported.

:func:`geosoft.gxapi.GXSEGYREADER.override_navigation_2d` Specify the X/Y coordinates of the traces, instead of using values from the trace headers.

:func:`geosoft.gxapi.GXSEGYREADER.set_crossline_slice_indices` Which crossline slices to export to a section grid.

:func:`geosoft.gxapi.GXSEGYREADER.set_gdb_output_filename` Exports contents of SEG Y file to a database.

:func:`geosoft.gxapi.GXSEGYREADER.set_inline_slice_indices` Which inline slices to export to a section grid.

:func:`geosoft.gxapi.GXSEGYREADER.set_is_3d` Specify if the input SEG-Y file is 3D or 2D.

:func:`geosoft.gxapi.GXSEGYREADER.set_section_output_filename` Exports contents of SEG Y file to a crooked section.

:func:`geosoft.gxapi.GXSEGYREADER.set_slice_output_prefix` Exports inline or crossline slices to a section grid.

:func:`geosoft.gxapi.GXSEGYREADER.set_trace_dummy_value` Sets the trace dummy value.

:func:`geosoft.gxapi.GXSEGYREADER.set_user_crossline_range` Sets crossline-range to clamp to.

:func:`geosoft.gxapi.GXSEGYREADER.set_user_inline_range` Sets inline-range to clamp to.

:func:`geosoft.gxapi.GXSEGYREADER.set_user_z_range` Sets Z-range to clamp to.

:func:`geosoft.gxapi.GXSEGYREADER.set_voxel_output_filename` Exports contents of SEG Y file to voxel.

:func:`geosoft.gxapi.GXSEGYREADER.set_z_decimation` Sets Z decimation factor.

:func:`geosoft.gxapi.GXSEGYREADER.set_z_slice_indices` Which z slices to export to a section grid.


  
Version 9.6
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXACQUIRE.get_selection_info` Get some information from existing selection file.

:func:`geosoft.gxapi.GXACQUIRE.selection_tool_force_grid_selection` Run the acQuire Selection Tool, but force selection of destination grid.

:func:`geosoft.gxapi.GXARCPY.add_error` Add error message to output of current script

:func:`geosoft.gxapi.GXARCPY.add_message` Add informational message to output of current script

:func:`geosoft.gxapi.GXARCPY.add_warning` Add warning message to output of current script

:func:`geosoft.gxapi.GXDH.get_mx_deposit_rights_info` Get MX Deposit Service API information via Geosoft ID rights.

:func:`geosoft.gxapi.GXDH.navigate_to_mx_deposit` Navigate to MX Deposit portal

:func:`geosoft.gxapi.GXDU.grav_drift2` Calculate base loop closure, calculate drift correction and correct for drift.

:func:`geosoft.gxapi.GXDU.qc_survey_plan2` Same as QCSurveyPlan_DU, but lines split by the polygon increment version numbers and keep the line number the same.

:func:`geosoft.gxapi.GXEDB.profile_rescale_all` Rescale all profiles in a selected window in both X and Y, based on current scaling selections

:func:`geosoft.gxapi.GXEMAP.draw_ply` Draws a polygon on the current map.

:func:`geosoft.gxapi.GXIMU.pigeon_hole_color` Pigeon-hole and count points by location and color locations in another grid based on ITR information.

:func:`geosoft.gxapi.GXMAP.render_view_bitmap` Render a map view to a bitmap.

:func:`geosoft.gxapi.GXMESHUTIL.extract_isosurface_from_voxel` Extracts isosurface from a voxel, and saves the voxel to a Geosurface file

:func:`geosoft.gxapi.GXPLY.clip_point` Clips a point in or out of the polygon.

:func:`geosoft.gxapi.GXSEGYREADER.check_sane_inline_crossline` Checks if the currently-configured inline and crossline fields seem sensible.

:func:`geosoft.gxapi.GXSEGYREADER.estimate_number_of_traces` Get the number of traces that would be in the SEG-Y file, given a trace length and data type.

:func:`geosoft.gxapi.GXSEGYREADER.export_voxel_and_database` Exports contents of SEG Y file to voxel and/or database.

:func:`geosoft.gxapi.GXSEGYREADER.get_binary_header` Get the SEG Y file's binary header.

:func:`geosoft.gxapi.GXSEGYREADER.get_endianess` Returns true if the file is little endian. false if it is big endian.

:func:`geosoft.gxapi.GXSEGYREADER.get_field_configuration` Returns information on the data in the trace headers.

:func:`geosoft.gxapi.GXSEGYREADER.get_georeferencing` Returns the georeferencing of the voxel that would be exported with the current configuration.

:func:`geosoft.gxapi.GXSEGYREADER.get_inline_and_crossline_azimuths` Get the inline and crossline azimuths, in degrees

:func:`geosoft.gxapi.GXSEGYREADER.get_last_sample_at` Returns the depth of the last sample in the traces, in the units specified by `SetZUnits()`

:func:`geosoft.gxapi.GXSEGYREADER.get_num_trace_data_types` Returns the number of supported trace data types.

:func:`geosoft.gxapi.GXSEGYREADER.get_possible_z_units` Get a list of the possible values that can be passed to `SetZUnits()`. The values returned by this function depend on what the z-type is set to.

:func:`geosoft.gxapi.GXSEGYREADER.get_sample_interval_configuration` Specifies where the sample interval comes from: can be a field in the binary file header, a field in the trace header, or a value specified by the user.

:func:`geosoft.gxapi.GXSEGYREADER.get_sample_interval` Returns the sample interval of the trace data.

:func:`geosoft.gxapi.GXSEGYREADER.get_text_header` Get the SEG Y file's text header.

:func:`geosoft.gxapi.GXSEGYREADER.get_tie_point` Return  the currently-active tie points. If SetTiePoints() has not already been called, then the returned points will be the automatically-selected ones.

:func:`geosoft.gxapi.GXSEGYREADER.get_trace_count` Get the number of traces in the SEG Y file

:func:`geosoft.gxapi.GXSEGYREADER.get_trace_data_at` Get the SEG Y trace file data for a particular data type, number of samples, and starting trace

:func:`geosoft.gxapi.GXSEGYREADER.get_trace_data_type_display_name` Get a string, suitable for displaying to the user, describing the type returned by passing the same `index` value to `GetTraceDataTypeName()`

:func:`geosoft.gxapi.GXSEGYREADER.get_trace_data_type_name` Get the name of one of the available data types. These are the names used as identifiers in this API. To get a name suitable for displaying to the user, use `GetTraceDataTypeDisplayName() instead.

:func:`geosoft.gxapi.GXSEGYREADER.get_trace_data_type` Get the data type of the trace data. This will match one of the names rfeturned by `GetTraceDataTypeName()`

:func:`geosoft.gxapi.GXSEGYREADER.get_trace_header_at` Get the SEG Y trace file header data for a particular starting trace

:func:`geosoft.gxapi.GXSEGYREADER.get_trace_length_configuration` Specifies where the trace length comes from: can be a field in the binary file header, a field in the trace header, or a value specified by the user.

:func:`geosoft.gxapi.GXSEGYREADER.get_trace_length` Returns the number of data samples per trace.

:func:`geosoft.gxapi.GXSEGYREADER.get_voxel_cell_size` Get the cell size of the voxel that would be exported with the current configuration.

:func:`geosoft.gxapi.GXSEGYREADER.get_voxel_dimensions` Get the size of the voxel that would be exported with the current configuration.

:func:`geosoft.gxapi.GXSEGYREADER.get_xy_units` Get the currently-specified xy-units.

:func:`geosoft.gxapi.GXSEGYREADER.get_z_offset_configuration` Specifies where the z-offset (time delay) comes from: can be a field in the binary file header, a field in the trace header, or a value specified by the user.

:func:`geosoft.gxapi.GXSEGYREADER.get_z_offset_units` Get the currently-specified units for the z offset.

:func:`geosoft.gxapi.GXSEGYREADER.get_z_offset` Returns the z-offset (time delay) of the trace data. Positive values correspond to a deeper top-of-trace; negative values to a higher top-of-trace.

:func:`geosoft.gxapi.GXSEGYREADER.get_z_type` Indicate if the z-dimension is time or depth.

:func:`geosoft.gxapi.GXSEGYREADER.get_z_units` Get the currently-specified z-units.

:func:`geosoft.gxapi.GXSEGYREADER.list_binary_header_fields` Returns the names and offsets of the fields in the binary header.

:func:`geosoft.gxapi.GXSEGYREADER.list_trace_header_fields` Returns the names and offsets of the fields in the trace header.

:func:`geosoft.gxapi.GXSEGYREADER.open_file` Opens a 3D SEG Y file.

:func:`geosoft.gxapi.GXSEGYREADER.recalculate_georeferencing` Recalculate georeferencing; call after configuration has changed.

:func:`geosoft.gxapi.GXSEGYREADER.reset_tie_points` Discard user-supplied tie points and auto-choose new ones..

:func:`geosoft.gxapi.GXSEGYREADER.scan_file` Scans the SEG Y file, and attempts to guess the layout.

:func:`geosoft.gxapi.GXSEGYREADER.set_auto_voxel_cell_size_xy` Set the XY cell size of the voxel that would be exported to the dimensions calculated from the tie points..

:func:`geosoft.gxapi.GXSEGYREADER.set_endianess` Set the endianess of the file.

:func:`geosoft.gxapi.GXSEGYREADER.set_field_configuration` Sets the interpretation of the fields in the SEG Y file, and specifies which fields should be exported to GDB.

:func:`geosoft.gxapi.GXSEGYREADER.set_georeferencing` Sets the georeferencing of the voxel that would be exported with the current configuration.

:func:`geosoft.gxapi.GXSEGYREADER.set_sample_interval_configuration` Specifies where the sample interval comes from: can be a field in the binary file header, a field in the trace header, or a value specified by the user.

:func:`geosoft.gxapi.GXSEGYREADER.set_tie_point` Set the currently-active tie points. If SetTiePoints() has not already been called, then the returned points will be the automatically-selected ones.

:func:`geosoft.gxapi.GXSEGYREADER.set_trace_data_type` Set the data type of the trace data. This must match one of the names returned by `GetTraceDataTypeName()`

:func:`geosoft.gxapi.GXSEGYREADER.set_trace_length_configuration` Specifies where the trace length comes from: can be a field in the binary file header, a field in the trace header, or a value specified by the user.

:func:`geosoft.gxapi.GXSEGYREADER.set_user_voxel_cell_size_xy` Set the XY cell size of the voxel that would be exported with the current configuration.

:func:`geosoft.gxapi.GXSEGYREADER.set_z_offset_configuration` Specifies where the z-offset (time delay) comes from: can be a field in the binary file header, a field in the trace header, or a value specified by the user.

:func:`geosoft.gxapi.GXSEGYREADER.set_z_offset_units` Set the units that the z-offset is in.

:func:`geosoft.gxapi.GXSEGYREADER.set_z_type` Specify if the z-dimension is time or depth.

:func:`geosoft.gxapi.GXSEGYREADER.set_z_units` Set the z-units.

:func:`geosoft.gxapi.GXSYS.check_product_updates` Check for product updates via Geosoft Connect

:func:`geosoft.gxapi.GXSYS.get_error_ap` Get the error number of an error.

:func:`geosoft.gxapi.GXSYS.testing_system_mode` Checks to see if the GX is running in the Geosoft testing system.

:func:`geosoft.gxapi.GXUSERMETA.set_xml_format` Get the XML Format

:func:`geosoft.gxapi.GXVA.range_columns` Computes the minimum and maximum range of the data for individual columns, in doubles,

:func:`geosoft.gxapi.GXVA.range` Computes the minimum and maximum range of the data, in doubles,

:func:`geosoft.gxapi.GXVV.get_ext_type` Return the internal data type of this VV


  
Version 9.5.1
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXEDB.get_profile_x_axis_options` Get profile X-axis options

:func:`geosoft.gxapi.GXEDB.set_profile_x_axis_options` Set profile X-axis options


  
Version 9.5
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDH.get_hole_survey_ex` Get the Survey information of a Hole.

:func:`geosoft.gxapi.GXDH.get_hole_survey_from_to` Get the Survey information of a Hole using From/To database.

:func:`geosoft.gxapi.GXDU.em_tau_trend_window` Automatic fitting EM Tau

:func:`geosoft.gxapi.GXDU.footprint_coverage_dynamic` Compute the footprint of a survey

:func:`geosoft.gxapi.GXDU.footprint_coverage_static` Compute the footprint of a survey

:func:`geosoft.gxapi.GXGU.despike_em_array` Despike a time-series with individual noise levels

:func:`geosoft.gxapi.GXGUI.import_drill_wizard_ex` Generate a template file for importing drill holes where type is known

:func:`geosoft.gxapi.GXMESH.add_face` Adds a face to a patch in a mesh

:func:`geosoft.gxapi.GXMESH.add_vertex` Adds a vertex to a patch in a mesh

:func:`geosoft.gxapi.GXMESH.create` Creates a new Mesh

:func:`geosoft.gxapi.GXMESH.delete_patch` Deletes a patch specified by Patch ID from a mesh

:func:`geosoft.gxapi.GXMESH.get_attribute_values` Inserts an attribute set to a mesh

:func:`geosoft.gxapi.GXMESH.get_faces` Returns all the faces comprising of vertex indices in a patch

:func:`geosoft.gxapi.GXMESH.get_vertex_point` Number of faces in a patch in mesh

:func:`geosoft.gxapi.GXMESH.get_vertices` Returns all the vertices in a patch

:func:`geosoft.gxapi.GXMESH.import_grid_to_mesh` Imports a Grid to a Surface. Creates a new Geosurface file for the surface

:func:`geosoft.gxapi.GXMESH.insert_attributes` Inserts an attribute set to a mesh

:func:`geosoft.gxapi.GXMESH.insert_patch` Inserts a new surface patch to the mesh specified by a unique ID

:func:`geosoft.gxapi.GXMESH.num_faces` Number of faces in a patch in mesh

:func:`geosoft.gxapi.GXMESH.num_patches` Returns the number of patches added to the mesh

:func:`geosoft.gxapi.GXMESH.num_vertices` Number of vertices in a patch in mesh

:func:`geosoft.gxapi.GXMESH.open` Opens an existing Mesh

:func:`geosoft.gxapi.GXMESH.patch_exists` Checks if a patch specified by a patch ID exists in a mesh

:func:`geosoft.gxapi.GXMESH.save` Saves Mesh to the Project Cache and Geosurface file

:func:`geosoft.gxapi.GXMESH.set_attribute_values` Inserts an attribute set to a mesh

:func:`geosoft.gxapi.GXMESHUTIL.clip_surface_with_extents` Clip a Surface with X,Y,Z extents

:func:`geosoft.gxapi.GXMESHUTIL.clip_surface_with_grid` Clip a Surface with a Grid Surface (grid converted to surface)

:func:`geosoft.gxapi.GXMESHUTIL.clip_surface_with_polygon2d` Clip a Surface a specified Polygon file

:func:`geosoft.gxapi.GXMESHUTIL.compute_surface_clip` Clip a surface with another surface, and output the clipped surfaces

:func:`geosoft.gxapi.GXMESHUTIL.compute_surface_intersection` Computes and outputs the intersection of two closed surfaces

:func:`geosoft.gxapi.GXMESHUTIL.compute_surface_simplification` Simplifies a surface by reducing the number of edges by half

:func:`geosoft.gxapi.GXMESHUTIL.compute_surface_subdivision` Smooths a surface by applying a loop subdivision algorithm

:func:`geosoft.gxapi.GXMESHUTIL.compute_surface_union` Compute union of two surfaces

:func:`geosoft.gxapi.GXMESHUTIL.does_surface_intersect` Checks if the two surfaces intersect at all

:func:`geosoft.gxapi.GXMESHUTIL.does_surface_self_intersect` Checks if a surface self-intersects

:func:`geosoft.gxapi.GXMESHUTIL.import_grid_to_surface` Imports a Grid to a Surface

:func:`geosoft.gxapi.GXMPLY.create` Creates a Multi Polygon Object.

:func:`geosoft.gxapi.GXMULTIGRID3D.get_data_extents` Get the voxel size that has non-dummy data.

:func:`geosoft.gxapi.GXMULTIGRID3D.get_data_ground_extents` Get the voxel size in ground units that has non-dummy data.

:func:`geosoft.gxapi.GXMULTIGRID3D.get_vector_orientation` Get the vector voxel orientation

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.clip_to_polygon` Invert the Z values in the Grid3d.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.convert_vector_to_double_using_rotation` Convert a Vector Voxel to 3 double Voxels using an external rotation. Internal rotations are ignored.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.create_double_constant_copy` Generate a double MultiVoxset with a constant value based on an input voxel

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.create_subset_from_double_extents` Create a new MULTIGRID3D that is a subset of the non-dummy extents.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.create_subset` Create a new MULTIGRID3D that is a subset of an exisiting MULTIGRID3D.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.extract_dem` Extract a DEM grid from a voxel.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.get_data_extents` Get the voxel size that has non-dummy data.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.get_data_ground_extents` Get the voxel size in ground units that has non-dummy data.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.grid_idw_from_gdb` Create a grid3d using IDW gridding.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.grid_points_from_gdb` Grid a grid3d from a database using kriging.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.grid_points_z_ex_from_gdb` Grid a grid3d from a database (using variable Z's)

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.grid_points_z_from_gdb` Grid a grid3d from a database (using variable Z's)

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.invert_z` Invert the Z values in the Grid3d.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.krig_from_gdb` A more compact and extensible form of `log_grid_points_z_ex_from_gdb <geosoft.gxapi.GXMULTIGRID3DUTIL.log_grid_points_z_ex_from_gdb>`.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.log_grid_points_z_ex_from_gdb` Log grid a grid3d from a database (using variable Z's)

:func:`geosoft.gxapi.GXMVIEW.polygon_mply` Draw multiple complex polygons from `GXMPLY <geosoft.gxapi.GXMPLY>`.

:func:`geosoft.gxapi.GXPLY.combine` Combines two `GXPLY <geosoft.gxapi.GXPLY>` Object with another

:func:`geosoft.gxapi.GXPLY.is_valid` Ensure a polygon is valid

:func:`geosoft.gxapi.GXVOXD.get_render_mode` Get voxel render mode.

:func:`geosoft.gxapi.GXVOXD.set_render_mode` Get voxel render mode.


  
Version 9.4
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXARCMAP.load_raster_ex` Load a raster file to the current data frame and create associated files

:func:`geosoft.gxapi.GXDU.em_tau_automatic` Automatic fitting EM Tau

:func:`geosoft.gxapi.GXDU.em_tau_calc` Fitting  f(t) = A * e^(-t/Tau) = e^s0 * e^(-s1*t), where s0=lnA, s1=1/Tau

:func:`geosoft.gxapi.GXDU.em_tau_late_time` Automatic fitting EM Tau

:func:`geosoft.gxapi.GXDU.em_tau_manual` Automatic fitting EM Tau

:func:`geosoft.gxapi.GXFFT2.rad_spc_alt` `GXFFT2 <geosoft.gxapi.GXFFT2>` transform Radially averaged power spectrum - log before average and no normalization

:func:`geosoft.gxapi.GXGRID3D.fill_double` Fill the grid3d with a single double value.

:func:`geosoft.gxapi.GXGRID3D.fill_thematic` Fill the grid3d with a single thematic value.

:func:`geosoft.gxapi.GXGRID3D.fill_vector` Fill the grid3d with a single vector value.

:func:`geosoft.gxapi.GXGRID3D.get_double_stats` Get Double statistics.

:func:`geosoft.gxapi.GXGRID3D.get_elements_in_block_x` Get the number of cells in the block in the X direction

:func:`geosoft.gxapi.GXGRID3D.get_elements_in_block_y` Get the number of cells in the block in the Y direction

:func:`geosoft.gxapi.GXGRID3D.get_elements_in_block_z` Get the number of cells in the block in the Z direction

:func:`geosoft.gxapi.GXGRID3D.get_thematic_stats` Get Thematic Data statistics.

:func:`geosoft.gxapi.GXGRID3D.get_tpat` Get the TPAT from the thematic grid3d.

:func:`geosoft.gxapi.GXGRID3D.get_type` Get the type of this GRID3D

:func:`geosoft.gxapi.GXGRID3D.get_vector_stats` Get Vector Data statistics.

:func:`geosoft.gxapi.GXGRID3D.is_double` Does this grid3d contain floating point data

:func:`geosoft.gxapi.GXGRID3D.is_thematic` Does this grid3d contain thematic data

:func:`geosoft.gxapi.GXGRID3D.is_vector` Does this grid3d contain vector data

:func:`geosoft.gxapi.GXGRID3D.read_x` Read data from a GRID3D in the x direction (MOST EFFICIENT)

:func:`geosoft.gxapi.GXGRID3D.read_y` Read data from a GRID3D in the Y direction

:func:`geosoft.gxapi.GXGRID3D.read_z` Read data from a GRID3D in the Z direction

:func:`geosoft.gxapi.GXGRID3D.set_tpat` Set the TPAT of a thematic grid3d.

:func:`geosoft.gxapi.GXGRID3D.write_x` Write data to a GRID3D in the X direction (MOST EFFICIENT)

:func:`geosoft.gxapi.GXGRID3D.write_y` Write data to a GRID3D in the Y direction

:func:`geosoft.gxapi.GXGRID3D.write_z` Write data to a GRID3D in the Z direction

:func:`geosoft.gxapi.GXIMU.refresh_shad` Refresh a shaded relief image

:func:`geosoft.gxapi.GXIP.locate_contributing_electrodes` Locate on a map electrodes selected in a database row.

:func:`geosoft.gxapi.GXIPGUI.launch_remove_contributing_electrodes_ext_tool` Launch the Remove Contributing Electrodes dialog.

:func:`geosoft.gxapi.GXIPJ.get_from_binary_as_string` Get `GXIPJ <geosoft.gxapi.GXIPJ>` from binary-as-string

:func:`geosoft.gxapi.GXIPJ.set_from_binary_as_string` Set `GXIPJ <geosoft.gxapi.GXIPJ>` from binary-as-string

:func:`geosoft.gxapi.GXITR.default_color_method` Return the user-defined global default color method.

:func:`geosoft.gxapi.GXMULTIGRID3D.create_default` Get the default voxset

:func:`geosoft.gxapi.GXMULTIGRID3D.create` Creates a new Multivoxset

:func:`geosoft.gxapi.GXMULTIGRID3D.duplicate` Creates an MULTIGRID3D with identical geometry to the input

:func:`geosoft.gxapi.GXMULTIGRID3D.export_to_binary` Export contents of `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to a Binary File.

:func:`geosoft.gxapi.GXMULTIGRID3D.export_to_gdb` Export To GDB

:func:`geosoft.gxapi.GXMULTIGRID3D.export_to_pg` Export a MULTIGRID3D To a PG

:func:`geosoft.gxapi.GXMULTIGRID3D.export_to_wa` Export To GDB

:func:`geosoft.gxapi.GXMULTIGRID3D.export_to_xml` Export a `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to XML

:func:`geosoft.gxapi.GXMULTIGRID3D.export_to_xyz` Export a `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to an XYZ File

:func:`geosoft.gxapi.GXMULTIGRID3D.fill` Fill a grid3d.

:func:`geosoft.gxapi.GXMULTIGRID3D.get_bounding_box` Get the bounding box

:func:`geosoft.gxapi.GXMULTIGRID3D.get_cell_sizes_x` Get the cell sizes in the X direction

:func:`geosoft.gxapi.GXMULTIGRID3D.get_cell_sizes_y` Get the cell sizes in the Y direction

:func:`geosoft.gxapi.GXMULTIGRID3D.get_cell_sizes_z` Get the cell sizes in the Z direction

:func:`geosoft.gxapi.GXMULTIGRID3D.get_default` Get the default voxset

:func:`geosoft.gxapi.GXMULTIGRID3D.get_ipj` Get the projection of the multigrid3d.

:func:`geosoft.gxapi.GXMULTIGRID3D.get_oriented_data_extents` Get the data extents based on an orientation

:func:`geosoft.gxapi.GXMULTIGRID3D.get_origin` Get the origin

:func:`geosoft.gxapi.GXMULTIGRID3D.get_section_cell_sizes` Get the cell sizes of a section

:func:`geosoft.gxapi.GXMULTIGRID3D.get_size_x` Get the number of cells in the X direction

:func:`geosoft.gxapi.GXMULTIGRID3D.get_size_y` Get the number of cells in the X direction

:func:`geosoft.gxapi.GXMULTIGRID3D.get_size_z` Get the number of cells in the X direction

:func:`geosoft.gxapi.GXMULTIGRID3D.get_uniform_cell_size_x` Get the uniform cell size in the X direction

:func:`geosoft.gxapi.GXMULTIGRID3D.get_uniform_cell_size_y` Get the uniform cell size in the Y direction

:func:`geosoft.gxapi.GXMULTIGRID3D.get_uniform_cell_size_z` Get the uniform cell size in the Z direction

:func:`geosoft.gxapi.GXMULTIGRID3D.get_volume_vectors` Get the direction of the volume

:func:`geosoft.gxapi.GXMULTIGRID3D.is_uniform_cell_size_x` Is the cell uniform in the X direction

:func:`geosoft.gxapi.GXMULTIGRID3D.is_uniform_cell_size_y` Is the cell uniform in the Y direction

:func:`geosoft.gxapi.GXMULTIGRID3D.is_uniform_cell_size_z` Is the cell uniform in the Z direction

:func:`geosoft.gxapi.GXMULTIGRID3D.modify` Opens an existing Multivoxset with an plan to modify it

:func:`geosoft.gxapi.GXMULTIGRID3D.open` Opens an existing Multivoxset

:func:`geosoft.gxapi.GXMULTIGRID3D.set_cell_sizes_x` Set the cell sizes in the X direction

:func:`geosoft.gxapi.GXMULTIGRID3D.set_cell_sizes_y` Set the cell sizes in the Y direction

:func:`geosoft.gxapi.GXMULTIGRID3D.set_cell_sizes_z` Set the cell sizes in the Z direction

:func:`geosoft.gxapi.GXMULTIGRID3D.set_ipj` Set the projection of the multigrid3d.

:func:`geosoft.gxapi.GXMULTIGRID3D.set_origin` Set the origin

:func:`geosoft.gxapi.GXMULTIGRID3D.set_uniform_cell_size_x` Set the uniform cell size in the X direction

:func:`geosoft.gxapi.GXMULTIGRID3D.set_uniform_cell_size_y` Get the uniform cell size in the Y direction

:func:`geosoft.gxapi.GXMULTIGRID3D.set_uniform_cell_size_z` Get the uniform cell size in the Z direction

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.check_equal_to_legacy_voxel` Compare `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to Legacy Voxel

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.compute_default_cell_size` Used if the user does not provide a default cell size.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.convert_density_to_velocity` Convert Density MultiVoxset to Velocity MultiVoxset

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.convert_double_to_thematic` Convert Double MultiVoxset to Thematic MultiVoxset

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.convert_double_to_vector` Convert 3 Double Voxels to a Vector Voxel

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.convert_thematic_to_double` Convert Thematic MultiVoxset to Double MultiVoxset

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.convert_vector_to_double` Convert a Vector Voxel to 3 double Voxels

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.convert_velocity_to_density` Convert Velocity MultiVoxset to Density MultiVoxset

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.create_double_constant_vv` Generate a double MultiVoxset with a constant value and non-uniform cell sizes

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.create_double_constant` Generate a double MultiVoxset with a constant value

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.create_thematic_constant_vv` Generate a double MultiVoxset with a constant value and non-uniform cell sizes

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.create_thematic_constant` Generate a double MultiVoxset with a constant value

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.create_vector_constant_vv` Generate a double MultiVoxset with a constant value and non-uniform cell sizes

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.create_vector_constant` Generate a double MultiVoxset with a constant value

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.export_to_binary` Export contents of `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to a Binary File.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.export_to_gdb` Export To GDB

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.export_to_segy` Export To SEGY

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.export_to_voxel` Exports a Multi-Voxset into a Voxel

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.export_to_wa` Export To GDB

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.export_to_xml` Export a `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to XML

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.export_to_xyz` Export a `GXMULTIGRID3D <geosoft.gxapi.GXMULTIGRID3D>` to an XYZ File

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.filter` Apply a 3D filter to a grid3d.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.get_gocad_location` Get the location of a grid3d with origin and scaled xyz vectors for use with GOCAD.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.grid_direct_from_gdb` Create a grid3d using direct gridding.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.import_from_datamine` Create a Geosoft Voxel file from a Datamine block model file.

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.import_from_gdb` Imports from a Geosoft Database

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.import_from_gocad` Imports a MultiVoxset from a GOCAD File

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.import_from_ubc` Import UBC file into a MultiVoxset

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.import_from_vector_gdb` Imports from a Vector Geosoft Database

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.import_from_voxel` Import a Voxel directly into a Multi-Voxset

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.import_from_xyz` Import XYZ file into a Multi-Voxset

:func:`geosoft.gxapi.GXMULTIGRID3DUTIL.list_properties_gocad` List all the properties available in this GOCAD file.

:func:`geosoft.gxapi.GXMVU.export_map_groups_to_gdb` Export map group(s) to database line(s).

:func:`geosoft.gxapi.GXPJ.project_bounding_volume` Project a bounding volume.

:func:`geosoft.gxapi.GXRGRD.run_list` Executes the Rangrid program from a list of databases.

:func:`geosoft.gxapi.GXSTORAGEPROJECT.close` Close the project storage.

:func:`geosoft.gxapi.GXSTORAGEPROJECT.open` Open a project storage.

:func:`geosoft.gxapi.GXSTORAGEPROJECT.remove_dataset` Remove this dataset from the project.

:func:`geosoft.gxapi.GXSURFACE.dump_geometry_to_text_file` Dump surface geometry to a text file.

:func:`geosoft.gxapi.GXSYS.geosoft_connect_authenticate_and_navigate` Automatically authenticate and navigate to my.geosoft.com URL

:func:`geosoft.gxapi.GXSYS.get_geosoft_id` Get the Geosoft ID (email) if signed in

:func:`geosoft.gxapi.GXSYS.get_profile_name` Get the profile name as defined in My Geosoft (or email if not defined)

:func:`geosoft.gxapi.GXSYS.get_profile_url` Get link to my.geosoft.com profile URL

:func:`geosoft.gxapi.GXSYS.is_signed_in` Check if signed in via Geosoft Connect

:func:`geosoft.gxapi.GXSYS.sign_in` Sign in via Geosoft Connect


  
Version 9.3.1
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDU.load_gravity_cg6` Load a CG-6 gravity survey file.

:func:`geosoft.gxapi.GXTB.set_sort_mode` Set the sort mode of a table.


  
Version 9.3
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXCSYMB.get_itr` Get the `GXITR <geosoft.gxapi.GXITR>` of the `GXCSYMB <geosoft.gxapi.GXCSYMB>`

:func:`geosoft.gxapi.GXDH.edit_classification_table_file_gui` Edit a symbol color/pattern CSV file

:func:`geosoft.gxapi.GXE3DV.get_base_view` Get the current Base `GXMVIEW <geosoft.gxapi.GXMVIEW>` (used to draw 2D legends for groups)

:func:`geosoft.gxapi.GXE3DV.get_data_view` Get the current data (3D) `GXMVIEW <geosoft.gxapi.GXMVIEW>`

:func:`geosoft.gxapi.GXEMAP.get_e_3dv` Get an `GXE3DV <geosoft.gxapi.GXE3DV>` from the `GXEMAP <geosoft.gxapi.GXEMAP>`

:func:`geosoft.gxapi.GXGUI.custom_file_form` General file Open/Save Form for Multiple/Single file selections and custom filter capability

:func:`geosoft.gxapi.GXGUI.show_3d_viewer_dialog` Display a standalone 3D viewer

:func:`geosoft.gxapi.GXIP.set_import_line` Set the line name for some imports.

:func:`geosoft.gxapi.GXMVIEW.delete_group_itr` Deletes existing `GXITR <geosoft.gxapi.GXITR>` associated with a group.

:func:`geosoft.gxapi.GXMVIEW.delete_group_storage` Deletes existing generic storage associated with a group.

:func:`geosoft.gxapi.GXMVIEW.delete_group_tpat` Deletes existing `GXTPAT <geosoft.gxapi.GXTPAT>` associated with a group.

:func:`geosoft.gxapi.GXMVIEW.find_group_by_guid` Find a Group by name.

:func:`geosoft.gxapi.GXMVIEW.get_group_guid` Gets a GUID of a group in the `GXMVIEW <geosoft.gxapi.GXMVIEW>`.

:func:`geosoft.gxapi.GXMVIEW.get_group_itr` Get group `GXITR <geosoft.gxapi.GXITR>`

:func:`geosoft.gxapi.GXMVIEW.get_group_tpat` Get group `GXTPAT <geosoft.gxapi.GXTPAT>`

:func:`geosoft.gxapi.GXMVIEW.get_guid` Gets the GUID of the `GXMVIEW <geosoft.gxapi.GXMVIEW>`.

:func:`geosoft.gxapi.GXMVIEW.get_vector_3d` Get an existing `GXVECTOR3D <geosoft.gxapi.GXVECTOR3D>` object from the view.

:func:`geosoft.gxapi.GXMVIEW.group_itr_exists` Determine if group `GXITR <geosoft.gxapi.GXITR>` exists.

:func:`geosoft.gxapi.GXMVIEW.group_storage_exists` Determine if generic storage associated with a group exists.

:func:`geosoft.gxapi.GXMVIEW.group_tpat_exists` Determine if group `GXTPAT <geosoft.gxapi.GXTPAT>` exists.

:func:`geosoft.gxapi.GXMVIEW.read_group_storage` Reads existing generic storage associated with a group into an in-memory `GXBF <geosoft.gxapi.GXBF>`.

:func:`geosoft.gxapi.GXMVIEW.set_group_itr` Set group `GXITR <geosoft.gxapi.GXITR>`

:func:`geosoft.gxapi.GXMVIEW.set_group_tpat` Set group `GXTPAT <geosoft.gxapi.GXTPAT>`

:func:`geosoft.gxapi.GXMVIEW.write_group_storage` Open generic existing storage associated with a group for reading.

:func:`geosoft.gxapi.GXPG.write_bf_ex` Write the contents of a 2D or 3D pager to a `GXBF <geosoft.gxapi.GXBF>`.

:func:`geosoft.gxapi.GXSYS.display_task_dialog_ui` Show a Windows TaskDialog UI (see https://msdn.microsoft.com/en-us/library/windows/desktop/bb760441(v=vs.85).aspx).

:func:`geosoft.gxapi.GXVECTOR3D.get_itr` Get the `GXITR <geosoft.gxapi.GXITR>` of the `GXVECTOR3D <geosoft.gxapi.GXVECTOR3D>`

:func:`geosoft.gxapi.GXVECTOR3D.set_itr` Set the `GXITR <geosoft.gxapi.GXITR>` of the `GXVECTOR3D <geosoft.gxapi.GXVECTOR3D>`

:func:`geosoft.gxapi.GXVOX.get_multi_voxset_guid` Get the UUID

:func:`geosoft.gxapi.GXVOXD.get_thematic_info` Get a copy of a thematic voxel's `GXTPAT <geosoft.gxapi.GXTPAT>` object and a `GXVV <geosoft.gxapi.GXVV>` containing the current display selections.

:func:`geosoft.gxapi.GXVOXD.is_thematic` Is this a thematic voxel?

:func:`geosoft.gxapi.GXVOXD.set_thematic_selection` Get a copy of a thematic voxel's `GXTPAT <geosoft.gxapi.GXTPAT>` object and a `GXVV <geosoft.gxapi.GXVV>` containing the current display selections.


  
Version 9.2
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GX3DV.from_map` Get an `GX3DV <geosoft.gxapi.GX3DV>` from `GXMAP <geosoft.gxapi.GXMAP>` handle (e.g. from `GXEMAP.lock <geosoft.gxapi.GXEMAP.lock>` on open geosoft_3dv document in project)

:func:`geosoft.gxapi.GXEDB.get_cur_point` Returns the coordinates of the currently selected point in the database (first value if range selected)

:func:`geosoft.gxapi.GXEMAP.packed_files` The number of packed files in the map.

:func:`geosoft.gxapi.GXIP.export_data_to_ubc_3d` Export of `GXIP <geosoft.gxapi.GXIP>` data to UBC 3D `GXIP <geosoft.gxapi.GXIP>` format.

:func:`geosoft.gxapi.GXIP.get_electrode_locations_and_mask_values2` Get unique electrodes, along with current mask info.

:func:`geosoft.gxapi.GXIP.get_qc_channel` Get the QC channel handle, if it exists.

:func:`geosoft.gxapi.GXIP.set_electrode_mask_values_single_qc_channel` Set unique electrodes, along with current mask info.

:func:`geosoft.gxapi.GXIPJ.set_vcs` Set the Vertical Coordinate System in the `GXIPJ <geosoft.gxapi.GXIPJ>` name string

:func:`geosoft.gxapi.GXMAP.create_linked_3d_view` Create a 3D View in this map that is linked to a `GXMVIEW <geosoft.gxapi.GXMVIEW>` in a 3D View file.

:func:`geosoft.gxapi.GXMVIEW.get_3d_point_of_view` Get 3D point of view (values are will be `rDUMMY <geosoft.gxapi.rDUMMY>` if view for 2D views)

:func:`geosoft.gxapi.GXMVIEW.get_aggregate` Get an existing Aggregate object from the view.

:func:`geosoft.gxapi.GXMVIEW.get_col_symbol` Get an existing colored symbol object from the view.

:func:`geosoft.gxapi.GXMVIEW.get_datalinkd` Get an existing Data Link Display (`GXDATALINKD <geosoft.gxapi.GXDATALINKD>`) object from the view.

:func:`geosoft.gxapi.GXMVIEW.set_3d_point_of_view` Set 3D point of view (no effect on 2D views)

:func:`geosoft.gxapi.GXPROJ.current_document_of_type` Get the name of a loaded document of a specific type.

:func:`geosoft.gxapi.GXPROJ.current_document` Get the name and type of the loaded document with focus.

:func:`geosoft.gxapi.GXPROJ.list_loaded_documents` Fills a `GXVV <geosoft.gxapi.GXVV>` with loaded documents of a certain type.

:func:`geosoft.gxapi.GXSYS.log_script_run` This method logs that a script was run

:func:`geosoft.gxapi.GXTEST.core_class` Generic Class Test Wrapper


  
Version 9.1
-----------------

New Classes
^^^^^^^^^^^

:exc:`geosoft.gxapi.GXAPIError` A subclass of `RuntimeError <https://docs.python.org/3/library/exceptions.html#RuntimeError>`_ which is raised whenever

:exc:`geosoft.gxapi.GXCancel` A subclass of `SystemExit <https://docs.python.org/3/library/exceptions.html#SystemExit>`_ which is raised when a

:exc:`geosoft.gxapi.GXError` A subclass of `RuntimeError <https://docs.python.org/3/library/exceptions.html#RuntimeError>`_ which is raised whenever

:exc:`geosoft.gxapi.GXExit` A subclass of `SystemExit <https://docs.python.org/3/library/exceptions.html#SystemExit>`_ which is raised when a


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXContext.clear_ui_console` Clears the console owned by UI applications. Has no effect on consoles owning standalone scripts.

:func:`geosoft.gxapi.GXContext.create` Creates the GX execution context (will return the current one if it exists).

:func:`geosoft.gxapi.GXContext.enable_application_windows` Used by to prevent user interaction while showing modal windows with APIs where it might be hard to use proper window parenting

:func:`geosoft.gxapi.GXContext.get_active_wnd_id` Get currently active window (main window, floating document or other popup, 0 if not available).

:func:`geosoft.gxapi.GXContext.get_main_wnd_id` Get the main window handle (0 if not available).

:func:`geosoft.gxapi.GXContext.has_ui_console` Checks if a console owned by UI applications is available

:func:`geosoft.gxapi.GXContext.is_ui_console_visible` Checks if a console owned by UI applications is visible

:func:`geosoft.gxapi.GXContext.show_ui_console` Shows or hides console owned by UI applications. Showing the console Will also bring the window to the front if behind

:func:`geosoft.gxapi.GXDB.valid_symb` This method checks to see if the specified symbol is a valid symbol in the database.

:func:`geosoft.gxapi.GXDH.plot_symbols_3d` Plot 3D symbols to an existing 3D map view.

:func:`geosoft.gxapi.GXDU.get_xyz_num_fields` Get the number of fields in the XYZ file.

:func:`geosoft.gxapi.GXDU.import_bin4` Same as `import_bin2 <geosoft.gxapi.GXDU.import_bin2>` but with an import mode

:func:`geosoft.gxapi.GXDU.table_selected_lines_fid` Place a Line/Fid information into a Channel for the selected lines in the database.

:func:`geosoft.gxapi.GXEMAP.draw_rect_3d` Plot a square symbol on a section view.

:func:`geosoft.gxapi.GXEMAP.get_point_3d` Returns the coordinates of a user selected point.

:func:`geosoft.gxapi.GXEMAP.get_view_ipj` Get a view's `GXIPJ <geosoft.gxapi.GXIPJ>`.

:func:`geosoft.gxapi.GXIPGUI.launch_offset_ipqc_tool` Launch the Offset `GXIP <geosoft.gxapi.GXIP>` QC tool on a database.

:func:`geosoft.gxapi.GXMVIEW.get_3d_group_flags` Get a 3D geometry group's 3D rendering flags.

:func:`geosoft.gxapi.GXMVIEW.set_3d_group_flags` Set a 3D geometry group's 3D rendering flags.

:func:`geosoft.gxapi.GXSYS.filter_parm_group` Controls filtering of specific group during logging.


  
Version 9.0
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDATALINKD.create_arc_lyr_ex` Create an `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` object from a ArcGIS LYR file

:func:`geosoft.gxapi.GXDATALINKD.create_arc_lyr_from_tmp_ex` Create an `GXDATALINKD <geosoft.gxapi.GXDATALINKD>` object from a temporary ArcGIS LYR file

:func:`geosoft.gxapi.GXDB.get_line_selection` Get the selection status for a line.

:func:`geosoft.gxapi.GXDB.set_line_selection` Set the selection status for a line.

:func:`geosoft.gxapi.GXDBWRITE.add_block` Add the current block of data.

:func:`geosoft.gxapi.GXDBWRITE.add_channel` Add a data channel to the `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object.

:func:`geosoft.gxapi.GXDBWRITE.commit` Commit remaining data to the database.

:func:`geosoft.gxapi.GXDBWRITE.create_xy` Create a `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object for a XY-located data. Add channels using the

:func:`geosoft.gxapi.GXDBWRITE.create_xyz` Create a `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object for a XYZ-located data.

:func:`geosoft.gxapi.GXDBWRITE.create` Create a `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object

:func:`geosoft.gxapi.GXDBWRITE.get_chan_array_size` Get the number of columns of data in a channel.

:func:`geosoft.gxapi.GXDBWRITE.get_db` Get the output `GXDB <geosoft.gxapi.GXDB>` handle from the `GXDBWRITE <geosoft.gxapi.GXDBWRITE>` object.

:func:`geosoft.gxapi.GXDBWRITE.get_v_vx` Get the X channel `GXVV <geosoft.gxapi.GXVV>` handle.

:func:`geosoft.gxapi.GXDBWRITE.get_v_vy` Get the Y channel `GXVV <geosoft.gxapi.GXVV>` handle.

:func:`geosoft.gxapi.GXDBWRITE.get_v_vz` Get the Z channel `GXVV <geosoft.gxapi.GXVV>` handle.

:func:`geosoft.gxapi.GXDBWRITE.get_va` Get the `GXVA <geosoft.gxapi.GXVA>` handle for an array channel.

:func:`geosoft.gxapi.GXDBWRITE.get_vv` Get the `GXVV <geosoft.gxapi.GXVV>` handle for a channel.

:func:`geosoft.gxapi.GXDBWRITE.test_func` Temporary test function.

:func:`geosoft.gxapi.GXDU.split_line_by_direction2` The same as SplitLineByDirection, but with the option to maintain line types when outputting sequentially numbered lines.

:func:`geosoft.gxapi.GXDU.split_line_xy3` Break up a line based on tolerance of lateral and horizontal distance, with

:func:`geosoft.gxapi.GXEDB.current_no_activate` This method returns the Current Edited Database.

:func:`geosoft.gxapi.GXEDB.get_window_position` Get the map window's position and dock state

:func:`geosoft.gxapi.GXEDB.set_window_position` Get the map window's position and dock state

:func:`geosoft.gxapi.GXEDOC.current_no_activate` This method returns the Current Edited Document.

:func:`geosoft.gxapi.GXEDOC.get_window_position` Get the map window's position and dock state

:func:`geosoft.gxapi.GXEDOC.load_no_activate` Loads a list of documents into the workspace

:func:`geosoft.gxapi.GXEDOC.set_window_position` Get the map window's position and dock state

:func:`geosoft.gxapi.GXEMAP.current_no_activate` This method returns the Current Edited map.

:func:`geosoft.gxapi.GXEMAP.digitize_peaks` Digitise points from the current map and place in VVs.

:func:`geosoft.gxapi.GXEMAP.get_window_position` Get the map window's position and dock state

:func:`geosoft.gxapi.GXEMAP.reload_grid` Reloads a grid document.

:func:`geosoft.gxapi.GXEMAP.set_window_position` Get the map window's position and dock state

:func:`geosoft.gxapi.GXEMAPTEMPLATE.current_no_activate` This method returns the Current Edited map template.

:func:`geosoft.gxapi.GXEMAPTEMPLATE.get_window_position` Get the map window's position and dock state

:func:`geosoft.gxapi.GXEMAPTEMPLATE.set_window_position` Get the map window's position and dock state

:func:`geosoft.gxapi.GXEUL3.ex_euler_calc` Does the exeuler depth calculations

:func:`geosoft.gxapi.GXEUL3.ex_euler_derive` Calculates gradients

:func:`geosoft.gxapi.GXGUI.coord_sys_wizard_grid` Launch the coordinate system definition/display `GXGUI <geosoft.gxapi.GXGUI>`.

:func:`geosoft.gxapi.GXGUI.get_client_window_area` Get the location of the Oasis montaj client window.

:func:`geosoft.gxapi.GXGUI.get_window_position` Get the Oasis montaj window's position state

:func:`geosoft.gxapi.GXGUI.get_window_state` Retrieve the current state of the Oasis montaj window

:func:`geosoft.gxapi.GXGUI.launch_geo_dotnetx_tool_ex` Launch a user created .Net GEOXTOOL.

:func:`geosoft.gxapi.GXGUI.launch_geo_x_tool_ex` Launch a user created GEOXTOOL.

:func:`geosoft.gxapi.GXGUI.launch_single_geo_dotnetx_tool_ex` Launch a user created .Net GEOXTOOL ensuring a single instance.

:func:`geosoft.gxapi.GXGUI.set_window_position` Get the Oasis montaj window's position and state

:func:`geosoft.gxapi.GXGUI.set_window_state` Changes the state of the Oasis montaj window

:func:`geosoft.gxapi.GXIMU.get_z_peaks_vv` Same as `get_zvv <geosoft.gxapi.GXIMU.get_zvv>`, but find the closest peak value to the input locations, and return

:func:`geosoft.gxapi.GXIP.get_electrode_locations_and_mask_values` Get unique electrodes, along with current mask info.

:func:`geosoft.gxapi.GXIP.set_electrode_mask_values` Set unique electrodes, along with current mask info.

:func:`geosoft.gxapi.GXIPJ.reproject_section_grid` Reproject a section grid

:func:`geosoft.gxapi.GXIPJ.set_3d_view_from_axes` Set 3D orientation parameters

:func:`geosoft.gxapi.GXLPT.get_standard_lst` Copies the six standard line types into a `GXLST <geosoft.gxapi.GXLST>` object.

:func:`geosoft.gxapi.GXMVIEW.is_projection_empty` Returns 1 if the view projection and view user projection are both empty (undefined).

:func:`geosoft.gxapi.GXMXD.convert_to_map` Create Geosoft map from ArcGIS `GXMXD <geosoft.gxapi.GXMXD>`

:func:`geosoft.gxapi.GXSYS.check_arc_license_ex` Check to see if a ESRI ArcEngine or ArcView license is available, returns type and version of available engine.

:func:`geosoft.gxapi.GXSYS.decrypt_string` Decrypts a string that has been previously encrypted by `encrypt_string <geosoft.gxapi.GXSYS.encrypt_string>`.

:func:`geosoft.gxapi.GXSYS.encrypt_string` Encrypts a string for secure storage in configuration files

:func:`geosoft.gxapi.GXSYS.get_entitlement_rights` Get the Entitlement Rights

:func:`geosoft.gxapi.GXSYS.get_loaded_menus` Get the loaded menus.

:func:`geosoft.gxapi.GXSYS.is_encrypted_string` Checks whether the specified string was encrypted by `encrypt_string <geosoft.gxapi.GXSYS.encrypt_string>`.

:func:`geosoft.gxapi.GXSYS.set_loaded_menus` Load a list of menus

:func:`geosoft.gxapi.GXVVU.offset_correct_xyz` Correct locations based on heading and fixed offset.

:func:`geosoft.gxapi.GXVVU.tokenize_to_values` Tokenize a string based on any characters.


  
Version 8.5
-----------------


New Functions
^^^^^^^^^^^^^

:func:`geosoft.gxapi.GXDBREAD.add_channel` Add a data channel to the `GXDBREAD <geosoft.gxapi.GXDBREAD>` object.

:func:`geosoft.gxapi.GXDBREAD.create_xy` Create a `GXDBREAD <geosoft.gxapi.GXDBREAD>` object for a XY-located data. Add channels using the

:func:`geosoft.gxapi.GXDBREAD.create_xyz` Create a `GXDBREAD <geosoft.gxapi.GXDBREAD>` object for a XYZ-located data.

:func:`geosoft.gxapi.GXDBREAD.create` Create a `GXDBREAD <geosoft.gxapi.GXDBREAD>` object

:func:`geosoft.gxapi.GXDBREAD.get_chan_array_size` Get the number of columns of data in a channel.

:func:`geosoft.gxapi.GXDBREAD.get_next_block` Get the next block of data.

:func:`geosoft.gxapi.GXDBREAD.get_number_of_blocks_to_process` Get the number of blocks to be served up.

:func:`geosoft.gxapi.GXDBREAD.get_v_vx` Get the X channel `GXVV <geosoft.gxapi.GXVV>` handle.

:func:`geosoft.gxapi.GXDBREAD.get_v_vy` Get the Y channel `GXVV <geosoft.gxapi.GXVV>` handle.

:func:`geosoft.gxapi.GXDBREAD.get_v_vz` Get the Z channel `GXVV <geosoft.gxapi.GXVV>` handle.

:func:`geosoft.gxapi.GXDBREAD.get_va` Get the `GXVA <geosoft.gxapi.GXVA>` handle for an array channel.

:func:`geosoft.gxapi.GXDBREAD.get_vv` Get the `GXVV <geosoft.gxapi.GXVV>` handle for a channel.

:func:`geosoft.gxapi.GXDU.import_io_gas` Import data columns from an ioGAS data file.

:func:`geosoft.gxapi.GXDU.range_xy` Find the range of X, and Y in the selected lines.

:func:`geosoft.gxapi.GXDU.range_xyz` Find the range of X, Y and Z in selected lines.

:func:`geosoft.gxapi.GXDU.split_line_by_direction` The line is split when the heading (calculated from the current X and Y channels) changes by more than a specified amount over

:func:`geosoft.gxapi.GXFFT.rc_filter` RC filter

:func:`geosoft.gxapi.GXGU.gravity_still_reading_correction` Gravity Still Reading Correction on selected lines.

:func:`geosoft.gxapi.GXIPJ.get_3d_matrix_orientation` Gets the coefficients of a 3D matrix orientation.

:func:`geosoft.gxapi.GXIPJ.set_3d_matrix_orientation` Apply a 3D orientation directly using matrix coefficients.

:func:`geosoft.gxapi.GXMVIEW.hide_shadow_2d_interpretations` Hide/Show 2d shadow interpretations.

:func:`geosoft.gxapi.GXMVU.generate_surface_from_voxel` TODO...

:func:`geosoft.gxapi.GXPDF3D.export_2d` Export a 2D map to a PDF file.

:func:`geosoft.gxapi.GXPROJ.add_document_without_opening` Adds (and opens) a document file in the current project.

:func:`geosoft.gxapi.GXSURFACE.get_extents` Get the spatial range of all surface items.

:func:`geosoft.gxapi.GXSURFACEITEM.compute_extended_info` Compute more information (including validation) about of all mesh components in the surface item.

:func:`geosoft.gxapi.GXSURFACEITEM.get_extents` Get the spatial range of the the surface item.

:func:`geosoft.gxapi.GXSURFACEITEM.get_geometry_info` Get the total number of vertices and triangles of all mesh components in item.

:func:`geosoft.gxapi.GXSURFACEITEM.get_info` Gets information about the surface item.

:func:`geosoft.gxapi.GXSURFACEITEM.get_properties_ex` Gets the properties of the surface item  (includes new properties introduced in 8.5).

:func:`geosoft.gxapi.GXSURFACEITEM.set_properties_ex` Sets the properties of the surface item (includes new properties introduced in 8.5).

:func:`geosoft.gxapi.GXVOX.add_generate_by_subset_pg` Add a subset 3D  pagers. These should be "slabs", 16 wide in the input direction, and the size of the

:func:`geosoft.gxapi.GXVOX.end_generate_by_subset_pg` Output the voxel, after adding all the subset PGs.

:func:`geosoft.gxapi.GXVOX.export_seg_y` Export a voxel to a depth SEG-Y file

:func:`geosoft.gxapi.GXVOX.generate_vector_voxel_from_db` Generate a vector voxel `GXVOX <geosoft.gxapi.GXVOX>` from a Database

:func:`geosoft.gxapi.GXVOX.init_generate_by_subset_pg` Initialize the generate of a `GXVOX <geosoft.gxapi.GXVOX>` from a series of 3D subset pagers

:func:`geosoft.gxapi.GXVOX.tin_grid_db` `tin_grid_db <geosoft.gxapi.GXVOX.tin_grid_db>`   `GXTIN <geosoft.gxapi.GXTIN>`-Gridding, `GXDB <geosoft.gxapi.GXDB>` version, 3D.


