'''

   Geosoft Desktop dependent functions.

'''

import os
import geosoft
import geosoft.gxapi as gxapi
from ..utility import dictFromLst

__version__ = geosoft.__version__

class OMException(Exception):
    pass

def _(s): return s

def running_script():
    '''
    :return: 1 if running from a script, 0 if running interactively.
    '''

    return not gxapi.GXSYS.interactive()

def message(title, message):
    '''
    Display a message to the user
    :param title:   message box title
    :param message: message
    '''
    gxapi.GXSYS.display_message(title, message)

def _user_input_gx(kind):
    ''' resolve and run the user_input GX'''
    gxapi.GXSYS.set_string("USER_INPUT", "TYPE", str(kind))
    dir = os.path.split(__file__)[0]
    user_input = os.path.join(os.path.join(dir,'user_input'), 'user_input.gx')
    ret = gxapi.GXSYS.run_gx(user_input)
    if ret == -1:
        gxapi.GXSYS.cancel()
    return ret

def pause(title='Pause...', cancel=False):
    '''
    Display a pause dialog, wait for user to press continue or cancel
    :param title:   The pause dialog title, default is "Pause..."
    :param cancel:  If True, show a cancel button
    :raises:        :py:ex:GXCancel if the user cancels the dialog
    '''
    
    gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
    if not cancel:
        _user_input_gx(9)
    else:
        _user_input_gx(10)


def get_user_input(title="Input required...", prompt='?', kind='string', default='', items='', filemask=''):
    '''
    Display a dialog prompt on the Geosoft Desktop and wait for user input.
    This method depends on "user_input.gx" and can only be used from an extension running
    inside a Geosoft Desktop application.

    :param title:       dialog box title.  A description can be added as a second-line using a line-break.
                        example: "Your title/nDescriptive help"
    :param prompt:      prompt string to
    :param kind:        kind of response required: 'string', 'int', 'float', 'file', 'colour' or 'list'
    :param items:       string of comma-separated items for a list
    :param default:     default value.  For multifile can be a string ('|' delimiter) or iterable.
    :param filemask:    File type mask "*.dat", "*.dat;*.grd", "**,*.grd" for multiple files
    :return:        user response
    :raise:         :py:ex:GXCancel if the user cancels the dialog
    '''

    gxapi.GXSYS.set_string("USER_INPUT", "TITLE", str(title))
    gxapi.GXSYS.set_string("USER_INPUT", "PROMPT", str(prompt))
    gxapi.GXSYS.set_string("USER_INPUT", "FILEMASK", filemask)

    # make a list out of the items.
    if len(items) > 0:
        if type(items) is dict:
            items = [(k) for k in items.keys()]
        elif isinstance(items, str):
            items = items.split(',')
        gxapi.GXSYS.set_string("USER_INPUT", "LIST", ",".join(items))

        # make sure default is in the list
        if default not in items:
            if len(items) > 0:
                default = items[0]

    # resolve default string, which may be a list of files for the multifile dialogs
    if isinstance(default, str):
        gxapi.GXSYS.set_string("USER_INPUT", "RESPONSE", default)
    else:
        try:
            gxapi.GXSYS.set_string("USER_INPUT", "RESPONSE", '|'.join(default))
        except TypeError:  # this happens if ints or reals are passed
            gxapi.GXSYS.set_string("USER_INPUT", "RESPONSE", str(default))

    if kind == 'color':
        kind = 'colour'
    kind_list = {'string':  0,
                 'float':   1,
                 'int':     2,
                 'list':    3,
                 'colour':  4,
                 'file':    5,
                 'newfile': 6,
                 'oldfile': 7,
                 'multifile':8}
    kind = kind_list[kind]

    # show the dialog
    ret = _user_input_gx(kind)

    if ret == 0:

        strr = gxapi.str_ref()
        gxapi.GXSYS.gt_string("USER_INPUT", "RESPONSE", strr)
        if kind == kind_list['int']:
            return int(strr.value)
        if kind == kind_list['float']:
            return float(strr.value)
        if kind == kind_list['multifile']:
            return strr.value.split('|')
        return strr.value

    raise OMException('GX Error ({})'.format(ret))


