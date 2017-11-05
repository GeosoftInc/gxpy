import geosoft.gxapi as gxapi
import geosoft.gxpy as gxpy

def rungx():

    gxapi.GXSYS.display_message("GX Python", "Hello {}".format(gxpy.gx.GXpy().gid))

if __name__ == "__main__":
    print('Hello {}'.format(gxpy.gx.GXpy().gid))