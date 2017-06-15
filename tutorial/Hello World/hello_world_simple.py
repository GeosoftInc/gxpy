import geosoft.gxpy as gxpy

# a GX context is required, and must be assigned to a variable that persists through the life of execution.
gxc = gxpy.gx.GXpy()

# gid is a property of the context that holds the user's Geosoft ID.  Say hello.
print('Hello {}'.format(gxc.gid))
