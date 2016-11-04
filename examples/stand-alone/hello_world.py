# This sample stand-alone Python script shows a minimal use of the Pythonic gxpy module to
# create a Geosoft context and say hello to the user.
# This example can be run stand-alon or as a Oasis montaj extension.

import geosoft.gxpy as gxpy   # gxpy methods


# running as an extension from Oasis montaj will execute rungx()
def rungx():

    # say hello
    gxpy.utility.display_message("GX Python", "Hello {}".format(gxpy.gx.GXpy().gid))


# running as stand-alone program
if __name__ == "__main__":

    # Stand-alone programs must create a GX context before calling Geosoft methods.
    gxc = gxpy.gx.GXpy()

    # The context has a member 'gid' which contains the user's Geosoft ID.
    # Say hello to the user
    print("Hello {}".format(gxc.gid))
