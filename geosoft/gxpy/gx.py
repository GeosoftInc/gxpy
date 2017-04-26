"""
GX Context and related methods required for Geosoft Python.

.. note::

    Regression tests provide usage examples: `Tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_gx.py>`_

"""

import tkinter.ttk as ttk
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


def _t(s):
    return geosoft.gxpy.system.translate(s)


class GXException(Exception):
    """
    Exceptions from this module.

    .. versionadded:: 9.1
    """
    pass


class _Singleton:
    """
    Used internally to create a singleton instance of GXpy.
    See http://www.aleax.it/Python/5ep.html
    """
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


# global GX handle, None if not valid
gx = None
_res_id = 0
_res_heap = {}
_max_resource_heap = 1000000
_stack_depth = 5
_max_warnings = 10

def _reset_globals():
    global gx
    global _res_id
    global _res_heap
    global _max_resource_heap
    global _stack_depth
    global _max_warnings
    gx = None
    _res_id = 0
    _res_heap = {}
    _max_resource_heap = 1000000
    _stack_depth = 5
    _max_warnings = 10

def track_resource(cl, info):
    global _res_id
    global _res_heap
    global _stack_depth
    if _res_id < _max_resource_heap:
        _res_id += 1
        rs = "{}:".format(cl)
        for i in range(_stack_depth):
            f = gxs.func_name(i + 2)
            if f is None:
                break
            rs += '<{}'.format(gxs.func_name(i + 2))
        rs += ' [{}]'.format(info)
        _res_heap[_res_id] = rs
        return _res_id


def pop_resource(id):
    if len(_res_heap):
        try:
            del (_res_heap[id])
        except KeyError:
            pass


GX_WARNING_FILE = '_gx_warning_'


