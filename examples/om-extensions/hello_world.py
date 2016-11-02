# Oasis montaj Python extension to say Hello.
# To run this extension, select "Settings / Run GX or Python...", then browse to this script file.

import geosoft.gxapi as gxapi
import geosoft.gxpy as gxpy

# a python script must have a rungx(), which is executed by OM when the script is run
def rungx():

    # get the current gx context, normally not required but in this example we want the gid.
    gxp = gxpy.gx.GXpy()
    
    # say hello to the user identified by gxp.gid.
    gxapi.GXSYS.display_message("GX Python", "Hello {}".format(gxp.gid))