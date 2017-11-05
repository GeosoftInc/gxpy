import geosoft.gxpy.gx as gx
import geosoft.gxpy.view as gxview
import geosoft.gxpy.group as gxgroup
import geosoft.gxpy.agg as gxagg
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.viewer as gxviewer

gxc = gx.GXpy()

grid_file = 'Wittichica Creek Residual Total Field.grd'

# create a 3D view
with gxview.View_3d.new("TMI in relief",
                        area_2d=gxgrd.Grid.open(grid_file).extent_2d(),
                        coordinate_system=gxgrd.Grid.open(grid_file).coordinate_system,
                        overwrite=True) as v:

    v3d_name = v.file_name

    # use the data grid as the relief surface
    v.set_plane_relief_surface(grid_file)

    # add the grid image to the view, with shading, 20 nT contour interval to match default contour lines
    gxgroup.Aggregate_group.new(v, gxagg.Aggregate_image.new(grid_file, shade=True, contour=20))

    # contour the grid
    gxgroup.contour(v, 'TMI_contour', grid_file)


# display the map in a Geosoft viewer
gxviewer.view_document(v3d_name, wait_for_close=False)
