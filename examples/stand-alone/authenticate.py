import geosoft.gxapi as gxapi
ctx = gxapi.GXContext.create('ian', '0.0', 0, 0)
user = gxapi.str_ref()
company = gxapi.str_ref()
gxapi.GXSYS.get_licensed_user(user, company)

try:
    gxapi.GXST2.create()
    print(user.value, 'is licenced.')
except gxapi.GXAPIError:
    print(user.value, 'is NOT licenced.')
