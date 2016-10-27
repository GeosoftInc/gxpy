'''

   Geosoft Desktop dependent functions.

'''

from time import gmtime, strftime
from jdcal import is_leap, gcal2jd, jd2gcal
import numpy as np

import geosoft
import geosoft.gxapi as gxapi

__version__ = geosoft.__release__

class OMException(Exception):
    pass

def running_script():
    '''
    :return: 1 if running from a script, 0 if running interactively.
    '''

    return not gxapi.GXSYS.interactive()

def pause(title='Pause...', cancel=None):
    '''
    Display a pause dialog, wait for user to press continue or cancel
    :param title:   The pause dialog title, default is "Pause..."
    :param cancel:  If specified, add a cancel button with cancel text (ie cancel="STOP")
    :raises:        :py:ex:GXCancel if the user cancels the dialog
    '''
    
    gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
    if cancel is None:
        gxapi.GXSYS.set_string("USER_INPUT", "TYPE", "4")
    else:
        gxapi.GXSYS.set_string("USER_INPUT", "TYPE", "5")
        gxapi.GXSYS.set_string("USER_INPUT", "PROMPT", str(cancel))

    if gxapi.GXSYS.run_gx("user_input.gx") == -1:
        gxapi.GXSYS.cancel()

def get_user_input(title="Input required...", prompt='?', kind='string', default='',items=''):
    '''
    Display a dialog prompt on the Geosoft Desktop and wait for user input.
    This method depends on "user_input.gx" and can only be used from an extension running
    inside a Geosoft Desktop application.

    :param title:   dialog box title.  A description can be added as a second-line using a line-break.
                    example: "Your title/nDescriptive help"
    :param prompt:  prompt string to
    :param kind:    kind of response required: 'string', 'int', 'float' or 'list'
    :param items:   string of comma-separated items for a list
    :param default: default value
    :return:        user response
    :raise:         :py:ex:GXCancel if the user cancels the dialog
    '''


    if (kind == 'float'):
        gxapi.GXSYS.set_string("USER_INPUT", "TYPE", "1")

    elif (kind == 'int'):
        gxapi.GXSYS.set_string("USER_INPUT", "TYPE", "2")

    elif (kind == 'list'):
        gxapi.GXSYS.set_string("USER_INPUT", "TYPE", "3")

        # first make a list out of the items.
        if type(items) is dict:
            items = [(k) for k in items.keys()]
        elif type(items) is str:
            items = items.split(',')

        # make sure default is in the list
        if default not in items:
            if len(items) > 0:
                default = items[0]

        gxapi.GXSYS.set_string("USER_INPUT", "LIST", ",".join(items))

    else:
        gxapi.GXSYS.set_string("USER_INPUT", "TYPE", "0")

    gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
    gxapi.GXSYS.set_string("USER_INPUT", "PROMPT", str(prompt))
    gxapi.GXSYS.set_string("USER_INPUT", "RESPONSE", str(default))
    ret = gxapi.GXSYS.run_gx("user_input.gx")

    if ret == 0:

        strr = gxapi.str_ref()
        gxapi.GXSYS.gt_string("USER_INPUT", "RESPONSE", strr)
        if kind == 'int':
            return int(strr.value)
        if kind == 'float':
            return float(strr.value)
        return strr.value

    if ret == -1:
        gxapi.GXSYS.cancel()
    raise OMException('GX Error {}'.format(ret))