class GXpy(_Singleton):
    """
    Geosoft GX context.  This is a singleton class, so subsequent creation returns an instance
    identical to the initial creation. This also means that initialization arguments are ignored
    on a subsequent instantiation.

    :parameters:
        :app:           application name, default is the script name
        :version:       application version number, default Geosoft version
        :parent_window: ID of the parent window.  A parent window is required for GUI-dependent
                        functions to work.  Set `parent_window=-1` to create a Tkinter frame that
                        provides a default parent window handle for GUI/Viewer functions.
        :log:           name of a file to record logging information, or a call-back function that
                        accepts a string.  Specifying `log=''` will log to a default file named
                        using the current date and time.  If not provided calls to log()
                        are ignored.
        :max_heap:      If logging is on, open gxpy resources (like grids, or databases) are tracked.
                        This is the maximum size of resource heap for tracking open resources.
                        Set to 0 to not track resources. On exit, if any resources remain open
                        a warning is logged together with a list of the open resources, each with a
                        call stack to help find the function that created the resources.
        :res_stack:     Depth of the call-stack to report for open-resource warning.
        :max_warnings:  Maximum number of resource warnings to report.

    :Properties:
        :gxapi:             GX context to be used to call geosoft.gxapi methods
        :gid:               User's Geosoft ID
        :global gx:         Global reference to this singleton class instance, None if invalid.
        :current_date:      date at start-up
        :current_utc_date:  UTC date at start-up
        :current_time:      time at start-up
        :current_utc_time:  UTC time at start-up
        :license_class:     Geosoft license class
        :folder_workspace:  Geosoft workspace folder
        :folder_temp:       Geosoft temporary folder
        :folder_user:       Geosoft Desktop installation 'user' folder

    :raises:
        :GXException(): if unable to create context

    .. versionchanged:: 9.2

        `parent_window=-1` creates a Tkinter frame as a parent for scripts that call UI functions.

        Added `log` argument to support `log()`.

        Made environment dictionary properties, deprecated environment.

    .. versionadded:: 9.1

    """

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "GID: {}, class: {}".format(self.gid, self.license_class())

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return

    def _close(self):

        global gx
        global _res_heap
        global _max_warnings

        if gx:

            self.log('GX close')

            if self._temp_file_folder and (self._temp_file_folder != gxu.folder_temp()):

                warning_file = os.path.join(self._temp_file_folder, GX_WARNING_FILE)
                if os.path.isfile(warning_file):
                    os.remove(warning_file)

                self._remove_gx_temporary_folders()
                self._temp_file_folder = None

            if len(_res_heap):
                # resources were created but not deleted or removed
                self.log(_t('Warning - cleaning up resources that are still open:'))
                i = 0
                for s in _res_heap.values():
                    if i == _max_warnings:
                        self.log(_t('    and there are {} more (change GXpy(max_warnings=) to see more)...'.format(
                            len(_res_heap) - i)))
                        break
                    self.log('   ', s)
                    i += 1
            if self._logf:
                self._logf.close()

            atexit.unregister(self._close)
            self.tkframe = None
            self.gxapi = None
            self._sr = None
            del self.license_class
            self._shared_state = {}
            _reset_globals()

    def __init__(self, name=__name__, version=__version__,
                 parent_window=0, log=None,
                 max_res_heap=10000000, res_stack=6, max_warnings=10):

        # singleton class

        _Singleton.__init__(self)
        global gx
        global _max_resource_heap
        global _stack_depth
        global _max_warnings

        if not gx:

            if log is None:
                _max_resource_heap = 0
            else:
                _max_resource_heap = max_res_heap
                _stack_depth = max(0, res_stack)
                _max_warnings = max(0, max_warnings)

            # create a Tkinter parent frame for the viewers

            if not parent_window == 0:
                try:
                    import pythoncom
                except ImportError:
                    raise ImportError(_t(
                        'Was unable to import the pythoncom module. It is needed for any GUI APIs to work within the Geosoft gxpy module.'))

            if parent_window == -1:
                self.tkframe = ttk.Frame(master=None)
                parent_window = self.tkframe.winfo_id()

            self.parent_window = parent_window
            try:
                self.gxapi = gxapi.GXContext.create(name, version, self.parent_window)

            except:
                self.gxapi = None
                raise GXException(_t('GX services are not available.'))

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
                        dts = "{}-{}-{}({}_{}_{}_{})" \
                            .format(self._start.year,
                                    str(self._start.month).zfill(2),
                                    str(self._start.day).zfill(2),
                                    str(self._start.hour).zfill(2),
                                    str(self._start.minute).zfill(2),
                                    str(self._start.second).zfill(2),
                                    str(self._start.microsecond // 1000).zfill(3))
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
                self.log('user path: {}'.format(gxu.folder_user()))

            # create a shared string ref for the convenience of Geosoft modules

            self._sr = gxapi.str_ref()
            atexit.register(self._close)
            gx = self
            self.log('GX open')

            # general properties
            self.current_date = gxapi.GXSYS.date()
            self.current_utc_date = gxapi.GXSYS.utc_date()
            self.current_time = gxapi.GXSYS.time()
            self.current_utc_time = gxapi.GXSYS.utc_time()
            self.license_class = self.license_class()
            self.folder_workspace = gxu.folder_workspace()
            self.folder_temp = gxu.folder_temp()
            self.folder_user = gxu.folder_user()

    def _remove_gx_temporary_folders(self):
        """ removes all GX temporary folders and """

        def file_error(fnc, path, excinfo):
            self.log(_t("error removing temporary file\n   \"{}\"\nfunction \"{}\"\nexception\"{}\"\n")
                     .format(path, str(fnc), str(excinfo)))

        for filename in os.listdir(gxu.folder_temp()):
            folder = os.path.join(gxu.folder_temp(), filename)
            if os.path.isdir(folder) and (len(filename) > 4) and (filename[:4] == '_gx_'):
                warning_file = os.path.join(folder, GX_WARNING_FILE)
                if not os.path.exists(warning_file):
                    shutil.rmtree(folder, ignore_errors=False, onerror=file_error)

    def _log_to_file(self, *args):

        now = datetime.datetime.now()
        dts = "{}-{}-{} {}:{}:{}:{} ".format(now.year,
                                             str(now.month).zfill(2),
                                             str(now.day).zfill(2),
                                             str(now.hour).zfill(2),
                                             str(now.minute).zfill(2),
                                             str(now.second).zfill(2),
                                             str(now.microsecond // 1000).zfill(3))
        for log_str in args:
            for l in str(log_str).split('\n'):
                logstr = dts + l + os.linesep
                self._logf.write(logstr.encode('utf-8'))

    def main_wind_id(self):
        """
        :returns: The main window ID (HWND cast to unsigned for Windows).

        .. versionadded:: 9.1
        """

        if self.parent_window == 0:
            return self.gxapi.get_main_wnd_id()
        else:
            return self.parent_window

    def active_wind_id(self):
        """
        :returns: The active window ID (HWND cast to unsigned for Windows).

        .. versionadded:: 9.1
        """

        return self.gxapi.get_active_wnd_id()

    def disable_app(self):
        """
        Disables application windows to allow modal Python UI.
        Call before opening your own UI window.

        .. versionadded:: 9.1
        """
        self.gxapi.enable_application_windows(False)

    def enable_app(self):
        """
        Enables application windows to allow modal Python UI.
        Call before returning control to OM.

        .. versionadded:: 9.1
        """
        self.gxapi.enable_application_windows(True)

    def entitlements(self):
        """
        :return: The current user entitlements as a dictionary.

        .. versionadded:: 9.1
        """

        lst = gxapi.GXLST.create(1000)
        gxapi.GXSYS.get_entitlement_rights(lst)
        return gxu.dict_from_lst(lst)

    def license_class(self):
        """
        :return: The current license class.

        .. versionadded:: 9.1
        """

        lc = gxapi.str_ref()
        gxapi.GXSYS.get_license_class(lc)
        return lc.value

    def temp_folder(self):
        """
        Return the GX temporary folder path.

        Each GX instance will create an instance-specific temporary folder as a child in the Geosoft 
        temporary folder.  Placing temporary files in the GX-specific temporary folder will ensure 
        temporary file names will not collide with other running GX-based programs, and that all 
        temporarty files are removed on termination of this GX.

        Call `keep_temp_folder` to prevent deletion of the temporary files, which can be useful
        when debugging.

        .. versionadded:: 9.2
        """

        if self._temp_file_folder is None:

            # create a temporary folder for this GX instance

            path = gxu.folder_temp()
            uuid = "_gx_" + self._gxid
            self._temp_file_folder = os.path.join(path, uuid)
            try:
                os.makedirs(self._temp_file_folder, exist_ok=True)
                self._keep_temp_files = False
                warning_file = os.path.join(self._temp_file_folder, GX_WARNING_FILE)
                with open(warning_file, 'w') as active:
                    active.write('This Geosoft temporary folder may be in use.\n')
                    active.write('Modifying or deleting content may may cause a dependant process to fail.')
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
        """
        .. deprecated:: 9.2 replaced by properties.
        """

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

    def log(self, *args):
        """
        Log a string to the log file or log call-back as defined when creating :class:`~gx.GXpy` instance.

        :param args: arguments to log, each will be converted to a str()

        If logging to a file each line is preceded by the date and time:

        .. code::
        
            2016-12-25 12:34:16.175 log_str_line_1
            2016-12-25 12:34:16.175 log_str_line_2

        .. versionadded:: 9.2
        """

        if self._log_it:
            self._log_it(*args)

    def elapsed_seconds(self, tag='', log=False):
        """
        Return the elapsed seconds since this GX instance started.
        The elapsed time is logged if logging is on.

        :param log:     True to log, which also requires logging to be on
        :param tag:     optional string to add to the log
        :return:        elapsed time in seconds

        .. versionadded:: 9.2
        """

        elapsed = datetime.datetime.now() - self._start
        elapsed_seconds = elapsed.seconds + elapsed.microseconds / 1000000.0
        if log:
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
        """
        .. deprecated:: 9.2 use :py:meth:`utility.folder_workspace`
        """
        return gxu.folder_workspace()

    def folder_temp(self):
        """
        .. deprecated: 9.2 use :py:meth:`utility.folder_temp`
        """
        return gxu.folder_temp()

    def folder_user(self):
        """
        .. deprecated: 9.2 use :py:meth:`utility.folder_user`
        """
        return gxu.folder_user()
