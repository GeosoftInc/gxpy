import geosoft.gxpy as gxpy
gxc = gxpy.gx.GXpy()
grid = gxpy.grid.Grid.open('elevation_surfer.grd(SRF;VER=V7)')
for x, y, z, v in grid:
    if v != grid.dummy_value:
        print(x, y, z, v)
