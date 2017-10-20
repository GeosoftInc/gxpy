import numpy as np
import os
import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.gx as gx
import geosoft.gxpy.utility as gxu
import geosoft.gxpy.system as gsys
import geosoft.gxpy.gdb as gxdb
import geosoft.gxpy.vv as gxvv
import geosoft.gxpy.va as gxva

gxc = gx.GXpy()
dir = 'g:\\db_stress_test'
max_lines_per_db = 4
for filename in os.listdir(dir):
    if filename.endswith('.gdb'):
        path = os.path.join(dir, filename)
        with gxdb.Geosoft_gdb.open(path) as gdb:
            if 'empty' in filename:
                gdb.delete_line('L0')
            print(gdb.file_name, gdb.list_channels())
            n = 0
            for line in gdb.list_lines():
                data, ch, fid = gdb.read_line(line)
                print(line, data.shape)
                n += 1
                if n >= max_lines_per_db:
                    break