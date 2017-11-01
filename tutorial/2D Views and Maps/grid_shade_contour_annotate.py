import geosoft.gxpy.gx as gx
import geosoft.gxpy.map as gxmap
import geosoft.gxpy.view as gxview
import geosoft.gxpy.group as gxgroup
import geosoft.gxpy.agg as gxagg
import geosoft.gxpy.grid as gxgrd
import geosoft.gxpy.viewer as gxviewer

gxc = gx.GXpy()

# create a map from grid coordinate system and extent
with gxgrd.Grid('Wittichica Creek Residual Total Field.grd') as grd:
    grid_file_name = grd.file_name_decorated

    # create a map for this grid on A4 media, scale to fit the extent
    with gxmap.Map.new('Wittichica residual TMI',
                       fixed_size=False,
                       data_area=grd.extent_2d(),
                       media="A4",
                       margins=(1, 3.5, 3, 1),
                       coordinate_system=grd.coordinate_system,
                       overwrite=True) as gmap:
        map_file_name = gmap.file_name

# draw into the views on the map. We are reopening the map as the Aggregate class only works with a closed grid.
with gxmap.Map.open(map_file_name) as gmap:

    # add a map surround to the map
    gmap.surround(outer_pen='kt500', inner_pen='kt100', gap=0.1)

    # work with the data view, draw a line around the data view
    with gxview.View(gmap, "data") as v:
        with gxgroup.Draw(v, 'line') as g:
            g.rectangle(v.extent_clip,
                        pen=g.new_pen(line_thick=0.1, line_color='K'))

    # add the grid image to the view
    with gxview.View(gmap, "data") as v:
        with gxagg.Aggregate_image.new(grid_file_name,
                                       contour=20,
                                       shade=True) as agg:
            gxgroup.Aggregate_group.new(v, agg)
            gxgroup.legend_color_bar(v, 'TMI_legend',
                                     title='Res TMI\nnT',
                                     location=(1.2,0),
                                     cmap=agg.layer_color_map(0),
                                     cmap2=agg.layer_color_map(1))
        with gxgroup.Draw(v, 'TMI_contour') as d:
            d.contour(grid_file_name)

    # annotate the data view locations
    gmap.annotate_data_xy(grid=gxmap.GRID_CROSSES)
    gmap.annotate_data_ll(grid=gxmap.GRID_LINES,
                          grid_pen=gxgroup.Pen(line_color='b'),
                          text_def=gxgroup.Text_def(color='b',
                                                    height=0.15,
                                                    italics=True))
    # scale bar
    gmap.scale_bar(location=(1, 3, 1.5),
                   text_def=gxgroup.Text_def(height=0.15))

    # map title
    with gxview.View(gmap, "base") as v:
        with gxgroup.Draw(v, 'title') as g:
            g.text("Tutorial Example\nresidual mag",
                   reference=gxgroup.REF_BOTTOM_CENTER,
                   location=(100, 10),
                   text_def=gxgroup.Text_def(height=3.5,
                                             weight=gxgroup.FONT_WEIGHT_BOLD))
            g.text("created by:" + gxc.gid,
                   location=(1, 1.5),
                   text_def=gxgroup.Text_def(height=1.2,
                                             italics=True))

# display the map in a Geosoft viewer
gxviewer.view_document(map_file_name, wait_for_close=False)

# save to a PNG file
gxmap.save_as_image(map_file_name, "wittichica_mag.png", type=gxmap.RASTER_FORMAT_PNG)