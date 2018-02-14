"""
GX Context and related methods required for Geosoft Python.  

:Classes:

    ============= =======================
    :class:`GXpy` the Geosoft GX context
    ============= =======================
    
The GX context is a singleton, which is either created for
stand-alone Python scripts, or is provided to the script for extensions to Geosoft Desktop applications.

.. note::

    Regression tests provide usage examples:     
    `gx tests <https://github.com/GeosoftInc/gxpy/blob/master/geosoft/gxpy/tests/test_gx.py>`_

"""

import tkinter.ttk as ttk
import pprint
import os
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
    Exceptions from :mod:`geosoft.gxpy.gx`.

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


_gx = None
_res_id = 0
_res_heap = {}
_max_resource_heap = 1000000
_stack_depth = 5
_max_warnings = 10
_stale_age = 24.*60*60
_remove_stale_geosoft_temp_files = False
_NULL_ID = -1


def _reset_globals():
    global _gx
    global _res_id
    global _res_heap
    global _max_resource_heap
    global _stack_depth
    global _max_warnings
    _gx = None
    _res_id = 0
    _res_heap = {}
    _max_resource_heap = 1000000
    _stack_depth = 5
    _max_warnings = 10


def track_resource(resource_class, info):
    """
    Track a resource.  Resource tracking is useful for debugging resource leaks.  If you create a class
    or resource that you expect to be removed before your script ends you can track it with this call.
    When you dispose of your resource call :meth:`pop_resource` to remove it from the tracking heap.
    On exit, any resource left on the tracked resource heap will be reported together with the call
    stack for each resource and the information you provided.
    
    :param resource_class: the resource class name
    :param info: some information about the resource
    :returns: resource_id, can be used with :meth:`pop_resource`
    
    .. versionadded:: 9.2
    """
    global _res_id
    global _res_heap
    global _stack_depth
    if _res_id < _max_resource_heap:
        _res_id += 1
        rs = "{}:".format(resource_class)
        for i in range(_stack_depth):
            f = gxs.func_name(i + 2)
            if f is None:
                break
            rs += '<{}'.format(gxs.func_name(i + 2))
        rs += ' [{}]'.format(info)
        _res_heap[_res_id] = rs
        return _res_id
    else:
        return _NULL_ID


def pop_resource(res_id):
    """
    Pop a tracked resource off the resource stack.
    
    :param res_id:  the resource id returned by :meth:`track_resource`
    
    .. versionadded:: 9.2

    .. versionchanged:: 9.3.1
        changed id to res_id to avoid built-in shadow

    """
    if res_id != _NULL_ID:
        if len(_res_heap):
            try:
                del (_res_heap[res_id])
            except KeyError:
                pass


def _log_file_error(fnc, path, excinfo):
    if _gx is not None:
        if hasattr(_gx, 'log'):
            _gx.log(_t("error removing temporary file\n   \"{}\"\nfunction \"{}\"\nexception\"{}\"\n")
                    .format(path, str(fnc), str(excinfo)))


def _remove_stale_gx_temporary_folders():
    """ removes stale gx temporary folders from user's geosoft temp folder"""

    global _stale_age

    for filename in list(os.listdir(gxu.folder_temp(False))):
        ff = os.path.join(gxu.folder_temp(False), filename)
        if os.path.isdir(ff):
            if filename[:4] == '_gx_' or _remove_stale_geosoft_temp_files:
                if not gxu.is_path_locked(ff, age=_stale_age):
                    shutil.rmtree(ff, ignore_errors=False, onerror=_log_file_error)
        elif _remove_stale_geosoft_temp_files:
            if not gxu.is_file_locked(ff, age=_stale_age):
                try:
                    os.remove(ff)
                except IOError as e:
                    _log_file_error('os.remove', ff, e)


