# NOTICE: Do not remove following line! The code generator needs it.
### extends 'init_empty.py'

### block Header
# NOTICE: The code generator will not replace the code in this block

class GXCancel(SystemExit):
    """
    A subclass of `SystemExit <https://docs.python.org/3/library/exceptions.html#SystemExit>`_ which is raised when a 
    script should cleanly exit due to a cancellation condition. Generally not caught since it will have the same effect 
    as :exc:`SystemExit` for both standalone and Oasis montaj extension scripts. Raised from within API by 
    :func:`geosoft.gxapi.GXSYS.cancel()`

    .. versionadded:: 9.1
    """
    pass

class GXExit(SystemExit):
    """
    A subclass of `SystemExit <https://docs.python.org/3/library/exceptions.html#SystemExit>`_ which is raised when a 
    script should cleanly exit due to a completion condition. Generally not caught since it will have the same effect as 
    :exc:`SystemExit` for both standalone and Oasis montaj extension scripts. Raised from within API by 
    :func:`geosoft.gxapi.GXSYS.exit()`

    .. versionadded:: 9.1
    """
    pass

class GXAPIError(RuntimeError):
    """
    A subclass of `RuntimeError <https://docs.python.org/3/library/exceptions.html#RuntimeError>`_ which is raised whenever 
    the GX Python API encounters initialization issues or other API violations. It generally indicates a bug in Python code.

    .. versionadded:: 9.1
    """
    pass


class GXError(RuntimeError):
    """
    A subclass of `RuntimeError <https://docs.python.org/3/library/exceptions.html#RuntimeError>`_ which is raised whenever 
    a GX Python API call encounters an error. Often the message string of these errors are informative to the user (e.g. File 
    'x' is locked in another application) but there could be cases where this is not the case. In most cases an attribute, 
    :attr:`number`, is also available on the exception object that matches the number in the :code:`geosoft.ger` file.
    These numbers instead of the string (which could change or even be translated) should be used to identify and handle
    very specific exceptions.

    .. versionadded:: 9.1
    """
    pass
### endblock Header

### block Constants
# NOTICE: Do not edit anything in this block, it is generated code
class GXGEOSOFTDefines:
    pass
class GX3DNDefines:
    pass
class GXVVDefines:
    pass
### endblock Constants

### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer