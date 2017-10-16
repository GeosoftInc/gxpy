import numpy as np
import geosoft.gxpy.gx as gx
import geosoft.gxpy.grid as gxgrid

# create context
gxc = gx.GXpy()

# open the grid
with gxgrid.Grid.open('elevation_surfer.grd(SRF;VER=V7)') as grid:

    # get the data in a numpy array
    data_values = grid.xyzv()[:, :, 3]

# print statistical properties
print('minimum: ', np.nanmin(data_values))
print('maximum: ', np.nanmax(data_values))
print('mean: ', np.nanmean(data_values))
print('standard deviation:', np.nanstd(data_values))