def _remove_stale_geosoft_temporary_files():
    """ removes stale geosoft temporary files and folders from user's geosoft temp folder"""

    global _stale_age

    for filename in list(os.listdir(gxu.folder_temp(False))):
        ff = os.path.join(gxu.folder_temp(False), filename)
        if os.path.isdir(ff):
            if filename == 'TempFileStacks':
                for item in list(os.listdir(ff)):
                    item = os.path.join(os.path.join(gxu.folder_temp(False), filename), item)
                    if not gxu.is_file_locked(item, age=_stale_age):
                        gxu.delete_file(item)

            elif not gxu.is_path_locked(ff, age=_stale_age):
                shutil.rmtree(ff, ignore_errors=False, onerror=_log_file_error)
        else:
            if not gxu.is_file_locked(ff, age=_stale_age):
                gxu.delete_file(ff)


def _exit_cleanup():
    global _gx
    global _res_heap
    global _max_warnings
    global _remove_stale_geosoft_temp_files

    if _gx:
        _gx.log('\nGX closing')
        atexit.unregister(_exit_cleanup)

        temp_folder = _gx.temp_folder()
        if temp_folder and (temp_folder != gxu.folder_temp()):
            shutil.rmtree(temp_folder, ignore_errors=False, onerror=_log_file_error)

        _remove_stale_gx_temporary_folders()
        if _remove_stale_geosoft_temp_files:
            _remove_stale_geosoft_temporary_files()

        if len(_res_heap):
            # resources were created but not deleted or removed
            _gx.log(_t('Warning - cleaning up resources that are still open:'))
            i = 0
            for s in _res_heap.values():
                if i == _max_warnings:
                    _gx.log(_t('    and there are {} more (change GXpy(max_warnings=) to see more)...'
                               .format(len(_res_heap) - i)))
                    break
                _gx.log('   ', s)
                i += 1

        _gx._tkframe = None
        _gx._gxapi = None
        _gx._shared_state = {}
        _gx.close_log()

    _reset_globals()


def gx():
    """Returns the `GXpy` instance.  Initializes to default state in not initialized."""
    global _gx
    if _gx is None:
        return GXpy()
    return _gx


