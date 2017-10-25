### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from typing import NewType
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXDB import GXDB


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXEDB:
    """
    GXEDB class.

    The `GXEDB` class provides access to a database as displayed within
    Oasis montaj, but does not change data within the database itself.
    It performs functions such as setting the current line.

    **Note:**

    To obtain access to the database itself, it is recommended practice
    to begin with an `GXEDB` object, and use the `lock` function to
    lock the underlying map to prevent external changes. The returned
    `GXDB` object (see `GXDB`) may then be safely used to make changes to the map itself.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapEDB(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXEDB`
        
        :returns: A null `GXEDB`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXEDB` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXEDB`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def apply_formula_internal(self, p2):
        """
        Apply a formula to selected cells of the
        current line. (Do not use this wrapper if you
        want to apply a formula across multiple lines)
        
        Notes:
        
        The current selection must be on cell(s) of
        a channel or on the a channel header.
        
        If the selection is on cell(s) of a channel,
        the formula is applied to only these cells.
        
        If the selection is on a channel header, the
        formula is applied to every cell in the channel.
        
        The given formula string must be of the form:
        "<NameOfCurrentChannel>=<SomeExpression>;"
        e.g. "x=y+1;"
        """
        self._wrapper.apply_formula_internal(p2.encode())
        



    @classmethod
    def current(cls):
        """
        This method returns the Current Edited Database.
        """
        ret_val = gxapi_cy.WrapEDB.current(GXContext._get_tls_geo())
        return GXEDB(ret_val)



    @classmethod
    def current_no_activate(cls):
        """
        This method returns the Current Edited Database.

        **Note:**

        This function acts just like `current` except that the document is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEDB.current_no_activate(GXContext._get_tls_geo())
        return GXEDB(ret_val)



    @classmethod
    def current_if_exists(cls):
        """
        This method returns the Current Edited Database.
        """
        ret_val = gxapi_cy.WrapEDB.current_if_exists(GXContext._get_tls_geo())
        return GXEDB(ret_val)




    def del_line0(self):
        """
        Delete Line 0.

        **Note:**

        Deletes an empty line 0 from the database.
        """
        self._wrapper.del_line0()
        






    def destroy_view(self, p2):
        """
        Removes the view from the workspace.

        **Note:**

        Can only be run in interactive mode. After this call the
        `GXEDB` object will become invalid. If this is the last view on
        the document and the document has been modified the map will be
        unloaded and optionally saved depending on the `EDB_REMOVE`
        parameter.
        """
        self._wrapper.destroy_view(p2)
        




    def get_cur_chan_symb(self):
        """
        Returns the currently marked channel symbol.
        """
        ret_val = self._wrapper.get_cur_chan_symb()
        return ret_val




    def get_cur_line_symb(self):
        """
        Get current line symbol.
        """
        ret_val = self._wrapper.get_cur_line_symb()
        return ret_val




    def get_displ_fid_range(self, p2, p3):
        """
        Return the displayed fiducial start index & number of cells
        """
        p2.value, p3.value = self._wrapper.get_displ_fid_range(p2.value, p3.value)
        




    def get_cur_point(self, p2, p3, p4):
        """
        Returns the coordinates of the currently selected point in the database (first value if range selected)
        """
        p2.value, p3.value, p4.value = self._wrapper.get_cur_point(p2.value, p3.value, p4.value)
        




    def get_fid_range(self, p2, p3, p4):
        """
        Returns currently displayed fid range
        """
        p2.value, p3.value, p4.value = self._wrapper.get_fid_range(p2.value, p3.value, p4.value)
        




    def get_next_line_symb(self):
        """
        Returns the next line symbol.
        """
        ret_val = self._wrapper.get_next_line_symb()
        return ret_val




    def get_prev_line_symb(self):
        """
        Returns the previous line symbol.
        """
        ret_val = self._wrapper.get_prev_line_symb()
        return ret_val




    def get_profile_range_x(self, p2, p3, p4):
        """
        Get profile X range and X channel
        """
        p2.value, p3.value, p4.value = self._wrapper.get_profile_range_x(p2.value, p3.value, p4.value)
        




    def get_profile_range_y(self, p2, p3, p4, p5, p6):
        """
        Get profile Y range and display option
        """
        p4.value, p5.value, p6.value = self._wrapper.get_profile_range_y(p2, p3, p4.value, p5.value, p6.value)
        




    def get_profile_split(self, p2, p3):
        """
        Get profile split for 3 windows.
        """
        p2.value, p3.value = self._wrapper.get_profile_split(p2.value, p3.value)
        




    def get_profile_split5(self, p2, p3, p4, p5):
        """
        Get profile split for 5 windows.
        """
        p2.value, p3.value, p4.value, p5.value = self._wrapper.get_profile_split5(p2.value, p3.value, p4.value, p5.value)
        




    def get_profile_split_vv(self, p2):
        """
        Get profile window splits.

        **Note:**

        The returned `GXVV` is sized to the maximum number of profiles
        that can be displayed. If a profile is not currently displayed,
        its height fraction is 0.  The sum of all the fractions returned
        is equal to 1.
        
        The profile splits refers to the relative sizes of the individual
        profile windows. To get/set the fraction of the total database window
        devoted to the profiles, use the `set_split` and `get_split` functions.
        """
        self._wrapper.get_profile_split_vv(p2._wrapper)
        




    def get_profile_vertical_grid_lines(self, p2, p3):
        """
        Get profile grid vertical line info.
        """
        p2.value, p3.value = self._wrapper.get_profile_vertical_grid_lines(p2.value, p3.value)
        




    def get_profile_window(self, p2, p3, p4):
        """
        Get profile window size
        """
        p3.value, p4.value = self._wrapper.get_profile_window(p2, p3.value, p4.value)
        




    def goto_column(self, p2):
        """
        Move the channel marker to a specific column.
        """
        self._wrapper.goto_column(p2)
        




    def goto_elem(self, p2):
        """
        Goto an element in the current line.
        """
        self._wrapper.goto_elem(p2)
        




    def goto_line(self, p2):
        """
        Goto to a line symbol in the editor.
        """
        self._wrapper.goto_line(p2)
        




    def histogram(self, p2, p3, p4, p5):
        """
        Create histogram stats.
        """
        self._wrapper.histogram(p2._wrapper, p3, p4, p5)
        




    def all_chan_list(self, p2):
        """
        Get a list of the all channels but in the way they are displayed.

        **Note:**

        The `GXVV` elements must be INT.
        
        Displayed channel lists are filled in the order the channels
        appear on the display, left to right.

        .. seealso::

            `disp_chan_list`
        """
        ret_val = self._wrapper.all_chan_list(p2._wrapper)
        return ret_val




    def channels(self):
        """
        Returns number of displayed channels
        """
        ret_val = self._wrapper.channels()
        return ret_val




    def disp_chan_list(self, p2):
        """
        Get a list of the displayed channel symbols.

        **Note:**

        The `GXVV` elements must be INT.
        
        Displayed channel lists are filled in the order the channels
        appear on the display, left to right.

        .. seealso::

            `disp_chan_lst`
        """
        ret_val = self._wrapper.disp_chan_list(p2._wrapper)
        return ret_val




    def disp_chan_lst(self, p2):
        """
        Get a list of the displayed channel names.

        **Note:**

        Displayed channel lists are filled in the order the channels
        appear on the display, left to right.
        
        The channel names will be placed in the "Name" part of
        the list and the values are set to the symbol handle.

        .. seealso::

            `disp_chan_list`
        """
        ret_val = self._wrapper.disp_chan_lst(p2._wrapper)
        return ret_val




    def disp_class_chan_lst(self, p2, p3):
        """
        Get a list of the displayed channels in a given channel class.

        **Note:**

        Displayed channel lists are filled in the order the channels
        appear on the display, left to right.
        
        The channel names will be placed in the "Name" part of
        the list and the values are set to the symbol handle.
        
        Examples of channel classes in current use are "MASK" and
        "ASSAY". (Searches are case tolerant).

        .. seealso::

            `disp_chan_list`
        """
        ret_val = self._wrapper.disp_class_chan_lst(p2._wrapper, p3.encode())
        return ret_val




    def find_channel_column(self, p2):
        """
        Find the column that contains a channel
        """
        ret_val = self._wrapper.find_channel_column(p2.encode())
        return ret_val




    def find_nearest(self, p2, p3, p4, p5):
        """
        Find the nearest point on the current line based
        on X,Y and Z and their projection.
        """
        ret_val, p2.value, p3.value, p4.value = self._wrapper.find_nearest(p2.value, p3.value, p4.value, p5._wrapper)
        return ret_val




    def get_cur_chan(self, p2):
        """
        Get current channel name.

        **Note:**

        Returns "" if mark not currently in a channel.
        """
        p2.value = self._wrapper.get_cur_chan(p2.value.encode())
        




    def get_cur_fid_string(self, p2):
        """
        This method returns the currently selected value
        at the current fid (if available).
        """
        p2.value = self._wrapper.get_cur_fid_string(p2.value.encode())
        




    def get_cur_line(self, p2):
        """
        Get current line name.
        """
        p2.value = self._wrapper.get_cur_line(p2.value.encode())
        




    def get_cur_mark(self, p2, p3, p4):
        """
        Returns the current data mark info.
        """
        ret_val, p2.value, p3.value, p4.value = self._wrapper.get_cur_mark(p2.value, p3.value, p4.value)
        return ret_val




    def get_current_selection(self, p2, p4, p6, p8):
        """
        Get current selection information.

        **Note:**

        Channel Name    Empty if no channel
        Line Name       "[All]" if all lines are selected
        Fid Range       "[All]" if all values in all lines are selected
        "[None]"  if no values are selected
        "10 to 20"  giving the range of values.
        """
        p2.value, p4.value, p6.value, p8.value = self._wrapper.get_current_selection(p2.value.encode(), p4.value.encode(), p6.value.encode(), p8.value.encode())
        



    @classmethod
    def get_databases_lst(cls, p1, p2):
        """
        Load the file names of open databases into a `GXLST`.
        """
        ret_val = gxapi_cy.WrapEDB.get_databases_lst(GXContext._get_tls_geo(), p1._wrapper, p2)
        return ret_val




    def get_mark_chan_vv(self, p2, p3):
        """
        Get channel data for the current mark.

        **Note:**

        The current "mark" in this case is the start and
        end fiducials and not the selected channel. You
        can use this method to retrieve the selected range
        from any channel, loaded or not.
        
        The `GXVV` will be resized to the length of the data
        """
        ret_val = self._wrapper.get_mark_chan_vv(p2._wrapper, p3)
        return ret_val




    def get_mark_chan_va(self, p2, p3):
        """
        Get channel data for the current mark.

        **Note:**

        The current "mark" in this case is the start and
        end fiducials and not the selected channel. You
        can use this method to retrieve the selected range
        from any channel, loaded or not.
        
        The `GXVA` will be resized to the length of the data
        """
        ret_val = self._wrapper.get_mark_chan_va(p2._wrapper, p3)
        return ret_val




    def get_name(self, p2):
        """
        Get the name of the database object of this `GXEDB`.
        """
        p2.value = self._wrapper.get_name(p2.value.encode())
        




    def get_profile_parm_int(self, p2, p3, p4):
        """
        Get integer profile parameter
        """
        ret_val = self._wrapper.get_profile_parm_int(p2, p3, p4)
        return ret_val




    def get_window_state(self):
        """
        Retrieve the current state of the database window
        """
        ret_val = self._wrapper.get_window_state()
        return ret_val



    @classmethod
    def have_current(cls):
        """
        Returns true if a database is loaded
        """
        ret_val = gxapi_cy.WrapEDB.have_current(GXContext._get_tls_geo())
        return ret_val




    def is_locked(self):
        """
        Is this Database locked
        """
        ret_val = self._wrapper.is_locked()
        return ret_val



    @classmethod
    def loaded(cls, p1):
        """
        Returns 1 if a database is loaded .
        """
        ret_val = gxapi_cy.WrapEDB.loaded(GXContext._get_tls_geo(), p1.encode())
        return ret_val




    def profile_open(self, p2):
        """
        Return TRUE or FALSE if profile window is open

        **Note:**

        This functions will return FALSE if requested window
        is not supported in current version of Oasis montaj.
        """
        ret_val = self._wrapper.profile_open(p2)
        return ret_val




    def read_only(self):
        """
        Checks if a database is currently opened in a read-only mode.
        """
        ret_val = self._wrapper.read_only()
        return ret_val




    def get_window_position(self, p2, p3, p4, p5, p6, p7):
        """
        Get the map window's position and dock state
        """
        p2.value, p3.value, p4.value, p5.value, p6.value, p7.value = self._wrapper.get_window_position(p2.value, p3.value, p4.value, p5.value, p6.value, p7.value)
        




    def set_window_position(self, p2, p3, p4, p5, p6, p7):
        """
        Get the map window's position and dock state
        """
        self._wrapper.set_window_position(p2, p3, p4, p5, p6, p7)
        




    def show_profile_name(self, p2, p3):
        """
        Show a profile in the profile window

        **Note:**

        If the symbol is not loaded, it will be loaded.
        """
        ret_val = self._wrapper.show_profile_name(p2, p3.encode())
        return ret_val




    def get_window_y_axis_direction(self, p2):
        """
        Get the y-axis direction for a window
        """
        ret_val = self._wrapper.get_window_y_axis_direction(p2)
        return ret_val




    def window_profiles(self, p2):
        """
        Get number of profiles in a window
        """
        ret_val = self._wrapper.window_profiles(p2)
        return ret_val




    def launch_histogram(self, p2):
        """
        Launch histogram tool on a database.

        .. seealso::

            `GXCHIMERA.launch_histogram` in chimera.gxh
        """
        self._wrapper.launch_histogram(p2.encode())
        




    def launch_scatter(self):
        """
        Launch scatter tool on a database.

        **Note:**

        The scatter tool uses the following INI parameters
        
        SCATTER.STM       name of the scatter template,"none" for none
        SCATTER.STM_NAME  name of last template section, "" for none.
        SCATTER.X         name of channel to display in X
        SCATTER.Y         name of channel to display in Y
        SCATTER.MASK      name of channel to use for mask

        .. seealso::

            `GXCHIMERA.launch_scatter` in chimera.gxh
        """
        self._wrapper.launch_scatter()
        



    @classmethod
    def load(cls, p1):
        """
        Loads a list of databases into the workspace

        **Note:**

        The last listed database will become the current database.
        
        Databases may already be loaded.
        
        Only the first file in the list may have a directory path.
        All other files in the list are assumed to be in the same
        directory as the first file.
        """
        ret_val = gxapi_cy.WrapEDB.load(GXContext._get_tls_geo(), p1.encode())
        return GXEDB(ret_val)



    @classmethod
    def load_no_activate(cls, p1):
        """
        Loads documents into the workspace

        **Note:**

        This function acts just like `load` except that the document(s) is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEDB.load_no_activate(GXContext._get_tls_geo(), p1.encode())
        return GXEDB(ret_val)




    def load_all_chans(self):
        """
        Load all channels into current database
        """
        self._wrapper.load_all_chans()
        




    def load_chan(self, p2):
        """
        Load a channel into current database

        **Note:**

        If the channel does not exist, or if channel is already
        loaded nothing happens.
        """
        self._wrapper.load_chan(p2.encode())
        



    @classmethod
    def load_new(cls, p1):
        """
        Loads a database into the workspace, flags as new.

        **Note:**

        See `load`. This is used for brand new databases, to set
        an internal flag such that if on closing the user chooses
        not to save changes, the database is deleted.
        """
        ret_val = gxapi_cy.WrapEDB.load_new(GXContext._get_tls_geo(), p1.encode())
        return GXEDB(ret_val)



    @classmethod
    def load_pass(cls, p1, p2, p3):
        """
        Loads a database into the editor with login and password.

        **Note:**

        The loaded database will become the current database.
        
        If the database is already loaded, it simply becomes
        the current database.
        """
        ret_val = gxapi_cy.WrapEDB.load_pass(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode())
        return GXEDB(ret_val)



    @classmethod
    def load_with_view(cls, p1, p2):
        """
        Load an `GXEDB` with the view from a current `GXEDB`.

        **Note:**

        Can only be run in interactive mode. Is used by
        dbsubset to create a new database with the same
        view as previously.
        """
        ret_val = gxapi_cy.WrapEDB.load_with_view(GXContext._get_tls_geo(), p1.encode(), p2._wrapper)
        return GXEDB(ret_val)




    def lock(self):
        """
        This method locks the Edited Database.
        """
        ret_val = self._wrapper.lock()
        return GXDB(ret_val)




    def make_current(self):
        """
        Makes this `GXEDB` object the current active object to the user.
        """
        self._wrapper.make_current()
        




    def remove_profile(self, p2, p3):
        """
        Remove a profile from the profile window
        """
        self._wrapper.remove_profile(p2, p3)
        




    def get_cur_fid(self):
        """
        This method returns the currently selected fiducial if
        the user is selecting a fiducial. If not, it returns
        a dummy.
        """
        ret_val = self._wrapper.get_cur_fid()
        return ret_val




    def get_profile_parm_double(self, p2, p3, p4):
        """
        Get real profile parameter
        """
        ret_val = self._wrapper.get_profile_parm_double(p2, p3, p4)
        return ret_val




    def get_split(self):
        """
        Get split ratio between spreadsheet and profile sections.
        """
        ret_val = self._wrapper.get_split()
        return ret_val




    def run_channel_maker(self, p2):
        """
        Run the maker for a single channel.

        **Note:**

        Skips channels without makers; will not return an
        error if the channel does not exist.
        """
        self._wrapper.run_channel_maker(p2.encode())
        




    def run_channel_makers(self):
        """
        Recreate channels with makers.

        **Note:**

        Skips channels without makers.
        """
        self._wrapper.run_channel_makers()
        




    def set_cur_line(self, p2):
        """
        Set the current line name.
        """
        self._wrapper.set_cur_line(p2.encode())
        




    def set_cur_line_no_message(self, p2):
        """
        Set Line but do not send a message.
        """
        self._wrapper.set_cur_line_no_message(p2.encode())
        




    def set_cur_mark(self, p2, p3):
        """
        Set the current mark.
        """
        self._wrapper.set_cur_mark(p2, p3)
        




    def set_profile_parm_i(self, p2, p3, p4, p5):
        """
        Set integer profile parameter
        """
        self._wrapper.set_profile_parm_i(p2, p3, p4, p5)
        




    def set_profile_parm_r(self, p2, p3, p4, p5):
        """
        Set real profile parameter
        """
        self._wrapper.set_profile_parm_r(p2, p3, p4, p5)
        




    def set_profile_range_x(self, p2, p3, p4):
        """
        Set profile X range and X channel
        """
        self._wrapper.set_profile_range_x(p2, p3, p4)
        




    def set_profile_range_y(self, p2, p3, p4, p5, p6):
        """
        Set profile Y range and display option

        **Note:**

        If channel is not loaded or displayed, it will
        loaded and/or displayed.
        """
        self._wrapper.set_profile_range_y(p2, p3, p4, p5, p6)
        




    def set_profile_split(self, p2, p3):
        """
        Set profile split for 3 windows.
        """
        self._wrapper.set_profile_split(p2, p3)
        




    def set_profile_split5(self, p2, p3, p4, p5):
        """
        Set profile split for 5 windows.
        """
        self._wrapper.set_profile_split5(p2, p3, p4, p5)
        




    def set_profile_split_vv(self, p2):
        """
        Set profile splits

        **Note:**

        The input `GXVV` values are the fractional heights for each
        profile window. Values are summed, and normalized (so you can
        enter "1,1,1", with a `GXVV` of length 3, if you want 3 equal profile windows).
        
        `GXVV` values beyond the maximum number of displayable
        profiles (`MAX_PROF_WND`) are ignored.
        """
        self._wrapper.set_profile_split_vv(p2._wrapper)
        




    def set_split(self, p2):
        """
        Set split ratio between spreadsheet and profile sections.

        **Note:**

        d = (spreadsheet window height/
        (spreadsheet window height + entire profile window height))
        """
        self._wrapper.set_split(p2)
        




    def set_window_state(self, p2):
        """
        Changes the state of the database window
        """
        self._wrapper.set_window_state(p2)
        




    def show_profile(self, p2, p3):
        """
        Show a profile in the profile window

        **Note:**

        If the symbol is not loaded, it will be loaded.
        """
        self._wrapper.show_profile(p2, p3)
        




    def statistics(self, p2):
        """
        Add all currently selected data to the `GXST`.

        **Note:**

        Use `histogram` to get median or histogram.
        """
        self._wrapper.statistics(p2._wrapper)
        



    @classmethod
    def un_load(cls, p1):
        """
        Unloads an edited database.

        **Note:**

        If the database is not loaded, nothing happens.
        Same as `un_load_verify` with FALSE to prompt save.
        """
        gxapi_cy.WrapEDB.un_load(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def un_load_all(cls):
        """
        Unloads all opened databases
        """
        gxapi_cy.WrapEDB.un_load_all(GXContext._get_tls_geo())
        




    def un_load_all_chans(self):
        """
        Unload all channels into current database
        """
        self._wrapper.un_load_all_chans()
        




    def un_load_chan(self, p2):
        """
        Unload a channel into current database

        **Note:**

        If the channel does not exist, or if channel is already
        loaded nothing happens.
        """
        self._wrapper.un_load_chan(p2.encode())
        



    @classmethod
    def un_load_discard(cls, p1):
        """
        Unloads a database in the workspace, discards changes.

        **Note:**

        If the database is not loaded, nothing happens.
        """
        gxapi_cy.WrapEDB.un_load_discard(GXContext._get_tls_geo(), p1.encode())
        



    @classmethod
    def un_load_verify(cls, p1, p2):
        """
        Unloads an edited database, optional prompt to save.

        **Note:**

        If the database is not loaded, nothing happens.
        The user can be prompted to save before unloading.
        If `EDB_UNLOAD_NO_PROMPT`, data is always saved.
        EDB_UNLOAD_MULTIPROMPT is now obsolete and
        is equivalent to `EDB_UNLOAD_SINGLE_PROMPT`.
        """
        gxapi_cy.WrapEDB.un_load_verify(GXContext._get_tls_geo(), p1.encode(), p2)
        




    def un_lock(self):
        """
        This method unlocks the Edited Database.
        """
        self._wrapper.un_lock()
        




# External Window


    @classmethod
    def load_control(cls, p1, p2):
        """
        Version of `load` that can be used to load a database via subclassing into a Windows control.
        """
        gxapi_cy.WrapEDB.load_control(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def load_new_control(cls, p1, p2):
        """
        Version of `load_new` that can be used to load a database via subclassing into a Windows control.
        """
        gxapi_cy.WrapEDB.load_new_control(GXContext._get_tls_geo(), p1.encode(), p2)
        



    @classmethod
    def load_pass_control(cls, p1, p2, p3, p4):
        """
        Version of `load_pass` that can be used to load a database via subclassing into a Windows control.
        """
        gxapi_cy.WrapEDB.load_pass_control(GXContext._get_tls_geo(), p1.encode(), p2.encode(), p3.encode(), p4)
        



    @classmethod
    def load_with_view_control(cls, p1, p2, p3):
        """
        Version of `load_with_view` that can be used to load a database via subclassing into a Windows control.
        """
        gxapi_cy.WrapEDB.load_with_view_control(GXContext._get_tls_geo(), p1.encode(), p2._wrapper, p3)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer