# This sample stand-alone Python script shows a minimal use of the Pythonic gxpy module to
# create a Geosoft context and say hello to the user.

# comment-out following 2 lines to support remote debugging
#import pydevd
#pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

import geosoft.gxpy as gxpy   # gxpy methods

# running as an extension from Oasis montaj will execute rungx()
def rungx():

    # say hello to the user identified by gxp.gid.
    gxapi.GXSYS.display_message("GX Python", "Hello world")

# running as stand-alone program
if __name__ == "__main__":

    # Stand-alone programs must create a GX context before calling any Geosoft methods.
    gxc = gxpy.gx.GXpy()

    # The context has a member 'gid' which contains the user's Geosoft ID.
    # Say hello to the user
    print("Hello world")