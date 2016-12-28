'''
GX Context and related methods to with Geosoft Python.
'''

import tkinter.ttk as ttk
import pythoncom
import pprint
import os
import sys
import shutil
import datetime
import atexit

import geosoft
import geosoft.gxapi as gxapi
from . import utility as gxu
from . import system as gxs

__version__ = geosoft.__version__


class GXException(Exception):
    '''
    Exceptions from this module.

    .. versionadded:: 9.1
    '''
    pass


class GXpy:
    '''
    Geosoft GX context.

    :param app:             application name, default is the script name
    :param version:         application version number, default geosoft version
    :param parent_window:   ID of the parent window.  If -1 a Tkinter window
                            is created for GUI/Viewer functions to work.
    :param: log_file        name of a file to record logging information, '' for a default name
                            based on the current date and time.  If not provided (log_file=None),
                            no log file is created.
    :members:
        :gxapi:             GX context to be used to call geosoft.gxapi methods
        :gid:               User's Geosoft ID

    :raises:
        :GXException():  if unable to create context

    .. versionadded:: 9.1

    .. versionchanged:: 9.2
        If parent window is not defined (None), create a Tkinter frame as a parent.

    '''

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "GID: {}, class: {}".format(self.gid, self.license_class())

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.__del__()
        return False

    def _cleanup_files(self):

        def file_error(fnc, path, excinfo):
            self.log("error removing temporary file \"{}\": function \"{}\": exception\"{}\"".format(path, str(fnc), str(excinfo)))

        elapsed = datetime.datetime.now() - self._start
        self.log('shutting down after {} minutes, {}.{} seconds'.format(elapsed.seconds//60, elapsed.seconds%60, str(elapsed.microseconds).zfill(6)))

        if not self._keep_temp_files:
            shutil.rmtree(self._temp_file_folder, ignore_errors=False, onerror=file_error)

        if self._logf:
            self._logf.close()

    def __init__(self, name=__name__, version=__version__, parent_window=0, log_file=None):

        now = datetime.datetime.now()
        self._start = now

        # create a Tkinter parent frame for the viewers

        self.tkf = None
        if parent_window == -1:
            self.tkf = ttk.Frame(master=None)
            parent_window = self.tkf.winfo_id()

        try:
            self.gxapi = gxapi.GXContext.create(name, version, parent_window)

        except:
            self.gxapi = None
            raise GXException('GX services are not available.')

        user = gxapi.str_ref()
        company = gxapi.str_ref()
        gxapi.GXSYS.get_licensed_user(user, company)
        self.gid = user.value

        # create a temporary folder for this GX instance

        path = gxu.folder_temp()
        uuid = "_gx_" + gxu.uuid()
        self._temp_file_folder = os.path.join(path, uuid)
        try:
            os.makedirs(self._temp_file_folder, exist_ok=True)
            self._keep_temp_files = False
        except OSError:
            self._temp_file_folder = path
            self._keep_temp_files = True

        # create a log file

        if log_file is None:
            self._logf = None

        else:

            if len(log_file) == 0:

                dts = "{}-{}-{}({}_{}_{}_{})".format(now.year,
                                                     str(now.month).zfill(2),
                                                     str(now.day).zfill(2),
                                                     str(now.hour).zfill(2),
                                                     str(now.minute).zfill(2),
                                                     str(now.second).zfill(2),
                                                     str(now.microsecond//1000).zfill(3))
                log_file = "_gx_" + dts + ".log"

            self._log_file_name = log_file
            self._logf = open(self._log_file_name, "wb+")

            self.log('starting')
            self.log('UTC date: {}'.format(gxapi.GXSYS.utc_date()))
            self.log('UTC time: {}'.format(gxapi.GXSYS.utc_time()))
            self.log('API: {}'.format(__version__))
            self.log('GID: {}'.format(self.gid))
            self.log('rights: {}'.format(self.entitlements()))
            self.log('script: {}'.format(gxs.app_name()))
            self.log('project path: {}'.format(gxu.folder_workspace()))
            self.log('user path: {}'.format(gxu.folder_workspace()))
            self.log('gx_temp_folder: {}'.format(self._temp_file_folder))

        # create a shared string ref for the convenience of Geosoft modules

        self._sr = gxapi.str_ref()

        atexit.register(self._cleanup_files)

    def __del__(self):
        pass

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

    def temp_folder(self):
        '''
        Return the GX temporary folder path.  Each GX instance will create an instance-specific
        temporary folder as a child in the Geosoft temporary folder.  Placing temporary files in
        the GX-specific temporary folder will ensure temporary file names will not collide with
        other running GX-based programs, and that all temporarty files are cleaned-up on termination
        of this GX.
        
        Call `keep_temp_folder` to prevent deletion of the temporary files, which can be useful
        when debugging.
        
        .. versionadded: 9.2
        '''
        return self._temp_file_folder

    def keep_temp_folder(self, keep=True):
        """
        Keep temporary file folder setting.
        :param keep: True to keep the temporary file folder, False to remove

        .. versionadded: 9.2
        """
        self._keep_temp_files = keep

    def temp_file(self, ext=''):
        """
        Return a unique temporary file name as a full path.

        :param ext: optional extension, including "." separator
        :return:    uuid-based file name in the Geosoft temporary folder.

        .. versionadded:: 9.2
        """

        return os.path.join(self._temp_file_folder, gxu.uuid() + ext)

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
                'folder_workspace': gxu.folder_workspace(),
                'folder_temp': gxu.folder_temp(),
                'folder_user': gxu.folder_user(),
                }

        if formated_indent >= 0:
            pp = pprint.PrettyPrinter(indent=formated_indent)
            return pp.pformat(info)
        else:
            return info

    def log(self, log_str):
        """
        Log a string in the log file.  A log file must be defined when the GX context
        is created, otherwise logging is ignored.

        :param log_str: string to log.  This should not contain a new-line

        Logging format is:

        .. code::
            2016-12-25 12:34:16.175 log_str

        .. versionadded:: 9.2
        """

        if self._logf:
            now = datetime.datetime.now()
            dts = "{}-{}-{} {}:{}:{}:{} ".format(now.year,
                                                 str(now.month).zfill(2),
                                                 str(now.day).zfill(2),
                                                 str(now.hour).zfill(2),
                                                 str(now.minute).zfill(2),
                                                 str(now.second).zfill(2),
                                                 str(now.microsecond//1000).zfill(3))

            self._logf.write(dts.encode('utf-8'))
            self._logf.write(str(log_str).encode('utf-8'))
            self._logf.write(os.linesep.encode('utf-8'))

####################################################
# deprecated

    def folder_workspace(self):
        '''
        .. deprecated: 9.2
            Use :method:`utility.project_path`
        '''
        return gxu.project_path()

    def folder_temp(self):
        '''
        .. deprecated: 9.2
            Use :method:`utility.temp_folder`
        '''
        return gxu.temp_folder()

    def folder_user(self):
        '''
        .. deprecated: 9.2
            Use :method:`utility.user_path`
        '''
        return gxu.user_path()

