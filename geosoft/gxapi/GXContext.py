from . import gxapi_cy

from geosoft.gxapi import GXAPIError, int_ref

import threading
import winreg

_tls = threading.local()


class GXContext:
    """
    The main GX execution context.

    A single instance of this object must be created per thread and persist before using any other class in the
    :py:mod:`.geosoft.gxapi` module.

    .. seealso::

        Class :class:`.gxpy.gx.GXpy`
    """
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self._release_tls_geo:
            _tls._gxa_geo = None

    def __del__(self):
        if self._release_tls_geo:
            _tls._gxa_geo = None

    def __init__(self, wrapper):
        tls_geo = getattr(_tls, '_gxa_geo', None)
        if tls_geo is None:
            _tls._gxa_geo = wrapper
            self._release_tls_geo = True
        else:
            self._release_tls_geo = False

    @classmethod
    def _get_tls_geo(cls):
        tls_geo = getattr(_tls, '_gxa_geo', None)
        if tls_geo is None:
            raise GXAPIError("A GXContext instance has not been created for current thread yet, or the original context has been released.");
        return tls_geo

    @classmethod
    def create(cls, application, version, wind_id = 0, flags = 0, key='Core', per_user_key=False,
               redist_override=False, redist_dir=None, user_dir=None, temp_dir=None):
        """
        Creates the GX execution context (will return the current one if it exists).

        :param application:   Calling application name"
        :param version:       Calling application version
        :param parent_wnd_id: Calling application main window handle (HWND cast to unsigned on Windows) as an int (default 0)
        :param flags:         0 default; 64 suppresses text progress messages; 128 suppresses GUI progress window
        :type  application:   str
        :type  version:       str
        :type  parent_wnd_id: int
        :type  flags:         int

        :returns: A GX execution context.
        :rtype:   GXContext

        .. versionadded:: 9.1
        """
        tls_geo = getattr(_tls, '_gxa_geo', None)
        if tls_geo is None:
            if not cls._geodist_init:
                if redist_override:
                    cls._set_geosoft_redist_overrides(redist_dir, user_dir, temp_dir)
                else:
                    reg_hive = winreg.HKEY_CURRENT_USER if per_user_key else winreg.HKEY_LOCAL_MACHINE
                    env_key = winreg.OpenKey(reg_hive, 'Software\Geosoft\{}\Environment'.format(key), 0, winreg.KEY_READ)
                    try:
                        geosoft_dir, _ = winreg.QueryValueEx(env_key, 'GEOSOFT')
                        cls._geosoft_dist_init(geosoft_dir)
                    finally:
                        winreg.CloseKey(env_key)

            p_geo = gxapi_cy.WrapPGeo()
            p_geo._create(application, version, wind_id, flags)
            return GXContext(p_geo)
        else:
            return GXContext(tls_geo)


    @classmethod
    def _create_internal(cls, internal_p_geo):
        tls_geo = getattr(_tls, '_gxa_geo', None)
        if tls_geo is None:
            p_geo = gxapi_cy.WrapPGeo()
            p_geo._create_internal(internal_p_geo)
            return GXContext(p_geo)
        else:
            return GXContext(tls_geo)

    @classmethod
    def _internal_p(cls):
        p_geo = GXContext._get_tls_geo()
        return p_geo._internal_p()

    _geodist_init = False
    @classmethod
    def _geosoft_dist_init(cls, dist_dir, dll_name='geodist.dll'):
        gxapi_cy.WrapPGeo.geosoft_dist_init(dist_dir, dll_name)
        _geodist_init = True

    @classmethod
    def _set_geosoft_redist_overrides(cls, redist_dir, user_dir, temp_dir, dll_name='geodist.dll'):
        gxapi_cy.WrapPGeo.set_geosoft_redist_overrides(redist_dir, user_dir, temp_dir, dll_name)
        _geodist_init = True

    @classmethod
    def _redirect_std_streams(cls):
        gxapi_cy.WrapPGeo.gx_redirect_std_streams()

    def get_main_wnd_id(self):
        """
        Get the main window handle (0 if not available).

        :returns: Window handle as an int (HWND cast to unsigned on Windows)
        :rtype:   int

        .. versionadded:: 9.1
        """
        p_geo = GXContext._get_tls_geo()
        return p_geo.get_main_wnd()

    def get_active_wnd_id(self):
        """
        Get currently active window (main window, floating document or other popup, 0 if not available).

        :returns: Window handle as an int (HWND cast to unsigned on Windows)
        :rtype:   int

        .. versionadded:: 9.1
        """
        p_geo = GXContext._get_tls_geo()
        return p_geo.get_active_wnd()

    def enable_application_windows(self, enable):
        """
        Used by to prevent user interaction while showing modal windows with APIs where it might be hard to use proper window parenting
        (e.g. in Python with PyQt, tkinter, wxPython etc.). Take care to enable window prior to any calls that need user interaction, e.g.
        The :class:`geosoft.gxapi.GXEMAP` digitization methods.

        :param enable: True to enable, False to disable keyboard and mouse interaction
        :type  enable: bool

        .. versionadded:: 9.1
        """
        p_geo = GXContext._get_tls_geo()
        return p_geo.enable_application_windows(enable)

    def has_ui_console(self):
        """
        Checks if a console owned by UI applications is available

        :returns: True if the parent has UI console.
        :rtype:   bool

        .. versionadded:: 9.1
        """
        p_geo = GXContext._get_tls_geo()
        return p_geo.has_ui_console()
    
    def is_ui_console_visible(self):
        """
        Checks if a console owned by UI applications is visible

        :returns: True if the UI console is visible.
        :rtype:   bool

        .. versionadded:: 9.1
        """
        p_geo = GXContext._get_tls_geo()
        return p_geo.is_ui_console_visible()

    def show_ui_console(self, show):
        """
        Shows or hides console owned by UI applications. Showing the console Will also bring the window to the front if behind 
        other application windows. Has no effect on consoles owning standalone scripts.

        :param show: True to show False to Hide
        :type  show: bool

        .. versionadded:: 9.1
        """
        p_geo = GXContext._get_tls_geo()
        return p_geo.show_ui_console(show)

    def clear_ui_console(self):
        """
        Clears the console owned by UI applications. Has no effect on consoles owning standalone scripts.

        .. versionadded:: 9.1
        """
        p_geo = GXContext._get_tls_geo()
        return p_geo.clear_ui_console()

