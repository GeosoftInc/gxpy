import geosoft.gxapi as gxapi	# gxapi methods
import geosoft.gxpy as gxpy		# gxpy methods

def rungx():																# a python script must have a rungx(), which is executed by OM when the script is run
    gxp = gxpy.gx.GXpy()													# get the current gx context
    gxapi.GXSYS.display_message("GX Python", "Hello {}".format(gxp.gid))	# say hello to the user identified by gxp.gid.