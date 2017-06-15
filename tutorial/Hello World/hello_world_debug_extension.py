import pydevd
import geosoft.gxapi as gxapi
import geosoft.gxpy as gxpy

def rungx():

    # remote debug, MUST be removed/commented out for production
    # this will break inside a running "Debug Extension" configuration in PyCharm
    pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

    gxc = gxpy.gx.GXpy()
    gxapi.GXSYS.display_message("GX Python", "Hello {}".format(gxc.gid))

if __name__ == "__main__":
    gxc = gxpy.gx.GXpy()
    print('Hello {}'.format(gxc.gid))