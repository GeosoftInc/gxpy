### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
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
class GXSYS:
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

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapSYS(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXSYS`
        
        :returns: A null `GXSYS`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXSYS` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXSYS`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Date/Time


    @classmethod
    def break_date(cls, date, year, month, day):
        """
        Breaks a decimal date value into year, month and day.
        """
        year.value, month.value, day.value = gxapi_cy.WrapSYS.break_date(GXContext._get_tls_geo(), date, year.value, month.value, day.value)
        



    @classmethod
    def dateto_long(cls, date):
        """
        Converts a double date to a value representing total
        days elapsed since day 0 of year 0. This uses the
        Numerical Receipies Julian function.
        """
        ret_val = gxapi_cy.WrapSYS.dateto_long(GXContext._get_tls_geo(), date)
        return ret_val



    @classmethod
    def timeto_long(cls, time):
        """
        Converts decimal hours to seconds in a day.
        """
        ret_val = gxapi_cy.WrapSYS.timeto_long(GXContext._get_tls_geo(), time)
        return ret_val



    @classmethod
    def date(cls):
        """
        Returns the current date in decimal years.

        **Note:**

        The FormatDate_STR function can be used to convert a date to
        a string.
        """
        ret_val = gxapi_cy.WrapSYS.date(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def longto_date(cls, days):
        """
        Converts a value representing total days elapsed since
        day 0 of year 0 to a geosoft date. This uses the
        Numerical Receipies Julian function.
        """
        ret_val = gxapi_cy.WrapSYS.longto_date(GXContext._get_tls_geo(), days)
        return ret_val



    @classmethod
    def longto_time(cls, sec):
        """
        Converts seconds to decimal hours.
        """
        ret_val = gxapi_cy.WrapSYS.longto_time(GXContext._get_tls_geo(), sec)
        return ret_val



    @classmethod
    def make_date(cls, year, month, day):
        """
        Returns the decimal date given the year, month and day.
        """
        ret_val = gxapi_cy.WrapSYS.make_date(GXContext._get_tls_geo(), year, month, day)
        return ret_val



    @classmethod
    def secondsto_time(cls, sec):
        """
        Converts fractional seconds to decimal hours.
        """
        ret_val = gxapi_cy.WrapSYS.secondsto_time(GXContext._get_tls_geo(), sec)
        return ret_val



    @classmethod
    def time(cls):
        """
        Returns the current time in decimal hours.

        **Note:**

        The FormatTime_STR function can be used to convert a time to
        a string.
        """
        ret_val = gxapi_cy.WrapSYS.time(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def timeto_seconds(cls, time):
        """
        Converts decimal hours to seconds in a day fractional
        """
        ret_val = gxapi_cy.WrapSYS.timeto_seconds(GXContext._get_tls_geo(), time)
        return ret_val



    @classmethod
    def utc_date(cls):
        """
        Returns the current UTC date in decimal years.

        **Note:**

        The FormatDate_STR function can be used to convert a date to
        a string.
        """
        ret_val = gxapi_cy.WrapSYS.utc_date(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def utc_time(cls):
        """
        Returns the current UTC time in decimal hours.

        **Note:**

        The FormatTime_STR function can be used to convert a time to
        a string.
        """
        ret_val = gxapi_cy.WrapSYS.utc_time(GXContext._get_tls_geo())
        return ret_val




# Environment


    @classmethod
    def exist_env(cls, parm):
        """
        Check if setting exists in environment.
        """
        ret_val = gxapi_cy.WrapSYS.exist_env(GXContext._get_tls_geo(), parm.encode())
        return ret_val



    @classmethod
    def get_env(cls, parm, set):
        """
        Get an environment setting.
        """
        set.value = gxapi_cy.WrapSYS.get_env(GXContext._get_tls_geo(), parm.encode(), set.value.encode())
        



    @classmethod
    def set_env(cls, parm, set):
        """
        Set an environment setting.
        """
        gxapi_cy.WrapSYS.set_env(GXContext._get_tls_geo(), parm.encode(), set.encode())
        




# Error Handling


    @classmethod
    def clear_err_ap(cls):
        """
        This method is called at to clear all registered errors.
        """
        ret_val = gxapi_cy.WrapSYS.clear_err_ap(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_top_error_ap(cls):
        """
        Get the error number of the last registered error.
        """
        ret_val = gxapi_cy.WrapSYS.get_top_error_ap(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_error_message_ap(cls, err, err_str):
        """
        Return the error message text as a string.

        **Note:**

        This wrapper is mostly for use outside of GXs,
        because in general if an error is registered in a GX
        the GX would terminate before it could be called.
        Use `num_errors_ap <geosoft.gxapi.GXSYS.num_errors_ap>` to get the number of registered errors.
        """
        err_str.value = gxapi_cy.WrapSYS.get_error_message_ap(GXContext._get_tls_geo(), err, err_str.value.encode())
        



    @classmethod
    def num_errors_ap(cls):
        """
        Returns the number of registered errors.

        **Note:**

        This wrapper is mostly for use outside of GXs,
        because in general if an error is registered in a GX
        the GX would terminate before it could be called.

        .. seealso::

            GetErrorMessageAP_SYS
        """
        ret_val = gxapi_cy.WrapSYS.num_errors_ap(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def set_server_messages_ap(cls, flag):
        """
        Control the server message handling.

        **Note:**

        Should be set to false when dialogs should not
        appear. This setting is thread specific.
        """
        gxapi_cy.WrapSYS.set_server_messages_ap(GXContext._get_tls_geo(), flag)
        




# Execution


    @classmethod
    def run(cls, command, args, process):
        """
        Run a command line process.

        **Note:**

        The Default option for each define below is the first one
        and is set to 0.
        
        We look for the command object in the following order:
        
        1. the local working directory
        2. the <geosoft>\\bin directory
        3. the system path
        """
        ret_val = gxapi_cy.WrapSYS.run(GXContext._get_tls_geo(), command.encode(), args.encode(), process)
        return ret_val



    @classmethod
    def run_gs(cls, gs):
        """
        Run a GS.

        .. seealso::

            `set_interactive <geosoft.gxapi.GXSYS.set_interactive>`, `run_gx <geosoft.gxapi.GXSYS.run_gx>`
        """
        ret_val = gxapi_cy.WrapSYS.run_gs(GXContext._get_tls_geo(), gs.encode())
        return ret_val



    @classmethod
    def run_gx(cls, gx):
        """
        Run a GX.

        **Note:**

        If the called GX returns an error, they will not be
        displayed until the "top" calling GX terminates, unless you
        call `show_error <geosoft.gxapi.GXSYS.show_error>`.

        .. seealso::

            `run_gx_ex <geosoft.gxapi.GXSYS.run_gx_ex>`, `set_interactive <geosoft.gxapi.GXSYS.set_interactive>` and `run_gs <geosoft.gxapi.GXSYS.run_gs>`
        """
        ret_val = gxapi_cy.WrapSYS.run_gx(GXContext._get_tls_geo(), gx.encode())
        return ret_val



    @classmethod
    def run_gx_ex(cls, gx, ret):
        """
        Run a GX.

        .. seealso::

            `run_gx <geosoft.gxapi.GXSYS.run_gx>`, `set_return <geosoft.gxapi.GXSYS.set_return>`
        """
        ret_val, ret.value = gxapi_cy.WrapSYS.run_gx_ex(GXContext._get_tls_geo(), gx.encode(), ret.value)
        return ret_val



    @classmethod
    def run_pdf(cls, mnu, pdf):
        """
        Run a PDF.

        **Note:**

        The group name of the PDF variables will be "group_pdf",
        where "group" is the name given in the first argument,
        and "pdf" is the root PDF file name.
        """
        ret_val = gxapi_cy.WrapSYS.run_pdf(GXContext._get_tls_geo(), mnu.encode(), pdf.encode())
        return ret_val



    @classmethod
    def shell_execute(cls, verb, file, parameters, directory, show):
        """
        Call Microsoft ShellExecute function (See `MSDN <https://msdn.microsoft.com/en-us/library/windows/desktop/bb762153(v=vs.85).aspx>`_)

        .. seealso::

            `do_command <geosoft.gxapi.GXSYS.do_command>`
        """
        ret_val = gxapi_cy.WrapSYS.shell_execute(GXContext._get_tls_geo(), verb.encode(), file.encode(), parameters.encode(), directory.encode(), show)
        return ret_val



    @classmethod
    def set_return(cls, ret):
        """
        Set the return value of a GX.

        **Note:**

        This value is returned in the `run_gx_ex <geosoft.gxapi.GXSYS.run_gx_ex>` call only.
        """
        gxapi_cy.WrapSYS.set_return(GXContext._get_tls_geo(), ret)
        




# External DLL


    @classmethod
    def do_command(cls, command):
        """
        Execute an Oasis montaj command.

        **Note:**

        Commands syntax:  "[type] command"
        
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
        gxapi_cy.WrapSYS.do_command(GXContext._get_tls_geo(), command.encode())
        



    @classmethod
    def error(cls, error_file, module, error):
        """
        Register an error message

        **Note:**

        Use this function to register your own error
        messages when an error occurs in your code.  Your
        errors can be provided in your own `GXGER <geosoft.gxapi.GXGER>` file.  See
        GEOSOFT.`GXGER <geosoft.gxapi.GXGER>` for an example of the `GXGER <geosoft.gxapi.GXGER>` file format.
        
        If the error # is not found in your error file, the
        OE32.`GXGER <geosoft.gxapi.GXGER>` file, then the GEOSOFT.`GXGER <geosoft.gxapi.GXGER>` file will be
        searched.
        """
        gxapi_cy.WrapSYS.error(GXContext._get_tls_geo(), error_file.encode(), module.encode(), error)
        



    @classmethod
    def error_tag(cls, tag, set):
        """
        Set an error message tag string

        **Note:**

        Use this method to replace tag strings in your error
        message text with run-time information.  For example,
        Geosoft error messages often use the tag strings "%1",
        "%2", etc. as place holders to be replaced by a string
        which is only known at run-time.
        """
        gxapi_cy.WrapSYS.error_tag(GXContext._get_tls_geo(), tag.encode(), set.encode())
        



    @classmethod
    def assert_gx(cls, exp, mod, parm):
        """
        DLL function argument error assertion

        **Note:**

        Use this function to evaluate errors in passed
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
        ret_val = gxapi_cy.WrapSYS.assert_gx(GXContext._get_tls_geo(), exp, mod.encode(), parm.encode())
        return ret_val



    @classmethod
    def ole_automation(cls, object, info_str, info_val):
        """
        Call OLE Automation designed to be called from Montaj.
        """
        ret_val = gxapi_cy.WrapSYS.ole_automation(GXContext._get_tls_geo(), object.encode(), info_str.encode(), info_val)
        return ret_val



    @classmethod
    def save_log(cls, file):
        """
        Saves the main log file to another file.
        """
        gxapi_cy.WrapSYS.save_log(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def terminate(cls, name):
        """
        DLL error termination

        **Note:**

        Call this function immediately before returning to
        the caller after an error has occurred inside the
        DLL.  If an error has occurred, you should clean-up
        (free memory, close files), call `error <geosoft.gxapi.GXSYS.error>` to register
        your own error messages, call `error_tag <geosoft.gxapi.GXSYS.error_tag>` to set any
        error message tags, call `terminate <geosoft.gxapi.GXSYS.terminate>` and return.
        
        Geosoft functions that detect an error will have
        already registered their own errors and called
        `terminate <geosoft.gxapi.GXSYS.terminate>`.
        """
        gxapi_cy.WrapSYS.terminate(GXContext._get_tls_geo(), name.encode())
        




# File System


    @classmethod
    def crc_file(cls, file):
        """
        Compute the CRC of a file
        """
        ret_val = gxapi_cy.WrapSYS.crc_file(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def crc_file_offset(cls, file, offset):
        """
        Compute the CRC of a file with an Offset
        """
        ret_val = gxapi_cy.WrapSYS.crc_file_offset(GXContext._get_tls_geo(), file.encode(), offset)
        return ret_val



    @classmethod
    def file_ren(cls, old_file, new_file):
        """
        Rename a file
        """
        gxapi_cy.WrapSYS.file_ren(GXContext._get_tls_geo(), old_file.encode(), new_file.encode())
        



    @classmethod
    def find_files_vv(cls, vv, mask):
        """
        Fill a `GXVV <geosoft.gxapi.GXVV>` with files matching an input file mask.

        **Note:**

        Fill a `GXVV <geosoft.gxapi.GXVV>` with files matching the input file mask.
        The `GXVV <geosoft.gxapi.GXVV>` should be of string type.
        """
        gxapi_cy.WrapSYS.find_files_vv(GXContext._get_tls_geo(), vv._wrapper, mask.encode())
        



    @classmethod
    def absolute_file_name(cls, abbr, name):
        """
        Convert an abbreviated path name to a full path name.

        **Note:**

        This is mainly intended to convert ".\\name" to a full
        name at run-time.
        """
        name.value = gxapi_cy.WrapSYS.absolute_file_name(GXContext._get_tls_geo(), abbr.encode(), name.value.encode())
        



    @classmethod
    def copy_file(cls, src_file, dest_file):
        """
        Copy a file.
        """
        ret_val = gxapi_cy.WrapSYS.copy_file(GXContext._get_tls_geo(), src_file.encode(), dest_file.encode())
        return ret_val



    @classmethod
    def delete_file(cls, file):
        """
        Delete a file.
        """
        ret_val = gxapi_cy.WrapSYS.delete_file(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def delete_gi_file(cls, file):
        """
        Delete the GI file associated with a grid.
        """
        ret_val = gxapi_cy.WrapSYS.delete_gi_file(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def delete_grid_file(cls, file):
        """
        Delete a grid file and its associated GI and XML files.

        **Note:**

        Deletes the grid file first, and, if they exist, the associated GI
        and XML files.
        No error is registered if a file is not found or cannot be deleted.
        """
        ret_val = gxapi_cy.WrapSYS.delete_grid_file(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def dir_exist(cls, dir):
        """
        Check to see if a directory exists
        """
        ret_val = gxapi_cy.WrapSYS.dir_exist(GXContext._get_tls_geo(), dir.encode())
        return ret_val



    @classmethod
    def file_exist(cls, file):
        """
        Check to see if a file exists

        **Note:**

        Use the FULL path for the file name. If the full
        path is not specified, then the current working
        directory is used for the path.
        """
        ret_val = gxapi_cy.WrapSYS.file_exist(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def file_size(cls, file):
        """
        Returns size of a file.
        """
        ret_val = gxapi_cy.WrapSYS.file_size(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def file_writable(cls, file):
        """
        Check if a file can be created or opened in read-write mode
        at a specific location
        """
        ret_val = gxapi_cy.WrapSYS.file_writable(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def find_path(cls, file, mode, fullname):
        """
        Get full path for a file with Geosoft subdirectory parameter.

        **Note:**

        Directories can be resolved from the Environment section of the
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
        ret_val, fullname.value = gxapi_cy.WrapSYS.find_path(GXContext._get_tls_geo(), file.encode(), mode, fullname.value.encode())
        return ret_val



    @classmethod
    def find_path_ex(cls, file, mode, dir_mode, fullname):
        """
        Get full path for a file.

        **Note:**

        Directories can be resolved from the Environment section of the
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
        ret_val, fullname.value = gxapi_cy.WrapSYS.find_path_ex(GXContext._get_tls_geo(), file.encode(), mode, dir_mode, fullname.value.encode())
        return ret_val



    @classmethod
    def get_directory(cls, sys_dir, dir):
        """
        Get a directory path

        **Note:**

        The path will always end with the file separator character
        """
        dir.value = gxapi_cy.WrapSYS.get_directory(GXContext._get_tls_geo(), sys_dir, dir.value.encode())
        



    @classmethod
    def get_path(cls, type, path):
        """
        Get a Geosoft path

        **Note:**

        The path name will have a directory separator at the end.
        """
        path.value = gxapi_cy.WrapSYS.get_path(GXContext._get_tls_geo(), type, path.value.encode())
        



    @classmethod
    def get_windows_dir(cls, dir):
        """
        Get the Windows directory path
        """
        dir.value = gxapi_cy.WrapSYS.get_windows_dir(GXContext._get_tls_geo(), dir.value.encode())
        



    @classmethod
    def make_dir(cls, dir):
        """
        Create a directory.
        """
        ret_val = gxapi_cy.WrapSYS.make_dir(GXContext._get_tls_geo(), dir.encode())
        return ret_val



    @classmethod
    def make_file_readonly(cls, file):
        """
        Set a file's read-only attribute.
        """
        ret_val = gxapi_cy.WrapSYS.make_file_readonly(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def make_file_writable(cls, file):
        """
        Removes a file's read-only attribute.
        """
        ret_val = gxapi_cy.WrapSYS.make_file_writable(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def relative_file_name(cls, abbr, name):
        """
        Convert a file name to a relative abbreviated path name

        **Note:**

        This will produce relative paths based on the workspace
        directory into ".\\name".
        """
        name.value = gxapi_cy.WrapSYS.relative_file_name(GXContext._get_tls_geo(), abbr.encode(), name.value.encode())
        



    @classmethod
    def short_path_file_name(cls, in_name, name):
        """
        Obtains the short path form of a specified input path.
        """
        name.value = gxapi_cy.WrapSYS.short_path_file_name(GXContext._get_tls_geo(), in_name.encode(), name.value.encode())
        



    @classmethod
    def temp_file_ext(cls, ext, out):
        """
        Generate a unique file name for this extension in the temp directory.

        **Note:**

        This is useful for created a unique tempory name for a file in the Geosoft temporary directory.
        """
        out.value = gxapi_cy.WrapSYS.temp_file_ext(GXContext._get_tls_geo(), ext.encode(), out.value.encode())
        



    @classmethod
    def temp_file_name(cls, path_file, out_filename):
        """
        Generate a file name for this file in the temp directory.

        **Note:**

        This is useful for created a unique tempory name for a file in the Geosoft temporary directory.
        
        From version 7.0 The file extension will match the input file, but the
        filename itself will be a process and thread unique value to ensure that
        clashes does not happen.
        """
        out_filename.value = gxapi_cy.WrapSYS.temp_file_name(GXContext._get_tls_geo(), path_file.encode(), out_filename.value.encode())
        



    @classmethod
    def transfer_path(cls, path_file, file):
        """
        Transfers file path to new file name.

        **Note:**

        The path and volume of from the input string is added to
        file name from the output string.
        """
        file.value = gxapi_cy.WrapSYS.transfer_path(GXContext._get_tls_geo(), path_file.encode(), file.value.encode())
        



    @classmethod
    def valid_file_name(cls, file):
        """
        Check to see if a file name valid

        **Note:**

        Use the FULL path for the file name. If the full
        path is not specified, then the current working
        directory is used for the path.
        """
        ret_val = gxapi_cy.WrapSYS.valid_file_name(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def write_in_dir(cls, dir):
        """
        Can I create files in this directory ?
        """
        ret_val = gxapi_cy.WrapSYS.write_in_dir(GXContext._get_tls_geo(), dir.encode())
        return ret_val



    @classmethod
    def file_date(cls, file):
        """
        File creation date in decimal years.

        **Note:**

        The FormatDate_STR function can be used to convert a date
        to a string.
        """
        ret_val = gxapi_cy.WrapSYS.file_date(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def file_time(cls, file):
        """
        File creation time in decimal hours.

        **Note:**

        The FormatTime_STR function can be used to convert a time
        to a string.
        """
        ret_val = gxapi_cy.WrapSYS.file_time(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def utc_file_date(cls, file):
        """
        File creation UTC date in decimal years.

        **Note:**

        The FormatDate_STR function can be used to convert a date
        to a string.
        """
        ret_val = gxapi_cy.WrapSYS.utc_file_date(GXContext._get_tls_geo(), file.encode())
        return ret_val



    @classmethod
    def utc_file_time(cls, file):
        """
        File creation UTC time in decimal hours.

        **Note:**

        The FormatTime_STR function can be used to convert a time
        to a string.
        """
        ret_val = gxapi_cy.WrapSYS.utc_file_time(GXContext._get_tls_geo(), file.encode())
        return ret_val




# Global Parameter


    @classmethod
    def get_settings_meta(cls, meta):
        """
        Get the settings metadata object.
        """
        gxapi_cy.WrapSYS.get_settings_meta(GXContext._get_tls_geo(), meta._wrapper)
        



    @classmethod
    def global_reset(cls, ini):
        """
        Reset the global parameters.
        """
        gxapi_cy.WrapSYS.global_reset(GXContext._get_tls_geo(), ini.encode())
        



    @classmethod
    def global_set(cls, parm, set):
        """
        Set a global parameter setting.
        """
        gxapi_cy.WrapSYS.global_set(GXContext._get_tls_geo(), parm.encode(), set.encode())
        



    @classmethod
    def global_write(cls, ini):
        """
        Modify the global parameters.

        **Note:**

        If the global parameters have been changed, use
        this function to make the changes permanent,
        """
        gxapi_cy.WrapSYS.global_write(GXContext._get_tls_geo(), ini.encode())
        



    @classmethod
    def global_(cls, parm, setting):
        """
        Get a global parameter setting.

        **Note:**

        The returned string will be empty if the parameter is
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
        ret_val, setting.value = gxapi_cy.WrapSYS.global_(GXContext._get_tls_geo(), parm.encode(), setting.value.encode())
        return ret_val



    @classmethod
    def reset_settings(cls):
        """
        Resets the GX_HELP settings in the geosoft.ini file
        after changes have been made.
        """
        gxapi_cy.WrapSYS.reset_settings(GXContext._get_tls_geo())
        



    @classmethod
    def set_settings_meta(cls, meta):
        """
        Set the settings metadata object.
        """
        gxapi_cy.WrapSYS.set_settings_meta(GXContext._get_tls_geo(), meta._wrapper)
        




# Licensing


    @classmethod
    def check_arc_license(cls):
        """
        Check to see if a ESRI ArcEngine or ArcView license is available
        """
        ret_val = gxapi_cy.WrapSYS.check_arc_license(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def check_arc_license_ex(cls, version):
        """
        Check to see if a ESRI ArcEngine or ArcView license is available, returns type and version of available engine.
        """
        ret_val, version.value = gxapi_cy.WrapSYS.check_arc_license_ex(GXContext._get_tls_geo(), version.value.encode())
        return ret_val



    @classmethod
    def check_intrinsic(cls, cl, name):
        """
        Check to see if an intrinsic object is licensed
        """
        ret_val = gxapi_cy.WrapSYS.check_intrinsic(GXContext._get_tls_geo(), cl, name.encode())
        return ret_val



    @classmethod
    def get_geodist(cls):
        """
        Gets a global flag that indicates whether we are
        running within the geodist library
        """
        ret_val = gxapi_cy.WrapSYS.get_geodist(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def get_license_class(cls, cl):
        """
        Get the current application license class.

        **Note:**

        String may be one of :  "ArcGIS"
        "OasisMontaj"
        "DapServer"
        """
        cl.value = gxapi_cy.WrapSYS.get_license_class(GXContext._get_tls_geo(), cl.value.encode())
        



    @classmethod
    def get_licensed_user(cls, user, company):
        """
        Get the licensed user name and Company
        """
        user.value, company.value = gxapi_cy.WrapSYS.get_licensed_user(GXContext._get_tls_geo(), user.value.encode(), company.value.encode())
        




# Lineage


    @classmethod
    def add_lineage_parameter(cls, name, value):
        """
        Add a parameter to the current lineage object
        """
        gxapi_cy.WrapSYS.add_lineage_parameter(GXContext._get_tls_geo(), name.encode(), value.encode())
        



    @classmethod
    def add_lineage_source(cls, source_type, source_name):
        """
        Add a source to the current lineage object
        """
        gxapi_cy.WrapSYS.add_lineage_source(GXContext._get_tls_geo(), source_type, source_name.encode())
        



    @classmethod
    def clear_lineage_parameters(cls):
        """
        Clear all the lineage parameters
        """
        gxapi_cy.WrapSYS.clear_lineage_parameters(GXContext._get_tls_geo())
        



    @classmethod
    def clear_lineage_sources(cls):
        """
        Clear all the lineage sources
        """
        gxapi_cy.WrapSYS.clear_lineage_sources(GXContext._get_tls_geo())
        



    @classmethod
    def copy_geo_file(cls, data, dir):
        """
        Copy a Geosoft data file and all associated files to a new folder

        **Note:**

        Grids are copied and the GI's are maintained - note that support
        for non-geosoft grids is limited since this method does not
        guarantee all grid files besides the main one are copied.
        """
        gxapi_cy.WrapSYS.copy_geo_file(GXContext._get_tls_geo(), data.encode(), dir.encode())
        



    @classmethod
    def backup_geo_file(cls, data, target):
        """
        Backup a Geosoft data file and all associated files to a temporary folder.

        **Note:**

        Grids are copied and the GI's are maintained - note that support
        for non-geosoft grids is limited since this method does not
        guarantee all grid files besides the main one are copied.
        """
        target.value = gxapi_cy.WrapSYS.backup_geo_file(GXContext._get_tls_geo(), data.encode(), target.value.encode())
        



    @classmethod
    def remove_lineage_output(cls, output_name):
        """
        Remove an output from the current lineage object
        """
        gxapi_cy.WrapSYS.remove_lineage_output(GXContext._get_tls_geo(), output_name.encode())
        



    @classmethod
    def remove_lineage_parameter(cls, name):
        """
        Remove a parameter in the current lineage object
        """
        gxapi_cy.WrapSYS.remove_lineage_parameter(GXContext._get_tls_geo(), name.encode())
        



    @classmethod
    def remove_lineage_source(cls, source_name):
        """
        Remove a source from the current lineage object
        """
        gxapi_cy.WrapSYS.remove_lineage_source(GXContext._get_tls_geo(), source_name.encode())
        



    @classmethod
    def restore_geo_file(cls, target, original):
        """
        Backup a Geosoft data file and all associated files to original location

        **Note:**

        Grids are copied and the GI's are maintained - note that support
        for non-geosoft grids is limited since this method does not
        guarantee all grid files besides the main one are copied.
        """
        gxapi_cy.WrapSYS.restore_geo_file(GXContext._get_tls_geo(), target.encode(), original.encode())
        



    @classmethod
    def set_lineage_description(cls, description):
        """
        Set the description for the current lineage object
        """
        gxapi_cy.WrapSYS.set_lineage_description(GXContext._get_tls_geo(), description.encode())
        



    @classmethod
    def set_lineage_display_name(cls, display_name):
        """
        Set the display name for the current lineage object
        """
        gxapi_cy.WrapSYS.set_lineage_display_name(GXContext._get_tls_geo(), display_name.encode())
        



    @classmethod
    def set_lineage_name(cls, name):
        """
        Set the name for the current lineage object
        """
        gxapi_cy.WrapSYS.set_lineage_name(GXContext._get_tls_geo(), name.encode())
        




# Menus and Toolbar


    @classmethod
    def clear_menus(cls, flag):
        """
        Clear all menus
        """
        gxapi_cy.WrapSYS.clear_menus(GXContext._get_tls_geo(), flag)
        



    @classmethod
    def get_loaded_menus(cls, lst_default, lst_loaded, lst_user):
        """
        Get the loaded menus.

        **Note:**

        The names of the LSTs contain the menus and the values contain any exclusions. Exlusions 
        are semicolon separated top level menu names and/or toolbar.geobar file names.
        """
        gxapi_cy.WrapSYS.get_loaded_menus(GXContext._get_tls_geo(), lst_default._wrapper, lst_loaded._wrapper, lst_user._wrapper)
        



    @classmethod
    def set_loaded_menus(cls, lst_default, lst_loaded, lst_user):
        """
        Load a list of menus

        **Note:**

        The names of the LSTs contain the menus and the values contain any exclusions. Exlusions 
        are semicolon separated top level menu names and/or toolbar.geobar file names.
        """
        gxapi_cy.WrapSYS.set_loaded_menus(GXContext._get_tls_geo(), lst_default._wrapper, lst_loaded._wrapper, lst_user._wrapper)
        



    @classmethod
    def get_entitlement_rights(cls, lst_rights):
        """
        Get the Entitlement Rights
        """
        gxapi_cy.WrapSYS.get_entitlement_rights(GXContext._get_tls_geo(), lst_rights._wrapper)
        




# Misc


    @classmethod
    def generate_guid(cls, guid):
        """
        Genrates a GUID string (e.g. {4FEDE8BF-CDAB-430A-8026-1CCC0EC0A2EB})
        """
        guid.value = gxapi_cy.WrapSYS.generate_guid(GXContext._get_tls_geo(), guid.value.encode())
        



    @classmethod
    def clipboard_to_file(cls, file):
        """
        Copy text from the clipboard to a file.
        """
        gxapi_cy.WrapSYS.clipboard_to_file(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def create_clipboard_ra(cls):
        """
        Create a `GXRA <geosoft.gxapi.GXRA>` to read text from the clipboard.

        **Note:**

        Destroy the `GXRA <geosoft.gxapi.GXRA>` as soon as possible. As long as it
        open the clipboard is not accessible from any
        application.
        """
        ret_val = gxapi_cy.WrapSYS.create_clipboard_ra(GXContext._get_tls_geo())
        return GXRA(ret_val)



    @classmethod
    def create_clipboard_wa(cls):
        """
        Create a `GXWA <geosoft.gxapi.GXWA>` to write text on the clipboard.

        **Note:**

        Destroy the `GXWA <geosoft.gxapi.GXWA>` as soon as possible. As long as it
        open the clipboard is not accessible from any
        application.
        """
        ret_val = gxapi_cy.WrapSYS.create_clipboard_wa(GXContext._get_tls_geo())
        return GXWA(ret_val)



    @classmethod
    def emf_object_size(cls, file, size_x, size_y):
        """
        Get the size of an EMF object
        """
        size_x.value, size_y.value = gxapi_cy.WrapSYS.emf_object_size(GXContext._get_tls_geo(), file.encode(), size_x.value, size_y.value)
        



    @classmethod
    def file_to_clipboard(cls, file):
        """
        Copy a text file onto the clipboard as text.
        """
        gxapi_cy.WrapSYS.file_to_clipboard(GXContext._get_tls_geo(), file.encode())
        



    @classmethod
    def font_lst(cls, lst, which):
        """
        List all Windows and geosoft fonts.

        **Note:**

        To get TT and GFN fonts, call twice with the same list
        and `SYS_FONT_TT <geosoft.gxapi.SYS_FONT_TT>`, then `SYS_FONT_GFN <geosoft.gxapi.SYS_FONT_GFN>`, or vice-versa to
        change order of listing.
        """
        gxapi_cy.WrapSYS.font_lst(GXContext._get_tls_geo(), lst._wrapper, which)
        



    @classmethod
    def get_dot_net_gx_entries(cls, gx, entry_buffer):
        """
        Get the list of entry points that this assembly has
        exposed to Oasis montaj.

        **Note:**

        The list of entry points are passed back as one
        string with each entry point separated by a semi-colon.
        For example: NewGDB|Run;NewGDB|RunEx
        """
        ret_val, entry_buffer.value = gxapi_cy.WrapSYS.get_dot_net_gx_entries(GXContext._get_tls_geo(), gx.encode(), entry_buffer.value.encode())
        return ret_val



    @classmethod
    def send_general_message(cls, cl, info):
        """
        Send a general information message to all listners
        """
        gxapi_cy.WrapSYS.send_general_message(GXContext._get_tls_geo(), cl.encode(), info.encode())
        



    @classmethod
    def write_debug_log(cls, log):
        """
        This method writes out information to the output
        debugging log file (in temp folder) or output window.
        """
        gxapi_cy.WrapSYS.write_debug_log(GXContext._get_tls_geo(), log.encode())
        



    @classmethod
    def log_script_run(cls, location):
        """
        This method logs that a script was run
        """
        gxapi_cy.WrapSYS.log_script_run(GXContext._get_tls_geo(), location.encode())
        




# Multithreading


    @classmethod
    def get_thread_id(cls):
        """
        Get the ID the current thread.

        **Note:**

        In a single threaded application this will always be 0.
        """
        ret_val = gxapi_cy.WrapSYS.get_thread_id(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def run_multi_user_script(cls, script, users, iterations, wait_min_time, wait_max_time, ramp_up_time):
        """
        Execute a script using multithreaded users

        **Note:**

        No access is provided in the script to EMAPS
        or EDBS. Users must ensure that the resources
        that are shared are protected.
        """
        gxapi_cy.WrapSYS.run_multi_user_script(GXContext._get_tls_geo(), script.encode(), users, iterations, wait_min_time, wait_max_time, ramp_up_time)
        




# Parameter


    @classmethod
    def clear_group(cls, group):
        """
        Clear current contents of a group
        """
        gxapi_cy.WrapSYS.clear_group(GXContext._get_tls_geo(), group.encode())
        



    @classmethod
    def clear_group_parm(cls, group):
        """
        Clears all paramters in a specified group.
        """
        gxapi_cy.WrapSYS.clear_group_parm(GXContext._get_tls_geo(), group.encode())
        



    @classmethod
    def clear_parm(cls):
        """
        Clears all paramters.
        """
        gxapi_cy.WrapSYS.clear_parm(GXContext._get_tls_geo())
        



    @classmethod
    def default_int(cls, group, field, val):
        """
        Allows a default int to be set.

        **Note:**

        The value will only be set if there is no existing
        setting.
        """
        gxapi_cy.WrapSYS.default_int(GXContext._get_tls_geo(), group.encode(), field.encode(), val)
        



    @classmethod
    def default_double(cls, group, field, val):
        """
        Allows a default real to be set.

        **Note:**

        The value will only be set if there is no existing
        setting.
        """
        gxapi_cy.WrapSYS.default_double(GXContext._get_tls_geo(), group.encode(), field.encode(), val)
        



    @classmethod
    def default_string(cls, group, field, val):
        """
        Allows a default string to be set.

        **Note:**

        The value will only be set if there is no existing
        setting.
        """
        gxapi_cy.WrapSYS.default_string(GXContext._get_tls_geo(), group.encode(), field.encode(), val.encode())
        



    @classmethod
    def get_pattern(cls, group, pat, size, thick, dense, col, back_col):
        """
        Gets pattern parameters from the parameter block.

        **Note:**

        Gets all the user-definable pattern parameters from
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
        pat.value, size.value, thick.value, dense.value, col.value, back_col.value = gxapi_cy.WrapSYS.get_pattern(GXContext._get_tls_geo(), group.encode(), pat.value, size.value, thick.value, dense.value, col.value, back_col.value)
        



    @classmethod
    def get_reg(cls, reg, group):
        """
        Get `GXREG <geosoft.gxapi.GXREG>` parameters.
        """
        gxapi_cy.WrapSYS.get_reg(GXContext._get_tls_geo(), reg._wrapper, group.encode())
        



    @classmethod
    def gt_string(cls, group, field, buff):
        """
        This method returns a string in the parameter block.

        **Note:**

        If the setting exits it is placed in the buffer, otherwise
        the buffer will have zero length
        """
        buff.value = gxapi_cy.WrapSYS.gt_string(GXContext._get_tls_geo(), group.encode(), field.encode(), buff.value.encode())
        



    @classmethod
    def exist_int(cls, group, field):
        """
        This method checks to see if a int parameter exists.
        """
        ret_val = gxapi_cy.WrapSYS.exist_int(GXContext._get_tls_geo(), group.encode(), field.encode())
        return ret_val



    @classmethod
    def exist_double(cls, group, field):
        """
        This method checks to see if a real parameter exists.
        """
        ret_val = gxapi_cy.WrapSYS.exist_double(GXContext._get_tls_geo(), group.encode(), field.encode())
        return ret_val



    @classmethod
    def exist_string(cls, group, field):
        """
        This method checks to see if a string parameter exists.
        """
        ret_val = gxapi_cy.WrapSYS.exist_string(GXContext._get_tls_geo(), group.encode(), field.encode())
        return ret_val



    @classmethod
    def get_int(cls, group, field):
        """
        This method returns an int from the parameter block.
        """
        ret_val = gxapi_cy.WrapSYS.get_int(GXContext._get_tls_geo(), group.encode(), field.encode())
        return ret_val



    @classmethod
    def get_yes_no(cls, group, field):
        """
        Check a YES/NO Setting
        """
        ret_val = gxapi_cy.WrapSYS.get_yes_no(GXContext._get_tls_geo(), group.encode(), field.encode())
        return ret_val



    @classmethod
    def replace_string(cls, str_val, output, group):
        """
        Replace "% %" tokens in a string with parameter values

        **Note:**

        If parameter does not exist, the token is removed.  Full parameter names,
        such as "%group.name%", are used as-is.  Partial parameter names, such as
        "%name%" will have the default group attached.
        """
        output.value = gxapi_cy.WrapSYS.replace_string(GXContext._get_tls_geo(), str_val.encode(), output.value.encode(), group.encode())
        



    @classmethod
    def load_parm(cls, file, groups):
        """
        Reads parameters from a file.
        """
        gxapi_cy.WrapSYS.load_parm(GXContext._get_tls_geo(), file.encode(), groups.encode())
        



    @classmethod
    def get_double(cls, group, field):
        """
        This method returns a real from the parameter block.
        """
        ret_val = gxapi_cy.WrapSYS.get_double(GXContext._get_tls_geo(), group.encode(), field.encode())
        return ret_val



    @classmethod
    def save_parm(cls, file, mode, groups):
        """
        Writes out one group (or all groups) to a file.
        """
        gxapi_cy.WrapSYS.save_parm(GXContext._get_tls_geo(), file.encode(), mode, groups.encode())
        



    @classmethod
    def filter_parm_group(cls, group, add):
        """
        Controls filtering of specific group during logging.

        **Note:**

        This is useful to prevent certain utility GX parameters from being recorded during GS script runs where the parameters does not influence the actual script execution.
        """
        gxapi_cy.WrapSYS.filter_parm_group(GXContext._get_tls_geo(), group.encode(), add)
        



    @classmethod
    def set_int(cls, group, field, val):
        """
        This method sets an int in the parameter block.
        """
        gxapi_cy.WrapSYS.set_int(GXContext._get_tls_geo(), group.encode(), field.encode(), val)
        



    @classmethod
    def set_pattern(cls, group, pat, size, thick, dense, col, back_col):
        """
        Sets pattern parameters in the parameter block.

        **Note:**

        Sets all the user-definable pattern parameters to
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
        gxapi_cy.WrapSYS.set_pattern(GXContext._get_tls_geo(), group.encode(), pat, size, thick, dense, col, back_col)
        



    @classmethod
    def set_double(cls, group, field, val):
        """
        This method Sets a real in the parameter block.
        """
        gxapi_cy.WrapSYS.set_double(GXContext._get_tls_geo(), group.encode(), field.encode(), val)
        



    @classmethod
    def set_reg(cls, reg):
        """
        Copy contents of a `GXREG <geosoft.gxapi.GXREG>` to current parameters.
        """
        gxapi_cy.WrapSYS.set_reg(GXContext._get_tls_geo(), reg._wrapper)
        



    @classmethod
    def set_string(cls, group, field, val):
        """
        This method sets a string in the parameter block.
        """
        gxapi_cy.WrapSYS.set_string(GXContext._get_tls_geo(), group.encode(), field.encode(), val.encode())
        




# Progress Control


    @classmethod
    def check_stop(cls):
        """
        This method is called at convenient points in the
        GX code to check if the user has asked the script
        to stop running. This method should be called by
        any GX program that may take a while to complete.
        """
        ret_val = gxapi_cy.WrapSYS.check_stop(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def prog_state(cls):
        """
        Return current progress state (On/Off)

        **Note:**

        This is useful, for instance, when calling one GX from another,
        especially if it is called multiple times in a loop.
        The called GX may turn the progress ON/OFF on its own, which
        means any progress tracking in the calling GX is disrupted.
        The called GX should use this function to determine the original
        progress state, and not turn off progress if it was already on.
        
        Returns				 0 - Progress is on
        - Progress is off
        """
        ret_val = gxapi_cy.WrapSYS.prog_state(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def prog_name(cls, name, reset):
        """
        This method allows you to name the current process being
        displayed by the progress bar. This method has no affect
        if no progress bar exists.
        """
        gxapi_cy.WrapSYS.prog_name(GXContext._get_tls_geo(), name.encode(), reset)
        



    @classmethod
    def progress(cls, on):
        """
        This method allows you to turn on the Progress BAR ON/OFF.
        Once the progress bar is on, use the UpdateProg method
        to drive it.
        """
        gxapi_cy.WrapSYS.progress(GXContext._get_tls_geo(), on)
        



    @classmethod
    def prog_update(cls, perc):
        """
        This method drives the Progress Bar. It is passed
        a percentage and will update the bar to reflect that
        percentage.
        """
        gxapi_cy.WrapSYS.prog_update(GXContext._get_tls_geo(), perc)
        



    @classmethod
    def prog_update_l(cls, v1, v2):
        """
        Updates progress bar based on count and maxcount.
        """
        gxapi_cy.WrapSYS.prog_update_l(GXContext._get_tls_geo(), v1, v2)
        




# Registry


    @classmethod
    def get_sys_info(cls, sys_info, info):
        """
        Get system information
        """
        info.value = gxapi_cy.WrapSYS.get_sys_info(GXContext._get_tls_geo(), sys_info, info.value.encode())
        



    @classmethod
    def registry_get_val(cls, domain, key, sub_key, value):
        """
        Get a registry value
        """
        ret_val, value.value = gxapi_cy.WrapSYS.registry_get_val(GXContext._get_tls_geo(), domain, key.encode(), sub_key.encode(), value.value.encode())
        return ret_val



    @classmethod
    def registry_delete_key(cls, domain, key):
        """
        Delete a registry value

        **Note:**

        All sub-keys and values will be deleted if they exist.
        """
        ret_val = gxapi_cy.WrapSYS.registry_delete_key(GXContext._get_tls_geo(), domain, key.encode())
        return ret_val



    @classmethod
    def registry_delete_val(cls, domain, key, value_name):
        """
        Delete a registry value
        """
        ret_val = gxapi_cy.WrapSYS.registry_delete_val(GXContext._get_tls_geo(), domain, key.encode(), value_name.encode())
        return ret_val



    @classmethod
    def registry_set_val(cls, domain, key, sub_key, value):
        """
        Set/create a registry value

        **Note:**

        This function will create the subkey and key if either do not
        already exist.
        """
        gxapi_cy.WrapSYS.registry_set_val(GXContext._get_tls_geo(), domain, key.encode(), sub_key.encode(), value.encode())
        




# Temporary File


    @classmethod
    def destroy_ptmp(cls, ptmp):
        """
        Destroy PTMP.
        """
        gxapi_cy.WrapSYS.destroy_ptmp(GXContext._get_tls_geo(), ptmp)
        



    @classmethod
    def get_ptmp(cls, ptmp):
        """
        Get temporary saves copy of parameter block.

        .. seealso::

            `save_ptmp <geosoft.gxapi.GXSYS.save_ptmp>`, `destroy_ptmp <geosoft.gxapi.GXSYS.destroy_ptmp>`
        """
        gxapi_cy.WrapSYS.get_ptmp(GXContext._get_tls_geo(), ptmp)
        



    @classmethod
    def save_ptmp(cls, groups):
        """
        Save a temporary copy of the parameter block.

        **Note:**

        All PTMP instances will be destroyed on exit.

        .. seealso::

            `get_ptmp <geosoft.gxapi.GXSYS.get_ptmp>`, `destroy_ptmp <geosoft.gxapi.GXSYS.destroy_ptmp>`
        """
        ret_val = gxapi_cy.WrapSYS.save_ptmp(GXContext._get_tls_geo(), groups.encode())
        return ret_val




# Termination


    @classmethod
    def abort(cls, message):
        """
        This method terminates the execution of a script. A message
        giving the reason for the abort will be displayed along with
        the line number where we stopped in the script.
        """
        gxapi_cy.WrapSYS.abort(GXContext._get_tls_geo(), message.encode())
        



    @classmethod
    def assert_(cls, exp):
        """
        Abort with GX line number if not true.
        """
        gxapi_cy.WrapSYS.assert_(GXContext._get_tls_geo(), exp)
        



    @classmethod
    def exit_(cls):
        """
        This method terminates the execution of a script in  a regular
        fashion with no error messages displayed.
        """
        gxapi_cy.WrapSYS.exit_(GXContext._get_tls_geo())
        



    @classmethod
    def cancel_(cls):
        """
        This method indicates that the GX program terminated without
        doing anything of interest and should be ignored.  In
        particular, the GX will not be logged in a recorded GS.
        """
        gxapi_cy.WrapSYS.cancel_(GXContext._get_tls_geo())
        




# Timing


    @classmethod
    def delay(cls, secs):
        """
        Idle delay method.
        """
        ret_val = gxapi_cy.WrapSYS.delay(GXContext._get_tls_geo(), secs)
        return ret_val



    @classmethod
    def get_timer(cls, flag, start_time, elapsed_time):
        """
        Return the elapsed time since the established time.

        **Note:**

        1st time through call the method with a flag of 1 to identify
        the count start time, subsequent times the time will be the time
        elapsed since the queried start time.  Do so by settign the flag to 0.
        """
        ret_val, start_time.value, elapsed_time.value = gxapi_cy.WrapSYS.get_timer(GXContext._get_tls_geo(), flag, start_time.value, elapsed_time.value)
        return ret_val




# User Interaction


    @classmethod
    def display_help(cls, group, topic):
        """
        Display the help dialog with the specified topic highlighted
        """
        gxapi_cy.WrapSYS.display_help(GXContext._get_tls_geo(), group.encode(), topic.encode())
        



    @classmethod
    def display_help_topic(cls, file, topic):
        """
        Display the help dialog without topic lookup in INI files
        """
        gxapi_cy.WrapSYS.display_help_topic(GXContext._get_tls_geo(), file.encode(), topic.encode())
        



    @classmethod
    def display_int(cls, title, int):
        """
        Display an integer.
        """
        gxapi_cy.WrapSYS.display_int(GXContext._get_tls_geo(), title.encode(), int)
        



    @classmethod
    def display_message(cls, title, message):
        """
        Display a user message.
        """
        gxapi_cy.WrapSYS.display_message(GXContext._get_tls_geo(), title.encode(), message.encode())
        



    @classmethod
    def display_double(cls, title, real):
        """
        Display a real number.
        """
        gxapi_cy.WrapSYS.display_double(GXContext._get_tls_geo(), title.encode(), real)
        



    @classmethod
    def display_question(cls, title, message):
        """
        Display a YES/NO type question. This method waits
        for the user to hit YES or NO.
        """
        ret_val = gxapi_cy.WrapSYS.display_question(GXContext._get_tls_geo(), title.encode(), message.encode())
        return ret_val



    @classmethod
    def display_question_with_cancel(cls, title, message):
        """
        Display a YES/NO/CANCEL type question. This method waits
        for the user to hit YES or NO or CANCEL.
        """
        ret_val = gxapi_cy.WrapSYS.display_question_with_cancel(GXContext._get_tls_geo(), title.encode(), message.encode())
        return ret_val



    @classmethod
    def display_task_dialog_ui(cls, title, main_instruction, content, common_buttons, custom_button_lst, icon, footer, footer_icon, verification_check_text, verification_checked, expanded_information, collapsed_control_text, expanded_control_text):
        """
        Show a Windows TaskDialog UI (see https://msdn.microsoft.com/en-us/library/windows/desktop/bb760441(v=vs.85).aspx).
        """
        ret_val, verification_checked.value = gxapi_cy.WrapSYS.display_task_dialog_ui(GXContext._get_tls_geo(), title.encode(), main_instruction.encode(), content.encode(), common_buttons, custom_button_lst._wrapper, icon, footer.encode(), footer_icon, verification_check_text.encode(), verification_checked.value, expanded_information.encode(), collapsed_control_text.encode(), expanded_control_text.encode())
        return ret_val



    @classmethod
    def interactive(cls):
        """
        Checks to see if you should run interactively.
        """
        ret_val = gxapi_cy.WrapSYS.interactive(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def prompt(cls, title, result):
        """
        Asks the User to enter a string.

        **Note:**

        The User string is displayed as the default value in the prompt.
        Empty the user string if no default is needed.
        """
        ret_val, result.value = gxapi_cy.WrapSYS.prompt(GXContext._get_tls_geo(), title.encode(), result.value.encode())
        return ret_val



    @classmethod
    def script(cls):
        """
        Checks to see if we are running inside OMS (script mode)
        """
        ret_val = gxapi_cy.WrapSYS.script(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def script_record(cls):
        """
        Checks to see if we are in scripting recording mode
        """
        ret_val = gxapi_cy.WrapSYS.script_record(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def set_cursor(cls, cursor):
        """
        Set the cursor on the display.

        **Note:**

        Possible Cursors:
        Normal, Horiz, Vert, Moving, Cross, Hand, NoEdit, Sun,
        View, Group, ViewSel, GroupSel, BoxSelect, Shadow, Link,
        Line, PolyLine, Polygon, Ellipse, Rectangle, Text, Symbol,
        Zoom, Pan, Rotate, InteractiveZoom, PolyFill, GetFill,
        SnapPoint, SnapLine, SnapOnPoint, SnapOnLine, NPolygon,
        ExcludeRect, ExcludePoly, ExcludeNPoly, AddVertex, DelVertex, GeneralAdd and GeneralDelete
        """
        gxapi_cy.WrapSYS.set_cursor(GXContext._get_tls_geo(), cursor.encode())
        



    @classmethod
    def set_info_line(cls, message):
        """
        Display a message on the information line at the left
        bottom corner of the OAISIS montaj application.
        """
        gxapi_cy.WrapSYS.set_info_line(GXContext._get_tls_geo(), message.encode())
        



    @classmethod
    def set_interactive(cls, mode):
        """
        Sets the interactive mode.

        **Note:**

        Call to `interactive <geosoft.gxapi.GXSYS.interactive>` will return the value
        set here.

        .. seealso::

            `interactive <geosoft.gxapi.GXSYS.interactive>`, `run_gx <geosoft.gxapi.GXSYS.run_gx>` and `run_gs <geosoft.gxapi.GXSYS.run_gs>`
        """
        gxapi_cy.WrapSYS.set_interactive(GXContext._get_tls_geo(), mode)
        




# Workspace


    @classmethod
    def get_workspace_reg(cls, reg):
        """
        Get a copy of the workspace `GXREG <geosoft.gxapi.GXREG>`;

        **Note:**

        The workspace `GXREG <geosoft.gxapi.GXREG>` is separate from the reg used
        to store `GXSYS <geosoft.gxapi.GXSYS>` parameters.
        
        Because `get_workspace_reg <geosoft.gxapi.GXSYS.get_workspace_reg>` returns a copy of the
        workspace `GXREG <geosoft.gxapi.GXREG>`, and not the workspace `GXREG <geosoft.gxapi.GXREG>` itself,
        you must call `set_workspace_reg <geosoft.gxapi.GXSYS.set_workspace_reg>` if you make changes
        to your own `GXREG <geosoft.gxapi.GXREG>` object and you wish them to take
        effect in the workspace `GXREG <geosoft.gxapi.GXREG>`.
        """
        gxapi_cy.WrapSYS.get_workspace_reg(GXContext._get_tls_geo(), reg._wrapper)
        



    @classmethod
    def set_workspace_reg(cls, reg):
        """
        Set the workspace `GXREG <geosoft.gxapi.GXREG>`;

        **Note:**

        The workspace `GXREG <geosoft.gxapi.GXREG>` is separate from the reg used
        to store `GXSYS <geosoft.gxapi.GXSYS>` parameters.
        
        Because `get_workspace_reg <geosoft.gxapi.GXSYS.get_workspace_reg>` returns a copy of the
        workspace `GXREG <geosoft.gxapi.GXREG>`, and not the workspace `GXREG <geosoft.gxapi.GXREG>` itself,
        you must call `set_workspace_reg <geosoft.gxapi.GXSYS.set_workspace_reg>` if you make changes
        to your own `GXREG <geosoft.gxapi.GXREG>` object and you wish them to take
        effect in the workspace `GXREG <geosoft.gxapi.GXREG>`
        """
        gxapi_cy.WrapSYS.set_workspace_reg(GXContext._get_tls_geo(), reg._wrapper)
        




# String Encryption


    @classmethod
    def encrypt_string(cls, input, output, key):
        """
        Encrypts a string for secure storage in configuration files
        or in the workspace parameters.
        """
        output.value = gxapi_cy.WrapSYS.encrypt_string(GXContext._get_tls_geo(), input.encode(), output.value.encode(), key)
        



    @classmethod
    def decrypt_string(cls, input, output, key):
        """
        Decrypts a string that has been previously encrypted by `encrypt_string <geosoft.gxapi.GXSYS.encrypt_string>`.
        """
        output.value = gxapi_cy.WrapSYS.decrypt_string(GXContext._get_tls_geo(), input.encode(), output.value.encode(), key)
        



    @classmethod
    def is_encrypted_string(cls, input):
        """
        Checks whether the specified string was encrypted by `encrypt_string <geosoft.gxapi.GXSYS.encrypt_string>`.
        """
        ret_val = gxapi_cy.WrapSYS.is_encrypted_string(GXContext._get_tls_geo(), input.encode())
        return ret_val




# GX Debugger


    @classmethod
    def disable_gx_debugger(cls):
        """
        Disable GX Debugger `GXGUI <geosoft.gxapi.GXGUI>` if active

        **Note:**

        All breakpoints will be cleared by this call.
        """
        gxapi_cy.WrapSYS.disable_gx_debugger(GXContext._get_tls_geo())
        



    @classmethod
    def enable_gx_debugger(cls, src_dir, first_gx):
        """
        Enable GX Debugger `GXGUI <geosoft.gxapi.GXGUI>`

        **Note:**

        Takes as input two strings one a path that will be scanned
        recursively for GXC source files and a second string without
        a path of the GX where the first breakpoint should be set in (i.e. "gxname.gx").
        The source of the GX should be found in the path (e.g. <path>\\somewhere\\gxname.gxc)
        and a breakpoint will be set on the first executing line of this GX. Make sure the
        GX binary is newer than the source file, otherwise unexpected results may occur. As
        soon as the GX is run the `GXGUI <geosoft.gxapi.GXGUI>` will become visible and it will be possible to set more
        breakpoints in any of the GXC files found in the path.
        """
        gxapi_cy.WrapSYS.enable_gx_debugger(GXContext._get_tls_geo(), src_dir.encode(), first_gx.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer