'''
Add a constant value to a channel on all selected lines.

This is a sample Python extension that shows how to work with saved parameters
and a Geosoft database.

'''

import geosoft.gxpy as gxpy
import geosoft.gxpy.om as gxom
import geosoft.gxpy.utility as gxu


def rungx():

    # get the current database
    db = gxpy.gdb.GXdb.open()

    # project parameters
    group = 'CHANADD'
    p_chan = 'CHANNEL'
    p_addval = 'ADDVAL'

    # get previous parameters from the parameter block, initializing to start-up defaults '' and 0.0
    parms = gxu.get_parameters(group, {p_chan: '', p_addval: 0.0})

    # if interactive, get user input
    if not gxom.running_script():

        try:
            # get channel to process from list of database channels
            chan = gxom.get_user_input(
                    'Channel to process',
                    'Channel:',
                    kind='list',
                    default=parms.get(p_chan),
                    items=sorted([k for k in db.list_channels().keys()]))

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
    lines = db.list_lines()

    # for each line, get the data, add a value, return the data to the line
    for l in lines:

        # print to the console to reflect progress
        print('line {}...'.format(str(l)))

        # get the data and determine the dummy to the data type
        data, ch, fid = db.read_line(l, channels=chan)
        dummy = gxu.gx_dummy(data.dtype)

        # make a dummy mask so we can replace dummies after processing
        dMask = gxu.dummy_mask(data)

        # process - add the value, then replace the dummies
        sum = data + addval
        sum[dMask] = dummy

        # write the data back to the database
        db.write_channel(l, chan, sum, fid)

    # pause the console so user can review
    input("Press return to continue...")
