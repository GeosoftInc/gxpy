import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.grid as gxgrid
import geosoft.gxpy.utility as gxu

# this example requires version 9.2.1, which adds iteration support
gxu.check_version('9.2.1b0')

# create context
gxc = gx.GXpy()

# open the grid
grid = gxgrid.Grid.open('elevation_surfer.grd(SRF;VER=V7)')

# create a gxapi.GXST instance to accumulate statistics
stats = gxapi.GXST.create()

# add data from each row to the stats instance
dummy = grid.dummy_value
number_of_dummies = 0
for x, y, z, v in grid:
    if v == dummy:
        number_of_dummies += 1
    else:
        stats.data(v)

# print statistical properties
print('grid file: ', grid)
print('minimum: ', stats.get_info(gxapi.ST_MIN))
print('maximum: ', stats.get_info(gxapi.ST_MAX))
print('mean: ', stats.get_info(gxapi.ST_MEAN))
print('standard deviation:', stats.get_info(gxapi.ST_STDDEV))
print('number of dummies: ', number_of_dummies)
print('number of valid data points: ', (grid.nx * grid.ny) - number_of_dummies)