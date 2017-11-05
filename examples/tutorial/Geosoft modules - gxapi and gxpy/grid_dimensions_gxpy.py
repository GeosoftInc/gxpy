import geosoft.gxpy as gxpy

gxc = gxpy.gx.GXpy()
grid = gxpy.grid.Grid.open('test.grd(GRD)')
print(' dimension (nx, ny): ({}, {})'.format(grid.nx, grid.ny),
      '\n separation (x, y): ({}, {})'.format(grid.dx, grid.dy),
      '\n origin (x, y): ({}, {})'.format(grid.x0, grid.y0),
      '\n rotation: {}'.format(grid.rot))
