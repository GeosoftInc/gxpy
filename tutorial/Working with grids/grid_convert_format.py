import geosoft.gxpy.gx as gx
import geosoft.gxpy.grid as gxgrid

# create context
gxc = gx.GXpy()

# open grid
grid_geosoft = gxgrid.open('elevation.grd(GRD)')

# copy the grid to a Grid eXchange File
grid_gxf = gxgrid.copy(grid_geosoft, 'elevation.gxf(GXF)', overwrite=True)

pass