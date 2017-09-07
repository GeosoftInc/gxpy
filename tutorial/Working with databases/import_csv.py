import numpy as np
import geosoft.gxpy as gxpy
import geosoft.gxpy.gdb as gxgdb

#create context
gxc = gxpy.gx.GXpy()

# Read the data into a numpy array
f = open('mag_data.csv', 'r')

#the first line contains the channel/field names
channel_names = f.readline().strip().split(',')

#the rest of the file contains data
data = np.loadtxt(f, delimiter=',')

#create a new database
gdb = gxgdb.Geosoft_gdb.new('mag_data', overwrite=True)
gdb.write_line('L0', data, channel_names)

exit()