# Oasis montaj Python extension to say Hello.
# To run this extension, select "Settings / Run GX or Python...",
# then browse to this script file.

import geosoft.gxpy as gxpy


# a python script must have a rungx()
def rungx():

    gxpy.utility.check_version('9.1')

    # Get the current gx context
    # This is normally not required but in this example we want the gid.
    gxp = gxpy.gx.GXpy()

    # say hello to the user identified by gxp.gid.
    gxpy.utility.display_message("GX Python", "Hello {}".format(gxp.gid))
