import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.grid as gxgrid

# create context
gxc = gx.GXpy()

# open the grid
grid = gxgrid.Grid.open('elevation_surfer.grd(SRF;VER=V7)')

# create a gxapi.GXST instance to accumulate statistics
stats = gxapi.GXST.create()

# add data from each row to the stats instance
for row in range(grid.ny):
    stats.data_vv(grid.read_row(row).gxvv)

# print statistical properties
print('grid file: ', grid)
print('minimum: ', stats.get_info(gxapi.ST_MIN))
print('maximum: ', stats.get_info(gxapi.ST_MAX))
print('mean: ', stats.get_info(gxapi.ST_MEAN))
print('standard deviation:', stats.get_info(gxapi.ST_STDDEV))
