'''

   Geosoft Desktop dependent functions.

'''

from time import gmtime, strftime
from jdcal import is_leap, gcal2jd, jd2gcal
import numpy as np

import geosoft
import geosoft.gxapi as gxapi
import geosoft.gxpy.utility as gxu

__version__ = geosoft.__version__

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

        # make a list out of the items.
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


def environment(self, formated_indent=-1):
    ''' :returns: Oasis montaj environment information as a dictionary'''

    def_menus = gxapi.GXLST.create(512)
    loaded_menus = gxapi.GXLST.create(512)
    user_menus = gxapi.GXLST.create(512)
    try:
        gxapi.GXSYS.get_loaded_menus(def_menus, loaded_menus, user_menus)
        def_menus = gxu.dictFromLst(def_menus),
        loaded_menus = gxu.dictFromLst(loaded_menus),
        user_menus = gxu.dictFromLst(user_menus),
    except:
        def_menus = loaded_menus = user_menus = ""

    info = {'gid': self.gid,
            'current_date': gxapi.GXSYS.date(),
            'current_utc_date': gxapi.GXSYS.utc_date(),
            'current_time': gxapi.GXSYS.time(),
            'current_utc_time': gxapi.GXSYS.utc_time(),
            'license_class': self.license_class(),
            'menu_default': def_menus,
            'menu_loaded': loaded_menus,
            'menu_user': user_menus,
            'folder_workspace': self.folder_workspace(),
            'folder_temp': self.folder_temp(),
            'folder_user': self.folder_user(),
            'id_window_main': self.main_wind_id(),
            'id_window_active': self.active_wind_id(),
            'id_thread': gxapi.GXSYS.get_thread_id(),
            }


def get_om_state():
    '''
    Return a dictionary that contains the current Oasis montaj state.

    project_path
    gdb {
        open_list
        current
        disp_chan_list
        selection
    }
    map {
        map_open_list
        map_current
        map_point
        map_cursor

    '''

    s = gxapi.str_ref()
    lst = gxapi.GXLST.create()
    state = {}

    # project path
    gxapi.gxsys.get_path(gxapi.SYS_PATH_LOCAL, s)
    s['project_path'] = s.value

    # databases
    ndb = gxapi.GXEDB.get_databases_lst(lst, gxapi.EDB_PATH_FULL)
    if ndb > 0:
        sdb = {}
        edb = gxapi.GXEDB.current_no_activate()
        edb.get_name(s)
        sdb['current'] = s.value
        sdb['open_list'] = list(lst.keys())

        n = gxapi.GXEDB.disp_chan_list(lst)
        if n > 0:
            sdb['disp_chan_list'] = list(lst.keys())
        else:
            sdb['disp_chan_list'] = []

        sch = gxapi.str_ref()
        sln = gxapi.str_ref()
        sfd = gxapi.str_ref()
        gxapi.GXEDB.get_current_selection(s, sch, sln, sfd)
        if sch.value == '[All]':
            sch.value = '*'
        if sln.value == '[All]':
            sln.value = '*'
        if sfd.value == '[None]':
            fd = None
        else:
            fd = sfd.value.split(' to ')
            fd = (fd[0], fd[1])
        sdb['selection'] = (sch, sln, fd)
