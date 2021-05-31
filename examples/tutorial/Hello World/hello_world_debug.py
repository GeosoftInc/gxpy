import geosoft.gxapi as gxapi
import geosoft.gxpy as gxpy

def rungx():

    gxc = gxpy.gx.gx()
    gxapi.GXSYS.display_message("GX Python", "Hello {}".format(gxc.gid))

if __name__ == "__main__":
    gxc = gxpy.gx.GXpy()
    print('Hello {}'.format(gxc.gid))