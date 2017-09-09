import numpy as np
import geosoft.gxpy as gxpy
import geosoft.gxpy.gdb as gxdb
import geosoft.gxapi as gxapi

#create context
gxc = gxpy.gx.GXpy()

# Open csv-format data file and skip the first line, which is a comment line
f = open('mag_data.csv', 'r')
f.readline()

# the second line contains the channel/field names, from which we create a list of channel names
channel_names = f.readline().strip().split(',')

#the rest of the file contains data, which we load into a numpy float array
data = np.loadtxt(f, delimiter=',')

#create a new database from list of channels and numpy data. All data is stored in a single line.
gdb = gxdb.Geosoft_gdb.new('mag_data', overwrite=True)
line_name = gxdb.create_line_name()
gdb.write_line(line_name, data, channel_names)

# set the coordinate system to 'NAD 83 / UTM zone 15N'
gdb.coordinate_system = 'NAD83 / UTM zone 15N'

print(gdb.list_lines())     # {'L0': 100020}
print(gdb.list_channels())  # {'mag': 100523, 'X': 100520, 'Y': 100521, 'Z': 100522}
print(gdb.xyz_channels)     # ('X', 'Y', 'Z')

exit()
