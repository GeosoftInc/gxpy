### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXDB import GXDB


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXEDB(gxapi_cy.WrapEDB):
    """
    GXEDB class.

    The `GXEDB <geosoft.gxapi.GXEDB>` class provides access to a database as displayed within
    Oasis montaj, but does not change data within the database itself.
    It performs functions such as setting the current line.

    **Note:**

    To obtain access to the database itself, it is recommended practice
    to begin with an `GXEDB <geosoft.gxapi.GXEDB>` object, and use the `lock <geosoft.gxapi.GXEDB.lock>` function to
    lock the underlying map to prevent external changes. The returned
    `GXDB <geosoft.gxapi.GXDB>` object (see `GXDB <geosoft.gxapi.GXDB>`) may then be safely used to make changes to the map itself.
    """

    def __init__(self, handle=0):
        super().__init__(GXContext._get_tls_geo(), handle)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXEDB <geosoft.gxapi.GXEDB>`
        
        :returns: A null `GXEDB <geosoft.gxapi.GXEDB>`
        :rtype:   GXEDB
        """
        return GXEDB()

    def is_null(self):
        """
        Check if this is a null (undefined) instance
        
        :returns: True if this is a null (undefined) instance, False otherwise.
        :rtype:   bool
        """
        return self._internal_handle() == 0



# Miscellaneous



    def apply_formula_internal(self, formula):
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
        
        :param formula:  Formula ("<NameOfCurrentChannel>=<SomeExpression>;")
        :type  formula:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._apply_formula_internal(formula.encode())
        



    @classmethod
    def current(cls):
        """
        This method returns the Current Edited Database.
        

        :returns:    `GXEDB <geosoft.gxapi.GXEDB>` Object
        :rtype:      GXEDB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEDB._current(GXContext._get_tls_geo())
        return GXEDB(ret_val)



    @classmethod
    def current_no_activate(cls):
        """
        This method returns the Current Edited Database.
        

        :returns:    `GXEDB <geosoft.gxapi.GXEDB>` Object
        :rtype:      GXEDB

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This function acts just like `current <geosoft.gxapi.GXEDB.current>` except that the document is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEDB._current_no_activate(GXContext._get_tls_geo())
        return GXEDB(ret_val)



    @classmethod
    def current_if_exists(cls):
        """
        This method returns the Current Edited Database.
        

        :returns:    `GXEDB <geosoft.gxapi.GXEDB>` Object to current edited database. If there is no current database,
                  the user is not prompted for a database, and 0 is returned.
        :rtype:      GXEDB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEDB._current_if_exists(GXContext._get_tls_geo())
        return GXEDB(ret_val)




    def del_line0(self):
        """
        Delete Line 0.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Deletes an empty line 0 from the database.
        """
        self._del_line0()
        






    def destroy_view(self, unload_flag):
        """
        Removes the view from the workspace.
        
        :param unload_flag:  :ref:`EDB_REMOVE`
        :type  unload_flag:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Can only be run in interactive mode. After this call the
        `GXEDB <geosoft.gxapi.GXEDB>` object will become invalid. If this is the last view on
        the document and the document has been modified the map will be
        unloaded and optionally saved depending on the :ref:`EDB_REMOVE`
        parameter.
        """
        self._destroy_view(unload_flag)
        




    def get_cur_chan_symb(self):
        """
        Returns the currently marked channel symbol.
        

        :returns:    Currently channel symbol.
                     `NULLSYMB <geosoft.gxapi.NULLSYMB>` if the mark is not in a channel.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_cur_chan_symb()
        return ret_val




    def get_cur_line_symb(self):
        """
        Get current line symbol.
        

        :returns:    Currently displayed line symbol.
                     `NULLSYMB <geosoft.gxapi.NULLSYMB>` if no line displayed.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_cur_line_symb()
        return ret_val




    def get_displ_fid_range(self, start, num):
        """
        Return the displayed fiducial start index & number of cells
        
        :param start:  Fiducial start
        :param num:    Number of fiducials
        :type  start:  int_ref
        :type  num:    int_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        start.value, num.value = self._get_displ_fid_range(start.value, num.value)
        




    def get_cur_point(self, x, y, z):
        """
        Returns the coordinates of the currently selected point in the database (first value if range selected)
        
        :param x:    X coordinate (dummy if no selection or if no X channel defined)
        :param y:    Y coordinate (dummy if no selection or if no Y channel defined)
        :param z:    Z coordinate (dummy if no selection or if no Z channel defined)
        :type  x:    float_ref
        :type  y:    float_ref
        :type  z:    float_ref

        .. versionadded:: 9.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        x.value, y.value, z.value = self._get_cur_point(x.value, y.value, z.value)
        




    def get_fid_range(self, start, incr, num):
        """
        Returns currently displayed fid range
        
        :param start:  Fiducial start
        :param incr:   Fiducial increment
        :param num:    Number of fiducials
        :type  start:  float_ref
        :type  incr:   float_ref
        :type  num:    int_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        start.value, incr.value, num.value = self._get_fid_range(start.value, incr.value, num.value)
        




    def get_next_line_symb(self):
        """
        Returns the next line symbol.
        

        :returns:    The next line symbol of currently displayed line.
                     `NULLSYMB <geosoft.gxapi.NULLSYMB>` if no line displayed.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_next_line_symb()
        return ret_val




    def get_prev_line_symb(self):
        """
        Returns the previous line symbol.
        

        :returns:    The previous line symbol of currently displayed line.
                     `NULLSYMB <geosoft.gxapi.NULLSYMB>` if no line displayed.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_prev_line_symb()
        return ret_val




    def get_profile_x_axis_options(self, rescale_x, lines, interval):
        """
        Get profile X-axis options
        
        :param rescale_x:  Auto rescale X-axis
        :param lines:      render vertical grid lines
        :param interval:   vertical lines interval
        :type  rescale_x:  bool_ref
        :type  lines:      bool_ref
        :type  interval:   float_ref

        .. versionadded:: 9.5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        rescale_x.value, lines.value, interval.value = self._get_profile_x_axis_options(rescale_x.value, lines.value, interval.value)
        




    def set_profile_x_axis_options(self, rescale_x, lines, interval):
        """
        Set profile X-axis options
        
        :param rescale_x:  Auto rescale X-axis
        :param lines:      render vertical grid lines
        :param interval:   vertical lines interval
        :type  rescale_x:  bool
        :type  lines:      bool
        :type  interval:   float

        .. versionadded:: 9.5.1

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_profile_x_axis_options(rescale_x, lines, interval)
        




    def get_profile_range_x(self, min_x, max_x, ph_chan_x):
        """
        Get profile X range and X channel
        
        :param min_x:      Minimum x
        :param max_x:      Maximum x
        :param ph_chan_x:  X axis channel, `NULLSYMB <geosoft.gxapi.NULLSYMB>` if none
        :type  min_x:      float_ref
        :type  max_x:      float_ref
        :type  ph_chan_x:  int_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        min_x.value, max_x.value, ph_chan_x.value = self._get_profile_range_x(min_x.value, max_x.value, ph_chan_x.value)
        




    def get_profile_range_y(self, window, prof, min_y, max_y, scl):
        """
        Get profile Y range and display option
        
        :param window:  Profile window number (0 to `MAX_PROF_WND <geosoft.gxapi.MAX_PROF_WND>`-1, see `profile_open <geosoft.gxapi.GXEDB.profile_open>`)
        :param prof:    Profile number in window (see `window_profiles <geosoft.gxapi.GXEDB.window_profiles>` which returns number of profiles in a window)
        :param min_y:   Minimum y
        :param max_y:   Maximum y
        :param scl:     :ref:`EDB_PROFILE_SCALE`
        :type  window:  int
        :type  prof:    int
        :type  min_y:   float_ref
        :type  max_y:   float_ref
        :type  scl:     int_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        min_y.value, max_y.value, scl.value = self._get_profile_range_y(window, prof, min_y.value, max_y.value, scl.value)
        




    def get_profile_split(self, d1, d2):
        """
        Get profile split for 3 windows.
        
        :param d1:   Split d1 (profile window 0 height / entire profile window height)
        :param d2:   Split d2 (profile window 1 height / entire profile window height)
        :type  d1:   float_ref
        :type  d2:   float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        d1.value, d2.value = self._get_profile_split(d1.value, d2.value)
        




    def get_profile_split5(self, d1, d2, d3, d4):
        """
        Get profile split for 5 windows.
        
        :param d1:   Split d1 (profile window 0 height / entire profile window height)
        :param d2:   Split d2 (profile window 1 height / entire profile window height)
        :param d3:   Split d3 (profile window 2 height / entire profile window height)
        :param d4:   Split d4 (profile window 3 height / entire profile window height)
        :type  d1:   float_ref
        :type  d2:   float_ref
        :type  d3:   float_ref
        :type  d4:   float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        d1.value, d2.value, d3.value, d4.value = self._get_profile_split5(d1.value, d2.value, d3.value, d4.value)
        




    def get_profile_split_vv(self, vv):
        """
        Get profile window splits.
        
        :param vv:   Split `GXVV <geosoft.gxapi.GXVV>` (REAL) (profile window heights / entire profile window height)
        :type  vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The returned `GXVV <geosoft.gxapi.GXVV>` is sized to the maximum number of profiles
        that can be displayed. If a profile is not currently displayed,
        its height fraction is 0.  The sum of all the fractions returned
        is equal to 1.

        The profile splits refers to the relative sizes of the individual
        profile windows. To get/set the fraction of the total database window
        devoted to the profiles, use the `set_split <geosoft.gxapi.GXEDB.set_split>` and `get_split <geosoft.gxapi.GXEDB.get_split>` functions.
        """
        self._get_profile_split_vv(vv)
        




    def get_profile_vertical_grid_lines(self, grid, interval):
        """
        Get profile grid vertical line info.
        
        :param grid:      Vertical grid lines?
        :param interval:  Vertical grid interval
        :type  grid:      int_ref
        :type  interval:  float_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        grid.value, interval.value = self._get_profile_vertical_grid_lines(grid.value, interval.value)
        




    def get_profile_window(self, window, x, y):
        """
        Get profile window size
        
        :param window:  Profile window number (0 to `MAX_PROF_WND <geosoft.gxapi.MAX_PROF_WND>`-1, see `profile_open <geosoft.gxapi.GXEDB.profile_open>`)
        :param x:       Window x size in pixels
        :param y:       Window y size in pixels
        :type  window:  int
        :type  x:       int_ref
        :type  y:       int_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        x.value, y.value = self._get_profile_window(window, x.value, y.value)
        




    def goto_column(self, col):
        """
        Move the channel marker to a specific column.
        
        :param col:  Channel column number, 0 is first -1 for first column without data
        :type  col:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._goto_column(col)
        




    def goto_elem(self, elem):
        """
        Goto an element in the current line.
        
        :param elem:  Element number
        :type  elem:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._goto_elem(elem)
        




    def goto_line(self, line_symb):
        """
        Goto to a line symbol in the editor.
        
        :param line_symb:  Line symbol to goto to
        :type  line_symb:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._goto_line(line_symb)
        




    def histogram(self, st, min, incr, count):
        """
        Create histogram stats.
        
        :param st:     `GXST <geosoft.gxapi.GXST>` handle to update
        :param min:    Histogram minimum
        :param incr:   Histogram increment
        :param count:  Number of increments
        :type  st:     GXST
        :type  min:    float
        :type  incr:   float
        :type  count:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._histogram(st, min, incr, count)
        




    def all_chan_list(self, vv):
        """
        Get a list of the all channels but in the way they are displayed.
        
        :param vv:   `GXVV <geosoft.gxapi.GXVV>` (INT) in which to place the list.
        :type  vv:   GXVV

        :returns:    Number of symbols in the list.
                     Terminates GX if there was an error.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The `GXVV <geosoft.gxapi.GXVV>` elements must be INT.

        Displayed channel lists are filled in the order the channels
        appear on the display, left to right.

        .. seealso::

            `disp_chan_list <geosoft.gxapi.GXEDB.disp_chan_list>`
        """
        ret_val = self._all_chan_list(vv)
        return ret_val




    def channels(self):
        """
        Returns number of displayed channels
        

        :returns:    x - number of displayed channels
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._channels()
        return ret_val




    def disp_chan_list(self, vv):
        """
        Get a list of the displayed channel symbols.
        
        :param vv:   `GXVV <geosoft.gxapi.GXVV>` (INT) in which to place the list.
        :type  vv:   GXVV

        :returns:    Number of symbols in the list.
                     Terminates GX if there was an error.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The `GXVV <geosoft.gxapi.GXVV>` elements must be INT.

        Displayed channel lists are filled in the order the channels
        appear on the display, left to right.

        .. seealso::

            `disp_chan_lst <geosoft.gxapi.GXEDB.disp_chan_lst>`
        """
        ret_val = self._disp_chan_list(vv)
        return ret_val




    def disp_chan_lst(self, lst):
        """
        Get a list of the displayed channel names.
        
        :param lst:  `GXLST <geosoft.gxapi.GXLST>` object
        :type  lst:  GXLST

        :returns:    Number of channels in the list.
                     Terminates GX if there was an error.
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Displayed channel lists are filled in the order the channels
        appear on the display, left to right.

        The channel names will be placed in the "Name" part of
        the list and the values are set to the symbol handle.

        .. seealso::

            `disp_chan_list <geosoft.gxapi.GXEDB.disp_chan_list>`
        """
        ret_val = self._disp_chan_lst(lst)
        return ret_val




    def disp_class_chan_lst(self, lst, class_name):
        """
        Get a list of the displayed channels in a given channel class.
        
        :param lst:         `GXLST <geosoft.gxapi.GXLST>` object
        :param class_name:  Class name ("" for all)
        :type  lst:         GXLST
        :type  class_name:  str

        :returns:           Number of channels in the list.
                            Terminates GX if there was an error.
        :rtype:             int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Displayed channel lists are filled in the order the channels
        appear on the display, left to right.

        The channel names will be placed in the "Name" part of
        the list and the values are set to the symbol handle.

        Examples of channel classes in current use are "MASK" and
        "ASSAY". (Searches are case tolerant).

        .. seealso::

            `disp_chan_list <geosoft.gxapi.GXEDB.disp_chan_list>`
        """
        ret_val = self._disp_class_chan_lst(lst, class_name.encode())
        return ret_val




    def find_channel_column(self, chan):
        """
        Find the column that contains a channel
        
        :param chan:  Channel
        :type  chan:  str

        :returns:     Column number that contains a specific channel
                      `iDUMMY <geosoft.gxapi.iDUMMY>` of channel not loaded
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._find_channel_column(chan.encode())
        return ret_val




    def find_nearest(self, x, y, z, ipj):
        """
        Find the nearest point on the current line based
        on X,Y and Z and their projection.
        
        :param x:    X - Modified with true point
        :param y:    Y - Modified with true point
        :param z:    Z - Modified with true point
        :param ipj:  Projection of X,Y,Z
        :type  x:    float_ref
        :type  y:    float_ref
        :type  z:    float_ref
        :type  ipj:  GXIPJ

        :returns:    x - Nearest point
                     -1 - Not available
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val, x.value, y.value, z.value = self._find_nearest(x.value, y.value, z.value, ipj)
        return ret_val




    def get_cur_chan(self, str_val):
        """
        Get current channel name.
        
        :param str_val:  Where to put the name
        :type  str_val:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Returns "" if mark not currently in a channel.
        """
        str_val.value = self._get_cur_chan(str_val.value.encode())
        




    def get_cur_fid_string(self, val):
        """
        This method returns the currently selected value
        at the current fid (if available).
        
        :param val:  String returned here
        :type  val:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        val.value = self._get_cur_fid_string(val.value.encode())
        




    def get_cur_line(self, str_val):
        """
        Get current line name.
        
        :param str_val:  Where to put the name
        :type  str_val:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        str_val.value = self._get_cur_line(str_val.value.encode())
        




    def get_cur_mark(self, start, end, inc):
        """
        Returns the current data mark info.
        
        :param start:  Start fiducial
        :param end:    End fiducial
        :param inc:    Fiducial increment
        :type  start:  float_ref
        :type  end:    float_ref
        :type  inc:    float_ref

        :returns:      0 - if data is marked.
                       1 - if data is not currently marked.
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val, start.value, end.value, inc.value = self._get_cur_mark(start.value, end.value, inc.value)
        return ret_val




    def get_current_selection(self, db, chan, line, fid):
        """
        Get current selection information.
        
        :param db:    Database name
        :param chan:  Name of Selected channel
        :param line:  Selected lines buffer
        :param fid:   Fiducial range
        :type  db:    str_ref
        :type  chan:  str_ref
        :type  line:  str_ref
        :type  fid:   str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Channel Name    Empty if no channel
        Line Name       "[All]" if all lines are selected
        Fid Range       "[All]" if all values in all lines are selected
        "[None]"  if no values are selected
        "10 to 20"  giving the range of values.
        """
        db.value, chan.value, line.value, fid.value = self._get_current_selection(db.value.encode(), chan.value.encode(), line.value.encode(), fid.value.encode())
        



    @classmethod
    def get_databases_lst(cls, lst, path):
        """
        Load the file names of open databases into a `GXLST <geosoft.gxapi.GXLST>`.
        
        :param lst:   `GXLST <geosoft.gxapi.GXLST>` to load
        :param path:  :ref:`EDB_PATH`
        :type  lst:   GXLST
        :type  path:  int

        :returns:     The number of documents loaded into the `GXLST <geosoft.gxapi.GXLST>`.
                      The `GXLST <geosoft.gxapi.GXLST>` is cleared first.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEDB._get_databases_lst(GXContext._get_tls_geo(), lst, path)
        return ret_val




    def get_mark_chan_vv(self, vv, chan):
        """
        Get channel data for the current mark.
        
        :param vv:    `GXVV <geosoft.gxapi.GXVV>` in which to place the data.
        :param chan:  Channel symbol to retrieve.
        :type  vv:    GXVV
        :type  chan:  int

        :returns:     0 if successful.
                      1 if failed, or if entire database is marked.
        :rtype:       int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The current "mark" in this case is the start and
        end fiducials and not the selected channel. You
        can use this method to retrieve the selected range
        from any channel, loaded or not.

        The `GXVV <geosoft.gxapi.GXVV>` will be resized to the length of the data
        """
        ret_val = self._get_mark_chan_vv(vv, chan)
        return ret_val




    def get_mark_chan_va(self, vv, chan):
        """
        Get channel data for the current mark.
        
        :param vv:    `GXVA <geosoft.gxapi.GXVA>` in which to place the data.
        :param chan:  Channel symbol to retrieve.
        :type  vv:    GXVA
        :type  chan:  int

        :returns:     0 if successful.
                      1 if failed, or if entire database is marked.
        :rtype:       int

        .. versionadded:: 8.2

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The current "mark" in this case is the start and
        end fiducials and not the selected channel. You
        can use this method to retrieve the selected range
        from any channel, loaded or not.

        The `GXVA <geosoft.gxapi.GXVA>` will be resized to the length of the data
        """
        ret_val = self._get_mark_chan_va(vv, chan)
        return ret_val




    def get_name(self, name):
        """
        Get the name of the database object of this `GXEDB <geosoft.gxapi.GXEDB>`.
        
        :param name:  Name returned
        :type  name:  str_ref

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        name.value = self._get_name(name.value.encode())
        




    def get_profile_parm_int(self, window, prof, parm):
        """
        Get integer profile parameter
        
        :param window:  Profile window number (0 to `MAX_PROF_WND <geosoft.gxapi.MAX_PROF_WND>`-1, see `profile_open <geosoft.gxapi.GXEDB.profile_open>`)
        :param prof:    Profile number in window (see `get_profile_range_y <geosoft.gxapi.GXEDB.get_profile_range_y>`)
        :param parm:    :ref:`EDB_PROF`
        :type  window:  int
        :type  prof:    int
        :type  parm:    int

        :returns:       Data Value (See notes)
        :rtype:         int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_profile_parm_int(window, prof, parm)
        return ret_val




    def get_window_state(self):
        """
        Retrieve the current state of the database window
        

        :returns:    :ref:`EDB_WINDOW_STATE`
        :rtype:      int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_window_state()
        return ret_val



    @classmethod
    def have_current(cls):
        """
        Checks if any database is currently loaded
        
        :rtype:      bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEDB._have_current(GXContext._get_tls_geo())
        return ret_val




    def is_locked(self):
        """
        Checks if the database locked
        
        :rtype:      bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._is_locked()
        return ret_val



    @classmethod
    def loaded(cls, name):
        """
        Checks if a specific database is loaded.
        
        :param name:  Database name
        :type  name:  str
        :rtype:       bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = gxapi_cy.WrapEDB._loaded(GXContext._get_tls_geo(), name.encode())
        return ret_val




    def profile_open(self, window):
        """
        Return TRUE or FALSE if profile window is open
        
        :param window:  Profile window number: 0 is the top window 1 is the middle window 2 is the bottom window
        :type  window:  int

        :returns:       TRUE if window is open
                        FALSE if window is closed
        :rtype:         int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This functions will return FALSE if requested window
        is not supported in current version of Oasis montaj.
        """
        ret_val = self._profile_open(window)
        return ret_val




    def read_only(self):
        """
        Checks if a database is currently opened in a read-only mode.
        
        :rtype:      bool

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._read_only()
        return ret_val




    def get_window_position(self, left, top, right, bottom, state, is_floating):
        """
        Get the map window's position and dock state
        
        :param left:         Window left position
        :param top:          Window top position
        :param right:        Window right position
        :param bottom:       Window bottom position
        :param state:        Window state :ref:`EDB_WINDOW_STATE`
        :param is_floating:  Docked or floating :ref:`EDB_WINDOW_POSITION`
        :type  left:         int_ref
        :type  top:          int_ref
        :type  right:        int_ref
        :type  bottom:       int_ref
        :type  state:        int_ref
        :type  is_floating:  int_ref

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        left.value, top.value, right.value, bottom.value, state.value, is_floating.value = self._get_window_position(left.value, top.value, right.value, bottom.value, state.value, is_floating.value)
        




    def set_window_position(self, left, top, right, bottom, state, is_floating):
        """
        Get the map window's position and dock state
        
        :param left:         Window left position
        :param top:          Window top position
        :param right:        Window right position
        :param bottom:       Window bottom position
        :param state:        Window state :ref:`EDB_WINDOW_STATE`
        :param is_floating:  Docked or floating :ref:`EDB_WINDOW_POSITION`
        :type  left:         int
        :type  top:          int
        :type  right:        int
        :type  bottom:       int
        :type  state:        int
        :type  is_floating:  int

        .. versionadded:: 9.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_window_position(left, top, right, bottom, state, is_floating)
        




    def show_profile_name(self, state, chan):
        """
        Show a profile in the profile window
        
        :param state:  Profile window number (0 to `MAX_PROF_WND <geosoft.gxapi.MAX_PROF_WND>`-1, see `profile_open <geosoft.gxapi.GXEDB.profile_open>`)
        :param chan:   Name of the channel
        :type  state:  int
        :type  chan:   str

        :returns:      Profile ID if loaded, -1 for error
        :rtype:        int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the symbol is not loaded, it will be loaded.
        """
        ret_val = self._show_profile_name(state, chan.encode())
        return ret_val




    def get_window_y_axis_direction(self, window):
        """
        Get the y-axis direction for a window
        
        :param window:  Profile window number (0 to `MAX_PROF_WND <geosoft.gxapi.MAX_PROF_WND>`-1, see `profile_open <geosoft.gxapi.GXEDB.profile_open>`)
        :type  window:  int

        :returns:       :ref:`EDB_YAXIS_DIRECTION`
        :rtype:         int

        .. versionadded:: 8.3

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_window_y_axis_direction(window)
        return ret_val




    def window_profiles(self, window):
        """
        Get number of profiles in a window
        
        :param window:  Profile window number (0 to `MAX_PROF_WND <geosoft.gxapi.MAX_PROF_WND>`-1, see `profile_open <geosoft.gxapi.GXEDB.profile_open>`)
        :type  window:  int

        :returns:       Number of profiles in a window
        :rtype:         int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._window_profiles(window)
        return ret_val




    def launch_histogram(self, chan):
        """
        Launch histogram tool on a database.
        
        :param chan:  First chan name
        :type  chan:  str

        .. versionadded:: 5.0.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        .. seealso::

            `GXCHIMERA.launch_histogram <geosoft.gxapi.GXCHIMERA.launch_histogram>` in chimera.gxh
        """
        self._launch_histogram(chan.encode())
        




    def launch_scatter(self):
        """
        Launch scatter tool on a database.
        

        .. versionadded:: 5.0.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Note:** The scatter tool uses the following INI parameters

        SCATTER.STM       name of the scatter template,"none" for none
        SCATTER.STM_NAME  name of last template section, "" for none.
        SCATTER.X         name of channel to display in X
        SCATTER.Y         name of channel to display in Y
        SCATTER.MASK      name of channel to use for mask

        .. seealso::

            `GXCHIMERA.launch_scatter <geosoft.gxapi.GXCHIMERA.launch_scatter>` in chimera.gxh
        """
        self._launch_scatter()
        



    @classmethod
    def load(cls, name):
        """
        Loads a list of databases into the workspace
        
        :param name:  List of databases (';' or '|' delimited) to load.
        :type  name:  str

        :returns:     Handle to current edited database, which will be the last
                      database in the list.
        :rtype:       GXEDB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The last listed database will become the current database.

        Databases may already be loaded.

        Only the first file in the list may have a directory path.
        All other files in the list are assumed to be in the same
        directory as the first file.
        """
        ret_val = gxapi_cy.WrapEDB._load(GXContext._get_tls_geo(), name.encode())
        return GXEDB(ret_val)



    @classmethod
    def load_no_activate(cls, name):
        """
        Loads documents into the workspace
        
        :param name:  List of documents (';' or '|' delimited) to load.
        :type  name:  str

        :returns:     Handle to current edited document, which will be the last
                      database in the list if multiple files were provided.
        :rtype:       GXEDB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** This function acts just like `load <geosoft.gxapi.GXEDB.load>` except that the document(s) is not activated (brought to foreground) and no
        guarantee is given about which document is currently active.
        """
        ret_val = gxapi_cy.WrapEDB._load_no_activate(GXContext._get_tls_geo(), name.encode())
        return GXEDB(ret_val)




    def load_all_chans(self):
        """
        Load all channels into current database
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._load_all_chans()
        




    def load_chan(self, chan):
        """
        Load a channel into current database
        
        :param chan:  Channel name
        :type  chan:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the channel does not exist, or if channel is already
        loaded nothing happens.
        """
        self._load_chan(chan.encode())
        



    @classmethod
    def load_new(cls, name):
        """
        Loads a database into the workspace, flags as new.
        
        :param name:  Database to load.
        :type  name:  str

        :returns:     Handle to the current edited database.
        :rtype:       GXEDB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** See `load <geosoft.gxapi.GXEDB.load>`. This is used for brand new databases, to set
        an internal flag such that if on closing the user chooses
        not to save changes, the database is deleted.
        """
        ret_val = gxapi_cy.WrapEDB._load_new(GXContext._get_tls_geo(), name.encode())
        return GXEDB(ret_val)



    @classmethod
    def load_pass(cls, name, login, password):
        """
        Loads a database into the editor with login and password.
        
        :param name:      Name of database to load
        :param login:     Login Name
        :param password:  Password
        :type  name:      str
        :type  login:     str
        :type  password:  str

        :returns:         Handle to current edited database.
        :rtype:           GXEDB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The loaded database will become the current database.

        If the database is already loaded, it simply becomes
        the current database.
        """
        ret_val = gxapi_cy.WrapEDB._load_pass(GXContext._get_tls_geo(), name.encode(), login.encode(), password.encode())
        return GXEDB(ret_val)



    @classmethod
    def load_with_view(cls, name, p2):
        """
        Load an `GXEDB <geosoft.gxapi.GXEDB>` with the view from a current `GXEDB <geosoft.gxapi.GXEDB>`.
        
        :param name:  Source `GXDB <geosoft.gxapi.GXDB>` name
        :param p2:    `GXEDB <geosoft.gxapi.GXEDB>` to use as the source view
        :type  name:  str
        :type  p2:    GXEDB

        :returns:     New `GXEDB <geosoft.gxapi.GXEDB>` handle.
        :rtype:       GXEDB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Can only be run in interactive mode. Is used by
        dbsubset to create a new database with the same
        view as previously.
        """
        ret_val = gxapi_cy.WrapEDB._load_with_view(GXContext._get_tls_geo(), name.encode(), p2)
        return GXEDB(ret_val)




    def lock(self):
        """
        This method locks the Edited Database.
        

        :returns:    Handle to database associated with edited database.
        :rtype:      GXDB

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._lock()
        return GXDB(ret_val)




    def make_current(self):
        """
        Makes this `GXEDB <geosoft.gxapi.GXEDB>` object the current active object to the user.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._make_current()
        




    def remove_profile(self, window, prof):
        """
        Remove a profile from the profile window
        
        :param window:  Profile window number (0 to `MAX_PROF_WND <geosoft.gxapi.MAX_PROF_WND>`-1, see `profile_open <geosoft.gxapi.GXEDB.profile_open>`)
        :param prof:    Profile number in window (see `get_profile_range_y <geosoft.gxapi.GXEDB.get_profile_range_y>`)
        :type  window:  int
        :type  prof:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._remove_profile(window, prof)
        




    def get_cur_fid(self):
        """
        This method returns the currently selected fiducial if
        the user is selecting a fiducial. If not, it returns
        a dummy.
        

        :returns:    x     - Fiducial
                     DUMMY - No Selected Fiducial
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_cur_fid()
        return ret_val




    def get_profile_parm_double(self, window, prof, parm):
        """
        Get real profile parameter
        
        :param window:  Profile window number (0 to `MAX_PROF_WND <geosoft.gxapi.MAX_PROF_WND>`-1, see `profile_open <geosoft.gxapi.GXEDB.profile_open>`)
        :param prof:    Profile number in window (see `get_profile_range_y <geosoft.gxapi.GXEDB.get_profile_range_y>`)
        :param parm:    :ref:`EDB_PROF`
        :type  window:  int
        :type  prof:    int
        :type  parm:    int

        :returns:       Real profile parameter
        :rtype:         float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_profile_parm_double(window, prof, parm)
        return ret_val




    def get_split(self):
        """
        Get split ratio between spreadsheet and profile sections.
        

        :returns:    d = (spreadsheet window height/
                     (spreadsheet window height + entire profile window height))
        :rtype:      float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        ret_val = self._get_split()
        return ret_val




    def run_channel_maker(self, chan):
        """
        Run the maker for a single channel.
        
        :param chan:  Channel name
        :type  chan:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Skips channels without makers; will not return an
        error if the channel does not exist.
        """
        self._run_channel_maker(chan.encode())
        




    def run_channel_makers(self):
        """
        Recreate channels with makers.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Skips channels without makers.
        """
        self._run_channel_makers()
        




    def set_cur_line(self, line):
        """
        Set the current line name.
        
        :param line:  Line name
        :type  line:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_cur_line(line.encode())
        




    def set_cur_line_no_message(self, str_val):
        """
        Set Line but do not send a message.
        
        :param str_val:  Line name
        :type  str_val:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_cur_line_no_message(str_val.encode())
        




    def set_cur_mark(self, start, end):
        """
        Set the current mark.
        
        :param start:  Start fiducial
        :param end:    End fiducial
        :type  start:  float
        :type  end:    float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_cur_mark(start, end)
        




    def set_profile_parm_i(self, window, prof, parm, value):
        """
        Set integer profile parameter
        
        :param window:  Profile window number (0 to `MAX_PROF_WND <geosoft.gxapi.MAX_PROF_WND>`-1, see `profile_open <geosoft.gxapi.GXEDB.profile_open>`)
        :param prof:    Profile number in window (see `get_profile_range_y <geosoft.gxapi.GXEDB.get_profile_range_y>`)
        :param parm:    :ref:`EDB_PROF`
        :param value:   Setting
        :type  window:  int
        :type  prof:    int
        :type  parm:    int
        :type  value:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_profile_parm_i(window, prof, parm, value)
        




    def set_profile_parm_r(self, window, prof, parm, value):
        """
        Set real profile parameter
        
        :param window:  Profile window number (0 to `MAX_PROF_WND <geosoft.gxapi.MAX_PROF_WND>`-1, see `profile_open <geosoft.gxapi.GXEDB.profile_open>`)
        :param prof:    Profile number in window (see `get_profile_range_y <geosoft.gxapi.GXEDB.get_profile_range_y>`)
        :param parm:    :ref:`EDB_PROF`
        :param value:   Setting
        :type  window:  int
        :type  prof:    int
        :type  parm:    int
        :type  value:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_profile_parm_r(window, prof, parm, value)
        




    def set_profile_range_x(self, min_x, max_x, x_ch):
        """
        Set profile X range and X channel
        
        :param min_x:  Minimum x, `rDUMMY <geosoft.gxapi.rDUMMY>` for data minimum
        :param max_x:  Maximum x, `rDUMMY <geosoft.gxapi.rDUMMY>` for data maximum
        :param x_ch:   X axis channel, `NULLSYMB <geosoft.gxapi.NULLSYMB>` to use fids
        :type  min_x:  float
        :type  max_x:  float
        :type  x_ch:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_profile_range_x(min_x, max_x, x_ch)
        




    def set_profile_range_y(self, min_x, max_x, min_y, max_y, scl):
        """
        Set profile Y range and display option
        
        :param min_x:  Profile window number (0 to `MAX_PROF_WND <geosoft.gxapi.MAX_PROF_WND>`-1, see `profile_open <geosoft.gxapi.GXEDB.profile_open>`)
        :param max_x:  Profile number in window (see `get_profile_range_y <geosoft.gxapi.GXEDB.get_profile_range_y>`)
        :param min_y:  Minimum y
        :param max_y:  Maximum y
        :param scl:    :ref:`EDB_PROFILE_SCALE`
        :type  min_x:  int
        :type  max_x:  int
        :type  min_y:  float
        :type  max_y:  float
        :type  scl:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If channel is not loaded or displayed, it will
        loaded and/or displayed.
        """
        self._set_profile_range_y(min_x, max_x, min_y, max_y, scl)
        




    def profile_rescale_all(self, window):
        """
        Rescale all profiles in a selected window in both X and Y, based on current scaling selections
        
        :param window:  Profile window number (0 to `MAX_PROF_WND <geosoft.gxapi.MAX_PROF_WND>`-1, see `profile_open <geosoft.gxapi.GXEDB.profile_open>`)
        :type  window:  int

        .. versionadded:: 9.6

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._profile_rescale_all(window)
        




    def set_profile_split(self, d1, d2):
        """
        Set profile split for 3 windows.
        
        :param d1:   Split d1 (profile window 0 height / entire profile window height)
        :param d2:   Split d2 (profile window 1 height / entire profile window height)
        :type  d1:   float
        :type  d2:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_profile_split(d1, d2)
        




    def set_profile_split5(self, d1, d2, d3, d4):
        """
        Set profile split for 5 windows.
        
        :param d1:   Split d1 (profile window 0 height / entire profile window height)
        :param d2:   Split d2 (profile window 1 height / entire profile window height)
        :param d3:   Split d3 (profile window 2 height / entire profile window height)
        :param d4:   Split d4 (profile window 3 height / entire profile window height)
        :type  d1:   float
        :type  d2:   float
        :type  d3:   float
        :type  d4:   float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_profile_split5(d1, d2, d3, d4)
        




    def set_profile_split_vv(self, vv):
        """
        Set profile splits
        
        :param vv:   Split `GXVV <geosoft.gxapi.GXVV>` (REAL) (relative sizes of each profile window)
        :type  vv:   GXVV

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** The input `GXVV <geosoft.gxapi.GXVV>` values are the fractional heights for each
        profile window. Values are summed, and normalized (so you can
        enter "1,1,1", with a `GXVV <geosoft.gxapi.GXVV>` of length 3, if you want 3 equal profile windows).

        `GXVV <geosoft.gxapi.GXVV>` values beyond the maximum number of displayable
        profiles (`MAX_PROF_WND <geosoft.gxapi.MAX_PROF_WND>`) are ignored.
        """
        self._set_profile_split_vv(vv)
        




    def set_split(self, d):
        """
        Set split ratio between spreadsheet and profile sections.
        
        :param d:    Split d (0.0 <= d <= 1.0).
        :type  d:    float

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** d = (spreadsheet window height/
        (spreadsheet window height + entire profile window height))
        """
        self._set_split(d)
        




    def set_window_state(self, state):
        """
        Changes the state of the database window
        
        :param state:  :ref:`EDB_WINDOW_STATE`
        :type  state:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._set_window_state(state)
        




    def show_profile(self, window, symb):
        """
        Show a profile in the profile window
        
        :param window:  Profile window number (0 to `MAX_PROF_WND <geosoft.gxapi.MAX_PROF_WND>`-1, -1 to plot to the currently selected profile window. See `profile_open <geosoft.gxapi.GXEDB.profile_open>`)
        :param symb:    Channel symbol
        :type  window:  int
        :type  symb:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the symbol is not loaded, it will be loaded.
        """
        self._show_profile(window, symb)
        




    def statistics(self, st):
        """
        Add all currently selected data to the `GXST <geosoft.gxapi.GXST>`.
        
        :param st:   `GXST <geosoft.gxapi.GXST>` handle to update
        :type  st:   GXST

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** Use `histogram <geosoft.gxapi.GXEDB.histogram>` to get median or histogram.
        """
        self._statistics(st)
        



    @classmethod
    def un_load(cls, name):
        """
        Unloads an edited database.
        
        :param name:  Name of database to unload
        :type  name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the database is not loaded, nothing happens.
        Same as `un_load_verify <geosoft.gxapi.GXEDB.un_load_verify>` with FALSE to prompt save.
        """
        gxapi_cy.WrapEDB._un_load(GXContext._get_tls_geo(), name.encode())
        



    @classmethod
    def un_load_all(cls):
        """
        Unloads all opened databases
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapEDB._un_load_all(GXContext._get_tls_geo())
        




    def un_load_all_chans(self):
        """
        Unload all channels into current database
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._un_load_all_chans()
        




    def un_load_chan(self, chan):
        """
        Unload a channel into current database
        
        :param chan:  Channel name
        :type  chan:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the channel does not exist, or if channel is already
        loaded nothing happens.
        """
        self._un_load_chan(chan.encode())
        



    @classmethod
    def un_load_discard(cls, name):
        """
        Unloads a database in the workspace, discards changes.
        
        :param name:  Name of database to unload
        :type  name:  str

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the database is not loaded, nothing happens.
        """
        gxapi_cy.WrapEDB._un_load_discard(GXContext._get_tls_geo(), name.encode())
        



    @classmethod
    def un_load_verify(cls, name, prompt):
        """
        Unloads an edited database, optional prompt to save.
        
        :param name:    Name of database to unload
        :param prompt:  :ref:`EDB_UNLOAD`
        :type  name:    str
        :type  prompt:  int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.

        **Note:** If the database is not loaded, nothing happens.
        The user can be prompted to save before unloading.
        If `EDB_UNLOAD_NO_PROMPT <geosoft.gxapi.EDB_UNLOAD_NO_PROMPT>`, data is always saved.
        EDB_UNLOAD_MULTIPROMPT is now obsolete and
        is equivalent to `EDB_UNLOAD_SINGLE_PROMPT <geosoft.gxapi.EDB_UNLOAD_SINGLE_PROMPT>`.
        """
        gxapi_cy.WrapEDB._un_load_verify(GXContext._get_tls_geo(), name.encode(), prompt)
        




    def un_lock(self):
        """
        This method unlocks the Edited Database.
        

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        self._un_lock()
        




# External Window


    @classmethod
    def load_control(cls, db_file, window):
        """
        Version of `load <geosoft.gxapi.GXEDB.load>` that can be used to load a database via subclassing into a Windows control.
        
        :param db_file:  Database filename
        :param window:   Window handle to receive document
        :type  db_file:  str
        :type  window:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapEDB._load_control(GXContext._get_tls_geo(), db_file.encode(), window)
        



    @classmethod
    def load_new_control(cls, db_file, window):
        """
        Version of `load_new <geosoft.gxapi.GXEDB.load_new>` that can be used to load a database via subclassing into a Windows control.
        
        :param db_file:  Database filename
        :param window:   Window handle to receive document
        :type  db_file:  str
        :type  window:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapEDB._load_new_control(GXContext._get_tls_geo(), db_file.encode(), window)
        



    @classmethod
    def load_pass_control(cls, db_file, user, password, window):
        """
        Version of `load_pass <geosoft.gxapi.GXEDB.load_pass>` that can be used to load a database via subclassing into a Windows control.
        
        :param db_file:   Database filename
        :param user:      Login name
        :param password:  Password
        :param window:    Window handle to receive document
        :type  db_file:   str
        :type  user:      str
        :type  password:  str
        :type  window:    int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapEDB._load_pass_control(GXContext._get_tls_geo(), db_file.encode(), user.encode(), password.encode(), window)
        



    @classmethod
    def load_with_view_control(cls, db_file, edb, window):
        """
        Version of `load_with_view <geosoft.gxapi.GXEDB.load_with_view>` that can be used to load a database via subclassing into a Windows control.
        
        :param db_file:  Database filename
        :param edb:      `GXEDB <geosoft.gxapi.GXEDB>` handle to use as the source view
        :param window:   Window handle to receive document
        :type  db_file:  str
        :type  edb:      GXEDB
        :type  window:   int

        .. versionadded:: 5.0

        **License:** `Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic>`_

        **Limitations:** May not be available while executing a command line program.
        """
        gxapi_cy.WrapEDB._load_with_view_control(GXContext._get_tls_geo(), db_file.encode(), edb, window)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer