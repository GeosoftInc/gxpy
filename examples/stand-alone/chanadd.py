#!python3.3
'''
Add a constant value to a channel on all selected lines.

This is a sample Python program that illustrates how to connect to the GX
developer environment from a stand-alone program.  In this case, there
the following basic steps:

   1. Get (create) a GX Object handle.

   2. Open existing database

   3. Save the list of database channels to a file

   4. Get the channel data

   5. Increase the data by a given amount

   6. Save the changed data back to the channel
'''
import os
import numpy as np
import argparse as argp
import geosoft.gxpy as gxpy


def process_database(db, channel_name, add_value):
    '''
    Process all selected lines in a database by adding a constant
    value to a channel. The data is processed in-place.
    '''

    # work through the data a line at a time - get a list of selected lines
    lines = db.lines()

    # for each line, get the data, add a value, return the data to the line
    for l in lines:

        # print to the console to reflect progress
        print('line {}...'.format(str(l)))

        # get the data and determine the dummy to the data type
        data, ch, fid = db.readLine(l, channels=channel_name)
        dummy = gxpy.utility.gxDummy(data.dtype)

        # make a dummy mask so we can replace dummies after processing
        dMask = gxpy.utility.dummyMask(data)

        # process - add the value, then replace the dummies
        sum = data + add_value
        sum[dMask] = dummy

        # write the data back to the database
        db.writeDataChan(l, channel_name, sum, fid)

if __name__ == "__main__":

    # The GX_GEOSOFT_BIN_PATH Environment variable should contain a path with geodist.dll
    print("GX_GEOSOFT_BIN_PATH: {}".format(os.getenv("GX_GEOSOFT_BIN_PATH")))
    print('Working directory: ' + os.path.abspath(os.curdir))

    # get command line parameters
    parser = argp.ArgumentParser(description="Add a constant to a Geosoft database channel")
    parser.add_argument("sDB", help="Geosoft database")
    parser.add_argument("sCh", help="channel to process")
    parser.add_argument("-v","--value", type=float, default=1.0, help="value to add, default is 1.0")
    args = parser.parse_args()

    # echo parameters
    print("Database = "+args.sDB)
    print("Channel = "+args.sCh)
    print("Value to add = {}".format(args.value))

    # get (create) a GX context
    gxp = gxpy.gx.GXpy()  # get the current gx context
    
    # open the database
    db = gxpy.gdb.GXdb.open(args.sDB)
    
    # process the data
    process_database(db, args.sCh, args.value)
    

