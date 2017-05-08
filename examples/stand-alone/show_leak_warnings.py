# This sample stand-alone Python script shows a minimal use of the Pythonic gxpy module to
# create a Geosoft context and say hello to the user.
# This example can be run stand-alon or as a Oasis montaj extension.

import geosoft.gxpy as gxpy   # gxpy methods
import numpy as np
import gc

# running as an extension from Oasis montaj will execute rungx()
def rungx():

    gxpy.utility.check_version('9.1')

    with gxpy.gx.GXpy() as gx:
        # say hello
        gxpy.utility.display_message("GX Python", "Hello {}".format(gx.gid))

# running as stand-alone program

if __name__ == "__main__":

    gxpy.utility.check_version('9.1')

    # Stand-alone programs must create a GX context before calling Geosoft methods.
    gxc_leaked_1 = gxpy.gx.GXpy(log=print)
    gxc_manual_close = gxpy.gx.GXpy()
    with gxpy.gx.GXpy() as gxc:

        with gxpy.grid.Grid.new(properties={'dtype': np.int16,
                                   'nx': 100, 'ny': 50,
                                   'x0': 4, 'y0': 8,
                                   'dx': 0.1, 'dy': 0.2,
                                   'rot': 5,
                                   'coordinate_system': gxpy.coordinate_system.Coordinate_system('NAD27 / UTM zone 18N')}) as grd:
            print("Hello {}".format(grd.coordinate_system))

        grd_leaked = gxpy.grid.Grid.new(properties={'dtype': np.int16,
                                       'nx': 100, 'ny': 50,
                                       'x0': 4, 'y0': 8,
                                       'dx': 0.1, 'dy': 0.2,
                                       'rot': 5,
                                       'coordinate_system': gxpy.coordinate_system.Coordinate_system('NAD27 / UTM zone 18N')})
        # The context has a member 'gid' which contains the user's Geosoft ID.
        # Say hello to the user
        print("Hello {}".format(gxc.gid))
    gxc_manual_close._close()
    gxc_leaked_1 = None
    gc.collect()
    print("Done.")
