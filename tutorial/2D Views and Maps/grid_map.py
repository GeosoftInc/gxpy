import geosoft.gxpy.gx as gx
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.view as gxview
import geosoft.gxpy.group as gxgroup
import geosoft.gxpy.agg as gxagg
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.viewer as gxviewer

gxc = gx.GXpy()

# create a map from the grid coordinate system and extent
with gxgrd.Grid('Wittichica Creek Residual Total Field.grd') as grd:
    grid_file_name = grd.file_name_decorated

    # create a map for this grid on A4 media, scale to fit the extent
    with gxmap.Map.new('Wittichica residual TMI',
                       data_area=grd.extent_2d(),
                       media="A4",
                       margins=(1, 3.5, 3, 1),
                       coordinate_system=grd.coordinate_system,
                       overwrite=True) as gmap:
        map_file_name = gmap.file_name

# draw into the views on the map. We are reopening the map as the Aggregate class only works with a closed grid.
with gxmap.Map.open(map_file_name) as gmap:

    # work with the data view
    with gxview.View.open(gmap, "data") as v:

        # add the grid image to the view
        with gxagg.Aggregate_image.new(grid_file_name) as agg:
            gxgroup.Aggregate_group.new(v, agg)

# display the map in a Geosoft viewer
gxviewer.view_document(map_file_name, wait_for_close=False)
