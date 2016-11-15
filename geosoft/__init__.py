# coding = utf-8

import json
from os.path import dirname, join

with open(join(dirname(__file__), 'pkg_info.json')) as fp:
    _info = json.load(fp)

__version__ = "{}{}".format(_info['version'], _info['pre-release'])

__all__ = ['gxapi', 'gxpy']


# docstring overrides for C++ classes inside gxapi module

import geosoft.gxapi as gxapi

gxapi.GXCancel.__doc__ = '''
A subclass of `SystemExit <https://docs.python.org/3/library/exceptions.html#SystemExit>`_ which is raised when a 
script should cleanly exit due to a cancellation condition. Generally not caught since it will have the same effect 
as :exc:`SystemExit` for both standalone and Oasis montaj extension scripts. Raised from within API by 
:func:`geosoft.gxapi.GXSYS.cancel()`

.. versionadded:: 9.1
'''

gxapi.GXExit.__doc__ = '''
A subclass of `SystemExit <https://docs.python.org/3/library/exceptions.html#SystemExit>`_ which is raised when a script 
should cleanly exit due to a completion condition. Generally not caught since it will have the same effect as 
:exc:`SystemExit` for both standalone and Oasis montaj extension scripts. Raised from within API by 
:func:`geosoft.gxapi.GXSYS.exit()`

.. versionadded:: 9.1
'''

gxapi.GXAPIError.__doc__ = '''
   A subclass of `RuntimeError <https://docs.python.org/3/library/exceptions.html#RuntimeError>`_ which is raised whenever 
   the GX Python API encounters initialization issues or other API violations. It generally indicates a bug in Python code.

   .. versionadded:: 9.1
'''

gxapi.GXError.__doc__ = '''
A subclass of `RuntimeError <https://docs.python.org/3/library/exceptions.html#RuntimeError>`_ which is raised whenever 
a GX Python API call encounters an error. Often the message string of these errors are informative to the user (e.g. File 
'x' is locked in another application) but there could be cases where this is not the case. In most cases an attribute, 
:attr:`number`, is also available on the exception object that matches the number in the :code:`geosoft.ger` file.
These numbers instead of the string (which could change or even be translated) should be used to identify and handle
very specific exceptions.

.. versionadded:: 9.1
'''

gxapi.GXContext.__doc__ = '''The main GX execution context

A single instance of this object needs to be created per thread and persisted before using any other class in the
geosoft.gxapi module.

'''

gxapi.GXContext.create.__doc__ = '''create((str)application, (str)version, (int)parent_wnd_id = 0) -> GXContext:
Creates the GX execution context (will return the current one if it exists).

:param application: Calling application name"
:type application: str
:param version: Calling application version
:type version: str
:param parent_wnd_id: Calling application main window handle (HWND cast to unsigned on Windows) as an int (default 0)
:type parent_wnd_id: int
:returns: A GX execution context.
:rtype: geosoft.gxapi.GXContext

.. versionadded:: 9.1

'''

gxapi.GXContext.current.__doc__ = '''current() -> GXContext:
Get the current thread's GX execution context (throws if not created yet).

:returns: A GX execution context.
:rtype: geosoft.gxapi.GXContext

.. versionadded:: 9.1

'''

gxapi.GXContext.get_main_wnd_id.__doc__ = '''get_main_wnd_id() -> int:
Get the main window handle (0 if not available).

:returns: Window handle as an int (HWND cast to unsigned on Windows)
:rtype: int

.. versionadded:: 9.1

'''

gxapi.GXContext.get_active_wnd_id.__doc__ = '''get_active_wnd_id() -> int:
Get currently active window (main window, floating document or other popup, 0 if not available).

:returns: Window handle as an int (HWND cast to unsigned on Windows)
:rtype: int

.. versionadded:: 9.1

'''

gxapi.GXContext.enable_application_windows.__doc__ = '''enable_application_windows((bool)enable) -> None:
Used by to prevent user interaction while showing modal windows with APIs where it might be hard to use proper window parenting
(e.g. in Python with PyQt, tkinter, wxPython etc.). Take care to enable window prior to any calls that need user interaction, e.g.
The :class:`geosoft.gxapi.GXEMAP` digitization methods.

:param enable: True to enable, False to disable keyboard and mouse interaction
:type enable: bool
:returns: Nothing
:rtype: None

.. versionadded:: 9.1

'''

gxapi.GXContext.clear_ui_console.__doc__ = '''clear_ui_console() -> None:
Clears the console owned by UI applications. Has no effect on consoles owning standalone scripts.

:returns: Nothing
:rtype: None

.. versionadded:: 9.1

'''

gxapi.GXContext.show_ui_console.__doc__ = '''show_ui_console((bool)show) -> None:
Shows or hides console owned by UI applications. Showing the console Will also bring the window to the front if behind 
other application windows. Has no effect on consoles owning standalone scripts.

:param show: True to show False to Hide
:type show: bool
:returns: Nothing
:rtype: None

.. versionadded:: 9.1

'''

gxapi.GXContext.has_ui_console.__doc__ = '''has_ui_console() -> bool:
Checks if a console owned by UI applications is available

:returns: Window handle as an int (HWND cast to unsigned on Windows)
:rtype: bool

.. versionadded:: 9.1

'''

