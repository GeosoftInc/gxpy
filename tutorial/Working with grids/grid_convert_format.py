import geosoft.gxpy.gx as gx
import geosoft.gxpy.grid as gxgrid

# create context
gxc = gx.GXpy()

# open grid
grid_surfer = gxgrid.Grid.open('elevation_surfer.grd(SRF;VER=V7)')

# copy the grid to an ER Mapper format grid file
grid_erm = gxgrid.Grid.copy(grid_surfer, 'elevation.ers(ERM)', overwrite=True)

exit()