class GXpy(_Singleton):
    """
    Geosoft GX context.  This is a singleton class, so subsequent creation returns an instance
    identical to the initial creation. This also means that initialization arguments are ignored
    on a subsequent instantiation.
    
    This class does not need to be instantiated by desktop extensions as the context is provided
    by the Geosoft desktop application.  If called, the desktop context is returned.

    :parameters:
        :name:          application name, default is the script name
        :version:       application version number, default Geosoft version
        :parent_window: ID of the parent window.  A parent window is required for GUI-dependent
                        functions to work.  Set `parent_window=-1` to create a Tkinter frame that
                        provides a default parent window handle for GUI/Viewer functions.
        :log:           name of a file to record logging information, or a call-back function that
                        accepts a string.  Specifying `log=''` will log to a default file named
                        using the current date and time.  If not provided calls to log()
                        are ignored.
        :max_res_heap:  If logging is on, open gxpy resources (like grids, or databases) are tracked.
                        This is the maximum size of resource heap for tracking open resources.
                        Set to 0 to not track resources. On exit, if any resources remain open
                        a warning is logged together with a list of the open resources, each with a
                        call stack to help find the function that created the resources.
        :res_stack:     Depth of the call-stack to report for open-resource warning.
        :max_warnings:  Maximum number of resource warnings to report.
        :suppress_progress: True to suppress progress reporting (default False)

    :Properties:
        :gxapi:             GX context to be used to call geosoft.gxapi methods
        :tkframe:           tkframe for UI applications.  Will be None if a the context was created from a window
                            application.
        :gid:               User's Geosoft ID
        :current_date:      date at start-up
        :current_utc_date:  UTC date at start-up
        :current_time:      time at start-up
        :current_utc_time:  UTC time at start-up
        :folder_workspace:  Geosoft workspace folder
        :folder_temp:       Geosoft temporary folder
        :folder_user:       Geosoft Desktop installation 'user' folder

    :Private properties for special use:
        :_stale_age:        stale temporary files older than this age (in seconds) will be removed upon loss
                            of context.  The default is 24 hours (24*60*60 seconds).
        :__remove_stale_geosoft_temp_files: if True, also remove Geosoft temporary files that may heve
                            been created by other processes. The default is False, in which case only stale temporary
                            files created by geosoft.gxpy processes will be removed.

    :raises:
        :GXException(): if unable to create context

    .. versionadded:: 9.1

    .. versionchanged:: 9.2

        | * `parent_window=-1` creates a Tkinter frame as a parent for scripts that call UI functions.
        | * Added `log` argument to support `log()`.
        | * Made environment dictionary properties, deprecated environment.

    """

    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)

    def __str__(self):
        return "GID: {}, class: {}".format(self.gid, self.license_class)

    def __enter__(self):
        return self

    def __exit__(self, _type, _value, _traceback):
        self.__del__()

    def __del__(self):
        self._refs = self._refs - 1
        if self._refs == 0:
            _exit_cleanup()

    def __init__(self, name=__name__, version=__version__,
                 parent_window=0, log=None,
                 max_res_heap=10000000, res_stack=6, max_warnings=10,
                 suppress_progress=False):

        global _gx
        global _max_resource_heap
        global _stack_depth
        global _max_warnings

        # singleton class, initialize only once
        _Singleton.__init__(self)
        if _gx:
            self._refs = self._refs + 1
            return

        self._refs = 1

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
                    'Unable to import the pythoncom module, which is needed for GUI APIs to work.'))

        if parent_window == -1:
            self._tkframe = ttk.Frame(master=None)
            parent_window = self._tkframe.winfo_id()

        self._parent_window = parent_window
        try:
            flags = 0
            if suppress_progress:
                if self._parent_window:
                    flags = 128
                else:
                    flags = 64
            self._gxapi = gxapi.GXContext.create(name, version, self._parent_window, flags)

        except gxapi.GXAPIError as e:
            self._gxapi = None
            raise GXException(_t('GX services are not available.\n{}'.format(e)))

        user = gxapi.str_ref()
        company = gxapi.str_ref()
        gxapi.GXSYS.get_licensed_user(user, company)
        self.gid = user.value
        self._temp_file_folder = None
        self._keep_temp_files = True

        self._start = datetime.datetime.utcnow()
        self._gxid = gxu.uuid()
        self._entitlements = None

        # general properties
        self.current_date = gxapi.GXSYS.date()
        self.current_utc_date = gxapi.GXSYS.utc_date()
        self.current_time = gxapi.GXSYS.time()
        self.current_utc_time = gxapi.GXSYS.utc_time()
        self.folder_workspace = gxu.folder_workspace()
        self.folder_temp = gxu.folder_temp()
        self.folder_user = gxu.folder_user()

        # determine license
        try:
            # test if we can create a GXST2 instance, which requires a minimal license
            gxapi.GXST2.create()
            self._entitled = True
        except gxapi.GXAPIError:
            self._entitled = False

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

            self.log('\n')
            self.log('-' * 80)
            self.log('UTC:      {}'.format(self._start))
            self.log('Script:   {}'.format(gxs.app_name()))
            self.log('GX API:   {}'.format(__version__))
            self.log('Core API: {}'.format(self.geosoft_version_label))
            self.log('BIN_PATH: {}'.format(os.environ.get('GX_GEOSOFT_BIN_PATH', 'default')))
            self.log('Project:  {}'.format(gxu.folder_workspace()))
            self.log('GID:      {}'.format(self.gid))
            self.log('Entitled: {}'.format(self.entitled))
            self.log('-' * 80)
            self.log('\n')

        # save context as a global
        _gx = self
        atexit.register(_exit_cleanup)
        self.log('\nGX open')

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

    @property
    def gxapi(self):
        """gxapi context for calls to geosoft.gxapi"""
        return self._gxapi

    @property
    def tkframe(self):
        """tkframe if created fro this context, None if not created"""
        return self._tkframe

    @property
    def parent_window(self):
        """parent window for this context"""
        return self._parent_window

    @property
    def version(self):
        """
        API version description

        .. versionadded:: 9.3
        """
        return __version__

    @property
    def main_wind_id(self):
        """
        The main window ID (HWND cast to unsigned for Windows).

        .. versionadded:: 9.1
        """

        if self._parent_window == 0:
            return self._gxapi.get_main_wnd_id()
        else:
            return self._parent_window

    @property
    def active_wind_id(self):
        """
        The active window ID (HWND cast to unsigned for Windows).

        .. versionadded:: 9.1
        """

        return self._gxapi.get_active_wnd_id()

    @property
    def geosoft_name(self):
        """
        Geosoft installed product name

        .. versionadded:: 9.3.2
        """
        i = gxapi.str_ref()
        gxapi.GXSYS.get_sys_info(gxapi.SYS_INFO_PRODUCTNAME, i)
        return i.value


    @property
    def geosoft_build_label(self):
        """
        Geosoft build label.

        .. versionadded:: 9.3.2
        """
        i = gxapi.str_ref()
        gxapi.GXSYS.get_sys_info(gxapi.SYS_INFO_BUILD_LABEL, i)
        return i.value

    @property
    def geosoft_build_number(self):
        """
        Geosoft build numberl.

        .. versionadded:: 9.3.2
        """
        i = gxapi.str_ref()
        gxapi.GXSYS.get_sys_info(gxapi.SYS_INFO_BUILD_NUMBER, i)
        return int(i.value)

    @property
    def geosoft_version_label(self):
        """
        Geosoft version label.

        .. versionadded:: 9.3.2
        """
        i = gxapi.str_ref()
        gxapi.GXSYS.get_sys_info(gxapi.SYS_INFO_VERSION_LABEL, i)
        return i.value

    @property
    def geosoft_version_major(self):
        """
        Geosoft major version number.

        .. versionadded:: 9.3.2
        """
        i = gxapi.str_ref()
        gxapi.GXSYS.get_sys_info(gxapi.SYS_INFO_VERSION_MAJOR, i)
        return int(i.value)

    @property
    def geosoft_version_minor(self):
        """
        Geosoft minor version number.

        .. versionadded:: 9.3.2
        """
        i = gxapi.str_ref()
        gxapi.GXSYS.get_sys_info(gxapi.SYS_INFO_VERSION_MINOR, i)
        return int(i.value)

    @property
    def geosoft_version_micro(self):
        """
        Geosoft micro version number.

        .. versionadded:: 9.3.2
        """
        i = gxapi.str_ref()
        gxapi.GXSYS.get_sys_info(gxapi.SYS_INFO_VERSION_SP, i)
        return int(i.value)

    def disable_app(self):
        """
        Disables application windows to allow modal Python UI.
        Call before opening your own UI window.

        .. versionadded:: 9.1
        """
        self._gxapi.enable_application_windows(False)

    def enable_app(self):
        """
        Enables application windows to allow modal Python UI.
        Call before returning control to OM.

        .. versionadded:: 9.1
        """
        self._gxapi.enable_application_windows(True)

    def entitlements(self):
        """
        :returns: The current user entitlements as a dictionary.

        .. versionadded:: 9.1
        """

        if not self._entitlements:
            lst = gxapi.GXLST.create(1000)
            gxapi.GXSYS.get_entitlement_rights(lst)
            self._entitlements = gxu.dict_from_lst(lst)
        return self._entitlements

    def has_entitlement(self, ent):
        """
        Returns True if the user has this entitlement.

        :param ent: Entitlement number or descriptive name (case sensitive)

        | Partial list of entitlements as of 9.3 platform (subject to change):
        |    1000: "Oasis montaj™ Base"
        |    10000: "Oasis montaj™ Mapping and Processing System"
        |    100010: "Geosoft - Virtual Computer License"
        |    10100: "Geophysics"
        |    10101: "Geochemistry"
        |    10102: "Drillhole Plotting"
        |    10103: "Induced Polarization"
        |    10104: "Geophysics Levelling"
        |    10105: "MAGMAP Filtering"
        |    10106: "Grav/Mag Interpretation"
        |    10107: "Airborne Quality Control"
        |    10108: "256-Channel Radiometric Processing"
        |    10109: "Gravity and Terrain Correction"
        |    10110: "GridKnit"
        |    10111: "UXO Land"
        |    10114: "UXO Marine"
        |    10500: "montaj plus™ Modeling Lite (PotentQ)"
        |    10520: "GM-SYS Basic Profile Modeling"
        |    10521: "GM-SYS Intermediate Profile Modeling"
        |    10522: "GM-SYS Advanced Profile Modeling"
        |    10523: "GM-SYS 3D Modeling"
        |    10524: "Depth to Basement"
        |    10525: "Isostatic Residual"
        |    10540: "montaj plus™ Grav/Mag Filtering"
        |    10541: "montaj plus™ Compudrape"
        |    10550: "montaj plus™ Praga Radiometric Processing System"
        |    10560: "montaj plus™ CET Grid Analysis"
        |    10561: "montaj plus™ CET Porphyry Analysis"
        |    2000: "ArcGIS"
        |    3000: "MapInfo"
        |    30000: "Target™ Surface and Drillhole Mapping"
        |    30101: "Target™ Geochemistry"
        |    40000: "Target™ for ArcGIS Surface and Drillhole Mapping"
        |    41000: "Geochemistry for ArcGIS"
        |    5104: "montaj™ Geophysics Leveling - Basic"
        |    5106: "montaj™ Grav/Mag Interpretation - Basic"

        .. versionadded:: 9.3
        """

        ent = str(ent)
        if ent in self.entitlements().keys():
            return True
        if ent in self.entitlements().values():
            return True
        return False

    @property
    def entitled(self):
        """
        True if this user has a minimal Geosoft desktop licence/entitlement

        .. versionadded:: 9.3
        """
        return self._entitled

    @property
    def license_class(self):
        """
        The user's license class.

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

        :param ext: optional extension
        :returns:   uuid-based file name in the instance temporary folder.

        .. versionadded:: 9.2
        """

        if ext and ext[0] != '.':
            ext = '.' + ext
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
        Log a string to the log file or log call-back as defined when creating :class:`GXpy` instance.

        :param args: arguments to log, each will be converted to a str()

        If logging to a file each line is preceded by the date and time:

        .. code::
        
            2016-12-25 12:34:16.175 log_str_line_1
            2016-12-25 12:34:16.175 log_str_line_2

        .. versionadded:: 9.2
        """

        if self._log_it:
            self._log_it(*args)

    def close_log(self):
        """close logging"""
        self.log('GX closed')
        if self._logf:
            self._logf.close()

    def elapsed_seconds(self, tag='', log=False):
        """
        Return the elapsed seconds since this GX instance started.
        The elapsed time is logged if logging is on.

        :param log:     True to log, which also requires logging to be on
        :param tag:     optional string to add to the log
        :returns:       elapsed time in seconds

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
        .. deprecated:: 9.2 use :meth:`geosoft.gxpy.utility.folder_workspace`
        """
        if self:
            return gxu.folder_workspace()

    def folder_temp(self):
        """
        .. deprecated:: 9.2 use :meth:`geosoft.gxpy.utility.folder_temp`
        """
        if self:
            return gxu.folder_temp()

    def folder_user(self):
        """
        .. deprecated:: 9.2 use :meth:`geosoft.gxpy.utility.folder_user`
        """
        if self:
            return gxu.folder_user()
