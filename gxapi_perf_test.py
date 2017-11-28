import time


import geosoft.gxapi as gxa
import geosoft.gxapi_old.gxapi as gxo
import geosoft.gxapi.gxapi_cy as gxc

def simple_set_get_doubles_baremetal(dn):
    print("simple_set_get_doubles_baremetal start")
    tstart = time.perf_counter()
    for i in range(0, 1000000):
        xv, yv, zv = dn._get_scale(0, 0, 0)
        dn._set_scale(2.0, 3.0, 4.0)
    elapsed = time.perf_counter() - tstart
    print("simple_set_get_doubles_baremetal end: {}".format(elapsed))

def simple_set_get_doubles(dn, x, y, z):
    print("simple_set_get_doubles start")
    tstart = time.perf_counter()
    for i in range(0, 1000000):
        dn.get_scale(x, y, z)
        dn.set_scale(2.0, 3.0, 4.0)
    elapsed = time.perf_counter() - tstart
    print("simple_set_get_doubles end: {}".format(elapsed))

def simple_set_get_string_baremetal(dn):
    print("simple_set_get_string_baremetal start")
    tstart = time.perf_counter()
    for i in range(0, 1000000):
        s = dn._get_axis_font("".encode())
        dn._set_axis_font("NewFont".encode())
    elapsed = time.perf_counter() - tstart
    print("simple_set_get_string_baremetal end: {}".format(elapsed))

def simple_set_get_string(dn, s):
    print("simple_set_get_string start")
    tstart = time.perf_counter()
    for i in range(0, 1000000):
        dn.get_axis_font(s)
        dn.set_axis_font("NewFont")
    elapsed = time.perf_counter() - tstart
    print("simple_set_get_string end: {}".format(elapsed))

ctx = gxa.GXContext.create("", "")
ctxo = gxo.GXContext.create("", "")
dn = gxa.GX3DN.create()

dno = gxo.GX3DN.create()
x = gxa.float_ref()
y = gxa.float_ref()
z = gxa.float_ref()
s = gxa.str_ref()
xo = gxo.float_ref()
yo = gxo.float_ref()
zo = gxo.float_ref()
so = gxo.str_ref()


print("OldAPI")
simple_set_get_doubles(dno, xo, yo, zo)
simple_set_get_string(dno, so)
print("NewAPI")
simple_set_get_doubles_baremetal(dn)
simple_set_get_doubles(dn, x, y, z)
simple_set_get_string_baremetal(dn)
simple_set_get_string(dn, s)
del dn
del dno
del ctxo
del ctx