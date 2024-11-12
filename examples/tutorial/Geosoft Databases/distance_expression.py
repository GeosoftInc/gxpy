#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import numpy as np
import math
import geosoft.gxpy as gxpy
import geosoft.gxpy.gdb as gxdb

gxc = gxpy.gx.GXpy()

# open the database, best practice is to use a 'with ...' construct
with gxdb.Geosoft_gdb.open('mag_data_split') as gdb:

    # make a distance channel
    dist_channel = gxdb.Channel.new(gdb, 'distance', dup='x', replace=True)

    # work through each line
    for line in gdb.list_lines():

        print ('processing line {}'.format(line))

        # read data from the line, returns in a 2D numpy array.
        xy_data, channels_read, fid = gdb.read_line(line, ('x', 'y'))


        # get the first point (x0, y0)
        x0 = xy_data[0, 0]
        y0 = xy_data[0, 1]

        # FAST - use numpy array math to calculate distance in a 1D array dist_array
        dist_array = np.sqrt((xy_data[:, 0] - x0)**2 + (xy_data[:, 1] - y0)**2)

        # save the distance
        gdb.write_channel(line, dist_channel, dist_array, fid)

exit()
