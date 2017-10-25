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

    The `GXSYS` library functions perform a wide range functions,
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
    
    If the index is a '*' in "`set_string`", then the value string
    will be parsed into multiple values. Commas are assumed to be delimiters.
    
    E.g.
    
    `set_string`("group1",
    "multiparm[*]",
    "value1,\\"value,2\\",\\"value 3\\",  value4  ,\\"value 5 \\"");
    
    This call will set   multiparm[0] ="value1"
    multiparm[1] ="value,2"
    multiparm[2] ="value 3"
    multiparm[3] ="value4"
    multiparm[4] ="value 5"
    
    To read a parameter, name the parameter with the index.  Thre is no
    looped-reading ability.  For example:
    
    GetString_SYS("group1","multiparm[3]",sSetting);
    
    returns sSetting = "value4"
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
    def break_date(cls, p1, p2, p3, p4):
        """
        Breaks a decimal date value into year, month and day.
        """
        p2.value, p3.value, p4.value = gxapi_cy.WrapSYS.break_date(GXContext._get_tls_geo(), p1, p2.value, p3.value, p4.value)
        



    @classmethod
    def dateto_long(cls, p1):
        """
        Converts a double date to a value representing total
        days elapsed since day 0 of year 0. This uses the
        Numerical Receipies Julian function.
        """
        ret_val = gxapi_cy.WrapSYS.dateto_long(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def timeto_long(cls, p1):
        """
        Converts decimal hours to seconds in a day.
        """
        ret_val = gxapi_cy.WrapSYS.timeto_long(GXContext._get_tls_geo(), p1)
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
    def longto_date(cls, p1):
        """
        Converts a value representing total days elapsed since
        day 0 of year 0 to a geosoft date. This uses the
        Numerical Receipies Julian function.
        """
        ret_val = gxapi_cy.WrapSYS.longto_date(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def longto_time(cls, p1):
        """
        Converts seconds to decimal hours.
        """
        ret_val = gxapi_cy.WrapSYS.longto_time(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def make_date(cls, p1, p2, p3):
        """
        Returns the decimal date given the year, month and day.
        """
        ret_val = gxapi_cy.WrapSYS.make_date(GXContext._get_tls_geo(), p1, p2, p3)
        return ret_val



    @classmethod
    def secondsto_time(cls, p1):
        """
        Converts fractional seconds to decimal hours.
        """
        ret_val = gxapi_cy.WrapSYS.secondsto_time(GXContext._get_tls_geo(), p1)
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
    def timeto_seconds(cls, p1):
        """
        Converts decimal hours to seconds in a day fractional
        """
        ret_val = gxapi_cy.WrapSYS.timeto_seconds(GXContext._get_tls_geo(), p1)
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
    def exist_env(cls, p1):
        """
        Check if setting exists in environment.
        """
        ret_val = gxapi_cy.WrapSYS.exist_env(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def get_env(cls, p1, p2):
        """
        Get an environment setting.
        """
        p2.value = gxapi_cy.WrapSYS.get_env(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def set_env(cls, p1, p2):
        """
        Set an environment setting.
        """
        gxapi_cy.WrapSYS.set_env(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        




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
    def get_error_message_ap(cls, p1, p2):
        """
        Return the error message text as a string.

        **Note:**

        This wrapper is mostly for use outside of GXs,
        because in general if an error is registered in a GX
        the GX would terminate before it could be called.
        Use `num_errors_ap` to get the number of registered errors.
        """
        p2.value = gxapi_cy.WrapSYS.get_error_message_ap(GXContext._get_tls_geo(), p1, p2.value.encode())
        



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
    def set_server_messages_ap(cls, p1):
        """
        Control the server message handling.

        **Note:**

        Should be set to false when dialogs should not
        appear. This setting is thread specific.
        """
        gxapi_cy.WrapSYS.set_server_messages_ap(GXContext._get_tls_geo(), p1)
        




# Execution


    @classmethod
    def run(cls, p1, p2, p3):
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
        ret_val = gxapi_cy.WrapSYS.run(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        return ret_val



    @classmethod
    def run_gs(cls, p1):
        """
        Run a GS.

        .. seealso::

            `set_interactive`, `run_gx`
        """
        ret_val = gxapi_cy.WrapSYS.run_gs(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def run_gx(cls, p1):
        """
        Run a GX.

        **Note:**

        If the called GX returns an error, they will not be
        displayed until the "top" calling GX terminates, unless you
        call `show_error`().

        .. seealso::

            `run_gx_ex`, `set_interactive` and `run_gs`
        """
        ret_val = gxapi_cy.WrapSYS.run_gx(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def run_gx_ex(cls, p1, p2):
        """
        Run a GX.

        .. seealso::

            `run_gx`, `set_return`
        """
        ret_val, p2.value = gxapi_cy.WrapSYS.run_gx_ex(GXContext._get_tls_geo(), p1.encode(), p2.value)
        return ret_val



    @classmethod
    def run_pdf(cls, p1, p2):
        """
        Run a PDF.

        **Note:**

        The group name of the PDF variables will be "group_pdf",
        where "group" is the name given in the first argument,
        and "pdf" is the root PDF file name.
        """
        ret_val = gxapi_cy.WrapSYS.run_pdf(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def shell_execute(cls, p1, p2, p3, p4, p5):
        """
        MS ShellExecute function

        **Note:**

        Examples
        
        `shell_execute`(open;http://www.geosoft.com);
        `shell_execute`(open;"mailto:geonet@lists.geosoft.com");
        `shell_execute`(open;"mailto:majordomo@lists.geosoft.com?body=UNSUBSCRIBE%20gxnet");

        .. seealso::

            `do_command`
        """
        ret_val = gxapi_cy.WrapSYS.shell_execute(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4.encode(), p5)
        return ret_val



    @classmethod
    def set_return(cls, p1):
        """
        Set the return value of a GX.

        **Note:**

        This value is returned in the `run_gx_ex` call only.
        """
        gxapi_cy.WrapSYS.set_return(GXContext._get_tls_geo(), p1)
        




# External DLL


    @classmethod
    def do_command(cls, p1):
        """
        Execute an Oasis montaj command.

        **Note:**

        Commands syntax:  "[type] command"
        
        type     command
        ----     -------
        ID       Internal Menu Command
        See "Internal Menu Commands" in GX Developer documentation.
        GX       gx file name
        GS       gs file name
        DOTNET   dll file name
        Use qualifiers to specify class and method e.g. [DOTNET] geogxnet.dll(Geosoft.GX.NewGDB.NewGDB;Run)
        PDF      pdf file name
        DOS      DOS style command
        HLP      help file name
        
        The must be ONE space between the "]" and the command.  For example:
        
        `do_command`("[ID] ID_EDIT_SELECT");  // bring up the line edit tool

        .. seealso::

            ShellExecute_SYS
        """
        gxapi_cy.WrapSYS.do_command(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def error(cls, p1, p2, p3):
        """
        Register an error message

        **Note:**

        Use this function to register your own error
        messages when an error occurs in your code.  Your
        errors can be provided in your own `GXGER` file.  See
        GEOSOFT.`GXGER` for an example of the `GXGER` file format.
        
        If the error # is not found in your error file, the
        OE32.`GXGER` file, then the GEOSOFT.`GXGER` file will be
        searched.
        """
        gxapi_cy.WrapSYS.error(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        



    @classmethod
    def error_tag(cls, p1, p2):
        """
        Set an error message tag string

        **Note:**

        Use this method to replace tag strings in your error
        message text with run-time information.  For example,
        Geosoft error messages often use the tag strings "%1",
        "%2", etc. as place holders to be replaced by a string
        which is only known at run-time.
        """
        gxapi_cy.WrapSYS.error_tag(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def assert_gx(cls, p1, p2, p3):
        """
        DLL function argument error assertion

        **Note:**

        Use this function to evaluate errors in passed
        function arguments.  Functions called by GX programs
        should be tolerant of all errors in the passed argument
        list.  The `assert_gx` can be used to test each
        argument before doing any work in the function.  If
        an assertion fails, an error will be registered with
        the name of the function and the parameter name and
        a 1 will be returned.  The caller should immediatley
        cleaning up (if necessary) and return.
        
        You could also test the validity of arguments and call
        the `error`, `error_tag` and `terminate`
        functions if you would like to provide a more specific
        error message.
        """
        ret_val = gxapi_cy.WrapSYS.assert_gx(GXContext._get_tls_geo(), p1, p2.encode(), p3.encode())
        return ret_val



    @classmethod
    def ole_automation(cls, p1, p2, p3):
        """
        Call OLE Automation designed to be called from Montaj.
        """
        ret_val = gxapi_cy.WrapSYS.ole_automation(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        return ret_val



    @classmethod
    def save_log(cls, p1):
        """
        Saves the main log file to another file.
        """
        gxapi_cy.WrapSYS.save_log(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def show_error(cls):
        """
        Display any errors to the user.

        **Note:**

        If you call a GX from another GX using `run_gx`, and
        the called GX registers errors, they will not be displayed
        until after the "top" GX exits.
        If you wish to continue without exiting, call this function
        so that errors are displayed immediately to the user. For
        instance, when creating a new map from inside another GX:
        
        --- Run NEWMAP wizard. Keep trying if something is wrong (like a
        too-small map scale), but exit if the user cancels (iRet==-1) ---
        
        do {
        iRet = `run_gx`("newmap.gx");
        if(iRet==1) `show_error`();     // Dump errors.
        } while(iRet==1);
        
        This wrapper is not intended for use outside a GX, because it
        uses the GX run-time machinery to display the error messages.
        """
        gxapi_cy.WrapSYS.show_error(GXContext._get_tls_geo())
        



    @classmethod
    def terminate(cls, p1):
        """
        DLL error termination

        **Note:**

        Call this function immediately before returning to
        the caller after an error has occured inside the
        DLL.  If an error has occured, you should clean-up
        (free memory, close files), call `error` to register
        your own error messages, call `error_tag` to set any
        error message tags, call `terminate` and return.
        
        Geosoft functions that detect an error will have
        already registered their own errors and called
        `terminate`.
        """
        gxapi_cy.WrapSYS.terminate(GXContext._get_tls_geo(), p1.encode())
        




# File System


    @classmethod
    def crc_file(cls, p1):
        """
        Compute the CRC of a file
        """
        ret_val = gxapi_cy.WrapSYS.crc_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def crc_file_offset(cls, p1, p2):
        """
        Compute the CRC of a file with an Offset
        """
        ret_val = gxapi_cy.WrapSYS.crc_file_offset(GXContext._get_tls_geo(), p1.encode(), p2)
        return ret_val



    @classmethod
    def file_ren(cls, p1, p2):
        """
        Rename a file
        """
        gxapi_cy.WrapSYS.file_ren(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def find_files_vv(cls, p1, p2):
        """
        Fill a `GXVV` with files matching an input file mask.

        **Note:**

        Fill a `GXVV` with files matching the input file mask.
        The `GXVV` should be of string type.
        """
        gxapi_cy.WrapSYS.find_files_vv(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def absolute_file_name(cls, p1, p2):
        """
        Convert an abbreviated path name to a full path name.

        **Note:**

        This is mainly intended to convert ".\\name" to a full
        name at run-time.
        """
        p2.value = gxapi_cy.WrapSYS.absolute_file_name(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def copy_file(cls, p1, p2):
        """
        Copy a file.
        """
        ret_val = gxapi_cy.WrapSYS.copy_file(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def delete_file(cls, p1):
        """
        Delete a file.
        """
        ret_val = gxapi_cy.WrapSYS.delete_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def delete_gi_file(cls, p1):
        """
        Delete the GI file associated with a grid.
        """
        ret_val = gxapi_cy.WrapSYS.delete_gi_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def delete_grid_file(cls, p1):
        """
        Delete a grid file and its associated GI and XML files.

        **Note:**

        Deletes the grid file first, and, if they exist, the associated GI
        and XML files.
        No error is registered if a file is not found or cannot be deleted.
        """
        ret_val = gxapi_cy.WrapSYS.delete_grid_file(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def dir_exist(cls, p1):
        """
        Check to see if a directory exists
        """
        ret_val = gxapi_cy.WrapSYS.dir_exist(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def file_exist(cls, p1):
        """
        Check to see if a file exists

        **Note:**

        Use the FULL path for the file name. If the full
        path is not specified, then the current working
        directory is used for the path.
        """
        ret_val = gxapi_cy.WrapSYS.file_exist(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def file_size(cls, p1):
        """
        Returns size of a file.
        """
        ret_val = gxapi_cy.WrapSYS.file_size(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def file_writable(cls, p1):
        """
        Check if a file can be created or opened in read-write mode
        at a specific location
        """
        ret_val = gxapi_cy.WrapSYS.file_writable(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def find_path(cls, p1, p2, p3):
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
        ret_val, p3.value = gxapi_cy.WrapSYS.find_path(GXContext._get_tls_geo(), p1.encode(), p2, p3.value.encode())
        return ret_val



    @classmethod
    def find_path_ex(cls, p1, p2, p3, p4):
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
        ret_val, p4.value = gxapi_cy.WrapSYS.find_path_ex(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4.value.encode())
        return ret_val



    @classmethod
    def get_directory(cls, p1, p2):
        """
        Get a directory path

        **Note:**

        The path will always end with the file separator character
        """
        p2.value = gxapi_cy.WrapSYS.get_directory(GXContext._get_tls_geo(), p1, p2.value.encode())
        



    @classmethod
    def get_path(cls, p1, p2):
        """
        Get a Geosoft path

        **Note:**

        The path name will have a directory separator at the end.
        """
        p2.value = gxapi_cy.WrapSYS.get_path(GXContext._get_tls_geo(), p1, p2.value.encode())
        



    @classmethod
    def get_windows_dir(cls, p1):
        """
        Get the Windows directory path
        """
        p1.value = gxapi_cy.WrapSYS.get_windows_dir(GXContext._get_tls_geo(), p1.value.encode())
        



    @classmethod
    def make_dir(cls, p1):
        """
        Create a directory.
        """
        ret_val = gxapi_cy.WrapSYS.make_dir(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def make_file_readonly(cls, p1):
        """
        Set a file's read-only attribute.
        """
        ret_val = gxapi_cy.WrapSYS.make_file_readonly(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def make_file_writable(cls, p1):
        """
        Removes a file's read-only attribute.
        """
        ret_val = gxapi_cy.WrapSYS.make_file_writable(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def relative_file_name(cls, p1, p2):
        """
        Convert a file name to a relative abbreviated path name

        **Note:**

        This will produce relative paths based on the workspace
        directory into ".\\name".
        """
        p2.value = gxapi_cy.WrapSYS.relative_file_name(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def short_path_file_name(cls, p1, p2):
        """
        Obtains the short path form of a specified input path.
        """
        p2.value = gxapi_cy.WrapSYS.short_path_file_name(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def temp_file_ext(cls, p1, p2):
        """
        Generate a unique file name for this extension in the temp directory.

        **Note:**

        This is useful for created a unique tempory name for a file in the Geosoft temporary directory.
        """
        p2.value = gxapi_cy.WrapSYS.temp_file_ext(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def temp_file_name(cls, p1, p2):
        """
        Generate a file name for this file in the temp directory.

        **Note:**

        This is useful for created a unique tempory name for a file in the Geosoft temporary directory.
        
        From version 7.0 The file extension will match the input file, but the
        filename itself will be a process and thread unique value to ensure that
        clashes does not happen.
        """
        p2.value = gxapi_cy.WrapSYS.temp_file_name(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def transfer_path(cls, p1, p2):
        """
        Transfers file path to new file name.

        **Note:**

        The path and volume of from the input string is added to
        file name from the output string.
        """
        p2.value = gxapi_cy.WrapSYS.transfer_path(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def valid_file_name(cls, p1):
        """
        Check to see if a file name valid

        **Note:**

        Use the FULL path for the file name. If the full
        path is not specified, then the current working
        directory is used for the path.
        """
        ret_val = gxapi_cy.WrapSYS.valid_file_name(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def write_in_dir(cls, p1):
        """
        Can I create files in this directory ?
        """
        ret_val = gxapi_cy.WrapSYS.write_in_dir(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def file_date(cls, p1):
        """
        File creation date in decimal years.

        **Note:**

        The FormatDate_STR function can be used to convert a date
        to a string.
        """
        ret_val = gxapi_cy.WrapSYS.file_date(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def file_time(cls, p1):
        """
        File creation time in decimal hours.

        **Note:**

        The FormatTime_STR function can be used to convert a time
        to a string.
        """
        ret_val = gxapi_cy.WrapSYS.file_time(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def utc_file_date(cls, p1):
        """
        File creation UTC date in decimal years.

        **Note:**

        The FormatDate_STR function can be used to convert a date
        to a string.
        """
        ret_val = gxapi_cy.WrapSYS.utc_file_date(GXContext._get_tls_geo(), p1.encode())
        return ret_val



    @classmethod
    def utc_file_time(cls, p1):
        """
        File creation UTC time in decimal hours.

        **Note:**

        The FormatTime_STR function can be used to convert a time
        to a string.
        """
        ret_val = gxapi_cy.WrapSYS.utc_file_time(GXContext._get_tls_geo(), p1.encode())
        return ret_val




# Global Parameter


    @classmethod
    def get_settings_meta(cls, p1):
        """
        Get the settings metadata object.
        """
        gxapi_cy.WrapSYS.get_settings_meta(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def global_reset(cls, p1):
        """
        Reset the global parameters.
        """
        gxapi_cy.WrapSYS.global_reset(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def global_set(cls, p1, p2):
        """
        Set a global parameter setting.
        """
        gxapi_cy.WrapSYS.global_set(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def global_write(cls, p1):
        """
        Modify the global parameters.

        **Note:**

        If the global parameters have been changed, use
        this function to make the changes permanent,
        """
        gxapi_cy.WrapSYS.global_write(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def global_(cls, p1, p2):
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
        ret_val, p2.value = gxapi_cy.WrapSYS.global_(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        return ret_val



    @classmethod
    def reset_settings(cls):
        """
        Resets the GX_HELP settings in the geosoft.ini file
        after changes have been made.
        """
        gxapi_cy.WrapSYS.reset_settings(GXContext._get_tls_geo())
        



    @classmethod
    def set_settings_meta(cls, p1):
        """
        Set the settings metadata object.
        """
        gxapi_cy.WrapSYS.set_settings_meta(GXContext._get_tls_geo(), p1._wrapper)
        




# Licensing


    @classmethod
    def check_arc_license(cls):
        """
        Check to see if a ESRI ArcEngine or ArcView license is available
        """
        ret_val = gxapi_cy.WrapSYS.check_arc_license(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def check_arc_license_ex(cls, p1):
        """
        Check to see if a ESRI ArcEngine or ArcView license is available, returns type and version of available engine.
        """
        ret_val, p1.value = gxapi_cy.WrapSYS.check_arc_license_ex(GXContext._get_tls_geo(), p1.value.encode())
        return ret_val



    @classmethod
    def check_intrinsic(cls, p1, p2):
        """
        Check to see if an intrinsic object is licensed
        """
        ret_val = gxapi_cy.WrapSYS.check_intrinsic(GXContext._get_tls_geo(), p1, p2.encode())
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
    def get_license_class(cls, p1):
        """
        Get the current application license class.

        **Note:**

        String may be one of :  "ArcGIS"
        "OasisMontaj"
        "DapServer"
        """
        p1.value = gxapi_cy.WrapSYS.get_license_class(GXContext._get_tls_geo(), p1.value.encode())
        



    @classmethod
    def get_licensed_user(cls, p1, p3):
        """
        Get the licensed user name and Company
        """
        p1.value, p3.value = gxapi_cy.WrapSYS.get_licensed_user(GXContext._get_tls_geo(), p1.value.encode(), p3.value.encode())
        




# Lineage


    @classmethod
    def add_lineage_parameter(cls, p1, p2):
        """
        Add a parameter to the current lineage object
        """
        gxapi_cy.WrapSYS.add_lineage_parameter(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def add_lineage_source(cls, p1, p2):
        """
        Add a source to the current lineage object
        """
        gxapi_cy.WrapSYS.add_lineage_source(GXContext._get_tls_geo(), p1, p2.encode())
        



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
    def copy_geo_file(cls, p1, p2):
        """
        Copy a Geosoft data file and all associated files to a new folder

        **Note:**

        Grids are copied and the GI's are maintained - note that support
        for non-geosoft grids is limited since this method does not
        guarantee all grid files besides the main one are copied.
        """
        gxapi_cy.WrapSYS.copy_geo_file(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def backup_geo_file(cls, p1, p2):
        """
        Backup a Geosoft data file and all associated files to a temporary folder.

        **Note:**

        Grids are copied and the GI's are maintained - note that support
        for non-geosoft grids is limited since this method does not
        guarantee all grid files besides the main one are copied.
        """
        p2.value = gxapi_cy.WrapSYS.backup_geo_file(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        



    @classmethod
    def remove_lineage_output(cls, p1):
        """
        Remove an output from the current lineage object
        """
        gxapi_cy.WrapSYS.remove_lineage_output(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def remove_lineage_parameter(cls, p1):
        """
        Remove a parameter in the current lineage object
        """
        gxapi_cy.WrapSYS.remove_lineage_parameter(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def remove_lineage_source(cls, p1):
        """
        Remove a source from the current lineage object
        """
        gxapi_cy.WrapSYS.remove_lineage_source(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def restore_geo_file(cls, p1, p2):
        """
        Backup a Geosoft data file and all associated files to original location

        **Note:**

        Grids are copied and the GI's are maintained - note that support
        for non-geosoft grids is limited since this method does not
        guarantee all grid files besides the main one are copied.
        """
        gxapi_cy.WrapSYS.restore_geo_file(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def set_lineage_description(cls, p1):
        """
        Set the description for the current lineage object
        """
        gxapi_cy.WrapSYS.set_lineage_description(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def set_lineage_display_name(cls, p1):
        """
        Set the display name for the current lineage object
        """
        gxapi_cy.WrapSYS.set_lineage_display_name(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def set_lineage_name(cls, p1):
        """
        Set the name for the current lineage object
        """
        gxapi_cy.WrapSYS.set_lineage_name(GXContext._get_tls_geo(), p1.encode())
        




# Menus and Toolbar


    @classmethod
    def clear_menus(cls, p1):
        """
        Clear all menus
        """
        gxapi_cy.WrapSYS.clear_menus(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def get_loaded_menus(cls, p1, p2, p3):
        """
        Get the loaded menus.

        **Note:**

        The names of the LSTs contain the menus and the values contain any exclusions. Exlusions 
        are semicolon separated top level menu names and/or toolbar.geobar file names.
        """
        gxapi_cy.WrapSYS.get_loaded_menus(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def set_loaded_menus(cls, p1, p2, p3):
        """
        Load a list of menus

        **Note:**

        The names of the LSTs contain the menus and the values contain any exclusions. Exlusions 
        are semicolon separated top level menu names and/or toolbar.geobar file names.
        """
        gxapi_cy.WrapSYS.set_loaded_menus(GXContext._get_tls_geo(), p1._wrapper, p2._wrapper, p3._wrapper)
        



    @classmethod
    def get_entitlement_rights(cls, p1):
        """
        Get the Entitlement Rights
        """
        gxapi_cy.WrapSYS.get_entitlement_rights(GXContext._get_tls_geo(), p1._wrapper)
        




# Misc


    @classmethod
    def generate_guid(cls, p1):
        """
        Genrates a GUID string (e.g. {4FEDE8BF-CDAB-430A-8026-1CCC0EC0A2EB})
        """
        p1.value = gxapi_cy.WrapSYS.generate_guid(GXContext._get_tls_geo(), p1.value.encode())
        



    @classmethod
    def clipboard_to_file(cls, p1):
        """
        Copy text from the clipboard to a file.
        """
        gxapi_cy.WrapSYS.clipboard_to_file(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def create_clipboard_ra(cls):
        """
        Create a `GXRA` to read text from the clipboard.

        **Note:**

        Destroy the `GXRA` as soon as possible. As long as it
        open the clipboard is not accessible from any
        application.
        """
        ret_val = gxapi_cy.WrapSYS.create_clipboard_ra(GXContext._get_tls_geo())
        return GXRA(ret_val)



    @classmethod
    def create_clipboard_wa(cls):
        """
        Create a `GXWA` to write text on the clipboard.

        **Note:**

        Destroy the `GXWA` as soon as possible. As long as it
        open the clipboard is not accessible from any
        application.
        """
        ret_val = gxapi_cy.WrapSYS.create_clipboard_wa(GXContext._get_tls_geo())
        return GXWA(ret_val)



    @classmethod
    def emf_object_size(cls, p1, p2, p3):
        """
        Get the size of an EMF object
        """
        p2.value, p3.value = gxapi_cy.WrapSYS.emf_object_size(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value)
        



    @classmethod
    def file_to_clipboard(cls, p1):
        """
        Copy a text file onto the clipboard as text.
        """
        gxapi_cy.WrapSYS.file_to_clipboard(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def font_lst(cls, p1, p2):
        """
        List all Windows and geosoft fonts.

        **Note:**

        To get TT and GFN fonts, call twice with the same list
        and `SYS_FONT_TT`, then `SYS_FONT_GFN`, or vice-versa to
        change order of listing.
        """
        gxapi_cy.WrapSYS.font_lst(GXContext._get_tls_geo(), p1._wrapper, p2)
        



    @classmethod
    def get_dot_net_gx_entries(cls, p1, p2):
        """
        Get the list of entry points that this assembly has
        exposed to Oasis montaj.

        **Note:**

        The list of entry points are passed back as one
        string with each entry point separated by a semi-colon.
        For example: NewGDB|Run;NewGDB|RunEx
        """
        ret_val, p2.value = gxapi_cy.WrapSYS.get_dot_net_gx_entries(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
        return ret_val



    @classmethod
    def send_general_message(cls, p1, p2):
        """
        Send a general information message to all listners
        """
        gxapi_cy.WrapSYS.send_general_message(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def write_debug_log(cls, p1):
        """
        This method writes out information to the output
        debugging log file (in temp folder) or output window.
        """
        gxapi_cy.WrapSYS.write_debug_log(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def log_script_run(cls, p1):
        """
        This method logs that a script was run
        """
        gxapi_cy.WrapSYS.log_script_run(GXContext._get_tls_geo(), p1.encode())
        




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
    def run_multi_user_script(cls, p1, p2, p3, p4, p5, p6):
        """
        Execute a script using multithreaded users

        **Note:**

        No access is provided in the script to EMAPS
        or EDBS. Users must ensure that the resources
        that are shared are protected.
        """
        gxapi_cy.WrapSYS.run_multi_user_script(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6)
        




# Parameter


    @classmethod
    def clear_group(cls, p1):
        """
        Clear current contents of a group
        """
        gxapi_cy.WrapSYS.clear_group(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def clear_group_parm(cls, p1):
        """
        Clears all paramters in a specified group.
        """
        gxapi_cy.WrapSYS.clear_group_parm(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def clear_parm(cls):
        """
        Clears all paramters.
        """
        gxapi_cy.WrapSYS.clear_parm(GXContext._get_tls_geo())
        



    @classmethod
    def default_int(cls, p1, p2, p3):
        """
        Allows a default int to be set.

        **Note:**

        The value will only be set if there is no existing
        setting.
        """
        gxapi_cy.WrapSYS.default_int(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        



    @classmethod
    def default_double(cls, p1, p2, p3):
        """
        Allows a default real to be set.

        **Note:**

        The value will only be set if there is no existing
        setting.
        """
        gxapi_cy.WrapSYS.default_double(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        



    @classmethod
    def default_string(cls, p1, p2, p3):
        """
        Allows a default string to be set.

        **Note:**

        The value will only be set if there is no existing
        setting.
        """
        gxapi_cy.WrapSYS.default_string(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        



    @classmethod
    def get_pattern(cls, p1, p2, p3, p4, p5, p6, p7):
        """
        Gets pattern parameters from the parameter block.

        **Note:**

        Gets all the user-definable pattern parameters from
        a specified group. Parameters are:
        "PAT_NUMBER"    0 is solid fill (default)
        "PAT_SIZE"      pattern tile size in mm. (can return `iDUMMY`)
        "PAT_THICKNESS" pattern line thickness in percent of the tile size.
        valid range is 0-100.
        "PAT_DENSITY"   Tile spacing. A value of 1 means tiles are laid with no overlap.
        A value of 2 means they overlap each other.
        "PAT_COLOR"     The color value.
        "PAT_BACKCOLOR" Background color value.
        
        Returned values may be DUMMY, but will be acceptable for use with
        the `GXGUI.color_form` function, to set defaults.
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = gxapi_cy.WrapSYS.get_pattern(GXContext._get_tls_geo(), p1.encode(), p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        



    @classmethod
    def get_reg(cls, p1, p2):
        """
        Get `GXREG` parameters.
        """
        gxapi_cy.WrapSYS.get_reg(GXContext._get_tls_geo(), p1._wrapper, p2.encode())
        



    @classmethod
    def gt_string(cls, p1, p2, p3):
        """
        This method returns a string in the parameter block.

        **Note:**

        If the setting exits it is placed in the buffer, otherwise
        the buffer will have zero length
        """
        p3.value = gxapi_cy.WrapSYS.gt_string(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.value.encode())
        



    @classmethod
    def exist_int(cls, p1, p2):
        """
        This method checks to see if a int parameter exists.
        """
        ret_val = gxapi_cy.WrapSYS.exist_int(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def exist_double(cls, p1, p2):
        """
        This method checks to see if a real parameter exists.
        """
        ret_val = gxapi_cy.WrapSYS.exist_double(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def exist_string(cls, p1, p2):
        """
        This method checks to see if a string parameter exists.
        """
        ret_val = gxapi_cy.WrapSYS.exist_string(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def get_int(cls, p1, p2):
        """
        This method returns an int from the parameter block.
        """
        ret_val = gxapi_cy.WrapSYS.get_int(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def get_yes_no(cls, p1, p2):
        """
        Check a YES/NO Setting
        """
        ret_val = gxapi_cy.WrapSYS.get_yes_no(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def replace_string(cls, p1, p2, p4):
        """
        Replace "% %" tokens in a string with parameter values

        **Note:**

        If parameter does not exist, the token is removed.  Full parameter names,
        such as "%group.name%", are used as-is.  Partial parameter names, such as
        "%name%" will have the default group attached.
        """
        p2.value = gxapi_cy.WrapSYS.replace_string(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4.encode())
        



    @classmethod
    def load_parm(cls, p1, p2):
        """
        Reads parameters from a file.
        """
        gxapi_cy.WrapSYS.load_parm(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def get_double(cls, p1, p2):
        """
        This method returns a real from the parameter block.
        """
        ret_val = gxapi_cy.WrapSYS.get_double(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def save_parm(cls, p1, p2, p3):
        """
        Writes out one group (or all groups) to a file.
        """
        gxapi_cy.WrapSYS.save_parm(GXContext._get_tls_geo(), p1.encode(), p2, p3.encode())
        



    @classmethod
    def filter_parm_group(cls, p1, p2):
        """
        Controls filtering of specific group during logging.

        **Note:**

        This is useful to prevent certain utility GX parameters from being recorded during GS script runs where the parameters does not influence the actual script execution.
        """
        gxapi_cy.WrapSYS.filter_parm_group(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def set_int(cls, p1, p2, p3):
        """
        This method sets an int in the parameter block.
        """
        gxapi_cy.WrapSYS.set_int(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        



    @classmethod
    def set_pattern(cls, p1, p2, p3, p4, p5, p6, p7):
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
        gxapi_cy.WrapSYS.set_pattern(GXContext._get_tls_geo(), p1.encode(), p2, p3, p4, p5, p6, p7)
        



    @classmethod
    def set_double(cls, p1, p2, p3):
        """
        This method Sets a real in the parameter block.
        """
        gxapi_cy.WrapSYS.set_double(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3)
        



    @classmethod
    def set_reg(cls, p1):
        """
        Copy contents of a `GXREG` to current parameters.
        """
        gxapi_cy.WrapSYS.set_reg(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def set_string(cls, p1, p2, p3):
        """
        This method sets a string in the parameter block.
        """
        gxapi_cy.WrapSYS.set_string(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        




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
    def prog_name(cls, p1, p2):
        """
        This method allows you to name the current process being
        displayed by the progress bar. This method has no affect
        if no progress bar exists.
        """
        gxapi_cy.WrapSYS.prog_name(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def progress(cls, p1):
        """
        This method allows you to turn on the Progress BAR ON/OFF.
        Once the progress bar is on, use the UpdateProg method
        to drive it.
        """
        gxapi_cy.WrapSYS.progress(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def prog_update(cls, p1):
        """
        This method drives the Progress Bar. It is passed
        a percentage and will update the bar to reflect that
        percentage.
        """
        gxapi_cy.WrapSYS.prog_update(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def prog_update_l(cls, p1, p2):
        """
        Updates progress bar based on count and maxcount.
        """
        gxapi_cy.WrapSYS.prog_update_l(GXContext._get_tls_geo(), p1, p2)
        




# Registry


    @classmethod
    def get_sys_info(cls, p1, p2):
        """
        Get system information
        """
        p2.value = gxapi_cy.WrapSYS.get_sys_info(GXContext._get_tls_geo(), p1, p2.value.encode())
        



    @classmethod
    def registry_get_val(cls, p1, p2, p3, p4):
        """
        Get a registry value
        """
        ret_val, p4.value = gxapi_cy.WrapSYS.registry_get_val(GXContext._get_tls_geo(), p1, p2.encode(), p3.encode(), p4.value.encode())
        return ret_val



    @classmethod
    def registry_delete_key(cls, p1, p2):
        """
        Delete a registry value

        **Note:**

        All sub-keys and values will be deleted if they exist.
        """
        ret_val = gxapi_cy.WrapSYS.registry_delete_key(GXContext._get_tls_geo(), p1, p2.encode())
        return ret_val



    @classmethod
    def registry_delete_val(cls, p1, p2, p3):
        """
        Delete a registry value
        """
        ret_val = gxapi_cy.WrapSYS.registry_delete_val(GXContext._get_tls_geo(), p1, p2.encode(), p3.encode())
        return ret_val



    @classmethod
    def registry_set_val(cls, p1, p2, p3, p4):
        """
        Set/create a registry value

        **Note:**

        This function will create the subkey and key if either do not
        already exist.
        """
        gxapi_cy.WrapSYS.registry_set_val(GXContext._get_tls_geo(), p1, p2.encode(), p3.encode(), p4.encode())
        




# Temporary File


    @classmethod
    def destroy_ptmp(cls, p1):
        """
        Destroy PTMP.
        """
        gxapi_cy.WrapSYS.destroy_ptmp(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def get_ptmp(cls, p1):
        """
        Get temporary saves copy of parameter block.

        .. seealso::

            `save_ptmp`, `destroy_ptmp`
        """
        gxapi_cy.WrapSYS.get_ptmp(GXContext._get_tls_geo(), p1)
        



    @classmethod
    def save_ptmp(cls, p1):
        """
        Save a temporary copy of the parameter block.

        **Note:**

        All PTMP instances will be destroyed on exit.

        .. seealso::

            `get_ptmp`, `destroy_ptmp`
        """
        ret_val = gxapi_cy.WrapSYS.save_ptmp(GXContext._get_tls_geo(), p1.encode())
        return ret_val




# Termination


    @classmethod
    def abort(cls, p1):
        """
        This method terminates the execution of a script. A message
        giving the reason for the abort will be displayed along with
        the line number where we stopped in the script.
        """
        gxapi_cy.WrapSYS.abort(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def assert_(cls, p1):
        """
        Abort with GX line number if not true.
        """
        gxapi_cy.WrapSYS.assert_(GXContext._get_tls_geo(), p1)
        



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
    def delay(cls, p1):
        """
        Idle delay method.
        """
        ret_val = gxapi_cy.WrapSYS.delay(GXContext._get_tls_geo(), p1)
        return ret_val



    @classmethod
    def get_timer(cls, p1, p2, p3):
        """
        Return the elapsed time since the established time.

        **Note:**

        1st time through call the method with a flag of 1 to identify
        the count start time, subsequent times the time will be the time
        elapsed since the queried start time.  Do so by settign the flag to 0.
        """
        ret_val, p2.value, p3.value = gxapi_cy.WrapSYS.get_timer(GXContext._get_tls_geo(), p1, p2.value, p3.value)
        return ret_val




# User Interaction


    @classmethod
    def display_help(cls, p1, p2):
        """
        Display the help dialog with the specified topic highlighted
        """
        gxapi_cy.WrapSYS.display_help(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def display_help_topic(cls, p1, p2):
        """
        Display the help dialog without topic lookup in INI files
        """
        gxapi_cy.WrapSYS.display_help_topic(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def display_int(cls, p1, p2):
        """
        Display an integer.
        """
        gxapi_cy.WrapSYS.display_int(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def display_message(cls, p1, p2):
        """
        Display a user message.
        """
        gxapi_cy.WrapSYS.display_message(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        



    @classmethod
    def display_double(cls, p1, p2):
        """
        Display a real number.
        """
        gxapi_cy.WrapSYS.display_double(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def display_question(cls, p1, p2):
        """
        Display a YES/NO type question. This method waits
        for the user to hit YES or NO.
        """
        ret_val = gxapi_cy.WrapSYS.display_question(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def display_question_with_cancel(cls, p1, p2):
        """
        Display a YES/NO/CANCEL type question. This method waits
        for the user to hit YES or NO or CANCEL.
        """
        ret_val = gxapi_cy.WrapSYS.display_question_with_cancel(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        return ret_val



    @classmethod
    def display_task_dialog_ui(cls, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13):
        """
        Show a Windows TaskDialog UI (see https://msdn.microsoft.com/en-us/library/windows/desktop/bb760441(v=vs.85).aspx).
        """
        ret_val, p10.value = gxapi_cy.WrapSYS.display_task_dialog_ui(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4, p5._wrapper, p6, p7.encode(), p8, p9.encode(), p10.value, p11.encode(), p12.encode(), p13.encode())
        return ret_val



    @classmethod
    def interactive(cls):
        """
        Checks to see if you should run interactively.
        """
        ret_val = gxapi_cy.WrapSYS.interactive(GXContext._get_tls_geo())
        return ret_val



    @classmethod
    def prompt(cls, p1, p2):
        """
        Asks the User to enter a string.

        **Note:**

        The User string is displayed as the default value in the prompt.
        Empty the user string if no default is needed.
        """
        ret_val, p2.value = gxapi_cy.WrapSYS.prompt(GXContext._get_tls_geo(), p1.encode(), p2.value.encode())
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
    def set_cursor(cls, p1):
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
        gxapi_cy.WrapSYS.set_cursor(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def set_info_line(cls, p1):
        """
        Display a message on the information line at the left
        bottom corner of the OAISIS montaj application.
        """
        gxapi_cy.WrapSYS.set_info_line(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def set_interactive(cls, p1):
        """
        Sets the interactive mode.

        **Note:**

        Call to `interactive` will return the value
        set here.

        .. seealso::

            `interactive`, `run_gx` and `run_gs`
        """
        gxapi_cy.WrapSYS.set_interactive(GXContext._get_tls_geo(), p1)
        




# Workspace


    @classmethod
    def get_workspace_reg(cls, p1):
        """
        Get a copy of the workspace `GXREG`;

        **Note:**

        The workspace `GXREG` is separate from the reg used
        to store `GXSYS` parameters.
        
        Because `get_workspace_reg` returns a copy of the
        workspace `GXREG`, and not the workspace `GXREG` itself,
        you must call `set_workspace_reg` if you make changes
        to your own `GXREG` object and you wish them to take
        effect in the workspace `GXREG`.
        """
        gxapi_cy.WrapSYS.get_workspace_reg(GXContext._get_tls_geo(), p1._wrapper)
        



    @classmethod
    def set_workspace_reg(cls, p1):
        """
        Set the workspace `GXREG`;

        **Note:**

        The workspace `GXREG` is separate from the reg used
        to store `GXSYS` parameters.
        
        Because `get_workspace_reg` returns a copy of the
        workspace `GXREG`, and not the workspace `GXREG` itself,
        you must call `set_workspace_reg` if you make changes
        to your own `GXREG` object and you wish them to take
        effect in the workspace `GXREG`
        """
        gxapi_cy.WrapSYS.set_workspace_reg(GXContext._get_tls_geo(), p1._wrapper)
        




# String Encryption


    @classmethod
    def encrypt_string(cls, p1, p2, p4):
        """
        Encrypts a string for secure storage in configuration files
        or in the workspace parameters.
        """
        p2.value = gxapi_cy.WrapSYS.encrypt_string(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4)
        



    @classmethod
    def decrypt_string(cls, p1, p2, p4):
        """
        Decrypts a string that has been previously encrypted by `encrypt_string`().
        """
        p2.value = gxapi_cy.WrapSYS.decrypt_string(GXContext._get_tls_geo(), p1.encode(), p2.value.encode(), p4)
        



    @classmethod
    def is_encrypted_string(cls, p1):
        """
        Checks whether the specified string was encrypted by `encrypt_string`().
        """
        ret_val = gxapi_cy.WrapSYS.is_encrypted_string(GXContext._get_tls_geo(), p1.encode())
        return ret_val




# GX Debugger


    @classmethod
    def disable_gx_debugger(cls):
        """
        Disable GX Debugger `GXGUI` if active

        **Note:**

        All breakpoints will be cleared by this call.
        """
        gxapi_cy.WrapSYS.disable_gx_debugger(GXContext._get_tls_geo())
        



    @classmethod
    def enable_gx_debugger(cls, p1, p2):
        """
        Enable GX Debugger `GXGUI`

        **Note:**

        Takes as input two strings one a path that will be scanned
        recursively for GXC source files and a second string without
        a path of the GX where the first breakpoint should be set in (i.e. "gxname.gx").
        The source of the GX should be found in the path (e.g. <path>\\somewhere\\gxname.gxc)
        and a breakpoint will be set on the first executing line of this GX. Make sure the
        GX binary is newer than the source file, otherwise unexpected results may occur. As
        soon as the GX is run the `GXGUI` will become visible and it will be possible to set more
        breakpoints in any of the GXC files found in the path.
        """
        gxapi_cy.WrapSYS.enable_gx_debugger(GXContext._get_tls_geo(), p1.encode(), p2.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer