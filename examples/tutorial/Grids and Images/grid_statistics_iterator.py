#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.grid as gxgrid
import geosoft.gxpy.utility as gxu

# this example requires version 9.2.1, which adds iteration support
gxu.check_version('9.2.1')

# create context
gxc = gx.GXpy()

# create a gxapi.GXST instance to accumulate statistics
stats = gxapi.GXST.create()

# add each data to stats point-by-point (slow, better to use numpy or vector approach)
number_of_dummies = 0
with gxgrid.Grid.open('elevation_surfer.grd(SRF;VER=V7)') as grid:
    for x, y, z, v in grid:
        if v is None:
            number_of_dummies += 1
        else:
            stats.data(v)
    total_points = grid.nx * grid.ny

# print statistical properties
print('minimum: ', stats.get_info(gxapi.ST_MIN))
print('maximum: ', stats.get_info(gxapi.ST_MAX))
print('mean: ', stats.get_info(gxapi.ST_MEAN))
print('standard deviation:', stats.get_info(gxapi.ST_STDDEV))
print('number of dummies: ', number_of_dummies)
print('number of valid data points: ', total_points - number_of_dummies)