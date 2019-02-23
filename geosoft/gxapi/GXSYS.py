### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXRA import GXRA
from .GXWA import GXWA


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXSYS(gxapi_cy.WrapSYS):
    """
    GXSYS class.

    The `GXSYS <geosoft.gxapi.GXSYS>` library functions perform a wide range functions,
    including the storage and retrieval of named parameters
    from the current workspace; writing messages to the user;
    display of progress bars; retrieving file, date and time
    information from the operating system; and providing warning
    and error handling functions.

    **Note:**

    PARAMETER CONTROL FUNCTIONS

    Parameters can be named with an index extension.
    For example, a parameter could be named as "PARM[1]".
    The index can be a positive number, or it can be a '*'.

    If the index is a '*' in `set_string <geosoft.gxapi.GXSYS.set_string>`, then the value string
    will be parsed into multiple values. Commas are assumed to be delimiters.

    E.g.

    ::

       "group1",
       "multiparm[*]",
       "value1,\\"value,2\\",\\"value 3\\",  value4  ,\\"value 5 \\""


    Will set:

    ::

        multiparm[0] ="value1"
        multiparm[1] ="value,2"
        multiparm[2] ="value 3"
        multiparm[3] ="value4"
        multiparm[4] ="value 5"

    To read a parameter, name the parameter with the index.  There is no
    looped-reading ability. For example using the following with `gt_string <geosoft.gxapi.GXSYS.gt_string>`:

    ``"group1","multiparm[3]",setting``

    will return:

    ``setting = "value4"``
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSYS <geosoft.gxapi.GXSYS>`
        
        :returns: A null `GXSYS <geosoft.gxapi.GXSYS>`
        :rtype:   GXSYS
        """
        return GXSYS()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Date/Time


    @classmethod
    def break_date(cls, date, year, month, day):
        """
        Breaks a decimal date value into year, month and day.
        
        :param date:   Date value to break
        :param year:   Year
        :param month:  Month (0-11)
        :param day:    Day   (0-30)
        :type  date:   float
        :type  year:   int_ref
        :type  month:  int_ref
        :type  day:    int_ref

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        year.value, month.value, day.value = gxapi_cy.WrapSYS._break_date(GXContext._get_tls_geo(), date, year.value, month.value, day.value)
        



    @classmethod
    def dateto_long(cls, date):
        """
        Converts a double date to a value representing total
        days elapsed since day 0 of year 0. This uses the
        Numerical Receipies Julian function.
        
        :param date:  Date
        :type  date:  float

        :returns:     x - Days
        :rtype:       int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._dateto_long(GXContext._get_tls_geo(), date)
        return ret_val



    @classmethod
    def timeto_long(cls, time):
        """
        Converts decimal hours to seconds in a day.
        
        :param time:  Time
        :type  time:  float

        :returns:     x - Seconds (integer)
        :rtype:       int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._timeto_long(GXContext._get_tls_geo(), time)
        return ret_val



    @classmethod
    def date(cls):
        """
        Returns the current date in decimal years.
        

        :returns:    Date in decimal years.
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The FormatDate_STR function can be used to convert a date to
        a string.
        """
        ret_val = gxapi_cy.WrapSYS._date(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def longto_date(cls, days):
        """
        Converts a value representing total days elapsed since
        day 0 of year 0 to a geosoft date. This uses the
        Numerical Receipies Julian function.
        
        :param days:  Day
        :type  days:  int

        :returns:     x - Date
        :rtype:       float

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._longto_date(GXContext._get_tls_geo(), days)
        return ret_val



    @classmethod
    def longto_time(cls, sec):
        """
        Converts seconds to decimal hours.
        
        :param sec:  Seconds
        :type  sec:  int

        :returns:    x - Time
        :rtype:      float

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._longto_time(GXContext._get_tls_geo(), sec)
        return ret_val



    @classmethod
    def make_date(cls, year, month, day):
        """
        Returns the decimal date given the year, month and day.
        
        :param year:   Year
        :param month:  Month (0-11)
        :param day:    Day   (0-30)
        :type  year:   int
        :type  month:  int
        :type  day:    int

        :returns:      Date in decimal years.
        :rtype:        float

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._make_date(GXContext._get_tls_geo(), year, month, day)
        return ret_val



    @classmethod
    def secondsto_time(cls, sec):
        """
        Converts fractional seconds to decimal hours.
        
        :param sec:  Seconds
        :type  sec:  float

        :returns:    x - Time
        :rtype:      float

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._secondsto_time(GXContext._get_tls_geo(), sec)
        return ret_val



    @classmethod
    def time(cls):
        """
        Returns the current time in decimal hours.
        

        :returns:    Time in decimal hours.
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The FormatTime_STR function can be used to convert a time to
        a string.
        """
        ret_val = gxapi_cy.WrapSYS._time(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def timeto_seconds(cls, time):
        """
        Converts decimal hours to seconds in a day fractional
        
        :param time:  Time
        :type  time:  float

        :returns:     x - Number of seconds with fractions
        :rtype:       float

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._timeto_seconds(GXContext._get_tls_geo(), time)
        return ret_val



    @classmethod
    def utc_date(cls):
        """
        Returns the current UTC date in decimal years.
        

        :returns:    Date in decimal years.
        :rtype:      float

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The FormatDate_STR function can be used to convert a date to
        a string.
        """
        ret_val = gxapi_cy.WrapSYS._utc_date(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def utc_time(cls):
        """
        Returns the current UTC time in decimal hours.
        

        :returns:    Time in decimal hours.
        :rtype:      float

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The FormatTime_STR function can be used to convert a time to
        a string.
        """
        ret_val = gxapi_cy.WrapSYS._utc_time(GXContext._get_tls_geo())
        return ret_val




# Environment


    @classmethod
    def exist_env(cls, parm):
        """
        Check if setting exists in environment.
        
        :param parm:  Setting
        :type  parm:  str

        :returns:     1 - Yes
                      0 - No
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._exist_env(GXContext._get_tls_geo(), parm.encode())
        return ret_val



    @classmethod
    def get_env(cls, parm, set):
        """
        Get an environment setting.
        
        :param parm:  Setting
        :param set:   Value string
        :type  parm:  str
        :type  set:   str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        set.value = gxapi_cy.WrapSYS._get_env(GXContext._get_tls_geo(), parm.encode(), set.value.encode())
        



    @classmethod
    def set_env(cls, parm, set):
        """
        Set an environment setting.
        
        :param parm:  Setting
        :param set:   Value
        :type  parm:  str
        :type  set:   str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._set_env(GXContext._get_tls_geo(), parm.encode(), set.encode())
        




# Error Handling


    @classmethod
    def clear_err_ap(cls):
        """
        This method is called at to clear all registered errors.
        

        :returns:    0 - Successful
        :rtype:      int

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._clear_err_ap(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_top_error_ap(cls):
        """
        Get the error number of the last registered error.
        

        :returns:    The top error number registered, 0 if none registered.
        :rtype:      int

        .. versionadded:: 8.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._get_top_error_ap(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_error_ap(cls, err):
        """
        Get the error number of an error.
        
        :param err:  The error index (0 to N-1, where N=number of registered errors)
        :type  err:  int

        :returns:    The error number registered, 0 if none registered.
        :rtype:      int

        .. versionadded:: 9.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._get_error_ap(GXContext._get_tls_geo(), err)
        return ret_val



    @classmethod
    def get_error_message_ap(cls, err, err_str):
        """
        Return the error message text as a string.
        
        :param err:      The error index (0 to N-1, where N=number of registered errors)
        :param err_str:  Buffer to return message in
        :type  err:      int
        :type  err_str:  str_ref

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This wrapper is mostly for use outside of GXs,
        because in general if an error is registered in a GX
        the GX would terminate before it could be called.
        Use `num_errors_ap <geosoft.gxapi.GXSYS.num_errors_ap>` to get the number of registered errors.
        """
        err_str.value = gxapi_cy.WrapSYS._get_error_message_ap(GXContext._get_tls_geo(), err, err_str.value.encode())
        



    @classmethod
    def num_errors_ap(cls):
        """
        Returns the number of registered errors.
        

        :returns:    The number of registered errors.
        :rtype:      int

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This wrapper is mostly for use outside of GXs,
        because in general if an error is registered in a GX
        the GX would terminate before it could be called.

        .. seealso::

            GetErrorMessageAP_SYS
        """
        ret_val = gxapi_cy.WrapSYS._num_errors_ap(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def set_server_messages_ap(cls, flag):
        """
        Control the server message handling.
        
        :param flag:  1 - Display messages, 0 - messages reported as errors
        :type  flag:  int

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Should be set to false when dialogs should not
        appear. This setting is thread specific.
        """
        gxapi_cy.WrapSYS._set_server_messages_ap(GXContext._get_tls_geo(), flag)
        




# Execution


    @classmethod
    def run(cls, command, args, process):
        """
        Run a command line process.
        
        :param command:  Command name
        :param args:     Command line arguments
        :param process:  Flags :ref:`SYS_RUN_TYPE` :ref:`SYS_RUN_DISPLAY` :ref:`SYS_RUN_HOLD` :ref:`SYS_RUN_WIN`
        :type  command:  str
        :type  args:     str
        :type  process:  int

        :returns:        -1 if failed to execute task
                         Exit status of the task
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The Default option for each define below is the first one
        and is set to 0.

        We look for the command object in the following order:

        1. the local working directory
        2. the <geosoft>\\bin directory
        3. the system path
        """
        ret_val = gxapi_cy.WrapSYS._run(GXContext._get_tls_geo(), command.encode(), args.encode(), process)
        return ret_val



    @classmethod
    def run_gs(cls, gs):
        """
        Run a GS.
        
        :param gs:  Name of GS to run.
        :type  gs:  str

        :returns:    Exit status of the GS
                    -1 cancelled
                    0 success
                    1 ended with an error.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `set_interactive <geosoft.gxapi.GXSYS.set_interactive>`, `run_gx <geosoft.gxapi.GXSYS.run_gx>`
        """
        ret_val = gxapi_cy.WrapSYS._run_gs(GXContext._get_tls_geo(), gs.encode())
        return ret_val



    @classmethod
    def run_gx(cls, gx):
        """
        Run a GX.
        
        :param gx:  Name of GX to run.
        :type  gx:  str

        :returns:    Exit status of the GX:
                    -1 cancelled
                    0 success
                    1 ended with an error.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the called GX returns an error, they will not be
        displayed until the "top" calling GX terminates, unless you
        call `show_error <geosoft.gxapi.GXSYS.show_error>`.

        .. seealso::

            `run_gx_ex <geosoft.gxapi.GXSYS.run_gx_ex>`, `set_interactive <geosoft.gxapi.GXSYS.set_interactive>` and `run_gs <geosoft.gxapi.GXSYS.run_gs>`
        """
        ret_val = gxapi_cy.WrapSYS._run_gx(GXContext._get_tls_geo(), gx.encode())
        return ret_val



    @classmethod
    def run_gx_ex(cls, gx, ret):
        """
        Run a GX.
        
        :param gx:   Name of GX to run.
        :param ret:  Return value set in the child GX (0 by default)
        :type  gx:   str
        :type  ret:  int_ref

        :returns:    Exit status of the GX:
                     -1 cancelled
                     0 success
                     1 ended with an error.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `run_gx <geosoft.gxapi.GXSYS.run_gx>`, `set_return <geosoft.gxapi.GXSYS.set_return>`
        """
        ret_val, ret.value = gxapi_cy.WrapSYS._run_gx_ex(GXContext._get_tls_geo(), gx.encode(), ret.value)
        return ret_val



    @classmethod
    def run_pdf(cls, mnu, pdf):
        """
        Run a PDF.
        
        :param mnu:  Group name, can be "".
        :param pdf:  PDF name    (.pdf assumed)
        :type  mnu:  str
        :type  pdf:  str

        :returns:    Exit status of the task, 0 usually means success.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The group name of the PDF variables will be "group_pdf",
        where "group" is the name given in the first argument,
        and "pdf" is the root PDF file name.
        """
        ret_val = gxapi_cy.WrapSYS._run_pdf(GXContext._get_tls_geo(), mnu.encode(), pdf.encode())
        return ret_val



    @classmethod
    def shell_execute(cls, verb, file, parameters, directory, show):
        """
        Call Microsoft ShellExecute function (See `MSDN <https://msdn.microsoft.com/en-us/library/windows/desktop/bb762153(v=vs.85).aspx>`_)
        
        :param verb:        Verb
        :param file:        File
        :param parameters:  Parameters
        :param directory:   Directory
        :param show:        :ref:`SHELL_EXECUTE`
        :type  verb:        str
        :type  file:        str
        :type  parameters:  str
        :type  directory:   str
        :type  show:        int

        :returns:           return value of ShellExecute as documented on MSDN
        :rtype:             int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `do_command <geosoft.gxapi.GXSYS.do_command>`
        """
        ret_val = gxapi_cy.WrapSYS._shell_execute(GXContext._get_tls_geo(), verb.encode(), file.encode(), parameters.encode(), directory.encode(), show)
        return ret_val



    @classmethod
    def set_return(cls, ret):
        """
        Set the return value of a GX.
        
        :param ret:  Return Value
        :type  ret:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This value is returned in the `run_gx_ex <geosoft.gxapi.GXSYS.run_gx_ex>` call only.
        """
        gxapi_cy.WrapSYS._set_return(GXContext._get_tls_geo(), ret)
        




# External DLL


    @classmethod
    def do_command(cls, command):
        """
        Execute an Oasis montaj command.
        
        :param command:  Command
        :type  command:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Commands syntax:  "[type] command"

        =======  ============================================================================================
        type     command
        =======  ============================================================================================
        ID       Internal Menu Command (as found in omn and geobar files e.g. ``*ID_EDIT_SELECT``)
        -------  --------------------------------------------------------------------------------------------
        GX       gx file name
        -------  --------------------------------------------------------------------------------------------
        GS       gs file name
        -------  --------------------------------------------------------------------------------------------
        DOTNET   dll file name 
                 Use qualifiers to specify class and method e.g.:
                 ``"[DOTNET] geogxnet.dll(Geosoft.GX.NewGDB.NewGDB;Run)"``
        -------  --------------------------------------------------------------------------------------------
        PDF      Geosoft pdf file name (Not Adobe PDF document, a legacy Geosoft Sushi script)
        -------  --------------------------------------------------------------------------------------------
        DOS      DOS style command
        -------  --------------------------------------------------------------------------------------------
        HLP      help file name
        =======  ============================================================================================

        The must be ONE space between the "]" and the command.  For example:

        ``"[ID] ID_EDIT_SELECT"``  // bring up the line edit tool

        .. seealso::

            `shell_execute <geosoft.gxapi.GXSYS.shell_execute>`
        """
        gxapi_cy.WrapSYS._do_command(GXContext._get_tls_geo(), command.encode())
        



    @classmethod
    def error(cls, error_file, module, error):
        """
        Register an error message
        
        :param error_file:  Your error file name, "" if none.
        :param module:      Module name in which error occurred.
        :param error:       Error number
        :type  error_file:  str
        :type  module:      str
        :type  error:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Use this function to register your own error
        messages when an error occurs in your code.  Your
        errors can be provided in your own `GXGER <geosoft.gxapi.GXGER>` file.  See
        GEOSOFT.`GXGER <geosoft.gxapi.GXGER>` for an example of the `GXGER <geosoft.gxapi.GXGER>` file format.

        If the error # is not found in your error file, the
        OE32.`GXGER <geosoft.gxapi.GXGER>` file, then the GEOSOFT.`GXGER <geosoft.gxapi.GXGER>` file will be
        searched.
        """
        gxapi_cy.WrapSYS._error(GXContext._get_tls_geo(), error_file.encode(), module.encode(), error)
        



    @classmethod
    def error_tag(cls, tag, set):
        """
        Set an error message tag string
        
        :param tag:  Tag string, ie "%1".
        :param set:  String to replace the tag.
        :type  tag:  str
        :type  set:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Use this method to replace tag strings in your error
        message text with run-time information.  For example,
        Geosoft error messages often use the tag strings "%1",
        "%2", etc. as place holders to be replaced by a string
        which is only known at run-time.
        """
        gxapi_cy.WrapSYS._error_tag(GXContext._get_tls_geo(), tag.encode(), set.encode())
        



    @classmethod
    def assert_gx(cls, exp, mod, parm):
        """
        DLL function argument error assertion
        
        :param exp:   Boolean expression (ie. (dB != 0.0) )
        :param mod:   Module name
        :param parm:  Argument name
        :type  exp:   int
        :type  mod:   str
        :type  parm:  str

        :returns:     0 assertion passed
                      1 assertion failed
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Use this function to evaluate errors in passed
        function arguments.  Functions called by GX programs
        should be tolerant of all errors in the passed argument
        list.  The `assert_gx <geosoft.gxapi.GXSYS.assert_gx>` can be used to test each
        argument before doing any work in the function.  If
        an assertion fails, an error will be registered with
        the name of the function and the parameter name and
        a 1 will be returned.  The caller should immediatley
        cleaning up (if necessary) and return.

        You could also test the validity of arguments and call
        the `error <geosoft.gxapi.GXSYS.error>`, `error_tag <geosoft.gxapi.GXSYS.error_tag>` and `terminate <geosoft.gxapi.GXSYS.terminate>`
        functions if you would like to provide a more specific
        error message.
        """
        ret_val = gxapi_cy.WrapSYS._assert_gx(GXContext._get_tls_geo(), exp, mod.encode(), parm.encode())
        return ret_val



    @classmethod
    def ole_automation(cls, object, info_str, info_val):
        """
        Call OLE Automation designed to be called from Montaj.
        
        :param object:    Object Name
        :param info_str:  Info String
        :param info_val:  Info Int
        :type  object:    str
        :type  info_str:  str
        :type  info_val:  int

        :returns:         Return from automation engine.
        :rtype:           int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapSYS._ole_automation(GXContext._get_tls_geo(), object.encode(), info_str.encode(), info_val)
        return ret_val



    @classmethod
    def save_log(cls, file):
        """
        Saves the main log file to another file.
        
        :param file:  Output file name
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapSYS._save_log(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def terminate(cls, name):
        """
        DLL error termination
        
        :param name:  Module name
        :type  name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Call this function immediately before returning to
        the caller after an error has occurred inside the
        DLL.  If an error has occurred, you should clean-up
        (free memory, close files), call `error <geosoft.gxapi.GXSYS.error>` to register
        your own error messages, call `error_tag <geosoft.gxapi.GXSYS.error_tag>` to set any
        error message tags, call `terminate <geosoft.gxapi.GXSYS.terminate>` and return.

        Geosoft functions that detect an error will have
        already registered their own errors and called
        `terminate <geosoft.gxapi.GXSYS.terminate>`.
        """
        gxapi_cy.WrapSYS._terminate(GXContext._get_tls_geo(), name.encode())
        




# File System


    @classmethod
    def crc_file(cls, file):
        """
        Compute the CRC of a file
        
        :param file:  File Name
        :type  file:  str

        :returns:     CRC Value
        :rtype:       int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._crc_file(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def crc_file_offset(cls, file, offset):
        """
        Compute the CRC of a file with an Offset
        
        :param file:    File Name
        :param offset:  Offset in the file (0 for start)
        :type  file:    str
        :type  offset:  int

        :returns:       CRC Value
        :rtype:         int

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._crc_file_offset(GXContext._get_tls_geo(), file.encode(), offset)
        return ret_val



    @classmethod
    def file_ren(cls, old_file, new_file):
        """
        Rename a file
        
        :param old_file:  Old file name
        :param new_file:  New file name
        :type  old_file:  str
        :type  new_file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._file_ren(GXContext._get_tls_geo(), old_file.encode(), new_file.encode())
        



    @classmethod
    def find_files_vv(cls, vv, mask):
        """
        Fill a `GXVV <geosoft.gxapi.GXVV>` with files matching an input file mask.
        
        :param vv:    `GXVV <geosoft.gxapi.GXVV>` object
        :param mask:  File mask to match
        :type  vv:    GXVV
        :type  mask:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Fill a `GXVV <geosoft.gxapi.GXVV>` with files matching the input file mask.
        The `GXVV <geosoft.gxapi.GXVV>` should be of string type.
        """
        gxapi_cy.WrapSYS._find_files_vv(GXContext._get_tls_geo(), vv, mask.encode())
        



    @classmethod
    def absolute_file_name(cls, abbr, name):
        """
        Convert an abbreviated path name to a full path name.
        
        :param abbr:  Input file name to resolve
        :param name:  Output name, can be the same as input
        :type  abbr:  str
        :type  name:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is mainly intended to convert ".\\name" to a full
        name at run-time.
        """
        name.value = gxapi_cy.WrapSYS._absolute_file_name(GXContext._get_tls_geo(), abbr.encode(), name.value.encode())
        



    @classmethod
    def copy_file(cls, src_file, dest_file):
        """
        Copy a file.
        
        :param src_file:   Source file
        :param dest_file:  Destination file
        :type  src_file:   str
        :type  dest_file:  str

        :returns:          0 if file copied ok.
                           1 if unable to copy file or source file not found.
        :rtype:            int

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._copy_file(GXContext._get_tls_geo(), src_file.encode(), dest_file.encode())
        return ret_val



    @classmethod
    def delete_file(cls, file):
        """
        Delete a file.
        
        :param file:  Name of file to delete
        :type  file:  str

        :returns:     0 if file deleted.
                      1 if unable to find file or delete file.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._delete_file(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def delete_gi_file(cls, file):
        """
        Delete the GI file associated with a grid.
        
        :param file:  Name of grid file to delete
        :type  file:  str

        :returns:     0 if file deleted.
                      1 if file is not found, or found but could not be deleted.

                      This is a "one-line" function to take a grid file name,
                      remove the qualifiers, add the ".gi" and delete the file.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._delete_gi_file(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def delete_grid_file(cls, file):
        """
        Delete a grid file and its associated GI and XML files.
        
        :param file:  Name of grid file to delete
        :type  file:  str

        :returns:     0 if grid file deleted.
                      1 if grid file not found or if one or more files is found but could not be deleted.
        :rtype:       int

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Deletes the grid file first, and, if they exist, the associated GI
        and XML files.
        No error is registered if a file is not found or cannot be deleted.
        """
        ret_val = gxapi_cy.WrapSYS._delete_grid_file(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def dir_exist(cls, dir):
        """
        Check to see if a directory exists
        
        :param dir:  Name of directory to check
        :type  dir:  str

        :returns:    0 - Directory doesn't exist
                     1 - Directory exists
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._dir_exist(GXContext._get_tls_geo(), dir.encode())
        return ret_val



    @classmethod
    def file_exist(cls, file):
        """
        Check to see if a file exists
        
        :param file:  Name of file to check
        :type  file:  str

        :returns:     0 - File doesn't exist
                      1 - File exists
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Use the FULL path for the file name. If the full
        path is not specified, then the current working
        directory is used for the path.
        """
        ret_val = gxapi_cy.WrapSYS._file_exist(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def file_size(cls, file):
        """
        Returns size of a file.
        
        :param file:  Name of file
        :type  file:  str

        :returns:     0 none/error
                      x Size
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._file_size(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def file_writable(cls, file):
        """
        Check if a file can be created or opened in read-write mode
        at a specific location
        
        :param file:  File path name to check
        :type  file:  str
        :rtype:       bool

        .. versionadded:: 6.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._file_writable(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def find_path(cls, file, mode, fullname):
        """
        Get full path for a file with Geosoft subdirectory parameter.
        
        :param file:      File to get path name for
        :param mode:      :ref:`SYS_SEARCH_PATH`
        :param fullname:  Buffer to place path name into
        :type  file:      str
        :type  mode:      int
        :type  fullname:  str_ref

        :returns:         0 if file found.
                          1 if file not found.
        :rtype:           int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Directories can be resolved from the Environment section of the
        Geosoft registry, or from system environment variables that are
        not defined in the Geosoft Environment registry.  The following
        file prefixes will be replaced by the environment settings:

        <geosoft>      the main Geosoft installation directory
        <geosoft2>     the secondary Geosoft installation directory
        <geotemp>      the Geosoft temporary file directory
        <windows>      the operating system Windows directory
        <system>       the operating system system directory
        <other>        other environment variables
        """
        ret_val, fullname.value = gxapi_cy.WrapSYS._find_path(GXContext._get_tls_geo(), file.encode(), mode, fullname.value.encode())
        return ret_val



    @classmethod
    def find_path_ex(cls, file, mode, dir_mode, fullname):
        """
        Get full path for a file.
        
        :param file:      File to get path name for
        :param mode:      :ref:`SYS_SEARCH_PATH`
        :param dir_mode:  :ref:`GEO_DIRECTORY`
        :param fullname:  Buffer to place path name into
        :type  file:      str
        :type  mode:      int
        :type  dir_mode:  int
        :type  fullname:  str_ref

        :returns:         0 if file found.
                          1 if file not found.
        :rtype:           int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Directories can be resolved from the Environment section of the
        Geosoft registry, or from system environment variables that are
        not defined in the Geosoft Environment registry.  The following
        file prefixes will be replaced by the environment settings:

        <geosoft>      the main Geosoft installation directory
        <geosoft2>     the secondary Geosoft installation directory
        <geotemp>      the Geosoft temporary file directory
        <windows>      the operating system Windows directory
        <system>       the operating system system directory
        <other>        other environment variable
        """
        ret_val, fullname.value = gxapi_cy.WrapSYS._find_path_ex(GXContext._get_tls_geo(), file.encode(), mode, dir_mode, fullname.value.encode())
        return ret_val



    @classmethod
    def get_directory(cls, sys_dir, dir):
        """
        Get a directory path
        
        :param sys_dir:  :ref:`SYS_DIR`
        :param dir:      Returned directory path string
        :type  sys_dir:  int
        :type  dir:      str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The path will always end with the file separator character
        """
        dir.value = gxapi_cy.WrapSYS._get_directory(GXContext._get_tls_geo(), sys_dir, dir.value.encode())
        



    @classmethod
    def get_path(cls, type, path):
        """
        Get a Geosoft path
        
        :param type:  :ref:`SYS_PATH`
        :param path:  String in which to place path
        :type  type:  int
        :type  path:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The path name will have a directory separator at the end.
        """
        path.value = gxapi_cy.WrapSYS._get_path(GXContext._get_tls_geo(), type, path.value.encode())
        



    @classmethod
    def get_windows_dir(cls, dir):
        """
        Get the Windows directory path
        
        :param dir:  Buff for directory path string
        :type  dir:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        dir.value = gxapi_cy.WrapSYS._get_windows_dir(GXContext._get_tls_geo(), dir.value.encode())
        



    @classmethod
    def make_dir(cls, dir):
        """
        Create a directory.
        
        :param dir:  Name of directory
        :type  dir:  str

        :returns:    0 - Directory made
                     1 - Directory cannot be made
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._make_dir(GXContext._get_tls_geo(), dir.encode())
        return ret_val



    @classmethod
    def make_file_readonly(cls, file):
        """
        Set a file's read-only attribute.
        
        :param file:  Name of file
        :type  file:  str

        :returns:     0 if read-only attribute successfully set,
                      1 if attribute change fails.
        :rtype:       int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._make_file_readonly(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def make_file_writable(cls, file):
        """
        Removes a file's read-only attribute.
        
        :param file:  Name of file
        :type  file:  str

        :returns:     0 if read-only attribute successfully removed,
                      1 if attribute change fails.
        :rtype:       int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._make_file_writable(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def relative_file_name(cls, abbr, name):
        """
        Convert a file name to a relative abbreviated path name
        
        :param abbr:  Input file name to resolve
        :param name:  Output name, can be the same as input
        :type  abbr:  str
        :type  name:  str_ref

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This will produce relative paths based on the workspace
        directory into ".\\name".
        """
        name.value = gxapi_cy.WrapSYS._relative_file_name(GXContext._get_tls_geo(), abbr.encode(), name.value.encode())
        



    @classmethod
    def short_path_file_name(cls, in_name, name):
        """
        Obtains the short path form of a specified input path.
        
        :param in_name:  Input file name to resolve
        :param name:     Output name, can be the same as input
        :type  in_name:  str
        :type  name:     str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        name.value = gxapi_cy.WrapSYS._short_path_file_name(GXContext._get_tls_geo(), in_name.encode(), name.value.encode())
        



    @classmethod
    def temp_file_ext(cls, ext, out):
        """
        Generate a unique file name for this extension in the temp directory.
        
        :param ext:  Input extension (without .)
        :param out:  Output name
        :type  ext:  str
        :type  out:  str_ref

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is useful for created a unique tempory name for a file in the Geosoft temporary directory.
        """
        out.value = gxapi_cy.WrapSYS._temp_file_ext(GXContext._get_tls_geo(), ext.encode(), out.value.encode())
        



    @classmethod
    def temp_file_name(cls, path_file, out_filename):
        """
        Generate a file name for this file in the temp directory.
        
        :param path_file:     Input file name to resolve (path is removed)
        :param out_filename:  Output name, can be the same as input
        :type  path_file:     str
        :type  out_filename:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is useful for created a unique tempory name for a file in the Geosoft temporary directory.

        From version 7.0 The file extension will match the input file, but the
        filename itself will be a process and thread unique value to ensure that
        clashes does not happen.
        """
        out_filename.value = gxapi_cy.WrapSYS._temp_file_name(GXContext._get_tls_geo(), path_file.encode(), out_filename.value.encode())
        



    @classmethod
    def transfer_path(cls, path_file, file):
        """
        Transfers file path to new file name.
        
        :param path_file:  Input file path/name
        :param file:       Output file name with path transfered
        :type  path_file:  str
        :type  file:       str_ref

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The path and volume of from the input string is added to
        file name from the output string.
        """
        file.value = gxapi_cy.WrapSYS._transfer_path(GXContext._get_tls_geo(), path_file.encode(), file.value.encode())
        



    @classmethod
    def valid_file_name(cls, file):
        """
        Check to see if a file name valid
        
        :param file:  Name of file to check
        :type  file:  str

        :returns:     0 - File name is not valid
                      1 - File name is valid
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Use the FULL path for the file name. If the full
        path is not specified, then the current working
        directory is used for the path.
        """
        ret_val = gxapi_cy.WrapSYS._valid_file_name(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def write_in_dir(cls, dir):
        """
        Can I create files in this directory ?
        
        :param dir:  Name of directory to check
        :type  dir:  str

        :returns:    0 - Directory doesn't allow write of does not exist
                     1 - Directory allows writes
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._write_in_dir(GXContext._get_tls_geo(), dir.encode())
        return ret_val



    @classmethod
    def file_date(cls, file):
        """
        File creation date in decimal years.
        
        :param file:  File name
        :type  file:  str

        :returns:     Date in decimal years, `rDUMMY <geosoft.gxapi.rDUMMY>` if the file does not exist.
        :rtype:       float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The FormatDate_STR function can be used to convert a date
        to a string.
        """
        ret_val = gxapi_cy.WrapSYS._file_date(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def file_time(cls, file):
        """
        File creation time in decimal hours.
        
        :param file:  File name
        :type  file:  str

        :returns:     Date in decimal hours, `rDUMMY <geosoft.gxapi.rDUMMY>` if the file does not exist.
        :rtype:       float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The FormatTime_STR function can be used to convert a time
        to a string.
        """
        ret_val = gxapi_cy.WrapSYS._file_time(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def utc_file_date(cls, file):
        """
        File creation UTC date in decimal years.
        
        :param file:  File name
        :type  file:  str

        :returns:     Date in decimal years, `rDUMMY <geosoft.gxapi.rDUMMY>` if the file does not exist.
        :rtype:       float

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The FormatDate_STR function can be used to convert a date
        to a string.
        """
        ret_val = gxapi_cy.WrapSYS._utc_file_date(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def utc_file_time(cls, file):
        """
        File creation UTC time in decimal hours.
        
        :param file:  File name
        :type  file:  str

        :returns:     Date in decimal hours, `rDUMMY <geosoft.gxapi.rDUMMY>` if the file does not exist.
        :rtype:       float

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The FormatTime_STR function can be used to convert a time
        to a string.
        """
        ret_val = gxapi_cy.WrapSYS._utc_file_time(GXContext._get_tls_geo(), file.encode())
        return ret_val




# Global Parameter


    @classmethod
    def get_settings_meta(cls, meta):
        """
        Get the settings metadata object.
        
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` object to store the settings metadata in
        :type  meta:  GXMETA

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._get_settings_meta(GXContext._get_tls_geo(), meta)
        



    @classmethod
    def global_reset(cls, ini):
        """
        Reset the global parameters.
        
        :param ini:  New INI file name, if "", use default.
        :type  ini:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._global_reset(GXContext._get_tls_geo(), ini.encode())
        



    @classmethod
    def global_set(cls, parm, set):
        """
        Set a global parameter setting.
        
        :param parm:  Name of the Parameter
        :param set:   Setting
        :type  parm:  str
        :type  set:   str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._global_set(GXContext._get_tls_geo(), parm.encode(), set.encode())
        



    @classmethod
    def global_write(cls, ini):
        """
        Modify the global parameters.
        
        :param ini:  Global INI file, if "" use default.
        :type  ini:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the global parameters have been changed, use
        this function to make the changes permanent,
        """
        gxapi_cy.WrapSYS._global_write(GXContext._get_tls_geo(), ini.encode())
        



    @classmethod
    def global_(cls, parm, setting):
        """
        Get a global parameter setting.
        
        :param parm:     Name of the Parameter
        :param setting:  Setting returned
        :type  parm:     str
        :type  setting:  str_ref

        :returns:        0 if parameter found.
                         1 if parameter not found or not set.
        :rtype:          int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The returned string will be empty if the parameter is
        not found.

        Parameters are derived from GEOSOFT.INI.
        This is a standard Windows style INI
        file that contains [GROUPS], PARAMETERS and SETTINGS
        as follows

        [GROUP1]
        PARAM1=setting1
        PARAM2 setting2
        PARAM3 "setting3 is text"

        To retrieve an entry, specify the group.parameter.  For
        example, iGlobal_SYS("GROUP1.PARAM3",sSetting) will
        retrieve the string "setting is text".  The double
        quotes will not appear in the setting.
        """
        ret_val, setting.value = gxapi_cy.WrapSYS._global_(GXContext._get_tls_geo(), parm.encode(), setting.value.encode())
        return ret_val



    @classmethod
    def reset_settings(cls):
        """
        Resets the GX_HELP settings in the geosoft.ini file
        after changes have been made.
        

        .. versionadded:: 5.1.8

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapSYS._reset_settings(GXContext._get_tls_geo())
        



    @classmethod
    def set_settings_meta(cls, meta):
        """
        Set the settings metadata object.
        
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` object
        :type  meta:  GXMETA

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._set_settings_meta(GXContext._get_tls_geo(), meta)
        




# Licensing


    @classmethod
    def check_arc_license(cls):
        """
        Check to see if a ESRI ArcEngine or ArcView license is available
        

        :returns:    1 - Licenced
                  0 - Not licenced
        :rtype:      int

        .. versionadded:: 7.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._check_arc_license(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def check_arc_license_ex(cls, version):
        """
        Check to see if a ESRI ArcEngine or ArcView license is available, returns type and version of available engine.
        
        :param version:  Version String
        :type  version:  str_ref

        :returns:        :ref:`ARC_LICENSE`
        :rtype:          int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val, version.value = gxapi_cy.WrapSYS._check_arc_license_ex(GXContext._get_tls_geo(), version.value.encode())
        return ret_val



    @classmethod
    def check_intrinsic(cls, cl, name):
        """
        Check to see if an intrinsic object is licensed
        
        :param cl:    Intrinsic Class Number
        :param name:  Intrinsic Name (must be exact)
        :type  cl:    int
        :type  name:  str

        :returns:     1 - Licenced
                      0 - Not licenced
        :rtype:       int

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._check_intrinsic(GXContext._get_tls_geo(), cl, name.encode())
        return ret_val



    @classmethod
    def get_geodist(cls):
        """
        Gets a global flag that indicates whether we are
        running within the geodist library
        

        :returns:    0 - Geodist not loaded, 1 - Geodist loaded
        :rtype:      int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._get_geodist(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_license_class(cls, cl):
        """
        Get the current application license class.
        
        :param cl:  Class String
        :type  cl:  str_ref

        .. versionadded:: 6.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** String may be one of :  "ArcGIS"
        "OasisMontaj"
        "DapServer"
        """
        cl.value = gxapi_cy.WrapSYS._get_license_class(GXContext._get_tls_geo(), cl.value.encode())
        



    @classmethod
    def get_licensed_user(cls, user, company):
        """
        Get the licensed user name and Company
        
        :param user:     User Name
        :param company:  Company Name
        :type  user:     str_ref
        :type  company:  str_ref

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        user.value, company.value = gxapi_cy.WrapSYS._get_licensed_user(GXContext._get_tls_geo(), user.value.encode(), company.value.encode())
        



    @classmethod
    def is_signed_in(cls):
        """
        Check if signed in via Geosoft Connect
        
        :rtype:      bool

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._is_signed_in(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def sign_in(cls):
        """
        Sign in via Geosoft Connect
        

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._sign_in(GXContext._get_tls_geo())
        



    @classmethod
    def check_product_updates(cls, silent):
        """
        Check for product updates via Geosoft Connect
        
        :param silent:  Do not show notification if no updates available.
        :type  silent:  bool

        .. versionadded:: 9.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._check_product_updates(GXContext._get_tls_geo(), silent)
        



    @classmethod
    def geosoft_connect_authenticate_and_navigate(cls, url):
        """
        Automatically authenticate and navigate to my.geosoft.com URL
        
        :param url:  URL
        :type  url:  str

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._geosoft_connect_authenticate_and_navigate(GXContext._get_tls_geo(), url.encode())
        



    @classmethod
    def get_geosoft_id(cls, id):
        """
        Get the Geosoft ID (email) if signed in
        
        :param id:  Returned ID
        :type  id:  str_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        id.value = gxapi_cy.WrapSYS._get_geosoft_id(GXContext._get_tls_geo(), id.value.encode())
        



    @classmethod
    def get_profile_name(cls, name):
        """
        Get the profile name as defined in My Geosoft (or email if not defined)
        
        :param name:  Returned name
        :type  name:  str_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        name.value = gxapi_cy.WrapSYS._get_profile_name(GXContext._get_tls_geo(), name.value.encode())
        



    @classmethod
    def get_profile_url(cls, url):
        """
        Get link to my.geosoft.com profile URL
        
        :param url:  Returned URL
        :type  url:  str_ref

        .. versionadded:: 9.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        url.value = gxapi_cy.WrapSYS._get_profile_url(GXContext._get_tls_geo(), url.value.encode())
        




# Lineage


    @classmethod
    def add_lineage_parameter(cls, name, value):
        """
        Add a parameter to the current lineage object
        
        :param name:   Paramter Name
        :param value:  Parameter Value
        :type  name:   str
        :type  value:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._add_lineage_parameter(GXContext._get_tls_geo(), name.encode(), value.encode())
        



    @classmethod
    def add_lineage_source(cls, source_type, source_name):
        """
        Add a source to the current lineage object
        
        :param source_type:  :ref:`SYS_LINEAGE_SOURCE`
        :param source_name:  Source Name
        :type  source_type:  int
        :type  source_name:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._add_lineage_source(GXContext._get_tls_geo(), source_type, source_name.encode())
        



    @classmethod
    def clear_lineage_parameters(cls):
        """
        Clear all the lineage parameters
        

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._clear_lineage_parameters(GXContext._get_tls_geo())
        



    @classmethod
    def clear_lineage_sources(cls):
        """
        Clear all the lineage sources
        

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._clear_lineage_sources(GXContext._get_tls_geo())
        



    @classmethod
    def copy_geo_file(cls, data, dir):
        """
        Copy a Geosoft data file and all associated files to a new folder
        
        :param data:  File Name
        :param dir:   Target directory
        :type  data:  str
        :type  dir:   str

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Grids are copied and the GI's are maintained - note that support
        for non-geosoft grids is limited since this method does not
        guarantee all grid files besides the main one are copied.
        """
        gxapi_cy.WrapSYS._copy_geo_file(GXContext._get_tls_geo(), data.encode(), dir.encode())
        



    @classmethod
    def backup_geo_file(cls, data, target):
        """
        Backup a Geosoft data file and all associated files to a temporary folder.
        
        :param data:    File Name
        :param target:  Buffer to place the target name into
        :type  data:    str
        :type  target:  str_ref

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Grids are copied and the GI's are maintained - note that support
        for non-geosoft grids is limited since this method does not
        guarantee all grid files besides the main one are copied.
        """
        target.value = gxapi_cy.WrapSYS._backup_geo_file(GXContext._get_tls_geo(), data.encode(), target.value.encode())
        



    @classmethod
    def remove_lineage_output(cls, output_name):
        """
        Remove an output from the current lineage object
        
        :param output_name:  Source Name
        :type  output_name:  str

        .. versionadded:: 7.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._remove_lineage_output(GXContext._get_tls_geo(), output_name.encode())
        



    @classmethod
    def remove_lineage_parameter(cls, name):
        """
        Remove a parameter in the current lineage object
        
        :param name:  Paramter Name
        :type  name:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._remove_lineage_parameter(GXContext._get_tls_geo(), name.encode())
        



    @classmethod
    def remove_lineage_source(cls, source_name):
        """
        Remove a source from the current lineage object
        
        :param source_name:  Source Name
        :type  source_name:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._remove_lineage_source(GXContext._get_tls_geo(), source_name.encode())
        



    @classmethod
    def restore_geo_file(cls, target, original):
        """
        Backup a Geosoft data file and all associated files to original location
        
        :param target:    Backup File Name
        :param original:  Original file name
        :type  target:    str
        :type  original:  str

        .. versionadded:: 7.0

        **License:** `Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic>`_

        **Note:** Grids are copied and the GI's are maintained - note that support
        for non-geosoft grids is limited since this method does not
        guarantee all grid files besides the main one are copied.
        """
        gxapi_cy.WrapSYS._restore_geo_file(GXContext._get_tls_geo(), target.encode(), original.encode())
        



    @classmethod
    def set_lineage_description(cls, description):
        """
        Set the description for the current lineage object
        
        :param description:  Description
        :type  description:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._set_lineage_description(GXContext._get_tls_geo(), description.encode())
        



    @classmethod
    def set_lineage_display_name(cls, display_name):
        """
        Set the display name for the current lineage object
        
        :param display_name:  DisplayName
        :type  display_name:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._set_lineage_display_name(GXContext._get_tls_geo(), display_name.encode())
        



    @classmethod
    def set_lineage_name(cls, name):
        """
        Set the name for the current lineage object
        
        :param name:  Name
        :type  name:  str

        .. versionadded:: 7.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._set_lineage_name(GXContext._get_tls_geo(), name.encode())
        




# Menus and Toolbar


    @classmethod
    def clear_menus(cls, flag):
        """
        Clear all menus
        
        :param flag:  :ref:`SYS_MENU_CLEAR`
        :type  flag:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapSYS._clear_menus(GXContext._get_tls_geo(), flag)
        



    @classmethod
    def get_loaded_menus(cls, lst_default, lst_loaded, lst_user):
        """
        Get the loaded menus.
        
        :param lst_default:  Default menus (typically a single entry based on product)
        :param lst_loaded:   Loaded menus
        :param lst_user:     Loaded user menus
        :type  lst_default:  GXLST
        :type  lst_loaded:   GXLST
        :type  lst_user:     GXLST

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The names of the LSTs contain the menus and the values contain any exclusions. Exclusions 
        are semicolon separated top level menu names and/or toolbar.geobar file names.
        """
        gxapi_cy.WrapSYS._get_loaded_menus(GXContext._get_tls_geo(), lst_default, lst_loaded, lst_user)
        



    @classmethod
    def set_loaded_menus(cls, lst_default, lst_loaded, lst_user):
        """
        Load a list of menus
        
        :param lst_default:  Default menus (typically a single entry based on product, do not change the name returned by `get_loaded_menus <geosoft.gxapi.GXSYS.get_loaded_menus>`)
        :param lst_loaded:   Loaded menus
        :param lst_user:     Loaded user menus
        :type  lst_default:  GXLST
        :type  lst_loaded:   GXLST
        :type  lst_user:     GXLST

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The names of the LSTs contain the menus and the values contain any exclusions. Exclusions 
        are semicolon separated top level menu names and/or toolbar.geobar file names.
        """
        gxapi_cy.WrapSYS._set_loaded_menus(GXContext._get_tls_geo(), lst_default, lst_loaded, lst_user)
        



    @classmethod
    def get_entitlement_rights(cls, lst_rights):
        """
        Get the Entitlement Rights
        
        :param lst_rights:  Rights
        :type  lst_rights:  GXLST

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._get_entitlement_rights(GXContext._get_tls_geo(), lst_rights)
        




# Misc


    @classmethod
    def generate_guid(cls, guid):
        """
        Genrates a GUID string (e.g. {4FEDE8BF-CDAB-430A-8026-1CCC0EC0A2EB})
        
        :param guid:  GUID
        :type  guid:  str_ref

        .. versionadded:: 8.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        guid.value = gxapi_cy.WrapSYS._generate_guid(GXContext._get_tls_geo(), guid.value.encode())
        



    @classmethod
    def clipboard_to_file(cls, file):
        """
        Copy text from the clipboard to a file.
        
        :param file:  File name to place it into
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._clipboard_to_file(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def create_clipboard_ra(cls):
        """
        Create a `GXRA <geosoft.gxapi.GXRA>` to read text from the clipboard.
        

        :returns:    `GXRA <geosoft.gxapi.GXRA>` to use for reading.
        :rtype:      GXRA

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Destroy the `GXRA <geosoft.gxapi.GXRA>` as soon as possible. As long as it
        open the clipboard is not accessible from any
        application.
        """
        ret_val = gxapi_cy.WrapSYS._create_clipboard_ra(GXContext._get_tls_geo())
        return GXRA(ret_val)



    @classmethod
    def create_clipboard_wa(cls):
        """
        Create a `GXWA <geosoft.gxapi.GXWA>` to write text on the clipboard.
        

        :returns:    `GXWA <geosoft.gxapi.GXWA>` to use for reading.
        :rtype:      GXWA

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Destroy the `GXWA <geosoft.gxapi.GXWA>` as soon as possible. As long as it
        open the clipboard is not accessible from any
        application.
        """
        ret_val = gxapi_cy.WrapSYS._create_clipboard_wa(GXContext._get_tls_geo())
        return GXWA(ret_val)



    @classmethod
    def emf_object_size(cls, file, size_x, size_y):
        """
        Get the size of an EMF object
        
        :param file:    EMF File holding data
        :param size_x:  Size X
        :param size_y:  Size Y
        :type  file:    str
        :type  size_x:  float_ref
        :type  size_y:  float_ref

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        size_x.value, size_y.value = gxapi_cy.WrapSYS._emf_object_size(GXContext._get_tls_geo(), file.encode(), size_x.value, size_y.value)
        



    @classmethod
    def file_to_clipboard(cls, file):
        """
        Copy a text file onto the clipboard as text.
        
        :param file:  File place into clipboard
        :type  file:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._file_to_clipboard(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def font_lst(cls, lst, which):
        """
        List all Windows and geosoft fonts.
        
        :param lst:    List Object
        :param which:  :ref:`SYS_FONT`
        :type  lst:    GXLST
        :type  which:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** To get TT and GFN fonts, call twice with the same list
        and `SYS_FONT_TT <geosoft.gxapi.SYS_FONT_TT>`, then `SYS_FONT_GFN <geosoft.gxapi.SYS_FONT_GFN>`, or vice-versa to
        change order of listing.
        """
        gxapi_cy.WrapSYS._font_lst(GXContext._get_tls_geo(), lst, which)
        



    @classmethod
    def get_dot_net_gx_entries(cls, gx, entry_buffer):
        """
        Get the list of entry points that this assembly has
        exposed to Oasis montaj.
        
        :param gx:            Name of .NET GX assembly
        :param entry_buffer:  Buffer to place list of entries in
        :type  gx:            str
        :type  entry_buffer:  str_ref

        :returns:             0  success
                              1  error.
        :rtype:               int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The list of entry points are passed back as one
        string with each entry point separated by a semi-colon.
        For example: NewGDB|Run;NewGDB|RunEx
        """
        ret_val, entry_buffer.value = gxapi_cy.WrapSYS._get_dot_net_gx_entries(GXContext._get_tls_geo(), gx.encode(), entry_buffer.value.encode())
        return ret_val



    @classmethod
    def send_general_message(cls, cl, info):
        """
        Send a general information message to all listners
        
        :param cl:    Message Class
        :param info:  Message Info
        :type  cl:    str
        :type  info:  str

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._send_general_message(GXContext._get_tls_geo(), cl.encode(), info.encode())
        



    @classmethod
    def write_debug_log(cls, log):
        """
        This method writes out information to the output
        debugging log file (in temp folder) or output window.
        
        :param log:  String to Write out
        :type  log:  str

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._write_debug_log(GXContext._get_tls_geo(), log.encode())
        



    @classmethod
    def log_script_run(cls, location):
        """
        This method logs that a script was run
        
        :param location:  Location that launched the script
        :type  location:  str

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._log_script_run(GXContext._get_tls_geo(), location.encode())
        




# Multithreading


    @classmethod
    def get_thread_id(cls):
        """
        Get the ID the current thread.
        

        :returns:    x - ID
        :rtype:      int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** In a single threaded application this will always be 0.
        """
        ret_val = gxapi_cy.WrapSYS._get_thread_id(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def run_multi_user_script(cls, script, users, iterations, wait_min_time, wait_max_time, ramp_up_time):
        """
        Execute a script using multithreaded users
        
        :param script:         Script to run
        :param users:          Number of users to run
        :param iterations:     Number of iterations to run (for each user)
        :param wait_min_time:  Minimum wait time between iterations (0 for none)
        :param wait_max_time:  Maximum wait time between iterations (0 for none)
        :param ramp_up_time:   Ramp up time for users (0 for all users start immediatly)
        :type  script:         str
        :type  users:          int
        :type  iterations:     int
        :type  wait_min_time:  int
        :type  wait_max_time:  int
        :type  ramp_up_time:   int

        .. versionadded:: 5.1.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** No access is provided in the script to EMAPS
        or EDBS. Users must ensure that the resources
        that are shared are protected.
        """
        gxapi_cy.WrapSYS._run_multi_user_script(GXContext._get_tls_geo(), script.encode(), users, iterations, wait_min_time, wait_max_time, ramp_up_time)
        




# Parameter


    @classmethod
    def clear_group(cls, group):
        """
        Clear current contents of a group
        
        :param group:  Group to clear
        :type  group:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._clear_group(GXContext._get_tls_geo(), group.encode())
        



    @classmethod
    def clear_group_parm(cls, group):
        """
        Clears all paramters in a specified group.
        
        :param group:  String
        :type  group:  str

        .. versionadded:: 5.1.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._clear_group_parm(GXContext._get_tls_geo(), group.encode())
        



    @classmethod
    def clear_parm(cls):
        """
        Clears all paramters.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._clear_parm(GXContext._get_tls_geo())
        



    @classmethod
    def default_int(cls, group, field, val):
        """
        Allows a default int to be set.
        
        :param group:  Group Name
        :param field:  Parameter Name
        :param val:    Int Value to Set
        :type  group:  str
        :type  field:  str
        :type  val:    int

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The value will only be set if there is no existing
        setting.
        """
        gxapi_cy.WrapSYS._default_int(GXContext._get_tls_geo(), group.encode(), field.encode(), val)
        



    @classmethod
    def default_double(cls, group, field, val):
        """
        Allows a default real to be set.
        
        :param group:  Group Name
        :param field:  Parameter Name
        :param val:    Real Value to Set
        :type  group:  str
        :type  field:  str
        :type  val:    float

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The value will only be set if there is no existing
        setting.
        """
        gxapi_cy.WrapSYS._default_double(GXContext._get_tls_geo(), group.encode(), field.encode(), val)
        



    @classmethod
    def default_string(cls, group, field, val):
        """
        Allows a default string to be set.
        
        :param group:  Group Name
        :param field:  Parameter Name
        :param val:    String to Set it To
        :type  group:  str
        :type  field:  str
        :type  val:    str

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The value will only be set if there is no existing
        setting.
        """
        gxapi_cy.WrapSYS._default_string(GXContext._get_tls_geo(), group.encode(), field.encode(), val.encode())
        



    @classmethod
    def get_pattern(cls, group, pat, size, thick, dense, col, back_col):
        """
        Gets pattern parameters from the parameter block.
        
        :param group:     Input group name
        :param pat:       Pattern
        :param size:      Size,
        :param thick:     Thick (0-100)
        :param dense:     Density,
        :param col:       Pattern Color
        :param back_col:  Background Color
        :type  group:     str
        :type  pat:       int_ref
        :type  size:      float_ref
        :type  thick:     int_ref
        :type  dense:     float_ref
        :type  col:       int_ref
        :type  back_col:  int_ref

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Gets all the user-definable pattern parameters from
        a specified group. Parameters are:
        "PAT_NUMBER"    0 is solid fill (default)
        "PAT_SIZE"      pattern tile size in mm. (can return `iDUMMY <geosoft.gxapi.iDUMMY>`)
        "PAT_THICKNESS" pattern line thickness in percent of the tile size.
        valid range is 0-100.
        "PAT_DENSITY"   Tile spacing. A value of 1 means tiles are laid with no overlap.
        A value of 2 means they overlap each other.
        "PAT_COLOR"     The color value.
        "PAT_BACKCOLOR" Background color value.

        Returned values may be DUMMY, but will be acceptable for use with
        the `GXGUI.color_form <geosoft.gxapi.GXGUI.color_form>` function, to set defaults.
        """
        pat.value, size.value, thick.value, dense.value, col.value, back_col.value = gxapi_cy.WrapSYS._get_pattern(GXContext._get_tls_geo(), group.encode(), pat.value, size.value, thick.value, dense.value, col.value, back_col.value)
        



    @classmethod
    def get_reg(cls, reg, group):
        """
        Get `GXREG <geosoft.gxapi.GXREG>` parameters.
        
        :param reg:    `GXREG <geosoft.gxapi.GXREG>` to add parameters to
        :param group:  Group name wanted
        :type  reg:    GXREG
        :type  group:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._get_reg(GXContext._get_tls_geo(), reg, group.encode())
        



    @classmethod
    def gt_string(cls, group, field, buff):
        """
        This method returns a string in the parameter block.
        
        :param group:  Group Name
        :param field:  Parameter Name
        :param buff:   Buffer to place the string into
        :type  group:  str
        :type  field:  str
        :type  buff:   str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If the setting exits it is placed in the buffer, otherwise
        the buffer will have zero length
        """
        buff.value = gxapi_cy.WrapSYS._gt_string(GXContext._get_tls_geo(), group.encode(), field.encode(), buff.value.encode())
        



    @classmethod
    def exist_int(cls, group, field):
        """
        This method checks to see if a int parameter exists.
        
        :param group:  Group Name
        :param field:  Parameter Name
        :type  group:  str
        :type  field:  str

        :returns:      1 - Yes
                       0 - No
        :rtype:        int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._exist_int(GXContext._get_tls_geo(), group.encode(), field.encode())
        return ret_val



    @classmethod
    def exist_double(cls, group, field):
        """
        This method checks to see if a real parameter exists.
        
        :param group:  Group Name
        :param field:  Parameter Name
        :type  group:  str
        :type  field:  str

        :returns:      1 - Yes
                       0 - No
        :rtype:        int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._exist_double(GXContext._get_tls_geo(), group.encode(), field.encode())
        return ret_val



    @classmethod
    def exist_string(cls, group, field):
        """
        This method checks to see if a string parameter exists.
        
        :param group:  Group Name
        :param field:  Parameter Name
        :type  group:  str
        :type  field:  str

        :returns:      1 - Yes
                       0 - No
        :rtype:        int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._exist_string(GXContext._get_tls_geo(), group.encode(), field.encode())
        return ret_val



    @classmethod
    def get_int(cls, group, field):
        """
        This method returns an int from the parameter block.
        
        :param group:  Group Name
        :param field:  Parameter Name
        :type  group:  str
        :type  field:  str

        :returns:      Int Value, `iDUMMY <geosoft.gxapi.iDUMMY>` if the parameter is not set.
        :rtype:        int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._get_int(GXContext._get_tls_geo(), group.encode(), field.encode())
        return ret_val



    @classmethod
    def get_yes_no(cls, group, field):
        """
        Check a YES/NO Setting
        
        :param group:  Group Name
        :param field:  Parameter Name
        :type  group:  str
        :type  field:  str

        :returns:      1 - if first char in setting is a "Y" or"y"
                       0 - Otherwise
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._get_yes_no(GXContext._get_tls_geo(), group.encode(), field.encode())
        return ret_val



    @classmethod
    def replace_string(cls, str_val, output, group):
        """
        Replace "% %" tokens in a string with parameter values
        
        :param str_val:  String to filter replace
        :param output:   Output string
        :param group:    Default group name
        :type  str_val:  str
        :type  output:   str_ref
        :type  group:    str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** If parameter does not exist, the token is removed.  Full parameter names,
        such as "%group.name%", are used as-is.  Partial parameter names, such as
        "%name%" will have the default group attached.
        """
        output.value = gxapi_cy.WrapSYS._replace_string(GXContext._get_tls_geo(), str_val.encode(), output.value.encode(), group.encode())
        



    @classmethod
    def load_parm(cls, file, groups):
        """
        Reads parameters from a file.
        
        :param file:    Name of the File to read from
        :param groups:  Group Name to write read ("" for all groups)
        :type  file:    str
        :type  groups:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._load_parm(GXContext._get_tls_geo(), file.encode(), groups.encode())
        



    @classmethod
    def get_double(cls, group, field):
        """
        This method returns a real from the parameter block.
        
        :param group:  Group Name
        :param field:  Parameter Name
        :type  group:  str
        :type  field:  str

        :returns:      Real Value, `rDUMMY <geosoft.gxapi.rDUMMY>` if parameter not set.
        :rtype:        float

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._get_double(GXContext._get_tls_geo(), group.encode(), field.encode())
        return ret_val



    @classmethod
    def save_parm(cls, file, mode, groups):
        """
        Writes out one group (or all groups) to a file.
        
        :param file:    Name of the File
        :param mode:    0 - New file, 1 - Append
        :param groups:  Group Name to write out ("" for all groups)
        :type  file:    str
        :type  mode:    int
        :type  groups:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._save_parm(GXContext._get_tls_geo(), file.encode(), mode, groups.encode())
        



    @classmethod
    def filter_parm_group(cls, group, add):
        """
        Controls filtering of specific group during logging.
        
        :param group:  Group Name
        :param add:    0 - Clear filter, 1 - Add filter
        :type  group:  str
        :type  add:    int

        .. versionadded:: 9.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is useful to prevent certain utility GX parameters from being recorded during GS script runs where the parameters does not influence the actual script execution.
        """
        gxapi_cy.WrapSYS._filter_parm_group(GXContext._get_tls_geo(), group.encode(), add)
        



    @classmethod
    def set_int(cls, group, field, val):
        """
        This method sets an int in the parameter block.
        
        :param group:  Group Name
        :param field:  Parameter Name
        :param val:    Int Value to Set
        :type  group:  str
        :type  field:  str
        :type  val:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._set_int(GXContext._get_tls_geo(), group.encode(), field.encode(), val)
        



    @classmethod
    def set_pattern(cls, group, pat, size, thick, dense, col, back_col):
        """
        Sets pattern parameters in the parameter block.
        
        :param group:     Group Name
        :param pat:       Pattern
        :param size:      Size. Input `GS_R8DM <geosoft.gxapi.GS_R8DM>` to use default
        :param thick:     Thickness (0-100).  Input `GS_S4DM <geosoft.gxapi.GS_S4DM>` to use default
        :param dense:     Density. Input `GS_R8DM <geosoft.gxapi.GS_R8DM>` to use default
        :param col:       Pattern Color
        :param back_col:  Background Color. Can be `C_TRANSPARENT <geosoft.gxapi.C_TRANSPARENT>`
        :type  group:     str
        :type  pat:       int
        :type  size:      float
        :type  thick:     int
        :type  dense:     float
        :type  col:       int
        :type  back_col:  int

        .. versionadded:: 6.4

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Sets all the user-definable pattern parameters to
        a specified group. Parameters are:
        "PAT_NUMBER"    0 is solid fill
        "PAT_SIZE"      pattern tile size in mm.
        "PAT_THICKNESS" pattern line thickness in percent of the tile size.
        valid range is 0-100.
        "PAT_DENSITY"   Tile spacing. A value of 1 means tiles are laid with no overlap.
        A value of 2 means they overlap each other.
        "PAT_COLOR"     The color value.
        "PAT_BACKCOLOR" Background color value.

        Input values may be DUMMY.

        Designed for use along with the sPatternForm_GUI function.
        """
        gxapi_cy.WrapSYS._set_pattern(GXContext._get_tls_geo(), group.encode(), pat, size, thick, dense, col, back_col)
        



    @classmethod
    def set_double(cls, group, field, val):
        """
        This method Sets a real in the parameter block.
        
        :param group:  Group Name
        :param field:  Parameter Name
        :param val:    Real
        :type  group:  str
        :type  field:  str
        :type  val:    float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._set_double(GXContext._get_tls_geo(), group.encode(), field.encode(), val)
        



    @classmethod
    def set_reg(cls, reg):
        """
        Copy contents of a `GXREG <geosoft.gxapi.GXREG>` to current parameters.
        
        :param reg:  `GXREG <geosoft.gxapi.GXREG>` object
        :type  reg:  GXREG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._set_reg(GXContext._get_tls_geo(), reg)
        



    @classmethod
    def set_string(cls, group, field, val):
        """
        This method sets a string in the parameter block.
        
        :param group:  Group Name
        :param field:  Parameter Name
        :param val:    String to Set it To
        :type  group:  str
        :type  field:  str
        :type  val:    str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._set_string(GXContext._get_tls_geo(), group.encode(), field.encode(), val.encode())
        




# Progress Control


    @classmethod
    def check_stop(cls):
        """
        This method is called at convenient points in the
        GX code to check if the user has asked the script
        to stop running. This method should be called by
        any GX program that may take a while to complete.
        

        :returns:    0 - No
                  1 - Yes, Terminate processing.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._check_stop(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def prog_state(cls):
        """
        Return current progress state (On/Off)
        
        :rtype:      int

        .. versionadded:: 7.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This is useful, for instance, when calling one GX from another,
        especially if it is called multiple times in a loop.
        The called GX may turn the progress ON/OFF on its own, which
        means any progress tracking in the calling GX is disrupted.
        The called GX should use this function to determine the original
        progress state, and not turn off progress if it was already on.

        Returns				 0 - Progress is on
        - Progress is off
        """
        ret_val = gxapi_cy.WrapSYS._prog_state(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def prog_name(cls, name, reset):
        """
        This method allows you to name the current process being
        displayed by the progress bar. This method has no affect
        if no progress bar exists.
        
        :param name:   New Process Name
        :param reset:  0 - Change the Name but do not change the percentage 1 - Change the Name and Reset Percent to 0 2 - Change the Name but no Percent Bar
        :type  name:   str
        :type  reset:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._prog_name(GXContext._get_tls_geo(), name.encode(), reset)
        



    @classmethod
    def progress(cls, on):
        """
        This method allows you to turn on the Progress BAR ON/OFF.
        Once the progress bar is on, use the UpdateProg method
        to drive it.
        
        :param on:  0 - Turn Progress Bar OFF 1 - Turn Progress Bar ON
        :type  on:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._progress(GXContext._get_tls_geo(), on)
        



    @classmethod
    def prog_update(cls, perc):
        """
        This method drives the Progress Bar. It is passed
        a percentage and will update the bar to reflect that
        percentage.
        
        :param perc:  Percentage Completed (0-100).
        :type  perc:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._prog_update(GXContext._get_tls_geo(), perc)
        



    @classmethod
    def prog_update_l(cls, v1, v2):
        """
        Updates progress bar based on count and maxcount.
        
        :param v1:  Count
        :param v2:  Max count >= count
        :type  v1:  int
        :type  v2:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._prog_update_l(GXContext._get_tls_geo(), v1, v2)
        




# Registry


    @classmethod
    def get_sys_info(cls, sys_info, info):
        """
        Get system information
        
        :param sys_info:  :ref:`SYS_INFO`
        :param info:      Returned setting
        :type  sys_info:  int
        :type  info:      str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        info.value = gxapi_cy.WrapSYS._get_sys_info(GXContext._get_tls_geo(), sys_info, info.value.encode())
        



    @classmethod
    def registry_get_val(cls, domain, key, sub_key, value):
        """
        Get a registry value
        
        :param domain:   :ref:`REG_DOMAIN`
        :param key:      Key to set
        :param sub_key:  Value name within key
        :param value:    String for value data
        :type  domain:   int
        :type  key:      str
        :type  sub_key:  str
        :type  value:    str_ref

        :returns:        0 if value exists
                         1 if value does not exist
        :rtype:          int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val, value.value = gxapi_cy.WrapSYS._registry_get_val(GXContext._get_tls_geo(), domain, key.encode(), sub_key.encode(), value.value.encode())
        return ret_val



    @classmethod
    def registry_delete_key(cls, domain, key):
        """
        Delete a registry value
        
        :param domain:  :ref:`REG_DOMAIN`
        :param key:     Key to delete
        :type  domain:  int
        :type  key:     str

        :returns:       0 - Ok
                        1 - Error
        :rtype:         int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All sub-keys and values will be deleted if they exist.
        """
        ret_val = gxapi_cy.WrapSYS._registry_delete_key(GXContext._get_tls_geo(), domain, key.encode())
        return ret_val



    @classmethod
    def registry_delete_val(cls, domain, key, value_name):
        """
        Delete a registry value
        
        :param domain:      :ref:`REG_DOMAIN`
        :param key:         Key
        :param value_name:  Name of value to delete
        :type  domain:      int
        :type  key:         str
        :type  value_name:  str

        :returns:           0 - Ok
                            1 - Error
        :rtype:             int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._registry_delete_val(GXContext._get_tls_geo(), domain, key.encode(), value_name.encode())
        return ret_val



    @classmethod
    def registry_set_val(cls, domain, key, sub_key, value):
        """
        Set/create a registry value
        
        :param domain:   :ref:`REG_DOMAIN`
        :param key:      Key to set
        :param sub_key:  Name of Subkey within key
        :param value:    Value for Subkey
        :type  domain:   int
        :type  key:      str
        :type  sub_key:  str
        :type  value:    str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** This function will create the subkey and key if either do not
        already exist.
        """
        gxapi_cy.WrapSYS._registry_set_val(GXContext._get_tls_geo(), domain, key.encode(), sub_key.encode(), value.encode())
        




# Temporary File


    @classmethod
    def destroy_ptmp(cls, ptmp):
        """
        Destroy PTMP.
        
        :param ptmp:  PTMP object to destroy
        :type  ptmp:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._destroy_ptmp(GXContext._get_tls_geo(), ptmp)
        



    @classmethod
    def get_ptmp(cls, ptmp):
        """
        Get temporary saves copy of parameter block.
        
        :param ptmp:  Saved with Save_PTMP_SYS
        :type  ptmp:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `save_ptmp <geosoft.gxapi.GXSYS.save_ptmp>`, `destroy_ptmp <geosoft.gxapi.GXSYS.destroy_ptmp>`
        """
        gxapi_cy.WrapSYS._get_ptmp(GXContext._get_tls_geo(), ptmp)
        



    @classmethod
    def save_ptmp(cls, groups):
        """
        Save a temporary copy of the parameter block.
        
        :param groups:  Group Name to save, "" for everything.
        :type  groups:  str

        :returns:       PTMP handle.
        :rtype:         int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All PTMP instances will be destroyed on exit.

        .. seealso::

            `get_ptmp <geosoft.gxapi.GXSYS.get_ptmp>`, `destroy_ptmp <geosoft.gxapi.GXSYS.destroy_ptmp>`
        """
        ret_val = gxapi_cy.WrapSYS._save_ptmp(GXContext._get_tls_geo(), groups.encode())
        return ret_val




# Termination


    @classmethod
    def abort(cls, message):
        """
        This method terminates the execution of a script. A message
        giving the reason for the abort will be displayed along with
        the line number where we stopped in the script.
        
        :param message:  Message to display
        :type  message:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._abort(GXContext._get_tls_geo(), message.encode())
        



    @classmethod
    def assert_(cls, exp):
        """
        Abort with GX line number if not true.
        
        :param exp:  Expression to evaluate (0 aborts)
        :type  exp:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._assert_(GXContext._get_tls_geo(), exp)
        



    @classmethod
    def exit_(cls):
        """
        This method terminates the execution of a script in  a regular
        fashion with no error messages displayed.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._exit_(GXContext._get_tls_geo())
        



    @classmethod
    def cancel_(cls):
        """
        This method indicates that the GX program terminated without
        doing anything of interest and should be ignored.  In
        particular, the GX will not be logged in a recorded GS.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        gxapi_cy.WrapSYS._cancel_(GXContext._get_tls_geo())
        




# Timing


    @classmethod
    def delay(cls, secs):
        """
        Idle delay method.
        
        :param secs:  Decimal Seconds to delay
        :type  secs:  float

        :returns:     Success if the delay has elapsed.
        :rtype:       int

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._delay(GXContext._get_tls_geo(), secs)
        return ret_val



    @classmethod
    def get_timer(cls, flag, start_time, elapsed_time):
        """
        Return the elapsed time since the established time.
        
        :param flag:          1 - set start time, 0 - return elapsed time
        :param start_time:    Start time in seconds
        :param elapsed_time:  Elapsed time in seconds
        :type  flag:          int
        :type  start_time:    float_ref
        :type  elapsed_time:  float_ref

        :returns:             Success if the delay has elapsed.
        :rtype:               int

        .. versionadded:: 6.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** 1st time through call the method with a flag of 1 to identify
        the count start time, subsequent times the time will be the time
        elapsed since the queried start time.  Do so by settign the flag to 0.
        """
        ret_val, start_time.value, elapsed_time.value = gxapi_cy.WrapSYS._get_timer(GXContext._get_tls_geo(), flag, start_time.value, elapsed_time.value)
        return ret_val




# User Interaction


    @classmethod
    def display_help(cls, group, topic):
        """
        Display the help dialog with the specified topic highlighted
        
        :param group:  Group string to lookup in gxhelp.ini
        :param topic:  Index string to lookup in gxhelp.ini
        :type  group:  str
        :type  topic:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapSYS._display_help(GXContext._get_tls_geo(), group.encode(), topic.encode())
        



    @classmethod
    def display_help_topic(cls, file, topic):
        """
        Display the help dialog without topic lookup in INI files
        
        :param file:   Help File (blank for default)
        :param topic:  Help Topic
        :type  file:   str
        :type  topic:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapSYS._display_help_topic(GXContext._get_tls_geo(), file.encode(), topic.encode())
        



    @classmethod
    def display_int(cls, title, int):
        """
        Display an integer.
        
        :param title:  Title of the Window
        :param int:    Number
        :type  title:  str
        :type  int:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapSYS._display_int(GXContext._get_tls_geo(), title.encode(), int)
        



    @classmethod
    def display_message(cls, title, message):
        """
        Display a user message.
        
        :param title:    Title of the Window
        :param message:  Message String
        :type  title:    str
        :type  message:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapSYS._display_message(GXContext._get_tls_geo(), title.encode(), message.encode())
        



    @classmethod
    def display_double(cls, title, real):
        """
        Display a real number.
        
        :param title:  Title of the Window
        :param real:   Number
        :type  title:  str
        :type  real:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapSYS._display_double(GXContext._get_tls_geo(), title.encode(), real)
        



    @classmethod
    def display_question(cls, title, message):
        """
        Display a YES/NO type question. This method waits
        for the user to hit YES or NO.
        
        :param title:    Title of the window
        :param message:  Message String
        :type  title:    str
        :type  message:  str

        :returns:        0 - user selected No
                         1 - user selected YES
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapSYS._display_question(GXContext._get_tls_geo(), title.encode(), message.encode())
        return ret_val



    @classmethod
    def display_question_with_cancel(cls, title, message):
        """
        Display a YES/NO/CANCEL type question. This method waits
        for the user to hit YES or NO or CANCEL.
        
        :param title:    Title of the window
        :param message:  Message String
        :type  title:    str
        :type  message:  str

        :returns:        0 - user selected No
                         1 - user selected YES
                         2 - user selected CANCEL
        :rtype:          int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapSYS._display_question_with_cancel(GXContext._get_tls_geo(), title.encode(), message.encode())
        return ret_val



    @classmethod
    def display_task_dialog_ui(cls, title, main_instruction, content, common_buttons, custom_button_lst, icon, footer, footer_icon, verification_check_text, verification_checked, expanded_information, collapsed_control_text, expanded_control_text):
        """
        Show a Windows TaskDialog UI (see https://msdn.microsoft.com/en-us/library/windows/desktop/bb760441(v=vs.85).aspx).
        
        :param title:                    Title
        :param main_instruction:         Main instruction (empty string for none)
        :param content:                  Content (empty string for none)
        :param common_buttons:           Common Buttons, one of :ref:`TD_BUTTON`
        :param custom_button_lst:        Optional `GXLST <geosoft.gxapi.GXLST>` of custom buttons. Name in `GXLST <geosoft.gxapi.GXLST>` will be used for button text, while value should be an int to return. Pass (`GXLST <geosoft.gxapi.GXLST>`)0 to only use standard button flags.
        :param icon:                     Icon :ref:`TD_ICON`
        :param footer:                   Footer (empty string for none)
        :param footer_icon:              Footer Icon :ref:`TD_ICON`
        :param verification_check_text:  Verification checkbox text (empty string for none)
        :param verification_checked:     Verification checkbox checked (in/out)
        :param expanded_information:     Expanded information (empty string for none)
        :param collapsed_control_text:   Collapsed control text for expanded information (empty string for default; 'More')
        :param expanded_control_text:    Expanded control text for expanded information (empty string for default; 'Less')
        :type  title:                    str
        :type  main_instruction:         str
        :type  content:                  str
        :type  common_buttons:           int
        :type  custom_button_lst:        GXLST
        :type  icon:                     int
        :type  footer:                   str
        :type  footer_icon:              int
        :type  verification_check_text:  str
        :type  verification_checked:     int_ref
        :type  expanded_information:     str
        :type  collapsed_control_text:   str
        :type  expanded_control_text:    str

        :returns:                        Button ID. One of :ref:`TD_ID` or the int value from `GXLST <geosoft.gxapi.GXLST>` of custom buttons.
        :rtype:                          int

        .. versionadded:: 9.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val, verification_checked.value = gxapi_cy.WrapSYS._display_task_dialog_ui(GXContext._get_tls_geo(), title.encode(), main_instruction.encode(), content.encode(), common_buttons, custom_button_lst, icon, footer.encode(), footer_icon, verification_check_text.encode(), verification_checked.value, expanded_information.encode(), collapsed_control_text.encode(), expanded_control_text.encode())
        return ret_val



    @classmethod
    def interactive(cls):
        """
        Checks to see if you should run interactively.
        

        :returns:    0 - Run in batch mode only
                  1 - Run Interactively only
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._interactive(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def testing_system_mode(cls):
        """
        Checks to see if the GX is running in the Geosoft testing system.
        

        :returns:    0 - Normal operation
                  1 - Running in the Geosoft testing system.
        :rtype:      int

        .. versionadded:: 9.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._testing_system_mode(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def prompt(cls, title, result):
        """
        Asks the User to enter a string.
        
        :param title:   Title of the window
        :param result:  Buffer to place the user's string
        :type  title:   str
        :type  result:  str_ref

        :returns:       0 - User hit OK
                        1 - user hit CANCEL
        :rtype:         int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The User string is displayed as the default value in the prompt.
        Empty the user string if no default is needed.
        """
        ret_val, result.value = gxapi_cy.WrapSYS._prompt(GXContext._get_tls_geo(), title.encode(), result.value.encode())
        return ret_val



    @classmethod
    def script(cls):
        """
        Checks to see if we are running inside OMS (script mode)
        

        :returns:    0 - Normal mode
                  1 - Scripting mode

                  A number of functions can only be run from inside Oasis montaj
                  (such as `GXEMAP.get_display_area_raw <geosoft.gxapi.GXEMAP.get_display_area_raw>`), because they require an actual
                  window object, such as an editable database or map. Use this
                  function to prevent calls
        :rtype:      int

        .. versionadded:: 6.0.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._script(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def script_record(cls):
        """
        Checks to see if we are in scripting recording mode
        

        :returns:    0 - Normal mode
                  1 - Recording mode
        :rtype:      int

        .. versionadded:: 6.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._script_record(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def set_cursor(cls, cursor):
        """
        Set the cursor on the display.
        
        :param cursor:  Cursor Names
        :type  cursor:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Possible Cursors:
        Normal, Horiz, Vert, Moving, Cross, Hand, NoEdit, Sun,
        View, Group, ViewSel, GroupSel, BoxSelect, Shadow, Link,
        Line, PolyLine, Polygon, Ellipse, Rectangle, Text, Symbol,
        Zoom, Pan, Rotate, InteractiveZoom, PolyFill, GetFill,
        SnapPoint, SnapLine, SnapOnPoint, SnapOnLine, NPolygon,
        ExcludeRect, ExcludePoly, ExcludeNPoly, AddVertex, DelVertex, GeneralAdd and GeneralDelete
        """
        gxapi_cy.WrapSYS._set_cursor(GXContext._get_tls_geo(), cursor.encode())
        



    @classmethod
    def set_info_line(cls, message):
        """
        Display a message on the information line at the left
        bottom corner of the OAISIS montaj application.
        
        :param message:  Message String
        :type  message:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapSYS._set_info_line(GXContext._get_tls_geo(), message.encode())
        



    @classmethod
    def set_interactive(cls, mode):
        """
        Sets the interactive mode.
        
        :param mode:  0 - interactive off 1 - interative on
        :type  mode:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Call to `interactive <geosoft.gxapi.GXSYS.interactive>` will return the value
        set here.

        .. seealso::

            `interactive <geosoft.gxapi.GXSYS.interactive>`, `run_gx <geosoft.gxapi.GXSYS.run_gx>` and `run_gs <geosoft.gxapi.GXSYS.run_gs>`
        """
        gxapi_cy.WrapSYS._set_interactive(GXContext._get_tls_geo(), mode)
        




# Workspace


    @classmethod
    def get_workspace_reg(cls, reg):
        """
        Get a copy of the workspace `GXREG <geosoft.gxapi.GXREG>`;
        
        :param reg:  `GXREG <geosoft.gxapi.GXREG>` object
        :type  reg:  GXREG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The workspace `GXREG <geosoft.gxapi.GXREG>` is separate from the reg used
        to store `GXSYS <geosoft.gxapi.GXSYS>` parameters.

        Because `get_workspace_reg <geosoft.gxapi.GXSYS.get_workspace_reg>` returns a copy of the
        workspace `GXREG <geosoft.gxapi.GXREG>`, and not the workspace `GXREG <geosoft.gxapi.GXREG>` itself,
        you must call `set_workspace_reg <geosoft.gxapi.GXSYS.set_workspace_reg>` if you make changes
        to your own `GXREG <geosoft.gxapi.GXREG>` object and you wish them to take
        effect in the workspace `GXREG <geosoft.gxapi.GXREG>`.
        """
        gxapi_cy.WrapSYS._get_workspace_reg(GXContext._get_tls_geo(), reg)
        



    @classmethod
    def set_workspace_reg(cls, reg):
        """
        Set the workspace `GXREG <geosoft.gxapi.GXREG>`;
        
        :param reg:  `GXREG <geosoft.gxapi.GXREG>` object
        :type  reg:  GXREG

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The workspace `GXREG <geosoft.gxapi.GXREG>` is separate from the reg used
        to store `GXSYS <geosoft.gxapi.GXSYS>` parameters.

        Because `get_workspace_reg <geosoft.gxapi.GXSYS.get_workspace_reg>` returns a copy of the
        workspace `GXREG <geosoft.gxapi.GXREG>`, and not the workspace `GXREG <geosoft.gxapi.GXREG>` itself,
        you must call `set_workspace_reg <geosoft.gxapi.GXSYS.set_workspace_reg>` if you make changes
        to your own `GXREG <geosoft.gxapi.GXREG>` object and you wish them to take
        effect in the workspace `GXREG <geosoft.gxapi.GXREG>`
        """
        gxapi_cy.WrapSYS._set_workspace_reg(GXContext._get_tls_geo(), reg)
        




# String Encryption


    @classmethod
    def encrypt_string(cls, input, output, key):
        """
        Encrypts a string for secure storage in configuration files
        or in the workspace parameters.
        
        :param input:   Input string for encryption.
        :param output:  Output buffer for encrypted result.
        :param key:     :ref:`SYS_ENCRYPTION_KEY`
        :type  input:   str
        :type  output:  str_ref
        :type  key:     int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        output.value = gxapi_cy.WrapSYS._encrypt_string(GXContext._get_tls_geo(), input.encode(), output.value.encode(), key)
        



    @classmethod
    def decrypt_string(cls, input, output, key):
        """
        Decrypts a string that has been previously encrypted by `encrypt_string <geosoft.gxapi.GXSYS.encrypt_string>`.
        
        :param input:   Input string for decryption.
        :param output:  Output buffer for decrypted result.
        :param key:     :ref:`SYS_ENCRYPTION_KEY`
        :type  input:   str
        :type  output:  str_ref
        :type  key:     int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        output.value = gxapi_cy.WrapSYS._decrypt_string(GXContext._get_tls_geo(), input.encode(), output.value.encode(), key)
        



    @classmethod
    def is_encrypted_string(cls, input):
        """
        Checks whether the specified string was encrypted by `encrypt_string <geosoft.gxapi.GXSYS.encrypt_string>`.
        
        :param input:  Input string to inspect.
        :type  input:  str

        :returns:      0 (false) or non-zero (true)
        :rtype:        int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_
        """
        ret_val = gxapi_cy.WrapSYS._is_encrypted_string(GXContext._get_tls_geo(), input.encode())
        return ret_val




# GX Debugger


    @classmethod
    def disable_gx_debugger(cls):
        """
        Disable GX Debugger `GXGUI <geosoft.gxapi.GXGUI>` if active
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** All breakpoints will be cleared by this call.
        """
        gxapi_cy.WrapSYS._disable_gx_debugger(GXContext._get_tls_geo())
        



    @classmethod
    def enable_gx_debugger(cls, src_dir, first_gx):
        """
        Enable GX Debugger `GXGUI <geosoft.gxapi.GXGUI>`
        
        :param src_dir:   Path that will be scanned recursively for GXC source files
        :param first_gx:  Name of gx where first breakpoint should be set
        :type  src_dir:   str
        :type  first_gx:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** Takes as input two strings one a path that will be scanned
        recursively for GXC source files and a second string without
        a path of the GX where the first breakpoint should be set in (i.e. "gxname.gx").
        The source of the GX should be found in the path (e.g. <path>\\somewhere\\gxname.gxc)
        and a breakpoint will be set on the first executing line of this GX. Make sure the
        GX binary is newer than the source file, otherwise unexpected results may occur. As
        soon as the GX is run the `GXGUI <geosoft.gxapi.GXGUI>` will become visible and it will be possible to set more
        breakpoints in any of the GXC files found in the path.
        """
        gxapi_cy.WrapSYS._enable_gx_debugger(GXContext._get_tls_geo(), src_dir.encode(), first_gx.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer