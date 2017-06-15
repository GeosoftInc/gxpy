import geosoft.gxapi as gxapi

gxc = gxapi.GXContext.create(__name__, '0.1')
img = gxapi.GXIMG.create_file(gxapi.GS_FLOAT,
                              'test.grd(GRD)',
                              gxapi.IMG_FILE_READONLY)
x_sep = gxapi.float_ref()
y_sep = gxapi.float_ref()
x_origin = gxapi.float_ref()
y_origin = gxapi.float_ref()
rotation = gxapi.float_ref()
img.get_info(x_sep, y_sep, x_origin, y_origin, rotation)

print(' dimension (nx, ny): ({}, {})'.format(img.nx(), img.ny()),
      '\n separation (x, y): ({}, {})'.format(x_sep.value, y_sep.value),
      '\n origin (x, y): ({}, {})'.format(x_origin.value, y_origin.value),
      '\n rotation: {}'.format(rotation.value))