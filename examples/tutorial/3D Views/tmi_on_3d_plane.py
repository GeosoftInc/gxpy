import geosoft.gxpy.gx as gx
import geosoft.gxpy.view as gxview
import geosoft.gxpy.group as gxgroup
import geosoft.gxpy.agg as gxagg
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.viewer as gxviewer

gxc = gx.GXpy()

grid_file = 'Wittichica Creek Residual Total Field.grd'

# create a 3D view
with gxview.View_3d.new("TMI on a plane",
                        area_2d=gxgrd.Grid(grid_file).extent_2d(),
                        coordinate_system=gxgrd.Grid(grid_file).coordinate_system,
                        overwrite=True) as v:

    v3d_name = v.file_name

    # add the grid image to the view, with shading, ands contour
    gxgroup.Aggregate_group.new(v, gxagg.Aggregate_image.new(grid_file, shade=True, contour=20))
    gxgroup.contour(v, 'TMI_contour', grid_file)

# display the map in a Geosoft viewer
gxviewer.view_document(v3d_name, wait_for_close=False)
