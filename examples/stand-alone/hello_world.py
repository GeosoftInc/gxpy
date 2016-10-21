# This sample stand-alone Python script shows a minimal use of the Pythonic gxpy module to
# create a Geosoft context and say hello to the user.

import geosoft.gxpy as gxpy   # gxpy methods

# Stand-alone programs must create a GX context before calling any Geosoft methods.
gxcontext = gxpy.gx.GXpy()

# The context has a member 'gid' which contains the user's Geosoft ID.
# Say hello to the user
print("Hello {}!".format(gxcontext.gid))