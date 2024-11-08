#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.grid as gxgrid

# create context
gxc = gx.GXpy()

# create a gxapi.GXST instance to accumulate statistics
stats = gxapi.GXST.create()

# open the grid
with gxgrid.Grid.open('elevation_surfer.grd(SRF;VER=V7)') as grid:

    # add data from each row to the stats instance
    for row in range(grid.ny):
        stats.data_vv(grid.read_row(row).gxvv)

# print statistical properties
print('minimum: ', stats.get_info(gxapi.ST_MIN))
print('maximum: ', stats.get_info(gxapi.ST_MAX))
print('mean: ', stats.get_info(gxapi.ST_MEAN))
print('standard deviation:', stats.get_info(gxapi.ST_STDDEV))
