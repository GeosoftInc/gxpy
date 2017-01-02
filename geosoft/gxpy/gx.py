'''
GX Context and related methods required for Geosoft Python.
'''

import tkinter.ttk as ttk
import pythoncom
import pprint
import os
import json
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

#: `geosoft.gxpy.gxcontext` references the global Geosoft Python GX (gxpy) context instance
#: once created. This can be accessed by any method that requires the global Python GX context.
#: `geosoft.gxpy.context.gxapi` is the GX context for the `gxapi`.
gxcontext = None

class GXpy:
    '''
    Geosoft GX context.  This can only be created once.

    Once created, `gxpy.gxcontext` will hold the GX context, which can be used where the application
    does not have access to the initial context instance.

    `gxpy.gxcontext` will be `None` if the context has not been created, or has been destroyed.

    :param app:             application name, default is the script name
    :param version:         application version number, default Geosoft version
    :param parent_window:   ID of the parent window.  A parent window is required for GUI-dependent
                            functions to work.  Set `parent_window=-1` to create a Tkinter frame that
                            provides a default parent window handle for GUI/Viewer functions.
    :param log:             name of a file to record logging information, or a call-back that
                            accepts a string.  Specifying `log=''` will log to a default file named
                            using the current date and time.  If not provided calls to log()
                            are ignored.

    :members:
        :gxapi:             GX context to be used to call geosoft.gxapi methods
        :gid:               User's Geosoft ID
        :gxcontext:         Class instance for this session, `None` if not created, or deleted.

    :raises:
        :GXException():  if unable to create context

    .. versionchanged:: 9.2
        `parent_window=-1` creates a Tkinter frame as a parent.

    .. versionchanged:: 9.2
        Added `log` argument to support `log()`.

    .. versionadded:: 9.1

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
            self.log("error removing temporary file \"{}\": function \"{}\": exception\"{}\""
                     .format(path, str(fnc), str(excinfo)))

        if not self._keep_temp_files:
            if self._temp_file_folder != gxu.folder_temp():
                shutil.rmtree(self._temp_file_folder, ignore_errors=False, onerror=file_error)
            self._temp_file_folder = None

        if self._logf:
            self._logf.close()

    def __init__(self, name=__name__, version=__version__, parent_window=0, log=None):

        global gxcontext
        if gxcontext is not None:
            raise GXException('GXpy cannot be created twice.  Use gxpy.gxcontext instead.')

        # create a Tkinter parent frame for the viewers

        self.tkf = None
        if parent_window == -1:
            self.tkf = ttk.Frame(master=None)
            parent_window = self.tkf.winfo_id()

        self.parent_window = parent_window
        try:
            self.gxapi = gxapi.GXContext.create(name, version, self.parent_window)

        except:
            self.gxapi = None
            raise GXException('GX services are not available.')

        user = gxapi.str_ref()
        company = gxapi.str_ref()
        gxapi.GXSYS.get_licensed_user(user, company)
        self.gid = user.value
        self._temp_file_folder = None
        self._keep_temp_files = True

        self._start = datetime.datetime.utcnow()
        self._gxid = gxu.uuid()

        # create a log file

        if log is None:
            self._logf = None
            self._log_it = None

        else:

            if callable(log):
                self._log_it = log
                self._logf = None
                
            else:
    
                if len(log) == 0:
    
                    dts = "{}-{}-{}({}_{}_{}_{})"\
                        .format(self._start.year,
                                                         str(self._start.month).zfill(2),
                                                         str(self._start.day).zfill(2),
                                                         str(self._start.hour).zfill(2),
                                                         str(self._start.minute).zfill(2),
                                                         str(self._start.second).zfill(2),
                                                         str(self._start.microsecond//1000).zfill(3))
                    log = "_gx_" + dts + ".log"
    
                self._logf = open(log, "wb")
                self._log_it = self._log_to_file

            self.log('\nGX start')
            self.log('GX id: {}'.format(self._gxid))
            self.log('UTC: {}'.format(self._start))
            self.log('API: {}'.format(__version__))
            self.log('GID: {}'.format(self.gid))
            self.log('rights: {}'.format(json.dumps(self.entitlements())))
            self.log('script: {}'.format(gxs.app_name()))
            self.log('project path: {}'.format(gxu.folder_workspace()))
            self.log('user path: {}'.format(gxu.folder_workspace()))

        # create a shared string ref for the convenience of Geosoft modules

        self._sr = gxapi.str_ref()

        atexit.register(self._cleanup_files)

        gxcontext = self

    def __del__(self):
        global gxcontext
        gxcontext = None

    def _log_to_file(self, log_str):

        now = datetime.datetime.now()
        dts = "{}-{}-{} {}:{}:{}:{} ".format(now.year,
                                             str(now.month).zfill(2),
                                             str(now.day).zfill(2),
                                             str(now.hour).zfill(2),
                                             str(now.minute).zfill(2),
                                             str(now.second).zfill(2),
                                             str(now.microsecond // 1000).zfill(3))
        for l in str(log_str).split('\n'):
            logstr = dts + l + os.linesep
            self._logf.write(logstr.encode('utf-8'))

    def main_wind_id(self):
        '''
        :returns: The main window ID (HWND cast to unsigned for Windows).

        .. versionadded:: 9.1
        '''

        if self.parent_window == 0:
            return self.gxapi.get_main_wnd_id()
        else:
            return self.parent_window

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
        Return the GX temporary folder path.

        Each GX instance will create an instance-specific
        temporary folder as a child in the Geosoft temporary folder.  Placing temporary files in
        the GX-specific temporary folder will ensure temporary file names will not collide with
        other running GX-based programs, and that all temporarty files are removed on termination
        of this GX.
        
        Call `keep_temp_folder` to prevent deletion of the temporary files, which can be useful
        when debugging.
        
        .. versionadded:: 9.2
        '''

        if self._temp_file_folder is None:

            # create a temporary folder for this GX instance

            path = gxu.folder_temp()
            uuid = "_gx_" + self._gxid
            self._temp_file_folder = os.path.join(path, uuid)
            try:
                os.makedirs(self._temp_file_folder, exist_ok=True)
                self._keep_temp_files = False
            except OSError:
                self._temp_file_folder = path
                self._keep_temp_files = True

        return self._temp_file_folder

    def keep_temp_folder(self, keep=True):
        """
        Keep temporary file folder setting.
        :param keep: True to keep the temporary file folder, False to remove

        .. versionadded:: 9.2
        """
        self._keep_temp_files = keep

    def temp_file(self, ext=''):
        """
        Return a unique temporary file name as a full path.  The temporary file is created in
        the instance temporary folder and will be deleted when this GXpy instance is deleted.

        :param ext: optional extension, including "." separator
        :return:    uuid-based file name in the instance temporary folder.

        .. versionadded:: 9.2
        """

        return os.path.join(self.temp_folder(), gxu.uuid() + ext)

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
        Log a string to the log file or log call-back as defined when creating :class:`~gx.GXpy` instance.

        :param log_str: string to log.

        If logging to a file each line is preceded by the date and time:

        .. code::
         2016-12-25 12:34:16.175 log_str_line_1
         2016-12-25 12:34:16.175 log_str_line_2

        .. versionadded:: 9.2
        """

        if self._log_it:
            self._log_it(log_str)


    def elapsed_seconds(self, tag=''):
        """
        Return the elapsed seconds since this GX instance started.
        The elapsed time is logged if logging is on.

        :param tag:     optional string to add to the log
        :return:        elapsed time in seconds

        .. versionadded:: 9.2
        """

        elapsed = datetime.datetime.now() - self._start
        elapsed_seconds = elapsed.seconds + elapsed.microseconds / 1000000.0
        if tag:
            tag = '{}> '.format(tag)
        self.log('{}Elapsed seconds: {} ({} minutes, {}.{} seconds)'.
                 format(tag,
                        elapsed_seconds,
                        elapsed.seconds // 60,
                        elapsed.seconds % 60,
                        str(elapsed.microseconds).zfill(6)))
        return elapsed_seconds

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

