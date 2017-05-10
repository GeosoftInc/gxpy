#!python3.3
'''
Add a constant value to a channel on all selected lines.

This is a sample Python program that illustrates how to connect to the GX
developer environment from a stand-alone program.

Follwoing are the basic steps:

   1. Get (create) a GX Object handle.
   2. Collect command-line parameters
   3. Open the database
   4. Process the data
'''

import os
import sys
import argparse as argp
import geosoft.gxpy as gxpy

def rungx():
    raise Exception("This is not an extension.  Please use a python interpreter.")

def process_database(db, channel_name, add_value):
    '''
    Process all selected lines in a database by adding a constant
    value to a channel. The data is processed in-place.
    '''

    # work through the data a line at a time - get a list of selected lines
    print('Processing selected lines...')
    lines = db.list_lines()

    # for each line, get the data, add a value, return the data to the line
    for l in lines:

        # print to the console to reflect progress
        print('line {}...'.format(str(l)))

        # get the data and determine the dummy to the data type
        data, ch, fid = db.read_line(l, channels=channel_name)
        dummy = gxpy.utility.gx_dummy(data.dtype)

        # make a dummy mask so we can replace dummies after processing
        dMask = gxpy.utility.dummy_mask(data)

        # process - add the value, then replace the dummies
        sum = data + add_value
        sum[dMask] = dummy

        # write the data back to the database
        db.write_channel(l, channel_name, sum, fid)


if __name__ == "__main__":

    gxpy.utility.check_version('9.2')

    # get (create) a GX context
    with gxpy.gx.GXpy() as gxp:  # get the current gx context

        # The GX_GEOSOFT_BIN_PATH Environment variable should contain a path with geodist.dll
        print("GX_GEOSOFT_BIN_PATH: {}".format(os.getenv("GX_GEOSOFT_BIN_PATH")))
        print('Working directory: ' + os.path.abspath(os.curdir))
        print('User: {}'.format(gxp.gid))

        # get command line parameters
        parser = argp.ArgumentParser(description="Add a constant to a Geosoft database channel")
        parser.add_argument("sDB", help="Geosoft database")
        parser.add_argument("sCh", help="channel to process")
        parser.add_argument("-v",
                            "--value",
                            type=float,
                            default=1.0,
                            help="value to add, default is 1.0")
        args = parser.parse_args()

        # echo parameters
        print("\nDatabase = "+args.sDB)
        print("Channel = "+args.sCh)
        print("Value to add = {}\n".format(args.value))

        # open the database
        with gxpy.gdb.Geosoft_gdb.open(args.sDB) as db:

            # process the data
            process_database(db, args.sCh, args.value)
