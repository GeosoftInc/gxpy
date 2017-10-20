# coding = utf-8

import json
import warnings
from os.path import dirname, join

with open(join(dirname(__file__), 'pkg_info.json')) as fp:
    _info = json.load(fp)

__version__ = "{}{}".format(_info['version'], _info['pre-release'])
version = __version__

__all__ = ['gxapi', 'gxpy']

# docstring overrides for C++ classes inside gxapi module

import geosoft.gxapi as gxapi


gxapi_GXContext___doc__ = '''

The main GX execution context.

A single instance of this object must be created per thread and persist before using any other class in the
:py:mod:`.geosoft.gxapi` module.

.. seealso::

    Class coordinate_system=:class:`.gxpy.gx.GXpy`

'''


gxapi_GXContext_create__doc__ = '''create((str)application, (str)version, (int)parent_wnd_id=0, flags=0) -> GXContext:
Creates the GX execution context (will return the current one if it exists).

:param application: Calling application name (str)"
:param version: Calling application version (str)
:param parent_wnd_id: Calling application main window handle (HWND cast to unsigned on Windows) as an int (default 0)
:param flags: 0 default; 64 suppresses text progress messages; 128 suppresses GUI progress window
:returns: A GX execution context.

.. versionadded:: 9.1

'''

gxapi_GXContext_current__doc__ = '''current() -> GXContext:
Get the current thread's GX execution context (throws if not created yet).

:returns: A GX execution context.

.. versionadded:: 9.1

'''

gxapi_GXContext_get_main_wnd_id__doc__ = '''get_main_wnd_id() -> int:
Get the main window handle (0 if not available).

:returns: Window handle as an int (HWND cast to unsigned on Windows)

.. versionadded:: 9.1

'''

gxapi_GXContext_get_active_wnd_id__doc__ = '''get_active_wnd_id() -> int:
Get currently active window (main window, floating document or other popup, 0 if not available).

:returns: Window handle as an int (HWND cast to unsigned on Windows)

.. versionadded:: 9.1

'''

gxapi_GXContext_enable_application_windows__doc__ = '''enable_application_windows((bool)enable) -> None:
Used by to prevent user interaction while showing modal windows with APIs where it might be hard to use proper window parenting
(e.g. in Python with PyQt, tkinter, wxPython etc.). Take care to enable window prior to any calls that need user interaction, e.g.
The :class:`geosoft.gxapi.GXEMAP` digitization methods.

:param enable: True to enable, False to disable keyboard and mouse interaction
:type enable: bool

.. versionadded:: 9.1

'''

gxapi_GXContext_clear_ui_console__doc__ = '''clear_ui_console() -> None:
Clears the console owned by UI applications. Has no effect on consoles owning standalone scripts.

.. versionadded:: 9.1

'''

gxapi_GXContext_show_ui_console__doc__ = '''show_ui_console((bool)show) -> None:
Shows or hides console owned by UI applications. Showing the console Will also bring the window to the front if behind 
other application windows. Has no effect on consoles owning standalone scripts.

:param show: True to show False to Hide

.. versionadded:: 9.1

'''

gxapi_GXContext_has_ui_console__doc__ = '''has_ui_console() -> bool:
Checks if a console owned by UI applications is available

:returns: True is the parent has UI console.

.. versionadded:: 9.1

'''

