#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import geosoft.gxpy.gx as gx
import geosoft.gxpy.grid as gxgrid

# create context
gxc = gx.GXpy()

# open grid
grid_surfer = gxgrid.Grid.open('elevation_surfer.grd(SRF;VER=V7)', mode=gxgrid.FILE_READWRITE)

# define the coordinate system
grid_surfer.coordinate_system = 'GDA94 / UTM zone 54S'

# copy the grid to an ER Mapper format grid file
grid_erm = gxgrid.Grid.copy(grid_surfer, 'elevation.ers(ERM)', overwrite=True)

print(str(grid_erm.coordinate_system))

exit()
