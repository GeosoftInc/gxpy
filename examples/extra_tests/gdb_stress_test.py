#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import os
import sys
import geosoft.gxpy.gx as gx
import geosoft.gxpy.gdb as gxdb

gxc = gx.GXpy()
try:
    dir = sys.argv[1]
except IndexError:
    print('folder path that contains one or more test databases is required as a single command line parameter')
    exit()
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