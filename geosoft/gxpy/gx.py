'''
GX Context and related methods to with Geosoft Python.
'''

import pprint
import geosoft
import geosoft.gxapi as gxapi
from . import utility as gxu

__version__ = geosoft.__version__

class GXException(Exception):
    pass

class GXpy():
    '''
    Geosoft GX context.

    :param app:             application name, default is the script name
    :param version:         application version number, default 0.
    :param parent_window    ID of the parent window if needed.

    :members:
        :gxapi:            GX context to be used to call geosoft.gxapi methods
        :gid:           Geosoft ID

    :raises:
        :GXException():  if unable to create context

    '''


    def __repr__(self):
        return "{}({})".format(self.__class__,self.__dict__)

    def __init__(self, name=__name__, version=__version__, parent_window=0):

        try:
            self.gxapi = gxapi.GXContext.create(name, version, parent_window)

        except:
            self.gxapi = None
            raise GXException('GX services are not available.')

        user = gxapi.str_ref()
        company = gxapi.str_ref()
        gxapi.GXSYS.get_licensed_user( user, company)
        self.gid = user.value

        # create a shared string ref for the convenience of Geosoft modules
        self._sr = gxapi.str_ref()

    def display_message(self, title, message):
        ''' display a message to the user.'''

        try:
            gxu.safeApiException(gxapi.GXSYS.display_message, (title, message), GXException)
        except GXException:
            print('Title: {}\nMessage: {}'.format(title,message))

    def main_wind_id(self):
        ''' :returns: the main window ID (HWND cast to unsigned for Windows).'''

        return self.gxapi.get_main_wnd_id()


    def active_wind_id(self):
        ''' :returns: the active window ID (HWND cast to unsigned for Windows).'''

        return self.gxapi.get_active_wnd_id()

    def dissable_app(self):
        ''' disables application windows to allow modal Python UI.  Call before opening your own UI window.'''
        self.gxapi.enable_application_windows(False)

    def enable_app(self):
        ''' enables application windows to allow modal Python UI.  Call before returning control to OM.'''
        self.gxapi.enable_application_windows(True)

    def entitlements(self):
        ''' :return: current entitlements as a dictionary'''

        lst = gxapi.GXLST.create(1000)
        gxapi.GXSYS.get_entitlement_rights(lst)
        return gxu.dictFromLst(lst)

    def license_class(self):
        ''' :return: current license class'''

        lc = gxapi.str_ref()
        gxapi.GXSYS.get_license_class(lc)
        return lc.value

    def folder_workspace(self):
        ''' :return: workspace folder'''

        folder = gxapi.str_ref()
        gxapi.GXSYS.get_path(gxapi.SYS_PATH_LOCAL, folder)
        return folder.value

    def folder_temp(self):
        ''' :return: temp folder'''

        folder = gxapi.str_ref()
        gxapi.GXSYS.get_path(gxapi.SYS_PATH_GEOTEMP, folder)
        return folder.value

    def folder_user(self):
        ''' :return: Geosoft user files'''

        folder = gxapi.str_ref()
        gxapi.GXSYS.get_path(gxapi.SYS_PATH_GEOSOFT_USER, folder)
        return folder.value

    def environment(self, formated_indent=-1):
        ''' :returns: Geosoft environment information as a dictionary'''

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

