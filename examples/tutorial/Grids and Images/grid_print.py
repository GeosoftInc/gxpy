#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import geosoft.gxpy as gxpy
gxc = gxpy.gx.GXpy()
with gxpy.grid.Grid.open('elevation_surfer.grd(SRF;VER=V7)') as grid:
    print('coordinate_system: ', grid.coordinate_system)
    for x, y, z, v in grid:
        if v is not None:
            print(x, y, z, v)
