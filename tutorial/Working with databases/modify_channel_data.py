import geosoft.gxpy as gxpy
import geosoft.gxpy.gdb as gxdb

#create context, open the database
gxc = gxpy.gx.GXpy()

# open the database, best practice is to use a 'with ...' construct
with gxdb.Geosoft_gdb.open('mag_data_split') as gdb:

    # make a new channel for the output, duplicate properties of 'mag' channel
    new_mag_channel = gxdb.Channel.new(gdb, 'mag_base', dup='mag', replace=True)

    # work through each line
    for line in gdb.list_lines():

        print ('processing line {}'.format(line))

        # read data from the line.
        # The read_channel method returns the data as a numpy array, and the fiducial
        mag_data, fid = gdb.read_channel(line, 'mag')
        mag_data = mag_data - 5000
        gdb.write_channel(line, new_mag_channel, mag_data, fid)

exit()