def menus():
    ''' Returns Oasis montaj menu information as a dictionary:
    {
        'default'
        'loaded'
        'user'
    }
    '''

    def_menus = gxapi.GXLST.create(512)
    loaded_menus = gxapi.GXLST.create(512)
    user_menus = gxapi.GXLST.create(512)
    gxapi.GXSYS.get_loaded_menus(def_menus, loaded_menus, user_menus)

    info = {'menu_default': list(dictFromLst(def_menus).keys()),
            'menu_loaded': list(dictFromLst(loaded_menus).keys()),
            'menu_user': list(dictFromLst(user_menus).keys()) }

    return info


def state():
    '''
    Return a dictionary that contains the current Oasis montaj state:

    {
        'gdb' {
            'open_list'
            'current'
            'disp_chan_list'
            'selection' [
                line, channel, start_fid, end_fid       # channel is '' if no channel selected
                                                        # start_fid is '' if no fiducials selected
                                                        # start_fid is '*' is all fiducials selected
                                                        # line is "*" is all lines selected
            ]
        }
        'map' {
            'open_list'
            'current'
            'point' [
                x, y, z
            ]
            'cursor' [
                x, y, z
            ]
            'display_area' [
                xmin, ymin, xmax, ymax
            ]
        }
    }
    '''

    s = gxapi.str_ref()
    glst = gxapi.GXLST.create(4096)
    state = {}

    # databases
    ndb = gxapi.GXEDB.get_databases_lst(glst, gxapi.EDB_PATH_FULL)
    if ndb > 0:
        sdb = {}
        edb = gxapi.GXEDB.current_no_activate()
        edb.get_name(s)
        sdb['current'] = s.value
        sdb['open_list'] = list(dictFromLst(glst).keys())

        n = edb.disp_chan_lst(glst)
        if n > 0:
            sdb['disp_chan_list'] = list(dictFromLst(glst).keys())
        else:
            sdb['disp_chan_list'] = []

        sch = gxapi.str_ref()
        sln = gxapi.str_ref()
        sfd = gxapi.str_ref()
        edb.get_current_selection(s, sch, sln, sfd)
        if sch.value == '[All]':
            sch.value = '*'
        if sln.value == '[All]':
            sln.value = '*'
        if sfd.value == '[All]':
            fd = ('*','*')
        elif sfd.value == "[None]":
            fd = ('','')
        else:
            fd = sfd.value.split(' to ')
            fd = (fd[0], fd[1])
        sdb['selection'] = (sln.value, sch.value, fd[0], fd[1])
        state['gdb'] = sdb

    # maps
    nmaps = gxapi.GXEMAP.get_maps_lst(glst, gxapi.EMAP_PATH_FULL)
    if nmaps > 0:
        fx = gxapi.float_ref()
        fy = gxapi.float_ref()
        fx2 = gxapi.float_ref()
        fy2 = gxapi.float_ref()

        smap = {}
        emap = gxapi.GXEMAP.current_no_activate()
        emap.get_name(s)
        smap['current'] = s.value
        smap['open_list'] = list(dictFromLst(glst).keys())

        emap.get_display_area(fx, fy, fx2, fy2)
        smap['display_area'] = (fx.value, fy.value, fx2.value, fy2.value)

        if emap.is_3d_view():

            emap.get_3d_view_name(s)
            smap['3d_view_name'] = s.value

        else:
            # 2D

            emap.get_cur_point(fx, fy)
            smap["point"] = (fx.value, fy.value, None)
            emap.get_cursor(fx, fy)
            smap["cursor"] = (fx.value, fy.value, None)

        state['map'] = smap

    return state