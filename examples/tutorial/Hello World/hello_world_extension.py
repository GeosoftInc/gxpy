#  Copyright (c) 2024 Bentley Systems, Incorporated. All rights reserved.
import geosoft.gxapi as gxapi
import geosoft.gxpy as gxpy

# a python script must have a rungx(), which is executed by OM when the script is run
def rungx():

    # get the current gx context
    gxp = gxpy.gx.gx()

    # say hello to the user identified by gxp.gid.
    gxapi.GXSYS.display_message("GX Python", "Hello {}".format(gxp.gid))
