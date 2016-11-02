# Oasis montaj Python extension to say Hello.import geosoft.gxapi as gxapi # gxapi methods
# To run this extension, select "Settings / Run GX or Python...", then browse to this script file.

# comment-out following 2 lines to support remote debugging
import pydevd
pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import geosoft.gxapi as gxapi
import geosoft.gxpy as gxpy

# a python script must have a rungx(), which is executed by OM when the script is run
def rungx():

    # get the current gx context, normally not required but in this example we want the gid.
    gxp = gxpy.gx.GXpy()
    
    # say hello to the user identified by gxp.gid.
    gxapi.GXSYS.display_message("GX Python", "Hello {}".format(gxp.gid))