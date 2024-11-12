#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import geosoft.gxpy as gxpy
import geosoft.gxpy.gdb as gxdb
import geosoft.gxapi as gxapi

gxc = gxpy.gx.GXpy()

# open the database, best practice is to use a 'with ...' construct
with gxdb.Geosoft_gdb.open('mag_data_split') as gdb:

    # make a new channel for the output, duplicate properties of 'mag' channel
    new_mag_channel = gxdb.Channel.new(gdb, 'mag_base', dup='mag', replace=True)

    # work through each line
    for line in gdb.list_lines():

        print ('processing line {}'.format(line))

        # read data from the line.
        # The read_channel method returns the data in a geosoft VV
        mag_data = gdb.read_channel_vv(line, 'mag')

        # use Geosoft GXVVU.translate function to subtract 5000.
        gxapi.GXVVU.translate(mag_data.gxvv, -5000, 1)
        gdb.write_channel_vv(line, new_mag_channel, mag_data)

exit()
