import geosoft.gxpy.gx as gx
import geosoft.gxpy.view as gxview
import geosoft.gxpy.group as gxgroup
import geosoft.gxpy.agg as gxagg
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.viewer as gxviewer

gxc = gx.GXpy()

tmi_file = 'Wittichica Creek Residual Total Field.grd'
dem_file = 'Wittichica DEM.grd'

# create a 3D view
with gxview.View_3d.new("TMI drapped on DEM",
                        area_2d=gxgrd.Grid.open(tmi_file).extent_2d(),
                        coordinate_system=gxgrd.Grid.open(tmi_file).coordinate_system,
                        scale=5000,
                        overwrite=True) as v:

    v3d_name = v.file_name

    # use the DEM as the relief surface
    v.set_plane_relief_surface(dem_file)
    gxgroup.Aggregate_group.new(v, gxagg.Aggregate_image.new(dem_file,
                                                             color_map='elevation.tbl'))

    # relief plane for the TMI, offset to elevation 2000
    v.new_drawing_plane('TMI relief')
    v.set_plane_relief_surface(tmi_file, base=-4000)
    gxgroup.Aggregate_group.new(v, gxagg.Aggregate_image.new(tmi_file))
    gxgroup.contour(v, 'TMI_contour', tmi_file)

    # add DEM contours on a plane floating beneath the DEM
    v.new_drawing_plane('Scratch plane', offset=(0, 0, -2000))
    gxgroup.contour(v, 'DEM contour', tmi_file)

# display the map in a Geosoft viewer
gxviewer.view_document(v3d_name, wait_for_close=False)
