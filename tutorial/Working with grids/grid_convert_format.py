import geosoft.gxpy.gx as gx
import geosoft.gxpy.grid as gxgrid

# create context
gxc = gx.GXpy()

# open grid
<<<<<<< HEAD
grid_surfer = gxgrid.Grid.open('elevation_surfer.grd(SRF;VER=V7)')

# copy the grid to an ER Mapper format grid file
grid_erm = gxgrid.Grid.copy(grid_surfer, 'elevation.ers(ERM)', overwrite=True)

exit()
=======
grid_geosoft = gxgrid.open('elevation.grd(GRD)')

# copy the grid to a Grid eXchange File
grid_gxf = gxgrid.copy(grid_geosoft, 'elevation.gxf(GXF)', overwrite=True)

pass
>>>>>>> Added tutorial exercise files and sample datasets
