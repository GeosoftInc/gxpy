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

import geosoft.gxpy as gxpy
import geosoft.gxpy.om as gxom
import geosoft.gxpy.utility as gxu
import pydevd

def rungx():

    # pydevd supports remote debugging - see Debugging Python Extensions in the GX Developer documentation
    # this sets a break-point after this line when this script is run from Oasis montaj.
    # un-comment the follwoing like to activate remote debugging:
    # pydevd.settrace('localhost', port=34765, stdoutToServer=True, stderrToServer=True)

    # get the current database
    db = gxpy.gdb.GXdb.open()

    # parameters
    group = 'CHANADD'
    p_chan = 'CHANNEL'
    p_addval = 'ADDVAL'

    # get parameters from the parameter block, initializing to start-up defaults '' and 0.0
    parms = gxu.get_parameters(group, {p_chan:'', p_addval:0.0})

    # if interactive, get user input
    if not gxom.running_script():

        try:
            # ask for a channel to process from list of channels in the database
            chan = gxom.get_user_input(
                                    'Channel to process',
                                    'Channel:',
                                    kind='list',
                                    default=parms.get(p_chan),
                                    items=sorted([k for k in db.channels().keys()]))

            # value to add to the channel
            addval = gxom.get_user_input(
                                    'Value to add to the data',
                                    'value to add:',
                                    kind='float',
                                    default=parms.get(p_addval))
        except gxom.OMException:
            exit()

        # save parameters to new user settings
        parms[p_chan] = chan
        parms[p_addval] = addval
        gxu.save_parameters(group, parms)



    # work through the data a line at a time - get a list of selected lines
    lines = db.lines()

    # for each line, get the data, add a value, return the data to the line
    for l in lines:

        # print to the console to reflect progress
        print('line {}...'.format(str(l)))

        # get the data and determine the dummy to the data type
        data, ch, fid = db.readLine(l, channels=chan)
        dummy = gxu.gxDummy(data.dtype)

        # make a dummy mask so we can replace dummies after processing
        dMask = gxu.dummyMask(data)

        # process - add the value, then replace the dummies
        sum = data + addval
        sum[dMask] = dummy

        # write the data back to the database
        db.writeDataChan(l, chan, sum, fid)

    # pause hold the console so user can review
    input("Press return to exit...")