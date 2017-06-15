import geosoft.gxpy as gxpy
import geosoft.gxapi as gxapi

gxc = gxpy.gx.GXpy()
grid = gxpy.grid.Grid.open('test.grd(GRD)')

cr = grid.gximg.query_double(gxapi.IMG_QUERY_rCOMPRESSION_RATIO)

print('compression ratio: {}'.format(cr))