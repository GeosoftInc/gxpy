'''
GX Context and related methods to with Geosoft Python.
'''

import pprint
import geosoft
import geosoft.gxapi as gxapi
from . import utility as gxu

__version__ = geosoft.__version__


class GXException(Exception):
    '''
    Exceptions from this module.

    .. versionadded:: 9.1
    '''
    pass


class GXpy():
    '''
    Geosoft GX context.

    :param app:             application name, default is the script name
    :param version:         application version number, default geosoft version
    :param parent_window:   ID of the parent window if needed, default 0.

    :members:
        :gxapi:             GX context to be used to call geosoft.gxapi methods
        :gid:               User's Geosoft ID

    :raises:
        :GXException():  if unable to create context

    .. versionadded:: 9.1
    '''

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __init__(self, name=__name__, version=__version__, parent_window=0):

        try:
            self.gxapi = gxapi.GXContext.create(name, version, parent_window)

        except:
            self.gxapi = None
            raise GXException('GX services are not available.')

        user = gxapi.str_ref()
        company = gxapi.str_ref()
        gxapi.GXSYS.get_licensed_user(user, company)
        self.gid = user.value

        # create a shared string ref for the convenience of Geosoft modules
        self._sr = gxapi.str_ref()

    def main_wind_id(self):
        '''
        :returns: The main window ID (HWND cast to unsigned for Windows).

        .. versionadded:: 9.1
        '''

        return self.gxapi.get_main_wnd_id()

    def active_wind_id(self):
        '''
        :returns: The active window ID (HWND cast to unsigned for Windows).

        .. versionadded:: 9.1
        '''

        return self.gxapi.get_active_wnd_id()

    def disable_app(self):
        '''
        Disables application windows to allow modal Python UI.
        Call before opening your own UI window.

        .. versionadded:: 9.1
        '''
        self.gxapi.enable_application_windows(False)

    def enable_app(self):
        '''
        Enables application windows to allow modal Python UI.
        Call before returning control to OM.

        .. versionadded:: 9.1
        '''
        self.gxapi.enable_application_windows(True)

    def entitlements(self):
        '''
        :return: The current user entitlements as a dictionary.

        .. versionadded:: 9.1
        '''

        lst = gxapi.GXLST.create(1000)
        gxapi.GXSYS.get_entitlement_rights(lst)
        return gxu.dict_from_lst(lst)

    def license_class(self):
        '''
        :return: The current license class.

        .. versionadded:: 9.1
        '''

        lc = gxapi.str_ref()
        gxapi.GXSYS.get_license_class(lc)
        return lc.value

    def folder_workspace(self):
        '''
        :return: The workspace folder.

        .. versionadded:: 9.1
        '''

        folder = gxapi.str_ref()
        gxapi.GXSYS.get_path(gxapi.SYS_PATH_LOCAL, folder)
        return folder.value

    def folder_temp(self):
        '''
        :return: The Geosoft tempporary folder.

        .. versionadded:: 9.1
        '''

        folder = gxapi.str_ref()
        gxapi.GXSYS.get_path(gxapi.SYS_PATH_GEOTEMP, folder)
        return folder.value

    def folder_user(self):
        '''
        :return: The Geosoft user configuration files folder.

        .. versionadded:: 9.1
        '''

        folder = gxapi.str_ref()
        gxapi.GXSYS.get_path(gxapi.SYS_PATH_GEOSOFT_USER, folder)
        return folder.value

    def environment(self, formated_indent=-1):
        '''
        :returns: Geosoft environment information as a dictionary.

        .. versionadded:: 9.1
        '''

        info = {'gid': self.gid,
                'current_date': gxapi.GXSYS.date(),
                'current_utc_date': gxapi.GXSYS.utc_date(),
                'current_time': gxapi.GXSYS.time(),
                'current_utc_time': gxapi.GXSYS.utc_time(),
                'license_class': self.license_class(),
                'folder_workspace': self.folder_workspace(),
                'folder_temp': self.folder_temp(),
                'folder_user': self.folder_user(),
                }

        if formated_indent >= 0:
            pp = pprint.PrettyPrinter(indent=formated_indent)
            return pp.pformat(info)
        else:
            return info
