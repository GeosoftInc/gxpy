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
gdb = gxdb.Geosoft_gdb.new('mag_data_split', overwrite=True)
line_name = gxdb.create_line_name()
gdb.write_line(line_name, data, channel_names)

# set the coordinate system to 'NAD 83 / UTM zone 15N'
gdb.coordinate_system = 'NAD83 / UTM zone 15N'

# set the mag data units to 'nT'
gxdb.Channel(gdb, 'mag').unit = 'nT'

print(list(gdb.list_lines()))     # ['L0']
print(list(gdb.list_channels()))  # ['mag', 'X', 'Y', 'Z']
print(gdb.xyz_channels)           # ('X', 'Y', 'Z')

# split the line into sections knowing lines are E-W, and separated by 200 m.
# see https://geosoftinc.github.io/gxpy/9.2/python/GXDU.html?highlight=split_line_xy2#geosoft.gxapi.GXDU.split_line_xy2

# starting line number for split lines
split_line_number_start = gxapi.int_ref()
split_line_number_start.value = 1

# create instances to the lines and channels needed by the split_line_xy2 function
line = gxdb.Line(gdb, 'L0')
x_channel = gxdb.Channel(gdb, 'X')
y_channel = gxdb.Channel(gdb, 'Y')

# lock items as required
line.lock = gxdb.SYMBOL_LOCK_READ
x_channel.lock = gxdb.SYMBOL_LOCK_WRITE
y_channel.lock = gxdb.SYMBOL_LOCK_WRITE

# split the original line into segments, based on a lateral distance tolerance of 100 m.
gxapi.GXDU.split_line_xy2(
    gdb.gxdb,
    line.symbol,
    gxdb.Channel(gdb, 'X').symbol,
    gxdb.Channel(gdb, 'Y').symbol,
    1,
    100.0,
    gxapi.rDUMMY,
    gxapi.DU_SPLITLINE_SEQUENTIAL,
    split_line_number_start,
    1,
    1)

#delete the original line as it is no longer needed
gdb.delete_line('L0')

# print a list of the new lines
print(list(gdb.list_lines()))   # ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', ...

exit()
