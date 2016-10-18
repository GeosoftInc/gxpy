import geosoft.gxapi as gxapi # gxapi methods
import geosoft.gxpy as gxpy   # gxpy methods

# a python script must have a rungx(), which is executed by OM when the script is run
def rungx():
    gxp = gxpy.gx.GXpy() # get the current gx context
    
    # say hello to the user identified by gxp.gid.
    gxapi.GXSYS.display_message("GX Python", "Hello {}".format(gxp.gid))