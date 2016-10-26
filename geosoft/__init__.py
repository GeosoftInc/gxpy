# coding = utf-8

import json
from os.path import dirname, join

import geosoft.__check_deps__

with open(join(dirname(__file__), 'pkg_info.json')) as fp:
    _info = json.load(fp)
__version__ = _info['version']
__branch__ = _info['branch']

if __branch__ == 'release':
    __release__ = _info['version']
else:
    __release__ = "{}.{}0".format(_info['version'], _info['branch'])

__all__ = ['gxapi', 'gxpy']


# docstring overrides for C++ classes inside gxapi module

import geosoft.gxapi as gxapi

gxapi.GXCancel.__doc__ = "TODO"

gxapi.GXExit.__doc__ = "TODO"

gxapi.GXAPIError.__doc__ = "TODO"

gxapi.GXError.__doc__ = "TODO"

gxapi.GXContext.__doc__ = '''The main GX execution context

A single instance of this object needs to be created per thread and persisted before using any other class in the geosoft.gxapi module.

'''

gxapi.GXContext.create.__doc__ = '''create((str)application, (str)version, (int)parent_wnd_id = 0) -> GXContext:
Creates the GX execution context (will return the current one if it exsists already).

:param application: Calling application name"
:type application: str
:param version: Calling application version
:type version: str
:param parent_wnd_id: Calling application main window handle (HWND cast to unsigned on Windows) as an int (default 0)
:type parent_wnd_id: int
:returns: A GX execution context.
:rtype: geosoft.gxapi.GXContext

.. versionadded:: 9.1.0

'''

gxapi.GXContext.current.__doc__ = '''current() -> GXContext:
Get the current thread's GX execution context (throws if not created yet).

:returns: A GX execution context.
:rtype: geosoft.gxapi.GXContext

.. versionadded:: 9.1.0

'''

gxapi.GXContext.get_main_wnd_id.__doc__ = '''get_main_wnd_id() -> int:
Get the main window handle (0 if not available).

:returns: Window handle as an int (HWND cast to unsigned on Windows)
:rtype: int

.. versionadded:: 9.1.0

'''

gxapi.GXContext.get_active_wnd_id.__doc__ = '''get_active_wnd_id() -> int:
Get currently active window (main window, floating document or other popup, 0 if not available).

:returns: Window handle as an int (HWND cast to unsigned on Windows)
:rtype: int

.. versionadded:: 9.1.0

'''

gxapi.GXContext.enable_application_windows.__doc__ = '''enable_application_windows((bool)enable) -> None:
Used by to prevent user interaction while showing modal windows with APIs where it might be hard to use proper window parenting
(e.g. in Python with PyQt, tkinter, wxPython etc.). Take care to enable window prior to any calls that need user interaction, e.g.
The :class:`geosoft.gxapi.GXEMAP` digitization methods.

:param enable: True to enable, False to disable keyboard and mouse interaction
:type enable: bool
:returns: Nothing
:rtype: None

.. versionadded:: 9.1.0

'''

gxapi.GXContext.clear_ui_console.__doc__ = '''clear_ui_console() -> None:
:returns: Nothing
:rtype: None

.. versionadded:: 9.1.0

'''

gxapi.GXContext.show_ui_console.__doc__ = '''show_ui_console((bool)show) -> None:
:param show: True to show False to Hide
:type show: bool
:returns: Nothing
:rtype: None

.. versionadded:: 9.1.0

'''

gxapi.GXContext.has_ui_console.__doc__ = '''has_ui_console() -> bool:
:returns: Window handle as an int (HWND cast to unsigned on Windows)
:rtype: bool

.. versionadded:: 9.1.0

'''

gxapi.GXContext.has_ui_console.__doc__ = '''has_ui_console() -> bool:
:returns: Window handle as an int (HWND cast to unsigned on Windows)
:rtype: bool

.. versionadded:: 9.1.0

'''

